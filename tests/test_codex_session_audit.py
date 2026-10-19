import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/codex_session_audit.py"
spec = importlib.util.spec_from_file_location("session_audit", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def row(kind, payload):
    return {"timestamp": "2026-10-01T00:00:00Z", "type": kind, "payload": payload}


def write(path, session_id, records=(), parent=None, role=None):
    meta = {"id": session_id, "cwd": "/project"}
    if parent:
        meta["source"] = {"subagent": {"thread_spawn": {
            "parent_thread_id": parent, "agent_role": role or "implementer"}}}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(item) + "\n" for item in [row("session_meta", meta), *records]))


def usage(response, count, owner="child"):
    return row("token_usage_record", {
        "thread_id": owner, "session_id": "root", "response_id": response,
        "usage": {"input_tokens": count, "cached_input_tokens": count // 2, "output_tokens": 2},
        "thread_token_usage": {"input_tokens": count},
    })


class SessionAuditTests(unittest.TestCase):
    def test_relative_rates_and_full_request_long_context_boundary(self):
        luna = {"input": 0.1, "cached_input": 0.01, "cache_write": 0.125, "output": 0.5}
        sol = {"input": 2.0, "cached_input": 0.1, "cache_write": 2.5, "output": 10.0}
        cached = {"input_tokens": 100000, "cached_input_tokens": 100000}
        fresh = {"input_tokens": 100000}
        self.assertAlmostEqual(audit.response_cost(cached, sol, 272000) /
                               audit.response_cost(cached, luna, 272000), 10)
        self.assertAlmostEqual(audit.response_cost(fresh, sol, 272000) /
                               audit.response_cost(fresh, luna, 272000), 20)
        exact = {"input_tokens": 272000, "cached_input_tokens": 270000, "output_tokens": 1000}
        over = {**exact, "input_tokens": 272001}
        self.assertAlmostEqual(audit.response_cost(exact, luna, 272000), 0.0034)
        self.assertAlmostEqual(audit.response_cost(over, luna, 272000), 0.0065502)
        # A cache write replaces that token's input charge; reasoning is already in output.
        self.assertAlmostEqual(audit.response_cost({"input_tokens": 1000000,
            "cache_write_input_tokens": 1000000, "output_tokens": 10,
            "reasoning_output_tokens": 10}, luna, 2000000), 0.125005)

    def test_cost_reconciles_snapshot_and_leaves_unknown_models_unpriced(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "sessions/root.jsonl"
            write(source, "root", [
                row("turn_context", {"model": "luna", "turn_id": "a"}),
                usage("one", 100, owner="root"), usage("one", 100, owner="root"),
                row("turn_context", {"model": "unpriced", "turn_id": "b"}),
                usage("two", 100, owner="root"),
            ])
            audit.build_index("root", [base / "sessions"], base / "index")
            rates = {"as_of": "2026-10-19", "source": "fixture", "basis": "Standard",
                     "long_context_threshold": 272000, "models": {"luna": {
                         "input": 0.1, "cached_input": 0.01, "cache_write": 0.125, "output": 0.5}}}
            result = audit.cost_index(base / "index", rates)
            self.assertEqual(result["by_model"]["luna"]["responses"], 1)
            self.assertEqual(result["unpriced_response_counts"], {"unpriced": 1})
            self.assertAlmostEqual(result["total_priced_usd"], 0.0000065)
            source.write_bytes(source.read_bytes().replace(b'"one"', b'"ONE"'))
            with self.assertRaisesRegex(ValueError, "Indexed source changed"):
                audit.cost_index(base / "index", rates)

    def test_exported_skill_runs_without_its_source_repository(self):
        export_spec = importlib.util.spec_from_file_location("export_plugin", SCRIPT.with_name("export_plugin.py"))
        exporter = importlib.util.module_from_spec(export_spec)
        export_spec.loader.exec_module(exporter)
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            repository = base / "source"
            (repository / ".codex-plugin").mkdir(parents=True)
            (repository / ".codex-plugin/plugin.json").write_text(json.dumps({
                "name": "my-skills", "version": "0.1.0", "skills": "./skills/"}))
            shutil.copytree(SCRIPT.parent.parent / "skills/session-audit", repository / "skills/session-audit")
            (repository / "scripts").mkdir()
            shutil.copy2(SCRIPT, repository / "scripts" / SCRIPT.name)
            for command in (["init"], ["add", "."], ["-c", "user.name=Test", "-c",
                           "user.email=test@example.com", "commit", "-m", "fixture"]):
                subprocess.run(["git", "-C", str(repository), *command], check=True, capture_output=True)
            destination = exporter.build(repository, base / "export")
            shutil.rmtree(repository)
            write(base / "sessions/root.jsonl", "root", [usage("one", 40, owner="root")])
            result = subprocess.run([sys.executable, "-B", str(destination / "scripts" / SCRIPT.name),
                                     "index", "root", "--sessions-root", str(base / "sessions"),
                                     "--output", str(base / "index")],
                                    cwd=base, check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["sessions"], 1)
            summary = json.loads((base / "index/summary.json").read_text())
            self.assertEqual(summary["sessions"][0]["tokens"]["input_tokens"], 40)

    def test_nested_parent_and_response_accounting_across_models(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            write(base / "sessions/root.jsonl", "root")
            write(base / "sessions/child.jsonl", "child", [
                row("turn_context", {"model": "model-a", "turn_id": "a"}),
                usage("one", 100), usage("one", 100),
                row("event_msg", {"type": "token_count", "info": {
                    "total_token_usage": {"input_tokens": 100}}}),
                row("turn_context", {"model": "model-b", "turn_id": "b"}),
                usage("two", 200), usage("foreign", 999, owner="root"),
            ], parent="root")
            result = audit.build_index("root", [base / "sessions"], base / "index")
            child = next(s for s in result["sessions"] if s["id"] == "child")
        self.assertEqual(result["session_count"], 2)
        self.assertEqual(child["tokens"]["input_tokens"], 300)
        self.assertEqual(child["tokens_by_model"]["model-a"]["input_tokens"], 100)
        self.assertEqual(child["tokens_by_model"]["model-b"]["input_tokens"], 200)
        self.assertEqual(child["anomalies"]["duplicate_usage_records"], 1)
        self.assertEqual(child["anomalies"]["foreign_usage_records"], 1)

    def test_legacy_counters_are_explicit_lower_bounds(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            write(base / "sessions/root.jsonl", "root", [row("event_msg", {
                "type": "token_count", "info": {"total_token_usage": {"input_tokens": 80}}})])
            result = audit.build_index("root", [base / "sessions"], base / "index")
        self.assertEqual(result["sessions"][0]["token_basis"], "cumulative_peak_lower_bound")
        self.assertEqual(result["sessions"][0]["tokens"]["input_tokens"], 80)
        self.assertEqual(result["sessions"][0]["tokens_by_model"], {})

    def test_signals_query_and_hash_checked_bounded_source(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "sessions/root.jsonl"
            write(source, "root", [
                row("response_item", {"type": "custom_tool_call", "name": "exec", "call_id": "c",
                                      "input": "await tools.exec_command({cmd: 'scripts/check-stage3.sh'})"}),
                row("response_item", {"type": "custom_tool_call_output", "call_id": "c", "output": [
                    {"type": "input_text", "text": "Process exited with code 7\nWarning: truncated output"}]}),
            ])
            result = audit.build_index("root", [base / "sessions"], base / "index")
            events = list(audit.select_events(base / "index", ["nonzero_exit"]))
            self.assertEqual(events[0]["call_ref"], "root:L2")
            self.assertEqual(len(list(audit.select_events(base / "index", query="check-stage3.sh"))), 1)
            with source.open("a") as stream:
                stream.write(json.dumps(row("compacted", {})) + "\n")
            shown = audit.show_event(base / "index", "root:L3", max_chars=60)
            self.assertIn("hash verified", shown)
            self.assertIn("excerpt clipped", shown)
            source.write_bytes(source.read_bytes().replace(b"code 7", b"code 9"))
            with self.assertRaisesRegex(ValueError, "evidence changed"):
                audit.show_event(base / "index", "root:L3")
        self.assertEqual(result["sessions"][0]["signals"], {"truncation": 1, "nonzero_exit": 1})

    def test_ambiguous_duplicates_and_existing_output_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            write(base / "a/root.jsonl", "root")
            write(base / "b/root.jsonl", "root")
            with self.assertRaisesRegex(ValueError, "Ambiguous duplicate"):
                audit.build_index("root", [base / "a", base / "b"], base / "output")
            self.assertFalse((base / "output").exists())
            (base / "output").mkdir()
            with self.assertRaises(FileExistsError):
                audit.build_index("root", [base / "a"], base / "output")

    def test_injected_messages_and_malformed_tail_are_not_silently_hidden(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "sessions/root.jsonl"
            write(source, "root", [
                row("response_item", {"type": "message", "role": "user", "content": [
                    {"text": "<codex_internal_context>Continue"}]}),
                row("response_item", {"type": "message", "role": "user", "content": [{"text": "continue"}]}),
            ])
            with source.open("a") as stream:
                stream.write('{"unfinished":')
            result = audit.build_index("root", [base / "sessions"], base / "index")
            events = list(audit.select_events(base / "index", ["user_message"]))
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["excerpt"], "continue")
        self.assertEqual(result["sessions"][0]["anomalies"]["malformed_rows"], 1)

    def test_encrypted_transport_is_explicit_and_not_a_missing_message(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            cipher = "gAAAA" + "a" * 100
            write(base / "sessions/root.jsonl", "root", [
                row("response_item", {"type": "agent_message", "content": [
                    {"type": "input_text", "text": "Payload:"},
                    {"type": "encrypted_content", "encrypted_content": cipher}]}),
                row("response_item", {"type": "function_call", "name": "send_message",
                                      "arguments": json.dumps({"target": "child", "message": cipher})}),
            ])
            result = audit.build_index("root", [base / "sessions"], base / "index")
            events = (base / "index/events.jsonl").read_text()
        self.assertNotIn(cipher, events)
        self.assertIn("opaque encrypted content", events)
        self.assertEqual(result["sessions"][0]["counts"]["opaque_agent_messages"], 1)
        self.assertEqual(result["sessions"][0]["counts"]["opaque_coordination_calls"], 1)


if __name__ == "__main__":
    unittest.main()

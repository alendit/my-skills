import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from codex_rollout_audit import summarize_rollout
from codex_session_compare import aggregate_tree, discover_sessions


def write_rollout(path, session_id, parent_id=None, usage_records=(), error=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "id": session_id,
        "cwd": "/tmp/project",
        "source": "cli",
    }
    if parent_id:
        metadata["parent_thread_id"] = parent_id
    rows = [
        {
            "timestamp": "2026-09-01T00:00:00Z",
            "type": "session_meta",
            "payload": metadata,
        },
        {
            "timestamp": "2026-09-01T00:00:01Z",
            "type": "event_msg",
            "payload": {"type": "task_started"},
        },
        {
            "timestamp": "2026-09-01T00:00:02Z",
            "type": "response_item",
            "payload": {
                "type": "custom_tool_call",
                "name": "exec",
                "input": "await tools.exec_command({cmd: 'rg x'}); "
                "await tools.apply_patch('patch')",
            },
        },
    ]
    for usage in usage_records:
        rows.append(
            {
                "timestamp": "2026-09-01T00:00:03Z",
                "type": "token_usage_record",
                "payload": {"thread_token_usage": usage},
            }
        )
    rows.extend(
        [
            {
                "timestamp": "2026-09-01T00:00:04Z",
                "type": "compacted",
                "payload": {},
            },
            {
                "timestamp": "2026-09-01T00:00:05Z",
                "type": "event_msg",
                "payload": {"type": "task_complete", "error": error},
            },
        ]
    )
    path.write_text("".join(json.dumps(row) + "\n" for row in rows))


class RolloutAuditTests(unittest.TestCase):
    def test_uses_per_field_peak_and_counts_nested_tools(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "root.jsonl"
            write_rollout(
                path,
                "root",
                usage_records=(
                    {
                        "input_tokens": 100,
                        "cached_input_tokens": 70,
                        "output_tokens": 8,
                    },
                    {
                        "input_tokens": 90,
                        "cached_input_tokens": 80,
                        "output_tokens": 10,
                    },
                ),
            )
            summary = summarize_rollout(path)

        self.assertEqual(summary["tokens"]["input_tokens"], 100)
        self.assertEqual(summary["tokens"]["cached_input_tokens"], 80)
        self.assertEqual(summary["tokens"]["uncached_input_tokens"], 20)
        self.assertEqual(summary["nested_tools"], {"exec_command": 1, "apply_patch": 1})
        self.assertEqual(summary["compactions"], 1)

    def test_supports_legacy_token_count_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "legacy.jsonl"
            write_rollout(path, "legacy")
            with path.open("a", encoding="utf-8") as stream:
                stream.write(
                    json.dumps(
                        {
                            "timestamp": "2026-09-01T00:00:06Z",
                            "type": "event_msg",
                            "payload": {
                                "type": "token_count",
                                "info": {
                                    "total_token_usage": {
                                        "input_tokens": 55,
                                        "cached_input_tokens": 34,
                                        "output_tokens": 5,
                                    }
                                },
                            },
                        }
                    )
                    + "\n"
                )
            summary = summarize_rollout(path)

        self.assertEqual(summary["tokens"]["input_tokens"], 55)
        self.assertEqual(summary["tokens"]["uncached_input_tokens"], 21)

    def test_discovers_and_aggregates_descendant_sessions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_rollout(
                root / "2026" / "root.jsonl",
                "root",
                usage_records=({"input_tokens": 100, "cached_input_tokens": 80},),
            )
            write_rollout(
                root / "2026" / "child.jsonl",
                "child",
                parent_id="root",
                usage_records=({"input_tokens": 50, "cached_input_tokens": 30},),
                error={"message": "quota reached", "codex_error_info": "quota"},
            )
            sessions, children = discover_sessions(root)
            tree = aggregate_tree("root", sessions, children)

        self.assertEqual(tree["session_count"], 2)
        self.assertEqual(tree["tokens"]["input_tokens"], 150)
        self.assertEqual(tree["tokens"]["uncached_input_tokens"], 40)
        self.assertEqual(tree["events"]["task_complete"], 2)
        self.assertEqual(tree["task_errors"][0]["session_id"], "child")
        self.assertEqual(tree["task_errors"][0]["code"], "quota")


if __name__ == "__main__":
    unittest.main()

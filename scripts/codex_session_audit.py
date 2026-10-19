#!/usr/bin/env python3
"""Index a local Codex session tree, then inspect bounded evidence on demand.

Uses only the Python standard library. Signals are leads for review, not verdicts.
"""

import argparse
import hashlib
import json
import re
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ANALYZER_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
TOKEN_FIELDS = ("input_tokens", "cached_input_tokens", "output_tokens",
                "reasoning_output_tokens", "total_tokens")
NESTED_TOOL = re.compile(r"\btools\.([A-Za-z_][A-Za-z0-9_]*)\s*\(")
PATH_ANCHOR = re.compile(r"[\w./-]+\.(?:sh|py|md|toml|json|rs|clj|wasm)\b")
SIGNALS = {
    "truncation": re.compile(r"Warning: truncated output|Output truncated|tokens truncated", re.I),
    "patch_failure": re.compile(r"Failed to find expected lines|patch verification failed", re.I),
    "tool_error": re.compile(r"SyntaxError:|Traceback \(most recent call last\)|isError[\\\"'\s:]+true"),
    "nonzero_exit": re.compile(r"(?:Process exited with code|exit_code[\\\"'\s:]+)\s*[1-9]\d*"),
}
INJECTED = ("# AGENTS.md", "<environment_context>", "<codex_internal_context", "<skill>")


def content_text(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(content_text(item) for item in value)
    if isinstance(value, dict):
        if "encrypted_content" in value:
            return "[opaque encrypted content]"
        return content_text(value.get("text", value.get("output", value.get("content", ""))))
    return ""


def has_opaque_content(value):
    if isinstance(value, str):
        return value.startswith("gAAAA") and len(value) > 40
    if isinstance(value, list):
        return any(has_opaque_content(item) for item in value)
    if isinstance(value, dict):
        return "encrypted_content" in value or any(has_opaque_content(item) for item in value.values())
    return False


def visible_arguments(value):
    if isinstance(value, str) and has_opaque_content(value):
        return "[opaque encrypted content]"
    if isinstance(value, dict):
        return {key: visible_arguments(item) for key, item in value.items()}
    if isinstance(value, list):
        return [visible_arguments(item) for item in value]
    return value


def arguments(value):
    if isinstance(value, dict):
        return value
    try:
        parsed = json.loads(value)
        return parsed if isinstance(parsed, dict) else {}
    except (ValueError, TypeError):
        return {}


def identity(path):
    with path.open("rb") as stream:
        for _ in range(64):
            raw = stream.readline()
            if not raw:
                break
            try:
                row = json.loads(raw)
            except (ValueError, UnicodeDecodeError):
                continue
            if row.get("type") == "session_meta":
                meta = row.get("payload") or {}
                source = meta.get("source")
                sub = source.get("subagent", {}) if isinstance(source, dict) else {}
                spawn = sub.get("thread_spawn", {})
                return {
                    "id": meta.get("id") or meta.get("session_id"),
                    "parent_id": meta.get("parent_thread_id") or meta.get("parent_id")
                    or spawn.get("parent_thread_id"),
                    "role": meta.get("agent_role") or spawn.get("agent_role")
                    or sub.get("other") or "root",
                    "agent_path": meta.get("agent_path") or spawn.get("agent_path"),
                    "cwd": meta.get("cwd"), "path": str(path.resolve()),
                    "cli_version": meta.get("cli_version"),
                }
    return None


def discover(roots, root_id):
    sessions, duplicates, unreadable = {}, [], []
    for root in roots:
        for path in sorted(root.rglob("*.jsonl")):
            try:
                meta = identity(path)
            except OSError as error:
                unreadable.append({"path": str(path), "error": str(error)})
                continue
            if meta and meta["id"]:
                previous = sessions.get(meta["id"])
                if previous and previous["path"] != meta["path"]:
                    duplicates.append({"id": meta["id"], "paths": [previous["path"], meta["path"]]})
                else:
                    sessions[meta["id"]] = meta
    if root_id not in sessions:
        raise ValueError(f"Session not found in supplied roots: {root_id}")
    children = defaultdict(list)
    for meta in sessions.values():
        children[meta["parent_id"]].append(meta["id"])
    selected, pending = {}, [root_id]
    while pending:
        key = pending.pop()
        if key not in selected:
            selected[key] = sessions[key]
            pending.extend(children[key])
    conflicts = [item for item in duplicates if item["id"] in selected]
    if conflicts:
        raise ValueError(f"Ambiguous duplicate rollout identities: {conflicts}")
    return selected, unreadable


def excerpt(text, limit=280):
    return " ".join(text.split())[:limit]


def add_tokens(counter, usage):
    for field in TOKEN_FIELDS:
        value = usage.get(field, 0)
        if isinstance(value, int) and value >= 0:
            counter[field] += value


def scan(meta, event_stream):
    path = Path(meta["path"])
    initial = path.stat()
    digest = hashlib.sha256()
    counts, tools, nested, signals = Counter(), Counter(), Counter(), Counter()
    models, tokens, peak, by_model = Counter(), Counter(), Counter(), defaultdict(Counter)
    repeated, first_call, waits = Counter(), {}, Counter()
    contexts, seen_usage, pending_calls = {}, set(), {}
    checkpoints, anomalies, daily = [], Counter(), defaultdict(Counter)
    last_assistant = None
    model, first_ts, last_ts, offset, line_no = "unknown", None, None, 0, 0

    with path.open("rb") as stream:
        while offset < initial.st_size:
            start = offset
            raw = stream.readline(initial.st_size - offset)
            if not raw:
                break
            offset += len(raw)
            line_no += 1
            digest.update(raw)
            if (line_no - 1) % 256 == 0:
                checkpoints.append([line_no, start])
            try:
                row = json.loads(raw)
            except (ValueError, UnicodeDecodeError):
                anomalies["malformed_rows"] += 1
                continue
            payload = row.get("payload") or {}
            kind = row.get("type", "unknown")
            counts[kind] += 1
            ts = row.get("timestamp")
            if ts:
                first_ts = min(first_ts, ts) if first_ts else ts
                last_ts = max(last_ts, ts) if last_ts else ts
            day = (ts or "unknown")[:10]
            ref = f"{meta['id']}:L{line_no}"

            def emit(category, text="", **extra):
                event_stream.write(json.dumps({
                    "ref": ref, "session_id": meta["id"], "line": line_no,
                    "timestamp": ts, "kind": category, "excerpt": excerpt(text),
                    "offset": start, "bytes": len(raw),
                    "record_sha256": hashlib.sha256(raw).hexdigest(), **extra,
                }, ensure_ascii=False) + "\n")
                daily[day][category] += 1

            if kind == "turn_context":
                model = payload.get("model") or "unknown"
                contexts[payload.get("turn_id")] = model
                models[model] += 1
            elif kind == "compacted":
                emit("compaction")
            elif kind == "token_usage_record":
                # session_id can be the ROOT session even in a child's own usage.
                owner = payload.get("thread_id")
                if owner and owner != meta["id"]:
                    anomalies["foreign_usage_records"] += 1
                    continue
                usage = payload.get("usage")
                response_id = payload.get("response_id")
                if isinstance(usage, dict) and response_id:
                    if response_id in seen_usage:
                        anomalies["duplicate_usage_records"] += 1
                        continue
                    seen_usage.add(response_id)
                    add_tokens(tokens, usage)
                    attribution = payload.get("model") or contexts.get(payload.get("turn_id"), model)
                    add_tokens(by_model[attribution], usage)
                else:
                    anomalies["usage_without_response_identity"] += 1
                for field, value in (payload.get("thread_token_usage") or {}).items():
                    if field in TOKEN_FIELDS and isinstance(value, int):
                        peak[field] = max(peak[field], value)
            elif kind == "event_msg":
                event_kind = payload.get("type")
                if event_kind == "token_count":
                    usage = ((payload.get("info") or {}).get("total_token_usage") or {})
                    for field in TOKEN_FIELDS:
                        if isinstance(usage.get(field), int):
                            peak[field] = max(peak[field], usage[field])
                elif event_kind in {"task_complete", "task_started"}:
                    counts[event_kind] += 1
                    if event_kind == "task_complete" and payload.get("error"):
                        emit("task_error", str(payload["error"]))
            elif kind == "response_item":
                item_kind = payload.get("type")
                if item_kind == "message":
                    role = payload.get("role", "unknown")
                    text = content_text(payload.get("content"))
                    counts[f"{role}_messages"] += 1
                    counts[f"{role}_characters"] += len(text)
                    if has_opaque_content(payload.get("content")):
                        counts[f"opaque_{role}_messages"] += 1
                    if role == "user":
                        emit("injected_context" if text.lstrip().startswith(INJECTED) else "user_message", text)
                    elif role == "assistant":
                        emit("assistant_message", text)
                        last_assistant = {"ref": ref, "text": excerpt(text, 2200)}
                    elif role == "developer":
                        emit("instruction", text)
                elif item_kind == "agent_message":
                    if has_opaque_content(payload.get("content")):
                        counts["opaque_agent_messages"] += 1
                    emit("agent_message", content_text(payload.get("content")),
                         author=payload.get("author"), recipient=payload.get("recipient"))
                elif item_kind in {"function_call", "custom_tool_call"}:
                    name = payload.get("name", "unknown")
                    short_name = name.rsplit(".", 1)[-1]
                    tools[short_name] += 1
                    value = payload.get("arguments", payload.get("input", ""))
                    args = arguments(value)
                    text = value if isinstance(value, str) else json.dumps(value, sort_keys=True)
                    normalized = json.dumps(args, sort_keys=True) if args else " ".join(text.split())
                    signature = (short_name, hashlib.sha256(normalized.encode()).hexdigest())
                    repeated[signature] += 1
                    first_call.setdefault(signature, ref)
                    pending_calls[payload.get("call_id")] = ref
                    if short_name == "exec":
                        code = args.get("code", text)
                        nested.update(NESTED_TOOL.findall(code))
                        emit("tool_call", code, tool=short_name,
                             anchors=sorted(set(PATH_ANCHOR.findall(code)))[:80])
                        if "SKILL.md" in code:
                            emit("skill_reference", code)
                    if short_name in {"wait_agent", "wait", "sleep"}:
                        duration = args.get("timeout_ms", args.get("yield_time_ms", args.get("duration_ms", "default")))
                        waits[f"{short_name}:{duration}"] += 1
                    if short_name != "exec":
                        if has_opaque_content(args):
                            counts["opaque_coordination_calls"] += 1
                        emit("coordination_call", json.dumps(visible_arguments(args)) if args else text,
                             tool=short_name)
                elif item_kind in {"function_call_output", "custom_tool_call_output"}:
                    text = content_text(payload.get("output"))
                    call_ref = pending_calls.pop(payload.get("call_id"), None)
                    for label, pattern in SIGNALS.items():
                        match = pattern.search(text)
                        if match:
                            signals[label] += 1
                            emit(label, text[max(0, match.start() - 80):match.end() + 200], call_ref=call_ref)

    basis = "deduplicated_response_usage" if seen_usage else "cumulative_peak_lower_bound"
    if not seen_usage:
        tokens = peak
    elif any(peak[field] > tokens[field] for field in TOKEN_FIELDS):
        anomalies["cumulative_exceeds_response_sum"] += 1
    tokens["uncached_input_tokens"] = max(0, tokens["input_tokens"] - tokens["cached_input_tokens"])
    final = path.stat()
    return {
        **meta, "snapshot_bytes": offset, "snapshot_sha256": digest.hexdigest(),
        "mtime_ns": initial.st_mtime_ns, "changed_during_scan":
        (initial.st_size, initial.st_mtime_ns) != (final.st_size, final.st_mtime_ns),
        "lines": line_no, "start": first_ts, "end": last_ts,
        "counts": dict(counts), "tools": dict(tools),
        "nested_tool_text_mentions": dict(nested), "signals": dict(signals),
        "models": dict(models), "tokens": dict(tokens), "token_basis": basis,
        "usage_responses": len(seen_usage), "tokens_by_model": dict(by_model),
        "anomalies": dict(anomalies), "wait_requests": dict(waits),
        "daily_event_counts": dict(daily), "last_assistant_message": last_assistant,
        "repeated_calls": [{"tool": key[0], "count": count, "first_ref": first_call[key]}
                           for key, count in repeated.most_common(12) if count > 1],
        "line_checkpoints": checkpoints,
    }


def build_index(root_id, roots, destination):
    started = time.monotonic()
    selected, unreadable = discover(roots, root_id)
    destination.mkdir(parents=True, exist_ok=False)
    sessions = []
    with (destination / "events.jsonl").open("w", encoding="utf-8") as stream:
        for key in sorted(selected):
            sessions.append(scan(selected[key], stream))
    totals = {key: Counter() for key in ("tokens", "tools", "signals", "counts")}
    for session in sessions:
        for key, value in totals.items():
            value.update(session[key])
    result = {
        "schema_version": 1, "root_id": root_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "analyzer_sha256": ANALYZER_SHA256,
        "analyzer_changed_during_scan": ANALYZER_SHA256 != hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "roots": [str(root.resolve()) for root in roots],
        "coverage": "Locally discovered metadata descendants; absence is not proof of a complete tree.",
        "unreadable_discovery_files": unreadable,
        "session_count": len(sessions), "roles": dict(Counter(s["role"] for s in sessions)),
        "totals_including_automated_agents": {key: dict(value) for key, value in totals.items()},
        "sessions": sessions,
    }
    (destination / "summary.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def select_events(directory, kinds=(), session=None, query=None):
    with (directory / "events.jsonl").open(encoding="utf-8") as stream:
        for line in stream:
            event = json.loads(line)
            if kinds and event["kind"] not in kinds:
                continue
            if session and event["session_id"] != session:
                continue
            searchable = event["excerpt"] + " " + " ".join(event.get("anchors", []))
            if query and query.casefold() not in searchable.casefold():
                continue
            yield event


def overview(directory):
    summary = json.loads((directory / "summary.json").read_text())
    groups = {}
    for session in summary["sessions"]:
        group = groups.setdefault(session["role"], {
            "sessions": 0, "snapshot_bytes": 0, "tokens": Counter(),
            "tools": Counter(), "signals": Counter(), "models": defaultdict(Counter),
        })
        group["sessions"] += 1
        group["snapshot_bytes"] += session["snapshot_bytes"]
        for key in ("tokens", "tools", "signals"):
            group[key].update(session[key])
        for model, usage in session["tokens_by_model"].items():
            group["models"][model].update(usage)
    root = next(item for item in summary["sessions"] if item["id"] == summary["root_id"])
    return {
        "root_id": summary["root_id"], "created_at": summary["created_at"],
        "elapsed_seconds": summary["elapsed_seconds"],
        "coverage": summary["coverage"], "roles": summary["roles"],
        "groups": groups,
        "root": {key: root[key] for key in (
            "start", "end", "lines", "counts", "tools", "signals", "wait_requests",
            "tokens", "token_basis", "repeated_calls", "last_assistant_message")},
        "limitations": {
            "unreadable_discovery_files": len(summary["unreadable_discovery_files"]),
            "changed_during_scan": [s["id"] for s in summary["sessions"] if s["changed_during_scan"]],
            "session_anomalies": {s["id"]: s["anomalies"] for s in summary["sessions"] if s["anomalies"]},
            "cost": "Not calculated; requires dated model and service-tier rates. Tokens are not prices.",
            "opaque_content": "Encrypted messages are counted and marked, not reconstructed or assessed for meaning.",
            "analyzer_changed_during_scan": summary["analyzer_changed_during_scan"],
            "signals": "Pattern matches in tool output are review leads, not confirmed failures.",
            "time": "Timestamps measure calendar span, not active work or critical-path duration.",
        },
    }


def response_cost(usage, rate, threshold):
    """Price an entire request; cache writes replace, rather than add to, input."""
    cached = usage.get("cached_input_tokens", 0)
    writes = usage.get("cache_write_input_tokens", 0)
    fresh = usage.get("input_tokens", 0) - cached - writes
    if fresh < 0:
        raise ValueError("Cached and cache-write tokens exceed total input")
    long_context = usage.get("input_tokens", 0) > threshold
    input_multiplier = 2 if long_context else 1
    output_multiplier = 1.5 if long_context else 1
    return ((fresh * rate["input"] + cached * rate["cached_input"]
             + writes * rate["cache_write"]) * input_multiplier
            + usage.get("output_tokens", 0) * rate["output"] * output_multiplier) / 1_000_000


def cost_index(directory, rates):
    """Re-read the indexed byte prefixes to apply per-request context pricing."""
    summary = json.loads((directory / "summary.json").read_text())
    for required in ("as_of", "source", "basis", "models", "long_context_threshold"):
        if required not in rates:
            raise ValueError(f"Missing rate provenance or configuration: {required}")
    by_model, by_role, sessions, unpriced = {}, Counter(), [], Counter()
    for session in summary["sessions"]:
        digest, seen, contexts = hashlib.sha256(), set(), {}
        active_model, offset, session_cost, priced_responses = "unknown", 0, 0.0, 0
        observed = Counter()
        with Path(session["path"]).open("rb") as stream:
            while offset < session["snapshot_bytes"]:
                raw = stream.readline(session["snapshot_bytes"] - offset)
                if not raw:
                    raise ValueError(f"Indexed source was shortened: {session['id']}")
                offset += len(raw)
                digest.update(raw)
                try:
                    row = json.loads(raw)
                except (ValueError, UnicodeDecodeError):
                    continue
                payload = row.get("payload") or {}
                if row.get("type") == "turn_context":
                    active_model = payload.get("model") or "unknown"
                    contexts[payload.get("turn_id")] = active_model
                elif row.get("type") == "token_usage_record":
                    if payload.get("thread_id") not in (None, session["id"]):
                        continue
                    response = payload.get("response_id")
                    usage = payload.get("usage")
                    if not response or response in seen or not isinstance(usage, dict):
                        continue
                    seen.add(response)
                    add_tokens(observed, usage)
                    model = payload.get("model") or contexts.get(payload.get("turn_id"), active_model)
                    rate = rates["models"].get(model)
                    if rate is None:
                        unpriced[model] += 1
                        continue
                    priced_responses += 1
                    item = by_model.setdefault(model, {
                        "usd": 0.0, "responses": 0, "long_context_responses": 0,
                        "tokens": Counter(), "same_usage_at_other_model_rates": Counter(),
                    })
                    amount = response_cost(usage, rate, rates["long_context_threshold"])
                    item["usd"] += amount
                    item["responses"] += 1
                    item["long_context_responses"] += usage.get("input_tokens", 0) > rates["long_context_threshold"]
                    add_tokens(item["tokens"], usage)
                    for other_model, other_rate in rates["models"].items():
                        item["same_usage_at_other_model_rates"][other_model] += response_cost(
                            usage, other_rate, rates["long_context_threshold"])
                    session_cost += amount
        if digest.hexdigest() != session["snapshot_sha256"]:
            raise ValueError(f"Indexed source changed: {session['id']}")
        if not seen:
            unpriced["sessions_without_response_usage"] += 1
        elif any(observed[field] != session["tokens"].get(field, 0) for field in TOKEN_FIELDS):
            raise ValueError(f"Response usage does not reconcile with indexed tokens: {session['id']}")
        if priced_responses:
            by_role[session["role"]] += session_cost
        sessions.append({"id": session["id"], "role": session["role"],
                         "usd": session_cost if priced_responses else None,
                         "priced_responses": priced_responses,
                         "unpriced_responses": len(seen) - priced_responses})
    return {
        "root_id": summary["root_id"], "rates": rates,
        "estimate_basis": "Current-rate API-equivalent scenario, not historical billing or subscription usage.",
        "pricing_analyzer_sha256": ANALYZER_SHA256,
        "total_priced_usd": sum(by_role.values()), "by_model": by_model,
        "by_role": by_role, "sessions": sessions, "unpriced_response_counts": unpriced,
        "limitations": "Standard tier assumed; service tiers were not established. Same-usage repricing does not predict another model's behavior.",
    }


def show_event(directory, ref, context=0, max_chars=14000):
    summary = json.loads((directory / "summary.json").read_text())
    event = next((item for item in select_events(directory) if item["ref"] == ref), None)
    if event is None:
        raise ValueError(f"Unknown event: {ref}")
    session = next(item for item in summary["sessions"] if item["id"] == event["session_id"])
    path = Path(session["path"])
    start_line, end_line = max(1, event["line"] - context), min(session["lines"], event["line"] + context)
    checkpoint_line, offset = max(pair for pair in session["line_checkpoints"] if pair[0] <= start_line)
    records = []
    with path.open("rb") as stream:
        stream.seek(event["offset"])
        raw = stream.read(event["bytes"])
        if hashlib.sha256(raw).hexdigest() != event["record_sha256"]:
            raise ValueError("Indexed evidence changed; build a new index before citing it")
        stream.seek(offset)
        for number in range(checkpoint_line, end_line + 1):
            raw = stream.readline()
            if number < start_line:
                continue
            try:
                row = json.loads(raw)
            except (ValueError, UnicodeDecodeError):
                continue
            payload = row.get("payload") or {}
            text = content_text(payload.get("content", payload.get("output", "")))
            if not text:
                raw_input = payload.get("arguments", payload.get("input", ""))
                parsed = arguments(raw_input)
                text = json.dumps(visible_arguments(parsed)) if parsed else str(raw_input)
            if not text and row.get("type") != "world_state":
                text = json.dumps(payload, ensure_ascii=False)
            records.append(f"L{number} [{row.get('type')}/{payload.get('type', '')}] {text}")
    output = "\n".join(records)
    return f"{path}:{start_line} (indexed record hash verified)\n" + output[:max_chars] + (
        "\n[excerpt clipped; narrow the request]" if len(output) > max_chars else "")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    index = commands.add_parser("index", help="stream local root and descendant rollouts once")
    index.add_argument("root_id")
    index.add_argument("--sessions-root", action="append", type=Path)
    index.add_argument("--output", type=Path, required=True)
    overview_command = commands.add_parser("overview", help="print bounded metrics grouped by agent role")
    overview_command.add_argument("directory", type=Path)
    cost = commands.add_parser("cost", help="apply sourced model rates to the indexed response usage")
    cost.add_argument("directory", type=Path)
    cost.add_argument("--rates", type=Path, required=True)
    events = commands.add_parser("events", help="query compact evidence without rereading rollouts")
    events.add_argument("directory", type=Path)
    events.add_argument("--kind", action="append", default=[])
    events.add_argument("--session")
    events.add_argument("--query")
    events.add_argument("--limit", type=int, default=12)
    events.add_argument("--skip", type=int, default=0)
    show = commands.add_parser("show", help="read a bounded, hash-checked source excerpt")
    show.add_argument("directory", type=Path)
    show.add_argument("ref")
    show.add_argument("--context", type=int, default=0)
    show.add_argument("--max-chars", type=int, default=14000)
    args = parser.parse_args()
    try:
        if args.command == "index":
            roots = args.sessions_root or [Path.home() / ".codex/sessions", Path.home() / ".codex/archived_sessions"]
            result = build_index(args.root_id, roots, args.output)
            print(json.dumps({"output": str(args.output), "sessions": result["session_count"], "roles": result["roles"]}))
        elif args.command == "overview":
            print(json.dumps(overview(args.directory), indent=2))
        elif args.command == "cost":
            print(json.dumps(cost_index(args.directory, json.loads(args.rates.read_text())), indent=2))
        elif args.command == "events":
            if not 1 <= args.limit <= 100 or args.skip < 0:
                raise ValueError("Use limit 1..100 and a nonnegative skip")
            for number, event in enumerate(select_events(args.directory, args.kind, args.session, args.query)):
                if number < args.skip:
                    continue
                if number >= args.skip + args.limit:
                    break
                print(json.dumps({key: event[key] for key in ("ref", "timestamp", "kind", "excerpt")}, ensure_ascii=False))
        else:
            if not 0 <= args.context <= 12 or not 1 <= args.max_chars <= 50000:
                raise ValueError("Use context 0..12 and max-chars 1..50000")
            print(show_event(args.directory, args.ref, args.context, args.max_chars))
    except (OSError, ValueError, StopIteration) as error:
        parser.exit(1, f"Audit error: {error}\n")


if __name__ == "__main__":
    main()

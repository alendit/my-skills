#!/usr/bin/env python3
"""Compare complete Codex session trees, including descendant subagents."""

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from codex_rollout_audit import summarize_rollout


def read_session_identity(path):
    path = Path(path)
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("type") != "session_meta":
                continue
            payload = row.get("payload") or {}
            return {
                "id": payload.get("id") or payload.get("session_id"),
                "parent_id": payload.get("parent_thread_id")
                or payload.get("parent_id"),
                "path": path,
            }
    return None


def discover_sessions(sessions_root):
    sessions = {}
    children = defaultdict(list)
    for path in Path(sessions_root).rglob("*.jsonl"):
        identity = read_session_identity(path)
        if not identity or not identity["id"]:
            continue
        sessions[identity["id"]] = identity
        if identity["parent_id"]:
            children[identity["parent_id"]].append(identity["id"])
    return sessions, children


def descendant_ids(root_id, children):
    found = []
    pending = [root_id]
    seen = set()
    while pending:
        session_id = pending.pop()
        if session_id in seen:
            continue
        seen.add(session_id)
        found.append(session_id)
        pending.extend(children.get(session_id, ()))
    return found


def aggregate_tree(root_id, sessions, children):
    ids = descendant_ids(root_id, children)
    missing = [session_id for session_id in ids if session_id not in sessions]
    if missing:
        raise ValueError(f"missing rollout files for: {', '.join(missing)}")

    summaries = [summarize_rollout(sessions[session_id]["path"]) for session_id in ids]
    tokens = Counter()
    outer_tools = Counter()
    nested_tools = Counter()
    events = Counter()
    models = Counter()
    efforts = Counter()
    for summary in summaries:
        tokens.update(summary["tokens"])
        outer_tools.update(summary["outer_tools"])
        nested_tools.update(summary["nested_tools"])
        events.update(summary["events"])
        models.update(summary["models"])
        efforts.update(summary["reasoning_efforts"])

    starts = [summary["start"] for summary in summaries if summary["start"]]
    ends = [summary["end"] for summary in summaries if summary["end"]]
    start = min(starts) if starts else None
    end = max(ends) if ends else None
    duration_seconds = 0
    if start and end:
        duration_seconds = (
            datetime.fromisoformat(end) - datetime.fromisoformat(start)
        ).total_seconds()
    task_errors = []
    for summary in summaries:
        task_errors.extend(
            {"session_id": summary["metadata"].get("id"), **error}
            for error in summary["task_errors"]
        )

    return {
        "root_id": root_id,
        "session_count": len(summaries),
        "start": start,
        "end": end,
        "duration_seconds": duration_seconds,
        "tokens": dict(tokens),
        "models": dict(models),
        "reasoning_efforts": dict(efforts),
        "events": dict(events),
        "outer_tools": dict(outer_tools),
        "nested_tools": dict(nested_tools),
        "compactions": sum(summary["compactions"] for summary in summaries),
        "task_errors": task_errors,
        "sessions": summaries,
    }


def compact_summary(tree):
    tokens = tree["tokens"]
    events = tree["events"]
    hours = tree["duration_seconds"] / 3600
    parent = next(
        summary
        for summary in tree["sessions"]
        if summary["metadata"].get("id") == tree["root_id"]
    )
    parent_input = parent["tokens"]["input_tokens"]
    input_tokens = tokens.get("input_tokens", 0)
    return {
        "root": tree["root_id"],
        "sessions": tree["session_count"],
        "hours": round(hours, 2),
        "input": input_tokens,
        "uncached": tokens.get("uncached_input_tokens", 0),
        "input_per_hour": round(input_tokens / hours) if hours else 0,
        "parent_share": f"{parent_input / input_tokens:.1%}" if input_tokens else "0.0%",
        "parent_execs": parent["nested_tools"].get("exec_command", 0),
        "agent_messages": parent["outer_tools"].get("send_message", 0)
        + parent["outer_tools"].get("followup_task", 0),
        "task_completions": events.get("task_complete", 0),
        "failed_tasks": len(tree["task_errors"]),
        "compactions": tree["compactions"],
    }


def print_table(trees):
    rows = [compact_summary(tree) for tree in trees]
    columns = list(rows[0])
    widths = {
        column: max(len(column), *(len(str(row[column])) for row in rows))
        for column in columns
    }
    print("  ".join(column.ljust(widths[column]) for column in columns))
    for row in rows:
        print("  ".join(str(row[column]).ljust(widths[column]) for column in columns))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root_ids", nargs="+", help="root Codex session IDs")
    parser.add_argument(
        "--sessions-root",
        type=Path,
        default=Path.home() / ".codex" / "sessions",
        help="directory containing rollout JSONL files",
    )
    parser.add_argument("--json", action="store_true", help="emit full JSON")
    args = parser.parse_args()

    sessions, children = discover_sessions(args.sessions_root)
    unknown = [root_id for root_id in args.root_ids if root_id not in sessions]
    if unknown:
        parser.error(f"unknown session ID: {', '.join(unknown)}")
    trees = [aggregate_tree(root_id, sessions, children) for root_id in args.root_ids]
    if args.json:
        print(json.dumps(trees, indent=2, sort_keys=True))
    else:
        print_table(trees)


if __name__ == "__main__":
    main()

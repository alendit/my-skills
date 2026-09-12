#!/usr/bin/env python3
"""Summarize token use and workflow activity in Codex rollout JSONL files."""

import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


TOKEN_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "cache_write_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)
NESTED_TOOL_PATTERN = re.compile(r"\btools\.([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def parse_timestamp(value):
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def text_content(content):
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "".join(
        item.get("text", "")
        for item in content
        if isinstance(item, dict) and isinstance(item.get("text"), str)
    )


def parse_tool_arguments(value):
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return {}
        return parsed if isinstance(parsed, dict) else {}
    return {}


def normalize_tool_input(value):
    arguments = parse_tool_arguments(value)
    if arguments:
        return arguments, json.dumps(arguments, sort_keys=True, separators=(",", ":"))
    if isinstance(value, str):
        return {}, " ".join(value.split())
    return {}, json.dumps(value, sort_keys=True, default=str)


def merge_token_peak(peak, candidate):
    if not isinstance(candidate, dict):
        return
    for field in TOKEN_FIELDS:
        value = candidate.get(field)
        if isinstance(value, int):
            peak[field] = max(peak[field], value)


def summarize_rollout(path):
    path = Path(path)
    metadata = {}
    timestamps = []
    models = Counter()
    efforts = Counter()
    event_types = Counter()
    response_types = Counter()
    message_counts = Counter()
    message_chars = Counter()
    outer_tools = Counter()
    nested_tools = Counter()
    repeated_tool_inputs = Counter()
    token_peak = {field: 0 for field in TOKEN_FIELDS}
    token_records = 0
    compactions = 0
    malformed_rows = 0
    inter_agent_records = 0
    task_errors = []

    with path.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                malformed_rows += 1
                continue

            timestamp = parse_timestamp(row.get("timestamp"))
            if timestamp is not None:
                timestamps.append(timestamp)

            row_type = row.get("type")
            payload = row.get("payload") or {}

            if row_type == "session_meta":
                source = payload.get("source")
                spawn = {}
                if isinstance(source, dict):
                    spawn = ((source.get("subagent") or {}).get("thread_spawn") or {})
                metadata = {
                    "id": payload.get("id") or payload.get("session_id"),
                    "parent_id": payload.get("parent_thread_id")
                    or payload.get("parent_id"),
                    "cwd": payload.get("cwd"),
                    "source": source,
                    "thread_source": payload.get("thread_source"),
                    "cli_version": payload.get("cli_version"),
                    "agent_path": spawn.get("agent_path"),
                    "agent_nickname": spawn.get("agent_nickname"),
                }
            elif row_type == "turn_context":
                model = payload.get("model")
                effort = payload.get("reasoning_effort")
                if model:
                    models[model] += 1
                if effort:
                    efforts[effort] += 1
            elif row_type == "token_usage_record":
                token_records += 1
                merge_token_peak(
                    token_peak,
                    payload.get("thread_token_usage") or payload.get("usage"),
                )
            elif row_type == "event_msg":
                event_type = payload.get("type") or "unknown"
                event_types[event_type] += 1
                if event_type == "task_complete" and payload.get("error"):
                    error = payload["error"]
                    task_errors.append(
                        {
                            "timestamp": row.get("timestamp"),
                            "message": error.get("message")
                            if isinstance(error, dict)
                            else str(error),
                            "code": error.get("codex_error_info")
                            if isinstance(error, dict)
                            else None,
                        }
                    )
                if event_type == "token_count":
                    token_records += 1
                    info = payload.get("info") or {}
                    merge_token_peak(token_peak, info.get("total_token_usage"))
            elif row_type == "compacted":
                compactions += 1
            elif row_type == "inter_agent_communication_metadata":
                inter_agent_records += 1
            elif row_type == "response_item":
                item_type = payload.get("type") or "unknown"
                response_types[item_type] += 1
                if item_type == "message":
                    role = payload.get("role") or "unknown"
                    message_counts[role] += 1
                    message_chars[role] += len(text_content(payload.get("content")))
                elif item_type in {"function_call", "custom_tool_call"}:
                    name = payload.get("name") or "unknown"
                    outer_tools[name] += 1
                    raw_input = payload.get("arguments", payload.get("input"))
                    arguments, normalized = normalize_tool_input(raw_input)
                    repeated_tool_inputs[(name, normalized)] += 1
                    if name in {"exec", "functions.exec"}:
                        code = arguments.get("code") or (
                            raw_input if isinstance(raw_input, str) else None
                        )
                        if isinstance(code, str):
                            nested_tools.update(NESTED_TOOL_PATTERN.findall(code))

    start = min(timestamps) if timestamps else None
    end = max(timestamps) if timestamps else None
    uncached_input = max(
        0, token_peak["input_tokens"] - token_peak["cached_input_tokens"]
    )
    repeated = [
        {"tool": name, "count": count, "arguments": arguments}
        for (name, arguments), count in repeated_tool_inputs.most_common(10)
        if count > 1
    ]

    return {
        "path": str(path),
        "metadata": metadata,
        "start": start.isoformat() if start else None,
        "end": end.isoformat() if end else None,
        "duration_seconds": (end - start).total_seconds() if start and end else 0,
        "models": dict(models),
        "reasoning_efforts": dict(efforts),
        "tokens": {**token_peak, "uncached_input_tokens": uncached_input},
        "token_records": token_records,
        "events": dict(event_types),
        "responses": dict(response_types),
        "messages": {
            role: {"count": count, "characters": message_chars[role]}
            for role, count in message_counts.items()
        },
        "outer_tools": dict(outer_tools),
        "nested_tools": dict(nested_tools),
        "repeated_tool_inputs": repeated,
        "compactions": compactions,
        "inter_agent_records": inter_agent_records,
        "task_errors": task_errors,
        "malformed_rows": malformed_rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rollouts", nargs="+", type=Path, help="rollout JSONL file")
    parser.add_argument(
        "--compact", action="store_true", help="emit compact rather than indented JSON"
    )
    args = parser.parse_args()
    result = [summarize_rollout(path) for path in args.rollouts]
    output = result[0] if len(result) == 1 else result
    print(json.dumps(output, indent=None if args.compact else 2, sort_keys=True))


if __name__ == "__main__":
    main()

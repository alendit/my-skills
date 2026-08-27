#!/usr/bin/env python3
"""Validate the four-case writing study package and mechanical capture records."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EXPECTED_CASE_IDS = {
    "initial-technical-writing",
    "revision-after-change",
    "project-glossary-use",
    "agent-handoff",
}
EXPECTED_DIMENSIONS = {
    "clarity",
    "factual-preservation",
    "terminology-consistency",
    "unnecessary-detail",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def emit(value: dict[str, Any]) -> None:
    print(json.dumps(value, indent=2, sort_keys=True))


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing JSON file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}:{exc.lineno}:{exc.colno}: {exc.msg}") from exc


def canonical_hash(value: Any) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(data).hexdigest()


def package_revision(skill_root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(skill_root.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        digest.update(path.relative_to(skill_root).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return "sha256:" + digest.hexdigest()


def parse_timestamp(value: Any) -> bool:
    if not nonempty(value):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def case_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        case.get("id", f"missing-{index}"): case
        for index, case in enumerate(manifest.get("cases", []))
        if isinstance(case, dict)
    }


def validate_manifest(manifest: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["case manifest must be a JSON object"]
    if manifest.get("schema_version") != 1:
        errors.append("case manifest schema_version must be 1")
    if not nonempty(manifest.get("study_question")):
        errors.append("case manifest study_question must be non-empty")
    if set(manifest.get("review_dimensions", [])) != EXPECTED_DIMENSIONS:
        errors.append(f"review_dimensions must be {sorted(EXPECTED_DIMENSIONS)}")
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        return errors + ["case manifest cases must be a list"]
    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if set(ids) != EXPECTED_CASE_IDS or len(ids) != len(EXPECTED_CASE_IDS):
        errors.append(f"case IDs must be exactly {sorted(EXPECTED_CASE_IDS)}, got {ids}")
    for index, case in enumerate(cases):
        location = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{location} must be an object")
            continue
        for field in ("id", "artifact_assignment", "intended_reader"):
            if not nonempty(case.get(field)):
                errors.append(f"{location}.{field} must be non-empty")
        contracts = case.get("contract_ids")
        if not isinstance(contracts, list) or not contracts or not all(nonempty(item) for item in contracts):
            errors.append(f"{location}.contract_ids must be non-empty strings")
        packet = case.get("source_packet")
        if not isinstance(packet, dict) or not packet:
            errors.append(f"{location}.source_packet must be a non-empty object")
        questions = case.get("review_questions")
        if not isinstance(questions, list):
            errors.append(f"{location}.review_questions must be a list")
            continue
        dimensions = [item.get("dimension") for item in questions if isinstance(item, dict)]
        if set(dimensions) != EXPECTED_DIMENSIONS or len(dimensions) != len(EXPECTED_DIMENSIONS):
            errors.append(f"{location}.review_questions must contain each review dimension once")
        if any(not isinstance(item, dict) or not nonempty(item.get("question")) for item in questions):
            errors.append(f"{location}.review_questions must contain non-empty questions")
    return errors


def validate_schema(schema: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(schema, dict):
        return ["capture schema must be a JSON object"]
    if schema.get("schema_version") != 1:
        errors.append("capture schema schema_version must be 1")
    if schema.get("record_type") != "clear-technical-writing-model-capture":
        errors.append("capture schema record_type is incorrect")
    required = schema.get("required_fields")
    if not isinstance(required, list) or not required:
        errors.append("capture schema required_fields must be non-empty")
    if set(schema.get("conditions", [])) != {"baseline", "skill"}:
        errors.append("capture schema conditions must be baseline and skill")
    statuses = set(schema.get("statuses", []))
    completed = set(schema.get("completed_statuses", []))
    if statuses != {"prepared", "current", "product-contract-failure", "model-capability-unconfirmed"}:
        errors.append("capture schema status vocabulary is incorrect")
    if completed != {"current", "product-contract-failure"} or not completed.issubset(statuses):
        errors.append("capture schema completed_statuses are incorrect")
    return errors


def validate_capture(
    capture: Any,
    manifest: dict[str, Any],
    schema: dict[str, Any],
    exact_revision: str,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(capture, dict):
        return ["capture must be a JSON object"]
    missing = sorted(set(schema["required_fields"]) - set(capture))
    if missing:
        errors.append(f"capture missing required fields: {missing}")
    if capture.get("schema_version") != schema["schema_version"]:
        errors.append("capture schema_version is incorrect")
    if capture.get("record_type") != schema["record_type"]:
        errors.append("capture record_type is incorrect")
    case = case_map(manifest).get(capture.get("case_id"))
    if case is None:
        errors.append(f"capture case_id is unknown: {capture.get('case_id')!r}")
        return errors
    for field in ("trial_id", "model_id", "runtime_id", "outer_instructions"):
        if not nonempty(capture.get(field)):
            errors.append(f"capture {field} must be non-empty")
    if capture.get("condition") not in schema["conditions"]:
        errors.append("capture condition must be baseline or skill")
    if capture.get("skill_revision") != exact_revision:
        errors.append("capture skill_revision does not match the exact current package revision")
    if capture.get("source_packet_hash") != canonical_hash(case["source_packet"]):
        errors.append("capture source_packet_hash does not match the selected case")
    for field in ("generation_settings", "tool_context_configuration"):
        if not isinstance(capture.get(field), dict):
            errors.append(f"capture {field} must be a JSON object")
    status = capture.get("status")
    if status not in schema["statuses"]:
        errors.append(f"capture status must be one of {schema['statuses']}")
    if not parse_timestamp(capture.get("recorded_at")):
        errors.append("capture recorded_at must be timezone-aware ISO-8601")
    completed = status in schema["completed_statuses"]
    if completed:
        if not nonempty(capture.get("output")):
            errors.append(f"capture status {status} requires non-empty output")
        if not parse_timestamp(capture.get("completed_at")):
            errors.append(f"capture status {status} requires completed_at")
    elif status == "prepared":
        if capture.get("output") is not None or capture.get("completed_at") is not None:
            errors.append("prepared capture requires null output and completed_at")
    elif status == "model-capability-unconfirmed":
        if capture.get("output") is not None:
            errors.append("model-capability-unconfirmed capture requires null output")
        if not parse_timestamp(capture.get("completed_at")):
            errors.append("model-capability-unconfirmed capture requires completed_at")
    return errors


def parse_object(value: str, label: str) -> dict[str, Any]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} is not valid JSON: {exc.msg}") from exc
    if not isinstance(parsed, dict):
        raise ValueError(f"{label} must be a JSON object")
    return parsed


def build_capture(
    case: dict[str, Any], revision: str, trial_id: str, condition: str,
    model_id: str, runtime_id: str, outer_instructions: str,
    generation_settings: dict[str, Any], tool_context: dict[str, Any],
    status: str, output: str | None,
) -> dict[str, Any]:
    now = utc_now()
    return {
        "schema_version": 1,
        "record_type": "clear-technical-writing-model-capture",
        "case_id": case["id"],
        "trial_id": trial_id,
        "condition": condition,
        "skill_revision": revision,
        "model_id": model_id,
        "runtime_id": runtime_id,
        "outer_instructions": outer_instructions,
        "source_packet_hash": canonical_hash(case["source_packet"]),
        "generation_settings": generation_settings,
        "tool_context_configuration": tool_context,
        "status": status,
        "recorded_at": now,
        "completed_at": None if status == "prepared" else now,
        "output": output,
    }


def package_files(repo_root: Path) -> tuple[Path, dict[str, Any], dict[str, Any]]:
    skill_root = repo_root / "skills/clear-technical-writing"
    manifest = load_json(skill_root / "evals/fixtures.json")
    schema = load_json(skill_root / "evals/capture.schema.json")
    return skill_root, manifest, schema


def validate_package_command(args: argparse.Namespace) -> int:
    try:
        skill_root, manifest, schema = package_files(args.repo_root.resolve())
        errors = validate_manifest(manifest) + validate_schema(schema)
        if not (skill_root / "SKILL.md").is_file():
            errors.append("clear-technical-writing/SKILL.md is missing")
        if not (skill_root / "scripts/validate_evidence.py").stat().st_mode & 0o111:
            errors.append("validate_evidence.py is not executable")
    except (ValueError, FileNotFoundError) as exc:
        errors = [str(exc)]
        skill_root = args.repo_root.resolve() / "skills/clear-technical-writing"
        manifest = {}
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    emit({
        "command": "validate-package",
        "status": "pass" if not errors else "fail",
        "case_ids": sorted(case_map(manifest)),
        "skill_revision": package_revision(skill_root) if skill_root.is_dir() else None,
        "capability_claim": "none-mechanical-validation-only",
        "errors": errors,
    })
    return 1 if errors else 0


def default_output_path(case_id: str, condition: str) -> Path:
    directory = Path(tempfile.gettempdir()) / "clear-technical-writing-captures"
    directory.mkdir(parents=True, exist_ok=True)
    return directory / f"{case_id}-{condition}-{uuid.uuid4().hex[:8]}.json"


def prepare_capture_command(args: argparse.Namespace) -> int:
    try:
        skill_root, manifest, schema = package_files(args.repo_root.resolve())
        case = case_map(manifest).get(args.case)
        if case is None:
            raise ValueError(f"unknown case {args.case!r}; choose one of {', '.join(sorted(EXPECTED_CASE_IDS))}")
        capture = build_capture(
            case,
            package_revision(skill_root),
            args.trial_id,
            args.condition,
            args.model_id,
            args.runtime_id,
            args.outer_instructions,
            parse_object(args.settings_json, "--settings-json"),
            parse_object(args.tool_context_json, "--tool-context-json"),
            args.status,
            args.output_text,
        )
        errors = validate_capture(capture, manifest, schema, package_revision(skill_root))
        if errors:
            raise ValueError("capture arguments are inconsistent:\n  - " + "\n  - ".join(errors))
        output_path = (args.output_path or default_output_path(args.case, args.condition)).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(capture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        emit({"command": "prepare-capture", "status": "fail", "error": str(exc)})
        return 1
    emit({
        "command": "prepare-capture",
        "status": "pass",
        "case_id": capture["case_id"],
        "condition": capture["condition"],
        "capture_status": capture["status"],
        "output_path": str(output_path),
        "capability_claim": "none-capture-record-only",
    })
    return 0


def validate_capture_command(args: argparse.Namespace) -> int:
    try:
        skill_root, manifest, schema = package_files(args.repo_root.resolve())
        capture = load_json(args.capture.resolve())
        errors = validate_capture(capture, manifest, schema, package_revision(skill_root))
    except ValueError as exc:
        errors = [str(exc)]
        capture = {}
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    emit({
        "command": "validate-capture",
        "status": "pass" if not errors else "fail",
        "capture": str(args.capture.resolve()),
        "case_id": capture.get("case_id"),
        "condition": capture.get("condition"),
        "capability_claim": "none-record-validation-does-not-judge-output",
        "errors": errors,
    })
    return 1 if errors else 0


def self_test_command(args: argparse.Namespace) -> int:
    try:
        skill_root, manifest, schema = package_files(args.repo_root.resolve())
    except ValueError as exc:
        emit({"command": "self-test", "status": "fail", "errors": [str(exc)]})
        return 1
    revision = package_revision(skill_root)
    case = case_map(manifest)["initial-technical-writing"]
    valid = build_capture(
        case, revision, "synthetic-pair", "skill", "synthetic-model", "synthetic-runtime",
        "Mechanical self-test only.", {}, {}, "current", "Observable synthetic output.",
    )
    tests: dict[str, bool] = {
        "manifest": not validate_manifest(manifest),
        "schema": not validate_schema(schema),
        "valid_completed_capture": not validate_capture(valid, manifest, schema, revision),
    }
    mutations = {
        "missing_record_field": lambda item: item.pop("model_id"),
        "invalid_condition": lambda item: item.__setitem__("condition", "candidate"),
        "wrong_revision": lambda item: item.__setitem__("skill_revision", "sha256:wrong"),
        "invalid_status": lambda item: item.__setitem__("status", "passed"),
        "completed_without_output": lambda item: item.__setitem__("output", None),
        "wrong_source_packet": lambda item: item.__setitem__("source_packet_hash", "sha256:wrong"),
    }
    for name, mutate in mutations.items():
        candidate = json.loads(json.dumps(valid))
        mutate(candidate)
        tests[name] = bool(validate_capture(candidate, manifest, schema, revision))
    malformed_path = Path(tempfile.gettempdir()) / f"clear-writing-malformed-{uuid.uuid4().hex}.json"
    try:
        malformed_path.write_text("{", encoding="utf-8")
        try:
            load_json(malformed_path)
            tests["malformed_json"] = False
        except ValueError:
            tests["malformed_json"] = True
    finally:
        malformed_path.unlink(missing_ok=True)
    failed = sorted(name for name, passed in tests.items() if not passed)
    emit({
        "command": "self-test",
        "status": "pass" if not failed else "fail",
        "cases": tests,
        "capability_claim": "none-mechanical-self-test-only",
    })
    return 1 if failed else 0


def build_parser() -> argparse.ArgumentParser:
    script_path = Path(__file__).resolve()
    default_repo = script_path.parents[3]
    parser = argparse.ArgumentParser(
        description="Validate four representative writing cases and mechanical baseline-or-skill capture records.",
        epilog=(
            "This helper checks structure and identity only. It does not score prose or terminology. "
            "Generated captures default to the system temporary directory."
        ),
    )
    parser.add_argument("--repo-root", type=Path, default=default_repo, help=f"repository root (default: {default_repo})")
    subparsers = parser.add_subparsers(dest="command", required=True)

    package_parser = subparsers.add_parser("validate-package", help="validate case and capture JSON structure")
    package_parser.set_defaults(handler=validate_package_command)

    prepare_parser = subparsers.add_parser("prepare-capture", help="write one mechanical capture record")
    prepare_parser.add_argument("--case", required=True, choices=sorted(EXPECTED_CASE_IDS))
    prepare_parser.add_argument("--trial-id", required=True, help="shared identifier for the paired baseline and skill outputs")
    prepare_parser.add_argument("--condition", required=True, choices=["baseline", "skill"])
    prepare_parser.add_argument("--model-id", required=True)
    prepare_parser.add_argument("--runtime-id", required=True)
    prepare_parser.add_argument("--outer-instructions", required=True)
    prepare_parser.add_argument("--settings-json", default="{}")
    prepare_parser.add_argument("--tool-context-json", default="{}")
    prepare_parser.add_argument(
        "--status", default="prepared",
        choices=["prepared", "current", "product-contract-failure", "model-capability-unconfirmed"],
    )
    prepare_parser.add_argument("--output-text")
    prepare_parser.add_argument("--output-path", type=Path)
    prepare_parser.set_defaults(handler=prepare_capture_command)

    capture_parser = subparsers.add_parser("validate-capture", help="validate one capture without judging its output")
    capture_parser.add_argument("capture", type=Path)
    capture_parser.set_defaults(handler=validate_capture_command)

    self_test_parser = subparsers.add_parser("self-test", help="exercise bounded valid and malformed records")
    self_test_parser.set_defaults(handler=self_test_command)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())

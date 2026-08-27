#!/usr/bin/env python3
"""Validate clear-writing evaluation mechanics and capture records.

Exit codes: 0 success, 1 conformance failure, 2 command-line usage error.
Generated captures default to the system temporary directory.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


EXPECTED_FIXTURE_IDS = {
    *(f"V{number}" for number in range(1, 9)),
    *(f"M{number}" for number in range(1, 9)),
    "V11-GLOSSARY-PRESENT",
    "V11-GLOSSARY-ABSENT",
}
CHANGED_SKILLS = (
    "clear-technical-writing",
    "technical-note-series",
    "project-architecture-doc",
    "add-architectural-guidances",
    "evidence-efficient-review",
    "supervised-implementer-loop",
    "review-fixpoint",
)
CHANGED_CONSUMER_MARKDOWN = (
    "skills/technical-note-series/SKILL.md",
    "skills/technical-note-series/references/research-and-reader-journey.md",
    "skills/technical-note-series/references/drafting-and-coherence.md",
    "skills/technical-note-series/references/validation-and-review.md",
    "skills/project-architecture-doc/SKILL.md",
    "skills/add-architectural-guidances/SKILL.md",
    "skills/evidence-efficient-review/SKILL.md",
    "skills/supervised-implementer-loop/SKILL.md",
    "skills/review-fixpoint/SKILL.md",
)

# CTW9 declares these composition links. Validate only rendered destinations
# and counts, never the meaning of surrounding prose.
DECLARED_STRUCTURAL_LINKS = {
    "skills/clear-technical-writing/SKILL.md": {
        "references/artifact-routing.md": 1,
        "references/revision-after-change.md": 1,
        "references/examples.md": 1,
        "references/research-rationale.md": 1,
        "references/validation-scenarios.md": 1,
        "references/project-glossaries.md": 1,
    },
    "skills/technical-note-series/SKILL.md": {"../clear-technical-writing/SKILL.md": 1},
    "skills/technical-note-series/references/research-and-reader-journey.md": {
        "../../clear-technical-writing/references/project-glossaries.md": 1
    },
    "skills/project-architecture-doc/SKILL.md": {
        "../clear-technical-writing/SKILL.md": 1,
        "../clear-technical-writing/references/project-glossaries.md": 1,
    },
    "skills/add-architectural-guidances/SKILL.md": {
        "../clear-technical-writing/SKILL.md": 1,
        "../clear-technical-writing/references/project-glossaries.md": 1,
    },
    "skills/evidence-efficient-review/SKILL.md": {
        "../clear-technical-writing/SKILL.md": 1,
        "../clear-technical-writing/references/project-glossaries.md": 1,
    },
    "skills/supervised-implementer-loop/SKILL.md": {
        "../clear-technical-writing/SKILL.md": 1,
        "../clear-technical-writing/references/project-glossaries.md": 1,
    },
    "skills/review-fixpoint/SKILL.md": {
        "../clear-technical-writing/SKILL.md": 1,
        "../clear-technical-writing/references/project-glossaries.md": 1,
    },
}
V11_ANSWER_FIELDS = ("before", "change", "correctness", "evidence", "requested_action")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing JSON file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}:{exc.lineno}:{exc.colno}: {exc.msg}") from exc


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def package_hash(skill_root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(skill_root.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        digest.update(path.relative_to(skill_root).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return "sha256:" + digest.hexdigest()


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def observable_evidence(value: Any) -> bool:
    return nonempty_string(value) or isinstance(value, (list, dict)) and bool(value)


def find_forbidden_keys(value: Any, forbidden: set[str], location: str = "$") -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}"
            if key in forbidden:
                errors.append(f"{child_location} is a forbidden private field")
            errors.extend(find_forbidden_keys(child, forbidden, child_location))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(find_forbidden_keys(child, forbidden, f"{location}[{index}]"))
    return errors


def fixture_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        fixture.get("id", f"missing-{index}"): fixture
        for index, fixture in enumerate(manifest.get("fixtures", []))
        if isinstance(fixture, dict)
    }


def fixture_lane(fixture_id: str) -> str:
    if fixture_id.startswith("V11-"):
        return "V11"
    if fixture_id.startswith("V"):
        return "V"
    if fixture_id.startswith("M"):
        return "M"
    return "unknown"


def compatible_states(fixture_id: str) -> set[str]:
    common = {"prepared", "current", "product-contract-failure"}
    lane_state = {
        "V": "model-capability-unconfirmed",
        "M": "capability-unconfirmed",
        "V11": "human-comprehension-unconfirmed",
    }.get(fixture_lane(fixture_id))
    return common | ({lane_state} if lane_state else set())


def validate_schema(schema: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(schema, dict):
        return ["capture schema must be a JSON object"]
    if schema.get("schema_version") != 1:
        errors.append("capture schema schema_version must be 1")
    if schema.get("record_type") != "clear-technical-writing-evaluation-capture":
        errors.append("capture schema record_type is incorrect")
    if schema.get("aggregation") != {
        "scope": "single-fixture-run",
        "confirms_capability_suite": False,
    }:
        errors.append("capture schema must limit validation to one fixture run without suite confirmation")
    for field in (
        "required_fields", "timestamp_fields", "status_rules", "scorecard_required_fields",
        "criterion_result_required_fields", "trace_event_required_fields", "forbidden_private_fields",
    ):
        if not schema.get(field):
            errors.append(f"capture schema requires non-empty {field}")
    expected = {
        "prepared", "current", "product-contract-failure", "model-capability-unconfirmed",
        "capability-unconfirmed", "human-comprehension-unconfirmed",
    }
    actual = set(schema.get("status_rules", {}))
    if actual != expected:
        errors.append(f"capture schema statuses must be {sorted(expected)}, got {sorted(actual)}")
    return errors


def validate_trace_cases(fixture: dict[str, Any], location: str) -> list[str]:
    errors: list[str] = []
    trace_cases = fixture.get("trace_cases")
    if not isinstance(trace_cases, list) or not trace_cases:
        return [f"{location}.trace_cases must be a non-empty list"]
    source_ids = {
        case.get("case_id") for case in fixture.get("source_packet", {}).get("cases", [])
        if isinstance(case, dict)
    }
    trace_ids: set[str] = set()
    for index, case in enumerate(trace_cases):
        here = f"{location}.trace_cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{here} must be an object")
            continue
        case_id = case.get("case_id")
        if not nonempty_string(case_id):
            errors.append(f"{here}.case_id must be non-empty")
        elif case_id in trace_ids:
            errors.append(f"{here}.case_id duplicates {case_id}")
        else:
            trace_ids.add(case_id)
        if case.get("glossary_state") not in {"selected", "opt-out"}:
            errors.append(f"{here}.glossary_state must be selected or opt-out")
        required = case.get("required_events")
        forbidden = case.get("forbidden_events")
        pairs = case.get("ordered_pairs")
        if not isinstance(required, list) or not required:
            errors.append(f"{here}.required_events must be non-empty")
            continue
        if not isinstance(forbidden, list):
            errors.append(f"{here}.forbidden_events must be a list")
            continue
        if not isinstance(pairs, list) or not pairs:
            errors.append(f"{here}.ordered_pairs must be non-empty")
            continue
        for pair in pairs:
            if not isinstance(pair, list) or len(pair) != 2:
                errors.append(f"{here}.ordered_pairs entries must contain two event types")
            elif pair[0] not in required or pair[1] not in required:
                errors.append(f"{here}.ordered_pairs references an event outside required_events: {pair}")
        if "private_reasoning" not in forbidden:
            errors.append(f"{here} must forbid private_reasoning events")
        if case.get("glossary_state") == "opt-out":
            for event_type in ("placement_question", "source_access", "glossary_write"):
                if event_type not in forbidden:
                    errors.append(f"{here} opt-out must forbid {event_type}")
    if trace_ids != source_ids:
        errors.append(f"{location}.trace_cases IDs {sorted(trace_ids)} do not match source cases {sorted(source_ids)}")
    return errors


def validate_fixtures(manifest: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["fixture manifest must be a JSON object"]
    if manifest.get("schema_version") != 1:
        errors.append("fixture manifest schema_version must be 1")
    fixtures = manifest.get("fixtures")
    if not isinstance(fixtures, list):
        return errors + ["fixture manifest fixtures must be a list"]
    ids = [item.get("id") for item in fixtures if isinstance(item, dict)]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append(f"fixture IDs are duplicated: {duplicates}")
    if set(ids) != EXPECTED_FIXTURE_IDS:
        errors.append(f"fixture IDs must be {sorted(EXPECTED_FIXTURE_IDS)}, got {sorted(str(value) for value in ids)}")
    required = {
        "id", "evidence_class", "contract_ids", "artifact", "intended_reader", "source_packet",
        "expected_material_outcomes", "forbidden_regressions", "scorer", "first_failure",
    }
    prohibited = {
        "target_prose", "exact_target_prose", "expected_heading", "expected_headings",
        "private_reasoning", "chain_of_thought",
    }
    for index, fixture in enumerate(fixtures):
        here = f"fixtures[{index}]"
        if not isinstance(fixture, dict):
            errors.append(f"{here} must be an object")
            continue
        fixture_id = fixture.get("id")
        missing = sorted(required - set(fixture))
        if missing:
            errors.append(f"{here} ({fixture_id}) missing fields: {missing}")
        expected_class = "blinded-human" if str(fixture_id).startswith("V11-") else "controlled-model"
        if fixture.get("evidence_class") != expected_class:
            errors.append(f"{here} ({fixture_id}) evidence_class must be {expected_class}")
        contracts = fixture.get("contract_ids")
        if not isinstance(contracts, list) or not contracts or not all(nonempty_string(item) for item in contracts):
            errors.append(f"{here} ({fixture_id}) contract_ids must be non-empty strings")
            contracts = []
        elif any(re.fullmatch(r"CTW(?:[1-9]|10)|GL[1-8]", item) is None for item in contracts):
            errors.append(f"{here} ({fixture_id}) contract_ids must name CTW1-CTW10 or GL1-GL8")
        artifact = fixture.get("artifact")
        if not isinstance(artifact, dict) or not all(nonempty_string(artifact.get(field)) for field in ("assignment", "intent")):
            errors.append(f"{here} ({fixture_id}) artifact requires assignment and intent")
        reader = fixture.get("intended_reader")
        if not isinstance(reader, dict) or not all(reader.get(field) for field in ("role", "assumed_knowledge", "required_outcome")):
            errors.append(f"{here} ({fixture_id}) intended_reader is incomplete")
        if not isinstance(fixture.get("source_packet"), dict) or not fixture["source_packet"]:
            errors.append(f"{here} ({fixture_id}) source_packet must be a non-empty object")
        outcomes = fixture.get("expected_material_outcomes")
        if not isinstance(outcomes, list) or not outcomes or any(
            not isinstance(item, dict) or not nonempty_string(item.get("field")) or not nonempty_string(item.get("relation"))
            for item in outcomes or []
        ):
            errors.append(f"{here} ({fixture_id}) outcomes require field and relation")
        regressions = fixture.get("forbidden_regressions")
        if not isinstance(regressions, list) or not regressions or any(
            not isinstance(item, dict) or not nonempty_string(item.get("id")) or not nonempty_string(item.get("description"))
            for item in regressions or []
        ):
            errors.append(f"{here} ({fixture_id}) regressions require id and description")
        scorer = fixture.get("scorer")
        if not isinstance(scorer, dict) or not nonempty_string(scorer.get("method")):
            errors.append(f"{here} ({fixture_id}) scorer requires a method")
            scorer = {}
        criteria = scorer.get("criteria")
        if not isinstance(criteria, list) or not criteria:
            errors.append(f"{here} ({fixture_id}) scorer.criteria must be non-empty")
            criteria = []
        seen: set[str] = set()
        for criterion_index, criterion in enumerate(criteria):
            criterion_here = f"{here}.scorer.criteria[{criterion_index}]"
            if not isinstance(criterion, dict):
                errors.append(f"{criterion_here} must be an object")
                continue
            criterion_id = criterion.get("id")
            if not nonempty_string(criterion_id):
                errors.append(f"{criterion_here}.id must be non-empty")
            elif criterion_id in seen:
                errors.append(f"{criterion_here}.id duplicates {criterion_id}")
            else:
                seen.add(criterion_id)
            for field in ("description", "failure_boundary"):
                if not nonempty_string(criterion.get(field)):
                    errors.append(f"{criterion_here}.{field} must be non-empty")
            if not criterion.get("observable_fields"):
                errors.append(f"{criterion_here}.observable_fields must be non-empty")
            criterion_contracts = criterion.get("contract_ids")
            if not isinstance(criterion_contracts, list) or not criterion_contracts:
                errors.append(f"{criterion_here}.contract_ids must be non-empty")
            elif not set(criterion_contracts).issubset(set(contracts)):
                errors.append(f"{criterion_here}.contract_ids must be declared by fixture {fixture_id}")
        first_failure = fixture.get("first_failure")
        if not isinstance(first_failure, dict) or not all(nonempty_string(first_failure.get(field)) for field in ("contract_id", "boundary")):
            errors.append(f"{here} ({fixture_id}) first_failure is incomplete")
        elif first_failure["contract_id"] not in contracts:
            errors.append(f"{here} ({fixture_id}) first_failure contract is not declared")
        errors.extend(find_forbidden_keys(fixture, prohibited, here))
        if fixture_id in {"M7", "M8"}:
            errors.extend(validate_trace_cases(fixture, here))

    by_id = fixture_map(manifest)
    v6_boundary = by_id.get("V6", {}).get("source_packet", {}).get("exact_boundaries", [{}])[0]
    if v6_boundary != {"name": "payload_limit", "value": 16, "unit": "MiB", "rule": "reject above"}:
        errors.append("V6 must retain the exact 16 MiB reject-above input boundary")
    v4_facts = by_id.get("V4", {}).get("source_packet", {}).get("compact", {}).get("facts", [])
    if set(v4_facts) != {
        "The parser accepts a successful empty result object.",
        "Successful row-bearing responses are unchanged.",
        "Parser tests pass.",
    }:
        errors.append("V4 must retain the three compact-artifact input facts")
    if by_id.get("V8", {}).get("source_packet", {}).get("changed_source") != {
        "latency": "equal within measurement precision", "correctness": "one unresolved failure", "decision": "not accepted",
    }:
        errors.append("V8 must retain its corrected input conclusion fields")
    conditions = {
        by_id.get("V11-GLOSSARY-PRESENT", {}).get("condition"),
        by_id.get("V11-GLOSSARY-ABSENT", {}).get("condition"),
    }
    if conditions != {"glossary-present", "glossary-absent"}:
        errors.append("V11 fixtures must contain glossary-present and glossary-absent conditions")
    for fixture_id in ("V11-GLOSSARY-PRESENT", "V11-GLOSSARY-ABSENT"):
        scorer = by_id.get(fixture_id, {}).get("scorer", {})
        if scorer.get("answer_key_fields") != list(V11_ANSWER_FIELDS):
            errors.append(f"{fixture_id} must define the five CTW10 answer-key fields")
        if scorer.get("requires_no_factual_regression") is not True:
            errors.append(f"{fixture_id} must require no factual regression")
        requirements = scorer.get("commissioning_requirements")
        if not isinstance(requirements, dict):
            errors.append(f"{fixture_id} must define commissioning requirements")
            continue
        if not nonempty_string(requirements.get("metric")) or not nonempty_string(requirements.get("direction")):
            errors.append(f"{fixture_id} commissioning requires metric and direction")
        if requirements.get("default_threshold", "missing") is not None:
            errors.append(f"{fixture_id} must not supply a default numeric threshold")
        if not requirements.get("required_before_generation"):
            errors.append(f"{fixture_id} must identify pre-generation commissioning fields")
        if "minimum_delta" in requirements or "basis" in requirements:
            errors.append(f"{fixture_id} contains an unsupported fixed-threshold field")
    return errors


def prose_lines(path: Path) -> Iterable[tuple[int, str]]:
    fenced = False
    fence_character = ""
    fence_length = 0
    for number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})", raw_line)
        if fence:
            run = fence.group(1)
            if not fenced:
                fenced, fence_character, fence_length = True, run[0], len(run)
            elif run[0] == fence_character and len(run) >= fence_length:
                fenced = False
            continue
        if fenced:
            continue
        line = raw_line
        previous = None
        while previous != line:
            previous = line
            line = re.sub(r"(`+)[^`]*?\1", "", line)
        yield number, line


def markdown_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for _, line in prose_lines(path):
        heading = re.match(r"^ {0,3}#{1,6} +(.+?) *#* *$", line)
        if not heading:
            continue
        title = heading.group(1).replace("`", "")
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", title)
        slug = re.sub(r"[^\w\- ]", "", title.lower())
        slug = re.sub(r" +", "-", slug.strip())
        duplicate = counts.get(slug, 0)
        counts[slug] = duplicate + 1
        anchors.add(slug if duplicate == 0 else f"{slug}-{duplicate}")
    return anchors


def rendered_relative_links(path: Path) -> list[tuple[int, str]]:
    links: list[tuple[int, str]] = []
    for line_number, line in prose_lines(path):
        for match in re.finditer(r"(?<!!)\[[^]\n]+\]\(([^)]+)\)", line):
            raw = match.group(1).strip()
            target = raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw.split()[0]
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("//"):
                continue
            links.append((line_number, target))
    return links


def relative_link_errors(paths: Iterable[Path], repo_root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    checked = 0
    for source in paths:
        for line_number, target in rendered_relative_links(source):
            checked += 1
            path_part, separator, fragment = target.partition("#")
            destination = source if not path_part else (source.parent / path_part).resolve()
            location = f"{source.relative_to(repo_root)}:{line_number}"
            if path_part and not destination.exists():
                errors.append(f"{location}: relative link target does not exist: {target}")
            elif separator and fragment:
                if destination.suffix.lower() not in {".md", ""}:
                    errors.append(f"{location}: fragment targets non-Markdown file: {target}")
                elif fragment not in markdown_anchors(destination):
                    errors.append(f"{location}: Markdown anchor does not exist: {target}")
    return errors, checked


def run_command(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def whitespace_errors(paths: Iterable[Path], repo_root: Path) -> list[str]:
    errors: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if text and not text.endswith("\n"):
            errors.append(f"{path.relative_to(repo_root)} lacks a final newline")
        for line_number, line in enumerate(text.splitlines(), 1):
            if line != line.rstrip():
                errors.append(f"{path.relative_to(repo_root)}:{line_number} has trailing whitespace")
    return errors


def validate_package(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    skill_root = repo_root / "skills/clear-technical-writing"
    errors: list[str] = []
    counts: dict[str, Any] = {}
    try:
        manifest = load_json(skill_root / "evals/fixtures.json")
        schema = load_json(skill_root / "evals/capture.schema.json")
    except ValueError as exc:
        print(f"error: [V10] {exc}", file=sys.stderr)
        emit({"command": "validate-package", "status": "fail", "errors": [str(exc)]})
        return 1
    errors.extend(f"[V10] {item}" for item in validate_fixtures(manifest))
    errors.extend(f"[V10] {item}" for item in validate_schema(schema))
    counts["fixtures"] = len(manifest.get("fixtures", []))

    required_files = {
        "SKILL.md", "references/artifact-routing.md", "references/revision-after-change.md",
        "references/examples.md", "references/research-rationale.md",
        "references/validation-scenarios.md", "references/project-glossaries.md",
        "evals/fixtures.json", "evals/capture.schema.json", "scripts/validate_evidence.py",
    }
    missing_files = sorted(item for item in required_files if not (skill_root / item).is_file())
    if missing_files:
        errors.append(f"[V10] package files are missing: {missing_files}")
    if (skill_root / "scripts/validate_evidence.py").is_file() and not (skill_root / "scripts/validate_evidence.py").stat().st_mode & 0o111:
        errors.append("[V10] deterministic entrypoint is not executable")
    package_text_files = [skill_root / item for item in required_files if (skill_root / item).is_file()]
    errors.extend(f"[V10] {item}" for item in whitespace_errors(package_text_files, repo_root))
    counts["package_text_files_whitespace_checked"] = len(package_text_files)

    quick_validator = args.quick_validator.expanduser().resolve()
    quick_passes = 0
    if not quick_validator.is_file():
        errors.append(f"[V10] skill validator not found: {quick_validator}; pass --quick-validator PATH")
    else:
        for skill_name in CHANGED_SKILLS:
            result = run_command([sys.executable, str(quick_validator), str(repo_root / "skills" / skill_name)], repo_root)
            if result.returncode:
                errors.append(f"[V10] quick validator failed for {skill_name}: {(result.stderr or result.stdout).strip()}")
            else:
                quick_passes += 1
    counts["quick_validate_passes"] = quick_passes

    markdown_paths = sorted(set(skill_root.rglob("*.md")) | {repo_root / item for item in CHANGED_CONSUMER_MARKDOWN})
    link_errors, link_count = relative_link_errors(markdown_paths, repo_root)
    errors.extend(f"[V10] {item}" for item in link_errors)
    counts["rendered_relative_links"] = link_count

    long_references = 0
    for skill_name in CHANGED_SKILLS:
        reference_root = repo_root / "skills" / skill_name / "references"
        if not reference_root.exists():
            continue
        for path in reference_root.rglob("*.md"):
            lines = path.read_text(encoding="utf-8").splitlines()
            if len(lines) <= 100:
                continue
            long_references += 1
            if not any(re.match(r"^#{1,6} +(?:table of )?contents\s*$", line, re.I) for line in lines):
                errors.append(f"[V10] reference over 100 lines lacks a Contents heading: {path.relative_to(repo_root)}")
    counts["references_over_100_lines"] = long_references

    declared_links = 0
    for relative, requirements in DECLARED_STRUCTURAL_LINKS.items():
        targets = [target for _, target in rendered_relative_links(repo_root / relative)]
        for target, expected_count in requirements.items():
            declared_links += 1
            actual_count = targets.count(target)
            if actual_count != expected_count:
                errors.append(f"[V10] {relative} must render {target} {expected_count} time(s), got {actual_count}")
    counts["declared_structural_links"] = declared_links

    standalone = sorted(
        path.name for path in (repo_root / "skills").iterdir()
        if path.is_dir() and re.search(r"(?:project-)?glossary|glossary-manager", path.name)
    )
    if standalone:
        errors.append(f"[V10] standalone project-glossary packages exist: {standalone}")
    counts["standalone_project_glossary_skills"] = len(standalone)

    installed = args.installed_skill.expanduser()
    entrypoint = skill_root / "SKILL.md"
    if not installed.is_symlink():
        errors.append(f"[V10] installed skill path is not a symlink: {installed}")
    elif installed.resolve() != skill_root.resolve():
        errors.append(f"[V10] installed skill resolves to {installed.resolve()}, expected {skill_root.resolve()}")
    else:
        installed_entry = installed / "SKILL.md"
        if not installed_entry.is_file() or not installed_entry.stat().st_size:
            errors.append(f"[V10] installed SKILL.md is not readable: {installed_entry}")
        elif installed_entry.read_bytes() != entrypoint.read_bytes():
            errors.append("[V10] installed SKILL.md does not match repository SKILL.md")

    diff_check = run_command(["git", "diff", "--check"], repo_root)
    if diff_check.returncode:
        errors.append(f"[V10] git diff --check failed: {(diff_check.stdout + diff_check.stderr).strip()}")
    revision = run_command(["git", "rev-parse", "HEAD"], repo_root)
    revision_text = revision.stdout.strip() if revision.returncode == 0 else None
    if revision.returncode:
        errors.append(f"[V10] cannot resolve repository revision: {revision.stderr.strip()}")
    show_check = run_command(["git", "show", "--check", "--oneline", "--no-renames", "HEAD"], repo_root)
    if show_check.returncode:
        errors.append(f"[V10] git show --check failed: {(show_check.stdout + show_check.stderr).strip()}")

    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    emit({
        "command": "validate-package",
        "status": "pass" if not errors else "fail",
        "repository_revision": revision_text,
        "skill_revision": package_hash(skill_root),
        "deterministic_gate": {"V10": "pass" if not errors else "fail"},
        "semantic_review_status": {
            "D1": "requires-independent-source-review",
            "D2": "requires-independent-source-review",
            "V9": "requires-independent-source-review",
        },
        "counts": counts,
        "installed_skill": str(installed),
        "external_status": {
            "V1-V8": "model-capability-unconfirmed",
            "M1-M8": "capability-unconfirmed",
            "V11": "human-comprehension-unconfirmed",
        },
        "errors": errors,
    })
    return 1 if errors else 0


def parse_json_argument(value: str, label: str) -> dict[str, Any]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} is not valid JSON: {exc.msg}") from exc
    if not isinstance(parsed, dict):
        raise ValueError(f"{label} must decode to a JSON object")
    return parsed


def scorecard_for_fixture(fixture: dict[str, Any], scores: dict[str, Any] | None, status: str) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for criterion in fixture["scorer"]["criteria"]:
        raw = None if scores is None else scores.get(criterion["id"])
        decision, evidence = (raw.get("passed"), raw.get("evidence")) if isinstance(raw, dict) else (raw, None)
        results.append({"criterion_id": criterion["id"], "passed": decision, "evidence": evidence})
    scored = status in {"current", "product-contract-failure"}
    overall = all(item["passed"] is True for item in results) if scored else None
    first_failed = next((item for item in results if item["passed"] is False), None) if scored else None
    definitions = {item["id"]: item for item in fixture["scorer"]["criteria"]}
    failed_definition = definitions.get(first_failed["criterion_id"]) if first_failed else None
    return {
        "criteria": results,
        "overall_passed": overall,
        "first_failed_contract": failed_definition["contract_ids"][0] if failed_definition else None,
        "first_failure_boundary": failed_definition["failure_boundary"] if failed_definition else None,
    }


def build_capture(
    fixture: dict[str, Any], skill_revision: str, model_id: str, runtime_id: str,
    outer_instructions: str, generation_settings: dict[str, Any],
    tool_context_configuration: dict[str, Any], trial_count: int, status: str,
    output: str | None = None, scores: dict[str, Any] | None = None,
    failure_kind: str | None = None, trace: list[dict[str, Any]] | None = None,
    commissioning_protocol: dict[str, Any] | None = None,
) -> dict[str, Any]:
    now = utc_now()
    return {
        "schema_version": 1,
        "record_type": "clear-technical-writing-evaluation-capture",
        "fixture_id": fixture["id"],
        "evidence_class": fixture["evidence_class"],
        "trial_run_id": str(uuid.uuid4()),
        "skill_revision": skill_revision,
        "model_id": model_id,
        "runtime_id": runtime_id,
        "outer_instructions": outer_instructions,
        "source_packet_hash": canonical_hash(fixture["source_packet"]),
        "generation_settings": generation_settings,
        "tool_context_configuration": tool_context_configuration,
        "trial_count": trial_count,
        "timestamps": {"prepared_at": now, "completed_at": None if status == "prepared" else now},
        "output": output,
        "scorecard": scorecard_for_fixture(fixture, scores, status),
        "status": {"state": status, "failure_kind": failure_kind},
        "observable_trace": trace or [],
        "commissioning_protocol": commissioning_protocol,
    }


def parse_timestamp(value: Any) -> datetime | None:
    if not nonempty_string(value):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def validate_commissioning_protocol(capture: dict[str, Any], fixture: dict[str, Any], prepared_at: datetime | None) -> list[str]:
    errors: list[str] = []
    protocol = capture.get("commissioning_protocol")
    state = capture.get("status", {}).get("state")
    if fixture_lane(fixture["id"]) != "V11":
        if protocol is not None:
            errors.append("non-V11 capture commissioning_protocol must be null")
        return errors
    if state == "prepared":
        if protocol is not None and not isinstance(protocol, dict):
            errors.append("prepared V11 commissioning_protocol must be an object or null")
        return errors
    if not isinstance(protocol, dict):
        return ["V11 capture cannot leave prepared without a commissioning_protocol"]
    required = {
        "recorded_at", "recorded_before_generation", "minimum_material_improvement",
        "reader_sample", "presentation", "answer_key",
    }
    missing = sorted(required - set(protocol))
    if missing:
        errors.append(f"V11 commissioning_protocol missing fields: {missing}")
    recorded_at = parse_timestamp(protocol.get("recorded_at"))
    if recorded_at is None:
        errors.append("V11 commissioning_protocol.recorded_at must be timezone-aware ISO-8601")
    elif prepared_at is not None and recorded_at > prepared_at:
        errors.append("V11 commissioning protocol must be recorded before generation preparation")
    if protocol.get("recorded_before_generation") is not True:
        errors.append("V11 commissioning protocol must affirm it was recorded before generation")
    improvement = protocol.get("minimum_material_improvement")
    requirements = fixture["scorer"].get("commissioning_requirements", {})
    if not isinstance(improvement, dict):
        errors.append("V11 commissioning protocol requires minimum_material_improvement")
    else:
        if improvement.get("metric") != requirements.get("metric"):
            errors.append("V11 commissioning metric does not match the fixture")
        if improvement.get("direction") != requirements.get("direction"):
            errors.append("V11 commissioning direction does not match the fixture")
        threshold = improvement.get("threshold")
        if isinstance(threshold, bool) or not isinstance(threshold, (int, float)) or not math.isfinite(threshold) or threshold <= 0:
            errors.append("V11 commissioning threshold must be a positive finite number supplied before generation")
    reader_sample = protocol.get("reader_sample")
    if not isinstance(reader_sample, dict):
        errors.append("V11 commissioning protocol requires reader_sample")
    else:
        if not nonempty_string(reader_sample.get("reader_profile")):
            errors.append("V11 reader_sample.reader_profile must be non-empty")
        if not isinstance(reader_sample.get("sample_size"), int) or reader_sample.get("sample_size", 0) < 1:
            errors.append("V11 reader_sample.sample_size must be a positive integer")
    presentation = protocol.get("presentation")
    if not isinstance(presentation, dict) or presentation.get("method") not in {"randomized", "counterbalanced"}:
        errors.append("V11 presentation.method must be randomized or counterbalanced")
    answer_key = protocol.get("answer_key")
    if not isinstance(answer_key, dict) or set(answer_key) != set(V11_ANSWER_FIELDS):
        errors.append(f"V11 answer_key must contain exactly {list(V11_ANSWER_FIELDS)}")
    elif any(not observable_evidence(answer_key[field]) for field in V11_ANSWER_FIELDS):
        errors.append("V11 answer_key fields must contain observable expected answers")
    return errors


def validate_trace(capture: dict[str, Any], fixture: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    trace = capture.get("observable_trace")
    if not isinstance(trace, list):
        return ["observable_trace must be a list"]
    if capture.get("status", {}).get("state") not in {"current", "product-contract-failure"} and not trace:
        return []
    required_fields = set(schema["trace_event_required_fields"])
    events_by_case: dict[str, list[dict[str, Any]]] = {}
    previous_sequence = 0
    for index, event in enumerate(trace):
        here = f"observable_trace[{index}]"
        if not isinstance(event, dict):
            errors.append(f"{here} must be an object")
            continue
        missing = sorted(required_fields - set(event))
        if missing:
            errors.append(f"{here} missing fields: {missing}")
            continue
        sequence = event.get("sequence")
        if not isinstance(sequence, int) or sequence <= previous_sequence:
            errors.append(f"{here}.sequence must be a strictly increasing integer")
        else:
            previous_sequence = sequence
        if event.get("run_id") != capture.get("trial_run_id"):
            errors.append(f"{here}.run_id must equal capture trial_run_id")
        for field in ("case_id", "event_type", "actor_id", "artifact_ref"):
            if not nonempty_string(event.get(field)):
                errors.append(f"{here}.{field} must be non-empty")
        if event.get("event_type") in set(schema["forbidden_private_fields"]):
            errors.append(f"{here}.event_type cannot record private reasoning")
        if parse_timestamp(event.get("timestamp")) is None:
            errors.append(f"{here}.timestamp must be timezone-aware ISO-8601")
        if not isinstance(event.get("details"), dict):
            errors.append(f"{here}.details must be an object")
        events_by_case.setdefault(event.get("case_id"), []).append(event)
    expected_ids = {case["case_id"] for case in fixture.get("trace_cases", [])}
    if set(events_by_case) != expected_ids:
        errors.append(f"observable_trace case IDs must be {sorted(expected_ids)}, got {sorted(str(value) for value in events_by_case)}")
    for case in fixture.get("trace_cases", []):
        case_id = case["case_id"]
        events = events_by_case.get(case_id, [])
        positions: dict[str, list[int]] = {}
        for event in events:
            positions.setdefault(event["event_type"], []).append(event["sequence"])
        for event_type in case["required_events"]:
            if event_type not in positions:
                errors.append(f"trace case {case_id} missing required event {event_type}")
        for event_type in case["forbidden_events"]:
            if event_type in positions:
                errors.append(f"trace case {case_id} contains forbidden event {event_type}")
        for earlier, later in case["ordered_pairs"]:
            if earlier in positions and later in positions and max(positions[earlier]) >= min(positions[later]):
                errors.append(f"trace case {case_id} event order invalid: {earlier} must precede {later}")
        if case["glossary_state"] == "selected" and "source_access" in positions:
            source_events = [event for event in events if event["event_type"] == "source_access"]
            if any(not event["details"].get("entries") for event in source_events):
                errors.append(f"trace case {case_id} source_access must list material entries")
    return errors


def validate_capture_record(
    capture: Any, manifest: dict[str, Any], schema: dict[str, Any], expected_skill_revision: str | None = None
) -> list[str]:
    errors: list[str] = []
    if not isinstance(capture, dict):
        return ["capture must be a JSON object"]
    missing = sorted(set(schema["required_fields"]) - set(capture))
    if missing:
        errors.append(f"capture missing required fields: {missing}")
    if capture.get("schema_version") != schema["schema_version"]:
        errors.append("capture schema_version does not match capture schema")
    if capture.get("record_type") != schema["record_type"]:
        errors.append("capture record_type does not match capture schema")
    fixture = fixture_map(manifest).get(capture.get("fixture_id"))
    if fixture is None:
        errors.append(f"capture fixture_id is unknown: {capture.get('fixture_id')!r}")
        return errors
    if capture.get("evidence_class") != fixture["evidence_class"]:
        errors.append("capture evidence_class does not match fixture")
    for field in ("trial_run_id", "skill_revision", "model_id", "runtime_id", "outer_instructions", "source_packet_hash"):
        if not nonempty_string(capture.get(field)):
            errors.append(f"capture {field} must be a non-empty string")
    if capture.get("source_packet_hash") != canonical_hash(fixture["source_packet"]):
        errors.append("capture source_packet_hash does not match the selected fixture")
    for field in ("generation_settings", "tool_context_configuration"):
        if not isinstance(capture.get(field), dict):
            errors.append(f"capture {field} must be a JSON object")
    if not isinstance(capture.get("trial_count"), int) or capture.get("trial_count", 0) < 1:
        errors.append("capture trial_count must be a positive integer")
    timestamps = capture.get("timestamps")
    if not isinstance(timestamps, dict):
        errors.append("capture timestamps must be an object")
        timestamps = {}
    prepared_at = parse_timestamp(timestamps.get("prepared_at"))
    completed_at = parse_timestamp(timestamps.get("completed_at"))
    if prepared_at is None:
        errors.append("capture timestamps.prepared_at must be timezone-aware ISO-8601")
    if prepared_at and completed_at and completed_at < prepared_at:
        errors.append("capture timestamps.completed_at cannot precede prepared_at")

    scorecard = capture.get("scorecard")
    if not isinstance(scorecard, dict):
        errors.append("capture scorecard must be an object")
        scorecard = {}
    else:
        absent = sorted(set(schema["scorecard_required_fields"]) - set(scorecard))
        if absent:
            errors.append(f"capture scorecard missing fields: {absent}")
    results = scorecard.get("criteria")
    if not isinstance(results, list):
        errors.append("capture scorecard.criteria must be a list")
        results = []
    expected_criteria = [item["id"] for item in fixture["scorer"]["criteria"]]
    actual_criteria = [item.get("criterion_id") for item in results if isinstance(item, dict)]
    if actual_criteria != expected_criteria:
        errors.append(f"capture scorecard criteria must be ordered as {expected_criteria}, got {actual_criteria}")
    for index, result in enumerate(results):
        if not isinstance(result, dict):
            errors.append(f"capture scorecard.criteria[{index}] must be an object")
            continue
        absent = sorted(set(schema["criterion_result_required_fields"]) - set(result))
        if absent:
            errors.append(f"capture scorecard.criteria[{index}] missing fields: {absent}")
        if result.get("passed") not in {True, False, None}:
            errors.append(f"capture scorecard.criteria[{index}].passed must be true, false, or null")

    status = capture.get("status")
    if not isinstance(status, dict):
        errors.append("capture status must be an object")
        status = {}
    state = status.get("state")
    rule = schema["status_rules"].get(state)
    if rule is None:
        errors.append(f"capture status.state is unknown: {state!r}")
    else:
        if state not in compatible_states(fixture["id"]):
            errors.append(f"capture status {state} is incompatible with {fixture_lane(fixture['id'])} fixture {fixture['id']}")
        if fixture["evidence_class"] not in rule["evidence_classes"]:
            errors.append(f"capture status {state} is incompatible with {fixture['evidence_class']} evidence")
        output_present = nonempty_string(capture.get("output"))
        if rule["requires_output"] and not output_present:
            errors.append(f"capture status {state} requires output to be non-empty")
        if not rule["requires_output"] and capture.get("output") is not None:
            errors.append(f"capture status {state} requires output to be null")
        if rule["requires_completed_at"] != (completed_at is not None):
            errors.append(f"capture status {state} requires completed_at to be {'present' if rule['requires_completed_at'] else 'null'}")
        if not rule["requires_completed_at"] and timestamps.get("completed_at") is not None:
            errors.append(f"capture status {state} requires completed_at to be null")
        decisions = [item.get("passed") for item in results if isinstance(item, dict)]
        overall = scorecard.get("overall_passed")
        if state in {"current", "product-contract-failure"}:
            for index, result in enumerate(results):
                if isinstance(result, dict) and not observable_evidence(result.get("evidence")):
                    errors.append(f"scored criterion {index} requires observable evidence recorded by the scorer")
        if state == "current":
            if overall is not True or not decisions or any(item is not True for item in decisions):
                errors.append("capture status current requires every criterion and overall_passed to be true")
            if scorecard.get("first_failed_contract") is not None or scorecard.get("first_failure_boundary") is not None:
                errors.append("capture status current cannot name a first failure")
            if expected_skill_revision and capture.get("skill_revision") != expected_skill_revision:
                errors.append("capture status current must identify the exact current skill revision")
        elif state == "product-contract-failure":
            if overall is not False or False not in decisions:
                errors.append("product-contract-failure requires a failed criterion and overall_passed false")
            if any(item not in {True, False} for item in decisions):
                errors.append("product-contract-failure requires every criterion to be scored")
            first_failed = next((index for index, value in enumerate(decisions) if value is False), None)
            if first_failed is not None:
                definition = fixture["scorer"]["criteria"][first_failed]
                if scorecard.get("first_failed_contract") != definition["contract_ids"][0]:
                    errors.append("product-contract-failure first_failed_contract does not match the first failed criterion")
                if scorecard.get("first_failure_boundary") != definition["failure_boundary"]:
                    errors.append("product-contract-failure first_failure_boundary does not match the first failed criterion")
        else:
            if overall is not None or any(item is not None for item in decisions):
                errors.append(f"capture status {state} cannot claim scored output")
            if scorecard.get("first_failed_contract") is not None or scorecard.get("first_failure_boundary") is not None:
                errors.append(f"capture status {state} cannot name a product-contract failure")
        failure_kinds = set(rule.get("failure_kinds", []))
        if failure_kinds and status.get("failure_kind") not in failure_kinds:
            errors.append(f"capture status {state} requires failure_kind in {sorted(failure_kinds)}")
        if not failure_kinds and status.get("failure_kind") is not None:
            errors.append(f"capture status {state} must not set failure_kind")

    errors.extend(validate_commissioning_protocol(capture, fixture, prepared_at))
    errors.extend(find_forbidden_keys(capture, set(schema["forbidden_private_fields"]), "capture"))
    if fixture["id"] in {"M7", "M8"}:
        errors.extend(validate_trace(capture, fixture, schema))
    elif not isinstance(capture.get("observable_trace"), list):
        errors.append("capture observable_trace must be a list")
    return errors


def default_output_path(fixture_id: str) -> Path:
    directory = Path(tempfile.gettempdir()) / "clear-technical-writing-captures"
    directory.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return directory / f"{fixture_id.lower()}-{timestamp}-{uuid.uuid4().hex[:8]}.json"


def prepare_capture(args: argparse.Namespace) -> int:
    skill_root = args.repo_root.resolve() / "skills/clear-technical-writing"
    try:
        manifest = load_json(skill_root / "evals/fixtures.json")
        schema = load_json(skill_root / "evals/capture.schema.json")
        fixture = fixture_map(manifest).get(args.fixture)
        if fixture is None:
            raise ValueError(f"unknown fixture {args.fixture!r}; choose one of {', '.join(sorted(fixture_map(manifest)))}")
        settings = parse_json_argument(args.settings_json, "--settings-json")
        tool_context = parse_json_argument(args.tool_context_json, "--tool-context-json")
        scores = None if args.scores_json is None else parse_json_argument(args.scores_json, "--scores-json")
        commissioning = None if args.commissioning_json is None else parse_json_argument(args.commissioning_json, "--commissioning-json")
        trace = [] if args.trace_file is None else load_json(args.trace_file)
        if not isinstance(trace, list):
            raise ValueError("--trace-file must contain a JSON list")
        revision = args.skill_revision or package_hash(skill_root)
        capture = build_capture(
            fixture, revision, args.model_id, args.runtime_id, args.outer_instructions,
            settings, tool_context, args.trial_count, args.status, args.output_text,
            scores, args.failure_kind, trace, commissioning,
        )
        capture_errors = validate_capture_record(capture, manifest, schema, package_hash(skill_root))
        if capture_errors:
            raise ValueError("capture arguments are inconsistent:\n  - " + "\n  - ".join(capture_errors))
        output_path = (args.output_path or default_output_path(args.fixture)).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(capture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        emit({"command": "prepare-capture", "status": "fail", "error": str(exc)})
        return 1
    emit({
        "command": "prepare-capture", "status": "pass", "capture_state": capture["status"]["state"],
        "fixture_id": fixture["id"], "output_path": str(output_path),
        "source_packet_hash": capture["source_packet_hash"],
        "capability_claim": "none-capture-preparation-does-not-aggregate-evidence",
    })
    return 0


def validate_capture_command(args: argparse.Namespace) -> int:
    skill_root = args.repo_root.resolve() / "skills/clear-technical-writing"
    try:
        manifest = load_json(skill_root / "evals/fixtures.json")
        schema = load_json(skill_root / "evals/capture.schema.json")
        capture = load_json(args.capture.resolve())
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        emit({"command": "validate-capture", "status": "fail", "errors": [str(exc)]})
        return 1
    errors = validate_capture_record(capture, manifest, schema, package_hash(skill_root))
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    emit({
        "command": "validate-capture", "status": "pass" if not errors else "fail",
        "capture": str(args.capture.resolve()), "fixture_id": capture.get("fixture_id"),
        "capture_state": capture.get("status", {}).get("state"),
        "capability_claim": "none-valid-record-does-not-confirm-or-aggregate-the-suite",
        "errors": errors,
    })
    return 1 if errors else 0


def synthetic_trace(fixture: dict[str, Any], run_id: str) -> list[dict[str, Any]]:
    trace: list[dict[str, Any]] = []
    sequence = 1
    for case in fixture.get("trace_cases", []):
        for event_type in case["required_events"]:
            if event_type in {"glossary_resolution", "dossier", "work_package", "assignment"}:
                actor = "coordinator"
            elif event_type in {"source_access", "review_handoff", "slice_handoff"}:
                actor = "fresh-reviewer" if fixture["id"] == "M7" else "persistent-implementer"
            elif event_type == "correction":
                actor = "fresh-reviewer" if fixture["id"] == "M7" else "supervising-parent"
            else:
                actor = "coordinator"
            details: dict[str, Any] = {"synthetic_self_test": True}
            if event_type == "source_access":
                details["entries"] = ["leaf owner", "semantic owner"]
            trace.append({
                "sequence": sequence, "case_id": case["case_id"], "event_type": event_type,
                "actor_id": actor, "run_id": run_id, "timestamp": utc_now(),
                "artifact_ref": f"synthetic://{fixture['id']}/{case['case_id']}/{event_type}",
                "details": details,
            })
            sequence += 1
    return trace


def scored_decisions(fixture: dict[str, Any]) -> dict[str, Any]:
    return {
        criterion["id"]: {
            "passed": True,
            "evidence": {"source": "synthetic structural self-test", "observable": criterion["observable_fields"]},
        }
        for criterion in fixture["scorer"]["criteria"]
    }


def synthetic_commissioning(fixture: dict[str, Any]) -> dict[str, Any]:
    source = fixture["source_packet"]
    requirements = fixture["scorer"]["commissioning_requirements"]
    return {
        "recorded_at": "2026-01-01T00:00:00Z",
        "recorded_before_generation": True,
        "minimum_material_improvement": {
            "metric": requirements["metric"], "direction": requirements["direction"], "threshold": 0.25,
        },
        "reader_sample": {"reader_profile": "synthetic schema test readers", "sample_size": 2},
        "presentation": {"method": "counterbalanced"},
        "answer_key": {field: source[field] for field in V11_ANSWER_FIELDS},
    }


def fully_scored_capture(fixture: dict[str, Any], revision: str) -> dict[str, Any]:
    capture = build_capture(
        fixture, revision, "synthetic-model", "synthetic-runtime",
        "Synthetic schema self-test; not external capability evidence.",
        {"synthetic": True}, {"synthetic": True}, 1, "current",
        "Synthetic observable output used only to validate record structure.",
        scored_decisions(fixture), commissioning_protocol=(
            synthetic_commissioning(fixture) if fixture_lane(fixture["id"]) == "V11" else None
        ),
    )
    if fixture["id"] in {"M7", "M8"}:
        capture["observable_trace"] = synthetic_trace(fixture, capture["trial_run_id"])
    return capture


def self_test(args: argparse.Namespace) -> int:
    skill_root = args.repo_root.resolve() / "skills/clear-technical-writing"
    try:
        manifest = load_json(skill_root / "evals/fixtures.json")
        schema = load_json(skill_root / "evals/capture.schema.json")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        emit({"command": "self-test", "status": "fail", "errors": [str(exc)]})
        return 1
    fixtures = fixture_map(manifest)
    results: dict[str, bool] = {}
    details: dict[str, list[str]] = {}
    revision = package_hash(skill_root)

    def record(name: str, errors: list[str], expected: str | None = None) -> None:
        results[name] = not errors if expected is None else any(expected in item for item in errors)
        details[name] = errors

    with tempfile.TemporaryDirectory(prefix="clear-writing-eval-self-test-") as temporary:
        temporary_root = Path(temporary)
        prepared = build_capture(
            fixtures["V1"], revision, "synthetic-model", "synthetic-runtime",
            "Synthetic preparation.", {}, {}, 1, "prepared",
        )
        record("prepared_capture", validate_capture_record(prepared, manifest, schema, revision))
        valid = fully_scored_capture(fixtures["V1"], revision)
        record("current_capture", validate_capture_record(valid, manifest, schema, revision))

        failed_scores = scored_decisions(fixtures["V1"])
        failed_scores["v1-preserve-finding"]["passed"] = False
        product_failure = build_capture(
            fixtures["V1"], revision, "synthetic-model", "synthetic-runtime",
            "Synthetic scored contradiction.", {}, {}, 1, "product-contract-failure",
            "Synthetic contradictory output.", failed_scores,
        )
        record("product_contract_failure_capture", validate_capture_record(product_failure, manifest, schema, revision))

        v_unconfirmed = build_capture(
            fixtures["V1"], revision, "synthetic-model", "synthetic-runtime",
            "Synthetic unavailable V trial.", {}, {}, 1, "model-capability-unconfirmed",
            failure_kind="inconclusive-timeout",
        )
        record("v_model_capability_unconfirmed", validate_capture_record(v_unconfirmed, manifest, schema, revision))

        m_unconfirmed = build_capture(
            fixtures["M1"], revision, "synthetic-model", "synthetic-runtime",
            "Synthetic unavailable M trial.", {}, {}, 1, "capability-unconfirmed",
            failure_kind="inconclusive-timeout",
        )
        record("m_capability_unconfirmed", validate_capture_record(m_unconfirmed, manifest, schema, revision))

        v11_unconfirmed = build_capture(
            fixtures["V11-GLOSSARY-PRESENT"], revision, "synthetic-model", "synthetic-runtime",
            "Synthetic unavailable human pilot.", {}, {}, 1, "human-comprehension-unconfirmed",
            failure_kind="missing-evaluators",
            commissioning_protocol=synthetic_commissioning(fixtures["V11-GLOSSARY-PRESENT"]),
        )
        record("v11_human_comprehension_unconfirmed", validate_capture_record(v11_unconfirmed, manifest, schema, revision))

        wording_variant = copy.deepcopy(manifest)
        fixture_map(wording_variant)["V1"]["artifact"] = {
            "assignment": "Express the same assigned review artifact using alternate words.",
            "intent": "Demonstrate structural validation without target-prose matching.",
        }
        record("wording_independent_fixture_variant", validate_fixtures(wording_variant))

        variant_root = temporary_root / "wording-independent-package"
        variant_references = variant_root / "references"
        variant_references.mkdir(parents=True)
        variant_targets = list(DECLARED_STRUCTURAL_LINKS["skills/clear-technical-writing/SKILL.md"])
        for target in variant_targets:
            (variant_root / target).write_text("# Alternate Reference\n\nDifferent explanatory wording.\n", encoding="utf-8")
        variant_entry = variant_root / "SKILL.md"
        variant_entry.write_text(
            "# Alternate Package Prose\n\n"
            + "\n".join(f"[Destination {index}]({target})" for index, target in enumerate(variant_targets, 1))
            + "\n",
            encoding="utf-8",
        )
        variant_errors, variant_link_count = relative_link_errors([variant_entry], temporary_root)
        if variant_link_count != len(variant_targets):
            variant_errors.append(
                f"wording-independent package variant exposed {variant_link_count} links, expected {len(variant_targets)}"
            )
        record("wording_independent_package_prose_variant", variant_errors)

        missing_identity = copy.deepcopy(valid)
        missing_identity.pop("model_id")
        record("missing_identity_rejected", validate_capture_record(missing_identity, manifest, schema, revision), "model_id")

        altered_manifest = copy.deepcopy(manifest)
        fixture_map(altered_manifest)["V6"]["source_packet"]["exact_boundaries"][0]["unit"] = "MB"
        record("altered_exact_boundary_rejected", validate_fixtures(altered_manifest), "16 MiB")

        contradictory = copy.deepcopy(valid)
        contradictory["scorecard"]["criteria"][0]["passed"] = False
        contradictory["scorecard"]["overall_passed"] = False
        record("contradictory_current_rejected", validate_capture_record(contradictory, manifest, schema, revision), "status current")

        wrong_v = copy.deepcopy(prepared)
        wrong_v["status"] = {"state": "capability-unconfirmed", "failure_kind": "inconclusive-timeout"}
        wrong_v["timestamps"]["completed_at"] = utc_now()
        record("wrong_v_state_rejected", validate_capture_record(wrong_v, manifest, schema, revision), "incompatible with V fixture")

        wrong_m = build_capture(
            fixtures["M1"], revision, "synthetic-model", "synthetic-runtime",
            "Synthetic unavailable trial.", {}, {}, 1, "model-capability-unconfirmed",
            failure_kind="inconclusive-timeout",
        )
        record("wrong_m_state_rejected", validate_capture_record(wrong_m, manifest, schema, revision), "incompatible with M fixture")

        missing_threshold = fully_scored_capture(fixtures["V11-GLOSSARY-PRESENT"], revision)
        del missing_threshold["commissioning_protocol"]["minimum_material_improvement"]["threshold"]
        record("v11_missing_threshold_rejected", validate_capture_record(missing_threshold, manifest, schema, revision), "threshold")

        for fixture_id in ("M7", "M8"):
            malformed = fully_scored_capture(fixtures[fixture_id], revision)
            first_case = fixtures[fixture_id]["trace_cases"][0]
            earlier, later = first_case["ordered_pairs"][2]
            events = [item for item in malformed["observable_trace"] if item["case_id"] == first_case["case_id"]]
            earlier_event = next(item for item in events if item["event_type"] == earlier)
            later_event = next(item for item in events if item["event_type"] == later)
            earlier_event["event_type"], later_event["event_type"] = later_event["event_type"], earlier_event["event_type"]
            record(
                f"malformed_{fixture_id.lower()}_order_rejected",
                validate_capture_record(malformed, manifest, schema, revision),
                "event order invalid",
            )
    failed = [name for name, passed in results.items() if not passed]
    for name in failed:
        print(f"error: self-test did not prove {name}: {details[name]}", file=sys.stderr)
    emit({
        "command": "self-test", "status": "pass" if not failed else "fail",
        "synthetic_cases": results, "temporary_output_retained": False,
        "capability_claim": "none-synthetic-structure-only",
    })
    return 1 if failed else 0


def build_parser() -> argparse.ArgumentParser:
    script_path = Path(__file__).resolve()
    default_repo = script_path.parents[3]
    parser = argparse.ArgumentParser(
        description=(
            "Validate V10 package mechanics, or prepare and validate observable external-evidence records. "
            "D1, D2, and V9 semantic ownership require independent source review."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""Examples:
  {script_path} --repo-root {default_repo} validate-package
  {script_path} --repo-root {default_repo} prepare-capture --fixture V1 \\
    --model-id MODEL --runtime-id RUNTIME --outer-instructions INSTRUCTIONS

Package validation proves mechanical conformance only. Scorers, not this helper,
decide natural-language criteria and record observable evidence. A valid current
record covers one commissioned fixture run; it does not confirm or aggregate the
capability suite. Exit codes: 0 success, 1 conformance failure, 2 usage error.""",
    )
    parser.add_argument("--repo-root", type=Path, default=default_repo, help=f"repository root (default: {default_repo})")
    subparsers = parser.add_subparsers(dest="command", required=True)

    package_parser = subparsers.add_parser("validate-package", help="run deterministic V10 mechanical checks")
    package_parser.add_argument(
        "--installed-skill", type=Path, default=Path.home() / ".agents/skills/clear-technical-writing",
        help="installed clear-writing skill symlink",
    )
    package_parser.add_argument(
        "--quick-validator", type=Path,
        default=Path.home() / ".codex/skills/.system/skill-creator/scripts/quick_validate.py",
        help="skill-creator quick_validate.py path",
    )
    package_parser.set_defaults(handler=validate_package)

    prepare_parser = subparsers.add_parser("prepare-capture", help="create a validated capture outside the repository by default")
    prepare_parser.add_argument("--fixture", required=True, help="fixture ID")
    prepare_parser.add_argument("--model-id", required=True, help="exact model identity")
    prepare_parser.add_argument("--runtime-id", required=True, help="exact runtime identity")
    prepare_parser.add_argument("--outer-instructions", required=True, help="complete outer trial instructions")
    prepare_parser.add_argument("--skill-revision", help="exact skill revision; defaults to package SHA-256")
    prepare_parser.add_argument("--settings-json", default="{}", help="exposed generation settings JSON object")
    prepare_parser.add_argument("--tool-context-json", default="{}", help="tool and context configuration JSON object")
    prepare_parser.add_argument("--commissioning-json", help="V11 pre-generation commissioning protocol JSON object")
    prepare_parser.add_argument("--trial-count", type=int, default=1, help="positive trial count")
    prepare_parser.add_argument(
        "--status", default="prepared",
        choices=[
            "prepared", "current", "product-contract-failure", "model-capability-unconfirmed",
            "capability-unconfirmed", "human-comprehension-unconfirmed",
        ],
    )
    prepare_parser.add_argument("--failure-kind", help="external unavailability classification")
    prepare_parser.add_argument("--output-text", help="observable generated output")
    prepare_parser.add_argument("--scores-json", help="criterion ID to {passed,evidence} scorer record JSON")
    prepare_parser.add_argument("--trace-file", type=Path, help="M7/M8 ordered observable trace JSON list")
    prepare_parser.add_argument("--output-path", type=Path, help="capture path; defaults under the system temporary directory")
    prepare_parser.set_defaults(handler=prepare_capture)

    capture_parser = subparsers.add_parser(
        "validate-capture", help="validate capture identity, scorer completeness, status, commissioning, and trace consistency"
    )
    capture_parser.add_argument("capture", type=Path, help="capture JSON file")
    capture_parser.set_defaults(handler=validate_capture_command)
    self_test_parser = subparsers.add_parser("self-test", help="exercise valid and adjacent invalid structural cases in a temporary directory")
    self_test_parser.set_defaults(handler=self_test)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.handler(args)
    except OSError as exc:
        print(f"error: filesystem or process failure: {exc}", file=sys.stderr)
        emit({"command": args.command, "status": "fail", "error": str(exc)})
        return 1


if __name__ == "__main__":
    sys.exit(main())

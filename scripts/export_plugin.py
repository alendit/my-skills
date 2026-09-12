#!/usr/bin/env python3
"""Export a closed, revision-pinned my-skills plugin from this repository."""

import argparse
import hashlib
import json
import posixpath
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def git(repository, *args):
    return subprocess.check_output(
        ["git", "-C", str(repository), *args], text=True
    ).strip()


def git_bytes(repository, revision, path):
    return subprocess.check_output(
        ["git", "-C", str(repository), "show", f"{revision}:{path}"]
    )


def normalize_link(source, target):
    target = unquote(target.strip().strip("<>"))
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target or target.startswith(("#", "/", "mailto:")) or "://" in target:
        return None
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), target))
    if resolved == ".." or resolved.startswith("../"):
        raise ValueError(f"Reference escapes repository: {source}: {target}")
    return resolved


def tracked_files(repository, revision):
    return set(git(repository, "ls-tree", "-r", "--name-only", revision).splitlines())


def package_files(repository, revision):
    available = tracked_files(repository, revision)
    selected = {path for path in available if path.startswith("skills/")}
    if not selected:
        raise ValueError("Revision contains no skills")
    selected.update(path for path in available if path.startswith("hooks/"))

    pending = [path for path in selected if path.endswith(".md")]
    inspected = set()
    while pending:
        source = pending.pop()
        if source in inspected:
            continue
        inspected.add(source)
        text = git_bytes(repository, revision, source).decode("utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = normalize_link(source, raw_target)
            if target is None:
                continue
            if target not in available:
                raise ValueError(f"Unresolved package reference: {source}: {raw_target}")
            if target not in selected:
                selected.add(target)
                if target.endswith(".md"):
                    pending.append(target)
    return selected


def inventory(directory):
    return {
        str(path.relative_to(directory)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(directory.rglob("*"))
        if path.is_file() and path.name != "build-manifest.json"
    }


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def publish_directory(staging, destination):
    try:
        destination.mkdir()
    except FileExistsError as error:
        raise ValueError(f"Destination must not exist: {destination}") from error
    try:
        for child in staging.iterdir():
            shutil.move(str(child), destination / child.name)
    except Exception:
        shutil.rmtree(destination)
        raise


def build(repository, destination, revision="HEAD"):
    repository = Path(repository).resolve()
    requested_destination = Path(destination).absolute()
    if requested_destination.exists() or requested_destination.is_symlink():
        raise ValueError(f"Destination must not exist: {requested_destination}")
    destination = requested_destination.resolve()
    commit = git(repository, "rev-parse", f"{revision}^{{commit}}")
    files = package_files(repository, commit)
    manifest_path = ".codex-plugin/plugin.json"
    if manifest_path not in tracked_files(repository, commit):
        raise ValueError(f"Revision lacks {manifest_path}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".my-skills-export-", dir=destination.parent
    ) as temporary:
        staging = Path(temporary) / "my-skills"
        staging.mkdir()
        for relative in sorted(files):
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(git_bytes(repository, commit, relative))

        manifest = json.loads(git_bytes(repository, commit, manifest_path))
        base_version = manifest["version"].split("+", 1)[0]
        manifest["version"] = f"{base_version}+codex.{commit[:12]}"
        write_json(staging / manifest_path, manifest)
        (staging / "SOURCE_REVISION").write_text(
            f"source=my-skills\nrevision={commit}\n"
        )
        write_json(
            staging / "build-manifest.json",
            {
                "source_revision": commit,
                "source_kind": "immutable_git_tree",
                "files_sha256": inventory(staging),
            },
        )
        publish_directory(staging, destination)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="new output directory")
    parser.add_argument("--revision", default="HEAD", help="committed revision to export")
    parser.add_argument("--repository", type=Path, default=ROOT, help="source repository")
    args = parser.parse_args()
    try:
        print(build(args.repository, args.destination, args.revision))
    except (ValueError, OSError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        parser.exit(1, f"Export failed: {error}\n")


if __name__ == "__main__":
    main()

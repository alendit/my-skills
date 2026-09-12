import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "export_plugin", ROOT / "scripts" / "export_plugin.py"
)
EXPORT_PLUGIN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPORT_PLUGIN)


def run(repository, *args):
    subprocess.run(
        ["git", "-C", str(repository), *args], check=True, capture_output=True
    )


def make_repository(root, broken=False):
    repository = root / "source"
    (repository / ".codex-plugin").mkdir(parents=True)
    (repository / "skills" / "one" / "references").mkdir(parents=True)
    (repository / "docs" / "evidence").mkdir(parents=True)
    (repository / ".codex-plugin" / "plugin.json").write_text(
        json.dumps({"name": "my-skills", "version": "0.1.0", "skills": "./skills/"})
    )
    link = "references/missing.md" if broken else "references/detail.md"
    (repository / "skills" / "one" / "SKILL.md").write_text(
        f"---\nname: one\ndescription: Test skill.\n---\n\n[detail]({link})\n"
    )
    (repository / "skills" / "one" / "references" / "detail.md").write_text(
        "[evidence](../../../docs/evidence/source.md)\n"
    )
    (repository / "docs" / "evidence" / "source.md").write_text("evidence\n")
    run(repository.parent, "init", str(repository))
    run(repository, "config", "user.email", "test@example.com")
    run(repository, "config", "user.name", "Test")
    run(repository, "add", ".")
    run(repository, "commit", "-m", "fixture")
    return repository


class PluginExportTests(unittest.TestCase):
    def test_exported_session_hook_runs_without_repository_or_working_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repository = make_repository(root)
            shutil.copytree(ROOT / "hooks", repository / "hooks")
            run(repository, "add", "hooks")
            run(repository, "commit", "-m", "bundle session hook")
            destination = root / "installed plugin with spaces"
            EXPORT_PLUGIN.build(repository, destination)
            shutil.rmtree(repository)

            config = json.loads((destination / "hooks/hooks.json").read_text())
            handler = config["hooks"]["SessionStart"][0]["hooks"][0]
            result = subprocess.run(
                ["/bin/sh", "-c", handler["command"]],
                env={**os.environ, "PLUGIN_ROOT": str(destination)},
                cwd=root,
                input='{"hook_event_name":"SessionStart","source":"startup"}',
                text=True, capture_output=True, check=True,
                timeout=handler["timeout"],
            )
            output = json.loads(result.stdout)["hookSpecificOutput"]
            self.assertEqual(output["hookEventName"], "SessionStart")
            self.assertTrue(output["additionalContext"].strip())
            self.assertEqual(result.stderr, "")
            manifest = json.loads((destination / "build-manifest.json").read_text())
            self.assertEqual(manifest["files_sha256"], EXPORT_PLUGIN.inventory(destination))

    def test_exports_closed_revision_with_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repository = make_repository(root)
            destination = root / "output" / "my-skills"
            EXPORT_PLUGIN.build(repository, destination)

            source_revision = EXPORT_PLUGIN.git(repository, "rev-parse", "HEAD")
            manifest = json.loads(
                (destination / ".codex-plugin" / "plugin.json").read_text()
            )
            build_manifest = json.loads(
                (destination / "build-manifest.json").read_text()
            )

            self.assertEqual(manifest["version"], f"0.1.0+codex.{source_revision[:12]}")
            self.assertIn(
                "docs/evidence/source.md", build_manifest["files_sha256"]
            )
            self.assertIn(
                f"revision={source_revision}",
                (destination / "SOURCE_REVISION").read_text(),
            )
            self.assertNotIn(
                str(repository), (destination / "SOURCE_REVISION").read_text()
            )

    def test_rejects_unresolved_reference_without_creating_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repository = make_repository(root, broken=True)
            destination = root / "my-skills"

            with self.assertRaisesRegex(ValueError, "Unresolved package reference"):
                EXPORT_PLUGIN.build(repository, destination)

            self.assertFalse(destination.exists())

    def test_refuses_existing_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repository = make_repository(root)
            destination = root / "my-skills"
            destination.mkdir()

            with self.assertRaisesRegex(ValueError, "Destination must not exist"):
                EXPORT_PLUGIN.build(repository, destination)

    def test_refuses_dangling_destination_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repository = make_repository(root)
            destination = root / "my-skills"
            destination.symlink_to(root / "missing")

            with self.assertRaisesRegex(ValueError, "Destination must not exist"):
                EXPORT_PLUGIN.build(repository, destination)

    def test_publish_refuses_destination_created_after_staging(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            staging = root / "staging"
            destination = root / "my-skills"
            staging.mkdir()
            (staging / "new").write_text("new\n")
            destination.mkdir()
            (destination / "existing").write_text("existing\n")

            with self.assertRaisesRegex(ValueError, "Destination must not exist"):
                EXPORT_PLUGIN.publish_directory(staging, destination)

            self.assertEqual((destination / "existing").read_text(), "existing\n")
            self.assertFalse((destination / "new").exists())


if __name__ == "__main__":
    unittest.main()

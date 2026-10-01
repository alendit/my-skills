# My Skills

Reusable engineering workflows packaged as a Codex plugin with eight skills,
a bundled implementer role, and a session hook. The plugin registers no MCP
server or additional tools; one Codex configuration entry makes the role
available for spawning.

## Build

Export an immutable committed revision to a new directory:

```sh
python3 scripts/export_plugin.py /tmp/my-skills --revision HEAD
```

The exporter includes all eight skills, their transitive repository-local
Markdown references, and the bundled hooks. It rejects unresolved or escaping
references and existing destinations. `SOURCE_REVISION` records the exact commit;
`build-manifest.json`
records hashes for the exported files. The exported plugin version includes the
source commit as its Codex cache key.

Set the bundled plugin-creator skill location for the commands below:

```sh
PLUGIN_CREATOR_ROOT="${CODEX_HOME:-$HOME/.codex}/skills/.system/plugin-creator"
```

Validate the staged package before replacing an installed source:

```sh
uv run --with pyyaml python \
  "$PLUGIN_CREATOR_ROOT/scripts/validate_plugin.py" /tmp/my-skills
```

For an initial personal-marketplace installation, first create the standard
`my-skills` entry and source location:

```sh
python3 "$PLUGIN_CREATOR_ROOT/scripts/create_basic_plugin.py" \
  my-skills --with-skills --with-marketplace
```

Preserve the generated source recoverably, then put the validated staged export
at that exact source location. Do not hand-edit `marketplace.json`.

For an update, read the configured personal marketplace name and refresh the
staged package's cache key through the supported helpers:

```sh
python3 "$PLUGIN_CREATOR_ROOT/scripts/read_marketplace_name.py"
python3 "$PLUGIN_CREATOR_ROOT/scripts/update_plugin_cachebuster.py" \
  /tmp/my-skills
uv run --with pyyaml python \
  "$PLUGIN_CREATOR_ROOT/scripts/validate_plugin.py" /tmp/my-skills
```

Confirm that the marketplace entry resolves to the source being updated.
Inventory and move the current `my-skills` source to a recoverable backup, then
move the complete validated export into its place. Replace only that plugin
directory. Reinstall using the marketplace name printed above:

```sh
codex plugin add my-skills@<marketplace-name> --json
```

Verify discovery and installation with:

```sh
codex plugin list --marketplace <marketplace-name> --json
```

Read back the installed/cache manifest, `SOURCE_REVISION`, eight-skill inventory,
and `build-manifest.json` hashes. The cachebuster changes the exported manifest
version after `build-manifest.json` was produced, so account for that one expected
hash difference or regenerate the staged build manifest before comparing.
Verify that the [role registration](#codex-implementer-role) still points to the
bundled file in the updated source. Start a fresh Codex thread so the new catalog
and role configuration are loaded.

## Codex Delegated Waits

Codex discovers [hooks/hooks.json](hooks/hooks.json) automatically when the plugin
and hooks feature are enabled. Its synchronous `SessionStart` command emits a
static `additionalContext` payload, which Codex inserts as a developer message.
This supplies a scoped exception to the default 60-second commentary and wait
guidance while awaiting an active implementer, reviewer, or long-running
verification command. Agree on milestones and a stall deadline, then choose a
generous timeout within runtime limits. Keep routine process polling inside the
executor or an existing cheaper capable worker; a persistent exec cell still
causes model turns when recurring status output or short observation windows
return control to the model. Completion and material decisions wake the parent.

The hook reads only its bundled payload; it adds no tool, network request, or
global instruction file. It runs at session lifecycle boundaries, including
resume and compaction, rather than every turn or tool call. Start a fresh thread
after installing. Check hook discovery and successful `SessionStart` execution
if the exception is absent; skill text alone cannot override developer rules.
Disabling the plugin disables this hook.

## Codex Implementer Role

The bundled [implementer role](skills/supervised-implementer-loop/assets/implementer.toml)
uses GPT-6 Luna Max for bounded code packages. Its execution instructions live
in that single file; the parent workflow owns assignment, acceptance, and
lifecycle.
Within authorized work, initial spawning and same-configuration respawning need
no additional user confirmation. Explicit identity restrictions still apply.

Register the bundled file directly in `$CODEX_HOME/config.toml` (normally
`~/.codex/config.toml`). For the standard source at `~/plugins/my-skills`:

```toml
[agents.implementer]
config_file = "../plugins/my-skills/skills/supervised-implementer-loop/assets/implementer.toml"
```

The path resolves relative to the configuration directory; adjust it to the
verified marketplace source when either location differs. Point to the stable
source directory, whose contents plugin updates replace, rather than a versioned
cache. Codex reads the name, description, model, and instructions from that file.
No separate role copy or symlink is needed.

When migrating an earlier installation, inspect and move the old
`~/.codex/agents/implementer.toml` outside agent discovery, preserving any local
customizations before replacing them. Verify that the registration resolves to
the bundled regular file and start a fresh Codex session. A symlink at the role
file itself is rejected at spawn time. Remove the registration when retiring the
role; disabling the plugin alone does not remove a configured agent.

The parent selects `agent_type: "implementer"` and explicitly sets
`fork_turns: "none"` for every spawn and respawn. The self-contained assignment
supplies task context; later messages carry only deltas to the same child. The
spawn default is a full history fork, so leaving the parameter out would copy
the parent conversation. The implementer appends checkpoints and the `DONE`
record to the shared progress log. It messages the parent's inbox only for a
decision or blocker; its final response is the completion notice.

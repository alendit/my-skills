# My Skills

Reusable engineering workflow skills packaged as a skills-only Codex plugin.
The plugin registers no MCP server or additional tools. It also carries an
implementer role that is installed separately into Codex's agent directory.

## Build

Export an immutable committed revision to a new directory:

```sh
python3 scripts/export_plugin.py /tmp/my-skills --revision HEAD
```

The exporter includes all eight skills and their transitive repository-local
Markdown references. It rejects unresolved or escaping references and existing
destinations. `SOURCE_REVISION` records the exact commit; `build-manifest.json`
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
hash difference or regenerate the staged build manifest before comparing. Start
a fresh Codex thread so the new catalog is loaded.

## Codex Implementer Role

The bundled [implementer role](skills/supervised-implementer-loop/assets/implementer.toml)
uses Luna Max for bounded code packages. Its execution instructions live in that
single file; the parent workflow owns assignment, acceptance, and lifecycle.
Within authorized work, initial spawning and same-configuration respawning need
no additional user confirmation. Explicit identity restrictions still apply.

After installing the plugin, link the role from the stable marketplace source
directory into Codex's personal agents directory. Set `PLUGIN_SOURCE_ROOT` to the
source path verified above; the standard personal location is shown here:

```sh
PLUGIN_SOURCE_ROOT="$HOME/plugins/my-skills"
mkdir -p "${CODEX_HOME:-$HOME/.codex}/agents"
ln -s "$PLUGIN_SOURCE_ROOT/skills/supervised-implementer-loop/assets/implementer.toml" \
  "${CODEX_HOME:-$HOME/.codex}/agents/implementer.toml"
```

Inspect an existing destination before replacing it; keep a matching link.
The link follows future complete source replacements, so ordinary plugin updates
also update this role without copying instructions or linking to a versioned
cache. Verify that the link resolves to the exported role, then start a fresh
Codex session. Plugin installation alone does not register custom agents.
Remove this link when retiring the role; disabling the plugin alone does not
disable a separately installed personal agent.

The parent selects `agent_type: "implementer"` and explicitly sets
`fork_turns: "none"` for every spawn and respawn. The self-contained assignment
supplies task context; later messages carry only deltas to the same child. The
spawn default is a full history fork, so leaving the parameter out would copy
the parent conversation. See [implementer selection](skills/supervised-implementer-loop/references/implementer-continuity.md#select-the-implementer)
for the same-configuration fallback when a session has not loaded the role yet.

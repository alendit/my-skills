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
hash difference or regenerate the staged build manifest before comparing.
If the implementer role is installed, refresh its regular-file copy using the
[role installation procedure](#codex-implementer-role). Start a fresh Codex thread
so the new catalog is loaded.

## Codex Implementer Role

The bundled [implementer role](skills/supervised-implementer-loop/assets/implementer.toml)
uses Luna Max for bounded code packages. Its execution instructions live in that
single file; the parent workflow owns assignment, acceptance, and lifecycle.
Within authorized work, initial spawning and same-configuration respawning need
no additional user confirmation. Explicit identity restrictions still apply.

After installing or updating the plugin, copy the role from the verified source
into Codex's personal agents directory as a **regular file**. Codex can advertise
a symlinked role, but its spawn-time reader rejects the link with
`agent type is currently not available` (the underlying macOS error is
`Too many levels of symbolic links`).

Inspect an existing destination before replacing it. Move an old symlink or
locally modified role to a recoverable backup outside the agents directory;
preserve local customizations deliberately. Set `PLUGIN_SOURCE_ROOT` to the
source path verified above; the standard personal location is shown here:

```sh
PLUGIN_SOURCE_ROOT="$HOME/plugins/my-skills"
ROLE_DESTINATION="${CODEX_HOME:-$HOME/.codex}/agents/implementer.toml"
mkdir -p "${CODEX_HOME:-$HOME/.codex}/agents"
test ! -L "$ROLE_DESTINATION" &&
  cp "$PLUGIN_SOURCE_ROOT/skills/supervised-implementer-loop/assets/implementer.toml" \
    "$ROLE_DESTINATION"
test -f "$ROLE_DESTINATION" && test ! -L "$ROLE_DESTINATION" &&
  cmp "$PLUGIN_SOURCE_ROOT/skills/supervised-implementer-loop/assets/implementer.toml" \
    "$ROLE_DESTINATION"
```

The bundled file remains the maintained source; repeat the copy and comparison
on plugin updates. Start a fresh Codex session after installation. Plugin
installation alone does not register custom agents, and disabling the plugin
does not disable this separately installed personal agent. Remove the installed
copy when retiring the role.

The parent selects `agent_type: "implementer"` and explicitly sets
`fork_turns: "none"` for every spawn and respawn. The self-contained assignment
supplies task context; later messages carry only deltas to the same child. The
spawn default is a full history fork, so leaving the parameter out would copy
the parent conversation. See [implementer selection](skills/supervised-implementer-loop/references/implementer-continuity.md#select-the-implementer)
for the same-configuration fallback when a session has not loaded the role yet.

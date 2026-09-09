# Implementer Continuity

The semantic MCP owns implementation context reuse and normal execution
continuation. The parent carries the opaque context identity, current state,
and any caller-required model, reasoning, execution mode, or identity constraint.
Use [the semantic operation contract](semantic-operation.md) for tool behavior.

Calls, design-blocker responses, local repairs, and acceptance corrections reuse
the exact backend thread. Later slices can continue in that context. Its current
accepted specification outranks remembered assumptions. Persistent slice context
does not expand the current edit's authority; the parent still selects the next
edit and retains integration reasoning. The runtime retains
concrete discoveries and evidence; the parent does not replay logs, verify a
turnover envelope, or operate an implementation-agent mailbox.

The initial backend relies on the coding harness's normal compaction while
retaining thread identity. It does not automatically replace a lost context.
If the thread is unavailable or continuation cannot preserve the authorized
configuration, return a failure and preserve partial work. A replacement needs
a concrete recovery decision and any required caller authorization; do not
silently start a new identity and claim continuity.

For an interrupted operation, establish that its writer has stopped and recover
its recorded mutation state before continuing. The runtime serializes writers
and refuses ambiguous replay. The parent intervenes only for missing authority,
a semantic rebaseline, or recovery evidence that the runtime cannot establish.
Ordinary timeouts are not requests for another agent or repeated status turns.
For cancellation or steering, follow the semantic contract's active-edit control
path. Stopping a caller wait or acknowledging interruption does not cancel an
active backend writer.

Acceptance belongs to the slice boundary. Context compaction, transport
reconnection, or a successfully completed operation does not accept a slice,
create a new package, or start an independent review phase.

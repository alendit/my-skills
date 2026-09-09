"""Host-bound stdio entrypoint. Configuration is never supplied by an MCP caller."""
import argparse
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from .runtime import Config, Runtime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', default=os.environ.get('SEMANTIC_EDIT_REPOSITORY'))
    parser.add_argument('--state-dir', default=os.environ.get('SEMANTIC_EDIT_STATE_DIR'))
    parser.add_argument('--codex', default=os.environ.get('SEMANTIC_EDIT_CODEX', 'codex'))
    parser.add_argument('--model', default=os.environ.get('SEMANTIC_EDIT_MODEL', 'gpt-5.6-luna'))
    parser.add_argument('--reasoning-effort', default=os.environ.get('SEMANTIC_EDIT_REASONING_EFFORT', 'high'))
    parser.add_argument('--timeout-seconds', type=float, default=float(os.environ.get('SEMANTIC_EDIT_TIMEOUT_SECONDS', '1800')))
    args = parser.parse_args()
    if not args.repository or not args.state_dir:
        parser.error('--repository and --state-dir (or corresponding SEMANTIC_EDIT_* environment variables) are required')
    if args.timeout_seconds <= 0:
        parser.error('timeout-seconds must be positive')
    runtime = Runtime(Config(Path(args.repository), Path(args.state_dir), args.codex,
                             args.model, args.reasoning_effort, args.timeout_seconds))
    server = FastMCP('semantic-edit')
    server.add_tool(runtime.realize_change, description=(
        'Apply one specific edit selected by the parent; the parent sequences and integrates the slice. '
        'Specify the owner, behavior, constraints and local completion condition. Slice contracts constrain this edit; do not finish remaining slice work. '
        'Returns APPLIED, BLOCKED or FAILED with compact evidence, context_id and result_state. '
        'For the next edit, use a new request_id and reuse context_id/result_state as expected_state; '
        'an identical retry retrieves the original operation.'))
    server.add_tool(runtime.inspect_semantics, description=(
        'Answer one bounded question about existing behavior, interfaces, ownership or failure paths. '
        'Uses a fresh read-only context; returns source-referenced facts, uncertainty and inspected_state. '
        'Supply expected_state when the answer must describe a specific worktree state. '
        'Requires a settled worktree; supplies evidence, not slice acceptance.'))
    server.add_tool(runtime.operation_status, description=(
        'Retrieve an edit result by request_id after a lost response or cancellation request, without re-execution. '
        'UNKNOWN means running or interrupted, not unchanged; observed_state is available only when the worktree lock is free. '
        'Does not cancel or acknowledge interruption.'))
    server.add_tool(runtime.cancel_change, description=(
        'Request that this server stop an active edit by request_id, preserving partial work without rollback. '
        'requested is not stopped: await the edit result or use operation_status for settlement. '
        'settled returns the recorded result and context_resumable; unavailable means this server cannot control it. '
        'To change direction, cancel, establish settlement, then realize one corrected edit with a new request_id.'))
    server.add_tool(runtime.acknowledge_interruption, description=(
        'Finalize an interrupted edit as FAILED after its writer has stopped. '
        'Use only for unresolved status with a current observed_state passed as expected_state. '
        'Checks writer exclusion and state, preserves partial work, and never cancels, rolls back or replays execution.'))
    server.add_tool(runtime.slice_summary, description=(
        'Collect accumulated edit outcomes and evidence for independent acceptance of a completed slice. '
        'Requires context_id and slice_id; returns current result_state and whether the packet is stale. '
        'Historical failures may be resolved by later edits. Does not inspect code or accept the slice.'))
    server.run(transport='stdio')


if __name__ == '__main__':
    main()

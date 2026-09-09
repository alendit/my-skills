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
    server.add_tool(runtime.realize_change, description='Realize one specific parent-selected edit using a persistent implementation context. Complete slice context is background, not authority to finish the slice. Trust compact results between calls; independently accept at the slice boundary. Retries must reuse the exact request_id and payload.')
    server.add_tool(runtime.operation_status, description='Recover a known request result without replaying implementation.')
    server.add_tool(runtime.slice_summary, description='Aggregate operation summaries and evidence for independent slice acceptance.')
    server.add_tool(runtime.acknowledge_interruption, description='Acknowledge an interrupted request at a known current state. Requires no active writer. Records partial work as FAILED and never replays it.')
    server.add_tool(runtime.cancel_change, description='Request cancellation of an active edit by request_id. Requested is not stopped: use the recorded operation result for settlement, exact state and preserved partial work. No rollback.')
    server.add_tool(runtime.steer_change, description='Record a bounded correction to an active edit. The CLI backend returns requires_stop_and_resume, never in-flight applied: cancel, establish settlement, then submit a new bounded request. control_id retries are immutable.')
    server.add_tool(runtime.inspect_semantics, description='Read-only semantic inspection in a fresh context. Answer one bounded code question with source-grounded facts, inspected state and uncertainty. No edits or acceptance authority.')
    server.run(transport='stdio')


if __name__ == '__main__':
    main()

"""Optional live compatibility probe; creates only a temporary fixture and evidence."""
import argparse
import asyncio
from datetime import timedelta
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run(model):
    root = Path(tempfile.mkdtemp(prefix='semantic-mcp-live-'))
    repo = root / 'repo'
    repo.mkdir()
    subprocess.run(['git', 'init', '-q', str(repo)], check=True)
    (repo / 'AGENTS.md').write_text('This is a disposable Python fixture. Use standard library checks. Do not commit.\n')
    params = StdioServerParameters(command=sys.executable, args=[
        '-m', 'semantic_edit_mcp.server', '--repository', str(repo),
        '--state-dir', str(root / 'state'), '--model', model, '--timeout-seconds', '300'])
    results = []
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=timedelta(seconds=360)) as session:
            await session.initialize()
            async def call(request):
                response = await session.call_tool('realize_change', request)
                if response.isError:
                    raise RuntimeError(response.content)
                result = response.structuredContent
                if result is None:
                    result = json.loads(response.content[0].text)
                results.append(result)
                (root / 'results.json').write_text(json.dumps(results, indent=2))
                print(json.dumps({k: result.get(k) for k in ('request_id', 'status', 'summary', 'context_id', 'mutation')}), flush=True)
                return result
            first = await call({'request_id': 'live-1', 'slice_id': 'arithmetic',
                'specification': 'Create arithmetic.py with double(x) returning x * 2. Add standard-library unittest coverage of zero, positive and negative integers. Run it. Only arithmetic.py and test_arithmetic.py may change.'})
            assert first['status'] == 'APPLIED', first
            blocked = await call({'request_id': 'live-2', 'slice_id': 'arithmetic',
                'context_id': first['context_id'], 'expected_state': first['result_state'],
                'specification': 'Extend double to consult the existing authoritative ScalingRepository before computing. Repository ownership must be preserved; do not invent a ScalingRepository or its semantics. If this fixture has no such owner, return BLOCKED without edits and identify the missing design decision.'})
            assert blocked['status'] == 'BLOCKED', blocked
            final = await call({'request_id': 'live-3', 'slice_id': 'arithmetic',
                'context_id': first['context_id'], 'expected_state': blocked['result_state'],
                'specification': 'Design correction: no repository lookup is required. Preserve double(x). Add quadruple(x) using double(double(x)). Extend unittest coverage of zero, positive and negative integers and run it. Only arithmetic.py and test_arithmetic.py may change.'})
            assert final['status'] == 'APPLIED', final
            packet = await session.call_tool('slice_summary', {'context_id': first['context_id'], 'slice_id': 'arithmetic'})
            assert not packet.isError
            (root / 'packet.json').write_text(packet.model_dump_json(indent=2))
    # Independent checks happen only now, at the accumulated slice boundary.
    checked = subprocess.run([sys.executable, '-c',
        'import arithmetic; assert all(arithmetic.double(x)==2*x and arithmetic.quadruple(x)==4*x for x in range(-17,18))'], cwd=repo)
    assert checked.returncode == 0
    assert (repo / 'AGENTS.md').read_text() == 'This is a disposable Python fixture. Use standard library checks. Do not commit.\n'
    assert len({item['context_id'] for item in results}) == 1
    print(f'Live MCP composition and independent slice acceptance passed. Evidence: {root}', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', default='gpt-5.6-luna')
    asyncio.run(run(parser.parse_args().model))

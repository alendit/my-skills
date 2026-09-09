import asyncio, json, subprocess, tempfile
from pathlib import Path
from semantic_edit_mcp.runtime import Runtime, Config
async def main():
    root=Path(tempfile.mkdtemp(prefix='semantic-inspection-live-'))
    repo=root/'repo'; repo.mkdir()
    subprocess.run(['git','init','-q',str(repo)],check=True)
    (repo/'arithmetic.py').write_text('def double(value):\n    return value * 2\n')
    runtime=Runtime(Config(repo,root/'state',timeout_seconds=180))
    before=runtime.snapshot()['identity']
    result=await runtime.inspect_semantics('What does double return, and does it mutate its argument? Cite arithmetic.py and identify any uncertainty about arbitrary input types.',before)
    assert result['inspected_state']==before and result['mutation']=='unchanged'
    assert result['facts']
    print(json.dumps({'evidence':str(root),'result':result},indent=2))
asyncio.run(main())

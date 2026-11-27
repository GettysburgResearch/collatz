"""Run the paired modules without network access. Supply Lean and mathlib roots."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--lean',required=True,type=Path)
    p.add_argument('--mathlib',required=True,type=Path)
    p.add_argument('modules',nargs='*',default=['FirstExit.lean','ShiftBalance.lean','AllShift.lean'])
    a=p.parse_args()
    root=Path(__file__).resolve().parent
    m=a.mathlib.resolve()
    paths=[m/'.lake/build/lib/lean',*(x/'.lake/build/lib/lean' for x in (m/'.lake/packages').iterdir())]
    env=dict(os.environ,LEAN_PATH=os.pathsep.join(str(x) for x in paths))
    for name in a.modules:
        cmd=[str(a.lean.resolve()),'-j1','-DElab.async=false','-DwarningAsError=true',name]
        print('checking',name, flush=True)
        result=subprocess.run(cmd,cwd=root,env=env)
        if result.returncode:
            return result.returncode
    return 0
if __name__=='__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Replay the phase-two module chain using a populated pinned mathlib cache."""
from pathlib import Path
import argparse
import os
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def checked(command, **kwargs):
    return subprocess.run(command, check=True, text=True, **kwargs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True, type=Path)
    parser.add_argument("--mathlib", required=True, type=Path)
    parser.add_argument("--extra-cache", action="append", type=Path, default=[],
                        help="optional prior dependency cache, searched after the fresh local outputs")
    parser.add_argument("--temp-root", type=Path)
    args = parser.parse_args()
    expected_controls = (HERE / "REFLECTED_CONTROLS.json").read_text()
    for flag in ([], ["-O"]):
        actual = checked([sys.executable,*flag,HERE / "reflected_controls.py"],capture_output=True).stdout
        if actual != expected_controls:
            raise RuntimeError("Reflected counts or terminating excitation controls differ")
    mathlib = args.mathlib.resolve()
    lean = args.lean.resolve()
    checked([lean,"--version"])
    with tempfile.TemporaryDirectory(dir=args.temp_root) as temp:
        root = Path(temp)
        search = [root, *(p.resolve() for p in args.extra_cache),
                  mathlib / ".lake/build/lib/lean", *(mathlib / ".lake/packages").glob("*/.lake/build/lib/lean")]
        env = dict(os.environ,LEAN_PATH=os.pathsep.join(map(str,search)))
        sources = [(HERE.parent / "FiniteTrace.lean",0),(HERE / "TernarySteering.lean",1),
                   (HERE / "BasinBlocks.lean",1),(HERE / "FiberInterval.lean",2)]
        for source,n_expected in sources:
            result = subprocess.run([lean,"-DwarningAsError=true","-o",root / (source.stem+".olean"),source.name],
                                    cwd=source.parent,env=env,capture_output=True,text=True)
            print(result.stdout,end="")
            print(result.stderr,end="",file=sys.stderr)
            result.check_returncode()
            matches = re.findall(r"depends on axioms:\s*\[([^]]*)\]", result.stdout)
            if len(matches) != n_expected or any(set(row.replace("\n","").replace(" ","").split(","))-ALLOWED
                                                   for row in matches):
                raise RuntimeError(f"Unexpected axiom inventory in {source.name}")
    print("Four module builds, four axiom inventories, and both exact control replays passed.")


if __name__ == "__main__":
    main()

"""Replay the mass packet with the pinned parents in a fresh module directory."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import tempfile


PIN = "eb91086951b66923787f696801f0c3ca52a0077d"
PARENT = "research/six-hour-20261127/pointwise"
PARENTS = ("PermanentSafeDebt", "PermanentSafeOrdinary")
LOCAL = ("SignedDeathClock",)


def run(args, cwd, env=None):
    result = subprocess.run(args, cwd=cwd, env=env, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stdout.decode() + result.stderr.decode())
    return result.stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    lean = str(args.lean.resolve())
    mathlib = args.mathlib.resolve()
    here = Path(__file__).resolve().parent
    repo = Path(run(["git", "rev-parse", "--show-toplevel"], here).decode().strip())
    data = {
        "lean": run([lean, "--version"], here).decode().strip(),
        "mathlib_commit": run(["git", "rev-parse", "HEAD"], mathlib).decode().strip(),
        "parent_commit": PIN, "modules": {},
    }
    with tempfile.TemporaryDirectory(prefix="collatz-first-exit-") as tmp:
        work = Path(tmp)
        paths = [work, mathlib / ".lake/build/lib/lean",
                 *sorted(mathlib.glob(".lake/packages/*/.lake/build/lib/lean"))]
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
        for name in PARENTS + LOCAL:
            if name in PARENTS:
                content = run(["git", "show", f"{PIN}:{PARENT}/{name}.lean"], repo)
            else:
                content = (here / f"{name}.lean").read_bytes()
            (work / f"{name}.lean").write_bytes(content)
            output = run([lean, "-j1", "-DwarningAsError=true", "-o",
                          f"{name}.olean", f"{name}.lean"], work, env).decode()
            data["modules"][name] = {
                "source_sha256": sha256(content).hexdigest(),
                "object_sha256": sha256((work / f"{name}.olean").read_bytes()).hexdigest(),
                "audit": output.splitlines(),
            }
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()

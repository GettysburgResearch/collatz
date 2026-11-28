"""Compile this pass's eight self-contained local Lean modules from fresh objects.

The density premise and upper-tail premise in ClosureConsumer remain explicit.
SignedDeathClock has a separate receipt including its two pinned PR200 parents.
This command does not rebuild any external claimed proof.
"""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import tempfile


def run(command, cwd, env=None):
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True)
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
    modules = {
        "ParityTail": here / "parity/ParityTail.lean",
        "ClosureConsumer": here / "ClosureConsumer.lean",
        "ExternalClaimChecks": here / "arithmetic/ExternalClaimChecks.lean",
        "CountedDeadline": here / "CountedDeadline.lean",
        "Resonance": here / "descent/Resonance.lean",
        "SignedFloor": here / "descent/SignedFloor.lean",
        "EndpointFlux": here / "descent/EndpointFlux.lean",
        "RationalControl": here / "parity/RationalControl.lean",
    }
    data = {
        "scope": "Local new modules only; no external full-proof rebuild",
        "lean": run([lean, "--version"], here).decode().strip(),
        "mathlib_commit": run(["git", "rev-parse", "HEAD"], mathlib).decode().strip(),
        "modules": {},
    }
    with tempfile.TemporaryDirectory(prefix="collatz-core-replay-") as tmp:
        work = Path(tmp)
        paths = [work, mathlib / ".lake/build/lib/lean",
                 *sorted(mathlib.glob(".lake/packages/*/.lake/build/lib/lean"))]
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
        for name, path in modules.items():
            content = path.read_bytes()
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

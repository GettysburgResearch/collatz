"""Rebuild the two local Lean sources against an existing mathlib cache."""
import argparse
import os
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory


PACKET = Path(__file__).resolve().parent
ROOTS = (
    "hits_step", "orbit_last", "first_meeting_count", "arrivals_one",
    "arrivals_two", "cycle_gate_identity", "separated_lift", "sixteen_delay",
    "distinct_dates_gate", "four_step_ties", "three_eighths",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib", type=Path, required=True)
    args = parser.parse_args()
    lake = args.mathlib.resolve() / ".lake"
    roots = [lake / "build/lib/lean", *sorted((lake / "packages").glob("*/.lake/build/lib/lean"))]
    opts = [str(args.lean.resolve()), "-j1", "-DwarningAsError=true",
            "-DautoImplicit=false", "-DElab.async=false"]
    affine = PACKET.parent / "astra-critical-rigidity-20261128/formal/AffineOrbit.lean"
    with TemporaryDirectory(prefix="median-merger-lean-") as temp:
        build = Path(temp)
        env = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, [build, *roots])))
        for source in (affine, PACKET / "MedianMerger.lean"):
            (build / source.name).write_bytes(source.read_bytes())
            subprocess.run([*opts, "-o", source.stem + ".olean", source.name],
                           cwd=build, env=env, check=True)
        audit = "import MedianMerger\n" + "".join(
            f"#print axioms Collatz.MedianMerger.{name}\n" for name in ROOTS)
        (build / "Audit.lean").write_text(audit, encoding="utf-8")
        result = subprocess.run([*opts, "Audit.lean"], cwd=build, env=env, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                encoding="utf-8")
        print(result.stdout, end="")
        for name in ROOTS:
            prefix = f"'Collatz.MedianMerger.{name}' "
            line, = [line for line in result.stdout.splitlines() if line.startswith(prefix)]
            claim = line.removeprefix(prefix)
            if claim == "does not depend on any axioms":
                continue
            start = "depends on axioms: ["
            if not claim.startswith(start) or not claim.endswith("]"):
                raise ValueError(line)
            if set(claim[len(start):-1].split(", ")) - {"propext", "Classical.choice", "Quot.sound"}:
                raise ValueError(line)


if __name__ == "__main__":
    main()

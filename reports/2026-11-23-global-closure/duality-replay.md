# Triadic dual: exact execution and proof scope

The fresh strict compile used Lean 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and the existing read-only
Mathlib checkout at `d13f23b723b8a846827a245b89c10fc7d3f11612`.

Both `TriadicDualClosure.lean` and `TriadicDualAudit.lean` compiled with
`-DwarningAsError=true` and exit code zero. The latter imported the freshly
compiled local object. Historical repository modules were not rebuilt.

[duality-lean-receipt.json](duality-lean-receipt.json) binds the exact
commands, paths, source hashes, log hashes and compiler version.
[duality-lean-compile.log](duality-lean-compile.log) is the empty successful
compile output. [duality-lean-axioms.log](duality-lean-axioms.log) is the
unedited audit output.

## Audit coverage

The audit lists all 20 authored public declarations: twelve theorems,
six definitions and two inductive/structure declarations. It also lists
the three transition constructors, the state constructor and its three
projections. Every listed declaration depends only on a subset of
`propext`, `Classical.choice`, and `Quot.sound`. The main theorem's audit
therefore also covers its private support-lemma dependencies.

The formal statement proves a closing implication for one unchanged
finite triadic candidate whose actual opposite-parity tests pass at every
clock. It does not prove universal candidate existence. The explicit
finite-prefix height certificate in `TRIADIC_RANK.md` has written-proof
scope; it is not included in the Lean theorem count.

## Reproduction

The commands below rebuild only the two new local modules. The output
directory remains outside the repository and the dependency checkout.

```python
from pathlib import Path
import os
import subprocess

repo = Path('/workspace/scratch/56e7a5765d0c/collatz_global_nov23')
source = repo / 'research/global-closure-20261123/duality/lean'
lean = Path('/workspace/scratch/56e7a5765d0c/nov23-runtime/lean-4.34.1-linux/bin/lean')
mathlib = Path('/workspace/scratch/c6766c1207a3/mathlib_nov23_runtime')
out = Path('/workspace/scratch/56e7a5765d0c/nov23-duality-lean')
out.mkdir(exist_ok=True)
env = os.environ.copy()
env['LEAN_PATH'] = ':'.join(map(str, [
    out,
    mathlib / '.lake/build/lib/lean',
    *sorted(mathlib.glob('.lake/packages/*/.lake/build/lib/lean')),
]))

for name in ['TriadicDualClosure', 'TriadicDualAudit']:
    command = [str(lean), '-DwarningAsError=true',
               '-o', str(out / (name + '.olean')),
               str(source / (name + '.lean'))]
    result = subprocess.run(command, cwd=source, env=env, text=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    print(name, result.returncode, result.stdout)
    if result.returncode:
        raise SystemExit(result.returncode)
```

The scientific note, formal implication, primary-source attribution and
unproved construction step are kept together in
[TRIADIC_RANK.md](../../research/global-closure-20261123/duality/TRIADIC_RANK.md).

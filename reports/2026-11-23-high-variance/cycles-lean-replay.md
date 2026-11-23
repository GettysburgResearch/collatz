# Exact cycle-module replay

The verified run used:

- Lean `4.34.1`, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- `-DwarningAsError=true` for the mathematical module and its exhaustive audit.
- A freshly compiled local `BalancedCycleUnit.olean` in an external build
  directory, followed by an audit import resolving to that directory.

The source hashes and the all-nine-declaration axiom output are bound in
[cycles-receipt.json](cycles-receipt.json).
[cycles-lean-compile.log](cycles-lean-compile.log) records the strict exit
codes and output. [cycles-lean-axioms.log](cycles-lean-axioms.log) contains
the unedited audit output. There are eight theorems and one definition;
all depend only on `propext`, `Classical.choice`, and `Quot.sound`.

## Commands

From the repository root, with the pinned runtime and its built Mathlib
available, this is the compile sequence used. Set the three absolute
paths for another environment; keep the output directory outside the
repository. The Mathlib checkout is read-only during the run. Its built
package dependencies are included in `LEAN_PATH`.

```python
from pathlib import Path
import os
import subprocess

repo = Path('/workspace/scratch/56e7a5765d0c/collatz_nov23')
lean = Path('/workspace/scratch/56e7a5765d0c/nov23-runtime/lean-4.34.1-linux/bin/lean')
mathlib = Path('/workspace/scratch/c6766c1207a3/mathlib_nov23_runtime')
out = Path('/workspace/scratch/56e7a5765d0c/nov23-cycle-lean-check')
source = repo / 'research/high-variance-20261123/cycles/lean'
out.mkdir(exist_ok=True)
env = os.environ.copy()
env['LEAN_PATH'] = ':'.join(map(str, [
    out,
    mathlib / '.lake/build/lib/lean',
    *sorted(mathlib.glob('.lake/packages/*/.lake/build/lib/lean')),
]))

for name in ['BalancedCycleUnit', 'BalancedCycleAudit']:
    command = [
        str(lean), '-DwarningAsError=true',
        '-o', str(out / (name + '.olean')),
        str(source / (name + '.lean')),
    ]
    result = subprocess.run(
        command, cwd=source, env=env, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    (out / (name + '.log')).write_text(result.stdout)
    print(name, 'exit', result.returncode, result.stdout)
    if result.returncode:
        raise SystemExit(result.returncode)
```

Both compilations returned zero. No local compiled object was committed.
The exhaustive audit is `lean/BalancedCycleAudit.lean`, which prints
axioms for all nine public declarations, including the literal finite
sum definition.

## Construction controls

The separate exact controls were run with normal and optimized Python:

```text
python research/high-variance-20261123/cycles/check_moving_prime_controls.py
python -O research/high-variance-20261123/cycles/check_moving_prime_controls.py
```

Their output was byte-identical and has SHA256
`72a3cea52cfaad7feb4f6f4b5b325375122f25926c38847fe809d198c515680d`.
The script uses explicit exceptions, so optimization does not remove
its checks. These two controls test the construction formulas; they do
not establish the universal all-finite-prime/all-real-floor theorem.

## Independent review boundary

The merger lane independently reviewed written Sections 1–4 at SHA256
`a6e8585f188899c08fd450d50fbbf85b53382bb5a4f6fea6440367d8c36bb3b1`.
Root also read the complete Lean module and checked its stated scope.
No review or compilation is presented as a proof of arbitrary positive
cycle exclusion or of the full Collatz theorem.

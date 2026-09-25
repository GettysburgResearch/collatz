# Collatz: arithmetic component-rigidity packet

A standalone proposed theory-building pass, 25 September 2026. **Not a complete Collatz proof; not independently reviewed; no external priority claim.**

Start with `PROOF.md`. It develops an ordinary-integer component-separator formulation, two exact arithmetic current laws, and a boundary-birth identity. It then proves a growing inverse-ladder lemma, uniform relative-gap geometry for **every original component**, a macroscopic convergent-block sufficiency criterion, and a quantitative obstruction to low-variation nonconstant invariant functions.

The key remaining estimate is stated explicitly: deriving sublinear dyadic variation from the actual three-term arithmetic law. It is not proved. The 5x+1 cycle control prevents topology or multiplicative independence alone from being misrepresented as a closing argument.

## Contents

- `PROOF.md`: statements, complete proof route, source pins, exact gap and limitations.
- `experiment.py`: exhaustive small finite-coloring checks, open-boundary larger checks, inverse ladders and negative controls.
- `build_certificates.py`: reproducible finite all-height net certificates.
- `verify_certificates.py`: separate literal checker, importing no generator or project code.
- `results.json`: normal/optimized-identical deterministic experiment output.
- `net_certificates.json`: all six retained physical source nets plus two exact universal arithmetic bounds.
- `validation.json`, `SHA256SUMS.txt`: executed checks and file identities.

## Reproduce

Python 3.10 or newer, standard library only. Run from this directory:

```sh
python -S -B experiment.py --output results.replayed.json
python -O -S -B experiment.py --output results.optimized.json
python -S -B build_certificates.py
python -S -B verify_certificates.py net_certificates.json
python -O -S -B verify_certificates.py net_certificates.json
```

Compare the regenerated experiment files with `results.json`. There are no external services, credentials, downloads, GPU requirements or repository imports. Tests raise errors explicitly rather than depending on Python assertions.

## Scope

Finite compatible colorings are not claimed to extend globally. Dense or equidistributed inverse phases do not imply different components intersect. Relative gaps tending to zero do not imply positive natural density. The experimental counts are not percentages of Collatz resolved.

No GitHub write or main-branch change was made. No full-repository validator, remote CI, formal proof assistant or independent mathematical reviewer was run. The packet can be reviewed or imported separately without replacing any existing scientific status.

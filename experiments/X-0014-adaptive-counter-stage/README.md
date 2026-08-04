# X-0014 — Adaptive counter isometry and stage Montgomery compression

Experiment ID: `X-0014`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0028` and `T-0027`--`T-0029`

## Research questions

1. Does a finite chain of odd-affine binary divisions compress to one offset Montgomery tile without losing intermediate integrality?
2. Is the normalized connector-prefix map an exact 2-adic isometry in the fine padding address?
3. Does every finite prefix have exactly one counter address?
4. Can arbitrary prefix requests be routed through one 512-cell annulus while preserving positive two-connector growth?
5. Does that growth remain valid for every fine-address choice across scale overflow?
6. Do the full stage exponents obey exact normalized squaring laws?

## Main audit

`run.py` uses exact Python integers. It:

- checks Montgomery composition on signed affine systems;
- verifies composite/local domain equivalence;
- replays an actual phase-34 residual slice;
- verifies the counter-prefix isometry and one-bit lifts;
- enumerates every fine address through seven-bit precision;
- constructs representative adaptive 512-cell annuli;
- checks within-annulus jumps and growth;
- verifies the normalized stage-scale squaring laws.

## Corrected scale-boundary audit

The first version of `T-0029` incorrectly stated that the same `4d` two-step jump bound holds unchanged across scale overflow.

The growth conclusion remains correct, but the final source cell permits a jump below `5d`. `boundary.py` exhaustively checks both cross-scale source cases for all four tower types at representative precision:

- source cell 510 to next-scale cell 0: two-step jump `< 4d`;
- source cell 511 to next-scale cell 1: two-step jump `< 5d`;
- all exact two-connector growth inequalities remain positive.

The final boundary lower coefficient is

\[
\frac5{53}(2B-d)-55d
=
\frac{275}{3392}B>0.
\]

## Commands

```bash
python3 -m py_compile experiments/X-0014-adaptive-counter-stage/run.py
python3 experiments/X-0014-adaptive-counter-stage/run.py
python3 -m py_compile experiments/X-0014-adaptive-counter-stage/boundary.py
python3 experiments/X-0014-adaptive-counter-stage/boundary.py
```

## Expected output

Main audit:

```text
verified offset Montgomery composition and exact path domains
verified padding-counter isometries and one-bit lifts
verified adaptive 512-cell prefix routing and robust growth
verified exact stage compression and normalized scale squaring
all adaptive-counter stage checks passed
```

Boundary audit:

```text
verified 4096 arbitrary adaptive scale-boundary cases
all adaptive 512-cell boundary checks passed
```

Checked-in copies are `results/summary.txt` and `results/boundary-summary.txt`.

## Interpretation

The padding height has coordinates

```text
scale m | 9-bit coarse cell j | H-bit fine address s | finite core residue
```

The fine address is isometrically equivalent to the normalized connector prefix. It can route any requested logarithmic prefix without leaving its cell.

The corrected theorem now distinguishes:

- within-annulus arbitrary routing, with a `<4d` two-step cost;
- final scale overflow, with a `<5d` cost but nearly doubled source height.

Both regimes retain positive two-connector growth.

## Limitations

- Prefix routing covers `O(m)` low bits, not the full `Theta(2^m)` connector block.
- `T-0031` shows that the stage quotient above the canonical correction still dies in any ordinary infinite realization.
- The adaptive chart does not solve exact cap-to-correction stitching.
- No marked Collatz seed or counterexample is constructed.

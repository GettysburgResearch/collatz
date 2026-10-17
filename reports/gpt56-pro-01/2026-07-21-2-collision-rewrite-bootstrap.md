# Session report — collision-rewrite bootstrap

Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Date: 2026-07-21

## Starting hypothesis

Finite shortcut-Collatz parity blocks may have exact supercritical collisions. Consecutive collisions should admit an affine coordinate in which they become a partial radix-replacement map. A counterexample could then be certified by a finite rewrite grammar that regenerates admissible words indefinitely.

## Approaches attempted

1. Re-derived the finite parity-affine formula with chronological bit conventions.
2. Abstracted adjacent and consecutive collisions into a general affine conjugacy theorem.
3. Verified the previously identified length-6 pair and length-9 triple collisions.
4. Exhaustively enumerated all consecutive collision bundles through length 17.
5. Promoted a newly found exact width-six length-17 collision to a finite observation with an explicit algebraic certificate.
6. Reconstructed the mixed-radix carry normalization for the `64 -> 81` chart.
7. Proved a nine-column carry cycle and a parameterized finite-horizon stack amplifier.
8. Audited every result for the distinction between finite ordinary integers and radix-adic limits.

## New results

### Proposed finite theorem

`T-0001` proves that any consecutive supercritical collision bundle

\[
T^L(2^Lq+r+j)=3^aq+s
\]

induces

\[
H(2^LB+j)=3^aB+j
\]

on a specific invariant congruence class that lifts to ordinary integers.

### Exact collision charts

- Width 2, length 6:
  \[
  T^6(64q+14)=T^6(64q+15)=81q+20.
  \]
- Width 3, length 9:
  \[
  T^9(512q+124+j)=729q+182,\quad0\le j\le2.
  \]
- Width 6, length 17:
  \[
  T^{17}(131072q+9090+j)=177147q+12302,\quad0\le j\le5.
  \]

### Stack amplifier

For one explicit nine-digit base-64 word \(W\),

\[
H^{9m+1}(L_1W^m(x))=81^{9m}(81x+1).
\]

This gives arbitrarily long exact finite segments but does not close indefinitely.

### Enumeration

`X-0001` exhausts all residue classes through `L=17`. The maximum supercritical bundle width found is 6.

## Candidate counterexamples

None. No finite integer has been shown to remain forever in the domain of an induced radix map.

## Failed approaches and blocked steps

- Periodic infinite parity words naturally produce 2-adic rational cycles; this does not produce a finite positive integer.
- A finite carry stack can force arbitrarily many steps without yielding one fixed integer with infinitely many steps.
- Local expansion is not enough; a complete boundary-repair or regeneration cycle must retain net expansion.
- The current contribution does not solve the high-order finite-boundary closure problem.

## Potential errors requiring adversarial attention

1. Chronological versus reversed parity-word orientation.
2. Low-order-first versus high-order-first digit composition.
3. The implication from the lifting congruence to a nonnegative quotient in `T-0001`.
4. Carry direction in `L-0002`.
5. Any silent passage from arbitrarily large finite `m` to an infinite word.
6. Dependence of parity blocks on residues modulo exactly `2^L`.
7. Independent reproduction of the length-17 enumeration.

## Files changed

```text
CURRENT_STATE.md
OPEN_PROBLEMS.md
CLAIMS.md
CANDIDATES.md
NEGATIVE_RESULTS.md
NOTATION.md
claims/lemmas/L-0001-parity-affine-formula.md
claims/lemmas/L-0002-nine-column-stack-amplifier.md
claims/theorems/T-0001-collision-bundle-conjugacy.md
claims/observations/O-0001-64-to-81-pair-chart.md
claims/observations/O-0002-512-to-729-triple-chart.md
claims/observations/O-0003-131072-to-177147-six-chart.md
experiments/X-0001-collision-enumeration/README.md
experiments/X-0001-collision-enumeration/run.py
experiments/X-0001-collision-enumeration/results/summary.txt
reports/gpt56-pro-01/2026-07-21-2-collision-rewrite-bootstrap.md
```

## Claims affected

Added `D-0001`, `L-0001`, `T-0001`, `O-0001`, `O-0002`, `O-0003`, `L-0002`, `X-0001`, and open questions `Q-0001` through `Q-0006`.

## Recommended next actions

1. Assign a blind verifier to `L-0001` and `T-0001`.
2. Give separate agents the width-three and width-six carry graphs.
3. Search for exact transitions among charts rather than optimizing one chart in isolation.
4. Require every proposed construction to supply a finite schema-regeneration induction.
5. Extend `X-0001` only when the search is tied to a theorem-oriented objective such as carry-cycle length or grammar closure.

## Organizational improvement ideas

No change to the project operating model is proposed in this contribution. At the present small collaboration size, the existing README is workable. The immediate organizational need was simply to instantiate its canonical state, claim, problem, experiment, and report files, which this branch does.

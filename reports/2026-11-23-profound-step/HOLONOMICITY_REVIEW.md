# Independent scoped review of the holonomicity route

Reviewer: `arithmetic_minimum` subagent. Date: 2026-11-23.

**Finding:** no mathematical gap found in the finite normalized-window
argument, its written implication to eventual parity/state periodicity, or
the scope of the six audited Lean declarations. No recurrence for an arbitrary
actual orbit is established. This review does not claim full Collatz closure.

## Frozen inputs

All paths below are relative to the repository root. SHA-256 values were
recomputed from the files after the two editorial clarifications described
below had been applied.

| Input | SHA-256 |
|---|---|
| `research/profound-step-20261123/HOLONOMICITY.md` | `474c5e54492ebe7f69d79e5bd858c44fa1fd3d7737350439d63e534ba81e6149` |
| `research/profound-step-20261123/lean/ParityRecurrence.lean` | `49e330cb36fa3e088490e4fa068c10ef38db9a6c2c98f9278570409a046c7074` |
| `research/profound-step-20261123/lean/ParityRecurrenceAudit.lean` | `b96fcbc728009a61e690b9237cd9d9a3bf2795db892c9fdbd23e62649cb1f27a` |
| `research/profound-step-20261123/reports/parity-lean-check.json` | `ab09bdc57fcc2993c9c0ba9b7e256f3cfae4f0678e34fbfc4e33ca769a279cfe` |

The Lean source, audit source, successful build log, and receipt were read.
The receipt reports fresh local output, warnings treated as errors, Lean
4.34.1 at commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. This reviewer inspected that
receipt and the proof source rather than performing a redundant rebuild.
The printed declaration audits use only `propext`, `Classical.choice`, and
`Quot.sound` (or subsets).

## Mathematical checks

1. For the coefficients
   \(b_k=e_k3^{-p_{k+1}}\), multiplying a length-\(d+1\) recurrence by
   \(3^{p_k}\) does produce the normalized entries
   \(e_{k+j}3^{-(e_k+\cdots+e_{k+j})}\). They range over a finite set
   determined by the actual parity window. This operation does not assume
   that the parity itinerary already has finite state complexity.

2. A finite family of nonzero polynomials has only finitely many natural
   roots in total. Therefore all normalized windows occurring sufficiently
   late annihilate the corresponding polynomial identically. Extracting
   one coefficient degree at which the supplied recurrence-polynomial
   family is nonzero produces a nonzero constant recurrence. No leading
   coefficient is divided by, so zeros at a finite number of clock values
   are handled by the common cutoff.

3. The explicit cutoff in the written note is valid after clearing
   denominators. Multiplication by \(3^{d+1}\) gives integral polynomial
   coefficients bounded by \((d+1)H3^{d+1}\). A nonzero leading integer
   coefficient has magnitude at least one, making the stated Cauchy root
   bound sufficient. This numerical cutoff is correctly excluded from
   the Lean inventory.

4. With the last nonzero constant coefficient at index \(d\), the first
   \(d\) parity bits fix the normalized contributions up to that index.
   The two possible final bits have distinct contributions. Hence each
   occurring block has at most one successor, and the finite directed
   graph gives an eventually periodic actual parity tail. The \(d=0\)
   case is separately handled as an eventually zero tail.

5. The return from periodic parity to periodic odd-denominator rational
   states retains the denominator. For a repeated block with multiplier
   \(3^a/2^L\), multiplying the fixed-point difference by the original
   odd denominator gives one fixed integer divisible by \(2^{Lt}\) for
   every \(t\). It must vanish. This excludes the possibility of using
   periodic parity merely as an approximation to a different rational
   state orbit.

6. The stronger written condition
   \((3-z^2)B_n(z)\in\mathbb Q[z]\) forces the eventually alternating
   support and the correct one-odd-step factor. An all-one two-periodic
   tail has the wrong factor, and the all-zero tail cannot arise from a
   positive ordinary source. Thus the stated classification under this
   stronger condition is justified. The note does not infer that
   arbitrary D-finiteness alone excludes nontrivial cycles.

## Literature attribution and formal boundary

The reviewed note explicitly credits the univariate Bézivin theorem and
Bell–Smertnig's Pólya-series rationality theorem. Their primary paper was
independently opened during this pass:
<https://math.smertnig.at/paper/bezivinmultivariate.pdf>.
Its finite-multiplicative-group coefficient hypothesis applies with
\(G=\langle3\rangle\). The note describes its finite-window argument as an
elementary reconstruction/application rather than claiming a new general
arithmetic-rationality theorem.

The Lean generic theorem has the polynomial recurrence, nonzero polynomial
family, normalization, and finite window type as explicit premises. The
specialization establishes the normalization for every binary itinerary and
passes the still-explicit recurrence premise to the generic theorem. The
fact that the finite type overcounts the possible normalized windows causes
no issue. The note correctly leaves formal power-series D-finiteness,
rationality, finite-state periodicity, the effective Cauchy bound, and the
classification under its stronger condition to written mathematics.

The author corrected two review suggestions before the hashes above were
frozen: malformed section references, and wording that could have been read
as claiming an arbitrary positive-cycle classification. No proof change was
required.

## Remaining proof obligation

The exact missing step is to construct a nonzero eventual polynomial
recurrence for the one fixed actual weighted parity series (or a stronger
relation such as the displayed quadratic denominator condition). The tail
functional identities do not close to a finite family for an arbitrary
source. Neither the finite-window theorem nor the successful Lean build
establishes that missing premise.

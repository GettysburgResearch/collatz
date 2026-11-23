# Checkpoint 14: direct high-variance closing attempts

**23 November 2026. Full Collatz remains OPEN. This checkpoint obtains no
new universal closing estimate and no new Lean closing theorem.** It records
four attempted routes through the remaining arithmetic difficulty, an exact
full-denominator trace interface, and reproducible finite tests of a proposed
stronger counting statement. The new finite counterexample rules out one
monotonicity argument; it does not refute the counting target.

The map is the ordinary shortcut map `T(n)=n/2` on even integers and
`T(n)=(3n+1)/2` on odd integers. Inverse analytic statements retain the
positive odd ternary-unit domain and the source qualifications of their
specified inputs. A cycle-counting statement does not exclude escape.

## What changed the research decision

The refresh inspected the latest PR titles and five active mathematical
heads, on top of the preceding whole-repository inventory and research map.
It did not recompile or re-audit all earlier work.

| Input | Fresh result used in choosing the attacks |
|---|---|
| PR178, `7e4569476e152f6b8537bdc1711df595ec1ffd89` | Actual-window phase discrepancy now gives polynomial low-run occupation decay. Its compact entropy criterion needs finite positive limiting canonical rows. |
| PR185, `39ba48e6a8af781193e28c679ea8ab64663c3aa6` | The same-source inverse-law comparison is uniform over all inverse horizons. Its cycle work retains the distinguished ideal and full denominator. |
| PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2` | Modular routing multiplicity pays for the number of routes, while a specified deep arithmetic prefix still has a precision cost. |
| PR175, `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73` | A complete-denominator cycle-minimum bound and concentration of actual stopping payoff on a long anchored prefix. |
| PR177, `0444986571f09f302cb3687b4bba3552600e4119` | Binary-run valuation clocks and the exact finite-Green depth/time profile. |

PR178's polynomial occupation estimate is stronger asymptotically than
checkpoint 13's effective `O_S(N/log N)` estimate. The older explicit
finite-core bound and logarithmic-horizon sparse-return descent have their
separate scope. This checkpoint does not pursue another occupation-rate
refinement.

## 1. Keep the exact identity atom

[The cycle attempt](cycles/IDENTITY_ATOM_ATTEMPT.md) works with

\[
D=2^A-3^p>0,\qquad
C_w=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i},\qquad
0\le d_0<\cdots<d_{p-1}<A.
\]

Let `N_r(A,p)` count the words with `C_w = r mod D`. On `Z/DZ`, let
`P_0,P_1` be the permutation matrices of `x -> x/2` and
`x -> (3x+1)/2`. The exact unnormalized identity is

\[
\boxed{[z^p]\operatorname{tr}(P_0+zP_1)^A=D\,N_0(A,p).}
\]

All words of that length and weight have multiplier one modulo the whole
`D`, so their affine maps are translations. Their traces select exactly
the zero translation. A primitive positive cycle supplies `A` distinct
rotations in that fiber. Therefore the strict bound

\[
[z^p]\operatorname{tr}(P_0+zP_1)^A<AD
\quad(A\ge3)
\]

would exclude every nontrivial positive cycle. **The strict bound is not
proved.** The trace identity is a research interface, not a new exclusion.
The note handles the known two-word cycle and the excluded `A=2,p=1` case.

Three proposed ways of estimating the coefficient were tested:

- **Uniform mixing:** the fixed-weight law has at most `binomial(A,p)`
  support points. Its total-variation distance from uniform is at least
  `1-binom(A,p)/D`, tending to one at the critical slope with the cited
  polynomial-loss denominator bound. The inspected affine cutoff theorem
  concerns different parameters and independent translations; it does not
  control this identity atom.
- **Marked rotations:** both rotation multipliers preserve zero. Their
  balance equation at zero is an identity and does not bound its mass.
- **Order and positivity:** fibers need not be antichains under the
  coordinatewise order on the one-positions. A unit-residue counterexample
  below also prevents removing this issue by discarding proper factors of
  `D`. Rounded positivity relaxations can accept nonintegral fixed points.

### A concrete failed monotonicity step

At `A=35,p=22`, put

\[
D=2978678759,\qquad r=2209100811,\qquad \gcd(r,D)=1.
\]

There are two distinct, coordinatewise comparable one-position lists with

\[
C_u=r+44D=133270966207,\qquad
C_v=r+233D=696241251658.
\]

Hence `C_v-C_u=189D`. Their full lists and the other seven words in the
same fiber are retained in [the witness JSON](cycles/maxfiber_35_22.json).
The small verifier independently recovers this complete nine-word fiber
from 86,283 possible numerators. It does not need the large enumeration.

The broader conjecture `max_r N_r(A,p)<A` survived two complete fixed-weight
enumerations: 225,792,840 words at `(32,20)` and 1,476,337,800 words at
`(35,22)`, with maximum fibers seven and nine. Four larger rational
denominator slices were also counted. These scopes are finite; the slices
are not complete word laws. [Exact commands, sources and output](cycles/RUNS.md)
preserve the distinction. Numerical survival is not a proof of the target.

## 2. Attempt an adelic entropy contradiction on the actual orbit

[The adelic attempt](ADELIC_MIXING_ATTEMPT.md) combines the new all-depth
inverse comparison with the stabilized actual real fibers and the joint
affine law's dyadic mixing. The intended conclusion is a nondegenerate
compact inverse kernel, which would activate PR178's entropy contradiction.

The mixing theorem controls the unconditioned law. The actual application
conditions at `q_j mod 3^(j+r+1)` and retains real height comparable to `q_j`.
No uniform conditional estimate at these moving ordinary centers was
obtained. An arbitrary dyadic pushforward is not one of the inverse windows
covered by PR185.

The direct simultaneous approximation test also has an exact outcome.
For an actual inverse prefix, write

\[
D'=2^{S_n},\quad
B=\sum_{i=1}^n3^{i-1}2^{S_n-S_i},\quad
qD'-B=3^n x.
\]

The proposed real, binary and ternary product is

\[
|D'(qD'-B)|_\infty\,|D'B|_2\,|D'(qD'-B)|_3=x.
\]

Along the reversed prefix ending at the original source `p`, it equals
`p`, rather than a negative power of height. In addition, `q=q_j` varies,
so the standard fixed-form Subspace Theorem does not directly apply.
This identifies the failed inference; it is not a Diophantine exclusion.

## 3. Try a pointwise comparison of canonical sibling mass

[The sibling attempt](NONLOCAL_SIBLING_ATTEMPT.md) tests nonlocal repair,
regeneration, a maximum principle, and subtraction from the least excessive
majorant. It obtains no OPEN-F/OPEN-S bound. The actual stopping mass
retains a deterministic anchored prefix; the routing count cannot be
substituted for its payoff law.

The near-contact subtraction argument is sound, but independent review
found it was already implied by the stronger result in checkpoint 8,
`OBSTACLE_ENTRANCE_RENEWAL.md`, Section 5. It is explicitly attributed as a
rederivation. Inverse near-contact mass recurs at unbounded ordinary
heights, so a height cutoff does not remove the active obstacle constraints.
No uniform hitting-time or sibling-comparison bound follows.

## 4. Try simultaneous Mahler rigidity

[The generating-function attempt](MAHLER_RIGIDITY_ATTEMPT.md) starts from
the exact identities for an invariant sequence,

\[
a_{2n}=a_n,\qquad a_{2n+1}=a_{3n+2}.
\]

For `F(z)=sum a_n z^n`, these give a historical Berg--Meinardus mixed
functional equation. The Adamczewski--Bell theorem, in the inspected
Schäfke--Singer formulation, requires two separate finite scalar Mahler
equations. The generated residue-extraction system has unbounded ternary
depth. No finite-rank closure, separate pair of equations, or analytic
continuation was proved. The rigidity theorem cannot be applied without
that missing deduction.

## Evidence and useful handoffs

The local identities and counterexample are written mathematics plus exact
integer verification. The large enumerations were executed by the cycle
lane; the root independently checks the small complete-fiber witness and
parameter bounds. Selected argument boundaries received independent agent
review. External analytic theorems remain attributed inputs, not newly
formalized results. **No new Lean declaration or axiom is added.**

- [Standalone finite affine-word question](FINITE_AFFINE_WORD_QUESTION.txt)
  gives the full-denominator counting problem without its application.
- [Standalone mixed-decimation question](MIXED_DECIMATION_QUESTION.txt)
  asks for the missing rigidity input and states the exact hypotheses.
- [Source pins and review record](../../../../reports/2026-11-23-high-variance-attacks/README.md)
  distinguish fresh execution from source-qualified mathematics and
  rediscovered results.

The next substantive arithmetic step would be a zero-specific coefficient
bound, not another uniform-mixing estimate. The escape routes still need a
pointwise estimate at the actual moving ordinary source, or a proof of the
finite closure required by the generating-function route. None has been
supplied in this checkpoint.

# Independent review of the actual-map scalar formalization

23 November 2026. Reviewer: `density_free_germ8`.

**Verdict: VERIFIED for R10-G1--R10-G3 at the exact pins below.**
The formal module constructs its scalar from the defined ordinary
odd Collatz orbit, proves unconditional real summability and the
scalar bounds, and proves the equivalence between reaching one and
the actual scalar being a rational with a power-of-three denominator.
The universal assertion that every such scalar has this arithmetic
form remains unproved.

## Exact source and review binding

Parent PR182 head: `c369ae3c426ec6aaf9a280ec9578b9910c2147d5`.
Paths are under `research/carry-tower-round10-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `ActualScalar.lean` | `85385ac9b4dbc2bab8b3f78f02d4f865ed16d2b8` | `5b0f035ad14624376ce722bfdff5d9d216b266a0d7066efc3715fcc19d37f4a9` |
| `ACTUAL_SCALAR_FORMALIZATION.md` | `05762ccab2796e49a0938db5442ebf1f61b3ac9f` | `e9aa6e16bd29487d19ec603f1c73a267b7bca93ee7334ea68882ab9c5b2be2d0` |

I read the entire final Lean source and its written explanation,
including the final strict-lower-bound and finite-tail additions.
There are 37 theorem declarations and 10 definitions in the namespace
`Collatz.CarryTowerRoundTen.ActualScalar`.

The written predecessor is the parent's
`research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`,
R8-G1--R8-G2, blob `540110f09cf68e3309fd83fea9c7ae497536ded4`.
The new Lean file does not import that file, any prior repository
module, or an abstract version of its convergence conclusion.

## Definitions and ordinary attachment

The gap is `(3*q+1).factorization 2`. The successor is the natural
quotient by the resulting full power of two. Since `3*q+1` is never
zero, the factorization lemmas prove the complete equation, positive
quotient, and odd quotient. For an odd source the first gap is at
least one. Recursion defines every orbit state, and induction/case
analysis keeps all subsequent states positive and odd.

The real term is the actual gap at `orbit q i` divided by
`3^(i+1)`. Both the finite prefix and infinite real scalar are
defined directly from those terms. There is no supplied gap stream,
chosen endpoint, abstract scalar with a recurrence axiom, or assumed
ordinary-orbit realization.

The principal equivalence explicitly requires `0<q` and `Odd q`.
This is the accelerated positive odd map. Although some preliminary
lemmas have wider natural-number domains, they do not present the
definition on an even input as the usual even Collatz branch. The
written explanation correctly preserves that distinction.

## Unconditional summability, recurrence, and strict lower bound

For every positive source, the full equation and `q>=1` give
`2^g U(q)=3q+1<=4q`. Positivity justifies every logarithm and its
multiplicative expansion. Dividing by the positive `log 2` gives
`g+logTwo(U(q))<=2+logTwo(q)`.

With `E(q)=1+logTwo(q)/3`, the nonnegativity of `logTwo(U(q))`
then gives `(g+E(U(q)))/3<=E(q)`. Induction bounds every finite
nonnegative prefix by E(q). The infinite-series step uses precisely
the theorem that a nonnegative series with uniformly bounded finite
partial sums is summable. Thus `scalar_summable` is established
before the first-term splitting used for `scalar_recurrence`.
There is no use of a default value assigned to a divergent tsum.

The geometric lower comparison is legitimate because every actual
odd-state gap is at least one, both series are summable, and
`sum_i 3^(-i-1)=1/2`. If the actual scalar equaled one half, its
recurrence and the lower bound at the actual successor would force
gap one and the same half-value at that successor. Induction would
force every actual gap to be one.

The complete equations would then yield
`2^i*(orbit q i+1)=3^i*(q+1)` for every i. Coprimality forces
`2^i | q+1`. Taking `i=q+1` contradicts the positive integer
bound `q+1<2^(q+1)`. This validates the strict lower bound and
retains exactly the ordinary integrality needed to exclude the
negative rational gap-one trajectory.

The finite-tail identity is proved by induction using the actual
orbit shift and scalar recurrence. Its lower and upper bounds use
the scalar bounds at `orbit q n`, divided by the positive `3^n`.
This verifies R10-G1 and the full endpoint intervals in (6)--(7).

## Integer scalar arithmetic forces an actual iterate to one

The defined logarithmic potential is
`log(q)-scalar(q)*log(2)`. Its uniform lower bound follows from
the unconditional scalar upper bound and `log(q)>=0`.

An integral actual scalar stays integral under the proved recurrence.
At every positive odd state, the geometric lower bound then forces
that integer to be at least one. If the actual orbit avoided one,
its positive odd states would all be at least three. The complete
ordinary equation gives the multiplicative factor at most `10/3`;
combining it with the recurrence and the integral lower bound gives
potential decrease at most `log(5/6)<0` at each step.

The induction in `integer_scalar_converges` applies this estimate
to the actual recursively defined orbit. An explicitly chosen
Archimedean index makes the resulting upper bound smaller than the
uniform lower bound. The contradiction yields
`exists i, orbit q i = 1`. Boundedness, periodicity, an escaping
product, and density hypotheses are not assumed. This verifies
R10-G2 and the same actual-map conclusion in its explanation.

## Ternary denominator clearing and the converse

For a supplied equality `scalar(q)=a/3^(r+1)`, the actual recurrence
gives successor numerator `a-gap(q)*3^r` with denominator `3^r`.
The induction in `triadic_scalar_converges` decreases that natural
denominator exponent while advancing the actual source exactly once.
At exponent zero it invokes the proved integer-scalar theorem; the
orbit-shift identity transfers the resulting iterate back to the
original source.

Conversely, the defined map fixes one, its gap there is two, and
the recurrence forces its scalar to be one. Backward induction over
an actual prefix reaching one constructs an integer numerator with
denominator `3^n`. The final theorem is therefore exactly

`Converges q <-> exists a : Int, exists r : Nat, scalar q = a/3^r`

under the stated positive odd hypotheses, with `Converges` itself
defined as reaching one under this same orbit. No merely equivalent
symbolic property is substituted for ordinary convergence. This
verifies R10-G3 and the top-level declaration reproduced in the note.

## Formal and evidentiary boundaries

The final source imports only Mathlib modules. Inspection found no
custom axiom, admitted proof, abstract orbit parameter, or imported
repository convergence theorem. The executing root reports that
this exact final file compiled with default heartbeats,
`warningAsError=true`, and `autoImplicit=false`. The fresh full
declaration dependency audit and publication compile are root's
separate execution receipts. This review is the independent source
and mathematical-scope reconstruction; it does not claim an
additional compiler run by this reviewer.

The written explanation accurately states what the file proves.
The analytic construction and convergence implication are no longer
only finite arithmetic cores under an assumed scalar recurrence.
They are connected to the literal actual infinite series inside
one module. The germ derivative identity, even-source extension,
measure-theoretic laws, and universal production of a triadic scalar
value are explicitly outside this formalization.

The first unsupported assertion remains
`forall positive odd q, scalar q belongs to Z[1/3]`.
The formal equivalence does not assert that right-hand side for an
arbitrary source, and does not prove the full Collatz conjecture.

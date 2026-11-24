# Independent review of the actual-source scalar law

23 November 2026. Reviewer: `density_free_germ8`.
Published parent: `6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Verdict: PASS for the written R9-L1--R9-L5 statements within their
stated actual-source and measure-theoretic scopes. No mathematical
correction is required.**

## Exact reviewed sources

Paths are relative to `research/scalar-rigidity-round9-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `ACTUAL_SCALAR_LAW.md` | `bbab9f86ccfa46929b5aea378e5ea62317caa87a` | `0ee3cca1ef3c1e07bd469edcf208e36fca61b2594b6ebf75e15c6eb03a1ef516` |
| `law_controls.py` | `d52ece5d2e2d41a267e230aab0c29df5211bbc05` | `0741b12e324778da3c502ad8af78c16a104cb8e355ad232b679cea22caf37a50` |

The actual scalar construction and bound are inherited from the pinned
R8-G1--G2 dependency. This reviewer authored that dependency; its separate
independent review is not being claimed again here. The present report
independently reconstructs the new cylinder, distribution, and measure
arguments and inspects the complete control source. Executed control
outputs have the parent's separate receipt.

## 1. Literal cylinders and the finite probability estimate

The terminal-odd congruence retains exactly one more binary bit than
mere terminal integrality. In the reverse induction, the suffix carry
is odd. Reducing the complete congruence modulo `2^(g_0+1)` forces the
first numerator to have exact valuation g_0. Division then gives the
same terminal-odd condition for the suffix. This validates every
intermediate actual positive odd state and the claimed complete word.

For an odd source sampled uniformly through X, the corresponding odd
indices form a consecutive interval of `ceil(X/2)` integers. A gap
word of total A selects one residue among `2^A` such indices. The
count discrepancy is at most one, so the normalized bound is exactly
`1/ceil(X/2)`. This holds for arbitrary positive words, without an
assumption about eventual orbit behavior.

There are `binom(4M,M)` positive M-tuples with sum at most 4M.
Summing their individual discrepancies gives the stated retained-word
bound. The empirical complement differs from the ideal complement
by at most that sum, explaining the factor two after truncation.
For the independent positive geometric variable,
`E[(4/3)^G]=2`; Markov's inequality therefore gives the tail factor
`2^M(3/4)^(4M)=(81/128)^M`.

The actual scalar tail is bounded by
`3^(-M)[1+(bl(X)+M)/3]`, using the literal endpoint inequality
`q_M<=2^M q`. The independent tail has expectation `3^(-M)` because
`EH=1`. These two terms give the first term of R9-L2 exactly. All
constants in its bounded-Lipschitz estimate are thus accounted for.
The proposed choice `M=floor(log_2(X)/8)` makes every term tend to
zero; no limit along a fixed Collatz path is used.

## 2. Singular continuity

The characteristic product follows from independence of the partial
sums and bounded convergence. The estimate
`|psi(u)-1|<=2|u|` makes the deviations from one summable along
`t/3^j`. Every factor is nonzero, so the product at `t=2pi` is
nonzero. At `2pi*3^N`, its first N factors equal one and the remaining
product is unchanged. This is a valid nondecay sequence, and it rules
out absolute continuity by the Riemann--Lebesgue lemma.

That observation alone would not prove pure singularity. The note
supplies the missing step correctly. The countable affine operator
preserves the absolutely continuous part and the singular part:
its countably many singular supports have a null union. Uniqueness
of the fixed probability measure follows by iterating its
characteristic recursion to zero, without a separate moment
assumption on an arbitrary fixed probability. Therefore a normalized
nonzero absolutely continuous part would equal the whole measure,
contradicting the established Fourier nondecay. Its mass must be zero.

The atom argument also closes. A positive supremum of atomic masses
is attained, since only finitely many masses can exceed half that
supremum. At a maximizing atom, support in `[1/2,infinity)` leaves
only finitely many terms in the affine recursion. Their positive
geometric weights sum to less than one, giving a strict contradiction.
Thus the singular measure has no atoms.

## 3. Fixed grids and the countable-union boundary

For fixed positive integer D, the grid `D^(-1)Z` is closed as well
as countable. Atomlessness gives it zero limiting measure. The
Portmanteau inequality for closed sets then proves density zero for
its actual source preimage. Boundedness of this closed set is not
required, so the unbounded grid causes no missing tail argument.

The fixed-D quantifier must remain before the source limit. There is
no contradiction between all these density-zero statements and every
actual scalar lying in the union of the triadic grids. The explicit
random variables consisting of a finite geometric prefix followed by
the scalar-one tail are triadic valued and converge almost surely to
H. This validates the stated warning about weak limits on a dense
countable set. No actual irrational scalar is produced by this proof.

## 4. Primary literature and finite controls

The reviewer independently inspected Tao's primary Definition 1.7,
Proposition 1.9, and its Section 4 cylinder calculation, together with
Solomyak's Section 2 statements and proof mechanisms for pure type
and Fourier nondecay. The cited relationships are accurate. The note
proves its countably supported affine-law argument directly and does
not apply a two-sign Bernoulli-convolution theorem beyond its stated
scope. No uninspected Jessen--Wintner text is imported.

The control program uses exact integers and fractions and explicit
exception-raising checks. Every ordinary replay has a prescribed
finite length; no sampled source is assumed to reach one. Its
composition and progression counts, actual endpoint bounds, and
scalar enclosures match the written proof. The four bounded-Lipschitz
controls are explicitly identified as monotone clipped affine test
functions, not as computational verification of every test function.
The high-depth negative-binomial checks and triadic completion checks
are correctly described as finite controls. Their normal/optimized
execution is recorded by the parent rather than represented as a
fresh execution by this reviewer.

## Remaining scope

These written arguments prove the limiting distribution of actual
scalars across growing source ranges and the fixed-grid consequence.
They are not newly formalized Lean theorems. They supply neither a
stationary law for one fixed ordinary orbit nor its successful
arithmetic certificate. The source-specific carry or approximation
construction remains open, and the paper preserves that boundary.

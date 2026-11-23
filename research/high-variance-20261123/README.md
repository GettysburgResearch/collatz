# High-variance attempts at global Collatz closure

**23 November 2026. Full Collatz remains OPEN.** This checkpoint continues
PR178 at `7e4569476e152f6b8537bdc1711df595ec1ffd89`. Three independent
agents and the coordinating agent pursued four closing routes. The results
below distinguish a formalization, written deductions, source-qualified
consequences, and failed closing steps.

The refresh inspected the 40 most recently updated open PRs and the newly
advanced PR185 packet at `39ba48e6a8af781193e28c679ea8ab64663c3aa6`.
The [source snapshot](SOURCE_SNAPSHOT.json) retains that metadata and the
prior 145-PR inventory's continuation boundary. This was a targeted current
refresh, not another proof audit of every historical packet.

## Outcomes

| Attack | Result in this checkpoint | Exact remaining obligation |
|---|---|---|
| Complete cycle denominator | Lean proves that the literal coprime balanced numerator is a unit modulo the **full** cycle denominator. A written construction produces primitive positive rational cycles above any prescribed real floor, integral at any prescribed finite set of primes. | Exclude integer cycles for arbitrary words, using a word-dependent obstruction retaining every required prime power. |
| Global arithmetic dual | A terminating, explicitly bounded decision procedure verifies or rejects any supplied rational complementary-parity dual of any positive integer. A correct dual supplies a finite paired cycle certificate. | Construct a rational dual for every positive integer; separately exclude nontrivial positive integer cycles. |
| Actual inverse entropy | On the retained hypothetical escape, a single first-ternary-digit log-odds observable diverges, with accumulated cost at least `N log N` asymptotically. The normalized trace has a uniform bilateral profile around the original-source clock. | Prove tightness of that scalar observable along the same ordinary orbit. A global bounded Poisson corrector is refuted by explicit finite ordinary paths. |
| Diophantine and joint renewal | The direct real/2-adic Subspace Theorem product is computed exactly and is at least `1/3`. Growing-precision shell estimates are tested against the retained source. | Obtain a different approximation gain or a bound exploiting the positive ordinary diagonal; an all-cylinder `o(B)` shell bound is false. |

## 1. A formal theorem modulo the entire denominator

For positive integers `A,p`, set

\[
C(A,p)=\sum_{i=0}^{p-1}2^{\lfloor Ai/p\rfloor}3^{p-1-i},
\qquad D(A,p)=2^A-3^p.
\]

The [Lean module](cycles/lean/BalancedCycleUnit.lean) proves

\[
\gcd(A,p)=1,\quad 2^A>3^p
\quad\Longrightarrow\quad \gcd(C(A,p),D(A,p))=1.
\]

It derives the floor-residue permutation and constructs a unit `u` in
`ZMod D` with `u^p=2` and `u^A=3`. The carry factors into a unit power
and the geometric sum `1+u+...+u^(p-1)`, whose product with `u-1` is one.
The final theorem has no supplied permutation, supplied root,
factorization of `D`, or cycle-exclusion premise. A separate corollary
gives `D>1 -> D ∤ C`.

The formalization has **8 theorems and 1 definition**, freshly compiled
with warnings as errors. All nine declarations have an explicit axiom
audit. The balanced S-unit observation is credited to PR185; this packet
does not claim that observation as a new discovery.

The [written cycle construction](cycles/MOVING_PRIME_CYCLE_ATTEMPT.md)
then proves a simultaneous all-parameter statement. For every finite set
of primes `S` and every real `H>0`, there are primitive positive rational
Collatz cycles with every state above `H`, integral at each prime in `S`,
and with the same nontrivial reduced denominator at every state. The
construction keeps the strict positive-cycle cone and uses an elementary
cyclotomic prime-selection argument.

These are rational cycles, not ordinary integer cycles. They show why
fixed finite-prime tests plus an arbitrarily large real minimum cannot
replace the full word-dependent denominator condition. Adaptive inspection
of the actual denominator is not refuted. Infinite prime selection,
rational realization, the real floor and primitivity are independently
reviewed written mathematics; they are not included in the Lean claim.

## 2. A finite decision procedure for a proposed rational dual

The [arithmetic attack](arithmetic/RATIONAL_DUAL_CERTIFICATE.md) starts
with a positive integer `n` and a proposed rational dual `a/d`, where
`d` is positive and odd. It evolves the actual integer `x` and signed
numerator `w`, checking that their parities are opposite.

Before `x` reaches one, negative-numerator steps that remain negative
contract `x|w|` by at least the factor `5/6`. In the positive phase,
steps with `w>d` contract `xw` by

\[
q_d=\frac{2d+3}{2d+4}<1,
\]

while departures from `1<=w<=d` cost at most `(d+3)/4`. There are at
most `d` distinct such small states before a repetition. The proof pays
separately for a negative-to-positive crossing and handles zero before
using a logarithm.

These estimates give an explicit finite event bound. If a small numerator
repeats with different integer states, their difference's 2-adic valuation
gives the exact terminal parity-failure index. If both states repeat,
the literal paired cycle certifies the dual. The exceptional states have
their own finite rules. Thus each supplied rational candidate is decided
without assuming that a long finite parity match continues forever.

Monks–Yazinski's qualitative rationality/escape equivalence is explicitly
credited. The output here is the effective certificate and its signed
product proof, not a proof of the missing universal rationality.
Even an accepted dual allows a nontrivial positive cycle if one exists.
The [exact checker](arithmetic/check_rational_dual.py) and
[retained output](arithmetic/rational-dual-check.json) exercise 2,701
cases, including the predicted terminal rejection after repeated small
numerators. These executions verify the implementation and examples;
the termination theorem is the written argument.

## 3. The entropy attack retains the first arithmetic digit

The [entropy note](entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md) defines

\[
\Xi(q)=\log\frac{K(q,\{x\equiv1\pmod3\})}
                      {K(q,\{x\equiv2\pmod3\})}.
\]

Under the pinned canonical-trace inputs, the probability of the contrary
first predecessor digit is summable along the actual retained escape.
Hence `|Xi(q_j)|` tends to infinity and its accumulated absolute size
has lower asymptotic scale `N log N`; the accumulated row entropy of
that digit is only `o(log N)`. Tightness of this one scalar along the
actual ordinary time laws would contradict escape. That tightness is
not proved.

Paired legal siblings `x` and `4x+1`, or `x` and `16x+5`, have opposite
nonzero ternary digits but exactly the same shifted binary phase. The
existing real-phase theorem therefore does not resolve their canonical
mass comparison by itself.

The same note proves a bilateral normalized-trace profile around the
original-source clock, using the retained source-qualified trace theorem.
It tests a bounded Poisson-corrector completion and refutes that stronger
premise on changing finite ordinary all-ones paths. No infinite escaping
path is manufactured from those finite controls.

## 4. The two-place and renewal applications were tested exactly

The [fourth attack](adelic/TWO_PLACE_AND_RENEWAL_ATTEMPT.md) uses the
same affine correction in its real and 2-adic completions. Even under
an additional algebraicity supposition, the proposed Subspace Theorem
product is exactly a positive tail with first term `1/3`, so it lacks
the required height saving. This does not rule out different
higher-dimensional Diophantine arguments.

For joint real/ternary renewal, every supplied finite shell moment gives
only `q_j^2 <= C 3^j` up to logarithmic factors at the actual moving
precision. An exact all-ones random-prefix control also rules out a
uniform `o(B)` shell-density bound over all ternary cylinders. That
control follows a negative rational fixed point; it does not refute a
stronger estimate restricted to the positive ordinary diagonal. The
missing positive-source restriction remains explicit.

## Verification and continuation boundary

The [report directory](../../reports/2026-11-23-high-variance/README.md)
contains exact source hashes, strict Lean and axiom outputs, independent
review scopes, and replay instructions. The standard complete checkout
gate is repository-integrity evidence, separate from these mathematical
claims. No historical Lean corpus or large old census was replayed.

The next closing obligations are universal rational-dual existence,
arbitrary-word full-denominator exclusion, or ordinary-source tightness
of the canonical digit comparison. None is asserted as proved here.

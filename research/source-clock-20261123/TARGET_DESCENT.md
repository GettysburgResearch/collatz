# Target descent: testing a semigroup lift against the finite boundary

Status: **OPEN**. This is an attempted use of a published global theorem to
force descent of the original target. The calculation below isolates an exact
obligation; it does not establish that obligation or claim Collatz. No new
bounded census was run in this lane.

The shortcut map throughout is

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

## 1. Source pins and the target information actually available

The finite-boundary interface used here is PR #177 at
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_WITNESS.md`,
claims **FB1--FB3** and the final open interface in Section 8. For an odd
target `t = 2B+1`, an actual complete source capturing `t` can be trimmed at
its last state at least `B`. The retained source satisfies

\[
B\leq S<2B,\qquad S\text{ even},\qquad T^j(S)<B\quad(j\geq1).
\]

The exact finite candidate set is

\[
R_B=\{1\leq n<B: T^j(n)<B\text{ for every }j,\quad T^k(n)=1
\text{ for some }k\},
\]

\[
F_B=\{2m:m\in R_B,\ B\leq2m\}.
\]

The supplied complete-grade minimization and same-grade maximum-source
tie-break can therefore be performed over first-hit certificates of this
finite set. This optimization is available for convergent targets as well.
In particular, excluding a lower-grade capturing source is already a property
of the optimizer. It is not additional evidence that the target fails.

The complete-cluster comparison available in our parent is PR #180 at
`04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
`research/high-variance-20261123/GLOBAL_SOURCE_SYNTHESIS.md`. It supplies the
all-length grade budget after deleting a prefix containing a gap four, and
the full two-gap-four source census. It also gives a convergent target that
satisfies the source optimizer and source-floor restrictions. No claim in
this note upgrades those source restrictions to a target obstruction.

For a least positive nonconvergent target `t`, the additional information is
stronger than `T^j(t) >= t`: no forward iterate of `t` can meet a forward
iterate of any `b < t`. Indeed, every such `b` converges, and a meeting would
make `t` converge. Equivalently, every `T^j(t)` has minimum positive ordinary
ancestor exactly `t`. This is an elementary implication of least-target
minimality. It is also the exact first-meeting formulation in Paper 178v1,
*The first meeting with a smaller Collatz orbit*, Section 2,
<https://rstation.ai/problems/collatz/papers/178> (20 November 2026).

The attempted closing step in this lane was to use an unconditional
multiplicative descent theorem to contradict this target information.

## 2. The published global input and what must be lifted

Applegate and Lagarias, *The 3x+1 Semigroup*, Theorem 1.1, prove

\[
\mathcal S=\left\langle2,\frac{2k+1}{3k+2}:k\geq0\right\rangle
=\left\{a/b>0:\gcd(a,b)=1,\ 3\nmid b\right\}.
\]

Consequently, in the inverse semigroup

\[
\mathcal W=\mathcal S^{-1}
=\left\langle\frac12,\frac{3u+1}{2u}:u\geq1\text{ odd}\right\rangle,
\]

the element `1/t` exists for every positive integer `t`. Thus some finite
product of these generators takes `t` multiplicatively to `1`.

Primary source: <https://arxiv.org/html/math/0411140v2>, Theorem 1.1 and
Section 2; journal reference *Journal of Number Theory* 117 (2006), 147--159.
The repository already cites this theorem as external context in
`research/astra-critical-mass/REMAINDER_CANCELLATION.md`, Section 8, and
`research/astra-critical-mass/CLOCK_DEFECT.md`, Section 7, both at the parent
commit above. The semigroup theorem is not a new result of this packet.

There are two separate obligations before such a factorization becomes a
Collatz descent certificate:

1. Choose an ordering whose intermediate multiplicative states are positive
   integers.
2. Prove that the generator chosen at each step agrees with the parity of
   the **actual original-target iterate** at that step.

The semigroup theorem asserts neither obligation. The exact calculation below
allows even multipliers at odd generators; it does not silently require the
multiplicative states themselves to have the generator's parity.

## 3. TD1: exact discrepancy for every integral word

**Locally proved, not Lean-formalized in this note.** Let
`z_0 = t, z_1, ..., z_N` be positive integers obtained by a specified ordered
word in the generators of `W`. Write `b_i = 0` for a factor `1/2` and
`b_i = 1` for a factor `(3u_i+1)/(2u_i)`, where `u_i` is positive and odd.

For each odd generator, integrality forces `u_i | z_i`, since
`gcd(u_i, (3u_i+1)/2) = 1`. Put `m_i = z_i/u_i >= 1`. Then

\[
z_{i+1}=\frac{3z_i+m_i}{2}\qquad(b_i=1),
\]

whereas a halving factor gives `z_{i+1} = z_i/2`.

Let `x_i = T^i(t)`. Suppose the actual parities agree with the generator
labels for all `0 <= i < N`: `x_i mod 2 = b_i`. Define
`D_i = z_i-x_i`. Direct subtraction gives the exact recurrence

\[
D_0=0,\qquad
D_{i+1}=\begin{cases}
D_i/2&b_i=0,\\
(3D_i+m_i-1)/2&b_i=1.
\end{cases}                                                    \tag{TD1a}
\]

In particular `D_i >= 0` for every `i`. If
`h_i = sum_{i < j < N} b_j`, expansion of this recurrence gives

\[
2^N D_N=
\sum_{\substack{0\leq i<N\\b_i=1}}
(m_i-1)2^i3^{h_i}.                                               \tag{TD1b}
\]

This formula follows by induction on the word length: an even final step
doubles the denominator and changes no numerator weight, while an odd final
step multiplies the old numerator by three and appends the term
`(m_{N-1}-1)2^(N-1)`. Every summand is nonnegative. Any occurrence of
`m_i > 1` makes the discrepancy strictly positive at the end.

### TD2: rigidity at endpoint one

If the integral multiplicative word ends at `z_N = 1` and matches every
actual target parity, positivity of `x_N` gives

\[
0\leq D_N=1-x_N\leq0.
\]

Therefore `x_N = 1`, and (TD1b) forces `m_i = 1` at every odd generator.
Now (TD1a) gives `D_i = 0` at every time. In other words, such a word was
already the ordinary orbit, with `u_i = x_i = z_i` at every odd step.

This is an all-length rigidity statement, not an assertion that no useful
prefix of a semigroup word can be lifted. A prefix ending at an integer
`q < t` would suffice for induction. More generally, if `z_N = q` and all
parities match, the exact budget is

\[
0\leq
\sum_{b_i=1}(m_i-1)2^i3^{h_i}
\leq2^N(q-1).                                                   \tag{TD2a}
\]

The endpoint-one result shows that importing the published factorization
and then demanding parity agreement throughout does not supply an easier
completion. Its nontrivial scaled steps would all have to disappear.

## 4. TD3: the exact target-dependent repair still required

Suppose `t` is a least nonconvergent target. Take any integral semigroup word
from `t` and let `r` be its first time with `z_r < t`. There must be an index
`i < r` at which the chosen generator label differs from the actual parity
of `T^i(t)`. Otherwise (TD1a) would give

\[
T^r(t)=z_r-D_r\leq z_r<t,
\]

contradicting least-target minimality.

Thus a successful use of the semigroup theorem must do more than exhibit
an integral product of ratio less than one. It must repair the first
actual-target parity disagreement, possibly by reordering or replacing
generators, while retaining a descent endpoint and preserving every earlier
parity guard.

The first unsupported step of this attack is precisely:

> For every least-bad target `t`, there is a finite ordered positive-integral
> semigroup descent from `t` for which the actual parity guards all hold
> through the first multiplicative state below `t`.

No such repair theorem is proved here. Positivity of the discrepancy alone
does not establish any next parity. Nor can convergence of a smaller
discrepancy be added to convergence of another integer: the required closure
of the Collatz basin under addition is unproved. The exact sum-carry issue
is already documented in PR #178 at
`2169884b64871b448cda16c7d74a0d5914ed870b`,
`research/high-variance-20261123/arithmetic/RATIONAL_DUAL_CERTIFICATE.md`.

The finite source boundary does not repair this step. It describes complete
source certificates and their grades; none of its edges determines the
parity of the original target after an independently chosen semigroup
factor. To use the boundary here, one would need an additional proved bridge
from a failed parity guard to either an actual meeting with a smaller target
or a legal lower-grade source capturing `t`, with its complete word and
initial halving exponent retained. This lane has not produced that bridge.

## 5. Outcome and validation scope

The attack tested a global, unconditional published theorem rather than
another finite source census. TD1--TD3 are exact elementary implications
with full proofs above. They were checked algebraically; no claim is made
that Lean has checked them. They identify the original-target parity repair
that a semigroup-based completion would have to supply, and the endpoint-one
rigidity prevents a spurious shortcut through the published weak theorem.

There is no proved all-target descent, no all-scale cover, and no new
Collatz completion in this lane. No numerical search result is used as
evidence for any universal statement.

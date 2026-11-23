# Prime potentials and the complete cycle denominator

Date: 23 November 2026. **The positive integer cycle problem remains open.**

This pass tried to turn original integer closure into an upper bound on the
complete reduced denominator of the complementary cycle. The paired affine
identities below did not provide that bound. A second route, through arbitrary
prime weights, does yield a definite result: **every globally nonincreasing
completely additive potential is constant on the odd integers prime to three**.
This is a source-qualified consequence of the Applegate–Lagarias semigroup
theorem. It applies even to potentials valued in an ordered abelian group,
including a finite lexicographic vector of prime features.

A separate five-edge certificate proves the strict-decrease obstruction
without importing that literature theorem. Its actual integer edges, product
balance, additive contradiction, and fixed-word factorization are checked in
Lean. None of these statements excludes a nontrivial Collatz cycle.

## 1. Maps, scope, and current inputs

Use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\]

and its accelerated odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\qquad(n>0\text{ odd}).
\]

A completely additive potential satisfies \(F(ab)=F(a)+F(b)\) for positive
integers. Its prime weights are unrestricted; no finite prime set, degree
bound, boundedness, continuity, or sign condition on those weights is assumed.
“Globally nonincreasing” below means the inequality holds on **every** indicated
positive ordinary edge. It does not mean merely the edges of an unknown cycle,
or merely all edges above some unspecified verified floor.

The current inputs were consulted at these exact heads; they are not newly
proved or generally re-reviewed by this packet:

| Source | Frozen head | Relevant boundary |
|---|---|---|
| PR180, `ARITHMETIC_CLOSURE.md` | `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161` | The complementary reduced denominator has a stronger lower budget; no closing upper bound follows. |
| PR182, `CYCLE_RIGIDITY.md` | `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c` | All rotated integral equations retain the same full gcd; choosing the least root creates no independent rarity factor. |
| PR176, `CYCLE_PRODUCT_TRANSFER_ATTEMPT.md` | `4171e1fe40e41842af9f800bd821084b724cf8f9` | Actual rational one-rise cycles at arbitrary floors attain maximal multiplicative products, so expansion alone does not supply integral closure. |
| PR177, `POSITIVE_CARRY_CLOSURE_ATTEMPT.md` | `f47a5ec51aa5853f104013a6d5046d6220ff7423` | The finite local-energy obstruction keeps the whole numerical gcd visible; its rational controls do not solve integrality. |

The retained local input is
[`COMPLEMENTARY_DENOMINATOR_CAPACITY.md`](../../central-step-20261123/cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md):
a nontrivial positive integer shortcut cycle of primitive period \(K\) has
complementary reduced denominator \(q>K/2\). The source ledger records full
paths and content hashes. This pass seeks an opposite arithmetic constraint,
not another lower bound on \(q\).

## 2. A finite circulation of actual integer edges

The following are exact accelerated steps:

| Source \(n\) | Exact exponent \(a=v_2(3n+1)\) | Successor \(U(n)\) |
|---:|---:|---:|
| 25 | 2 | 19 |
| 19 | 1 | 29 |
| 29 | 3 | 11 |
| 55 | 1 | 83 |
| 83 | 1 | 125 |

They form two open paths,

\[
25\longrightarrow19\longrightarrow29\longrightarrow11,
\qquad 55\longrightarrow83\longrightarrow125.
\tag{1}
\]

Every displayed integer is positive, odd, and prime to three. The five sources
are distinct; their minimum is 19. The endpoint products agree:

\[
25\cdot55=11\cdot125=1375.
\tag{2}
\]

Consequently, with \(S=\{19,25,29,55,83\}\),

\[
\prod_{n\in S}U(n)=\prod_{n\in S}n,
\qquad
\prod_{n\in S}(3n+1)=2^8\prod_{n\in S}n.
\tag{3}
\]

This is complete balance at **every prime**, using genuine integer edges.
It is not state balance: \(11,125\notin S\), so \(U(S)\ne S\). In particular
(3) must not be called an integer cycle.

### Proposition 1 — arbitrary additive weights cannot strictly decrease

For any real-valued completely additive \(F\), the five edge changes have sum
zero:

\[
\begin{split}
&(F(19)-F(25))+(F(29)-F(19))+(F(11)-F(29))\\
&\qquad +(F(83)-F(55))+(F(125)-F(83))=0.
\end{split}
\tag{4}
\]

Indeed, cancellation reduces the left side to
\(F(11)+F(125)-F(25)-F(55)\), and (2) makes this zero. If all five changes
are nonpositive, each is zero. They cannot all be strictly negative; in fact
weak decrease on all five forbids strict decrease on even one of them.

Thus a globally strictly decreasing prime-weight potential fails regardless
of how its infinitely many weights are chosen. The certificate involves no
rational or 2-adic replacement for an ordinary source. It also refutes a proof
that substitutes prime-product balance for permutation closure of the state
set. It does not refute an argument that retains that extra closure.

All sources are at least 19, but one successor is 11. Accordingly, the
source-only strict-edge statement fails already at source floor 19. If a
method requires inequalities only on edges whose **two** endpoints remain
above a floor, this certificate applies through floor 11. It makes no claim
at every floor.

## 3. Classification using the primary semigroup theorem

The sole external mathematical input here is Applegate–Lagarias,
[*The 3x+1 semigroup*, Theorem 1.1](https://arxiv.org/pdf/math/0411140v2),
*Journal of Number Theory* **117** (2006), 146–159. Their semigroup

\[
\mathcal S=\left\langle 2,\frac{2k+1}{3k+2}:k\ge0\right\rangle
\]

consists exactly of positive rationals whose reduced denominator is prime to
three. Equivalently its inverse semigroup

\[
\mathcal W=\left\langle\frac12,\frac{3k+2}{2k+1}:k\ge0\right\rangle
\tag{5}
\]

consists exactly of positive rationals whose reduced numerator is prime to
three. The quoted result concerns multiplicative representations, not
concatenated ordinary trajectories. Its representations have no stipulated
lower bound on their sources. We use precisely that theorem, with no claim
that its proof or the theorem has been formalized here.

### Theorem 2 — classification on odd integers prime to three

**Status: SOURCE-QUALIFIED**, using the primary theorem just stated and the
following argument.

Let \(G\) be an ordered abelian group, with translation-invariant order, and
let \(F\) be completely additive with values in \(G\). Suppose

\[
F(U(n))\le F(n)\quad\text{for every positive odd }n\text{ with }3\nmid n.
\tag{6}
\]

Then

\[
\boxed{F(n)=0\quad\text{for every positive odd }n\text{ prime to three}.}
\tag{7}
\]

**Proof.** Replace \(F(n)\) on general positive integers by
\(H(n)=F(\operatorname{oddpart}(n))\). This leaves the values on odd
integers unchanged and sets \(H(2)=0\). Extend it multiplicatively to positive
rationals by \(H(a/b)=H(a)-H(b)\), a well-defined additive homomorphism.

For an odd source \(n=2k+1\), the generator in (5) is
\(g_n=(3n+1)/(2n)\). It satisfies

\[
v_3(g_n)=-v_3(n)\le0.
\tag{8}
\]

Fix a prime \(p\ne2,3\). By the primary theorem, both \(p\) and \(1/p\)
have finite representations by the generators (5). Each representation has
total 3-adic valuation zero. Since every summand in that valuation is
nonpositive, each odd source appearing in it is prime to three. Thus (6)
applies to each of these sources. Removing powers of two gives

\[
H(g_n)=F(U(n))-F(n)\le0,
\qquad H(1/2)=0.
\]

Adding along the representations of \(p\) and \(1/p\) yields respectively
\(F(p)\le0\) and \(-F(p)\le0\). Antisymmetry gives \(F(p)=0\).
Complete additivity now proves (7). No representation is asserted to be a
physical orbit. Only each individual generator is evaluated at its genuine
ordinary source. \(\square\)

The proof uses no Archimedean property. In particular, a finite lexicographic
vector of real completely additive features also vanishes on the odd integers
prime to three if it is globally nonincreasing in lexicographic order. This
does not cover nonlinear features, state-dependent weights, or a rank using
noncommutative ordinal addition.

### Corollary 3 — all globally nonincreasing additive potentials

If (6) holds for **all** positive odd sources, including multiples of three,
then on odd integers the exact classification is

\[
\boxed{F(n)=v_3(n)c\quad\text{with }c=F(3)\ge0.}
\tag{9}
\]

Theorem 2 kills every other odd prime weight. The edge \(3\to5\) gives
\(0=F(5)\le F(3)\). Conversely \(U(n)\) is always prime to three, so (9)
is indeed nonincreasing. The value on the even prime is unconstrained if only
odd accelerated steps are under consideration.

If instead \(F(T(n))\le F(n)\) holds on **every positive shortcut step**,
then exactly the same formula (9) holds for all positive integers. To prove
this, concatenate the shortcut inequalities to obtain the odd accelerated
ones. Then \(F(5)=0\). The even step \(2\to1\) gives \(F(2)\ge0\), while
\(5\to8\) gives \(3F(2)\le0\). Hence \(F(2)=0\). The converse follows
because a halving preserves \(v_3\), and an odd step sends it to zero.

For the last implication in a partially ordered group, note that
\(F(2)\ge0\) implies \(0\le F(2)\le3F(2)\le0\); total order is unnecessary.

Every state in a positive periodic orbit is prime to three: the orbit must
contain an odd step, which removes divisibility by three, and no step can
restore it. Thus every potential in (9) is identically zero on every such
orbit, including a hypothetical nontrivial one.

## 4. Why this does not yield an arbitrary-floor obstruction

The fixed words in (1), with variable starting values, have affine endpoints

\[
P(x)=\frac{27x+29}{64},\qquad Q(y)=\frac{9y+5}{4}.
\]

Their endpoint-product condition is exactly

\[
P(x)Q(y)=xy
\iff(13x-261)(13y-135)=37120=256\cdot5\cdot29.
\tag{10}
\]

This factorization is also checked in Lean over the integers. For positive
solutions, the unfactored equation gives
\((13x-261)y=135x+145>0\) and
\((13y-135)x=261y+145>0\). Both factors in (10) are therefore positive
integer divisors of a fixed nonzero integer. There are only finitely many
positive integer endpoint pairs, even before imposing the exact parity
conditions for the words. The fixed words cannot supply arbitrary floors.

Likewise, the representations supplied by Theorem 1.1 of Applegate–Lagarias
may use small sources. A deleted-initial-generators theorem is not one of its
stated conclusions. To obtain an all-floor version by this route, a sufficient
new statement would be:

> **OPEN tail-circulation statement.** For every \(M\), some nonempty finite
> multiset of actual odd edges has every source and successor above \(M\),
> and the product of the sources equals the product of the successors.

No such statement is proved or inferred here. One would also need to specify
which edges a proposed eventual potential must treat strictly; a positive
circulation only obstructs the corresponding strict or charged requirement.

## 5. The tested full-denominator attack

Let \(x_i\) be a hypothetical nontrivial positive integer shortcut cycle of
primitive period \(K\), with \(p\) odd and \(b=K-p\) even steps. Let \(y_i\)
be its positive rational complementary cycle, as in the retained capacity
packet. If \(e_i\in\{0,1\}\) is the original parity, the paired updates are

\[
\begin{array}{c|cc}
e_i&x_{i+1}&y_{i+1}\\\hline
0&x_i/2&(3y_i+1)/2\\
1&(3x_i+1)/2&y_i/2.
\end{array}
\]

Both branches give the exact bilinear identity

\[
4x_{i+1}y_{i+1}=3x_i y_i+(1-e_i)x_i+e_i y_i.
\]

Summing around the full cycle yields

\[
\sum_i x_i y_i=\sum_{e_i=0}x_i+\sum_{e_i=1}y_i.
\tag{11}
\]

Write \(y_i=u_i/q\) in lowest terms with common reduced denominator \(q\).
Then (11) is the integer equation

\[
q\sum_{e_i=0}x_i=\sum_i x_i u_i-\sum_{e_i=1}u_i.
\tag{12}
\]

The attempt was to combine these identities and all original integer
rotations to force large common content in the complementary carry. The full
quantity is

\[
\Delta=2^K-3^b>0,\quad
g=\gcd(\Delta,C_*),\quad q=\Delta/g.
\tag{13}
\]

Here \(C_*\) is the **complete numerical complementary carry**, not a
polynomial, partial factor, or selected block. The previous capacity bound
is \(q>K/2\). One exact sufficient closing line would be

\[
\boxed{\gcd(2^K-3^b,C_*)\ge\frac{2(2^K-3^b)}K.}
\tag{14 — OPEN}
\]

It would give \(q\le K/2\), a contradiction. The original full integer
closure must be used essentially to obtain (14); its validity has not been
established. Equation (12) supplies no independent upper bound because the
integer numerators \(u_i\) also depend on \(q\). Rewriting (12) as a formula
for \(q\) therefore does not prove (14). The all-rotation gap identities in
PR182 retain the same full gcd rather than producing extra independent
integrality conditions. The bilinear calculation and the semigroup
classification do not change that boundary.

The arithmetic result of this pass is consequently the exact exclusion of a
global additive-prime descent mechanism, together with the explicit point
where the attempted full-denominator closure still needs new information.

## 6. Formalization and reproducibility

[`PrimePotentialCirculation.lean`](PrimePotentialCirculation.lean) defines a
genuine odd-to-odd integer edge by positivity, oddness of both endpoints, and
\(3n+1=2^a m\) with \(a>0\). Since \(m\) is odd, the displayed exponent
is exact. It proves the five edges, endpoint and full product balance, the
additive identities, forced flatness, the strict global obstruction, and
(10). The audit prints the axiom dependencies of all 12 declarations.

The new two-module build uses Lean 4.34.1 with `autoImplicit=false` and
`warningAsError=true`, against the pinned mathlib objects. The compiler and
audit both exited zero. The axiom union is only `propext`, `Classical.choice`,
and `Quot.sound`; there is no `sorryAx`. The global semigroup classification,
its ordered-group extension, and the complete-denominator attempt are written
mathematics, not new Lean theorems. The exact receipt is
[`cycles-lean-receipt.json`](../../../reports/2026-11-23-reassessment/cycles-lean-receipt.json).

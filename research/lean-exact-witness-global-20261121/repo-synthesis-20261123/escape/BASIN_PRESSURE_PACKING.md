# Critical root summability of the actual sibling Green ratios

23 November 2026. **Written theorem on one unchanged hypothetical escaping
ordinary component; escape exclusion remains OPEN.** The new input is the
ordinary first-hit bound [BM3](SPARSE_BASIN_MINIMA.md). It gives a strict
power saving for the number of disjoint sibling basins that contain any
small ordinary source. This converts the previous summability of Green
ratios into summability of their **s-th roots**, for every s>1. No
predecessor-density assertion, Haar law, stationary limit, or random gap
model is required.

The finite graph, actual first-hit implication, and complete source-cutoff
accounting are formalized in `BasinPacking.lean`. Infinite sums and real
power estimates below are written mathematics; they are not silently
included in that finite Lean scope.

## 1. Retain the original component and every upper sibling

Use the shortcut T and odd map U from the companion note. Fix an escaping
eventual-meeting component E of positive odd ternary units. The parent
packet proves, by an elementary ordinary-orbit count,

\[
r(n)=\frac1n\prod_{k\ge0}\frac{3U^kn}{3U^kn+1},\qquad
\frac{c_*}{n}\le r(n)\le\frac1n,
\qquad c_*=e^{-160/3}>0.
\tag{BP1}
\]

Its exact edge identity is
\(r(n)=(3/2^{a(n)})r(Un)\). For s>1 put

\[
M_s=\sum_{n\in E}r(n)^s<\infty,\qquad
A_s(q)=\sum_{\substack{n\in E\\U^kn=q\text{ for some }k}}r(n)^s.
\tag{BP2}
\]

Every root is nonperiodic, so each ancestor has a unique hitting depth.
For the unchanged inverse operator

\[
P_sf(q)=\sum_{\substack{e\ge1\\(2^eq-1)/3\text{ a positive odd unit}}}
\left(\frac3{2^e}\right)^s f((2^eq-1)/3),
\qquad Z_s(q)=\sum_{k\ge0}P_s^k1(q),
\]

the exact source identity is

\[
A_s(q)=r(q)^s Z_s(q).
\tag{BP3}
\]

Let q_j=U^j(q_0), S(q)=64q+21, and v_{j,b}=S^b(q_j), b>=1.
Write B_{j,b} for the unit-odd predecessor set of v_{j,b}, and

\[
b_{j,b}=\sum_{n\in B_{j,b}}r(n)^s,\qquad
a_s=A_s(q_0)>0,\qquad
R_{j,b}=\frac{Z_s(S^bq_j)}{Z_s(q_j)}.
\]

All B_{j,b} are disjoint. They lie in the disjoint **full shortcut
basins** used in BM3. In particular, if B_{j,b} meets [1,X], then the
minimum of its full shortcut basin is at most X. That full minimum may
be divisible by three; it is not substituted for a unit-pressure atom.

Since r(S^bq)=64^{-b}r(q), and the predecessor sets of q_j increase,

\[
\boxed{\quad
\beta_{j,b}:=64^{-bs}R_{j,b}
=\frac{b_{j,b}}{A_s(q_j)}\le\frac{b_{j,b}}{a_s}.
\quad}
\tag{BP4}
\]

Every term keeps the same original component and the same q_0. No
normalization of the operator rows is made.

## 2. The finite cutoff inequality retains the entire source tail

Let F be any finite family of disjoint basins, each with s-mass at least
lambda>0. Let K(X) be an upper bound for the number of those basins that
meet the ordinary integers [1,X], with integer X>=1. All the other
basins draw their entire mass from integers greater than X. Therefore

\[
\boxed{
(|F|-K(X))_+\lambda
\le\sum_{n>X}n^{-s}\le\frac{X^{1-s}}{s-1}.
}
\tag{BP5}
\]

The same inequality with the actual tail sum is valid for any finite
source pool, and is the statement checked by Lean. Disjointness is used
both when counting low sources and when summing the tail. Dropping a
tail atom or charging one source to two basins invalidates it.

For arbitrary partitions one can take K(X)<=X. This alone gives decreasing
rearrangement b_N^*=O_s(N^{-s}), and no stronger universal exponent:
singleton groups with weights n^{-s} attain that exponent. Real Collatz
basins supply additional information. BM3 gives uniformly

\[
K(X)\le12X^\eta,\qquad\eta=799/800<1.
\tag{BP6}
\]

The saving concerns the **number of basins touched**, not the number of
sources inside a single basin.

Combining BP5 and BP6 gives an exact distribution-function estimate

\[
\boxed{
\#\{(j,b):b_{j,b}\ge\lambda\}
\le12X^\eta+\frac{X^{1-s}}{(s-1)\lambda}
\qquad(X\in\mathbb Z_{\ge1}).
}
\tag{BP7}
\]

First apply BP5 to every finite subset of the displayed level set; its
bound is independent of that subset. This proves BP7 even before knowing
that the level set is finite. Choosing X of order
lambda^{-1/(s+eta-1)} proves

\[
\boxed{
b_N^*=O_s(N^{-\kappa_s}),\qquad
\kappa_s=1+\frac{s-1}{\eta}>s.
}
\tag{BP8}
\]

For lambda>1, finiteness follows from total mass, and the finitely many
large levels can be absorbed into the constant. For small lambda the
choice X=ceil(lambda^{-1/(s+eta-1)}) is legitimate. Equivalently,
one can choose X of order N^{1/eta} in BP5 so that the low-source term
is at most N/2. BP4 gives the same rearrangement exponent for all the
normalized beta_{j,b}, with a constant also depending on a_s.

## 3. An explicit sum bound, including the critical s-th root

For 0<p<1, split the ordinary sources into dyadic shells
D_k=[2^k,2^{k+1}), k>=0. Put

\[
b_{i,k}=\sum_{n\in B_i\cap D_k}r(n)^s,
\qquad i=(j,b).
\]

There are at most 12(2^{k+1})^eta nonzero terms in that shell. Their
sum is at most 2^{k(1-s)}, because D_k contains 2^k integers and
each weighs at most 2^{-ks}. Concavity, on this actual finite list,
gives

\[
\sum_i b_{i,k}^p
\le (12\,2^\eta)^{1-p}
 2^{k[\eta-p(s+\eta-1)]}.
\tag{BP9}
\]

Since (sum_k x_k)^p <= sum_k x_k^p for nonnegative x_k, Tonelli now
proves the explicit inequality

\[
\boxed{
\sum_i b_i^p
\le\frac{(12\,2^\eta)^{1-p}}
 {1-2^{\eta-p(s+\eta-1)}}<\infty
\quad\text{when }\frac{\eta}{s+\eta-1}<p<1.
}
\tag{BP10}
\]

Only the elementary finite concavity inequality is applied before
nonnegative limits. There is no replacement by a uniform law on words,
ancestors, or boxes. Powers p>=1 are also summable by total finite mass
and boundedness. Thus the allowed range is all p>1/kappa_s.

The crucial new endpoint is p=1/s. Because eta<1 and s>1,
1/s>eta/(s+eta-1), so it is inside the proved range. BP4 gives

\[
\boxed{
\sum_{j\ge0}\sum_{b\ge1}
64^{-b}\left(\frac{Z_s(S^bq_j)}{Z_s(q_j)}\right)^{1/s}
\le
\frac{a_s^{-1/s}(12\,2^\eta)^{1-1/s}}
 {1-2^{-(1-\eta)(1-1/s)}}<\infty.
}
\tag{BP11}
\]

For s=2, kappa_2=1599/799>2. In particular,

\[
\boxed{\sum_{j\ge0}
 \sqrt{Z_2(64q_j+21)/Z_2(q_j)}<\infty.}
\tag{BP12}
\]

The prior checkpoint proved summability of the ratios themselves. BP12
proves the strictly stronger square-root summability, using ordinary
first-hit dynamics to go beyond generic partition bounds.

## 4. What comparison would now exclude escape

The actual growth bound is q_j+1<=(3/2)^j(q_0+1). Therefore

\[
\sum_j\frac1{(1+\log(q_j+1))\log(2+\log(q_j+1))}=\infty.
\tag{BP13}
\]

Combining BP11 with BP13 shows that the following comparison, if proved
on every escaping ray for one fixed s>1 and c>0, would exclude escape:

\[
\boxed{
Z_s(64q+21)\ge
\frac{c\,Z_s(q)}
 {[(1+\log(q+1))\log(2+\log(q+1))]^s}
\quad\text{eventually on that ray.}
}
\tag{HC-new}
\]

Taking the s-th root gives the divergent series in BP13, contradicting
BP11. This comparison is **OPEN**. Its scale is weaker than the previous
comparison with only the first power of that denominator. More generally,
a lower bound c/(1+log(q+1))^a for the ratio suffices whenever
a<kappa_s: choose p>1/kappa_s with ap<=1 and use BP10.

The result concerns escape. Even a proof of HC-new would leave
nontrivial positive cycles as a separate obligation.

## 5. The actual integer cost of a proposed repair

BM3 also yields a source-rank budget without pressure normalization.
For the full minima m_i of all the sibling basins, Tonelli gives

\[
\boxed{
\sum_i\frac1{m_i}
=\int_1^\infty\#\{i:m_i\le X\}X^{-2}\,dX
\le\frac{12}{1-\eta}=9600.
}
\tag{BP14}
\]

Every choice of one actual positive ancestor n_i from each distinct
basin has n_i>=m_i, so sum_i 1/n_i<=9600 too. This conclusion does not
use an inherited predecessor-population theorem.

Consequently, a universal repair that produces an ordinary ancestor of
S q_j at height O((j+1) log(j+2)) along the same escaping ray would
contradict BP14. More generally BM3 implies

\[
\sum_i m_i^{-t}\le\frac{12t}{t-\eta}\quad(t>\eta),
\tag{BP15}
\]

so a bound n_j=O((j+1)^d) with d<1/eta is already impossible on an
escaping ray. This gives a precise arithmetic consumer for an ordinary
integer repair of a bounded rational inverse leaf. A bounded rational
leaf, or finite congruence compatibility, does not supply that repair.

The existing balanced inverse compiler gives an actual ancestor n'_j
in the basin of S q_j when it transports the real inverse word from
q_j back to the fixed q_0. Its exact signed exponent cost Delta_j obeys

\[
2^{\Delta_j}
=\frac{q_j}{Sq_j}\frac{n'_j}{q_0}
 \frac{\Lambda(q_0,q_j)}{\Lambda(n'_j,Sq_j)}.
\tag{BP16}
\]

Both correction products lie in [c_*,1]. Thus n'_j is comparable to
q_0 2^{Delta_j}, with fixed constants independent of j. BP15 implies
sum_j 2^{-t Delta_j}<infinity for every t>eta. This is the actual
ordinary cost that a claimed favorable signed-cost cancellation would
have to overcome. No centering, independence, or low-cost bound on this
compiler is inferred from the existence of positive and negative edges.

## 6. Sharp controls and what was not imported

The exponent in the generic packing step is sharp under its stated
information. Abstract groups B_j=[j^2,(j+1)^2) have minimum count of
order X^{1/2}. Give integer n the telescoping weight
1/[n(n+1)]<=n^{-2}. Then exactly

\[
b_j=1/j^2-1/(j+1)^2
=\frac{2j+1}{j^2(j+1)^2}\asymp j^{-3}.
\]

This attains kappa=1+(2-1)/(1/2)=3. These groups are not claimed to be
Collatz basins. Singleton groups similarly attain the earlier generic
exponent s. The new strict improvement therefore comes from BM3, not
from an incorrect claim that arbitrary regrouping improves summability.

The latest PR175 complete-carry transfer and PR180 exact iid Renyi
spectrum were inspected. They do not supply HC-new on the unchanged
ordinary ray. PR180's qualified predecessor-density input would give a
different antichain-minimum argument, but it is **not a premise** here:
BM3 and the elementary source cutoff replace it. The stronger external
interval-compression manuscript found during the repository comparison
is likewise unnecessary.

`check_basin_packing.py` checks finite actual predecessor sets, the first-hit
minimum condition, the exact integer height inequality, source-cutoff
accounting, and the sharp abstract control. Its actual examples converge;
they are finite arithmetic controls, not simulations of an escaping ray.
The formal declarations and execution receipts are listed in the report.
The infinite pressure theorem is conditional only on the hypothetical
escaping component it constrains, with BM3 proved unconditionally for
any such injective ordinary ray.

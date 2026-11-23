# The complete off-spine kernel has summable capacity increments

23 November 2026. **Written all-branch extension on one unchanged hypothetical
escaping ordinary component.** Every positive odd unit inverse parent is
retained, including lower-exponent parents and both legal ternary colours.
The result strengthens the upper-sibling theorem to the complete inverse
kernel. It does not prove a lower Green comparison or exclude escape.

Use the maps, component E, weights r, and unnormalized masses A_s from
[`BASIN_PRESSURE_PACKING.md`](BASIN_PRESSURE_PACKING.md), BP1–BP3.
In particular c_*/n<=r(n)<=1/n, s>1, and q_j=U^j(q_0) is the original
injective odd ray. Put a_j=v_2(3q_j+1).

## 1. Every inverse branch and the exact component partition

For every j>=0, take **all** exponents e>=1 for which

\[
v_{j,e}=\frac{2^e q_{j+1}-1}{3}
\]

is a positive odd ternary unit, except the unique spine exponent e=a_j.
There is no upper cutoff on e. Denote this index family by I, and let

\[
B_{j,e}=\{n\in E:U^k n=v_{j,e}\text{ for some }k\ge0\},
\qquad b_{j,e}=\sum_{n\in B_{j,e}}r(n)^s.
\tag{AC1}
\]

These roots are distinct and off the entire ray. Applying U to an
equality v_{j,e}=q_i would give q_{j+1}=q_{i+1}, hence i=j and
e=a_j, which was excluded. An off-ray root enters the ray at its next
odd step; its intervening shortcut states are even. Thus these roots
are pairwise incomparable under T, and their full positive shortcut
basins are disjoint.

There is also a complete partition of the unchanged unit component:

\[
\boxed{
E=\operatorname{Pred}_U(q_0)
\ \sqcup\ \{q_j:j\ge1\}
\ \sqcup\ \bigsqcup_{(j,e)\in I} B_{j,e}.
}
\tag{AC2}
\]

To prove coverage, take any n in E and its first hit of the original
odd ray. If it hits q_0, it is in Pred_U(q_0). If n is itself a later
ray point, it is in the displayed singleton family. Otherwise the
state immediately before its first hit of q_{j+1}, j>=0, is one of
the roots in AC1. That state cannot be q_j, since that would be an
earlier hit of the ray. All the alternatives are disjoint by the
same deterministic-path argument. This is a partition of E, not of
all positive integers.

Consequently the full tree identity is

\[
\boxed{
A_s(q_{j+1})-A_s(q_j)
=r(q_{j+1})^s+\sum_{e:(j,e)\in I}b_{j,e}.
}
\tag{AC3}
\]

It includes the new root atom. No discarded parent or external source
distribution is hidden in this equality.

## 2. Count all these roots, then their ordinary basin minima

Write beta=39/40. If v_{j,e}<=Y with Y>=1, then

\[
q_{j+1}\le\frac{3Y+1}{2^e}\le\frac{4Y}{2^e}.
\]

The inherited elementary count of the same injective odd ray gives

\[
\begin{aligned}
\#\{(j,e)\in I:v_{j,e}\le Y\}
&\le4(4Y)^\beta\sum_{e\ge1}2^{-e\beta}\\
&=\frac{4\,4^\beta}{2^\beta-1}Y^\beta
<24Y^\beta.
\end{aligned}
\tag{AC4}
\]

Terms whose argument is below one contribute zero. The final constant
uses beta>3/4 and 2^(3/4)>5/3, the latter following from 8*81>625.
Integrality, the unit guard and exclusion of the spine parent only
reduce this upper count.

For each root let m_{j,e} be its full positive shortcut basin minimum,
as in BM2. Apply the general first-hit split BM4 with
H=floor(log_2 X/25). Its no-descent contribution is at most

\[
X^{8/125}+2^{1/32}X^{799/800}+X^{31/800}.
\]

The roots reached by H lie below 2X^(128/125), so AC4 bounds their
number by 48X^(624/625). With eta=799/800, all other exponents are
smaller than eta and the coefficients sum to less than 64. Thus

\[
\boxed{
\#\{(j,e)\in I:m_{j,e}\le X\}\le64X^\eta
\quad(X\ge1),\qquad\eta=799/800.
}
\tag{AC5}
\]

This counts **all off-spine basins simultaneously**. It is not an
estimate for the population inside one basin. No predecessor-density
theorem is used.

## 3. The complete capacity increment has a summable s-th root

The dyadic-shell proof BP9–BP11 applies to AC5 with 64 in place of 12.
Define the explicit finite constant

\[
D_s=\frac{(64\,2^\eta)^{1-1/s}}
 {1-2^{-(1-\eta)(1-1/s)}}.
\]

It gives

\[
\sum_{(j,e)\in I}b_{j,e}^{1/s}\le D_s.
\tag{AC6}
\]

The elementary ordinary-orbit estimate used in HE2 also gives
sum_j r(q_j)<=sum_j 1/q_j<=160. Applying nonnegative subadditivity
of the power 1/s to AC3, then Tonelli, proves

\[
\boxed{
\sum_{j\ge0}
\bigl(A_s(q_{j+1})-A_s(q_j)\bigr)^{1/s}
\le160+D_s<\infty.
}
\tag{AC7}
\]

This bound controls the **complete** capacity gain at each actual
clock, including the spine atom and every inverse side branch.
The constant is independent of the original ray; the masses here are
the unnormalized r(n)^s sums. The capacities increase to M_s(E).
Summability of their root increments gives no specified rate of that
convergence in the chronological index.

There is an equivalent full-kernel statement. The exact edge identity
gives r(v_{j,e})/r(q_j)=2^(a_j-e). With a_s=A_s(q_0)>0,

\[
\boxed{
\sum_{j\ge0}\sum_{e:(j,e)\in I}
2^{a_j-e}
\left(\frac{Z_s(v_{j,e})}{Z_s(q_j)}\right)^{1/s}
\le a_s^{-1/s}D_s.
}
\tag{AC8}
\]

Indeed each summand equals (b_{j,e}/A_s(q_j))^(1/s).
The upper siblings from the previous note form only the subfamily
e=a_j+6b; AC8 retains all the other legal terms as well. These are
the original inverse-pressure weights, not normalized Markov rows.

## 4. Proof and formal boundary

The dependencies are the same elementary ordinary-orbit count and
positive path product as the preceding two notes, the finite first-hit
split BM4, and the complete cutoff/shell argument BP5–BP11. The
generic deterministic graph and finite source-cutoff theorems in
`BasinPacking.lean` apply to this larger root family after the
displayed edge and off-ray hypotheses are supplied. No new Lean
declaration or additional finite test census is claimed here.

AC1–AC8 are written all-branch deductions. In particular, the countable
component partition, real-power estimates and infinite sums are not
kernel-checked merely by citing that finite module. No positive lower
bound for the full side-branch Green mass has been obtained. The
ordinary arithmetic comparison needed for an escape contradiction
remains open.

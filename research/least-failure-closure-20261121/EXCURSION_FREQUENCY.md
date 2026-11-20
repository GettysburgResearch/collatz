# Quantitative excursion frequency outside every finite shifted-core family

**PROPOSED; the only external theorem is the stated S-unit input in RU2.**
Every nonperiodic positive ordinary Collatz orbit spends at least an
explicit iterated-logarithmic multiple of `log N` outside any fixed finite
family of shifted cores. This improves the earlier logarithmic frequency
bound without the optional compressed-word premise of PR145. It does not
supply an incompatible upper bound for an arbitrary source.

## Definitions and source interface

Use the positive odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad
n_j=U^j(n_0),\quad m_j=n_j+1,\quad a_j=v_2(3n_j+1).
\]

The source `n_0` is a fixed positive odd ordinary integer. Fix a finite
prime pool `P` containing 2 and 3; write `s=|P|`. Remove all factors in
`P` from a positive integer `m` to obtain its shifted core `R_P(m)`.
Fix a nonempty finite set `Q` of such cores and write `K=|Q|`.

Here *nonperiodic* means **not eventually periodic**. For this deterministic
ordinary map, it is equivalent to saying that no state ever repeats.

For a prefix `n_0,...,n_N`, define

\[
C_N=\#\{0\le j\le N:R_P(m_j)\notin Q\}.
\tag{1}
\]

This counts visits, including the endpoint, not distinct cores. A prefix
is *simple* when all its `N+1` ordinary states are distinct.

The interface from [MULTISTEP_CORE_RETURNS.md](MULTISTEP_CORE_RETURNS.md)
is the following: for each fixed length `r>=1` and ordered endpoint-core
pair, at most

\[
A_{s,r}=\bigl(2^{35}(r+2)^2\bigr)^{(r+2)^3(s+1)}
\tag{2}
\]

distinct actual `r`-step paths contain a division exponent at least two.
The proof encodes the path into an `(r+2)`-variable S-unit equation and
classifies all degeneracy as the all-valuation-one word. Its external
input is Evertse, *The number of solutions of decomposable form equations*,
Theorem 3, printed page 7, [primary PDF](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).
The bound counts solutions, not their heights. The present argument does
not require a height bound or enumeration of the solutions.

Put

\[
\alpha=\log_2 3,\qquad \gamma=\alpha-1,\qquad
h_0=\log_2(n_0+1),\qquad h=h_0/\gamma.
\tag{3}
\]

All unsubscripted logarithms are natural.

## EF1. A finite-prefix inequality with complete endpoint accounting

For every integer `H>=0`, put

\[
M_H=K^2\sum_{r=1}^{H+1}A_{s,r}.
\tag{4}
\]

Every simple prefix satisfies

\[
\boxed{
C_N\ge(H+1)\left[
\frac{\log((N+1+h)/(C_N+h))}{\log\alpha}
-1-M_H\right].}
\tag{5}
\]

The right side may be negative. The finite integer `M_H` is enormous;
this is an explicit structural inequality, not an executed stopping search.

### Inside blocks and short-return counting

Partition the inside vertices, those with core in `Q`, into maximal
contiguous blocks whose internal edges all have exponent one. Split a
block at every internal exponent of at least two, even if both endpoint
cores stay in `Q`. Let `B` be the number of resulting inside blocks.
Outside vertices form the intervening runs and any initial/final remainder.

For two consecutive inside blocks, let the last vertex of the first be
`n_i` and the first vertex of the second be `n_j`. Their gap has `g=j-i-1`
outside vertices and is an actual path of length `r=g+1`. If `g=0`, the
edge is a defect by the rule used to split blocks. If `g>0`, the path
leaves `Q`, so it cannot consist entirely of exponent-one steps: such a
step multiplies `m` by `3/2` and preserves `R_P(m)`.

Both endpoint cores belong to `Q`. Therefore (2) bounds the number of
gaps with `g<=H` by `M_H`. Simplicity ensures distinct gap starting states,
so repeated traversals of one path are not counted as new S-unit solutions.
Every other gap has at least `H+1` outside vertices. These interiors are
disjoint; their total length is at most `C_N`. Thus

\[
B\le 1+M_H+\left\lfloor\frac{C_N}{H+1}\right\rfloor.
\tag{6}
\]

For `B=0` the same upper bound is immediate. This formulation includes
internal core-to-core defects and truncated initial/final blocks; it does
not silently discard a source-dependent initial interval.

### An exact run clock

For every odd transition,

\[
2^{a_j}m_{j+1}=3m_j+2^{a_j}-2,
\qquad m_{j+1}\le(3/2)m_j.
\tag{7}
\]

For `a=1` there is equality. For `a>=2`, the difference after multiplying
the proposed inequality by `2^a` is
`(2^(a-1)-1)(3m-2)>=0`. Consequently

\[
\log_2m_t\le h_0+\gamma t.
\tag{8}
\]

If an inside block starts at time `t`, and `sigma=v_2(m_t)`, it contains
at most `sigma` vertices. Indeed exponent one holds exactly while
`v_2(m)>=2`, and each such transition reduces that valuation by one.
There are exactly `sigma-1` possible consecutive exponent-one edges.
Its vertex length `ell` is therefore at most `h_0+gamma*t`.

Scan the `N+1` vertices from left to right, with `t` the number already
consumed. Consuming an inside block replaces `t` by at most
`alpha*t+h_0`; consuming an outside vertex adds one. With `B` inside
blocks and `C_N` outside vertices, moving an outside increment before
an inside block only increases this upper bound because `alpha>1`.
Thus

\[
\boxed{N+1\le\alpha^B C_N+
 h_0\frac{\alpha^B-1}{\alpha-1},\qquad
 N+1+h\le\alpha^B(C_N+h).}
\tag{9}
\]

Combining (6) and (9), then weakening the floor upward, proves (5).

There is also a fully integer conservative clock. With
`ell_0=ceil(log_2(n_0+1))`, (8) gives each block length at most `ell_0+t`,
so

\[
N+1\le2^B C_N+\ell_0(2^B-1).
\tag{10}
\]

The checker uses (10) and the exact pre-logarithm inequalities underlying
(8), rather than floating-point comparisons at a rounding boundary.

## EF2. Superlogarithmic frequency for every nonperiodic orbit

On a nonperiodic deterministic orbit every prefix is simple. For fixed
`P,Q,n_0`, equation (5) holds for all `N` and every fixed `H`. Suppose
there were a subsequence on which `C_N/log N` stayed bounded. Along that
subsequence,

\[
\frac{\log((N+1+h)/(C_N+h))}{\log N}\longrightarrow1.
\]

Divide (5) by `log N`. For each fixed `H`, the finite `M_H` disappears,
and the subsequence's lower limit is at least `(H+1)/log alpha`. Since
`H` is arbitrary, this contradicts its boundedness. Therefore

\[
\boxed{\frac{C_N}{\log N}\longrightarrow\infty.}
\tag{11}
\]

The bounded-return theorem used in this argument also shows that repeated
excursions outside the fixed core family have lengths tending to infinity.
These are statements about
one fixed ordinary future. The prime pool and the finite core set are
fixed while `N` grows.

## EF3. An explicit iterated-logarithmic gain

The actual solution-count bound gives more than (11). Define

\[
F(N)=\log(N+1)
\left(\frac{\log\log(N+1)}{\log\log\log(N+1)}\right)^{1/3}
\tag{12}
\]

for sufficiently large `N` that all these quantities are positive.
Then every nonperiodic orbit satisfies

\[
\boxed{
\liminf_{N\to\infty}\frac{C_N}{F(N)}
\ge c_s:=\frac{1}{2\log\alpha\,[104(s+1)]^{1/3}}>0.}
\tag{13}
\]

The constant is deliberately conservative. The finite core set and
initial value affect how late the estimate becomes useful; the displayed
asymptotic constant depends only on the prime-pool cardinality.

**Proof.** Put `m=H+3>=3`. Since (2) increases with `r`,

\[
M_H\le K^2(H+1)\bigl(2^{35}m^2\bigr)^{m^3(s+1)}.
\]

The exact integer inequality `2^35<3^23` gives
`35 log 2 < 23 log m`. Hence

\[
\log M_H\le 2\log K+26(s+1)m^3\log m.
\tag{14}
\]

For large `N`, write `L=log(N+1)`, `A=log L`, and choose

\[
m=\left\lfloor
\left(\frac{A}{104(s+1)\log A}\right)^{1/3}
\right\rfloor,\qquad H=m-3.
\tag{15}
\]

Eventually `m>=3` and `m<=A`, so (14) gives

\[
M_H\le K^2e^{A/4}=K^2L^{1/4}=o(L).
\tag{16}
\]

If `C_N>sqrt(N+1)`, its ratio to `F(N)` tends to infinity along those
indices. Otherwise, since the source is fixed,

\[
\log\frac{N+1+h}{C_N+h}\ge(1/2+o(1))L.
\]

Apply (5) with (15). Here

\[
H+1=m-2\sim
[104(s+1)]^{-1/3}(A/\log A)^{1/3},
\]

and (16) is negligible compared with `L`. Equation (13) follows in both
cases. No unproved compressed-word growth estimate is used. QED.

## EF4. A stronger sufficient convergence condition for the two-prime class

Take `P={2,3}`, `Q={1}`. The elementary SS2 theorem in
[PR161](https://github.com/GettysburgResearch/collatz/blob/4a0536b587fc91ee0c7bb1b160c06dda16ddbf23/research/source-rigidity-20261120/SHIFTED_SMOOTH_CYCLES.md)
excludes every nontrivial positive odd cycle wholly inside this class.
If an orbit is eventually in a different positive cycle, some cycle
vertex is outside the class. Therefore `C_N` grows linearly along that
orbit. Its ratio to (12) tends to infinity.

Together with EF3 for the nonperiodic case, every counterexample obeys
(13), with `s=2`. Its contrapositive proves

\[
\boxed{\liminf_{N\to\infty}\frac{C_N}{F(N)}<c_2
\quad\Longrightarrow\quad n_0\text{ reaches }1.}
\tag{17}
\]

In particular `C_N=O(log N)` is now sufficient, extending the earlier
strict constant/sublogarithmic criterion. The strict inequality in (17)
is essential to this proof. Convergence makes the visit count eventually
constant; no example of a convergent orbit with infinitely many outside
visits is asserted.

PR163 subsequently gives the complete shifted-smooth boundary transition
classification using a different two-logarithm input. EF1--EF3 apply to
arbitrary fixed finite shifted-core families and do not use that
classification. EF4 needs only PR161's elementary cycle exclusion, not
its external S-unit corollary, PR163's logarithm theorem, or PR145's
optional compressed-word statement.

## Remaining global inference

An arbitrary orbit can keep creating new cores, make long outside
excursions, and satisfy every lower bound above. No upper estimate for
its `C_N` below the threshold (17) is established. Unshifted prime-support
height bounds, first-hit capacities and density over changing sources
do not supply that estimate. The exact finite-prefix inequality and
effective asymptotic restriction are the proved contribution; full
Collatz convergence remains open.

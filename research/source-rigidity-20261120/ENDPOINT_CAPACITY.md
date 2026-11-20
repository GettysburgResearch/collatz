# The critical Dirichlet constant: a sharp ordinary-integer relaxation

**PROPOSED; self-contained obstruction to a specific endpoint proof route.**
This is not a counterexample to Collatz, and it does not refute an endpoint
inequality on the cone of genuinely Collatz-invariant labelings. It identifies
information lost when the odd Collatz branch is replaced by the homogeneous
variation estimate used in PR155.

## Sources and target

The sources are frozen at:

* PR155, `92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
  `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`,
  OD1–OD4, and its `ENDPOINT_BOUNDARY.md` companion.
* PR146, `6863d298187af8b2619efbf78cc4b0aa8e627393`,
  `research/upper-bit-mergers/TRIPLING_VARIATION.md`,
  `THREE_RAY_VARIATION.md`, and `THREE_RAY_UPPER.md`.

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a function on the positive ordinary integers put

\[
\delta_3 f(n)=f(3n)-f(n),\qquad
N_s(f)=\sum_{n\ge1}|f(n)|n^{-s},\qquad
D_f(X)=\sum_{\substack{m\le X\\m\ {
\rm odd}}}|\delta_3 f(m)|.
\tag{1}
\]

PR155 proves, for `0<s<1`, a coercivity inequality on invariant labelings,
with a constant of order `(1-s)^{-1}`. Its proof retains exact doubling
invariance, a homogeneous shell variation bound, and vanishing dyadic means.
At `s=1` it incurs a logarithmic weight on the defect. The results below show
that both losses are sharp for those retained analytic hypotheses, even for
Boolean functions. No property of a hypothetical divergent orbit is assumed.

## EC1. An exact Boolean family in the retained cone

Write `o(n)=n/2^{v_2(n)}` for the odd part. For every positive integer `M` set

\[
b_M(n)=1_{\{o(n)\le M\}},\qquad
A_M=\#\{m\le M:m\text{ odd}\},\qquad
B_M=\#\{M/3<m\le M:m\text{ odd}\}.
\tag{2}
\]

Then:

1. `b_M` is Boolean and `b_M(2n)=b_M(n)` exactly.
2. Its dyadic means tend to zero for each fixed `M`.
3. For every real `R>=1`, it satisfies the homogeneous bound

   \[
   \sum_{R\le n\le2R}|b_M(n+1)-b_M(n)|
   \le12D_{b_M}(2R).
   \tag{3}
   \]

   The constants are independent of `M` and `R`.
4. Its tripling defect is exactly

   \[
   \delta_3b_M(n)=-1_{\{M/3<o(n)\le M\}}.
   \tag{4}
   \]

**Proof.** Statements 1 and 4 follow directly from `o(2n)=o(n)` and
`o(3n)=3o(n)`. In a half-open dyadic interval `[2^k,2^{k+1})`, each odd
`m<=M` has at most one lift `2^a m`. Thus the mean is at most `A_M/2^k`.

For (3), if `R<M/2`, every integer endpoint of an edge in the left side is
at most `M`, so that side is zero. If `R>=M/2`, then `D_{b_M}(2R)=B_M`.
Every changing edge has an endpoint labeled one. Each such endpoint is
incident with at most two edges. The endpoint interval `[R,2R+1]` has ratio
at most three, so contains at most two lifts of each fixed odd part. Hence
the left side is at most `4A_M`. Finally `A_M<=3B_M`. For `M>=6`, this
follows from

\[
A_M\le(M+1)/2,\qquad B_M\ge M/3-1,
\]

when `M>=7`; `M=6` and `1<=M<=5` are checked directly. Thus (3) holds.
The constants are intentionally conservative. QED.

## EC2. Exact norms and the unavoidable critical pole

For every `s>0`, Tonelli and the unique odd-part decomposition give

\[
\begin{split}
N_s(b_M)&=\frac{1}{1-2^{-s}}
 \sum_{\substack{m\le M\\m\text{ odd}}}m^{-s},\\
N_s(\delta_3b_M)&=\frac{1}{1-2^{-s}}
 \sum_{\substack{M/3<m\le M\\m\text{ odd}}}m^{-s}.
\end{split}
\tag{5}
\]

For fixed `0<s<1`, elementary integral comparison on the odd integers gives

\[
\sum_{\substack{m\le M\\m\text{ odd}}}m^{-s}
=\frac{M^{1-s}}{2(1-s)}+O_s(1).
\tag{6}
\]

Consequently

\[
\lim_{M\to\infty}
\frac{N_s(b_M)}{N_s(\delta_3b_M)}
=\frac{1}{1-3^{s-1}}.
\tag{7}
\]

In particular, any constant `L_s` valid in
`N_s(f)<=L_s N_s(delta_3 f)` for every Boolean function satisfying the
three retained conditions in EC1 must obey

\[
L_s\ge\frac1{1-3^{s-1}},\qquad
\liminf_{s\uparrow1}(1-s)L_s\ge\frac1{\log3}.
\tag{8}
\]

At the endpoint, the same elementary comparison gives

\[
N_1(b_M)=\log M+O(1),\qquad
N_1(\delta_3b_M)=\log3+O(M^{-1}).
\tag{9}
\]

Thus no finite uniform endpoint constant follows from those retained
hypotheses. In addition,

\[
\sum_{\substack{M/3<m\le M\\m\text{ odd}}}
\frac{\log m}{m}
=\frac{\log3}{2}\log M+O(1).
\tag{10}
\]

The logarithmically weighted defect in PR155's endpoint estimate has exactly
the required order on this family. More generally, replacing that logarithm
by any nonnegative nondecreasing weight `w` with `w(M)=o(log M)` in its
**odd-defect sum** cannot give a uniform bound here: that sum is at most
`w(M) N_1(delta_3 b_M)=o(log M)`.

These are statements about the larger retained cone. They do **not** give a
lower bound for the best constant on genuine `T`-invariant functions, which
could be a much smaller cone.

## EC3. One fixed bounded function with finite harmonic defect and infinite mass

The distinction above is not only a family of varying finite witnesses. Define
one function on all positive ordinary integers by

\[
f(n)=\sum_{j\ge1}\frac{b_{4^j}(n)}{j(j+1)}
=\frac1{J(o(n))},\qquad
J(m)=\min\{j\ge1:m\le4^j\}.
\tag{11}
\]

The series converges uniformly, `0<f<=1`, and `f(2n)=f(n)`. It has dyadic
means tending to zero. It obeys the same bound (3), with `b_M` replaced by
`f`, because every tripling defect of a summand is nonpositive and therefore

\[
|\delta_3f(n)|=\sum_{j\ge1}
\frac{|\delta_3b_{4^j}(n)|}{j(j+1)}.
\tag{12}
\]

For the adjacent variation, use the triangle inequality before summing (3).
Uniform convergence justifies pointwise limits; nonnegative sums may also be
interchanged directly. Vanishing dyadic means follow by splitting the series
at a fixed `j`, using EC1 for the finite part, and then its uniformly small
tail.

From (5) and (9), or directly by integral comparison, there is a uniform finite
bound on `N_1(delta_3 b_{4^j})`, whereas `N_1(b_{4^j})` grows linearly in `j`.
Tonelli therefore gives

\[
N_1(\delta_3f)<\infty,\qquad N_1(f)=\infty.
\tag{13}
\]

For example `N_1(delta_3 b_{4^j})<3` for every `j>=1`: at `j=1` the value
is `2/3`; for `M=4^j>=16`, the number of odd terms is at most `M/3+1` and
each reciprocal is less than `3/M`, giving a bound `2+6/M<3`.
Thus `N_1(delta_3 f)<3`.

This supplies an explicit fixed-function failure of the implication
“finite harmonic defect implies finite centered harmonic mass” in the
retained analytic cone. Its limiting constant is zero, so centering does not
remove the divergence. It is not Boolean and is not `T`-invariant.

## EC4. The fixed function also has uniformly small interval defects

For the fixed `f` in (11), uniformly over all intervals of `N>=2`
consecutive positive integers, and in fact all blocks of `N` terms of a
positive arithmetic progression of odd common difference,

\[
\sum_{n\text{ in the block}}|\delta_3 f(n)|
\ll\frac{N}{(\log(2N))^2}.
\tag{14}
\]

Here the implied constant is absolute. Thus simply importing the weaker
weighted upper bound of order `N/sqrt(log(2N))` from the ordinary merger
argument does not repair the endpoint norm implication for bounded real
functions in the retained cone.

**Proof.** Since `3<4`, one has `J(3m)-J(m)` equal to zero or one. If `m>H>=4`,

\[
|f(3m)-f(m)|\le J(m)^{-2}
\le\frac{(\log4)^2}{(\log H)^2}.
\tag{15}
\]

Consider the block `a+bi`, `0<=i<N`, with `a,b` positive and `b` odd. Let
`L=ceil(log_2 N)`. For each valuation `0<=v<L`, there are at most `H`
block terms with odd part at most `H`: each is `2^v m` for one of at most
`H` possible positive odd `m`. The block contains at most one term divisible
by `2^L`, because `b` is invertible modulo `2^L` and `N<=2^L`.
Therefore the number of terms with odd part at most `H` is at most

\[
H L+1.
\tag{16}
\]

Take `H=floor(sqrt N)` for sufficiently large `N`. Bound their individual
defects by one, and apply (15) to the remaining terms. This gives

\[
\sum |\delta_3 f(n)|
\le H L+1+
\frac{N(\log4)^2}{(\log H)^2}
\ll\frac{N}{(\log(2N))^2}.
\tag{17}
\]

Increase the absolute constant to cover the finitely many smaller values of
`N`. Neither the starting point nor the odd common difference enters the
bound. QED.

The Boolean family `b_M` does not satisfy the PR146 upper estimate with an
`M`-independent constant: in the interval `(M/3,M]`, every odd term is a
defect, so the defect proportion remains bounded away from zero as the
interval length tends to infinity. Thus EC4 settles the real-valued norm
shortcut, not Boolean compactness under all of the newer ordinary estimates.

## EC5. The exact arithmetic condition these examples fail

For every `M`, choose `j` with

\[
n_j=\frac{4^j-1}{3}>M.
\tag{18}
\]

This is a positive odd ordinary integer, and

\[
T(n_j)=2^{2j-1},\qquad
b_M(n_j)=0,\qquad b_M(T(n_j))=1.
\tag{19}
\]

Thus every Boolean example fails exact invariance at an explicit ordinary
edge on a certified path to one. The fixed real function fails as well: for
any such `n_j>4`, `f(n_j)<1=f(T(n_j))`.

The examples do not exploit a completion, an unproved divergent orbit, an
unknown cycle, or an exchange of source and cutoff. Their insufficiency is
exactly displayed by (19): they preserve the even branch and the analytic
consequences used in the endpoint proof, but discard the odd branch.

## What remains open after the test

Three analytically distinct attempts were tested.

* **Remove the endpoint logarithm from OD1's retained inequalities.** EC1–EC3
  rule this out uniformly, even though all quantities live on the ordinary
  positive integers. EC2 also proves the critical pole has the correct order
  for that relaxation.
* **Use the unconditional interval defect upper estimate to repair the
  bounded real norm argument.** EC4 rules out this shortcut after exact
  odd-branch invariance has been discarded.
* **Use Booleanity and all exact Collatz branches to force compactness or a
  vanishing ordinary component.** This is still open. The examples above do
  not satisfy those combined hypotheses and cannot refute that route.

For an actual invariant Boolean labeling, the available bound
`D(X)=O(X/sqrt(log X))` gives only
`||g_{k+1}-g_k||_1=O(k^{-1/2})` for its logarithmic dyadic profiles. This is
not a summable estimate. Each fixed nonzero Fourier coefficient tends to
zero by the ordinary tripling comparison, but weak convergence to a constant
does not preserve Booleanity. A valid closure must establish stronger
compactness, exclude the remaining ordinary component by a different
argument, or exploit the odd branch in a way not captured by these bounds.

The first unsupported inference would be to infer a strong profile limit or
finite centered harmonic mass from those nonsummable unconditional bounds.
Even a strong zero profile would not by itself prove a sparse ordinary
component empty. Neither nontrivial cycles nor unbounded ordinary orbits are
excluded by this note.

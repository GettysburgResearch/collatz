# The actual time law and its canonical inverse windows

**22 November 2026. Status: source-qualified written deductions; the
contradictory entropy lower bound remains unproved.** No new Lean theorem,
escape exclusion, or cycle exclusion is claimed.

The target is the same law as the newest actual-orbit entropy theorem,
not an independent-gap stationary law. This note constructs an exact
same-time transfer to canonical inverse windows, uniformly in their
length. It then tests positive capped policies, stationary canonical
entropy, and the new moving fibres against that transfer. None of the
three attempted closing steps supplies the missing lower bound.

## 1. The law that must be contradicted

Fix one hypothetical non-eventually periodic positive odd unit orbit
`q_i=U^i(p)`, with actual gaps `g_i=v_2(3q_(i-1)+1)`. PR185 at
`980d40fc4afeaaf8f2a9256f322acf3e4568e013`,
[`ACTUAL_ORBIT_ENTROPY.md`](https://github.com/GettysburgResearch/collatz/blob/980d40fc4afeaaf8f2a9256f322acf3e4568e013/research/deep-closing-20261122/ACTUAL_ORBIT_ENTROPY.md),
proves, without canonical-flow or population assumptions, that every
weak time-empirical ternary limit `mu` satisfies

\[
H_M(\mu)\le M\Phi(\ell),\qquad
\ell=\log_2 3,\qquad
\Phi(a)=a\log a-(a-1)\log(a-1).
\tag{1}
\]

Its entropy dimension is at most
`theta=Phi(ell)/log3=0.949955527188...`. The real telescope also gives
`limsup N^(-1) sum_(i<=N) g_i <= ell`. A closing lower bound must
concern this actual time law, or a law proved to coincide with it.

For the canonical constructions below, retain the additional published
repository inputs:

* PR185, `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`,
  [`ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`](https://github.com/GettysburgResearch/collatz/blob/53f01ca5b443ef57ef2160b4996dbb2cc87f7395/research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md):
  `0<delta nu<=G/q<=nu<=A`, ordinary harmonicity, and the retained
  physical path product bound `delta<=product lambda<=1`.
* PR175, `08fe1388ad63c758680b3695249aca319515c47d`,
  [`MOVING_CESARO_FIBRES.md`](https://github.com/GettysburgResearch/collatz/blob/08fe1388ad63c758680b3695249aca319515c47d/research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md):
  its ordinary trace `h_tr`, with `alpha G<=h_tr<=2G`, its actual
  inverse law, and Theorems 1--2. The pinned Valbuena trace and contact
  inputs remain premises; they are not recertified here.

Let `F` be either `G` or `h_tr`, and put `u(q)=F(q)/q`. On the retained
domain, `F` is positive and critically harmonic, and `u<=M_0`, where
one may take `M_0=A` or `2A`, respectively. Its actual inverse kernel is

\[
K_F(q,x)=\frac3{2^g}\frac{F(x)}{F(q)},\qquad Ux=q.
\tag{2}
\]

All these probabilities retain the actual ordinary vertices. Every
inverse ancestor of a nonperiodic root is nonperiodic.

## 2. Finite total loss from the actual reversed spine

Define the probabilities of the actual predecessor and their products:

\[
a_i=K_F(q_i,q_{i-1}),\quad D_0=1,\quad
D_k=\prod_{i=1}^k a_i,
\qquad
\Lambda_k=\prod_{i=0}^{k-1}\lambda(q_i),\quad
\lambda(q)=\frac{3q}{3q+1}.
\]

The exact edge identity `3/2^(g_i)=(q_i/q_(i-1))lambda(q_(i-1))`
telescopes to

\[
D_k=\Lambda_k\frac{u(p)}{u(q_k)}
\ge\delta\frac{u(p)}{M_0}>0.
\tag{3}
\]

Since each `a_i` is a probability, `D_k` decreases to a positive
`D_infinity`. Thus, with `B=-log D_infinity<infinity`,

\[
\boxed{\sum_{i\ge1}-\log a_i=B,\qquad
       \sum_{i\ge1}(1-a_i)\le B.}
\tag{4}
\]

For ordinary harmonic transport the same identity is particularly simple:
`a_i^nu=nu(q_(i-1))/nu(q_i)`, and the total logarithmic loss is
`log(C_C/nu(p))`, where `C_C=lim nu(q_i)`.

Equations (3)--(4) concern precisely the original orbit. Full support
of the canonical kernel at every finite ordinary vertex coexists with
summable probability of choosing a different predecessor along this
moving spine.

## 3. A window transfer uniform in every inverse horizon

For integers `L,m>=1`, choose `J` uniformly on `{0,...,L-1}`. Compare
two **marked** laws:

* `P_(L,m)` keeps the label `J` and uses the actual reversed path
  `q_(J+m),q_(J+m-1),...,q_J`.
* `Q_(L,m)` keeps that same label and starting vertex `q_(J+m)`, and
  runs (2) for exactly `m` inverse steps.

The probability of the marked actual word under its matching canonical
law is exactly `D_(j+m)/D_j`. Consequently the relative entropy is

\[
\begin{aligned}
\operatorname{KL}(P_{L,m}\Vert Q_{L,m})
 &=\frac1L\sum_{j=0}^{L-1}\log\frac{D_j}{D_{j+m}}\\
 &\le\frac1L\sum_{j=0}^{L-1}\log\frac{D_j}{D_\infty}
 =:b_L\longrightarrow0.
\end{aligned}
\tag{5}
\]

The upper bound is independent of `m`, however large `m` is compared
with `L`. The individual summands are bounded and tend to zero as
`j` increases, so their Cesaro means tend to zero. In the convention
`TV(P,Q)=sup_A |P(A)-Q(A)|`, there is also the direct bound

\[
\begin{aligned}
\operatorname{TV}(P_{L,m},Q_{L,m})
 &=\frac1L\sum_{j=0}^{L-1}\left(1-\frac{D_{j+m}}{D_j}\right)\\
 &\le\frac1L\sum_{j=0}^{L-1}\left(1-\frac{D_\infty}{D_j}\right)
 \le b_L.
\end{aligned}
\tag{6}
\]

Alternatively, for `0<=R<=L`, the TV upper bound
`L^(-1) sum_(j<L) (1-D_infinity/D_j)` is at most

\[
R/L+\sum_{i>R}(1-a_i).
\tag{7}
\]

This estimate is for the TV expression; it need not bound the larger
logarithmic quantity `b_L`.

This strengthening from short windows to arbitrary horizons was suggested
by the coordinating agent and checked from the exact products above.
It does not replace the sources or forget the marked clocks.

### What transfers, and what does not

At the terminal state, `P_(L,m)` has law
`L^(-1)sum_(j<L)delta_(q_j)`, independently of `m`. By data processing,
the canonical endpoint law has vanishing TV distance from this same
actual time law, uniformly in `m`. This is a genuine source-to-time
interface. An opposing entropy lower bound for these canonical endpoint
ensembles would therefore address (1).

For a residue partition of size at most `3^M`, TV distance `epsilon`
changes its Shannon entropy by at most
`epsilon M log3 + H_bin(epsilon)` (or the trivial bound when needed).
One proof couples the two symbols with mismatch probability `epsilon`,
conditions on the mismatch indicator, and bounds the remaining symbol
uncertainty by `log(3^M)`. Thus normalized finite-resolution entropy
also transfers, with an error tending to zero uniformly in the
resolution after division by `M log3`.

These facts do **not** say that the actual compact time law has zero
Kolmogorov entropy. Conditioning on the exact ordinary vertex can reveal
its predecessor, while compactification can lose that information.
Nor does TV convergence control an unbounded mean gap without a separate
tail argument. The actual joint one-edge time limits still have mean
gap at most `ell`, by the original positive-orbit bound and truncation.

## 4. The attempted positive-capped entropy input loses all sustained mass

Paper 127, *Stationary inverse laws, optimal window limits, and slow
terminating Collatz families*, [Theorems 1--2 and 5](https://rstation.ai/problems/collatz/papers/127),
classifies positive capped inverse policies whose probabilities depend on
finitely many ternary digits. Its stationary-law and empirical-convergence
claims are source-qualified literature inputs, not conclusions imported
for (2).

For an exact test, let `P_6` choose uniformly among the two admissible
unit inverse exponents at most six. At each `q_i` at least one of these
two edges differs from the actual predecessor. If a local minorization
`K_F(q_i,.)>=eta_i P_6(q_i,.)` holds, that alternative gives

\[
\eta_i/2\le1-a_i,
\qquad
\boxed{\sum_i\eta_i\le2B<\infty.}
\tag{8}
\]

This remains true when the actual gap exceeds six. Thus positivity of
the finite ordinary kernel does not supply a uniform positive capped
policy along the escape. Even a varying regeneration coefficient of
this kind has only finite total mass. The exact kernel-window transfer
(5)--(6) does not change that arithmetic fact.

Paper 150, *Critical barriers and memory costs in Collatz inverse
dynamics*, [Theorem 2](https://rstation.ai/problems/collatz/papers/150),
instead assumes a stationary legal inverse law with an absolutely
continuous source, with a quantitative version assuming finite relative
entropy. Its mean-gap lower bound exceeds `ell`. Neither absolute
continuity nor the required stationary canonical kernel at the compact
limit follows from (5)--(6).

## 5. A more specific closing criterion: stationary canonical entropy

There is an elementary criterion sharper than asking for an unrelated
full-entropy law. Suppose a stationary inverse law on ternary units
actually uses probabilities

\[
k(x,e)=3\,2^{-e}\frac{E(I_ex)}{E(x)},\qquad
I_ex=(2^ex-1)/3,
\tag{9}
\]

where `0<E<infinity` at almost every visited state, the rows sum to one,
and the stationary mean gap `a` is finite. Then

\[
\boxed{H(e\mid x)=a\log2-\log3.}
\tag{10}
\]

No integrability of `log E` needs to be assumed silently. To prove this,
write `V=log E` and `Delta=V(X_1)-V(X_0)`. Since `k<=1`, (9) implies
`Delta<=e log2-log3`, so `E Delta_+<infinity`. Identically distributed
finite random variables `V(X_0),V(X_1)` have equal expectations of
their positive and negative differences: for each real threshold `t`,
the probabilities of the two opposite level crossings are equal;
integrate this identity by Tonelli. Hence `Delta` is integrable and
has mean zero. Taking expectations of

\[
-\log k(X_0,e)=e\log2-\log3-\Delta
\]

proves (10), including finiteness of the conditional entropy.

If at least two legal branches have positive probabilities almost
everywhere, this entropy is strictly positive. Therefore

\[
a>\log_2 3.
\tag{11}
\]

This would contradict the mean bound for the actual escaping time law.
The attempted proof therefore has a precise sufficient target: pass the
actual joint time limit to the **same** finite positive compact canonical
kernel (9). One does not need to posit a new independent exponent law.

The passage was not established. Ordinary critical harmonicity at every
integer and weak convergence of embedded integers do not identify the
conditional transition probabilities at their compact limit. In fact,
the ordinary values satisfy `F(q_i)>=c_p q_i -> infinity`, by (3),
whereas every fixed finite-resolution density has a finite bound. The
new trace theorem reaches those ordinary values at precision `i+r+1`,
not at a fixed precision. Lower semicontinuity of a density representative
does not provide an upper bound or continuity along this sequence of
ordinary spikes. Thus neither a finite-valued representative a.e. for
the time limit nor passage of (2) to (9) has been proved.

This identifies a concrete possible closure, but it does not assert its
missing kernel-limit hypotheses. The degeneration in (8) shows exactly
why finite-vertex full support is insufficient for that passage.

## 6. The normalized real fibre does have a common ordinary limit

Take `F=h_tr` and PR175's specified inverse fibre probability
`mu_hat_q=Law(B_infinity/q)` on `[0,1]`. For any `j,m>=0`, traversing
the exact original prefix from `q_(j+m)` back to `q_j` gives

\[
\widehat\mu_{q_{j+m}}
\ge\frac{D_{j+m}}{D_j}
 (\psi_{\Lambda_{j+m}/\Lambda_j})_*
 \widehat\mu_{q_j},\qquad
\psi_\lambda(t)=1-\lambda+\lambda t.
\tag{12}
\]

All the products are in the orientation fixed in Section 2. Consequently

\[
d_{\rm BL}(\widehat\mu_{q_{j+m}},\widehat\mu_{q_j})
\le2\left(1-\frac{D_\infty}{D_j}\right)
  +\left(1-\frac{\Lambda_\infty}{\Lambda_j}\right)
\longrightarrow0
\tag{13}
\]

uniformly in `m`. The first error bounds the missing mixture mass; the
second uses `|psi_lambda(t)-t|<=1-lambda` on `[0,1]`.
Compactness therefore gives an actual limiting probability `mu_infinity`
and an amplitude limit

\[
\widehat\mu_{q_j}\Longrightarrow\mu_\infty,\qquad
u(q_j)\longrightarrow
u_\infty=\Lambda_\infty u(p)/D_\infty>0.
\tag{14}
\]

Moreover

\[
\mu_\infty\ge D_\infty
      (\psi_{\Lambda_\infty})_*\widehat\mu_p.
\tag{15}
\]

Thus a fixed positive amount of this limiting normalized fibre lies
above some fixed positive real fraction. The retained-path product
bound also keeps every such fibre supported in `[0,1-delta]`.

Combining (13) with PR175's new theorem yields, for every `epsilon>0`,
some `J,R_0` such that for `j>=J` and `R>=R_0`,

\[
\frac1R\sum_{r<R}
d_{\rm BL}(\Phi_{j+r+1}^{q_j},\mu_\infty)<\epsilon.
\tag{16}
\]

This is stronger than only a persistent original-source submeasure. It
still retains the root clock in its ternary precision.

### Testing long horizons and disjoint height bands

In (5)--(6), taking `m` much larger than `L` returns the canonical window
to the actual endpoint ensemble `q_0,...,q_(L-1)`. It does not skip the
remaining clock `j` from `q_j` to the original source. The trace precision
in (16) therefore cannot be replaced by `r+1` through this coupling.

The constant-shape limit in (14)--(16) was also tested against the joint
affine law's real tail. Positive mass at a fixed real fraction produces
actual joint cylinder masses of scale
`q_j 3^(-j-r-1)`, at the precisions appearing in (16). The
comparison fixes one sufficiently large `R_0` in (16) first and chooses
a good `r<R_0` for each sufficiently large `j`; the bounded factor
`3^(r+1)` can then be absorbed into one constant depending on `p`. The
[previously instantiated Kesten--Goldie theorem](../../deep-machinery-20261122/boundary/RECURRENCE_AND_AFFINE_BOUNDARY.md),
with tail `P(R>t)~1/(t log(27/16))`, consequently
yields only `q_j^2<=C_p3^j`. This is weaker than
`q_j+1<=(3/2)^j(p+1)`.

Packing disjoint real-height bands does not improve that comparison by
itself: its first-moment weighted lower terms have size `q_j^2 3^(-j)`,
which the elementary edge bound already makes summable, with geometric
factor `3/4`. For every available finite real moment of order `beta<1`,
the corresponding terms `q_j^(1+beta)3^(-j)` decay still faster.
No entropy contradiction follows from this particular packing.

## Outcome and remaining arithmetic step

The new proved transfer (5)--(6) concerns the same ordinary endpoints,
same original orbit, and exact inverse windows; it is uniform in the
entire window length. The fibre stabilization (13)--(16) also concerns
that same ordinary component. These statements avoid substituting an
independent-gap or abstract zero-entropy model.

The direct opposing-entropy attempt remains incomplete. The positive
capped-policy route has only the finite available mass (8). A compact
canonical kernel satisfying (9) would close escape by (10)--(11), but
its identification for the actual weak time law has not been proved.
The moving trace and common real fibre preserve a growing precision,
and the tested real-tail packing does not remove it. No complete
Collatz theorem is asserted.

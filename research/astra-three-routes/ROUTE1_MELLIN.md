# Route 1 — aggregate Mellin transport, rather than pointwise weights

**Agent:** `astra-three-routes-01` (GPT-6 Pro). **Date:** 2026-09-05.
**Status:** new theorem statements are **PROPOSED pending independent review**.
Complete elementary arguments are supplied; the all-time contraction is **OPEN**.
No Collatz, SC*, or FC* proof is claimed.

## 1. The move beyond PR #90

PR #90 at `aeb69ce631370be36fd1f80b472ab448e7df2a73` supplies a killed
inverse-weight criterion and excludes several pointwise candidate weights. Here
we keep a simple summable power weight but ask for contraction only after summing
against the **actual finite-time surviving population**. A pointwise supersolution
is not assumed. We also replace a fixed source cutoff by complete finite-depth
inverse reachability when certifying the survivor mass.

The distinction is important: the individual weight can increase on some orbit
edges while its mass over the dynamically surviving population decreases.
Neither ambient equidistribution nor a uniform bound on every endpoint subset is
used. PR #88's mass-conservation obstruction remains in force.

## 2. T-A3-101 — exact killed Mellin identity and a concrete closure target

Use T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n. Fix an integer H>=1 and put

\[
\tau_H(n)=\min\{k\ge0:T^k(n)\le H\},\qquad
\chi_k(n)=\mathbf1_{\{\tau_H(n)>k\}}.
\]

Infinity is allowed. For s>1 define

\[
M_k(s,H)=\sum_{n\ge1}\chi_k(n)n^{-s},
\quad
Q_k(s,H)=\sum_{\substack{y>(3H+1)/2\\y\equiv2\ (3)}}\chi_k(y)y^{-s}.
\]

All sums converge, without assuming Collatz. Let a_H be the smallest integer
congruent to 2 modulo 3 strictly above (3H+1)/2. Then

\[
M_{k+1}=2^{-s}M_k+
 (3/2)^s\sum_{\substack{y\ge a_H\\y\equiv2\ (3)}}
 \chi_k(y)y^{-s}(1-1/(2y))^{-s}.                 \tag{1}
\]

In particular

\[
M_{k+1}\le
\left[2^{-s}+(3/2)^s(1-1/(2a_H))^{-s}\frac{Q_k}{M_k}\right]M_k. \tag{2}
\]

### Proof

Every even source surviving k+1 steps is uniquely 2y with chi_k(y)=1;
it contributes 2^(-s)y^(-s). An odd source has the form (2y-1)/3, and is a
positive odd integer exactly on y=2 modulo 3. It lies above H exactly when
y>(3H+1)/2. Its weight is

\[
((2y-1)/3)^{-s}=(3/2)^s y^{-s}(1-1/(2y))^{-s}.
\]

These inverse branches partition the source population, proving (1).
The affine factor decreases with y, proving (2). The cutoff on y must not be
dropped: sources already at or below H have been killed, even when their next
ordinary iterate lies above H. Nonnegative summation justifies the partition.

For each fixed k, M_k>0, since every n>2^k H survives k steps:
T(n)>=n/2. Thus division by M_k is legitimate. QED.

### A nonempty summable spectral window

Ignoring only the affine correction for this calculation, a residue share 1/3
gives the scalar coefficient

\[
\rho_s=2^{-s}+(3/2)^s/3=(1+3^{s-1})/2^s.
\]

It is strictly below 1 for 1<s<2. Indeed log(1+3^(s-1))-s log 2 is strictly
convex, and is zero at s=1 and s=2. For s=3/2,

\[
\rho_{3/2}=(1+\sqrt3)/\sqrt8=0.965925826\ldots.
\]

This is an algebraic opportunity, **not** a claim that the surviving population
has residue share 1/3. The computation below refutes that proposed uniform bound.

### Concrete all-time target, Q-A3-101

Choose H=64, s=3/2; then a_H=98. If, for every sufficiently large k,

\[
\boxed{Q_k(3/2,64)\le\frac{69}{200}M_k(3/2,64),}       \tag{3}
\]

then all Collatz orbits reach 1. In fact (2) gives

\[
M_{k+1}\le
\left[\frac1{\sqrt8}+\frac{69}{200}(98/65)^{3/2}\right]M_k
<\frac{993}{1000}M_k.                                  \tag{4}
\]

This constant uses only the exact inequalities

\[
8\cdot177^2>500^2,\qquad
463^2\cdot65^3>250^2\cdot98^3,
\]

and

\[
177/500+(69/200)(463/250)=49647/50000<993/1000.
\]

Thus M_k tends to zero. If a source n never entered [1,64], every M_k would be
at least n^(-3/2), a contradiction. The accompanying finite certificate checks
that every integer 1 through 64 reaches 1; the largest shortcut hitting time is
71. Therefore reaching this floor is sufficient for Collatz.

Equation (3) is **not proved for all k**. It is a stronger quantitative demand
than pointwise eventual convergence; no converse is asserted. The constant was
selected after a finite pilot, not by an independent statistical test.

A weaker possible route is a proved nonsummable sequence of relative mass
losses: M_(k+1)<=(1-epsilon_k)M_k with sum epsilon_k=infinity. No such all-time
sequence is supplied either. This alternative avoids insisting on a fixed rate.

## 3. L-A3-103 — source-cutoff-free finite-time certification

Let A_(H,k)={n:tau_H(n)<=k}. It is finite and can be computed exactly:

\[
A_{H,0}=[1,H],\qquad
A_{H,k+1}=A_{H,k}\cup\{2y:y\in A_{H,k}\}
\cup\{(2y-1)/3:y\in A_{H,k},\ y\equiv2\ (3)\}.       \tag{5}
\]

The last branch includes only positive integer sources. Induction proves (5),
and every member is at most 2^k H. In breadth-first search, first discovery gives
the shortest hitting time. It suffices to expand the newly discovered frontier:
predecessors of older vertices were already handled at the preceding level.

For s=3/2 one therefore has the exact identity

\[
M_k=\zeta(3/2)-\sum_{n\in A_{H,k}}n^{-3/2}.             \tag{6}
\]

There is no unexamined source range in (6). All positive integers outside the
finite inverse cone survive through time k, whether or not they eventually
converge. Similarly Q_k is one residue-class zeta sum minus a finite explicitly
known set: remove y<a_H and the members of A_(H,k) in the eligible residue class.

This trades forward source-range enumeration for inverse-cone growth. The cone
still grows rapidly with k, so it is not an all-time proof or a cost-free method.

### Elementary tail inequalities used in the certificate

For f(x)=x^(-3/2), the trapezoid error on [n,n+1] has Peano kernel
(t-n)(n+1-t)/2, which lies in [0,1/8]. Summing gives

\[
0\le\sum_{n>N}n^{-3/2}
 -\left(2N^{-1/2}-\tfrac12N^{-3/2}\right)
\le\tfrac3{16}N^{-5/2}.                               \tag{7}
\]

The same argument applied to (m+3t)^(-3/2) gives

\[
0\le\sum_{j\ge0}(m+3j)^{-3/2}
 -\left(\tfrac23m^{-1/2}+\tfrac12m^{-3/2}\right)
\le\tfrac9{16}m^{-5/2}.                               \tag{8}
\]

Use N=65536 and common denominator B=2^96. Every weight is enclosed by

\[
a_n/B\le n^{-3/2}<(a_n+1)/B,\quad
 a_n=\left\lfloor\sqrt{B^2/n^3}\right\rfloor.
\]

Integer square-root tests certify the endpoints. Equations (7)-(8) enclose the
entire analytic tail. Subtracting finite sums in the outward direction proves
the emitted intervals. No floating-point value is used as a proof premise.

### Actual finite results

At H=1, k=40, the complete inverse cone has 267,024 vertices and

\[
0.1304093417816475<M_{40}(3/2,1)<0.1304093417818182.
\]

At H=64, k=36, it has 2,510,783 vertices and

\[
0.0488772216411294<M_{36}(3/2,64)<0.0488772216413000.
\]

The certificate checks (3) for every 0<=k<=36. The largest certified upper
share in that range is less than 0.341102341, at k=34.

The simpler statement Q_k<=M_k/3 is **refuted**: at H=64, k=19, the exact lower
bound for Q_k exceeds the exact upper bound for M_k/3. This is an actual finite
Collatz-population counterexample to that proposed inequality, not evidence
against Collatz. It is the first such certified failure in the tested range.

The inverse enumeration and interval checker use different implementations.
This is implementation independence only, not independent mathematical review.

## 4. T-A3-102 — what a critical exceptional basin would have to look like

This connects the aggregate route back to the original forward-inverse exponent
race. Let E be the actual set of sources never reaching 1. Its forward and
backward invariance give n in E iff T(n) in E and 1,2 not in E. For s>0 write

\[
D_s(X)=\sum_{n\le X,n\in E}n^{-s},\qquad
D_{s,2}(X)=\sum_{n\le X,n\in E,n\equiv2\ (3)}n^{-s},
\quad \kappa_s=\frac{2^s-1}{3^s}.
\]

Let U=(3X+1)/2 and

\[
R_s(U)=\sum_{\substack{y\le U,y\in E\\y\equiv2\ (3)}}
y^{-s}\left[(1-1/(2y))^{-s}-1\right].
\]

Exact source partition gives

\[
\boxed{
D_{s,2}(X)-\kappa_sD_s(X)
=3^{-s}[D_s(X)-D_s(X/2)]
-[D_{s,2}(U)-D_{s,2}(X)]-R_s(U).}                       \tag{9}
\]

The correction R_s(U) is nonnegative and uniformly bounded in U: its summand
is O_s(y^(-s-1)), by the mean value theorem. There is no missing source-1 term,
because E omits the trivial cycle.

If E(X)=O(X^s), the two multiplicative-shell masses on the right are O(1).
Consequently

\[
\boxed{D_{s,2}(X)=\kappa_sD_s(X)+O(1).}                 \tag{10}
\]

If additionally D_s(X) tends to infinity, the weighted residue share must tend
to kappa_s. This is a quantitative inverse statement about any hypothetical
critical-growth exceptional set, not an equidistribution assertion.

For s=901/1000, the certificate encloses

\[
\kappa_s=0.3223391707\ldots<1/3.
\]

Hence such a critical exceptional basin has a persistent residue-2 deficit
relative to uniform ternary mass. In particular, at that exponent, a critical
upper count E(X)=O(X^s) together with a limiting lower residue share strictly
above kappa_s would close Collatz **conditional on** the imported predecessor
lower bound: that lower bound forces D_s(X)>=c log X-O(1). Neither the critical
upper count nor the incompatible residue-share lower bound is proved here.

PR #90 already proves the critical weighted-mass bridge; we do not claim that
bridge as new. Equation (9), the resulting forced residue bias, and the finite-time
aggregate test above are the additional interfaces in this packet.

## 5. Failed shortcut and exact remaining work

Uniform ambient residue share 1/3 cannot replace the survivor-conditioned share:
the certified k=19 example refutes it. The weaker 69/200 ceiling survives the
present finite test, but no induction across k has been found. Its first missing
step is control of the ternary distribution **after conditioning on the entire
surviving history**. More inverse-cone levels alone do not supply that step.

The native all-time target (3) uses no external predecessor theorem, no
unexamined convergence range, and no pointwise inverse supersolution. The only
external mathematical dependence in this file is the explicitly conditional
last implication in Section 4. See [SOURCES.md](SOURCES.md).

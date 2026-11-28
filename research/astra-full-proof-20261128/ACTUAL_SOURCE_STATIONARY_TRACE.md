# The whole positive source average as one conditional stationary trace

**Written exact identity and source-qualified full-proof interface.**
This note aggregates the integer-window argument in concurrent
[PR217, Section 4, at head 6b5e0ce](https://github.com/GettysburgResearch/collatz/blob/6b5e0ce5135ba779af6f5b3559175ad47b96eea7/research/astra-collision-factor-bridge-20261128/factoring/CONDUCTOR_AND_STATIONARY_TRANSFER.md).
That source proves a uniform error for one fixed endpoint and grade.
Here a single source injection handles all endpoints and grades at once,
so their number does not multiply the error. Its separate finite Lean
receipt is not a local compile by this pass.

**Concurrent overlap, checked at the closing review.** PR217 subsequently
published the same whole-law shifted-window aggregation in
[STATIONARY_COLLISION_CONSUMER.md at e9c31f5](https://github.com/GettysburgResearch/collatz/blob/e9c31f56099c9f7df07ed2ecb82a93883d7a74bd/research/astra-collision-factor-bridge-20261128/factoring/STATIONARY_COLLISION_CONSUMER.md),
including its two-copy collision consumer and exact one-copy selection
normalization. This packet's signed postcritical consumer and arbitrary
word payoff formulation are retained here; the common aggregation is
credited as concurrent work, not claimed as an exclusive new theorem.

Let \(N,h\) be positive integers. A length-\(h\) binary word \(w\) has
odd count \(q(w)\) and affine map
\[
 F_w(x)=A_w x+B_w,\qquad A_w=3^{q(w)}2^{-h}.
\]
Choose any independent random seed \((R,Z)\) with
\(R\ge0\) real and \(Z\in\mathbf Z_3\). The same word acts on its two
coordinates, giving \(R_h=F_w(R)\), \(Z_h=F_w(Z)\).
For each positive ordinary integer \(y\) define
\[
 E(w,y;R,Z)=
 \{Z_h\equiv y\pmod{3^{q(w)}},\
                  0<y-R_h\le A_w N\}.                         \tag{1}
\]
All endpoint sums below are finite for a fixed seed and word.

## Exact simultaneous source identity

For every bounded real payoff \(G(w,y)\), pointwise in the seed,
\[
 \sum_{|w|=h}\sum_{y\ge1}G(w,y){\bf1}_{E(w,y;R,Z)}
 =\sum_{n=\lfloor R\rfloor+1}^{\lfloor R\rfloor+N}
                  G(w_h(n),T^h n).                            \tag{2}
\]
Here \(w_h(n)\) is the actual native word of the single ordinary source
\(n\). No alternative representative is selected at a later clock.

To prove (2), write \(B_w=C_w/2^h\). The full ternary congruence in
(1) says \(3^{q(w)}\mid 2^h y-C_w\). Thus
\[
 n=(2^h y-C_w)/3^{q(w)}
\]
is an ordinary integer. The real inequality is exactly \(R<n\le R+N\).
Backward parity induction from the integral endpoint forces \(w=w_h(n)\):
an even reverse branch gives an even binary integer, and an odd reverse
branch gives an odd binary integer. Starting at the positive real \(n\)
also makes every actual forward state positive. Conversely every integer
in this shifted window gives precisely one selected pair \((w,y)\).
The membership of \(Z\) in \(\mathbf Z_3\) is essential to the full
congruence cancellation; its law and its correlation with \(R\) are arbitrary.

Consequently, if \(W\) is an independent uniform word, the seeded
normalized statistic
\[
 \mathcal S_{h,N}(G)=\frac{2^h}{N}
     \mathbb E\sum_{y\ge1}G(W,y){\bf1}_{E(W,y;R,Z)}
\]
obeys
\[
 \left|\mathcal S_{h,N}(G)-
       \frac1N\sum_{n=1}^N G(w_h(n),T^h n)\right|
 \le \frac{2\|G\|_\infty}{N}\mathbb E\min(R,N).                 \tag{3}
\]
For a fixed shift \(j\), the symmetric difference of the two length-\(N\)
integer windows has \(2\min(j,N)\) members. Equation (2) proves (3)
directly, without summing a separate error over words, grades, or endpoints.

## A single rare event with exactly known probability

Suppose \(N\le2^h\), and let \(E_{h,N}\) mean that some \(y\) satisfies
(1), using the actual random grade \(Q_h=q(W)\). At most one such \(y\)
exists: candidate integers are separated by \(3^{Q_h}\), while the real
window has length \(3^{Q_h}N/2^h\le3^{Q_h}\) with one endpoint excluded.
Applying (2) to \(G=1\) gives the exact conditional normalization
\[
 \Pr(E_{h,N}\mid R,Z)=N2^{-h}.                                \tag{4}
\]
In particular conditioning on this event preserves the entire seed law.
It need not preserve the law of the future word or its odd count.
If \(Y\) denotes the unique selected integer, then
\[
 \mathcal S_{h,N}(G)=\mathbb E[G(W,Y)\mid E_{h,N}].             \tag{5}
\]

This event can be written as a one-sided distance to a full ternary
lattice. Let \(z_q\) be the representative of \(Z_h\bmod3^q\) in
\(\{0,\ldots,3^q-1\}\). The smallest lattice point strictly above
\(R_h\) is
\[
 y_+=z_q+3^q\left(1+
                  \left\lfloor\frac{R_h-z_q}{3^q}\right\rfloor\right).
\]
Then \(E_{h,N}\) is exactly
\[
                  0<\frac{y_+-R_h}{3^q}\le N2^{-h}.           \tag{6}
\]
The use of the lattice point above the nonnegative real coordinate is
what retains positive ordinary inputs.

## Stationary seed and the signed full-proof target

Take the jointly stationary real/ternary seed for independent fair affine
branches. Its real coordinate has, for every \(0<\alpha<1\),
\[
 \mathbb E R^\alpha\le
 M_\alpha=\frac{2^{-\alpha-1}}
 {1-(1+3^\alpha)/2^{\alpha+1}}<\infty.
\]
The nonnegative affine series and subadditivity prove this bound directly,
as in the cited PR217 source. Therefore (3) is at most
\(2\|G\|_\infty M_\alpha N^{-\alpha}\). The endpoint pair
\((R_h,Z_h)\) has the stationary marginal law, while its correlation
with the future grade and earlier bits is retained.

The displayed moment constant is \(O((1-\alpha)^{-1})\) as
\(\alpha\uparrow1\): the denominator has a simple zero there, with
coefficient \((3/4)\log3-\log2>0\) in its expansion in \(1-\alpha\). Taking
\(\alpha=1-1/\log N\) for \(N\ge e^2\) improves the error to
\(O(\|G\|_\infty\log N/N)\), as in the concurrent PR217 whole-law
note. The fixed-\(\alpha\) estimate already suffices below.

Use \(N=2^k\), \(M=\lfloor k/(1-\log_2(3)/2)\rfloor\), and even
\(g\sim k^{3/5}\), with \(h=M+g\). Set
\[
 G(W,Y)=\frac{Q_h(W)-Q_M(W)-g/2}{g},
                       \qquad \|G\|_\infty\le1/2.
\]
The [signed first-moment consumer](descent/FIRST_MOMENT.md) now shows
that the following one conditional estimate would imply full Collatz:
\[
 \boxed{\quad
 \liminf_{k\to\infty}
 \mathbb E\left[
 \frac{Q_{M+g}-Q_M-g/2}{g}\,\middle|\,E_{M+g,2^k}
 \right]\le0 .\quad}                                         \tag{7}
\]
The replacement error is at most \(M_\alpha2^{-\alpha k}\).
This is a whole-source statement, not a sum of uncontrolled pointwise
approximations.

**Equation (7) remains open.** Although the endpoint is jointly stationary
and the event has the exact probability (4), the grade cannot be made
independent of that event. Its mass is exponentially small in \(k\).
Unconditional weak convergence, a stationary marginal, or a polynomial
absolute error does not bound the normalized conditional mean in (7).
This note supplies the precise stationary observable, not its sign.

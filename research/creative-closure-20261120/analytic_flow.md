# Signed Hardy flows inside the known basin of one

**Status: PROPOSED, with complete elementary deductions below and exact
finite certificates. No Collatz proof.** The attempted analytic closure
instead produces an explicit reason that signed fixed points cannot be
counted as exceptional ordinary components. The operator has an
infinite-dimensional exact fixed space already on a constructively known
subset of the basin of 1.

The main construction concerns the **unweighted Hardy space**, not a
weighted Bergman space and not the derivative-weighted operators in
PR156. It supplies actual eigenvectors, rather than only approximate
eigenvectors. No priority over the wider operator-theory literature is
claimed.

## 1. Normalization and the analytic attempt

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

Identify \(\mathcal H=H^2_+(\mathbb D)\) with \(\ell^2(\mathbb N_{>0})\):
\(f(z)=\sum_{n\ge1}a_nz^n\) has norm squared \(\sum_n|a_n|^2\).
There is no coefficient at zero. Define the pushforward and pullback by

\[
(Qa)_m=\sum_{T(n)=m}a_n,\qquad (Pa)_n=a_{T(n)}.
\tag{1}
\]

Each fiber has at most two elements. Hence both are bounded, \(P=Q^*\),
and \(\|P\|,\|Q\|\le\sqrt2\). Explicitly,

\[
Pz^m=z^{2m}+\mathbf1_{m\equiv2\ (3)}z^{(2m-1)/3}.
\tag{2}
\]

The original idea was to use regularity or a Fredholm argument for the
analytic functional equation of an invariant component indicator.
The fixed-point equation itself is classical, not a new reduction:

\[
f(z^3)=f(z^6)+\frac1{3z}\sum_{r=0}^2\omega^r f(\omega^r z^2),
\qquad \omega=e^{2\pi i/3}.
\tag{3}
\]

Coefficient comparison makes (3) exactly \(Pa=a\). A bounded component
indicator defines a holomorphic function in the disk, but need not lie
in \(\mathcal H\). In fact \(\ker(I-P)=\{0\}\) on \(\mathcal H\):
its even-coordinate equations say \(a_{2n}=a_n\), and any nonzero
coefficient would repeat on an infinite dyadic ray, contradicting square
summability. This observation excludes the known constant labeling as
well as any hypothetical exceptional labeling. It is not a proof of
analytic uniqueness in the larger holomorphic space.

### Primary source boundary

Berg and Meinardus's 1994 functional equation is credited in
[Efrem, arXiv:2510.06736v1, section 1.1](https://arxiv.org/html/2510.06736v1)
and is reproduced directly above. The root-of-unity expression is only a
coefficient identity; no analytic continuation follows from it.

[Neklyudov, arXiv:2106.11859v9](https://arxiv.org/pdf/2106.11859v9),
Proposition 4.2, Lemma 4.3 and Theorem 4.4, uses these adjoint operators
and an index expression involving their fixed spaces. The later corollary
here addresses the finite Fredholm interpretation at this exact Hardy
normalization, not every convention for an extended index and not the
paper's other results.

[Béhani, arXiv:2303.03203v1](https://arxiv.org/pdf/2303.03203v1),
Definition 2.2 and Proposition 2.3, credits earlier signed two-ray
eigenvectors. Those vectors belong to the unweighted Hardy space for
\(|\lambda|<1\). The cited Bergman and weighted-space theorems retain
their own weights. Below, branching and splitting the flow instead of
using a single ray permits \(\lambda=1\), and a whole disk slightly
beyond it, in the unweighted space.

## CAF-001: a genuine binary inverse tree with bounded ordinary clocks

Let \(p>1\) be odd and prime to three. If \(p\equiv1\pmod3\), consider
the exponents \(2,4,6\); if \(p\equiv2\pmod3\), consider \(3,5,7\).
For each candidate put

\[
I_j(p)=\frac{2^jp-1}{3}.
\tag{4}
\]

All three candidates are positive odd integers. Exactly one is divisible
by three: the three values \(2^jp\pmod9\) are \(1,4,7\), in some order.
Retain the other two, ordered by their exponents \(j_0<j_1\).
They are odd ternary units and are strictly larger than \(p\), since
\(j_i\ge2\) and \(p>1\). Moreover,

\[
3I_j(p)+1=2^jp,\qquad
T^j(I_j(p))=p,
\qquad j\le7.
\tag{5}
\]

There is exactly one odd step followed by \(j-1\) even steps. The odd
map \(U(n)=(3n+1)/2^{v_2(3n+1)}\) therefore sends each child to its
parent.

Iterate the two retained choices starting at \(p_*=5\). This is a
binary tree of distinct positive ordinary integers. A repeated vertex
would have two different deterministic forward \(U\)-histories to 5,
or would put a larger descendant back at an ancestor, both impossible.
Every vertex reaches 5, then 1, by its displayed finite ordinary path.

The first children of 5 are 13 and 53, with exponents 3 and 5. The
discarded candidate is 213. Thus the entire tree is a constructive
subset of the actual basin of 1, requiring no unproved convergence input.

## CAF-002: exact square-summable stationary flows

Fix any vertex \(p\) of this tree. Put odd-node weight zero at \(p\),
weight \(+1\) and \(-1\) at its two children, and divide the parent's
weight equally between the two children at every later generation.
At odd depth \(d\ge1\), each of the \(2^d\) weights has modulus
\(2^{1-d}\). Consequently,

\[
\sum_{v\text{ odd}}|a_v|^2
=\sum_{d\ge1}2^d2^{2-2d}=4.
\tag{6}
\]

Extend a child weight along its literal shortcut path to its odd parent.
At an even vertex, add the contributions of the two child paths if they
overlap. Such overlaps can occur only between children of the same odd
parent: every internal vertex has the unique odd part equal to that
parent. At every retained odd parent the incoming sum equals its weight.
At the root the incoming sum is zero. Hence no mass leaks into the
forward orbit below \(p\).

Every nonroot odd parent has at most six internal even vertices, each
of modulus at most its own weight's modulus. The root's two paths cancel
on their common part and leave at most four internal vertices of modulus
one, because \(j_1-j_0\le4\). Thus the resulting full sequence satisfies

\[
4\le\|a\|_2^2\le7\cdot4+4=32,
\qquad Qa=a.
\tag{7}
\]

The conservation identity holds at every ordinary integer, including
unselected vertices: only displayed edges have nonzero source weights,
and their endpoints are displayed, or cancel at the root. Boundedness
of \(Q\) and the convergent square sum justify the Hilbert-space
identity as well as the pointwise one.

This is a signed stationary flow with infinite total variation. Its odd
generation has total absolute weight 2 at every depth, so \(a\notin\ell^1\).
Every integer in its support nevertheless reaches 1. It encodes neither
a nontrivial cycle nor a divergent orbit.

### Infinite multiplicity with disjoint ordinary supports

Label the selected child choices 0 and 1. The vertices with words
\(1,01,001,\ldots,0^k1,\ldots\) form an antichain in the tree. Their
entire ordinary inverse subtrees are disjoint: otherwise a deterministic
forward orbit would pass through two incomparable vertices. The even
parts of the constructed flows remain disjoint as well, since each has
the odd part of a vertex in its own subtree.

Apply the preceding construction at each antichain vertex. It gives
infinitely many nonzero, pairwise orthogonal vectors in
\(\ker(I-Q)\), all supported inside the known basin of 1. Therefore

\[
\dim\ker(I-Q)=\infty
\quad\text{on unweighted }H^2_+(\mathbb D).
\tag{8}
\]

In particular, subtracting the one polynomial for the trivial cycle does
not make this fixed space trivial or finite dimensional.

## CAF-003: an open disk of exact eigenvalues beyond the unit circle

The construction is not confined to stationarity. For

\[
0<|\lambda|<2^{1/14},
\tag{9}
\]

give the two children of the zero-weight root the weights
\(+\lambda^{j_0}\) and \(-\lambda^{j_1}\). At every nonroot parent of
weight \(a_p\), give its exponent-\(j\) child weight
\(\lambda^j a_p/2\).

For an even internal vertex \(2^kp\), a child with exponent \(j>k\)
contributes \(\lambda^k a_p/2\). At the root use the corresponding
signed contribution \(\pm\lambda^k\). Add overlapping contributions.
Directly checking the incoming sums now gives

\[
Qa=\lambda a.
\tag{10}
\]

For example, at an odd parent the two last even edges contribute
\(\lambda a_p/2\) each; at the root they cancel. At an internal vertex,
moving one step forward divides its child contribution by \(\lambda\),
which is precisely the eigenvector conservation equation.

Let \(r=|\lambda|\) and

\[
q(r)=\tfrac12\max(r^4,r^{14})<1.
\tag{11}
\]

The sum of squared odd-child weights is at most \(q(r)\) times the
parent's square weight. The initial odd generation has square sum at
most \(4q(r)\). Therefore the total odd square sum is at most
\(4q(r)/(1-q(r))\). The internal even contribution for each nonroot
parent is bounded by
\(\sum_{k=1}^6r^{2k}|a_p|^2\); the root contributes only finitely many
such terms. This proves membership in \(\mathcal H\). The maximum in
(11) is necessary: for \(r<1\) it is the *smallest* exponent that gives
the upper bound.

Antichain roots again give infinitely many disjoint-support eigenvectors
for every \(\lambda\) in (9). At \(\lambda=0\), ordinary collision
vectors also give infinite multiplicity. For example, with
\(m=2^{2k+1}\), the two sources
\(2m\) and \((2m-1)/3\) reach \(m\) in one shortcut step, are distinct
across \(k\ge1\), and both reach 1. Their monomial differences lie in
\(\ker Q\).

Thus the full disk \(|\lambda|<2^{1/14}\) is contained in the point
spectrum with infinite multiplicity on constructively convergent support.
The radius is a convenient rigorous bound, not an optimal spectral-radius
claim.

### Exact finite truncations, including every boundary term

Retain odd generations through depth \(D\), together with every internal
shortcut vertex on their edges. Call the finite vector \(a^{[D]}\).
All interior conservation equations are exact. Its residual is supported
**only** at its odd leaves:

\[
(Q-\lambda I)a^{[D]}=-\lambda a^{[D]}
\quad\text{on leaves},\qquad0\quad\text{elsewhere}.
\tag{12}
\]

For \(\lambda=1\), this gives the exact identity

\[
\|(Q-I)a^{[D]}\|_2^2=2^{2-D}.
\tag{13}
\]

Its residual's \(\ell^1\) norm is nevertheless exactly 2 at every
depth. Vanishing square-energy residual therefore does not supply a
vanishing original-mass defect. The finite vectors' total absolute mass
is at least \(2D\), so their limit is not a finite signed source measure.

The missing generations have a proved geometric square tail. A finite
replay of (12) supports the implementation; the infinite eigenvector
claim follows from the preceding uniform tail and conservation proof.

## CAF-004: positivity changes the meaning of a fixed point

For any \(1\le p<\infty\), a nonnegative sequence \(a\in\ell^p\)
with \(Qa=a\) is supported on periodic ordinary states and is constant
around each cycle. Conversely every nonnegative sum of cycle indicators
that belongs to \(\ell^p\) is fixed.

Indeed \(a_{T(n)}\ge a_n\). If the forward orbit of a positive
coefficient contains infinitely many distinct values, all those values
have coefficient at least \(a_n>0\), contradicting \(\ell^p\)
summability. If it eventually reaches a cycle, coefficients along the
cycle are nondecreasing and hence equal. At each cycle vertex the
coefficient from the preceding cycle vertex already exhausts its whole
incoming sum. Positivity forces every off-cycle incoming coefficient to
vanish. Repeating backward excludes every positive preperiodic coefficient.

Consequently the signed flows in CAF-002 cannot be replaced by positive
ones. Positivity can make stationary vectors represent cycles, but it
also removes every escaping ordinary orbit from this finite-\(p\)
stationary cone. A full proof would still need cycle exclusion and a
separate escape argument. This is compatible with PR157's positive
*time-accumulated* source criterion, which is a different object.

## CAF-005: quantitative finite coercivity, and its sharp order

There is a useful finite estimate even though no degree-independent gap
exists. Let \(f(z)=\sum_{n=1}^D a_nz^n\) and
\(L=1+\lfloor\log_2D\rfloor\). Then

\[
\|f\|_2^2\le\frac{L(L+1)}2\|(I-P)f\|_2^2.
\tag{14}
\]

To prove it, partition the support into dyadic rays with odd bases. For
one ray write \(b_0,\ldots,b_{\ell-1}\), where \(\ell\le L\), and
append \(b_\ell=0\). The residual's even coordinates contain every
\(d_i=b_i-b_{i-1}\), \(1\le i\le\ell\), including the last edge
outside the original polynomial's support. Since
\(b_j=-\sum_{i=j+1}^{\ell}d_i\), Cauchy--Schwarz and summation give

\[
\sum_{j=0}^{\ell-1}|b_j|^2
\le\sum_{i=1}^{\ell}|d_i|^2
\sum_{j=0}^{i-1}(\ell-j)
\le\frac{\ell(\ell+1)}2\sum_{i=1}^{\ell}|d_i|^2.
\]

Different rays use distinct even coordinates. Discarding the nonnegative
odd-coordinate energy and summing proves (14).

The logarithmic dependence on degree cannot be removed or improved to
smaller order. For \(K=2h-1\), put the triangular integer coefficients
\(1,2,\ldots,h,\ldots,2,1\) on the powers
\(z^{3\cdot2^j}\), \(0\le j<K\). Every support integer reaches 3,
then 1. All these exponents are divisible by three, so (2) shifts each
monomial to its double, with no omitted odd predecessor. Directly,

\[
\|f\|_2^2=\frac{2h^3+h}{3},\qquad
\|(I-P)f\|_2^2=2h,
\qquad
\frac{\|(I-P)f\|_2^2}{\|f\|_2^2}
=\frac6{2h^2+1}.
\tag{15}
\]

Its degree is \(3\cdot2^{2h-2}\). Thus the optimal order of the uniform
finite-polynomial condition number is \(\log D\). This is a finite
norm estimate, not a stopping-time estimate.

Because \(I-P\) is injective on \(\mathcal H\), (15) also proves its
range is not closed: an injective bounded operator with closed range
would be bounded below. By the closed-range theorem the range of
\(I-Q\) is not closed either; it is dense because \(\ker(I-P)=0\).
Together with (8), neither operator is Fredholm here. A conventional
finite Fredholm index therefore cannot supply a cycle bound at this
normalization. If the index expression is read as an extended difference
of kernel dimensions instead, its positive kernel term is already
infinite in the known basin, so it yields no finite exclusion. This is
the precise boundary of the attempted index route.
Restoring the coefficient at zero adds only a one-dimensional fixed
summand. It changes neither infinite multiplicity nor the failure of
Fredholmness.

## CAF-006: analytic forcing is not a regularity bootstrap

Even an entire right-hand side can have a disk-holomorphic solution with
a natural boundary in this problem. For any positive \(m\) divisible by
three,

\[
G_m(z)=\sum_{j\ge0}z^{m2^j},\qquad (I-P)G_m=z^m.
\tag{16}
\]

There is a short direct proof of the natural boundary. If \(\zeta\) is
a root of unity whose order divides \(m2^k\), every term with \(j\ge k\)
has phase 1 along \(z=r\zeta\). As \(r\uparrow1\) their positive sum
diverges, while the finitely many earlier terms stay bounded. Such roots
are dense on the circle. Hence no open arc admits analytic continuation.
For \(m=3\), every coefficient represents an ordinary input that reaches
1. Smooth forcing does not make this resolvent regular across the circle.

This example is a special case of prior inverse-orbit natural-boundary
phenomena; see [Bell--Lagarias, arXiv:1408.6884v1](https://arxiv.org/pdf/1408.6884v1).
It is recorded here as the exact control that stopped the proposed
regularity bootstrap, not as a new discovery of natural boundaries.

## What would still be needed

The component-indicator equation belongs to a larger holomorphic space,
not the Hardy fixed space of its adjoint. A closing theorem must impose
and use the actual positivity, arithmetic, and source constraints there.
The signed eigenvectors above show that exact spectral data alone can be
generated entirely by known convergent integers. The positive stationary
cone removes that artifact but cannot see escape. No argument here proves
the physical forward-five law, the reciprocal-psi upper estimate, or
universal termination.

The exact replay is [creative_analytic_flow.py](../../experiments/creative_analytic_flow.py),
with its deterministic [report](../../reports/2026-11-20-creative-closure/analytic-flow-report.json).
It checks finite trees and all their physical edges, merged internal flow,
every residual coordinate including leaves, disjoint-support examples,
the geometric certificates, and the finite coercivity bound. These
computations do not replace the infinite proofs above.

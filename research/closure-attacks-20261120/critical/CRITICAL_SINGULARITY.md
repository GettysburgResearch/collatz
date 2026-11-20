# Critical component mass and the boundary that its normalization loses

**Status: PROPOSED, complete source-qualified consequences; no Collatz
resolution.** The external positive-density theorem below is an explicit
dependency, not a newly accepted theorem of the resident baseline. The
conditional endpoint limit and its binary positive-density consequence
already occur in the cited PR146/PR155 sources. The contribution here is
the combined critical singularity statement, its source-loss interpretation,
and the metric-label and directed-energy formulations.

All populations are actual positive ordinary integers. Use the shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

A set \(K\) is invariant when \(1_K(Tn)=1_K(n)\) for every \(n\).
It may be one merger component or any union of components. Put

\[
 A_K(X)=\#(K\cap[1,X]),\qquad
 D_K(s)=\sum_{n\in K}n^{-s},
\]
\[
 \partial_3K=\{n:1_K(3n)\ne1_K(n)\},\qquad
 B_K(s)=\sum_{n\in\partial_3K}n^{-s}.
\]

## 1. Exact inputs and their status

**PD: fixed-target positive lower density.** For every fixed positive
ordinary target \(u\) not divisible by three, its predecessor set has
strictly positive lower natural density. This is the theorem stated by
Lech Mazur in the September 2026 primary record
[Positive lower density of Collatz predecessor sets](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/),
with its separately advertised
[proof artifact](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html).
No hypothesis that \(u\) reaches 1 is used. This packet does not rebuild
the advertised Lean supplement and does not promote PD into the resident
accepted baseline. It uses PD as a named source-qualified dependency.

Every nonempty invariant set contains an eligible target: strip powers of
two from any member; if the remaining odd integer is divisible by three,
take one ordinary odd step. That endpoint is a ternary unit. Its whole
predecessor set remains in \(K\). The primary record uses the ordinary
unaccelerated map. Shortcut invariance also gives
\(f(3n+1)=f(n)\) for odd \(n\), since \(n\) and \(3n+1\) have
the same shortcut successor \((3n+1)/2\). Thus its predecessor paths
preserve exactly the invariant sets used here. Consequently PD implies

\[
 K\ne\varnothing\quad\Longrightarrow\quad
 \underline d(K)>0.                                      \tag{1}
\]

**UP: actual tripling synchronization bound.** For an absolute \(C\),

\[
 \#\{n\le X:n\text{ and }3n\text{ never meet}\}
 \le \frac{CX}{\sqrt{\log(2X)}}\qquad(X\ge1).             \tag{2}
\]

The exact repository source is PR146,
`6863d298187af8b2619efbf78cc4b0aa8e627393`,
[THREE_RAY_UPPER.md](https://github.com/GettysburgResearch/collatz/blob/6863d298187af8b2619efbf78cc4b0aa8e627393/research/upper-bit-mergers/THREE_RAY_UPPER.md).
Its proof reconstructs the fair pair process only on complete ordinary
binary source blocks. It does not assume fresh bits after conditioning on
an invariant component. The source also proves a translated-interval
version; only (2) is needed here. The present author checked the printed
holding-time, return-walk and finite-block counting argument, but did not
run a separate simulation or an external proof artifact.

**EP: finite harmonic tripling defect forces a profile limit.** If a bounded
real or complex ordinary invariant label \(f\) obeys

\[
 \sum_{n\ge1}\frac{|f(3n)-f(n)|}{n}<\infty,                \tag{3}
\]

then its logarithmic profiles
\(g_k(t)=f(\lfloor2^{k+t}\rfloor)\), \(0\le t<1\), converge
in \(L^1\) to a constant \(c\), and

\[
 2^{-k}\sum_{2^k\le n<2^{k+1}}|f(n)-c|\longrightarrow0.   \tag{4}
\]

For binary labels, \(c\in\{0,1\}\). The source is PR155,
`92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
[ENDPOINT_BOUNDARY.md, Section 1](https://github.com/GettysburgResearch/collatz/blob/92f499b9d340d1ff8cc643c3eef3477d61b477c1/research/gemini-dirichlet-global-20261120/ENDPOINT_BOUNDARY.md).
It uses homogeneous ordinary variation, Tonelli summation and irrational
rotation on the logarithmic circle. In particular it assumes (3), rather
than inferring it from boundedness. PR146 already states the binary
positive-upper-density consequence in
[THREE_RAY_DENSITY.md](https://github.com/GettysburgResearch/collatz/blob/6863d298187af8b2619efbf78cc4b0aa8e627393/research/upper-bit-mergers/THREE_RAY_DENSITY.md),
Section “A separate criterion when both components have positive upper
density.” The harmonic-divergence implication below is credited to that
earlier mechanism.

The PR155 finite-variation input is separately frozen there at PR146
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`. No inherited review is silently
extended to a later file. The current PR146 head above supplies UP and
the directed-return statement used in Section 4.

## 2. CS-001: the forced critical singularity

**Theorem, conditional on PD, UP and EP.** If \(K\) is a nonempty proper
ordinary invariant set, then, as \(\epsilon\downarrow0\),

\[
 D_K(1+\epsilon)\asymp_K\epsilon^{-1},\qquad
 D_{K^c}(1+\epsilon)\asymp_K\epsilon^{-1},                \tag{5}
\]
\[
 B_K(1+\epsilon)\longrightarrow\infty,
 \qquad B_K(1+\epsilon)=O(\epsilon^{-1/2}),               \tag{6}
\]
\[
 \boxed{\frac{B_K(1+\epsilon)}{D_K(1+\epsilon)}
          =O_K(\sqrt\epsilon)\longrightarrow0.}           \tag{7}
\]

All three nonnegative Dirichlet series have convergence abscissa exactly
one and diverge at that abscissa. Equation (5) asserts two-sided order,
not existence of a residue or a natural density for \(K\).

**Proof of the component mass.** By (1), choose \(d>0\) and \(X_0\)
such that \(A_K(X)\ge dX\) for every \(X\ge X_0\). Nonnegative
partial summation gives, for \(s>1\),

\[
 D_K(s)=s\int_1^\infty A_K(x)x^{-s-1}\,dx
 \ge \frac{sd X_0^{1-s}}{s-1}.                           \tag{8}
\]

The upper bound \(D_K(1+\epsilon)\le\zeta(1+\epsilon)
\le1+1/\epsilon\) is elementary. Apply the same argument to the
nonempty complement to obtain (5). These estimates also show divergence
at one directly.

**Proof of the boundary upper bound.** An ordinary merger preserves every
invariant label, so \(\partial_3K\) is contained in the failure set of
(2). Another nonnegative partial summation, with \(t=\log x\), yields

\[
\begin{split}
 B_K(1+\epsilon)
 &\le C(1+\epsilon)\int_1^\infty
          \frac{x^{-1-\epsilon}}{\sqrt{\log(2x)}}\,dx\\
 &\le C(1+\epsilon)\int_0^\infty e^{-\epsilon t}t^{-1/2}\,dt\\
 &= C(1+\epsilon)\sqrt\pi\,\epsilon^{-1/2}.
\end{split}                                               \tag{9}
\]

Only a nonnegative integral was used. The estimate does not condition the
pair process on the putative component.

**Proof of critical divergence.** If \(B_K(1)<\infty\), EP applied to
\(1_K\) gives (4) with \(c=0\) or \(1\). Hence either \(K\) or
\(K^c\) has natural density zero: sum the dyadic shells in (4), treating
finitely many early shells separately. This contradicts (1) for that
nonempty invariant set. Thus \(B_K(1)=\infty\). Monotone convergence
as \(\epsilon\downarrow0\) proves the first part of (6). Finiteness
for every \(s>1\), divergence at one and monotonicity then give the
claimed abscissa. Dividing (9) by (8) proves (7). QED.

At the counting level the same argument gives

\[
 \sum_{\substack{n\le X\\n\in\partial_3K}}\frac1n
 \longrightarrow\infty,
 \qquad
 \sum_{\substack{n\le X\\n\in\partial_3K}}\frac1n
 =O(\sqrt{\log(2X)}).                                   \tag{10}
\]

No lower divergence rate is claimed. Divergence may be arbitrarily slower
than the displayed upper rate under the estimates proved here.

## 3. CS-002: what a critical normalization necessarily forgets

For \(s=1+\epsilon\), define the genuine ordinary probability

\[
 \nu_{K,\epsilon}(\{n\})=
 \frac{1_K(n)n^{-1-\epsilon}}{D_K(1+\epsilon)}.           \tag{11}
\]

If a nonempty proper \(K\) exists, then for every fixed finite \(M\),

\[
 \nu_{K,\epsilon}([1,M])\longrightarrow0,\qquad
 \nu_{K,\epsilon}(\partial_3K)=O_K(\sqrt\epsilon)
       \longrightarrow0.                               \tag{12}
\]

The first claim follows because the numerator over a fixed finite set is
bounded and the denominator grows like \(1/\epsilon\). The second
follows by bounding its numerator by \(B_K(1+\epsilon)\). Thus both
the fixed ordinary source and the separating boundary disappear from this
normalized population. This is a conclusion about the specified measures;
it is not a claim that the unnormalized boundary vanishes.

An endpoint argument that replaces the actual source by (11), discards
all normalized boundary terms, and then invokes compactness has therefore
discarded precisely the data distinguishing a hypothetical component.
Uniform finite-place marginals do not restore a fixed ordinary atom.
This explains why the feasible homogeneous critical residue balance is
compatible with the surviving source-persistent question.

Likewise, a uniform bound
\(D_K(1+\epsilon)\le C B_K(1+\epsilon)\) on this class, if it
could be proved for all invariant \(K\), would contradict (5)--(6) and
close the problem under the stated inputs. We have **not** refuted that
possible theorem by exhibiting a proper invariant set: none is known.
We have proved its incompatibility with the precise behavior forced by
the existence of such a set. There is no extension of PR155's subcritical
inequality being asserted here.

## 4. CS-003: finite critical energy of arbitrary metric labels is rigid

Let \((Y,d)\) be any metric space and let
\(f:\mathbb N_{>0}\to Y\) be ordinary invariant. No boundedness of
\(f\) or \(Y\) is required. Under PD and EP,

\[
 \sum_{n\ge1}\frac{d(f(3n),f(n))}{n}<\infty
 \quad\Longrightarrow\quad f\text{ is constant}.         \tag{13}
\]

Indeed, if \(f(a)\ne f(b)\), put \(L=d(f(a),f(b))>0\) and
\(h(n)=\min\{d(f(n),f(a)),L\}\). This is a bounded real invariant
label with tripling defect dominated pointwise by that of \(f\).
EP gives (4) for \(h\). The component of \(a\) has \(h=0\), and
the component of \(b\) has \(h=L\). Each has positive lower natural
density by PD. At least one of these two values stays at distance at
least \(L/2\) from the putative constant \(c\), contradicting the
density-zero conclusion of (4). This is a Lipschitz reduction of the
prior binary/real endpoint mechanism, not a new unconditional endpoint
estimate.

For bounded metric labels of diameter at most \(L\), UP also yields
the upper bound \(O(L\epsilon^{-1/2})\) for their tripling energy
at \(1+\epsilon\). If such a label is nonconstant, (13) shows that
its defect series has abscissa exactly one and diverges there.

For a real invariant label, both oriented energies diverge separately:

\[
 \sum_{n\text{ odd}}\frac{(f(3n)-f(n))_+}{n}=\infty,
 \qquad
 \sum_{n\text{ odd}}\frac{(f(n)-f(3n))_+}{n}=\infty       \tag{14}
\]

whenever \(f\) is nonconstant. To justify the separate directions,
use PR146's
[DIRECTED_TRIPLING.md](https://github.com/GettysburgResearch/collatz/blob/6863d298187af8b2619efbf78cc4b0aa8e627393/research/upper-bit-mergers/DIRECTED_TRIPLING.md)
at that same full SHA. Its return from \(3x\) to \(x\) uses ordinary
edges and forward triplings, with odd tripling sources drawn from a fixed
finite list of injective rational affine functions of \(x\), lying in
\([x/H,Hx]\). Along that path ordinary differences vanish, and

\[
 (f(3x)-f(x))_+
 \le\sum_{y\text{ queried}}(f(y)-f(3y))_+.              \tag{15}
\]

Sum (15) against \(x^{-s}\); injectivity, the finite list and height
comparability give \(E_+(s)\le C_s E_-(s)\), with extended
nonnegative sums allowed. Apply the same argument to \(-f\) for the
reverse comparison. Exact doubling contributes only the geometric factor
\((1-2^{-s})^{-1}\). Equation (13) forces the total energy to diverge
at \(s=1\), hence both terms in (14) diverge. This does not assume
that arbitrary bounded labels have summable defects.

## 5. Full five rays, and the remaining single-slice question

Define \(\delta_5f(n)=d(f(5n+1),f(n))\). Ordinary paths give
\(T^2(20x+1)=15x+1\), while doubling identifies \(f(4x)=f(x)\).
Therefore

\[
 d(f(3x),f(x))\le\delta_5f(3x)+\delta_5f(4x).           \tag{16}
\]

On odd \(x\), these two query sets are disjoint. At every \(s>0\),

\[
 \sum_{x\text{ odd}}x^{-s}d(f(3x),f(x))
 \le4^s\sum_{n\ge1}n^{-s}\delta_5f(n).                 \tag{17}
\]

Thus every nonconstant invariant metric label also has infinite full
five-ray harmonic energy. This comparison is PR155's existing bridge;
no square-root upper bound for the five-ray series follows from it.

The new neighboring packet proves that the **single multiplicative-five
law** \(f(5x)=f(x)\) for positive odd ternary units already forces
constancy. Its complete conditional integer descent is
[SINGLE_MULTIPLIER.md](../merger/SINGLE_MULTIPLIER.md).
An energy statement for this smaller domain is a different claim. The
exact partial bridge and its unfilled propagation step are in
[SINGLE_SLICE_ENERGY.md](SINGLE_SLICE_ENERGY.md). Neither the descent's
\(O(\log n)\) number of abstract stages nor the height of one stage
is a bound for weighted global congestion.

## 6. First unsupported closing inference

The rigorously available upper bound in (10) is not integrable and is
fully compatible with the forced harmonic divergence. No actual ordinary
boundary estimate of finite harmonic energy is proved. The proposed
single-slice finite-energy implication also needs a genuine global
transport lemma. Its two-class local identity is not such a lemma.

The new critical singularity description does not exclude a second
component, whether escaping or cyclic. It instead identifies exactly why
simple critical normalization loses that component, while retaining an
unnormalized finite-energy route that would be sufficient if an upper
estimate could be established.

# A singular continuous law for the actual discounted scalar

23 November 2026. Published parent:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb` (PR182).

**Status: proposed written theorems with exact finite controls. The
probability and measure arguments in this file are not formalized in
Lean. Collatz remains OPEN.**

This result concerns the scalar values of actual positive odd integer
sources as the source range increases. It proves their limiting law;
it does not replace an individual ordinary orbit by a random orbit.
The law is continuous and singular with respect to Lebesgue measure.
One consequence is that every fixed denominator grid captures a set
of sources of density zero. A countable union of those grids is still
allowed to capture every source.

## 1. Actual scalar and primary literature

For the actual odd accelerated orbit put

\[
q_0=q,\qquad g_i=v_2(3q_i+1),\qquad
q_{i+1}=(3q_i+1)/2^{g_i},\qquad
h(q)=\sum_{i\ge0}g_i/3^{i+1}.
\]

The input is precisely (PR182,
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`,
`research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`, R8-G1--G2;
blob `540110f09cf68e3309fd83fea9c7ae497536ded4`). It supplies the
unconditional identities and bounds

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\quad
h(q)=\sum_{i<M}\frac{g_i}{3^{i+1}}+3^{-M}h(q_M),\quad
q_M\le2^M q.                                      \tag{1}
\]

It also proves convergence of q if and only if `h(q)` lies in
`Z[1/3]`. No convergence assumption is used below.

Two primary sources suggest the method:

* Terence Tao, *Almost all orbits of the Collatz map attain almost
  bounded values*, [Definition 1.7, Proposition 1.9, and its Section 4
  proof](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F).
  These sections explicitly relate finite actual valuation words to
  independent positive geometric variables by ordinary residue
  cylinders. The finite cylinder calculation below is given in full.
* Boris Solomyak, [*Notes on Bernoulli convolutions*, Section 2,
  especially Theorems 2.1 and 2.4 and the accompanying
  proofs](https://u.math.biu.ac.il/~solomyb/RESEARCH/Bernotes.pdf).
  Fourier nondecay and preservation of Lebesgue types suggest the
  proof below. The present geometric digit distribution has countably
  many affine maps; the two-sign Bernoulli theorem is not applied to
  it verbatim. Its required statements are proved directly.

The original Jessen--Wintner AMS PDF was located but returned HTTP403;
it is not treated as an inspected input. No novelty claim relative to
the broader distribution literature is made.

## 2. Exact finite cylinders

Fix a positive gap word `w=(g_0,...,g_(M-1))`. Write

\[
A_j=\sum_{i<j}g_i,\quad A=A_M,\qquad
B=\sum_{j=0}^{M-1}3^{M-1-j}2^{A_j}.
\]

**R9-L1 (literal cylinder).** A positive odd q has exactly this
initial word if and only if

\[
\boxed{3^M q+B\equiv2^A\pmod {2^{A+1}}.}       \tag{2}
\]

Consequently this word occupies one odd residue class modulo
`2^(A+1)`.

For completeness, the forward implication follows by multiplying the
complete ordinary equations: `2^A q_M=3^M q+B`, with `q_M` odd.
For the reverse implication use induction on M. For M=1, (2) states
exactly that `v_2(3q+1)=g_0`. If M>1, write
`B=3^(M-1)+2^g_0 B_tail`, with `B_tail` odd, and reduce (2)
modulo `2^(g_0+1)`. Since `A>=g_0+1`, this forces
`3q+1=2^g_0 times an odd integer`. The actual next state is therefore
the positive odd integer `q_1=(3q+1)/2^g_0`. Dividing (2) by
`2^g_0` gives exactly the suffix condition at q_1. This proves every
intermediate quotient and every exact valuation, not just integrality
of a final affine formula. Since three is invertible modulo every
power of two, (2) specifies one residue; it is odd since B is odd.

Let `X>=1` be an integer, `N_X=ceil(X/2)`, and let `Q_X` be uniform
on the N_X positive odd integers through X. Counting in an arithmetic
progression gives

\[
\left|\mathbb P((g_0(Q_X),\ldots,g_{M-1}(Q_X))=w)
                 -2^{-A}\right|\le1/N_X.        \tag{3}
\]

The formula includes small sources and arbitrary positive words.
There is no assumption that the orbit reaches one.

## 3. A quantitative law for actual sources

Let `G_0,G_1,...` be independent with
`P(G_i=g)=2^(-g)` for positive integers g, and define

\[
H=\sum_{i\ge0}\frac{G_i}{3^{i+1}}.               \tag{4}
\]

This is almost surely finite, because the summands are nonnegative
and `E H=sum 2/3^(i+1)=1`. Also `H>=1/2`.

**R9-L2 (quantitative actual-source law).** For any real function f
with `|f|<=1` and Lipschitz constant at most one, and any integer M>=1,

\[
\boxed{
\left|\mathbb E f(h(Q_X))-\mathbb E f(H)\right|
\le 3^{-M}\left(2+\frac{\operatorname{bl}(X)+M}{3}\right)
 +\frac{2\binom{4M}{M}}{N_X}
 +2\left(\frac{81}{128}\right)^M.}             \tag{5}
\]

Here `bl(X)=floor(log_2 X)+1` is the positive binary bit length.
In particular the empirical measures of the actual h(q), with q
positive odd through X, converge weakly to the law of H.

**Proof.** Put `K=4M` and first truncate both scalars after M gaps.
The number of positive M-tuples with total A<=K is

\[
\sum_{A=M}^K\binom{A-1}{M-1}=\binom KM.          \tag{6}
\]

On these tuples (3) bounds the total sum of probability discrepancies
by `binom(K,M)/N_X`. The independent word has probability `2^(-A)`.
Moreover

\[
\mathbb E(4/3)^{G_i}=2,\qquad
\mathbb P\left(\sum_{i<M}G_i>K\right)
 \le 2^M(3/4)^K=(81/128)^M.                     \tag{7}
\]

The empirical mass outside the retained words is at most the
independent outside mass plus `binom(K,M)/N_X`. Splitting any bounded
test function over the retained set and its complement therefore
bounds its prefix expectation discrepancy by
`2 binom(K,M)/N_X + 2(81/128)^M`.

By (1), the actual discarded scalar tail is at most

\[
3^{-M}\left(1+\frac{\operatorname{bl}(X)+M}{3}\right).
\]

The independent discarded tail has expectation `3^(-M) E H=3^(-M)`.
The Lipschitz property and the triangle inequality give (5).

For example, choose `M=floor(log_2(X)/8)` for X>=256. Then
`binom(4M,M)<=2^(4M)<=sqrt(X)`, the displayed tail bounds tend to
zero, and so does the middle term since `N_X>=X/2`. Convergence in
the bounded Lipschitz metric implies weak convergence on the real
line. This statement retains actual deterministic integer sources
throughout its empirical side. It is not a stationarity claim for one
fixed Collatz trajectory. QED.

## 4. The limiting distribution is singular continuous

**R9-L3.** The law mu of H has no atoms and is singular with respect
to Lebesgue measure.

First its characteristic function is

\[
\phi(t)=\mathbb E e^{itH}
 =\prod_{j\ge1}\psi(t/3^j),\qquad
\psi(u)=\mathbb E e^{iuG_0}=\frac{e^{iu}}{2-e^{iu}}.
                                                               \tag{8}
\]

The finite product formula follows from independence; convergence
follows from almost sure convergence of (4) and bounded convergence.
Every factor is nonzero, and
`|psi(u)-1|<=E|exp(iuG_0)-1|<=2|u|`. Thus the product at `t=2 pi`
is nonzero by the elementary nonzero-product criterion. For every
integer N>=0, periodicity of psi gives

\[
\boxed{\phi(2\pi 3^N)=\phi(2\pi)\ne0.}         \tag{9}
\]

The first N factors on the left equal one, and the remaining factors
are those on the right. The Riemann--Lebesgue lemma now rules out
absolute continuity of mu.

To conclude pure singularity rather than merely a nonzero singular
part, consider the countable affine operator on finite measures

\[
\mathcal T\nu=\sum_{g\ge1}2^{-g}(S_g)_*\nu,
\qquad S_g(x)=(g+x)/3.                          \tag{10}
\]

Mu is fixed by this operator. It is the unique probability measure
fixed by it: the characteristic function of any fixed probability
satisfies `phi(t)=psi(t/3) phi(t/3)`. Iterating and using continuity
at zero yields exactly (8). Each S_g is an invertible affine map of
the line. It preserves absolute continuity and singularity, and a
countable sum of singular measures is still supported on a Lebesgue
null set. Uniqueness of the Lebesgue decomposition therefore shows
that the absolutely continuous part and the singular part of a fixed
measure are separately fixed by T. If the absolutely continuous
part of mu had positive mass, normalizing it would give a fixed
absolutely continuous probability measure. Uniqueness would make
this equal to mu, contradicting (9). Hence that part has mass zero.

Finally mu has no atoms. Otherwise the supremum A>0 of its atomic
masses is attained: only finitely many atoms can have mass at least
A/2, and a sequence of masses tending to A eventually lies among
them. At an atom x of mass A, (10) implies

\[
A=\sum_{g\ge1}2^{-g}\mu\{3x-g\}.
\]

The support is contained in `[1/2,infinity)`. Consequently only
finitely many g can contribute, namely those with `g<=3x-1/2`.
Each contribution has atomic mass at most A, so the right hand side
is at most A times a finite initial sum of `2^(-g)`, strictly less
than A. This contradiction proves atomlessness. QED.

This proof uses the actual law established in R9-L2. An arbitrary
abstract distribution would not on its own attach to the integer
sources.

## 5. Fixed arithmetic grids are thin; their union need not be

**R9-L4 (fixed-grid density zero).** For every fixed positive integer
D,

\[
\boxed{\lim_{X\to\infty}
\frac{\#\{1\le q\le X:q\text{ odd},\ h(q)\in D^{-1}\mathbb Z\}}
     {\lceil X/2\rceil}=0.}                     \tag{11}
\]

The grid `D^(-1) Z` is a closed countable subset of the real line.
Atomlessness gives it mu-measure zero. The closed-set inequality
in the Portmanteau theorem, applied to R9-L2, gives (11). The grid
need not be bounded. Finite unions of fixed grids obey the same
conclusion.

In particular, for every fixed r the actual sources whose triadic
certificate can use a denominator dividing `3^r` have density zero.
This identifies a concrete limitation of any uniformly fixed
denominator construction. It says nothing against certificates with
denominators depending on the source.

**R9-L5 (no countable-union inference).** These results do not imply
that any actual h(q) is irrational, or even that any actual h(q)
lies outside `Z[1/3]`. The set `Z[1/3]` is a countable union of the
grids in (11), and density zero is not preserved by arbitrary
countable unions of sets of integers. Weak convergence also does not
preserve mass on a dense countable set. As a direct model, set

\[
H_M=\sum_{i<M}G_i/3^{i+1}+3^{-M}.
\]

Every H_M is triadic rational, whereas `H_M -> H` almost surely and
the limit has the singular continuous law proved above. Thus the
limiting law is compatible with all actual sources converging to one.

## 6. Verification boundary and next task

`law_controls.py` reconstructs literal residue cylinders, progression
counts, geometric tail sums, and scalar enclosure transport using
integer and rational arithmetic. It uses a fixed number of actual
odd steps, not an assumption that every sampled orbit terminates.
It checks finite instances of the estimates; it does not prove weak
convergence, singularity, or the Portmanteau implication by testing.
The mathematical proofs of those assertions are the arguments above.

The next arithmetic task is still source-specific: produce a triadic
candidate at sufficiently high precision for a given source, or find
a deterministic constraint on the complete carry sequence. An
average law, even this explicitly attached actual law, cannot supply
that construction on its own.

# L-ASTRA-006 — exact first-passage fibers in ordinary endpoint coordinates

**Status:** PROPOSED pending independent review. This is an exact finite
interface, not a mixing theorem and not a proof of Collatz.

Use the shortcut map T of [PROOF.md](PROOF.md). Fix integers X>Y>=2 and a
clock cap L>=1. For Y<n<=X define

\[
t_Y(n)=\min\{j\ge1:T^j(n)\le Y\}.
\]

The partial map F(n)=T^(t_Y(n))(n) is defined only when t_Y(n)<=L. Its
unresolved source set R contains those n that do not pass by this clock;
no eventual claim is made about them.

## 1. Exact physical support

Every defined endpoint belongs to

\[
J_Y=\{\lfloor Y/2\rfloor+1,\ldots,Y\}.
\tag{1}
\]

Indeed a positive odd step increases its input, so the crossing step is even.
Its preceding state is 2y>Y, while y<=Y. This support must be built into any
mixing comparison. Uniformity on [1,Y] is already the wrong baseline for
sources starting above Y.

## 2. Each first-passage word gives one arithmetic progression in one interval

For a word w=(v_0,...,v_(j-1)) of length 1<=j<=L ending in 0, define prefix
weights q_i and affine numerators A_i by

\[
q_0=A_0=0,\quad q_{i+1}=q_i+v_i,
\quad A_{i+1}=3^{v_i}A_i+v_i2^i.
\]

Set P=2^j, Q=3^(q_j), and A=A_j. Then

\[
T^i(n)=\frac{3^{q_i}n+A_i}{2^i},
\qquad n=\frac{Py-A}{Q}.
\tag{2}
\]

Define the integer interval [ell_w,u_w] by

\[
u_w=\min\left(Y,\left\lfloor\frac{A+QX}{P}\right\rfloor\right),
\]

\[
\ell_w=\max\left(\lfloor Y/2\rfloor+1,
\max_{0\le i<j}\left\{
\left\lfloor\frac{3^{q_i}A+Q(2^iY-A_i)}{3^{q_i}P}\right\rfloor+1
\right\}\right).
\tag{3}
\]

Finally let

\[
b_w\equiv A P^{-1}\pmod Q,
\quad 0\le b_w<Q,
\tag{4}
\]

with the convention b_w=0 when Q=1. Exactly the endpoints contributed by w
are

\[
y\in[\ell_w,u_w]\cap(b_w+Q\mathbb Z).
\tag{5}
\]

The corresponding source is (Py-A)/Q. Empty intervals or progressions
contribute nothing.

### Proof and quantifier check

The upper bound in (3) is exactly n<=X. The inequality at i=0 in the lower
bound is exactly n>Y. For each proper prefix, substituting the source from
(2) shows that T^i(n)>Y is equivalent to

\[
3^{q_i}P y>3^{q_i}A+Q(2^iY-A_i),
\]

which gives the strict floor-plus-one bound in (3), including negative
numerators without changing rounding conventions. Equation (4) is exactly
ordinary integrality of the source.

To check parity legality, every binary word of length j has one source
residue class modulo 2^j. Inductively, the two lifts of a length-i source
class differ by 2^i; after i common branches their images differ by the odd
integer 3^(q_i), so precisely one lift realizes each next parity. The affine
congruence 3^(q_j)n+A_j=0 modulo 2^j also has exactly one solution because
3^(q_j) is odd. Thus it is the same class. Final integrality together with
(2) therefore certifies the entire word, not just its last step.

Every source in the original finite problem has a unique first-passage time
and word. Conversely (5) gives exactly one source with that first-passage word.
No source is counted twice by different branch records. QED.

## 3. The exact mass identity that any proposed contraction must respect

Let

\[
K_{X,Y,L}(y)=\sum_w\mathbf1_{\{y\text{ satisfies (5) for }w\}}.
\tag{6}
\]

This is the actual number of defined sources sent to y. In particular

\[
\sum_{y\in J_Y}K(y)=X-Y-\#R.
\tag{7}
\]

For any nonnegative source weight omega define

\[
K_\omega(y)=\sum_{w:\ y\text{ satisfies (5)}}
\omega((Py-A)/Q).
\tag{8}
\]

If e is the indicator of the true exceptional set, its orbit invariance gives

\[
E(X)=E(Y)+\#(R\cap\mathcal E)+\sum_{y\in J_Y}K(y)e(y).
\tag{9}
\]

For critical mass the equally exact formula is

\[
D_\gamma(X)=D_\gamma(Y)
+\sum_{n\in R\cap\mathcal E}n^{-\gamma}
+\sum_{y\in J_Y}K_{n^{-\gamma}}(y)e(y).
\tag{10}
\]

The unresolved term cannot be silently dropped. Counting minima instead of
the last term changes the population. And a nonnegative inequality that
saves a power beyond the average fiber for *every* endpoint subset contradicts
(7) by taking the complete image. The latter mass-conservation observation
was already made in PR #88; it is not claimed as new here.

For one survivor subset B, ordinary equidistribution predicts roughly

\[
\sum_{y\in B}K(y)\approx
\frac{X-Y-\#R}{|J_Y|}|B|,
\]

not a polynomial saving relative to this value. A stronger saving needs a
specific arithmetic anticorrelation with future survival. Equations (3)-(5)
say exactly which progressions and real intervals that claim must control.

## 4. Pilot: control for support before interpreting a survivor bias

The experiment uses X=2^k, Y=2^(k/2), k=8,10,...,18. For each stage cap c*k,
c=1,2,4, it counts exact first passages from (Y,X]. For each q=1,2,4, the
endpoint set B consists of y in J_Y that do not hit 1 through q*(k/2) steps.
This is a finite-horizon set, not the unknown eternal exceptional set.

The reported ratio is

\[
\operatorname{bias}=\frac{\#F^{-1}(B)}{\#\operatorname{dom}F}
\frac{|J_Y|}{|B|}.
\tag{11}
\]

An empty B receives no ratio. For c=q=4 the exact ratios at k=10,...,18 are

\[
632/743,\quad5960/5091,\quad5182/4745,\quad747904/741125,
\quad3052224/3094429.
\]

At the last scale the ratio is approximately 0.98636, not an observed
polynomial depletion. These small data do not disprove a future-survivor
estimate with another clock, another descent map, or an asymptotic bound.
They do refute treating a generic "mixing" explanation as evidence that the
needed *extra* saving has already appeared.

The compiler was independently compared against every source at (X,Y,L)
=(256,16,8) and (512,32,10), giving 99 and 233 defined sources respectively.
All six larger pilot histograms were separately replayed by a memoized
physical-hitting implementation. See [the experiment](../../experiments/X-ASTRA-001-critical-mass/README.md).

## 5. Research interface

A proposed ordinary-mass certificate can consume (8) directly. Its obligations
are to preserve first-passage history, prove the bound on R, and control the
intersection of future survivors with the exact endpoint progressions. Neither
random future parity nor independence after the native information horizon
is assumed by this compiler.

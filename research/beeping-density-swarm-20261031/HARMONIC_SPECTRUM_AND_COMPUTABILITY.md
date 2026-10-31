# Harmonic transport: exact spectrum, escape mass, and the cost of computing a Green potential

**Status: PROPOSED, with complete arguments and a separate bounded replay.
Collatz remains OPEN.** The operator here is the Jacobian-weighted inverse
operator of `INVERSE_GREEN.md`. It is not the unweighted inverse operator
used by the full-convergence rank criterion. All spectral statements specify
their Banach space; changing to a nonequivalent arithmetic norm is outside
the obstruction.

This note independently reconstructs the harmonic transport and first-hit
arguments in the current inverse track. It then gives a complete spectral
description in the harmonic space, an exact description of residual mass,
and an effective equivalence for the pointwise finite Green potential.
No priority claim is made for general weighted-shift or survival-probability
principles. The orbit reciprocal estimate is inherited and credited below.

## 1. Definitions and normalization

Let `O={1,3,5,...}` and

\[
U(x)=(3x+1)/2^{a(x)},\qquad a(x)=v_2(3x+1),
\quad b(x)=3/2^{a(x)},\quad c(x)=\frac{3x}{3x+1}.
\]

The map is unabsorbed: `U(1)=1`. Define

\[
(Lf)(t)=\sum_{Ux=t}b(x)f(x),\qquad
\mathcal H=\left\{f:O\to\mathbb C:
\|f\|_H=\sum_{x\in O}|f(x)|/x<\infty\right\}.
\]

The vectors `e_x=x 1_{x}` are a normalized basis. In this basis,

\[
L e_x=c(x)e_{U(x)}. \tag{1}
\]

Thus `f -> (f(x)/x)_x` is an isometry to ordinary `ell^1(O)`; the conjugated
operator is a deterministic substochastic transport with survival factor
`c(x)` at x. This is a mathematical killing mechanism, not the Collatz
termination event.

For a finite set `K subset O`, let `H_K` consist of functions supported on
`O\K`, and let `L_K=P_{O\K} L P_{O\K}` act on that space. A trajectory is
killed on its first entry into K. The case K empty is included.

## 2. HS-001: exact local dissipation, but no uniform power loss

For nonnegative f with finite harmonic norm, Tonelli gives

\[
\|Lf\|_H=\sum_x\frac{3f(x)}{3x+1},\qquad
\|f\|_H-\|Lf\|_H=
\sum_x\frac{f(x)}{x(3x+1)}. \tag{2}
\]

For signed or complex f, `|Lf|<=L|f|` gives the corresponding inequality.
Consequently L and every L_K are contractions, and every nonzero vector
loses norm strictly in one step. In particular neither L nor L_K has an
eigenvector of eigenvalue lambda with `|lambda|=1`.

Nevertheless, for every finite K and every q>=1,

\[
\boxed{\|L_K^q\|_{H_K\to H_K}=1.} \tag{3}
\]

**Proof.** Choose an odd b and

\[
n_0=2^{q+1}b-1,\qquad
n_j=3^j2^{q+1-j}b-1\quad(0\le j\le q).
\]

For j<q, `n_j=-1 mod4`, so each valuation is exactly one and
`U(n_j)=n_{j+1}`. All n_j are distinct, increase, and lie outside K once
n_0 exceeds its maximum. Equation (1) gives

\[
\|L_K^q e_{n_0}\|_H=\prod_{j<q}c(n_j)
=\frac{n_0}{n_0+1-(2/3)^q}\longrightarrow1
\quad(b\to\infty).
\]

The upper bound one follows from (2). This proves (3). Notice that every
member of this test family is an ordinary positive integer, and each test
uses only a finite legal segment.

## 3. HS-002: the complete spectrum and essential spectrum

Work over the complex field. For every finite K,

\[
\boxed{\sigma(L_K)=\sigma_{\mathrm{ess,Fredholm}}(L_K)
=\{\lambda\in\mathbb C:|\lambda|\le1\}.} \tag{4}
\]

Every `|lambda|<1` has an infinite-dimensional eigenspace. Every point of
the unit circle is an approximate eigenvalue, but is not an eigenvalue.
Here the Fredholm essential spectrum is the set of lambda for which
`L_K-lambda I` is not Fredholm.

### Rapidly growing genuine inverse rays

If y is a positive odd unit modulo three, its legal predecessors have
`x=(2^a y-1)/3`, where a lies in one parity class. Increasing a by two
cycles x through the three residues modulo three, because four has order
three modulo nine. Hence two of three successive choices are units.
Increasing a further by six preserves the residue modulo three and makes
x arbitrarily large. In particular one can choose a unit predecessor x>2y.

There are infinitely many unit predecessors of 1 of the form

\[
u_{r,0}=(2^{4+6r}-1)/3,
\]

all exceeding max K after finitely many are omitted. From each, recursively
choose unit predecessors `u_{r,j+1}>2u_{r,j}`. Thus
`U(u_{r,j+1})=u_{r,j}` and `U(u_{r,0})=1`.
All ray nodes are outside K.

Different rays are disjoint. Each u_{r,j} has first hitting time j+1 to 1;
equality across two rays would first force the same j and then the same
first predecessor of 1. Define

\[
C_{r,j}=\prod_{i=0}^{j}c(u_{r,i}).
\]

These products are bounded below by a positive constant depending on the
ray, since

\[
-\log C_{r,j}
=\sum_{i=0}^j\log(1+1/(3u_{r,i}))
\le\frac13\sum_{i\ge0}\frac1{u_{r,i}}
\le\frac2{3u_{r,0}}.
\tag{5}
\]

### Interior eigenvectors and infinite multiplicity

Fix `|lambda|<1` and two distinct rays r,s. The series

\[
v_{r,s}(\lambda)=
\sum_{j\ge0}\frac{\lambda^j}{C_{r,j}}e_{u_{r,j}}
-\sum_{j\ge0}\frac{\lambda^j}{C_{s,j}}e_{u_{s,j}}
\tag{6}
\]

converges absolutely in H_K by (5). Its incoming flux at 1 cancels: the
two initial coefficients give +1 and -1 after multiplication by c. If 1
belongs to K, those contributions are individually killed instead.
At every other ray node the recurrence in (1) gives

\[
L_K v_{r,s}(\lambda)=\lambda v_{r,s}(\lambda).
\]

Hold s fixed and vary r. These eigenvectors are linearly independent,
as each new ray has a coordinate absent from the others. Thus the kernel
of `L_K-lambda I` is infinite-dimensional for every interior lambda.
It is consequently not Fredholm there. The Fredholm set is open, so its
complement is closed and contains the closed unit disk. Conversely
`||L_K||<=1` puts the spectrum inside that disk. This proves (4).

### Explicit approximate eigenvectors on the circle

For `|lambda|=1`, use an all-one segment of length ell as in Section 2,
far above K, and put

\[
v=\frac1\ell\sum_{j=0}^{\ell-1}\lambda^{-j}e_{n_j}.
\]

The support is distinct and `||v||_H=1`. Only the two endpoints and the
small defects `1-c(n_j)` remain after subtraction, giving

\[
\|(L_K-\lambda I)v\|_H
\le\frac2\ell+\frac1{3n_0+1}. \tag{7}
\]

Let ell and n_0 grow. Equation (2) already excludes a genuine eigenvector
on this circle.

### Consequences and their exact scope

Compact perturbations preserve the Fredholm essential spectrum; this is
the standard Fredholm/Atkinson fact. Thus adding any compact operator to
L_K cannot reduce its spectral radius below one. The essential norm of
every power is also exactly one: its essential spectral radius is one,
and its ordinary norm is at most one. Changing to an equivalent
norm also preserves the spectrum, so cannot give a fixed-block norm
contraction. Removing any finite terminal set is already covered directly.

These conclusions do **not** exclude a useful nonequivalent arithmetic
space, nonuniform source-specific estimates, a different clock or induced
operator, or a correct unweighted descent argument. Finite-dimensional
truncations have no authority to infer an infinite-dimensional gap: their
terminal-boundary loss can erase the infinite inverse rays used in (6).

No argument here assumes that compact operators send normalized basis
vectors to zero; that would be invalid in ell^1. Infinite kernel and
Fredholm stability give the essential-spectrum assertion directly.

## 4. Inherited reciprocal control, independently reconstructed

The next sections use the explicit theorem T-A3-651 at
`research/astra-three-routes/pass3/FINITE_RECORDS.md`, present at PR142 head
`d0f48c472d45a336e9083b37b45e1a8d39a2cf16`:

> If a finite simple shortcut path stays above m>=1, the reciprocal sum of
> its distinct odd states is at most `200 m^(-1/40)`.

This is an inherited result, not a discovery of this pass. Its needed
argument is reconstructed here. List the odd states in time order and put
`q=floor((3/5)log_2 X)`, `a_0=floor(5q/3)`. Discard the last q odd states,
so every retained source has q successors within the same simple path and
those endpoints are distinct. A valuation word of total A specifies one
odd residue modulo `2^(A+1)`. For `A<=a_0`, its number of sources below X
is at most `(3/2)X 2^(-A)`, because `2^A<=X`.

The geometric composition generating function at z=4/5 gives a total
low-A probability at most `rho^q`, where `rho^3=3125/3456`. In the high-A
case the affine image lies below
`sigma^q X+(3/2)^q-1`, where `sigma^3=27/32<rho^3`.
The distinct odd endpoints therefore contribute at most
`[sigma^q X+(3/2)^q]/2`. Including the terminal q states yields

\[
N(X)\le2X\rho^q+\tfrac12(3/2)^q+q\le5X^{39/40}.
\tag{8}
\]

For q>=1, the exact inequality `8*3125^24<3456^24` gives
`rho<2^(-1/24)`, while `rho>2/3`. Hence the three displayed terms are
bounded by `3X^(39/40)`, `(1/2)X^(39/40)`, and `(6/5)X^(39/40)`.
The last uses `log_2 X<2 sqrt X`. The q=0 and fewer-than-q-odd-states cases
are covered by the trivial count. Integrating
`1/x=integral_x^infinity y^(-2)dy` and using the floor m gives

\[
\sum_{x\text{ odd on the simple path}}\frac1x
\le\int_m^\infty5y^{39/40}y^{-2}\,dy
=200m^{-1/40}. \tag{9}
\]

Every simple odd-to-odd segment expands to a simple shortcut segment:
a repeated intermediate even state would force the same subsequent odd
state. Its odd minimum is also a lower bound on the intermediate halving
states. Thus (9) applies to the odd paths used below. Repeated cycles are
never counted with multiplicity in this argument.

## 5. HS-003: exact escape mass and a dual boundary description

For x outside K let `x_j=U^j(x)`. The remaining harmonic mass from e_x is

\[
s_{K,q}(x)=\|L_K^q e_x\|_H
=\mathbf1_{x_0,\ldots,x_q\notin K}
\prod_{j=0}^{q-1}c(x_j).
\tag{10}
\]

It decreases with q, so write `s_K(x)=lim_q s_{K,q}(x)`.

If the orbit hits K or is eventually periodic, s_K(x)=0. In the latter
case every lap of a finite cycle multiplies the mass by a factor strictly
less than one. If the orbit stays outside K and is not eventually periodic,
all states are distinct and tend to infinity. Let m be its attained
minimum. Applying (9) to every finite prefix and taking a monotone limit,

\[
\boxed{1\ge s_K(x)\ge
\exp\!\left(-\frac{200}{3}m^{-1/40}\right)>0.}
\tag{11}
\]

The same bound on later tails shows `s_K(U^j x)->1` along every such
escaping orbit. This uniform finite-path estimate provides the substantive
arithmetic input; strict one-step loss alone would not imply (11).

For any nonnegative f in H_K, Tonelli and dominated convergence now give

\[
\boxed{\lim_{q\to\infty}\|L_K^qf\|_H
=\sum_{x\notin K}\frac{f(x)}x s_K(x).} \tag{12}
\]

Consequently the following are equivalent:

1. `L_K^q f ->0` in harmonic norm for every f in H_K.
2. Every positive ordinary Collatz orbit is eventually periodic.

For 2=>1, use (10) and dominated convergence, then positivity for signed
f. Conversely, any escaping orbit has a tail avoiding a fixed finite K;
(11) supplies a normalized basis vector whose norm does not vanish.
This is **not** equivalent to the full Collatz conclusion unless all
additional positive cycles are independently excluded.

There is also an exact positive functional invariant under actual transport:

\[
E_K(f)=\sum_{x\notin K}\frac{f(x)}x s_K(x),\qquad
E_K(L_K f)=E_K(f). \tag{13}
\]

The equality follows from `s_K(x)=c(x)s_K(Ux)` away from a killed edge,
with zero on that edge. It identifies all residual mass as escape mass.

For completeness, the fixed functions of the dual have a simple full
description. Use the normalized ell^1 coordinates from Section 1, so the
dual is ell^infinity and `L_K^*h(x)=c(x)h(Ux)` on retained edges. Let
`mathscr E_K` denote the set of forward-coalescence classes of escaping
orbits that avoid K.
Every bounded fixed dual function has the form

\[
h(x)=s_K(x)\alpha([x])
\quad\text{on escaping retained states},\qquad h(x)=0\text{ otherwise},
\tag{14}
\]

for an arbitrary bounded function alpha on those classes. Indeed, fixedness
makes `h(x)/s_K(x)` constant along each retained escaping orbit; coalescence
then identifies it throughout its class. On periodic or killed paths,
iteration forces zero. Since `s_K(U^j x)->1`, the map alpha to h is an
isometry. Thus the bounded invariant dual boundary is exactly the set of
escaping components. Its emptiness remains an unproved mathematical fact.

The weighted product and divergent-component distinction also occur in
Valbuena's newly located canonical-trace manuscript. We do not claim those
ingredients as new. The present statement concerns this explicit harmonic
Banach space and does not import any of that manuscript's density or
formalization claims.

## 6. HS-004: effective evaluation of the critical Green potential is a reachability problem

Return to the unabsorbed operator L and put

\[
V(t)=\sum_{q\ge0}L^q g(t),\qquad g(x)=1/x.
\tag{15}
\]

The first-hit/renewal argument in `INVERSE_GREEN.md` proves

\[
0<V(t)\le t(3t+1)\sum_{x\in O}x^{-2}<\infty,
\qquad LV=V-g. \tag{16}
\]

The function V is uniformly lower semicomputable: enumerate finite source
and clock rectangles in its nonnegative rational path sum. Finiteness with
a computable upper bound does not by itself supply a computable error
bound in the clock variable.

### A uniform positive gap for a previously unseen first hit

If x first reaches t at clock q, its path is simple. Its weight satisfies

\[
w_q(x)=\frac tx\prod_{j<q}c(U^j x)
\ge e^{-200/3}\frac tx>2^{-100}\frac tx. \tag{17}
\]

The last strict inequality is elementary: the expansion
`log 2=2 sum_{j>=0} 1/[(2j+1)3^(2j+1)]` gives
`log2>56/81>2/3`, and hence `100 log2>200/3`.
Its first-hit contribution to V(t) is therefore at least

\[
\delta_{x,t}=2^{-100}t/x^2. \tag{18}
\]

### Computability equivalence

For each fixed positive odd t, the following are equivalent:

1. V(t) is a computable real number.
2. The actual predecessor set `P(t)={x in O: U^q x=t for some q>=0}`
   is a decidable set.

The equivalence is uniform: uniform real computability of t to V(t) is
equivalent to a uniform algorithm deciding the reachability relation (x,t).

**Proof of 1=>2.** Let

\[
A_N(t)=\sum_{\substack{x\le N\\x\text{ odd}}}
\sum_{\substack{0\le q\le N\\U^qx=t}}w_q(x)/x.
\]

These are computable rationals increasing to V(t). A real-computation
algorithm for V(t) supplies rational upper bounds B_N(t) with
`B_N(t)-V(t)<=2^(-N)`. At stage N, compute A_N(t) and check the queried
source x through the **same forward clock N**, reusing its previously
computed prefix if desired. If any of those N+1 states equals t, answer
yes before applying the rejection test. Thus a lagging separate simulation
cannot overlook a hit already included in A_N(t). Otherwise wait for N>=x
with

\[
B_N(t)-A_N(t)<\delta_{x,t}.
\]

This eventually happens if no hit has been detected, because the left side
tends to zero. A later first hit would contribute at least delta_{x,t} by
(18), contradicting the remaining tail bound. Hence answer no. A true
future hit prevents premature rejection by the same inequality.

**Proof of 2=>1.** Query whether U(t) belongs to P(t). If it does, iterate
until the first return to determine the least period p and its rational
multiplier eta; set kappa=`1/(1-eta)`. If it does not, set kappa=1.
Thus `kappa<=3t+1` is obtained without an undecided periodicity branch.

For each odd source x<=B, use the membership decider. If the answer is yes,
simulate to its first hit and compute w exactly; otherwise its contribution
is zero. Cycle renewal gives the exact truncated sum

\[
S_B(t)=\kappa\sum_{\substack{x\le B,\ x\text{ odd}\\x\in P(t)}}
w_{\tau_t(x)}(x)/x.
\]

The remaining error satisfies

\[
0\le V(t)-S_B(t)
\le\kappa t\sum_{x>B}x^{-2}
\le\frac{t(3t+1)}B. \tag{19}
\]

Choose B from the required precision. Every loop then terminates, proving
computability. The procedures are uniform in the supplied target and
membership oracle.

No noncomputability theorem is asserted. If every positive orbit eventually
repeats, reachability is decidable by literal simulation until repetition,
so V is uniformly computable. In particular full Collatz would imply this.
The implication does not run from a mere pointwise finite formula (15) to
an executable total evaluation algorithm. The strict potential (16) remains
a mathematical object whose effective evaluation has exactly the stated
reachability content.

## 7. Independent audit of the inverse track

The following current claims were reconstructed from their definitions:

* **IFT-001:** equations (2) and Tonelli prove the transport identity and
  the local Green bound `Gf(t)<=t(3t+1)H(f)` on its stated input domain.
  The reference input one is outside that harmonic domain and cannot be
  substituted into the bound.
* **IFT-002:** first-hit paths are simple; two different first-hit depths
  cannot have the same source. Periodic targets require the exact renewal
  factor, including the empty first hit at t. The distinction between
  nonperiodic and nonpreperiodic is correctly retained.
* **IFT-003:** for q<=Q and A<=6Q, all weights are at most
  `(3/2)^Q` and at most t/x, and all sources are below `t2^(6Q)`.
  Decreasing-function integral comparison gives `t(1+Q log96)`.
  The discarded tail is bounded by `(2/3)^(6Q) sum_{q=1}^Q9^q`, hence
  `(9/8)(64/81)^Q`. Summation by parts preserves the special Q=0 term
  and gives the displayed real Abel bound, with no meromorphic claim.
* **IFT-004:** root-outward prefix-free words have unique decompositions
  after arbitrary legal inverse extension. The map from prefix/extension
  pairs into complete histories is injective, including Q=0, so the
  transported depth-average bound is valid. It is an averaged-depth
  estimate, not a prescribed-depth estimate.
* **IFT-005:** the source-charge Green potential is pointwise finite by
  first-hit injection and renewal. Nonnegative Tonelli proves its strict
  supersolution identity. Finite-tree induction followed by monotone
  convergence gives the budget for arbitrary prefix-free stopping lines.
  Its computability caveat is sharpened by HS-004 above.
* **IFT-006:** the lower-bound deduction is valid provided its advertised
  external fast-predecessor theorem has exactly the stated positive-density
  and clock scope. The all-input distortion step is reconstructed in
  Section 4. The external analytic theorem and Lean development were not
  independently rebuilt. Fatou supplies only a superharmonic subsequential
  profile, not harmonic equality without inverse-tail control.

The independent review finds no surviving defect within these scopes. It
does not upgrade the external premises or the unresolved full-convergence
obligations.

## 8. What was attempted and what remains missing

The original concentration attack investigated whether PR140's positive
collision exponent forces repetitions long enough to violate its fixed-source
height bound. That inference was not obtained. The occupation limit takes
the time horizon to infinity at each fixed precision; late return sources
may be exponentially large. Low entropy alone supplies no repetition whose
precision beats that actual source height. Computability of a single orbit
also gives no useful bound on its empirical block entropy; computable normal
sequences already prevent that generic inference.

The strongest surviving output of this track is therefore the precise
operator and computability analysis above, not a new concentration theorem.
An argument proving actual dissipation must show `s_K=0`, or use a genuinely
different space or arithmetic mechanism. A proof that V is uniformly
computable must supply the reachability information identified in HS-004.
Neither property is established here, and additional positive cycles remain
a separate obstruction even if strong stability is proved.

The companion verifier checks exact finite transport, legal inverse rays,
truncated eigenvector residuals, circle-approximation residuals, first-hit
distortion identities, and retained periodic examples. It cannot test an
infinite spectrum or decide the open escape problem; those statements rest
on the written arguments.

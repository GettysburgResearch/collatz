# Independent review: dyadic regularity, softened stopping time, and approximate invariants

**Review status:** the mathematical implications below are verified by
independent reconstruction, subject to the explicitly external density
hypotheses. The required regularity/concentration statement remains **OPEN**.
This review does not independently verify Mazur's positive-density theorem
or any Lean development. It neither proves Collatz nor upgrades that source.

Scope: the density agent's communicated theorem and formulas, and the root
agent's communicated majority-parity obstruction, reviewed on 2026-10-30.
The all-parameter arguments are given below so the scope does not depend on
an evolving draft. The independent finite script is
`check_regularity_review.py`; its output is `regularity_review_checks.json`.

## 1. Norm completion and pullback: verified

For bounded sequences on the positive integers define

\[
\|f\|_C=\limsup_{X\to\infty}\frac1X\sum_{1\le n\le X}|f(n)|,
\quad
\|f\|_L=\limsup_{X\to\infty}\frac1{\log X}\sum_{1\le n\le X}\frac{|f(n)|}{n}.
\]

Let D_C and D_L be the respective seminorm closures of bounded functions
periodic modulo a power of two. Both norms of a dyadic-periodic function
equal its Haar L1 norm on Z₂. Quotienting out seminorm-zero functions and
completing therefore identifies either dyadic closure isometrically with
L1(Z₂). This is an identification of **norm classes**. It is not a
pointwise identification of arbitrary sequence values with a Haar function
at the countable dense subset of positive integers.

For the shortcut map T, composition is bounded on either ambient seminorm:

\[
\|f\circ T\|_C\le2\|f\|_C,
\qquad
\|f\circ T\|_L\le2\|f\|_L.
\]

For the ordinary norm, even inputs contribute the sum up to X/2, hence
at most one half the original limsup. Odd inputs map injectively to
m≡2 (mod 3) below (3X+1)/2, hence at most three halves the original
limsup. Adding gives two. Floors and the final O(1) terms disappear.

For the logarithmic norm, even inputs have weight 1/(2m). Odd inputs have
weight 3/(2m−1), and

\[
\frac3{2m-1}=\frac3{2m}+O(m^{-2}).
\]

The O(m⁻²) contribution is bounded for each bounded f and disappears
after division by log X. The two surviving coefficients are again 1/2
and 3/2. No uniform bound across all approximants is needed for this
fixed-function estimate.

If p has period 2ᵏ, p∘T has period 2ᵏ⁺¹. Its arithmetic norm agrees
with its Haar norm, and T preserves Haar measure. Thus pullback acts
isometrically on the dyadic subspace and its completion. The ambient
factor-two inequality justifies passage from actual sequence approximants
to this completed action; it is not silently replaced by an isometry on
all bounded sequences.

## 2. Liouville conclusion: verified, with an important interpretation

Every K-bit shortcut parity vector labels exactly one residue class modulo
2ᴷ. Under Haar measure these parity coordinates are independent fair bits,
and T shifts the vector. This conjugates T to the one-sided Bernoulli
shift; an invariant measurable function is tail measurable and therefore
constant almost everywhere.

Consequently, for *=C or L,

\[
f\in D_*,\qquad\|f\circ T-f\|_*=0
\quad\Longrightarrow\quad
\exists c:\|f-c\|_*=0.
\]

All limits have the right order: first fix an approximant, take the
arithmetic limsup defining its norm, and then let the approximation error
go to zero. A growing modulus depending on the summation cutoff X is
not substituted for this sequence of limits.

**Interpretive correction.** For an f already known to have zero defect,
membership in D_* is equivalent to convergence in that norm to a constant:
the reverse direction holds because constants are dyadic-periodic.
Thus the proposed regularity hypothesis is a genuine concentration
obligation. It is not a weak automatic consequence of computability, a
finite algorithm for each input, or finite lookup tables.

## 3. Rational-valued softened stopping observable: verified with wording fix

Write τ(n) for the first shortcut hitting time of one, allowing infinity,
and b(n) for the positive bit length. Set

\[
R(n)=\frac{b(n)}{b(n)+\tau(n)}\quad(\tau(n)<\infty),
\qquad R(n)=0\quad(\tau(n)=\infty).
\]

This function is rational-valued, and it is **uniformly computable as a
real-valued function**. On input n and integer M≥1, simulate at most M b(n)
steps. If one is reached, output the exact rational above; otherwise output
zero. The approximation error is at most 1/(M+1), uniformly in n.

This does not provide an algorithm that always terminates with an exact
rational encoding of R(n). In a still-unresolved case, bounded simulation
cannot distinguish zero from a sufficiently small positive rational. An
exact-output claim needs an additional argument. The review makes no
impossibility claim about such an algorithm for this particular map.

For n>1 with finite τ=t, one has τ(Tn)=t−1 and
b(Tn)∈{b−1,b,b+1}. Writing b′=b(Tn),

\[
R(Tn)-R(n)=\frac{(b'-b)t+b}{(b+t)(b'+t-1)}.
\]

The numerator in absolute value is at most b+t and the second denominator
factor is at least b+t−2≥b−1. Hence

\[
|R(Tn)-R(n)|\le\frac1{b(n)-1}\quad(n>1).
\]

If τ=∞ both values vanish. Thus R has zero ordinary and logarithmic
defect. The isolated n=1 value is irrelevant to either norm.

For the exponential version F(n)=exp(−τ(n)/log n), defined separately
at one, the corresponding estimate communicated by the density agent
also checks:

\[
|F(Tn)-F(n)|\le
\frac{1+(\log2)/e}{\log n-\log2},\qquad n\ge4.
\]

Changing τ by one costs at most 1/L, and changing the positive denominator
L=log n costs at most |ΔL|/(e\min L), since the derivative of exp(−t/L)
with respect to L is at most 1/(eL). Here |ΔL|≤log2.

**Non-automatic regularity.** The finite cutoff for R inspects as many as
M b(n) parity bits, with a growing modulus 2^{M b(n)}. It does not give
one fixed dyadic period that approximates R throughout the asymptotic
ordinary or logarithmic average. This is the precise missing limit swap.

## 4. Density-to-universality bridge: verified conditionally

Assume the following two external inputs, keeping them separate:

1. There is a set of positive lower natural density on which
   τ(n)≤A log n for one finite constant A.
2. If a nonconvergent positive input exists, the set of nonconvergent
   inputs has positive lower natural density. It suffices to establish
   this through a positive-density predecessor basin of a unit target
   on a bad orbit.

Positive lower natural density implies positive lower logarithmic density
by partial summation. On the fast set,

\[
F(n)\ge e^{-A},\qquad
R(n)\ge\frac1{1+A\log2},
\]

because b(n)≥log n/log2. If either observable belongs to D_L, Section 2
makes it equal in logarithmic norm to a constant c. On a positive-density
set bounded below by a>0, norm convergence forces c≥a: if c<a, the
positive lower density gives a positive lower bound for the norm error.
There is no missing density multiplier in this conclusion.

If a bad input exists, the observable is zero on the whole bad set.
Assumption 2 then forces c=0, a contradiction. The same proof works with
D_C and the ordinary norm.

A bad input divisible by three eventually reaches an odd multiple of three
after finitely many even steps; the next shortcut step is 2 modulo three.
So a bad orbit does contain a target coprime to three. Every predecessor of
that target is bad. This verifies the unit-target reduction if the external
positive-density predecessor theorem actually has the advertised domain.

**Essential restriction:** a lower bound of the form cX^γ with γ<1 for a
bad basin does not suffice here. Such a basin may have zero logarithmic
density. An o(1) normalized norm error cannot contradict this weaker
polynomial-size lower bound without an additional quantitative rate.
The newer linear/positive-density theorem, rather than the older 0.90x
exponent, is doing real work in this bridge.

No step above establishes D_L membership or the resulting concentration.
Nor does this review certify the external density proof. Those remain
separate dependencies, not consequences of the Liouville argument.

## 5. Majority-parity obstruction: verified with anchor conditions

Let K=2m+1 and f_K be the indicator that a strict majority of the first
K shortcut parity bits are one. This is periodic modulo 2ᴷ and has mean
1/2. The shifted majority differs precisely when the middle 2m bits contain
exactly m ones and the two endpoint bits differ. Hence in Haar, ordinary,
and logarithmic L1 norms,

\[
\|f_K\circ T-f_K\|_1
=\frac{\binom{2m}{m}}{2^{2m+1}}
\longrightarrow0.
\]

At the same time its L1 distance from every constant is at least 1/2.
There is therefore no universal Poincaré inequality bounding distance to
constants by a fixed multiple of this defect.

For a finite anchor set S, choose K large enough that its elements are
distinct modulo 2ᴷ. Prescribe anchor values a_s∈[0,1], and change f_K on
the corresponding residue classes to obtain g_K. Then

\[
\|g_K-f_K\|_1\le\frac{|S|}{2^K},
\quad
|\operatorname{mean}(g_K)-\tfrac12|\le\frac{|S|}{2^K},
\]

and, by Haar-preserving pullback on periodic functions,

\[
\left|\|g_K-g_K\circ T\|_1-
\|f_K-f_K\circ T\|_1\right|
\le\frac{2|S|}{2^K}.
\]

The conditions on range and separated anchor residues are necessary for
these stated constants and for the patch to be well defined. Arbitrary
bounded anchor values give the same result with their maximum change
included in the constants. Fixed finite S is separated for all sufficiently
large K.

This blocks a quantitative argument based only on a small defect plus
finitely many certified input values, even when all candidates are themselves
dyadic-periodic. It does not refute the qualitative Liouville theorem:
the majority sequence does not converge in L1 to an invariant function.
A true approximation sequence for R would also need the Cauchy/convergence
property, which is absent from these examples.

## 6. An explicit warning against inferring regularity from computability

Define, for n≥3,

\[
h(n)=\tfrac12\big(1+\sin(\log\log n)\big),
\]

and assign any bounded values at one and two. This is a bounded uniformly
computable sequence, and

\[
|h(Tn)-h(n)|=O(1/\log n).
\]

Nevertheless it is in neither D_C nor D_L. Its ordinary average is
h(X)+o(1): on n∈[ηX,X] the function varies by o(1) for each fixed η>0,
while the omitted interval has relative size at most η. The average
therefore oscillates and cannot converge to a constant.

Partial summation, or replacing the weighted sum by its integral, gives

\[
\frac1{\log X}\sum_{n\le X}\frac{h(n)}n
=\frac12+
\frac{\sin(\log\log X)-\cos(\log\log X)}4+o(1).
\]

This also oscillates. Any norm convergence to a constant would force the
corresponding averages to converge, so Section 2 excludes dyadic regularity.
The example has the same type of vanishing pointwise defect as R, showing
directly that computability and asymptotic invariance alone leave the decisive
hypothesis unproved.

## 7. Further review of the written density packet

After the initial reconstruction, the complete
`REGULARITY_BRIDGE.md` was read, including DREG-007 and its
fiber-variance characterization. The following additional statements check.

**Indicator equivalence and pointwise Liouville.** Under the advertised
positive-density predecessor theorem, the convergence indicator belongs to
either dyadic completion exactly when Collatz holds. The positive density
of the good basin needed here follows already by taking the target a=1;
the separate fast-convergence theorem is not required for this indicator
version. For a general bounded exactly invariant f, if f(n) differs from
the seminorm constant c, its value propagates forward to a unit target and
backward throughout that target's predecessor basin. Positive lower density
then contradicts zero seminorm error. Exact shortcut invariance implies
ordinary invariance because f(2m)=f(m) and C(n)=2T(n) at odd n. Thus the
pointwise Liouville strengthening is correctly conditional on the external
positive-density theorem.

**Fiber variance.** Suppose conditional first and second moments exist in
every fixed dyadic residue class. Their mean within-class variance V_r is
the limiting squared error of the periodic function of class means, and
it is the minimum squared error at that period. These minima decrease
when the period is refined. Therefore V_r→0 is equivalent to dyadic L2
approximability; for bounded f, clipping approximants to its range and
Cauchy–Schwarz make this equivalent to the stated L1 approximability.

The converse existence assertion is also correct: dyadic L1 approximation
implies all these conditional moments exist. Fix r first. The conditional
mean approximation error in one class is bounded by 2^r times the global
limsup error. For second moments use |f²−g²|≤2B|f−g| after clipping to
[-B,B]. The factor 2^r is harmless because r is fixed before the global
error tends to zero. Approximating periodic functions have actual limiting
conditional moments, so a Cauchy argument gives the limits for f.

For an indicator, p(1−p) lies between one half and one times min(p,1−p),
giving exactly the packet's comparison of impurity with optimal periodic
binary-classification error. These are limiting identities; increasing a
sample-dependent period can fit finite data and has no bearing on the
required order of limits.

## 8. Independent finite checks and disposition

The independent script enumerated all parity residues for
K=1,3,5,7,9,11,13; verified each exact majority mean/defect; checked the
anchor perturbation inequalities for four rational anchors; and checked
the rational-clock recurrence, defect, and cutoff estimates for n=2,…,5000
with cutoff multipliers 1,2,4,8. It passed. These are bounded regressions;
the universal statements are justified by the proofs in this review.

**Disposition:** retain the dyadic bridge as a clearly labeled conditional
route, the rational-valued computable-real observable as an unconditional
construction, and the majority family as an exact obstruction to universal
quantitative coercivity. Do not describe any of them as having established
the missing regularity or the source's external density theorem. Prefer
“normalized stopping-time concentration” when explaining what the new
regularity condition would actually require.

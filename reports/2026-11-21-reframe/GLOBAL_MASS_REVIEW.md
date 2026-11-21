# Independent review of the global mass lane

## Reviewed artifacts and verdict

Reviewer: the discrete-closure research lane, independent of the author of
the mass lane. Review date: 2026-11-21.

| Artifact | SHA-256 reviewed |
| --- | --- |
| `research/reframe-20261121/GLOBAL_MASS.md` | `212999316311aa1e6b79b764b4686828fc36b5e49e6c211f5cc6931791fb1472` |
| `research/reframe-20261121/global_mass_green_certificate.py` | `4ba23fd51bc07a4f7bc54957046f4499aa9386b8cef203f3f64f1af4f539ea50` |

**Verdict:** no mathematical gap found in the new GM1, GM2, GM3, column
normalization, or Green-weight norm arguments under the definitions and
explicit scope in the note. The rational replay completed successfully. These
are reviewed paper arguments and an exact finite-source replay, not Lean
formalizations and not a proof of Collatz.

The inherited existence and positivity of a nonperiodic component's original
eigenvector relies on the earlier reciprocal-budget interface identified in
the note. This review did not re-prove that earlier interface or re-audit
every cited source packet. GM1's operator obstruction and GM2/GM3's ordinary
inequalities do not require the existence of a nonperiodic component.

One terminology correction was requested and incorporated: the Green-weighted operator is a
norm-one contraction with strict norm decrease on each nonzero vector. The
phrase “strict contraction” can incorrectly suggest operator norm strictly
less than one. The exact norm-loss identity is valid; a uniform contraction
margin is not claimed by that identity.

## 1. Exact hyponormality criterion

For the weighted composition operator

\[
(Wf)(n)=\lambda_n f(U(n)),\qquad
D_\rho(t)=\sum_{U(n)=t}\lambda_n^2,
\]

the identities in the note have the correct orientation:
`W*W` is diagonal with entries `D_rho(n)`, while `WW*` restricts to the
rank-one matrix `lambda_n lambda_m` on each inverse fiber. Positivity of
`W*W−WW*` is therefore equivalent to

\[
\sum_{U(n)=t}\lambda_n^2/D_\rho(n)\le1.
\]

The finite-support necessity test is valid even for infinite fibers: on a
finite subset, set `f(n)=lambda_n/D_rho(n)`. Its quadratic form is `S−S²`.
Any infinite sum greater than one has a finite partial sum greater than one.
The Cauchy–Schwarz sufficiency direction has the same denominator and sign.

For the stated continuous positive weight class, the incoming sums are
uniformly bounded above and below, so the bounded-operator and denominator
conditions needed for this test hold.

## 2. GM1: continuous ternary weights

### Branch measure and the exact averaged factor

The inverse branch is

\[
F_a(\zeta)=(2^a\zeta-1)/3.
\]

Its domain inside the ternary units is exactly
`2^a ζ mod 9 ∈ {4,7}`. This guard enforces both integrality and a unit child.
The forward branch `u ↦ 2^(−a)(3u+1)` maps all ternary units bijectively onto
that domain. Multiplication by three scales additive Haar measure by `1/3`;
the unit normalization does not change that ratio because domain and image
are both measured with the same restricted Haar measure. Consequently each
branch contributes

\[
\frac13(3/2^a)^\alpha\int\phi\,d\mu,
\]

and summing gives precisely
`Lambda_alpha = 3^(alpha−1)/(2^alpha−1)`. There is no hidden equidistribution
assumption about ordinary orbit populations in this calculation.

### Ordinary-to-ternary passage

For `rho(n)=n^s V(n)` and `alpha=2−s`, the exact ordinary edge factor is

\[
\lambda_n^2=(3/2^a)^\alpha
 (1-1/(2^at))^s V(n)/V(t).
\]

The correction factor tends to one along ordinary targets tending to
infinity. It is uniformly bounded above and below on all legal edges.
Positivity and continuity of `V` on the compact unit space give uniform
bounds for the remaining ratio. Every target has two legal exponent classes
represented among `1,…,6`, furnishing a uniform positive lower bound for
`D_rho` as well.

Every ternary unit has positive odd ordinary approximants tending to it
ternarily and to infinity in ordinary size. For a fixed allowed exponent,
its children likewise tend to the corresponding ternary child and to
infinity in ordinary size. Uniform geometric tails therefore justify both
limits in G7, including the denominator `D_rho(n)` in the second limit.
This is enough to transfer an eventual ordinary hyponormality inequality
to the compact pointwise inequality in the note.

### Equality and the negative fixed point

Writing `D=P_alpha V/V`, the integrated inequality yields an upper bound on
`integral(V/D)` equal to its weighted Cauchy–Schwarz lower bound, because
`integral(VD)=Lambda_alpha integral(V)`. Equality forces `D` constant almost
everywhere under the positive weight `V dmu`. Continuity and full support
then force it constant everywhere, with value `Lambda_alpha`.

At `ζ=−1`, the legal branch `a=1` fixes `−1`. Its contribution alone requires

\[
\Lambda_\alpha\ge(3/2)^\alpha,
\]

contradicting the displayed ratio `3(1−2^(−alpha))>1` for `alpha>1`.
This use of a negative ternary point is sound: it contradicts a continuous
equation forced by arbitrarily large positive ordinary approximants. It
does not identify a negative orbit with a positive counterexample.

**Accepted scope of GM1:** failure of the exact hyponormality inequality at
arbitrarily large ordinary positive targets for every stated positive
continuous ternary factor and every `s<1`. This does not rule out arbitrary
height-dependent or discontinuous weights, different operators, or
non-diagonal inner products.

## 3. Normalization and Green weights

### Column normalization

The normalized operator in G9 has incoming squared column sums exactly one,
so it is an isometry. The two uniformly positive short inverse branches
ensure every normalized edge probability is at most `1−delta`. The
coordinate bound on its powers then proves the intersection of all ranges
is zero. The purity conclusion is justified.

The integrability explanation is also correct. On a nonperiodic component,
distinct inverse levels of a fixed target are disjoint; otherwise that target
would lie on a cycle. A nonzero formal unit-circle eigenvector of the
normalized operator places the same positive squared mass on every such
level. It cannot be square summable. The formal gauge changes the function
space membership rather than eliminating the ordinary component.

### Fixed-target Green estimates

For a first hit from `n` to `t`, the derivative product is at most `t/n`.
A periodic target's return multiplier is at most `3t/(3t+1)` because the
cycle product contains that factor and all its other factors are below one.
The sum over first hits and subsequent cycle returns therefore gives G10
for every `alpha>1`. It does not assume all sources converge to one.

The per-source telescoping estimate G11 has the correct exponent and
constant. The concavity inequality applies to
`g(u)=1−(1+u)^(−alpha)`, with `g(0)=0`, giving
`t g(1/(3t)) >= g(1/3)` for `t>=1`. Equality at the fixed source one verifies
the sharp constant in that stated bound.

Tonelli then gives `P_alpha G_alpha=G_alpha−1`. At square pressure,

\[
\|Af\|_{\ell^2(G_2)}^2
=\|f\|_{\ell^2(G_2)}^2-\|f\|_{\ell^2}^2,
\qquad
\|f\|_{\ell^2(G_2)}^2=\sum_{q\ge0}\|A^qf\|_2^2.
\]

Both identities are correct. Finite-support vectors consequently form a
dense set on which the original unweighted powers tend to zero. The claimed
failure of a uniform unweighted power bound is also correct: actual
all-valuation-one paths give `||A^q|| >= (3/2)^q`. Dense-set stability cannot
be extended to all of the unweighted space by a uniform-boundedness argument.

The Green-weighted norm is exactly one, rather than uniformly below one.
Indeed the same paths give `G_2(t_q)>=(3/2)^(2q)`, so the incoming ratios
`1−1/G_2(t_q)` tend to one. Each nonzero vector nevertheless loses the
strictly positive unweighted squared norm in the displayed identity.

### Eigenvector integrability loss

For an injective forward orbit and a unit-circle eigenvector nonzero at its
start, each endpoint contributes at least the same positive constant to
the new squared norm. The lower bound
`G_2(U^q n_0)>=J_q(n_0)^2` comes from that actual source's single contribution
to the Green sum. The conclusion does not need asymptotic orbit estimates.

The extension to every strictly positive weight satisfying
`P_2 rho<=rho` is valid by iterating one positive path contribution. This
explains precisely why the diagonal contraction cannot retain the original
nonperiodic unit-circle witness in its space.

## 4. Compressed weights and parameter ranges

The sufficient summability condition G14 follows directly from the
polynomial Green upper bound and `|w(n)|<=1/n`:
the summand is bounded by a constant times
`n^((alpha+1)theta−alpha)`, whose exponent is below `−1` exactly under the
stated strict inequality. This is a sufficient range; it is not claimed to
be an optimal characterization of witness membership.

For GM2 the sources `m_q=6*2^q−1` genuinely have `q` consecutive
valuation-one steps to `t_q=6*3^q−1`. Every intermediate source is a positive
odd ternary unit, and the smallest source tends to infinity with `q`. Thus
an eventual column inequality would apply to the whole path for large `q`.
Its required growth is `(3/2)^(alpha*q)`, whereas the Green bound supplies at
most a constant times `3^((alpha+1)*theta*q)`. The strict threshold G16 has
the correct direction.

Comparing G16 with G14 yields precisely
`alpha log 2 <= log 3`, so the entire sufficient summability range is
excluded when `1<alpha<=log(3)/log(2)`. Bounded positive multiplicative
corrections only change constants and do not change this contradiction.

At `alpha=2`, the remaining possible eventual range described in the note is

\[
\frac{2\log(3/2)}{3\log3}\le\theta<\frac13.
\]

This interval is nonempty. GM3 rules out the unmodified weight globally
through target eleven but does not rule out an eventual inequality beyond
all small targets. The note preserves that distinction correctly. Such an
eventual inequality, together with certified finite exceptions and the
credited nonperiodic eigenvector interface, would exclude nonperiodic
components. It would still require a separate positive-cycle argument.

## 5. Exact replay of GM3

Command executed successfully:

```sh
python3 research/reframe-20261121/global_mass_green_certificate.py
```

The replay classifies all 21 positive odd ternary units at most 63. Nine
reach eleven before one and twelve reach one first. The actual tail
`11,17,13,5,1` proves that eleven is not itself periodic, so each source can
contribute at most one visit to eleven.

The finite derivative sum is exactly
`68729473/16777216`. For omitted odd sources, convexity on the disjoint
intervals `[n−1,n+1]` gives

\[
\sum_{\substack{n>63\\n\text{ odd}}}n^{-2}
\le\tfrac12\int_{64}^{\infty}x^{-2}\,dx=1/128.
\]

Combining this bound with the first-hit derivative inequality yields

\[
G_2(11)\le\frac{84589185}{16777216}<\frac{81}{16}.
\]

The one legal edge `7→11` has squared derivative `9/4`, and `G_2(7)>=1`.
It alone violates the proposed global column inequality for every
`0<theta<=1/2`. The strict comparison, source traces, and pressure totals
were checked using exact integers and rational arithmetic. The unbounded
source tail is supplied by the analytic bound above, not by the finite
replay or by a convergence cutoff.

## Final scope

This review accepts the stated new paper proofs within their explicit
classes and finds the exact replay reproducible. No step supplies the
remaining eventual compressed-weight inequality, a universal target-aware
dispatcher, or exclusion of every positive cycle. The full Collatz theorem
remains open in this packet.

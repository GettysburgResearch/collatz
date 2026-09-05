# Cross-direction arithmetic wave twenty-one

**Agent:** `gpt56-synthesis-01`
**Branch:** `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
**Draft PR:** [#34](https://github.com/gfreund123/collatz/pull/34)
**Date:** 2026-07-22
**Status:** three proposed theorems, three reusable lemmas, and one source-confirmed method-boundary refutation; no counterexample claim

## Purpose

Wave twenty-one pursued four high-value proof closures and boundary audits in
parallel:

1. independently audit the new universal corrected-stage exclusion in PR #33,
   including its external Evertse theorem and signed ordinary bridge; and
2. use the maximal-run odd-carry zipper from wave twenty to exclude a genuine
   infinite class of low-complexity binary-chart schedules;
3. isolate the exact outside-prime gcd needed to turn the combined period-ten
   Pade construction from cubic raw height into quadratic primitive height;
   and
4. audit whether archimedean Hecke--Mahler transcendence can extend the run
   exclusion from periodic to Sturmian schedules.

The PR #33 audit passed, with one important source-scope clarification.  Its
arithmetic core was then abstracted into bounded- and subpower-normalization
fixed-rank endpoint-budget lemmas, together with a sharp warning that ESS
capacity cannot be summed diagonally across growing dimensions.  The
completion lane separately proved that every eventually periodic maximal-run
schedule forces an impossible rational tail carry, then located a genuine
cross-place obstruction at the Sturmian boundary.  The period-ten lane
converted the remaining primitive-height problem into one explicit
almost-total cubic gcd supported entirely at primes at least five.

## Frozen-source reconciliation

The corrected-stage audit freezes PR #33 at

```text
c9d62bce3e93f5785f72e4520bc576863d9379eb
```

and the PR #3 core imported by its exact experiment at

```text
f274dfeee3c9c391c48e58d8b57cb9f1759236f8.
```

The live PR #3 head advanced to
`d918e9a94ee28de69dc6d22ef86586e3bf62281c`, but the intervening 52 commits
add downstream room claims, experiments, and reports; they do not modify
`L-0016`, `L-0017`, `L-0028`, or `T-0027`.  The source boundary used here is
therefore both frozen and still inherited by the live head.

The signed extension needs explicit care.  `PR3/T-0027` presents its canonical
stage domain for nonnegative inputs and `Y>=0`.  Negative residuals are valid
only through `PR3/L-0028`'s all-integer composite congruence and exact finite-
domain equivalence, followed by the elementary representation

```text
z=R+QY,  z'=S+PY,  Y in Z.
```

The co-cap branch is a formal signed residual trajectory, not a positive
physical Collatz tail.  `T-9828` records this qualification explicitly.

## T-9828 -- source-qualified corrected-stage closure

The signed stage zipper has canonical data

```text
z_m     = R_m + Q_m Y_m,
z_(m+1) = S_m + P_m Y_m,
P_m/Q_(m+1) < 1/4.
```

If `Y_m>=0`, then

```text
0 <= Y_(m+1) < (Y_m+1)/4,
```

so the integer quotient reaches `0`.  If `Y_m<=-1`, put `K_m=-Y_m-1`; the
dual inequality

```text
0 <= K_(m+1) < (K_m+1)/4
```

forces `Y=-1`.  Thus every signed ordinary completion has a permanent cap or
co-cap tail.

The connector-free boundary coordinate gives, in the two orientations,

```text
2^E U_(m+1) = 3^A U_m + sum_(j=0)^255 b_j 2^(u_j)3^(v_j),
3^A U_m     = 2^E U_(m+1) + sum_(j=0)^255 b_j 2^(u_j)3^(v_j),
```

where `b_j` lies in `{9,54,36,24}`, `u_0=0`, and `v_255=0`.
The cap and co-cap correction recurrences have the same shifted height bound.
Adding the first connector exponent reconstructs

```text
2827/256 + 161341/10496 = 1083/41.
```

Relative to

```text
E_m=(8459/2)2^m+2816,
```

the two moving endpoints satisfy

```text
limsup log_2(U_m)/E_m     <=2166/346819 <1/160,
limsup log_2(U_(m+1))/E_m <=4332/346819 <1/80.
```

Their combined exponent is

```text
6498/346819 < 1/50,
```

with exact gap `21919/17340950`.

The resulting stage relation has 258 coordinates, exactly one positive.
Therefore no nonempty proper subsum vanishes.  Primitive normalization costs
at most

```text
2^3 3^3 = 216,
```

because the two endpoint internal monomials separately cap the 2- and
3-valuations.  Every internal coordinate is a `{2,3}`-unit, so all outside-
`{2,3}` content is confined to the two endpoints.  The strict exponent gap
and the raw coordinate `2^E U_(m+1)` give, eventually,

```text
product out_{2,3}(x_k) <= ||x||^(1/50)
```

with the fixed constant `c=1` after the loss 216 is absorbed.

Finally, the projective ratio of the `2^E U_(m+1)` coordinate to the `j=0`
internal coordinate has 2-adic valuation in

```text
[E_m-3,E_m+3].
```

These intervals are disjoint because

```text
E_(m+1)-E_m=(8459/2)2^m>6.
```

Hence a tail produces infinitely many distinct primitive projective tuples.

The primary source was rendered and inspected directly.  Evertse's 1984
Corollary 1, page 227, permits only finitely many primitive integer tuples with
fixed

```text
n=257, c=1, d=1/50, S_0={2,3},
```

total sum zero, no proper zero subsum, and the displayed outside-prime
product.  Pages 226 and 228 confirm the rational norm/height and the two
primitive representatives per rational projective point.  No pairwise-
coprimality hypothesis is present.  The infinite cap or co-cap tail is
therefore impossible.

This independently validates the `PR33/T-9705` conclusion conditional on its
frozen physical source identities: the unique 2-adic completion is not any
signed ordinary integer, and its canonical residue blocks are nonzero
infinitely often.

## L-9900 and L-9901 -- reusable moving-endpoint budgets

The PR #33 proof pattern is not specific to 256 cells.  `L-9900` extracts the
following fixed-rank criterion.

Suppose a family of integer zero sums has:

- a fixed number of internal `S_0`-unit coordinates;
- no nonempty proper vanishing subsum, certified for example by exactly one
  positive coordinate;
- primitive gcd bounded by `G`;
- raw height at least `H_m -> infinity`;
- two moving endpoints with combined outside-`S_0` content `B_(m,0)B_(m,1)`;
  and
- a fixed coordinate ratio separating infinitely many projective points.

If

```text
Theta=limsup log(B_(m,0)B_(m,1))/log(H_m) < 1,
```

choose any `d` with `Theta<d<1`.  Primitive height is at least `H_m/G`, and
the strict gap absorbs `G` with `c=1`.  Evertse then forbids the infinite
family.  A preassigned exponent `d` needs `Theta<d`; equality is still usable
when a fixed uniform constant is already available, by increasing `c`.

Primitive height tends to infinity under these hypotheses, so infinitely many
projective points are automatic; the explicit valuation ratio in `T-9828` is
a stronger audit certificate rather than a logical necessity.

`L-9901` permits any fixed number of moving endpoints and an unbounded
normalization gcd.  If

```text
gamma=limsup log(g_m)/log(H_m),
Theta=limsup log(B_m)/log(H_m),
```

then a prescribed Evertse exponent `d<1` works under the sharp marginal gate

```text
Theta < d(1-gamma).
```

Some `d<1` exists exactly when `Theta<1-gamma`.  The direct normalized-height
invariant

```text
Xi=limsup log(B_m)/log(H_m/g_m)
```

can be stronger when endpoint-content and gcd peaks occur on different
subsequences.  Uniform multiplicative bounds also permit equality of
exponents by increasing Evertse's fixed constant `c`.

The boundary is real, not a proof artifact.  For `S_0={2}`, the family

```text
(G_m N_m, -G_m(N_m-1), -G_m)
```

is nondegenerate and projectively distinct, has
`Theta=1-gamma`, and after normalization has outside content `N_m-1` against
height `N_m`.  It violates every fixed `c H^d` bound with `d<1`.

`T-9828` is the exact bounded-gcd specialization

```text
(r,S_0,G,H_m,d)=(256,{2,3},216,2^E,1/50).
```

The sign condition is only a transparent nondegeneracy certificate.  The
lemma also records the proper-subsum condition as the exact replacement and
gives a counterexample showing why some such hypothesis is essential.

## T-9829 -- eventually periodic run exclusion

For the binary chart

```text
U M_(n+1)=V M_n-(V-U)epsilon_n,
U=2^a<V,  V odd,
```

wave twenty gave positive odd maximal-run carries

```text
U^(ell_(k+1))q_(k+1)=V^(ell_k)q_k+sigma_k,
sigma_(k+1)=-sigma_k.
```

At an arbitrary run `k`, put `r=U/V` and
`S_(k,j)=ell_(k+1)+...+ell_(k+j)`.  Backward composition gives

```text
q_k=-V^(-ell_k) sum_(j>=0) sigma_(k+j) r^(S_(k,j)) in Q_2.
```

Normally this 2-adic sum must not be identified with its real shadow.  If the
run lengths are eventually periodic from `K`, however, choose an even common
period `T` for the lengths and alternating signs.  With

```text
L=S_(K,T),
B=sum_(t<T) sigma_(K+t)r^(S_(K,t)),
```

both completions equal the same rational geometric expression

```text
A=B/(1-r^L).
```

The real series is strictly alternating with decreasing magnitudes from one,
so

```text
0 < sigma_K A < 1.
```

Thus the required tail carry satisfies

```text
sgn(q_K)=-sigma_K,
0<|q_K|<V^(-ell_K)<=1/V,
```

contradicting its positive odd integrality.  The contradiction is deliberately
taken at the first periodic-tail carry: a finite affine preperiod can cancel a
rational denominator when propagated backwards.

Both symbols occur infinitely often in every nontrivial positive orbit.
Ultimate periodicity of the binary phase word is then equivalent to eventual
periodicity of its maximal-run lengths: one direction uses an even number of
runs, and the other uses the periodic switch-boundary indicator.  The
one-sided Morse--Hedlund lemma consequently gives, for every `n>=1`,

```text
p_phase(n)>=n+1,
p_run(n)>=n+1,
```

where the second value may be infinite.

For the physical `4 -> 5` chart, every positive ordinary survivor must
therefore have genuinely aperiodic phase and maximal-run words.  This excludes
an infinite schedule class; it does not settle aperiodic automatic, morphic,
Sturmian, or arbitrary schedules.

## R-9810 -- the Sturmian Hecke--Mahler cross-place boundary

The next natural schedule class is mechanical.  Suppose

```text
ell_(K+j)=h+floor((j+1)alpha+rho)-floor(j alpha+rho),
```

with irrational `alpha`, and put `beta={alpha+rho}`.  The exponent telescope
in the exact carry series is

```text
S_j=h j+floor(j alpha+beta).
```

Thus the required carry is a rational factor times the `Q_2` value

```text
H_2=sum_(j>=0)(-1)^j r^(h j+floor(j alpha+beta)).
```

The identical rational partial sums converge in the real place.  With

```text
b=V/U,  theta=2(h+alpha),  gamma=h+alpha+beta,
```

the real shadow splits exactly as

```text
H_infinity
 =sum_(m>=0)b^(-floor(m theta+beta))
  -sum_(m>=0)b^(-floor(m theta+gamma)).
```

The offsets obey

```text
gamma-beta=theta/2 not in Z theta+Z.
```

Integer-offset and zero-offset index normalization preserve the two lattice
classes but change the coefficients and can add an algebraic initial term.
The exact normalized form is

```text
H_infinity=c+S(b,theta,A,v),
```

with algebraic `c`, a nonzero algebraic weight vector `v`, and two distinct
offsets in `(0,1)`.  Luca--Ouaknine--Worrell Theorem 2 proves that `1` and
`S` are algebraically linearly independent, so `H_infinity` is
transcendental.  It does not evaluate `H_2`.  The even/odd Beatty split itself
does hold in `Q_2`, because both subseries converge there; only the value
theorem is archimedean.

The failure is concrete inside the same chart formalism.  For

```text
2M_(n+1)=3M_n-epsilon_n,  M_0=2,
```

iteration gives

```text
sum_(n>=0) epsilon_n(2/3)^n=6 in Q_2,
```

whereas the real limit of the same rational partial sums lies in `[0,3]`.
This rules out any silent completion identification.

Ooto's p-adic Sturmian results do not repair the bridge.  They prove
transcendence for values built from nonperiodic canonical automatic, morphic,
or Sturmian digit strings, and separately treat unweighted sparse Beatty sums
`sum p^(floor(n theta+rho))`.  Our terms carry the varying units
`V^(-S_j)` and alternating signs; no audited theorem identifies their
canonical digits with the exponent-gap word.  Lopez--Stoll's `3x+1`
conjugacy paper explicitly records the analogous aperiodic-to-rational 2-adic
question as open.

The precise missing input is therefore narrower than a generic linear-
independence statement.  For rational `b=V/2^a`, every irrational `theta>0`,
and every real `beta`, one needs irrationality in `Q_2` of

```text
F_beta^(2)(b,theta)-F_(beta+theta/2)^(2)(b,theta).
```

This directly equals the forced mechanical carry series.  `R-9810` is a
source-confirmed method boundary, not a Sturmian counterexample or exclusion.

## L-9902 -- fixed-term-count capacity cannot be diagonalized

The quantitative Evertse--Schlickewei--Schmidt bound

```text
A(n,rho)=exp((6n)^(3n)(rho+1))
```

counts nondegenerate solutions over characteristic-zero fields only after the
term count, coefficient vector, and one common multiplicative group have been
frozen.  `L-9902` makes the
correct binning explicit: capacities may be summed over finitely many such
classes, but not over one new equation dimension at every stage.

The boundary family is

```text
(2^(n-1), -1, -2, -2^2, ..., -2^(n-2), -1),  n>=2.
```

It has exactly one positive coordinate, no proper zero subsum, gcd one,
unbounded height, and outside-`{2}` endpoint budget one.  After normalization,
the unique displayed solution at each fixed `n` lies in a cyclic group of
rank one.  It remains far below `A(n,1)`, while the union over changing `n` is
infinite.  Multiplying by `2^floor(sqrt(n))` supplies the same example with an
unbounded subpower gcd.

Hence the endpoint budgets in `L-9900`--`L-9901` genuinely require fixed
coordinate count.  A growing-term-count argument must overfill one fixed bin; point
separation across different projective spaces has no ESS counting force.

The characteristic-zero hypothesis is essential.  Over `F_p(t)`, Frobenius
puts `(t^(p^k),(1-t)^(p^k))` in one rank-one group and yields infinitely many
solutions of `y_1+y_2=1`.

## T-9830 -- period-ten height becomes an outside-prime cubic gcd

For a fixed positive stack word `W` of length `r`, the normalized base Schur
quotient has the exact form

```text
Q_n(T)=T^(a_n)F_(n,0)(T),
d_n=deg F_(n,0)
   =n gamma_*+[9S(r-1)/6]n(n-1)(n+7),
```

where `F_(n,0)` has nonnegative integral coefficients, constant term one, and
leading coefficient one.  Homogenizing at `T=64/81` gives

```text
G_(n,0)=81^(d_n)F_(n,0)(64/81)>0,
gcd(G_(n,0),6)=1.
```

Every maximal Cramer minor has an analogous prime-to-six core `G_(n,k)`, and
the canonical coefficient factors exactly as

```text
b_(n,k)=(-1)^k 2^(6 alpha_(n,k))G_(n,k)
          /[3^(4 beta_(n,k))G_(n,0)].
```

Thus all coefficient content invisible at `2` and `3` is literally a gcd
among these homogeneous integers.

At `Y=1`, clear with

```text
D_n=3^(4 beta_n)G_(n,0),
hat A_n=D_n A_n(1),  hat B_n=D_n B_n(1).
```

The endpoint selectors give

```text
v_2(hat A_n)=v_2(hat B_n)=0,
v_3(hat B_n)=0,
v_3(hat A_n)=4 kappa.
```

Consequently `gcd(hat A_n,hat B_n)` is supported only at primes at least
five.  Real principal-specialization bounds prove
`B_n(1)->1` and `A_n(1)->H_infinity>0`, so additive cancellation cannot hide
the clearing-factor size.  With `W,S,m` fixed,

```text
log_2 max(|hat A_n|,|hat B_n|)
 =6S(r-1)log_2(3)n^3+O_(W,m)(n^2).
```

Therefore quadratic primitive height is equivalent to the almost-total gcd
law

```text
log_2 gcd(|hat A_n|,|hat B_n|)
 =6S(r-1)log_2(3)n^3+O_(W,m)(n^2).
```

For period ten the cubic coefficient is `54S log_2(3)`.  This cancellation,
if it exists, must come entirely from primes at least five.

The same theorem adds an exact finite 3-adic distance law to the 2-adic
ladder from `T-9826`:

```text
v_2(R_m-R_n)=12 zeta n+81Sr n(n-1),
v_3(R_m-R_n)=4(kappa+9Sr n),  m>n.
```

It follows that at least one of every pair of consecutive approximants lies
above the half-error height floor.  This constrains full or nonlacunary
sequences, not an arbitrarily sparse subsequence.

An independent cold review reconstructed both Schur selectors, all Cramer
exponents, clearing integrality, real convergence, raw gcd support, and both
distance ladders.  It found one notation-level issue: the cubic remainder was
initially written `O_r(n^2)` although its constants depend on the fixed word
and starting height.  The claim now says `O_(W,m)(n^2)` and states the fixed-
parameter asymptotic regime explicitly.

## Review and exact boundaries

- Three independent lanes reconstructed the PR #33 proof: connector algebra
  and endpoint heights, the exact Evertse source map, and primitive/native
  arithmetic plus the signed-completion bridge.
- The primary PDF was used only to verify the theorem statement.  Temporary
  render files were removed and are not part of the repository.
- `L-9900`--`L-9902` expose exactly which parts of the closure are reusable,
  quantify normalization loss, identify a sharp exponent boundary, and show
  why fixed-term-count ESS capacity cannot be diagonalized across dimensions.
- `T-9829` uses no external theorem beyond an elementary proof of the one-
  sided Morse--Hedlund implication.  A nonauthoring cold review passed the
  carry signs, terminal factor, even-period rationalization, preperiod example,
  phase/run equivalence, and complexity proof.
- `R-9810` maps the real Beatty value to its primary complex theorem but
  quarantines that conclusion from the required 2-adic value.  Cold review
  corrected both zero-offset normalization and the exact p-adic target.
- `T-9830` received a nonauthoring algebraic cold review; every selector,
  valuation, gcd, convergence, and distance identity passed after the
  asymptotic constant was qualified as word-and-start dependent.
- No finite experiment is a proof dependency.  Exact fraction replay checked
  the endpoint identities and strict gaps redundantly.
- No theorem here constructs or excludes a nontrivial Collatz orbit outside
  the stated chart or corrected-stage interfaces.

All claims remain `PROPOSED` pending external review.  No `K-####` candidate
is proposed.  The pre-publication memory snapshot was healthy at 9.14 GiB
free with 40.7% of physical memory in use.

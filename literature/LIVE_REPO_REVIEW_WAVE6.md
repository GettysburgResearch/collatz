# Live repository review — literature audit wave 6

**Agent:** `gpt56-pro-03`  
**Issue:** `#7`  
**Snapshot:** 2026-07-22, after PR #20's withdrawn all-directive chain, PR #34's combined-moment and late-wave synthesis, PR #3's finite-room/transcendence/two-block reduction, and PR #35's exact `5/4` control frontier  
**Status:** literature and strategic applicability audit; no native claim is promoted by this file

## Executive assessment

The repository has now produced two unusually sharp fronts.

1. **Fixed periodic stack tails.** Periods at most nine are excluded by the fully inspected Väänänen–Wallisser theorem. Period ten has been reduced natively to one scalar combined-moment Padé problem with exact nonvanishing and exact `2`-adic error. The remaining obstruction is one global reduced-height estimate.
2. **The corrected phase-34 construction.** Every hypothetical late ordinary path lies in one of at most 64 transcendental real rooms and must satisfy one adjacent twelve-bit Hensel pattern at every sufficiently late scale. The finite audit finds no such pattern through scale 19, but no cofinal theorem exists.

The most important correction is equally clear: PR #20's brief all-directive conclusion was withdrawn for a genuine mathematical reason. The same rational partial sums can converge to different rational values in `R` and `Q_2`; a bounded Archimedean shadow cannot be used as a height bound for the rational `2`-adic target. The withdrawal is properly preserved in atomic claim files, but should be foregrounded in the PR summary and current-state documents before further agents resume.

The strongest route toward **all fixed periods** is now a block moment-factorization program:

```text
combined periodic moments
 -> one decimated quadratic-exponential moment functional
 -> block/multiple-orthogonal Christoffel factorization
 -> cancel the universal cubic Hankel bulk
 -> bound the fixed-rank boundary determinant globally
 -> combine with the exact 2-adic error by the product formula.
```

This is more focused than returning to ten independent phase windows.

---

## 1. PR #20 — the withdrawn all-directive chain and its valid residue

### The withdrawn inference

The following claims are explicitly withdrawn in the branch:

```text
T-9418  unbounded gaps imply irrationality;
T-9419  every positive stack directive is irrational;
T-9420  rational code iff eventually periodic;
T-9421  the ordinary section is trivial.
```

The first invalid inference was cross-completion identification. For rational partial sums `x_N`, convergence in two completions does not force the two limits to be the same rational number. The elementary control

```text
x_N=2^N/(1+2^N)
```

satisfies

```text
x_N -> 1 in R,
x_N -> 0 in Q_2.
```

For the binary `64/81` tails, the positive real series is bounded, while the `2`-adic series used by the survivor coding may be a different rational value with unbounded ordinary numerator.

### What remains valid

`L-9416` and `L-9417` prove an exact arithmetic fact:

```text
if a Q_2 tail is rational,
then its later reduced denominators divide one fixed odd denominator.
```

This does **not** yield finitely many tail states because the numerators remain uncontrolled.

The periodic theorems remain intact:

```text
native Padé: minimal periods <=3;
Väänänen–Wallisser: minimal eventual periods <=9.
```

The withdrawal therefore does not damage the valid periodic program. It identifies the missing coordinate: ordinary numerator or global height.

### Process correction

The branch's atomic files document the withdrawal well. The top-level PR body, `LATEST.md`, `README.md`, and any project crosswalk should also state prominently:

```text
WITHDRAWN:
all-positive-stack irrationality,
rationality => eventual periodicity,
ordinary-section triviality.

FIRST INVALID STEP:
Archimedean bound transferred to a separate Q_2 limit.
```

This prevents a later agent from rebuilding downstream work on a superseded headline.

`LIT-KTHM-0044` adds a reusable completion firewall and records the correct two-place Padé architecture.

---

## 2. The all-fixed-period path — decimated q-Gaussian moments

### Exact native object

For a period-`r` word, PR #34 `T-9821` uses the combined moments

```text
u_N
 =R^[N(N-1)/2] Z^N P_W(X lambda^N)
 =sum_(h=0)^(r-1)
   C_h R^[N(N-1)/2](Zlambda^h)^N,
R=lambda^r.
```

It proves:

- every square combined Hankel minor is nonzero;
- the canonical Padé denominator exists uniquely;
- the first evaluated error has exact order
  ```text
  v_2(error)=81Sr n^2+O(n);
  ```
- there is no hidden phase cancellation in that first error.

The remaining theorem is one primitive-height estimate for the evaluated Cramer ratios.

### New exact decimation lift

`LIT-KTHM-0045` introduces algebraic parameters `q_0,b` with

```text
q_0^r=lambda,
b^r=Z q_0^[-r(r-1)/2]
```

and one fine moment sequence

```text
m_k=q_0^[k(k-1)/2]b^k.
```

With fixed word coefficients `D_h`, it proves exactly

```text
boxed:
nu_N=sum_(h=0)^(r-1)D_h m_(rN+h).
```

Equivalently, for the formal functional `L(x^k)=m_k`,

```text
boxed:
nu_N=L(D_W(x)x^(rN)),
D_W(x)=sum_(h=0)^(r-1)D_hx^h.
```

The base fine Hankel determinant is an explicit Vandermonde product. Thus the periodic-stack moments are not an arbitrary ten-phase family: they are one fixed polynomial deformation of a quadratic-exponential moment functional, followed by `r`-fold decimation.

### External factorization theorem

Krattenthaler's Christoffel determinant theorem says that, for an ordinary moment functional, a fixed degree-`d` polynomial deformation factors as

```text
base Hankel determinant
 x one d-by-d determinant of orthogonal-polynomial values
 / one Vandermonde.
```

The identity is formal and does not require a positive real measure.

`LIT-KTHM-0046` imports this theorem and records the exact nonapplication: the stack functional is sampled at `x^(rN)`, so in the coarse variable `y=x^r`, the word polynomial contains fractional powers `y^(h/r)`. A scalar Christoffel formula would silently erase the residue classes modulo `r`.

The correct object is the `r`-component functional

```text
L_h(y^N)=L(x^(rN+h)),
0<=h<r.
```

Mixed multiple-orthogonal and biorthogonal Stieltjes–Wigert theory supplies the natural framework for its block moment matrix.

### Why this can remove the cubic height

Raw Hankel determinants have cubic logarithmic height. But orthogonal-polynomial norms and recurrence coefficients are ratios

```text
h_n=Delta_(n+1)/Delta_n,
beta_n=Delta_(n+1)Delta_(n-1)/Delta_n^2.
```

`LIT-KTHM-0047` proves these identities from the moment determinants. Such ratios cancel a universal cubic term formally. This explains why `T-9824`'s cubic Schur quotient is a method boundary for one raw determinant, not a no-go for Cramer ratios or block recurrence coefficients.

### The exact theorem to prove

For each fixed period `r`, derive a block Christoffel–Uvarov identity for every base and bordered minor used by `T-9821`:

```text
minor
 = universal fine q-Gaussian bulk
   x fixed-rank r-component boundary determinant.
```

Then prove, after rational specialization,

```text
log_2 H(A_n(1):B_n(1))
 <=(81Sr-eta_r)n^2+o(n^2)
```

for some `eta_r>0` along an infinite subsequence. The exact `2`-adic error and the product formula then prove the prescribed fixed-period value irrational.

This would close **every fixed positive period**.

### What still remains after all fixed periods

Qualitative irrationality for each fixed period does not automatically settle the balanced nonperiodic `17/18` directive. The boundary factors must be controlled as `r` grows along adjacent standard words. The desired output is a bound with `eta_r` and all constants deteriorating slowly enough to pass through the exact S-adic transfer matrices.

This is the mathematically mature descendant of the earlier Liouville/Staircase special-value proposal.

---

## 3. Completion-safe Padé rather than equal completion values

The withdrawn PR #20 proof should not cause the project to abandon Archimedean companions. The correct use is subtler.

The Euler-factorial/Hardy-integral literature uses the same rational Padé polynomials in two places:

```text
finite-place limit:  the target p-adic series;
real companion:      a different analytic value used to bound coefficients.
```

The proof estimates the same rational Padé numerator and denominator at all places and invokes the product formula. It never identifies the two completion limits.

For the stack moments, every new Padé packet should expose four separate objects:

```text
2-adic target value;
real analytic companion;
rational Padé coefficient vector;
nonzero ordinary integer or projective product-formula expression.
```

This is now encoded in `LIT-KTHM-0044`.

---

## 4. PR #3 — from a huge stage grammar to one moving twelve-bit filter

PR #3 has advanced beyond cap-to-correction equality.

### Current conditional classification

For an assumed infinite corrected-stage path:

1. the free quotient eventually vanishes;
2. the scaled boundary is generated by one real room `C_infinity`;
3. the complete local type sequence is a floor-orbit coding of that room;
4. the path must introduce infinitely many fresh ordinary prime factors;
5. there are at most 64 eventual rooms/tails;
6. every such room is transcendental by a two-place Ridout argument.

These are classification results, not contradictions.

### Atomic remaining condition

A three-symbol prefix has one canonical input address `rho_m(a,b,c)` and one six-bit Hensel lift `h_m(a,b,c)`. A late room requires both

```text
q_m(a,b,c)=floor(64 rho_m/M_m)=0,
[-N_m h_m(a,b,c)]_64 in {5,30,20,56}.
```

Thus one adjacent twelve-bit pattern must occur at every sufficiently late scale:

```text
[allowed six-bit output lift]
[zero six-bit input cell]
```

The exact audit finds no such prefix for scales 12 through 19. Cofinal emptiness of this finite moving filter would close the entire fixed corrected-stage architecture.

### Literature-shaped next theorem

The useful product-formula object is not the real room alone. It is the same modular inverse viewed in three coordinates:

```text
real:    rapidly convergent positive defect digit expansion;
binary:  a high zero input block plus six-bit Hensel lift;
ternary: the next boundary valuation/type.
```

A next proof should derive a rational approximation or nonzero integer from these **same exact quantities**, avoiding the cross-completion mistake. Two plausible targets are:

1. a two-block Newton-carry recurrence whose long zero cell forces a nonzero integer to be divisible by too large a power of two relative to its full height;
2. a fixed finite-term exponential equation for one recurring three-symbol state, followed by a complete proper-subsum audit and a two-place logarithmic-form bound.

The finite-room theorem means only finitely many coherent tails need survive, but it does not produce their values effectively.

---

## 5. PR #16 and PR #32 — use the reviewed EQ theorem downstream

PR #32 independently reconstructs the complete all-depth weighted-EQ chain through `ADEL/T-9312`. This should now enter the canonical review registry and native status ledger.

PR #16's ordinary-section frontier is separate:

```text
ordinary survivor
 <=> exists xi>0 with ||xi(81/64)^n||<=1/81 for all n
 <=> appended nearest-integer blocks are eventually zero
 <=> exact finite survivor minima remain bounded.
```

The real centered-error system is a full binary shift, so a pure interval-graph emptiness argument cannot work. The missing theorem must retain the nearest-integer arithmetic.

The next literature task remains the full Dubickas specialization at `(81,64)`, including its extremal Thue–Morse word, translated into the appended-block recurrence. Further Fourier expansion is lower priority.

---

## 6. PR #19 — the H subsystem's three arithmetic regimes

PR #19 now has a monotone ordinary-section minimum `nu_K` with

```text
H termination
 <=> nu_K -> infinity.
```

The clean literature split remains:

1. **critical two-term regime:** expose one fixed difference of algebraic powers and use explicit `2`-adic logarithmic-form estimates;
2. **nondegenerate finite-term regime:** place persistent prime support in one finite-rank multiplicative group and apply S-unit finiteness after every proper subsum is classified;
3. **subcritical regime:** build an integral transformed height and use a finite trap.

The newest PR #34 successive-core equations make the first two reductions more concrete but do not yet freeze the fresh-prime support.

---

## 7. PR #35 — the `5x+1` control identifies a named rational-base frontier

The exact `4 -> 5` amplifier gives a clean comparison universe. Its ordinary completion is equivalent to an infinite base-`5/4` low-digit word using only digits `0,1`, and the exact depth-50 frontier is now certified.

This does not directly transfer a divergent seed to `3x+1`. Its value is diagnostic:

- finite cylinders, Cantor dimension, and density zero still do not decide emptiness;
- the least-root sequence and its exact meet-in-the-middle composition provide a control for the PR #16 and PR #19 minimum programs;
- the surviving global question coincides with a named rational-base approximate-multiplication/normality frontier.

The control therefore confirms that minimum divergence, not finite thinness, is the decisive asymptotic object.

---

## 8. Critical-path priorities

1. **All fixed periods:** prove the block q-Gaussian Christoffel factorization and a quadratic primitive-height bound for `T-9821` Cramer ratios.
2. **All fixed periods to the balanced directive:** make the boundary estimate uniform along adjacent standard-word periods and use `PADIC/L-9408` S-adic transfer.
3. **Fixed corrected stage:** prove cofinal emptiness of PR #3 `T-0039`'s adjacent twelve-bit filter using a completion-safe product-formula or Newton-carry recurrence.
4. **Ordinary `64 -> 81` section:** specialize Dubickas exactly and translate the extremal word into appended blocks.
5. **H subsystem:** freeze one two-term logarithmic form and one proper-subsum-audited S-unit equation.
6. **Integration:** foreground PR #20's withdrawals and admit PR #32's reviewed statuses before another broad wave.

## Status boundary

No theorem in this review proves all fixed periods, the balanced nonperiodic directive, an ordinary survivor, or the Collatz conjecture. The new contribution is an exact algebraic reduction and a sharply specified literature-backed proof program.

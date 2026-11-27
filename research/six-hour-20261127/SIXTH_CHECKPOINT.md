# Sixth checkpoint: a finite cycle-period exclusion and physical residue sources

**Collatz remains open.** This checkpoint follows `8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec`. Its strongest finite result rules out ordinary cycles of odd period at most $10^{1000}$ in the canonical-height-one class, using a published minimum-state verification as input. The finite arithmetic now has a compressed Lean certificate. The physical and analytic bridges are written proofs with independent reviews.

The [root review](../../reports/six-hour-20261127/ROOT_REVIEW_WAVE6.md) states the exact evidence and unresolved steps. The [fifth checkpoint](FIFTH_CHECKPOINT.md) retains the ordinary safe-suffix equivalence and its explicit bit-length bound.

## 1. A cycle in this class needs more than $10^{1000}$ odd phases

For a positive ordinary cycle, let $P$ be its least odd period, $e_i$ its accelerated valuations, $A=\sum_{i<P}e_i$, and $E_j=\sum_{i<j}e_i$. Define its canonical real width by

$$
 W=\max_{0\le j<P}(E_j-jA/P)-\min_{0\le j<P}(E_j-jA/P).
$$

The [finite theorem](cycles/ADJACENT_GAP_PERIOD_EXCLUSION.md) proves

$$
 W<2\quad\text{and}\quad\min_i x_i\ge2^{71}
 \quad\Longrightarrow\quad P>10^{1000}.             \tag{1}
$$

Valuation three is allowed. This broadens the earlier finite exclusion which assumed binary valuations and a particular physical strip. Bařina's published verification below $2^{71}$ supplies the minimum for a nontrivial ordinary cycle. The root and reviewer checked that publication's map and stated coverage; its trajectory enumeration was not repeated here. The theorem with the explicit floor hypothesis uses no Subspace Theorem or irrationality-exponent estimate. [Bařina, 2025, Section 6](https://link.springer.com/article/10.1007/s11227-025-07337-0).

### Why only 959 candidate periods need arithmetic tests

The rank-convexity proof from checkpoint five is made effective over the finite range. Exact continued-fraction fences first exclude $P\le10^6$ and bound the maximum odd phase by $2X<2^{7000}$ for $P\le10^{1000}$. An exact logarithm interval checks all short mechanical multiples through 7003, providing the seam avoidance needed by the arithmetic-progression contradiction. This proves strict rank convexity throughout the finite problem without an asymptotic irrationality input.

Write $L_r$ for the scaled labels in mechanical rank order and $g_r=L_{r+1}-L_r$. The convexity gives strictly increasing integer gaps with $g_P=2g_0$. It also gives a lower quadratic profile for $L_r$. An eight-bin reciprocal estimate then shows

$$P^2(A/P-\log_2 3)<0.484763<\tfrac12.$$

Consequently the slope $A/P$ must be an upper continued-fraction convergent of $\log_2 3$. The common exact rational enclosure supplies every convergent in the finite range. After the minimum-state test, 959 candidates remain.

The source count is especially efficient because the gaps are ordered. After discarding at most $b+1$ seam terminals, the backward mechanical calendars are constant on at most $b+1$ rank intervals. The numerical spans of their terminal gaps sum to less than $g_0$. At each mechanical-one edge, two of the nine consecutive drift pairs are forbidden; those edges are disjoint. Thus every hypothetical cycle satisfies

$$
 P\le b+1+\bigl(g_0+(b+1)3^b\bigr)
       (7/9)^{\lfloor(2-A/P)(b-1)\rfloor}.            \tag{2}
$$

For each convergent the product identity bounds $g_0$ by an explicit integer $Y$. A concrete choice of $b$ makes the right side of (2) strictly below $P$ for all 959 candidates. The closest comparison is

| Quantity | Exact value |
|---|---:|
| $A$ | 217976794617 |
| $P$ | 137528045312 |
| Upper bound $Y$ for $g_0$ | 771316334040 |
| Window $b$ | 18 |
| Disjoint constrained pairs | 7 |
| Integer upper count | 134074517099 |

The maximum count-to-period ratio is below $0.974889$. The author uses an inverse-hyperbolic-tangent logarithm series; the independent reviewer uses different positive geometric logarithm series. Both obtain the same 959 exclusions. The [independent review](../../reports/six-hour-20261127/ADJACENT_PERIOD_EXCLUSION_INDEPENDENT_REVIEW.md) reconstructs the coverage, seam conditions, reciprocal estimate and total-span argument.

### What Lean proves here

[AdjacentPeriodCensus.lean](cycles/AdjacentPeriodCensus.lean) contains 1,944 pairs consisting of a continued-fraction coefficient and a chosen window length. It reconstructs the numerators and denominators itself. It checks the prescribed common 1,944-term prefix of both rational endpoint Euclidean algorithms, their order and precision, the count of 959 selected rows, and the actual integer exclusion inequality for every selected row. All seven declarations are proved by kernel reduction with empty axiom sets.

This is a certificate of the finite arithmetic. The real logarithm enclosure, completeness inference from the continued fractions, and Collatz-to-census argument remain written proofs. [Certificate scope](cycles/ADJACENT_PERIOD_LEAN_CERTIFICATE.md). The additional [RankSpacingExtinction module](cycles/RankSpacingExtinction.lean) proves divisibility and extinction of a positive arithmetic-progression spacing over an arbitrary finite mechanical clock.

Equation (1) leaves periods above the bound, wider cycles, and escaping ordinary orbits unresolved.

## 2. Denominators can be removed inside one physical residue class

For a positive primitive rational cycle write $x_i=N_i/d$ in lowest terms. Let $R$ count the different residues $N_i\bmod d$, equivalently the fractional parts actually visited by its odd phases. Set $S=|\langle2,3\rangle_d|$; always $R\le S$, and take $R=S=1$ when $d=1$.

The [physical source reduction](cycles/RESIDUE_FIBRE_PHYSICAL_SOURCE.md) fixes a residue $r$ and writes $N=r+dJ$, where $J=\lfloor x\rfloor$. From the true window identity $2^KN_b=3^bN_0+dB$ it obtains

$$
 J_0\equiv-3^{-b}B-r_0d^{-1}\pmod{2^K},\qquad
 J_b\equiv2^{-K}B-r_bd^{-1}\pmod{3^b}.               \tag{3}
$$

Thus the denominator contributes a known translation of the source interval. The interval has physical size $X$, rather than numerator size $dX$, and the frequency coefficient tested by separation no longer contains $d$. The constants are uniform over the full denominator and the fixed residue. A floor of zero is included. The floor sequence itself is not asserted to be an ordinary Collatz orbit.

The earlier fourth- and fifth-moment source estimates therefore hold for each occupied residue separately:

| Cycle class | Per-residue population at physical height $X$ |
|---|---|
| Binary valuations, $W\le1.98$ | $O_\epsilon((1+X)^{999/3000+\epsilon})$ |
| Binary valuations, $W<2$ | $O_\epsilon((1+X)^{1/3-1/40000+\epsilon})$ |
| Binary valuations, $W\le2+10^{-5}$ | $O_\epsilon((1+X)^{1/3-1/80000+\epsilon})$ |
| Binary valuations, $W\le2.42$ | $O_\epsilon((1+X)^{2/5+\epsilon})$ |
| All positive valuations, $W\le2.1$ | $O_\epsilon((1+X)^{29/60+\epsilon})$ |

These rows use the inherited fixed-place separation theorem. The separately qualified exponent-three input converts the first three into lower bounds on actual residue diversity. The sparse canonical and physical alternatives likewise strengthen: their small-denominator hypothesis can be replaced by small **occupied residue population** $R$. Unbounded excursions and unbounded valuations at the charged sites remain allowed. The [fresh review](../../reports/six-hour-20261127/RESIDUE_SOURCE_PHYSICAL_INDEPENDENT_REVIEW.md) checks the translations before source enlargement and the uniformity of the resulting bounds.

## 3. Rational convexity and removal of a small-offset loss

The [rational rank theorem](cycles/RATIONAL_RESIDUE_RANK_CONVEXITY.md) identifies exactly which rank offsets have matching scaled numerator residues. If $g=\gcd(A,P)$, $q=P/g$ and the canonical height is at most two, the order of $3^q2^{-A/g}\bmod d$ is $g$. Put $T=S/g$. The compatible nonzero rank offsets are exactly the multiples of $T$ below $q$, each with one chronological lift.

At height at most one and $S\le P/(\log P)^8$, the compatible-step curvatures are at least $d$. Every compatible gap value has at most $S$ occurrences, and $X\gg(P/S)^2$. This uses the published finite logarithm estimate and no Subspace Theorem. The [independent review](../../reports/six-hour-20261127/RATIONAL_RANK_LANES_INDEPENDENT_REVIEW.md) checks the multiple rank copies and both seam types.

The [adjacent-gap refinement](cycles/RATIONAL_ADJACENT_GAP_LOSS_REMOVAL.md) then proves, when $S=P^{o(1)}$,

$$
 \liminf\frac{\log X}{\log P}\ge
 1+\frac{\ln3}{\ln3+(2-\log_2 3)\ln(7/9)}
 =2.1049020798\ldots .                              \tag{4}
$$

This elementary source count follows compatible physical gaps at scale $XS/P$ and loses only the subpower factor $S$. It needs no integral separation. For ordinary cycles, Weaver 145 already has the stronger numerical exponent $16/7$ using its Subspace Theorem argument; the distinct point of (4) is its method and rational subgroup scope.

Combining (4) with the signed-gap entropy argument removes the residue-order multiplier that was needed for very small incompatible offsets. At every nonresonant lag $q\nmid h$, the valuation-mismatch fraction has limiting infimum strictly above $1/1000$ under the published 2018 input, or above $1/55$ under the quoted exponent-three input. At vanishing shorter rank fraction, $1/55$ already follows from the 2018 input. The earlier stronger $1/36$ remains in its previously covered classes. The $g-1$ possible proper resonant multiples of $q$ remain excluded from these assertions.

The [original rational lag transfer](cycles/RATIONAL_RANK_LAG_CONSUMERS.md) and its [independent review](../../reports/six-hour-20261127/INDEPENDENT_RATIONAL_LAG_CONSUMER_REVIEW.md) are preserved. The improvement has its own [fresh review](../../reports/six-hour-20261127/INDEPENDENT_RATIONAL_GAP_CENSUS_REVIEW.md), so the stronger result is not silently attributed to the older statement.

## 4. The ternary residue word must also disagree with its shifts

In an ordinary cycle, $x_{i+1}\equiv(-1)^{e_i}\pmod3$. The [new separation theorem](cycles/TERNARY_RESIDUE_LAG_RIGIDITY.md) concerns

$$Q_h=\#\{i:x_i\not\equiv x_{i+h}\pmod3\},$$

which identifies valuations one and three and is therefore a coarser observable than the full valuation word. For height-one cycles it proves a qualitative positive fraction $Q_h/P$ uniformly over shifts of additive order at least 2000 using the 2018 estimate and fixed-place separation. With the quoted exponent-three input it covers every proper shift. The latter result uses an exact 64-letter two-parameter energy certificate.

The key distinction is between drift strings and hidden bit histories. Unobserved bits are projected by Boolean relations, and energy counts each distinct drift string once. Ternary peeling proceeds from the terminal block and bounds every inherited shifted residue. The [independent reviewer](../../reports/six-hour-20261127/INDEPENDENT_TERNARY_RESIDUE_LAG_REVIEW.md) reconstructs the parameter coverage using a different phase-square decomposition and an uncollapsed six-state transfer. No numerical mismatch constant or effective onset is claimed for these rows.

## 5. An unrestricted elementary residue bound and an abstract obstruction

The [exact residue census](cycles/EXACT_RESIDUE_SUPPORT_AND_UNCAPPED_DIVERSITY.md) handles deficient clock order as well as the ordered low-height regime. It gives the entire population distribution of scaled residues using $k=\operatorname{ord}_d(3^q2^{-A/g})$, including $k<g$. In the ordered regime this yields

$$\frac{\min(P,S)}{H+1}\le R\le\min(P,S).$$

For arbitrary positive rational cycles, without any width or valuation cap, an elementary maximum-ending interval argument gives

$$d<4^R\quad\text{or}\quad P<R\big((3/2)^R+1/2\big). \tag{5}$$

If $R=1$, the cycle is ordinary or a rational singleton. These conclusions describe actual fractional parts, not a uniform distribution assumption for them.

The [abstract counterconstruction](cycles/CONVEX_TERNARY_CAP_OBSTRUCTION.md) tests another route to a cubic height contradiction. It builds integer rank populations with exact octave doubling, strict convexity at both seams, arbitrary prescribed lowbits one or two, distinct odd parts, every-depth ternary midpoint restrictions, and a smooth exponential profile with error $o(P)$. Nevertheless their height is only

$$P^{,2+\log_2(3/2)}=P^{2.5849625\ldots}.$$

A second construction fits one freely chosen additive digit cube through a modulus comparable to height divided by period. Neither construction is an actual Collatz orbit. The [root's independent review](../../reports/six-hour-20261127/ROOT_RANK_CAP_REVIEW.md) proves that these abstract constraints alone cannot supply the desired cubic contradiction. The exact chronological Collatz weights or another missing physical property are essential.

## 6. Remaining global task

The finite theorem leaves larger periods and other widths. The residue-source results constrain populations with specified recurrence or strip structure. They do not give a cyclic incidence law to an escaping ordinary trajectory. The completed Lean safe-suffix equivalence still leaves the universal exclusion of permanently safe ordinary sources unproved. That all-source step is the focus of the remaining session.

The packet's portable replay now includes 30 Lean modules and 77 finite programs, including regeneration of the compressed Lean data. The root review and receipts record which runs completed and what they certify. Imported analytic theorems, external trajectory verification and written asymptotic proofs retain their distinct scopes.

# Live repository review — literature audit wave 5

**Agent:** `gpt56-pro-03`  
**Issue:** `#7`  
**Snapshot:** 2026-07-22, after the full Väänänen–Wallisser paper was supplied and after the newest PR #3, PR #16, PR #19, PR #20, PR #33, and PR #34 theorem waves  
**Status:** literature and applicability audit; no native claim is promoted by this file

## Executive assessment

The previous pass did state its forward ideas explicitly: the highest-priority item was to obtain and inspect the full Väänänen–Wallisser theorem. That source has now been supplied, and it delivers a real theorem rather than only methodology.

The exact new conclusion is:

```text
Every eventually periodic positive stack directive
whose minimal eventual period is at most nine
selects an irrational 2-adic context.
```

Thus no such directive can initialize an ordinary integer. Period ten—not period four—is the first fixed period outside the numerical range of that source theorem.

Meanwhile, the overnight native work has substantially narrowed three other frontiers:

1. PR #3 and PR #33 eliminate the free corrected-stage quotient and reduce every late ordinary trajectory to exact cap-to-correction equality in an exponentially shrinking cusp.
2. PR #16 and PR #19 each produce a monotone ordinary-section minimum whose divergence is equivalent to exclusion of all nontrivial ordinary points in the relevant subsystem.
3. PR #34 turns broad cross-program ideas into exact finite-state, cyclotomic, Hensel, survivor-order, and two-place Diophantine interfaces.

The best literature contribution now is not another broad survey. It is to attach the strongest available theorem to each exact interface and state the missing native reduction precisely.

## 1. PR #20 — the attached paper closes periods one through nine

### Full source theorem

Väänänen and Wallisser study

```text
f_q(z)=sum_(n>=0) q^(n(n-1)/2) z^n
```

for rational `q` with `0<|q|_p<1`. Their Theorem 1 gives a quantitative linear-independence measure for

```text
1,f_q(y_1),...,f_q(y_D)
```

when the points lie in distinct multiplicative `q^Z`-orbits and one explicit numerical inequality holds.

### Exact native reduction

For a periodic word `W` of length `r`, PR #20 writes

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j f_R(Z lambda^j),
R=lambda^r,
```

with rational nonzero coefficients and evaluation points in distinct `R^Z`-orbits.

At `p=2`, the source parameter simplifies to

```text
1-log(64)/log(81),
```

independently of the word and its height sum. `LIT-KTHM-0042` proves exactly that the source inequality holds through dimension nine and fails at dimension ten.

### Result

Every fixed periodic tail of minimal period at most nine is irrational. The exact finite-prefix transfer identity propagates this to every eventually periodic directive with minimal eventual period at most nine.

### Strategic correction

PR #20's native periods-one-through-three Padé proofs remain important because they are self-contained and reveal the approximation mechanism. The extensive period-four work remains a valuable exact laboratory. But its next mission should be one of:

1. period ten, the first source-uncovered fixed period;
2. a source-independent all-period theorem;
3. quantitative bounds uniform in period length, suitable for adjacent standard-word limits.

Fixed-period irrationality without period-uniform constants still does not decide the balanced nonperiodic `17/18` directive.

## 2. PR #34 — retarget the Padé forge and exploit exact new interfaces

PR #34 has moved well beyond the 70-claim initial forge. The newest waves add:

- period-four quotient, jet, q-Lucas, and Cartier structures;
- post-window phase dominance;
- adjacent-order Casoratian nonvanishing;
- survivor one-hot and rank exposure;
- cap collar/triple compression and Hensel stitch isometries;
- repaired H ghost boundaries and dual renewal coordinates;
- successive H-core compatibility equations.

### Padé retarget

Because Väänänen–Wallisser already closes periods at most nine, the q-Lucas/Cartier and adjacent-Casoratian machinery should be tested at period ten and then parameterized by period `r`.

The decisive benchmark is no longer “repair the period-four deficit.” It is:

```text
obtain a reduced-height/vanishing estimate
whose constants remain controlled as r grows.
```

The period-four packet should remain as a regression and proof-of-method suite.

### Successive H cores

The exact equation

```text
8^R 4^b Y - 9^R 3^a X = 9^R - 8^R
```

is now close enough to the S-unit and p-adic-logarithmic-form literature to justify a dedicated reduction. The next file should split `X,Y` into persistent and fresh prime support, enumerate proper vanishing subsums, and determine whether the persistent part lies in one fixed finite-rank group.

`LIT-KTHM-0043` supplies the correct nondegenerate finiteness theorem. It is not applicable until that support and proper-subsum audit is complete.

### Survivor order statistics

The 64-bucket and rank-exposure lemmas suggest a min-plus transducer, but PR #34 also proves infinite sections for one padding isometry. This is a useful correction: bounded-state closure must be demonstrated for the **actual augmented bucket/carry map**, not inferred from triangularity.

## 3. PR #3 and PR #33 — the main constructive branch is now an exact stitch problem

### New native reductions

PR #3 proves a universal canonical cap bound for finite connector chains and then shows that the free quotient in every ordinary corrected-stage trajectory obeys

```text
0<=Y_(m+1)<(Y_m+3)/512.
```

Hence the quotient reaches zero and every late ordinary trajectory must satisfy

```text
S_m(w_m)=R_(m+1)(w_(m+1)).
```

PR #33 independently compresses the same frontier, proves cap-chain height collapse, and shows that a surviving correction uses asymptotically less than one part in 275 of its complete cylinder precision.

These are major reductions. The remaining object is no longer a free growing residual; it is a sequence of exact equalities among finitely computed stage corrections.

### Highest-value literature route

For each fixed ordered stage-word pair `(w,w')`, expand the equality into a canonical finite sum of rational multiples of powers of `2` and `3`.

If the coefficients and number of terms stabilize with scale, the equation lies in a finite-rank multiplicative group. Evertse–Schlickewei–Schmidt then gives finiteness of nondegenerate solutions. Because the word alphabet is finite, an infinite stitch sequence repeats an ordered pair infinitely often.

A complete proof therefore has four native obligations:

1. derive one fixed finite-term equation for every ordered pair;
2. prove distinct scales give distinct group solutions;
3. classify every proper-subsum degeneracy;
4. show repeated pairs force the same normalized equation.

This route is recorded in `fixed-word-s-unit-stitching.md`. It is currently conditional but considerably more concrete than a generic appeal to “linear forms in logarithms.”

### Additional route

If a proper-subsum audit reduces one pair to a two-term near-equality, the explicit p-adic logarithmic-form results of Bugeaud or Chim become relevant. The exact algebraic bases and exponents must be written before any theorem is quoted.

## 4. PR #16 — real full-shift closure sharpens the Dubickas target

PR #16 now proves:

```text
ordinary survivor
 <=>
 exists xi>0 with ||xi(81/64)^n||<=1/81 for all n,
```

and also proves that every binary itinerary has one bounded real error path. Therefore a real interval graph by itself cannot eliminate itineraries: the real scheduled language is a full shift.

The arithmetic lies in the appended nearest-integer blocks

```text
R_(K+1)=R_K+q_K 64^K,
```

with ordinary stabilization equivalent to `q_K=0` eventually.

### Correct literature task

The next source task remains to obtain Dubickas's full 2006 and 2008 formulas and specialize them at `(81,64)` and radius `1/81`. The specialization should include the extremal Thue–Morse sign pattern and translate it into the native `q_K` recurrence.

A lower bound exceeding `1/81` would close the ordinary section. Equality would isolate the exact critical language. A weaker lower bound would quantify the native deficit.

The full-shift theorem means that any external result stated only as real-cylinder nonemptiness is insufficient; nearest-integer arithmetic must remain visible.

## 5. PR #19 — monotone H minimum and two-place arithmetic

The newest H iteration decomposes the ghost closure into centered valuation rooms around the fixed ghost `4` and defines the monotone minimum

```text
nu_K
 =min{P>=16 : P=1 mod 3 and P mod 2^K lies in the ghost residue set}.
```

Termination of the H subsystem is equivalent to

```text
nu_K -> infinity.
```

This is the same high-quality ordinary-section reduction as PR #16's minimum sequence, adapted to a different subsystem.

### Literature split

The H frontier naturally separates into:

1. a critical near-Pillai/two-term regime, for explicit p-adic logarithmic forms;
2. a nondegenerate finite-term regime, for S-unit finiteness;
3. a subcritical regime, for a transformed-height finite trap.

The exact room coordinate

```text
P=4+4^(q+1)z
```

should be inserted into the first-nonzero branch before choosing the external theorem. This may reduce the number of algebraic bases and make source constants tractable.

Finite growth such as the current exact checkpoint for `nu_K` is useful but not asymptotic proof.

## 6. PR #32 — review status is now a stable input

PR #32 independently reconstructed the complete all-depth weighted-EQ chain through `ADEL/T-9312`, with independent code and no fatal inference found.

The appropriate next use is downstream:

- integrate the review status into the native ledger;
- audit every claimed finite-survivor consequence;
- keep the exceptional ordinary point separate;
- focus ordinary-section work on the centered block/minimum formulations.

Further Fourier expansion is lower priority than exploiting the reviewed theorem.

## 7. Issue #21 / Foundry

The earlier finite-state and standard one-counter feedback collapse remains valid strategically. The latest PR #34 finite-section results sharpen the machine boundary:

```text
finite synchronous realization
 <=>
 finitely many rooted-tree sections.
```

A positive Foundry class should therefore expose either:

- a finite augmented section set despite unbounded arithmetic state; or
- a stronger machine model with digit/residue access, genuine stack memory, or multiple counters.

Merely proving triangularity or causal computability is not a finite-state theorem.

## 8. Cross-program synthesis

The repository now has several exact equivalents of ordinary realization:

```text
PR #20: rationality of an explicit p-adic q-series value;
PR #16: eventual zero nearest-integer blocks / bounded minimum;
PR #19: bounded centered ghost minimum;
PR #3/#33: eventual exact cap-to-correction stitches;
Foundry: eventually zero digits of one causal fixed point.
```

The literature tools align by structural class:

```text
fixed periodic q-series vector
 -> p-adic linear independence;

fixed finite-term power equation
 -> S-unit finiteness / p-adic logarithmic forms;

finite p-adic map
 -> rooted-tree sections / van der Put;

growing S-adic family
 -> period-uniform Padé/height estimates;

one ordinary point
 -> stabilization or nonstabilization theorem plus exact initialization.
```

This prevents one theorem from being stretched beyond its quantifiers.

## Priority order after the attached-paper audit

1. Add and independently reconstruct the Väänänen–Wallisser period-nine corollary in PR #20.
2. Derive fixed-word S-unit normal forms for PR #3/PR #33 cap stitches.
3. Retarget PR #34 Padé work to period ten and period-uniform estimates.
4. Obtain and specialize Dubickas's exact `(81,64)` constants and extremal word.
5. Reduce the H critical regime to one explicit two-term logarithmic form and the successive-core regime to a proper-subsum-audited S-unit equation.
6. Independently review PR #3 `L-0030/T-0031`, PR #33 `T-9703/T-9704`, PR #16 `T-9315/L-9314`, and PR #19 `L-9516/T-9510`.
7. Integrate PR #32's verified status before extending the EQ theory.

## Status boundary

No native claim is promoted by this review. The Väänänen–Wallisser corollary is supplied as an imported theorem with a complete native reduction, but the native PR #20 ledger still requires independent reconstruction before status change.

No source or repository claim in this wave constructs a positive ordinary Collatz counterexample or resolves the conjecture.

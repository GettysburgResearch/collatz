# Live repository review — literature audit wave 4

**Agent:** `gpt56-pro-03`  
**Issue:** `#7`  
**Snapshot:** 2026-07-22, after PR #20's Padé irrationality results, PR #3's Montgomery/compiler chain, PR #16's centered-power equivalence, PR #32's adversarial reconstruction, PR #33's finite-trap theorem, and PR #34's overnight cross-direction lemma wave  
**Status:** literature and applicability audit; no native claim is promoted by this file

## Executive assessment

The repository has crossed from a collection of structural obstructions into several **decisive model-family theorems**:

1. PR #20 excludes all eventually periodic stack directives of period at most three by proving irrationality of their exact selected 2-adic values.
2. PR #32 independently reconstructs the complete all-depth weighted-EQ proof chain.
3. PR #33 proves nonstabilization for every directive in a frozen one-counter affine family.
4. PR #3 now has exact finite connector compilation, Montgomery residual coordinates, an adaptive finite-scale counter chart, and an ordinary quadratic bulk generator.
5. PR #16 converts the remaining ordinary-section problem into an exact centered rational-power orbit at radius `1/81`.
6. PR #34 supplies a large collection of exact finite-state, Padé-residual, Hall-allocation, and survivor-order-statistic lemmas.

The literature now does more than classify novelty. It supplies three plausible shortcuts:

```text
periodic Padé values  -> p-adic Tschakaloff linear independence;
centered survivor     -> rational-power nearest-integer/two-interval theorems;
finite arithmetic map -> rooted-tree sections / van der Put / symbolic embedding.
```

## 1. PR #20 — from short periods to a possible all-period theorem

### Native breakthrough

The scalar q-binomial Padé construction crosses the exact rational-target threshold. Its block extension proves irrationality for every periodic increment word of length at most three and every finite prefix of such a tail. Period four misses only by a small exponent deficit.

### Exact literature reduction

Every fixed period is a finite vector of the p-adic Tschakaloff function

```text
f_R(z)=sum_(N>=0)R^(N(N-1)/2)z^N
```

at rational points in distinct `R`-orbits. `LIT-KTHM-0034` gives the complete reduction.

Väänänen--Wallisser (1991) studies linear-independence measures for this exact p-adic function in the exact regime `0<|R|_2<1`. The full theorem statement was not available in the inspected source. It is therefore the top acquisition target rather than a claimed solution.

### If the 1991 theorem applies

Linear independence of `1` and the phase vector would exclude every nontrivial rational linear combination and could close **all fixed periods in one step**, including arbitrary finite prefixes through the existing transfer identity.

### If it does not apply

The period-four deficit is small enough that three established techniques are immediately relevant:

1. determinant nonvanishing for q-functional equations (Matala-aho 2002);
2. cyclotomic factors of Hankel/Padé determinants (Krattenthaler--Rochev--Väänänen--Zudilin 2009);
3. Bombieri--Vaaler improvement through the gcd of all maximal symbolic minors (Matala-aho--Seppälä 2018).

The next computation must factor the **symbolic maximal minors before evaluation**, not only search for gcds of evaluated numerators and denominators. A saving greater than the exact period-four deficit suffices.

### Route to the true balanced directive

The correct ladder is:

```text
all fixed periods with a measure uniform in the word
 -> adjacent standard-word periodic approximants
 -> exact transfer comparison to the S-adic limit
 -> rational-target exclusion for the balanced 17/18 directive.
```

A qualitative theorem for each fixed period is not enough; the constants must be controlled as the period grows.

## 2. PR #16 — the ordinary section is a centered rational-power problem

`ADEL/T-9315` gives the exact equivalence

```text
nontrivial ordinary survivor
 <=>
exists xi>0 with ||xi*(81/64)^n||<=1/81 for every n.
```

This is a literal archimedean rational-power problem, not only a 2-adic analogy.

### Standard width theorem is insufficient

A lower bound on the ordinary interval width of the fractional parts does not exclude a wrapped union of two arcs. The target has circular length `2/81` but may have ordinary interval diameter close to one.

### Two high-leverage source checks

1. Dubickas (2006) gives explicit large-limit constants for `||xi(p/q)^n||`. Compute the constant for `(81,64)`. A value greater than `1/81` closes the ordinary section immediately.
2. Dubickas (2008) proves noncontainment in certain unions of two intervals. Translate the exact centered arcs into that coding and specialize every inequality.

Neither specialization has yet been completed.

### Native finite-state reduction

`LIT-KTHM-0041` converts the target into a finite carry alphabet `{-1,0,1}` with a sign-dependent interval transition. Build its exact sign/carry graph and intersect interval images. This can either prove emptiness finitely or isolate the exact critical symbolic language to which the Dubickas/Thue--Morse argument must be adapted.

## 3. PR #3 — normalize before synthesizing the final router

### Formal-group simplification

The ordinary quadratic bulk is multiplication by two in the formal multiplicative group. The recurrence

```text
V_(m+1)=V_m+2^(m+1)V_m^2
```

is simply the coordinate form of

```text
Y_(m+1)=Y_m^2,
Y_m=3^(7*2^m).
```

The analysis coordinate `log_2 Y_m` doubles linearly. This should reduce the physical bulk gadget to one fixed squaring/doubling compiler plus filtration bookkeeping.

### Finite-state compressibility has an exact criterion

The padding counter and correction maps are 2-adic isometries. Their exact finite-state complexity is the number of distinct rooted-tree sections; Anashin supplies the van der Put coefficient criterion. The next task is to compute the actual section orbit, not merely prove triangularity or bijectivity.

### Symbolic embedding remains conditional

Krieger/MacDonald can replace a hand-built huge substitution only after the normalized legal stage relation is a stationary mixing SFT, the demand process has lower entropy, periodic-point inequalities hold, and the visible arithmetic output is preserved. The current scale-dependent counter stack is not yet in that form.

### q/Mahler cocycle target

The full Montgomery stage map has scale doubling. Derive an exact recurrence for the normalized offset cocycle. Finite-dimensional closure would turn the stage zipper into a Mahler-type affine system; failure would expose the precise additional memory.

## 4. Foundry — standard one-counter feedback also collapses

Finite-state Foundry operators already have ultimately periodic autonomous zero-input tails. `LIT-KTHM-0036` extends the same conclusion to the standard deterministic one-counter model with only zero/nonzero testing and unit counter changes.

Therefore the next positive machine class should not be a plain one-counter automaton. It must have at least one stronger feature:

- digit or residue access to the counter;
- scale-dependent transitions;
- a genuine pushdown alphabet;
- two counters;
- or another source of unbounded nonperiodic autonomous output.

This helps distinguish Foundry from PR #3: the padding-address counter reads unbounded low-bit information and is not a standard one-counter device.

## 5. PR #33 — from common contraction to path-complete potentials

The direct finite-trap theorem succeeds for a frozen contracting family. Expansion-positive systems require state-dependent potentials rather than one common absolute radius.

`LIT-KTHM-0040` supplies the next proof object:

```text
V_j(alpha_e z+beta_e)<=V_i(z)-delta
```

outside a finite trap, with rational state-dependent affine or piecewise-linear potentials.

Search order:

```text
common trap
 -> state-dependent affine potential
 -> path-complete piecewise-linear potential
 -> occupation-measure/cycle dual
 -> exact congruence refinement.
```

A failed Lyapunov search should return an exact rational cycle or edge flow, not only solver failure.

## 6. PR #34 — several abstract lemmas have canonical external machinery

### Rooted-tree sections

The abstract part of `L-9863/L-9867` is known automaton-group infrastructure: finite-state tree automorphisms are exactly those with finitely many sections. The native contribution is the exact LSF normalization and application to collision/residual maps.

### Fractional Hall allocation

`L-9866` solves the static fractional problem. If the decoder measure is atomless, Dvoretzky--Wald--Wolfowitz purification can produce a deterministic measurable selector preserving the finite residue loads exactly. This removes static randomization but not orbit-time, integer, or cross-modulus coherence.

### q-Lucas/Cartier renormalization

`L-9862/L-9864` show powers-of-two channel refinement and an exact four-step q-Pascal operator. Characteristic-two Frobenius and q-Lucas congruences suggest an all-`2^a` block operator with Cartier extraction of coefficient classes. The missing invariant is endpoint-state cancellation, not local branch filtration.

### Survivor minima as a min-plus section machine

`L-9865` reduces each width lift to bucket-local heads and tails. If the bucket/carry map has finitely many sections, these order statistics can be carried by a finite min-plus weighted automaton. If not, the first new section identifies the missing state coordinate.

## 7. PR #32 — all-depth EQ now has an independent reconstruction

The adversarial reviewer independently reconstructed

```text
L-9309 -> T-9307 -> T-9308
L-9310 -> T-9311 -> T-9312
```

with independent code and no fatal gap. The literature suite should record the exact reviewed commit as `INDEPENDENTLY RECONSTRUCTED / integration pending`, while the native ledger performs any formal status promotion.

This makes the next EQ-related task downstream:

1. verify the translation from weighted EQ to every claimed finite-survivor consequence;
2. preserve the separation from the exceptional ordinary point;
3. focus ordinary-section work on `T-9315`.

## 8. Cross-program synthesis

Four formerly separate frontiers now share a common finite-state-versus-arithmetic split:

```text
symbolic/analytic layer:
  Tschakaloff vectors, q-functional equations, rooted-tree sections,
  SFT embeddings, Hall allocations, Lyapunov potentials;

ordinary arithmetic layer:
  reduced height, exact low-bit routing, one finite initialization,
  positivity, and stabilization/nonstabilization.
```

The literature can now plausibly close the first layer for several programs. It does not automatically cross the second.

## Priority order

1. Obtain and inspect the full Väänänen--Wallisser 1991 theorem.
2. Compute Dubickas's `(81,64)` nearest-integer constant.
3. Build symbolic maximal-minor factorizations for PR #20 period four.
4. Construct the exact sign/carry interval graph for `T-9315`.
5. Compute section orbits/van der Put coefficients for the actual PR #3 and PR #34 isometries.
6. Prove atomlessness and apply static purification to `L-9866`, if possible.
7. Derive the all-dyadic q-Lucas/Cartier block operator.
8. Integrate PR #32's review status and audit the downstream EQ consequences.

No located theorem constructs a positive ordinary Collatz counterexample, and no statement in this review resolves the conjecture.
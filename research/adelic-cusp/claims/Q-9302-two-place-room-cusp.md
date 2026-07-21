# Q-9302 — Two-place and room mechanisms after all-depth EQ

**Claim ID:** Q-9302  
**Title:** Can the room/adelic representation help resolve the remaining ordinary-integer section or sharpen the all-depth theorem?  
**Status:** IDEA  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `D-9302`, `T-9304`, `L-9306`--`L-9310`, `T-9305`--`T-9312`; issue-#4 room crosswalk  
**Scope:** post-EQ ordinary-section, sharper-rate, and proof-mechanism frontier  
**Related counterexample candidates:** none

## 1. Exact split equivalence already proved

For a split

\[
K=n+j,
\qquad
Q=64^n81^j,
\]

put

\[
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j}.
\]

The normalized CRT coefficient is

\[
G_{n,j}(h)
=
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j).
\]

`L-9307` and `L-9308` prove that these are the two local components of one rational character and that the factors stitch one reciprocal phase chain.

`T-9305` and `T-9306` give, for every bounded harmonic test and every `H`,

\[
\left|
\sum_{h\le H}\frac{w_h}{h}G_{n,j}(h)
-
\sum_{h\le H}\frac{w_h}{h}
\widehat\mu(h/64^K)
\right|
<
\frac{2\pi H}{64^K}.
\tag{1}
\]

Thus a two-place Fourier proof in every sub-`64^K` range proves the original one-place statement simultaneously.

## 2. Weighted EQ is no longer the open target

`L-9310` discovers the integral signed-phase carry

\[
a_\ell=64x_\ell-81x_{\ell+1}\in\mathbb Z.
\]

Its completion-height rigidity gives `T-9311`, uniform pointwise decay on every subexponential numerator window. Together with the uniform entropy tail `T-9308`, this gives `T-9312`:

\[
\sum_{1\le h\le2^K}
\frac{|S_K(h)|}{2^Kh}
\longrightarrow0
\]

at every depth.

Accordingly, this open question is no longer “can the two-place representation prove weighted EQ?” The packet already proposes such a proof without requiring room-tower closure.

## 3. Reframed research question

Can the fixed product measure, rational diagonal, room-wrap coding, and completion-height carries provide one of the following genuinely new outputs?

1. an ordinary-integer nonintersection theorem for `D-9302`;
2. a constructive nontrivial integer-section point, which would require immediate adversarial verification;
3. substantially sharper pointwise or harmonic rates than the tiny exponent in `T-9311`;
4. a general theorem for other `M -> N` collision-fiber rungs;
5. a structural bridge between PR #20's output factor complexity and the arithmetic carries of `L-9310`.

## 4. Most promising route: complexity–carry incompatibility

PR #20 and `L-9310` independently produce the same criticality constant

\[
\kappa
=
\frac1{\log_{64}81-1}.
\]

PR #20 says a hypothetical ordinary survivor code must have output factor-complexity slope at least `kappa`.

`L-9310` says prolonged zero-carry behavior is bounded by the same `kappa` through completion-height separation.

A decisive theorem should show that one ordinary itinerary cannot simultaneously:

1. introduce fresh output factors at the required rate;
2. satisfy all integral tail recurrences;
3. obey the room and chart congruences;
4. keep the real companion coordinate in its bounded interval;
5. avoid both repeated-factor and zero-carry height contradictions.

This is the proposed **complexity–carry incompatibility theorem**.

## 5. Candidate proof mechanisms

### A. Return-word pressure

Replace exact repeated factors by return words. Freeze a finite state carrying:

- return-word class;
- ordinary tail residue;
- reciprocal carry;
- room-wrap digit;
- terminal `81`-adic residue.

Use a cycle-mean or tilted-transfer certificate only after the state and truncation error are exact. The target is to prove that every infinite path has information/carry cost above the binary budget.

### B. Positive room operator for one itinerary

The finite-set room walk mixes, but an ordinary point defines one deterministic wrap sequence. Construct a positive observable that detects simultaneous recurrence and arithmetic carry cost along that single sequence.

The inverse-limit tower remains real; the goal is no longer to close its marginals for EQ, but to show that one section orbit cannot remain inside the admissible safety kernel.

### C. Adelic shrinking-target rigidity

In `D-9302`, an ordinary point lies on a symbolic stable leaf with zero third coordinate. Under multiplication by `81/64`, the local coordinates expand and contract in opposite directions.

Seek a quantitative theorem saying that an orbit meeting the ordinary section at every shift must generate either a forbidden repetition or an impossible carry-height chain.

Generic measure rigidity is insufficient; the proof must use the shared symbolic itinerary.

### D. General `M -> N` chart theorem

`L-9310` already applies to every coprime expanding pair. Add a digit-mask spectral gap and ordinary-section complexity theorem to obtain a reusable collision-fiber result at every ladder rung.

## 6. What is now ruled out as progress by itself

The following no longer advances the main theorem frontier alone:

- proving another absolute two-place weighted decay estimate equivalent to `T-9312`;
- treating the two local absolute factors as independent;
- using complete-group Parseval to infer short-orbit behavior;
- invoking a fixed-real self-similar theorem without a moving-character bridge;
- closing only a finite room marginal while ignoring the deeper tower;
- citing generic S-unit or measure-rigidity language without constructing its exact hypotheses.

## 7. Dependency audit

- `D-9302` supplies the exact ordinary section.
- `T-9304`, `L-9307`, and `L-9308` supply the stationary two-place rational diagonal.
- `T-9305` and `T-9306` prove split equivalence.
- `L-9310` supplies completion-height carry rigidity.
- `T-9312` changes the research target from EQ closure to the ordinary section.
- PR #20 supplies an independent branch-qualified complexity obstruction; it is not imported as a proved dependency here.
- Every route in this file is open and is not a premise of another theorem.

## 8. Gap audit

- All-depth finite-set EQ does not exclude one exceptional infinite ordinary point.
- High output complexity alone does not contradict ordinary realization.
- Carry energy for frequency characters is not yet a theorem about the digit itinerary of one ordinary survivor.
- A finite-state pressure proof must control state growth and truncation uniformly.
- A constructive section point could be a `2`-adic ghost unless ordinary integrality and the chart translation are proved exactly.

## 9. Suggested next attack

Build the smallest exact return-word/carry state that simultaneously sees:

\[
(A_k\bmod64^L,
\text{return word},
\text{room word},
\text{reciprocal carry template}).
\]

Then seek a finite cycle-mean certificate showing that every cycle either:

1. violates the PR #20 repetition-height bound;
2. violates `L-9310`'s completion-height bound;
3. leaves the ordinary-section safety kernel.

That would convert the shared criticality constant into a direct M1 obstruction.
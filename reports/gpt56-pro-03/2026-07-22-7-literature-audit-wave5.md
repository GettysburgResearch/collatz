# Agent report — literature audit wave 5

```text
Agent: gpt56-pro-03
Issue: #7
Branch: agent/gpt56-pro-03/4-literature-audit
Date: 2026-07-22
```

## Starting point

The repository owner supplied the complete Väänänen–Wallisser 1991 paper that wave 4 had identified as the highest-priority acquisition. At the same time, several agents finished long-running theorem waves that had begun before the wave-4 comments were available.

The task was therefore twofold:

1. decide the exact applicability of the attached theorem;
2. re-read the newly pushed mathematics and attach the most useful external machinery to its current, much narrower interfaces.

## Repository snapshot reviewed

- PR #20 through the unequal-allocation optimality theorem and period-four method closure;
- PR #34 through the period-four quotient packet and waves eight, nine, and ten;
- PR #3 through the canonical cap bound and stage-quotient extinction;
- PR #33 through quotient exhaustion and cap-chain height collapse;
- PR #16 through centered rational powers, real full-shift closure, and appended block recurrence;
- PR #19 through centered ghost rooms and the monotone H ordinary-section minimum;
- PR #32's independent reconstruction of the all-depth EQ chain;
- issue #21's finite-state/one-counter collapse boundary.

## Main result: Väänänen–Wallisser applies through period nine

The source theorem treats

```text
f_q(z)=sum_(n>=0) q^(n(n-1)/2)z^n
```

and gives a quantitative linear-independence measure for values at rational points in distinct multiplicative `q^Z`-orbits.

PR #20's exact periodic decomposition has precisely this form. For a minimal period `r`, the evaluation points are

```text
Z, Zlambda, ..., Zlambda^(r-1),
R=lambda^r,
```

and are in distinct `R^Z`-orbits.

At `p=2`, the source parameter is

```text
1-log(64)/log(81),
```

independent of the period word. Exact integer inequalities show that the source condition holds for dimension nine and fails at dimension ten.

Therefore every eventually periodic positive increment directive of minimal eventual period at most nine has irrational selected `2`-adic context.

Added:

- `LIT-KTHM-0042`;
- `period-nine-tschakaloff-closure.md`;
- a detailed comment on PR #20.

## Strategic consequence for PR #20 and PR #34

The first fixed period not covered by the source theorem is period ten. The extensive period-four work remains valuable as a self-contained method and exact regression suite, but the highest-value target is now:

```text
period ten
or
uniform-in-period estimates for standard-word limits.
```

A retargeting comment was posted on PR #34.

## New cap-stitch route

PR #3 and PR #33 now prove that the free corrected-stage quotient eventually vanishes. The late ordinary problem is exactly

```text
S_m(w_m)=R_(m+1)(w_(m+1)).
```

The stage alphabet is finite and the corrections occupy an exponentially shrinking fraction of the full cylinder.

The proposed external route is to expand each fixed ordered word pair into a fixed finite equation in powers of `2` and `3`, audit proper subsums, and apply Evertse–Schlickewei–Schmidt to the nondegenerate solutions.

Added:

- `LIT-KTHM-0043`;
- `fixed-word-s-unit-stitching.md`.

This is not yet an application. The native branch must prove coefficient stability, finite-rank membership, distinct scale solutions, and all degeneracies.

## H two-place route

The newest H work supplies:

- centered rooms around the fixed ghost `4`;
- a monotone minimum `nu_K` whose divergence is equivalent to termination;
- an exact successive-core equation carrying both `2`-adic and `3`-adic information.

The literature split is now precise:

- nondegenerate multi-term persistent-prime equations: S-unit finiteness;
- critical two-term near-equalities: explicit p-adic logarithmic forms;
- subcritical transformed heights: finite-trap methods.

Added:

- `h-two-place-logarithmic-forms.md`;
- source-ledger entries for Evertse–Schlickewei–Schmidt, Chim, and Bugeaud.

## Centered rational-power route

PR #16's real error system is a full shift, so real interval propagation alone cannot exclude itineraries. The arithmetic object is the appended nearest-integer block, which must eventually vanish for an ordinary point.

The correct source task is to specialize Dubickas's explicit nearest-integer and two-interval results to `(81,64)` and translate the extremal Thue–Morse word into the native block recurrence.

Added:

- `centered-power-arithmetic-blocks.md`.

The full formulas are still unavailable, so the specialization remains `UNVERIFIED — HIGH PRIORITY`.

## Suite additions

Wave 5 adds:

- imported theorems `LIT-KTHM-0042` and `LIT-KTHM-0043`;
- `LIVE_REPO_REVIEW_WAVE5.md`;
- `SOURCE_LEDGER_WAVE5.md`;
- `references-wave5.bib`;
- `claim-maps/WAVE5.md`;
- `UNVERIFIED-WAVE5.md`;
- four topic notes;
- `check_literature_wave5.py`;
- this report.

## Mathematical assessment

The overnight work materially improves the project because several branches now prove model-family exclusion or exact ordinary-section equivalences rather than only finite compatibility.

The highest-value developments are:

1. external closure of periodic stack tails through period nine;
2. independent reconstruction of all-depth weighted EQ;
3. strict extinction of the corrected-stage free quotient;
4. exact monotone-minimum equivalences in two separate subsystems;
5. a finite-alphabet cap-stitch equation with a very large completion-height gap.

The central risk remains the same: exact finite or `2`-adic compatibility is not an ordinary positive initialization. No current branch has crossed that boundary.

## Validation status

The wave-5 checker validates file presence, imported IDs, bibliography-key uniqueness, stale citation markers, and load-bearing theorem markers.

Run:

```bash
python3 literature/check_literature.py
python3 literature/check_literature_wave2.py
python3 literature/check_literature_wave3.py
python3 literature/check_literature_wave4.py
python3 literature/check_literature_wave5.py
```

The GitHub connector does not execute repository code, so this report does not claim that the commands were run remotely.

## Recommended next actions

1. Independently reconstruct `LIT-KTHM-0042` against PR #20 and add the source-dependent native corollary.
2. Symbolically expand fixed PR #3/PR #33 stitch pairs and test coefficient stability across scales.
3. Rebase PR #34's Padé benchmarks around period ten and period-uniformity.
4. Obtain the full Dubickas formulas and compute the exact `(81,64)` constants.
5. Freeze one H critical two-term form and one successive-core S-unit form with full parameter tables.
6. Independently review the newest cap, centered-power, and H-minimum chains before further extension.

## Candidate counterexamples

None proposed or promoted.

## Potential errors / unresolved doubts

- The PR #20 periodic decomposition still needs independent reconstruction against the source notation.
- The fixed-word cap-stitch S-unit normal form has not yet been derived.
- Fresh prime support may prevent direct S-unit treatment of the H equation.
- Dubickas's exact constants have not been evaluated.
- The latest long PR #34 packet has same-session audits but no repository-independent review as a whole.
- No ordinary positive Collatz counterexample or full resolution is claimed.

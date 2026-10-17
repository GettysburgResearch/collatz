# Session report — signed phase shadows and the rational-base frontier

Agent: `gpt56-drift-01`  
Issue: #26  
Branch: `agent/gpt56-drift-01/26-5x1-portability`  
Date: 2026-07-22

## Starting hypothesis

A finite connector family between phases `-2` and `-1` might replenish enough
precision to turn the exact `4 -> 5` amplifier into one positive ordinary
infinite orbit.

## Approaches attempted

1. Derived the exact map of a full dyadic cylinder from the signed orbit of its
   residue phase.
2. Classified the complete signed phase graph on `{-2,-1}`.
3. Computed the odd-step balance of arbitrary connector segments and closed
   circuits.
4. Shifted the physical chart by `A -> A+1` and `A -> A+2` to search for a
   simpler integer recurrence.
5. Identified the exact base-`5/4` representation-tree edge relation.
6. Recast the positive survivor question as a bottom-word digit-avoidance
   problem.
7. Computed the exact `2`-adic cylinder geometry of all binary completions.
8. Built a dependency-free experiment for finite interface checks and a bounded
   root census.
9. Located rational-base subtree and bottom-word literature as a methodological
   neighbor; no external theorem was imported into a claim.

## New results

### Proposed theorem-level results

- `L-8803`: every dyadic shortcut cylinder is a lift of one signed phase orbit.
- `T-8804`: positive cycles are subcritical; negative cycles are supercritical.
- `T-8805`: the two-phase connector imbalance is an exact coboundary and
  vanishes on closed circuits.
- `T-8806`: positive chart survivors are exactly base-`5/4` bottom paths using
  only digits `0,1`; any such survivor diverges.
- `T-8807`: the full `2`-adic completion set has Haar measure zero and Hausdorff
  dimension `1/2`; its positive ordinary section has density zero.

### Refutation

- `R-8801`: phase-switch scheduling alone cannot create an additional
  asymptotic odd-step surplus. The one-way gain is a telescoping boundary term.

### Exact finite observations

X-8802:

- replays all two-phase connector lengths through `20` on quotient samples
  through `1000`;
- reconstructs signed cycles through parity-word length `18`;
- checks the physical/rational-base conjugacy for all `A<=10^6`;
- finds maximum bounded survival depth `19`, at `A=786766`.

## Candidate counterexamples

None. No positive infinite low-digit path was found or claimed.

## Failed approaches

The coarse connector strategy whose only state was the phase label failed. The
phase graph is deterministic and alternating, and its putative gain telescopes.
This does not refute refined quotient/carry automata.

## Potential errors

1. T-8806 must be reviewed for orientation of the rational-base edge equation
   and for the distinction between the bottom edge and an arbitrary child.
2. T-8807's lower Hausdorff-dimension estimate should be independently rebuilt
   for arbitrary `2`-adic ball radii.
3. The signed-cycle census is bounded and must never be cited as a uniqueness
   theorem.
4. External rational-base results require exact hypothesis audits before use.

## Files changed

- five new theorem/lemma files;
- one formal refutation;
- `RATIONAL_BASE_FRONTIER.md`;
- experiment X-8802 with canonical output;
- this append-only report;
- updated packet README.

## Claims affected

```text
L-8803,
T-8804,
T-8805,
T-8806,
T-8807,
R-8801,
X-8802.
```

## Recommended next actions

1. Independently reconstruct T-8806 and T-8807.
2. Implement a finite-state/PDR search for eventual escape of the bottom map
   `tau(x)=ceil(5x/4)` from digit set `{0,1}`.
3. Audit the rational-base successor transducer and test whether it yields a
   forbidden-pattern propagation theorem.
4. Search for additional negative signed cycles that generate richer expanding
   control charts.
5. Attempt a Diophantine upper bound for low-digit prefix length versus root
   height.

## Organizational improvement ideas

Add a **signed phase-shadow field** to every exact collision or connector claim:

```text
SIGNED PHASE START:
SIGNED PHASE END:
SIGNED PHASE ORBIT:
CYCLE SIGN / MULTIPLIER SIGN:
STATE BEYOND PHASE:
```

This exposes when a purported connector family has genuine state freedom and
when it is only a resegmentation of one signed orbit.

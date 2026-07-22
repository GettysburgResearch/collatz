# Claim map — literature audit wave 5

All references are branch-qualified. Verdicts in this file do not promote native statuses.

## PR #20 (`PADIC/...`)

| Native claim / frontier | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `L-9408`, `L-9410` periodic phase decomposition | NATIVE EXACT REDUCTION | `LIT-KTHM-0034` and `LIT-KTHM-0042` | Independent reconstruction of the decomposition and coefficient normalization |
| `T-9412`–`T-9415` periods at most three | NATIVE SELF-CONTAINED, externally subsumed in range | Väänänen–Wallisser Theorem 1 closes every minimal period at most nine | Keep as source-independent proofs and regression models |
| eventually periodic tails of minimal period `4,...,9` | KNOWN — COROLLARY, native mapping supplied | `LIT-KTHM-0042` | Add a source-dependent native corollary after independent checking |
| period ten | FIRST FIXED PERIOD OUTSIDE THIS SOURCE CONDITION | Väänänen–Wallisser numerical hypothesis fails at `D=10` | New determinant/height theorem; failure of the source condition is not rationality |
| `T-9416` equal phase allocation optimality | NATIVE METHOD-CLOSURE | explains why the current phasewise root product cannot close period four by reallocation | Retarget toward period ten or uniform-in-period bounds |
| balanced `17/18` directive | OPEN NATIVE FRONTIER | fixed-period linear independence is insufficient without constants uniform in the growing period | Period-uniform measure plus adjacent-standard-word transfer |

## PR #3 (`PR3/...`) and PR #33 (`CYL/...`)

| Native claim / frontier | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `PR3/L-0030` canonical cap bound | NATIVE ELEMENTARY | finite odd-affine completion-height interface | Independent proof reconstruction |
| `PR3/T-0031` stage quotient extinction | SERIOUS NATIVE REDUCTION | converts the supercritical stage to eventual exact cap-to-correction stitching | Audit the next-stage modulus, strict quotient bound, and exact finite initialization |
| `CYL/T-9703`, `CYL/T-9704` cap-chain height collapse | NATIVE COMPLETION-HEIGHT THEOREMS | suggests fixed-word S-unit or p-adic-logarithmic nonvanishing | Derive an exact fixed finite-term equation and classify every degeneracy |
| eventual stitch `S_m(w_m)=R_(m+1)(w_(m+1))` | OPEN NATIVE FRONTIER | Evertse–Schlickewei–Schmidt may give finiteness after an S-unit reduction | Expose the terms, finite-rank group, nondegenerate solutions, and repeated-word implication |
| changing stage-word directive | OPEN, NOT COVERED BY FIXED EQUATION | finite alphabet alone does not fix one Diophantine equation | Pigeonhole/repetition argument plus uniform constants, or one global automaton/cocycle theorem |

## PR #16 (`ADEL/...`) and PR #32 review

| Native claim / frontier | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `ADEL/L-9309`–`T-9312` | INDEPENDENTLY RECONSTRUCTED / integration pending | PR #32 supplies independent derivation and replay | Native ledger/review integration and downstream-consequence audit |
| `ADEL/T-9315` centered rational-power equivalence | SERIOUS NATIVE REFORMULATION | `LIT-KTHM-0041`; Dubickas nearest-integer and two-interval results | Independent proof; specialize the external constants to `(81,64)` |
| `ADEL/L-9313` real error full shift | METHOD-CLOSURE | shows real interval propagation alone cannot eliminate itineraries | Arithmetic nearest-integer blocks must remain in every future theorem |
| `ADEL/L-9314` appended nearest-integer block recurrence | OPEN NATIVE FRONTIER | finite carry alphabet and Thue–Morse extremals are the closest external structure | Derive long-zero-block contradiction or evaluate the exact Dubickas bound |
| `M_K -> infinity` / no eventual zero blocks | OPEN FULL ORDINARY-SECTION TARGET | no located theorem yet specializes exactly to the critical radius `1/81` | Explicit source calculation or native block recurrence theorem |

## PR #19 (`H/...`) and PR #34 H bridges

| Native claim / frontier | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `H/L-9516` centered rooms around `4` | NATIVE EXACT GEOMETRY | completion-height normalization around one rational fixed point | Independent boundary and integrality audit |
| `H/T-9510` monotone ordinary-section minimum | NATIVE EXACT REFORMULATION | same fixed-room/minimum architecture as `ADEL/T-9313` | Prove `nu_K -> infinity`; finite checkpoints are not asymptotic proof |
| `H/Q-9504` critical near-Pillai regime | OPEN; DIRECT EXPLICIT TOOL AVAILABLE IN PRINCIPLE | Chim 2025 and Bugeaud 2007 two-term p-adic logarithmic forms | Freeze exact algebraic bases/exponents and verify all hypotheses/constants |
| `SYN/L-9894` successive-core equation | NATIVE EXACT DIOPHANTINE INTERFACE | Evertse–Schlickewei–Schmidt for nondegenerate S-unit equations | Split persistent/fresh prime mass and audit proper subsums |
| H critical/subcritical dichotomy | OPEN NATIVE FRONTIER | combine two-place valuation bounds with the discounted budget | Uniform native reduction; no generic invocation of “Yu” or “S-unit” is enough |

## PR #34 (`SYN/...`) general state machinery

| Native claim / frontier | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `L-9863`, `L-9867` rooted-tree sections | KNOWN ABSTRACT STRUCTURE + NATIVE LSF APPLICATION | `LIT-KTHM-0038`; automaton-group/van der Put framework | Compute sections for the actual maps rather than only prove triangularity |
| `L-9876` infinite sections for padding map | NATIVE NEGATIVE RESULT | rules out a uniformly bounded synchronous transducer for that exact map | Identify the minimal augmenting scale/counter coordinate |
| `L-9862`–`L-9891` period-four Padé machinery | STRONG NATIVE METHOD PACKET | Väänänen–Wallisser removes period four as the first source-unresolved class | Retarget to period ten or a theorem uniform in period length |
| `L-9865`, `L-9892` survivor order statistics | NATIVE FINITE RECURSION / EXPOSURE | potential min-plus section machine | Prove finite augmented sections or identify the first unbounded state variable |
| `L-9866` fractional Hall allocation | KNOWN FINITE FLOW CONVERSE + NATIVE DECODER | Dvoretzky–Wald–Wolfowitz under atomlessness | Static purification still does not give temporal/integer coherence |

## Cross-program verdict

The newest results split the project into three sharply different theorem obligations:

```text
fixed finite symbolic family
 -> often approachable by linear independence, S-units, or finite sections;

growing but structured family
 -> requires estimates uniform in the growing period/scale;

one ordinary infinite trajectory
 -> still requires stabilization/nonstabilization plus exact finite initialization.
```

The attached Väänänen–Wallisser theorem closes a meaningful fixed-family range. It does not remove the need for period-uniform estimates, exact cap-stitch nonvanishing, or ordinary initialization.

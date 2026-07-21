# Direction: Heteroclinic / adelic interpolation

Suggested issue title: `Heteroclinic adelic interpolation between 2-adic cycles and archimedean growth`

```text
Status: IDEA
Proposal class: unclaimed research direction
Suggested claim IDs once work begins: Q-01xx, C-01xx, K-01xx, X-01xx
Authoring agent (handoff only): grok45-01
Claimed by: nobody
Related active work: none — orthogonal to collision-fiber regeneration and AYH tropical templates
```

## One-paragraph pitch

Known nontrivial cycles live in the 2-adic extension and on the negative
integers; ordinary positive orbits cannot be eventually periodic. Construct a
single positive integer whose Collatz itinerary is **archimedean-unbounded**
while remaining arbitrarily close, in the 2-adic metric, to a chosen 2-adic
cycle template along a sparse set of times — a heteroclinic shadow between a
local cycle and global growth.

## Relationship to the counterexample objective

A successful construction is a `K-####` candidate with failure mode
“unbounded / never reaches 1”, certified by (i) an exact local 2-adic
shadowing lemma and (ii) an archimedean growth lower bound along the same
itinerary. This is a divergent-orbit counterexample, not a cycle.

## Background facts to treat carefully

- Periodic parity words reconstruct 2-adic rationals (e.g. `(100)^ω ↦ 1/5`);
  that alone is **not** a positive-integer counterexample.
- Eventual periodicity of least digits is already obstructed for nontrivial
  ordinary induced orbits in the collision-fiber packet (`T-0003` / `N-0001`
  on branch `agent/gpt56-pro-01/...`). Do not fight that theorem; use it.
- Negative integer cycles (`-1`, `-5`, `-17`, …) are supercritical amplifiers
  in the shortcut map. They are scaffolds, not counterexamples.

Label every use of those statements with the actual repository status after
independent review; until then treat them as external/proposed dependencies.

## Proposed construction shape

1. Fix a 2-adic cycle template \(C\) with periodic parity word \(w^\omega\).
2. Choose a sparse sequence of times \(0 = t_0 < t_1 < t_2 < \cdots\) and
   congruence demands
   \[
   n_{t_k} \equiv c\pmod{2^{m_k}},\qquad m_k\to\infty,
   \]
   forcing deeper 2-adic approach to \(C\).
3. Between \(t_k\) and \(t_{k+1}\), insert a **growth block** (supercritical
   finite word or finite concatenation) that multiplies an archimedean height
   by a factor \(\ge 1+\delta\).
4. Solve the resulting CRT / nested-congruence system for one
   \(n\in\mathbb{Z}_{>0}\).
5. Prove the infinite concatenation is realizable by that single \(n\)
   (infinite consistency), not merely by a compatible inverse-limit point.

## Falsification criteria

Abandon or sharply revise the direction if any of the following is proved:

1. **Rigidity:** any itinerary that is 2-adically asymptotic to a cycle
   template is archimedean-bounded on positive integers.
2. **CRT bankruptcy:** the growth blocks destroy the congruence depth
   required for \(m_k\to\infty\), uniformly in the block library.
3. **Fuel accounting:** each forced return near \(C\) consumes more
   2-adic valuation / Terras fuel than the growth blocks can repay
   (compare fuel-conservation heuristics in the symbolic-rewrite packet).
4. **Reduction to periodicity:** every solution of the nested system is
   eventually periodic, hence excluded for ordinary divergent orbits.

## Starter experiments (suggested `X-####`)

```text
X-A: Enumerate short periodic templates; compute their 2-adic points and
     negative/positive rational cycles explicitly.
X-B: For each template, search finite “excursion words” that start and end
     in a deep 2-adic neighborhood of the cycle while increasing log n.
X-C: Measure congruence destruction: if n ≡ c mod 2^m and an excursion of
     length L is applied, what modulus survives?
X-D: Attempt CRT gluing for two excursions; report the maximal reachable
     shadowing depth before positivity fails.
```

Keep exact integer arithmetic. Record failures in `NEGATIVE_RESULTS.md` style
notes inside the issue or a session report.

## Suggested deliverables for a claiming agent

- Issue claim comment with agent ID and branch.
- A definition file for “heteroclinic shadowing of depth \((m_k)\)”.
- At least one computational report (`X-A`–`X-D`) with reproducible scripts.
- Either a `K-####` candidate with a full verification plan, or a labeled
  `R-####` / negative result explaining the obstruction.

## Handoff

```text
HANDOFF FROM: grok45-01
HANDOFF TO: any
CURRENT CLAIM OR CANDIDATE: none (direction only)
BLOCKING STEP: open this as a GitHub Issue and claim it; then run X-A/X-B
FILES TO READ: README.md; directions/README.md; this file;
  research/termination-frontier/README.md (optional); collision-fiber
  NEGATIVE_RESULTS N-0001/N-0004 if/when merged
FAILED ATTEMPTS: none yet in-repo
MOST PROMISING NEXT MOVE: quantify congruence destruction for one concrete
  template (e.g. (100)^ω or the -5 cycle word) under supercritical excursions
MAIN RISK: shadowing depth and archimedean growth may be strictly antagonistic
POSSIBLE ORGANIZATIONAL IMPROVEMENT: keep broad directions in Issues (or
  directions/ when Issues are unavailable); never silently edit root ledgers
```

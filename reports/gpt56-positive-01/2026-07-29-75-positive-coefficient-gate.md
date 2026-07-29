# Session report — positive coefficient-stopping gate

**Agent:** `gpt56-positive-01`  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-01/75-positive-coefficient-gate`  
**Date:** 2026-07-29  
**Model:** GPT-5.6 Pro

## Starting hypothesis

The repository's constructive counterexample programs repeatedly encounter the same quantifier barrier:

```text
for every finite depth there is a compatible ordinary seed
```

does not imply

```text
there is one ordinary seed compatible at every depth.
```

The positive-direction mirror is to assume Collatz is false, take the least ordinary counterexample that must then exist, and exploit its minimality before introducing any symbolic completion. I searched for a route that combines the repository's ordinary-extraction insight with recent descent and parity-prefix literature rather than adding another amplifier, cycle search, or prescribed infinite word.

## Approaches attempted

1. Read the repository operating rules and current open PR/issue map.
2. Reconstructed PR #57's ordinary-extraction boundary: a nested ordinary survivor requires bounded, eventually stable least representatives.
3. Searched repository issues, PRs, and indexed files for coefficient stopping time, paradoxical sequences, the `485/306` descent barrier, Farey windows, and mechanical remainder extremizers. No overlapping lane was found.
4. Audited recent primary sources:
   - Barina's verified range below `2^71`;
   - Ansari's recursively sufficient extension;
   - Rozier--Terracol's coefficient/remainder framework;
   - Angeltveit's 2026 descent theorem;
   - Kramer's July 2026 mechanical-code experiments as non-load-bearing context.
5. Derived the first-crossing Diophantine window for a least counterexample.
6. Located the exact Farey neighbors around `log(2)/log(3)` and proved the first denominator gate.
7. Reconstructed a right-shift remainder order and identified the upper mechanical extremizer.
8. Converted its remainder into an irrational-rotation Birkhoff sum and bounded it with two Denjoy--Koksma blocks.
9. Built and replayed a dependency-free rational checker.
10. Excluded the unique first Farey candidate and derived the sharpened next denominator gate.

## New results

### Proposed: `T-6701` — stronger verified floor

Combining the published `2^71` computation with Ansari's recursively sufficient interval extension gives

```text
N_* = 4*3^44+2
    = 3,939,083,608,734,444,931,526.
```

Every least counterexample must exceed this number. The result remains `PROPOSED` in the repository until an independent agent audits the imported dependencies and their precise composition.

### Proposed: `T-6702` — all-prefix ballot barrier

For a least counterexample, minimality prevents every descent. Angeltveit's Theorem 4.1 therefore forces

```text
485 q_k > 306 k
```

at every shortcut prefix.

### Proposed: `T-6703`--`T-6704` — first Farey gate

If the affine coefficient first falls below one at time `j`, then

```text
0 < log(2)/log(3) - q/j < 4.86e-23.
```

Consecutive convergents isolate one first rational candidate and force

```text
j >= 114,208,327,604.
```

Equality is possible only for

```text
q/j = 72,057,431,991 / 114,208,327,604.
```

### Proposed: `L-6705` — mechanical remainder extremizer

Among first-crossing words of that length and weight, the exact additive Collatz remainder is maximized by the word whose prefix counts are

```text
ceil(k log(2)/log(3)),
```

followed by the required final even step. The proof is an explicit adjacent swap: moving `10` to `01` increases the final affine remainder.

### Proposed: `T-6706` — exclusion of the unique first candidate

The maximal remainder is a Birkhoff sum of a circle function of integral `1/(3 log(3))` and variation `4/3`. Since the candidate denominator is the sum of two consecutive convergent denominators, two Denjoy--Koksma blocks give

```text
remainder < 17,326,149,966.768241...
```

while no descent above `N_*` requires

```text
remainder > 21,707,856,845.723104...
```

The exact contradiction margin exceeds `4.381e9`.

### Proposed: `T-6707` — sharpened dichotomy

After excluding that candidate and separating the adjacent Farey cells, any least counterexample satisfies

```text
coefficient stopping time = infinity
```

or

```text
coefficient stopping time >= 217,976,794,617.
```

This is the session's headline reduction. It is not a proof of Collatz.

### Exact: `X-6701`

A dependency-free `fractions.Fraction` checker certifies:

- rational logarithm enclosures;
- the continued-fraction prefix;
- Farey determinant identities and interval ordering;
- the candidate coefficient gap;
- the positive exclusion margin;
- all first- and second-gate denominators.

## Candidate counterexamples

None.

This session deliberately attacked the positive conjecture. It assumes a least counterexample only to derive necessary conditions and a contradiction for one exhaustive first-crossing class.

## Failed approaches

1. **Verification floor alone.** It gives the microscopic rational window but does not exclude the first mediant; the coefficient gap times `N_*` and a crude geometric remainder bound are of comparable size.
2. **Coefficient density alone.** The inequality `q_k/k >= log(2)/log(3)` permits many nonordinary infinite words and does not address ordinary extraction.
3. **Denjoy--Koksma for the next convergent.** The current floor and the generic variation error do not immediately exclude the next candidate denominator. Stronger prefix restrictions are needed.
4. **The `485/306` ballot inequality alone.** Its asymptotic density threshold is weaker than coefficient-supercriticality, though its finite-prefix shape may still reduce the mechanical remainder.
5. **Latest experiments as proof.** Kramer's mechanical-code searches are suggestive but were kept contextual; no empirical candidate or scaling trend was promoted into the argument.

## Potential errors and review risks

1. The composition of Barina and Ansari must be reconstructed independently from the primary text.
2. Denjoy--Koksma is imported rather than proved in-repository.
3. The circular variation `4/3`, endpoint convention in the mechanical word, and two-block starting points deserve adversarial checking.
4. The exact checker certifies arithmetic only; it cannot certify the combinatorial and analytic lemmas.
5. No external novelty claim has been established.
6. During publication, the connector initially interpreted an unsupported `branch_name` alias as the default branch. The three exact commits were immediately moved to the intended agent branch and `main` was restored to its prior head before any PR was opened. Future connector writes should use the documented `branch` field explicitly.

## Files changed

1. `research/positive-coefficient-gate/README.md`
2. `research/positive-coefficient-gate/PROOF.md`
3. `experiments/X-6701-farey-gate/run.py`
4. `experiments/X-6701-farey-gate/README.md`
5. `reports/gpt56-positive-01/2026-07-29-75-positive-coefficient-gate.md`

## Claims affected

```text
D-6701
T-6701
T-6702
T-6703
T-6704
L-6705
T-6706
T-6707
X-6701
Q-6701
Q-6702
```

No existing claim status was modified.

## Recommended next actions

### Critical path A — eliminate the uniform-supercritical ordinary survivor

For each depth, construct the finite union of parity residue cylinders satisfying simultaneously:

- coefficient supercriticality at every prefix;
- no descent below the start;
- the `485/306` ballot condition;
- sound path-merging and preimage exclusions.

Track the least ordinary representative of the union. By the repository's ordinary-extraction theorem, proving that this least representative diverges excludes the entire infinite lane.

### Critical path B — iterate the delayed-crossing exclusion

Use Ostrowski decompositions into convergent-denominator blocks to bound each later mechanical remainder. The needed advance is a loss beyond generic Denjoy--Koksma, obtained from the ballot condition or intermediate no-descent inequalities.

### Independent verification packet

A verifier should reconstruct, in order:

1. the published verification floor;
2. the first-crossing window;
3. the Farey isolation;
4. the adjacent-swap extremizer;
5. the rotation formula and variation;
6. the two-block Denjoy--Koksma bound;
7. the exact checker output and second Farey gate.

## Organizational improvement ideas

1. Add a visible **positive-conjecture funnel** alongside the counterexample and cycle funnels:
   ```text
   least counterexample
    -> no descent + verified floor
    -> constrained parity cylinders
    -> coefficient-stopping alternatives
    -> least-root divergence / contradiction.
   ```
2. Record connector write schemas in the contributor guide; unsupported branch aliases can otherwise target the default branch.
3. Track imported computational theorems separately from in-repository exact replays, even when the publication is peer-reviewed.
4. Reserve one issue for independent positive-direction verification so that this packet is not conflated with the repository's counterexample mission.
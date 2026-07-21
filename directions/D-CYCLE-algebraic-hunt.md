# Direction: Algebraic nontrivial-cycle hunt

Suggested issue title: `Algebraic hunt for nontrivial positive Collatz cycles`

```text
Status: IDEA
Proposal class: unclaimed research direction
Suggested claim IDs once work begins: Q-01xx, C-01xx, K-01xx, X-01xx, R-01xx
Authoring agent (handoff only): grok45-01
Claimed by: nobody
Related active work: almost none in this repository — divergence/rewrite
threads dominate; cycles are an equally valid counterexample mode
```

## One-paragraph pitch

A counterexample may be a **nontrivial positive cycle**, not only a divergent
orbit. For a chronological parity word \(w\) of length \(L\) and odd-weight
\(a\) with \(3^a\neq 2^L\), the shortcut-cycle formula

\[
n=\frac{B(w)}{2^L-3^a}
\]

is an explicit rational. The task is to force this rational (or a block-
concatenated generalization) to be a positive integer outside the trivial
cycle, using modular sieves, resultants, and lattice-reduction searches.

## Relationship to the counterexample objective

One verified nontrivial positive cycle is a full resolution of the mission.
This direction is therefore a direct `K-####` factory with unusually sharp
acceptance tests: integrality, positivity, and periodic closure.

## Exact object format

For a single primitive word \(w\):

\[
n_w=\frac{B(w)}{2^L-3^a},
\qquad
B(w)=\sum_{t_j=1}2^j3^{\#\{i>j:t_i=1\}}.
\]

For a concatenation \(w=w_1\cdots w_m\) of blocks, derive the composed affine
fixed point and demand integrality of that fixed point.

## Falsification criteria

1. **Modular kill:** for a proposed pattern family, show
   \(B(w)\not\equiv 0\pmod{2^L-3^a}\) (or the denominator never divides)
   for all members beyond a checked range, by covering congruences.
2. **Sign kill:** prove \(n_w\le 0\) for all supercritical words in the family
   (supercritical words have \(2^L-3^a<0\), so positivity needs \(B(w)<0\),
   which never happens for the standard positive \(B\) — hence nontrivial
   positive cycles must be **subcritical**: \(3^a<2^L\)).
3. **Known-cycle completeness (conditional):** if a claimed search range is
   already covered by published cycle bounds, do not reopen it without a new
   method; advance the length/weight frontier instead.
4. **Trivial-cycle trap:** any solution with orbit \(\{1,2\}\) / shortcut
   \(\{1\}\) is not a counterexample.

Important labeling note: because positive \(B(w)\) and subcritical denominators
are required for \(n_w>0\), this direction is **not** helped by supercritical
collision fibers. It is structurally orthogonal to the divergence amplifiers
used elsewhere.

## Starter experiments (suggested `X-####`)

```text
X-Cyc-1: Brute-force all words with L ≤ L0 (start L0=20), compute n_w exactly
         as a rational, accept only positive integers, verify genuine cycles.
X-Cyc-2: Modular sieve: for each L, factor |2^L - 3^a| over a in 1..L-1 and
         record impossible residue patterns for B(w) mod small primes.
X-Cyc-3: Block concatenation search: random or SAT-guided concatenations of
         short subcritical blocks whose composed fixed point has tiny height.
X-Cyc-4: LLL/Coppersmith-style attack on linearized cycle equations near
         continued-fraction convergents of log3(2), where 2^L ≈ 3^a.
```

Use exact integers / exact rationals only. Never call a failed search a proof
that no cycle exists.

## Suggested deliverables for a claiming agent

- Issue claim with agent ID and branch.
- Reproducible `X-Cyc-1` census with an explicit `L0` and machine-checkable
  output digest.
- A short note separating (i) no cycle found up to bound, (ii) modular
  impossibility for a family, (iii) a positive integer candidate.
- If a candidate appears: a full `K-####` file meeting README §9.

## Handoff

```text
HANDOFF FROM: grok45-01
HANDOFF TO: any
CURRENT CLAIM OR CANDIDATE: none (direction only)
BLOCKING STEP: open as a GitHub Issue; run X-Cyc-1 to a clear L0 and publish
FILES TO READ: README.md; directions/README.md; this file; NOTATION for B(w)
  once a notation packet is merged
FAILED ATTEMPTS: none yet in-repo
MOST PROMISING NEXT MOVE: exact census + modular sieve before any LLL work
MAIN RISK: classical cycle bounds may already cover naive search ranges;
  novelty must come from structured families or new lattice methods
POSSIBLE ORGANIZATIONAL IMPROVEMENT: track cycle-search bounds in a single
  issue so agents do not repeat the same L0 census
```

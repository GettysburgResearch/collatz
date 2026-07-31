# Q-6501 — Close both least-counterexample coefficient lanes

**Claim ID:** `Q-6501`  
**Title:** Eliminate the sparse-return supercritical lane and every finite first-crossing cylinder  
**Status:** **OPEN / GLOBAL BLOCKER**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `D-6501`, `T-6501`--`T-6503`, `L-6502`; branch-qualified PR #76--#77

## Exact target

After independent reconstruction of the branch-qualified dependencies, prove both statements below.

## Lane A — exclude sparse-return supercritical ordinary orbits

There is no positive integer `n` whose actual shortcut-Collatz orbit satisfies

\[
D_k=q_k-{\log2\over\log3}k\ge0
\qquad(k\ge0).
\tag{A}
\]

The present packet proves that any such orbit would have to satisfy all of:

\[
T^k(n)\to+\infty,
\]

\[
\max_{m\le k}3^{D_m}\gg_n k^{4/9},
\]

\[
3^{D_r}\gg_n r^{8/9}
\quad\text{at every coefficient-record time }r,
\]

and, for every fixed `H`,

\[
\#\{m<k:D_m\le H\}=O_{n,H}(k^{1/9}).
\]

Thus the remaining Lane-A object is not a critical recurrent or bounded-discrepancy path. It is an ordinary orbit with unbounded coefficient records and only sparse returns to every fixed surplus band.

A valid closing theorem must contradict ordinary integrality, minimality, or exact orbit mixing in this sparse-return regime. Proving more growth after assuming `(A)` is not enough.

## Lane B — exclude all finite first crossings

For every first-crossing parity word `w`, use the exact data of `L-6502`:

\[
x=r_w+2^j t,
\]

\[
T^j(x)=y_w+3^q t,
\]

\[
0\le t\le
H_w=\left\lfloor{y_w-r_w\over2^j-3^q}\right\rfloor.
\]

Prove that no member of this finite list can be a least positive counterexample.

Sufficient global outcomes include:

1. a uniform verified-range bound on all listed starts;
2. a cofinal lower bound on `r_w` exceeding the paradoxical ceiling;
3. a theorem forcing one later descent for every listed start;
4. for periodic words, complete whole-denominator cycle nondivisibility and exact replay.

Another finite set of crossing lengths or continued-fraction cells does not close Lane B.

## Why this is exhaustive

If Collatz is false, choose a least positive counterexample.

- If its coefficient never crosses below one, it belongs to Lane A.
- If the crossing is finite, its first crossing belongs to Lane B.
- If the orbit is eventually periodic, rotate the nontrivial positive cycle to its minimum; one period belongs to Lane B.

There is no third positive ordinary failure mode.

## What would count as a proof of Collatz

A complete packet must provide:

1. independent reconstruction of the imported least-counterexample and coefficient-stopping gates;
2. an unconditional exclusion of Lane A;
3. an unconditional cofinal exclusion of Lane B, including positive cycles;
4. no invocation of a prescribed parity directive or nonordinary completion;
5. exact handling of all positive integers above the verified range.

## What does not count

- another finite prefix census;
- another lower bound on the first crossing without cofinal exclusion;
- map-level balance without orbit-level mixing;
- almost-all descent without an exceptional-set contradiction;
- conditional divergence of an assumed ordinary orbit;
- a compatible `2`-adic parity path;
- a proper-factor positive-cycle hit;
- a heuristic polynomial delay or maximum-excursion law.

## Current status

`T-6501` and `T-6503` remove the bounded-surplus and positive-frequency-return sublanes of Lane A. `T-6502` and `L-6502` sharpen Lane B into a complete finite ordinary decision for each word. Neither infinite family has yet been eliminated.

No proof of Collatz and no counterexample is claimed.

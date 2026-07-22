# Global counterexample map — fourth pass

**Agent:** `gpt56-cartographer-01`  
**Issue:** #36  
**Cutoff:** `2026-07-22T21:54:16Z`  
**Prior cutoff:** `2026-07-22T20:46:30Z`

## Work performed

- diffed every materially changed branch after reviewed pass 3 through PR #51;
- read the exact new refund, pulse, cycle, block-carry, commutator, and H claims;
- preserved source/proposed/independent-review boundaries;
- reconciled the PR #34 versus PR #51 six-defect status mismatch;
- derived the invariant `h=21x` negative-three pulse chart and its physical Collatz embedding;
- derived its H-like toll-one renewal form;
- added a separately written finite exact-interface checker;
- updated the primary map, crosswalk, atom index, Mermaid, Graphviz, and PR description;
- rendered both the global map and a focused ordinary-state frontier diagram.

## Main findings

1. PR #49's local state is only `(t,i,k)`. Next type, physical replay, positivity, and growth are automatic once the changing-modulus divisibility test remains defined forever.
2. PR #51 proves finite all-size caps for each fixed two-pulse negative-cycle packet and records zero nontrivial hits in more than forty million bounded pulse candidates.
3. The invariant section `h=21x` of PR #51's negative-three chart gives the exact fixed map
   ```text
   x -> 9x/8        for x=0 mod8,
   x -> (9x+1)/16  for x=7 mod16,
   n=42x-5.
   ```
   One positive all-time path is a complete Collatz counterexample.
4. Grouping the pulse chart between `(2,2)` blocks gives
   ```text
   p_next=[3^(2r+2)/2^(3r+4)]p+1,
   ```
   creating a direct transfer target for H renewal methods.
5. PR #50 extends the ordered-jump local-minimum exclusion to odd-state length 185 at proposed level.
6. PR #45's block residue decoder, PR #47's commutator sieve, and PR #34's cross-prime compiler form a new mixed-drift critical cycle architecture.
7. PR #47's proposed exact seven-defect certificate raises the proposed positive-cycle support floor to eight valuations different from two, pending independent reconstruction.
8. PR #19 iteration 9 proposes the `10/30` H compiler closed on both its physical zero-carry and renormalized Sturmian faces.

## New files

- `ANALYSIS_SNAPSHOT_PASS_4.md`
- `CARTOGRAPHY_PASS_4.md`
- `cartography/ATOMS_PASS_4.md`
- `cartography/PULSE_CHART_SYNTHESIS.md`
- `cartography/check_pulse_chart.py`
- `cartography/pulse-chart-check.json`
- `cartography/pulse_chart_frontier.cpp`
- `cartography/verify_pulse_chart_frontier.py`
- `cartography/pulse-chart-frontier.json`
- `docs/ordinary-state-frontier.dot`
- this report

## Counterexample status

No explicit positive nontrivial cycle, divergent seed, regular sanctuary, H survivor, centered survivor, or equivalent third-component witness was found.

The two sharpest deterministic ordinary-state targets are:

```text
PR #49 complement counter:
  one physical n whose intrinsic (t,i,k) state is defined forever
  and whose shifted boundary values generate infinitely many fresh odd primes;

negative-three pulse chart:
  one x>0 defined forever under the fixed 9/(8,16) map.
```

## Verification boundary

The pulse-chart algebra was independently rederived and its exact physical block replay was checked on 37,500 finite branch cases. The renewal identity was checked on 15,872 completed finite renewals.

The exact frontier enumerator exhausts all `4,294,967,294` finite prefix words through depth 31. The separately written verifier independently repeats the exhaustive computation through depth 20 and replays the frozen depth-31 minimizer physically. Thus the depth-31 minimum is exact source computation plus partial independent reproduction, not a theorem about infinite survival.

All source theorem statuses remain unchanged.

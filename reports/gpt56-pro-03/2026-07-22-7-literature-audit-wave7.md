# Agent report — literature audit wave 7

**Agent:** `gpt56-pro-03`  
**Issue:** #7  
**Date:** 2026-07-22  
**Branch:** `agent/gpt56-pro-03/4-literature-audit`

## Prompt objective

Re-read the newest repository mathematics after wave 6, connect it to the literature, and make a serious constructive push toward a full unconditional Collatz counterexample rather than producing only another negative literature catalogue.

## Repository cutoff read

The pass inspected the latest available states of:

- PR #3 — collision/tower/ordinary-spine architecture;
- PR #13 — literature suite;
- PR #16 and independent PR #37 — centered recurrence;
- PR #19 — H frontier;
- PR #20 — value theory;
- PR #32 — verified all-depth EQ chain;
- PR #33 — proposed complete exclusion of the frozen corrected stage;
- PR #34 — maximal finite-type Evertse boundary, primitive cycles, spectral support, and period-ten gcd;
- PR #35 — rational-base `5x+1` control;
- PR #38 — global path cartography;
- issues #39, #40, and #41 — the newest constructive lanes;
- issues #9 and #36 as umbrella cycle/cartography threads.

No proposed proof was silently promoted.

## Main mathematical finding

The frozen corrected phase-34 construction uses a doubling-scale schedule whose next full radix is larger than the current odd multiplier. PR #33 uses that inequality to trap every signed ordinary quotient in cap/co-cap states before applying Evertse.

I replaced the scale doubling by a linear grid

```text
t_j=B+16j,
0<=j<=256.
```

Using the exact arbitrary-chain recurrence already present in PR #3, one stage has

```text
A(B)=1792B+3657472,
E(B)=2816B+5792512.
```

For every multiple of 16 with `B>=477424`,

```text
3^[A(B)]>2^[E(B+4096)].
```

The proof uses only `3^53>2^84` and exact integer arithmetic. For every ordered pair of finite stage words, the next-cylinder congruence then has one quotient class modulo the next radix and infinitely many positive ordinary lifts; the next quotient grows asymptotically.

This is recorded as `LIT-KTHM-0050`. It is an exact constructive **architecture escape** from quotient extinction. It is not yet an infinite path: the next theorem must choose the ordinary lift at every stage from one finite current state and prove forward invariance.

## Exact cycle packet

For the frozen accelerated-cycle parameters

```text
k=8,
A=13,
D=2^13-3^8=7*233,
```

I built an exhaustive residue dynamic program over all 792 positive compositions. The numerator residues modulo 233 are all residues except `0` and `138`. Hence the single prime 233 excludes the complete packet.

This is `LIT-KTHM-0051`. It is deliberately scoped as a proof-pipeline regression because Hercher's external theorem already places every nontrivial positive cycle beyond 91 local minima.

## Literature contribution

Wave 7 adds:

```text
LIT-KTHM-0048  rational-base finite representations and ordinary markers
LIT-KTHM-0049  rational-base rooted trees require genuine unbounded exact state
LIT-KTHM-0050  linear-height quotient-refund theorem
LIT-KTHM-0051  exact (8,13) cycle prime sieve
```

Sources newly ledgered:

- Akiyama–Frougny–Sakarovitch (2008);
- Frougny–Klouda (2012);
- Akiyama–Marsault–Sakarovitch (2018);
- Hercher (2023);
- Dubickas–Mossinghoff (2009);
- the 2025 rational-base normality conjecture, explicitly marked conjectural.

The rational-base literature gives a useful positive design lesson: canonical exact futures distinguish every integer-rooted subtree, so a finite modular machine is generally too small. A successful construction should deliberately retain one unbounded quotient/carry coordinate and prove that it is sufficient on an invariant subfamily.

## Counterexample priority conclusion

The current order is:

1. proof-producing positive cycle synthesis beyond the local-minimum frontier;
2. issue #39's cross-cycle ordinary-spine finite return or all-time resource invariant;
3. linear-height quotient refund with an integer-first invariant;
4. issue #40's centered forced-tail PDR with exact carry lift;
5. H reset-renewal with critical/supercritical primitive endpoint product.

The all-fixed-period q-series program remains a valuable exclusion theorem but is not the shortest positive route.

## Files added

```text
literature/LIVE_REPO_REVIEW_WAVE7.md
literature/SOURCE_LEDGER_WAVE7.md
literature/references-wave7.bib
literature/UNVERIFIED-WAVE7.md
literature/claim-maps/WAVE7.md
literature/imported-theorems/LIT-KTHM-0048-rational-base-ordinary-marker.md
literature/imported-theorems/LIT-KTHM-0049-rational-base-tree-infinite-state.md
literature/imported-theorems/LIT-KTHM-0050-linear-height-quotient-refund.md
literature/imported-theorems/LIT-KTHM-0051-eight-thirteen-cycle-prime-sieve.md
literature/topic-notes/integer-first-counterexample-architecture.md
literature/topic-notes/linear-height-quotient-refund.md
literature/topic-notes/restricted-rational-base-integer-search.md
literature/topic-notes/primitive-cycle-prime-sieves.md
literature/check_literature_wave7.py
reports/gpt56-pro-03/2026-07-22-7-literature-audit-wave7.md
```

## Validation boundary

The GitHub connector cannot execute repository scripts. The required commands now include:

```bash
python3 literature/check_literature.py
python3 literature/check_literature_wave2.py
python3 literature/check_literature_wave3.py
python3 literature/check_literature_wave4.py
python3 literature/check_literature_wave5.py
python3 literature/check_literature_wave6.py
python3 literature/check_literature_wave7.py
```

No positive ordinary counterexample, positive nontrivial cycle, or full resolution is claimed.
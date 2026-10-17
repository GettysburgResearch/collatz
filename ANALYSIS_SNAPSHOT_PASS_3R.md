# Analysis snapshot — reviewed pass 3 replacement

**Agent:** `gpt56-cartographer-01`  
**Issue:** #36  
**Purpose:** exact provenance for the quality-audited replacement of pass 3  
**Prior published pass:** [`ANALYSIS_SNAPSHOT_PASS_3.md`](ANALYSIS_SNAPSHOT_PASS_3.md)  
**Quality audit:** [`PASS_3_QUALITY_AUDIT.md`](PASS_3_QUALITY_AUDIT.md)

## Cutoff

- Repository: `gfreund123/collatz`
- Main commit: `b40e5c44959b20842e6c064084c668f5243b6ebd`
- Final reviewed cutoff UTC: `2026-07-22T20:46:30Z`
- Final reviewed cutoff Asia/Jerusalem: `2026-07-22T23:46:30+03:00`
- Issue/PR range reviewed: through `#49`
- Cartography head before replacement writes: `7c9afd20c2db60d95a74fc69a422d2b1bedeca60`
- Proof policy: preserve source labels; distinguish successful frozen-source review from native-ledger integration; never promote finite computations into universal theorems

## Exact material heads

| Source | State | Head SHA | Role in replacement |
|---|---|---|---|
| PR #3 | open draft | `d918e9a94ee28de69dc6d22ef86586e3bf62281c` | phase-`-34` towers, room filter, physical connector formulas |
| PR #13 | open draft | `6b314a6bca2fb6b2f4f2ad9d6f470f1dc4b4acec` | wave-7 refund theorem, `(8,13)` sieve, length-184 cycle exclusion |
| PR #16 | open draft | `87478352e65c7b816dfc8b3b30894b71fb50f662` | centered source for PDR follow-on |
| PR #19 | open draft | `8d249c9e3ec9b844dfdf15e0b3800edba908ff82` | H iteration-8 cycle, entropy, and return barriers |
| PR #20 | open draft | `82ca2f932438a9fe0897704ba62959ca23ec830f` | native periods 1–9 and period-10 boundary |
| PR #33 | open draft | `c9d62bce3e93f5785f72e4520bc576863d9379eb` | frozen corrected-stage exclusion reviewed by PR #44 |
| PR #34 | open draft | `b7eec65ffb13c5a89415a888c0153f36a52f23e3` | waves 24–25: cycle support floor, cross-prime compiler, distributed pulses, controller no-go |
| PR #35 | open draft | `eaba69839c07cb83794b711ecdce62c75ce765f9` | exact `5/4` control frontier |
| PR #37 | open draft | `a518db7feece37513ddcda729553e8b8c4c4d657` | centered independent review and `T-9318` repair |
| PR #42 | open draft | `94fcd99fe7fb71e0f5a15915ba40e9d74b167a13` | cycle windows through 27 and bare-congruence sanctuary no-go |
| PR #44 | open draft | `efafd32b0d99c4d02adda19c7d932bcb0e3f05fd` | independent PR #33 review and centered fixed-modulus PDR theorem |
| PR #45 | open draft | `5d17926b48e29f94a935f1d433559b0c417cef55` | critical mechanical compiler, independently reviewed by PR #48 |
| PR #47 | open draft | `fad408741bcba43a64b27e55be67b271d9bbe612` | one-pulse offense and later packet updates |
| PR #48 | open draft | `4f75cca14601bb418422324989d34832871f565d` | independent PR #45/T-8601 reviews; refund growth and cylinder sparsity |
| PR #49 | open draft | `e77a2ac230b8ed0b757c9c3208f2d4b670a4350e` | width-one refund, causal connector compiler, deterministic expanding decoder |
| PR #38 | open draft | current cartography branch | quality-audited replacement being published |

## Issue-carried source state

| Issue | Status at cutoff | Load-bearing update |
|---:|---|---|
| #39 | active | scale-22 cross-cycle handoff; permanent phase-1 tail is shifted ordinary Collatz |
| #40 | active / PR #44 | fixed-modulus centered PDR is the ghost cylinder graph; top boundary is mandatory |
| #41 | active / PR #45 | serious positive-cycle search must use critical continued-fraction scale |
| #43 | active / PRs #48–#49 | refund is atomic at width one; deterministic expansion proved conditionally on infinite definedness |
| #46 | active | two-pulse offense claimed; wave-25 exact arbitrary-pulse formula available |

## Status rules applied

1. PR #44 makes PR #33 `T-9705` independently verified at the frozen source for global confidence mapping; PR #33 has not integrated that status.
2. PR #48 independently passes PR #45's frozen compiler and rejected near-candidate, and passes PR #42 `T-8601`; it explicitly does **not** reproduce PR #42 `T-8602` or the 802-billion-composition census.
3. PR #49's decoder and refund results remain `PROPOSED`; its exact finite checker remains finite evidence.
4. PR #34 wave-25 claims remain `PROPOSED`; the distributed-pulse formulas in its report are exact constructive notes, not promoted theorem IDs.
5. PR #13, PR #19, PR #20, PR #42, PR #47, PR #48, and PR #49 retain their native source labels.
6. No counterexample or `K-####` object exists at this cutoff.

## Original-synthesis audit

The distributed-pulse formula introduced in the first pass-3 publication was independently rederived. PR #34 wave 25 later supplied the sharper negative-cycle remainder form

```text
C_delta=z_0 D_delta+R_delta,
R_delta=sum_i b_i(2^delta_i-1)2^(A_i+Delta_i)3^(N-i-1),
b_i=-(3z_i+1)>0.
```

Hence integrality is exactly `D_delta | R_delta`, positivity is `z_0+R_delta/D_delta>0`, and a fixed-total two-pulse family reduces to one exponential congruence. The reviewed atom now uses that sharper form and requires critical-scale, full-factor compatibility.

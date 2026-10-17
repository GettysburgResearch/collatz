# Analysis snapshot — pass 4

**Agent:** `gpt56-cartographer-01`  
**Issue:** #36  
**Purpose:** immutable provenance for the fourth full-conjecture cartography pass  
**Prior snapshot:** [`ANALYSIS_SNAPSHOT_PASS_3R.md`](ANALYSIS_SNAPSHOT_PASS_3R.md)

## Cutoff

- Repository: `gfreund123/collatz`
- Main commit: `b40e5c44959b20842e6c064084c668f5243b6ebd`
- Cutoff UTC: `2026-07-22T21:54:16Z`
- Cutoff Asia/Jerusalem: `2026-07-23T00:54:16+03:00`
- Issue/PR range reviewed: through `#51`
- Prior reviewed cutoff: `2026-07-22T20:46:30Z`
- Cartography head before pass-4 writes: `25ee4d5e0277317566854dc22a92efb5cce968f8`
- Proof policy: retain source statuses; distinguish source exact computation, independent replay, and theorem-level review; never infer an infinite result from a finite packet

## Exact material heads

| Source | State | Head SHA | Pass-4 role |
|---|---|---|---|
| PR #3 | open draft | `d918e9a94ee28de69dc6d22ef86586e3bf62281c` | phase-`-34` physical connector substrate |
| PR #13 | open draft | `6b314a6bca2fb6b2f4f2ad9d6f470f1dc4b4acec` | source audit, refund seed theorem, length-184 exclusion |
| PR #16 | open draft | `87478352e65c7b816dfc8b3b30894b71fb50f662` | centered source |
| PR #19 | open draft | `bd1ba3e09898c869d07873dc36470af8a2937223` | H iteration 9; `10/30` compiler no-go and renewal audit |
| PR #20 | open draft | `82ca2f932438a9fe0897704ba62959ca23ec830f` | periods 1–9 and period-10 boundary |
| PR #33 | open draft | `c9d62bce3e93f5785f72e4520bc576863d9379eb` | frozen corrected class independently reviewed by PR #44 |
| PR #34 | open draft | `b7eec65ffb13c5a89415a888c0153f36a52f23e3` | support floor, cross-prime compiler, distributed pulses, one-counter no-go |
| PR #35 | open draft | `eaba69839c07cb83794b711ecdce62c75ce765f9` | `5/4` control frontier |
| PR #37 | open draft | `a518db7feece37513ddcda729553e8b8c4c4d657` | centered independent review and repair |
| PR #42 | open draft | `94fcd99fe7fb71e0f5a15915ba40e9d74b167a13` | bounded cycle packets and sanctuary no-go |
| PR #44 | open draft | `efafd32b0d99c4d02adda19c7d932bcb0e3f05fd` | PR #33 review and centered fixed-modulus PDR boundary |
| PR #45 | open draft | `5eab58a9637d9f137197456e9bc0dc73d2174e34` | critical mechanical compiler plus new block-carry decoder |
| PR #47 | open draft | `aae8d18ebb1e2529e8c44b6b9a30b1333ca44363` | one-pulse packet, two-block commutator sieve, and proposed seven-defect exclusion |
| PR #48 | open draft | `4f75cca14601bb418422324989d34832871f565d` | independent PR #45/T-8601 review and refund firewall |
| PR #49 | open draft | `72c17c230df0f5b80971891d5013152189c0b099` | deterministic `(t,i,k)` refund map, intrinsic physical marker, and fresh-prime turnover |
| PR #50 | open draft | `de3dbedbd8907752e1b2707a2a0806b3f4e5c9da` | proposed exact exclusion of odd-state length 185 |
| PR #51 | open draft | `0487d96e82eaa3d251820373ed690f3b0c9575f1` | all-size two-pulse reduction, pulse chart, exact finite packets |
| PR #38 | open draft | `25ee4d5e0277317566854dc22a92efb5cce968f8` | prior cartography state |

## Material deltas from pass 3

### PR #49

The ordinary refund state is reduced from `(t,i,j,z)` to

```text
(t,i,k).
```

The next type is selected by `k mod64`; complete continuation is one exact divisibility test. For `t>=3744`, `k>=256`, every legal step satisfies `k'>=2k`. Physical initialization, positivity, and unboundedness are automatic after infinite definedness.

`L-8504` strengthens the physical interface: the state is an intrinsic unimodular marker recoverable from one ordinary boundary integer `n`, through `v_2(n+34)` and the odd boundary word. No separately trusted stage/type metadata is required. `T-8505` proposes that every infinite refund path must introduce infinitely many globally new odd primes into `n_j+34`; no fixed finite prime library or bounded `S`-unit ansatz can realize the missing state.

### PR #50

Conditional on the source theorem requiring at least 92 local minima, the only length-185 ascent/descent skeletons are the `AA` and `DD` one-defect forms. An ordered-jump decoder, finite multiplier bounds, exact low-height scans, and a high-divisibility stability induction propose exclusion of both families for every valuation height.

### PR #51

Two nonzero eliminants give finite caps on every positive two-pulse size for each fixed repeated negative-cycle packet. Exact scans cover 16,445,391 all-size two-pulse candidates and 24,192,960 bounded three/four-pulse candidates with no nontrivial hit. `O-8001` supplies a live exact ordinary block chart. `T-8001` independently proposes the five-defect exclusion; its bounded six-defect scout does not supersede PR #34's proposed complete six-defect theorem.

### PR #45 / PR #47

`L-8404` gives a unique valuation-block decoder from one dyadic residue and a finite carry-graph interface for positive-drift block alphabets. `L-9604` gives an opposite-drift two-block commutator divisibility sieve with a monotone all-repetition cutoff.

At the final cutoff, PR #47 also added proposed `T-9601`: an exact finite certificate excluding exactly seven non-neutral valuations. Combined with the earlier proposed exclusions through six, this raises the proposed support floor to **eight** valuations different from two. It has not yet received repository-independent review.

### PR #19

Iteration 9 proposes that the adaptive H suffixes `10` and `30` strictly descend on the physical zero-carry slice. Removing the terminal zeros gives a bounded-multiplier Sturmian `3/1` core, also nonphysical. The compiler lane is therefore proposed closed; a new H macro family must be physically nondescending and have multiplier escape.

## Issue-carried state

| Issue | Standing at cutoff | Load-bearing point |
|---:|---|---|
| #39 | active | permanent phase 1 remains shifted ordinary Collatz |
| #40 | active / PR #44 | centered fixed-modulus PDR is a completion ghost |
| #41 | active / PR #45 | critical-scale cycle compiler now has a residue/carry decoder |
| #43 | active / PRs #48–#49 | one complement counter and one current type are the complete local state; infinite definedness open |
| #46 | active / PRs #47 and #51 | exact one-, two-, and bounded multi-pulse packets; live negative-cycle block chart |

## Original cartography synthesis

From PR #51 `O-8001`, the multiple-of-21 section `h=21x` is forward invariant and gives

```text
x == 0 mod 8  -> 9x/8,
x == 7 mod16 -> (9x+1)/16,
n=42x-5.
```

Every legal step is exactly the accelerated block `(1,2)` or `(2,2)`. Any positive all-time path is a Collatz counterexample. Grouping from one `(2,2)` block to the next gives the toll-one renewal

```text
p_next=[3^(2r+2)/2^(3r+4)]p+1,
p=16x,
```

which supplies an exact new interface to PR #19's H methods. The derivation and finite checker are in `cartography/PULSE_CHART_SYNTHESIS.md` and `cartography/check_pulse_chart.py`.

A separate exact exhaustive frontier computation covers all `4,294,967,294` finite prefix words at depths `1..31`. The least positive `x` surviving depth `31` is `24643395416689283212736`, corresponding to physical `n=1035022607500949894934907`; it exits at the next block. The full depth-31 enumeration is source-exact, with an independent verifier through depth 20 and full physical replay of the frozen minimizer.

## Status rules

1. PR #44's frozen-source review remains the only status promotion of PR #33; native integration is still pending.
2. PR #48's review applies to PR #45 at its frozen earlier head. New `L-8404` remains proposed.
3. PRs #49–#51 and PR #19 iteration 9 remain proposed at theorem level; their finite computations remain exact finite evidence.
4. PR #50 has no independent reviewer at this cutoff.
5. PR #34's proposed six-defect exclusion, PR #51's bounded six-defect scout, and PR #47's proposed complete seven-defect exclusion are three distinct status levels.
6. PR #49's fresh-prime theorem is a necessary condition for a hypothetical path, not an existence theorem.
7. No counterexample or `K-####` object exists at this cutoff.

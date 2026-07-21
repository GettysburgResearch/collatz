# Agent report — dyadic-boundary residue-cylinder dichotomy

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Branch:** `agent/gpt56-cylinder-01/31-residue-cylinder-dichotomy`  
**Namespace:** `97xx`  
**Date:** 2026-07-22  
**Status:** first coherent packet complete; theorem claims remain `PROPOSED`

## Claim and repository audit

Before substantive work, issue #31 was opened and claimed with the dedicated
branch and `97xx` namespace. The reservation audit found active native ranges
through `96xx`; closed duplicate issue #28 explicitly did not reserve `97xx`.
No competing root ledger was edited.

The following live interfaces were read at their latest available heads during
the session:

- repository `README.md`;
- PR #3's `CURRENT_STATE.md`, `OPEN_PROBLEMS.md`, `CLAIMS.md`, `CANDIDATES.md`,
  `NEGATIVE_RESULTS.md`, and `NOTATION.md`;
- PR #3 head `bdbf5620743f48914331f015d5cba1ba9268b616`, including `T-0028`
  padding-counter isometry, `T-0029` adaptive 512-cell chart, `L-0029` exact
  prefix peeling, and `T-0030` ordinary quadratic bulk generation;
- PR #16 head `e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6`, especially `L-9310`;
- PR #19 head `2e7b313efa178d46d8513add74e54575e9b71767`, especially `L-9503`;
- PR #20 head `717ab8a0f3be7a87800d81b23973e2e59adaa7f6`, especially `T-9409` and the
  new short-period boundary `T-9414`/`T-9415`;
- issue #21's Foundry branch, especially `T-9601`, `T-9603`, `T-9604`, and
  `Q-9608`;
- PR #13 wave 3 head `3157bfa294e4b7287416b9469f6007815dead328`, especially
  `LIT-KTHM-0030`, `LIT-KTHM-0033`, and the completion-height note.

## Frozen class

The packet freezes the four phase-`-34` tower types from PR #3 and the direct
connector between successive dyadic boundary heights

```text
t_n = 2^(m_0+n),
t_(n+1) = 2t_n.
```

Finite control chooses any type sequence in `{5,6,7,8}^N`; the scale counter is
`m -> m+1`. For source type `i_n` and target type `i_(n+1)`, the exact high-tail
map is

```text
h_(n+1)
 = [3^(7(t_n+1)) h_n + B_(i_n)(t_n) - A_(i_(n+1))(2t_n)]
   / 2^(11(2t_n+1)).
```

This is intentionally the direct boundary comparison class, not PR #3's
chronological 256-transition composite. The direct map contracts; the composed
stage is supercritical and remains `Q-9701`.

## Theorem packet

### `D-9701`

Freezes the four finite-control types, universal exponent schedules, physical
tower replay, direct boundary recurrence, and its exact initial cylinders.

### `L-9701`

For any chain

```text
x_(n+1)=(N_n x_n+C_n)/q_n,
N_n odd,
q_n a power of two,
```

proves one exact finite initial cylinder and the block recurrence

```text
rho_k = [-C_k N_k^(-1)]_(q_k),
a_k   = [(rho_k-H_k) P_k^(-1)]_(q_k),
H_(k+1) = [N_k(H_k+P_k a_k)+C_k]/q_k.
```

The proof includes equivalence between one composite congruence and every local
integrality condition.

### `T-9701`

Proves a general completion-height theorem: if every integral transition obeys
`|x'| <= c|x|+d` with `c<1`, and the limiting height lies inside a finite set
with no legal next transition, then the nested completion is not any signed
ordinary integer and its new residue blocks are nonzero infinitely often.

### `T-9702`

Applies the theorem uniformly to every infinite four-type directive. The exact
bounds are

```text
N/q < 1/512,
0 < B < N,
q/64 <= A <= 63q/64,
|h'| < |h|/512 + 513/512.
```

The limiting height `513/511` is below `2`. For each `h in {-1,0,1}`, the next
numerator lies strictly in `(-q,0)`, so it is nonzero and not divisible by `q`.
Therefore no signed ordinary high-tail path exists. In particular every
infinite directive has `a_k != 0` infinitely often.

## Exact experiment and independent checker

`X-9701` contains two intentionally separate implementations.

- `derive.py` uses the theorem recurrence, checks it against direct composite
  congruences, and writes exact certificates.
- `verify.py` does not import `derive.py`. It reconstructs each finite recovery
  core by brute-force modular search; lifts cylinders by replaying `R` and
  `R+Q` through the accepted prefix; and directly iterates the shortcut map on
  every generated physical block.

Validation completed successfully:

```text
exhaustive type words: 1024
exhaustive transitions: 4096
finite zero blocks observed: 0
finite nonzero blocks observed: 4096
maximum cumulative modulus bits: 374
selected certificates: 5
physical tower blocks replayed: 30
exhaustive record digest: fc9a6c4dc1eba674056d05dcb859b3009914fda7859d78e80188c37b447392bb
payload digest: 135aa7b6b3ae27fa451b5c40542f88beabf9fbcc49bda23f47e603c33611bff9
all derivation checks passed
all independent replay checks passed
```

The zero-block observation is finite evidence only. `T-9702` does not use it.

## Ordinary-integer audit

The packet does not count any of the following as initialization:

- finite-prefix compatibility;
- the unique `Z_2` completion;
- the logarithmic bulk `-(7/4)log_2(3)`;
- entropy or bit-length surplus;
- a counter address naming a requested prefix.

The negative theorem excludes all signed ordinary high-tail completions, so it
also excludes a positive initialization. No `K-####` candidate is created.

## Exact remaining gap

PR #3's composed stage zipper is

```text
S_m(w_m)+3^(A_m)Y_m
 = R_(m+1)(w_(m+1))+2^(D_(m+1))Y_(m+1).
```

The stage slope is positive, and `T-0024` proves a genuine surplus. The
finite-trap proof therefore cannot be copied to it. A transfer requires a new
renormalized height, a product-formula numerator, a finite forbidden state
forced by zero blocks, or an explicit self-feeding quotient. This is recorded
without promotion as `Q-9701`.

## Files in the packet

```text
research/residue-cylinder-dichotomy/
  README.md
  CLAIM_INVENTORY.md
  INTERFACES.md
  GAP_AUDIT.md
  definitions/D-9701-dyadic-boundary-tower-class.md
  claims/L-9701-cylinder-block-recurrence.md
  claims/T-9701-finite-trap-nonstabilization.md
  claims/T-9702-dyadic-boundary-tower-exclusion.md
  claims/Q-9701-supercritical-stage-transfer.md

experiments/X-9701-dyadic-boundary-cylinders/
  README.md
  derive.py
  verify.py
  results/summary.txt

reports/gpt56-cylinder-01/
  2026-07-22-31-residue-cylinder-dichotomy.md
```

No root ledger, candidate ledger, or competing branch file is included.


## Session record required by README §11

### Starting hypothesis

A completion-height theorem should be provable once one freezes a class whose exact ordinary quotient contracts uniformly after all required cylinder costs are paid.

### Approaches attempted

- First inspected the normalized 256-stage zipper and its latest counter-prefix/bulk generators.
- Rejected a direct finite-trap argument there because `T-0024` gives positive stage slope.
- Froze the direct dyadic boundary comparison class, derived the general odd-affine block recurrence, and proved the finite-trap theorem.
- Built a derivation implementation and a separately structured exact replay checker.

### New results

`D-9701`, `L-9701`, `T-9701`, and `T-9702` form a proposed side-A theorem chain for every directive in the frozen class. `X-9701` supplies exact finite interface checks and direct physical replay.

### Candidate counterexamples

None. No positive ordinary infinite initialization exists in the frozen class, and no `K-####` ID is created.

### Failed or closed approaches

The raw finite-trap strategy does not transfer to PR #3's composed 256-transition stage because its quotient is supercritical. Prefix peeling and ordinary bulk generation do not by themselves establish residual-cylinder membership.

### Potential errors

The highest-risk points for review are the source/target exponent indexing in the direct connector, the reverse implication in the composite-cylinder lemma, and the strict trap inequalities for signed `h`. The independent checker exercises all three finite interfaces.

### Files changed

Only the namespaced research packet, `X-9701`, and this append-only report. No root ledger is changed.

### Claims affected

Added `D-9701`, `L-9701`, `T-9701`, `T-9702`, `Q-9701`, and `X-9701`. All external claim IDs remain branch-qualified and unchanged.

### Recommended next actions

Independently reconstruct `L-9701` and the three trap inequalities in `T-9702`, then attack `Q-9701` with a zero-block-run invariant rather than raw growth.

### Organizational improvement ideas

Maintain a small shared completion-height interface containing only: local odd-affine map, cumulative cylinder, new block, ordinary-height function, and forbidden finite set. Branch-specific symbolic machinery can then plug into that interface without copying root ledgers or silently promoting claims.

# Residue-cylinder dichotomy packet

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Namespace:** `97xx`  
**Status:** all mathematical claims are `PROPOSED`; `X-9701` is an exact finite experiment only  
**Created:** 2026-07-22

## Headline

This packet proves side **A** of the residue-cylinder dichotomy for one concrete,
fully quantified class cut from PR #3's four phase-`-34` cycle-padded tower types.

The frozen class uses:

- finite control: an arbitrary directive in the four tower types;
- one unbounded scale counter: `m -> m+1`;
- dyadic boundary heights `t_m=2^m`;
- the canonical **direct** connector from height `t_m` to height `2t_m`;
- one exact high-tail recurrence;
- one nested initial residue cylinder for every finite directive prefix.

For every infinite type directive, the least initial representatives have
infinitely many nonzero new blocks. The unique `Z_2` completion is not an
ordinary integer.

The proof is not a finite-prefix count. It is a uniform archimedean contraction
plus a finite exact trap exclusion. Every finite prefix remains exactly
realizable, but no single ordinary integer realizes all prefixes.

## Frozen recurrence

For source type `i`, target type `j`, and `t=2^m`, let `A_i(t), B_i(t), K_i(t),
G_i(t)` be the exact tower data of PR #3 `L-0016`. The universal exponents are

```text
K_i(t)=11(t+1),
G_i(t)=7(t+1).
```

The direct boundary connector acts on the ordinary high tail by

```text
h_(n+1)
 = [3^(7(t_n+1)) h_n + B_(i_n)(t_n) - A_(i_(n+1))(2t_n)]
   / 2^(11(2t_n+1)),

t_(n+1)=2t_n.
```

Whenever the quotient is integral, the corresponding physical shortcut-Collatz
states satisfy one exact tower replay from phase `-34` to phase `-34`.

## Claims

- `D-9701` — exact definition of the dyadic boundary tower class.
- `L-9701` — unique finite cylinders and the exact residue-block recurrence.
- `T-9701` — general finite-trap contraction theorem for odd-affine cylinder systems.
- `T-9702` — all dyadic boundary tower directives have infinitely many nonzero blocks.
- `Q-9701` — transfer target for PR #3's genuinely supercritical composed 256-stage zipper.
- `X-9701` — exact derivation and independently structured replay verifier.

See `CLAIM_INVENTORY.md` for status and dependencies.

## Exact result

For every source/target type pair and every dyadic boundary height `t>=1`, put

```text
N = 3^(7(t+1)),
M = 2^(11(2t+1)),
C = B_i(t)-A_j(2t).
```

The tower bounds give

```text
N/M < 1/512,
0 < B_i(t) < N,
M/64 <= A_j(2t) <= 63M/64.
```

Hence every integral transition satisfies

```text
|h'| < |h|/512 + 513/512.
```

Every infinite integer trajectory would therefore eventually enter
`{-1,0,1}`. For each of those three values the exact numerator lies strictly
between `-M` and `0`, so no next integral transition exists. This contradiction
is uniform in the complete infinite type directive.

By `L-9701`, eventual zero residue blocks would supply exactly such an ordinary
integer trajectory. Therefore residue blocks are nonzero infinitely often for
every directive.

## Scope boundary

This packet deliberately freezes the **direct dyadic boundary connector**. It
is not the composed 256-transition map of PR #3 `T-0027`.

That distinction is load-bearing:

- the direct boundary connector is uniformly contracting by more than nine bits;
- the corrected 256-transition stage has the positive bulk surplus of `T-0024`;
- its ordinary quotient `Y_m` is not controlled by the finite trap used here.

Thus `T-9702` is a rigorous negative comparison theorem and a reusable cylinder
principle, not a resolution of PR #3's supercritical zipper.

## Verification

Run from the repository root:

```bash
python3 -B -m py_compile \
  experiments/X-9701-dyadic-boundary-cylinders/derive.py \
  experiments/X-9701-dyadic-boundary-cylinders/verify.py

python3 -B experiments/X-9701-dyadic-boundary-cylinders/derive.py \
  --output experiments/X-9701-dyadic-boundary-cylinders/results/canonical.json \
  --summary experiments/X-9701-dyadic-boundary-cylinders/results/summary.txt

python3 -B experiments/X-9701-dyadic-boundary-cylinders/verify.py \
  --check-results experiments/X-9701-dyadic-boundary-cylinders/results/canonical.json
```

The checker does not import the derivation module. It reconstructs each tower
core by brute-force modular search, independently lifts the cylinders, replays
every affine connector, and directly executes every shortcut-Collatz tower
block in the generated certificates.

## Repository hygiene

This packet does not edit `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`,
`CANDIDATES.md`, `NEGATIVE_RESULTS.md`, `NOTATION.md`, or any competing branch
ledger. Cross-branch claims are cited with their native IDs and remain at their
native status.

No `K-####` candidate is proposed.

# X-9701 — Exact dyadic-boundary cylinders and independent replay

**Status:** `EMPIRICAL / EXACT FINITE CHECK`  
**Claims audited:** `D-9701`, `L-9701`, `T-9701`, `T-9702`  
**Issue:** `#31`  
**Agent:** `gpt56-cylinder-01`  
**Dependencies:** Python 3.11+ standard library only  
**Randomness:** none

## Purpose

The experiment audits five distinct finite interfaces without treating any
finite run as the proof of the infinite theorem:

1. reconstruct the four phase-`-34` tower cores and direct boundary connectors;
2. generate nested initial cylinders and exact new residue blocks;
3. compare the block recurrence with direct composite congruences;
4. check the contraction and three-integer trap inequalities on representative
   dyadic heights and every source/target type pair;
5. hand generated positive finite members to a separately written verifier that
   directly executes the shortcut map through every tower block.

`derive.py` uses the theorem recurrence. `verify.py` does not import it. The
checker finds each recovery residue by brute-force search, lifts each cylinder
by replaying both `R` and `R+Q` through the already accepted prefix, and then
runs the physical shortcut map step by step.

## Frozen finite audit

The canonical run covers:

- all `4^5 = 1024` type words of length five (`4096` exact connector steps);
- all 16 source/target pairs at six dyadic heights for the proof-interface
  inequalities;
- five longer positive certificates with thirty physical tower blocks;
- exact nesting, block bounds, endpoint integrality, and odd-step counts.

Finite zero blocks are allowed and are reported honestly. The theorem says
only that no infinite directive can have zero blocks eventually.

## Commands

From the repository root:

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

Expected final lines:

```text
all derivation checks passed
all independent replay checks passed
```

Frozen result digests:

```text
exhaustive records  fc9a6c4dc1eba674056d05dcb859b3009914fda7859d78e80188c37b447392bb
payload             135aa7b6b3ae27fa451b5c40542f88beabf9fbcc49bda23f47e603c33611bff9
```

## Non-consequence

The exhaustive and replay checks do not prove `T-9702`. Its infinite step is
the finite-trap contraction argument in `T-9701`. The experiment validates the
frozen arithmetic interfaces and supplies an independent exact replay path.

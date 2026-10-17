# X-8802 — Signed phase shadows and the base-`5/4` low-digit tree

Experiment ID: X-8802  
Agent: `gpt56-drift-01`  
Issue: #26  
Classification: **EXACT FINITE COMPUTATION**

## Research questions

1. Does every finite connector on phases `-2,-1` agree with the signed
   phase-shadow identity?
2. Does the odd-step imbalance telescope exactly as T-8805 predicts?
3. Which signed `5x+1` cycles are reconstructed in a frozen parity-word range?
4. Does the physical `4 -> 5` chart agree step-for-step with the restricted
   bottom path in the base-`5/4` representation tree?
5. How deep do positive roots below one million survive before a bottom digit
   `2` or `3` appears?

## Replay

```bash
python3 -B -m py_compile experiments/X-8802-phase-shadow-tree/run.py
python3 -B experiments/X-8802-phase-shadow-tree/run.py \
  --check-results \
  experiments/X-8802-phase-shadow-tree/results/canonical.json
```

No third-party Python packages are required.

## Frozen scope

```text
connector lengths:          1..20
connector quotient samples: 1..1000
signed parity words:         lengths 1..18
positive seeds A:            1..1,000,000
survival depth cap:          64
```

The canonical run performs:

- `39,999` physical connector replays;
- `40` closed-circuit coboundary checks;
- exhaustive signed-cycle reconstruction in the stated word range;
- `1,000,052` exact physical/tree edge checks in the bounded root census.

It recovers the mandatory negative cycle

```text
-2 -> -1 -> -2
```

and the positive cycles containing `1`, `13`, and `17`.

The maximum bounded survival depth is `19`, attained at

```text
A=786766,
X=A+1=786767,
low-digit prefix=1101100001001100001.
```

## Digests

Script SHA-256:

```text
e05dc40d317a9c684581cc2c4f43c66f0762fc47e34506f5b9090b5c07f97ab9
```

Canonical file SHA-256:

```text
76196998072cf4563c4f5e6600eb4507407cb953155d6218ef94de4a81036f1c
```

Canonical content digest recorded inside the result:

```text
ffc1244fd17626d4ef632213a26b46be70c04ddc97d176e1e70971c5502ab8c5
```

## Interpretation boundary

The connector identities are finite algebraic interfaces and have independent
proofs in the claim files. The cycle and seed censuses are finite. They do not
prove that the displayed cycles are globally unique, and they do not prove or
refute an infinite positive low-digit path.

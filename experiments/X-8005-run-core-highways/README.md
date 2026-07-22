# X-8005 — Run-core quotient and reset-highway audit

**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Claims:** `L-8002`, `T-8002`, `L-8003`  
**Arithmetic:** Python standard-library exact integers only

## Research question

Can the exact negative-three-cycle pulse chart

```text
A: z = 8q      -> 9q
B: z = 1+16q   -> 1+9q
```

be reduced to one ordinary quotient state, and does it contain explicit
families illuminating the missing all-time invariant?

## What is checked

`run.py` performs:

- `93,750` exact legal local chart edges for `z<=500,000`;
- `35,716` maximal-run macro identities;
- `2,555` two-macro core recurrences, mod-144 laws, and full changing-modulus
  quotient-cylinder identities;
- all `200` reset seeds
  ```text
  z_m=(2^(m+4)-7)/9,
  6<=m<=1200,
  m=0 mod6;
  ```
- the exact consecutive-`B` count and re-entry criterion;
- the first run indices producing the one-core valuations
  ```text
  4,7,10,13,16,19,22;
  ```
- a bounded search for two tempting exact reset closures.

The longest reset seed in the frozen range has `402` exact chart blocks at
`m=1200`. This is finite evidence; the theorem already proves unbounded finite
prefix length without relying on that endpoint.

The bounded reset search finds only exponent `1`, the trivial fixed cycle. It
is not extrapolated beyond the declared range.

`verify.py` is independently written. It reconstructs a strict subset of the
local/macro checks, every frozen sample seed, and the first-Hensel-hit table
without importing `run.py`.

## Replay

```bash
python3 -B experiments/X-8005-run-core-highways/run.py \
  --check-results \
  experiments/X-8005-run-core-highways/results/canonical.json

python3 -B experiments/X-8005-run-core-highways/verify.py \
  experiments/X-8005-run-core-highways/results/canonical.json
```

Frozen file hashes from the authoring environment:

```text
run.py
53700d9313d30b4541af0e5ae5a559d1bfba88df00514e1549b9246bb5f990ce

verify.py
d8cb7d15511c952869c47d65c68d822751445a9a8aa2781e3d0368fec0d7e667

canonical.json
655a1b9bfe8372af24638e9c5097c67de330a910814b6f820382e0d48ae2a2dc
```

## Interpretation boundary

The experiment verifies exact finite interfaces. It does not provide:

- a forever-defined ordinary quotient;
- a nontrivial cycle;
- an infinite run-five highway;
- or a Collatz counterexample.

The full positive target is the one in `T-8002`: one finite ordinary state whose
deterministic run-core map remains defined and emits only runs at least five.
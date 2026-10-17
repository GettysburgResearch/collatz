# X-8401 — Critical mechanical-cycle audit

Experiment ID: `X-8401`  
Agent: `gpt56-complexity-01`  
Issue: #41  
Associated claims: `L-8402`, `L-8403`, `O-8401`  
Classification: exact finite-circuit verification; no counterexample

## Research question

Can a source-admissible trillion-step balanced valuation word be repaired by a
small proof-carrying block circuit so that its cycle numerator passes a
substantial certified component of `2^A-3^k`, and does the resulting rational
fixed point become an ordinary integer?

## Frozen target

```text
k=3,149,971,404,836
A=4,992,586,555,009
```

The base `{1,2}` valuation word is the lower mechanical word with `A-k` symbols
`2`.  It is compiled by the Euclidean monoid recursion of `L-8403` rather than
expanded.

The experiment independently verifies the denominator factors

```text
7, 191, 281, 28,591, 136,398,329
```

and their product

```text
1,465,129,870,107,858,983.
```

A frozen four-list join chooses 43 disjoint adjacent swaps.  The script rebuilds
every legal swap position and delta from first principles; the masks are not
trusted as precomputed residues.

## Exact outputs

The modified numerator is zero modulo the displayed factor product.  The cyclic
local-minimum count is

```text
1,307,356,254,653.
```

A 120-digit outward-rounded affine interval gives a unique real fixed point in

```text
(1791361447298439130709020.99752835390985101078597115625463997678316699077019108974634764751200085257269769107803891195190,
 1791361447298439130709020.99752835390985101078597115625463997678316699077019108974634764751200085455151399874064825798230).
```

Therefore this word is not integral and is not a Collatz cycle.

## Replay

```bash
python3 -B -m py_compile experiments/X-8401-critical-mechanical-cycle/run.py
python3 -B experiments/X-8401-critical-mechanical-cycle/run.py \
  --check-results \
  experiments/X-8401-critical-mechanical-cycle/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-8401-critical-mechanical-cycle/run.py \
  --write-results \
  experiments/X-8401-critical-mechanical-cycle/results/canonical.json
```

Canonical SHA-256:

```text
7f9c69b95598326f9593ad5fb59f222e0c2355c31ac9c28ac49b882d041171b6
```

## Interpretation boundary

The experiment proves its displayed residue identities, local changes, directed
interval, and local-minimum count.  It does not prove a complete factorization,
cycle integrality, a divergent orbit, or a disproof of Collatz.
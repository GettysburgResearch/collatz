# O-9401 — Bounded period-four reduced-height census

Claim ID: O-9401  
Title: Primitive `{17,18}` period-four Padé approximants cross below exponent one by order three in the frozen census  
Status: EMPIRICAL  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9410, X-9409  
Scope: Padé orders `1,2,3` for three primitive cyclic period-four representatives  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Observation

For the primitive cyclic representatives

```text
W_1=(17,17,17,18),
W_2=(17,17,18,18),
W_3=(17,18,18,18),
```

`X-9409` computes the exact L-9410 approximants through order three, clears the
universal odd denominator, reduces the final rational, and records

```text
error v_2 / reduced height bit length.
```

For every representative, the measured ratio is slightly above one at order
one, essentially at one at order two, and below one at order three:

| word | order 1 | order 2 | order 3 |
|---|---:|---:|---:|
| `17,17,17,18` | 1.0063931 | 1.0000951 | 0.9979828 |
| `17,17,18,18` | 1.0062128 | 0.9999734 | 0.9978896 |
| `17,18,18,18` | 1.0063674 | 1.0001494 | 0.9979724 |

The corresponding gcd bit lengths at order three are only

```text
89, 25, 87
```

against reduced rational heights of approximately

```text
1.42, 1.44, 1.46 million bits.
```

## Interpretation

This is consistent with the universal limiting constant

```text
mu_4=0.993714361875... .
```

It provides no visible finite evidence for the `0.6286%` quadratic-scale height
saving required by Q-9411.

## Classification boundary

The observation is **bounded evidence only**. It does not establish an
asymptotic upper bound on the reduced exponent, an upper bound on future gcds,
or rationality of any period-four value.

A later order, a different determinant family, or a provable systematic common
factor could change the conclusion. No period-four theorem is promoted from
this census.

## Verification

Replay:

```bash
python3 -B experiments/X-9409-period-four-height/run.py \
  --check-results experiments/X-9409-period-four-height/results/canonical.json
```

Canonical SHA-256:

```text
bf85a00cc1b34aef1d85f5b7e483547b1200ac10e53c02375333447bb1c31546
```

## Suggested next attack

Compute order four or construct adjacent-order determinants only if accompanied
by exact sparse evaluation and reduced-height accounting. The target remains an
asymptotic theorem, not a longer table.
# X-8202 — Critical-path core/quotient crosswalk

**Agent:** `gpt56-refund-01`  
**Date:** 2026-07-23  
**Status:** exact finite corroboration plus independently derived universal algebra

## Frozen sources

```text
PR #49  3357d36c7464e036363c6579d873f19f5674adad
PR #51  9c0753db8543a99247ed55beefbce75ca8f2b507
```

`run.py` imports no repository or author module. `verify.py` is separately written and does not import `run.py`.

## Questions

1. Does PR #49's intrinsic core decoder and eight-block compiler reconstruct?
2. Does its second-cylinder modulus really cancel all target-type dependence?
3. Does the genuine top lift double uniformly after one exact height threshold?
4. Do PR #51's physical chart, maximal-run core, full `2^(8+3s)` cylinder, divisible-seven normalization, and reset highways reconstruct?
5. Are both architectures instances of one changing-modulus quotient law?

## Exact result

Both routes have the same hidden form:

```text
q      = rho + 2^H ell
q_next = sigma + P ell
sigma >= 0.
```

For PR #49,

```text
H = 11(t+33)
```

is independent of both target types. The next imposed cylinder has exponent `11(t+49)`. The exact certificate

```text
3^665 > 2^1054
```

gives the first uniform connector threshold

```text
t=5632,
```

after which every coherent positive top lift satisfies

```text
ell_next >= 2 ell.
```

For PR #51, the corresponding sufficient cone is

```text
9^(r_n+1) > 2^(5+3 r_(n+3)).
```

The explicit aperiodic schedule

```text
r_n=64+n
```

lies in that cone and also has every run above the physical growth threshold. This is an exact target schedule, not an ordinary realization theorem.

## Coverage

```text
PR #49 local states:                    12
PR #49 canonical blocks:                96
PR #49 exact block replays:            288
PR #49 two-block crosswalks:           384
PR #49 finite-state threshold checks:   12

PR #51 physical chart edges:         10,001
PR #51 maximal-run macros:              208
PR #51 quotient identities:          13,056
PR #51 divisible-seven checks:          256
PR #51 reset seeds:                     200
PR #51 reset chart edges:            40,412
PR #51 refund-cone doubling checks:  11,250
```

## Replay

```bash
python3 -B experiments/X-8202-critical-core-crosswalk/run.py \
  --output /tmp/X-8202.json \
  --check-results experiments/X-8202-critical-core-crosswalk/results/canonical.json

python3 -B experiments/X-8202-critical-core-crosswalk/verify.py \
  experiments/X-8202-critical-core-crosswalk/results/canonical.json
```

## Frozen digests

```text
run.py:
0a804ad1c480f1b0ed09ae773378641904dfa5030fec32ba6b090b2ee9107edf

verify.py:
072edfc1103fcdb786a9e8cb22815e2ad04ebc1e7b2820b5f4d8fb6a10f9b149

canonical.json:
a12d633bd7bb439f73f59aac051459fccb50a41d5bf8c51e91592586e515f6be

semantic:
e22874271350a0223cc3008153ea6a3e313a013bfa542cec691ec11b038eaa1f
```

## Limitations

- No forever-defined ordinary core or run state is supplied.
- The linear run schedule selects one compatible `2`-adic completion; ordinary integrality remains open.
- Top-lift growth is conditional on coherence. It removes the height/drift obligation, not the residue-generation obligation.
- Source-qualified fresh-prime and irrationality claims outside the named review chains remain pending separate independent source review.

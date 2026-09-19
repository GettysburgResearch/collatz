# X-AEM-001: exact two-exit source-merging evidence

Standard-library Python 3.10+; no repository modules or external packages.
Use the raw shortcut map, including raw iteration after reaching 1. The
proof is in [PROOF.md](../../research/astra-exit-merging/PROOF.md).

## Run from the repository root

```bash
python -B experiments/X-AEM-001-exit-merging/run.py \
  --check experiments/X-AEM-001-exit-merging/results/canonical.json
python -B experiments/X-AEM-001-exit-merging/verify.py \
  experiments/X-AEM-001-exit-merging/results/canonical.json --self-test
python -O -B experiments/X-AEM-001-exit-merging/run.py \
  --check experiments/X-AEM-001-exit-merging/results/canonical.json
python -O -B experiments/X-AEM-001-exit-merging/verify.py \
  experiments/X-AEM-001-exit-merging/results/canonical.json --self-test
```

Interactive investigation:

```bash
python -B experiments/X-AEM-001-exit-merging/run.py --example 23 1 0
python -B experiments/X-AEM-001-exit-merging/run.py --source 819
```

On Windows, replace `python` by the appropriate `py -3` invocation. No Windows
execution is claimed for this authoring pass. To reconstruct the artifact,
use `--output <new-file>`; `--check` compares the complete typed canonical
payload and never overwrites the reference.

## Payload and coverage

`results/canonical.json` is compact, exact JSON. Large integers are literal
Python/JSON integers, never IEEE-754 approximations. A JavaScript consumer
must use a lossless integer parser or a schema-preserving string conversion.
Do not open and re-save it through a floating-point JSON pipeline.

Semantic SHA-256 (sorted compact ASCII JSON of `payload` only):

```text
207bdb81b078c67fb18a304d0997b988e747f0dad165546e18cf6343c6783b8d
```

| Population | Exact scope and result |
|---|---|
| Good odd-exit rule | Odd n from 3 through 8191: 2,048 certificates and 2,047 rule misses, all retained. |
| Even-exponent Mersennes | All even exponents 2 through 256: 128 physical certificates. This is not a proof of convergence of the reduced odd-exponent sources. |
| Two-exit CRT families | 1,084 (k,h,t) cases, each with both half-source and equal-clock one-third certificates. Small grid k=1..32,h=1..16,t=0,1; additional k in {48,64,128,256,1024}, h in {1,2,8,32,128,1024}, t=0,1. |
| No forward descent specialization | All 380 CRT cases with k>=23 have the actual forward-arm minimum strictly above the original source. |
| Independent ambient grid | k=1..24 and odd u=1..255: 96 rule certificates and 2,976 rule misses. |
| Partial normalizer | Every source 2..4096; all chains, composed clocks, and residual outputs retained. 217 end at CORE and 3,878 at UNRESOLVED. These are **not** Collatz convergence/divergence counts. |

Both physical arms of all family cases, including k/h=1024, are **literally
replayed** in this corpus, not merely substituted into an endpoint formula.
No individual arm may exceed 100,000 steps in this software implementation;
that explicit replay budget is not a bound in the mathematical theorem.

## Independent implementation boundary

`run.py` constructs guarded rules and a partial selector. `verify.py` imports
neither it nor any project module. The verifier:

- reconstructs the same CRT inputs by solving for u modulo `3*2^(h+6)`, rather
  than for a modulo `12*9^k`;
- checks every encountered physical parity with an independently written raw
  map, and also reconstructs each full word's affine numerator/denominator;
- verifies the original-source strict order, both arrivals, peaks, minima,
  exact inventories, guard failures, and actual composed clocks;
- symbolically checks both seed paths on the **whole** cylinder v=7+32t by
  exact affine coefficients, separately from numerical family samples.

The self-test rejects **20 re-sealed altered envelopes**, including the new
CRT parameter/valuation, seed word, one-third witness, no-forward minimum,
coverage omissions, and integer/boolean/integral-float aliases. Four further
direct adversarial controls reject two real but non-decreasing meetings, an
equal-source zero-progress certificate, and an illegal parity path. Re-sealing
means the submitted digest is valid, so merely checking the hash cannot pass
the self-test. The full tests are repeated under optimized Python; no test
relies on `assert` for a required guard.

Both implementations have the same author. This is implementation diversity,
not independent mathematical review or proof-assistant verification.

## Partial selector semantics

Priority: stop at 1; halve even values; use the usual n=1 mod4 forward rule;
use the n=2 mod3 or n=4 mod9 smaller ancestor; use the good odd-exit rule; use
the two-exit rule; otherwise return UNRESOLVED. Each successful move strictly
decreases the ordinary source. Convergence at an arbitrary residual source
is not silently imported from a separate convergence oracle.

This is intentionally **not** an implementation of every older rank or
inverse-dictionary rule. Its counts should not be compared as universal
coverage scores against different algorithms, clocks, or source populations.

## Evidence exclusions

The receipt records only commands actually executed. No full repository
checkout, `tools/validate.py`, CI, external Lean build, native browser test,
old full artifact protocol, or remote publication is claimed. The proof's
all-parameter statements do not follow from these bounded computations;
review them as mathematics.

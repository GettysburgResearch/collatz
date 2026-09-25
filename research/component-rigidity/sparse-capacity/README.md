# Constructive two-ladder capacities

**SC-001--006: PROPOSED. No complete Collatz proof or independent mathematical review.**

Read [PROOF.md](PROOF.md). This is the new continuation of the
[preserved anchored-cut packet](../anchored-cuts/README.md), not the separate
[residue-locked geometry](../pass2/PROOF.md).

## Main results

Two deterministic ordinary inverse ladders force arbitrarily large fixed-source
separation costs, with finite certificates that do not enumerate the ambient
interval. The pin-only minimum is exactly the weighted sum of circular color
alternations. The associated sparse graph has sharp pair-separation energy
threshold two. An explicit finite-height construction replaces compactness.

A permanent 3x+1 control is essential: the selected ladders of 27 and 1 never
meet, although 27 converges. The full-graph upper repair bound remains OPEN;
capacity escape is not merger completeness. Both 5x+1 cycle controls survive.

## Replay (Python 3.10+, standard library)

```sh
python -S -B research/component-rigidity/sparse-capacity/run.py --output /tmp/sparse.json
python -S -B research/component-rigidity/sparse-capacity/verify.py /tmp/sparse.json --corpus --self-test
python -S -B research/component-rigidity/sparse-capacity/check_models.py > /tmp/sparse-models.json
```

Repeat all commands with `-O` to reproduce the optimized checks. `run.py` without
`--source` generates the fixed 47-case inventory. For one bounded request:

```sh
python -S -B research/component-rigidity/sparse-capacity/run.py --source 13 --multiplier 5 --depth 1024 --output /tmp/example.json
python -S -B research/component-rigidity/sparse-capacity/verify.py /tmp/example.json --self-test
```

The command returns a finite exact lower certificate or an actual convergence
path. It does not infer nonconvergence, and an insufficient chosen depth is not
reported as satisfying an unspecified budget. Hexadecimal strings preserve large
integers without changing Python's decimal safety limits. Height `2^6463` means
a symbolically certified ambient cutoff, NOT an exhaustive enumeration.

The checker has explicit resource guards: depth at most 16,384, shell/height
exponents at most 100,000, and hexadecimal fields at most 100,000 digits. These
are implementation limits, not hypotheses of the unbounded mathematical recipe.

`verify.py` imports no generator or max-flow implementation. `check_models.py`
is separately labeled a bounded comparison and does import the generator and
the preceding full-cut implementation. These distinctions and actual counts are
recorded in [VALIDATION.json](VALIDATION.json). Full payloads are regenerated,
not committed. Source and corpus hashes authenticate the executed bytes, not the
mathematical proof. No complete-checkout validator, remote CI or formal proof
build was run. Main, source branches, statuses and workflows are unchanged.

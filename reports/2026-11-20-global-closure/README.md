# Global-closure certificate and review reports

This folder supports the [research packet](../../research/global-closure-20261120/README.md).
**Collatz is not proved.** The principal completed result is a conditional
all-lift induction from forward-five basin closure. The physical five law
and the actual reciprocal-psi upper estimate remain open.

## Evidence map

| Manuscript | Production evidence | Independent reconstruction |
|---|---|---|
| [merger.md](../../research/global-closure-20261120/merger.md) | [Affine certificate](merger-certificate.json), [report](merger-report.json), [checker](../../experiments/global_closure_merger.py) | [MERGER_REVIEW.md](MERGER_REVIEW.md), [checker](check_merger_independent.py), [report](merger-independent-report.json) |
| [transport.md](../../research/global-closure-20261120/transport.md) | [Report](transport-report.json), [checker](../../experiments/global_closure_transport.py) | [TRANSPORT_REVIEW.md](TRANSPORT_REVIEW.md), [checker](arithmetic-transport-independent.py), [report](arithmetic-transport-independent.json) |
| [arithmetic.md](../../research/global-closure-20261120/arithmetic.md) | [Report](arithmetic-report.json), [checker](../../experiments/global_closure_arithmetic.py) | [ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md), [checker](arithmetic-independent-check.py), [report](arithmetic-independent-report.json) |
| [closing-attempts.md](../../research/global-closure-20261120/closing-attempts.md) | Written exact identities and attributed source reconstruction | [CLOSING_REVIEW.md](CLOSING_REVIEW.md), [checker](check_closing_independent.py), [report](closing-independent-report.json) |

Each review is by a different agent from the claim's author. These are
agent reconstructions, not external peer review or formal verification.
The transport comparison independently reconstructs physical returns and
exact source mass but reuses the author's logarithm enclosure routine
after a separate algebraic audit; its independence is not overstated.

The arithmetic review required one software correction: the assertion-based
production checker now explicitly refuses optimized Python. The mathematical
manuscript and deterministic report were unchanged. Normal production
comparison and expected optimized refusal are separate bundle checks.

## Reproduce the frozen bundle

From a clean, complete checkout with Python 3.11 or newer:

```sh
python -X utf8 -B reports/2026-11-20-global-closure/run_bundle.py
python -X utf8 -B tools/validate.py --regressions
```

Both commands accept an optional `--receipt` path **outside** the checkout.
The first checks [CONTENT_SHA256.json](CONTENT_SHA256.json), all three
production reports, the four separate review computations, and the
arithmetic optimized-mode refusal. It records the exact Git head and tree
and requires the checkout to remain clean. The second performs the
repository's existing structural and bounded-regression validation; it is
not mathematical verification.

[VALIDATION.md](VALIDATION.md) distinguishes the exact execution heads,
attached receipts, final publication head, and their evidence limits.
The attached [scientific receipt](execution-content-science.json) records
all 8 checks passing at content commit
`3cd47dbdeaddf6e4f4446d795271e75a52d68c99`; the
[repository receipt](execution-content-repository.json) records all 11
existing validation commands passing there. The publication child retains
all 26 manifest files unchanged. These are actual completed executions,
not predictions about an unexecuted head.

## Scope of the finite and symbolic checks

- Merger: 464 infinite affine cells and 497,664 reduced residues in the
  author's complete cover; independent CRT disjointness and exact density
  cover; adversarial corrupted certificates rejected.
- Arithmetic: 16 generated legal blocks, 260 displayed odd edges, 5,600
  pairwise gcd checks, and states up to 71,358 bits. Independent counting,
  clock, block, prime-share, and recharge checks cover different bounded
  instances. The proofs, not those samples, supply the universal finite
  construction for each length.
- Transport: 2,941 unsafe original sources, 64 return observations, 25,037
  physical shortcut edges, and an analytic tail for all original sources
  beyond 8192. The reviewer separately replays 183 unsafe sources and 32
  returns with exact source-mass conservation.
- Direct closing attempts: 79 shifted-power words, 3,220 inverse lifts,
  800 lift identities, 512 progression guards, 3,857 stopping-grade
  endpoint comparisons, and 1,667 product identities.

No finite trajectory test establishes all-time convergence. The merger's
uniform finite graph is conditional at each `/5`; it is not a uniformly
bounded program of ordinary Collatz transitions.

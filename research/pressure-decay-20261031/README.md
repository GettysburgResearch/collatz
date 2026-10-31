# Pressure-decay attack, 2026-10-31

**PROPOSED; pointwise F(t)->0 remains OPEN.** Stacked on PR140 at
`6bee3183ff7f29f2e20ca88ab94bc7745c1af602`. No earlier proof, accepted status,
main, workflow, setting or license is modified.

Read [ENERGY.md](ENERGY.md) first for the new finite-clock route, then
[PROOF.md](PROOF.md) and [SOURCES.md](SOURCES.md).

## What this pass establishes within the proposed arguments

- **PF-006/007:** an all-source finite-clock energy E_q decreases to the
  total nonperiodic component mass. Its finite-prefix truncations give
  uniform upper bounds for F at all sufficiently large targets WITHOUT
  waiting for any source to converge. The residual energy is not proved zero.
- **PF-008:** an explicit, computable fixed-depth squared-derivative moment
  S_q would force F decay if S_q=O(q^2). The proof combines a fixed escaping
  source with uniform orbit packing. Only an exponential unconditional
  upper bound is obtained; the quadratic bound is OPEN. A literal trajectory
  from 27 already forces S_32>13, ruling out naive stepwise contraction.
- **PF-001:** `sum_(odd t<=Y) F(t) < (25/4)Y^(39/40)`, hence explicit
  polynomial decay outside a density-zero set of TARGETS. An endpoint-safe
  extension of the credited orbit recurrence improves the asymptotic
  exponent to every beta>h_2(log(2)/log(3)). This is not density-one
  convergence of starting sources and not pointwise decay.
- **PF-002:** a bounded weighted composition operator on ordinary l2 has
  fixed space exactly the span of the nonperiodic component-pressure
  vectors. Thus F decay is equivalent to absence of these fixed vectors.
  This characterization does not prove their absence.
- **PF-003:** no positive periodic-residue power function of exponent below
  two can be a fixed-block supersolution for inverse square pressure.
  Exact positive trajectories prove the obstruction at every modulus and
  above every fixed height. This does not disprove pressure decay itself.
- **PF-004/005:** the classical all-one trajectories impose a sharp stated
  limitation on possible polynomial exponents; a separate 2n+1 toy shows
  why even faster averaged decay does not close the pointwise gap.

No independent-agent launcher was available. The analysis and both code
implementations are same-author work; neither a swarm nor independent
mathematical peer review is claimed.

## Replay

Python standard library only; run from the repository root:

```sh
python -B experiments/pressure-decay-20261031/run.py --output /tmp/pressure.json
python -B experiments/pressure-decay-20261031/verify.py /tmp/pressure.json
python -OO -B experiments/pressure-decay-20261031/run.py --output /tmp/pressure-oo.json
python -OO -B experiments/pressure-decay-20261031/verify.py /tmp/pressure-oo.json
```

The producer writes a companion `.profile.json`; keep it beside its checks
file. Full outputs are deterministic and regenerated rather than committed.
The verifier imports neither the producer nor any repository module and
reconstructs all profile entries and all 83,968 finite source/clock entries
using raw shortcut clocks. Forty-one energy certificates retain unfinished
sources. Their finite-bank moment values are NOT full-source upper bounds;
the explicit omitted-source allowance grows exponentially with the clock.

[Execution receipt](../../reports/pressure-decay-20261031/receipt.json) and
[self-audit](../../reports/pressure-decay-20261031/REVIEW.md) distinguish
universal proof statements, bounded checks, and unavailable validation.

**Still missing:** prove the quadratic moment bound (M), exclude the
nonzero ordinary fixed vectors, or otherwise eliminate their sparse
pressure spikes. No complete Collatz proof is claimed.

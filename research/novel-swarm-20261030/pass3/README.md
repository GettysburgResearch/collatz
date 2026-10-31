# Pass 3: ordinary pressure boundary and finite invariant witnesses

**PROPOSED; self-audited, not an accepted proof of Collatz.** Parent:
`c8a5f1a391a10ef4927383e472bceebb2b04c5e7`, draft PR #140. This pass adds
new files only; earlier proof bytes and mathematical statuses are preserved.

## What materially changes

[Pressure bridge](PRESSURE_BRIDGE.md), B1--B4, applies the credited uniform
finite-simple-path reciprocal budget to FIRST hits. It gives the universal
positive discount `2^-100 t/x < J_0(x,t) <= t/x`. As a result, pressure and
the ordinary basin Dirichlet series have exactly the same convergence
threshold, and computing the first-hit square pressure to arbitrary precision
is equivalent to deciding that target's odd basin membership. The external
positive-density consequences are separately SOURCE-QUALIFIED and conditional;
their Lean projects were not replayed.

[Ordinary boundary](ORDINARY_BOUNDARY.md), Q1--Q5, is the main new direction.
It constructs a normalized profile `F(t)=H_2(t)/t^2` and classifies its entire
cluster set at ordinary infinity. Every nonzero cluster vector belongs to
one actual nonperiodic merger component. Consequently `F(t)->0` is equivalent
to universal eventual periodicity, with nontrivial positive cycles STILL
ALLOWED. The vanishing statement is open, not inferred from the classification.
A correctly transported first-hit pressure also has a bounded monotone
all-time ledger along any nonperiodic orbit; the old moving-endpoint gap is
addressed for this specific quantity, not for occupation collisions.

The finite bank through 65,535 produces one uniform certificate for EVERY
positive odd target: a rational profile with 52,063 support points and
supremum error less than 1/131072. Its maximum support is 197,759,717, so
`F(t)<1/131072` for EVERY odd t above that value. This is one accuracy level,
not a proof that all future source banks can be completed.

[Finite witnesses](FINITE_WITNESSES.md), W1--W3, builds an explicit 4d-state
linear carry system. Any failed Collatz invariance identity for a supplied
d-dimensional binary linear model has a violated ordinary edge below
`2^(4d+1)`. Combining this with the proposed parent rigidity theorem gives
the same guarantee for EVERY nonconstant model in that class. A reachable-
span algorithm finds witnesses without scanning the exponential interval.
A 48-dimensional example returns source 187,649,984,473,769. No finite-rank
hypothesis is established for the actual convergence indicator.

## Replay and evidence

The [producer](../../../experiments/novel-swarm-20261030/pass3/run.py) uses
four Python worker processes, NOT independent AI agents. The
[verifier](../../../experiments/novel-swarm-20261030/pass3/verify.py) imports
neither the producer nor any project module. Standard library, Python >=3.11.
Run from the repository root:

```sh
python -B experiments/novel-swarm-20261030/pass3/run.py --output /tmp/p3.json
python -B experiments/novel-swarm-20261030/pass3/run.py --serial --output /tmp/p3-serial.json
python -OO -B experiments/novel-swarm-20261030/pass3/run.py --output /tmp/p3-oo.json
python -B experiments/novel-swarm-20261030/pass3/verify.py /tmp/p3.json --output /tmp/p3-verify.json
python -OO -B experiments/novel-swarm-20261030/pass3/verify.py /tmp/p3-oo.json --output /tmp/p3-verify-oo.json
```

Each producer run also creates `<output>.profile.json`. Keep that companion
next to its checks JSON. All three producer outputs AND profiles agreed
byte-for-byte; both verifier modes agreed. Full deterministic outputs are
regenerated, not committed as large payloads.

Coverage: 4,300 models; 33 exported certificates; 8,448 carry checks; 32,768
odd sources; 52,063 exact profile entries; 296 transported ledger entries;
5,460 valuation words and 16,380 lifts. The separate raw-clock reconstruction
executes 2,379,157 shortcut steps and rejects ten targeted corruptions.
See the [review](../../../reports/novel-swarm-20261030/pass3/REVIEW.md),
[receipt](../../../reports/novel-swarm-20261030/pass3/receipt.json), and
[verification summary](../../../reports/novel-swarm-20261030/pass3/verification.json).
The prior pass-2 output was freshly replayed and matched its original hash.

## Boundary that must not be hidden

No theorem forces `F(t)->0`, excludes all nontrivial cycles, or supplies the
parent fixed-source collision upper bound E5. Bounded increasing transport
mass is not a decreasing well-founded rank. Finite matrix-model rejection
does not assert finite complexity of the actual convergence indicator.
No independent AI review, external formal build, full-checkout root validator,
remote CI result, or exhaustive literature-priority audit is claimed.

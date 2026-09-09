# Repeated arithmetic spikes: an all-future mass certificate

**PROPOSED pending independent mathematical review.** This continues
[the critical-tail packet](../README.md) at PR105 commit
`3c7fa4a0a2c5c48792c8efd5f5e90e94e44dab0f`. It does not amend Reviewer D's
verdicts or promote any canonical result.

## Main outcome

For the same initial weight `w=1_U/R_*^2` and the same quarter-unsafe return
operator H, the new certificate proves

$$
\boxed{\|H^j w\|_1\le \frac{12}{2^{48}}
       =\frac{3}{70,368,744,177,664}
       <4.264\cdot10^{-14}\quad\text{for every }j\ge52.}
$$

The right side does **not** grow with the number of future returns. All
unverified sources are included in it, with no assumption about their eventual
behavior. It is an absolute mass in this summable weighted ensemble, not a
fraction of integers or a percentage of the conjecture resolved.

**The residual is positive. This is not Collatz closure or a proof of uniform
tightness at arbitrarily small error.**

## What changed in the proof attempt

The earlier critical moment is destroyed by an input-dependent unsafe clock;
a fractional output bound does not regenerate its input envelope. This pass
does not try to reset that envelope. It retains original source mass through
all later times.

A complete finite rank ball supplies initial sources. Actual exits from that
ball are followed into a finite **forward-closed clearance forest**, allowing
large rank increases. Once an orbit enters this certified forest it never
returns to the unknown part. The forest block of the operator is nilpotent,
so its elimination has no unsafe feedback or re-entry assumption.

The precise separation is:

- all remaining unknown initial mass is charged once;
- its mass at every later time is bounded by the same initial remainder;
- its total first-entry mass into the forest is also bounded by that remainder;
- its total late occupation of the forest is bounded by 52 times the remainder.

The last item is a genuinely summed, undiscounted all-time bound. No analogous
bound on total repeated visits in the unknown complement is claimed.

## The finite certificate behind the all-time conclusion

At initial rank cutoff `Y=2^32`, the complete rank ball has **163,168** non-core
sources; **78,828** are quarter-unsafe. Their exact B-forest has **111,763**
unsafe vertices, including **32,935 outside the initial rank ball**. Every
root reaches 1 within **52 B returns / 261 shortcut steps**. The largest
physical value encountered is **21,206,132,666**.

The unknown *initial* rank tail is analytically at most `12Y^(-3/2)`.
Positive killed transport cannot create additional mass from it. Combining
these facts, rather than extrapolating a finite-time numerical trend, proves
the displayed all-future bound. The same reasoning controls the weight of
sources that ever exceed rank `449700062647992267556` at any shortcut time.

The finite part was independently reconstructed by different rank, trajectory
and graph algorithms. The universal analytic tail and operator statements are
in [PROOF.md](PROOF.md); their acceptance still needs mathematical review.

## Claims and boundaries

| ID | Content | Boundary |
|---|---|---|
| ATT-101 | Source truncation gives uniform error over all future times and source-dependent finite clocks. | Bounded observables or once-only source events, not arbitrary unbounded moments or summed visits. |
| ATT-102 | Exact finite first-exit flux and cycle-aware classification for every rank cutoff. | Exiting sources are not assumed killed; an inverse resolvent on a trapped cycle is not used. |
| ATT-103 | Nilpotent elimination of a forward-closed clearance forest; total inflow and occupation bounds. | Clearance is an explicit hypothesis/certificate, not a universally successful search rule. |
| ATT-104 | The three reconstructed forests yield actual all-source, all-future nonzero mass bounds. | No cofinal family of successful forests or zero residual is proved. |
| ATT-105 | `||H^J||_(l1->l1)=1` for every finite J, using actual unsafe CRT shadows. | The tiny output for canonical w is not a reusable contraction on arbitrary inputs. |

The measure identities are elementary. The arithmetic input is credited to the
existing moving-rank and unsafe-switch packets; the precise new certificate
and its no-reset interface are the work of this continuation. No broad
external novelty claim is made.

## Replay and handoff

From a complete checkout:

```bash
python -B experiments/X-ATT-002-repeated-spikes/run.py \
  --check experiments/X-ATT-002-repeated-spikes/results/canonical.json
python -B experiments/X-ATT-002-repeated-spikes/verify.py \
  experiments/X-ATT-002-repeated-spikes/results/canonical.json --self-test
python -O -B experiments/X-ATT-002-repeated-spikes/verify.py \
  experiments/X-ATT-002-repeated-spikes/results/canonical.json --self-test
```

[Experiment details](../../../experiments/X-ATT-002-repeated-spikes/README.md)
state exact coverage and limits. [Sources and status](SOURCES_AND_STATUS.md)
record the dependency and publication boundaries.

The full-proof obligation is to force the residual mass to zero, for example
by a *proved cofinal* family of physically cleared rank balls. Merely running
the bounded checker at larger cutoffs does not supply that theorem. Preserve
the long unsafe shadows, the parent's critical-tail failures, and all unknown
source mass when attempting this next step.

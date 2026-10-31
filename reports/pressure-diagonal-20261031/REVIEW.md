# Scoped self-audit and publication boundary

**PROPOSED; same-author reconstruction and separate code paths, not
independent mathematical review. No proof of F(t)->0.**

## Frozen dependencies

- Parent PR143: `41a408e5e617fb4e65142485f6f3ff3e6ef6c408`, tree
  `47a1c60856ce3466d3f6afeee3f535b2420dbe39`.
- PR143 `research/pressure-decay-20261031/ENERGY.md`, PF-006--008:
  finite-clock populations, energy, and the earlier quadratic S_q target.
  Blob `e75f57679065227ec85cfb8c674d0b5ed850ab4a`.
- PR140 pass 4: `fe2247fcd7730c15430941a7b6e011d006d41d84`,
  `research/novel-swarm-20261030/pass4/WINDOWS.md`, W2:
  K=16,beta=19/20 finite-simple-path packing. Blob
  `b6ac911e613c0ecaaa4032b2831790e09c3a5f54`.
- PR140 pass 3: `6bee3183ff7f29f2e20ca88ab94bc7745c1af602`,
  PRESSURE_BRIDGE.md B1 and ORDINARY_BOUNDARY.md Q2--Q4:
  positive first-hit discount, component pressure, and the eventual-periodicity
  equivalence. Their original PROPOSED statuses are retained.
- PR140 pass 2 INVERSE_PRESSURE.md P5 and EXACT_DENSITY.md:
  prior geometric-law and periodic-residue framework. The new s=4 trace is
  not claimed as the discovery of that framework.

## Claim reconstruction

D1: all terms are nonnegative; dropping distinct-source cross terms is valid.
The 17/15 factor comes from COMPLETE immediate-predecessor fibers, not a
sample or an independence assumption. Later mergers can only increase S_q.

D2: killing is at the first actual repeated odd state, including 1->1.
The raw finite-clock D_q is NOT killed. The tail allowance keeps every
uninspected source. The finite-prefix maximum includes the starting state.
A killed source has no new future values, which is exactly why (6) is valid.

D3: the cutoff is N=ceil(1/E), in NUMBER OF ODD SOURCES. Its reciprocal-square
tail is 1/(4N). This distinction prevents a factor-two cutoff error. The
cube bound is an interpolation statement under a summable envelope.

D4: only ACTIVE sources have Q distinct states. Their earlier normalized
weights dominate their final weights. Sorting is applied to the squared
value sum, not to the temporal order. Tonelli is valid for positive terms.
All source families are retained; no basin is treated as an injective orbit.

D5: beta=19/20 gives 1+2/beta=59/19 and rate
(2/beta-2)/3=2/57. A finite-clock bound is not a height-modulus for F: the
maximum prefix height must still be controlled for such a modulus. The
quadratic DIAGONAL moment is a sufficient open hypothesis, not a result.

D6/T1--T3: immediate inverse valuations have the appropriate parity. Every
positive integral inverse is a positive odd source. Ternary table residues
are represented by positive odd integers. The negative reference spike is
not assigned a negative-integer reciprocal weight. All exponent tails and
positive target tails are bounded, not truncated without error.

L1--L4: the exact one-step loss is bounded below by 7/(16t), with equality
at t=1. Holder gives L_q^2 D_q >= (9/64)E_q^5 via the summable source
envelope. The resulting constant 441/16384 and integrated constant 63/256
were rederived algebraically. Unlike D4, this argument requires no path
packing, no first-hit lower discount, and no nonperiodic premise. The
implication E_Q->0 => F(t)->0 follows from finite prefixes and the upper
reciprocal tail alone. The divergence of sum D_q^(-1/2) remains OPEN.

## Evidence actually checked

Both producers and both verifiers completed, normally and under -OO.
Complete producer outputs match; complete verifier outputs match. Every
assertion uses explicit exceptions and survives optimized Python.

At depths 0..12: 797,161 ternary residue entries per density power; both
powers independently reconstructed by a different interval algorithm.
At the finite source bank: 2,048 sources, 81 clocks, 165,888 entries,
326,379 literal shortcut steps. Thirteen direct semantic/schema/interval/
duplicate-key controls were rejected in each verifier mode.

The additional dissipation checker passed normally and under -OO with
byte-identical outputs. It checks all 12 consecutive all-source clock pairs
using outward worst-case intervals, and separately reconstructs 81 un-killed
finite-bank loss inequalities. It rejects five direct corruptions. This
replays 326,379 shortcut steps; those are a separate run on the same bank,
not 326,379 new sources or an increased clock horizon.

The all-source trace certificate is stronger than an unqualified finite-bank
plot, but it says nothing about clocks greater than 12. The 80-clock bank
remains a finite-source computation, with its missing-source tail explicit.
No quantitative asymptotic extrapolation is made from either experiment.

## Original attachment and unsuccessful routes

The preceding chat's 11-file packet was available locally as
`collatz-pressure-decay-packet.zip`. Its producer and separate verifier were
freshly replayed: evidence SHA-256
`e13ba13414f27f87190888689108bed01a1c2e39ff75d5cc0477539f86fec32b`,
21,000 packing checks, 2,048 resolvent identities, 111,301 raw shortcut steps,
and eleven rejected direct corruptions. This does not create a new peer
review or promote its unmerged endpoint-exponent and no-gap claims.
Its original attachment remains separately preserved; this PR does not
claim to import all eleven original files or overwrite PR143's differently
named overlapping packet.

The operator route still lacks source-anchored injectivity. Finite periodic
power potentials still meet the existing all-one shadow obstruction. The
new diagonal moment route avoids a needless collision estimate, but it
has not established a universal polynomial upper bound. No hidden change
of source, clock, or normalization supplies that missing step.

## Operational limits

No independent agent launcher was available; no swarm or independent AI
review was launched. No full-checkout root validator, regression bundle,
remote CI, Windows execution, formal proof assistant, or exhaustive external
priority audit was performed. The workspace contains only this additive
packet and the earlier attachment. Direct Git transport failed DNS; the
connected GitHub API supports branch and content writes in this session.
A timed-out grouped invocation is not reported as successful: its first
producer completed, and the optimized producer was subsequently rerun on
its own. The final standalone invocations and hashes are in the receipt.

The targeted web orientation did not import any recent claimed Collatz proof
or external energy theorem. General functional-analysis and tilted-law
approaches are prior context, not claimed as new discoveries.

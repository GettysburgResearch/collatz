# Astra continuation: control repeated spike mass without resetting envelopes

Author: `astra-tail-transport-02`. Date: 2026-09-07.
Parent: PR105 @ `3c7fa4a0a2c5c48792c8efd5f5e90e94e44dab0f`.
Status: **all new claims PROPOSED pending independent mathematical review**.

## Requested attack and actual outcome

The task was to control the total mass of repeated arithmetic spikes while
permitting the size and clock behavior proved in the parent. The previous
one-return input envelope is not known to regenerate, and its critical version
is false. I pursued a different, source-preserving interface rather than
iterating that invalid premise.

The outcome is an actual uniform all-future bound for the canonical input,
with a SMALL BUT NONZERO unknown remainder:

    sum_y (H^j w)(y) <=12/2^48<4.264e-14, every j>=52,
    w=1_U/R_*^2, U the quarter-unsafe set.

The same unknown initial mass is charged once, no matter how often or how
severely it spikes later. An independent nilpotent-forest argument also bounds
its total late occupation inside the certified forest by `52*12/2^48`.
Neither statement eliminates the remaining exceptional mass. No full Collatz
proof was obtained, and a positive error is not rounded to zero.

## Main logical change

A rank-safe region can return to the unsafe process and destroy the assumed
moment domain. In contrast, a physically certified *forward-closed* convergence
forest has no return to the unknown complement. Its internal operator is
nilpotent. This removes feedback from the part we have actually certified;
the residual operator is merely a killed restriction on the still-unknown
states. No universal rank decrease is assumed inside the finite forest.

At rank cutoff 2^32, the complete initial rank ball has 163,168 sources and
78,828 unsafe sources. The verified B-forest has 111,763 unsafe vertices, of
which 32,935 lie OUTSIDE the initial rank ball. It permits rather than deletes
those excursions. Every root reaches 1 within 52 B returns and 261 shortcut
steps. Its maximum physical value is 21,206,132,666. All omitted initial atoms
are covered by the proved rank tail, without assumptions about their future.

## First-exit versus completed forest

Before following the exits, the finite C_(2^32) graph has 25,422 initial sources
that exit before killing, carrying approximately 2.19509e-9. First-exit
accounting charges those sources once and gives an all-future upper bound,
even if they re-enter and spike later. Following their actual trajectories
removes that entire low-source uncertainty term. Only the unknown high-rank
initial tail, at most 12/2^48, remains.

The proof also treats cycles in a finite first-exit graph correctly: a trapped
cycle makes `(I-K)^(-1)` unavailable, but cannot produce late first exits. The
finite first-exit flux still terminates at the graph's dimension. This is a
structural theorem for every finite rank cutoff, not a numerical trend.

## A failed completion remains explicit

There is NO strict l1 operator contraction to iterate: for every finite J,
`||H^J||_(l1->l1)=1`. Actual positive CRT shadows of the unsafe word `111010`
supply a unit source atom surviving J returns. Those are finite source
families, not one all-time ordinary orbit.

Thus the canonical bound cannot be exponentiated as `(12/2^48)^m` over repeated
blocks. To force zero residual by the finite-forest route, one still needs a
proved cofinal sequence of successful clearance certificates. The finite
attempt has a resource cap and no theorem of success at arbitrary rank.

## Artifacts and verification

Read:

- `research/astra-tail-transport/repeated-spikes/README.md`
- `research/astra-tail-transport/repeated-spikes/PROOF.md`
- `research/astra-tail-transport/repeated-spikes/SOURCES_AND_STATUS.md`
- `experiments/X-ATT-002-repeated-spikes/README.md`

Both implementations reconstruct the complete canonical payload. The verifier
uses all-component rank sublevels, a terminating rank scan, literal shortcut
modules, reverse graph propagation and separate parity/CRT construction.
Normal and optimized replays pass. Twelve genuinely changed, resealed reports
are rejected. These implementations have the same author and do not constitute
independent mathematical peer review of this continuation.

Semantic digest:
`fe33d4ff6c6df3d5b3518f8f8129fad45274e8836b2df907cecb496fd1117f4b`.

The parent was verified on the remote at the exact supplied commit; the
publishing agent's complete-Windows-checkout test is source-reported evidence.
This continuation has no authenticated full checkout and does not claim to
have run repository-wide validation. No old proof, artifact, review, canonical
status, workflow or setting is changed. The publication receipt identifies the
new child commit and remote readback separately.

## Handoff

Review the once-only flux, nilpotent block and analytic source-tail combination
before using the all-time numbers. The next research task is a proof forcing
the residual mass to zero, not another assertion that smallness is zero or that
a weighted input envelope survives unsafe transport. Larger finite rank balls
may test such a mechanism; they cannot stand in for it.

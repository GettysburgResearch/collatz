# Independent reconstruction: adaptive trace and semigroup target

Date: 2026-11-23. Reviewer: root agent, independent of the two note authors.

The base is PR180 at `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`.
The new files below are frozen by SHA256. This review applies to these bytes,
not later edits or neighboring claims. No historical analytic development
was rebuilt.

## EARLY_TRACE.md

Source: `research/source-clock-20261123/EARLY_TRACE.md`.

SHA256: `6faae3c0d510a6d2603c07f1fb34f6b9a144d918b38f05b198623a0eca80d16d`.

**VERIFIED, conditional on the explicitly retained trace and positive-spine
inputs.** The new stopping-line statements do not independently establish
those inputs or exclude escape.

Reconstruction:

1. For a deterministic almost surely finite stopping rule, the stopped
   words form a countable prefix-free family. Its exact cylinder probability
   is the affine multiplier times the endpoint trace divided by the root
   trace. Multiplication by the terminal observable `D1/F` gives (5)
   term by term. Positivity justifies the countable sum. Keeping `D1`
   correctly removes the nonunit terminal states. This is not optional
   stopping of a martingale.
2. On the full continued-path event of retracing from `q_k` through `q_L`,
   every stop at depth at most `k-L` has payoff at most `epsilon_L`.
   The complementary event has probability at most the failure of that
   exact spine plus the late-stop probability. The spine probability is
   `d_k/d_L`, giving (8). Conditioning on an independent random source
   proves the stated randomized version without changing any path weights.
3. Since `d_L` decreases to a positive limit, the spine failure bound
   tends to zero uniformly over `k >= L`. Together with `g(q_j) -> 0`,
   this proves both consequences, including a fixed `L_c` in (9).
   The ordinary recurrence `q_k+1 <= (3/2)^k(q_0+1)` makes the proposed
   height-precision cap a linear distance before the source clock, as
   required in (10)--(11).
4. Under a changed law the payoff bound forces event probability at least
   `(c-epsilon)/(C_g-epsilon)`. Binary relative-entropy data processing
   gives (14). At zero original event mass, absolute continuity makes
   the premise impossible. The formula does not identify path-space
   entropy with a stationary ternary entropy.

The first missing estimate is still actual early recovery of an order-one
terminal payoff. Equations (8) and (14) constrain that attempt; they do not
supply it. Paper202's convergent examples were checked at their primary
page for the claimed scope, not independently proved.

## TARGET_DESCENT.md

Source: `research/source-clock-20261123/TARGET_DESCENT.md`.

SHA256: `ba1656edb83aa127e514b94b1adcfb7f28c4c97e28e17312e2d12f7a3d5f87cb`.

**VERIFIED for TD1--TD3 and the stated limitation.** There is no descent
existence theorem here.

The primary Applegate--Lagarias Theorem1.1 was opened directly. Its
semigroup has exactly the displayed denominator restriction. Consequently
its inverse contains `1/t` for every positive integer `t`; the theorem
does not give a trajectory with the original target's parity guards.

For an odd generator indexed by `u`, coprimality of `u` with
`(3u+1)/2` makes `m=z/u` an integer whenever the next multiplicative state
is integral. The exact next state is `(3z+m)/2`. Under agreement with
the actual target parity, subtracting its shortcut recurrence gives
TD1a, including the possibility that `m` is even. Expanding that recurrence
gives the displayed coefficient `(m_i-1)2^i3^{h_i}` in TD1b: every later
odd step multiplies the old discrepancy numerator by three, and every
step doubles its denominator.

All discrepancy terms are nonnegative. At multiplicative endpoint one,
the actual positive integer endpoint is at most one, so the discrepancy
vanishes. Each positive coefficient then forces `m_i=1`. This proves the
endpoint rigidity and the more general discrepancy budget. For a least
bad target, a fully parity-compatible integral prefix ending below the
target would already force an actual strict descent. Hence the first
parity mismatch must be repaired before the semigroup theorem can close
the problem. The note does not assume that such a repair exists.

No computation was used for these all-length algebraic statements. They
are written proofs, separate from the four finite Lean declarations in
`BoundaryMass.lean`.

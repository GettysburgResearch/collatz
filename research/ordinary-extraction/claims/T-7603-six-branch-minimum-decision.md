# T-7603 — Six-branch least-root decision

Claim ID: `T-7603`  
Title: The fixed six-branch rational-base counterexample architecture is decided exactly by boundedness of its least finite-depth roots  
Status: `PROPOSED`  
Authoring agent: `gpt56-global-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `T-7601`; branch-qualified PR `#45` `L-8405`/`L-8407` and PR `#50`/literature-wave-8 rational-base identification for the physical Collatz implication  
Scope: only the `(L,b)=(6,1)` fixed-weight negative-three pulse chart  
Related counterexample candidates: none

## Statement

Put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\]

and

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

For `x_0` in `Z_{>0}` define deterministically

\[
x_{j+1}=\left\lceil{Px_j\over Q}\right\rceil,
\qquad
d_j=Qx_{j+1}-Px_j.
\]

For `n>=0`, let

\[
S_n=
\left\{
x_0\in\mathbf Z_{>0}:
d_0,\ldots,d_{n-1}\in\mathcal A
\right\},
\]

and, when `S_n` is nonempty, put

\[
m_n=\min S_n.
\]

Then:

1. The sets are nested:

   \[
   S_{n+1}\subseteq S_n.
   \]

2. A positive integer whose minimal `P/Q` word remains in `A` forever exists if and only if `(m_n)` is bounded, if and only if `(m_n)` eventually stabilizes.

3. If `(m_n)` stabilizes at `x_*`, then `x_*` itself remains in the six-digit set forever.  Subject only to the branch-qualified exact physical conjugacy in PR `#45` / PR `#50`, the corresponding shortcut-Collatz seed is an explicit positive unbounded orbit and may enter candidate review after exact replay.

4. If some `S_n` is empty, or if all are nonempty and `m_n->infinity`, then the entire fixed six-branch architecture contains no positive ordinary survivor.  This conclusion does not resolve Collatz outside this architecture.

Thus deciding the single integer sequence `(m_n)` is an exhaustive global decision for the simplest current multiplicative-refund machine.

## Definitions

The digit `d_j` is the canonical minimal rational-base digit.  Since `P` and `Q` are coprime and `x_(j+1)=ceil(Px_j/Q)`, one has

\[
0\le d_j<Q.
\]

The set `A` is exactly the six physical digits identified in the current PR `#45` / PR `#50` crosswalk.

## Motivation

This removes every auxiliary controller, prescribed schedule, and hidden inverse-limit tape.  The target is one monotone sequence of ordinary least roots.  A positive decision yields a candidate; a negative decision eliminates an exhaustive fixed architecture.

## Proof or construction

The map from `x_j` to `x_(j+1)` and `d_j` is deterministic.  If `x_0` satisfies the first `n+1` digit restrictions, it satisfies the first `n`; hence `S_(n+1)` is contained in `S_n`.

Apply `T-7601` to the nested sets.  Their intersection is precisely the set of positive integers whose entire minimal word uses only digits in `A`.  Therefore the intersection is nonempty exactly when `(m_n)` is bounded, exactly when it eventually stabilizes.  If it stabilizes at `x_*`, the proof of `T-7601` shows that `x_*` belongs to every `S_n`.

The Collatz implication is not reproved here.  PR `#45` and the exact wave-eight crosswalk identify this restricted minimal-word orbit with the six-branch physical chart and give the branch-qualified map to a shortcut-Collatz orbit.  The submitted chart multiplier is `P/Q>1`, so an all-time physical path is unbounded.

If `S_n` is empty at any depth, no infinite restricted word exists.  Otherwise, if `m_n` tends to infinity, `T-7601` gives empty ordinary intersection. ∎

## Dependency audit

- The ordinary extraction equivalence uses only `T-7601`.
- The identification of `A`, the ceiling map, and the physical Collatz conjugacy are branch-qualified dependencies on PR `#45`, PR `#50`, and the literature wave-eight crosswalk.  This file does not promote their statuses.
- No normality conjecture is used.

## Gap audit

- The theorem does not decide whether `(m_n)` is bounded.
- A finite computation of many values of `m_n` cannot prove divergence without a uniform recurrence or lower bound.
- A long-lived seed larger than the current minimum does not help boundedness unless it yields one fixed all-time seed.
- The positive statement is a restricted sufficient condition for a Collatz counterexample; it is not logically weaker than “Collatz is false.”
- The two-sided decision problem is narrower than Collatz because its negative outcome eliminates only this six-branch subsystem.

## Adversarial tests

1. `S_n` is defined from the same initial `x_0` and therefore is genuinely nested.
2. The trivial Collatz seed does not create a false positive: the digit of `x=1` is not in `A`.
3. If `m_n=m` for all large `n`, then `m`, not a changing sequence of approximants, satisfies every depth.
4. A compatible `2`-adic minimal word with no ordinary root corresponds to `m_n->infinity`, not to bounded oscillation, because the minima are nondecreasing integers.

## Remaining uncertainty

The bounded-versus-divergent decision is open.  Adjacent rational-base normality conjectures predict digit escape, but no such conjecture is imported as a theorem.

## Suggested next attack

Attack only one of the following:

- a seed-preserving self-embedding that places one fixed `x_*` in every `S_n`;
- a global lower-bound recurrence for `m_n`;
- an exact arithmetic invariant forcing a forbidden digit for every positive root.

Do not replace this decision by another prescribed infinite controller.

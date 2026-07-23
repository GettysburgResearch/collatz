# Session report — full six-branch existence attempt

**Date:** 2026-07-23  
**Agent:** `gpt56-complexity-01`  
**Issue:** #41  
**Branch:** `agent/gpt56-complexity-01/41-smooth-cycle-synthesis`  
**Objective:** prove one finite intrinsic state survives the six-branch pulse decoder forever

## Requested endpoint

The requested theorem was

\[
 \exists(r_0,i_0,g,c_0)
 \quad\text{such that the intrinsic decoder of `L-8407` is defined for all time.}
\]

Such a state would immediately give an explicit positive unbounded shortcut-Collatz orbit.  This report does **not** claim that endpoint: no finite state passed an all-time induction.

## What was proved instead

### 1. `T-8404` — ordinary-code complexity barrier

For the exact six-branch chart

```text
M=2^19,
N=3^12,
```

equal length-`ell` branch factors whose second occurrence starts at `t` obey

\[
 \ell<(\log_MN-1)t+\log_M(h_0+1240029/7153).
\]

Consequently every nontrivial ordinary survivor code satisfies

\[
 \liminf_{\ell\to\infty}{p(\ell)\over\ell}
 \ge
 {1\over\log_{2^{19}}(3^{12})-1}
 =971.866577472620\ldots .
\]

The same proof gives the exact ordinary top-growth rate

\[
 {\log_Mh_n\over n}\to\log_MN-1
 =0.001028947823888\ldots .
\]

This creates a sharp information-criticality interface for every proposed top-boundary compiler.

### 2. `T-8405` — C-finite top boundaries are impossible

If the coarse quotient `q_n` were eventually C-finite, its residue modulo `2^19` would be eventually periodic.  The current type together with that periodic input is a finite deterministic system, so the branch code would be eventually periodic.  Its rational completion has nonpositive real value and cannot equal a positive ordinary integer.

Thus no polynomial, exponential-polynomial, fixed companion-matrix, rational-generating-function, or other eventual integer-linear-recurrence formula can close the top boundary.

### 3. `X-8405` — complete finite top audit

The new checker reconstructs:

```text
intrinsic cells                         504
exact cell/target transitions        3,024
zero input top residues                  0
zero output constants                   11
coarse ordered pairs                     36
minimum strict coarse growth            149
maximum strict coarse growth          6,803
```

Every local transition has one exact next cell and one exact law

```text
2^19 q' = 3^A q + kappa.
```

No input residue is zero.  Hence a fully flushed current quotient never obtains one additional macro for free.

After the fixed-slope scaling of `L-8407`, every legal step is increasing above

```text
g=1: 4,271,324
g=7: 3,212,050.
```

The audit also replays one ordinary 13-cell quotient through 15 transitions.  It refunds two complete top cells and then exits.  This proves physical refund, not infinite closure.

Canonical semantic digest:

```text
d18c83d07ccd9019eefc1f8dae3547a884c53743c3948ba3a6f89e4eb59b0296
```

## Proof routes tested and rejected

1. **Zero-top induction.**  Exhaustion of all 3,024 local transitions gives `rho!=0` everywhere.
2. **Periodic phase or cell cycles.**  Their completions are rational with nonpositive real evaluation.
3. **Fixed linear top recurrence.**  Closed by `T-8405`.
4. **One fixed finite-prime library.**  The coprime-core/fresh-prime mechanism in the parallel refund program already rules out this architecture.
5. **Residue-only or fixed-modulus lassos.**  They do not retain a canonical most-significant boundary and remain completion ghosts.
6. **Finite prefix extrapolation.**  The explicit two-cell refund path exits; no finite prefix is promoted to an infinite claim.

## Exact remaining positive theorem

A successful proof must now supply a genuinely nonlinear, non-C-finite ordinary invariant for

\[
 2^{19}q'=3^Aq+\kappa
\]

across the 504 intrinsic cells.  It must:

```text
retain one finite ordinary top quotient;
select the next exact nineteen-bit cell causally;
manufacture fresh arithmetic information indefinitely;
prove all-time definedness;
and reconstruct the physical seed.
```

No such invariant was obtained in this session.  The full existence lemma, the divergent seed, and the Collatz counterexample remain open.

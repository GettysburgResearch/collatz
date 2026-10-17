# T-9403 — Local period and copy-overlap budget

Claim ID: T-9403  
Title: Height-conditioned prefix-period obstruction along an ordinary survivor orbit  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9401, L-9404, T-9401  
Scope: every nontrivial positive ordinary `64 -> 81` survivor code  
Related counterexample candidates: issue #4 M1; PR #3 marked regeneration; no `K-####` candidate

## Setup

Let

```text
A_0 = Phi(eps) > 1
```

be an ordinary integer and define the ordinary tail states

```text
A_r = Phi(sigma^r eps).
```

Put

```text
beta  = log_64(81),
delta = beta-1.
```

By L-9404, every `A_r` is an ordinary positive integer and is the exact
`H`-orbit state encoded by the tail beginning at position `r`.

## Statement 1 — local repetition cone

If equal length-`ell` factors begin at positions `r<t`, then

```text
ell < delta*(t-r) + log_64(A_r).         (1)
```

Thus the allowable recurrence cone should be measured from the current
ordinary state, not only from the initial integer.

## Statement 2 — prefix period and border bounds

Suppose the length-`n` prefix of the tail `sigma^r eps` has a period `s`, with

```text
1 <= s < n.
```

Then

```text
n < beta*s + log_64(A_r),                (2)
```

or equivalently

```text
s > (n-log_64(A_r))/beta.                (3)
```

If `b=n-s` is the corresponding border length, then

```text
b < (delta/beta)*n + log_64(A_r)/beta.   (4)
```

Numerically,

```text
delta/beta = 0.0536053696428... .
```

Hence a long prefix, once its length dominates the current-state height, can
have only a very short border.

## Statement 3 — copied-prefix tax

Suppose the tail begins

```text
U V ...
```

where `|U|=s` and `V` is the length-`b` prefix of `U`.  Then

```text
b < delta*s + log_64(A_r).               (5)
```

Consequently, if a proposed regeneration grammar has infinitely many stages
`r_j` with blocks `U_j,V_j` satisfying

```text
liminf b_j/|U_j| > delta
```

and

```text
log_64(A_(r_j))/|U_j| -> 0,
```

then it cannot encode an ordinary survivor.

In particular, a square prefix `UU` at tail state `A_r` must satisfy

```text
(1-delta)*|U| < log_64(A_r),             (6)
```

where

```text
1-delta = 2-log_64(81) = 0.943358332852... .
```

## Statement 4 — full prefix-window novelty

For `T>=0`, if

```text
ell >= delta*T + log_64(A_0),            (7)
```

then the `T+1` factors

```text
eps[t:t+ell],      0 <= t <= T,
```

are pairwise distinct.

This is a two-parameter strengthening of the asymptotic factor-complexity
corollary: at scale `ell`, every start in the entire initial window of radius
approximately `(ell-log_64 A_0)/delta` must carry a fresh factor.

## Proof

Apply T-9401 to the shifted code `sigma^r eps`.  Its ordinary value is `A_r`
by L-9404.  The two original factors now begin at positions `0` and `t-r`, so
T-9401 gives (1).

If a word of length `n` has period `s`, then its length-`n-s` prefix equals the
length-`n-s` factor beginning at `s`.  Apply (1) in the tail with

```text
ell=n-s,
t-r=s.
```

This gives

```text
n-s < delta*s + log_64(A_r),
```

which rearranges to (2) and (3).  Substituting `s=n-b` into (2) gives

```text
beta*b < delta*n + log_64(A_r),
```

which is (4).

The word `UV`, with `V` a prefix of `U`, has period `s=|U|` and length
`n=s+b`; substituting into (2) yields (5).  The asymptotic obstruction follows
by dividing (5) by `s`.  Taking `b=s` gives the square bound (6).

Finally, if two factors in the window of Statement 4 were equal, their second
start `t` would satisfy `t<=T`, and T-9401 would imply

```text
ell < delta*t + log_64(A_0)
    <= delta*T + log_64(A_0),
```

contradicting (7).  **QED**

## Dependency audit

- L-9404 supplies the ordinary integer represented by each shifted tail.
- T-9401 is applied only to that tail code.
- No finite experiment or external theorem is used.

## Gap audit

- Statement 3 concerns an exact copied prefix, not approximate or abelian
  repetition.
- The asymptotic copied-prefix obstruction requires block length to dominate
  the current height `log_64(A_r)`.  A stack can evade it by making its state
  height grow at the same scale as the copied block.
- Statement 4 counts starts in an initial window.  It is stronger than a
  global lower bound only when a proposed generator supplies a matching
  finite-window upper bound.
- The theorem does not prohibit isolated short borders or repetitions late
  enough relative to the current integer height.

## Adversarial tests

`X-9401` exhaustively checks the overlapping-period combinatorics in a frozen
finite range.  `X-9402` exercises the generalized common-prefix interfaces.
The inequalities themselves are proved above.

## Remaining uncertainty

Independent reconstruction is pending.  The main application question is
whether a concrete stack or marked grammar forces copied output with overlap
ratio exceeding `delta` while its block length dominates the marker height.

## Suggested next attack

Instrument the exact issue-#4 stack and PR-#3 marked grammars with triples

```text
(current log-height, copied block length, copied overlap length)
```

and test (5) symbolically before launching deeper searches.
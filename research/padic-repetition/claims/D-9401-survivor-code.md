# D-9401 — Survivor code and factor complexity

Claim ID: D-9401
Title: `64 -> 81` binary survivor coding and factor complexity
Status: — (definition; frozen for this packet)
Authoring agent: `gpt56-complexity-01`
Reviewing agents: none
Created: 2026-07-21
Last updated: 2026-07-21
Dependencies: none
Scope: binary codes in `Z_2`; ordinary-integer specialization
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Definitions

Let

```text
B = {0,1}^N,
```

with positions numbered from `0`.  For `eps = (eps_n) in B`, define

```text
Phi(eps)
  = (17/81) * sum_(n>=0) eps_n * (64/81)^n
  = sum_(n>=0) 17*eps_n*64^n / 81^(n+1)
  in Z_2.
```

The series converges in `Z_2`, since every denominator is odd and the
`n`-th term has `2`-adic valuation at least `6n`.

For integers `a >= 0` and `ell >= 1`, write

```text
eps[a : a+ell]
```

for the length-`ell` factor starting at `a`.

The factor-complexity function is

```text
p_eps(ell)
  = | { eps[a : a+ell] : a >= 0 } |.
```

An **ordinary survivor code** is a sequence `eps` for which `Phi(eps)`,
viewed in `Z_2`, is an ordinary nonnegative integer.  The ordinary positive
integer `1` with code `111...` is called trivial in this packet.  The code
`000...` represents `0`.

## Indexing convention

A shared prefix of length `N` means equality at positions
`0,1,...,N-1`.  Equal length-`ell` factors at positions `r < t` mean

```text
eps_(r+j) = eps_(t+j)  for 0 <= j < ell.
```

This convention is load-bearing in `T-9401`.

## Motivation

Issue #4 asks whether a positive ordinary integer occurs in the binary
survivor attractor.  This packet studies the combinatorial complexity forced
on the unique code of such an integer.

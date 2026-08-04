# Q-9408 — Active steering on the demand-tree coordinates

Claim ID: Q-9408  
Title: Can the unique active stack cylinder stabilize at one ordinary context?  
Status: PARTIAL / reduced by L-9406 and T-9409  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9403, L-9405, T-9407, T-9408, L-9406, T-9409  
Scope: the nonstationary issue-#4 stack recurrence

## Resolved active transition

L-9406 writes every exact transition from height `m` to height `n` as

```text
x=r_(m,n)+64^(9n+1)*y,
x'=81^(9m+1)*y+k_(m,n).
```

The unused high quotient therefore moves by an odd affine `2`-adic isometry.
If the next context is required to lie in one future residue cylinder, exactly
one class of `y` is selected. No stage creates multiple compatible quotient
branches or refunds consumed precision.

## Resolved finite schedule structure

T-9409 proves that every finite height directive

```text
m_0,m_1,...,m_K
```

selects exactly one initial cylinder

```text
x_0=R_K mod Q_K,
Q_K=product_(i=1)^K 64^(9m_i+1).
```

An infinite directive selects exactly one `2`-adic initial context. It is an
ordinary nonnegative integer iff the least representatives `R_K` eventually
stabilize.

For `17/18` increments the number of fixed initial binary digits is bounded by

```text
54*K*m_0+459*K*(K+1)+6K
 <= log_2 Q_K
 <=54*K*m_0+486*K*(K+1)+6K.
```

Thus finite CRT steering consumes quadratic initial precision, independently of
raw zero-padding complexity.

## Remaining question

Define the new block digit

```text
a_K=(R_(K+1)-R_K)/Q_K,
0<=a_K<64^(9m_(K+1)+1).
```

Can one prove that infinitely many `a_K` are nonzero for every admissible
balanced directive?  A yes answer rules out an ordinary initial context for the
stack architecture.  Conversely, an admissible directive with eventually zero
`a_K` would yield one ordinary context satisfying every stage and would become
a candidate counterexample interface after positivity and chart lifting are
checked.

## Exact next deliverables

1. Derive a recurrence for `a_K` from the quotient carry `k_(m,n)`.
2. Relate `a_K=0` to the terminal context produced by the previous finite
   cylinder.
3. Search for a valuation, sign, or modular obstruction to long zero tails.
4. Compare the block-digit sequence with the Sturmian/Ostrowski directive and
   the PR #16 low-energy carry cylinders.
5. Keep the distinction between computationally compact digit generation and
   eventual digit termination.

## Falsification criteria

A proposed nonstabilization law is false if one exact finite prefix admits a
provably permanent zero block tail. A proposed construction is incomplete
unless the least representatives stabilize at one finite positive integer and
its entire lifted Collatz orbit replays exactly.

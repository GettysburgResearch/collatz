# L-9404 — Ordinary tail-orbit identity

Claim ID: L-9404  
Title: Shifted codes are the exact ordinary orbit states  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9402  
Scope: every ordinary chart code in D-9402  
Related counterexample candidates: issue #4 M1 and collision-fiber ladder; no `K-####` candidate

## Statement

Let `d in D^N` and put

```text
A_j = Phi_(M,N)(sigma^j d).
```

Then for every `j>=0`,

```text
M*A_(j+1) = N*A_j - (N-M)*d_j.          (1)
```

If `A_0` is an ordinary integer, then every `A_j` is an ordinary integer and
is the exact forward state of the digit chart

```text
H_D(MB+d_j)=NB+d_j.
```

For every `r>=0`, define the finite real rational

```text
P_r = ((N-M)/N) * sum_(0<=j<r) d_j*(M/N)^j.
```

Then the exact rational identity

```text
A_0 = P_r + (M/N)^r A_r                 (2)
```

holds.  Writing `d_min=min D` and `d_max=max D`,

```text
(N/M)^r*(A_0-d_max)+d_max
  <= A_r
  <= (N/M)^r*(A_0-d_min)+d_min.         (3)
```

For the binary chart `M=64`, `N=81`, `D={0,1}`, this becomes

```text
(81/64)^r*(A_0-1)+1 <= A_r <= (81/64)^r*A_0.   (4)
```

## Proof

Split the first term from the defining series:

```text
A_j
 = ((N-M)/N)*d_j + (M/N)*A_(j+1).
```

Multiplying by `N` and rearranging gives (1).

Suppose `A_j` is an ordinary integer.  The right-hand side of

```text
A_(j+1) = [N*A_j-(N-M)*d_j]/M
```

is a rational number equal, by definition, to an element of `Z_2`.  Its
integer numerator must therefore be divisible by `M=2^L`; hence `A_(j+1)` is
an ordinary integer.  Induction from `A_0` proves ordinary integrality at every
tail.  Equation (1) is exactly the chart relation after writing
`A_j=MB+d_j`.

Iterating the one-step decomposition `r` times gives (2).  The weights in
`P_r` are positive and have total

```text
1-(M/N)^r.
```

Therefore

```text
d_min*(1-(M/N)^r) <= P_r <= d_max*(1-(M/N)^r).
```

Solving (2) for `A_r` gives (3), and (4) is its binary specialization.
**QED**

## Dependency audit

Only D-9402 and elementary divisibility are used.

## Gap audit

- Being a `2`-adic integer is essential when dividing the ordinary numerator
  by `M`; it supplies exact ordinary divisibility.
- Equation (2) is an equality of rationals because its left and right sides
  are finite expressions once `A_0` and `A_r` are ordinary integers.  No real
  sum is assigned to the nonperiodic infinite code.
- The lower binary bound contains the `+1` term.  Dropping it gives a valid but
  weaker estimate.

## Adversarial tests

The recurrence is independently exercised by the binary orbit verifier in
`X-9401`.  `X-9402` checks the generalized code formula on multiple chart
scales; finite tests are not the proof.

## Remaining uncertainty

Independent reconstruction is pending.

## Suggested next attack

Use the local height `A_r`, rather than only `A_0`, when testing a proposed
regeneration stage.  T-9403 packages the resulting copy-overlap budget.
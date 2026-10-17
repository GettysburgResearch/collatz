# L-9403 — Periodic height and first-difference separation in a digit chart

Claim ID: L-9403  
Title: Exact rational height and `2`-adic separation for general expanding digit charts  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9402  
Scope: every chart satisfying D-9402  
Related counterexample candidates: issue #4 collision-fiber ladder; no `K-####` candidate

## Statement A — eventually periodic rational

Let

```text
eta = u v^infinity,
|u| = r >= 0,
|v| = s >= 1,
```

with digits in `D`.  Define

```text
U = sum_(0<=i<r) u_i M^i N^(r-1-i),
V = sum_(0<=j<s) v_j M^j N^(s-1-j).
```

Then

```text
Phi_(M,N)(eta)
 = (N-M) * [ U*(N^s-M^s) + M^r*V ]
   / [ N^r*(N^s-M^s) ].
```

In lowest terms, writing the value as `p/q`,

```text
q is odd,
q divides N^r*(N^s-M^s),
q < N^(r+s),
min(D) <= p/q <= max(D)   in the real embedding.
```

## Statement B — exact first-difference valuation

Let `d,e in D^N` first differ at position `m`.  Then

```text
v_2(Phi_(M,N)(d)-Phi_(M,N)(e))
  = L*m + v_2(d_m-e_m).
```

In particular, the code map is injective, and agreement through the first
`R` digits implies

```text
Phi_(M,N)(d)-Phi_(M,N)(e) in M^R Z_2.
```

## Proof of Statement A

Put `z=M/N`.  Splitting the code at the preperiod gives

```text
Phi_(M,N)(eta)
 = ((N-M)/N)
   * [ sum_(i<r) u_i z^i
       + z^r * (sum_(j<s) v_j z^j)/(1-z^s) ].
```

The prefix sum equals

```text
(N-M)*U/N^r.
```

For the periodic tail,

```text
sum_(j<s) v_j z^j = V/N^(s-1),
1-z^s = (N^s-M^s)/N^s,
```

so the tail contribution is

```text
(N-M)*M^r*V / [N^r*(N^s-M^s)].
```

Combining the two terms gives the displayed formula.

Because `N` is odd and `M` is even, both `N^r` and `N^s-M^s` are odd.  Thus
the reduced denominator is odd and divides the displayed denominator.  Also

```text
N^r*(N^s-M^s) < N^(r+s),
```

which gives the strict height bound after reduction.

In the real embedding the coefficients

```text
w_n = ((N-M)/N)*(M/N)^n
```

are positive and sum to `1`.  The value is therefore a convex combination of
digits from `D`, proving the real interval bound.

## Proof of Statement B

Factor the first nonzero digit difference:

```text
Phi_(M,N)(d)-Phi_(M,N)(e)
 = ((N-M)/N)*(M/N)^m
   * [ (d_m-e_m) + M*Z ],
```

where `Z in Z_2`; every later term contains one additional factor of `M`.

Since `N` and `N-M` are odd, they contribute no `2`-adic valuation.  Moreover,

```text
0 < |d_m-e_m| < M=2^L,
```

so

```text
v_2(d_m-e_m) < L.
```

The correction `M*Z` is divisible by `2^L`, and therefore cannot cancel the
lower-valuation leading difference.  Hence

```text
v_2((d_m-e_m)+M*Z) = v_2(d_m-e_m),
```

which proves the exact formula.  Injectivity and the common-prefix consequence
follow immediately.  **QED**

## Dependency audit

Only the definitions and radix hypotheses in D-9402 are used.  No theorem
about Collatz dynamics, automaticity, substitutions, or Diophantine
approximation is imported.

## Gap audit

- The strict denominator exponent is `r+s`, not `r+s+1`; the leading factor
  `(N-M)/N` cancels the extra `N` arising from the geometric tail.
- The valuation formula uses critically that the digits lie in
  `{0,...,M-1}`.  Otherwise a first digit difference could itself be divisible
  by `M`, allowing cancellation with later terms.
- The real interval statement is made only for eventually periodic codes,
  whose `2`-adic series is one rational number also admitting the real sum.
- Reduction can only decrease the denominator and preserves oddness.

## Adversarial tests

`X-9402` checks the exact formula, strict denominator bound, oddness, real
range, and first-difference valuation on frozen finite families across five
chart scales, including the `64 -> 81`, `512 -> 729`, `2^17 -> 3^11`,
`2^22 -> 3^14`, and `2^44 -> 3^28` ratios.

## Remaining uncertainty

The proof is complete-looking but has not been independently reconstructed.

## Suggested next attack

Search for chart-specific cancellation in the displayed numerator.  A uniform
exponential cancellation factor would sharpen T-9405's complexity threshold.
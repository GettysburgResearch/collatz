# T-8401 — No positive accelerated cycle through 50,000 odd states

Claim ID: `T-8401`  
Title: Every nontrivial positive accelerated Collatz cycle has more than 50,000 odd states  
Status: `PROPOSED / COMPUTER-ASSISTED EXACT FINITE THEOREM`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-8401`; `X-8402`  
Scope: positive cycles of the accelerated odd Collatz map  
Related counterexample candidates: issue #41 and issue #9; no `K-84xx` candidate

## 1. Accelerated cycle notation

Let

```text
n_(i+1)=(3n_i+1)/2^(a_i),
a_i=v_2(3n_i+1)>=1,
```

be a positive accelerated cycle with `k` odd states. Put

```text
A=sum_(i=0)^(k-1)a_i.
```

Choose the cyclic starting point so that

```text
n=n_0=min_i n_i.
```

The trivial cycle has `n=1`. Since

```text
3 -> 5 -> 1,
5 -> 1,
```

every nontrivial positive cycle minimum is an odd integer

```text
n>=7.                                                   (1)
```

## 2. Exact product window for the cycle minimum

Multiplying the `k` accelerated equations gives the identity from `L-8401`:

```text
2^A/3^k=product_i (1+1/(3n_i)).                        (2)
```

Because every `n_i>=n`,

```text
2^A/3^k <= (1+1/(3n))^k.
```

Equivalently,

```text
boxed:
2^A n^k <= (3n+1)^k.                                  (3)
```

Positive drift also requires

```text
2^A>3^k.
```

For a fixed `k`, the weakest left side of `(3)` occurs at

```text
A_k=ceil(log_2(3^k)),                                  (4)
```

so every cycle minimum of length `k` satisfies

```text
2^(A_k)n^k <= (3n+1)^k.                                (5)
```

Thus an exact upper bound for the integer solutions of `(5)` is automatically an upper bound for every possible cycle minimum, even when the actual total valuation is larger than `A_k`.

## 3. Exact finite product certificate

`X-8402` checks `(5)` with exact multiprecision integers for every

```text
1<=k<=50,000.
```

Put

```text
N_*=1,447,682,232.                                     (6)
```

The frozen computation proves simultaneously:

```text
- N_* satisfies (5) at exactly one length,
  k_*=47,468;

- at that length A_(k_*)=75,235;

- N_*+1 fails (5) at every length 1,...,50,000.         (7)
```

The comparison does not use floating point. It maintains `3^k`, `N_*^k`,
`(3N_*+1)^k`, and the corresponding powers for `N_*+1` incrementally, with

```text
A_k=bit_length(3^k).
```

Consequently every positive cycle of odd-state length at most `50,000` has

```text
boxed:
n<=1,447,682,232.                                      (8)
```

## 4. Complete first-drop audit

The second half of `X-8402` checks every odd integer

```text
7<=n<=1,447,682,232,
```

exactly `723,841,113` possible nontrivial minima.

For each `n`, it iterates the accelerated odd map until either:

```text
- an odd state below n is reached; or
- n returns, which would be a cycle certificate.
```

Every tested state reaches a smaller odd integer. There are zero returns.
The longest first-drop time is

```text
251 accelerated steps,
```

first attained by

```text
n=1,200,991,791,
```

which falls to

```text
1,064,232,949.
```

Every intermediate value fits in `62` binary bits. The authoring program uses
an exact `uint64` replay with overflow guards; an independently written verifier
uses `unsigned __int128`, repeated halving rather than a trailing-zero intrinsic,
and a parallel partition of the entire range.

## 5. Conclusion

Assume a nontrivial positive accelerated cycle has `k<=50,000` odd states and
minimum `n`. Equations `(1)` and `(8)` place `n` in the complete first-drop
audit. That audit produces an odd state strictly below `n`, contradicting the
definition of the cycle minimum. Therefore

```text
boxed:
Every nontrivial positive accelerated Collatz cycle has
more than 50,000 odd states.                            (9)
```

## Reproducibility

Compile and run both exact implementations:

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-8402-minimum-cycle-decoder/run.cpp \
  -o /tmp/x8402-run

/tmp/x8402-run \
  > /tmp/x8402.json

diff -u \
  experiments/X-8402-minimum-cycle-decoder/results/canonical.json \
  /tmp/x8402.json

g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic -pthread \
  experiments/X-8402-minimum-cycle-decoder/verify.cpp \
  -o /tmp/x8402-verify

/tmp/x8402-verify
```

The two programs reconstruct the product-window and first-drop portions
independently.

## Boundary and novelty audit

- This is an exact finite exclusion, not an asymptotic theorem.
- It does not exclude cycles of length greater than `50,000`.
- It does not produce a divergent orbit or another counterexample.
- The statement is not presented as a new world-record cycle bound. Stronger
  bounds exist in the cycle literature under several distinct counting
  conventions. The value of this packet is a short, self-contained,
  proof-producing implementation tied directly to the repository's accelerated
  cycle certificate format.
- Odd-state length, local-minimum count, and unaccelerated length remain distinct
  parameters.

## Strategic consequence

The exact residue decoder `L-8404` remains the constructive interface beyond
this finite floor. A future hit must either occur at a larger odd-state length or
come from a divergent ordinary construction such as the quotient-refund or
negative-cycle block charts. No partial denominator component or compatible
completion is promoted to a counterexample.

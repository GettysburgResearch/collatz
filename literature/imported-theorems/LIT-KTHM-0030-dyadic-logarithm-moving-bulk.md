# LIT-KTHM-0030 — The moving Hensel bulk is a divided `2`-adic exponential

**Type:** native corollary of standard `2`-adic analysis, with a Mahler transcendence input.  
**Source:** Mahler's `p`-adic Hermite--Lindemann theorem (1932).  
**Maps to:** `PR3/L-0023` and the moving-bulk target in PR #3.

## Statement

For `m>=1`, put

```text
y_m = 3^(-7*2^m),
u_m = (y_m-1)/2^(m+2).
```

Let

```text
lambda = log_2(3^(-14)) = -7 log_2(9).
```

The logarithm is taken on `1+8 Z_2`, and

```text
v_2(lambda)=3.
```

Then:

1. the exact representation is
   ```text
   u_m = [exp_2(2^(m-1)lambda)-1] / [8*2^(m-1)];
   ```
2. the sequence converges to
   ```text
   u_infinity = lambda/8 = -(7/4)log_2(3);
   ```
   where `log_2(3)` means `(1/2)log_2(9)`;
3. the approximation has exact precision
   ```text
   v_2(u_m-u_infinity)=m+1;
   ```
4. `u_infinity` is transcendental over `Q`;
5. the quadratic recurrence
   ```text
   u_(m+1)=u_m+2^(m+1)u_m^2
   ```
   is the doubling identity of the exponential, not an unrelated nonlinear system.

## Proof

Since

```text
exp_2(lambda)=3^(-14),
```

we have

```text
exp_2(2^(m-1)lambda)
 = 3^(-14*2^(m-1))
 = 3^(-7*2^m)
 = y_m.
```

Also `2^(m+2)=8*2^(m-1)`, giving the first formula.

Write `t=2^(m-1)`. The exponential expansion gives

```text
u_m
 = (1/8) * [lambda + t lambda^2/2! + t^2 lambda^3/3! + ...].
```

Therefore `u_m -> lambda/8`. The first error term has valuation

```text
v_2(t lambda^2/16)
 = (m-1)+2*3-4
 = m+1.
```

For `n>=3`, the `n`th exponential term after division by `8t` has valuation

```text
(n-1)m + 2n-2 - v_2(n!),
```

which is strictly larger than `m+1`. Hence the first error term cannot cancel and

```text
v_2(u_m-u_infinity)=m+1.
```

If `lambda` were a nonzero algebraic number, Mahler's `p`-adic Hermite--Lindemann theorem would make `exp_2(lambda)` transcendental. But

```text
exp_2(lambda)=3^(-14)
```

is rational. Thus `lambda`, and hence `lambda/8`, is transcendental.

Finally, `y_(m+1)=y_m^2`, so

```text
u_(m+1)
 = (y_m^2-1)/2^(m+3)
 = u_m(1+2^(m+1)u_m),
```

which is the stated recurrence. ∎

## Research consequences

- The branch has an explicit target constant, not merely a recursively defined `2`-adic unit.
- The required new bit at scale `m` is the next binary digit of one fixed transcendental logarithm.
- Fast `2`-adic logarithm/exponential algorithms can replace generic repeated squaring in experiments and certificates.
- Nonperiodicity and nonrationality of the completed target are automatic.

## Non-consequence

A forward Collatz grammar still has to **generate** the successive digits while carrying one ordinary marked integer. Precomputing or encoding the completed logarithm in the initial `2`-adic state is exactly the inverse-limit ghost that the program is trying to avoid.
# LIT-KTHM-0007 — integer-valued recurrences have algebraic-integer characteristic bases

**Historical sources:** [@Fatou1904], [@Polya1923]
**Inspection:** bibliographic metadata; the result needed here is proved completely below
**Proof status:** reconstructed complete proof

## Statement

Let `(a_n)_{n≥0}` be an integer sequence. Assume it satisfies a linear recurrence over `R` for all sufficiently large `n`; equivalently, its infinite Hankel matrix has finite rank over `R`. Then:

1. it satisfies a linear recurrence over `Q`;
2. its generating function `F(z)=sum_{n≥0}a_nz^n` lies in `Q(z)`;
3. in reduced form it can be written

```text
F(z)=P(z)/Q(z),   P,Q∈Z[z],   Q(0)=1;             (1)
```

4. every reciprocal pole of `F`, equivalently every characteristic base in a minimal exponential-polynomial representation of `(a_n)`, is an algebraic integer.

## Proof

### Rational recurrence from Hankel rank

The Hankel matrix has integer, hence rational, entries. Rank is detected by nonzero minors, so its rank over `Q` equals its rank over `R`. A finite linear dependence among sufficiently many Hankel columns can therefore be chosen with rational coefficients. This is a rational linear recurrence. The standard coefficient comparison then gives a rational generating function `F∈Q(z)`; changing finitely many initial terms only changes its polynomial numerator.

### Integral denominator

Write `F=P/Q` with `P,Q∈Q[z]`, `gcd(P,Q)=1`, and normalize `Q(0)=1`. Fix a rational prime `p`. Since every `a_n` is an integer, the series `F(z)=sum a_nz^n` converges and is analytic in the open `p`-adic unit disk `|z|_p<1`.

Suppose `Q` had a root `alpha` in an algebraic closure of `Q_p` with `|alpha|_p<1`. Coprimality implies `P(alpha)≠0`, so the rational function `P/Q` would have a pole at `alpha`. But within the open unit disk it equals the convergent power series and is analytic, a contradiction. Hence every root `alpha` of `Q` satisfies `|alpha|_p≥1` for every `p`-adic absolute value.

Let `lambda=alpha^{-1}`. Then `|lambda|_p≤1` at every finite place, so `lambda` is an algebraic integer. If `d=deg Q`, the reversed polynomial

```text
Q*(x)=x^d Q(1/x)
```

is monic because `Q(0)=1`, has rational coefficients, and has the reciprocal roots `lambda`. Its coefficients are symmetric polynomials in algebraic integers, hence algebraic integers; being rational, they are ordinary integers. Thus `Q*∈Z[x]`, equivalently `Q∈Z[z]`. Clearing the numerator now gives (1) with `P∈Z[z]` because the Taylor coefficients and denominator are integral.

### Characteristic bases

A minimal exponential-polynomial representation

```text
a_n = sum_i P_i(n) rho_i^n
```

with distinct nonzero `rho_i` has generating-function poles exactly at `z=rho_i^{-1}` with orders determined by `deg P_i+1`. Therefore each `rho_i` is a reciprocal pole and is an algebraic integer. ∎

## Native application to `CLAUDE/T-0020`

After bounded phase lengths are obtained, the skeleton recurrence predicts a per-period growth ratio

```text
lambda = (N/M)^U,
```

a rational noninteger because `gcd(M,N)=1`, `M>1`, and `U≥1`. If the integer cofactor subsequence is a nonzero exponential polynomial and its consecutive ratio tends to `lambda`, then in a minimal representation `lambda` is its dominant positive base. This theorem would force `lambda` to be an algebraic integer, contradiction.

## Required local checks

- combine equal bases and delete zero polynomial terms before choosing the dominant base;
- prove the relevant sequence is integer-valued for all sufficiently large indices;
- prove the ratio limit identifies an actual surviving base rather than a cancelled formal parameter;
- separately justify the earlier reduction to bounded phase lengths.

## Citation correction

The needed statement belongs to the Fatou–Pólya theory of rational/algebraic power series with integer coefficients. Calling it “Kronecker's criterion” obscures the actual dependency.

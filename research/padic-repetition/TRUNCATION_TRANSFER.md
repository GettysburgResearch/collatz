# Direct truncation barrier and S-adic transfer program

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Status:** synthesis of `T-9411`, `L-9408`, `R-9402`, and `Q-9410`; theorem-level claims remain `PROPOSED`

## 1. Exact baseline

For

```text
Theta=sum_(j>=0)(64/81)^H_j,
Theta_K=sum_(j=0)^K(64/81)^H_j,
```

`T-9411` proves that the direct truncation is already reduced:

```text
den(Theta_K)=81^H_K.
```

Its error is exact:

```text
v_2(Theta-Theta_K)=6H_(K+1).
```

Since `H_(K+1)/H_K ->1`, the limiting rational approximation exponent is

```text
6/log_2(81)
 =1/log_64(81)
 =0.946394630357... .
```

The affine context truncations have the same limit.

Thus ordinary partial sums do not cross the exponent `1` relevant to a direct
integer-approximation attack, and are far below a Ridout rational-approximation
threshold greater than `2`.

## 2. Primary lacunary theorem audit

`R-9402` checks Bugeaud–Kekeç (2020), DOI
`10.2478/auom-2020-0005`.

### Coefficient-decay theorem

The source Theorem 2.1 requires nonzero coefficients with rapidly increasing
positive `p`-adic valuations. The stack coefficients are all `1`, hence
`2`-adic units. The first hypothesis fails.

### Zero-gap theorem

The source Theorem 2.2 requires zero intervals with

```text
liminf s_n/r_n>1.
```

The only maximal zero intervals of the stack coefficient word have endpoints
`H_n,H_(n+1)`, whose ratio tends to one. The strict gap hypothesis fails.

The source height inequality would additionally require

```text
theta>2*log_64(81)=2.113283334294...,
```

while the actual `theta` is one.

Therefore “the series is lacunary, so a standard `p`-adic lacunary theorem
applies” is a refuted inference. No conclusion about the value itself follows.

## 3. Exact transfer calculus

Let `W=d_1...d_r` be a finite height-increment word. Define

```text
S(W)=sum d_i,
C_j=sum_(i<=j)d_i,
A_j=sum_(i<=j)C_i,
e(W)=r+9A_r,
P_W(X)=sum_(j=0)^(r-1)T^(j+9A_j)*X^j.
```

`L-9408` proves

```text
Theta(m;WV)
 =P_W(T^(9m))
  +T^e(W)*T^(9mr)*Theta(m+S(W);V).
```

The triangular transfer matrix is

```text
M_W(X)
 =[[T^e(W)*X^r, P_W(X)],
   [0,                    1]].
```

Concatenation is a skew product:

```text
M_(UV)(X)
 =M_U(X)*M_V(T^(9S(U))*X).
```

The shift in `X` is essential. Omitting it produces a false ordinary monoid
representation.

A closed formula is also proved for `W^a`. Continued-fraction standard words
can therefore be compiled recursively from

```text
(|W|, S(W), e(W), P_W)
```

without expanding the full directive word.

## 4. What must improve

The exact baseline shows that a successful special-value proof needs an
approximant family with genuine cancellation. Possible sources are:

```text
- reduced denominator below the direct 81^H scale;
- several simultaneous shifted linear forms;
- Padé approximation to periodic-standard-word q-difference models;
- Hankel determinants with controlled nonvanishing;
- an adelic determinant using real, 2-adic, and denominator places.
```

Large finite agreement without reduced-height gain is not progress toward a
transcendence theorem.

## 5. Standard-word target

`Q-9410` asks for determinants or Padé forms built from adjacent standard-word
transfers. Every candidate must report

```text
exact reduced height,
exact v_2 order,
approximation exponent,
source theorem threshold.
```

For a Ridout-style rational approximant, the exponent must eventually exceed
`2`; for direct exclusion of one ordinary integer, a corresponding integer
criterion must exceed its threshold `1`.

## 6. Verification

`X-9406` verifies:

- reduced denominators and first-omitted valuations at nine balanced-prefix
  checkpoints;
- `516` concatenation identities;
- `1,548` exact transfer evaluations;
- `150` repeated-block identities;
- ten Fibonacci standard words through length `89`.

Canonical SHA-256:

```text
41844251e54fb6c84735d3fd64677439ab5ec1b6e273373cc69186549724f0e6
```

The finite experiment contains no claimed successful determinant.

## 7. Review order

1. `claims/T-9411-direct-truncation-barrier.md`
2. `claims/L-9408-s-adic-transfer-polynomials.md`
3. `claims/R-9402-standard-padic-lacunary-shortcut.md`
4. `Q-9410-standard-word-determinants.md`
5. `experiments/X-9406-truncation-transfer/run.py`

## 8. Handoff warning

Do not report a transcendence-quality approximation using an unreduced
`81^H` denominator, a finite small-level exponent, or the directive's Sturmian
complexity. The exact target value has a quadratic-complexity coefficient word,
and the direct asymptotic exponent is already known.
# Periodic block Padé synthesis

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Claims:** L-9410, T-9414, T-9415, R-9403  
**Experiment:** X-9408  
**Status:** theorem-level claims `PROPOSED` pending independent reconstruction

## Headline

The constant-increment `q`-binomial Padé construction extends to a single
explicit common denominator for every phase of a repeated finite increment
word `W`.

For displayed period length `r`, the construction has rigorous limiting
approximation gain

```text
mu_r
 =[6/log_2(81)]*(r^2+r+1)/[r(r+1)].
```

Therefore:

```text
period 1: mu_1=1.419591945535...  -> irrational,
period 2: mu_2=1.104127068750...  -> irrational,
period 3: mu_3=1.025260849553...  -> irrational,
period 4: mu_4=0.993714361875...  -> current estimate misses.
```

Every positive periodic stack block of length at most three, and every finite
steering prefix followed by such a tail, is excluded from the ordinary integer
section.

No claim is made for minimal period four or the balanced nonperiodic `17/18`
directive.

## Phase decomposition

For a word

```text
W=d_1...d_r,
S=sum d_i,
```

L-9408 gives transfer data `(e,P_W)`. At starting height `m`, put

```text
X=T^(9m),
lambda=T^(9S),
Z=T^e X^r,
R=lambda^r,
T=64/81.
```

Writing

```text
P_W(X)=sum_(j=0)^(r-1) p_j X^j,
C_j=p_j X^j,
```

the periodic value is

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j
  sum_(N>=0) R^[N(N-1)/2](Z lambda^j)^N.            (1)
```

Thus a period-`r` block is a vector of `r` adjacent partial-theta phases.

## Common denominator

At Padé order `n`, set `D=rn`. Define

```text
beta(k)
 =[(1-r)k^2+(2r^2n-r-1)k]/2,
```

and

```text
B_n(Y)
 =sum_(k=0)^D
   (-1)^k Z^k lambda^beta(k)
   [D choose k]_lambda Y^k.                         (2)
```

After multiplying any phase in (1), the block-`N` coefficient factors exactly
as

```text
phase_N
 *prod_(h=0)^(D-1)
  (1-lambda^[h+r^2n-rN-j]).                         (3)
```

For

```text
N=D+t,
0<=t<n,
```

the factor with `h=rt+j` is zero. One denominator therefore cancels `n`
consecutive coefficients in every phase—`rn` exact conditions with `rn`
nonconstant denominator coefficients.

## First error and height

The first surviving block is

```text
N_0=(r+1)n.
```

It comes uniquely from phase zero. Its exact valuation is

```text
6{
 N_0[e+9mr]
 +9S*n[nr(r^2+r+1)-r^2-2r]/2
}.                                                   (4)
```

The evaluated denominator is a `2`-adic unit.

The rational height has upper exponent

```text
[e+9mr]rn
 +9S*(r+1)rn(rn-1)/2
 +O_(W,m)(1).                                        (5)
```

The quotient of the leading terms in (4) and (5) is `mu_r`.

## Irrationality threshold

If a `2`-adic integer `alpha=a/b` is rational and `p/q` has odd reduced
denominator, then the nonzero cross integer

```text
a q-b p
```

forces

```text
v_2(alpha-p/q)
 <=log_2 height(p/q)+O_alpha(1).                    (6)
```

Hence any infinite rational-approximant family with limiting exponent above
one proves irrationality.

Equation (6) and `mu_r>1` establish T-9414 for `r<=3`.

## Finite-prefix stability

For a finite steering prefix `U`, L-9408 gives

```text
Theta(m;U W^infinity)
 =rational
  +nonzero rational*Theta(m+S(U);W^infinity).       (7)
```

Therefore irrationality of the periodic tail survives every finite prefix,
which is T-9415.

## Method boundary at period four

The universal gain first drops below one at `r=4`:

```text
1-mu_4=0.006285638124... .
```

This refutes only the claim that the current universal estimate proves all
periods. It does not decide a period-four value.

The missing logarithmic saving is about `0.6286%`. Q-9411 asks whether it can be
recovered through:

```text
- common-factor reduction;
- adjacent-order determinants;
- phase-sensitive denominators;
- cyclic/reversal classification of primitive words.
```

## Exact replay

```bash
python3 -B experiments/X-9408-block-pade/run.py \
  --check-results experiments/X-9408-block-pade/results/canonical.json
```

Canonical SHA-256:

```text
9895b3723a3a5d19f43ef5158c18a0511f58f923df2f1919a68771f1f322583c
```

Frozen examples include `(17,18)^infinity` through order three and
`(17,17,18)^infinity` through order two. Every exact reduced-height ratio is
above one.

## Review order

1. Reconstruct the normalization exponent `beta(k)` in L-9410.
2. Check the phase cancellation index `h=rt+j`.
3. Recompute the unique first-error phase and formula (4).
4. Audit the monomial-height inequality, especially the lower coefficients.
5. Reconstruct the rational cross-integer argument in T-9414.
6. Verify that T-9415 uses a nonzero transfer coefficient.

## Current frontier

The periodic hierarchy is now:

```text
minimal period <=3             excluded;
minimal period 4               exact small height deficit;
minimal period >=5             larger deficit;
balanced nonperiodic 17/18     standard-word/S-adic determinant problem.
```

A period-four height-saving mechanism would be the first candidate tool that
could plausibly scale to adjacent standard words.
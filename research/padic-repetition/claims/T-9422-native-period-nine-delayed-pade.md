# T-9422 — Native source-independent irrationality through period nine

Claim ID: `T-9422`  
Title: One rational delayed-window Padé schedule excludes every eventually periodic positive stack tail of minimal period at most nine  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9407`, `L-9408`, `L-9418`; elementary integer height  
Scope: every positive increment directive eventually periodic with minimal eventual period at most nine  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Statement 1 — fixed periodic tails

Let

```text
W=d_1...d_r,
d_i>=1,
1<=r<=9,
m>=0,
```

and assume that `W` has minimal period `r`. Then

```text
boxed:
Theta(m;W^infinity) notin Q.                          (1)
```

Consequently the unique formal stack context associated by `L-9407` and
`T-9409` to `W^infinity` is irrational and cannot be an ordinary integer.

## Statement 2 — finite steering prefixes

Let `U` be any finite positive increment word and let `W` be as above. Then

```text
boxed:
Theta(m;U W^infinity) notin Q.                        (2)
```

Thus no finite CRT-steering or initialization prefix can repair a periodic tail
whose minimal period is at most nine.

## A uniform exact delay

Apply `L-9418` along even Padé orders `n` with

```text
M=37n/2.                                              (3)
```

For `n>=2` and `r<=9`, this satisfies the required inequality

```text
M>=rn+1.
```

The delayed exponent in `L-9418(26)` is

```text
mu_r
 =log_81(64)
  *[((39/2)^2-r)/((37/2)^2+r)].                       (4)
```

The rational shape in (4) is strictly decreasing in `r`. At the endpoint
`r=9`, it is

```text
[((39/2)^2-9)/((37/2)^2+9)]
 =297/281.                                            (5)
```

The exact integer inequality

```text
64^93>81^88                                           (6)
```

implies

```text
log_81(64)>88/93.                                     (7)
```

Finally,

```text
88*297-93*281=3>0.                                    (8)
```

Equations (5)--(8) give

```text
boxed:
mu_r>=mu_9
 > (88/93)(297/281)
 >1                                                   (9)
```

for every `1<=r<=9`.

## Proof of Statement 1

Let the delayed approximants from (3) be written in lowest terms as

```text
p_n/q_n.
```

By `L-9418`, their errors are nonzero, `q_n` is odd, and

```text
liminf
 v_2(Theta(m;W^infinity)-p_n/q_n)
 /log_2 height(p_n/q_n)
 >1.                                                  (10)
```

Suppose for contradiction that

```text
Theta(m;W^infinity)=a/b
```

in lowest terms. The value lies in `Z_2`, so `b` is odd. Form the nonzero
ordinary integer

```text
N_n=a q_n-b p_n.                                      (11)
```

Oddness gives

```text
v_2(N_n)
 =v_2(Theta(m;W^infinity)-p_n/q_n)+O_(a,b)(1),         (12)
```

while

```text
|N_n|
 <=(|a|+|b|)height(p_n/q_n).                          (13)
```

Every nonzero ordinary integer satisfies

```text
2^[v_2(N_n)]<=|N_n|.                                  (14)
```

Equations (10)--(14) are incompatible for large `n`. If the approximant heights
had a bounded subsequence, the same contradiction would be immediate because
(12) tends to infinity while only finitely many bounded-height rationals exist.
Thus (1) holds.

`L-9407` expresses the selected initial stack context as a nonzero rational
affine transform of the periodic value. A rational context would therefore make
the periodic value rational, again contradicting (1). **QED**

## Proof of Statement 2

The exact finite-prefix transfer identity of `L-9408` has the form

```text
Theta(m;U W^infinity)
 =P_U(T^(9m))
  +c_U Theta(m+S(U);W^infinity),                      (15)
```

where `P_U(T^(9m))` and the nonzero multiplier `c_U` are rational. If the left
side were rational, solving (15) for the final periodic tail would make that
tail rational, contradicting Statement 1. **QED**

## Relationship to the external theorem

`T-9417` previously excluded the same period range by importing the fully
inspected Väänänen--Wallisser theorem after an exact native reduction. The
present theorem is source-independent: it uses only the explicit native
Gaussian-binomial approximants of `L-9418` and an elementary product-formula
integer.

The two routes should both be retained:

```text
T-9417  external cross-check and quantitative literature interface;
T-9422  self-contained native proof and period-uniform design laboratory.
```

Neither route covers period ten or a growing nonperiodic standard-word sequence.

## Dependency audit

- `L-9418` supplies exact cancellation, first error, denominator parity, and
  height.
- `L-9408` supplies finite-prefix propagation.
- `L-9407` supplies the affine context relation.
- No external irrationality, linear-independence, Subspace-Theorem, or
  computation result is used.

## Gap audit

- The theorem is fixed-period and stops at nine.
- The delay `37/2` is a convenient uniform rational certificate, not the
  optimizer for each period.
- Period ten misses the threshold in the full delayed-window family by
  `R-9410`; this theorem cannot be extrapolated to ten.
- No bound here is yet uniform enough for the balanced nonperiodic `17/18`
  directive whose standard-word periods grow.

## Adversarial tests

`X-9413` verifies the exact shape fractions at delay `37/2`, the integer margin
in (8), and the Laurent-product and height formulas on which `L-9418` rests.
The universal theorem is the written proof, not the finite replay.

## Suggested next attack

Use period ten as the first exact stress test for a construction that cancels
the combined native moments or exploits the homogeneous order-two
`q`-difference equation of `L-9415`. Any successful estimate should be written
as a function of both period and Padé order so it can later be tested on
standard words.
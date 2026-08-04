# T-9414 — Short-period stack values are `2`-adically irrational

Claim ID: T-9414  
Title: No periodic positive height-increment block of length at most three yields an ordinary stack context  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9407, L-9410  
Scope: every positive periodic height-increment word of displayed length `1`, `2`, or `3`  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Statement

Let

```text
W=d_1...d_r,
d_i>=1,
1<=r<=3,
m>=0.
```

Then the periodic sparse stack tail

```text
F_(W,m)=Theta(m;W^infinity)
```

is irrational in `Q_2`:

```text
F_(W,m) notin Q.                                    (1)
```

Consequently, the unique formal stack context associated by L-9407 and T-9409
to the periodic height-increment directive

```text
WWWW...
```

is not rational and in particular is not an ordinary integer. No positive
periodic stack block of length at most three supplies an ordinary infinite
Collatz seed.

This includes every nonconstant period-two and period-three word, for example

```text
(17,18)^infinity,
(18,17)^infinity,
(17,17,18)^infinity,
(17,18,17)^infinity.
```

## Proof

Let

```text
r_n=A_n(1)/B_n(1)
```

be the rational approximants from L-9410. That lemma gives nonzero errors and

```text
liminf_(n->infinity)
 v_2(F_(W,m)-r_n)/log_2 height(r_n)
 >=mu_r,                                             (2)
```

where

```text
mu_r
 =[6/log_2(81)]*(r^2+r+1)/[r(r+1)].                 (3)
```

For the three allowed lengths,

```text
mu_1=1.419591945535...,
mu_2=1.104127068750...,
mu_3=1.025260849553... .                            (4)
```

In particular,

```text
mu_r>1.                                             (5)
```

Assume for contradiction that

```text
F_(W,m)=a/b
```

in lowest terms. The series belongs to `Z_2`, so `b` is odd. Write

```text
r_n=p_n/q_n
```

in lowest terms. L-9410 gives `v_2(B_n(1))=0`; all rational denominators in the
construction are odd, so `q_n` is odd.

The nonzero integer

```text
N_n=a q_n-b p_n                                    (6)
```

satisfies

```text
v_2(N_n)=v_2(F_(W,m)-r_n),                          (7)
```

while

```text
|N_n|
 <=(|a|+|b|)height(r_n).                            (8)
```

Every nonzero integer satisfies

```text
2^[v_2(N_n)]<=|N_n|.                                (9)
```

Therefore a fixed rational target can support only

```text
v_2(F_(W,m)-r_n)
 <=log_2 height(r_n)+O_(a,b)(1),                    (10)
```

contradicting (2) and (5). This proves (1).

L-9407 expresses the associated initial stack context as a nonzero rational
affine transform of `F_(W,m)`. A rational context would therefore force the
tail value to be rational, contradicting (1). **QED**

## Strength relative to T-9412

- `r=1` recovers the constant-increment theorem T-9412.
- `r=2` is the first genuinely nonconstant periodic family. The common
  denominator cancels both phases and retains exponent
  `1.104127068750...>1`.
- `r=3` remains above threshold by the smaller margin
  `1.025260849553...>1`.

The proof is uniform in the actual positive letters of `W`; only the displayed
period length enters the limiting threshold.

## Dependency audit

- L-9410 supplies the exact simultaneous Padé cancellations, first error, and
  height estimate.
- L-9407 supplies the rational affine translation from the tail value to the
  initial stack context.
- No finite computation, equidistribution theorem, automaticity theorem, or
  external irrationality theorem is a proof dependency.

## Gap audit

- The theorem uses the displayed word length. A word with a shorter true period
  can be reduced before applying it.
- Period length four is not covered: L-9410's universal constant there is
  `0.993714...<1`.
- Irrationality excludes ordinary integers but does not prove transcendence.
- The balanced nonperiodic `17/18` directive remains open.
- Positivity and chart lifting would still be separate obligations for any
  different construction that survives the value obstruction.

## Adversarial tests

`X-9408` checks the new common denominator on period-two and period-three
`17/18` examples. The finite measured exponents remain above one and approach
the constants in (4).

## Remaining uncertainty

The first unresolved periodic class has minimal period four. It needs either a
nontrivial common-factor reduction in the current approximants or a stronger
coupled determinant family.

## Suggested next attack

Compute the exact gcd and resultant structure of the period-four numerator and
denominator. The universal estimate misses the threshold by only

```text
1-0.993714361875...=0.006285638124...,
```

so even a small quadratic-scale height saving would close that class.
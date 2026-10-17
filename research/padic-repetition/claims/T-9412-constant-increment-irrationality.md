# T-9412 — Constant-increment stack values are `2`-adically irrational

Claim ID: T-9412  
Title: No constant positive height increment yields an ordinary infinite stack context  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9407, L-9409  
Scope: every constant increment `d>=1` and starting height `m>=0`  
Related counterexample candidates: issue #4 periodic stack models; no `K-####` candidate

## Statement

Put

```text
T=64/81,
d>=1,
m>=0,
rho=T^(9d),
X=T^(9m+1),
```

and define

```text
F_(d,m)
 =sum_(N>=0)rho^(N(N+1)/2)*X^N
 in Q_2.                                             (1)
```

Then

```text
F_(d,m) notin Q.                                    (2)
```

Consequently, the unique formal stack context associated by L-9407 to the
constant height schedule

```text
m_t=m+t*d                                           (3)
```

is not rational and in particular is not an ordinary integer. No
constant-increment infinite stack tower can supply a positive ordinary Collatz
seed.

## Proof

Let

```text
r_n=A_n(X)/B_n(X)                                   (4)
```

be the rational Padé approximants from L-9409. That lemma proves

```text
v_2(F_(d,m)-r_n)
 =27*d*(3n^2+n)+12*n*(9m+1),                        (5)
```

and

```text
height(r_n)
 <=C*(n+1)^2*81^[9dn^2+(9m+1)n]                    (6)
```

for one constant `C` independent of `n`. Hence

```text
liminf_(n->infinity)
 v_2(F_(d,m)-r_n)/log_2 height(r_n)
 >=9/log_2(81)
 =1.419591945535...>1.                              (7)
```

The errors in (5) are nonzero, so `r_n!=F_(d,m)` for every `n`.

Assume for contradiction that

```text
F_(d,m)=a/b
```

in lowest terms. Since the series belongs to `Z_2`, its reduced denominator
`b` is odd. Write

```text
r_n=p_n/q_n
```

in lowest terms. L-9409 gives `v_2(B_n(X))=0`, and both evaluated Padé
polynomials have odd rational denominators; thus `q_n` is odd as well.

The nonzero integer

```text
N_n=a*q_n-b*p_n                                    (8)
```

satisfies

```text
v_2(N_n)=v_2(F_(d,m)-r_n).                          (9)
```

On the other hand,

```text
|N_n|
 <=|a|*|q_n|+|b|*|p_n|
 <=(|a|+|b|)*height(r_n).                           (10)
```

Every nonzero integer obeys

```text
2^v_2(N_n)<=|N_n|.                                  (11)
```

Equations (9)--(11) imply

```text
v_2(F_(d,m)-r_n)
 <=log_2 height(r_n)+O_(a,b)(1),                    (12)
```

contradicting (7). This proves (2).

L-9407 expresses the initial context for (3) as a fixed rational affine
transform of `F_(d,m)`. A rational context would therefore make `F_(d,m)`
rational, contradicting (2). **QED**

## Quantitative interpretation

The proof crosses exactly the threshold that direct truncations miss:

```text
direct truncation exponent: 0.946394630357...,
q-binomial Padé exponent:    1.419591945535... .    (13)
```

The second value is enough to exclude a fixed rational target. It remains below
`2`, so this theorem does not classify `F_(d,m)` as transcendental or exclude
all algebraic irrational values.

## Relationship to earlier rigidity results

Periodic or constant increment schedules were already strategically disfavored
by frequency, automaticity, and schedule-locking obstructions on issue #4.
T-9412 is logically different:

- it works directly on the exact selected `2`-adic ordinary section;
- it does not assume a chart-class frequency theorem;
- it demonstrates that the Padé program can generate enough Diophantine gain to
  decide a genuine infinite-stack value family.

This makes the scalar constant-increment case a proved model for the block
standard-word program Q-9410.

## Dependency audit

- L-9409 supplies the Padé identities, exact error, and height estimate.
- L-9407 supplies the affine translation from the tail value to the stack
  context.
- No finite computation or external transcendence theorem is a proof
  dependency.

## Gap audit

- The schedule (3) is constant-increment, not the balanced nonperiodic `17/18`
  schedule needed by the surviving issue-#4 frontier.
- Irrationality of the formal context does not prove a convergence theorem for
  any different grammar.
- The threshold argument relies on reduced denominators being odd; this is
  proved from `2`-adic-unit Padé denominators.
- The theorem excludes rational contexts, hence ordinary integers, but does not
  prove transcendence.

## Adversarial tests

`X-9407` checks the Padé family for `d=17,18`, `m=1`, and orders through `5`.
Every finite exponent is greater than one and trends toward the proved constant
in (13).

## Remaining uncertainty

The central open problem is to preserve a gain above one when the constant
letter is replaced by adjacent S-adic standard words.

## Suggested next attack

Construct a block Gaussian-binomial or matrix Padé family for periodic finite
words `W^infinity`, then perturb from the periodic block model to the true
balanced standard-word directive.
# L-9412 — Väänänen–Wallisser interface for periodic stack phases

Claim ID: `L-9412`  
Title: The periodic stack phase vector satisfies the exact source hypotheses through dimension nine  
Status: `PROPOSED / SOURCE-DEPENDENT`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9408`, `L-9410`; Väänänen–Wallisser (1991), Theorem 1  
Scope: every positive periodic stack increment word  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Source theorem used

For

```text
q=s/t in Q,
(s,t)=1,
t>0,
|s|>1,
```

put

```text
f_q(z)=sum_(n>=0) q^[n(n-1)/2] z^n.
```

Fix a prime `p` dividing `s` and nonzero rational points
`y_1,...,y_D` lying in distinct multiplicative `q^Z`-orbits. Define

```text
gamma(q,p)
 =1+log|s|_p/log max(|s|,t),
```

and

```text
Gamma(D)
 =(2D+1-sqrt(1+4D^2))/(2D).
```

Väänänen and Wallisser prove that if

```text
gamma(q,p)<Gamma(D),
```

then

```text
1,f_q(y_1),...,f_q(y_D)
```

are linearly independent over `Q`. Their theorem gives a stronger quantitative
linear-independence measure; only its qualitative consequence is used here.

## Exact stack normalization

Let

```text
W=d_1...d_r,
r=|W|>=1,
S=S(W),
m>=0,
T=64/81.
```

Use the transfer data of `L-9408` and the phase decomposition of `L-9410`:

```text
lambda=T^(9S),
R=lambda^r,
X=T^(9m),
Z=T^e X^r,
```

and nonzero rational coefficients `C_0,...,C_(r-1)` satisfying

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j f_R(Z lambda^j).               (1)
```

The coefficients are the nonzero monomials

```text
C_j=T^[j+9 A_j(W)] X^j.
```

## Statement 1 — distinct multiplicative orbits

For `0<=i<j<r`,

```text
(Z lambda^i)/(Z lambda^j)=lambda^(i-j).               (2)
```

If this were `R^n=lambda^(rn)` for an integer `n`, then, because
`0<lambda<1` in the real embedding,

```text
i-j=rn.
```

But `0<|i-j|<r`, which is impossible. Hence the `r` evaluation points in
(1) occupy distinct `R^Z`-orbits.

## Statement 2 — the source parameter is universal

Write

```text
R
 =64^(9Sr)/81^(9Sr)
 =s/t
```

in lowest terms and take `p=2`. Then

```text
|s|_2=2^(-6*9Sr),
max(|s|,t)=t=81^(9Sr).
```

Therefore

```text
gamma
 =1-log(64)/log(81)
 =0.053605369642813... .                              (3)
```

It is independent of the word, its height sum, the starting height, and the
displayed period.

## Statement 3 — exact endpoint nine

The source inequality holds at `D=9`.

Indeed,

```text
64^93>81^88
```

gives

```text
log(64)/log(81)>88/93.                                (4)
```

Also,

```text
88/93>(sqrt(325)-1)/18,
```

because the latter inequality follows from

```text
sqrt(325)<559/31,
559^2-325*31^2=156>0.                                 (5)
```

Since

```text
Gamma(9)=(19-sqrt(325))/18,
1-Gamma(9)=(sqrt(325)-1)/18,
```

equations (3)--(5) give

```text
gamma<Gamma(9).                                       (6)
```

As `Gamma(D)` is strictly decreasing in `D`, the source condition holds for
every `D<=9`.

## Statement 4 — exact source cutoff at ten

The displayed source condition fails at `D=10`.

Indeed,

```text
64^20<81^19
```

gives

```text
log(64)/log(81)<19/20,
```

while `sqrt(401)>20` gives

```text
19/20<(sqrt(401)-1)/20=1-Gamma(10).
```

Thus

```text
gamma>Gamma(10).                                      (7)
```

Since `Gamma(D)` decreases, this numerical source condition fails for every
`D>=10`.

Equation (7) is a theorem-hypothesis boundary. It is not evidence that any
dimension-ten special value is rational.

## Proof

Equation (1) is the repeated-block formula of `L-9408`, grouped by phase as in
`L-9410`. The orbit calculation proves Statement 1. The valuation and height of
the reduced rational parameter `R` prove Statement 2. Statements 3 and 4 are the
displayed exact integer comparisons. **QED**

## Dependency and source audit

- `L-9408` supplies the finite-word and repeated-block transfer.
- `L-9410` supplies the exact Tschakaloff phase decomposition.
- The implication from (6) to linear independence is imported from the fully
  inspected Väänänen–Wallisser paper.
- No finite experiment proves the source theorem.
- The native mapping, orbit separation, and endpoint arithmetic are written
  explicitly here so that source applicability can be reconstructed independently.

## Gap audit

- The theorem must use the **minimal** period. A word displayed with a longer
  period should first be reduced.
- Failure of the numerical condition at ten does not negate the stronger
  quantitative theorem below dimension ten and does not decide a special
  ten-term coefficient vector.
- The source gives full linear independence, which is stronger and potentially
  more expensive than irrationality of the one native combination (1).
- This lemma does not address a growing S-adic sequence of periods.

## Adversarial tests

`X-9411` checks the exact endpoint inequalities, all phase-pair orbit residues
through period ten, and finite direct-versus-phase decompositions for sample
words through displayed period ten.

## Suggested next attack

Use the source's **quantitative** nine-phase measure, not only its qualitative
independence, to eliminate one phase of the native period-ten vector. This is
formalized in `L-9414` and `Q-9413`.

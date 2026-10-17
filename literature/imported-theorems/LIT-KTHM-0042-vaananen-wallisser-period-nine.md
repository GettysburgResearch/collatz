# LIT-KTHM-0042 — Väänänen–Wallisser excludes periodic stack tails through period nine

**Type:** external theorem plus an exact native parameter reduction.  
**Source:** K. Väänänen and R. Wallisser, *A Linear Independence Measure for Certain p-Adic Numbers*, Journal of Number Theory 39 (1991), 225–236, especially Theorem 1.  
**Maps to:** `PADIC/L-9408`, `PADIC/L-9410`, `PADIC/T-9414`, `PADIC/T-9415`, and the periodic part of the ordinary stack frontier in PR #20.

## 1. Source theorem

For a rational number

```text
q=s/t,
(s,t)=1,
t>0,
|s|>1,
```

let

```text
f_q(z)=sum_(n>=0) q^(n(n-1)/2) z^n.
```

Fix a prime `p` dividing `s`, and let `y_1,...,y_D` be nonzero rationals satisfying

```text
y_i/y_j != q^n
```

for all `i!=j` and all `n in Z`. Put

```text
gamma(q,p)
 =1+log|s|_p/log max(|s|,t),
```

and

```text
Gamma(D)
 =(2D+1-sqrt(1+4D^2))/(2D).
```

If

```text
gamma(q,p)<Gamma(D),
```

then

```text
1, f_q(y_1), ..., f_q(y_D)
```

are linearly independent over `Q`. The source proves the stronger quantitative lower bound for every nonzero integer linear form.

This statement is imported as a black box from the fully inspected paper.

## 2. Periodic stack decomposition

Let `W` be a positive height-increment word of length

```text
r=|W|>=1,
```

and let `m>=0`. In the notation of `PADIC/L-9408` and `PADIC/L-9410`, put

```text
T=64/81,
S=S(W),
lambda=T^(9S),
R=lambda^r,
Z=T^e * T^(9mr),
```

where `e=e(W)`. There are nonzero rational coefficients `C_0,...,C_(r-1)` such that

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j f_R(Z lambda^j).              (1)
```

This is the exact finite Tschakaloff-vector reduction of `LIT-KTHM-0034`.

## 3. Orbit separation

The evaluation points in `(1)` satisfy the source theorem's multiplicative-orbit hypothesis.

Indeed, for `i!=j`,

```text
(Z lambda^i)/(Z lambda^j)=lambda^(i-j).
```

If this were `R^n=lambda^(rn)` for some integer `n`, then

```text
i-j=rn.
```

But `0<|i-j|<r`, so this is impossible. Hence the `r` points occupy distinct `R^Z`-orbits.

## 4. Exact numerical range of the source theorem

Write

```text
R
 =64^(9Sr)/81^(9Sr)
 =s/t
```

in lowest terms and take `p=2`. Then

```text
|s|_2=2^(-6*9Sr),
max(s,t)=t=81^(9Sr),
```

so the source parameter is independent of `W`, `S`, and `r`:

```text
gamma
 =1-log(64)/log(81)
 =0.053605369642... .                                (2)
```

The function `Gamma(D)` is strictly decreasing in `D`. To verify the endpoint `D=9`, note that

```text
64^93 > 81^88,
```

so

```text
log(64)/log(81)>88/93.                               (3)
```

Also

```text
88/93 > (sqrt(325)-1)/18,
```

because this is equivalent to

```text
sqrt(325)<559/31,
```

and

```text
559^2-325*31^2=156>0.
```

Therefore

```text
gamma
 <(19-sqrt(325))/18
 =Gamma(9).                                          (4)
```

Consequently the source theorem applies for every `D<=9`.

The stated numerical condition first fails at `D=10`. Indeed,

```text
64^20<81^19
```

implies

```text
log(64)/log(81)<19/20,
```

while `sqrt(401)>20` gives

```text
19/20<(sqrt(401)-1)/20=1-Gamma(10).
```

Thus

```text
gamma>Gamma(10).                                     (5)
```

Equation `(5)` does not prove any period-ten value rational; it only identifies the exact endpoint of this source theorem's guaranteed range for the current parameter.

## 5. Native corollary

Let `W` be a positive increment word whose minimal period has length at most nine. Then, for every starting height `m>=0`,

```text
Theta(m;W^infinity) notin Q.                         (6)
```

### Proof

Use the minimal period in `(1)`, so `r<=9`. Sections 3–4 verify every hypothesis of the source theorem for

```text
1, f_R(Z), f_R(Zlambda), ..., f_R(Zlambda^(r-1)).
```

Suppose the rational linear combination `(1)` were rational. Move that rational value to the left and clear all rational denominators. This would produce a nontrivial integer linear relation among `1` and the displayed `r` Tschakaloff values, contradicting the source theorem. Hence `(6)` holds. ∎

## 6. Finite steering prefixes

For any finite positive increment word `U`, the exact transfer identity of `PADIC/L-9408` has the form

```text
Theta(m;U W^infinity)
 =P_U(T^(9m))
  +c_U Theta(m+S(U);W^infinity),                     (7)
```

where both `P_U(T^(9m))` and the nonzero coefficient `c_U` are rational. If the left side of `(7)` were rational, the periodic tail would be rational, contradicting `(6)`.

Therefore every eventually periodic positive increment directive of minimal eventual period at most nine selects an irrational `2`-adic stack context and cannot select an ordinary integer.

## 7. Consequences for the current PR #20 program

1. `PADIC/T-9412`–`T-9415` remain valuable self-contained native proofs and exact Padé models.
2. Once this imported theorem is admitted, period four is no longer the first unresolved fixed-period class.
3. Period ten is the first fixed period not covered by the source theorem's stated numerical condition.
4. Period-four q-Lucas, Cartier, cyclotomic, and Casoratian machinery should be retained as proof-of-method and retargeted toward:
   - periods at least ten;
   - a source-independent all-period theorem; or
   - bounds uniform in the period for passage to standard-word approximants.

## 8. Nonconsequences

This theorem does **not** prove:

- irrationality for minimal period at least ten;
- transcendence of any stack value;
- irrationality of the balanced nonperiodic `17/18` directive;
- a bound uniform enough to pass automatically to growing standard words;
- or the Collatz conjecture.

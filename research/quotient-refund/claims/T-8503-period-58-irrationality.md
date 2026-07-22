# T-8503 — Every eventually periodic linear-height type directive of period at most 58 is nonordinary

**Claim ID:** `T-8503`  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependencies:** branch-qualified `PR3/L-0031`; Väänänen–Wallisser 1991, Theorem 1, as imported in `LIT-KTHM-0042`  
**Scope:** local tower-type directives on `t_n=B+16n`

## Completion series

Fix a multiple of `16`, denoted `B`, and a type directive `i_0,i_1,...`. The scaled boundary recurrence is

\[
2^{11(B+16n+17)}W_{n+1}
=
3^{7(B+16n+1)}W_n+b_{i_n}.
\tag{1}
\]

Its unique `2`-adic initial completion is

\[
\boxed{
\Omega_B(i)
=-3^{-7(B+1)}
\sum_{n\ge0}
 b_{i_n}
 q^{n(n-1)/2}y^n,
}
\tag{2}
\]

where

\[
\boxed{
q=\frac{2^{176}}{3^{112}},
\qquad
y=q\frac{2^{11(B+1)}}{3^{7(B+1)}}.
}
\tag{3}
\]

## Theorem

If the type directive is eventually periodic with minimal eventual period

\[
1\le r\le58,
\]

then

\[
\boxed{
\Omega_B(i)\notin\mathbb Q.
}
\tag{4}
\]

In particular, it is not any signed ordinary integer. No positive ordinary trajectory can have such an eventual type tail.

The source theorem's numerical condition is guaranteed exactly through `r=58` and first fails at `r=59` for the parameter (3).

## Periodic phase decomposition

For a purely periodic word `i_0,...,i_(r-1)`, split `n=rm+j`. Put

\[
Q=q^{r^2},
\]

\[
Y_j=q^{r(r+2j-1)/2}y^r,
\]

\[
C_j=b_{i_j}q^{j(j-1)/2}y^j.
\]

Then

\[
\boxed{
\sum_{n\ge0}b_{i_n}q^{n(n-1)/2}y^n
=
\sum_{j=0}^{r-1}C_j f_Q(Y_j),
}
\tag{5}
\]

where

\[
f_Q(z)=\sum_{m\ge0}Q^{m(m-1)/2}z^m.
\]

All `C_j` are nonzero rationals. For `j!=k`,

\[
\frac{Y_j}{Y_k}=q^{r(j-k)}
\]

is not in `Q^Z=q^(r^2 Z)`, because `0<|j-k|<r`. Thus the evaluation points occupy distinct multiplicative `Q`-orbits.

## Exact source cutoff

For `p=2`, the Väänänen–Wallisser parameter is

\[
\gamma
=1-\frac{\log(2^{176})}{\log(3^{112})}
=1-\frac{\log2048}{\log2187}.
\tag{6}
\]

The exact inequalities

\[
2^{1287}>3^{812}
\]

and

\[
2^{1298}<3^{819}
\]

give

\[
\frac{116}{117}
<
\frac{\log2048}{\log2187}
<
\frac{117}{118}.
\tag{7}
\]

At dimension `58`,

\[
\frac{116}{117}
>
\frac{\sqrt{13457}-1}{116}
=1-\Gamma(58),
\]

because

\[
13573^2-13457\cdot117^2=13456>0.
\]

Hence `gamma<Gamma(58)`. At dimension `59`,

\[
\frac{117}{118}
<
\frac{\sqrt{13925}-1}{118}
=1-\Gamma(59),
\]

because `118^2<13925`. Hence `gamma>Gamma(59)`.

The source theorem therefore proves linear independence of

\[
1,f_Q(Y_0),\ldots,f_Q(Y_{r-1})
\]

for every `r<=58`. Equation (5) cannot be rational, proving (4) for a purely periodic tail.

A finite steering prefix maps an ordinary initial value to another ordinary integer at the start of the periodic tail. Applying the same argument there excludes every eventually periodic directive. ∎

## Consequence for construction

A linear-refund witness cannot come from a constant tower type, a short cycle of types, or any autonomous type controller whose eventual output cycle has length at most `58`. The surviving positive route must use genuinely unbounded arithmetic state. Failure of the source condition at `59` is not evidence of a rational completion.

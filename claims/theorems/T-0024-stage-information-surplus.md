# T-0024 — A full 256-step stage has exponential precision surplus

Claim ID: `T-0024`  
Title: Aggregate residual-stack growth exceeds the next-stage connector-precision demand  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `T-0023`, `L-0024`  
Scope: one phase-34 self-return tower type over one complete corrected dyadic stage  
Related counterexample candidates: none

## Statement

Fix one of the four phase-34 self-return tower types. Write

\[
K_t=11t+K_*,
\qquad
G_t=7t+G_*.
\tag{1}

At dyadic scale \(m\), put

\[
B=2^m,
\qquad
d=2^{m-8}=B/256.
\tag{2}

Use the corrected stage heights

\[
t_j=B+jd,
\qquad
0\le j\le256,
\tag{3}

and the first height of the next stage after its initial point,

\[
t_{257}=2B+2d.
\tag{4}

For each \(0\le j<256\), the residual-stack update from connector \(j\) to connector \(j+1\) has linear slope

\[
\lambda_j
=
\frac{3^{G_{t_j}}}{2^{K_{t_{j+2}}}}.
\tag{5}

Define the full-stage slope

\[
\boxed{
\Lambda_m
=
\prod_{j=0}^{255}\lambda_j.
}
\tag{6}

Then:

### 1. Exact leading exponent

\[
\boxed{
\log_2\Lambda_m
=
\Gamma B
+256\bigl(G_*\log_2 3-K_*\bigr),
}
\tag{7}

where

\[
\boxed{
\Gamma
=
\frac{687232\log_2 3-1085579}{256}
\approx14.2888644359.
}
\tag{8}

### 2. Elementary rigorous lower bound

The exact integer inequality

\[
3^{53}>2^{84}
\tag{9}

implies

\[
\log_2 3>84/53.
\]

Therefore

\[
\boxed{
\Gamma>
\frac{191801}{13568}
\approx14.1362765330.
}
\tag{10}

### 3. Connector-precision demand

The first connector of stage \(m\) targets height \(t_1=B+d\). The first connector of stage \(m+1\) targets height

\[
t_{257}=2B+2d.
\]

The required increase in canonical binary connector depth is exactly

\[
\boxed{
K_{t_{257}}-K_{t_1}
=
11(B+d)
=
\frac{2827}{256}B.
}
\tag{11}

### 4. Exponential precision surplus

Subtracting (11) from (7) gives

\[
\boxed{
\log_2\Lambda_m
-
\bigl(K_{t_{257}}-K_{t_1}\bigr)
=
\Sigma B
+256\bigl(G_*\log_2 3-K_*\bigr),
}
\tag{12}

where

\[
\Sigma
=
\Gamma-rac{2827}{256}
\approx3.24589568594.
\tag{13}

The elementary lower bound (9) gives

\[
\boxed{
\Sigma>
\frac{20985}{6784}
\approx3.09330778302.
}
\tag{14}

Hence there is a finite type-dependent \(m_0\) such that, for every \(m\ge m_0\),

\[
\boxed{
\Lambda_m
>
2^{K_{t_{257}}-K_{t_1}}
\,2^{(20985/13568)B}.
}
\tag{15}

The weaker exponent \(20985/13568\), half the rigorous surplus coefficient, absorbs the fixed constant in (12).

Thus after paying for the entire increase in connector precision from one scale to the next, the stage retains an additional exponential bit budget.

### 5. Affine stage map above a finite threshold

On a valid 256-transition residual path, the exact stage map has the form

\[
\boxed{
z_{\rm out}
=
\Lambda_m z_{\rm in}+\beta_m,
}
\tag{16}

for one rational \(\beta_m\); integrality is guaranteed on the accepted stage cylinder.

There is an explicit finite threshold \(Z_m\) obtained by composing the 256 affine updates such that

\[
z_{\rm in}\ge Z_m
\quad\Longrightarrow\quad
z_{\rm out}
\ge
\frac12\Lambda_m z_{\rm in}.
\tag{17}

Consequently, above that threshold, the output residual contains enough archimedean binary length to carry:

1. the entire next-stage increase in connector precision; and
2. at least \(c2^m\) additional bits for one fixed \(c>0\).

## Proof

The source-height sum is

\[
\begin{aligned}
\sum_{j=0}^{255}t_j
&=256B+d\frac{255\cdot256}{2}\\
&=256B+32640\frac B{256}\\
&=\frac{767}{2}B.
\end{aligned}
\tag{18}

For the future denominators, the indices are \(2,3,\ldots,256,257\). Hence

\[
\begin{aligned}
\sum_{j=0}^{255}t_{j+2}
&=
\sum_{i=2}^{256}(B+id)
+(2B+2d)\\
&=257B+32897d\\
&=\frac{98689}{256}B.
\end{aligned}
\tag{19}

Using (1),

\[
\begin{aligned}
\log_2\Lambda_m
&=
\log_2 3
\sum_{j=0}^{255}G_{t_j}
-
\sum_{j=0}^{255}K_{t_{j+2}}\\
&=
7\log_2 3
\sum_{j=0}^{255}t_j
-11
\sum_{j=0}^{255}t_{j+2}\\
&\qquad
+256(G_*\log_2 3-K_*).
\end{aligned}
\]

Substituting (18)--(19) gives (7)--(8).

Direct integer evaluation gives

\[
3^{53}
=19383245667680019896796723
>
19342813113834066795298816
=2^{84}.
\]

Therefore \(\log_2 3>84/53\). Substitution into (8) gives

\[
\Gamma
>
\frac{687232(84/53)-1085579}{256}
=
\frac{191801}{13568},
\]

proving (10).

Equation (11) is direct from

\[
t_{257}-t_1
=(2B+2d)-(B+d)
=B+d.
\]

Subtracting proves (12)--(14). The fixed type-dependent constant in (12) is eventually dominated by half of the positive linear lower bound, proving (15).

Finally, composing finitely many affine maps gives (16). Write

\[
\beta_m
\]

for the resulting constant. Taking

\[
Z_m
>
\frac{2|\beta_m|}{\Lambda_m}
\]

and also above every intermediate integrality/growth threshold gives (17). ∎

## Interpretation

The packet's precision problem is not an information-theoretic shortage.

One full corrected stage generates, asymptotically,

\[
\approx14.29\cdot2^m
\]

residual bits. Moving to the next scale asks for only

\[
\approx11.04\cdot2^m
\]

additional connector bits. The spare budget is

\[
\approx3.25\cdot2^m
\]

bits.

This surplus is more than enough in magnitude to run the quadratic Hensel update of `L-0023`, extend the inverse-prefix stack, and retain a growing ordinary residual—**provided the exact congruence domains can be made invariant**.

The central blocker has therefore sharpened again:

> not information supply, not local expansion, and not finite connectors, but exact arithmetic routing of the surplus into the next required stack prefix.

## Dependency audit

- `T-0023` supplies the residual maps and positive local slopes.
- `L-0024` supplies the exact 256-step stage indexing.
- The stage sum is elementary and uses no limiting approximation.

## Gap audit

- The stage threshold \(Z_m\) is not yet generated by one finite schema.
- Large bit-length surplus does not imply the correct low bits.
- The exact accepted stage cylinder may still have no ordinary forward-invariant member.
- No marked starting integer is constructed.

## Adversarial tests

`X-0012` checks the exact sums, the integer inequality (9), the local residual maps, and representative finite-stage affine compositions.

## Suggested next attack

Design a proof-producing stage router that spends part of the surplus on the quadratic update

\[
u_{m+1}=u_m+2^{m+1}u_m^2
\]

and uses the remaining bits to satisfy the next residual cylinder. The required output is a finite substitution on the four stack tracks identified in `L-0023`.
# L-9828 — Sparse prime-power support for period-four Padé residuals

Claim ID: `L-9828`  
Title: Reduced prime-power Padé residual obstructions have subquadratic squarefree support  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`, integrated by `gpt56-synthesis-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9816`, `L-9832`, `L-9839`; elementary cyclotomic identities and Legendre valuations  
Scope: period-four block Padé residuals at reduced orders `p^k`, `k>=2`  
Related counterexample candidates: the abstract `L=4,s=2` residual in the adversarial audit below

## Definitions

Use the period-four Padé notation of `L-9816`: `r=4`, `D=4n`,

\[
a=9S,
\qquad
\zeta=e+9mr,
\qquad
G=\gcd(a,\zeta).
\tag{1}
\]

For an automatically eligible root order `d`, put

\[
g=\gcd(d,a),
\qquad
L=\frac d g,
\qquad
U=T^g,
\qquad
a_g=\frac ag,
\qquad
\zeta_g=\frac\zeta g.
\tag{2}
\]

Then `g|G`, `(a_g,L)=1`, and automatic eligibility implies

\[
L\le X:=\frac D2.
\tag{3}
\]

Write `s=D mod L`.  The reduced residual polynomial is

\[
R_{g,L,s}(U)
=
\sum_{v=0}^s(-1)^v
U^{\zeta_gv+a_g\beta_s(v)}
{s\brack v}_{U^{a_g}},
\qquad
\beta_s(v)=\frac{-3v^2+(8s-5)v}{2}.
\tag{4}
\]

Call `d` a reduced prime-power obstruction when `L=p^k`, `k>=2`, and
`R_(g,L,s)` vanishes at a primitive `L`-th root.  Let `P_D` be the set of
these root orders and define only its squarefree support product

\[
\mathcal P_D^{\rm sf}(T)=\prod_{d\in P_D}\Phi_d(T).
\tag{5}
\]

This product records one possible exceptional copy at each order.  It does
not assert that the copy enters the common gcd, and it does not encode higher
residual or common-gcd multiplicity.

## Statement

### 1. Exact finite test at a prime power

Expand (4), collect its coefficients by exponent modulo `L`, and write

\[
\overline R_{g,L,s}(Y)=\sum_{c=0}^{L-1}\rho_cY^c.
\tag{6}
\]

For `L=p^k`, the residual obstruction is equivalent to the exact block
equalities

\[
\boxed{
\rho_b=\rho_{b+p^{k-1}}=\cdots
=\rho_{b+(p-1)p^{k-1}}
\quad(0\le b<p^{k-1}).
}
\tag{7}
\]

Thus this sector is a finite integral test, with no numerical root-of-unity
evaluation.

### 2. Exact small-remainder sector

For odd `s`, set

\[
C_{g,s}=\zeta_g+\frac{5a_g}{2}(s-1).
\]

`L-9832` proves that for every odd reduced order `p^k` with `s<p`, the
residual vanishes exactly when `s` is odd and `p^k|C_(g,s)`; in that case its
`Phi_(p^k)` factor is exactly simple.  Thus every non-antisymmetric
odd-prime-power zero and every higher odd-prime-power residual multiplicity is
confined to the frontier `p<=s<p^k`.

### 3. Subquadratic squarefree support

Put `y=floor(sqrt(X))`.  Even if every eligible reduced prime power were an
obstruction, its one-copy degree would satisfy

\[
\boxed{
\deg\mathcal P_D^{\rm sf}
\le
\sigma_1(G)
\left(
\frac{y(y+1)(2y+1)}6
+X^{4/3}\log_2X
\right).
}
\tag{8}
\]

In particular,

\[
\boxed{
\deg\mathcal P_D^{\rm sf}=O_G(D^{3/2})=o(D^2).
}
\tag{9}
\]

After honest homogenization,

\[
\boxed{
\log_2\left|
(\mathcal P_D^{\rm sf})^{\rm hom}(64,81)
\right|
\le
(\log_2 145)\deg\mathcal P_D^{\rm sf}
=o(D^2).
}
\tag{10}
\]

At the best `G=71` height of `L-9816`, both `g=1` and `g=71` chains are
included automatically through `sigma_1(G)=72`.  Hence one copy at every
reduced prime-power order cannot change the leading
`343.372048 n^2`-bit deficit.

### 4. Antisymmetric copies remain only linear

Recall `C_(g,s)` from the small-remainder statement and put

\[
N=2\zeta+5a(D-1).
\tag{11}
\]

Complement pairing gives

\[
1-U^{C_{g,s}}\mid R_{g,L,s}(U).
\tag{12}
\]

Consequently the antisymmetric prime-power orders, namely those with
`L|C_(g,s)`, are a subfamily of the divisors of `N`.  Their distinct product
has degree at most `|N|=O(D)`, the stronger linear bound already proved in
`L-9816/(20m)`.

### 5. Exact per-order residual-multiplicity caps

Let

\[
e_{g,p^k}
=
\operatorname{ord}_{\Phi_{p^k}(U)}R_{g,p^k,s}(U).
\tag{13}
\]

These are residual-polynomial multiplicities, not asserted excess
multiplicities of `gcd(A,B)`.  If `p` is odd, then

\[
\boxed{
e_{g,p^k}
\le
\begin{cases}
\displaystyle
\nu_p\!\left(\frac{(2u)!}{u!}\right),&s=2u,\\[8pt]
\displaystyle
\nu_p\!\left(\frac{(2u+1)!}{u!}\right)
+\nu_p(C_{g,s}),&s=2u+1.
\end{cases}
}
\tag{14}
\]

For `p=2`, `(a_g,2)=1` and `D=4n` force `s` to be even, in fact divisible by
four, and

\[
\boxed{e_{g,2^k}\le \frac{s}{2}.}
\tag{15}
\]

The improvement over the direct `e<=s` valuation bound is `L-9839`: all
lower dyadic macro factors already present in the same residual consume
exactly `s/2` powers of two in its diagonal value.

Thus higher prime-power residual multiplicity has a completely explicit
finite upper bound.  For reference, if

\[
M_g=\max\!\left(2,
\left\lceil\frac{|N|}{2g}\right\rceil\right),
\]

then the total valuation bound

\[
V_D=
\sum_{g\mid G}
\sum_{\substack{p^k\le X\\k\ge2}}
\varphi(gp^k)e_{g,p^k}
\tag{16}
\]

satisfies

\[
\boxed{
V_D
\le
\sigma_1(G)S_2(X)
+
\left(\sum_{g\mid G}g\log_2M_g\right)S_1(X),
}
\tag{17}
\]

where

\[
S_1(X)=\sum_{\substack{p^k\le X\\k\ge2}}p^k,
\qquad
S_2(X)=\sum_{\substack{p^k\le X\\k\ge2}}p^{2k-1}.
\tag{18}
\]

The first sum obeys (8) without the factor `sigma_1(G)`, while

\[
S_2(X)
\le
X^2\sum_{p\le\sqrt X}\frac{p}{p^2-1}
=O(X^2\log\log X).
\tag{19}
\]

Unlike (8), (17)--(19) are not subquadratic.  They isolate higher
prime-power multiplicity as a genuine surviving issue rather than promoting
the squarefree support estimate into a multiplicity theorem.

### 6. The entire dyadic residual budget is below the remaining deficit

`L-9839` sums (15) over every eligible power-of-two reduced order.  At the
best `G=71` height, including both `g=1` and `g=71`, it proves

\[
\boxed{
\sum_{g\in\{1,71\}}
\sum_{\substack{L=2^k\le D/2\\k\ge2}}
\varphi(gL)e_{g,L}
\le\frac{71D^2}{27}
=\frac{1136}{27}n^2.
}
\tag{19a}
\]

After honest homogeneous specialization this is at most

\[
\boxed{
\frac{1136}{27}\log_2 81\,n^2+o(n^2)
=266.743319\,n^2+o(n^2).
}
\tag{19b}
\]

This leaves `76.628729 n^2+o(n^2)` of the
`343.372048 n^2` automatic-sector deficit.

The estimate is unconditional for residual-polynomial multiplicities.  To
turn it into a theorem about the original Padé gcd one still needs

\[
\operatorname{ord}_{\Phi_{gL}}\gcd(A,B)
-\left\lfloor\frac{D}{2L}\right\rfloor
\le e_{g,L}.
\tag{19c}
\]

Inequality (19c) is not proved here.  Thus a separate transverse jet argument
is still necessary before the improved residual budget preserves the
full-gcd deficit.  The exact even-`K` first jet in
`L-9839/(14b)--(14f)` reduces that argument to noncancellation between
one sheared residual derivative and one weighted residual moment.

## Proof

Equation (7) is `L-9816/(20f)` specialized to

\[
\Phi_{p^k}(Y)
=1+Y^{p^{k-1}}+\cdots+Y^{(p-1)p^{k-1}}.
\]

Since `deg(overline R)<p^k`, divisibility by this polynomial is equivalent to
the coefficient equalities in (7).

For the support bound, every possible obstruction has `d=gp^k` with `g|G`,
`k>=2`, and `p^k<=X`.  The elementary estimate

\[
\varphi(gp^k)\le g\varphi(p^k)\le gp^k
\]

therefore gives

\[
\deg\mathcal P_D^{\rm sf}
\le
\sigma_1(G)
\sum_{\substack{p^k\le X\\k\ge2}}p^k.
\tag{20}
\]

For `k=2`, enlarge the prime sum to all integers and use

\[
\sum_{p\le\sqrt X}p^2
\le
\sum_{j=1}^{y}j^2
=\frac{y(y+1)(2y+1)}6.
\]

For each `k>=3`, there are at most `X^(1/k)` bases and every summand is at
most `X`; hence that `k` contributes at most `X^(1+1/k)<=X^(4/3)`.  There are
at most `log_2 X` possible exponents.  This proves (8)--(9).  Each homogeneous
cyclotomic factor satisfies

\[
|\Phi_d^{\rm hom}(64,81)|
\le145^{\varphi(d)},
\]

which proves (10).  Complement pairing and the divisor-of-`N` argument are
exactly `L-9816/(20l)--(20m)`, proving (11)--(12).

It remains to prove the multiplicity caps.  Remove the exact diagonal power
of `U-1` from (4).  If `s=2u`, its value at `U=1` is

\[
c_{2u}
=\frac{(2u)!(-4a_g)^u}{2^uu!},
\tag{21}
\]

while for `s=2u+1` it is

\[
c_{2u+1}
=-
\frac{(2u+1)!(-4a_g)^u}{2^uu!}C_{g,s}.
\tag{22}
\]

The factor `Phi_(p^k)` is coprime to `U-1` and
`Phi_(p^k)(1)=p`.  Therefore `Phi_(p^k)^e` dividing the residual forces
`p^e|c_s`.  For odd `p`, both `2` and `a_g` are units, giving (14).  For
`p=2`, Legendre's identity

\[
\nu_2((2u)!)-\nu_2(u!)=u
\]

and the additional `u` powers of two in `(-4a_g)^u/2^u` give
`nu_2(c_(2u))=2u=s`.  The denominator macro argument applied inside this
same length-`s` residual also forces

\[
\Phi_{2^j}^{\lceil\lfloor s/2^j\rfloor/2\rceil}\mid R
\qquad(2^j\le s).
\]

For `4|s`, the sum of these lower-factor exponents is exactly `s/2`.
Evaluating them together with the distinct target factor at one gives
`e_(g,2^k)+s/2<=nu_2(c_s)=s`, proving the sharpened (15).  The complete
telescoping and global dyadic summation are `L-9839`.

Finally, Legendre's bound gives

\[
\nu_p(s!)\le\frac{s}{p-1}<\frac{p^k}{p-1}
\]

for odd `p`, while `nu_p(C_(g,s))<=log_p M_g<=log_2 M_g`.  Multiplication by
`phi(gp^k)<=g phi(p^k)` yields (17).  For fixed `p`, the geometric sum gives

\[
\sum_{\substack{k\ge2\\p^k\le X}}p^{2k-1}
\le
X^2\frac{p}{p^2-1}.
\]

Summing over `p<=sqrt(X)` and using the standard elementary estimate
`sum_(p<=x)1/p=O(log log x)` proves (19).

Equations (19a)--(19b) are `L-9839/(9)--(13)`.  Its proof is an
elementary induction on the residues `D mod 2^k`, and its total
specialization error is `O(D log^2 D)`.  Equation (19c) is displayed as
an open transfer condition, not used as an input.  This completes the proof. ∎

## Motivation

`L-9816` shows that the automatic cyclotomic product still misses the best
period-four Padé threshold by `343.372048 n^2` bits.  Prime residual orders and
distinct antisymmetric orders are already subquadratic.  This lemma removes
the remaining squarefree prime-power support as a possible quadratic-density
rescue, without pretending that higher multiplicity is controlled.

## Dependency audit

- The reduced variables and residual polynomial are exactly those of
  `L-9816/(20a)--(20b)`.
- The block test is elementary polynomial division by `Phi_(p^k)`.
- The exact `s<p` classification and simplicity statement are `L-9832`.
- The support bound enlarges prime sums to integer sums; no prime number
  theorem is used.
- The odd per-order multiplicity caps use only `Phi_(p^k)(1)=p`, the exact
  diagonal coefficients, and Legendre valuations.
- The sharpened dyadic cap and its global envelope are `L-9839`.

## Gap audit

- One possible extra copy at every reduced prime-power order is `o(D^2)`.
- The antisymmetric subfamily is smaller, only `O(D)`.
- In the exact small-remainder range `s<p`, odd prime-power zeros are exactly
  antisymmetric and their residual factors are simple.
- The coarse all-prime bound (17) is not subquadratic and is not a theorem
  about excess common-gcd multiplicity.
- The full dyadic residual budget is only
  `266.743319 n^2+o(n^2)` bits at `G=71`, but transfer to excess
  common-gcd multiplicity requires the still-open inequality (19c).
- Genuinely non-antisymmetric zeros of (7), higher residual multiplicity, and
  the transfer from residual multiplicity to extra `gcd(A,B)` multiplicity
  remain open.

## Adversarial tests

- The tempting unrestricted statement "every prime-power residual zero is
  antisymmetric" is false.  With `r=4,L=4,s=2,a_g=1,zeta_g=0`, (4) is
  `R(U)=1-U^4`, so it vanishes at primitive fourth roots although `s` is even.
  This is not an actual period-four remainder because `D=4n` forces
  `D mod 4=0`; it shows that the `s=D mod L` constraint cannot be discarded.
- Modular coefficient-block censuses found no non-antisymmetric odd-prime-power
  zero through `L=49`, and no power-of-two zero with `s=0 mod 4` through
  `L=128`.  These checks motivated the next attack but are not used in any
  theorem above.
- The factor `sigma_1(G)` in (8) is essential.  At `G=71`, both `g=1` and
  `g=71` chains occur.

## Remaining uncertainty

Outside the proved small-remainder range, the data suggest that odd reduced
prime-power zeros may still all be antisymmetric and that the period-four
congruence `s=0 mod 4` may exclude every reduced power-of-two zero.  Neither
extension is claimed.  A proof would improve (8) from subquadratic support to
the linear bound (12) and might also control higher multiplicity.

## Suggested next attack

Use (7) in the tower
`Q(zeta_(p^k))/Q(zeta_(p^(k-1)))`.  For odd `p`, prove that the block
equalities force `s` odd and `p^k|C_(g,s)` in the remaining range
`p<=s<p^k`.  For `p=2`, either show that one top-block coefficient
difference is nonzero for every actual `s=D mod 2^k=0 mod 4`, or prove
the transverse jet inequality (19c), which would already make the global
dyadic budget too small to close the deficit.  For odd powers, compute the
first transverse derivative after the complement factor (12) to test whether
every antisymmetric prime-power factor is simple.

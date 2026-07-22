# L-9816 — Cyclotomic common factors in block Padé systems

Claim ID: `L-9816`  
Title: Block Padé numerators and denominators have exact diagonal and growing cyclotomic common factors  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: the formal Padé polynomials of `PR20/L-9410`; finite `q`-Lucas and elementary root-of-unity identities  
Scope: polynomial and specialized gcd cancellation at the period-four rigidity boundary  
Related counterexample candidates: none

## Definitions

Use the block Padé construction of `PR20/L-9410`, but retain `T` as an
indeterminate instead of setting `T=64/81`. Put

\[
a=9S,
\qquad
\zeta=e+9mr,
\qquad
D=rn,
\tag{1}
\]

and denote the evaluated formal numerator and denominator by

\[
A(T)=A_n(1),
\qquad
B(T)=B_n(1)
\qquad\text{in }\mathbb Z[T].
\tag{2}
\]

For a root of unity `tau`, write

\[
q=\tau^a,
\qquad
Z=\tau^\zeta.
\tag{3}
\]

## Statement

### 1. Exact diagonal multiplicity

The common order at `T=1` is exactly

\[
\boxed{
\operatorname{ord}_{T=1}\gcd(A,B)
=\left\lfloor\frac D2\right\rfloor.
}
\tag{4}
\]

More precisely, if `D=2g`, then

\[
\operatorname{ord}_1B=g,
\qquad
\left.\frac{B(T)}{(T-1)^g}\right|_{T=1}
=\frac{D!}{2^gg!}(-ar)^g,
\tag{5}
\]

while `ord_1 A>=g`. If `D=2g+1`, then

\[
\operatorname{ord}_1B=g+1,
\tag{6}
\]

\[
\left.\frac{B(T)}{(T-1)^{g+1}}\right|_{T=1}
=-\frac{D!(-ar)^g}{2^gg!}
\bigl(\zeta+a(r+1)g\bigr),
\tag{7}
\]

and

\[
\operatorname{ord}_1A=g,
\qquad
\left.\frac{A(T)}{(T-1)^g}\right|_{T=1}
=(-1)^gr(2ar)^gg!.
\tag{8}
\]

At `T=64/81`, this factor contributes the exact certified divisor

\[
\boxed{17^{\lfloor rn/2\rfloor},}
\tag{9}
\]

only `O(n)` bits. Thus the diagonal factor alone cannot change a quadratic
Padé height exponent.

### 2. Exact local factors in the `q^r=1` sector

Suppose `q^r=1`, let `L=ord(q)`, and assume `Zq^h=1` for at least one phase.
Put `kappa=D/L`. Then

\[
\operatorname{ord}_{T=\tau}\gcd(A,B)
=\left\lfloor\frac\kappa2\right\rfloor
\tag{10}
\]

provided, when `kappa` is odd, the selected-phase sum

\[
C_{\rm sel}
=\sum_{\substack{0\le j<r\\Zq^j=1}}\tau^{c_j}
\tag{11}
\]

is nonzero. This is automatic when `L=r` because the selected phase is unique.

For the period-four words `0001` and `0111` at `m=1`, this gives the exact
factor

\[
\boxed{
(T-1)^{2n}(T+1)^n(T^2+1)^{\lfloor n/2\rfloor}.
}
\tag{12}
\]

Its homogeneous specialization is

\[
\boxed{
17^{2n}145^n10657^{\lfloor n/2\rfloor}.
}
\tag{13}
\]

The word `0011` has no nontrivial factor from this local `q^4=1` sector.

### 3. General root-of-unity macro factors

Let `tau` have order `d`, and put

\[
g=\gcd(d,a),
\qquad
L_d=\frac d g=\operatorname{ord}(q),
\qquad
D=K_dL_d+d_0.
\tag{14}
\]

Call `d` automatically eligible when

\[
\boxed{
g\mid\zeta,
\qquad
K_d=\left\lfloor\frac D{L_d}\right\rfloor\ge2.
}
\tag{15}
\]

Then the common factor has the rigorous growing multiplicity

\[
\boxed{
\operatorname{ord}_{\Phi_d}\gcd(A,B)
\ge
\left\lfloor\frac{K_d}{2}\right\rfloor
=\left\lfloor\frac{D}{2L_d}\right\rfloor.
}
\tag{16}
\]

For odd `L_d` the statement holds for every root order `d`. If the block
length `r` is even, it also holds when `L_d` is even. In particular, it holds
for every root order in the period-four case `r=4`. Generically the lower
bound is exact.

Define

\[
\boxed{
\mathcal C_D(T)
=
\prod_{d\in\mathcal E_D}
\Phi_d(T)^{\lfloor D/(2L_d)\rfloor},
}
\tag{17}
\]

where `E_D` is the eligible set in (15). Then

\[
\boxed{\mathcal C_D(T)\mid\gcd_{\mathbb Z[T]}(A(T),B(T)).}
\tag{18}
\]

For example, `0011` has `a=630,zeta=1597`. The order `d=11` becomes eligible
at `n=6`, so

\[
\boxed{
\Phi_{11}(T)\mid\gcd(A,B)
\qquad(n\ge6).
}
\tag{19}
\]

Thus the tempting conjecture that `0011` has only the diagonal factor is
false beyond the small census.

### 4. Residual tests and exact size of the full automatic sector

Fix an eligible order `d`, and retain the notation `g,L_d` from (14).  Since
`g|zeta`, every exponent in its residual block is divisible by `g`.  Thus the
correct reduced variables are

\[
U=T^g,
\qquad
a_g=\frac ag,
\qquad
\zeta_g=\frac\zeta g,
\qquad
s=D\bmod L_d,
\tag{20a}
\]

and `(a_g,L_d)=1`.  In these variables the residual polynomial is

\[
R_{g,L_d,s}(U)
=
\sum_{v=0}^s(-1)^v
U^{\zeta_gv+a_g\beta_s(v)}
{s\brack v}_{U^{a_g}},
\qquad
\beta_s(v)
=\frac{(1-r)v^2+(2rs-r-1)v}{2}.
\tag{20b}
\]

Expand the residual Gaussian binomials as

\[
{s\brack v}_q=\sum_t p_{s,v}(t)q^t.
\]

For `c mod L_d`, define the signed residue totals and their reduced group-ring
polynomial by

\[
\rho_c=
\sum_{\substack{v,t\\
\zeta_gv+a_g(\beta_s(v)+t)\equiv c\pmod {L_d}}}
(-1)^vp_{s,v}(t),
\qquad
\overline R_{g,L_d,s}(X)=\sum_{c=0}^{L_d-1}\rho_cX^c.
\tag{20e}
\]

Then the exceptional residual condition is finite and exact at every eligible
order, prime or composite:

\[
\boxed{
B_0(1)=0
\iff
\Phi_{L_d}(X)\mid\overline R_{g,L_d,s}(X).
}
\tag{20f}
\]

For example, if `L_d=p^k`, then (20f) is equivalent to the finite block
equalities

\[
\rho_b=\rho_{b+p^{k-1}}=\cdots=\rho_{b+(p-1)p^{k-1}}
\qquad(0\le b<p^{k-1}).
\]

For a reduced order `L_d` with at least two distinct prime divisors, (20f) is
the exact cyclotomic-remainder test; unlike the prime case below, its solutions
are not yet classified.

For `r=4` and a reduced odd prime order `L_d=p`, (20f) admits a complete
closed form.  Put

\[
C_{g,s}
=\zeta_g+\frac{a_g(r+1)}2(s-1),
\qquad
N=2\zeta+a(r+1)(D-1),
\qquad
N_g=\frac Ng.
\tag{20g}
\]

Then

\[
\boxed{
B_0(1)=0
\iff
s\text{ is odd and }p\mid C_{g,s}.
}
\tag{20h}
\]

In particular every exceptional reduced prime divides `N_g`.  More strongly,
if `Phi_d^e` divides the residual block, then

\[
\boxed{e\le \nu_p(C_{g,s}).}
\tag{20i}
\]

For `r=4` and prime `p>=5`, the phase residual `P_0(1)` is nonzero: completing
the quadratic Gauss sum reduces it to a sum of four `p`-th roots, and a
polynomial of degree less than `p` with four nonnegative terms cannot be
divisible by `Phi_p`.  Thus (20h) is the only prime-order residual obstruction.

Put `G=gcd(a,zeta)`.  The prime exceptions, including all their possible
multiplicities, have subquadratic total degree.  Indeed, with

\[
M_g=\max\!\left(2,\left\lceil\frac{|N|}{2g}\right\rceil\right),
\]

let `R_prime(T)` be their product, with multiplicity, and put
`E_prime(D)=deg R_prime`.  Then

\[
\boxed{
E_{\rm prime}(D)
\le
|N|\sum_{g\mid G}\log_2M_g,
\qquad
\log_2\left|R_{\rm prime}^{\rm hom}(64,81)\right|
\le
(\log_2 145)E_{\rm prime}(D).
}
\tag{20j}
\]

At the best `G=71` height for the period-four `S=71` family,

\[
a=639,
\quad
\zeta=2272,
\quad
D=4n,
\quad
N=12780n+1349,
\]

and both reduced chains `g=1` and `g=71` must be included:

\[
\boxed{
E_{\rm prime}(D)
\le
N\left(
\log_2\left\lceil\frac N2\right\rceil
+\log_2\left\lceil\frac N{142}\right\rceil
\right)
=O(n\log n).
}
\tag{20k}
\]

There is also a uniform antisymmetric family, including composite orders,
forced by complement symmetry.  If `s` is odd, then

\[
\boxed{1-U^{C_{g,s}}\mid R_{g,L_d,s}(U).}
\tag{20l}
\]

Consequently every distinct antisymmetric order `d` divides `N`.  If
`A_D(T)` is the squarefree product of all such `Phi_d`, then

\[
\boxed{
A_D(T)\mid T^{|N|}-1,
\qquad
\deg A_D\le |N|,
\qquad
\log_2\left|A_D^{\rm hom}(64,81)\right|<|N|\log_2 81.
}
\tag{20m}
\]

Thus the complete reduced-prime sector and one copy of every antisymmetric
composite factor are `o(n^2)`.  In the best `G=71` row they leave the leading
`343.372048 n^2`-bit deficit unchanged.  This does not bound higher
multiplicity at composite orders.  In particular, genuinely
non-antisymmetric solutions of (20f), and extra powers of antisymmetric
composite factors, remain open.

When `G=1`, as for all three period-four `m=1` census
words, the product in (17) has

\[
\boxed{
\deg\mathcal C_D
=\frac{D^2}{8}
\prod_{p\mid a}\frac1{1+1/p}
+O(D\log^2D).
}
\tag{20}
\]

For `r=4`, the exact leading degree and homogeneous-specialization savings are

| digit sum `S` | `deg(C_D)/n^2` | saving bits per `n^2` | remaining required bits per `n^2` |
|---:|---:|---:|---:|
| 69 | `23/16` | `9.113534` | `980.760537` |
| 70 | `35/48` | `4.622807` | `999.597265` |
| 71 | `71/48` | `9.377695` | `1009.188379` |

At other starting heights, divisors of `G` amplify the factor density. Define

\[
K_g=
\frac3{\pi^2}\varphi(g)
\prod_{p\mid a/g}\frac1{1+1/p}
\prod_{\substack{p\mid g\\p\nmid a/g}}\frac1{1-1/p^2}.
\tag{20c}
\]

Then

\[
\boxed{
\deg\mathcal C_D
=\frac{\pi^2D^2}{24}\sum_{g\mid G}K_g
+O(D\log^2D).
}
\tag{20d}
\]

The largest possible `G` in the three period-four families gives

| `S` | maximal `G` | first height `m` | `deg(C_D)/n^2` | saving bits per `n^2` | remaining deficit |
|---:|---:|---:|---:|---:|---:|
| 69 | 23 | 14 | `34.5` | `218.724825` | `771.149247` |
| 70 | 35 | 14 | `35` | `221.894750` | `782.325323` |
| 71 | 71 | 19 | `106.5` | `675.194025` | `343.372048` |

Even in the most favorable automatic case, the best Padé exponent is only
approximately `0.997872`, still strictly below one.

Therefore

\[
\boxed{
\text{the full automatic cyclotomic sector cannot close period four.}
}
\tag{21}
\]

The classified exceptional sectors do not alter this conclusion: all reduced
prime exceptions, with multiplicity, contribute only `O(n log n)` degree, and
one copy of every antisymmetric composite exception contributes only `O(n)`.
Any successful cancellation must therefore come from genuinely composite
residual multiplicity of quadratic total size, noncyclotomic factors, or an
arithmetic specialization gcd.

### 5. Honest denominator clearing and residual support

Let `C(T)` be any common monic polynomial factor and let `H` be a common degree
bound for the Padé polynomials. Its homogenization genuinely divides both
cleared integers:

\[
\boxed{
C^{\rm hom}(64,81)
\mid
81^HA(64/81),
\quad
C^{\rm hom}(64,81)
\mid
81^HB(64/81).
}
\tag{22}
\]

Moreover `C^hom(64,81)=1 mod3` for a product of the cyclotomic factors above,
so the divisor is not an artifact of clearing powers of `81`.

After removing the full polynomial gcd, write the primitive coprime cofactors
as `P,Q in Z[T]`. For every prime `ell` not dividing `81`,

\[
\boxed{
\nu_\ell\!\left(
\gcd(P^{\rm hom}(64,81),Q^{\rm hom}(64,81))
\right)
\le\nu_\ell(\operatorname{Res}(P,Q)).
}
\tag{23}
\]

Thus every remaining prime-to-`81` gcd is a genuine arithmetic specialization
factor supported by the resultant.

## Proof

### Diagonal Boolean moments

The Gaussian-binomial subset identity rewrites the denominator at `T=e^z` as

\[
B(e^z)
=\sum_{I\subseteq\{0,\ldots,D-1\}}
(-1)^{|I|}e^{zE(I)},
\tag{24}
\]

where, with `x_i=1_(i in I)`,

\[
E(I)
=\sum_i\bigl(ai+\zeta+ar(D-1)\bigr)x_i
-ar\sum_{i<j}x_ix_j.
\tag{25}
\]

Alternating Boolean summation kills every multilinear monomial not containing
all `D` variables. Since `E^h` has degree at most `2h`, every moment below
`ceil(D/2)` vanishes.

If `D=2g`, the first surviving moment consists exactly of perfect matchings of
the `D` variables. Their number is `D!/(2^g g!)`, giving (5). If `D=2g+1`,
the first denominator moment consists of `g` disjoint edges plus a singleton,
or one wedge together with `g-1` disjoint edges. Counting and combining these
two classes gives (6)--(7).

For the numerator one obtains the companion identity

\[
A(e^z)
=\sum_I(-1)^{|I|}
\sum_{j=0}^{r-1}\sum_{t<D-|I|}
e^{z(E(I)+H_j(t))},
\tag{26}
\]

where

\[
H_j(t)=c_j+\zeta t+ajt+\frac{ar,t(t-1)}2.
\tag{27}
\]

Its `z^h` coefficient has Boolean degree at most `2h+1`. In the odd case the
first top coefficient reduces to

\[
\int_0^1(1-x^2)^g\,dx
=\frac{4^g(g!)^2}{(2g+1)!},
\]

which yields (8). The even denominator or odd numerator therefore has exact
order `floor(D/2)`, proving (4).

### Root-of-unity block factorization

Finite `q`-Lucas gives the unified factorization

\[
B_\tau(Y)
=(1-\omega Y^{L_d})^{K_d}B_{0,\tau}(Y),
\tag{28}
\]

where

\[
\omega=
\begin{cases}
Z^{L_d},&L_d\text{ odd},\\
(-1)^rZ^{L_d},&L_d\text{ even}.
\end{cases}
\]

Indeed, for `k=uL_d+v` with even `L_d`, the extra signs satisfy

\[
q^{\beta(k)-\beta(v)}=(-1)^{u(r+1)},
\qquad
(-1)^k=(-1)^v.
\]

The phase coefficients obey `f_(t+L_d)=omega f_t`, so

\[
F_\tau(Y)
=\frac{P_\tau(Y)}{1-\omega Y^{L_d}},
\qquad
\deg P_\tau<L_d.
\tag{29}
\]

Condition `g|zeta` is exactly `Z^(L_d)=1`. When `r=4`, this makes `omega=1`
for both parities. If `K_d>=2`, equations (28)--(29) make `B_tau F_tau` a
polynomial of degree at most `D-1` with a remaining factor
`(1-Y^(L_d))^(K_d-1)`. It equals the defining truncation `A_tau(Y)`, proving
at least one common copy of `Phi_d`.

For the growing multiplicity, put `Theta=Y d/dY`, `v=q^r`, and

\[
P_T(Y)=\prod_{i=0}^{D-1}(1-Zq^iY).
\]

The exact operator forms are

\[
B_T(Y)=v^{F_D(\Theta)}P_T(Y),
\qquad
F_D(u)=Du-\frac{u(u+1)}2,
\tag{30}
\]

and, phasewise,

\[
G_j(Y)=v^{G(\Theta)}(1-Zq^jY)^{-1},
\qquad
G(u)=\frac{u(u-1)}2.
\tag{31}
\]

At `T=tau`, the `K_d` complete blocks of `P_tau` each equal
`Delta=1-Y^(L_d)`. For even `L_d`, the quadratic multiplier remains
`L_d`-periodic because `r` is even. In a transverse derivative
`T=tau e^z`, differentiating the product destroys at most one block, while
each occurrence of `F_D(Theta)` has differential order two. Hence

\[
\left.\partial_z^hB_{\tau e^z}(Y)\right|_{z=0}
\text{ is divisible by }
\Delta^{K_d-2h}.
\tag{32}
\]

The `h`-th derivative of the tail series has denominator at worst
`Delta^(2h+1)`. Every `h`-th derivative of the product `BF`, and hence of its
degree-`D-1` truncation, is therefore divisible by
`Delta^(K_d-2h-1)`. Evaluating at `Y=1` proves

\[
\operatorname{ord}_\tau B\ge\lceil K_d/2\rceil,
\qquad
\operatorname{ord}_\tau A\ge\lfloor K_d/2\rfloor,
\]

which is (16).

If `K_d=2m` and the residual `B_0(1)` is nonzero, the `m`-th transverse
derivative of `B` is

\[
(ar)^m(-1/2)^m(2m)!L_d^{2m}B_0(1)\ne0.
\]

If `K_d=2m+1` and `B_0(1)P_0(1)` is nonzero, the `m`-th derivative of `A` is

\[
(-1)^m2^m(ar)^mL_d^{2m}(m!)^2B_0(1)P_0(1)\ne0.
\]

These formulas prove the asserted generic exactness and identify the only
residual obstruction.

### Residual classification

If `tau` has order `d=gL_d`, then `tau^g` has order `L_d`.  Eligibility gives
`g|zeta`, while `g|a` by definition, so division of every residual exponent
by `g` gives (20a)--(20b).  Reducing its exponents modulo `L_d` gives (20e).
Since `Phi_{L_d}` is the minimal polynomial of `tau^g`, this proves (20f).
For `L_d=p^k`, the displayed block equalities follow at once from

\[
\Phi_{p^k}(X)=1+X^{p^{k-1}}+\cdots+X^{(p-1)p^{k-1}}.
\]

The symmetry of Gaussian binomials gives the exact ratio between the `v` and
`s-v` summands of (20b):

\[
\frac{\text{summand}(s-v)}{\text{summand}(v)}
=(-1)^sU^{(s-2v)C_{g,s}}.
\tag{33}
\]

Indeed,

\[
\beta_s(s-v)-\beta_s(v)
=(s-2v)\frac{(r+1)(s-1)}2.
\]

When `s` is odd, pairing `v` with `s-v` in (33) proves (20l); if
`C_{g,s}=0`, the pairs cancel identically.

Now specialize to `r=4` and a reduced odd prime `p=L_d`.  Write `s=2u` or
`s=2u+1`.  Applying the exact diagonal formulas (4)--(6) to the reduced
parameters `a_g,zeta_g` gives

\[
\left.\frac{R_{g,p,2u}(U)}{(U-1)^u}\right|_{U=1}
=\frac{(2u)!(-a_gr)^u}{2^uu!},
\tag{34}
\]

and

\[
\left.\frac{R_{g,p,2u+1}(U)}{(U-1)^{u+1}}\right|_{U=1}
=-
\frac{(2u+1)!(-a_gr)^u}{2^uu!}
C_{g,2u+1}.
\tag{35}
\]

Because `s<p`, `(p,a_g)=1`, and `p` is odd, every factor in (34) is a
`p`-adic unit.  Thus `Phi_p` cannot divide an even-`s` residual: otherwise,
after removing the displayed power of `U-1`, evaluation at `U=1` would make
(34) divisible by `Phi_p(1)=p`.  The same argument applied to (35) shows that
an odd-`s` zero requires `p|C_{g,s}`.  Conversely, (33) cancels every pair at
a primitive `p`-th root when `p|C_{g,s}`.  This proves (20h).  If `Phi_p^e`
divides the residual, then the same evaluation makes (35) divisible by `p^e`;
all its other factors are `p`-adic units, proving (20i).

For completeness, the phase residual at `p>=5` is nonzero.  Completing its
quadratic Gauss sum writes it as a nonzero Gauss factor times a sum of four
`p`-th roots.  If that sum vanished, collecting equal roots would give a
polynomial of degree less than `p` with nonnegative integral coefficients,
coefficient sum four, and divisible by `Phi_p`.  Such a polynomial would be a
constant multiple of `Phi_p` and would have coefficient sum divisible by
`p`, a contradiction.

It remains to prove the quantitative bounds.  Since

\[
N_g-2C_{g,s}=a_g(r+1)(D-s),
\]

every prime in (20h) divides `N_g`.  Also `|C_{g,s}|<=M_g` in the
period-four range.  Hence, using `phi(gp)<=gp`, (20i), and the elementary
inequality that the sum of the distinct prime divisors of a positive integer
is at most that integer,

\[
\begin{aligned}
\deg R_{\rm prime}
&\le
\sum_{g\mid G}\sum_{p\mid N_g}
gp\,\nu_p(C_{g,s})\\
&\le
\sum_{g\mid G}g|N_g|\log_2M_g
=|N|\sum_{g\mid G}\log_2M_g.
\end{aligned}
\]

Moreover

\[
|\Phi_d^{\rm hom}(64,81)|
=\prod_{\substack{1\le j\le d\\(j,d)=1}}
|81-64e^{2\pi ij/d}|
\le145^{\varphi(d)},
\]

which proves (20j), and substitution gives (20k).

Finally, an antisymmetric order has `L_d|C_{g,s}`, so `d|gC_{g,s}`.  Since

\[
N-2gC_{g,s}=a(r+1)(D-s)
\]

is also divisible by `d`, every such `d` divides `N`.  The product of its
distinct cyclotomic factors is therefore a subproduct of `T^|N|-1`, the
product of `Phi_d(T)` over the positive divisors `d` of `|N|`.  After
homogenization it divides
`81^|N|-64^|N|`, proving all three bounds in (20m).  The estimates (20j) and
(20m) are respectively `O(n log n)` and `O(n)`, so neither changes a
quadratic leading deficit.  They do not control extra powers at composite
orders.  For a reduced order with at least two distinct prime divisors the
Taylor argument loses all force because `Phi_L(1)=1`; prime-power block
solutions and their higher multiplicities are likewise not classified.  This
is exactly the remaining composite obstruction recorded after (20m).

### Asymptotic size and clearing

For `G=1`, eligible orders in the period-four case are all `d` coprime to `a`,
and the degree in (17) is

\[
\sum_{\substack{d\le D/2\\(d,a)=1}}
\varphi(d)\left\lfloor\frac{D}{2d}\right\rfloor.
\]

Euler products and partial summation give (20). Also, for `0<x<1`,
`log Phi_d(x)=O(tau(d))`; hence

\[
\log_2\mathcal C_D^{\rm hom}(64,81)
=\deg(\mathcal C_D)\log_2 81+O(D\log^2D).
\]

Substitution of `a=9S,D=4n` gives the first table. Reparameterizing a general
eligible order as `d=gL`, with `g|G` and `(L,a/g)=1`, gives (20c)--(20d) and
the arbitrary-height table. This proves (21).

Finally, if `A=CA_1` and `deg A<=H`, then

\[
81^HA(64/81)
=C^{\rm hom}(64,81)
81^{H-\deg C}A_1(64/81),
\]

and the final factor is integral. This proves (22). Bezout's resultant identity
for the coprime homogenized cofactors proves (23). ∎

## Motivation

`PR20/L-9410` left common-factor cancellation as the only visible route across
the period-four Padé threshold. This lemma finds the full automatic source of
such cancellation: a linear diagonal factor and a genuinely quadratic family
of even and odd cyclotomic factors with growing multiplicity. It then
quantifies the bad news precisely: even the most favorable automatic sector
remains far below the required constant.

## Dependency audit

- The formal Padé definitions come from `PR20/L-9410`; every new divisibility
  and multiplicity statement is proved after retaining `T` as a variable.
- The only algebraic inputs are finite `q`-Lucas, Gaussian-binomial subset
  expansion, and elementary cyclotomic/resultant facts.
- Symbolic census checks were used for discovery but not for the stated general
  factors or asymptotic constants.
- No irrationality conclusion from the source branch is assumed.

## Gap audit

- Reduced-prime residual blocks are completely classified by (20h), and even
  with multiplicity they save only `O(n log n)` bits after homogenization.
- The distinct antisymmetric composite blocks save only `O(n)` bits.  Thus at
  the best `G=71` height these classified sectors leave the leading
  `343.372048 n^2`-bit deficit unchanged.
- Non-antisymmetric composite solutions of (20f), and higher multiplicity at
  antisymmetric composite orders, remain unbounded.
- Noncyclotomic polynomial factors and resultant-supported arithmetic gcds
  remain possible.
- A Hadamard resultant bound of order `O(Sn^3)` is too weak to exclude the
  required `O(Sn^2)` specialization saving.

## Adversarial tests

- The factor `(T-1)^floor(D/2)` is exact, but it is not the full polynomial gcd.
- `Phi_11` for `0011,n>=6` disproves extrapolation from the `n<=3` census.
- Residual classification must use `U=T^g`; at `G=71`, both `g=1` and `g=71`
  reduced prime chains occur.  Counting only the pure-order chain gives a
  false upper bound.
- Polynomial divisibility is transported through homogeneous clearing; merely
  evaluating rational polynomials without this check would overstate the gcd.
- The quantitative refutation in (21) applies only to the automatic
  cyclotomic sector, not to every possible cancellation mechanism.

## Remaining uncertainty

The period-four rigidity theorem remains open. Its surviving cyclotomic target
is sharply localized to genuinely non-antisymmetric composite residual zeros
or higher composite multiplicity; noncyclotomic factors and unexpectedly large
resultant-supported arithmetic gcds also remain possible.

## Suggested next attack

`L-9828` proves that one exceptional copy at every reduced prime-power order
is already `o(n^2)`, but its exact valuation caps do not control higher common
multiplicity.  `L-9832` classifies the odd-prime-power range `p>s` exactly and
simply, leaving `p<=s`.  Classify that frontier and the finite residue
condition (20f) for reduced orders with at least two prime divisors.  Then bound the
residual resultant after removing every automatic and classified exceptional
cyclotomic factor.  Any rescue still needs hundreds of additional gcd bits per
`n^2`, so coarse constant-factor bounds can already be decisive.

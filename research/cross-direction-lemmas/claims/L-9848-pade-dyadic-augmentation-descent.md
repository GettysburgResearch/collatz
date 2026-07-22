# L-9848 — Dyadic residual zeros reduce to one characteristic-two augmentation slack

Claim ID: `L-9848`  
Title: Exact doubling convolution and augmentation-slack criterion for period-four dyadic Padé residuals  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`  
Reviewing agents: `gpt56-synthesis-01-a`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9816`, `L-9839`  
Scope: reduced dyadic orders `L=2^k`, actual remainders `s=4t<L`

## Definitions

Retain the reduced residual of `L-9839`,

\[
R_{a,\zeta,s}(U)
=
\sum_{v=0}^{s}(-1)^v
U^{\zeta v+a\beta_s(v)}
{s\brack v}_{U^a},
\qquad
\beta_s(v)=-3\binom v2+(4s-4)v,
\tag{1}
\]

where `a` is odd and `s=4t`.  Write

\[
\lambda_s(a,\zeta)
=\operatorname{ord}_{U-1}
\bigl(R_{a,\zeta,s}(U)\bmod2\bigr).
\tag{2}
\]

This order is finite in the two base layers proved below.  More generally,
finiteness is part of the augmentation problem isolated by this claim.

For `n>=0` and a 2-adic parameter `c`, put

\[
F_{n,c}(q)
=\sum_{v=0}^{n}
q^{cv-3\binom v2}{n\brack v}_q
\in\mathbf F_2[[q-1]].
\tag{3}
\]

Here and below, if `X=q-1` and `alpha in Z_2`, then

\[
q^\alpha=(1+X)^\alpha
=\sum_{h\ge0}\binom\alpha hX^h
\in\mathbf F_2[[X]],
\tag{3a}
\]

with the 2-adic binomial coefficients reduced modulo two. Thus (3) is
defined even when `c` is not an ordinary integer.

If `q=U^a`, the substitution `U\mapsto U^a` is an automorphism of
`F_2[[U-1]]`, because `a` is odd.  Under this automorphism (1) becomes (3)
with

\[
c=\zeta/a+4s-4\in\mathbf Z_2.
\tag{4}
\]

Thus `lambda_s(a,zeta)=ord_(q-1)F_(s,c)`.

For the forced lower dyadic factors of `L-9839`, set

\[
h_j=\left\lceil\frac12
\left\lfloor\frac{s}{2^j}\right\rfloor\right\rceil,
\qquad
A(s)=\sum_{\substack{j\ge1\\2^j\le s}}h_j\varphi(2^j).
\tag{5}
\]

## Statement

### 1. Exact subset form and exact doubling convolution

In characteristic two,

\[
\boxed{
F_{n,c}(q)
=\sum_{E\subseteq\{0,\ldots,n-1\}}
q^{c|E|+\sum_{i\in E}i-4\binom{|E|}{2}}.
}
\tag{6}
\]

For every `n` and every 2-adic `c`, finite `q`-Vandermonde gives

\[
\boxed{
F_{2n,c}(q)
=\sum_{j=0}^{n}
q^{cj-3\binom j2}{n\brack j}_q
F_{n,c+n-4j}(q).
}
\tag{7}
\]

Formula (7) is an exact dyadic descent inside the same one-parameter family;
there is no transverse Padé variable and no unproved genericity assumption.

### 2. Exact degree already consumed after reduction modulo two

For `s=4t`, let

\[
W(t)=\sum_{m=1}^{t}2^{\nu_2(m)}.
\tag{8}
\]

Then the lower factors in `L-9839` consume the exact augmentation degree

\[
\boxed{A(4t)=t+2W(t).}
\tag{9}
\]

Including the exact diagonal factor `(U-1)^(s/2)`, define the remaining
characteristic-two slack

\[
\delta_s(a,\zeta)
=\lambda_s(a,\zeta)-\frac{s}{2}-A(s).
\tag{10}
\]

Whenever `lambda_s` is finite, `delta_s>=0`.  If `L=2^k>s` and

\[
\boxed{\delta_s(a,\zeta)<\frac L2,}
\tag{11}
\]

then

\[
\boxed{\Phi_L(U)\nmid R_{a,\zeta,s}(U).}
\tag{12}
\]

Thus the remaining dyadic residual-zero problem is exactly reduced to an
augmentation-slack bound.  It no longer requires the weighted next jet in
`L-9839/(14e)` if (11) is established.

### 3. The first two actual dyadic remainder layers are nonexceptional

Uniformly for odd `a` and every integer `zeta`,

\[
\boxed{
\lambda_4(a,\zeta)=6,
\qquad
\lambda_8(a,\zeta)=14.
}
\tag{13}
\]

Consequently, for every dyadic target larger than the remainder,

\[
\boxed{
s\in\{4,8\},\quad L=2^k>s
\quad\Longrightarrow\quad
\Phi_L\nmid R_{a,\zeta,s}.
}
\tag{14}
\]

In particular the simple-residual hypothesis in `L-9839/(14e)` is vacuous
in the first two nonzero actual remainder layers.

### 4. Exact all-layer target left by the descent

The exact finite data, including (13), support the uniform identity

\[
\boxed{
\lambda_{4t}(a,\zeta)=4t+2W(t)
=\frac{s}{2}+A(s)+\frac{s}{4}.
}
\tag{15}
\]

Equation (15) is **not proved here**.  It is recorded as the precise next
algebraic target, not as a theorem.  Its equivalent binary recurrence is

\[
\Lambda_0=0,
\qquad
\Lambda_{2u}=2\Lambda_u+2u,
\qquad
\Lambda_{2u+1}=2\Lambda_u+2u+6,
\tag{16}
\]

where `Lambda_t=lambda_(4t)`.  If (15), or merely
`delta_(4t)<L/2`, is proved, then every actual dyadic target residual is
nonzero because `L>s`.

## Proof

The Gaussian subset identity is

\[
q^{\binom v2}{n\brack v}_q
=\sum_{\substack{E\subseteq\{0,\ldots,n-1\}\\|E|=v}}
q^{\sum_{i\in E}i}.
\tag{17}
\]

Multiplying it by `q^(-4 binom(v,2)+cv)` and summing over `v` proves (6).

For (7), use the form of finite `q`-Vandermonde

\[
{2n\brack v}_q
=\sum_{j+k=v}
q^{(n-j)k}{n\brack j}_q{n\brack k}_q.
\tag{18}
\]

The exponent in the `(j,k)` summand is

\[
\begin{aligned}
c(j+k)-3\binom{j+k}{2}+(n-j)k
&=cj-3\binom j2\\
&\quad +(c+n-4j)k-3\binom k2.
\end{aligned}
\tag{19}
\]

Summing first over `k` gives (7).

We next prove (9).  The `j=1` term in (5) is `t`.  For `j>=2`, put
`ell=j-2`.  Since `ceil(K/2)` counts the odd integers not exceeding `K`,

\[
\begin{aligned}
A(4t)-t
&=\sum_{\ell\ge0}2^{\ell+1}
\#\{u\ge1:(2u-1)2^\ell\le t\}\\
&=\sum_{m=1}^{t}2^{\nu_2(m)+1}
=2W(t).
\end{aligned}
\tag{20}
\]

The second equality uses the unique decomposition
`m=(2u-1)2^ell`.  This proves (9).

By the exact diagonal formula in `L-9816`, `(U-1)^(s/2)` divides the
integer residual.  By `L-9839/(6)`, every
`Phi_(2^j)^(h_j)` with `2^j<=s` also divides it.  These monic factors are
pairwise coprime over `Z[U]`, so their product divides the residual.  After
reduction modulo two,

\[
\overline{\Phi_{2^j}(U)}=(U-1)^{\varphi(2^j)}
\qquad(j\ge1).
\tag{21}
\]

Hence `lambda_s>=s/2+A(s)`.  If the distinct target `Phi_L` also divided
the residual, the same argument would give

\[
\lambda_s\ge\frac{s}{2}+A(s)+\frac L2.
\tag{22}
\]

This is the contrapositive of (11)--(12).  Notice that (21) counts the
diagonal `Phi_1=U-1` separately; no lower or target factor is counted twice.

It remains to prove (13).  By (6), reduction of the exponents modulo `8`
and `16`, respectively, gives the exact group-ring identities

\[
\boxed{
F_{4,c}(q)\equiv q+q^3+q^5+q^7
=q(1+q)^6\pmod{q^8-1}
}
\tag{23}
\]

for every `c mod 8`, and

\[
\boxed{
F_{8,c}(q)\equiv
1+q^2+q^4+\cdots+q^{14}
=(1+q)^{14}\pmod{q^{16}-1}
}
\tag{24}
\]

for every `c mod 16`.  These are complete finite residue identities, not
numerical root tests.  We first justify exponent reduction for a 2-adic
parameter.  If `m` is `8` or `16`, substitution `q=1+X` identifies

\[
\mathbf F_2[q,q^{-1}]/(q^m-1)
\cong\mathbf F_2[X]/(X^m),
\tag{24a}
\]

because `m` is a power of two.  If `alpha'=alpha+m beta` in `Z_2`, then

\[
(1+X)^{\alpha'-\alpha}
=(1+X)^{m\beta}
=(1+X^m)^\beta
\equiv1\pmod {X^m}.
\tag{24b}
\]

Hence the image of `q^alpha` modulo `(q-1)^m` depends only on
`alpha modulo m`, and the ordinary group-ring monomial with that residue is
its rigorous representative.  In particular, the complete systems for `c`
in (23)--(24) cover every `c in Z_2`.

For a direct proof-grade reproduction, let `P_(i,v)^(c)` be the parity
enumerator, modulo `q^m-1`, of the exponents in (6) coming from the
`v`-subsets of `{0,...,i-1}`.  Adding the new coordinate `i` gives

\[
P_{0,0}^{(c)}=1,
\qquad
P_{i+1,v}^{(c)}
=P_{i,v}^{(c)}
+q^{c+i-4(v-1)}P_{i,v-1}^{(c)},
\qquad
F_{n,c}=\sum_vP_{n,v}^{(c)}.
\tag{24c}
\]

Encoding a support by the bit mask whose bit `e` is the coefficient of
`q^e`, iteration of (24c) gives the complete table

| `n` | complete `c` system | mask for each listed `c` | support modulo `2n` |
|---:|:---|:---|:---|
| `4` | `0,...,7` | `0xAA` eight times | `{1,3,5,7}` |
| `8` | `0,...,15` | `0x5555` sixteen times | `{0,2,4,6,8,10,12,14}` |

Equivalently, for each subset one records

\[
c|E|+\sum_{i\in E}i-4\binom{|E|}{2}\pmod{2n}
\tag{25}
\]

and cancels residue classes occurring an even number of times.  Recurrence
(24c) performs exactly this enumeration without a root evaluation; the two
masks list every surviving coefficient for every parameter residue.

In characteristic two,

\[
q^8-1=(q-1)^8,
\qquad
q^{16}-1=(q-1)^{16}.
\tag{26}
\]

Therefore (23) determines the expansion through augmentation degree `7`
and has exact order `6`; (24) determines it through degree `15` and has
exact order `14`.  The truncation argument (24a)--(24b) proves these exact
orders for every `c in Z_2`.  This proves (13), including nonvanishing of
the mod-two series.

Equivalently, put `q=1+X`.  The coefficient of `X^h` is

\[
\gamma_h(n,c)
=\sum_{E\subseteq\{0,\ldots,n-1\}}
\binom{c|E|+\sum_{i\in E}i-4\binom{|E|}{2}}{h}
\pmod2.
\tag{27}
\]

Lucas' theorem applied to (27) recovers
`(gamma_0,...,gamma_6)=(0,0,0,0,0,0,1)` and
`(gamma_0,...,gamma_14)=(0,...,0,1)` from (23)--(24).

For `s=4`, equations (9) and (13) give

\[
A(4)=3,
\qquad
\delta_4=6-2-3=1.
\tag{28}
\]

Every target has `L>=8`, hence `L/2>=4>1`.  For `s=8`,

\[
A(8)=8,
\qquad
\delta_8=14-4-8=2,
\tag{29}
\]

and every target has `L>=16`, hence `L/2>=8>2`.  Applying (11) proves
(14).  This completes the proved assertions. ∎

## Motivation

`L-9839/(14e)` shows that a simple target residual zero does not by itself
control the first excess transverse jet: a sheared derivative and a weighted
`Y`-moment can cancel.  In characteristic two, however, every dyadic
cyclotomic factor collapses to a known power of the single augmentation
factor `U-1`.  The already-forced diagonal and lower dyadic factors consume
most of that order.  Only the slack (10) remains available to a new target.

The conjectural exact slack is only `s/4`, whereas a target with `L>s`
would cost `L/2`.  Thus the augmentation route would make the transverse
problem vacuous rather than solve its weighted noncancellation term by term.

## Dependency audit

- The residual formula and forced lower factors are from `L-9839`.
- Exact diagonal divisibility is from the denominator diagonal formula in
  `L-9816`.
- The subset form and doubling convolution are proved here from the Gaussian
  subset identity and finite `q`-Vandermonde.
- The lower-factor degree (9) is an elementary unique-2-adic-decomposition
  count.
- The base layers use only Lucas' theorem and the explicitly displayed finite
  residue audit; no numerical approximation or root search is used.

## Gap audit

- The full identity (15) is conjectural.  No claim beyond `s=4,8` uses it.
- Formula (7) is exact, but extracting the unit-normalized binary transitions
  in (16) from it remains open.  The missing step must control cancellations
  among the shifted parameters `c+n-4j`; uniform leading order alone is not
  enough.
- The theorem proves target nonvanishing for the first two actual nonzero
  remainder layers.  It does not yet prove all-layer dyadic nonvanishing.
- For an actual even macro count, (14) makes `L-9839/(14e)` vacuous in these
  two layers.  Odd-macro numerator/phase jets are outside this claim.

## Adversarial tests

- One must include the exact diagonal factor `Phi_1^(s/2)` before comparing
  augmentation orders.  Omitting it loses `s/2` degrees and obscures the
  contradiction.
- The lower factors and the target are distinct because `2^j<=s<L`; this is
  what permits multiplication before reduction modulo two.
- Over `F_2`, signs disappear, but the quadratic exponent does not: the
  `-4 binom(|E|,2)` term in (6) is essential to the orders `6` and `14`.
- The exact doubling convolution (7) does not by itself prove (16).  Treating
  all shifted normalized units as equal would miss the very cancellations
  responsible for the extra augmentation slack.

## Remaining uncertainty

Does the augmentation order satisfy the all-layer identity (15), or at least
the targetwise slack bound (11), for every actual remainder `s=4t`?  The
proved convolution exposes the correct descent family, but a unit-preserving
pairing argument is still missing beyond `s=8`.

## Suggested next attack

Prove the following unit-valued dyadic pairing statement in
`F_2[[X]]`, uniformly in `c`:

\[
F_{8u,c}(1+X)
=X^{2u}F_{4u,c_0}(1+X)F_{4u,c_1}(1+X)\,U_{u,c}(X),
\tag{30}
\]

and

\[
F_{8u+4,c}(1+X)
=X^{2u+6}F_{4u,c_0'}(1+X)F_{4u,c_1'}(1+X)\,V_{u,c}(X),
\tag{31}
\]

where all shifted `c`-parameters remain in `Z_2` and
`U_(u,c)(0)=V_(u,c)(0)=1`.  Equations (30)--(31) give (16) immediately.
The exact convolution (7) is the algebraic starting point; the required new
ingredient is a triangular pairing which exposes the units rather than
assuming their leading terms cannot cancel.

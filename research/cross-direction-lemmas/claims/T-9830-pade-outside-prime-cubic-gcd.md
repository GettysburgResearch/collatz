# T-9830 -- The combined Pade height problem is an outside-prime cubic-gcd problem

Claim ID: `T-9830`
Title: Normalized combined-moment minors retain a cubic prime-to-six core, while canonical Pade values satisfy exact two-prime distance laws
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-period-ten`
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9821`, `T-9824`, `T-9826`; frozen `PR20/L-9408`, `L-9410`, `Q-9413` at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1`
Scope: every positive periodic stack word; especially primitive period ten
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Put

\[
 T={64\over81},
 \qquad \lambda=T^{9S},
 \qquad R=\lambda^r,
 \qquad X=T^{9m},
 \qquad Z=T^\zeta.
\tag{1}
\]

For the positive word `W` of length `r`, retain the transfer exponents

\[
 P_W(Xz)=\sum_{h=0}^{r-1}C_hz^h,
 \qquad C_h=T^{\gamma_h},
 \qquad0=\gamma_0<\cdots<\gamma_{r-1}.
\tag{2}
\]

Write

\[
 \gamma_*=\gamma_{r-1}.
\tag{3}
\]

In the notation of `PR20/L-9408`,

\[
 \zeta=r+9A_r(W)+9mr,
 \qquad
 \gamma_h=h+9A_h(W)+9mh,
\tag{4}
\]

and `A_r-A_(r-1)=S`.  Hence the fixed positive integer

\[
 \boxed{
 \kappa=\zeta+9S(r-1)-\gamma_*
 =1+9m+9Sr.}
\tag{5}
\]

The combined moments and generating series are

\[
 u_N=R^{N(N-1)/2}Z^NP_W(X\lambda^N),
 \qquad
 H(Y)=\sum_{N\ge0}u_NY^N.
\tag{6}
\]

Let

\[
 B_n(Y)=\sum_{k=0}^nb_{n,k}Y^k,
 \qquad b_{n,0}=1,
\tag{7}
\]

be the unique canonical denominator from `T-9821`, let `A_n(Y)` be its Pade
numerator, and put

\[
 R_n={A_n(1)\over B_n(1)}.
\tag{8}
\]

The real and 2-adic limits of `H(1)` remain separate and are denoted by
`H_infinity` and `H_2`.

All asymptotic statements below take `n -> infinity` with the positive word
`W` and its starting parameters `S,m` fixed.  Constants written
`O_(W,m)(...)` are not asserted to be uniform across changing words or
starting heights.

For `0<=k<=n`, let

\[
 \mathcal T_{n,k}=\{0,1,\ldots,n\}\setminus\{n-k\},
\tag{9}
\]

written in increasing order, and define the maximal Hankel minor

\[
 D_{n,k}
 =\det(u_{i+t})_{\substack{0\le i<n\\t\in\mathcal T_{n,k}}}.
\tag{10}
\]

Thus `D_(n,0)` is the base Hankel determinant.  Cramer's rule and `T-9826`
give

\[
 \boxed{b_{n,k}=(-1)^k{D_{n,k}\over D_{n,0}}.}
\tag{11}
\]

## Statement 1 -- the base Schur quotient has a cubic prime-to-six core

Retain

\[
 K_n={n(n-1)(n-2)\over6},
 \qquad
 L_n={n(n-1)(2n+5)\over6}.
\tag{12}
\]

For the normalized base alternant `mathcal Q_n` of `T-9824`, put

\[
 a_n=9S(r-1)K_n,
 \qquad
 b_n^+=n\gamma_*+9S(r-1)L_n,
\tag{13}
\]

and

\[
 \boxed{
 d_n=b_n^+-a_n
 =n\gamma_*+{9S(r-1)\over6}n(n-1)(n+7).}
\tag{14}
\]

Then there is a polynomial

\[
 \boxed{F_{n,0}(T)\in\mathbf Z_{\ge0}[T]}
\tag{15}
\]

such that

\[
 \boxed{\mathcal Q_n(T)=T^{a_n}F_{n,0}(T),}
\tag{16}
\]

and

\[
 F_{n,0}(0)=1,
 \qquad F_{n,0}\text{ is monic},
 \qquad\deg F_{n,0}=d_n.
\tag{17}
\]

Define its homogeneous specialization by

\[
 \boxed{G_{n,0}=81^{d_n}F_{n,0}(64/81).}
\tag{18}
\]

Then

\[
 \boxed{G_{n,0}\in\mathbf Z_{>0},\qquad\gcd(G_{n,0},6)=1,}
\tag{19}
\]

and

\[
 \boxed{
 81^{d_n}\le G_{n,0}
 \le81^{d_n}r^n(2r-1)^{n(n-1)/2}.}
\tag{20}
\]

Consequently

\[
 \boxed{
 \mathcal Q_n(64/81)
 ={2^{6a_n}G_{n,0}\over3^{4b_n^+}}}
\tag{21}
\]

is already in lowest terms, and

\[
 \boxed{\log_2G_{n,0}=d_n\log_2 81+O_r(n^2).}
\tag{22}
\]

For period ten,

\[
 \boxed{
 d_n=n\gamma_9+{81S\over6}n(n-1)(n+7),}
\tag{23}
\]

so

\[
 \boxed{
 \log_2G_{n,0}
 =54S\log_2(3)n^3+O_{W,m}(n^2)
 =85.5879750389\ldots S n^3+O_{W,m}(n^2).}
\tag{24}
\]

### Proof

The positive Schur expansion of `T-9824/(4)` shows that `mathcal Q_n(T)` has
nonnegative integral coefficients.  Its unique 2-adic selector is the
all-zero phase choice and the lowest principal-specialization tableau.  Its
exponent is `a_n`, and its coefficient is one.

The unique 3-adic selector is the all-`(r-1)` phase choice and the highest
tableau.  Its exponent is `b_n^+`, again with coefficient one.  This proves
(16)--(17).

At `T=1`, all phase weights equal one.  Weyl's dimension formula gives

\[
 s_\mu(1^n)
 =\prod_{1\le i<j\le n}
 {\mu_i-\mu_j+j-i\over j-i}.
\tag{25}
\]

For every partition occurring in `T-9824/(4)`, each factor in (25) is at most
`2r-1`.  There are `r^n` phase vectors.  Therefore

\[
 F_{n,0}(1)\le r^n(2r-1)^{n(n-1)/2}.
\tag{26}
\]

Since `0<T<1`,

\[
 1\le F_{n,0}(T)\le F_{n,0}(1),
\tag{27}
\]

which proves (20).

In the homogenization

\[
 G_{n,0}=\sum_{j=0}^{d_n}c_j64^j81^{d_n-j},
\tag{28}
\]

the constant term makes `G_(n,0)` odd, while the monic leading term gives

\[
 G_{n,0}\equiv64^{d_n}\not\equiv0\pmod3.
\tag{29}
\]

This proves (19).  Equation (21) follows from `b_n^+=a_n+d_n`, and
(22)--(24) follow from (20). **QED**

## Statement 2 -- exact prime-to-six Cramer-unit decomposition

Define

\[
 \boxed{\alpha_{n,k}=k\{\zeta+9Sr(n-1)\},}
\tag{30}
\]

\[
 \boxed{
 \beta_{n,k}
 =k\{\zeta+9Sr(2n-k-1)+9S(r-1)\}.}
\tag{31}
\]

After removing the common specialized Vandermonde and the least remaining
power of `T` from `D_(n,k)`, there is a monic polynomial

\[
 F_{n,k}(T)\in\mathbf Z_{\ge0}[T],
 \qquad F_{n,k}(0)=1,
\tag{32}
\]

of degree

\[
 \boxed{d_{n,k}=d_n+\beta_{n,k}-\alpha_{n,k}.}
\tag{33}
\]

Put

\[
 \boxed{G_{n,k}=81^{d_{n,k}}F_{n,k}(64/81).}
\tag{34}
\]

Then

\[
 G_{n,k}\in\mathbf Z_{>0},
 \qquad\gcd(G_{n,k},6)=1,
\tag{35}
\]

and the canonical coefficient has the exact factorization

\[
 \boxed{
 b_{n,k}=(-1)^k
 {2^{6\alpha_{n,k}}G_{n,k}
  \over3^{4\beta_{n,k}}G_{n,0}}.}
\tag{36}
\]

Moreover,

\[
 \boxed{
 81^{d_{n,k}}\le G_{n,k}
 \le81^{d_{n,k}}r^n(3r-1)^{n(n-1)/2}.}
\tag{37}
\]

Thus

\[
 \log_2G_{n,k}=d_{n,k}\log_2 81+O_r(n^2).
\tag{38}
\]

If

\[
 g_{n,k}=\gcd(G_{n,k},G_{n,0}),
\tag{39}
\]

then the reduced height of `b_(n,k)` is exactly

\[
 \boxed{
 H(b_{n,k})
 =\max\left\{
 2^{6\alpha_{n,k}}{G_{n,k}\over g_{n,k}},
 3^{4\beta_{n,k}}{G_{n,0}\over g_{n,k}}
 \right\}.}
\tag{40}
\]

In particular, every contribution not visible at two and three is precisely
a gcd problem between the integers `G_(n,k)`.

### Proof

For the column set `mathcal T_(n,k)`, the row-factor-stripped determinant is

\[
 \det\!\left[
 z_i^{rt_j}P_W(X\lambda^{t_j}z_i)
 \right]_{0\le i,j<n}.
\tag{41}
\]

Expanding each column in its phase index gives generalized alternants with
strictly increasing exponents.  Division by the ordinary Vandermonde produces
Schur polynomials with nonnegative integral coefficients.

The reverse 2-adic selector and identity 3-adic selector are unique.  By
`T-9821/(15)--(16)`, their differences from the base minor are exactly
`alpha_(n,k)` and `beta_(n,k)`.  Therefore the difference of the exponent
spans is

\[
 d_{n,k}-d_n=\beta_{n,k}-\alpha_{n,k},
\tag{42}
\]

proving (33).

At `T=64/81`,

\[
 {D_{n,k}\over D_{n,0}}
 =T^{\alpha_{n,k}}{F_{n,k}(T)\over F_{n,0}(T)}.
\tag{43}
\]

Using

\[
 d_{n,k}-d_n=\beta_{n,k}-\alpha_{n,k}
\tag{44}
\]

in the two homogenizations gives

\[
 T^{\alpha_{n,k}}81^{d_n-d_{n,k}}
 ={2^{6\alpha_{n,k}}\over3^{4\beta_{n,k}}},
\tag{45}
\]

which, together with the Cramer sign (11), proves (36).

For `mathcal T_(n,k)`, one has

\[
 t_j-t_i\le(j-i)+1.
\tag{46}
\]

Hence every Weyl factor in the corresponding Schur specialization is at most

\[
 {r(t_j-t_i)+(r-1)\over j-i}\le3r-1.
\tag{47}
\]

Summing over the `r^n` phase choices proves (37).  The parity and modulo-three
argument from Statement 1 proves (35).  Finally, all displayed 2- and
3-powers are coprime to the `G`-factors, so ordinary reduction yields (40).
**QED**

## Statement 3 -- the raw pair is cubic, and quadratic primitive height is equivalent to cubic outside-prime gcd

Put

\[
 \boxed{
 \beta_n=\beta_{n,n}
 =n\{\zeta+9Sr(n-1)+9S(r-1)\}.}
\tag{48}
\]

Define the common clearing factor

\[
 \boxed{\mathcal D_n=3^{4\beta_n}G_{n,0},}
\tag{49}
\]

and the raw evaluated integers

\[
 \boxed{
 \widehat A_n=\mathcal D_nA_n(1),
 \qquad
 \widehat B_n=\mathcal D_nB_n(1).}
\tag{50}
\]

Then `widehat A_n,widehat B_n` are integers.  Explicitly,

\[
 \boxed{
 \widehat B_n
 =\sum_{k=0}^n(-1)^k
 2^{6\alpha_{n,k}}
 3^{4(\beta_n-\beta_{n,k})}G_{n,k}.}
\tag{51}
\]

Their exact endpoint valuations are

\[
 \boxed{v_2(A_n(1))=v_2(B_n(1))=0,}
\tag{52}
\]

\[
 \boxed{v_3(B_n(1))=-4\beta_n,}
\tag{53}
\]

\[
 \boxed{v_3(A_n(1))=-4(\beta_n-\kappa).}
\tag{54}
\]

Consequently

\[
 v_2(\widehat A_n)=v_2(\widehat B_n)=0,
\tag{55}
\]

\[
 v_3(\widehat B_n)=0,
 \qquad
 v_3(\widehat A_n)=4\kappa.
\tag{56}
\]

Thus

\[
 \boxed{
 \gcd(\widehat A_n,\widehat B_n)
 \text{ is coprime to }6.}
\tag{57}
\]

Furthermore,

\[
 \boxed{B_n(1)\longrightarrow1\quad\text{in the real embedding},}
\tag{58}
\]

and

\[
 \boxed{A_n(1)\longrightarrow H_\infty>0.}
\tag{59}
\]

If

\[
 N_n^{\rm raw}=\max\{|\widehat A_n|,|\widehat B_n|\},
\tag{60}
\]

then

\[
 \boxed{
 \log_2N_n^{\rm raw}
 =d_n\log_2 81+4\beta_n\log_2 3+O_{W,m}(n^2),}
\tag{61}
\]

and therefore

\[
 \boxed{
 \log_2N_n^{\rm raw}
 =6S(r-1)\log_2(3)n^3+O_{W,m}(n^2).}
\tag{62}
\]

For period ten,

\[
 \boxed{
 \log_2N_n^{\rm raw}
 =54S\log_2(3)n^3+O_{W,m}(n^2).}
\tag{63}
\]

Let

\[
 g_n=\gcd(|\widehat A_n|,|\widehat B_n|).
\tag{64}
\]

Then the usual reduced rational height satisfies the exact identity

\[
 \boxed{H(R_n)={N_n^{\rm raw}\over g_n},}
\tag{65}
\]

and hence

\[
 \boxed{
 \log_2H(R_n)
 =d_n\log_2 81+4\beta_n\log_2 3-
 \log_2g_n+O_{W,m}(n^2).}
\tag{66}
\]

Therefore, along any index set, an `O(n^2)` primitive-height bound is
equivalent to

\[
 \boxed{
 \log_2g_n
 =6S(r-1)\log_2(3)n^3+O_{W,m}(n^2).}
\tag{67}
\]

For period ten this is

\[
 \boxed{
 \log_2g_n=54S\log_2(3)n^3+O_{W,m}(n^2).}
\tag{68}
\]

By (57), this almost-total cubic cancellation must be supported entirely at
primes at least five.

### Proof

Equation (36) immediately proves that `mathcal D_n B_n(1)` is integral and
gives (51).

The largest possible 3-denominator exponent in a term of `A_n(1)` is obtained
by maximizing

\[
 \beta_{n,k}+9Sr{s(s-1)\over2}+\zeta s+\gamma_*+9S(r-1)s
\tag{69}
\]

subject to `k+s<=n-1`.  The unique maximum occurs at

\[
 k=n-1,
 \qquad s=0,
\tag{70}
\]

and equals

\[
 \beta_{n,n-1}+\gamma_*=\beta_n-\kappa.
\tag{71}
\]

Thus `mathcal D_n A_n(1)` is also integral, and (53)--(54) follow from the
unique maximizing terms.

At two, `B_n(1)` has constant term one and every nonconstant coefficient has
positive valuation.  In `A_n(1)`, the degree-zero term is

\[
 u_0=P_W(X)=1+\sum_{h=1}^{r-1}T^{\gamma_h},
\tag{72}
\]

a 2-adic unit, while every other contribution has positive valuation.  This
proves (52), and hence (55)--(57).

It remains to prove the real convergence needed to distinguish raw size from
gcd cancellation.  Put

\[
 q=T^{9S},
 \qquad
 \mathscr P=\sum_{h=0}^{r-1}T^{\gamma_h},
 \qquad
 \mathscr C_q=\prod_{j\ge1}(1-q^j)^{-1},
 \qquad M=\mathscr P\mathscr C_q.
\tag{73}
\]

The principal specialization formula gives, after removal of its least power
of `q`,

\[
 s_\mu(1,q,\ldots,q^{n-1})
 \le\prod_{1\le i<j\le n}(1-q^{j-i})^{-1}
 \le\mathscr C_q^n.
\tag{74}
\]

Summing the phase weights gives at most `mathscr P^n`.  Therefore

\[
 1\le F_{n,k}(T)\le M^n.
\tag{75}
\]

Equations (30) and (36) now give

\[
 |b_{n,k}|\le M^nT^{\alpha_{n,k}}.
\tag{76}
\]

Since `q<=T^9<1/8`,

\[
 \mathscr C_q<{7\over6},
 \qquad
 \mathscr P<\sum_{h\ge0}T^h={81\over17}.
\tag{77}
\]

For the first inequality, the elementary product bound

\[
 \prod_{j\ge1}(1-q^j)
 \ge(1-q)\left(1-\sum_{j\ge2}q^j\right)
 =1-q-q^2
 \ge{55\over64}>{6\over7}
\tag{78}
\]

at `q<=1/8` gives a reciprocal below `7/6`.  Therefore

\[
 MT^{9Sr}
 <{7\over6}{81\over17}{1\over8}
 ={189\over272}<1.
\tag{79}
\]

Hence

\[
 \sum_{k=1}^n|b_{n,k}|
 \le M^n
 {T^{\zeta+9Sr(n-1)}
  \over1-T^{\zeta+9Sr(n-1)}}
 \longrightarrow0.
\tag{80}
\]

This proves `B_n(1)->1`.

If

\[
 H_j=\sum_{s=0}^ju_s,
\tag{81}
\]

then

\[
 A_n(1)=\sum_{k=0}^{n-1}b_{n,k}H_{n-1-k}.
\tag{82}
\]

The positive partial sums `H_j` are bounded by `H_infinity`, while
`H_j->H_infinity`.  Equation (80) therefore proves (59).

It follows that both raw integers in (50) have size comparable, up to fixed
multiplicative constants, to `mathcal D_n`.  Applying (20) to `G_(n,0)`
proves (61)--(63).  Division by their ordinary gcd proves (65)--(68). **QED**

## Statement 4 -- exact 3-adic distance ladder and the unavoidable half-error height floor

The evaluated canonical values have the fixed 3-adic signature

\[
 \boxed{v_3(R_n)=4\kappa.}
\tag{83}
\]

For every `m>n>=1`,

\[
 \boxed{
 v_2(R_m-R_n)
 =E_n=12\zeta n+81Sr\,n(n-1),}
\tag{84}
\]

as in `T-9826`, and additionally

\[
 \boxed{
 v_3(R_m-R_n)
 =J_n=4\{\kappa+9Sr\,n\}.}
\tag{85}
\]

Consequently

\[
 \boxed{H(R_m-R_n)\ge2^{E_n}3^{J_n}.}
\tag{86}
\]

Using the elementary rational-height inequality

\[
 H(x-y)\le2H(x)H(y),
\tag{87}
\]

one obtains

\[
 \boxed{
 \log_2H(R_n)+\log_2H(R_m)
 \ge E_n+J_n\log_2 3-1.}
\tag{88}
\]

In particular,

\[
 \boxed{
 \max\{\log_2H(R_n),\log_2H(R_{n+1})\}
 \ge{E_n+J_n\log_2 3-1\over2}.}
\tag{89}
\]

For period ten,

\[
 E_n=12\zeta n+810S\,n(n-1),
\tag{90}
\]

\[
 J_n=4\{1+9m+90S+90Sn\},
\tag{91}
\]

and therefore

\[
 \boxed{
 \begin{aligned}
 \max\{\log_2H(R_n),\log_2H(R_{n+1})\}
 \ge{}&405S\,n(n-1)+6\zeta n\\
 &+2(1+9m+90S+90Sn)\log_2 3-{1\over2}.
 \end{aligned}}
\tag{92}
\]

Thus a full-sequence estimate

\[
 \log_2H(R_n)\le(81Sr-\eta)n^2+o(n^2)
\tag{93}
\]

can hold only if

\[
 \boxed{\eta\le{81Sr\over2}.}
\tag{94}
\]

For period ten this necessary condition is

\[
 \boxed{\eta\le405S.}
\tag{95}
\]

This restriction applies to the full sequence, or to a subsequence with
asymptotically adjacent indices.  It does not exclude a highly lacunary
subsequence: the height of its much later member may absorb the distance lower
bound.

### Proof

Equation (83) follows immediately from (53)--(54).

The consecutive Pade identity is

\[
 A_{n+1}(Y)B_n(Y)-A_n(Y)B_{n+1}(Y)
 =\varepsilon_{n,0}Y^{2n}.
\tag{96}
\]

Hence

\[
 R_{n+1}-R_n
 ={\varepsilon_{n,0}\over B_n(1)B_{n+1}(1)}.
\tag{97}
\]

For the base Hankel determinant, `T-9821/(9)` gives the `T`-exponent

\[
 \begin{aligned}
 \mathcal E_3(n)={}&\zeta n(n-1)+18SrK_n+n\gamma_*\\
 &+9S\left\{(r-1)n(n-1)
 +r{n(n-1)(2n-1)\over6}\right\}.
 \end{aligned}
\tag{98}
\]

Since

\[
 v_3(\varepsilon_{n,0})
 =-4\{\mathcal E_3(n+1)-\mathcal E_3(n)\},
\tag{99}
\]

subtraction of (53) at orders `n` and `n+1` gives

\[
 v_3(R_{n+1}-R_n)=4\{\kappa+9Sr\,n\}.
\tag{100}
\]

These consecutive valuations increase strictly with `n`.  For `m>n`,

\[
 R_m-R_n=\sum_{j=n}^{m-1}(R_{j+1}-R_j),
\tag{101}
\]

and the first term has uniquely least 3-adic valuation.  This proves (85)
without assuming that `H` converges 3-adically.

Equation (84) is `T-9826/(18)`.  If `R_m-R_n=a/b` is reduced, the positive
valuations (84)--(85) imply

\[
 2^{E_n}3^{J_n}\mid a,
 \qquad\gcd(b,6)=1,
\tag{102}
\]

which proves (86).  Equation (87) then proves (88)--(89).  The leading term
in `E_n` gives (94), and specialization to `r=10` gives (90)--(95). **QED**

## Consequence for the period-ten route

The desired quadratic primitive-height estimate is not obtained here.
Instead, the remaining requirement is identified exactly:

\[
 \boxed{
 \text{period-ten quadratic height requires an almost-total cubic gcd
 among the evaluated raw integers, supported only at primes }\ge5.}
\tag{103}
\]

The visible Vandermonde and all 2-/3-adic monomial factors have already been
removed before this gcd appears.  Thus neither the opposite tropical
selectors nor the ordinary Vandermonde can prove `T-9821/(23)`.

A successful continuation must prove a new cross-minor polynomial factor, a
resultant-supported arithmetic specialization gcd, or an equivalent
cancellation among the integers `G_(n,k)` and the evaluated sums (50)--(51).

## Gap audit

- No lower bound of the required size is proved for `g_n`.
- No upper bound refuting such a gcd is proved either.
- The cubic estimate concerns the raw cleared pair.  It is not itself a cubic
  lower bound for the reduced rational height.
- Additive cancellation is separated from gcd cancellation by
  `A_n(1)->H_infinity>0` and `B_n(1)->1`.
- The gcd in (64) is necessarily prime to six; endpoint valuations cannot
  create it.
- The height floor (89) constrains consecutive or nonlacunary orders, not an
  arbitrarily sparse subsequence.
- The real limit `H_infinity`, the 2-adic limit `H_2`, and the finite 3-adic
  distance computation are not identified.
- No period-ten irrationality or Collatz conclusion is claimed.

## Suggested next attack

Factor or bound the specialization gcd `g_n` directly.  The only viable
quadratic-height route is now an outside-prime correlation among the Schur
cores `G_(n,k)` and the evaluated sums.  A modular resultant, primitive-prime
argument, or cross-minor content theorem must account for a cubic amount of
prime-to-six cancellation; local endpoint valuations alone cannot do so.

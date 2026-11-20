# Ordinary primitive trace: exact endpoint reduction and the unresolved estimate

**PROPOSED derivations; no Collatz closure is claimed.** This note follows the
actual ordinary operators of PR156, head
`c5cb84502c7289705d59a8781a65fd845b9b6b14`, especially
`research/global-rigidity-20261120/SMOOTHING_BOUNDARY.md`, SM4--SM5. Its
all-word trace and the coincidence of the two least positive representatives
are already present there. The contributions here are the explicit geometric
remainder, the finite endpoint head formulation, and precise checks on two
suggested closing shortcuts. No novelty claim is made for the underlying
affine word or inverse-column calculus.

The attempted target is PR144's particular-vector bound

$$
D_q:=\|A_2^q(1/n)\|_2^2
 =\sum_{n\ge1,\ n\text{ odd}}\frac{J_q(n)^4}{U^q(n)^2}
 =O((q+1)^2).                                                   \tag{1}
$$

Here $U(n)=(3n+1)/2^{a(n)}$, $a(n)=v_2(3n+1)$,
$J_q(n)=3^q/2^{\sum_{j<q}a(U^jn)}$, and the norm uses counting measure
on **all positive odd integers**, with no killing. This target would exclude
nonperiodic positive orbits using PR150's reciprocal budget, as explained in
PR156 OE5. It would still need a separate exclusion of nontrivial positive
cycles.

## 1. The two primitive representatives are the same exact affine orbit

For a word $w=(a_1,\ldots,a_q)$, $a_i\ge1$, put

$$
A_j=\sum_{i\le j}a_i,\quad A=A_q,\quad m=3^q,\quad
C_w=\sum_{j=0}^{q-1}3^{q-1-j}2^{A_j},\quad
J_w=m/2^A,\quad \gamma_w=C_w/2^A.
$$

The affine equation is

$$
2^A t=mn+C_w.                                                 \tag{2}
$$

Let $r_w$ be the least positive **odd** representative of
$2^At\equiv C_w\pmod m$. Thus $1\le r_w<2m$. Each reverse step
$(2^a t-1)/3$, when integral at a positive odd endpoint, is positive
and odd. The single final congruence gives integrality at all reverse
intermediates by reducing modulo three and inducting. Consequently

$$
b_w=(2^Ar_w-C_w)/m
$$

is a positive odd source realizing exactly the word, and

$$
1\le b_w<2^{A+1},\qquad r_w=J_w b_w+\gamma_w\ge J_w+\gamma_w.   \tag{3}
$$

Conversely, every positive ordinary source with this word is exactly

$$
n=b_w+2^{A+1}\ell,\qquad
t=r_w+2m\ell,\qquad \ell=0,1,\ldots.                         \tag{4}
$$

Thus the least positive binary source and least positive odd ternary
endpoint correspond to the same orbit. No additional positivity shift is
needed. It is important to use odd representatives: the least residue in
$[0,m)$ can have the wrong parity.

The empty word has $m=1$, $C=0$, $J=1$, $b=r=1$, so the
statements below also cover $q=0$.

## 2. A two-sided geometric bound for all nonprimitive lifts

Define the primitive head and the rest by

$$
P_q=\sum_{|w|=q}\frac{J_w^4}{r_w^2},\qquad R_q=D_q-P_q.
$$

All sums have nonnegative terms; regrouping does not presume a probabilistic
law for any forward ordinary trajectory. Equation (4) gives

$$
R_q=\sum_w J_w^4\sum_{\ell\ge1}(r_w+2m\ell)^{-2}.
$$

Since $0<r_w<2m$,

$$
\frac{\zeta(2)-1}{4m^2}
\le\sum_{\ell\ge1}(r_w+2m\ell)^{-2}
\le\frac{\zeta(2)}{4m^2}.
$$

The unrestricted gap sum is exact:

$$
\sum_{|w|=q}J_w^4
 =81^q\left(\sum_{a\ge1}2^{-4a}\right)^q
 =\left(\frac{27}{5}\right)^q.
$$

Therefore

$$
\boxed{\frac{\zeta(2)-1}{4}\left(\frac35\right)^q
\le R_q\le
\frac{\zeta(2)}4\left(\frac35\right)^q.}                     \tag{5}
$$

In particular, the full moment bound (1) is **equivalent** to
$P_q=O((q+1)^2)$. The tail is already exponentially small. Improving a
large-source/lift estimate alone cannot prove the remaining bound.

## 3. The head is a finite set of actual positive endpoints

Let

$$
H_q(t)=\sum_{U^q n=t}J_q(n)^4,
\qquad t\ge1\text{ odd}.
$$

Every inverse word is either admissible or inadmissible according to the
single congruence modulo $3^q$; all its positive odd endpoints give positive
ordinary inverse sources. Hence $H_q$ is periodic on odd integers with
period $2\cdot3^q$, and

$$
\boxed{P_q=\sum_{\substack{1\le t<2\cdot3^q\\t\text{ odd}}}
               \frac{H_q(t)}{t^2}.}                          \tag{6}
$$

The exact sum over one such period is

$$
\sum_{\substack{1\le t<2\cdot3^q\\t\text{ odd}}}H_q(t)
 =\left(\frac{27}{5}\right)^q.                              \tag{7}
$$

For $q\ge1$, all entries at multiples of three are zero. No infinite gap
cutoff is needed to compute an individual finite head. Put
$L_q=2\cdot3^{q-1}$. Since the order of 2 modulo $3^q$ is $L_q$,

$$
H_q(t)=\frac{81}{1-2^{-4L_q}}
\sum_{\substack{1\le a\le L_q\\2^at\equiv1\ (3)}}
2^{-4a}H_{q-1}\!\left(\frac{2^at-1}{3}\right).               \tag{8}
$$

The argument of $H_{q-1}$ is evaluated modulo $3^{q-1}$ on its odd
representatives. This formula is obtained by grouping the original positive
gap sum into classes modulo $L_q$; it retains every hidden ternary lift.
It is not the uniform-lift averaged matrix criticized in PR155.

Let $F_q(y)=\sum_{1\le t\le y,\ t\text{ odd}}H_q(t)$ for
$1\le y\le 2\cdot3^q$. Partial summation yields the precise remaining
integral:

$$
\boxed{P_q=\frac14\left(\frac35\right)^q
       +2\int_1^{2\cdot3^q}\frac{F_q(y)}{y^3}\,dy.}          \tag{9}
$$

Thus the unproved arithmetic estimate is

$$
\int_1^{2\cdot3^q}\frac{F_q(y)}{y^3}\,dy=O((q+1)^2).        \tag{10}
$$

For example, $F_q(y)\le B(q+1)y^2$ for every $q,y$ would suffice;
that pointwise estimate has **not** been proved. The elementary total mass
(7), positive-source inequality (3), and uniform spectral bounds do not
give (10).

## 4. Independence does not even have the desired sign of effect

The following are calculations in deliberately artificial replacement
models, not claims about the actual representatives.

First replace every $r_w$, independently of its weight, by a uniformly
chosen odd ternary-unit representative in $[1,2m)$. There are $2m/3$
such representatives when $q\ge1$, and

$$
\frac{1}{2m/3}
\sum_{\substack{1\le r<2m\\r\text{ odd},\ 3\nmid r}}
 \sum_{\ell\ge0}(r+2m\ell)^{-2}
 =\frac{\pi^2}{6m}.
$$

This replacement would give the exponentially growing moment

$$
D_q^{\mathrm{uniform}}=\frac{\pi^2}{6}\left(\frac95\right)^q.
                                                                    \tag{11}
$$

Even retaining the elementary positive-source cutoff is insufficient in a
natural continuous replacement model. For each word let
$X_w$ be uniform on $[J_w+\gamma_w,2m]$, and put
$\beta_w=\gamma_w/J_w$. The interval is nonempty by (3), and elementary
integration gives

$$
\mathbb E[X_w^{-2}]=\frac{1}{2m(J_w+\gamma_w)}.
$$

Normalize word weights $J_w^3$. Their sum is $(27/7)^q$, so the
corresponding iid gap law is $\mathbb P(a=g)=7/8^g$. This is only a
normalization of the word sum. Under that law,

$$
\beta_w=\frac13\sum_{j=0}^{q-1}\frac{2^{A_j}}{3^j},\qquad
\mathbb E\beta_w=\frac32\left(1-(7/9)^q\right)\le\frac32.
$$

Jensen's inequality and positivity then give

$$
\begin{split}
D_q^{\mathrm{cutoff\ uniform}}
 &=\frac12\left(\frac97\right)^q
     \mathbb E\frac1{1+\beta_w},\\
\frac15\left(\frac97\right)^q
 &\le D_q^{\mathrm{cutoff\ uniform}}
 \le\frac12\left(\frac97\right)^q.                          \tag{12}
\end{split}
$$

Consequently a successful estimate needs a specifically arithmetic joint
bound on the true endpoint and its word weight. Merely imposing
$r_w\ge J_w+\gamma_w$ and appealing to generic endpoint mixing does not
supply that estimate. Equations (11)--(12) neither refute (1) nor describe
the actual orbit law.

## 5. A boundary for common power supersolutions

Consider the exact inverse-weight operator

$$
(Lf)(t)=\sum_{\substack{a\ge1\\2^at\equiv1\ (3)}}
             \left(\frac3{2^a}\right)^4
             f\!\left(\frac{2^at-1}{3}\right),
\quad H_q=L^q\mathbf1.
$$

Suppose a positive function satisfies $Lw\le\rho w$ and
$c\,t^\theta\le w(t)\le C\,t^\theta$ at all positive odd integers,
with $0<c\le C<\infty$ and $\theta<4$. Take
$t_h=2\cdot3^h-1$. Its $h$ repeated inverse gap-one steps are ordinary,
positive and integral, and end at $n_h=2^{h+1}-1$. Therefore

$$
\rho^h C t_h^\theta
 \ge L^h w(t_h)
 \ge (3/2)^{4h}c n_h^\theta.
$$

Taking $h$-th roots and passing to the limit proves

$$
\rho\ge(3/2)^{4-\theta}>1.                                  \tag{13}
$$

Thus a subquartic power-comparable positive supersolution cannot be
contracting. This does **not** rule out a highly nonuniform positive
supersolution, a bound only on $L^q\mathbf1$, or the particular-vector
moment (1). It also does not invoke the unit-circle essential-spectrum
argument; the witnesses here are explicit ordinary inverse chains.

## 6. Attempted closure and its actual stopping point

The canonical pair-process upper bound in PR146, head
`6863d298187af8b2619efbf78cc4b0aa8e627393`, gives
$O(X/\sqrt{\log X})$ permanent tripling failures. Combined with PR155's
ordinary coercivity, it does not reach a power saving below the
source-qualified $X^{0.84}$ boundary lower bound. The logarithmic-scale
increments are not summable, and neither Boolean labels nor the pair
process supplies a new independent arithmetic sample after transport.

The fixed-source moment attack therefore isolated the exact inverse-column
mass in (10). The binary and ternary positive representatives coincide;
their determinant/congruence relation alone supplies only (3). The two
natural independence replacements grow exponentially, while the common
power supersolutions fail on (13). No bound on (10), no exclusion of a
permanent ordinary separated pair, and no exclusion of nontrivial cycles
was obtained. These are remaining mathematical obligations, not numerical
precision issues.

The accompanying checker is a small exact regression: it reconstructs
ordinary words and both representatives, checks complete untruncated inverse
columns through q=5, verifies period masses, and replays the inverse-one
family. Its finite checks support the formulas, not (1) or (10).

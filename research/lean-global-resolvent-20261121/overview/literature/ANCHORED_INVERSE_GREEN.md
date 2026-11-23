# An admissibility-sensitive inverse Green estimate

## Status and outcome

**Proposed written analytic derivation; not Lean formalized; no Collatz closure.**

**Later integration:** [ABEL_CANONICAL_COMPARISON.md](ABEL_CANONICAL_COMPARISON.md)
uses PR180's finite canonical envelope to justify the actual Abel parent-tail
limit interchange. The common critical profile below can now be chosen
harmonic, so its defect `h-Ph` vanishes. The finite floor-boundary and terminal
transport terms remain. The original nonperiodic constant `h(q)<=8q` stays
valid for this common Abel limit; substituting the distinct harmonic envelope
`G` would require adjusting that constant. The original proof and its frozen
CFJ input are preserved below.

The result below is a pointwise estimate for the complete inverse operator on
actual positive odd integers. It does not replace that operator by its Haar
average. It also constructs the positive excessive profile needed for the
change of measure, so that existence of a finite ordinary trace is not a
hidden assumption.

The one non-elementary input is the uniform finite residue atom floor implied
by PR180's written fixed-total theorem (CFJ), at
`cf91e46fa9fbadba3df7942202a5197c134d0ce0`,
`research/lean-forward-band-20261121/JOINT_CLOCK_MIXING.md`.
That theorem is itself an analytic deduction from Tao's specified renewal
estimate, not a Lean theorem. Nothing here promotes its verification status.

For a fixed floor `m >= 1`, write `L_m` for actual accelerated inverse
transport, retaining only positive odd ternary-unit states at least `m`.
There is a positive finite excessive profile `h`, constructed in Section 2,
such that, if `q >= m` is not periodic and

\[
\rho=39/40,\qquad 1+\rho<s\le2,
\]

then

\[
\boxed{
\sum_{k=0}^{\infty} L_m^k\!\left(\frac{h(x)}{x^s}\right)(q)
\le K_s(m)\frac{h(q)}q,
\qquad
K_s(m)=\frac{5(s-1)}{s-1-\rho}
  \exp\!\left(\frac{200}{3}m^{-1/40}\right)
  m^{1+\rho-s}.
} \tag{G}
\]

In particular `K_s(m) -> 0` as `m -> infinity`. Since the constructed profile
satisfies `h(q) <= 8q` at nonperiodic targets, the right side is also at most
`8 K_s(m)`, uniformly over these targets. The displayed bound (G), without
this uniform `8` simplification, holds for the first-return-truncated Green
series at *every* target, including periodic ones.

This is a pointwise row bound. It is not a bound on the sum of all rows.
At a cycle wholly above the floor the complete Green series diverges, as it
must. A fixed escaping source can contribute at infinitely many different
rows. Sections 6 and 7 retain both phenomena explicitly.

## 1. Actual inverse words and the real constraint

Let

\[
U(x)=\frac{3x+1}{2^{v_2(3x+1)}}
\]

on positive odd integers. An inverse letter from an odd target `q` is

\[
x=\frac{2^e q-1}{3},\qquad e\ge1,
\]

provided `x` is an integer. It is then positive and odd, and `U(x)=q`
with valuation exactly `e`.

For a word read backwards from `q=x_0`, let

\[
3x_j+1=2^{e_j}x_{j-1},\quad
A_j=e_1+\cdots+e_j,\quad
\omega_j=3^j2^{-A_j},\quad
\beta_j=\sum_{i=1}^j3^{i-1}2^{-A_i}.
\]

Then the exact identities are

\[
q=\omega_j x_j+\beta_j,
\qquad
\beta_j=\frac13\sum_{i=1}^j\omega_i,
\qquad
0\le\beta_j<q.                                      \tag{1}
\]

Thus every legal inverse word at this fixed positive target satisfies

\[
\sum_{i=1}^j\omega_i<3q.                            \tag{2}
\]

This is a deterministic consequence of positivity. A purely ternary word
need not satisfy it. It is the point at which the negative ternary fixed
point `-1` is excluded from the actual positive-real process.

Define the retained real fraction

\[
Z_j=\frac{\omega_jx_j}{q}
 =\prod_{i=1}^j\frac{3x_i}{3x_i+1},\qquad Z_0=1.    \tag{3}
\]

Unlike a geometric probability, this fraction must not be dropped when
recovering physical inverse mass.

## 2. A finite positive excessive profile, with existence proved

Put

\[
\rho_j(q)=3^j\Pr(X_j=q\pmod{3^j}),\qquad \rho_0(q)=1,
\]

where `X_j` is the finite Syracuse offset with independent exponents having
probabilities `2^{-e}`. On positive odd targets, exact inverse reconstruction
gives

\[
\rho_j(q)=\sum_{U^j(x)=q}\omega_j(x).                \tag{4}
\]

Every source in this identity is an actual positive odd integer. In
particular, no real admissibility indicator was removed in passing from the
residue law to (4).

The finite densities obey the exact recurrence

\[
\rho_{j+1}(q)= (L_1\rho_j)(q),\qquad
(L_1v)(q)=\sum_{U(x)=q}\frac3{2^{v_2(3x+1)}}v(x).   \tag{5}
\]

Here `L_1` is the critical weighted inverse operator; its subscript is a
weight exponent, not the floor used later.

### 2.1 The lower input

The CFJ window contains at least `sqrt(j)` integer totals for every
sufficiently large `j`. The associated word families have disjoint totals.
Summing its lower bound `c_0/sqrt(j)` therefore gives an absolute
`alpha > 0` such that

\[
\rho_j(q)\ge\alpha                               \tag{6}
\]

for every positive odd unit `q` and every sufficiently large `j`, with one
onset independent of `q`. This finite-level statement, rather than an
almost-everywhere limiting density, is the sole analytic positivity input.

### 2.2 An elementary bound on cumulative mass

Let `S_N(q)=sum_{j=0}^N rho_j(q)`. If `q` is nonperiodic, a source can hit it
at only one accelerated depth. By (1), its contribution is at most `q/x`.

If `q` is periodic, let `eta` be the multiplier of one complete positive
cycle through `q`. The exact product formula gives

\[
\eta=\prod_{y\text{ in the cycle}}\frac{3y}{3y+1}
\le\frac{3q}{3q+1}<1.
\]

A source's later hits of `q` have geometric weights with ratio `eta`.
Consequently its total contribution is at most `q(3q+1)/x`.

Write `c_q=1` in the nonperiodic case, and use `c_q=3q+1` otherwise.
For sources `x <= exp(8N)`, their total contribution is at most

\[
q c_q\sum_{x\le e^{8N}}\frac1x\le q c_q(1+8N).      \tag{7}
\]

For the remaining sources, (1) implies
`A_j > (8N-log q)/log 2`. With

\[
u=\frac{\log(4/3)}{\log2},\qquad c=8u-\log6>0,
\]

the geometric moment `E[(4/3)^e]=2` and Markov's inequality give, after
dropping residue restrictions only in this upper estimate,

\[
\sum_{j=0}^N\sum_{\substack{U^j(x)=q\\x>e^{8N}}}\omega_j(x)
\le \frac65 q^u e^{-cN}.                            \tag{8}
\]

For `j=0`, the same inequality is interpreted directly if the displayed
threshold is negative; the exponential Markov bound is still valid.
Thus

\[
S_N(q)\le q c_q(1+8N)+\frac65q^u e^{-cN}.            \tag{9}
\]

The constant `8` is deliberately loose. No stopping conjecture was used to
separate the two cases for `q`.

### 2.3 Abel limits and excessiveness

For `0<r<1`, define

\[
H_r(q)=(1-r)\sum_{j=0}^{\infty}r^j\rho_j(q)
      =(1-r)^2\sum_{N=0}^{\infty}r^N S_N(q).         \tag{10}
\]

Equations (6) and (9) imply

\[
\liminf_{r\uparrow1}H_r(q)\ge\alpha,
\qquad
\limsup_{r\uparrow1}H_r(q)\le8q c_q                \tag{11}
\]

at every positive odd unit. Since that domain is countable, choose a common
sequence `r_l -> 1` along which every `H_{r_l}(q)` converges. Call its limit
`h(q)`, and put `h(q)=0` at odd multiples of three. Then

\[
\alpha\le h(q)<\infty,
\quad h(q)\le8q\ \text{if }q\text{ is nonperiodic},
\quad h(q)\le8q(3q+1)\ \text{always}.               \tag{12}
\]

For odd nonunits, `rho_j(q)=0` when `j>=1`, so their Abel limit is indeed
zero. From the exact nonnegative identity

\[
L_1H_r=\frac{H_r-(1-r)\rho_0}{r}
\]

and Fatou's lemma, applied to the countable parent sum, we obtain

\[
\boxed{L_1h\le h.}                                  \tag{13}
\]

We do **not** claim equality, uniqueness, canonical identification, or
convergence of the entire Abel family. Equality would require an additional
parent-tail argument. It is unnecessary for the estimate below.

In particular, the resulting Doob kernel

\[
P_h(q,x)=\frac3{2^{v_2(3x+1)}}\frac{h(x)}{h(q)}
\quad(U(x)=q)
\]

is a substochastic kernel on positive odd units. Its missing mass is sent to
a cemetery state. That auxiliary killing is not a declaration that any
ordinary Collatz trajectory has reached one.

## 3. Uniform packing for finite distinct ordinary segments

The following elementary extension is included to avoid assuming that a
finite preperiod is globally injective under every later iterate.

For any finite segment of a positive odd orbit whose entries are distinct,
let `N(X)` count its entries at most `X`. Then

\[
\boxed{N(X)\le5X^{39/40}\qquad(X\ge1).}              \tag{14}
\]

Proof. This is the cylinder split from T-A3-401 in
`research/astra-three-routes/pass2/ORBIT_MELLIN.md`, frozen at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, with a finite endpoint correction.
The details needed for that correction follow.

For a block of `k` odd steps with total valuation `A`, its sources occupy one
odd residue modulo `2^(A+1)`, and

\[
U^k(n)=3^k2^{-A}n+R,\qquad 0<R\le(3/2)^k-1.
\]

Take `b=floor(5k/3)` with `2^b <= X`. In the lane `A<=b`, the generating
function with parameter `4/5` gives the bound

\[
\frac32 X\eta^k,\qquad \eta^3=3125/3456.
\]

In the other lane, the images lie below
`sigma^k X+(3/2)^k-1`, where `sigma=3/2^(5/3)<eta`.
Delete at most the last `k` entries of the finite segment. The `k`-step
images of all remaining entries lie inside that same distinct segment and
are distinct. Counting positive odd endpoints therefore gives

\[
N(X)\le2X\eta^k+\frac12(3/2)^k+k.                  \tag{15}
\]

Choose `k=floor((3/5)log_2 X)`. The exact integer certificate
`8*3125^24 < 3456^24` gives `eta<2^(-1/24)`, while `eta>2/3`.
Thus the first two terms are less than
`3X^(39/40)+(1/2)X^(3/5)`. The added endpoint term is at most
`(3/5)log_2 X <= (3/5)X^(39/40)`. For the last elementary inequality, maximize
`log_2 X / X^(39/40)`; its maximum is
`1/((39/40)e log 2)<1`. When `k=0`, use `N(X)<=X` and
`X<2^(5/3)`. These bounds prove (14).

Exhaustion gives the same estimate for any infinite inverse path with no
repeated states. If every state on such a path is at least `m`, then, for
every `p>rho=39/40`, layer-cake summation gives

\[
\sum_j x_j^{-p}\le C_p m^{\rho-p},\qquad
C_p=\frac{5p}{p-\rho}.                             \tag{16}
\]

In particular, `C_1=200`. Combining (3) with `log(1+t)<=t` yields

\[
Z_j^{-1}\le
\exp\!\left(\frac13\sum_{i=1}^j\frac1{x_i}\right)
\le \exp\!\left(\frac{200}{3}m^{-1/40}\right).       \tag{17}
\]

The proof is written here from the exact finite cylinders. Garcia--Tal
orbit-sparsity results provide historical context; their theorem is not an
uninspected quantitative input to (14).

## 4. Exact Doob conversion to the physical inverse operator

Let `D_m` be the positive odd ternary units at least `m`, and define

\[
(L_m f)(q)=\sum_{\substack{x\in D_m\\U(x)=q}}f(x),
\qquad q\in D_m.                                   \tag{18}
\]

There is no branch probability in (18). It transports actual source mass.
Each edge carries its exact ordinary shortcut clock `v_2(3x+1)`, although
`k` in `L_m^k` counts accelerated odd steps.

For a legal inverse path of length `k`, multiplication of the Doob factors
telescopes:

\[
\Pr_h[x_0=q,\ldots,x_k=x]
=\omega_k\frac{h(x)}{h(q)}.                         \tag{19}
\]

Kill this auxiliary chain on exiting `D_m`, in addition to its cemetery
killing. Taking `w_s(x)=h(x)/x^s` and using (3), we obtain the exact identity

\[
\boxed{
(L_m^k w_s)(q)=\frac{h(q)}q
\mathbb E_q^h\left[
  \frac{X_k^{1-s}}{Z_k};\ k<\zeta_m
\right].
}                                                   \tag{20}
\]

Here a dead path contributes zero. Every finite legal path is still counted
with exactly its source weight on the left. No claim that auxiliary killing
is ordinary absorption is used in (20).

## 5. Proof of the pointwise Green estimate

If the target `q` is nonperiodic, no inverse path from it can repeat a state:
a repeat would put that state, and hence `q`, on a cycle. Each surviving
path therefore satisfies (16) and (17). Sum (20) in `k`, use Tonelli, and put
`p=s-1>rho` to get

\[
\begin{aligned}
\sum_{k\ge0}(L_m^k w_s)(q)
&=\frac{h(q)}q\mathbb E_q^h
  \sum_{k<\zeta_m}\frac{X_k^{-p}}{Z_k}\\
&\le\frac{h(q)}q
  \exp\!\left(\frac{200}{3}m^{-1/40}\right)
  C_p m^{\rho-p}.
\end{aligned}
\]

This is (G). The argument also works for finite paths and finite horizons,
with the same constants. No exchange of a signed series is involved.

For an arbitrary target, stop inverse paths before their first positive
return to `q`. Such paths have no repeated states: if an earlier state
repeated, determinism would imply that the root lies on that same cycle,
and the inverse path would already have returned to the root. The same
proof bounds this first-return-truncated series at all targets.

The restriction `s<=2` is useful because it lies in the averaged contraction
strip motivating the question. The proof itself is valid for all
`s>1+rho`; it does not use the averaged factor
`3^(s-1)/(2^s-1)`.

## 6. Exact cycle obstruction and finite source anchors

Suppose a positive odd cycle of length `r` stays in `D_m` and contains `q`.
For each `ell>=0`, one actual inverse word follows that cycle `ell` times
and starts again at `q`. Therefore

\[
(L_m^{\ell r}w_s)(q)\ge w_s(q)>0,
\qquad \sum_k(L_m^k w_s)(q)=\infty.                 \tag{21}
\]

The Doob formula retains the same obstruction. If `eta<1` is the cycle's
critical multiplier, the probability of following it `ell` times is
`eta^ell`, while `Z_(ell r)=eta^ell`. These factors cancel in (20).
Almost-sure departure of the auxiliary inverse chain from the cycle would
therefore not prove finite physical Green mass.

More generally, fix an actual source `x` whose first `k` odd iterates remain
in `D_m`. At its endpoint `q=U^k(x)`, its particular path contributes exactly

\[
w_s(x)
\]

to `(L_m^k w_s)(q)`. This finite source atom is not erased by a density norm,
an Abel limit, or the change of measure. If its forward orbit is escaping,
it contributes at infinitely many distinct target rows. Thus, by Tonelli,

\[
\sum_{q\in D_m}\sum_{k\ge0}(L_m^kw_s)(q)
=\sum_{x\in D_m}w_s(x)\,	au_m(x),                 \tag{22}
\]

where `tau_m` counts the number of surviving odd-time states and may be
infinite. Equation (22), rather than a pointwise row estimate, is the global
quantity needed for an absorbed Green criterion.

The bound `h(q)/q<=8` at nonperiodic roots is boundedness, not summability.
It does not control the left side of (22). Raising the floor along an
escaping trajectory removes its original source from the allowed inputs;
that operation cannot be used to claim decay of the original atom.

## 7. An anchored resolvent identity

The exact profile defect can also be kept at every stage. Put

\[
g(q)=h(q)/q,\quad
c(q)=\frac{h(q)}{q(3q+1)},\quad
a(q)=g(q)-c(q)=\frac{h(q)}{q+1/3}.
\]

Let

\[
\epsilon(q)=h(q)-(L_1h)(q)\ge0,
\]

and let `b_m(q)` be the contribution to the full parent sum
`sum_{U(x)=q} h(x)/(x+1/3)` from parents `x<m`. Direct calculation gives

\[
(I-L_m)g=\frac{\epsilon}{q}+b_m-L_m c.              \tag{23}
\]

The terms `epsilon/q` and `b_m` are retained. The former is the unproved
harmonic-equality defect of the constructed excessive profile; the latter
is an actual finite ordinary boundary term. Neither is a negligible set to
be quotiented away.

At a nonperiodic target, the Green estimate with `s=2` controls the positive
correction potential, since `c(x)<=h(x)/(3x^2)`:

\[
\sum_{k\ge0}L_m^k c(q)\le\frac13K_2(m)g(q).        \tag{24}
\]

For finite `N`, telescoping (23) gives the exact anchored identity

\[
g-L_m^{N+1}g
=\sum_{k=0}^{N}L_m^k\left(\frac{\epsilon}{q}+b_m\right)
 -\sum_{k=1}^{N+1}L_m^k c.                          \tag{25}
\]

The nonnegative boundary term and the terminal term are both visible.
Passing to an infinite-horizon identity would require controlling the
terminal term and the appropriate boundary series. No such control is
asserted here.

If a *separately justified* harmonic profile were used, `epsilon` would be
zero. Even then, the ordinary boundary `b_m` and possible mass transported
to infinity would remain. This is the anchored version of the renewal
question, not an automatic resolution of it.

## 8. Literature interface and the remaining step

Brofferio's published rational-affine boundary theorem identifies the
product of mean-contracting completions. For the Syracuse geometric law
these are the real and ternary factors: the drifts are
`log 3-2 log 2<0` and `-log 3<0`. This justifies retaining both coordinates
as the natural boundary setting. It does not supply ordinary diagonal trace
estimates or eliminate (22)'s fixed-source contributions.

Guivarc'h--Le Page's renewal theory for affine recursions motivates the use
of positive profiles and a change of measure. Its hypotheses and conclusions
concern the stated random affine walks; no theorem from it is used to assert
mixing of an actual prescribed Collatz orbit.

Recent primary-but-unreviewed rStation papers 12 and 19 already discuss a
canonical integer trace and its Doob inverse law. They were used to locate
that interface. The author's stationary-envelope and cylinder-energy
manuscripts were subsequently consulted directly for their exact integer
and Haar conclusions; their formal developments were not rebuilt. Section 2
instead constructs the weaker excessive profile sufficient here directly
from the repository's frozen finite atom input. It does not claim novelty
for Doob transforms, canonical traces, or orbit reciprocal summability.

The closing obligations are now sharply separated:

1. The pointwise nonperiodic Green bound (G) is proved in this written
   argument from the stated analytic input and elementary cylinder packing.
2. A surviving cycle creates the explicit pole (21); none is excluded.
3. A globally summable anchored potential or an all-source survivor loss is
   still required to control (22). Uniform pointwise boundedness and positive
   predecessor populations do not provide it.

### Source pins

- PR180, `cf91e46fa9fbadba3df7942202a5197c134d0ce0`,
  `research/lean-forward-band-20261121/JOINT_CLOCK_MIXING.md`, CFJ.
- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded
  values*, Forum of Mathematics, Pi 10 (2022), e12,
  [DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8),
  [author preprint](https://arxiv.org/abs/1909.03562).
  PR180 specifies Proposition 7.3, equation (7.10), and its prefix-separation
  dependencies. This note imports PR180's stated finite consequence, not
  a new theorem about a prescribed forward orbit from Tao's random law.
- Repository elementary cylinder split,
  `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`,
  `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-401.
- Sara Brofferio, *The Poisson boundary of random rational affinities*,
  Annales de l'Institut Fourier 56(2) (2006), 499--515,
  [DOI 10.5802/aif.2191](https://doi.org/10.5802/aif.2191),
  [primary PDF](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf).
- Yves Guivarc'h and Emile Le Page, *Spectral gap properties for linear
  random walks and Pareto's asymptotics for affine stochastic recursions*,
  Annales de l'Institut Henri Poincare, Probabilites et Statistiques 52(2)
  (2016), 503--574, [DOI 10.1214/15-AIHP668](https://doi.org/10.1214/15-AIHP668),
  [author preprint](https://arxiv.org/abs/1204.6004).
- *First-landing bounds and canonical inverse laws for Collatz*, rStation
  paper 12/v1, [primary manuscript](https://rstation.ai/problems/collatz/papers/12/v1).
  This is a literature lead, not a proof dependency here.
- *Geometry, integer fibres, and dyadic equidistribution of the joint Collatz
  affine law*, rStation paper 19/v2,
  [primary manuscript](https://rstation.ai/problems/collatz/papers/19).
  This is a literature lead, not a proof dependency here.
- Lucas Valbuena, *A positive semicontinuous density for the Syracuse
  stationary law*,
  [author's source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/positive-stationary-envelope.tex).
  Its stronger canonical identification is not imported in Section 2.
- Lucas Valbuena, *Quadratic cylinder energy and integrability of the
  Syracuse law*,
  [author's source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/quadratic-cylinder-energy.tex).
  Its Haar conclusions are discussed in the separate trace-height note;
  they are not a dependency of the Green bound.

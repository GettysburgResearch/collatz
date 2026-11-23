# Testing recurrence and affine-boundary machinery against ordinary escape

**Status: written deductions, with the imported hypotheses listed below. No
universal Collatz proof and no new Lean theorem are claimed.** This attack
tests two substantial literature theorems on the actual operators. The
recurrence theorem encounters an explicitly nonzero directed-clock term.
The affine renewal theorem applies, but its sharp real tail yields an
ordinary-orbit bound weaker than the elementary edge bound. The final
section records a precise, additionally conditional moving-fibre requirement.

## 1. Pinned inputs and their status

The repository is `GettysburgResearch/collatz`.

| Source | Exact commit | Input used |
|---|---|---|
| PR185 | `4b0c2c27812db555061f5d9006de82a87e7e364f` | `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, equations (7)--(15), (19), and (22)--(25). |
| PR183 | `68345f60a4f757acb42a69a4ac95910f8ce26163` | `research/profound-step-20261122/operator/WOLD_CHANNELS.md`, equations (W4)--(W8). |
| PR180 | `a9f471543d7fed0a76f348e6d97a9d6d44fa369e` | `research/central-step-20261122/UNIVERSAL_SOURCE.md`, the exact copied-word obstruction and its retained-unit qualification. |

Let `N` be the positive odd ternary units that are not themselves periodic
under the accelerated map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Forward transport is killed on first entering a periodic state. An escaping
component below is a component on which this never happens; its existence
is assumed temporarily, never asserted.

PR185 supplies, by a written derivation,

\[
0<\nu(q)\le A<\infty,\qquad
\sum_{Ux=q}\nu(x)=\nu(q).                                    \tag{1}
\]

These are not independent new assumptions about an arbitrary measurable
representative. In the source they follow from the ordinary-point canonical
function `G`, its critical harmonicity, the positive population/envelope
inputs stated there, and the retained-path reciprocal bound. The source
defines `h(q)=G(q)/q` and proves

\[
\delta\nu(q)\le h(q)\le\nu(q),\qquad G(q)\ge\gamma>0,
\quad \delta=e^{-200/3},                                    \tag{2}
\]

and, along every retained finite path,

\[
\prod_i\frac{3q_i}{3q_i+1}\ge\delta.                        \tag{3}
\]

Thus positivity and balance in (1) are proved in the current PR, subject
to its displayed population and canonical-envelope inputs. They have not
been independently formalized here. The finite-clock algebra has a Lean
companion in PR183; the measure and operator results used here are written
mathematics.

Fix an escaping component `C`, a ray `q_j=U^j(q_0)`, and its integer clock
`t_C(x)`: if `U^i(x)=q_j`, set `t_C(x)=j-i`. Injectivity of the ray makes
this well defined. PR183 proves

\[
t_C(Ux)=t_C(x)+1,\qquad
C_C:=\lim_{j\to\infty}\nu(q_j)\in(0,A],
\qquad
\sum_{t_C(x)=l}\nu(x)=C_C\quad(l\in\mathbb Z).              \tag{4}
\]

For clarity, the last assertion requires the whole ordinary component,
not only its chosen forward ray. For fixed `l`, the inverse fronts
`{x:U^(r-l)x=q_r}`, with `r>=max(l,0)`, increase to the clock level.
Their masses are `nu(q_r)` by repeated balance. Monotone convergence proves
(4). In particular every level has finite positive mass, whereas the
component has infinite total mass.

## 2. The symmetrized actual transport is recurrent

On `ell^2(C,nu)` define

\[
(Cf)(x)=f(Ux),\qquad
(Pf)(q)=\nu(q)^{-1}\sum_{Ux=q}\nu(x)f(x).
\]

Equation (1) gives `C* = P` and `C*C = I`. Both are Markov on this escaping
component. The reversible Markov operator

\[
S=\frac{C+P}{2}
\]

has conductance `nu(x)/2` across the undirected edge `{x,Ux}`. Its clock
moves up or down by one with equal probabilities. The bounded symmetric
Dirichlet form is

\[
\mathcal E_s(f,f)=\langle(I-S)f,f\rangle_\nu.
\]

For a clock function `f(x)=b(t_C(x))`, (4) gives

\[
\|f\|_\nu^2=C_C\sum_{l\in\mathbb Z}|b(l)|^2,\qquad
\mathcal E_s(f,f)=\frac{C_C}{2}
       \sum_l|b(l+1)-b(l)|^2.                              \tag{5}
\]

Choose `b_N(l)=max(1-|l|/N,0)`. These functions increase pointwise to one,
belong to `ell^2(C,nu)`, and satisfy

\[
\boxed{\mathcal E_s(b_N\circ t_C,b_N\circ t_C)=C_C/N.}      \tag{6}
\]

Indeed exactly `2N` successive differences have squared size `1/N^2`.
The recurrence criterion for symmetric Dirichlet forms therefore proves
recurrence of `S` on the hypothetical escaping component. This argument
does not need local finiteness of the Collatz predecessor graph. The
bounded form has domain all of `ell^2`; finitely supported functions are
a core, even though a whole clock-level indicator need not have finite
physical support.

The relevant published transfer theorem is Beznea--Cimpean--Rockner,
*Irreducible recurrence, ergodicity, and extremality of invariant measures
for resolvents*, SPA 128 (2018), 1405--1437, Theorem 5.1 and Corollary 5.2.
Recurrence of a nonsymmetric Dirichlet form implies recurrence of its
symmetric part; the converse follows under the strong sector condition

\[
|\mathcal E(u,v)|\le K
 \mathcal E(u,u)^{1/2}\mathcal E(v,v)^{1/2}.                 \tag{7}
\]

[Published primary source](https://doi.org/10.1016/j.spa.2017.07.009).
The published theorem was inspected through the publisher's indexed text.
The older [arXiv v2](https://arxiv.org/pdf/1409.6492v2) has different
numbering and only a finite-measure recurrence corollary in its Section 5;
that older corollary is not the justification for the infinite-measure
application here.

## 3. The missing strong-sector hypothesis fails on the actual clock

The directed form is

\[
\mathcal E_C(u,v)=\langle(I-C)u,v\rangle_\nu.
\]

Its quadratic form on real functions equals (5). The skew part cannot be
bounded as in (7). This can be checked on the exact clock-level subspace,
without a surrogate dynamics or guessed spectrum.

For an integer `m>=2`, put

\[
z_m(l)=\begin{cases}e^{il/m},&1\le l\le m^2,\\0,&\text{otherwise}.
\end{cases}
\]

Using `Cz(l)=z(l+1)` and (4),

\[
\frac{\mathcal E_C(z_m\circ t_C,z_m\circ t_C)}{C_C}
 =m^2-(m^2-1)e^{i/m}.                                     \tag{8}
\]

Consequently

\[
\operatorname{Re}\mathcal E_C(z_m,z_m)/C_C\le3/2,\qquad
|\operatorname{Im}\mathcal E_C(z_m,z_m)|/C_C
 \ge\frac{m^2-1}{2m}.                                    \tag{9}
\]

Here and below the clock composition in the argument is suppressed.
The bounds follow from `1-cos t<=t^2/2` and `sin t>=t/2` for
`0<=t<=1`. If the real form satisfied (7), writing `z=u+iv` would give

\[
|\operatorname{Im}\mathcal E_C(z,z)|
 \le 2K\sqrt{\mathcal E_C(u,u)\mathcal E_C(v,v)}
 \le K\operatorname{Re}\mathcal E_C(z,z),
\]

contradicting (9) as `m` increases. The sector ratio is at least
`(m^2-1)/(3m)` on these actual vectors.

There is no paradox: the Poissonized directed chain
`exp(t(C-I))` is conservative on an escaping component because `C1=1`,
yet visits any starting state only during its initial holding interval.
Its expected total occupation of that state is one. Conservativeness
and recurrent symmetrization therefore coexist with directed escape.
The cited theorem does not transfer (6) across the unbounded skew term.

This result is a test of applicability, not a proposed abstract countermodel
and not a new claim that a sector estimate should hold globally.

## 4. Rational affine Poisson boundaries: the exact change of law

Take independent exponents with `P(E=e)=2^(-e)`, `e>=1`. The inverse
affinities are

\[
\phi_e(x)=(2^e x-1)/3.
\]

Brofferio's unnumbered main theorem in *The Poisson boundary of random
rational affinities*, Ann. Inst. Fourier 56 (2006), 499--515, identifies
the boundary of a nonabelian rational affine random walk with finite
adelic first moment as the product of its negatively drifting completions.
[Primary journal PDF, pp.500--501](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf).

All those hypotheses can be checked here. The first moment is finite
because `E[E]=2`. The maps `phi_1` and `phi_2` do not commute. Their
linear-part drifts are

\[
\chi_\infty=2\log2-\log3>0,\quad
\chi_2=-2\log2<0,\quad \chi_3=\log3>0,
\]

with zero drift at the other primes. The i.i.d. inverse affine walk thus
has its contracting boundary in `Q_2`.

This is not the actual ordinary inverse law. For the latter, a retained
edge `U(x)=q` with exponent `e` has probability

\[
K_G(q,x)=\frac3{2^e}\frac{G(x)}{G(q)}.                      \tag{10}
\]

This is exactly PR185's critical inverse law after substituting `h=G/q`.
On a retained inverse word of length `r`, its probability divided by the
i.i.d. word probability is

\[
\boxed{3^rG(x_r)/G(q).}                                   \tag{11}
\]

Moreover, i.i.d. exponents keep a unit integer inverse state integral
for the next step with probability at most `2/3`: the required parity
of `e` has probability `1/3` or `2/3`. Requiring the new state also to
be a unit can only lower it. The probability of legal retention for
`r` steps is therefore at most `(2/3)^r`. Under (10) it is one.
The two infinite path measures are singular on this explicit event.
The bounded comparison of PR185's ordinary and critical inverse laws
does not compare either of them to the unconditioned affine walk.

Thus the group's boundary theorem really applies to the stated i.i.d.
law, but its almost-sure conclusions cannot be substituted for a theorem
about (10). The rare arithmetic conditioning is visible in (11).

## 5. Kesten--Goldie applies exactly to the forward real perpetuity

For the forward affinities

\[
F_e(x)=(3x+1)/2^e=M_ex+Q_e,
\quad M_e=3/2^e,\quad Q_e=1/2^e,
\]

with the same exponent law, the real stationary series is

\[
R=\sum_{j\ge1}\frac{3^{j-1}}{2^{E_1+\cdots+E_j}}.
\]

It is finite almost surely, since `E log M=log3-2log2<0`. It satisfies
`R =d M R' + Q` with `R'` independent of `(M,Q)`. The same series
converges in `Q_3`; Brofferio's theorem now has negatively drifting
completions `R` and `Q_3`, and supplies the joint stationary boundary.

The perpetuity case of Goldie's implicit renewal theorem is Theorem 4.1
of *Implicit Renewal Theory and Tails of Solutions of Random Equations*,
Ann. Appl. Probab. 1 (1991), 126--166,
[DOI 10.1214/aoap/1177005985](https://doi.org/10.1214/aoap/1177005985).
The publisher PDF was not retrievable in this session. The complete
applicable statement and tail-constant formula were directly inspected
in Alsmeyer's author-hosted *Random Recursive Equations and Their
Distributional Fixed Points*, Theorems 4.1 and 4.19, printed pp.104 and
119, and Definition 2.11 for the arithmetic convention:
[author text](https://www.uni-muenster.de/Stochastik/lehre/SS11/StochRekGleichungen/book.pdf).
Alsmeyer's research article also records the renewal theorem in Proposition
4.1: [author-hosted primary preprint](https://www.uni-muenster.de/SFB878/publications/files/phpIyzbmn2357.pdf).

Here all its conditions hold at `kappa=1`:

\[
\begin{aligned}
\mathbb E M^s&=\frac{3^s}{2^{s+1}-1},&\mathbb EM&=1,\\
\mathbb E Q&=1/3,&
\mathbb E(M\log M)&=\log3-\frac43\log2>0.
\end{aligned}                                             \tag{12}
\]

The required positive logarithmic moment is finite since `M<=3/2`.
The law of `log M` is nonarithmetic in the renewal sense: if both
`log3-log2` and `log3-2log2` belonged to `d Z`, then both `log2` and
`log3` would be integer multiples of `d`, contradicting unique prime
factorization. Although the support lies in a translated lattice, it
does not lie in a discrete additive subgroup. No logarithmically periodic
tail correction is therefore required by this theorem.

There is no common fixed point: the fixed points of `F_1` and `F_2` are
`-1` and `1`, respectively. At exponent one, the numerator of Goldie's
constant is simply `E[(MR'+Q)-MR']=EQ`; this subtracts inside the
expectation, so it does not subtract two infinite first moments. Thus

\[
\boxed{\lim_{t\to\infty}t\,\mathbb P(R>t)
       =\frac1{\log(27/16)}.}                             \tag{13}
\]

This instantiation concerns the genuine affine law. It has no population
or ordinary-harmonic-reference premise.

## 6. Applying the sharp tail to an actual escaping prefix

Suppose `q_k=U^k(p)` survives, let `s_k` be its total division count,
and compose the actual affine branches. In outer order they are the
reversal of the chronological list, and give

\[
q_k=A_kp+B_k,\qquad A_k=3^k/2^{s_k},\qquad B_k\ge0.
\]

The branch probability is still `2^(-s_k)`. Equation (3) gives

\[
\frac{A_kp}{q_k}
 =\prod_{i=0}^{k-1}\frac{3q_i}{3q_i+1}\ge\delta.             \tag{14}
\]

Set `b_p=P(R>p)>0`, positive by (13). Stationarity and the event that
the outer prefix is exactly this reversed word give the genuine bound

\[
\mathbb P(R>q_k)\ge2^{-s_k}b_p
 \ge\frac{\delta b_p}{p}\frac{q_k}{3^k}.                   \tag{15}
\]

Combining (13) and (15) yields

\[
q_k^2\le C_p3^k                                             \tag{16}
\]

for large `q_k`, with a fixed constant depending on the original source.
This is the result of the attempted contradiction, not an omitted
estimate. The elementary inequality

\[
q_{k+1}+1\le\tfrac32(q_k+1)
\]

already gives `q_k+1<=(3/2)^k(p+1)`, which is stronger than (16).
The sharp marginal renewal theorem therefore supplies no escape
contradiction through this actual-prefix comparison.

The adelic Jacobian identity is likewise exact: `F_e` scales real Haar
measure by `3/2^e` and ternary Haar measure by `1/3`, so its product
Jacobian equals its branch probability `2^(-e)`. That equality alone
does not assert disjoint images, a self-affine tiling, or absolute
continuity of the stationary joint law.

## 7. Auxiliary: the precise moving-fibre cost

This section has **additional unverified source premises** and is not
needed for Sections 1--6. The October 2026 manuscript *Geometry, integer
fibres, and dyadic equidistribution of the joint Collatz affine law*,
v2, [Section 9.2](https://rstation.ai/problems/collatz/papers/19), states
a canonical Cesaro fibre theorem, using its separately cited trace,
population-floor, and selection results. Those dependencies were not
reaudited or imported as Lean axioms here. Its notation `h` is a critical
density, not the normalized `h=G/q` used in Section 1.

Assume explicitly that its fibre statement applies with the repository's
same `G` and inverse law (10). Write `mu_q` for the real coded-limit law
of (10), and `mu` for the joint stationary law. The stated convergence is

\[
\frac1N\sum_{r=1}^N3^r
 \mu(dR\times(q+3^r\mathbb Z_3))
 \Longrightarrow G(q)\mu_q                                  \tag{17}
\]

for each fixed ordinary root. It gives no uniformity as the root moves.

On an escaping spine from `p`, the probability in `mu_(q_k)` of first
following its exact inverse prefix back to `p` is

\[
A_kG(p)/G(q_k)\ge\delta G(p)/(pA)>0,                        \tag{18}
\]

using (2), (14), and `G(q_k)<=A q_k`. The inverse real series at `p`
is strictly positive on every path, so choose `epsilon,b>0` with
`mu_p((epsilon,infinity))>=b`. On the event in (18), its continuation
has real value at least `A_k epsilon>=delta epsilon q_k/p`.
Thus constants `eta,b_0>0`, depending only on `p`, satisfy

\[
\mu_{q_k}((\eta q_k,\infty))\ge b_0\quad\text{for every }k. \tag{19}
\]

Also `G(q_k)>=delta nu(p)q_k`. If an index `N` is large enough for the
Cesaro measure in (17), tested on this real tail, to contain at least
half the mass guaranteed by (19), then (13) bounds it above by

\[
\frac1N\sum_{r=1}^N3^r\mathbb P(R>\eta q_k)
 \le\frac{C\,3^{N+1}}{2\eta q_k N}.
\]

Its stipulated lower bound is at least
`b_0 delta nu(p) q_k/2`. Therefore necessarily

\[
\boxed{3^N/N\ge c_p q_k^2.}                                \tag{20}
\]

This is a lower bound on the ternary resolution needed for such a
moving-root approximation; it is not a proof that approximation occurs
at a usable resolution. The manuscript's relative endpoint gap is
compatible with (19), and even the known eventually convergent
nonperiodic root `5` has that endpoint gap. Full topological support is
also compatible with a canonical fibre gap at an individual root.

The missing arithmetic addition is a genuinely uniform joint
conditioning or altered-word comparison at ordinary moving roots.
Neither the applicable Poisson-boundary theorem, recurrent symmetrization,
critical Haar Jacobian, nor the fully instantiated renewal tail supplies
that addition. No universal escape or cycle exclusion is claimed by
this packet.

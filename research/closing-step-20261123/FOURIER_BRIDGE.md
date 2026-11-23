# The exact integrability threshold of the random affine model

Date: 2026-11-23. Author: root lane, with the endpoint overlap argument
supplied by the source-collision lane and independently reconstructed below.

**Status: written theorems for the specified iid model; the pointwise
ordinary-source bridge remains OPEN.** This note combines the complete-carry
estimate in [COLLISION_CLOSURE.md](COLLISION_CLOSURE.md) with Tao's published
fine-scale mixing theorem. It determines the full Renyi spectrum of the
geometric-2 ternary law and the exact range of its finite Lebesgue norms:
the density lies in every `L^p`, `1 <= p < 2`, and in none for `p >= 2`.
Its depth-`m` squared density norm lies between `c m` and `C m^4` eventually.
These are properties of one explicitly defined random model, not a proof
of Collatz or a selection theorem for the conditional law at an ordinary
integer. No priority claim is made for these deductions.

The real Fourier attack goes further than a comparison of dimensions:
Bremont's theorem applies to the corresponding average-contracting real
system, and gives decay after conditioning on a growing but sufficiently
shallow ordinary residue cylinder. The exact depth/frequency quantifiers,
and the missing passage to an ordinary point fibre, are retained.

## 1. One probability law and one Haar normalization

Let `G_1,G_2,...` be independent positive geometric variables with

\[
 \mathbb P(G_j=e)=2^{-e},\quad e\ge1,
 \qquad A_j=G_1+\cdots+G_j.
\]

The same rational partial sums define

\[
 R_m=\sum_{j=1}^m3^{j-1}2^{-A_j},\qquad
 Y=\sum_{j\ge1}3^{j-1}2^{-A_j}\in\mathbb Z_3^\times,
 \qquad R=\sum_{j\ge1}3^{j-1}2^{-A_j}\in\mathbb R_{>0}.
 \tag{1}
\]

Ternary convergence is immediate; real convergence follows from the strong
law `A_j/j -> 2 > log_2 3`. Write `rho` for the law of `Y`. Throughout,
`H` is Haar **probability on all of Z_3**, not probability renormalized on
its units. Put

\[
 p_m(r)=\rho(r+3^m\mathbb Z_3),\quad
 F_m(x)=3^m p_m(x\bmod3^m),\quad F_0=1,
 \quad C_q(m)=\sum_{r\bmod3^m}p_m(r)^q.
 \tag{2}
\]

Thus `integral F_m dH=1` and

\[
 \|F_m\|_q^q=3^{m(q-1)}C_q(m).
 \tag{3}
\]

The finite residue distributions are projectively consistent. In the
chronological convention of the companion collision note, reversal of a
length-`m` iid word has the same law. Its endpoint residue therefore has
exactly the law in (2). Reversal is used here only for this iid law;
no general stationary process is declared reversible.

The companion's Theorem 4, proved without a mixing theorem, supplies

\[
 3^{-m}\le C_2(m)\le C m^4 3^{-m},\qquad
 \|F_m\|_2\le C^{1/2}m^2.
 \tag{4}
\]

## 2. Full Renyi spectrum, with all carry labels retained

For `q>1` define the order-`q` residue dimension by the limit, when it
exists,

\[
 D_q=\lim_{m\to\infty}
       \frac{-\log C_q(m)}{(q-1)m\log3}.
\]

**Theorem 1.** For the single law (1),

\[
 \boxed{D_q=
 \begin{cases}
  1,&1<q\le2,\\[2pt]
  \displaystyle\frac{\log(2^q-1)}{(q-1)\log3},&q>2.
 \end{cases}}
 \tag{5}
\]

For `1<q<=2`, Jensen/interpolation on the finite probability vector gives

\[
 3^{-m(q-1)}\le C_q(m)\le C_2(m)^{q-1}
       \le C^{q-1}m^{4(q-1)}3^{-m(q-1)}.
 \tag{6}
\]

For the proof at `q>2`, retain the exact chronological carry labels `(A,K)`
from the companion note. The map from a word to `(A,K,residue)` is
injective. Weighted Holder on each residue, followed by this injection,
gives for any positive penalties `L_{a,k}` with finite displayed sum

\[
 C_q(m)\le
 \left(\sum_{a,k\ge0}L_{a,k}^{-1/(q-1)}\right)^{q-1}
 \sum_w P_m(w)^q L_{A(w),K(w)}.
 \tag{7}
\]

This counts the cross terms between every carry channel. It is first
proved for finite word sets and then passed to increasing finite sets by
monotone convergence. The lower bound is the ungrouped word moment.
Here the exact `q`-tilt is iid:

\[
 Z_{q,m}:=\sum_wP_m(w)^q=(2^q-1)^{-m},\qquad
 \mathbb P_q(G=e)=(2^q-1)2^{-qe},\quad
 \beta_q=\mathbb E_qG=\frac1{1-2^{-q}}.
 \tag{8}
\]

For `a=2^G/3` its moment at `q-1` is

\[
 \mathbb E_q a^{q-1}=\frac{2^q-1}{3^{q-1}}<1.
 \tag{9}
\]

For completeness, the logarithm of the ratio in (9) vanishes at `q=2`.
Its derivative is `2^q log(2)/(2^q-1)-log(3)`, decreasing in `q` and
already negative at two, since `16<27`. Thus the strict inequality holds
for every `q>2`. The moment generating expression is continuous for
exponents below `q`, so there exists `u>q-1` with `E_q a^u<1`.
Minkowski applied to

\[
 C(w)/3^m=\frac13\sum_{i=0}^{m-1}\prod_{j=1}^i(2^{G_j}/3)
\]

proves `sup_m E_q(K+1)^u < infinity`. Choose `t` with `q-1<t<u` and use

\[
 L_{a,k}=
 \left(1+\frac{|a-m\beta_q|}{\sqrt m}\right)^{2(q-1)}
 (k+1)^t.
 \tag{10}
\]

The reciprocal-power sum in (7) is at most
`4 sqrt(m) zeta(t/(q-1))`. All fixed moments of
`(A-m beta_q)/sqrt(m)` are uniformly bounded: expand a sufficiently high
even centered moment, discard singleton-index terms by independence, and
count the remaining terms, which use at most half as many distinct
indices. Holder with exponents `u/(u-t)` and `u/t` now bounds
`E_q L_{A,K}` uniformly in `m`. Equations (7)--(10) give

\[
 \boxed{(2^q-1)^{-m}\le C_q(m)
       \le C(q)m^{(q-1)/2}(2^q-1)^{-m},\qquad q>2.}
 \tag{11}
\]

Taking logarithms proves (5). Constants depend on fixed `q`; the estimates
are not asserted uniform as `q` approaches two from above.

## 3. Tao's uniform mixing supplies every L^p norm below two

The external analytic input is Terence Tao, *Almost all orbits of the
Collatz map attain almost bounded values*, Proposition 1.14, in the
[published primary paper](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F).
For every fixed `A>0`, its bound on `Osc_{m,n}`, uniformly for `1<=m<=n`,
is exactly

\[
 \|F_n-F_m\|_{L^1(H)}\le C_A m^{-A}.
 \tag{12}
\]

Indeed the averaged depth-`n` probability at a residue is
`3^{m-n} p_m(r mod 3^m)`. Multiplying by `3^n` to form densities and
integrating against atoms of Haar mass `3^{-n}` cancels both factors.
There is no extra `3^m` or unit-normalization loss. The random variable
in that proposition is precisely (1) modulo `3^n`.

In particular `F_m` is Cauchy in `L^1(H)`. Its limit `F` is nonnegative,
has integral one, and represents `rho`, since every cylinder integral
stabilizes at the specified probability. Thus

\[
 F_m=\mathbb E_H[F\mid x\bmod3^m].
 \tag{13}
\]

Fix `1<p<2`. Apply interpolation to `D_m=F_{2m}-F_m`. By (4) and (12),

\[
 \|D_m\|_p
 \le\|D_m\|_1^{2/p-1}\|D_m\|_2^{2-2/p}
 \le C_{A,p}m^{-A(2/p-1)+4(1-1/p)}.
 \tag{14}
\]

Choose `A` so that the displayed exponent is negative. Summing over
`m=1,2,4,...` proves convergence of `F_{2^j}` in `L^p`. Its limit is the
same `F` by uniqueness of the `L^1` limit. This proves

\[
                         F\in L^p(H),\quad 1\le p<2.
 \tag{15}
\]

This argument uses the new polynomial `L^2` estimate only for adjacent
dyadic depths. It does not incorrectly demand a uniform `L^2` bound.

## 4. The critical endpoint fails: positive overlaps force L^2 growth

The density transfer operator for this same iid law is explicit. Define

\[
 f_e(x)=\frac{1+3x}{2^e},\qquad
 (T_e h)(y)=3\,2^{-e}
 \mathbf1_{\{y\equiv2^{-e}\pmod3\}}
 h\!\left(\frac{2^e y-1}{3}\right),\qquad
 P h=\sum_{e\ge1}T_e h.
 \tag{16}
\]

Each `f_e` contracts ternary Haar by a factor `1/3`; its real expansion
or contraction plays no role here. Thus `T_e h dH` is the pushforward of
`2^{-e}h dH`, and `P` preserves the integral of a nonnegative function.
Projective consistency or composition of the gap series gives

\[
 P F_m=F_{m+1},\qquad P F=F,\qquad
 \|T_e h\|_2^2=3\,4^{-e}\|h\|_2^2.
 \tag{17}
\]

The equality for `F_0=1` uses independent Haar filling below depth zero;
`f_e` sends each depth-`m` cylinder to a depth-`m+1` cylinder. The passage
to `F` also follows from the `L^1` contraction of `P`.

Suppose `F` were in `L^2`. Tonelli and nonnegativity give

\[
 \|F\|_2^2=
 3\sum_{e\ge1}4^{-e}\|F\|_2^2
 +2\sum_{e<d}\int(T_eF)(T_dF)\,dH
 =\|F\|_2^2+2\sum_{e<d}\int(T_eF)(T_dF)\,dH.
 \tag{18}
\]

All cross products would vanish. But the positivity set `S={F>0}` has
positive Haar measure `s`, and the positivity set of every `T_e F` is
`f_e(S)`, of measure `s/3`. More than `3/s` such sets cannot be pairwise
disjoint in a probability space. Some pair overlaps in positive measure;
its two factors are positive there, so its product integral is positive.
This contradicts (18).

The same argument gives a quantitative lower rate for the approximants.
Put `Q_m=||F_m||_2^2`. These are finite by (4), and

\[
 Q_{m+1}-Q_m=2\sum_{e<d}\int(T_eF_m)(T_dF_m)\,dH.
 \tag{19}
\]

Choose the fixed overlapping pair just obtained, without assuming `F`
square-integrable. Since `T_eF_m -> T_eF` in `L^1` and similarly for
`d`, Fatou along an almost-everywhere convergent subsequence of any
subsequence attaining the lower limit yields

\[
 \liminf_m\int(T_eF_m)(T_dF_m)\,dH
 \ge\int(T_eF)(T_dF)\,dH>0.
 \tag{20}
\]

The right side is permitted to be infinite; a fixed finite positive lower
bound is enough. Consequently `Q_{m+1}-Q_m >= c` eventually, and

\[
 \boxed{c' m\le\|F_m\|_2^2\le C m^4\quad(m\ge m_0).}
 \tag{21}
\]

Combining (15), (18), and the inclusion of `L^q` in `L^2` on a probability
space for `q>2`, we obtain the exact integrability threshold

\[
 \boxed{F\in L^p(H)\quad\Longleftrightarrow\quad1\le p<2,
        \qquad 1\le p\le\infty.}
 \tag{22}
\]

Independently, (11) already forces exponential growth of `||F_m||_q^q`
when `q>2`. The positive-overlap argument supplies the missing endpoint
and does not assert the precise polynomial rate in (21).

## 5. Real Fourier decay from an average-contracting affine theorem

For the broader iid geometric law of mean `b>log_2 3`, the real series
has the same distribution as the stationary random affine system

\[
 x\mapsto x/2\ \text{with probability }1-1/b,
 \qquad x\mapsto(3x+1)/2\ \text{with probability }1/b.
 \tag{23}
\]

Group successive even choices before each odd choice to recover the
geometric gap series. The mean logarithmic multiplier is
`(log 3)/b-log 2<0`. The two maps have different fixed points, zero and
minus one. Their multiplier logarithms are incommensurable: a rational
relation between `log(1/2)` and `log(3/2)` would give a nontrivial equality
between a power of two and a power of three.

Julien Bremont's *Self-similar measures and the Rajchman property*,
[primary arXiv PDF](https://arxiv.org/pdf/1910.03463), Theorem 2.3 in the
November 2020 version, applies to finite positive-slope systems with
negative mean logarithmic multiplier and no common fixed point. Its
non-Rajchman alternative requires all slopes to be integral powers of
one common base, even allowing some expanding maps. The slopes in (23)
exclude that alternative. Therefore the real marginal `nu_R` satisfies

\[
 \widehat\nu_{\mathbb R}(t)\longrightarrow0
                  \quad\text{as }|t|\to\infty.
 \tag{24}
\]

The paper was published in Annales Henri Lebesgue 4 (2021), 973--1004;
[DOI 10.5802/ahl.94](https://doi.org/10.5802/ahl.94).
We cite the read arXiv theorem number to avoid conflating version numbers.
We use no decay rate, absolute continuity, or strict-contraction-only
theorem for this real marginal.

A useful but still averaged consequence is worth making explicit. For
every bounded measurable `g(Y)`, the signed real projection of
`g(Y) dLaw(R,Y)` has a bounded Radon--Nikodym derivative with respect to
`nu_R`. Such a measure is Rajchman whenever `nu_R` is. One proof
approximates its density in `L^1(nu_R)` by continuous functions on a
large compact set, and then by finite linear combinations of real
characters; Fourier transforms of the latter are finite sums of shifted
transforms in (24). Hence

\[
 \mathbb E[g(Y)e^{2\pi itR}]\longrightarrow0.
 \tag{25}
\]

In particular every fixed positive-mass ternary-cylinder-conditioned
real law is Rajchman. An individual point `Y=q` is not such a cylinder.

## 6. Quantitative depth retention for an ordinary residue cylinder

Return to mean two. For a word `w=(e_1,...,e_m)` in the outward inverse
order used in (1), set

\[
 a_w=3^m2^{-A_m},\quad R_w=\sum_{j=1}^m3^{j-1}2^{-A_j},
 \quad \mathcal W_m(q)=\{w:R_w\equiv q\pmod{3^m}\},
 \quad Z_m(q)=\mathbb P(Y\equiv q\pmod{3^m}).
\]

For the normalized conditionals below, restrict to a positive odd ordinary
`q` with `3` not dividing `q`. Roots divisible by three have zero cylinder
mass and are excluded. Every word in `W_m(q)` gives an exact
ordinary inverse chain. Multiplying by `2^{A_i}` shows that every prefix
has an integral endpoint; successive inverse values are positive odd
integers. The final value may be divisible by three; it is not silently
discarded. The exact identity is `q=R_w+a_w n` with that final ordinary
endpoint `n`. Words are retained with their actual model weights `2^-A`.

Conditioned on this finite cylinder, independence of the unused gaps gives
the characteristic function

\[
 \widehat\nu_{q,m}(t)=\frac1{Z_m(q)}
 \sum_{w\in\mathcal W_m(q)}2^{-A_m}
 e^{2\pi itR_w}\widehat\nu_{\mathbb R}(a_wt).
 \tag{26}
\]

This is a model conditional law and is not identified with the canonical
trace boundary of a specified ordinary component. For `0<delta<1`,
`tau>0`, `t!=0`, discard the restriction on words only in the nonnegative
small-frequency remainder. Markov's inequality and
`E 2^{delta G}=1/(2^{1-delta}-1)` prove

\[
 \boxed{
 |\widehat\nu_{q,m}(t)|\le
 \sup_{|u|\ge\tau}|\widehat\nu_{\mathbb R}(u)|
 +\frac1{Z_m(q)}
 \left(\frac{\tau}{3^m|t|}\right)^\delta
 \left(\frac1{2^{1-\delta}-1}\right)^m.}
 \tag{27}
\]

For these unit roots, two exponents in `{1,...,6}` give
positive odd unit parents. Each retained branch weighs at least `2^-6`.
Iterating just these two parents gives the uniform bound `Z_m(q)>=32^-m`.
Thus the error term in (27) is at most

\[
 \left(\frac{32\,3^{-\delta}}{2^{1-\delta}-1}\right)^m
       \left(\frac\tau{|t|}\right)^\delta.
 \tag{28}
\]

Taking `tau=|t|^{1/2}` proves decay uniformly over positive odd unit roots
and integer depths `m=m(t)` whenever `m(t)=o(log |t|)`. A fixed depth is
allowed. This establishes a concrete growing-depth result, but the depth
is restricted relative to the frequency.

## 7. The exact remaining ordinary-source step

The source-qualified actual common-boundary law in PR180 is the real law
`mu` on one ordinary component, obtained from its canonical trace and
whole predecessor path measure. Its scales `chi_j` tend to infinity and
its conditioned laws approach `mu` in total variation; these statements
are frozen in `research/profound-step-20261123/ENTROPY_ARITHMETIC.md` at
`7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`.

If that **actual** `mu` were Rajchman, its dilates under the real embedding
of the compact solenoid `X_6` would tend to Haar. For any nontrivial
character `r in Z[1/6]`, the corresponding coefficient is
`mu_hat(r chi_j)`, which would vanish. Total variation convergence of the
conditioned laws preserves this conclusion. The vanishing also survives
bounded deterministic time weights, including weights chosen from the
actual next-gap labels. This is a precise Fourier input capable of
strengthening the previously obtained tail-density statement.

Neither (22) nor (27) proves that input. The missing assertions are:

1. An identification or quantitatively controlled comparison of the
   **ordinary component's canonical trace boundary** with the finite
   model conditionals in (26), for that fixed ordinary root.
2. An approximation error valid at the frequencies needed for the actual
   scales, with depth small enough for (27) to apply. Weak convergence at
   fixed frequency alone does not permit exchanging depth and frequency
   limits.

The ordinary roots form a countable Haar-null subset of `Z_3`. The exact
`L^p` threshold of an averaged density does not specify those fibres.
Even decay of all bounded weighted real projections in (25) does not imply
pointwise conditional decay: a joint law can encode its entire real
coordinate in its other coordinate, making each conditional real law a
point mass despite an averaged Rajchman real marginal.

Finally, Haar distribution in the compact solenoid is not automatically
Haar distribution of the original integers modulo `3^m`. The integer-floor
carry in that projection remains part of the earlier exact arithmetic
interface. A Fourier conclusion cannot erase it.

The companion [TILTED_MOMENT_OBSTRUCTION.md](TILTED_MOMENT_OBSTRUCTION.md)
also shows why bounded stationary gaps and negative original drift do
not alone provide the collision-weighted moment used above. The random
model is now controlled much more sharply; the still unsupported step
is its pointwise arithmetic connection to one ordinary orbit.

# All correction-word thresholds: uniform pressure and the count-rate limit

**Checkpoint 9; independently reconstructed by a second agent.** This extends the near-maximal
word theorem to every fixed threshold `0<c<1`. It concerns precisely the
valuation-word model in Polson–Sokolov's M4; it does not exclude integer
cycles of the original Collatz map.

## Statements and prior question

Write `theta=log_2 3`, `alpha=theta-1`, and `mu=1/(2 log 2)`. Let `N(c,r)`
and `Z_r(lambda)` have exactly the meanings in the pinned book's M4:
positive valuation words of length `r`, total `ceil(r theta)`, interior
partial totals at most `floor(t theta)`, and reward
`Phi=sum_(t<r) 2^(K_t)/3^t`, at a rung `r`. Set `B_r=sum_(t<r)2^(floor(t theta))/3^t`.
The definitions and the two missing limit steps are in the
[exact primary source, M4 and R8–R9](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex),
tag `v1.4.0`, November 10, 2026.

**Theorem.** The untruncated pressure exists for every real `lambda`,
uniformly over every starting rotation phase. In particular the book's
`r^(-1) log Z_r(lambda)` converges at phase zero along the rungs for every
`lambda>=0`. Denote the pressure by `P(lambda)`. For every `0<c<1`,
\[
 \boxed{\quad
 \rho(c)=\lim_{\substack{r\to\infty\\r\ {\rm rung}}}
             \frac1r\log_{10}N(c,r)
  =\frac1{\log10}\inf_{\lambda\ge0}
             \bigl(P(\lambda)-\lambda c\mu\bigr).\quad}             \tag{1}
\]
The same formula holds along all lengths in the pinned model below,
and for every phase, uniformly. The rate is continuous and concave as
a function of the reward threshold in the interior. Also
\[
 P(0)=\theta\log\theta-(\theta-1)\log(\theta-1).                    \tag{2}
\]
This establishes M4's count-rate limit and the convergence part of R8
on its full tilt range. This proof does **not** assume differentiability of `P` at every tilt.
The companion [differentiability theorem](DEPTH_PRESSURE_DIFFERENTIABILITY.md)
now establishes that remaining part of R8, including at the transition. Possible pressure corners are handled by concatenating
two families of pinned words. The separate near-one theorem establishes
analyticity at large positive tilt and its sharp R9 expansion.

## 1. Pinning the endpoint without changing the words

For `0<=v<1` put
\[
 b_t(v)=\lfloor v+t\theta\rfloor,\qquad
 v_t=\{v+t\theta\},\qquad a_t(v)=2^{-v_t}.
\]
A pinned word of length `n` is a strictly increasing integer cumulative
sequence
\[
 K_0=0,\qquad K_n=b_n(v),\qquad K_t\le b_t(v)\quad(0\le t\le n).
                                                                    \tag{3}
\]
Its positive letters are `K_(t+1)-K_t`. Its reward and partition function are
\[
 \Phi_v(K)=\sum_{t=0}^{n-1}\frac{2^{K_t-v}}{3^t},\qquad
 Z_n(\lambda,v)=\sum_K e^{\lambda\Phi_v(K)}.                         \tag{4}
\]
The depth is `j_t=b_t(v)-K_t`, so `j_0=j_n=0` and
`Phi_v=sum a_t(v)2^(-j_t)`. Every interior depth path has a unique positive
final letter `g_(n-1)+j_(n-1)`, where `g_t=b_(t+1)-b_t` is one or two.
At phase zero, the book's final letter is this letter plus one, since
`ceil(n theta)=floor(n theta)+1`. The final letter contributes no term to
(4). Increasing it by one therefore gives a reward-preserving bijection
between this pinned family and the book's words at every rung. This is not
an extra terminal restriction on its interior paths.

Concatenate a pinned length-`n` word at phase `v` and a pinned length-`m`
word at phase `v_n`. Since
`b_(n+s)(v)=b_n(v)+b_s(v_n)`, their concatenation is a legal pinned word.
The rewards add exactly, including the new segment's initial zero-depth
site. Distinct pairs give distinct words. Hence
\[
 Z_{n+m}(\lambda,v)\ge
          Z_n(\lambda,v) Z_m(\lambda,v_n)                         \tag{5}
\]
for every real tilt. This pinning is what makes the scalar ergodic theorem
applicable without an infinite-matrix norm assertion.

## 2. The phase-clamping comparison

Take `0<=v<w<1`, set `delta=w-v`, and define
\[
 D_t=b_t(w)-b_t(v)\in\{0,1\},\qquad
 Q_n(v,w)=\#\{1\le t<n:D_t=1\}.
\]
Map an upper-phase word to the lower phase by the pointwise minimum
\[
                       K'_t=\min(K_t,b_t(v)).                     \tag{6}
\]
The minimum of two strictly increasing integer sequences is strictly
increasing: if each sequence grows by at least one, so does its minimum.
Thus (6) preserves every positive letter, pins the correct endpoints,
and satisfies the lower ceiling. No condition about consecutive changes
or isolated phase crossings is needed.

The map can change a coordinate only at `D_t=1`, and only from
`b_t(w)=b_t(v)+1` to `b_t(v)`. Given an image, each such interior coordinate
has at most two choices; the endpoints are fixed. Therefore every fibre
of (6) has at most `2^(Q_n)` elements. The reward identity is exact:
\[
 \Phi_w(K)=2^{-\delta}\Phi_v(K')+
        \frac12\sum_{\substack{t<n\\K_t\ne K'_t}}a_t(w).
                                                                    \tag{7}
\]
The last sum lies between zero and `Q_n/2`.

Conversely, retain every interior coordinate of a lower-phase word and
increase only its last coordinate by `D_n`. This is an injection into the
upper-phase family, changes no rewarded coordinate, and scales its reward
by `2^(-delta)`. Consequently, for `lambda>=0`,
\[
 Z_n(\lambda2^{-\delta},v)\le Z_n(\lambda,w)
 \le 2^{Q_n}e^{\lambda Q_n/2} Z_n(\lambda2^{-\delta},v).           \tag{8}
\]
For negative tilt the same bounds hold with the exponential factor in
the upper bound omitted. In particular every real tilt admits the weaker
common upper factor `exp((log 2+|lambda|/2)Q_n)`.

Each word has `0<Phi_v<=n`, so `log Z_n` is `n`-Lipschitz in its real
tilt. With `F_n(lambda,v)=n^(-1) log Z_n(lambda,v)`, (8) gives
\[
 |F_n(\lambda,w)-F_n(\lambda,v)|
 \le |\lambda|(1-2^{-\delta})
       +(\log2+|\lambda|/2)\frac{Q_n(v,w)}n.                     \tag{9}
\]
This finite comparison is the key new ingredient.

## 3. From almost every phase to every phase, uniformly

For each fixed positive `eta<1`, every phase interval in (9) with
`delta<=eta` satisfies
\[
 Q_n(v,w)\le\#\{1\le t<n:\{v+t\theta\}\in[1-\eta,1)\}.
\]
Uniform equidistribution of irrational rotations gives an upper bound
`(eta+o(1))n`, with the error uniform in `v`. Hence
\[
 \limsup_{n\to\infty}\sup_{|v-w|\le\eta}
 |F_n(\lambda,v)-F_n(\lambda,w)|
 \le\bigl(|\lambda|\log2+\log2+|\lambda|/2\bigr)\eta.            \tag{10}
\]
The endpoint values use one-sided neighbors in `[0,1)`; no unproved
continuity across the phase seam is required.

The functions `-log Z_n(lambda,v)` form a subadditive cocycle by (5) over
the irrational rotation. They are measurable and bounded in absolute
value by a constant times `n`: the zero-depth word exists, `|lambda Phi|<=|lambda|n`,
and the total number is at most the number of compositions of
`b_n(v)<=2n`, hence at most `2^(2n)`. Kingman's subadditive ergodic theorem
therefore gives, for almost every `v`, a common deterministic finite limit
`P(lambda)` of `F_n(lambda,v)`. Its use here is the standard scalar theorem,
with all integrability and lower-bound hypotheses just checked; see
[Kingman, *Subadditive Ergodic Theory*](https://doi.org/10.1214/aop/1176996798).

For completeness, choose a finite `eta`-net made of good phases from that
full-measure set. At all of those phases convergence holds simultaneously.
Equation (10) then controls every intervening phase; first let `n` grow,
then `eta` shrink. This proves
\[
                    \sup_{0\le v<1}|F_n(\lambda,v)-P(\lambda)|
                         \longrightarrow0                       \tag{11}
\]
for every real `lambda`. A finite tilt net and the same Lipschitz bound
also make convergence uniform on every compact real tilt interval.

The pressure is finite, convex and nondecreasing, as each finite
logarithmic partition function has these properties. Since the maximal
reward is `B_n(v)=sum_(t<n)a_t(v)` and `B_n(v)/n -> mu` uniformly,
all pressure slopes lie in `[0,mu]`.

## 4. The unweighted entropy and the large-tilt endpoint

At phase zero let `M=floor(n theta)`. There are
`binom(M-1,n-1)` positive compositions of `M` into `n` parts. Every cyclic
orbit of compositions contains a word whose cumulative sums lie below
the line `tM/n`: rotate immediately after a maximum of the partial
excesses `K_t-tM/n`. That rotated word satisfies
`K_t<=tM/n<=t theta`, and thus the integer ceiling in (3).
A cyclic orbit has at most `n` elements. Consequently
\[
 \frac1n\binom{M-1}{n-1}\le Z_n(0,0)
                      \le\binom{M-1}{n-1}.                       \tag{12}
\]
Stirling's formula proves (2); (11) gives the same limit at every phase.
Write its value as `H`. For `lambda>=0`, the total count and the maximal
word give
\[
        \max\{H,\lambda\mu\}\le P(\lambda)\le H+\lambda\mu.
                                                                    \tag{13}
\]
In particular the pressure's limiting slope at infinity is `mu`.
The separately proved near-one theorem gives the sharper
`P(lambda)-lambda mu -> 0` and large-tilt analyticity. Neither the exact
small-tilt behavior nor full differentiability is needed below.

## 5. Uniform concentration at a differentiability point

Fix a real tilt `lambda>0` at which `P` is differentiable, and put
`m=P'(lambda)`. Give finite pinned words their Gibbs probabilities
`exp(lambda Phi)/Z_n(lambda,v)`. Uniformly over `v`, the normalized
logarithmic moment-generating function of their reward is
\[
 \frac1n\log \mathbb E_{\lambda,n,v}e^{h\Phi}
       \longrightarrow P(\lambda+h)-P(\lambda)                  \tag{14}
\]
for each sufficiently small real `h`. Differentiability and exponential
Markov bounds with both signs of `h` give, for every `eta>0`,
\[
 \Pr_{\lambda,n,v}(|\Phi/n-m|>\eta)\le e^{-c n}                 \tag{15}
\]
for all sufficiently large `n`, uniformly in `v`, with some `c>0`.
If the event is vacuous on one side its bound is automatic.

The number of words in this reward band is at least
\[
 Z_n(\lambda,v)e^{-\lambda(m+\eta)n}(1-e^{-c n}).                \tag{16}
\]
Thus it has lower exponential rate `P(lambda)-lambda m` as `eta` shrinks,
uniformly over its initial phase. This supplies genuine counted families,
not independent-block heuristics.

## 6. Matching the upper-tail count even at a pressure corner

Let `A_n(t,v)` count pinned words with `Phi>=nt`, for `0<t<mu`, and put
\[
                       F(t)=\inf_{\lambda\ge0}
                                  [P(\lambda)-\lambda t].         \tag{17}
\]
Markov's inequality and (11) give the upper exponential rate `F(t)`
uniformly in phase. The infimum is attained: (13) forces its objective to
infinity as `lambda` tends to infinity. Moreover `0<=F(t)<=H`, and `F`
is concave and therefore continuous on this open interval.

We give the lower bound without supposing `P` differentiable everywhere.
Choose `t'` strictly between `t` and `mu`, to be sent down to `t` later,
and a minimizer `lambda_*` in (17) for `t'`.

If `lambda_*=0`, then `t'<=P'_+(0)`. At differentiability points
`lambda_j` decreasing to zero, the means tend to `P'_+(0)` and the
entropies `P(lambda_j)-lambda_j P'(lambda_j)` tend to `H=F(t')`.
They eventually have means strictly above `t`, so (16) supplies the
required lower count.

If `lambda_*>0`, convexity gives
\[
                P'_-(\lambda_*)\le t'\le P'_+(\lambda_*).
\]
Choose differentiability points approaching `lambda_*` from the left
and right. Their means tend to these two endpoints, and their entropies
tend to `P(lambda_*)-lambda_* m`, with `m` the corresponding mean. If the two
means agree, this is one family with limiting mean `t'`. Otherwise take
a convex combination whose limiting mean is `t'`.

For fixed sufficiently close choices, use two word lengths in these
proportions, with integer rounding. Count the first family at phase `v`
and the second at the phase reached after that first length. Uniformity
of (16) makes this second, length-dependent phase harmless. Concatenation
(5) is injective and adds rewards exactly. Its word count is the product
of the two counts. The mean can be kept above `t`, and its lower entropy
can be made arbitrarily close to
\[
 P(\lambda_*)-\lambda_*t'=F(t').
\]
Zero proportions mean simply omitting that family. Let the band widths
shrink, the slopes approach their endpoints, and finally `t'` decrease
to `t`. Continuity of `F` gives
\[
       \frac1n\log A_n(t,v)\longrightarrow F(t),                 \tag{18}
\]
uniformly over `v`. The same conclusion holds for thresholds `t_n->t`
by a two-sided squeeze with fixed nearby thresholds.

At phase zero and a rung `r`, the book's threshold is `c B_r`, whose
ratio to `r` tends to `c mu`. The endpoint bijection of §1 and (18)
therefore prove (1). One may also use `c B_n(v)` at every phase and all
lengths, because that normalized threshold converges uniformly to `c mu`.

## What this changes

The book identified phase-zero convergence and a matching lower count as
two missing steps for the M4 rate formula. The minimum-of-cumulatives map
settles the first, while uniform tilted families and their pinned
concatenations settle the second even if the pressure has a corner.
The proposed rate formula is now a theorem for this exact word model.

This does not bound the complete denominator of an individual word.
Exponential word counts can still contain integer-cycle exceptions.
Differentiability at every nonnegative tilt is proved in the
[companion argument](DEPTH_PRESSURE_DIFFERENTIABILITY.md); the count-rate
proof above remains valid independently of that extra conclusion. The near-one R9 expansion and its large-tilt
analyticity are proved separately.

## Exact and formal controls

Root and an independent agent reconstructed the endpoint bijection,
pointwise-minimum clamp, multiplicity and reward bounds, scalar Kingman
hypotheses, uniform phase upgrade, cyclic composition count and the
pressure-corner concatenation. The finite proof was simplified during
review: the clamp works for all two phases in the unit interval, without
an isolated-crossing assumption.

[The exact checker](check_phase_clamping.py) tests 60 phase/length cases,
132,633 upper-phase words, 113,300 changed coordinates, 66,611 image
fibres and lower-family injections, 14,122 pinned concatenations and
43,748 cyclic composition rotations. All rewards are rational and all
multiplicities are exact. Both normal and optimized Python pass.

[PhaseClamping.lean](PhaseClamping.lean) proves ten finite kernels,
including strict increase of the pointwise minimum, endpoint and ceiling
preservation, recovery from the clamp bit, and rational reward and sum
bounds. It does not formalize Kingman's theorem, irrational equidistribution,
exponential concentration or the infinite count-rate limit.

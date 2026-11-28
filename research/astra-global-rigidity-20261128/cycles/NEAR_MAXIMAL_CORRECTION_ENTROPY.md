# Near-maximal correction words: a pressure limit and its sharp rate

**Checkpoint 8; independently reconstructed in this pass.** This concerns a
precisely defined family of valuation words. It does not exclude all integer cycles
or prove convergence of the Collatz map.

## The question and the result

Put `theta = log_2 3`, `alpha = theta-1`, and
\[
 b_t=\lfloor t\theta\rfloor,\quad a_t=2^{b_t}/3^t,
 \quad B_r=\sum_{t=0}^{r-1}a_t,\qquad
 \mu=\int_0^1 2^{-v}\,dv=\frac1{2\log2}.
\]
A rung is a positive integer `r` for which
`ceil(r theta)-r theta` is smaller than its values at all earlier positive
integers. At such a rung, consider positive integer valuation words
`(k_0,...,k_(r-1))` with total `ceil(r theta)` and partial totals
`K_t = sum_(i<t) k_i <= b_t` for `1 <= t < r`. Define
\[
 \Phi(w)=\sum_{t<r}\frac{2^{K_t}}{3^t},\qquad
 N(c,r)=\#\{w:\Phi(w)\ge cB_r\}.
\]
These are the words and count in Polson--Sokolov, *On the Collatz
Conjecture*, edition 1, Problem M4 and Problems R8--R9. Their depth
recursion is the starting point, and their suggested order for the rate is
explicit prior work. We use the source at tag `v1.4.0`, commit
`5840497a23fc0d64127b850aea68862d7c93f2b7`, labels
`rrt:sec:m4`, `rrt:prop:chernoff`, `rrt:prob:r8`, `rrt:prob:r9`.
[Exact primary source](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex)

**Theorem.** For some `c_* < 1`, the limit
\[
 \rho(c)=\lim_{\substack{r\to\infty\\r\ \mathrm{rung}}}
                  \frac1r\log_{10}N(c,r)
\]
exists for every `c_* < c < 1`. As `epsilon` decreases to zero,
\[
 \boxed{\quad
 \rho(1-\epsilon)=\frac{3\epsilon}{2\log2\log10}
 \left[\log\frac1\epsilon-\log\log\frac1\epsilon
              +1-\log\frac32+o(1)\right].\quad}                 \tag{1}
\]
In particular the leading constant, the negative double-logarithmic
correction and the next constant are determined. The tilted word pressure
also exists and is real analytic for every sufficiently large positive
tilt, uniformly over the initial rotation phase. This answers the
near-one question R9 and the large-tilt portion of R8. The full range is now established separately in the
[all-threshold count theorem](FULL_CORRECTION_WORD_ENTROPY.md) and the
[all-tilt differentiability proof](DEPTH_PRESSURE_DIFFERENTIABILITY.md).
The near-one derivation here remains independent of those extensions.

## 1. The exact depth model

For `0 <= t < r` put `j_t=b_t-K_t`. Then `j_0=0`, and with
`g_t=b_(t+1)-b_t` the interior constraints are exactly
\[
             0\le j_{t+1}\le j_t+g_t-1,\qquad g_t\in\{1,2\}.     \tag{2}
\]
Conversely every such interior path determines one word: its interior
letters are `k_t=g_t+j_t-j_(t+1) >= 1`, and the final letter is
`k_(r-1)=g_(r-1)+1+j_(r-1) >= 1`. Thus there is no omitted endpoint
constraint and no multiplicity. Its deficit is
\[
             D(w)=B_r-\Phi(w)
                 =\sum_{t<r}a_t(1-2^{-j_t}).                       \tag{3}
\]
For arbitrary initial phase `v`, the same finite model has
`v_t={v+t alpha}`, `a_t=2^(-v_t)` and
`g_t=1+floor(v_t+alpha)`. At phase zero it is precisely (2).
The phase-zero model is defined at all lengths; at the rungs it gives
the specified count without modification.

Every positive depth costs at least `1/4` in (3), because `a_t >= 1/2`.
A maximal positive block starts after a zero. Its first depth must be one
and the preceding `g` must be two. Therefore its first phase belongs to
`[0,alpha)`, and its first-site cost is at least
\[
                   \tfrac12 2^{-\alpha}=\tfrac13.                 \tag{4}
\]
A block of length `l` consequently costs at least
`1/3+(l-1)/4`. This extra entry cost is responsible for the factor three
in (1). Treating every positive site as an independent cost-`1/4`
choice would give the wrong leading constant.

The number of possible shapes of a length-`l` positive block is at most
`4^(l-1)`, uniformly in its phase. To see this, write its heights as
`h_1=1,h_2,...,h_l >= 1`, where `h_(i+1) <= h_i+1`. The `l`
nonnegative integers
`1+h_i-h_(i+1)` for `i<l`, followed by `h_l-1`, sum to `l-1` and
determine the heights. Their number is at most
`binom(2l-2,l-1) <= 4^(l-1)`. Restricting to the actual `g` pattern
can only reduce it.

## 2. An untruncated renewal equation

For a block occupying sites `t,...,t+l-1`, let `w_(t,l)(lambda)` be
the sum of `exp(-lambda D_block)` over its legal positive shapes,
and set it to zero if its start is ineligible. Ending the block by a zero
is always a legal transition. For real `lambda >= 0`,
\[
 0\le w_{t,l}(\lambda)
       \le e^{-\lambda/3}(4e^{-\lambda/4})^{l-1}.                 \tag{5}
\]
The same absolute bound holds at complex tilt with `lambda` replaced
by its real part. Each activity is a finite sum of entire functions of
the tilt, and is a bounded piecewise continuous function of the phase.

Let `Z_n^D(lambda,v)` sum `exp(-lambda D)` over the depth paths on
sites `1,...,n` with site zero fixed at depth zero. Set `Z_0^D=Z_(-1)^D=1`.
Splitting according to the last maximal positive block gives exactly
\[
 Z_n^D=Z_{n-1}^D+
          \sum_{l=1}^n w_{n-l+1,l}Z_{n-l-1}^D.                   \tag{6}
\]
The site immediately before a block is the separating zero. The last
block may end at `n`; appending a zero imposes no further restriction.
Consequently (6) includes all depths and all words, with no truncation.

Write `R_n=Z_n^D/Z_(n-1)^D`, `u_n=log R_n`, and set `u_0=0`.
If `W_l(v_n)` denotes the length-`l` activity ending at `n`, then
\[
 u_n=\log\left(1+\sum_{l=1}^n W_l(v_n)
                \exp\left[-\sum_{j=1}^l u_{n-j}\right]\right).
                                                                    \tag{7}
\]
This scalar equation is used in place of a finite-dimensional positivity
claim about the infinite-depth transfer matrices.

## 3. Uniform pressure and analytic dependence

On the Banach space of bounded complex functions on the circle, consider
\[
 (\mathcal H_\lambda u)(v)=
 \log\left(1+\sum_{l\ge1}W_l(v)
           \exp\left[-\sum_{j=1}^l u(v-j\alpha)\right]\right),     \tag{8}
\]
with the logarithm on its branch near one. For example, on the ball
`||u||_infinity <= 1/10` and `Re lambda >= 64`, (5) bounds the
absolute sum inside the logarithm, after its initial one, by
\[
 \frac{e^{1/10}e^{-\operatorname{Re}\lambda/3}}
          {1-4e^{1/10-\operatorname{Re}\lambda/4}}.
\]
It is less than `2^(-19)`. The Lipschitz constant is bounded by twice
the same sum with an additional factor `l`, and is less than `1/4`.
These loose inequalities follow already from `e>2` and `e^(1/10)<2`.
Thus (8) has a unique fixed point `u_lambda`, obtained by uniform
iteration from zero. The iteration is holomorphic in the tilt on the
open half-plane, uniformly on compact subsets; its limit and its circle
integral are holomorphic there as well.

For completeness, the finite initialization in (7) has a uniformly
summable effect. The Lipschitz coefficients of its delayed arguments
are bounded by constants times
`e^(-Re lambda/3)(4e^(1/10-Re lambda/4))^(l-1)`.
More explicitly, put
`b_l=exp(1/10) exp(-Re lambda/3) (4 exp(1/10-Re lambda/4))^(l-1)`.
The coefficient of delay `j` is at most `c_j=2 sum_(l>=j) b_l`.
Consequently `sum_(j>=1) 2^j c_j <= 4 sum_(l>=1) 2^l b_l < 1/4`
throughout the stated half-plane. The omitted activity tail of lengths greater than `n` decays
faster than `2^(-n)`. Comparing (7) to (8) by induction, and enlarging
the constant to cover `u_0`, gives
\[
             |u_n-u_\lambda(v_n)|\le C2^{-n}.                     \tag{9}
\]
All constants can be chosen uniformly on a smaller closed complex
half-plane. This also supplies a consistent nonvanishing continuation
of the finite partition functions near every real tilt in this range.

Each finite fixed-point iterate in (8) is Riemann integrable in phase:
truncate the activity sum first, use its finitely many phase breaks,
then take a uniform limit. The full fixed point is Riemann integrable
by the same uniform-limit argument. Irrational rotation averages of a
bounded Riemann integrable function converge to its integral, uniformly
over the initial phase. This follows by sandwiching with step functions
and using uniform equidistribution of intervals. Summing (9) yields
\[
 \frac1n\log Z_n^D(\lambda,v)\longrightarrow
       P_D(\lambda):=\int_0^1u_\lambda(v)\,dv                       \tag{10}
\]
for every real `lambda >= 64`, uniformly over `v`. No assertion only
for almost every phase is substituted for the actual phase zero.

At a rung the original reward partition function is exactly
`Z_r(lambda)=exp(lambda B_r) Z_(r-1)^D(lambda,0)`.
Since `B_r/r -> mu`, its pressure in this range is
\[
                         P(\lambda)=\lambda\mu+P_D(\lambda).     \tag{11}
\]

## 4. The isolated-block asymptotic

The singleton activity at phase `v` is
\[
 W_1(v)=\mathbf1_{[0,\alpha)}(v)\,
                    \exp[-\lambda 2^{-v}/2].                     \tag{12}
\]
In (8), the total of longer blocks is `O(exp(-7 Re lambda/12))`,
while interactions involving two singleton activities and the quadratic
logarithm error are `O(exp(-2 Re lambda/3))`. Also
`||u_lambda||_infinity=O(exp(-Re lambda/3))`.
It follows uniformly in the phase that
\[
 u_\lambda(v)=W_1(v)+O(e^{-7\operatorname{Re}\lambda/12}).
\]
Integration gives, as the real tilt tends to infinity,
\[
 \begin{split}
 P_D(\lambda)&=I(\lambda)+O(e^{-7\lambda/12}),\\
 I(\lambda)&=\int_0^\alpha e^{-\lambda2^{-v}/2}\,dv
       =\frac1{\log2}\int_{1/3}^{1/2}\frac{e^{-\lambda z}}z\,dz.
 \end{split}                                                       \tag{13}
\]
The same error bound holds for the first two tilt derivatives, by
Cauchy's estimate on a fixed-radius complex disk. In particular
\[
 \begin{split}
 I(\lambda)&=\frac{3e^{-\lambda/3}}{\lambda\log2}
                              (1+O(1/\lambda)),\\
 -I'(\lambda)&=\frac{e^{-\lambda/3}-e^{-\lambda/2}}
                            {\lambda\log2},\\
 I''(\lambda)&\sim\frac{e^{-\lambda/3}}{3\lambda\log2}.
 \end{split}                                                       \tag{14}
\]
Hence, for some finite `lambda_1`, `P_D''(lambda)>0` and
`d(lambda)=-P_D'(lambda)>0` for every `lambda>=lambda_1`, and
`d(lambda)` decreases continuously to zero. These are statements about
the untruncated pressure (10).

## 5. Matching lower counts

Let `A_n(d)` count the depth paths of length `n` with deficit at most
`dn`, with any fixed initial phase. Markov's inequality gives
\[
 \limsup_{n\to\infty}\frac1n\log A_n(d)
                  \le P_D(\lambda)+\lambda d.                    \tag{15}
\]
For `d=d(lambda)` with `lambda>lambda_1`, give the finite paths
probability proportional to `exp(-lambda D)`. Their normalized
logarithmic moment generating function for `D` tends to
`P_D(lambda-h)-P_D(lambda)` for small real `h`, by (10).
Differentiability implies concentration of `D/n` at `d(lambda)`:
apply exponential Markov bounds with sufficiently small positive and
negative `h` to each fixed deviation. Both error probabilities decay
exponentially. This is a direct argument, requiring no independent
block assumption.

Choose `d'<d` of the form `d(lambda')`. With probability tending to
one, the tilted paths lie in `[(d'-eta)n,(d'+eta)n]` for any fixed
`eta>0`. If `d'+eta<d`, these paths are counted in `A_n(d)` and their
number is at least
\[
       Z_n^D(\lambda')\,e^{\lambda'(d'-\eta)n}(1-o(1)).
\]
First let `n` tend to infinity, then `eta` decrease to zero, and then
`d'` increase to `d`. Strict convexity and continuity give
\[
 \lim_{n\to\infty}\frac1n\log A_n(d)
       =P_D(\lambda(d))+\lambda(d)d                              \tag{16}
\]
for every sufficiently small positive `d`, where `d=-P_D'(lambda(d))`.
The same argument permits a threshold `d_n -> d`.
Applying it to `n=r-1` and threshold `epsilon B_r`, whose ratio to
`n` tends to `epsilon mu`, proves existence of `rho(1-epsilon)`
and the exact large-tilt Legendre formula in the stated near-one range.

## 6. Inverting the saddle relation

Let `d=mu epsilon`. By (13)--(14),
\[
 d=\frac{e^{-\lambda/3}}{\lambda\log2}(1+o(1)),\qquad
 P_D(\lambda)=3d(1+o(1)).
\]
The relative error in the first relation is exponentially small, so
taking logarithms and substituting once gives
\[
 \lambda=3\left[\log\frac1d-\log\log\frac1d
                         -\log(3\log2)+o(1)\right].              \tag{17}
\]
Inserting (17) into (16), dividing by `log 10`, and using
`3 mu log 2=3/2` proves (1). Equivalently the leading saddle is
`lambda/3 = W(1/(3d log 2))+o(1)`, with `W` the positive Lambert
function, but no properties of that named function are needed.

## Scope

The combinatorial depth model, the choice of the observable and the
suggested leading order belong to the cited book. The proof above adds
an infinite-depth pressure argument in the large-tilt regime, matches
the lower count there, and computes the sharper expansion (1). It
uses ordinary irrational-rotation equidistribution and a uniformly
contractive scalar renewal equation; it does not use an unverified
Collatz density, mixing, or logarithmic-form premise.

The count includes rational cycle words as well as any integer words
meeting these constraints. Even an exponentially small proportion of
all words can contain a denominator-one exception. No averaging of
complete denominators, and no exclusion of such exceptions, is claimed.

## Verification and formal boundary

An independent agent reconstructed the proof against the pinned primary
source, including the final letter, separating-zero indices, complex
contraction, summable initialization error, phase-zero convergence,
Cauchy derivative bounds and the moving-threshold count squeeze. Root
reconstructed the same steps. This is internal mathematical review, not
external peer review or a formalization of the analytic theorem.

[The exact finite checker](check_near_maximal_entropy.py) independently
enumerates positive valuation words and constructs the block-renewal deficit
polynomial. It compares every rational deficit and its integer multiplicity,
without floating bins, at four initial phase weights and lengths 1 through
13: 52 cases, 97,914 words and 177,192 positive blocks. It also verifies the
entry and total block costs in those cases. These are finite controls, not
the argument establishing the infinite limits.

[DepthDeficits.lean](DepthDeficits.lean) proves six finite rational/natural
lemmas: zero loss, the half-power bound, the cost of a positive site, the
forced depth-one entrance, its stronger one-third cost, and the aggregate
block cost. It does not formalize the renewal pressure, equidistribution,
complex-analytic argument, count-rate limit or expansion (1).

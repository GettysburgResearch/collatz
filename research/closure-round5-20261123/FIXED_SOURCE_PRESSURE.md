# Actual entropy forces height growth on the same ordinary orbit

Date: 23 November 2026. Parent: `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Status: written finite and stationary-limit theorems, with a finite
ordinary arithmetic core in `FixedSourcePressure.lean`. Full Collatz
and the same-law ternary collision upper remain OPEN.**

This attack asks whether the newly proved critical renewal and
nonatomicity statements force enough entropy to invoke measure rigidity.
They do not by themselves: an explicit critical ergodic gap law has a
nonatomic ternary factor of dimension zero. The positive result instead
uses the original integer source. Polynomial prefix heights force
positive entropy in **every stationary parity limit along the same
subsequence**, with the sharp elementary tradeoff

\[
 \boxed{\quad
 \liminf_i\frac{\log H_{N_i}}{\log N_i}
 \ge \frac{\log2}{h(\lambda)}.
 \quad}                                                     \tag{1}
\]

Here `H_N` is the actual maximum height through shortcut clock `N`,
`lambda` is the stationary limit of the actual overlapping parity-block
laws, and entropy is in nats per shortcut bit. If `h(lambda)=0`, the
conclusion means that the displayed height ratio tends to infinity.
No convergence rate for the stationary limit is required. The growing
block size enters through an exact finite inequality before the limit.

The classical parity-prefix congruence and block entropy mechanism are
not claimed as historically new. The purpose is an explicit source-
preserving consumer for the current stationary-law attack, including
its finite normalization and its remaining arithmetic boundary.

## 1. Current inputs and literature scope

The following files were read at their full source identities.

| Source | Pin and inspected claim |
|---|---|
| PR180, `research/whole-source-20261123/COLLISION_CORE.md` | Head `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`, blob `d94a3c4153c7d02802f50bd3a1136c71f6936dca`: actual stationary backward-gap lift, strict collision-exponent gap, finite block averaging and its limit order. |
| PR180, `research/whole-source-20261123/BOUNDARY_DESCENT.md` | Same head, blob `34b437972096ae409568842e655509a8233a8087`: minimum-source flux and the source-height cost of occupation transfer. |
| PR180, `research/profound-step-20261123/STATIONARY_REAL.md` | Same head, blob `2dacbd99dc90ca4b7dc324a59c492f42eb963a1e`: exact logarithmic renewal, conditional critical divergence, rational-cycle atom classification, and the moving-height residual. |
| PR180, `research/profound-step-20261123/ENTROPY_ARITHMETIC.md` | Same head, blob `4530ed36c4f3ff6c9cf21149989e97cb94eb1714`: actual unthickened fibre density and fixed-modulus scale-clock independence in the critical iid branch. |
| PR178, `research/central-step-20261123/stationary/FAST_EQUIVALENT_FLOW.md` | Head `c91b80a3156e640ad471cf30c47721145ae21eb1`, blob `39ccf195e42ee17121ff856c45541e70e05d393f`: an explicit equivalent flow with `O(1/N)` total-variation error and uniform relative collision comparison. It preserves the original root's inverse law but does not supply the missing residue upper. |
| PR182, `research/whole-repo-round3-20261123/{ACTUAL_COLLISION,GLOBAL_ORBIT_COUNT}.md` | Retained at the parent: complete source/carry boxes and the elementary all-visit count. Their original scopes remain unchanged. |

The full affine congruence used below is classical parity coding, as in
[Bernstein--Lagarias, *The 3x+1 conjugacy map* (1996)](https://websites.umich.edu/lagarias/doc/bernstein.pdf).
It is derived directly from finite words below.

[Rudolph, *Times 2 and times 3 invariant measures and entropy* (1990)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/64243AD8323B37089540F911F8CC77EB/S0143385700005629a.pdf/2_and_3_invariant_measures_and_entropy.pdf)
requires a measure invariant under both multiplications and ergodic for
their generated semigroup. Positive entropy is an additional hypothesis.
Stationarity under the actual valuation-selected affine skew map does
not give those two separate invariances. The theorem is inspected as a
possible consumer; it is not applied to a substitute measure here.

Mechanical itineraries and their ordinary approximation obstruction have
substantial prior work. [Lyapunov Weaver, *Finite approximation bounds
for mechanical Collatz itineraries*, Paper 84 (2026)](https://rstation.ai/problems/collatz/papers/84)
states stronger quantitative positive-integer prefix estimates, including
two-gap schedules and robustness under binary substitutions. Its stated
results and scope were read; its entire external proof is not imported
as a newly audited theorem. Our sparse-perturbation application below
is an elementary consequence of (1), not a priority or best-bound claim.

## 2. A finite ordinary word law at its actual source height

Use the shortcut map

\[
 T(x)=x/2\ (x\text{ even}),\qquad T(x)=(3x+1)/2\ (x\text{ odd}).
\]

Let `x_j=T^j(n)` for `0<=j<=N`, and assume these `N+1` positive
ordinary states are distinct. Put

\[
 H_N=\max_{0\le j\le N}x_j,
 \qquad b_j=x_j\bmod2\quad(0\le j<N).
\]

For `1<=m<=N`, let `P_(N,m)` be the uniform empirical law on the
overlapping words

\[
 (b_j,\ldots,b_{j+m-1}),\qquad 0\le j\le N-m.
\]

Its number of sampled starts is

\[
 M_{N,m}=N-m+1.                                            \tag{2}
\]

These are words from one unchanged ordinary path. No uniform source
residue law or independence of overlapping windows is assumed.

For a chronological binary word `w` of length `m`, let `p(w)` be its
odd count and `C(w)` its complete carry. Every occurrence satisfies

\[
 2^m x_{j+m}=3^{p(w)}x_j+C(w).                              \tag{3}
\]

If the same word occurs at `i` and `j`, subtraction and coprimality
give

\[
 \boxed{2^m\mid x_i-x_j.}                                 \tag{4}
\]

This is where ordinary height enters. If `2^m>H_N`, both sources are
positive integers smaller than the modulus, so (4) gives `x_i=x_j`.
Injectivity then gives `i=j`.

**Theorem 1 (exact long-word law).** Whenever `2^m>H_N`, all
`M_(N,m)` sampled words are distinct. Consequently

\[
 \boxed{H(P_{N,m})=\log(N-m+1),\qquad
        \sum_w P_{N,m}(w)^2=\frac1{N-m+1}.}                \tag{5}
\]

Here the collision is in **word space**, not endpoint residues modulo
a power of three. Both identities retain every overlapping occurrence.

A useful finite variant requires no relation between `m` and height.
Every word's sources lie in one residue class modulo `2^m`, hence
there are at most

\[
 L_{N,m}=\lfloor H_N/2^m\rfloor+1
\]

of them. Thus its empirical atom is at most `L_(N,m)/M_(N,m)`, and

\[
 H(P_{N,m})\ge
 \log(N-m+1)-\log(\lfloor H_N/2^m\rfloor+1).              \tag{6}
\]

The harmless extra residue cell in this upper count avoids special
endpoint conventions. A negative right side of (6) is simply a weak
bound. In the range of (5), the exact uniform word law is available.

## 3. Finite block averaging, with all endpoints retained

Write `H_(N,m)=H(P_(N,m))`. For every `1<=k<=m<=N`,

\[
 \boxed{
 H_{N,m}\le
 \left\lceil\frac mk\right\rceil
 \frac{N-k+1}{N-m+1}\,H_{N,k}.
 }                                                         \tag{7}
\]

**Proof.** Sample the start `J` uniformly from `0,...,N-m`. For any
internal offset `0<=a<=m-k`, the corresponding `k`-window is uniform
over the starts `a,...,a+N-m`. This interval is a subset of the
`N-k+1` starts used by `P_(N,k)`. Therefore its law `Q_a` has the
exact mixture relation

\[
 P_{N,k}=\rho Q_a+(1-\rho)Q'_a,
 \qquad \rho=\frac{N-m+1}{N-k+1}.                          \tag{8}
\]

Entropy concavity and nonnegativity imply `H(Q_a)<=H_(N,k)/rho`.
Partition the sampled `m`-word into complete consecutive `k`-blocks
and a final remainder. The chain rule bounds its entropy by the sum
of their entropies, with no independence assumption. If the remainder
is nonempty, it is a projection of the `k`-window at offset `m-k`,
which lies inside the same sampled word. Its entropy obeys the same
bound. There are `ceil(m/k)` terms, proving (7).

The overlapping last comparison is intentional and harmless: entropy
subadditivity does not require disjointness or independence of these
comparison windows. This proof is the finite block mechanism already
used for backward gaps in the pinned PR180 source, now applied to the
actual shortcut parity law and the new lower bound (5).

Combining (5) and (7) gives the explicit finite source inequality

\[
 \boxed{
 H_{N,k}\ge
 \frac{N-m+1}{N-k+1}
 \frac{\log(N-m+1)}{\lceil m/k\rceil}
 \quad(1\le k\le m\le N,\ 2^m>H_N).
 }                                                         \tag{9}
\]

## 4. Every same-subsequence stationary limit pays for slow height growth

Now suppose `n` has an infinite injective positive ordinary orbit.
Choose a subsequence `N_i -> infinity` along which every fixed parity
block law converges to `lambda_k`. Compactness of the finite binary
alphabets and diagonal extraction supply such subsequences.

Deleting either the first or the last coordinate changes the sampled
start interval by only its endpoints. The limiting block laws are
consistent under both deletions, and therefore define a stationary
binary process `lambda`. Every fixed-block entropy converges, because
the relevant alphabet is finite. Put

\[
 h(\lambda)=\lim_{k\to\infty}\frac{H(\lambda_k)}k
            =\inf_{k\ge1}\frac{H(\lambda_k)}k.             \tag{10}
\]

The equality follows from stationarity and block entropy subadditivity.

**Theorem 2 (same-source entropy--height tradeoff).** If along this
same subsequence

\[
 \limsup_i\frac{\log H_{N_i}}{\log N_i}\le\beta<\infty,
\]

then

\[
 \boxed{h(\lambda)\ge\frac{\log2}{\beta}.}                \tag{11}
\]

**Proof.** Distinct positive states give `H_N>=N+1`. Choose

\[
 m_i=\lceil\log_2(H_{N_i}+1)\rceil.
\]

Then `2^(m_i)>H_(N_i)`, `m_i -> infinity`, and
`m_i=O(log N_i)=o(N_i)`. For any fixed `k`, equation (9) eventually
applies. Its boundary ratio tends to one, and

\[
 \liminf_i
 \frac{\log(N_i-m_i+1)}{\lceil m_i/k\rceil}
 \ge \frac{k\log2}{\beta}.
\]

Passing only the fixed `k` entropy to the limit gives
`H(lambda_k)>=k log2/beta`. Taking the infimum in (10) proves (11).
The growing-word law was never identified with a growing-word block of
the limiting process.

For the more general statement (1), take a further subsequence on
which the height exponent approaches any finite value of its liminf.
It has the same fixed-block limit `lambda`, so (11) applies there.
If `h(lambda)=0`, existence of any bounded subsequence of height
exponents would contradict (11). Therefore

\[
 \boxed{
 h(\lambda)=0\quad\Longrightarrow\quad
 \frac{\log H_{N_i}}{\log N_i}\longrightarrow\infty.
 }                                                         \tag{12}
\]

In particular an ordinary escaping orbit with a polynomial bound on
all its prefix heights cannot have any zero-entropy stationary parity
limit. This is a statement about the same original integer, not about
changing finite realizers.

### Consistency with the existing critical height exponent

Under the finite polynomial-height hypothesis, the actual odd count
through shortcut clock `N_i` has density tending to
`alpha=log_3 2`. To see this, telescope logarithms of the actual map:

\[
 \log x_N-\log n
 =s_N\log3-N\log2
  +\sum_{\substack{j<N\\b_j=1}}
          \log(1+1/(3x_j)).                               \tag{13}
\]

Distinct positive states make the last sum `O(log(N+1))`: the sum of
reciprocals of any `N` distinct positive integers is at most the first
`N` harmonic sum. Also `0<=log x_N<=log H_N=O(log N)` along the
chosen subsequence. Divide (13) by `N`.

Thus `lambda{b_0=1}=alpha`, and the binary maximum entropy bound gives

\[
 h(\lambda)\le H_2(\alpha)\log2=\theta\log2,
 \qquad \theta=0.949955527188\ldots.
\]

Equation (11) consequently recovers `beta>=1/theta`. This is not a
new best general height bound; the existing global count is stronger
at its logarithmic endpoint and external compression work goes further.
The added information is dependence on the **actual limiting entropy**.
A strict entropy-rate deficit gives a strictly larger necessary power;
zero entropy excludes every polynomial height bound along that limit.

### The companion theorem on the exact backward odd-gap clock

The preceding theorem uses shortcut parity time. For the actual ternary
stationary lift in PR180, there is a direct statement on its original
odd clock, without identifying two different limiting laws by a return
map. Let `q_0,q_1,...` be the distinct positive odd states of one
unchanged ordinary orbit, with

\[
 q_{j+1}=\frac{3q_j+1}{2^{g_j}},\qquad
 A_M=\sum_{j<M}g_j,\qquad
 H_M^{\rm odd}=\max_{0\le j\le M}q_j.
\]

Let `Q_(M,m)` be the empirical law, with exactly `M-m+1` equally
weighted endpoints, of the actual reversed words

\[
 (g_{j-1},\ldots,g_{j-m}),\qquad m\le j\le M.
\]

Take a subsequence `M_i` along which every fixed word law converges
to a stationary positive-integer gap process `eta`. This is the same
kind of backward-gap lift used for the original ternary time limit
in PR180's pinned `COLLISION_CORE.md`. Put `a=E_eta G_1` and let
`h(eta)` be its entropy in nats per odd gap.

**Theorem 3 (direct ordinary-gap entropy--height tradeoff).** If

\[
 \limsup_i\frac{\log H_{M_i}^{\rm odd}}{\log M_i}
 \le\beta<\infty,
\]

then `h(eta)>=log 2/beta`. If `eta` is ergodic, the stronger bound is

\[
 \boxed{h(\eta)\ge\frac{a\log2}{\beta},
        \qquad 1\le a\le\ell=\log_2 3.}                 \tag{14}
\]

The same further-subsequence argument as before replaces the displayed
limsup by a liminf bound `beta>=a log 2/h(eta)` in the ergodic case.
Zero entropy forces a superpolynomial prefix-height exponent even
without ergodicity.

**Proof of the moment and entropy passage.** The exact odd-map
logarithm telescopes to

\[
 A_M\log2=M\log3+\log q_0-\log q_M
        +\sum_{j<M}\log(1+1/(3q_j)).
\]

Distinct positive sources make the sum `O(log(M+1))`. Hence
`A_M/M<=ell+o(1)`. Every fixed `k`-word empirical law has uniformly
bounded mean total gap, since each gap occurs in at most `k` words:
its mean is at most `k A_M/(M-k+1)`. Truncating the cost before
passing to the limit gives `1<=a<=ell`. Equality is not silently
assumed: the original average tends to `ell` under polynomial height,
but its limiting first moment can lose mass.

Uniform first-moment bounds do suffice for convergence of each fixed
block entropy, despite this possible loss of mean. Indeed, for a law
on positive-integer `k`-tuples with expected total cost at most `C`,
the mass `delta` above total cost `R` is at most `C/R`. Its entropy
contribution is at most

\[
 \delta\log(1/\delta)
       +k\delta\log\!\left(\frac{eC}{k\delta}\right).
                                                               \tag{15}
\]

To prove (15), normalize the tail, use entropy subadditivity and the
geometric maximum-entropy bound at the conditional coordinate means,
then use concavity of the logarithm. The bound tends uniformly to
zero as `R` tends to infinity. Entropy on the finite set with total
cost at most `R` converges under the fixed-block weak convergence.
Thus `H(Q_(M_i,k))->H(eta_k)` for every fixed `k`, and `H(eta_1)`
is finite. No uniform integrability of the unbounded gap itself has
been inferred.

**Proof of the unconditional bound.** Equal reversed gap words
have equal forward words and equal complete affine corrections.
If their total gap is `A`, their original sources are congruent
modulo `2^A`. Since every gap is positive, `A>=m`. With
`m_i=ceil(log_2(H_(M_i)^odd+1))`, every sampled word is therefore
distinct. Its entropy equals `log(M_i-m_i+1)`. The finite blocking
inequality (7) is valid on this alphabet too: all empirical laws
still have finite support and the exact endpoint mixture is unchanged.
The entropy passage just proved yields `h(eta)>=log 2/beta`.

**Proof of the ergodic improvement.** We first record the needed
growing-window conclusion without assuming convergence at a growing
block length. Fix a truncation `f_R(g)=min(g,R)` and put
`a_R=E_eta f_R(G_1)`. For any lengths `m_i -> infinity` with
`m_i=o(M_i)`, the empirical mean of `f_R` over a sampled `m_i`-word
converges to `a_R` in mean absolute deviation.

Here is the finite estimate behind that assertion. For fixed
`K<=m`, compare the mean over the `m` entries with the average of
its `m-K+1` internal `K`-window means. Their difference is at most
`R(K-1)/m`: after reversing the two sums, each comparison is an
average of a consecutive `m-K+1`-entry interval with only `K-1`
entries removed. Jensen's inequality and the exact endpoint-mixture
domination then give

\[
 \mathbb E_{Q_{M,m}}|\overline f_{R,m}-a_R|
 \le\frac{R(K-1)}m+
       \frac{M-K+1}{M-m+1}
       \mathbb E_{Q_{M,K}}|\overline f_{R,K}-a_R|.         \tag{16}
\]

Take `M=M_i` to infinity with `K` fixed; the bounded function on the
right passes to `eta_K`. Then take `K` to infinity. Ergodicity and
boundedness give mean convergence of the `K`-window average to `a_R`.
This proves the asserted growing-window concentration in exactly that
order. It uses no growing-block weak-convergence assertion.

Choose `0<epsilon<a/2`, then `R` with `a_R>a-epsilon/2`, and put

\[
 m_i=\left\lceil
       \frac{\log_2(H_{M_i}^{\rm odd}+1)}{a-2\epsilon}
      \right\rceil.
\]

These lengths are `O(log M_i)`. By (16), a proportion `1-o(1)`
of sampled words have total gap at least `(a-epsilon)m_i`, hence
strictly greater than `log_2 H_(M_i)^odd`. Every such word is unique
among the sampled occurrences by the complete source congruence.
The condition depends only on the word, so each of those words has
empirical mass exactly `1/(M_i-m_i+1)`. Their entropy contribution
alone gives

\[
 H(Q_{M_i,m_i})\ge(1-o(1))\log(M_i-m_i+1).
\]

Apply (7), pass only a fixed `k` entropy to its limit, then take its
stationary entropy-rate infimum. The result is
`h(eta)>=(a-2 epsilon)log 2/beta`. Let `epsilon` decrease to zero.
This proves (14) on the exact actual backward-gap lift.

In a critical ergodic limit with `a=ell`, (14) reads
`h(eta)>=log 3/beta`. This is an input to any separately proved
Shannon-dimension theorem for that same ternary code. It is still
not a Renyi-2 estimate: the exceptional `o(1)` word mass in the
argument comes with no collision-scale decay rate.

## 5. Criticality and nonatomicity alone allow zero ternary dimension

There is an exact stationary control showing why a source condition
such as (11) matters. Put `ell=log_2 3`, and choose `t` uniformly in
`[0,1)`. Define

\[
 G_i(t)=\lfloor t+i\ell\rfloor-\lfloor t+(i-1)\ell\rfloor,
 \qquad i\ge1.                                            \tag{17}
\]

These gaps lie in `{1,2}`. Their law is stationary and ergodic under
the irrational rotation `t -> {t+ell}`. Integration gives
`E G_i=ell` exactly. Thus it is conditionally critical.

Let

\[
 Z(t)=\sum_{i\ge1}3^{i-1}2^{-(G_1+\cdots+G_i)}
 \quad\text{in }\mathbb Z_3^\times,
 \qquad \mu=Z_*dt.                                       \tag{18}
\]

For an `m`-word over `{1,2}`, the residue in (18) modulo `3^m`
determines the complete word. Its residue modulo three determines
`G_1`, because `2^(-1)=2` and `2^(-2)=1` there. Stripping the
affine term gives
`(2^(G_1)Z-1)/3` modulo `3^(m-1)`, and induction recovers the rest.

The `m`-gap word in (17) changes only at the `m+1` distinct circle
points

\[
 0,\{-\ell\},\ldots,\{-m\ell\}.
\]

There are exactly `m+1` positive-length interval cells. Their words
are distinct: every prefix sum is `floor(t+i ell)`, which is
nondecreasing in `t` and changes at its own breakpoint. Write their
lengths as `a_(m,0),...,a_(m,m)`. The coding injection proves the
exact formula

\[
 \boxed{\operatorname{Col}_{3^m}(\mu)
       =\sum_{j=0}^m a_{m,j}^2\ge\frac1{m+1}.}            \tag{19}
\]

The breakpoint mesh tends to zero by density of the irrational
rotation. Consequently the collision tends to zero; every nested
code cylinder has vanishing mass, so `mu` is nonatomic. Yet (19)
gives

\[
 \boxed{\dim_2\mu=0.}                                    \tag{20}
\]

Indeed the support itself is covered at ternary depth `m` by only
`m+1` cylinders, so its upper box dimension is zero. This is not a
finite atomic approximation being mislabeled as a nonatomic limit.

The same code also verifies the real divergence explicitly. Since
`A_i=floor(t+i ell)`, its real partial sum is

\[
 R_m(t)=\frac13\sum_{i=1}^m2^{\{t+i\ell\}-t},
 \qquad
 \frac{2^{-t}}3m\le R_m(t)<\frac{2^{1-t}}3m.              \tag{21}
\]

Thus this ergodic critical law has linearly divergent real sums and
a nonatomic ternary factor of dimension zero. It satisfies those
conclusions of PR180's stationary-real theorem without supplying any
positive collision dimension. It is an auxiliary symbolic law, not
asserted to be an actual ordinary time limit.

## 6. An attempted polynomial-growth model is excluded by the actual theorem

The pure mechanical script (17) has bounded coherent scale
`chi_j=3^j/2^(A_j)`. It already fails the unbounded-scale condition
of an escaping ordinary source. It would also give only linear real
state growth, conflicting with the existing ordinary count. It is
therefore not presented as a countermodel satisfying every source input.

One can make the symbolic scales grow polynomially without changing
the stationary local law. Here is a precise attempted repair and why
it still cannot be an ordinary positive orbit.

Take one mechanical gap sequence `g_j^0` from (17), with indices now
starting at zero. Because `ell-1>1/2`, every two consecutive positions
contain a gap two. For every `k>=4`, let `n_k` be the first gap-two
position at or after `ceil(2^(k/2))`. These positions are distinct,
and at most one later than their prescribed thresholds. Change those
gaps from two to one, leaving all other gaps unchanged. If `D_j`
counts changes before `j`, then

\[
 D_j=2\log_2 j+O(1),\qquad
 A_j=A_j^0-D_j,
 \qquad \chi_j=3^j2^{-A_j}\asymp j^2.                    \tag{22}
\]

The changes have zero density. Every fixed gap-block empirical law
still tends to the mechanical law, since only `O(m D_j)` of its
length-`m` windows can meet a changed position.

The shortcut parity script obtained by expanding a gap `g` to
`1 0^(g-1)` likewise has only `O(log j)` deleted zeroes relative to
the unmodified script. Every stationary parity limit has entropy zero.
One can see this without importing a symbolic classification: an
unmodified length-`k` binary factor is determined by at most `k+1`
successive mechanical gaps and one of at most two starting offsets.
There are at most `2(k+2)` such factors. The fraction of actual
`k`-windows touching a deletion tends to zero. Each limiting block
law is supported on at most `2(k+2)` words, and its entropy rate is zero.

If a fixed positive ordinary source `n` realized this entire script,
the full forward affine identity would give

\[
 q_j=\chi_j\left(n+\frac13\sum_{i<j}\chi_i^{-1}\right).
                                                               \tag{23}
\]

The sum converges by (22), so `q_j` is of order `j^2`. Intermediate
shortcut heights have the same polynomial bound, because gaps are
one or two. The states tend to infinity and hence cannot repeat in
a deterministic ordinary trajectory. Theorem 2 would therefore give
positive entropy at least `log2/2`, contradicting the zero-entropy
limit just obtained.

**Conclusion:** no fixed positive ordinary integer realizes this
polynomial-scale sparse mechanical perturbation. Every finite prefix
has positive ordinary realizers by the exact parity cylinder, but
those sources must change. The attempted repair is eliminated by a
same-source arithmetic argument, not merely by failure of stationarity.
This illustrative exclusion does not improve the cited best mechanical
approximation bounds.

## 7. What remains before a collision contradiction

The new positive theorem separates two regimes of a hypothetical
escaping orbit. Along any stationary parity limit of finite polynomial
height exponent, that limit must have quantitatively positive entropy.
Along a zero-entropy limit, the same prefix maxima must exceed every
fixed power of the clock. No theorem here excludes the latter regime,
or rules out positive-entropy limits in the former.

Moreover positive parity entropy is not the missing ternary collision
upper. The ternary observable groups many complete gap words; its
source and carry quotients cannot be discarded. Even a positive
Shannon entropy rate does not identify a Renyi-2 rate or supply separate
times-two and times-three invariance. The actual finite word injection
occurs at a binary precision determined by the original height.

PR178's new equivalent flow removes a coalescence-rate loss while
preserving the original root inverse law. Its uniform relative collision
comparison makes the same-source issue particularly explicit: it
transfers an upper estimate if one is proved, but does not generate it.
No new choice of that flow changes the parity blocks or the height
inequality above.

The first unproved closing bridge remains an arithmetic theorem on
the same source: either exclude its allowed positive-entropy limit,
exclude its superpolynomial zero-entropy regime, or control the actual
ternary aggregation strongly enough to meet the critical dimension
target. The invariant measure required by Rudolph's theorem has not
been constructed, and no Haar or independent gap law is substituted.

## 8. Formal and verification boundary

`FixedSourcePressure.lean` defines the ordinary shortcut map and its
chronological parity prefix, proves their complete affine identity,
and then checks finite ordinary source equality, word injection and
exact word cardinality at the original source-height bound. Its general
residue-cell multiplicity theorem counts every source of a repeated
word at arbitrary height. These are the arithmetic inputs to (5)--(6).
The entropy chain rule, finite mixture inequality, stationary-limit
argument, irrational rotation law and sparse perturbation analysis
remain written proofs. No universal growth or collision theorem is
assumed as an implicit axiom.

Author development compilation succeeded with Lean 4.34.1, one thread,
and `-DwarningAsError=true`, using separately compiled unchanged
`CycleWordAlgebra` and `CarryFibers` dependencies in a scratch output
directory. Independent source review and root fresh replay have separate
receipts; a source author does not claim another process's execution.
The finite arithmetic controls are not evidence of an escaping ordinary
example.

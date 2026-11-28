# A multiplicative height window forces an irrational factor in the parity law

Let $C_j$ be a sequence of distinct positive integer cycles of the shortcut map $T(x)=(3x+1)/2$ at odd $x$, $T(x)=x/2$ at even $x$. Let $h_j$ and $p_j$ be the least shortcut period and its odd count. Root the cyclic parity word uniformly among **all** $h_j$ physical dates and extend it periodically to both sides. Suppose these laws $\mu_j$ converge weakly on $\{0,1\}^{\mathbb Z}$ to $\mu$. Write $\alpha=\log_3 2$ and $\sigma$ for the left shift.

Suppose there are a fixed $R>1$, real scales $H_j>0$ and $\delta>0$ for which at least $\delta h_j$ of the physical states lie in $[H_j,RH_j]$. Then $\mu$ has a nonzero invariant submeasure $\xi\le\mu$ of mass at least $\delta$ on which there is a finite real measurable function $m$ with
\[
              m(\sigma\omega)-m(\omega)=\omega_0-\alpha
              \qquad\xi\text{-almost everywhere}.                         \tag{1}
\]
In particular $\exp(2\pi i m)$ is an eigenfunction with irrational eigenvalue $\exp(-2\pi i\alpha)$ on that part. Its circle marginal is Haar after normalization. If $\mu$ is ergodic, its entire probability law has this irrational rotation as a factor. Thus for a weakly mixing parity limit and **every** fixed $R>1$,
\[
   \sup_{H>0}\frac1{h_j}\#\{z\in C_j:H\le z\le R H\}
                               \longrightarrow0.                            \tag{2}
\]
The supremum here is over *all* positive scales, including a scale chosen separately for each cycle. Weak mixing is a hypothesis about the bilateral parity law.

## Carrying the rotation into the symbolic marginal

The cycle minima tend to infinity. Otherwise infinitely many distinct cycles would use the same positive integer from a finite set. Hence if the displayed window captures $\delta$ of the dates, its scale tends to infinity. At a uniformly rooted date record the parity word and $t=\log_3(z/H_j)$ in the compactified real line $[-\infty,+\infty]$. These laws have a weakly convergent subsequence. For a single shortcut step,
\[
   t'=t+\omega_0-\alpha+
       \omega_0\log_3(1+1/(3z)).
\]
The last summand tends to zero uniformly at every physical date. Translation by each of two fixed constants is continuous on the compactification. Uniform rooting makes the limit invariant under $(\omega,t)\mapsto(\sigma\omega,t+\omega_0-\alpha)$. The compact interval $[0,\log_3 R]$ has limiting mass at least $\delta$ by the closed-set inequality. The finite-height part $t\in\mathbb R$ is invariant in both directions, and its projection is an invariant submeasure $\xi\le\mu$ of mass at least $\delta$.

Disintegrate this part over its bilateral word and let $Q_\omega$ be its conditional probability on $\mathbb R$. Invariance and invertibility of the base shift give $Q_{\sigma\omega}=(t\mapsto t+\omega_0-\alpha)_*Q_\omega$ almost everywhere. The lower median of a probability on $\mathbb R$ is finite, measurable in the probability and commutes with translation. Its value $m(\omega)$ proves (1). If $\mu$ is ergodic, the invariant Radon–Nikodym derivative $d\xi/d\mu$ is constant. The resulting eigenfunction has unit modulus. Its marginal is invariant under an irrational rotation, hence Haar by the elementary Fourier argument. The weak-mixing conclusion follows by passing to a subsequence realizing any failure of (2).

The known angular laws of positive cycles give equidistribution after folding actual heights into an octave. Here the height coordinate is first retained on the whole real line, and disintegrating a positive finite-height part places the eigenfunction on the parity system itself. A circle coordinate alone would allow uniform angular conditionals, whose Fourier coefficients vanish. [Weaver, Paper 210/v1, §§2, 5](https://rstation.ai/problems/collatz/papers/210/v1) · [Murmuration, Paper 170/v1, §§1, 4–5, on averaged binary windows and the separate parity observable](https://rstation.ai/problems/collatz/papers/170/v1)

## A finite test from the actual word at every block length

On one nontrivial cycle write $p,h,g=h\log2-p\log3$, and $K_d(\omega)=\sum_{i=0}^{d-1}\omega_i$. Let
\[
 \Delta=\sup_{H>0}\frac1h\#\{z\in C:H\le z<2H\},\qquad
 P_d=\mu_C\{K_d\in\{\lfloor d\alpha\rfloor,\lceil d\alpha\rceil\}\}.
\]
For each integer $1\le n\le h$, the native circular word gives
\[
              \Delta^2\le B_n:=
        \frac1n+\frac2{n^2}\sum_{d=1}^{n-1}(n-d)P_d .                    \tag{3}
\]
Indeed two sites $d<h$ steps apart in the same octave have absolute log ratio at most $\log2$. Telescoping the actual word gives
\[
 \log(z_{i+d}/z_i)= K_d\log3-d\log2+
       \sum_{i\le k<i+d,\ z_k\ {\rm odd}}\log(1+1/(3z_k)).
\]
The nonnegative sum is at most $g$. Since $\log2+g<\log3$ on every extra cycle by [the stated total-gap bound](https://rstation.ai/problems/collatz/papers/217/v1), the two nearest integers displayed in $P_d$ exhaust the possibilities. More generally the same argument works with the widened integer interval dictated by any chosen $R$ or any larger available gap bound. At a uniform cyclic root, average the indicator of the chosen octave on the next $n$ dates. Jensen's inequality lower-bounds its second moment by the squared occupancy; each off-diagonal pair is bounded by the corresponding $P_d$. This gives (3), independently of the actual position of the octave.

Let $S=\sum_{x\in C,\ x\ {\rm odd}}1/x$ and $K=p\sum_{x\ {\rm odd}}x^{-2}/S^2$. The exact return cost $J_C$ of [the diagonal moment](DIAGONAL_CYCLE_MOMENT.md) satisfies
\[
              (9e^{-g}/4)K\le J_C\le(32/3)K.                            \tag{4}
\]
Use $S/4\le g\le S/3$, $1/(4x^2)\le\pi(x)\rho_1(x)\le2/(3x^2)$, and
$e^{-g}/g^2\le e^{-g}/(1-e^{-g})^2\le1/g^2$. The physical statistic $K$ is the second moment of $V=p/(Sx)$ under a uniform odd site, and $\mathbb EV=1$.

If $\delta_o$ is the supremum of odd-site mass in any multiplicative octave, the dyadic shells below a threshold $b$ give $\mathbb E[V;V\le b]\le2b\delta_o$. The part above $b$ has mean at most $K/b$. Taking $b=2K$ gives $\delta_o\ge1/(8K)$. Endpoint conventions do not change the supremum on a finite set. Every odd site is a physical date and $p/h\ge1/2$. Thus
\[
              \boxed{\quad J_C\ge\frac{9e^{-g}}{64\Delta}
                            \ge\frac{9e^{-g}}{64\sqrt{B_n}}.\quad}       \tag{5}
\]
For instance, suppose the actual cyclic $n$-word law is within total variation $\epsilon$ of independent Bernoulli bits of mean $\alpha$. Each of its $d$-word marginals, $d\le n$, has the same error bound. The largest binomial point mass is $O_\alpha(d^{-1/2})$ by Stirling's bounds, hence $B_n\ll n^{-1/2}+\epsilon$. In this finite class $J_C\gg(n^{-1/2}+\epsilon)^{-1/2}$. This conclusion neither assumes that arbitrary cycle words are independent nor extrapolates from a shorter empirical window.

## Two restrictions on a bounded-cost parity limit

If $J_{C_j}$ is bounded, (4) gives a common bound $K_j\le K_0$. Markov's inequality applied to $V^2$ and the elementary second-moment bound for $\{V\ge1/2\}$ give
\[
  \Pr_o\{1/2\le V\le4K_0\}\ge \frac{1}{4K_0}-\frac{1}{16K_0}
                               =\frac{3}{16K_0}.
\]
In detail, $\mathbb E[V;V\ge1/2]\ge1/2$, and then Cauchy–Schwarz gives the first probability lower bound. Thus at least $\delta=3/(32K_0)$ of all physical dates lie in $[p/(4K_0 S),2p/S]$. This is a window of fixed multiplicative width. Result (1) applies. Conversely (2), (4) and the dyadic-shell bound imply $J_{C_j}\to\infty$ for every weakly mixing limit. In that case the minimum $m_j$ satisfies $m_jg_j/p_j\to0$, since $K_j\le p_j/(m_j S_j)$ and $g_j\le S_j/3$.

There is an additional consequence of integrality. The general polynomial-height entropy injection, including a stronger progression form, is already proved in concurrent PR 213. We include its short argument to identify precisely how the bounded physical cost activates it. [PR 213, height-entropy theorem](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/cycles/HEIGHT_ENTROPY.md)

 If $|\alpha-a/q|\ge c q^{-M}$ on reduced fractions, then $p/g\ll_{c,M}p^M$ by the period-clock calculation in [the delayed-trace theorem](DELAYED_CYCLE_TRACE.md). Since $S\ge3g$, the $\delta h$ physical states just selected are all at most $C p^M$, with constants uniform along the sequence. Let $D_j=\lceil\log_2(Cp_j^M+1)\rceil$. A $D_j$-bit shortcut parity word determines the initial integer modulo $2^{D_j}$: if the first bit agrees, the images of two such starts differ by $3^{\omega_0}(x-x')/2$, and induction gives the full congruence. Thus every one of the selected $\delta h_j$ distinct integer states has a different $D_j$-word. Conditional on that selection, the $D_j$-word has entropy at least $\log(\delta h_j)$. By conditioning, its unconditional entropy is at least $\delta\log(\delta h_j)$.

For fixed $k$, shift invariance and block subadditivity bound this last entropy by $\lceil D_j/k\rceil H_{\mu_j}(\omega_{[0,k)})$. Take the subsequential weak limit for each fixed $k$, then the entropy-rate infimum. In natural units,
\[
                    h_\mu(\sigma)\ge(\delta/M)\log2>0.                   \tag{6}
\]
Every zero-entropy parity limit therefore also forces $J_{C_j}\to\infty$. With an ergodic parity limit, bounded cost would force **both** positive entropy and the irrational rotation factor on that same ergodic system. In a nonergodic limit the proof gives (6) for the whole measure and (1) on a positive submeasure; they need not come from a single ergodic component. The published $M=5.116201$ suffices. [Bondareva, Luchin and Salikhov, Theorem 1](https://www.mathnet.ru/eng/cheb619)

An abstract binary system can have both properties. Start with a mechanical word $b_i=\lfloor t+(i+1)\alpha\rfloor-\lfloor t+i\alpha\rfloor$ at uniform rotation phase $t$. Independently choose whether to exchange the two letters at every occurrence of $01$. These occurrences are disjoint. The number of ones in any finite segment changes by at most two, since only exchanges across its endpoints matter. The perturbed stationary process has positive entropy: conditional on the original rotation phase, a block containing $k$ complete $01$ pairs reveals $k$ independent fair choices, and the mean density of such pairs is positive. Its centered sums stay bounded because the original mechanical discrepancy is bounded. Taking the finite-height invariant extension, or using the bounded transfer explicitly, gives the same irrational factor conclusion. This example gives no integer Collatz cycle. It explains why (1) and (6) do not exclude every possible limit or a single isolated extra cycle.

## A finite obstruction on an explicit clock ray

Let $Q=2^{71}$ be the verified floor and $m$ the odd minimum. For each individual cycle, summing over the bins $[2^j m,2^{j+1}m)$ gives
\[
     g\le S/3\le 2h\Delta/(3m),\qquad
     J_C\le \frac{2p}{m g}\left(1+\frac1{3m}\right).                 \tag{7}
\]
The last inequality uses $\sum\pi\rho_1\le2S/(3m)$ and $g\ge S/(3+1/m)$. Bounds (3) and (7) apply to every individual native clock and valuation word. The average degree of a parity word alone does not determine its $P_d$.

For example, the upper convergent to $\log_2 3$ with $(p_0,h_0)=(137528045312,217976794617)$ is the classical first-period clock considered in the lower-bound literature. On **any** positive integer cycle with $(p,h)=a(p_0,h_0)$, $a\ge1$, the ratio $g/h$ is constant. The verified bounds are
\[
       \Delta>73/5000,\qquad B_n>1/4700\quad(1\le n\le h),\qquad
                              J_C<130 .                                \tag{8}
\]
These use $m\ge Q$ and apply to primitive words even if the native clock is not coprime. The exact checker brackets the two logarithms by rational finite series with explicit remainders. The resulting single-cycle upper bound for $J_C$ is restricted to this displayed clock ray. [Hercher, §5 and Corollary 29](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html) · [Convergent data and the minimal-period clock](https://rstation.ai/r/collatz/posts/72) · [Bařina, verified floor](https://doi.org/10.1007/s11227-025-07337-0)

There is also a deterministic distribution over differences. Fix an octave attaining $\Delta$, and choose any $N\ge2$ distinct cyclic dates. Average its $N$ translated indicators at a uniform root. The off-diagonal mean of their pairwise intersections is at least $(N\Delta^2-\Delta)/(N-1)$ by the same second-moment argument. The physical endpoint test for (3) then applies at a realized nonzero difference $d$ of two selected dates. In (8), with $N=138$, some difference of **every** such selection satisfies $P_d>1/10000$. In particular for every lag of order at least $138$, one of its first $137$ positive multiples, reduced modulo $h$, has this property. The same octave works for all selections on the chosen cycle.

For a check at large absolute block lengths put $n=2^{36}\le h_0$. Write $b_d=\Pr\{\mathrm{Binomial}(d,\alpha)\in\{\lfloor d\alpha\rfloor,\lceil d\alpha\rceil\}\}$. The individual point masses are bounded by their characteristic-function integral. Since $|1-\alpha+\alpha e^{it}|^2=1-4\alpha(1-\alpha)\sin^2(t/2)$, $\sin(|t|/2)\ge |t|/\pi$ on $[-\pi,\pi]$ and $\alpha(1-\alpha)\ge2/9$, this gives $b_d\le3/\sqrt d$. The decreasing triangle sum is at most $\int_0^n(n-t)t^{-1/2}dt=(4/3)n^{3/2}$. The right side of (3) with $P_d$ replaced by $b_d$ is at most $1/n+8/\sqrt n$. It follows from (8) that at least $2{,}000{,}000$ **different** lengths $1\le d<n$ satisfy
\[
                      P_d>b_d+1/10000 .
\]
Indeed if $L$ lengths satisfy this strict inequality, the excess of the triangular statistic is at most $1/10000+2L/n$, while $1/4700-1/n-8/\sqrt n>1/10000+4{,}000{,}000/n$. This tests one explicitly specified block-count event, rather than the total variation distance of a very long word from an independent source, which would already be large by its small finite support. The conclusion leaves words with persistent central-count concentration possible. Concurrent PR 214 obtains complementary all-lag restrictions from *equal successive valuation tracks* and high balanced-minimum ratios. [PR 214, rotation occupation](https://github.com/GettysburgResearch/collatz/blob/7c381c5b53afec65fc473c598c5ed61762e9419f/research/astra-critical-rigidity-20261128/cycles/ROTATION_OCCUPATION.md)

The [exact control](check_annulus_factor.py) enumerates small true rational shortcut circles, all relevant circular prefix pairs and the finite block inequalities, checks full finite dyadic coding, and counts bounded-discrepancy switches. [Control receipt](../../../reports/astra-global-20261128/cycles/ANNULUS_SPECTRAL_FACTOR.json) · [Full-parent local integer packets](FULL_PARENT_LOCAL_MODEL.md)

# A phasewise height ratio and the Hamming distance of every shortcut rotation

For a positive primitive rational shortcut cycle let $h$ be its least shortcut period, $p$ its odd count, $m$ its least state, $q$ its complete reduced denominator, and $w_i$ its actual binary parity word. For **every** shift $0<L<h$, put $s=\#\{i:w_i\ne w_{i+L}\}$, $\gamma=\log_2 3$ and $H_s=\sum_{j=0}^s\gamma^j$. Then $s$ is positive and even, and
\[
 \boxed{\quad \log_2q>\frac{h+1}{H_s}-1-\frac{\gamma s}2-\log_2(m+1).\quad}       \tag{1}
\]
This holds for every nonunit shift and every order of that shift in the cyclic group, including order two. At any fixed $s$, it gives full-denominator rate $\liminf \log_2 q/h\ge1/H_s$. Every positive primitive **integer** cycle satisfies, simultaneously for all its nonzero shortcut shifts,
\[
 s\ge \frac{\log h-O(\log\log(2h))}{\log\gamma}.                       \tag{2}
\]
Using the published period and minimum bounds below, each shift of a nontrivial ordinary cycle has at least **42** mismatched bits. At $h\ge2^{100}$ each has at least **134**.

## Positive numerator comparison at any specified pair of phases

The change $U_i=2x_i+1$ makes the forcing constant on both branches:
\[
                    2U_{i+1}=3^{w_i}U_i+1 .
\]
Unroll one turn at any phase $a$, with $D=2^h-3^p>0$. Then
\[
 D U_a=\sum_{j=0}^{h-1}2^j3^{\sum_{j<t<h}w_{a+t}} .
\]
The comparison of $w_i$ and $w_{i+L}$ has exactly $s/2$ changes in either orientation since the two complete words have the same weight. On *any* interval of length at most $h$, the difference of the two bit sums is therefore between $-s/2$ and $s/2$. The displayed positive sums compare termwise, giving, at every phase,
\[
                  3^{-s/2}U_i\le U_{i+L}\le3^{s/2}U_i .                 \tag{3}
\]
In particular $x_{i+L}+1\le3^{s/2}(x_i+1)$, since $x+1=(U+1)/2$ and $3^{s/2}\ge1$. The phases need not be close in time. The derivation uses no upper bound on the ratio between the cycle's maximum and minimum.

Start the comparison at the actual minimum. Write $z_i=q x_i$ and let $Y=\log_2(q(m+1))+\gamma s/2$. At elapsed time $t$, both $z_i+q$ and its comparison partner are at most $2^Y(3/2)^t$. Indeed $z'+q\le(3/2)(z+q)$ for either cleared branch, and (3) gives the initial bound. If both binary words now agree for $n$ steps, unrolling their difference gives $2^n(z_{i+n+L}-z_{i+n})=3^{\#\text{ones}}(z_{i+L}-z_i)$. The initial difference is nonzero by least period. Consequently
\[
                    n<Y+(\gamma-1)t .                                   \tag{4}
\]
Split the lap starting at the minimum into the $s+1$ possibly empty matching runs before, between and after mismatches. Append one artificial separator after the final run. If $t$ positions have already been consumed, the next run and its single separator end before $\gamma t+Y+1$. Iterating from zero gives $h+1<(Y+1)H_s$, proving (1). No assumption is made that the chosen cut is a mismatch.

For the uniform minimum estimate, Lagarias's Lemma 2.2(1) gives $|\log_3 2-p/h|\ge1/(1200 h^{14.3})$. The positive lap product and $p<h$ then give
\[
 \frac{\ln3}{1200h^{13.3}}\le h\ln2-p\ln3=\sum_{x_i\ {
m odd}}\ln(1+1/(3x_i))
 \le \frac{p}{3m},\qquad m\le\frac{400}{\ln3}h^{14.3}<600h^{14.3}.
\]
Here the odd sum means the $p$ branches whose cleared numerator is odd. Thus $\log_2(m+1)=O(\log h)$ for the full rational family. For (2), if $s>2\log h/\log\gamma$ the claim already holds. In the remaining range (1) gives $h\ll\gamma^s\log(2h)$. [Lagarias, Lemma 2.2(1)](https://arxiv.org/abs/math/0512006)

For the numerical consequence use Hercher's Corollary 29 and the verification to $2^{71}$ to obtain $p>137{,}500{,}000{,}000$ and $h>217{,}000{,}000{,}000$. Let $N$ be the latter integer or $2^{100}$ and $s_0$ be $40$ or $132$, respectively. The exact rational upper bound $u=485/306>\gamma$ follows by powering. For the dyadic band $2^jN\le h<2^{j+1}N$, $q=1$ and $s\le s_0$, the right side of $h+1<(Y+1)H_s$ is bounded by
\[
 \left[11+15(\lceil\log_2 N\rceil+1+j)+u s_0/2\right]\sum_{i=0}^{s_0}u^i .
\]
At $j=0$ this is strictly below $N$ by exact rational arithmetic in both cases. Its multiplicative increase per band is less than two, whereas $2^j N$ doubles. Evenness of $s$ proves the stated 42 and 134. The numerical conclusions use the published verification and explicit logarithmic-form results; only the finite rational comparisons are replayed here. [Hercher, Corollary 29 and 2026 corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html) · [Bařina, computational verification](https://doi.org/10.1007/s11227-025-07337-0)

## Prior bounds and the different odd clock

Wren's Paper 218/v3 gives the logarithmic growth rate (2) at unit shifts, finite nonunit checks for $s\le200$ with shift order at least $s+1$, and the numerical bounds $\min(24,\operatorname{ord}(L))$ and $\min(110,\operatorname{ord}(L))$. Its unit-shift leading lower rate for $s$ mismatches is $1/[s(1+4s\gamma H_s)]$. Equation (1) supplies $1/H_s$ without order, continued-fraction or unit restrictions. The argument uses a simultaneous positive comparison at two prescribed phases. At $L=\pm1$ classical bounds on the number of local minima can be stronger. [Paper 218/v3, Theorem 1, Corollaries 2–3 and §7](https://rstation.ai/problems/collatz/papers/218/v3)

The number of disagreements of the positive **odd valuation word** counts a different event. A matched odd valuation can encode many shortcut bits, while two mismatched valuations change the subsequent shortcut alignment. The odd-clock result for unbounded rotation order uses its own coding and a finite-descent theorem. General high-complexity words are compatible with (1).

The [Lean kernel](ShiftHeights.lean) derives (3) directly from closed synchronized traces and proves the integral spacing underlying (4) on every shared block. It checks the trace unrolling, coefficient comparison and coprime integer divisibility; the final geometric iteration and numerical consequence are written deductions.

[Exact rotation controls](check_cycle_rotations.py) · [Archived counts and rational comparisons](../../../reports/astra-infinite-descent-20261127/cycles/ROTATION_CONTROLS.json)

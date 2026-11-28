# How much of an aperiodic integer orbit can shadow simpler rational starts?

**PROPOSED, written proof using Evertse's Theorem 2.** Let $x_t=T^t(n)$ be a non-eventually-periodic positive integer orbit. References have odd denominator and use the genuine shortcut map on the rationals in $\mathbb Z_2$. Choose disjoint intervals of matching parity, with initial times $a_i$ in increasing order. The reference $\rho_i$ can change at every interval. Require its exact forward match length to be finite and positive:
$$
 \ell_i=v_2(x_{a_i}-\rho_i),\qquad a_i+\ell_i\le a_{i+1}.
$$
Thus each comparison continues to its first discrepancy, even when the next one starts immediately afterward. Write $B_i=\log_2(x_{a_i}+1)$ and fix $\delta>0$ with $\ell_i\ge\delta B_i$. For $\rho=A/D$ in lowest terms with $D>0$, let $H(\rho)=\max(|A|,D)$. Assume
$$
 \log_2(2H(\rho_i))=o(\ell_i).
$$
Let $M(t)$ count all steps in the union of the matching intervals among the first $t$ inputs, and let $U(t)$ count the **odd** inputs outside those intervals. If there are only finitely many intervals, the bounds below hold directly.

**Theorem.** Set $\gamma=\log_2 3$ and $c=\gamma-1$. For arbitrary such references,
$$
 (1-c)M(t)\le cU(t)+o(t),\qquad
 \limsup_{t\to\infty}\frac{M(t)}t\le c=0.5849625\ldots.
$$
If in addition their terminal states $\sigma_i=T^{\ell_i}(\rho_i)$ satisfy $\log_2(2+|\sigma_i|)=o(\ell_i)$, then
$$
 M(t)\le cU(t)+o(t),\qquad
 \limsup_{t\to\infty}\frac{M(t)}t\le\frac{c}{1+c}=0.3690702\ldots.
$$
In this second case $\liminf U(t)/t\ge1/\gamma^2$. Any fixed finite dictionary of rational periodic phases satisfies both small-height hypotheses. All matches can be chosen after seeing the orbit. The general statement also allows changing odd denominators and unbounded references subject to the stated size bounds.

## 1. Exact signed carries and nonvanishing subsums

Take $d$ consecutive selected intervals, with indices renumbered $1,\ldots,d$. In the gap from $a_i+\ell_i$ to $a_{i+1}$, let $r_i=s_i+h_i$ count odd and even steps. Denote the constant term of its ordinary affine numerator by $A_i^{\rm gap}$, so that the following comparison holds with $F_i$ as displayed:
$$
 2^{r_i}(x_{a_{i+1}}-\rho_{i+1})
   =3^{s_i}(x_{a_i+\ell_i}-\sigma_i)+F_i,\qquad
 F_i=3^{s_i}\sigma_i+A_i^{\rm gap}-2^{r_i}\rho_{i+1}.
$$
For an empty gap, $s_i=h_i=A_i^{\rm gap}=0$ (and $2^{r_i}=1$). Let $Q$ be the least common multiple of the odd denominators of the $\rho_i$. A rational orbit retains its initial odd denominator as a common denominator, so $QF_i$ is an integer.

It is **odd**. For a nonempty gap, in the first prescribed gap step the parity of $\sigma_i$ is the opposite of the actual bit. Therefore the numerator $3^b\sigma_i+b$ is an odd 2-adic integer at this step. Propagating it to the gap end by multiplying by 1 or 3 and adding even integers keeps the numerator odd. Subtracting $2^{r_i}\rho_{i+1}$ preserves oddness. For an empty gap, $\sigma_i$ has parity opposite to the actual next input, whereas $\rho_{i+1}$ matches it, so $\sigma_i-\rho_{i+1}$ is odd.

On each matching interval the actual and reference differences evolve homogeneously. Put $L=a_d-a_1$, let $A$ count all odd inputs there, $P_i=a_i+\ell_i-a_1$ and $J_i$ count the odd inputs after gap $i$ up to time $a_d$. The composed identity is
$$
 2^L Q(x_{a_d}-\rho_d)=3^A Q(x_{a_1}-\rho_1)
              +\sum_{i<d}2^{P_i}3^{J_i}QF_i. \tag{1}
$$
The $d-1$ gap terms have the strictly increasing dyadic valuations $P_i$. They are all less than the valuation $L+\ell_d$ of the nonzero complete sum. No nonempty subsum of the right-hand terms vanishes: without the root term there is a unique lowest valuation; if a root-containing proper subsum omits gap terms, its complement has lower valuation than the complete sum, so the subsum cannot vanish. This verifies the exact hypothesis that signs had made automatic only in the all-odd case.

## 2. Carry size and the fixed-dimensional estimate

For the ordinary unshifted map an odd step contributes one to its local affine numerator. With fixed $s,h$, placing all evens before all odds maximizes the numerator, by adjacent exchanges. It is thus at most $2^h(3^s-2^s)\le 2^h3^s$. Consequently
$$
 |QF_i|\le 3 Q(1+|\sigma_i|)(1+|\rho_{i+1}|)3^{s_i}2^{h_i}.
$$
Define $D_i=\log_2(2H(\rho_i))$ and $R_i=\log_2(2+|\sigma_i|)$. Since $\log_2 Q\le\sum D_i$, the outside-$\{2,3\}$ parts of the right-hand terms in (1) have product at most
$$
 2^{B_1-\ell_1+C d\sum_i D_i+\sum_{i<d}R_i+\sum_{i<d}(\gamma s_i+h_i)}
$$
for an absolute constant $C$: the first term has outside part at most $Q|x_{a_1}-\rho_1|/2^{\ell_1}$, and the powers of two and three in the other terms cost nothing outside those primes. A further absolute constant covers their per-term numerical factors since all $D_i\ge1$. The maximum of the ordinary absolute values of the right-hand terms has logarithm at most
$$
 B_1+\gamma L+C d\sum_i D_i+\max_{i<d}R_i+C.
$$
Indeed each mixed power $2^{P_i}3^{J_i}3^{s_i}2^{h_i}$ is at most $3^L$, because the indicated positions occupy disjoint parts of the interval of length $L$.

Apply Evertse's sum theorem with $S=\{\infty,2,3\}$ and $T=\{2\}$ to (1), as in [the all-odd proof](MACROSCOPIC_ODD_MASS.md). The root term has dyadic norm $2^{-\ell_1}$. For $d\ge2$ this yields
$$
 \sum_{i\le d}\ell_i\le B_1+c\sum_{i<d}s_i
 +C d\sum_{i\le d}D_i+\sum_{i<d}R_i
 +\epsilon\left(B_1+\gamma L+C d\sum_{i\le d}D_i+\max_{i<d}R_i+C\right)+K_{d,\epsilon}.
 \tag{2}
$$
At $d=1$ one has directly $\ell_1\le B_1+D_1$ from the nonzero integer numerator of $x_{a_1}-\rho_1$. This also implies $\ell_i=O(B_i)$ for all sufficiently large selected indices under $D_i=o(\ell_i)$. [Evertse, *Compositio Mathematica* 53 (1984), printed p. 228, Theorem 2](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf).

## 3. Summation and the two constants

For fixed $m>1/\delta$, carry out exactly the $m$ shifted partitions into blocks with at most $m$ intervals in [the mass proof](MACROSCOPIC_ODD_MASS.md). For every partition the spans of its blocks are disjoint before $a_j$. Let $G_j=\sum_{i\le j}\ell_i=O(a_j)$: earlier intervals are disjoint, while $\ell_j=O(B_j)$ and $B_j\le B_0+c a_j$. The initial bit-length cost over all partitions is at most $G_j/\delta+O_m(1)$. Finite-$m$ sums of the $D_i$ costs are $o_m(a_j)$ because $D_i=o(\ell_i)$. The additive constants are $o_m(a_j)$ because $\ell_i\ge\delta B_i\to\infty$.

If $R_i=o(\ell_i)$ their cost is also $o_m(a_j)$. Letting $\epsilon$ decrease after the time limit, we obtain $(m-1/\delta)G_j\le c(m-1)U(a_j)+o_m(a_j)$. In the general case, the elementary estimate $1+|T^k(\rho)|\le(3/2)^k(1+|\rho|)$ holds also for negative rational states. Thus $R_i\le c\ell_i+D_i+O(1)$. Each $R_i$ from the term outside the $\epsilon$ bracket occurs at most $m-1$ times: a gap is absent precisely when a cut separates its two intervals. This yields $[m-1/\delta-c(m-1)]G_j\le c(m-1)U(a_j)+o_m(a_j)$. The $\epsilon$-weighted height terms are absorbed by taking $\epsilon\downarrow0$ for each fixed $m$. Take $m$ large enough that the coefficient on $G_j$ is positive.

At any $a_j\le t<a_{j+1}$ the total matched time is at most $G_j$ and $U(t)\ge U(a_j)$. Now divide by $m$ and let $m$ increase after the time limit, obtaining the two stated $o(t)$ inequalities. Since $U(t)\le t-M(t)$, the time proportions follow. In the terminal small-height case the total odd count is at most $M(t)+U(t)\le\gamma U(t)+o(t)$ and at least $t/\gamma-o(t)$ by the shifted log identity. This gives the final lower bound.

A next step would have to handle long agreement words whose cheapest rational descriptions have height exponential in their length, or show how a given divergent orbit would be covered by admissible intervals beyond the proved proportion. Deterministic computability of an orbit supplies no such rational-height estimate.

## 4. What the intervening gaps must pay

For a binary gap word $G$ write
$$
 V(G)=\max_{S\ {\rm suffix\ of}\ G}\{\gamma\,\#1(S)-|S|\},
$$
including the empty suffix. Every branch multiplier of a suffix is at most $2^{V(G)}$. Unrolling each odd step's additive $1/2$ yields
$$
 |F_i|/2^{r_i}\le(r_i+2)(1+|\sigma_i|)(1+|\rho_{i+1}|)\,2^{V(G_i)}.
$$
Thus the term $c\sum s_i$ in (2) may instead be $\sum_i(V(G_i)+\log_2(r_i+2))$; the old absolute-height bound still suffices for the $\epsilon$ term. Over the first $j-1$ gaps, $\sum\log_2(r_i+2)\le j\log_2(2+a_j/j)=o(a_j)$ by concavity and $j=o(a_j)$. A nonempty suffix with $u$ odd runs contains at least $u-1$ zeros. Its score is at most $c(\#1-u+1)$ when $u\ge1$, since $c<1$. Thus $V(G)\le c(1+\#11(G))$, where $\#11$ counts overlapping adjacent odd pairs wholly inside the gap. The preceding two mass inequalities hold with $U(t)$ replaced by the number of adjacent odd pairs wholly in the complementary gaps before $t$. In particular, in the bounded-terminal regime every unit of matched time requires at least $1/c$ units of uncompensated adjacent-odd growth in the gaps, asymptotically up to $o(t)$. The longest-rise-groups literature in the all-odd case uses this finer rise count. [rStation paper 174](https://rstation.ai/problems/collatz/papers/174/v1).

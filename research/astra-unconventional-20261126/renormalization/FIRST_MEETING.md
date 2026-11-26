# Exact cost of a smaller visitor to an all-odd ascent

**PROPOSED.** The minimum number of odd steps on a competing positive trajectory is determined exactly by a shortest path in the *negative* integer Collatz graph. The lower bound holds at the supplied source, without assumptions on its convergence, the visitor's clock or its parity word. Sharpness varies the cofactor of the positive source. The theorem does not force a smaller competitor to exist for every cofactor.

Use the positive shortcut $T(2n)=n, T(2n+1)=3n+2$ and on signed integers the same two branches. On positive magnitudes the negative map is $T_-(2n)=n, T_-(2n+1)=3n+1$. Count an odd input as one odd step.

For $r\ge1$, let $L(r)$ be the minimum shortcut clock of a trajectory with exactly $r$ odd inputs ending at $-2$. Its source must be a negative integer. This minimum can be computed by breadth-first search in the inverse tree. It is finite. From a positive magnitude $u$ coprime to three choose $e\ge1$ so $2^eu+1$ is $3$ or $6\bmod9$. For $u\bmod9=1,2,4,5,7,8$ take $e=1,4,3,2,1,2$ respectively. The integer $(2^eu+1)/3$ is another odd positive unit with a path containing one odd step to $u$. Start at $u=2$ and repeat. This gives $L(r)\le4r$. Put
$$
 K(r)=\min\{k\ge0:3^k>2^{k+L(r)+1-r}\}.
$$

**Theorem.** Fix any positive $a$ and $x=2^ra-1$. Its first $r$ inputs are odd and its endpoint is $y=3^ra-1$. Suppose $1\le w<x$ visits $y$, entering along the edge different from the native final edge. Count odd steps up to that visit. The count is at least $r+K(r)$. This applies in particular if the minimum native clock of any intersection of the two full forward orbits is $r$, taking the visitor's first arrival at $y$. For **each** $r$, infinitely many $a$ attain the bound, even when $y$ is a power of two and the first intersected site on the entire native trajectory in native-clock order is $y$. Finally
$$
                      r+K(r)-2r\longrightarrow+\infty .
$$

## Lower bound on one actual ordinary word

The native predecessor is odd. A different predecessor is necessarily $2y$, because there is at most one odd predecessor. A visitor starting at $y$ is impossible as $y>x$. The final edge is even, so it suffices to count the visitor's odd steps before reaching
$$
                         U=2\cdot3^r a-2 .
$$
Run this physical word backwards. The inverse letters are $E(v)=2v$ and $O(v)=(2v-1)/3$, the latter requiring $v=2\bmod3$. Through the first $q\le r$ odd inverse letters, the identical inverse word is legal at $-2$. Indeed the two initial values differ by $2a3^r$; after $S$ inverse clocks their difference is $2^{S+1}a3^{r-q}$, and the difference before a required odd inverse is divisible by three. Write the resulting signed endpoint as $-s$. Its magnitude is at least two, since $-1$ is fixed forward and cannot reach $-2$. Each even inverse doubles the magnitude. An odd inverse sends $b\ge1$ to $(2b+1)/3\le b$. Consequently the actual ordinary endpoint of this backward segment is
$$
                     b=2^{S+1}a3^{r-q}-s,\qquad
                     2\le s\le2^{S-q+1}.                       \tag{1}
$$
If the entire visitor had $q\le r$ odd steps, this gives
$w\ge2^{S-q+1}(2^q3^{r-q}a-1)\ge2(2^ra-1)>w$.
Thus the backward word reaches its $r$-th odd inverse. Stop just there. Let $S$ be the clock and let $k$ count all subsequent odd inverses. Then $S\ge L(r)$ and
$$
 b+1\ge2^{S+1-r}(2^ra-1)+1>2^{S+1-r}(w+1).
$$
Here $w+1\le x$ uses strict smaller-source height. On positive integers an inverse odd step multiplies shifted height $v+1$ exactly by $2/3$, while an inverse even step increases it. Hence $b+1\le(3/2)^k(w+1)$. This gives the strict inequality in the definition of $K(r)$, for the actual supplied visitor.

## Attainment with genuine convergent sources

Choose one shortest signed inverse word from $-2$ with $r$ odd letters, clock $S=L(r)$, ending at $-s$. Use this word at $U$ to reach $b=2^{S+1}a-s$. To continue with $k=K(r)$ consecutive odd inverses it suffices to choose
$$
                     2^{S+1}a\equiv s-1\pmod {3^k}.
$$
Then $d=(b+1)/3^k$ is an integer and $w=2^k d-1$ follows $k$ odd steps to $b$. These steps do not require $d$ to be odd. Completing the signed word forward from $b$ visits $U$, then one even step visits $y$. The visitor uses $r+k$ odds. The leading coefficient of $w+1$ as a function of $a$ is $2^{k+S+1}/3^k<2^r$, so all sufficiently large such $a$ give $0<w<x$.

One may insist that $y=2^H$. Prescribe the indicated residue $a_0\bmod3^k$, and solve $2^H\equiv3^ra_0-1\pmod {3^{r+k}}$. Its right side is a unit and powers of 2 generate this unit group. For completeness $v_3(4^{3^t}-1)=t+1$ by cubing and retaining the first nonzero ternary digit, so the order of 2 modulo $3^m$ is $2\cdot3^{m-1}$. Add multiples of the order to $H$ and set $a=(2^H+1)/3^r$.

Take $H>1$. The apex $2^H$ never visits itself again, since it decreases by halvings to the cycle through one. The constructed word therefore reaches it for the first time on its prescribed even edge. A prior visit to an earlier native site would reach the apex on its native odd edge, because the native prefix is strictly increasing. After the apex all visited sites are powers of two, while every earlier native site is odd and greater than one. This proves the minimum-native-clock assertion.

## A complete test at a supplied cofactor

Let $\mathcal S_r$ be the set of positive magnitudes of the starting points of all signed words of length $L(r)$ with $r$ odds ending at $-2$. These words are determined by their starting points. For **each** given $a\ge1$, a smaller visitor attaining the optimal cost on the other edge exists if and only if
$$
      2^{L(r)+1}a\equiv s-1\pmod {3^{K(r)}}\quad
      \text{for some }s\in\mathcal S_r .                           \tag{3}
$$
To prove necessity, apply the backward cut above and keep the number $d$ of evens after that cut. Each positive even inverse multiplies shifted height by at least $3/2$. Therefore
$$
        2^{S+1-r} < (3/2)^{k-d}.
$$
The right side exceeds one, so $k>d$. Since $S\ge L(r)$, the least-cost case $k=K(r)$ forces $d=0$. Also $(3/2)^{K(r)}\le(3/2)2^{L(r)+1-r}$ by minimality. A single extra signed clock $S\ge L(r)+1$ would require a factor two. Hence $S=L(r)$, all remaining inverses are odd, and (3) follows from their integrality. Conversely choose a matching $s$ and take that signed word and the all-odd continuation. For every positive $a$ the lifted signed endpoint $b=2^{L(r)+1}a-s$ is positive by (1), so the congruence gives a positive quotient $(b+1)/3^{K(r)}$. The resulting $w$ is positive and $w+1<2^ra$ by the strict leading-coefficient inequality and $s\ge2$.

All $s$ satisfy $2\le s\le2^{L(r)+1-r}<3^{K(r)}/2^{K(r)}$. They give disjoint cofactor residue classes. The frequency of attaining the optimum is exactly $|\mathcal S_r|/3^{K(r)}<2^{-K(r)}$. An input outside these classes must pay at least one more odd if it has any visitor on the other edge. The fixed-input test concerns a specified arrival edge. A power-of-two apex as above gives the additional conclusion about the entire future orbit; that extra conclusion is not asserted at arbitrary $a$.

## The extra cost goes to infinity

Every signed prefix ending at $-2$ is simple. A repetition would place its terminal on a cycle, while the signed path from $-2$ is $-2,-1,-1,\ldots$. There is an absolute $C_0$ with
$$
                  \sum_{v\text{ departed in a simple }T_-\text{ path}}1/v\le C_0
$$
for positive magnitudes. Here is the proof for this map. At height $X\ge2$, set $h=\lfloor\log_2 X\rfloor$. Omit the last $h$ positions. Among earlier departed values at most $X$, the first $h$ parity bits specify one residue modulo $2^h$, by the odd leading coefficient in the usual affine map for either affine correction sign. Each word therefore accounts for at most two distinct values up to $X$. The number of words with more than $3h/5$ odds is $O(2^{H_2(3/5)h})$, with $H_2(3/5)<1$, by the binomial entropy bound. Every other position has $h$-step endpoint at most $X3^{3h/5}/2^h=O(X^{(3/5)\log_2 3})$, since the minus update has nonpositive affine correction. These endpoints are distinct. The omitted last $h$ positions add at most $h=O(\log X)$ sites. Both exponents are less than one, so the total number of sites up to $X$ is $O(X^{1-\delta})$ for an absolute $\delta>0$, uniformly in the path. Summing over dyadic annuli proves the reciprocal bound.

Telescoping a word from magnitude $s$ to 2 gives
$$
             2^{S}\,2=3^r s
             \prod_{v\text{ odd departure}}(1-1/(3v))
             \ge c_0 3^r s,                                   \tag{2}
$$
for an absolute $c_0>0$, using the uniform reciprocal bound and $v\ge2$. Take a shortest word for each $r$. Its source magnitude $s_r$ goes to infinity. Each fixed positive magnitude has at most one visit to 2, so it can supply only one odd count to that terminal. Thus $L(r)-r\log_2 3\to+\infty$. Inserting this in the definition of $K(r)$ proves the divergence above. No termination claim for the general negative map is required.

The kernel proves the lower bound and existence of an attaining smaller ordinary visitor at arbitrarily large cofactors for every $r$. The power-of-two-apex strengthening, supplied-cofactor equivalence and frequency, and limiting excess have written proofs. [Signed lift and matched word](AscentMerger.lean) · [unconditional optimization](ExactOptimum.lean)

Weaver's [Paper 230, §§2–4](https://rstation.ai/problems/collatz/papers/230) gives a closely related exact threshold and frequency under a different test. It allows visitors that entered the original ascent at an earlier site and treats a specified postpeak window on inputs with $3^D\mid(2^hu-1)$. Its optimization pairs positive and negative trajectories at the extra depth $D$. The signed root $-2$ here comes from requiring the other edge into the specified crest itself. [Paper 180, §2](https://rstation.ai/problems/collatz/papers/180/v1) uses copied words from negative centers to bound signed work. [Paper 219, §5](https://rstation.ai/problems/collatz/papers/219/v1) forces the other incoming even edge for first-step visitors at odd multiples of three. [Paper 222, §§3,7](https://rstation.ai/problems/collatz/papers/222) gives sharp visitor counts at first octave exits and later returns on specified families. The threshold pattern, signed comparisons and forced-edge observation all have these antecedents.

The argument adapting the simple-path occupation count uses the same parity split as [round twelve for the positive map](../../astra-global-closure-20261124/round12/arithmetic/README.md). Weaver's [Paper 178/v1, §§2,7,8](https://rstation.ai/problems/collatz/papers/178/v1) gives all-depth density laws for protected sources and uses a sharp cycle product on inverse branches of the negative-five cycle. It does not supply a pointwise source selector here. Its [Paper 148 reference](https://rstation.ai/problems/collatz/papers/148/v1) concerns matched or shallower accelerated odd depth. [PR192's inverse envelope](https://github.com/GettysburgResearch/collatz/blob/0e313e2cd42cfce1275dbef6129ac13e9a49abd5/research/astra-literature-closure-20261125/carry/README.md) excludes visits with insufficient odd budget into a native ascent. The all-word optimizer above counts the further odds needed after available ternary precision has been spent.

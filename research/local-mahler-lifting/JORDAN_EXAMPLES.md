# Explicit parity words beyond the two-component Jordan class

**Proposed consequence of the [exponential-substitution theorem](EXPONENTIAL_MORPHIC.md).** For every $h\ge2$ take letters $A_0,\ldots,A_h$, substitute
$$
 A_i\longmapsto A_i A_i A_{i+1}\quad(i<h),\qquad A_h\longmapsto A_h A_h,
$$
and start at $A_0$. Code $A_0$ by zero and all the other letters by one. No positive rational 2-adic integer realizes the resulting parity word, including after finite modification of a prefix.

The row incidence matrix is $2I+J$ with $J$ the nilpotent upper shift. In the $j$th seed image there are exactly $\binom ji2^{j-i}$ copies of $A_i$ for $0\le i\le\min(j,h)$. Its length is therefore comparable to $(1+j)^h2^j$ and its zero count equals $2^j$. Consecutive complete lengths have bounded ratio and each is a prefix of the infinite word. The zero count through arbitrary $N$ letters consequently satisfies
$$
 Z(N)\asymp_h N/(1+\log N)^h.
$$
The word has infinitely many zeros and zero frequency, hence is not eventually periodic. The proposed theorem would force periodicity of any positive rational orbit realizing it, which is impossible.

This count separates the actual word from each coding class in rStation paper 16, even if one seeks a different generating presentation. In the semisimple-peripheral class the paper proves that zero-frequency indicator counts are $O(N^{1-\delta})$ for some $\delta>0$, covering also uniform substitutions. A primitive coding with any zero has bounded gaps and positive lower frequency. Finally in its coupled two-component class with positive irreducible diagonal block, a lower letter coded zero gives positive frequency. If zeros occur only on some upper letters, positivity of the block and the complete seed prefix give $Z(N)\asymp N/\log N$ (the chosen nonempty subset has a fixed positive share of all upper letters in every sufficiently long complete seed image). The only other case has no zeros. None matches the displayed rate for $h\ge2$. [Paper 16 v3, Sections 19 and 20.6](https://rstation.ai/problems/collatz/papers/16/v3)

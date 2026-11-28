# Quantitative first-landing reserve up to the mean-two boundary

Let $0<\epsilon\le1$, $\tau=2-\epsilon$, and
\[
                    K_\epsilon=C\epsilon^{-1}\log(2/\epsilon)
\]
for a sufficiently large absolute $C$. For every $M\ge a\ge1$ with $a$ a positive odd ternary unit, and $X/M\ge\exp(C'K_\epsilon)$, at least
\[
                         e^{-C'K_\epsilon}\,X/M                     \tag{1}
\]
odd integers in $(X/4,X]$ first hit an odd integer at or below $M$ at the specified $a$. For each such source, read its actual odd gaps in reverse chronological order from $a$. At every positive prefix length $j$ of this reversed path,
\[
                         S_j-\tau j>\log_2(M/a).                      \tag{2}
\]
Its path has $O(1+\log X)$ shortcut steps with an absolute implied constant. A source satisfying (2) fails the forward $\tau$ gate at every earlier odd position, on the suffix through $a$. Therefore whenever $a$ is permanently passing, each counted source has its first permanent landing precisely at $a$.

For a nonperiodic target, let $d_a$ be its relative natural predecessor density on odd integers and $Q_a$ the natural reverse entrance law at this target. Then
\[
                d_a Q_a(S_j-\tau j>0\text{ for every }j\ge1)
                      \ \ge\ e^{-C''K_\epsilon}/a.                    \tag{3}
\]
This assertion uses fixed-depth conditional limits for $Q_a$. It requires no rate of convergence for a global first-permanent-label law at slopes near two. The [fixed $7/4$ proof](../mass/NO_RETURN_LANDING_FLOOR.md) directly uses the original selected block set. Here extra partial-sum constraints are imposed within every selected block and within the final free segment.

## Refined fixed-total floor

For iid positive gaps of mass $2^{-e}$ write $S_j$ for their prefix total. The source statements used here are Weaver, Paper 12, Appendix A, equations (51)–(60), and Weaver and Wren, Paper 48 v2, equations (70)–(79). The original complete blocks have lengths $b_i$, grow between factors $1.005$ and $1.01$, and have total within $\lceil b_i^{3/5}\rceil$ of $2b_i$. The normalized selected-word subdensity at the final fixed total uses full blocks followed by a free tail $t_j<2b_j$, with $n<202b_j$. The new selection retains a lower floor at exactly the same central totals $|s-2n|\le2\sqrt n$ and admissible extra depths $0\le q\le\delta n$, on a possibly different fixed favorable cylinder. It retains the real-offset bound of the original. [Weaver, Paper 12 v1, Appendix A](https://rstation.ai/problems/collatz/papers/12/v1) · [Weaver and Wren, Paper 48 v2, §9](https://rstation.ai/problems/collatz/papers/48/v2).

Set $L_i=A\sqrt{b_i\log(2b_i)}$ with a fixed large $A$. Keep an original complete block only if all its partial totals obey $|S_u-2u|\le L_i$. Impose that same bound with $L_j$ on the final free segment of length $t_j\le 2b_j$. For sums up to length $2b_i$ the probability of failing this additional bound is $O(b_i^{-10})$ with $A$ sufficiently large. Indeed $\log \mathbb E e^{v(e-2)}\le C_1v^2$ for $|v|\le c_1$. Applying the exponential martingale maximal inequality at a positive and a negative $v$ gives $2\exp[-c\min(L_i^2/b_i,L_i)]$. Finite initial indices can be accommodated by increasing $A$.

Here is the verification that the refined selection preserves the floor. Write $\Gamma_i'$ for the concatenations of the new complete blocks. They form subfamilies of the old $\Gamma_i$ and inherit the multiplier, offset, and count of distinct total estimates in (51). Each individual new complete selection has positive probability, since the constant-two word qualifies. The product of these probabilities over $i$ is positive, since the old per-block rejection is $O(e^{-c b_i^{1/5}})$ and the added loss is summable. Denote this positive product by $p'$.

In (56), use $\Gamma_i'$ on the right and the new complete selection in $h_i$. The composition identity is unchanged and (52) applies to the subfamily. The actual rejection in (57) depends on the first $b_i$ independent letters. The suffix of $t_i-b_i$ letters has length at least $n/1616$. Its maximal total probability is $O(n^{-1/2})$. Consequently the new rejection contribution summed over the distinct remaining totals is at most
\[
 C(1+i b_i^{3/5}) n^{-1/2}
        (e^{-c b_i^{1/5}}+b_i^{-10}).
\]
The unselected oscillation term in (57) is unchanged. After division by the final central-slice probability $\pi_n(s)\gg n^{-1/2}$, the errors in (59) remain summable, uniformly over the stated central totals. At any fixed base $i$, the new family is finite. The same negative-binomial ratio limit gives $G'_i/\pi_n(s)\to g'_i$ uniformly on the central window. Its normalized mean on units is at least $p'$: integration of the selected subdensity gives precisely the probability of the selected prefix family in the unconditional fixed-base limit. Choose the base so that all later summed increment errors are $<p'/8$, and pick a unit where $g'_i\ge p'$. This selects a fixed favorable cylinder independent of all final parameters.

At the final stage, compare the provisional $G'_j$ to the expression (79) with $\Gamma'_j$. The same averaged extra-depth oscillation bound applies by positivity and (72), since the selected prefixes are a subfamily. After additionally clamping the final free tail, the further **unnormalized** pointwise loss is at most $C b_j^{-10}$: in (72) the distinct remaining total slices are disjoint in the sum of their means, so their total rejected mass is bounded by $\Pr(\max_{u\le2b_j}|S_u-2u|>L_j)$. After division by $\pi_n(s)$ this costs $O(\sqrt n\,b_j^{-10})=o(1)$. The optional individual-letter cap of (76) is unnecessary here. All retained words already obey the real-offset bound from (70) and (79). These estimates give a lower bound $c\pi_n(s)$ on the refined normalized density on the selected cylinder, with absolute constants. The residue, exact prescribed total, and extra-depth claims are identical to (76).

For every prefix $t$ of any word so retained we have
\[
                    |S_t-2t|\le C\sqrt{(t+1)\log(t+2)}.             \tag{4}
\]
At a positive block boundary this follows by summing the complete bounds $L_i$ backwards as a geometric series. In a partial block add at most its own $L_i$; for $i\ge1$ its predecessor already contributes $b_{i-1}\ge b_i/1.01$ letters to $t$. The finite initial block can be covered by enlarging the absolute $C$ because its own $L_0$ is fixed. This also covers the last free segment.

Estimate (4) gives $S_t-\tau t\ge-K_\epsilon$ for every prefix. For example split the supremum of $C\sqrt{(t+1)\log(t+2)}-\epsilon t$ at $t=D\epsilon^{-2}\log(2/\epsilon)$ with a large absolute $D$. Above this threshold $\log(t+2)/(t+1)$ is decreasing and the square-root term is at most $\epsilon t$. Below it the term is $O(\epsilon^{-1}\log(2/\epsilon))$. This is a deterministic bound on the selected physical words.

## Ordinary first passage and the infinite natural law

Choose a first inverse bridge $a\leftarrow w=(2^e a-1)/3$ into that fixed favorable cylinder with
\[
 \log_2(M/a)+K_\epsilon+C_2\le e
       <\log_2(M/a)+K_\epsilon+C_3 .
\]
The fixed absolute $C_3-C_2$ accommodates an entire period of the powers of two modulo $3^{h+1}$ for the cylinder depth $h$. Increase $C_2$ so that $w$ exceeds $M$ times the fixed multiplier and offset bounds with room to spare. Then all intermediate physical odd states in the refined word stay above $M$, and the first gap plus every subsequent partial total has the strict reserve (2). We have $w\asymp2^{K_\epsilon}M$ with absolute constants.

For completeness put $L=\log_2(X/w)$, $\lambda=2-\log_2 3$, take the $\gg\sqrt L$ successive odd-map depths $|b-L/\lambda|\le c\sqrt L$, and set $s_b=\lfloor L+b\log_2 3\rfloor$. These totals all meet $|s_b-2b|\le2\sqrt b$ for small absolute $c$ and large $L$. At each fixed depth the refined floor supplies $\gg (2^{s_b}/3^b)/\sqrt b\gg X/(w\sqrt L)$ physical ancestors. One may require a terminal unit by taking extra depth one and the target offset residue $w-3^b2^{-s_b}\bmod3^{b+1}$, with only a constant loss. Every endpoint $x$ is $2^{s_b}3^{-b}(w-B_b)$ and $B_b\le F$ for a fixed $F$, giving $X/4<x\le X$ after the bridge enlargement. Every intermediate height is $(w-B_i)/A_i$ where $A_i=3^i2^{-S_i}\le3F$. This proves its strict height reserve. Distinct depths give distinct first odd landings by their different actual clocks; this holds even for periodic $a$. The existence of a large enough absolute $L$ follows from the stated lower bound on $X/M$. Summing proves (1). Also $e+s_b\ll1+\log X$.

With $M=a$, fix any natural reverse depth $m$. For fixed $m,a$, the number through $X$ hitting $a$ within fewer than $m$ odd steps is $O_{m,a}((1+\log X)^m)$, since the total of a path of each such depth is $O_{m,a}(1+\log X)$ by $2^S a\le4^m x$. Removing these from (1) still gives a relative lower density $\gg e^{-C'K_\epsilon}/a$ of odd sources whose reversed path satisfies (2) at least through depth $m$. At a nonperiodic root, the conditional fixed-depth natural entrance distribution converges in total variation to $Q_a$ on this partition. Divide by $d_a$, then let $m\to\infty$ by continuity from above. This proves (3). [Canonical inverse paths at repository commit aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

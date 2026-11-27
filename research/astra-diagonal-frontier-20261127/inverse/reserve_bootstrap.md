# Building a reverse reserve up to the mean-two boundary

Let $U$ be the accelerated odd Collatz map. A reverse word from $a$ lists positive gaps $e_1,e_2,\ldots$ outward along ordinary integer predecessors. Write $S_j=e_1+\cdots+e_j$. There are absolute $c,C>0$ such that, for $0<\epsilon\le1$, every positive odd ternary unit $a$, and every $M\ge a$, set
\[
       H=\log(2/\epsilon),\qquad \tau=2-\epsilon .
\]
If $\log(X/M)\ge C\epsilon^{-2}H^2$, at least
\[
                   c\exp(-C H^{3/2})\,X/M                         \tag{1}
\]
positive odd unit sources in $(X/4,X]$ make their first odd landing at or below $M$ at $a$. At every positive prefix length $j$ of the actual reversed route from $a$ to each counted source,
\[
                     S_j-\tau j>\log_2(M/a).                        \tag{2}
\]
Their routes use $O(1+\log X)$ shortcut steps. In particular for nonperiodic $a$, with relative natural predecessor density $d_a$ and natural reverse entrance law $Q_a$,
\[
       d_a Q_a\{S_j>(2-\epsilon)j\ \hbox{for all }j\ge1\}
                    \ge c\exp(-C H^{3/2})/a.                      \tag{3}
\]
The proof accumulates the initial reserve on the true inverse tree. The earlier estimate used one prescribed long initial gap and gave $\exp(-C\epsilon^{-1}H)/a$, with a smaller finite-height onset. Both estimates use the same source-qualified selected-word inputs. [All-slope selected-word floor](all_slope_no_return.md) · [Weaver, Paper 12 v1, Appendix A, equations (51)–(60)](https://rstation.ai/problems/collatz/papers/12/v1) · [Weaver and Wren, Paper 48 v2, Lemma 7, equations (72)–(79)](https://rstation.ai/problems/collatz/papers/48/v2).

## A positive shell with controlled internal loss

There are absolute $b_0,C_0>0$ and $0<p_0<1$ with the following property at every supplied positive odd unit $y$ and every $b\ge b_0$. A family of actual inverse words $w$ of common length $b$ from $y$, with unit terminal states, satisfies
\[
\begin{gathered}
  \sqrt b\le S_b(w)-2b\le2\sqrt b,\qquad
  S_i(w)-2i\ge-C_0\sqrt{(b+1)\log(b+2)}
       \quad(1\le i\le b),\\
                       \sum_w3^b2^{-S_b(w)}\ge p_0.                \tag{4}
\end{gathered}
\]
To see this, prepend a bounded positive legal exponent from $y$ into the favorable unit cylinder of the refined fixed-total floor. Use a representative large enough that its ordinary output exceeds $4F+4$, where $F$ bounds the retained real offsets. This is possible at every $y$, including $y=1$, by adding a bounded number of full unit periods at the fixed ternary depth. For every integer $s\in[2b+\sqrt b,2b+\tfrac32\sqrt b]$, the remaining total at length $b-1$ is within $2\sqrt{b-1}$ of its mean for all sufficiently large $b$. Prescribe one extra ternary digit to make the terminal state $1$ modulo three. The refined floor gives $\gg 2^s/(3^b\sqrt b)$ physical words for each of the $\gg\sqrt b$ totals. Its deterministic within-word discrepancy bound is $C\sqrt{(i+1)\log(i+2)}$ at every prefix. Absorb the bounded initial exponent into $C_0$ and sum over totals with weight $3^b2^{-s}$. This uses the refined selected subfamily itself. It requires no subtraction of an unconditioned exceptional probability at one supplied residue.

## Accumulating reserve at common depths

It suffices to treat $\epsilon\le1/8$. The resulting assertion at $1/8$ implies the larger-$\epsilon$ cases by monotonicity, after absolute changes of constants in the onset and the lower bound. Write $L=\log_2(M/a)$. Choose a large absolute $A$. Whenever a reverse path satisfies
\[
                    S_j-\tau j\ge L+A\qquad(j\ge1),               \tag{5}
\]
all the corresponding ordinary sites are strictly above $M$. Indeed, putting
\[
       B_j=\sum_{i=1}^j3^{i-1}2^{-S_i},\qquad
       x_j=2^{S_j}3^{-j}(a-B_j),
\]
gives $B_j\le 2^{-L-A}\sum_{i\ge1}3^{i-1}2^{-15i/8}<a/2$ for $A$ sufficiently large. Then $x_j\ge(M/2)2^A(2^{15/8}/3)^j>M$. This proves the strict height condition from the entire actual reserve, including the small root $a=1$.

Take an absolute $R_0$ sufficiently large. Choose one legal exponent at $a$ in $[L+A+R_0+2,L+A+R_0+C_1]$ with unit output. A complete period modulo $9$ suffices. Its reserve above $L+A$ is at least $R_0$, its weight is $3\cdot2^{-e_1}\gg a/M$, and it uses the same single edge for all later words.

Choose a small absolute $\eta>0$. At deterministic reserve $R\ge R_0$ define
\[
 b(R)=\left\lfloor\frac{\eta R^2}{\log R}\right\rfloor,\qquad
 R'=R+\sqrt{b(R)} .
\]
By choosing $\eta$ small and then $R_0$ large, $b(R)\ge b_0$ and $C_0\sqrt{(b(R)+1)\log(b(R)+2)}\le R/2$ for every such $R$. Apply (4) at every retained terminal state. Throughout each new block the total reserve above $L+A$ remains positive, and at its end it is at least $R'$. The term $\epsilon i$ only increases these lower bounds. Every branch uses precisely the same successive block lengths, determined from the lower reserves and independent of the realized overshoots.

Let $K=C_2\epsilon^{-1}H$ be large enough to bound the loss of the entire final selected word relative to slope $\tau$. This is the deterministic estimate following equation (4) of the all-slope floor. Stop the bootstrap at the first $R_m\ge K+C_3$, for a sufficiently large absolute $C_3$. The number of stages is $m\le C H^{3/2}$. In fact $\sqrt{b(R)}\asymp R/\sqrt{\log R}$, so $(\log R')^{3/2}-(\log R)^{3/2}$ has a positive lower bound. The final reserve is $O(K+R_0)$. The total common number of bootstrap gaps is $N=1+\sum b(R_i)\ll 1+K^2$, since $b(R_i)\le C R_i(R_{i+1}-R_i)$ and the resulting sum is bounded by a constant times $R_m^2$. Each completed block has total at most $3b(R_i)$. Thus every terminal $y$ has $\log(y/M)\ll1+K^2$ by the exact affine formula.

At depth $N$, no merging can occur among different gap words, because from the terminal ordinary state the forward word of fixed length is determined. Most importantly the reciprocal heights retain the product of the unnormalized shell masses:
\[
 \sum_{y}\frac1y
 \ \ge\ \frac1a\sum_{w}\frac{3^N}{2^{S_N(w)}}
 \ \ge\ \frac{c}{M}p_0^m.                                         \tag{6}
\]
This follows by iterating (4) on the ordinary tree. One does not multiply a separate canonical trace denominator at each stage.

## Finishing on the prescribed octave

From each retained $y$ choose a bounded legal gap into the refined favorable cylinder, increasing it by a bounded number of full periods when necessary so that the new state $z$ exceeds $4F+4$, where $F$ bounds the real offsets of the final selected family. All these $z$ satisfy $z\asymp y$ uniformly. One extra gap can consume at most one unit of relative reserve. For the final selected words the maximum possible prefix loss is at most $K$. By (5), the entire route after the original $a$ therefore stays strictly above $M$ and satisfies (2). The finite-height onset with a sufficiently large constant guarantees $\log(X/z)$ exceeds the absolute onset of the final selected count for every bootstrap terminal.

For each $z$ the octave assembly in the all-slope floor uses the $\gg\sqrt{\log(X/z)}$ admissible lengths near $\log_2(X/z)/(2-\log_2 3)$, with one central prescribed gap total per length and a terminal unit digit. It produces $\gg X/z\gg X/y$ true odd unit endpoints in $(X/4,X]$. Different full words from this construction cannot give the same source at different lengths, since its first odd landing at or below $M$ is $a$ and fixes the length. At the same length the forward word fixes every letter, including the common bootstrap prefix read backwards from $a$. This reasoning also handles a periodic $a$. Summing by (6) proves (1). The initial gap is $O(1+\log M)$, bootstrap totals are $O(1+K^2)$, and the final route uses $O(1+\log(X/z))$ further shortcuts. The stated onset gives the claimed clock bound.

Finally set $M=a$ and fix a reverse depth $t$. The number of sources through $X$ hitting $a$ in fewer than $t$ odd steps is $O_{a,t}((1+\log X)^t)$. Removing them preserves the lower density from (1) among odd sources satisfying the first $t$ inequalities. The fixed-depth natural entrance partition at a nonperiodic $a$ converges in total variation to $Q_a$. Divide by $d_a$ and let $t\to\infty$, using continuity from above, to obtain (3). [Canonical ordinary inverse paths, fixed commit aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

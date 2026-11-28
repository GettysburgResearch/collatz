# The low-cost spectrum at the original ternary source

For a ternary unit $x$, write $C_n(x)$ for the smallest total positive gap among legal inverse paths of exactly $n$ odd arrivals, keeping unit states throughout. Let
$$
 H(a)=a\log a-(a-1)\log(a-1),\qquad H(1)=0,
 \qquad H(a_*)=\log3,\qquad D(a)=H(a)/\log3 .
$$
Thus $a_*=1/\theta_*$ is the known geometric entropy ceiling. For every $1\le u\le v\le a_*$ the original-source set
$$
 E(u,v)=\{x:\liminf C_n(x)/n=u,\ \limsup C_n(x)/n=v\}
$$
has the exact dimensions
$$
                  \dim_{\rm H}E(u,v)=D(u),\qquad
                  \dim_{\rm P}E(u,v)=D(v).                         \tag{1}
$$
Its normalized-cost accumulation set is the full interval $[u,v]$. For $1<b<a_*$ and **every** nonnegative $g(n)=o(n)$, each of the following two subsets of $E(b,b)$ still has Hausdorff dimension $D(b)$:
$$
 \{C_n\ge bn+g(n)\text{ eventually}\},\qquad
 \{C_n\le bn-g(n)\text{ eventually}\}.                            \tag{2}
$$
The second assertion also holds at $b=a_*$. In (2) the cheap or expensive comparison is with every candidate inverse word through the minimum $C_n$. The construction supplies actual witnesses for its upper estimates. Section 4 gives an ordinary-integer octave count through depth $\log_3X+O(1)$.

## 1. Counting and separated finite words

A positive gap word $w$ of length $n$ confines all its sources to the single depth-$n$ ternary cylinder $A_w(0)\bmod3^n$, where $A_e(y)=2^{-e}(1+3y)$. Unit terminal legality can impose an additional digit, which only reduces that source set. The number of positive $n$-part compositions of total at most $s$ is $\binom{s}{n}$ for integral $s\ge n$. In particular, for $t\ge1$,
$$
        \#\{\text{$n$-trit source cells needed to cover }C_n\le tn\}
           \le \binom{\lfloor tn\rfloor}{n}\le e^{nH(t)}.          \tag{3}
$$
The last inequality is the usual binomial entropy bound, also immediate from the positive geometric weights. A unit always has a legal gap at most four: in each of the six unit residues modulo nine one of $1,2,3,4$ yields an integral unit. Hence $C_n+1\le C_{n+1}\le C_n+4$. The increments of $C_n/n$ tend uniformly to zero since $n\le C_n\le4n$, giving the accumulation-set assertion.

For the Hausdorff upper bound cover the infinitely many depths with $C_n\le(u+\varepsilon)n$ using (3) and sum diameters to any power greater than $D(u+\varepsilon)$. For the packing upper bound, for each fixed cutoff $N$ the set where $C_n\le(v+\varepsilon)n$ for **all** $n\ge N$ has upper box dimension at most $D(v+\varepsilon)$ by (3). Take the countable union over $N$ and let $\varepsilon\downarrow0$, also imposing the ambient bound one if necessary.

For a slope $1<t\le a_*$ and any $\eta>0$, arbitrarily large block lengths $\ell$ admit a family $\mathcal W$ of positive words such that
$$
 |\mathcal W|\ge e^{(H(t)-\eta)\ell},\quad
 |S(w)/\ell-t|\le\eta\quad(w\in\mathcal W),\quad
     A_w(0)\bmod3^\ell\text{ are pairwise distinct}.               \tag{4}
$$
Draw iid positive geometric gaps of mean $t$. Their ternary source entropy at depth $\ell$ is $H(t)\ell+o(\ell)$ by Leen's entropy dimension theorem. The event of a typical total as in (4) has probability $1-o(1)$ by the strong law. If its projected support has size $M$, splitting by that event bounds the total source entropy by $\log2+\log M+o(1)\ell\log3$, since there are at most $3^\ell$ possible residues. Select one typical representative for each occupied residue. This proves (4), including the endpoint where $H(t)=\log3$. At $t=1$ use the single all-one word. Only finite Shannon entropy dimension is imported; no pointwise upper density estimate is assumed. [Leen, *Tilted 3-adic Syracuse laws*, Theorem C](https://zenodo.org/records/23268832) · [Weaver, geometric entropy dimension, equation (2)](https://rstation.ai/problems/collatz/papers/135/v1).

Choose independent uniform words from a sequence of finite families (4), with the block family at each position specified in advance. Concatenation gives an infinite legal gap code and a ternary source. At any complete block boundary the distinct choices of all completed words give disjoint ternary cylinders at that depth. At the first differing block the source cylinders are distinct by (4); applying the shared preceding affine map increases their matching depth by exactly the length of that prefix. Consequently the mass of any cylinder at an intermediate depth $n$ is at most the reciprocal product of the cardinalities of all blocks completed by $n$. This applies to *every* cylinder, including those outside the support. Any partial block has positive cost at most the total cost of that one block.

## 2. Arbitrary oscillation intervals

Select stages alternating between the slopes $u$ and $v$ (the same value is allowed), approximating their block rates and mean costs with errors tending to zero. Their block lengths $\ell_j$ may be chosen first. Repeat the blocks in stage $j-1$ long enough that the starting time $N_j$ of stage $j$ satisfies $N_j\ge j\ell_j$. Also repeat stage $j$ until its endpoint $T_j$ satisfies $T_j\ge j^2(N_j+1)$. Both requirements are compatible by extending the stage before moving on. All early finitely many depths are immaterial.

For every word choice, the selected path total divided by depth has limsup at most $v$: completed block means are eventually at most $v+o(1)$ and the partial-block cost is $O(\ell_j)=o(n)$. Along low-stage endpoints its mean tends to $u$, while along high-stage endpoints it tends to $v$. The original-source minimum is at most this path's cost at each depth. Globally, every $n$-trit cylinder has mass at most $\exp[-H(u)n+o(n)]$, uniformly in its center, because every late stage has block rate at least $H(u)-o(1)$ and the incomplete length is $o(n)$. At high-stage endpoints it has mass at most $\exp[-H(v)T_j+o(T_j)]$ by the domination of the last stage.

For each $1\le t<u$, (3) and the global bound imply a summable probability of $C_n\le tn$. For each $1\le t<v$, the high-stage bound gives a summable probability of $C_{T_j}\le tT_j$ along the high stages. Thresholds below one are impossible. Applying Borel–Cantelli on countably many thresholds proves that the measure gives full mass to $E(u,v)$. Every positive-mass subset has Hausdorff dimension at least $D(u)$ by the uniform cylinder estimate. Its upper box dimension is at least $D(v)$ because at each high-stage endpoint that subset needs at least its mass times $\exp[H(v)T_j-o(T_j)]$ distinct cells. Every countable cover of a full-measure set contains at least one piece of positive outer measure, to which the same cell-count argument applies. The countable-cover characterization of packing dimension now gives the lower bound $D(v)$. Combined with (3), this proves (1).

## 3. An arbitrary sublinear delay on either side

First fix $1<b<a_*$ and take stage slopes $t_j\downarrow b$ with $b<t_j<a_*$. Choose positive $\epsilon_j\downarrow0$ small enough and the block tolerances in (4) fine enough that every stage's per-letter log cardinality is at least $H(b)+8\epsilon_j$. Also take the block tolerances tending to zero. At the start $N_j$ of each stage $j\ge2$, extend the previous stage as necessary to impose
$$
 (H(b)+2)\ell_j\le\epsilon_j N_j,\qquad
 H'(b)g(n)+3\log(n+1)\le\epsilon_j n\quad(n\ge N_j).
$$
This uses only $g(n)=o(n)$ and the preselected finite lengths. Make $\epsilon_1$ small enough that $8\epsilon_1\le1$. At a depth $n$ in stage $j$, all completed blocks have rate at least $H(b)+8\epsilon_j$. Discard at most $\ell_j$ symbols for the incomplete block. Every cylinder then has mass at most $\exp[-H(b)n-7\epsilon_j n]$ for $j\ge2$. Concavity gives $nH(b+g(n)/n)\le nH(b)+H'(b)g(n)$. With (3) the probability of $C_n\le bn+g(n)$ is summable. Thus $C_n>bn+g(n)$ eventually almost surely. The chosen path mean tends to $b$ uniformly over all choices by the vanishing block slope errors and $\ell_j/n\to0$. The source set has Hausdorff dimension at least $D(b)$ and satisfies $C_n/n\to b$; (1) gives equality.

For the other side take $1<b\le a_*$ and $t_j\uparrow b$ with $1<t_j<b$. Tolerances in (4) may now be chosen so that all complete block means are at most $b-8\epsilon_j$, for some decreasing positive $\epsilon_j\to0$, while the log cardinality rates approach $H(b)$. Extend the previous stage until $(b+2)\ell_j\le\epsilon_j N_j$ and $g(n)\le\epsilon_j n$ for all $n\ge N_j$. All complete blocks in the prefix have mean at most $b-8\epsilon_j$. At most one incomplete block costs at most $(b+1)\ell_j$. This proves that the actual chosen prefix, hence also the minimum, satisfies $C_n\le bn-g(n)$ eventually for every code in the construction. All cylinders have mass $\le\exp[-H(b)n+o(n)]$. Borel–Cantelli with (3) excludes $C_n\le tn$ infinitely often for each $t<b$, so the rate tends to $b$ almost surely and the dimension is $D(b)$. This proves (2). At $u=v=1$, (1) also follows directly from (3) and the fixed source $-1$.

## 4. Positive odd integer sources in each large octave

For either side in (2), there exist a fixed $N_0$ and deterministic $\delta_n\downarrow0$ for which the simultaneous finite conditions
$$
 |C_m(x)/m-b|\le\delta_m\quad(N_0\le m\le n),
$$
together with the corresponding one-sided inequalities in (2) on the whole same range, hold at
$$
          X^{D(b)+o(1)}
$$
positive odd integer units $x\in[X,2X]$ as $X\to\infty$, with $n$ the largest nonnegative integer satisfying $2\cdot3^{n+1}\le X$. To get the lower bound, restrict the relevant measure above to a positive-mass set on which both the eventual inequality and the convergence in (1) hold uniformly (Egoroff). Its depth-$(n+1)$ cells number at least $\exp[H(b)n-o(n)]$ by the uniform cylinder bound. Each cell contains an odd positive representative in $[X,2X]$. Every test through depth $n$ is constant on such cells: legality of a fixed $m$-letter word including unit terminal is determined by the first $m+1$ trits. All the resulting inverse branches of an odd positive representative are ordinary positive odd integers. Different represented cells give distinct sources. For the upper bound use the terminal condition $C_n\le(b+\delta_n)n$ in (3); each depth-$n$ cell contributes $O(1)$ integers in this octave since $X<2\cdot3^{n+2}$. This census concerns long finite properties of the actual input. It gives no assertion that a particular positive integer realizes the prescribed infinite asymptotics.

Theorem 4 of paper 184 already gives the sublevel dimension and two gain behaviors at $b=\log_2 3$, including a logarithmic lower correction for a specific first-descent law. Its critical geometric comparison and the composition cover are direct predecessors. The assertions above allow an arbitrary interval of limiting minima up to the entropy slope and, at interior slopes, prescribed sublinear corrections on both sides. They do not identify the Haar-almost-sure critical endpoint of finite adaptive control. [Weaver, *Full ternary support and singular mass before the first Collatz descent*, Theorem 4](https://rstation.ai/problems/collatz/papers/184).

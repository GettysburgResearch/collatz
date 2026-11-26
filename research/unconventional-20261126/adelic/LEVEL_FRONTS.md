# Which ordinary sources can share one predicted odd count per landing target?

**Status.** Proposed finite-source and ordinary-component theorems. The exact error (3) is unconditional and computable from a finite parity table. Its square-root rate uses the externally reported, unrefereed adjacent counted-synchronization estimate of D. Leen. We specify that input below. The source range is one ordinary octave, and the target set can vary with that octave.

Let $T(n)$ be the positive shortcut map and $p_t(n)$ the number of odd departures before its time $t$. Fix integers $1\le Y<X$, let $A\subseteq[1,Y]\cap\mathbb Z$ be arbitrary, and let $\tau_A(n)$ be the first native time with $T^{\tau_A(n)}n\in A$, allowing infinity. For each $a\in A$ choose an arbitrary set $E_a$ of at most $w$ integers, where $w\ge1$. Then
\[
 \frac{1}{X}\#\{X\le n<2X:\tau_A(n)<\infty,\ p_{\tau_A(n)}(n)\in E_{T^{\tau_A(n)}n}\}
 \ll\frac{w}{\sqrt{1+\log(X/Y)}} .                                      \tag{1}
\]

The constant is absolute under the indicated pair estimate. The sets $E_a$ may be selected using the *whole* actual first-entrance table in this octave. In particular (1) bounds the sum, over landing targets, of their individual largest count atoms in the unconditioned joint source law. Conditioning on a rare target would instead require division by its probability.

For the whole positive graph let $C$ run over its acyclic components. Fix an arbitrary origin of signed odd-count level $b_C$ in each component, so that $b_C(Tn)=b_C(n)+1_{n\text{ odd}}$. This is well-defined because forward rays meet and, in the absence of cycles, an edge relation extends uniquely on the underlying tree. Choose any at most $w$ integer levels $E_C$ in *each* component, allowing all these choices to depend on $X$. Then
\[
 \frac1X\#\{X\le n<2X:n\in C\text{ acyclic},\ b_C(n)\in E_C\}
       \ll\frac{w}{\sqrt{1+\log X}} .                                   \tag{2}
\]
This controls the union over all escaping components at once. Along one hypothetical escaping ray the signed level rises by one per odd step. Large inverse basins can occupy many levels and therefore remain compatible with (2).

## The external synchronization input and its exact finite replacement

Define $Q_h$ as the fraction of residues $r\pmod{2^h}$ such that $r,r+1$ have not met at the *same* shortcut time with the *same* odd count by time $h$. This event can be tested on any integer lifts, including $r=0$ with $T(0)=0$. Indeed a lift by $2^h d$ changes its time-$h$ endpoint by $3^{p_h(r)}d$ and preserves its first $h$ parities. An earlier counted meeting persists through time $h$. Thus equality at time $h$ with equal counts either holds on the whole residue class or nowhere on it. Counting complete periods and the remainder shows that a physical interval of length $N$ contains at most $NQ_h+2^h$ failed adjacent starts.

We use solely $Q_h\ll(h+1)^{-1/2}$ from Leen's preprint. Finite parity coding alone gives the preceding exact identity. The argument below, with no asymptotic synchronization theorem, yields for the left sides of (1) and (2) the bound
\[
                  C w\,(Q_h+2^h/X),                                     \tag{3}
\]
provided $X$ is sufficiently large and, in (1), $(X-10)2^{-h}>Y$. If needed the trivial bound one is available. This packet does not rebuild the external Lean development. The quoted form is the offset-one case of the explicitly stated pair theorem and its exact-cylinder realization. [D. Leen, *Exact rates in Collatz synchronization*, Theorem 2.11](https://doi.org/10.5281/zenodo.23268751) · [D. Leen, *Quantitative synchronization of Collatz trajectories*, Uniform pair absorption](https://doi.org/10.5281/zenodo.23268755) · [source exposition of the input and cylinder transfer](https://rstation.ai/problems/collatz/papers/13/v1) · [physical interval form, equation (18)](https://rstation.ai/problems/collatz/papers/124/v1)

## One rotation couples the whole joint law to its unit translate

For (1) label $n$ by $g(n)=(a,-p_{\tau_A(n)}(n))$ upon a finite first hit at $a$, and by $\partial$ otherwise. For (2) label it $(C,b_C(n))$ on an escaping component and $\partial$ on the others. In both cases let $S$ add one to the integer label, leaving the other coordinate unchanged and fixing $\partial$. Above $Y$, with intermediate halving arguments also above $Y$, one has $g(2n)=g(n)$. At an odd argument $o>Y$ one has $g(3o+1)=Sg(o)$, since $o$ and $3o+1$ reach the identical shortcut state after one departure, odd in the first case and even in the second. In (2) these relations hold at every positive argument. Counted fusion of adjacent starts by time $h$ gives equal labels: in (1), before that time $T^j(v)\ge v/2^j>Y$ at every start $v\ge X-10$ under (3)'s guard, and thus neither path has previously visited any target. From their common state forward both have the identical first visit or both miss. In (2) the component and both accumulated grades agree at the merger. The fusion test itself uses only the first $h$ letters and does not depend on $A$, the choice of surviving components, or a selected target/count table.

Take continuous $u\in[X,2X)$ with law $du/(u\log 2)$. The map $R(u)=3u/2^j$ back into $[X,2X)$, with $j=1$ or $2$, preserves this law. Put $n=\lfloor u\rfloor$, $m=\lfloor R(u)\rfloor$, and $o=n$ if $n$ is odd or $o=n+1$ otherwise. The positive integers $3o+1$ and $2^jm$ differ by at most eight, since both are within four of $3u$. To compare $g(n)$ to $g(m)$ we need only the adjacent edge from $n$ to $o$ and those between $3o+1$ and $2^jm$. All their smaller endpoints lie within ten of $n$ or $3n$ in $[X-10,7X+10]$. A single failed adjacent integer in this range invalidates at most an absolute number of choices of $n$, since $n$ or $3n$ must lie within ten of it. Each floor bin has probability $\le1/(X\log 2)$. The finite residue count therefore bounds the failure probability by $C(Q_h+2^h/X)$. On success,
\[
                 g(m)=g(2^jm)=g(3o+1)=Sg(o)=Sg(n).
\]
All intervening powers of two begin at least at $m\ge X$. The same $u$ couples the law $\mu$ of $g(\lfloor u\rfloor)$ to $S_*\mu$. Thus $\|\mu-S_*\mu\|_{\rm TV}\le C(Q_h+2^h/X)$.

For its masses $v_{a,k}$ on a line of labels $\{a\}\times\mathbb Z$, tending to zero at both ends, $\sum_k|v_{a,k}-v_{a,k-1}|\ge2\sup_k v_{a,k}$. Summing also for countably many rows gives $\sum_a\sup_k v_{a,k}\le\|\mu-S_*\mu\|_{\rm TV}$. The cemetery has identical mass. Each integer in the octave has logarithmic probability at least $1/(2X\log2)$, proving (3) for ordinary counts. In (1) take $h=\lfloor\frac12\log_2(X/Y)\rfloor$ when the ratio is large. Then $2^h/X\le X^{-1/2}$, and the safety guard holds for all sufficiently large ratios. In (2) take $h=\lfloor\frac12\log_2 X\rfloor$. Bounded small parameters are absorbed in the constant. This proves (1) and (2).

## The square-root loss is necessary for unrestricted landing sets

This lower control uses no synchronization estimate. Take $X=2^{L^2},\ Y=2^{L^2-L}$ and $A=[1,Y]\cap\mathbb Z$ for integers $L\to\infty$. For uniform integer $n\in[X,2X)$ the first $H=\lceil2L/D\rceil$ parity digits are exactly independent fair bits by the dyadic word bijection, where $D=1-\tfrac12\log_2 3>0$. Here $H\le L^2$ for large $L$. By the elementary maximal variance inequality, with probability at least $3/4$ one has $|p_t-t/2|\le K\sqrt L$ for every $t\le H$, for an absolute $K$. Until and including first passage, the exact logarithmic expansion gives
\[
 \log_2 T^t n=\log_2 n-Dt+(\log_2 3)(p_t-t/2)+O(H/Y),
\]
since each previous iterate exceeded $Y$. On this event the first passage exists before $H$; comparing against $\log_2Y$ on either side of $L/D\pm C\sqrt L$ places its clock in that interval for a sufficiently large $C$. Its odd count is consequently in a set of $O(\sqrt L)$ integers. Some *one* count accounts for $\gg1/\sqrt L$ of the octave. Taking that same singleton in every $E_a$ attains the order in (1). A universal improvement to little-oh of that order would fail on these genuine positive integer trajectories. No lower bound on a single infinite escaping component is inferred.

Stable-label congruence results, predecessor antichain inequalities, and first-hit laws supply important related estimates. The present observable allows an arbitrary family of landing targets below a moving guard, separately optimizes the count for each target, and places the sum of these maxima inside one ordinary octave. [Related stable-label averaging and attribution](https://rstation.ai/problems/collatz/papers/13/v1) · [fixed-root terminal laws](https://rstation.ai/problems/collatz/papers/175) · [uniform predecessor bounds and harmonic antichains](https://rstation.ai/problems/collatz/papers/10)

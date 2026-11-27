# A width restriction on ordinary Collatz cycles

**Proposed theorem.** Let $N$ be the smallest odd value in a nontrivial positive Collatz cycle. Its largest odd value is strictly greater than $52N/25=2.08N$. The period and the number of local minima can be arbitrary.

The proof uses the small number of possible ordinary paths in this band, a published lower bound for a linear form in two logarithms, and a published period lower bound. The same path count applies to excursions of an escaping orbit up to its first exit. An exit can be upward. A wide nontrivial cycle is also consistent with this theorem.

## Counting actual terminal values

Let $x_0,\ldots,x_k$ be successive odd values in $[N,208N/100]$, with exact gaps $e_j$, and write $S_i=\sum_{j<i}e_j$. Assume $1000k\le N$ and $N>0$. Telescoping the equations $2^{e_j}x_{j+1}=3x_j+1$ gives

$$
  3^i x_0 \le 2^{S_i} x_i \le (1001/1000)3^i x_0 .
$$

Indeed each correction factor is at most $1+1/(3N)$. For $i\le k$, its $i$th power is at most $3N/(3N-i)\le1001/1000$. The first bound follows by induction from $(u+1)^i(u-i)\le u^{i+1}$ for $u\ge i$.

Put $b=\lfloor100x_0/N\rfloor$. There are 109 possible integer bins, $100\le b\le208$. At index $i$, every possible cumulative clock $s$ in bin $b$ belongs to the same set of integer slots

$$
 b3^i\le208\,2^s,\qquad 100000\,2^s\le1001(b+1)3^i .
$$

The ratio of the upper to lower endpoint for $2^s$ is at most $208\cdot1001\cdot101/(100000\cdot100)<40/19$. Thus the set has at most two members, and any pair is consecutive. At a branching index consider the smaller slot $s$. The additional admissibility of $s+1$ implies that $2^s/3^i$ belongs to the fixed interval from $b/208$ to $1001(b+1)/200000$. Its endpoint ratio is less than $20/19$.

If two indices $i<j$ branch, the smaller clocks $s,t$ therefore satisfy

$$
 \frac{19}{20}\le\frac{2^t 3^i}{2^s 3^j}\le\frac{20}{19}.
$$

Here $t>s$, since $3^{j-i}\ge3$. For $1\le d\le11$ and every $m\ge0$, direct integer comparison gives either $20\,2^m<19\,3^d$ or $20\,3^d<19\,2^m$. Checking $m<20$ suffices because $3^{11}<2^{18}$. Thus $j-i\ge12$. Branching refers to the entire fixed bin, so the locations of possible choices are shared by all its paths. Partition the indices $1,\ldots,k$ into consecutive groups of twelve. With $S_0=0$ known, a bin allows at most $2^{\lceil k/12\rceil}$ entire clock words, including the last partial group.

Equal clock words specify equal gap lists by successive differences. Subtract the affine identities for two paths with the same gap list to get $2^{S_k}(x_k-y_k)=3^k(x_0-y_0)$. Since $2$ and $3$ are coprime, their terminals agree modulo $3^k$. If $3^k\ge2N$, the interval width $1.08N$ is smaller than this modulus. Each word therefore has at most one ordinary terminal.

Choose $k$ least with $3^k\ge2N$, giving $3^k<6N$. For $N\ge10000$ this $k$ satisfies $1000k\le N$. This is immediate for $k\le10$. For $k\ge11$, use $2000k\le3^{k-1}<2N$ by induction starting at $k=11$. The number $p$ of distinct endpoints of such $k$-step windows satisfies

$$
 p\le109\cdot2^{\lceil k/12\rceil},\qquad p^{19}\le250^{19}N .
$$

For the last inequality put $g=\lceil k/12\rceil$. If $g>0$, $12(g-1)\le k$ and $2^{19}<3^{12}$. Therefore $2^{19g}\le2^{19}3^k$. The remaining comparison is $6\cdot218^{19}<250^{19}$.

## Excluding a band-contained cycle

On a cycle of least odd period $p$, select exactly one $k$-gap window ending at each of its $p$ distinct odd values. Each window stays on the cycle even when $k>p$. Repetitions inside a window do not add to the number of terminals. Take $S$ to be the total shortcut clock of one period. The exact cycle product gives

$$
 0<\Lambda=S\log2-p\log3
   =\sum_{j=0}^{p-1}\log(1+1/(3x_j))<p/(3N).
$$

Simons and de Weger give $\Lambda>\exp[-13.3(0.46057+\log p)]$. Their $K$ is the number $p$ of odd sites, and their $K+L$ is the total shortcut clock $S$. Thus $N^2\le 2^{18}p^{29}$. For example $13.3\cdot0.46057<9\log2$ follows from $\log2>0.69$, and $2(1+13.3)<29$. [Simons–de Weger, Lemma 12, printed p. 61](https://www.impan.pl/shop/en/publication/transaction/download/product/82263)

Together the two integer estimates give $p^9\le250^{38}2^{18}< (10^{11})^9$. Hence $p<10^{11}$. Hercher's Corollary 29 gives $p>1.375\cdot10^{11}$ when all starting integers up to $3\cdot2^{69}$ reach the trivial cycle. Barina's verification through $2^{71}$ covers that bound and gives $N\ge10000$. This excludes a nontrivial cycle in the stated band. [Hercher, Corollary 29 and article corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html) · [Barina, verification limit, Section 6](https://doi.org/10.1007/s11227-025-07337-0)

Any consecutive segment remaining inside the band for $N\ge10000$ consequently has distinct odd values. Apart from its first $k$ values, every value is the terminal of a preceding $k$-window in the band. Its length in odd values is at most $k+250N^{1/19}$. This allows excursions on either side. The conclusion concerns the ratio of actual odd values and does not assume any per-gap alphabet restriction.

In Lean, `terminal_count` bounds the number of distinct actual window endpoints. `cycle_power` proves $p^{19}\le250^{19}N$ for any band-contained ordinary odd cycle with a distinct first period. It constructs a full window ending at each position and permits windows longer than a period. `exclude_narrow_cycle` takes the three integer consequences of the published inputs as explicit hypotheses: $N\ge10000$, $N^2\le2^{18}p^{29}$ and $p\ge10^{11}$. The logarithm estimate and the use of the published verification are the written steps above. [Lean proof](OrbitAttack.lean)

The use of bounded height to control the number of ternary terminal classes is related to the more specialized excursion count in [PR #205](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md). Here the fixed-bin separation of the two possible clocks gives a uniform branch count.

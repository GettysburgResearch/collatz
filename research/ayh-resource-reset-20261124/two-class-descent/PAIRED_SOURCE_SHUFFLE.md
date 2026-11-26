# Simultaneous nearby representatives for the original two-arm marks

Let $0\le r<81$ be fixed and take both ordinary shortcut arms $n$ and $81n+r$. For a clock $h$ write
$$
 K_h(n)=(p_n(h),p_{81n+r}(h),T^h n,T^h(81n+r)).
$$
Equality of these four integers preserves the entire subsequent physical trajectories in their original order, including every subsequent odd-count difference. The two different arms of one sample need not have merged. The theorem below concerns repetitions of a sample's *ordered pair* by other original samples.

Put $a=1-\tfrac12\log_2 3$. Fix $0<\theta<a/10$ and define
$$
 N=2^h,\qquad K=\lfloor2^{(a-4\theta)h}\rfloor,\qquad
 D=\lceil2^{(a+3\theta)h}\rceil.
$$
On every block $n=2^h Q+v$, $0\le v<2^h$, with positive inputs, there is an explicit good subset with complement $O_\theta(N e^{-c_\theta h})$. Outside a further set of the same order, every source has at least $K$ distinct smaller **and** at least $K$ distinct larger good sources with the identical ordered record $K_h$. Each such source is within distance $D$ of the given one and stays in the same binary block. The constants are uniform in $Q,r$. If a block includes zero, extend the shortcut by $T(0)=0$ for the count, or pay one exceptional term.

This is a two-arm extension, at a deterministic clock, of the stopped scalar sibling construction in [Synchronization of growing Collatz blocks and selected references, Lemma 3 and equations (9)--(12)](https://rstation.ai/problems/collatz/papers/124). The scalar construction preserves the counted future of one chosen arm. Using two separate scalar displacements would not preserve the relation $81n+r$ when the parent parameter is moved. The joint estimate below counts both outputs simultaneously.

## Joint record count, span and repetitions

Write $g_1=p_n(h)$, $g_2=4+p_{81n+r}(h)$, and apply the usual binary affine lift to the parameter $v$. The two endpoint values are
$$
 Y_i=3^{g_i}Q+B_i(v),\qquad
 B_1=T^h v,\qquad B_2=T^h(81v+r).
$$
Uniformly, $0\le B_i\le C3^{g_i}$. Indeed the ordinary word formula for an input $m$ and $p$ odd steps gives $T^h m\le3^p(2^{-h}m+1/3)$. Sort the grades, breaking ties by a fixed label; let $s=g_{\rm hi}-g_{\rm lo}$ and $C_v=B_{\rm hi}-3^s B_{\rm lo}$. This integer is the canonical offset of the two affine profiles. The one-step contraction of $\sqrt{|C_v|/3^s}$ in [PR 146, growing additive gaps, at the frozen source](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) shows
$$
          2^{-h}\sum_{v<2^h}\sqrt{|C_v|/3^s}\le C.
$$
The initial states are $(4,r)$. At a tied slope the two possible orientations give the same absolute normalized offset.

Declare a residue good when $|C_v|/3^s\le2^{\theta h}$ and both arms, at every $0\le j\le h$, satisfy $|p(j)-j/2|\le\theta h$. The normalized-offset estimate, Markov's inequality, the binary word bijection on either odd-coefficient arm, and Hoeffding's inequality give exceptional fraction at most
$$
             C2^{-\theta h/2}+4h\exp(-2\theta^2h).                 \tag{1}
$$
For each fixed pair of counts on good residues, enumerate only $B_{\rm lo}$ and $C_v$. Their numbers of possibilities are at most $C3^{g_{\rm lo}}$ and $1+2\cdot3^s2^{\theta h}$. These data recover the two *exact* endpoint values within the $Q$ block. Thus the number of distinct ordered records on good residues is
$$
   \ll (h+1)^2\,3^{4+(1/2+\theta)h}2^{\theta h}
   \ll (h+1)^2 2^{(1-a+(1+\log_2 3)\theta)h}.                    \tag{2}
$$
A separate count of the two individual endpoints would multiply two powers of $3^{h/2}$ and lose the saving.

For each of these good record fibers the spread in original parent parameters is at most $D$ for large $h$. To see this, fix the parent endpoint and parent count $p$. If $w$ is the parent parity word and $p_i$ its first $i$ odd counts, then
$$
 n=\frac{2^hT^hn}{3^p}-\sum_{i<h:\,w_i=1}\frac{2^i}{3^{p_{i+1}}}.
$$
The subtracted sum is nonnegative and $\ll h\,2^{(a+(\log_2 3)\theta)h}$ from the running prefix bound. Its total range is less than $D$. Within each good record fiber remove the first $K$ and last $K$ entries *only as origins to which the conclusion is asserted*. They remain available as target siblings. From (2) their total mass divided by $N$ is
$O((h+1)^2 2^{-(3-\log_2 3)\theta h})$. Adding (1) proves the theorem. To work on a longer arbitrary interval tile by aligned full blocks and discard at most two partial blocks. For a single much wider interval and $h=o(\log_2 N_{\rm interval})$ the boundary loss is negligible.

For the actual head rows take $X=81^{j-1}$, $n\in[7X,8X)$, and use any clock $h$ with $C\log\log X\le h\le c_0\log_2 X$, with fixed $c_0<1$. The total normalized exception over rows is summable by taking $C$ large enough (or by taking $h$ a fixed positive fraction of $\log_2X$). All stages before $h$ exceed every fixed polylogarithmic landing threshold, since $T^i n\ge n/2^h$ on this range. Every sibling in the row therefore has exactly both of the original first entrances, including hit/miss status, landing values, absolute entrance clocks and odd counts on the hitting arms. Pooling the 81 suffixes costs a fixed factor. In particular this is an absolute original-source statement for actual two-color disagreements, with the smaller and larger marks retaining the same directed pair of colors.

## Tests allowed to depend on the exact future

For each binary block and good record fiber $S$, keep the entire fiber for measuring its conditional law, discarding only fibers with $|S|<K$. By (2) their combined mass obeys the preceding exponential bound. Every remaining $S$ lies in an interval of length $D+1$. For any integer $q$ and any list $E_S\subset\mathbb Z/q$ allowed to depend on the exact two-arm record and all its future data, one obtains
$$
  \Pr(n\bmod q\in E_S\mid n\in S)
  \le \frac{|E_S|(1+\lfloor D/q\rfloor)}{|S|}
  \le \frac{|E_S|(1+D/q)}{K}.                                    \tag{3}
$$
This conclusion holds fiber by fiber, with no factor inverse to the probability of its landing mark. For example, for $q=2^k\le D$, an absolute full-grid density at most $2^{-8\theta h}$ gives a conditional bound $O(2^{-\theta h})$, uniformly over the retained fibers. The same statement tests the parent's first $k$ parity symbols, by their bijection with residues mod $2^k$. When the child is tested, $81$ is odd and the child's residue is also a bijective image of the same parent residue modulo $2^k$. Choosing a distinct sparse early-word test retrospectively for every pair of ordered futures is permissible. Conditioning on a further union of retained fibers preserves the upper bound with no rare-mark cost.

The tested bits in (3) belong to the *past* of the retained record. The record's future is identical across the siblings, so this shuffle itself creates no new randomness in the common continuation. The sparse chronological tests already admitted by generic source counting should be distinguished from this exact recordwise assertion.

## Signed arithmetic cancellation and exact coupling of marks

There is also an actual total-variation coupling to a uniform source residue, for most moduli in a common interval of primes. This uses a classical additive large-sieve inequality, stated explicitly below. Choose $P=\lceil\sqrt{D+1}\rceil$ and let $\mathcal P$ be the primes in $[P,2P]$. For any retained $S$ and $q\in\mathcal P$ let
$$
 \Delta_q(S)=d_{\rm TV}\bigl(\mathcal L(n\bmod q\mid n\in S),
                               {\rm Unif}(\mathbb Z/q)\bigr).
$$
With $n$ uniform on the original integer block, one has
$$
 \frac1{|\mathcal P|}\sum_{q\in\mathcal P}
 d_{\rm TV}\!\left(\mathcal L(K_h,n\bmod q),\
                \mathcal L(K_h)\times{\rm Unif}(\mathbb Z/q)\right)
 \ll_\theta e^{-c_\theta h}
        + C\sqrt{\frac{P\log(2P)}{K}}.                             \tag{4}
$$
In (4), one may also retain the binary block index and suffix when several blocks or head rows of a common $h$ are pooled. The right side tends to zero exponentially in $h$ when $a-4\theta>(a+3\theta)/2$, in particular for $\theta<a/12$. For almost all moduli with an exponentially decaying exceptional fraction, the common joint law has exponentially decaying total-variation error by Markov's inequality with a square-root loss. One can couple while keeping the exact paired record fixed by maximal coupling of the conditional residue distributions. The marginal on the right uses the actual record frequencies, including unequal basin colors.

Indeed finite Fourier Parseval and Cauchy--Schwarz give
$$
 \Delta_q(S)^2\le\frac1{4|S|^2}
        \sum_{b=1}^{q-1}\left|\sum_{n\in S}e(bn/q)\right|^2,
 \qquad e(y)=\exp(2\pi i y).
$$
Distinct reduced frequencies $b/q$ over all these primes are separated on the circle by at least $1/(4P^2)$. The classical additive large sieve for an interval of length $D+1$ consequently bounds the sum of all squared exponential sums by $(D+1+4P^2)|S|$ up to an absolute constant; the location of the interval is arbitrary. Using $|\mathcal P|\gg P/\log(2P)$ and then Cauchy--Schwarz yields the displayed mean bound for each $S$. Average with the original source weights. Good/bad status may be included in the record before this calculation and dropped afterwards; exceptional sources contribute at most their total original probability. The proof works unchanged for any coarsening of the record and any deterministic marks of its two future orbits.

This decorrelation randomizes an actual original residue for a broad family of prime moduli, even conditional on the ordered two-class landing data in the stated absolute sense. The counting assertion (3), unlike (4), is for every retained fiber and fixed modulus. Neither assertion establishes decorrelation of the two future endpoint colors from one another. The unresolved mass can consist of dense local clusters of sources having the same ordered pair of different colors.

## Row-weighted rare selections

Take a fixed $c_0\in(0,1)$ and $h=\lfloor c_0\log_2(81^{j-1})\rfloor$ on row $j$. For any union of ordered landing marks $A_j$, including an arbitrary subset of the discordant pairs, let $a_j$ be its mass in original-source units divided by row length. If $B_j$ is a retrospective prefix test on each retained record satisfying the density requirement immediately following (3), then, with constants independent of the chosen marks and tests,
$$
 \Pr_j(A_j\cap B_j)\ \ll\ e^{-c j}(1+a_j).
$$
Here the exponentially small discard includes the two tiling fringes. Consequently all such test-passing contributions sum to a finite original-row weight, irrespective of $\sum a_j$. Rows with $a_j<j^{-2}$ incur only a summable total mass. On every remaining row the relative probability $\Pr_j(B_j\mid A_j)$ is $O(j^2e^{-cj})$. If two arms with distinct colors necessarily passed such a retrospective sparse test on the remaining rows, this would prove the target series. No such necessity follows from the shuffled record alone.

For fixed $h$, (4) also applies after conditioning on **any preselected union of good retained fibers**, since its prime-average Fourier proof holds separately for every such fiber and can use any mixture of their weights. The prime exceptional sets can depend on the selected mixture. For an unrestricted mark of mass at least $j^{-2}$, the ratio of the discarded original mass to the selected mass is still exponentially small. A choice of one prime after the selection can therefore give exponentially small conditional TV while retaining the exact marked futures. This quantifier does not assert a single universal prime for every possible selection.

The separated-frequency inequality used above is due to H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika 20 (1973), 119–134. [Original paper](https://doi.org/10.1112/S0025579300004708). The finite rank trimming and per-fiber sparse numerator (3) are checked in [PairedSourceShuffle.lean](PairedSourceShuffle.lean).

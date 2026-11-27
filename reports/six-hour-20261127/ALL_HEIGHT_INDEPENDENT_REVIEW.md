# Independent audit of the all-height ordinary census

The two frozen manuscripts prove their stated Theorems A and B. The reciprocal thresholds include divergence at equality. The source law in B is the uniform law on actual odd integers in one octave. Its gate consequence holds for the original weighted sources subject to the stated macroscopic lower mass. None of these results excludes a single exceptional forward orbit.

| Frozen input | SHA-256 |
|---|---|
| Author handoff | 4f04f6aced6e672d316e1d100d8039da93b452a5dd6468bd19286e6c65324b7b |
| ALL_HEIGHT_ORDINARY_CENSUS.md | 83c8661eaec0630bca1aec8db5d81a3e9fbacb2ef98cc6a9a37947ffb7173872 |
| ALL_HEIGHT_LOGARITHMIC_WINDOWS.md | 3299dffc969f750b50199fdab541b6c425add9008fa79e4b3fd7d6ecedd3df2b |
| Author checker | 823327db2a728b290a7101dddda10a21b503822d42100278510482f3cf5579ae |
| Author finite receipt | e59d810eb3e9326f3a1ed365ccdcbfcfbb8b901988551deda450cb3fa5903e0e |

## Static threshold and literal anchors

Take positive coprime integers $p,q$ of height $h=\max(p,q)$ and $3\nmid q$. The score is $v_3(qx+p)/\ln(2h)$. The positive numerator gives $v_3(qx+p)\ln 3\le \ln h+\ln(x+1)$, so the supremum defining $Q$ is finite. With $3\mid q$ a reduced fraction would have strictly negative valuation and cannot increase $Q$. For a strict violation by a supremum, a violating individual anchor always exists.

Write $I_k=[2^k,2^{k+1})$ and $g(x)=\ln(3+\ln(x+1))$. Uniformly on $I_k$, $\ln k-C\le g(x)\le\ln k+C$. A violation of $Q(x)\le cg(x)$ forces
$$
 (c g(x)\ln3-1)\ln h<\ln(x+1)-c g(x)\ln3\ln2.
$$
For fixed $c>0$ the possible heights consequently satisfy $h\le\exp(C_c k/\ln k)$ eventually. At each height there are at most $2h$ pairs. Put $d_h=1+\lfloor c\ln(2h)(\ln k-C)\rfloor$. Every violating pair specifies one residue modulo $3^{d_h}$. Among the $2^{k-1}$ odds, the fraction in any such class differs from $3^{-d_h}$ by at most $2^{1-k}$, since two is a unit in the modulus. The total of the rounding errors is exponentially small even after summing all possible heights. For $s=c\ln3(\ln k-C)\ge3$, $\sum_{h\ge1}2h(2h)^{-s}\le 2\zeta(2)2^{-s}$. This bounds the octave probability by $O_c(k^{-c\ln2\ln3})$.

At $h=1$ choose instead $d=1+\lfloor c\ln2(\ln k+C)\rfloor$. Every odd source $x=-1\pmod{3^d}$ strictly violates. Its octave probability is at least $3^{-d}-2^{1-k}\gg_c k^{-c\ln2\ln3}$. An octave probability $p$ contributes between $p/4$ and $p/2$ to the unreduced reciprocal sum. Equality in the threshold therefore gives divergence of the harmonic series.

## Finite ordinary source law

Let $T$ be the native shortcut map and $U$ the accelerated odd map. Each length-$k$ parity string beginning with one occurs once among the odds of $I_k$. Indeed, two inputs separated by $2^s$ with the same $s$ native bits have $s$th iterates separated by an odd power of three, giving opposite next bits. This proves the congruence-class bijection by induction. The remaining $k-1$ bits are exactly independent. If $E_j$ is the elapsed number of native steps to accelerated clock $j$, then for $m<k$ the event $E_j>m$ asks for fewer than $j$ ones in bit positions $1,\ldots,m$. It has probability
$$
 2^{-m}\sum_{i=0}^{j-1}\binom mi.
$$
With $j_*=\lfloor\alpha(k+1)\rfloor$ and $m=\lfloor\tau k\rfloor$, $2\alpha<\tau<1$, this is exponentially small for $j=j_*$. All actual dates $j\le\alpha\log_2 n$ lie below $j_*$.

On $G=\{E_{j_*}\le m\}$ each observed state $y$ satisfies $y\ge3^j n/2^{E_j}\ge2^{k-m}$ and $y+1\le(3/2)^j(n+1)$. Thus $g(y)=\ln k+O_\alpha(1)$ and the same finite height cutoff applies. For a gap word of length $j$ with total $E\le m$, exactly $2^{k-E-1}$ ordinary sources produce it. The terminal progression has step $2\,3^j$. In particular if $d>j$, the matched class modulo $3^j$ splits into the residue classes modulo $3^d$ with fractions $3^{-(d-j)}+O(2^{E+1-k})$. Enlarging $G$ to $\{E_j\le m\}$ and summing word masses $2^{-E}$ gives the second line of (B3), including $j=0$. If $d\le j$, the last $d$ gap letters alone determine the terminal class, whatever the earlier state was. Extending the summation over all independent geometric words gives the first line. This uses a dominating finite-prefix computation, and preserves coalescence and every dependency in the original source law.

## Reflected mass and strict thresholds

For a terminal target $r$ modulo $3^d$, the first reversed exponent $e\ge1$ must satisfy $2^e r\equiv1\pmod3$ before another ternary division. The allowed exponent parity has geometric mass at most $2/3$. Induction gives $p_d(r)\le(2/3)^d$. At $r=-1$, every compatible word has an actual negative odd inverse from the terminal integer $-1$. Recursive integrality follows by taking one residue modulo three and cancelling one ternary factor at each inverse. The positive magnitudes have inverse $u'=(2^e u+1)/3$ and deterministic forward map $u\mapsto(3u-1)/2^{v_2(3u-1)}$. On a word of length $d$ from $u$ to 1 the product is exactly
$$
 2^{-E}=\frac{3^{-d}}u\prod_{i=0}^{d-1}\left(1-\frac1{3u_i}\right)^{-1}.
$$
All magnitudes before the first hit on 1 are distinct integers exceeding one. For $s$ such magnitudes their factors multiply to at most $s+1$, by arranging them in increasing order and using $v/(v-1)$ at the $v$th integer. Every subsequent factor is $3/2$ and every subsequent gap is one. For $E\le6d$, $u\le2^{6d}$ and determinism permits each starting integer only once. Summing its reciprocal gives $O(d+1)$. For $E>6d$ the unconditional geometric Markov bound is $3^d(2/3)^{6d}$, since $\mathbb E[(3/2)^e]=3$. These estimates prove $p_d(-1)\ll(d+1)^2 2^{-d}$ as written.

At height one and $d>j$, the initial incomplete suffix costs $3^{-(d-j)}$, so $(j+1)^2 2^{-j}3^{-(d-j)}\le(d+1)^22^{-d}$. For larger heights the corresponding bound $(2/3)^j3^{-(d-j)}\le(2/3)^d$ holds. Summing $2h(2h)^{-s}$ for $h\ge2$ and $s=c\ln(3/2)(\ln k-C_\alpha)\ge3$ costs $O(4^{-s})$, by comparison to $\sum_{h\ge2} h(2/h)^3$. There are $O_\alpha(k)$ dates. The errors from incomplete source progressions cost at most $O(k)\exp(O(k/\ln k))2^{m+1-k}$ in total. Hence the exponents in (B4) are exactly $1-c(\ln2)^2$ for the first height and $1-c\ln4\ln(3/2)$ for the others. The second decreases faster, since $2\ln(3/2)>\ln2$.

For the lower bound, use only bit positions from 1 through $\lfloor\alpha k\rfloor-1$. An all-ones block of $d+1$ bits has an actual odd endpoint within those native times, with $d$ preceding gap-one edges. Each gap-one edge satisfies $2(y+1)=3(x+1)$. Thus $v_3(y+1)\ge d$. The accelerated date of the endpoint is at most its native time, which is at most $\alpha\log_2 n$. Choose $d=1+\lfloor c\ln 2(\ln k+C_\alpha')\rfloor$ using the upper growth bound for all these states. This guarantees the required strict inequality at the chosen height. There are $\asymp k/\ln k$ disjoint independent blocks. Their success probability is $2^{-(d+1)}\asymp_c k^{-c(\ln2)^2}$. The exact complement is $(1-2^{-(d+1)})^N$, which tends to zero for $c<(\ln2)^{-2}$. At $c=2(\ln2)^{-2}$ the lower bound is a constant times $1/(k\ln k)$. It suffices for equality-case divergence. No across-octave probability independence is used.

## Gate weights, clocks, and fixed sources

For arbitrary nonnegative $F_X(x)\le1/x$, mass above any given bad set of odd cores is at most $2\sum_{n\in B,\,n<X}1/n$. Good convergence in octave probability yields $o(\ln X)$ for the cumulative harmonic mass of each fixed deviation, including the final partial octave. A finite harmonic sum gives $O(1)$. These give (B6) after division by the stipulated $\delta\ln X$. This is valid even for an $X$-dependent choice of weights, including the first-exit gate weights.

The actual first-exit convention is the first native shortcut state at least $X$. If $L_s=3^{o_s}/2^s$ is the accumulated linear slope, $L_1=3/2$ and $(L_s)_{s=1}^k$ is a positive martingale under the ordinary octave law. The translation in the affine formula satisfies $0\le A_s\le (3/2)^s-1$. For $2^{k+1}\le X$ this is at most $X/2$. A crossing by time $k$ forces $\max L_s\ge X/2^{k+2}$, so the chance is $O(2^k/X)$, using the trivial bound for a low threshold. Include $G^c$ to ensure that the full accelerated test window ends by this native horizon. The dyadic sum of $O(2^k/X+\exp(-c_\alpha k))$ over all full octaves is $O_\alpha(1)$. The top partial octave and the odd core 1 also have bounded mass. An initial even path only decreases before its odd core. Consequently every observation really occurs before first exit, outside conditional probability $O_{\alpha,\delta}(1/\ln X)$. This does not make the sampled prefix a suffix of any named escaping ray.

Finally set $s=\lceil(\ln(k+2))^2\rceil$ and $n=2^{k+1}3^s-1$. Up to $j=k$ the exact identity $U^j(n)+1=2^{k+1-j}3^{s+j}$ follows from gap-one transitions, for which the preceding state is $3\bmod 4$. The exact valuation is $s+j$ and $\max_{j\le k}g(U^jn)=O(\ln k)$. Since $\ln n/k\to\ln2$, every fixed $C<1/\ln2$ obeys $C\ln n<k$ eventually. For every fixed multiplier $D$ all those dates violate $Q\le Dg$. The family makes no assertion at $C=1/\ln2$ or larger.

## Numerical controls and review scope

The accompanying independent checker solves each finite geometric residue law by the cyclic equation $2p(r)=p(2r)+J(2r)$, where $J(1+3a)=p_{d-1}(a)$ and $J=0$ off that class. It also exhausts finite ordinary sources, stopped ternary residues, full-word progressions, rational-height cutoffs with exact integer powers, marked runs, reflected first hits, native martingale maxima and obstruction states. All checks use ordinary integer or exact rational arithmetic. The finite certificate supports the written proof and has no asymptotic or Lean-verified scope. The frozen authors' texts need no repairs under this audit. The stronger estimates in the separate refinement are new results and do not retroactively alter either source.

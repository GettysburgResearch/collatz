# Ordinary Collatz parity cannot be a logarithmically sparse perturbation of an expanding periodic word

**PROPOSED.** Let T be the shortcut map on positive integers, continued through $1\to2\to1$. Fix a nonempty binary parity word w of length L and weight q with $P=3^q>Q=2^L$. For every fixed positive ordinary source x, let $D_w(N)$ be the Hamming distance between the first N shortcut parities from x and the first N letters of $w^\infty$. Then
$$
 \frac{D_w(N)}{\log N}\longrightarrow\infty .                    \tag{1}
$$
In particular the number of even shortcut steps from any fixed positive source is $\omega(\log N)$ by taking the one-letter word 1. No positive source realizes an all-time perturbation of the repository's expanding $(1110)^\infty$ ghost in which errors occur only at powers of two. The result is uniform in the *choice of each fixed word and initial source* in the logical sense that all such choices satisfy (1); it supplies no common cutoff or rate over word lengths and starting heights.

The external input is the rational p-adic Subspace Theorem of Schmidt–Schlickewei. We use the standard integer-vector formulation: for a fixed dimension $m\ge2$, fixed linearly independent rational forms at each of $\infty,2,3$, and fixed $\eta>0$, integer vectors with product of all these absolute values at most $\|X\|_\infty^{-\eta}$ lie in finitely many proper rational linear subspaces. One may divide out a common gcd: the discarded scalar contributes at least one to the product over these three places. Bounded primitive vectors add only finitely many lines. [J.-H. Evertse, The p-adic Subspace Theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

## 1. Translate to the signed periodic fixed point

For a length-L word v the formal affine endpoint is $(p_v x+C_v)/Q$, $p_v=3^{\mathrm{wt}(v)}$. Its legal 2-adic cylinder is the residue $p_v x+C_v=0\pmod Q$: the usual parity lifting gives a unique cylinder and every legal input satisfies this congruence. Write $y=(P-Q)x+C_w$. At a w block, $Qy'=Py$. At any block v,
$$
 Qy'=p_v y+b_v,\qquad b_v=(P-Q)C_v+(Q-p_v)C_w.
$$
The signed rational $c=-C_w/(P-Q)$ is a 2-adic integer, and its physical parity word is $w^\infty$: the formal affine map fixes c, so the cylinder congruence first gives w, and then repeats. In particular **any concatenation of complete L-blocks containing a mismatch has nonzero additive constant in the y coordinate**. Otherwise its formal affine map would fix c; its own length-cylinder congruence would then give it as the physical prefix at c, contradicting the known prefix. This prevents cancellation when several bounded gaps are grouped below. The positive-orbit coordinate $y$ is a positive integer, with $y\to\infty$ when $x\to\infty$. [Resident ghost example](../integrated/completion-ghost/README.md)

Starting at an aligned block boundary, take $a_0$ successive w blocks and one mismatching block $v_0$, then $a_1$ successive w blocks and a mismatch $v_1$, and so on. Each waiting time is finite: infinitely many exact w blocks would make the entering positive y divisible by $Q^j$ for every j. Zero waiting times are permitted. If $y_i$ enters the ith group, put $u_i=y_i/Q^{a_i}$, a positive integer by coprimality of P and Q. Consecutive groups satisfy
$$
 Q^{a_{i+1}+1}u_{i+1}=p_iP^{a_i}u_i+b_i,                         \tag{2}
$$
where $p_i=p_{v_i}$ and $b_i=b_{v_i}$. Before the mismatch the physical value of the translated coordinate is $P^{a_i}u_i$.

## 2. A fixed number of waiting times has one source budget

For every fixed integer $k\ge1$ and every $\varepsilon>0$, all sufficiently large positive entering y satisfy
$$
 \sum_{j=0}^k a_j\le(1+\varepsilon)\log_Q y .                    \tag{3}
$$
The threshold can depend on k, w and $\varepsilon$. For $k=0$ the same statement follows immediately from divisibility.

Suppose a sequence $y=y_0\to\infty$ violates (3). Pass to a subsequence on which the first k mismatch types are fixed and each interior $a_j$ ($1\le j<k$) is either fixed or tends to infinity. Iteration of (2) gives
$$
 Q^B u_k=X_0+\sum_{i=0}^{k-1} b_i X_{i+1},\qquad
 B=\sum_{j=1}^k(a_j+1),
$$
where
$$
 X_0=u_0\prod_{j=0}^{k-1}p_jP^{a_j},\qquad
 X_{i+1}=Q^{\sum_{j=1}^i(a_j+1)}\prod_{j=i+1}^{k-1}p_jP^{a_j}.
$$
Every coordinate after $X_0$ is a positive integer with prime support contained in $\{2,3\}$. Moreover $X_0/X_1=u_0 p_0P^{a_0}\ge y_0$. Two adjacent coordinates of the sum with gap $a_j$ have ratio, later over earlier, equal to $(Q/p_j)(Q/P)^{a_j}$.

Group consecutive terms of the sum when their interior gaps are fixed and keep the first X coordinate of each group. Each group becomes a fixed rational coefficient times that coordinate. The coefficient is nonzero: multiplying by the nonzero fixed product of its internal $p_jP^{a_j}$ gives the translated additive constant of the finite word $v_i w^{a_{i+1}}v_{i+1}\cdots w^{a_l}v_l$, nonzero by Section 1. Across different groups the ratio of later to earlier representative tends to zero. The same is true from $X_0$ to the first representative by the preceding lower bound. Thus the surviving coordinates, in order, have strictly separated asymptotic sizes.

Use those coordinates as one integer vector X. At the real and the 3-adic place use the coordinate forms. At 2 replace the first coordinate by the displayed sum, keeping every other coordinate. These forms are independent since the coefficient of $X_0$ in the sum is one. The product of their absolute values is at most
$$
 u_0 Q^{-B}.
$$
Indeed every retained coordinate other than $X_0$ is a $\{2,3\}$-unit, the factors of $X_0$ other than $u_0$ are powers of three, and the sum is divisible by $Q^B$. Since $a_0=\log_Q y_0-\log_Q u_0$, violation of (3) makes the product at most $y_0^{-\varepsilon}$.

For fixed k the vector height is polynomially bounded in $y_0$: from $a_i\le\log_Q y_i$ and (2), $y_{i+1}\le C_w y_i^{\log_Q P}$, and iteration bounds each displayed product. The p-adic Subspace Theorem applies with a fixed positive exponent after this height change. A single proper subspace would contain infinitely many of the selected vectors. In any fixed nonzero rational linear relation on their coordinates the first term with a nonzero coefficient eventually dominates the later terms, which is impossible. This proves (3).

## 3. Counting mismatches in time

Write $H_i=\log_Q y_i$. A group of $a_i$ exact blocks followed by its one mismatch gives
$$
 H_{i+1}\le H_i+a_i\log_Q(P/Q)+C_w
$$
with a constant independent of i. For each fixed $k\ge1$, sum this inequality through k groups and use (3) with $\varepsilon=1$ (or simple divisibility for one group). There is a constant $C_{w,k}$ such that, for **all** entering y, including the finitely many small exceptions,
$$
 H_{i+k}\le K_w H_i+C_{w,k},
 \qquad K_w=1+2\log_Q(P/Q)>1 .
$$
In particular the multiplier does not depend on k. Iteration separately in the k residue classes gives
$$
 \limsup_{i\to\infty}\frac{\log(1+H_i)}i\le\frac{\log K_w}{k}.
$$
Since k was arbitrary and $H_i\ge0$, this limit is zero. Also $a_i\le H_i$. The number of aligned blocks through the first j mismatches is $B_j=\sum_{i<j}(a_i+1)$, so $\log B_j=o(j)$: for any $\delta>0$ the tail summands are at most $e^{\delta i}$ for all sufficiently large i. Any time up to but not including the next mismatch is bounded by $LB_{j+1}$ shortcut positions, while the first j completed mismatches already contribute at least j Hamming differences. This proves (1) including prefixes that end inside a block.

For a *nonperiodic* positive orbit a contracting periodic template ($3^q<2^L$) already differs on a positive asymptotic lower density of positions: the orbitwise coefficient escape implies its actual odd count eventually exceeds $N\log_3 2$, while the template count is $(q/L)N+O(1)$. The equality case is impossible by unique factorization. [T-A3-451 and source-pinned orbitwise estimates](../integrated/orbitwise-boundaries/README.md)

**Open.** The theorem does not show a positive frequency of deviations for an expanding template. For example it does not exclude $\asymp\sqrt N$ deviations. Its Subspace Theorem input gives no effective threshold here, and it does not establish universal coefficient stopping.

# Many passing ancestors of every supplied ordinary target

Use the odd map $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. For $1<\tau<2$ let $P_\tau$ contain those $x$ whose first $j$ odd gaps have sum at most $\tau j$ for every $j\ge1$. For a positive odd target $a$ prime to three, let $G_\tau(a)$ comprise its positive odd, ternary-unit ancestors that satisfy this same inequality for every prefix ending at or before their first visit to $a$. It includes the target. Write $H_2$ for binary entropy.

**Theorem.** There are absolute $C,\epsilon_0>0$ with the following property. Given $0<\epsilon<\epsilon_0$, put $\tau=2-\epsilon$. There is $c_\epsilon>0$ such that for every supplied positive odd $a$ prime to three and $X/a$ sufficiently large in terms of $\epsilon$ alone,
\[
  |G_\tau(a)\cap[1,X]|\ \ge\ c_\epsilon (X/a)^{1-C\epsilon^2}.                    \tag{1}
\]
If $a\in P_\tau$, each of these ancestors belongs to $P_\tau$ and its ordinary forward path passes through this same $a$. Every counted point can reach it in $O_\epsilon(1+\log(X/a))$ odd steps. The constants in (1) are independent of the target.

The arithmetic input is Weaver and Wren's favorable-cylinder floor at fixed total and extra ternary depth. The conclusion iterates that floor on integers produced on the preexisting target's own inverse tree. The entropy loss is quadratic as $\tau\uparrow2$. The unrestricted permanent-set entropy upper bound has the same order of deficit, since $1-H_2(1/\tau)\asymp(2-\tau)^2$. Constants in the two deficits need not coincide. The result gives no lower bound of this exponent at the fixed slope $7/4$. [Weaver and Wren, Paper 48 v2, October 28, 2026, Lemma 7, equation (76)](https://rstation.ai/problems/collatz/papers/48/v2).

## A pointwise block floor

Write an inverse gap $e$ as the ordinary operation $I_e(y)=(2^e y-1)/3$ when the result is integral. A list in inverse chronological order has cumulative gap sums $S_i$ and normalized additive offset $B_i=\sum_{u=1}^i3^{u-1}2^{-S_u}$. Its endpoint from $w$ is $2^{S_i}3^{-i}(w-B_i)$.

There are absolute $c_0>0$ and $b_0$ such that the following holds for every integer $b\ge b_0$, every positive odd ternary unit $y$ and every integer
\[
                    2b-\tfrac32\sqrt b\le s\le 2b-\sqrt b .
\]
From $y$ there are at least $c_0m_s/\sqrt b$ distinct actual inverse words of length $b$, total $s$, and terminal odd phase $1\bmod3$, where $m_s=2^s3^{-b}$. Every such endpoint is strictly below $ym_s$.

Indeed, denote the fixed cylinder in Lemma 7 by $v\bmod3^h$. Choose $e$ in $[E,E+4\cdot3^h-1]$ for a sufficiently large fixed integer $E$ with $2^e y\equiv1+3v\pmod {3^{h+1}}$; the powers of two exhaust these units twice. At the root $a$ choose a bridge which is not its periodic inverse child, if such a child exists. There is at most one periodic child and the two choices give distinct positive integers. Along any resulting word the specified terminal hit to $a$ is the first: an earlier visit to $a$ would put this bridge on a closed orbit at $a$. The positive odd $w=I_e(y)$ then belongs to the cylinder. Put $n=b-1$ and $t=s-e$. For $b$ sufficiently large, the uniform bound on $e$ gives $|t-2n|\le2\sqrt n$. At extra depth one, apply (76) to the residue $w-3^n2^{-t}\pmod {3^{n+1}}$, which lies over the favorable cylinder for $n\ge h$. The independent coding weight for each such word is $2^{-t}$, and its central slice probability $2^{-t}\binom{t-1}{n-1}$ is $\gg1/\sqrt b$ by Stirling's bounds. The resulting count is $\gg2^t/(3^{n+1}\sqrt b)\gg m_s/\sqrt b$, with an absolute constant since $e$ is bounded.

All inverse letters act physically. Convergence of the residue of the full offset implies $w\equiv B_i\bmod3^i$ at each prefix. The integral intermediate states are odd. They are positive by induction since $I_e$ of a positive odd integer, when integral, is positive. The terminal state $2^t3^{-n}(w-B_n)$ is $1\bmod3$ by the chosen extra digit. Two words of the same length starting at the same target and ending at the same integer must coincide, by determinism of the forward odd map. The forward gap is exact because every subsequent forward odd state is odd. Positive offsets imply the claimed upper height bound at the end of the concatenated length-$b$ word.

## Normalize by the actual block scale

Take $b=\lfloor1/(4\epsilon^2)\rfloor$ large enough for the block floor. Every allowable block advances the reverse running sum
\[
                       V_i=\tau i-S_i
\]
by at least $\sqrt b/2$ at its right boundary, since $\epsilon\sqrt b\le1/2$. Put $D=\log(4/3)>0$ and let $m_-,m_+$ be the minimum and maximum $m_s$ on these totals. For sufficiently large $b$, $\log m_-\ge Db/2$. Their number of totals is at least $\sqrt b/3$.

At every integer node $y$ in the tree take all its admissible block words from the floor. Let $d=1-K/b>0$, where the absolute $K$ is selected independently of $b$. Then
\[
 Z(y)=\sum_{w\text{ at }y}m_{s(w)}^{-d}
     \ge\frac{c_0}{\sqrt b}\sum_s m_s^{1-d}
     \ge(c_0/3)e^{KD/2}\ge1 .
\]
The finitely many branches thus admit probabilities $m_{s(w)}^{-d}/Z(y)\le m_{s(w)}^{-d}$. These are assigned conditionally at each *actual* positive integer node; no distributional assumption on earlier or later residues is used.

For $L>1$, stop a concatenated path at the first complete block for which its product $Q=\prod_w m_{s(w)}$ reaches $L$. This is a finite exhaustive stopping family since $m_->1$. Every stopped product lies in $[L,Lm_+)$ and every stopped word has probability at most $L^{-d}$. Summing probabilities gives at least $L^d$ stopped words. Their full block depth is at most $1+\log L/\log m_-$. Along any partial block the height relative to its beginning is at most $2^{2b}$, since all gaps are positive with total at most $2b$. Therefore every intermediate integer is at most $2^{2b} aL m_+$. We may use $L=X/(2^{2b} a m_+)$.

## Return each word to an actual passing ancestor

Mark a position attaining the maximum of $V_i$ over the entire stopped word, taking the last such position. An ordinary source at this recorded position passes every forward prefix to $a$. Indeed, a forward prefix corresponds to an inverse interval $[u,i]$, and its forward passing inequality is exactly $V_i\ge V_u$. If $a$ is already permanent, intervals extending beyond $a$ pass by addition. All recorded sources are ternary units, since intermediate states have an inverse child when the word continues, and block endpoints are prescribed units.

The map from stopped words to marked positions discards uniformly bounded terminal data. If there are $N$ full blocks and a maximum lies in block $j$, then it is at most $V_{(j-1)b}+2b$, as all gaps are at least one and $\tau<2$. The terminal value is at least $V_{(j-1)b}+(N-j+1)\sqrt b/2$. Thus any maximum is within the final $4\sqrt b+1$ blocks. The initial position cannot be a global maximum when $N\ge1$. The number of possible discarded suffixes is bounded by a constant $C_b$, since each of their at most $(4\sqrt b+2)b$ letters is at most $2b$.

For a fixed marked integer its first-hit depth to $a$ is unique, by the first-bridge choice. Its entire inverse prefix from $a$ is therefore also unique. The discarded suffix determines the complete stopped word because the concatenation is at fixed length $b$. Consequently distinct marked vertices number at least $L^d/C_b$. Because $1/b\le C'\epsilon^2$, and $L$ is an $\epsilon$-dependent constant multiple of $X/a$, this proves (1), including for periodic targets.

For the global comparison, fix $k=\lceil\log_2(X+1)\rceil$ and take the first $k$ shortcut parity bits of any odd $x\in P_\tau\cap[1,X]$. If it has $j$ odd inputs in that interval, its $j$th odd gap ends at native time $S_j\ge k$, so $j\ge k/\tau$. The shortcut parity map on residues modulo $2^k$ is bijective by one-step induction. Summing the binomial upper tail gives $|P_\tau\cap[1,X]|\le 2^{kH_2(1/\tau)+O(\log k)}$. This comparison uses permanence. A target-stopped path may hit its target before the $k$th native step. The lower theorem allows such paths and retains their target, clock and every prior gate, without imposing any additional forward behavior after the target.

## An explicit ceiling for block normalization

There is a stronger limit on the constant achievable by this particular proof. Fix positive block length $b$ and slope $\log_2 3<\tau<2$. Suppose that for *every* ordinary odd ternary unit a collection of physical $b$-letter words, ending in ternary units and having total at most $\tau b$, satisfies $\sum_w m_{s(w)}^{-d}\ge1$, with $0\le d\le1$. Then necessarily
\[
  1-d\ \ge\ \frac{I(\tau)}{\tau\log2-\log3},\qquad
  I(\tau)=\tau[\log2-h(1/\tau)],
\]
where $h(p)=-p\log p-(1-p)\log(1-p)$ uses natural logarithms.

To see this, include *all* such words in the sum and average the resulting periodic function of the supplied root modulo $3^{b+1}$ over its unit classes. Every class occurs among positive odd ordinary integers. For a given inverse word the first $b$ ternary digits are forced by $B_b$. At the next digit exactly two of three lifts give a unit terminal. The normalized probability under a uniformly chosen unit root is $3^{-b}$. Thus the average of the full sum is $\mathbb E[1_{S_b\le\tau b}m_{S_b}^{1-d}]$ under independent gap weights $2^{-e}$. The geometric Chernoff bound $\Pr(S_b\le\tau b)\le e^{-bI(\tau)}$ follows by minimizing $e^{-u\tau b}(e^u/(2-e^u))^b$ over $u\le0$, with optimizer $e^u=2(\tau-1)/\tau$. Also $m_{S_b}^{1-d}\le e^{b(1-d)(\tau\log2-\log3)}$ on the event. This proves the ceiling.

At $\tau=2-\epsilon$, the right hand side is $\epsilon^2/(4\log(4/3))+O(\epsilon^3)$, whereas $1-H_2(1/\tau)=\epsilon^2/(8\log2)+O(\epsilon^3)$. Even the best possible all-root block normalization of this form loses at least $2\log2/\log(4/3)\approx4.82$ times the global permanent entropy deficit to quadratic order. This ceiling applies to the proposed uniform local normalization. It does not supply an upper bound on the actual $G_\tau(a)$ or on other constructions with state-dependent weights.

## A positive lower exponent down to a window-certified slope

For every $10^6/569908<\tau<2$ there are $c_\tau,d_\tau>0$ such that $|G_\tau(a)\cap[1,X]|\ge c_\tau(X/a)^{d_\tau}$ uniformly in every supplied odd ternary unit $a$ and sufficiently large $X/a$. The reciprocal endpoint is $1.754669175\ldots$. This corollary has a smaller positive exponent and reaches closer to $7/4$ than the near-two proof with its unspecified onset.

Write $M_m$ for the maximum over ternary units of the minimum total among $m$ legal inverse odd gaps ending in a unit. Paper 229 proves $M_m/m\to 1/\Theta_\infty$ including the worst root; the minimizer only depends on a finite residue. Paper 154 gives $\Theta_\infty\ge569908/10^6$ by its window-22 certificate and the cited transfer. The numerical certificate is an imported result. Choose $1/\Theta_\infty<\tau_0<\tau$ and $b$ sufficiently large that $M_{b-1}+12\le\tau_0 b$ and $v=2^{\tau_0b}3^{-b}>1$; $\tau_0$ can be chosen greater than $\log_2 3$. [Worst-root inverse cost, Paper 229 v1, §2](https://rstation.ai/problems/collatz/papers/229/v1) · [Wren, Paper 154, window-22 certificate, Corollary 1](https://rstation.ai/problems/collatz/papers/154).

Every ternary unit has two distinct legal unit children among the gaps $1,\ldots,6$: modulo nine the six powers of two range over all units and $2^e a$ may be either $4$ or $7\bmod9$. In the range through twelve each of these possibilities occurs twice. At the initial root exclude its periodic child, if present, and still choose two; at all other roots choose any two. Follow each child by one cost-minimizing $(b-1)$-letter word on its actual residue. This gives two distinct physical length-$b$ choices at every actual node, each with total at most $\tau_0b$. After $N$ blocks there are exactly $2^N$ chosen words. Their block endpoints have height at most $av^N$, and each intermediate height is at most $2^{2b}av^N$. The reverse reserve $V$ increases at least $(\tau-\tau_0)b$ per complete block and can rise by at most $2b$ inside one block. Its last global maximum therefore falls within the final $1+2/(\tau-\tau_0)$ blocks. The same unique-first-hit and bounded-suffix argument gives $\gg_\tau 2^N$ different vertices of $G_\tau(a)$. Taking $N=\lfloor\log(X/(2^{2b}a))/\log v\rfloor$ proves the assertion with $d_\tau=\log2/\log v$. The proof only requires a single minimizing word at each true state plus a separately retained binary choice, and preserves the complete path to $a$.

## Ordinary sources in every octave near slope two

For all sufficiently small $\epsilon>0$, the lower bound also gives
\[
       |G_{2-\epsilon}(a)\cap[X,2X]|
        \ \gg_\epsilon\ (X/a)^{1-C\epsilon^2}
                                                                         \tag{4}
\]
for every large enough $X/a$ depending only on $\epsilon$. This counts odd units themselves. A final dyadic multiple would generally be even and would not establish this statement.

We first construct an extension. Uniformly for positive odd units $y$ and $X/y$ sufficiently large in terms of $\epsilon$, there is a positive odd unit $x\in[X,2X]$ passing every forward prefix through its visit to $y$ and reaching $y$ within $O_\epsilon(1+\log(X/y))$ odd steps. Use the strengthened fixed-total, extra-depth floor and global partial-sum bound $|S_i-2i|\le C\sqrt{(i+1)\log(i+2)}$ from [the central-shell refinement](all_slope_no_return.md). Choose a bounded initial gap into its favorable cylinder, producing $w=I_e(y)$ with $K y\le w\le K' y$ for fixed constants $K,K'$ and $K\gg F$, where $F$ is its real-offset cap. Write $R=\log_2(X/w)$, $\lambda=2-\log_23>0$, $\ell=\log_2(3/2)>0$, and put $h=\lceil10\epsilon R/\lambda\rceil$. Next choose an integer $b$ within an absolute bounded distance of $(R+h\ell)/\lambda$. Fixing $h$ first makes the fractional parts of $R+b\log_23+h\ell$ a translated irrational rotation in $b$. There is an absolute number of consecutive $b$ sufficient to ensure an integer $s$ with
\[
     R+h\ell+\log_2(5/4)\ \le\ s-b\log_23
                      \ \le\ R+h\ell+\log_2(3/2).
\]
Indeed a finite initial segment of the irrational rotation meets every translate of this fixed-length arc (compactness, or a sufficiently fine rational convergent grid). Thus $s=2b+O(1)$ uniformly. For small enough absolute $\epsilon$, $h+1\le\delta b$ and $h\ge 4\epsilon b$ for large $R$, where $\delta$ is the extra-depth constant and $b\sim (R+h\ell)/\lambda$.

From $w$ take one refined physical word of length $b$, total $s$, and terminal $u\equiv-1\bmod3^{h+1}$. This follows by prescribing the offset residue $w+3^b2^{-s}\bmod3^{b+h+1}$ before division by $3^b$. Append $h$ inverse gaps of one, yielding $x=(2/3)^h(u+1)-1$, a positive odd ternary unit. Every intermediate gap is exact. The height formula is
\[
 x=(2/3)^h 2^s3^{-b}w(1-B_b/w)+(2/3)^h-1 .
\]
The ideal leading term lies in $[5X/4,3X/2]$, $B_b\le F$, and $F/w$ is sufficiently small, hence $X\le x\le2X$. For the initial bridge and full middle word the maximum reverse reserve $V_j=(2-\epsilon)j-S_j$ exceeds its terminal value by at most $\epsilon b+O(\sqrt{b\log(2b)}+e+1)$, by the uniform partial-sum bound and $s=2b+O(1)$. The final $h$ ones increase the reserve monotonically by $(1-\epsilon)h$, which exceeds this entire drawdown for all sufficiently large $R$ depending on $\epsilon$. Therefore the final position is a running maximum. This proves every forward passing inequality through $y$. The odd length $1+b+h$ is $O_\epsilon(1+\log(X/y))$.

A lower bound on the heights of the original marked vertices removes any logarithmic multiplicity cost. Enlarge the absolute lower endpoint $E$ of the first-gap choices in the pointwise block floor so $(1+3F)2^{-E}\le1/8$, using the real-offset cap $F$ in (76). Each selected full block then has inverse affine form $y'=m_s(y-B)$ with $0<B\le1/8$: the concatenated offset is $2^{-e}(1+3B_{b-1})$. Enlarge $b_0$ so $(7/8)m_->2$. At successive full boundaries $y_i\ge2^i a$, hence the actual stopped endpoint obeys
\[
 y_N=aQ_N\prod_{i<N}(1-B_i/y_i)
       \ge aQ_N(1-\textstyle\sum_{i<N} B_i/y_i)\ge(3/4)aQ_N .
\]
At most $O_b(1)$ letters are discarded to the recorded vertex and each changes the height by at most the fixed factor $2^{2b}$. Consequently (1) already gives $\gg_\epsilon(X/a)^{1-C\epsilon^2}$ marked vertices in $[c'_\epsilon X,X]$.

Apply this at $X/C_\epsilon$ for a fixed sufficiently large $C_\epsilon$ so that every returned ancestor $y$ is eligible for the extension. Its ratio $X/y$ now lies between two positive constants depending only on $\epsilon$. The extension to $x\in[X,2X]$ has only $O_\epsilon(1)$ ordinary odd steps. Both passing segments concatenate. For one output $x$, every candidate old $y$ is on its unique forward trajectory within this fixed number of steps, so only $O_\epsilon(1)$ old vertices can produce it. This proves (4) with no independence between the original integer and its extension.

The [record and stationary-flow checker](check_retained_trees.py) checks 58 positive-depth records, including 57 proper cuts and two paths with tied maxima, 340 exact word Haar counts, and higher-precision balance of a ternary block flow. The [frozen-root checker](check_frozen_root.py) exhausts every eligible ordinary unit source for target 25 through depth 89 at slope $7/4$. There is no positive-depth word of total $\le7b/4$ for $1\le b\le87$. At depth 88 exactly the sources 586223 and 588103 have total 154, and at depth 89 precisely 390815 has total 155. Each passes every forward prefix to 25. The height cutoff $25\,2^{\lfloor7b/4\rfloor}/3^b$ makes these certified finite exhaustions rather than samples. In particular a gate-debt stopping rule demanding a nonzero passing extension for *every* root cannot have a uniform horizon below 88.

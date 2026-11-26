# A pointwise spacing obstruction at the full reduced denominator

**Proposed written theorem.** Let $p$ be the primitive odd period of an ordered positive rational cycle in the three-band strip, $s$ its minimum and $d$ its complete reduced denominator. For $s\ge2^{30}$, uniformly in the octave mask,
$$
                 d\,\max\{p^2,s/p^{1/3}\}\gg p^{1000/479}.             \tag{1}
$$
In particular any sufficiently long **ordinary** cycle in the bounded least-tripling-disagreement branch has
$$
             s\gg p^{1000/479+1/3}, \qquad
             0<h/p-\log_2 3\ll p^{-1000/479-1/3}.                  \tag{2}
$$
The previous strip count gave $s\gg p^{1000/479}$. The additional power follows by counting close pairs of points on an exponential curve modulo an integer. It uses all $p$ physical phases in one lap. For rational cycles with $p^{1000/479}\lesssim s\le p^{1000/479+1/3-\epsilon}$, (1) gives a growing lower bound on $d$ even where the earlier height count could allow $d=1$.

Require $2^{a_j}x_{j+1}=3x_j+1$, actual valuations $a_j\in\{1,2\}$, $s\le x_j\le(16s+7)/3$, a common $d$ prime to six, and the ordered dyadic rotation in the [window theorem](README.md). The bounded ordinary branch supplies these hypotheses. For a rational candidate ordering is an additional hypothesis. If $D=2^h-3^p>0$, the affine equation at a cyclic cut with carry $C$ gives $d=D/\gcd(D,C)$, with all prime powers included. The bound concerns this $d$ itself.

## Upper bound from the incoming words

Put $\delta=479/1000$. The 4096-step count in PR200 bounds the number of possible length-$k$ incoming odd-gap words uniformly by $2^{4096} 3^{\delta k}$. The count uses positive real strip bounds and the specified exponents, and hence applies also to the rational points here. Its exact certificate overcounts the strip walks through bins for the starting height, then concatenates the blocks. For $Q=3^k$, a given word fixes $d x_j\bmod Q$: iterate the affine steps and reduce the resulting identity modulo $3^k$, cancelling the invertible power of two. Thus the **literal integer** $N_j=d Z_j=2^{2-k_j}d x_j$ occupies at most $3\cdot 2^{4096} Q^\delta$ residue classes. This factor three allows every octave separately at the terminal time. [PR200, Theorem S and the integer block certificate](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md)

Taking $Q$ just above $8ds$ gives the elementary bound $p\ll (ds)^\delta$: the folded mantissas are distinct, and all $N_j<8ds$. This proves (1) immediately if $s\le p^2$. For $s>p^2$, let $Q$ be the smallest power of three at least $\max(dp^2,ds/p^{1/3})$. As $r$ runs through the sorted ranks $0,\ldots,p-1$, the amplitude estimate at the true minimum gives
$$
       N(r)/Q=R2^{r/p}+O(dp/Q)=R2^{r/p}+O(1/p),\qquad R=4ds/Q.
       \tag{3}
$$
Indeed the starting amplitude is $4s$, and (1) of the [window proof](README.md) applies across the whole lap. We have $R\gg1$ and $R\le4p^{1/3}$. If two actual residues of $N$ agree, the difference between the two corresponding ideal values is within $K/p$ of an integer for one absolute $K$. This controls coincidence of the complete integer residues, without requiring full equidistribution at bin size $1/p$.

## Counting inverse images of an integer difference

For fixed $K,C,c>0$, $c\le R\le Cp^{1/3}$, the number of ordered pairs $0\le i,j<p$ satisfying
$$
       \|R(2^{j/p}-2^{i/p})\|_{\mathbb R/\mathbb Z}\le K/p          \tag{4}
$$
is $O_{c,C,K}(p)$. The diagonal contributes $p$. For $i<j$ and a nearest integer $m=0$, the mean value theorem gives $j-i=O_K(1/R)$, contributing $O_{c,K}(p)$. Every other pair has $1\le m\le R+O_K(1)$. At such a pair put
$$
       \psi_m(v)=p\log_2(2^{v/p}+m/R).
$$
The mean value theorem for the logarithm gives $\|\psi_m(i)\|\le C_K/R$. For $R$ bounded, direct monotonicity gives $O_{c,K}(1)$ possible $j$ per $i,m$, which suffices. For large $R$ there is at most one $j$ for any $i,m$ having (4). On the full interval $0\le v\le p$,
$$
   \psi_m''(v)=\frac{\log2}{p}\,
      \frac{2^{v/p}(m/R)}{(2^{v/p}+m/R)^2}
        \asymp \lambda_m=\frac{m}{pR}.                              \tag{5}
$$
This uses the difference index $m$. The full curve need not be chopped into pieces of length $p/R$.

Take $H=\lfloor R/C'_K\rfloor$, with $C'_K$ large and $R$ above a fixed threshold. The nonnegative kernel $H^{-2}|\sum_{a=0}^{H-1}e(at)|^2$ is bounded below by an absolute positive constant whenever $\|t\|\le C_K/R$, by the sine formula. Its Fourier coefficients have absolute value at most $1/H$. Thus the number of $i$ contributing for this $m$ is
$$
   \ll_K \frac pH+\frac1H\sum_{h=1}^{H}
        \left|\sum_{i=0}^{p-1}e(h\psi_m(i))\right|
   \ll_K \frac pR+\sqrt{pm}+\sqrt{p/m}.                             \tag{6}
$$
The second derivative estimate is $O(p\sqrt{h\lambda_m}+(h\lambda_m)^{-1/2})$, from (5), and the two sums of square roots give (6). Here $e(t)=\exp(2\pi i t)$. [D. R. Heath-Brown, classical derivative test (1), with k=2](https://arxiv.org/abs/1601.04493)

Summing (6) gives $O_K(p+\sqrt p\,R^{3/2}+\sqrt{pR})=O_{c,C,K}(p)$. Symmetry handles $j<i$. This proves (4). Cauchy–Schwarz applied to the multiplicities of the exact residues in (3) now gives $\gg p$ occupied residue classes modulo $Q$. Their number is at most $O(Q^\delta)$ by the incoming-word count. Therefore $p^{1/\delta}\ll Q\ll d\max(p^2,s/p^{1/3})$, proving (1). At $d=1$ the $p^2$ option alone is eventually too small since $1/\delta>2$, so (2) follows, including its clock estimate from the positive lap product.

## Whole-range closure attempt

For $d=1$ one can instead always take $p^2\le Q=3^k<3p^2$. The strip language permits at most $O(p^{\,0.958})$ exact residues there, while equal residues force the near-coincidence (4). A uniform bound $O(p^{1.042-\eta})$ with fixed $\eta>0$ in (4) throughout the remaining possible amplitudes would contradict Cauchy–Schwarz and exclude this entire branch. The two-log height ceiling permits $R$ up to a little over $p^{3.1163}$. This is an ordinary pointwise spacing problem with fixed amplitude set by the actual minimum. In (6) the term $\sqrt p\,R^{3/2}$ grows too quickly there. Bounds averaged over the amplitude do not establish the required uniform bound.

Both the spacing argument and the ternary language count concern every phase of one candidate. They give no conclusion about an escaping trajectory or an eventual cycle encountered outside this strip. No all-amplitude spacing theorem has been proved here.

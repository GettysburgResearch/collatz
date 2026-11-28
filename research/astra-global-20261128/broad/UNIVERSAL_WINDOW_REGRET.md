# All fixed-window selectors lose on the same full-dimensional set of critical sources

Let $1<b\le a_*$, $\theta=1/b$, $p_e=\theta(1-\theta)^{e-1}$, $t=-\log(1-\theta)$, $H= -\sum p_e\log p_e$ and $r=\theta(1-\theta)^4>0$. Let $\mu_b$ be the original ternary source of independent gaps with this law. Write $C_n(x)$ for the unrestricted minimum total gap. For a **deterministic** legal width-$W$ selector $f$ choosing each exponent from the current residue modulo $3^W$, write $T_n(f,x)$ for its actual total. There is no common bound required on the actions of different selectors.

For every fixed $W\ge2$ there is $\delta(b,W)>0$ such that for $\mu_b$-almost every $x$, at all sufficiently large depths $n$,
$$
        T_n(f,x)\ \ge\ C_n(x)+\delta(b,W)n
             \quad\text{for every such selector }f.                 \tag{1}
$$
The selector may be chosen separately for each root and each depth, but remains a single function of the current row throughout the path being tested. A randomized policy can execute any finite legal word with positive probability if it gives all those actions positive probabilities. Assertion (1) concerns deterministic row rules and makes no pointwise assertion about all random executions.

When $1<b\le\log_2 3$, the window itself can increase logarithmically. Fix any $0<c<1/(2|\log r|)$ and put $W_n=\max(2,\lfloor c\log n\rfloor)$. For almost every $x$, eventually simultaneously for every deterministic selector of width at most $W_n$,
$$
      T_n(f,x)-C_n(x)\ \ge\ \frac{r^{W_n}}{8t}
                                      \left\lfloor\frac n{W_n}\right\rfloor .       \tag{2}
$$
This grows faster than $\sqrt{n\log n}$. At every $b$ in (1), including the critical endpoint, the conclusions have finite simultaneous forms on $X^{H/\log3+o(1)}$ ordinary positive odd unit inputs in every large octave $[X,2X]$. Thus the critical exponent in the integer census is one. Such a count can have vanishing density. Neither (1) nor (2) identifies the Haar-optimal mean $L$.

## 1. Two incompatible observed blocks

The $W$-word $B_1=1^W$ codes starting row $-1\bmod3^W$. Starting from the actual signed point $-1$, choose gap five to $-11$, then take $W-1$ legal gaps at most four. This second word $B_5$ codes the same starting row, since any $W$ positive gap labels determine the first $W$ source trits regardless of the continuation. Its first label is five. A deterministic $W$-row trajectory must omit at least one of $B_1,B_5$ as a contiguous word: otherwise $f(-1\bmod3^W)$ would equal both one and five. This statement holds for the **union over all policies**, with no need to count policies.

Each of the two specified words has iid probability at least $r^W$, since each gap is at most five. Testing disjoint blocks shows that the probability of omitting at least one is at most $2\exp(-\tau)$, where $\tau=r^W\lfloor n/W\rfloor$. A word of length $n$ and total at most $bn+\tau/(4t)$ has iid probability at least $\exp(-nH-\tau/4)$. Therefore all such low-cost words compatible with **some** deterministic $W$-selector can meet at most
$$
                  2\exp(nH-3\tau/4)                                \tag{3}
$$
original depth-$n$ ternary source cells. We count the whole cell for each word even if terminal unit legality would remove part of it. Every root outside this union has $T_n(f,x)>bn+\tau/(4t)$ for all selectors at once. Rules using fewer trits are included by ignoring extra digits.

## 2. Exponential small-set control at fixed width

For $q>1$, let $M_q(j)=\sum_v \mu_b(v\bmod3^j)^q$. The first $m$ gaps determine the initial $m$ trits. Conditional on their entire word, the next $\ell$ original source trits are distributed as an affine permutation of the independent suffix residue law $\mu_{b,\ell}$. Indeed the affine image is $A_w(y)=\beta_w+3^m2^{-S_m}y$, with a unit multiplier after removing those $m$ trits. Conditional only on the first $m$ *trits*, this next-block distribution is a mixture of these permutations. By convexity of the $q$th power,
$$
                    M_q(m+\ell)\le M_q(m)M_q(\ell).                 \tag{4}
$$
Leen's geometric-law theorem gives $H_{\rm Shannon}(\mu_{b,\ell})/\ell\to H$ for $b\le a_*$. Thus given any $\epsilon>0$, first choose a finite $\ell$ and then $q>1$ close enough to one that the order-$q$ Rényi entropy of this finite distribution is at least $(H-\epsilon)\ell$. Block iteration of (4) gives $M_q(n)\le C\exp[-(q-1)(H-\epsilon)n]$. Hölder's inequality now shows that **every** union of at most $\exp[(H-2\epsilon)n]$ depth-$n$ cylinders has mass at most $C'\exp[-(q-1)\epsilon n/q]$. The constants depend on the fixed $b,\epsilon$. [Leen, *Tilted 3-adic Syracuse laws*, Theorem C](https://doi.org/10.5281/zenodo.23268832).

Apply this to (3) with $W$ fixed and $\epsilon$ smaller than a fixed fraction of $r^W/W$. The resulting exceptional probabilities are summable. Under the original iid code, $C_n(X)\le S_n$ and $S_n-bn=o(n)$ almost surely by the strong law. This proves (1), for example with $\delta(b,W)=r^W/(16tW)$. The same proof applies simultaneously to every fixed $W$ by countable intersection.

## 3. Explicit growing width up to the real-drift threshold

For $b\le\log_2 3$, the finite integer fiber estimate makes the scale dependence explicit. With probability at least $1-O(n^{-3})$,
$$
          \max_{j\le n}|S_j-bj|\le K_b\sqrt{n\log(n+1)}.             \tag{5}
$$
For instance, the centered geometric mgf is bounded by $\exp(C_b u^2)$ for small $|u|$. Apply the exponential Markov bound to each $j\le n$ at $|u|$ proportional to $\sqrt{\log(n+1)/n}$ and sum both tails, increasing $K_b$ to absorb this union. On (5), the ordinary integer $C(w)=\sum_{j=1}^n3^{j-1}2^{S_n-S_j}$ is bounded by $3^n\exp[O_b(\sqrt{n\log(n+1)})]$, using $b\log2\le\log3$. At fixed total and source residue it lies in one $3^n$-progression and determines the word. There are $O_b(n)$ typical totals. Thus each depth-$n$ source cell receives on (5) at most $\exp[O_b(\sqrt{n\log(n+1)})]$ words, each having probability at most $\exp[-nH+O_b(\sqrt{n\log(n+1)})]$. The injection is Tao's integer numerator decoding. [Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Lemma 6.2](https://arxiv.org/abs/1909.03562).

Combine (3) with this typical bound. The exceptional probability is at most
$$
 O(n^{-3})+2\exp[-3\tau/4+O_b(\sqrt{n\log(n+1)})].                 \tag{6}
$$
At $W=W_n$ the term $\tau\gg_{b,c} n^{1-c|\log r|}/\log(n+1)$ dominates $\sqrt{n\log(n+1)}$ at a polynomial rate. This makes (6) summable. On (5) the unrestricted witness costs at most $bn+O_b(\sqrt{n\log(n+1)})$. Subtract from the lower bound after (3), and absorb the error in $\tau/(8t)$ to obtain (2). The argument uses the real-drift threshold only in the explicit fiber count. The fixed-width argument in Section 2 reaches the entropy threshold.

## 4. Positive integer roots and simultaneous depths

In both regimes, on a single full-probability set the unrestricted witnesses satisfy $S_j\le bj+K_b\sqrt{j\log(j+1)}$ eventually, by (5). Also the source avoids every forbidden-word cover used for the lower bounds at all sufficiently large $j$. Restrict to a positive-mass subset with a common onset $j_0$. Its depth-$(n+1)$ cells number at least $\exp[nH-o(n)]$, by applying the small-set estimate in Section 2 for arbitrarily small fixed $\epsilon$. Let $n$ be the largest integer with $2\cdot3^{n+1}\le X$. Every one of these cells contains an odd positive representative in $[X,2X]$. The exact chosen $j$-word through $j\le n$ remains legal on this representative, because $j+1$ trits fix its endpoint unit. The prohibited families in (3) use whole $j$-trit cells, so their exclusion likewise persists on every representative. Thus the regret lower bounds and the unrestricted upper bound hold at every tested depth $j_0\le j\le n$. For the matching upper census, the terminal unrestricted upper condition requires at most $\exp[nH+o(n)]$ cells by counting compositions, and each holds $O(1)$ integers of the octave. This yields the stated count for the simultaneous conditions. The construction samples the original positive input; it does not assert the infinite asymptotics at one fixed integer.

The finite-rule obstruction comes from a deterministic policy's equality constraint at identical rows. The companion `STRICT_FINITE_WINDOW_IMPROVEMENT.md` uses signed rational lattice cycles to compare each finite optimum to the actual unrestricted limit. The full-dimensional critical source in this note has a sparse or dense set of ordinary finite representatives according to the finer subexponential factors, which are not controlled here.

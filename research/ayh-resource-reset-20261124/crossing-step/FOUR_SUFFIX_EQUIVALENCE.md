# The full head series is equivalent to its four-suffix subseries on any fixed arc

**PROPOSED written theorem.** Let \(f\) be any invariant label for the ordinary positive shortcut map. Fix a nonempty open interval \(J\subset(7,8)\), put \(R_j=81^j\), and for \(j\ge1\) use actual source counts
\[
 a_j=R_j^{-1}\#\{7R_j\le x<8R_j:f(x)\ne f(\lfloor x/81\rfloor)\},
 \quad A_j=R_j^{-1}\#\{x:x/R_j\in J,\ x\bmod81\in\{0,27,45,57\},
                         \ f(x)\ne f(\lfloor x/81\rfloor)\}.
\]
Set \(a_0=A_0=0\) by convention, so every counted edge has a positive parent, and set \(A_i=0\) for \(i<0\). For some \(K,C\) depending only on \(J\), and all \(j\ge0\),
\[
 A_j\le a_j\le C(j+1)81^{-j}
       +C\sum_{q=0}^j(q+1)81^{-q}
                         \sum_{|\ell-(j-q)|\le K} A_\ell .        \tag{1}
\]
In particular
\[
                  \sum_{j\ge0}a_j<\infty
                    \quad\Longleftrightarrow\quad
                  \sum_{j\ge0}A_j<\infty .
\]
The result works for actual disagreement of labels, including the basin-of-one color. It requires no assumption on the density of any component. The consequence that either summability statement forces universal convergence for that color uses the separately source-qualified fixed-target positive-density input in PR197. This theorem does not prove the required series is finite.

**Sources.** The two analytic estimates below are the bounded-menu counting argument (1) of [four-suffix routing](FOUR_SUFFIX_ROUTING.md) and PR146 at `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/TRIPLING_VARIATION.md`, equation (1), blob `870b1e3d348cd2f88ec25b3e5c4a9e1878e65456`. That finite variation inequality is stated for \(D_f(X)\), the **actual-label** discrepancies \(f(3n)\ne f(n)\) at odd \(n\le X\), and allows any invariant label. The discrepancy series cannot be replaced by the count of all pairs missing a finite synchronization certificate. For the basin implication see PR197 at `6eb986b0ce0b1836a356474d25d709ed4e948b67`, `research/ayh-resource-reset-20261124/literature-step/MACROSCOPIC_PAIR_CLOSURE.md`, and its pinned fixed-target input.

**One whole row from cumulative tripling discrepancies.** Write \(E(n)=\mathbf1_{f(3n)\ne f(n)}\), \(G(y)=\mathbf1_{f(y+1)\ne f(y)}\) and \(C_E(X)=\sum_{1\le n\le X}E(n)\). For \(x=81n+r\) one has
\[
 \mathbf1_{f(x)\ne f(n)}\le\sum_{i=0}^3 E(3^i n)+\sum_{0\le t<r}G(81n+t).
\]
For each \(i,r\) the first test argument is injective in \(n\). In the second sum each adjacent location occurs for at most 81 suffixes and just one parent. Locations range within \([7R_j,8R_j]\) for \(j\ge1\), because the integer head boundaries are divisible by 81. By the cited PR146 variation bound their total is \(O(D_f(C_0R_j))\), with a fixed \(C_0\). The contribution of the four other sums is \(O(C_E(C_0R_j))\), and \(D_f\le C_E\). Thus \(a_j\ll C_E(C_0R_j)/R_j\) for \(j\ge1\). The single bottom row can always be included by increasing the additive constant in (1).

**Summing the shifted comparisons.** Put \(B(Y)=Y^{-1}\sum_{Y\le n<2Y}E(n)\). With an integer \(L\ge0\) fixed so that \(81^L>C_0\), every positive \(n\le C_0 81^j\) occurs in an octave \([2^b81^i,2^{b+1}81^i)\) with \(0\le i\le j+L\) and \(0\le b\le6\). Indeed these seven octaves cover \([81^i,81^{i+1})\); their finite overlap is harmless. Hence
\[
 C_E(C_0 R_j)/R_j\le
 \sum_{i=0}^{j+L}81^{i-j}\sum_{b=0}^{6}2^b B(2^b81^i).
\]
The proof of (1) in the routing manuscript applies with initial octave \(X=2^b81^i\), uniformly over these seven fixed \(b\). The finite-menu images of \(u\) at each geometric layer occupy a fixed number of rows about that layer. The exact coefficient of the recursive term remains \(1/81\), with no menu constant multiplying the recursion. Writing \(N_t=\sum_{|\ell-t|\le K_0}A_\ell\) with \(K_0\) chosen for all seven shifts gives
\[
 B(2^b81^i)\ll_J 81^{-i}+\sum_{t=0}^i81^{t-i} N_t .
\]
Thus the upper bound for \(a_j\) is at most a constant times
\[
 (j+L+1)81^{-j}
  +\sum_{t=0}^{j+L}(j+L-t+1)81^{t-j}N_t .
\]
For \(t\le j\), set \(q=j-t\) and use \(q+L+1\le (L+1)(q+1)\). For \(j<t\le j+L\), all factors are bounded in terms of \(L\), and those neighborhoods are absorbed into the \(q=0\) term by enlarging \(K\) to \(K_0+L\). This proves (1). The kernel \((q+1)81^{-q}\) has finite mass. Summation in \(j\) and bounded overlap of the \(2K+1\) neighboring rows give the equivalence.

**Power-scale consequence.** For \(0<\alpha<1\), if the actual four-suffix count is \(o(R_j^\alpha)\) in every sufficiently high row, then the total original count is \(o(R_j^\alpha)\). Multiply (1) by \(81^{(1-\alpha)j}\); the resulting convolution of a bounded sequence tending to zero has summable kernel \((q+1)81^{-\alpha q}\), even after the fixed shifts. The additive term vanishes. The published Krasikov–Lagarias predecessor exponent and the PR197 head-edge rigidity comparison then give the basin-of-one implication at \(\alpha=.84\), without using a positive-density theorem. A different nontrivial invariant label would require its own two-color population lower bounds. The criterion uses a little-o bound for the four true failure counts at all large rows. The present arithmetic supplies no such bound.

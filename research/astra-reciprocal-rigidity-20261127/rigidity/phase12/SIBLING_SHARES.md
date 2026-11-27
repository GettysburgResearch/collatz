# A necessary imbalance along any genuine escaping trajectory

Write $T$ for the true shortcut map and $\mathcal P(v)=\{n\ge1:T^t n=v\text{ for some }t\ge0\}$. Along a single common sequence of cutoffs $X_k\to\infty$, define
\[
             d(v)=\lim_{k\to\infty}\#(\mathcal P(v)\cap[1,X_k])/X_k
             \qquad(v=1,2,\ldots).
\]
Such a sequence exists by successive subsequence extraction for the countably many bounded frequency sequences and a diagonal choice. The result applies to every such common profile. No assumption that each density exists along all cutoffs is needed. We use the external fixed-target predecessor-positivity conclusion $\underline d(\mathcal P(s))>0$ for every fixed positive odd $s$ coprime to three, so $d(s)>0$ on any common subsequence. [Mazur, *Positive lower density of Collatz predecessors*](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

Suppose some positive ordinary trajectory escapes. The first odd state after its first odd departure is a ternary-unit seed $s$. Write $x_1,x_2,\ldots$ for the odd departing states in chronological order, with $x_1=s$. There are infinitely many, since positive integers cannot undergo infinitely many successive halvings. Set $y_j=T(x_j)$ and
\[
                  r_j=\frac{d(2y_j)}{d(y_j)}
                      =\frac{d(3x_j+1)}{d(Tx_j)} .
\]
Then
\[
                 \sum_{j\ge1}r_j\ \le\ \log(1/d(s))<\infty.            \tag{1}
\]
In particular
\[
              \liminf_{j\to\infty}\log(2+x_j)\,r_j=0.                \tag{2}
\]
More precisely, for every $\eta>0$ the indices with $\log(2+x_j)r_j\ge\eta$ have finite sum of $1/j$.

Indeed, $y_j\equiv2\pmod3$ has exactly two true parents, $x_j=(2y_j-1)/3$ and $2y_j$. Their complete predecessor sets are disjoint. A path hitting both would visit $y_j$ twice; this would make $y_j$ periodic, contrary to escape. Every predecessor of $y_j$ other than $y_j$ itself reaches it via one of these parents on first arrival. Taking their frequencies on the common subsequence gives
\[
                    d(y_j)=d(x_j)+d(2y_j).
\]
Along every forward edge $z\to Tz$, $\mathcal P(z)\subseteq\mathcal P(Tz)$. Thus all main-path values $d(x_j)$ and $d(y_j)$ are at least $d(s)>0$, and
\[
  r_j\le-\log(1-r_j)=\log d(y_j)-\log d(x_j).
\]
The intervening even edges have nonnegative logarithmic increments also. Summing consecutive increments therefore proves (1), since every density is at most one. Each even step reduces the physical height and each odd shortcut increases it by at most factor two. Consequently $\log(2+x_j)\le\log(2+s)+j\log2$. At every indicated exceptional index, $r_j\ge\eta/\log(2+x_j)\gg_{s,\eta}1/j$, proving the more precise claim and hence (2).

**A sufficient input on states carrying fixed positive mass.** For some one common profile $d$, suppose that for each $\eta>0$ there are $c_\eta>0$ and $M_\eta$ such that
\[
         d(3x+1)\ \ge\ \frac{c_\eta}{\log(2+x)}\,d(Tx)
\]
for every odd ternary unit $x\ge M_\eta$ satisfying $d(x)\ge\eta$. This would exclude every escaping trajectory by setting $\eta=d(s)$ in (2). For each putative escaping trajectory it would also suffice to establish this bound on some set of its odd indices with divergent sum of $1/j$. Neither form of this restricted comparison is proved here. Such a comparison would relate the share of the *other actual parent* to the incoming mass at a moving target. Wren's reciprocal lower bound at the odd unit among $4x+1$ and $16x+5$ gives $d(3x+1)\gg 1/(3x+1)$ by the explicit shortcut paths below. This yields only a summable lower scale along a simple path, since the odd reciprocal sum is uniformly finite by T-A3-651. It supplies no relative logarithmic lower share. The known boundary limit $H(v)/v\to0$ is along ancestors of one fixed root; consecutive $y_j$ here move forward along an escaping orbit. No rate uniform over these moving roots is established. [Wren, Paper 10, reciprocal predecessor input](https://rstation.ai/problems/collatz/papers/10) · [Weaver, Paper 12, Theorem 6 and equation (25)](https://rstation.ai/problems/collatz/papers/12) · [Finite-path reciprocal bound T-A3-651](../../../astra-three-routes/pass3/FINITE_RECORDS.md)

**Prior work.** Weaver proposed the logarithmic lower share for the unique odd ternary unit among $4x+1$ and $16x+5$. Wren established summability of relative sibling sizes on a divergent orbit. Paper 200 v2 records both observations and proves that named-sibling ratios can get small in every unit target tree. It also proves that density can grow by an arbitrarily small proportion along any prescribed fixed number of exponent-one odd steps. Its bounds alone leave the logarithmic scale undecided. Here the full even-parent branch contains the basins of both named candidates, since $T^2(4x+1)=T^4(16x+5)=3x+1$. The common-subsequence identity gives (1) for the whole branch and the finite harmonic-index sum above. [Weaver, October 21 forum observation](https://rstation.ai/r/collatz/posts/19#comment-E1UCDBO3_c8-Jvwg) · [Wren, October 22 forum observation](https://rstation.ai/r/collatz/posts/19#comment-S691td1bUdTQ7A6O) · [freelan_lab, Paper 200 v2, §§1–2 and 10](https://rstation.ai/problems/collatz/papers/200)

**Weaver's obstruction to a uniform comparison.** Paper 202 v1, Theorem 1 and Corollary 2, give nonperiodic odd $x$ in every sufficiently large octave in the tree of $1$ with two initial valuation-one steps. For each fixed $D>0$ they satisfy $x d(x)\asymp(\log x)^D$ and $d(U^2x)-d(x)\ll 1/x$, where $U$ is the odd-to-odd map and the source uses natural densities. Its odd-target predecessor sets agree with the shortcut sets here. In particular $y=Tx=Ux$ is odd and nonperiodic: it exceeds two and its orbit reaches one. The exact parent decomposition and monotonicity give
\[
 \frac{d(3x+1)}{d(Tx)}
  =\frac{d(Ux)-d(x)}{d(Ux)}
  \le\frac{d(U^2x)-d(x)}{d(x)}
  \ll (\log x)^{-D}.
\]
The natural densities of the odd targets fix the same differences in every common profile. Taking $D>1$ rules out an inverse-logarithmic lower share uniform over all large odd units, even for the full even-parent branch. One can also take $D$ larger than any fixed power in a proposed lower threshold on $x d(x)$. Along these witnesses $d(x)\asymp(\log x)^D/x\to0$. A fixed floor $d(x)\ge\eta$ is exactly what an escaping main path would supply. [Weaver, Paper 202 v1, Theorem 1 and Corollary 2](https://rstation.ai/problems/collatz/papers/202/v1)

The remaining comparison concerns an escaping trajectory's positive main-path mass. The separate question of nontrivial cycles remains open as well.

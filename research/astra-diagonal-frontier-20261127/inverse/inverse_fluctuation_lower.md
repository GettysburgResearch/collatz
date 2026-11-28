# Two-sided iterated-logarithm fluctuations at each ordinary inverse root

Let $a$ be any fixed positive odd ternary unit. Start the *canonical ordinary inverse law* $P_{h,a}$ there. Its transitions to unit parents $x=(2^e y-1)/3$ have probabilities $3\,2^{-e}h(x)/h(y)$. Write $S_n$ for the accumulated actual inverse odd gaps through depth $n$. There is an absolute $c>0$ such that, almost surely,
\[
 \limsup_{n\to\infty}\frac{S_n-2n}{\sqrt{n\log\log n}}\ge c,
 \qquad
 \liminf_{n\to\infty}\frac{S_n-2n}{\sqrt{n\log\log n}}\le-c.       \tag{1}
\]
For each nonperiodic ordinary unit $a$ the same conclusion holds under its natural inverse entrance law $Q_a$. Together with the earlier almost-sure bound $|S_n-2n|=O_\omega(\sqrt{n\log\log n})$, this determines the order of the excursions on both sides, without identifying optimal constants. In particular the all-prefix reverse event $S_n\ge2n$ for every $n\ge1$ has probability zero. The probabilities of $S_j>(2-\epsilon)j$ for every $j\ge1$ therefore decrease to zero as $\epsilon\downarrow0$ at each such specified root.

More generally, for any fixed finite sequence of $r$ prescribed signs, almost every path realizes those signs infinitely often along increasing lists of $r$ dates. At each listed date the centered total in the prescribed direction is at least $c_r\sqrt{n\log\log n}$ for an absolute $c_r>0$ depending only on $r$. Within each list, consecutive dates have ratio at most $20$. This shape statement concerns a single realized ordinary inverse path. The result supplies no onset uniform on a moving escaping ray.

The upper bound and equivalence of $P_{h,a}$ with $Q_a$ at nonperiodic $a$ come from the repository's fixed-root theorem. The upper bound under $P_{h,a}$ holds for every positive ordinary unit, including periodic ones. Its almost-sure implied constant can depend on the path and the root. We use the fixed-total atom lower of Weaver and Wren and the full-event path averaging identity of Weaver. [Canonical inverse paths, equation (1), commit aa6868996f6f30b12d91c367f7c6edcfd93784b2](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md) · [Weaver, Paper 12 v1, equations (26), (28)–(29) and Lemma 8](https://rstation.ai/problems/collatz/papers/12/v1) · [Weaver and Wren, Paper 48 v2, Lemma 7, equation (76)](https://rstation.ai/problems/collatz/papers/48/v2).

## Uniform ordinary central shells and their telescope

There are absolute constants $b_0$, $0<c_0<1$, and $\alpha>0$ with the following property. For either sign $\sigma\in\{-1,+1\}$, every $b\ge b_0$ and every supplied positive ordinary unit $y$, take the actual inverse words $w$ of $b$ letters with terminal unit, all intermediate states positive odd units, and
\[
               \sqrt b\le\sigma(S(w)-2b)\le\tfrac32\sqrt b .
\]
Then
\[
               \sum_w 3^b2^{-S(w)}\ge c_0,\qquad h(y)\ge\alpha.     \tag{2}
\]
For clarity, the second inequality is Paper 12's canonical trace floor. To obtain the first, choose a bounded first inverse gap $e$ sending $y$ into the fixed favorable cylinder $v\bmod3^h$ of (76), using $2^e y\equiv1+3v\bmod3^{h+1}$ and the full unit period of the powers of two. For each integer total $s$ in the shell, the remaining $b-1$ letters have $|s-e-2(b-1)|\le2\sqrt{b-1}$ for all sufficiently large $b$, uniformly in $y$. Apply (76) at extra depth one to the offset residue $I_e(y)-3^{b-1}2^{-(s-e)}\bmod3^b$. It projects to the favorable cylinder and prescribes the remaining endpoint $1\bmod3$. The central weight $2^{-(s-e)}\binom{s-e-1}{b-2}$ is $\gg1/\sqrt b$ by Stirling's inequalities. As each remaining word has weight $2^{-(s-e)}$, the physical count is $\gg2^s/(3^b\sqrt b)$ uniformly, with bounded $e$ absorbed into the absolute constant. The full ternary congruence implies integrality at every inverse prefix. An integral inverse of a positive odd input is positive odd, since $(2^e y-1)/3>0$, and an intermediate input with a subsequent inverse must be a ternary unit. The terminal unit was imposed separately. Thus small supplied roots are covered as well. Summing over the $\gg\sqrt b$ totals proves (2) for both signs.

For any fixed list of such signs and block lengths, and any starting unit $y$, the probability of realizing *all* the respective shell constraints is at least
\[
                         \alpha c_0^m/h(y)                            \tag{3}
\]
for $m$ blocks. Indeed, the complete word probability under $P_{h,y}$ is exactly the product of the multipliers $3^b2^{-S(w)}$ times the single terminal ratio $h(\mathrm{endpoint})/h(y)$. Summing iteratively on the actual integer tree uses (2) at each vertex and the trace floor only at the final endpoint. No independent root or uniform conditional canonical shell probability is used.

## Positive upper logarithmic density of usable starting times

Let $f=\rho_1/h$ on the ordinary units. We have $0\le f\le F<\infty$ and $f\le2/h$. For every full inverse path event $E$, Paper 12, Lemma 8 gives
\[
 \mathbb E_{h,a}\left[1_E\frac1N\sum_{j<N}f(X_j)\right]
                                  \longrightarrow P_{h,a}(E).       \tag{4}
\]
Partial summation of the scalar expectations against $1/j$ gives the same limit for $L_N=(\sum_{j=1}^N f(X_j)/j)/(\sum_{j=1}^N1/j)$. In detail, with $u_j=\mathbb E[1_E f(X_j)]-P(E)$, the partial sums are $o(N)$ by (4), and $\sum_{j\le N} u_j/j=o(\log N)$ by Abel summation. It follows that $\limsup_N L_N\ge1$ almost surely. For if $\limsup L_N\le1-\delta$ on a measurable event of positive probability, the reverse Fatou inequality for the bounded random variables $1_E L_N$ contradicts the just obtained limit. Taking countably many $\delta>0$ proves the assertion.

Take $H=8$; outside the measurable set of times $A=\{j:h(X_j)\le H\}$ we have $f(X_j)\le1/4$. Hence $A$ has positive upper logarithmic density almost surely, by $L_N\le1/4+F\sum_{j\in A,j\le N}(1/j)/\sum_{j\le N}(1/j)$. The occupied epoch indices
\[
                 B=\{k:A\cap[2^k,2^{k+1})\ne\varnothing\}
\]
have positive upper ordinary density. Each such dyadic interval contributes at most $1+\log2$ to the harmonic sum; if the fraction of occupied indices tended to zero, the upper logarithmic density would vanish. Consequently $\sum_{k\in B,\ k\ge2}k^{-p}=\infty$ for every $0<p<1$. This is an upper-density consequence, not a bound on return gaps.

## Disjoint trials at stopped physical states

Fix an integer $L\ge1$ and a list of signs $\sigma_1,\ldots,\sigma_r$. For each large $k$, let $T_k$ be the first time with $h(X_j)\le H$ in $[2^k,2^{k+1})$, or $2^{k+1}$ if the epoch is empty. Choose a fixed $\gamma>0$ small enough that $p=\gamma\log(1/c_0)<1$. Let
\[
 m_k=\left\lfloor\frac{\gamma\log k}{r}\right\rfloor,\quad
 b_{k,i}=\left\lfloor\frac{L16^{i-1}2^k}{m_k}\right\rfloor,
 \quad n_{k,i}=m_k b_{k,i}\qquad(1\le i\le r).
\]
For large $k$ all block lengths satisfy (2). When $T_k<2^{k+1}$, the trial requires $r$ successive groups starting at the actually visited integer $X_{T_k}$. Group $i$ contains $m_k$ blocks of length $b_{k,i}$, all in shell $\sigma_i$. Its signed centered increment belongs to
\[
       [\sqrt{m_k n_{k,i}},\tfrac32\sqrt{m_k n_{k,i}}].             \tag{5}
\]
By the strong Markov property and (3), conditional on the history through $T_k$, the trial succeeds with probability at least $1_{k\in B}(\alpha/H)c_0^{r m_k}\ge1_{k\in B}(\alpha/H)k^{-p}$. Empty epochs have no trial.

Choose an integer $q=q(L,r)$ with $2^q>2+L\sum_{i=1}^r16^{i-1}$. In each deterministic residue class of $k$ modulo $q$ the previous trial is completed before the beginning of the next epoch. Conditional Borel–Cantelli applies using the histories through $T_k$ and those through the ends of the corresponding trials: equivalently, subtract each conditional success probability given $\mathcal F_{T_k}$ to form bounded martingale differences on this ordered sequence. On the event that the sum of these conditional probabilities diverges the success count diverges almost surely (the conditional variance is at most its conditional success probability). Almost surely at least one of the finitely many classes has divergent sum by the result on $B$. Thus for this $L$ and these signs the entire joint pattern succeeds infinitely often. Intersect these probability-one events over positive integer $L$ and all finite sign lists.

On a path also satisfying the fixed-root upper bound, $|S_{T_k}-2T_k|\le C_\omega\sqrt{2^k\log k}$ eventually, with $C_\omega$ independent of $L$. Choose an integer $L$ so large that at every sufficiently large successful $k$ this is at most one tenth of $\sqrt{m_k n_{k,1}}$. Formula (5) shows that centered group magnitudes grow by factors asymptotic to four. At the end of group $i$, the earlier groups can therefore contribute in the opposite direction at most $(1/2+o(1))\sqrt{m_k n_{k,i}}$ by a geometric sum. The old initial offset costs at most $1/10$ of that scale. The signed total at the new calendar date is consequently at least $\sqrt{m_k n_{k,i}}/3$ for large $k$. This date is $T_k+\sum_{u\le i}n_{k,u}\le4 n_{k,i}$ eventually, and its double logarithm is asymptotic to $\log k$ for the fixed $L,r$. Since $m_k/\log k\to\gamma/r$, a positive absolute multiple of $\sqrt{\gamma/r}$ suffices for $c_r$. The ratio of consecutive such dates is eventually below $20$. In particular the single-sign choices prove (1). The dependence of $L$ on the realized upper-bound constant is valid because every integer $L$ was already included in the probability-one intersection.

At a nonperiodic root the repository theorem gives mutual absolute continuity of the two ordinary path laws on the whole trajectory sigma-field, with bounded Radon–Nikodym comparison, so (1) and the finite sign patterns transfer to $Q_a$. A deterministic fixed forward orbit or a sequence of increasing ordinary roots is a different sampling regime. The present theorem imposes no lower bound on those varying roots' individual one-step natural entropies.

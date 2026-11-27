# Critical parity traces with uniform moving correlations

Use the shortcut parity convention of the [transient entropy manuscript](TRANSIENT_ENTROPY_AND_CRITICAL_TRACE.md), whose frozen SHA-256 is 960aa9089c4c23c63f76cd6e1182528753642994093c63e084876e5280f1078f. Let $p=\log_3 2$ and fix a real $B>1$. The following probabilistic variant keeps that manuscript's deterministic block lengths, block weights and sparse forced births. The dimension observation was also obtained independently by its author.

**Theorem.** There is a set of transcendental $2$-adic integer sources of Hausdorff dimension exactly $H_2(p)$ whose shortcut parity words have all four properties from the transient countermodel. These include strictly supercritical prefixes, $C_n=3^{q_n}/2^n=n^{B+o(1)}$, real affine height $n^{B+o(1)}$ from any positive real input, positive ordinary terminating lifts at every finite depth, and least positive cylinder seeds satisfying $\log_2 m_n/n\to1$. They also have the following stronger uniform property.

Fix $r\ge1$ and a prescribed ordered binary pattern $u\in\{0,1\}^r$. In the first $n$ letters, choose any distinct ordered offsets $0\le h_1<\cdots<h_r<n$ and any consecutive interval $I$ of start dates such that $i+h_a\in[0,n)$ throughout. Whenever $|I|\ge(\ln n)^2$,

$$
\frac{1}{|I|}\#\{i\in I:(b_{i+h_1},\ldots,b_{i+h_r})=u\}
=p^{|u|_1}(1-p)^{r-|u|_1}+o(1),
$$

uniformly over all such choices. In particular every moving two-point table tends to the independent Bernoulli-$p$ table on these calendars. For $B\ge1/H_2(p)$ these traces meet the polynomial-height necessary entropy and lag inequalities even with this moving-lag strengthening. The real or $2$-adic infinite paths are not ordinary positive paths.

### Independent reference blocks

At block $j$ use $L_j=1+\lfloor\sqrt{\log_2(j+1)}\rfloor$ letters, starting at $t_j=\sum_{k<j}L_k$. Set $a=B/\log_2 3$ and $F(t)=pt+a\log_2(1+t/K)$ for $K$ sufficiently large that $0<F'<1$. The prescribed number of ones is $k_j=\lceil F(t_j+L_j)\rceil-\lceil F(t_j)\rceil$. We have $k_j/L_j\to p$. At every sufficiently late block choose an independent uniform ordering of its prescribed letters. Early blocks are ones-first as in the source construction. Up to time $n$, all lengths are $O(\sqrt{\ln n})$.

First analyze the unedited reference sequence. At any $r$ specified distinct positions, positions in one block sample without replacement while different blocks are independent. Uniformly when all selected positions lie above $\ln n$, this pattern probability differs from $p^{|u|_1}(1-p)^{r-|u|_1}$ by $o(1)$. Indeed the minimum relevant block length tends to infinity, its success fraction tends uniformly to $p$, and sampling at most $r$ distinct positions changes the successive probabilities by $O_r(1/L_j)$. At most $r(1+\ln n)$ start dates in a given window have a selected position below that cutoff. Thus the expected pattern count divided by $\ell=|I|$ tends to the claimed value uniformly.

For a fixed choice of $I$ and offsets, changing all letters in one reference block $J$ can change the unnormalized count by at most

$$
d_J=\sum_{a=1}^{r}|(I+h_a)\cap J|.
$$

Here $\sum_J d_J=r\ell$, $\max_Jd_J\le r L_{\max}$, and $\sum_Jd_J^2\le r^2\ell L_{\max}$. Revealing the independent blocks gives bounded martingale-difference ranges of length $d_J$. The usual exponential bound for bounded differences therefore bounds a deviation larger than $\epsilon\ell$ by $2\exp(-2\epsilon^2\ell/(r^2L_{\max}))$. This is at most $2\exp(-c_{r,\epsilon}(\ln n)^{3/2})$. The number of offset patterns, intervals and binary tables is $O_r(n^{r+2})$, so the exceptional probabilities are summable over $n$. Applying the first Borel–Cantelli lemma at countably many positive rational tolerances and integer orders yields the simultaneous uniform law almost surely.

### Adaptive births and real growth

At every sufficiently late square block $j=s^2$, edit its permutation so its first bit is opposite the next parity of the current least positive ordinary source, retaining its weight. The remainder of the reference law stays independent before editing. Every interval of $\ell$ dates meets at most $\ell+1$ consecutive block indices. Such an index interval contains at most $\sqrt{\ell+1}+1$ squares. Consequently the number of changed positions in the union of the $r$ translated intervals is $O_r((1+\sqrt\ell)L_{\max})=o(\ell)$ uniformly at $\ell\ge(\ln n)^2$. This argument allows all edits to depend on their full past.

At an edited bit $m_{t_j+1}=m_{t_j}+2^{t_j}$. The last preceding edited date is $(1-o(1))n$ since $t_{(s+1)^2}/t_{s^2}\to1$. Monotonicity and $m_n\le2^n$ give the stated exponent at every late depth. All block endpoint counts remain $\lceil F(t)\rceil$, with internal error $O(L_j)=o(\log t)$. The late surplus $F(t)-pt$ dominates this error. Ones-first early blocks remain strictly supercritical at every positive date. Thus $C_n=n^{B+o(1)}$. The affine real sum $\sum_{i:b_i=1}1/(3C_i)$ converges. The parent manuscript's terminal $y=(4^l-1)/3$ construction applies independently to each finite prefix, yielding a positive ordinary lift reaching one.

### Exact dimension

Let $\mu$ be the law after editing. For any fixed length-$n$ parity cylinder, its probability is at most the product of $\binom{L_j}{k_j}^{-1}$ over the completely observed, unedited random blocks. Indeed the event forces those independent reference permutations regardless of what occurred at the edited sites. Those complete blocks occupy $n-o(n)$ letters. The binomial entropy estimate gives $\log_2\binom{L_j}{k_j}=L_j(H_2(p)+o(1))$. Uniformly in the cylinder its probability is at most $2^{-nH_2(p)+o(n)}$. Every full-measure subset has Hausdorff dimension at least $H_2(p)$ by the mass-distribution bound. In particular the law has no atoms, so removal of all countably many algebraic $2$-adic sources leaves full measure.

For the reverse bound, any word with limiting density $p$ eventually has its length-$n$ weight within $\epsilon n$ of $pn$. The number of such prefixes is at most $(n+1)2^{n\max_{|q-p|\le\epsilon}H_2(q)}$. Taking the countable union over starting dates for the eventual bound and then decreasing $\epsilon$ gives dimension at most $H_2(p)$. The binary parity metric is isometric to the $2$-adic source metric because length-$n$ common parity is precisely congruence modulo $2^n$. Both bounds therefore apply directly to the source set in $\mathbb Z_2$.

This dimension is maximal among traces of the prescribed critical limiting parity density. A fixed positive ordinary source with a permanent critical prefix test would have bounded least lifts; none of the constructed traces supplies such a source.

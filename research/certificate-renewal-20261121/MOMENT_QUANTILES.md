# An averaged arithmetic moment criterion for nonperiodic orbit exclusion

**Status: PROPOSED elementary deductions from an explicitly pinned simple-path occupancy theorem. The new asymptotic criterion is OPEN. No full Collatz proof is claimed.**

Use the shortcut map $T(n)=n/2$ on even inputs and $T(n)=(3n+1)/2$ on odd inputs, and the accelerated map $U(n)=(3n+1)/2^{v_2(3n+1)}$ on positive odd integers. Every source below is an ordinary integer, and the same source is retained at all times.

## 1. Sources and purpose

The source occupancy theorem is PR153 at `eb04a5d79020cefa0ba46794095b5766c5ff66a4`, `research/fixed-integer-descent/drift.md`, FID-DRIFT-002 and FID-DRIFT-005. For every finite simple shortcut path and every integer interval of width $X\ge1$, it proves an occupancy bound $C_\alpha X^\alpha$ for each

$$H_2(\log_3 2)<\alpha<1.$$

In particular $\alpha=19/20$ is valid, with a uniform finite effective constant not numerically evaluated in that source. The weaker explicit choice $\alpha=29/30$, $C_\alpha=10$ is also available.

The arithmetic moment $P_q$ and the prior pointwise sufficient condition $P_q=o(q^{40/19})$ are frozen in PR165 at `78bdb31ccba608de3d089b751a0ab59a52007408`, `research/certificate-transfer-intake-20261120/questions/02_weighted_representatives.txt` and `reports/2026-11-20-certificate-transfer-intake/initial-review-and-problem-key.txt`. The primitive-word decomposition there is reconstructed below, without invoking an uninspected analytic operator.

The contribution is a family of weaker, averaged or quantile-based sufficient conditions. These conditions allow arbitrarily large intermittent values of $P_q$. They are not estimates proving that the actual sequence satisfies any of them. No novelty claim beyond this repository comparison is made.

## 2. Exact arithmetic moment and ordinary-source identity

For a word $w=(a_1,\ldots,a_q)$ of positive integers set

$$A_0=0,\quad A_j=\sum_{i=1}^j a_i,\quad
 C_w=\sum_{j=0}^{q-1}3^{q-1-j}2^{A_j},\quad J_w=3^q2^{-A_q}.$$

Let $r_w$ be the unique positive odd representative less than $2\cdot3^q$ satisfying

$$2^{A_q}r_w\equiv C_w\pmod {3^q},$$

and put

$$b_w=(2^{A_q}r_w-C_w)/3^q,\qquad
 P_q=\sum_w J_w^4/r_w^2.$$

The integer $b_w$ is odd. The full identity forces the first division by $2^{a_1}$; after that division the suffix identity forces the next division, and so on. Each intermediate value is odd because the next prescribed division is by an even number and the final value $r_w$ is odd. If $b_w$ were negative, each such step would preserve negativity, contradicting $r_w>0$. Thus

$$1\le b_w<2^{A_q+1}.$$

Every positive ordinary source having exactly this word is

$$n=b_w+2^{A_q+1}k,\qquad k\ge0,$$

and its endpoint is

$$U^q(n)=r_w+2\cdot3^q k.$$

Indeed the final oddness condition identifies one class modulo $2^{A_q+1}$, and the displayed shifts preserve every intermediate oddness and exact valuation. Hence, by summing nonnegative terms over actual source cylinders,

$$\mathcal D_q:=\sum_{n\text{ positive odd}}
 \frac{J_q(n)^4}{U^q(n)^2}
 =P_q+R_q,$$

where

$$R_q=\sum_w J_w^4\sum_{k\ge1}(r_w+2\cdot3^q k)^{-2}.$$

Using $\sum_{k\ge1}k^{-2}<2$ and

$$\sum_w J_w^4=\left(81\sum_{a\ge1}2^{-4a}\right)^q=(27/5)^q,$$

we obtain the convenient entirely rational envelope

$$0<R_q<\tfrac12(3/5)^q,\qquad
 Q_q:=P_q+\tfrac12(3/5)^q\ge\mathcal D_q.\tag{MQ1}$$

The sharper bound with $\zeta(2)/4$ is already in the source packet; the larger rational constant simplifies standalone use. The sums are finite because $P_q\le(27/5)^q$ and the displayed tail is finite.

## 3. What one nonperiodic orbit would force

Suppose $n_0,n_1,\ldots$ is a nonperiodic positive odd orbit. Its expansion into shortcut steps has no repeated state, since a repeat in a deterministic map forces eventual periodicity. Put $C=C_\alpha$.

The occupancy theorem gives

$$\#\{j:n_j\le X\}\le CX^\alpha$$

by applying the finite theorem to successively longer prefixes. Positive summation then gives

$$\sum_{j\ge0}\frac1{n_j}
 =\int_1^\infty\frac{\#\{j:n_j\le t\}}{t^2}\,dt
 \le\frac C{1-\alpha}.$$

The exact multiplicative correction therefore satisfies

$$n_q=n_0J_q(n_0)I_q,\qquad
 I_q=\prod_{j<q}\left(1+\frac1{3n_j}\right)
 \le M:=\exp\left(\frac C{3(1-\alpha)}\right).$$

The fixed original source $n_0$ contributes one term to $\mathcal D_q$. Combining this observation with (MQ1) yields

$$\boxed{Q_q\ge\frac{n_q^2}{n_0^4M^4}.}\tag{MQ2}$$

There is no change of source as $q$ increases.

### MQ3: a bound for every finite choice of times

Let $I$ be any finite set of positive time indices, with $|I|=N$. Arrange the distinct values $\{n_q:q\in I\}$ in increasing order $y_1<\cdots<y_N$. Occupancy implies

$$y_j\ge(j/C)^{1/\alpha}.$$

Consequently, with $H_N=\sum_{j=1}^N1/j$,

$$\boxed{\sum_{q\in I}Q_q^{-\alpha/2}
 \le C n_0^{2\alpha}M^{2\alpha}H_N.}\tag{MQ3}$$

Proof: (MQ2) gives $Q_q^{-\alpha/2}\le n_0^{2\alpha}M^{2\alpha}n_q^{-\alpha}$, and $\sum_{j\le N}y_j^{-\alpha}\le CH_N$.

Thus existence of even one nonperiodic orbit imposes a logarithmic upper bound on these negative arithmetic moments, uniformly over every finite selection of times. For the explicit pair $\alpha=29/30,C=10$, the right side is

$$10e^{580/3} n_0^{29/15}H_N.$$

This constant is very large; it is displayed to make finiteness independent of an unevaluated $C_{19/20}$ when desired.

### MQ4: a quantile bound

For every $Y>0$, even allowing an infinite set of candidate times,

$$\boxed{\#\{q\ge1:Q_q\le Y\}
 \le C n_0^{2\alpha}M^{2\alpha}Y^{\alpha/2}.}\tag{MQ4}$$

Every such time has $n_q\le n_0^2M^2\sqrt Y$ by (MQ2), and these are distinct ordinary states in the same orbit. Apply occupancy. In particular that time set is finite. This is a necessary condition on the globally defined sequence $Q_q$ if any nonperiodic orbit exists.

### MQ5: an averaged positive-moment lower bound

Take $I=\{1,\ldots,N\}$. The same ordering, now with positive powers, gives

$$\begin{aligned}
\sum_{q=1}^N Q_q
&\ge\frac1{n_0^4M^4}\sum_{j=1}^N y_j^2\\
&\ge\frac{C^{-2/\alpha}}{n_0^4M^4(1+2/\alpha)}N^{1+2/\alpha}.
\end{aligned}\tag{MQ5}$$

The last step uses $\sum_{j=1}^N j^{2/\alpha}\ge\int_0^N t^{2/\alpha}\,dt$. This condition does not follow from treating the representatives as independent uniform residues.

## 4. Four open closing criteria for nonperiodic orbits

The root agent observed a particularly simple complementary criterion. Every nonperiodic integer orbit has $n_q\to\infty$: there are only finitely many positive integers below each bound, and none can repeat. Thus (MQ2) and the exponentially vanishing remainder imply

$$\text{one nonperiodic orbit exists}\quad\Longrightarrow\quad P_q\longrightarrow\infty.$$

Consequently the following would exclude every nonperiodic positive orbit:

$$\boxed{\liminf_{q\to\infty}P_q<\infty.}\tag{BC}$$

BC allows arbitrarily large values away from a cofinal sequence, however sparse. It is complementary to a growing polynomial upper estimate; neither is claimed to imply the other. BC has not been proved for the actual moment sequence.

With $\alpha=19/20$, **any one** of the following three additional statements would also exclude every nonperiodic positive orbit:

1. **Chronological negative moment:**

   $$\boxed{\limsup_{N\to\infty}\frac1{\log(N+1)}
       \sum_{q=1}^N Q_q^{-19/40}=\infty.}\tag{NC}$$

2. **Quantile excess:**

   $$\boxed{\sup_{Y\ge1}Y^{-19/40}
       \#\{q\ge1:Q_q\le Y\}=\infty.}\tag{QC}$$

3. **Averaged positive moment:**

   $$\boxed{\liminf_{N\to\infty}
       N^{-59/19}\sum_{q=1}^N P_q=0.}\tag{PC}$$

For PC, replacing $P_q$ by $Q_q$ makes no difference because their cumulative difference is bounded by $\frac12\sum_{q\ge1}(3/5)^q=3/4$. Each criterion contradicts its corresponding necessary bound from the fixed hypothetical source. The constants may depend on that source, but are finite and fixed; no uniform source choice is needed for the contradiction.

For any $\alpha$ strictly above the entropy threshold, replace the fractions by $\alpha/2$, $1+2/\alpha$ as appropriate. This small optimization is separate from proving one of the open arithmetic estimates.

### Why NC is strictly more permissive than the old pointwise premise

The old $P_q=o(q^{40/19})$ implies NC: $Q_q^{-19/40}=q^{-1}L_q$ for a positive $L_q\to\infty$, and its harmonic average diverges. But NC can hold when a comparison sequence is exponentially large at almost every time.

For example, define an illustrative positive sequence, **not the actual $Q_q$**, by

$$A_q=\begin{cases}
 q^{10/19},&q\text{ is a square},\\
 2^q,&q\text{ is not a square}.
\end{cases}$$

At $q=j^2$, $A_q^{-19/40}=j^{-1/2}$. Therefore

$$\sum_{q\le N}A_q^{-19/40}\ge\sum_{j\le\sqrt N}j^{-1/2}
 \ge\sqrt{\lfloor\sqrt N\rfloor},$$

so NC holds. The pointwise polynomial premise fails on a set of natural density one, and a positive-average small-moment premise also fails. This shows that NC genuinely permits intermittent enormous spikes; it does not establish such a pattern for $P_q$.

QC is a common weaker sufficient target: BC, NC, or PC each implies QC. Indeed, if QC fails, the counting function of the $Q_q$ values is bounded by a fixed multiple of $Y^{19/40}$ for $Y\ge1$. Only finitely many $Q_q$ are below one, and their minimum is positive, so increasing the constant extends this bound to every $Y>0$. Ordering any finite selection then proves a fixed multiple of $H_N$ as an upper bound for its negative moments and a fixed positive multiple of $N^{59/19}$ as a lower bound for its positive moments. This contradicts NC and PC respectively. BC directly supplies infinitely many values below one fixed bound and also contradicts that counting bound.

Equivalently QC can be written using only finite counts:

$$\sup_{N\ge1,\,Y\ge1}Y^{-19/40}
  \#\{1\le q\le N:Q_q\le Y\}=\infty.$$

No one of these sufficient conditions is asserted equivalent to universal convergence.

## 5. Why cycles are still a separate obligation

On a nontrivial positive cycle the odd states repeat. The occupancy argument applied to the values remains valid, but it cannot count repeated time indices. Also $I_q$ grows exponentially with repeated positive contributions. The uniform bound on $I_q$ used in (MQ2) then fails.

Therefore these moment criteria exclude nonperiodic orbits only. Full Collatz would additionally require excluding every nontrivial positive cycle, for example by the full-denominator condition in the existing standalone Problem 03. No energy, density, or cycle conclusion is imported silently.

## 6. Attempt to prove the new criterion

The exact recurrence for $H_q(t)$, retained from standalone Problem 02, gives a positive finite-period computation for each fixed $q$. I reconstructed it independently using the untruncated positive-exponent sum and exact rational truncation errors. This produces certified finite enclosures for $P_q$ in the accompanying report.

I also tried to derive NC from the fixed total word mass $(27/5)^q$, from the positivity cutoff $r_w\ge J_w+C_w/2^{A_q}$, and from finite-energy propagation in PR163. None supplies the needed upper control on the actual low endpoint concentration. Convexity by itself only converts an already sufficient positive-average bound into another criterion; it does not prove such a bound. PR163 controls tripling defect by five defect but does not bound either actual defect at the harmonic endpoint. No implication from those facts to NC, QC, or PC was established.

The finite moment values are diagnostics, not asymptotic evidence sufficient for any boxed closing statement. The first unsupported step remains proving BC or one of NC/QC/PC for the exact arithmetic sequence. This is a wider target than the previous pointwise upper estimate, not a discharged target.

## 7. Reproducible finite checks

The adjacent checker imports no source research code. It checks word representatives, positivity and exact valuation replay, whole source-cylinder shifts, rational moment enclosures with an explicit omitted-exponent allowance, the moment identity on finite word/source sums, and finite simple-orbit uses of the relevant inequalities. Damaged representatives and valuation words are rejected using explicit exceptions that remain active with optimized Python. It does not verify an infinite sum by truncation or claim an infinite-time empirical theorem.

### Exact enclosure derivation and observed values

For odd positive $t$, let $[t]_m$ mean its unique positive odd representative below $2m$ modulo the odd integer $m$. Starting with $H_0(t)=1$, the untruncated recurrence is

$$H_q(t)=81\sum_{\substack{a\ge1\\2^a t\equiv1\pmod3}}
 16^{-a}H_{q-1}\left(\left[(2^at-1)/3\right]_{3^{q-1}}\right).$$

It groups a complete word by its last exponent, so

$$P_q=\sum_{\substack{1\le t<2\cdot3^q\\t\text{ odd}}}H_q(t)/t^2.$$

All values satisfy $H_q(t)\le(27/5)^q$. If $H_q^{[A]}$ uses only exponents $a\le A$ at every step, positivity and induction give

$$0\le H_q(t)-H_q^{[A]}(t)
 \le q(27/5)^q16^{-A}.$$

The positive row mass is at most $27/5$, while the omitted row mass is at most $(27/5)16^{-A}$. These give the induction directly. Therefore the omitted contribution to $P_q$ is less than

$$2q(27/5)^q16^{-A}.$$

The checker uses $A=12$ and integer numerators at the common denominator $16^{12q}$. It rounds each of the $3^q$ endpoint terms down at scale $10^{18}$; adding $3^q/10^{18}$ and the displayed omitted-exponent bound gives a rigorous upper enclosure. Thus both infinitely many exponents and finite rounding are accounted for. It does not substitute the truncated menu for the full sum.

The actual normal and optimized executions gave the same report bytes. Selected outward decimal enclosures are:

| $q$ | Lower bound for $P_q$ | Upper bound for $P_q$ |
|---:|---:|---:|
| 1 | 0.520941176470 | 0.520941176471 |
| 3 | 0.165136823745 | 0.165136823750 |
| 6 | 0.082614638405 | 0.082614639463 |
| 9 | 0.114005626195 | 0.114005875872 |
| 12 | 0.235522686400 | 0.235575106347 |

The complete report contains all twelve values. Neither their small size nor their later increase proves anything about BC, NC, QC, or PC. The proof of the reductions, not numerical extrapolation, is the result retained here.

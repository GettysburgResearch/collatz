# How often an ordinary cycle must leave a low band

**PROPOSED written theorem.** Let a primitive positive odd Collatz cycle have odd period $p$, minimum $s$, and reduced common denominator $d$. Count the phases $x>Ks$, allowing them to be arbitrarily high. For all sufficiently large $p$, the following statements hold.

| Threshold $K$ | If at most $p/300$ phases exceed $Ks$ | External input |
|---|---|---|
| $12/5$ | $d>p^{1/10}$ | Wu–Wang, published Theorem 1 |
| $14/5$ | $d>p^{1/100}$ | Chudnovsky, preprint Corollary 1.2, source-qualified |

In particular, every sufficiently long **ordinary** positive cycle has more than $p/300$ odd phases above $12s/5$, without any upper bound on its largest member. The threshold rises to $14s/5$ using the separately identified preprint. The period onset is unspecified. The new estimate extends the PR209 count beyond windows contained wholly in one band. It excludes complete denominator divisibility for every word satisfying the displayed period and occupation restrictions. For the additional restriction that all odd valuations are one or two, the source-qualified threshold can be raised to $3s$ with more than $p/2000$ high phases. Cycles with more frequent excursions remain open. [Paired-clock refinement](TWO_GAPS.md)

## Cycles, parameters and general bound

Take the exact odd-step equations $2^{a_i}x_{i+1}=3x_i+1$, with positive integer valuations $a_i$ and indices cyclic modulo $p$. Write $h=\sum a_i$. At one phase put $A_i=\sum_{j<i}a_j$ and $C=\sum_{i<p}3^{p-1-i}2^{A_i}$. Then $D=2^h-3^p>0$ and the actual reduced denominator is $d=D/\gcd(D,C)$. It is coprime to six and unchanged at every phase. Indeed, for a reduced numerator $y$ the step starts with $3y+d$, coprime to $d$, and division by a power of two preserves coprimality. A rational cycle is taken in the odd rationals with denominator prime to six, with exact dyadic valuation at each step. In numerator coordinates $y_i=dx_i$ the integer recurrence has increment $d$.

Assume a homogeneous lower estimate
$$
 |h\ln2-p\ln3|\gg_\varepsilon p^{-\kappa-\varepsilon}
 \quad(p\le h\le 2p)
$$
for every $\varepsilon>0$. Fix $2<K<4,\ 0<Q<1/4$, set $t=Q/(1-2Q)$, and let
$$
 B(K,Q)=\frac{\ln(K/2)+H(t)+t\ln3}{\ln3},\qquad
 H(t)=-t\ln t-(1-t)\ln(1-t).
$$
For every $0\le\gamma<1$ such that $(\kappa+1+\gamma)B(K,Q)<1$, all sufficiently large cycles with at most $Qp$ high phases have $d>p^\gamma$. In particular, for **each** $2<K<2\cdot3^{1/(\kappa+1)}$ in the indicated range, there is $Q(K)>0$ such that every sufficiently long ordinary cycle spends more than $Q(K)p$ odd phases above $Ks$. Here $H(t)+t\ln3\to0$ as $Q\downarrow0$.

## Proof for a fixed period and denominator

Argue along a sequence with $p\to\infty,\ d\le p^\gamma$ and at most $Qp$ high phases. At least $(1-Q)p$ distinct positive integer numerators are at most $Kds$, so $s\gg p^{1-\gamma}$. In particular $s\ge1$ eventually. The full lap gives
$$
 0<h\ln2-p\ln3=\sum_{i<p}\ln(1+1/(3x_i))\le p/(3s).
$$
Each $a_i\ge1$ and $\prod 2^{a_i}=\prod(3+1/x_i)\le4^p$, hence $p\le h\le2p$. The form estimate gives $s\ll_\varepsilon p^{\kappa+1+\varepsilon}$. Put $k=\lceil\log_3(Kds)\rceil$, so $k\to\infty,\ k=O(\ln p),\ k/s\to0$.

Use all cyclic $k$-windows whose **two endpoints** are at most $Ks$. At least $(1-2Q)p$ remain since translation permutes the phases. A position $i\in\{1,\ldots,k\}$ is marked if its endpoint $x_i>Ks$. Write $R$ for the number of marks in one window. Over the retained windows, the mean of $R$ is at most $kt$ by double counting first over all $p$ windows.

**Clock cost of a marked run.** Just before each maximal run of $r$ marked endpoints the state is low. Its last endpoint is high. If $A$ is the sum of the $r$ valuations on the entering steps, multiplication of the odd-step equations gives
$$
 2^A=\frac{x_{\rm before}}{x_{\rm last}}
       \prod_{i\text{ in the run}}(3+1/x_{i-1})\le(3+1/s)^r.
$$
Give each positive marked valuation $a$ weight $2^{-a}$. The total negative log weight of marked valuations, in nats, is at most $R\ln(3+1/s)$. This pays for arbitrary excursions including individual large valuations. In numerator coordinates the Lean proof establishes the stronger clipped-product inequality, valid also for windows ending inside an excursion. Set $m=ds,\ H_0=\lfloor Kds\rfloor$ and let $A$ now sum the clocks of all marked endpoints. Then
$$
 m^R 2^A\max(H_0,y_k)\le(3m+d)^R\max(H_0,y_0).
$$
For a high endpoint use $m(3y+d)\le(3m+d)\max(H_0,y)$. For a low endpoint the clipped height decreases weakly. Multiplication gives the result. [Lean proof](ExcursionBudget.lean)

**Clock cost inside the band.** Write $\alpha=\log_2 3,\ \beta=\log_2K$, pick $\eta>0$ with $\beta+2\eta<2$, and partition possible starting log-heights $\log_2(x_0/s)\in[0,\beta]$ into finitely many bins of width at most $\eta$. For a bin with lower endpoint $b$, every unmarked $i$ has cumulative clock $S_i=\sum_{j<i}a_j$ in
$$
 [\,b+i\alpha-\beta,\ b+i\alpha+2\eta\,].
$$
Indeed $S_i=\log_2(x_0/s)+i\alpha-\log_2(x_i/s)+e_i$, where $0\le e_i\le k/s\le\eta$, even if intervening states were high. The interval has one or two integer options. Uniformly in the starting bin, at most $(\beta+2\eta-1+o(1))k$ positions have two. The fractional lower endpoints follow the irrational rotation by $\alpha$ and two options occur on a closed arc of length $\beta+2\eta-1$. For a uniform estimate take an arbitrarily large reduced approximant $v/q$ with $|\alpha-v/q|<q^{-2}$. Each $q$-block is within $1/q$ of a translated full grid and contributes at most $q(\beta+2\eta-1)+4$ hits. First let $k\to\infty$ and then $q\to\infty$. [Uniform-band argument, PR209 at 2d0230aa52d85732dbc85b5df20e30108dc1396f](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/arithmetic/README.md)

**Distinct windows.** Give the starting bin uniform probability. Give the marks independent Bernoulli probability $t$. At marked positions record the preceding gap $a_{i-1}$ with probability $2^{-a_{i-1}}$. At unmarked positions record $S_i$ uniformly among the available choices. These choices have total probability one. Starting at $S_0=0$, the code determines all the gaps by iteration. Two windows of the same code have the same word, and their terminal numerators differ by a multiple of $3^k$ by the affine identity and coprimality of the clock power with three. Both endpoints in numerator coordinates lie in $[ds,Kds]$, of length strictly smaller than $3^k$. The numerators are equal, and primitivity makes the terminal phases equal. This injection uses the full common numerator lattice. [Common-word terminal proof](ExcursionBudget.lean)

The mean negative log probability of a realized code is at least $\ln((1-2Q)p)$ by arithmetic–geometric means. Since $t<1/2$ and mean $R\le tk$, the mean mask cost is at most $kH(t)$. The run and band estimates bound the remaining costs, giving
$$
 \ln((1-2Q)p)\le O_\eta(1)+k\bigl[H(t)+t\ln(3+1/s)+(\beta+2\eta-1+o(1))\ln2\bigr].
$$
Use $k=\ln(Kds)/\ln3+O(1)$, then let $\eta\downarrow0$. This gives $\limsup\ln p/\ln(ds)\le B(K,Q)$. Combining with $ds\ll_\varepsilon p^{\kappa+1+\gamma+\varepsilon}$ contradicts the strict hypothesis on $\gamma$.

## Exact margins and the scope of the external inputs

For $Q=1/300$, $t=1/298$. From $-(1-t)\ln(1-t)\le t$ and $e<3$, one gets $H(t)+t\ln3<\ln(9\cdot298)/298<(15/596)\ln3$. The last comparison follows from $(9\cdot298)^2<3^{15}$. The following strict margins are tested by integer powers:
$$
 \log_3(6/5)+15/596<50/261,\qquad
 \log_3(7/5)+15/596<100/301 .
$$
Wu and Wang's Theorem 1 gives $\kappa=4.1163051$ upon taking their constant coefficient zero and their other coefficients $h,-p$. Thus $\kappa+1+1/10<261/50$. Chudnovsky's November Corollary 1.2 reports $\kappa=2$ for the multiplicatively independent rationals 2 and 3 and credits its two-logarithm case to the October paper. This gives $\kappa+1+1/100=301/100$. We checked the statements in the primary sources. The preprint and its external Lean development have not been independently rebuilt here. [Published Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007) · [November Corollary 1.2](https://arxiv.org/html/2611.30820v1) · [October preprint](https://arxiv.org/abs/2610.28079)

## Why the estimate cannot yet be iterated at a high valley

Applying the full-lap argument with a higher floor would require every phase of that lap to stay above the new floor. Rotating a lap preserves its minimum. Taking the segment from one high local minimum to the next produces an open path in general. The full-lap log identity then has an endpoint term. Inducing on the high phases changes one accelerated edge into a variable number of ordinary odd steps, so the fixed-window count and its period bound also change.

A direct count with both actual rank orders admits more than $\ln3/3$ nats of physical word entropy per odd step. The family can have more than $p/50$ odd phases above $3s$, all-shift mismatch above $p/83$, and maximum below $3.3s$ simultaneously. Its reduced denominator is exponential. Thus a uniform low-entropy bound for the half-dozen geometric and occupation conditions tested there fails. An individual ordinary or least-disagreement cycle could still obey a stronger denominator-sensitive window bound. [Counting proof and real-order checks](ORDER_ENTROPY.md)

The published $12s/5$ bound and the source-qualified $14s/5$ bound both leave room below the least-disagreement ceiling $(16s+7)/3$. For a remaining high-occupation word the argument supplies no strict inequality $D\nmid C$. Its denominator can still equal one under the conclusions established here. Escape is a separate obligation.

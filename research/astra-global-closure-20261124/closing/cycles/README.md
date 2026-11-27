# Full cycle denominators in the unrestricted word family

For every sufficiently long hypothetical primitive integer cycle, the centers obtained by deleting the first one through $\lfloor\sqrt A/2\rfloor$ bits after its minimum are multiplicatively independent modulo sign. A dependence among the first $t$ centers instead forces $\log d\ge (A/t)\log2-O(t+\log A)$ on its complete original reduced denominator. The proof uses integer endpoints at every cut and cross-gcd bounds on both the numerators and denominators of the reduced centers. [Pointwise theorem and proof](NEAR_MINIMUM.md)

Among all length-$A$ marked parity words having a positive rational cycle, the mean of the **entire cancelled factor** of the numerical denominator is $\exp(o(A))$. For every fixed $0<\epsilon<1$ the proportion with reduced denominator $d\le 2^{(1-\epsilon)A}$ is at most $2^{-\epsilon A+o(A)}$. At each fixed reduced denominator $d$, a collection of distinct primitive cycles with $P$ odd positions has total logarithmic clock imbalance $o_d(\log P)$ as $P\to\infty$. Both conclusions allow an isolated nontrivial integer cycle.

These are written deductions. Eight declarations in [DenominatorBudget.lean](DenominatorBudget.lean) verify the finite multiplicative identities, comparisons and signed cut arithmetic used here and in the pointwise proof. Two further declarations in [ValuationDominance.lean](ValuationDominance.lean) formalize the signed valuation cover and its truncation. The compiled scope and the independent integer controls are recorded in [the execution report](../../../../reports/astra-global-closure-20261124/closing/cycles/EXECUTION.md).

## 1. Literal rational cycles and the minimum

Use the shortcut map $x\mapsto x/2$ at parity zero and $x\mapsto(3x+1)/2$ at parity one. Parity for a rational of odd reduced denominator is the parity of its numerator. Let $p$ be the number of ones, at positions $0\le e_0<\cdots<e_{p-1}<A$. Put

$$
 D=2^A-3^p,\qquad C=\sum_{i=0}^{p-1}2^{e_i}3^{p-1-i},\qquad
 d=\frac{D}{\gcd(C,D)},\qquad \Lambda=A\log2-p\log3 .
$$

We consider $p>0,D>0$. A marked word has a designated time zero. A necklace is its cyclic rotation class. The composed branch is $x\mapsto(3^px+C)/2^A$ with fixed point $C/D>0$. The first bit is the parity of $C$ since $D$ is odd. Rotating the word takes its fixed point to the result of its first step, by conjugating the branch composition. This proves literal parity and positivity at every rotation. Also $\gcd(D,6)=1$. Division of an even numerator by two preserves coprimality with $d$. Replacing an odd numerator $n$ by $(3n+d)/2$ preserves it because $\gcd(d,6)=1$. Hence $d$ is the same reduced denominator everywhere.

The minimum is odd because an even point is followed by a smaller point. Let $n_i$ be the odd numerators in cyclic order and $g_i$ the number of shortcut steps from that odd point to the next. Then $2^{g_i}n_{i+1}=3n_i+d$, $\sum g_i=A$, and $3\nmid n_{i+1}$. Multiplying and taking logs yields

$$
 2^A\prod_i n_i=\prod_i(3n_i+d),\qquad
 \Lambda=\sum_i\log(1+d/(3n_i)). \tag{1}
$$

For $m=\min_i n_i$, (1) yields $m/d\le Q_{A,p}:=p/(3\Lambda)$. A weaker rational bound suitable for exact controls is $Q_{A,p}\le p\,2^A/(3D)$, by $1-e^{-\Lambda}\le\Lambda$. The sharp optimization of rational cycle minima for fixed clocks has a separate literature. [Halbeisen and Hungerbühler, *Optimal bounds for the length of rational Collatz cycles*](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)

For all $A\ge1$ and integral $p$, Lagarias gives $|\log_3 2-p/A|\ge(1200A^{14.3})^{-1}$. Thus $\Lambda\ge(\log3)/(1200A^{13.3})$ on the contracting side, and

$$
 Q_{A,p}\le \frac{400}{\log3}\,pA^{13.3}\le\frac{400}{\log3}A^{14.3}. \tag{2}
$$

The explicit bound holds throughout the near-critical clock range. Lagarias derives it from the Simons–de Weger application of Rhin. [Lagarias, *Ternary expansions of powers of 2*, Lemma 2.2(1), equation (2.4)](https://arxiv.org/pdf/math/0512006)

## 2. Counting the complete numerical gcd

For fixed $A,p,d$, mapping each necklace to its least numerator $m$ is injective. From $m/d$ the deterministic shortcut map determines all $A$ successive bits. This includes imprimitive words because $A$ fixes the number of repetitions. Every necklace has at most $A$ marked words. Consequently

$$
 \#\{w:d(w)=d\}\le A\lfloor dQ_{A,p}\rfloor,\qquad d\mid D. \tag{3}
$$

The count is zero when $d\nmid D$. Dividing each bound by $d$, then summing over divisors, gives

$$
 \sum_{w\text{ at }A,p}\frac1{d(w)}\le A\,Q_{A,p}\,\tau(D). \tag{4}
$$

The divisor bound $\tau(D)=\exp(o(A))$ holds uniformly for $D\le2^A$. For any $\eta>0$, primes $r\ge2^{1/\eta}$ satisfy $v+1\le2^v\le r^{\eta v}$ for all $v\ge0$. For the finitely many other primes one pays the finite constant $\prod_r\sup_{v\ge0}(v+1)r^{-\eta v}$. Thus $\tau(D)\ll_\eta D^\eta$ for every $\eta>0$. Combining (2)–(4) over at most $A$ choices of $p$ gives four consequences.

* The number of positive marked words of length $A$ with $d\le Y$ is at most $Y\exp(o(A))$, uniformly for $Y\ge1$.
* There are $2^A(1-O(e^{-cA}))$ positive marked words for an absolute $c>0$. Every word of weight $1\le p\le 3A/5$ qualifies, and the upper binomial tail beyond $3A/5$ is exponentially small relative to $2^A$. It follows that $\Pr(d\le2^{(1-\epsilon)A})\le 2^{-\epsilon A+o(A)}$ for any fixed $0<\epsilon<1$. In particular $\log_2d/A\to1$ in probability.
* As $\gcd(C,D)=D/d$ and $D\le2^A$, the uniform expectation among positive marked words satisfies $\log\mathbb E[\gcd(C,D)]=o(A)$. The gcd includes every prime and its complete multiplicity in the cancelled factor.
* At fixed contracting clocks with $p/A\to\theta\in(0,\log_3 2]$, Stirling gives $\binom Ap=\exp(Ah(\theta)+o(A))$ with $h(\theta)=-\theta\log\theta-(1-\theta)\log(1-\theta)$. Thus the fraction with $\log d\le(h(\theta)-\epsilon)A$ is at most $\exp(-\epsilon A+o(A))$. In particular this holds at near-critical contracting convergents. Primitive-word sampling gives the same exponent. A word repeated $j\ge2$ times requires $j\mid\gcd(A,p)$, and $\binom{A/j}{p/j}\le\exp(Ah(p/A)/j)$. Removing all repetitions leaves the leading entropy unchanged because $h(\theta)>0$.

No partition, return-block alphabet, or distribution assumption on residues enters (3)–(4). At $d=1$ there is a polynomial-size finite search reduction at any prescribed period ceiling. Over *all* least lengths $\le X$, each distinct primitive integer cycle has a different positive integer minimum at most $400X^{14.3}/\log3$. The ceiling $X$ is unrestricted.

## 3. Disjoint cycles at a fixed reduced denominator

Let $\mathcal F$ be a finite collection of distinct primitive positive cycles with the same $d$. All their odd numerators are distinct since a shared numerator specifies the same rational point and hence the same cycle. Write $P=\sum_{C\in\mathcal F}p_C$ and $A_*=\sum_{C\in\mathcal F}A_C$. Order the numerators as $n_{(1)}<\cdots<n_{(P)}$. They are coprime to $6d$. If $u_j$ is the $j$-th positive integer coprime to $6$, then $u_j\le n_{(j)}$. Multiplying (1) and using that $3+d/n$ decreases gives

$$
 2^{A_*}\prod_{j=1}^P u_j\le\prod_{j=1}^P(3u_j+d). \tag{5}
$$

Using the integers coprime to $6d$ strengthens (5). With the first choice of $u_j$, the two residue classes $1,5\bmod6$ give $\sum_{j\le P}1/u_j=(\log(P+1))/3+O(1)$. Thus $\sum_{C\in\mathcal F}\Lambda_C\le(d/9)\log(P+1)+O(d)$.

For fixed $d$ let $E_d$ be the odd numerators on its reduced periodic orbits. Gonçalves, Greenfeld and Madrid prove almost-boundedness in logarithmic density for generalized accelerated Collatz maps. Their parameters here are $p_0=2,\ q_0=3,\ r(1)=d>0$, which satisfy coprimality, $3<2^{2/(2-1)}=4$, and $3+d\equiv0\bmod2$. Their accelerated map on odd inputs is $n\mapsto(3n+d)/2^{v_2(3n+d)}$, exactly the odd numerator dynamics. Given $\delta>0$, all but at most $(\delta/2+o(1))\log X$ in harmonic mass among the odd inputs $\le X$ have an iterate below a fixed $B_\delta$. Only finitely many periodic points belong to cycles that meet that interval. On taking $\delta\downarrow0$ we obtain

$$
 \sum_{\substack{n\in E_d\\n\le X}}\frac1n=o_d(\log X).
$$

This applies to the periodic points themselves. The authors state universal finiteness of cycles separately as Conjecture 1.5. [Gonçalves, Greenfeld and Madrid, *Generalized Collatz Maps with Almost Bounded Orbits*, Theorem 1.3 and Conjecture 1.5](https://arxiv.org/pdf/2111.06170)

In a family of $P$ distinct odd numerators, terms exceeding $P$ contribute at most 1 to their reciprocal sum. Equation (1) therefore gives the following estimate, uniform over families at the specified $d$.

$$
 \sum_{C\in\mathcal F}\Lambda_C=o_d(\log P)\qquad(P\to\infty). \tag{6}
$$

In particular a sequence of growing primitive integer cycles must have $A\log2-p\log3=o(\log p)$. There is no stated uniformity as $d$ varies.

Let $N_d(X)$ count distinct primitive cycles at denominator $d$ with least shortcut length $\le X$. The minimum bound gives $N_d(X)\le400dX^{14.3}/\log3$. Their total odd count is at most $XN_d(X)$. Each cycle contributes at least $(\log3)/(1200X^{13.3})$ by (2). If the total odd count grows unboundedly, applying (6) gives

$$
 N_d(X)=o_d(X^{13.3}\log X). \tag{7}
$$

If that count stays bounded, (7) also follows. The estimate allows sparse exceptional cycles and finite collections of isolated cycles.

### The stronger periodic-set estimate from translated packing

The fixed-$d$ almost-boundedness argument is an independent route to (6). The repository already provides a stronger estimate for synchronously distinct sets. Here it applies to the union $E_d$ itself because the odd dynamics restricts to a permutation of the periodic nodes. For $d=1$, PR #193 §1b gives $|E_1\cap[M,M+L)|\ll L^\theta/\sqrt{\log(2L)}$, where $\theta=H_2(\log_3 2)<1$. Its proof also works for every fixed positive odd $d$ coprime to 3. Indeed the $k$-step numerator carry is now $dB$ with $0\le B\le3^k-2^k$, the parities still biject the residues modulo $2^k$ because lifts have final difference $3^p$, and stripping twos still gives the same fixed-weight odd-clock transport identity for the $3n+d$ map. Replace the width $2\,3^p+(3/2)^k$ there by $2\,3^p+d(3/2)^k$. In the induction the secondary sum becomes $O_d((k+1)(L^{\log_2(3/2)}+3)^\theta)=o_d(L^\theta)$ and the logarithmic comparability of image lengths is preserved. This gives

$$
 |E_d\cap[M,M+L)|\ll_d L^\theta/\sqrt{\log(2L)}.
$$

In particular the total sum of $\Lambda_C$ over **all** distinct primitive cycles of this fixed denominator is finite. Summing the dyadic count beyond a cycle's minimum numerator $m$ also yields the *pointwise* bound
$$
 \Lambda_C\le (d/3)\sum_{\substack{n\in E_d\\ n\ge m}}\frac1n
 \ll_d m^{\theta-1}/\sqrt{\log(2m)}. \tag{8a}
$$
Every sequence of distinct cycles at fixed $d$ has $m\to\infty$, since a minimum uniquely determines its cycle. Thus eventually $A=\lceil p\log_2 3\rceil$ and the positive upper-rounding errors tend to zero. Also $N_d(X)=o_d(X^{13.3})$: exclude a finite collection whose complement has total imbalance at most $\delta$, apply the individual lower bound $(\log3)/(1200X^{13.3})$ to each remaining cycle of length $\le X$, then take $\delta\downarrow0$. These are applications of the existing synchronous packing theorem, without a priority claim for periodic sparsity or reciprocal summability. An isolated cycle has finite cost and can survive all these estimates. [PR #193, translated packing §1b at the comparison head](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/escape.md)

## 4. Which Diophantine hypotheses survive

**Fixed-rank unit equations.** Evertse–Schlickewei–Schmidt Theorem 1.1 bounds nondegenerate solutions of a fixed $a_1x_1+\cdots+a_nx_n=1$ in a subgroup $\Gamma\subset(K^*)^n$ of finite rank $r$ in characteristic zero by $\exp((6n)^{3n}(r+1))$. At fixed $A,p$, let the tuple $(2^{e_i}3^{p-1-i})_i$ range over all unrestricted words. When $A\ge p+1$, the quotient of two permitted tuples can be $2$ in coordinate $i$ and $1$ elsewhere. Choose $e_j=j$ for $j\le i$ and $e_j=j+1$ afterwards, then shift $e_i$ right once. This works for every $i$. The $p$ coordinate units are independent by coordinatewise prime-2 valuations. Fixing $e_0=0$ leaves $p-1$ coordinate units. Passing to the quotient by a common scalar in the unrestricted tuple also leaves rank at least $p-1$. This proves rank growth for the raw physical sum. A lower-rank parametrization restricted to actual integer-producing words would require additional structure. Even with bounded rank, the cited theorem bounds a count and permits one exceptional candidate. [Evertse, Schlickewei and Schmidt, *Linear equations in variables which lie in a multiplicative group*, Theorem 1.1](https://arxiv.org/pdf/math/0409604)

**Moving-target gcd.** Grieve–Wang Theorem 1.2 takes an infinite sequence of $S$-unit points in a fixed-dimensional torus over a fixed number field. Two polynomials are relatively prime, have fixed positive degrees, at least one has nonzero constant term, and their coefficient heights are $o(\max_i h(u_i))$. For each $\epsilon>0$, either the log-gcd is below $\epsilon\max_i h(u_i)$ on an infinite subset, or the full sequence lies in a finite union of proper algebraic subgroups translated by small-height data. At the fixed point $(2,3)$, the polynomials $X^A-Y^p$ and $\sum X^{e_i}Y^{p-1-i}$ have unbounded degrees. Introducing a variable per moving clock instead gives unbounded dimension. A compressed encoding must also verify polynomial coprimality and handle exceptional translates. PR #192 supplies the exact telescoping obstruction for a particular endpoint parametrization and genuine conditional estimates with cheap partitions. These theorem applications leave the exceptional individual gcd in (4) open. [Grieve and Wang, *Greatest common divisors with moving targets and consequences for linear recurrence sequences*, Theorem 1.2](https://arxiv.org/pdf/1902.09109)

**Arithmetic dynamics.** The shortcut map at every positive even integer equals $x/2$. A rational function over characteristic zero reproducing it on all positive integers would therefore equal $x/2$ identically, which fails on odd integers. Applying fixed-degree periodic-height theorems would require a different faithful encoding. The fixed-$d$ accelerated map does admit the generalized almost-boundedness theorem used in (6), with its density quantifier intact.

PR #192's two-cut and moving-partition estimates, PR #196's rotation and full-gcd tests, and PR #198's minimum-arc inequality restrict individual candidate cycles. Equations (4) and (6) sum over all words or over distinct cycles with one denominator. Neither summation proves a pointwise gcd gap on a final primitive positive integer word. Even complete cycle exclusion would require a separate proof excluding divergent positive orbits to establish convergence. Comparison pins are [#192](https://github.com/GettysburgResearch/collatz/tree/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124), [#196](https://github.com/GettysburgResearch/collatz/blob/27d03cfe902660e06604eb55bb28ca3d2754ff48/research/astra-orbit-cycle-20261124/cycles/ROTATIONAL_EXCLUSION.md), and [#198](https://github.com/GettysburgResearch/collatz/blob/c76acf99ba3fb05e7cc07ca7db7e467954c2d950/research/astra-frontier-20261124/MINIMUM_ARC.md).

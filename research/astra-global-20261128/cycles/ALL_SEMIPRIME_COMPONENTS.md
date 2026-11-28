# The complete component law among all semiprimes

Let $I_X=(X,2X]\cap\mathbb N$, with integer $X$. Sample either an ordinary uniform integer $u\in I_X$, or a uniform product of exactly two primes $m\in I_X$. The primes are unrestricted. Removing prime squares or even semiprimes changes the second probability by $o(1)$. Under the counted-pair synchronization input below, the two **entire distributions of eventual Collatz components** approach one another in total variation. The components are the equivalence classes for intersecting forward orbits of the shortcut map. They include every periodic basin and every possibly escaping component.

There is a uniform version for an odd multiplier $D$. If $\log(2D)=o(\log X)$, the component of $Dm$ has total-variation distance $o(1)$ from the component of a uniform ordinary integer in $(DX,2DX]$. The estimate permits arbitrary subpower $D=D(X)$ without any factorisation restriction. It also transfers the true first-hit times, odd counts, exact landing and a long terminal word, on the clearance described below. There is no hypothesis on zeros of any zeta or $L$-function. The Collatz synchronization and predecessor-density inputs are research-preprint results; the number-theoretic inputs here are published theorems.

For example let $d_y$ be the ordinary density of visits to a fixed odd target $y$ prime to three. Under the stated natural-density and positivity inputs the fraction of **all** squarefree semiprimes in each large octave which visit $y$ tends to $d_y>0$. If any positive orbit misses one, a fixed positive fraction of this full population misses one in every sufficiently large octave. In particular universal convergence is equivalent to the limsup of the relative proportion converging to one being one. The limiting fraction is the ordinary convergence density $d_1$. This changes the sampling population but does not determine $d_1$.

The prior [PR 213 restricted-semiprime theorem](https://github.com/GettysburgResearch/collatz/blob/f2fb6bd2ed9dd4172d9e2040ca6b9ca012ca8ae0/research/astra-global-rigidity-20261128/mersenne/SEMIPRIME_CANCELLATION.md) already proves that every fixed unit target has $\gg_y X/\log X$ semiprime ancestors without RH. Its semiprimes have a smaller prime in a specified polylogarithmic band, and it permits a prescribed multiplier of polynomial size for its positive lower bound. That entire band is a vanishing fraction of all semiprimes. [Paper 233](https://rstation.ai/problems/collatz/papers/233) gives an all-semiprime law additionally marking the smaller **prime** and the product, under ordinary RH and further Collatz inputs. The transfer here concerns the complete law of the product in the unrestricted semiprime population without RH, and below it applies independently at successive **semiprime** increments.

## A relative short-interval law for the sampling population

Write $L=\log X$, $H=\lfloor\exp(L/\log L)\rfloor$, and let $w(n)$ indicate an odd integer with exactly two distinct prime factors, each of multiplicity one. Put $G=X^{-1}\sum_{I_X}w(n)$. Landau's semiprime asymptotic gives $G\sim(\log\log X)/\log X$. One can also derive this normalisation by summing the prime number theorem over the smaller prime and using Mertens' theorem. The excluded squares contribute $O(\sqrt X)$, while the even semiprimes contribute $O(X/\log X)$. Define the relative window density
\[
                  S(u)=\frac1{HG}\sum_{1\le j\le H}w(u+j).
\]
Then
\[
                  \frac1X\sum_{u\in I_X}|S(u)-1|^2=o(1).                 \tag{1}
\]

Use Natalie Evans's Theorem 1.3 for the indicators of **all** products of exactly two primes, with $A=4$ and $B=5$. Its triangular application here only needs the upper bound for even shifts. Outside $O(HL^{-5})$ shifts, the correlation at even $0<h\le H$ is at most $(1+o(1))\mathfrak S(h)G^2$. The source's full normalisation equals $(1+o(1))G$. Odd shifts have exactly zero correlation for our odd $w$. The chosen $H=X^{o(1)}$ exceeds $\exp(L^{1-\varepsilon})$ for every fixed $\varepsilon>0$ and is well below $XL^{-4}$. It also accommodates the typical-factor proof in §9: $\exp(L/(\log L)^2)$ times any fixed logarithmic power is below $H$, and the corresponding exponent loss tends to zero. [Evans, *Correlations of almost primes*, Math. Proc. Cambridge Philos. Soc. 174 (2023), Theorem 1.3, p. 303 and §9](https://doi.org/10.1017/S0305004122000251)

For completeness the singular series has mean one. It vanishes for odd $h$ and at $h=2k$ is $2C_2\prod_{p\mid k,\,p>2}(1+1/(p-2))$, where $C_2=\prod_{p>2}(1-1/(p-1)^2)$. Expand over odd squarefree divisors $d\mid k$ with coefficient $g(d)=\prod_{p\mid d}1/(p-2)$. The normalized mean of the products tends to $\sum_d g(d)/d=\prod_{p>2}(1+1/[p(p-2)])=C_2^{-1}$ by dominated convergence. Partial summation gives $2H^{-2}\sum_{h<H}(H-h)\mathfrak S(h)\longrightarrow1$.

Now $E_{I_X} S=1+O(H/(XG))$. Expand the square. Its diagonal is $O(1/(HG))$ and shifting an octave endpoint costs $O(H/(XG^2))$ in the normalized second moment. For bad even differences use the trivial correlation at most one, at total cost $O(L^{-5}/G^2)=o(1)$. Summing the good even correlations with their triangular weights gives $\limsup E_{I_X}S^2\le1$. This proves (1) without interpreting a relative asymptotic with zero odd-shift main term.

## Keeping the physical source selector

Use Leen's arbitrary-offset pair theorem: for $d\ge1$, the proportion of residues $a\bmod 2^t$ on which $a,a+d$ have failed to agree in both shortcut state and cumulative odd count by date $t$ is
\[
                 \ll\sqrt{\frac{1+\log(1+d)}{t}}.                      \tag{2}
\]
The event is exactly periodic on ordinary source integers. Both state and odd count matter for first-hit clock marks. [Paper 209/v1, Theorem 4.2 and its attribution to Leen's unrefereed pair result](https://rstation.ai/problems/collatz/papers/209) · [Exact realization of the counted cylinders, Paper 124/v1, §6](https://rstation.ai/problems/collatz/papers/124/v1)

Fix $t=\lfloor(\log_2 X)/10\rfloor$ and $Q=2^t$. Every odd class $a\bmod Q$ holds at most $C XG/Q$ of our semiprimes in the relevant enlarged octave. Indeed factor $n=pq$ at its smaller odd prime $p\le\sqrt{3X}$. The other prime belongs to the single coprime class $q\equiv ap^{-1}\pmod Q$. By Brun–Titchmarsh it contributes $O(X/[p Q\log(X/(pQ))])\ll X/(p Q L)$ points, uniformly since $pQ\ll X^{0.6}$. Summing $1/p\ll\log\log X$ gives the claim; even classes contain none. Only an upper bound per binary cell is required. [Montgomery–Vaughan, *The large sieve*, explicit Brun–Titchmarsh bound](https://doi.org/10.1112/S0025579300004708)

Let $F$ have modulus at most one and take equal values on ordinary inputs in the product octave and its $O(DH)$ enlargement whenever they counted-fuse by $t$. It may vary with the octave, multiplier and the selected subset of eventual components. Uniformly for $1\le j\le H$ compare sources $Dm$ and $D(m-j)$ using offset $Dj$. Since $D$ is odd, the affine map to the lower source permutes the residue classes modulo $Q$. By (2) and the semiprime upper bound the normalized cost is
\[
            O(\epsilon_X),\qquad
 \epsilon_X=\sqrt{\frac{1+\log(2D)+\log(2H)}{\log X}}=o(1).
\]
Average over $j$ and move the two ends of the interval. With $E=E_{I_X}$ this gives
\[
 \frac{E[w(m)F(Dm)]}{G}
       =E[F(Du)S(u)]+O(\epsilon_X+H/(XG))
       =E[F(Du)]+o(1) .                                                   \tag{3}
\]
The last step is Cauchy–Schwarz and (1). For the ordinary sources compare $Du$ with $Du+i$, $0\le i<D$, again using (2) and invertibility of $D$ modulo $Q$. Integer periodic counting costs $O(Q/X)$ per normalized comparison. The blocks tile $(DX,2DX]$ up to $O(D)$ endpoints, so
\[
                 E[F(Du)]=E_{I_{DX}}F+O(\epsilon_X+Q/X+1/X).            \tag{4}
\]
Equations (3)–(4) hold uniformly for all the indicated bounded marks, and hence give total variation for the full countable component label.

For a finite stopping set below $B$, retain first shortcut time $s$, odd count $k$, exact landing $y$ and final $\ell$ parity bits. If $2^{t+\ell} B<DX/2$, all starts being compared exceed this bound for large $X$. As in [the stopped symmetry theorem](STOPPED_CLOCK_SYMMETRY.md), the first hit occurs after $t+\ell$, if it occurs, and all four discrete fields and the miss option agree on a counted merger. Thus one may use **arbitrary** bounded joint tests of these exact records, not only fixed clock residues. The real survival marks at a fused pair differ by $O(H/X)$ for the shifts here, so bounded-Lipschitz dependence on that additional coordinate is permitted. Total variation on its exact real atoms does not follow.

For any fixed finite clock modulus, the stopped symmetry theorem now yields Haar residues jointly with the discrete terminal fields, and bounded-Lipschitz independence with the real mark, relative to the entire unrestricted semiprime population. In positive-mass terminal samples, division by that fixed mass gives the conditional law. Uniform relative control after a vanishing-mass terminal selection would require an additional rate.

## Consequences for a single possible exceptional component

For fixed $y$ prime to three, the published research-preprint input gives existence and positivity of the ordinary predecessor density $d_y$; for odd $y$ ordinary and shortcut visits coincide. Apply (3)–(4) with $D=1$ to the true first-hit mark. A positive orbit missing 1 has an odd unit in its component: strip initial halvings and, if this odd state is divisible by three, take its next odd iterate. The positive-density set visiting that unit also misses one. Hence the ordinary convergence density $d_1$ is strictly below one, and the same positive deficit occurs in all sufficiently large full semiprime octaves. [Paper 12/v1, Theorem 1 under Inputs C–D, including density existence](https://rstation.ai/problems/collatz/papers/12/v1)

More generally fix $k$ and sample independent unrestricted squarefree semiprimes $m_j\in(Y_j,2Y_j]$ uniformly. Take all $Y_j\to\infty$ with $\sum_{i<j}\log(2Y_i)=o(\log Y_j)$ at each later stage. Write $D_j=\prod_{i\le j}m_i$. Conditional on **any** earlier odd product $D_{j-1}$, equations (3)–(4) give the ordinary component law at scale $D_{j-1}Y_j$, with uniform $o(1)$ error. Even sampled semiprimes have total probability $o(1)$. For fixed component events $E_j$ with ordinary natural densities $d_j$, it follows inductively that
\[
              \Pr\{D_j\text{ belongs to }E_j\ (1\le j\le k)\}
                          \longrightarrow \prod_{j=1}^k d_j.             \tag{5}
\]
The same fixed-event statement holds for hits at prescribed fixed odd unit roots. Pairwise repeated primes between sampled semiprimes occur with probability $o(1)$: for each of the finitely many earlier prime factors $p\le\prod_{i<j}2Y_i=Y_j^{o(1)}$, the fraction of semiprimes in the new octave divisible by $p$ is $O(1/(p\log\log Y_j))$ by the elementary prime count for the other factor. Thus one can also require all sampled primes to be distinct.

A single extra positive cycle $C$ would therefore produce any prescribed finite alternation between its basin and the basin of one on these **actual integer partial products** with positive limiting probability. Take $E_j$ to be visits to a selected odd site on the corresponding cycle. In particular the two-step mismatch from a start missing 1 to a product visiting 1 has limiting fraction $(1-d_1)d_1$, without RH, in two separated unrestricted semiprime octaves. This tests the exact fates of the semiprime partial products, not the fate of either individual prime inside an increment. The conclusion imposes no multiplication rule on actual Collatz paths and does not itself exclude an extra cycle.

## All products with a fixed number of prime factors

For every fixed $r\ge2$, uniform sampling on **all squarefree $r$-prime products** in $(X,2X]$ has the same full component law in total variation as uniform ordinary integers there, up to $o(1)$. Repeated prime factors can also be included: by the usual fixed-$r$ Landau asymptotic they have negligible relative proportion. Every transfer above for a component-union or for a cleared first-hit record remains uniform over its test sets. In this application $D$ varies, so choose a common sufficient clearance, for example $2^\ell B\le X^{4/5}$ for all large $X$.

The case $r=2$ is (3)–(4). For $r\ge3$ put $Z=X^{1/\log\log X}$. Sum over odd squarefree products $D\le Z$ of exactly $j=r-2$ primes, and complete each $D$ by an odd squarefree semiprime $m\in(X/D,2X/D]$. We may discard $(m,D)>1$ at uniform relative cost $O_r(1/\log\log X)$, as in the repeated-prime estimate above. For any uniformly bounded admissible mark $F$, the weighted completion count is
\[
       \frac{X\log\log X}{D\log X}\big(E_{I_X}F+o(1)\big),
\]
uniformly over these $D$. Indeed $Y=X/D$ satisfies $Y\ge X/Z$, $\log D=o(\log Y)$ and $\log Y\sim\log X$ uniformly. Replacing noninteger octave endpoints by their floors costs $O(1)$ on the parameter side and $O(D)$ on the product side. Equations (3)–(4) apply with product scale $X$ up to these negligible errors.

The reciprocal mass of the allowed prefixes is $(1+o(1))(\log\log Z)^j/j!$. To verify this without a cutoff subtlety, the unrestricted distinct-prime reciprocal sum with each prime at most $Z$ is asymptotic to this value by Mertens' theorem and the $O(1)$ repeated-prime square sum. Restricting each prime instead to $Z^{1/j}$ gives the same leading value and guarantees $D\le Z$. The fixed exclusion of two has no effect on it. Thus the total unweighted number of completions is
\[
                  (1+o(1))\frac{X(\log\log X)^{r-1}}{(r-2)!\log X}.
\]
A single $r$-prime product appears at most $r-1$ times, because its largest prime exceeds $X^{1/r}>Z$. It must therefore be one of the two primes in $m$, leaving at most $r-1$ choices for its partner. Landau's count of all squarefree $r$-prime products in the octave is $(1+o(1))X(\log\log X)^{r-1}/((r-1)!\log X)$. The unweighted completions saturate this multiplicity bound on average, so the total number of missing choices is $o$ of the full population. Removing this error in bounded marked sums proves the claimed total-variation transfer. This argument does not need the prime-only limit at $j=1$, since the prefix here is unmarked.

There is a corresponding joint law on one full almost-prime octave. Take $r=2a$ even and choose a uniform squarefree $r$-prime product $n$ in $(X,2X]$. Delete its largest prime together with one uniformly chosen partner from among the other primes. Iterate until two primes remain. In reverse order let $D_1,\ldots,D_a=n$ be the resulting partial products, so that $D_i$ has $2i$ prime factors. For any fixed component or first-visit events $E_i$ with ordinary densities $d_i$, the probability of $D_i\in E_i$ for every $i$ tends to $\prod_i d_i$.

For proof the base is the all-semiprime theorem. In one inductive deletion, bounded event indicators on earlier products can be averaged over the random deletions conditional on the remaining $j=r-2$ product $D$; denote the resulting prefix weight by $b(D)\in[0,1]$. Only the $o(1)$ fraction of missing partner choices from the unweighted argument is discarded. The marked completions at $D$ contribute $b(D)(d_a+o(1))X\log\log X/(D\log X)$ uniformly. By the induction hypothesis in ordinary product octaves, the mean of $b(D)$ among $j$-prime numbers in each growing octave tends to $\prod_{i<a}d_i$. Its mean in the reciprocal sum up to $Z$ has the same limit. For this last step partition into dyadic octaves or first pass to ordinary cumulative counting by dyadic summation, then use partial summation; the reciprocal mass diverges and bounded initial intervals disappear. The exclusion of even prefixes removes a lower-order reciprocal mass, by the same Mertens estimate in one fewer prime. Division by the full unweighted completion count proves the induction.

In particular take $r=4$. One uniformly chosen pair among the three smaller prime factors of a typical four-prime $n$ forms $D_1$. The exact limiting fraction for $D_1$ missing one and $n$ visiting one is $(1-d_1)d_1$. This uses **the entire four-prime product octave** and no preselected separated ranges for its factors. Every prescribed finite alternation of two positive-density cycle basins occurs with the product probability under these repeated random deletions in the full $2a$-prime octave. A deterministic rule selecting the two smallest factors is a different marking and is not included.

Under the ordinary RH Selberg prime-variance estimate the same source-smoothing proof can instead be run with primes and a polylogarithmic $H$. The variable-multiplier argument, upper bounds on failed binary cells, and short-interval step for primes already appear explicitly in [Paper 233, §3, equation (1)](https://rstation.ai/problems/collatz/papers/233), building on [Paper 221, “On the primes”](https://rstation.ai/problems/collatz/papers/221). The arbitrary-set fixed-date conclusion of Paper 233 already encompasses any union of eventual components. Proof (3) on all semiprimes uses Evans in place of that prime number-theoretic input and retains arbitrary discrete first-hit clock tests. In particular we do not infer an unconditional-in-RH prime-only source law from the almost-prime laws above.

[Exact native record, clock-character and semiprime incidence controls](check_stopped_semiprimes.py) · [Recorded finite counts](../../../reports/astra-global-20261128/cycles/STOPPED_SEMIPRIMES.json)

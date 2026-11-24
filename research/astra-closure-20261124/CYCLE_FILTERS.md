# Complete exclusions from physical residue profiles and two short power relations

**PROPOSED written proofs.** We use the shortcut map, taking one division by two on both branches. PR188 at `beed685ab713923191ae40c9559bf7400298d2d3`, `research/scalar-carry-cocycle-20261124/RESIDUE_NORM.md`, RN1–3, supplies the starting full-gcd norm. Here the single interior interval is excluded at *every* period. We also exclude entire families with arbitrarily many disjoint residue intervals. The independent two-binomial estimate in §4 admits full-modulus tests that do not require a small norm against $X^p-2$ alone.

## 1. Full denominator and physical legality

A candidate positive integer cycle has $p$ odd steps, $A$ total steps, positive gaps $a_i=d_{i+1}-d_i$, $d_0=0$, $d_p=A$, and $D=2^A-3^p>0$. The odd starting state equals $C/D$, where $C=\sum_{i=0}^{p-1}3^{p-1-i}2^{d_i}$. Below the residue profile requires $\gcd(A,p)=1$. Rotate at a minimum of $p d_i-Ai$ and write $p d_i-Ai=r_i+p k_{r_i}$, $0\le r_i<p$. Then $r_i=-Ai\bmod p$ permutes all residues, $k_r\ge0$ and $k_0=0$. Set $F=\sum_{r=0}^{p-1}2^{k_r}X^r$ and $R=\mathbb Z[X]/(X^p-2)$.

For any common divisor $M>1$ of $C,D$, the units 2 and 3 modulo $M$ admit a common root $x$ with $x^p=2$, $x^A=3$. Indeed take $x=2^b3^{-c}$ for $bp-cA=1$. Termwise $C=3^{p-1}F(x)\bmod M$, so $F(x)=0$. A nonzero $G=\sum_{j<p}g_jX^j$ in $R$ with $G(x)=0$ satisfies

$$M\mid N(G),\qquad 0< |N(G)|\le \left(\sum_{j<p}g_j^2 2^{2j/p}\right)^{p/2}. \tag{1}$$

The evaluation row annihilates its multiplication matrix modulo $M$; multiplying by the integer adjugate gives the full divisibility, also for prime powers. Eisenstein irreducibility gives nonvanishing. For the upper estimate take the geometric mean of $|G(2^{1/p}\zeta_p^j)|^2$ over all $p$-th roots and apply arithmetic–geometric mean and Fourier orthogonality. All multiples of $F$ and $X^A-3$ qualify when their remainder is nonzero. In an integer cycle take $M=D$.

Write $s=A-p$. Multiplying the actual odd-state equations gives $2^A=\prod_i(3+1/q_i)$ for odd states $q_i$. A nontrivial cycle has $q_i\ge3$, so $p<A<7p/4$ by $(10/3)^4<2^7$. In particular $0<s<p$. The next residue is $r'=(r-s)\bmod p$. Subtracting the two discrepancy equations gives the **exact gap**

$$a_i=1+\mathbf1_{r<s}+k_{r'}-k_r.\tag{2}$$

Thus $k_{r-s}\ge k_r$ for $r\ge s$, in particular $k_s=0$. Conversely the displayed gaps being positive is precisely the positive-gap condition on such a normalized profile. Formula (2) also identifies the coefficient of $X^r$ in $(X^s-1)F$ in $R$ as $2^{k_r}(2^{a_i-1}-1)$. It vanishes exactly on a unit gap. This positive filter has norm multiplier $|2^s-1|$, since $\gcd(s,p)=1$; positivity alone does not bound $N(F)$.

## 2. An explicit denominator floor at every possible nontrivial cycle

We use a published result with its verification input. J. Simons and B. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70, Corollary 2 and Lemma 12, give $p>2.2564\cdot10^8$ and $\Lambda>\exp[-13.3(0.46057+\log p)]$. Their $K=p$ counts odd steps, their $L=A-p$ counts even steps and their $\Lambda=A\log2-p\log3$. Their Corollary 2 uses Crandall’s convergents and the reported verification floor $X_0=301\cdot2^{50}$; Lemma 12 uses Rhin’s linear-form bound. The paper treats the one-local-minimum case through Steiner’s exclusion. These are external dependencies. We did not replay the historical distributed computation. [Publisher's paper, §§1.2–1.4, 3.1, 5](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).

For $2^n\le p<2^{n+1}$, $n\ge20$, we have $42000(n+2)<2^n$: check $n=20$ and double. Hence $p/3000>14(n+2)>13.3(0.46057+\log p)$. Also $\log(3000/2999)>1/3000$ by integration. Thus

$$D=3^p(e^\Lambda-1)>3^p\Lambda>(2999/1000)^p.\tag{3}$$

No residue patterns or huge periods have to be enumerated to obtain (3). For later use $A/p<8/5$ follows from $q_i>64$ and $(3+1/64)^5<2^8$, so $s<3p/5$.

## 3. One interval and all progressions of stride at most four

**CF1.** If $k_r=1$ on $[u,v)$ with $0<u<v\le p$ and is zero otherwise, there is no nontrivial positive integer cycle. The downwards condition (2) forces $v\le s$: otherwise $s$ lies in the interval or, if $u>s$, $u$ is elevated and $u-s$ is not. This already excludes a terminal interval ending at $p$. For the other intervals $(X-1)F=1+X^v-X^u$ in $R$. Its weighted squared coefficient norm in (1) is at most $1+2\cdot2^{3/2}<7$, by $u<v\le s<3p/4$. This contradicts (3). It also follows directly by combining PR188 RN3 with (3).

**CF2.** Fix any $t\in\{1,2,3,4\}$ and let the elevated residues be exactly $u,u+t,\dots,u+(m-1)t$, with $m\ge1$, $u>0$ and last term $<p$. The elevation is one and it is zero elsewhere. No nontrivial positive integer cycle has this profile. Put $v=u+mt$ and $B_t=1+\cdots+X^{t-1}$. Before reducing the final power, the exact filter is

$$(X^t-1)F=B_t+X^v-X^u\quad\text{in }R.\tag{4}$$

If every elevated point is $<s$, then $v<s+t\le3p/5+4\le5p/8$. Each baseline power has squared weight $2^{2j/p}<33/32$ ($j<t$, $p\ge2^{20}$); each remaining monomial has squared weight $\le2^{5/4}<12/5$. Should $u<t$, its negative coefficient cancels a baseline term. The weighted squared sum of the reduced coefficients is at most $4(33/32)+2(12/5)<(2999/1000)^2$. Nonvanishing follows from (4) as a product in the field of fractions of $R$, since both factors are nonzero. Apply (1) and (3).

If there is an elevated point $r\ge s$, its successor $r-s$ is elevated too. Thus $t\mid s$, and the minimum elevated point $u$ is below $s$ by (2). At the first elevated $r\ge s$, one has $0\le r-s<t$, hence $u<t$. Formula (4) now reads $B_t-X^u+X^v$, with nonnegative coefficients. If $v<p$, its squared weighted sum is $\le3(33/32)+4<(2999/1000)^2$. If $v\ge p$, then $v<p+t$, and its remainder is $B_t-X^u+2X^{v-p}$, of degree $<t$ and coefficient sum $t+1\le5$. The short relation criterion of §4 excludes it, including coefficient collisions. For $t=2$ there is a simpler independent ending: $u=1$, so $x^v=-1$ and $D\mid 2^v-(-1)^p$. This is a nonzero integer of absolute value at most $2^{p+1}+1<(2999/1000)^p$ for $p\ge2^{20}$.

## 4. A simultaneous resultant bound for ordinary low-degree residuals

**CF3.** Suppose the complete-modulus root $x$ of an actual nontrivial integer cycle annihilates a nonzero $G\in\mathbb Z[X]$. Write $h=\deg G$ and $M(G)=|\operatorname{lc}(G)|\prod_{G(\alpha)=0}\max(1,|\alpha|)$ with multiplicities. Then

$$D\le M(G)^{p/32}\,(2^{67})^{h}.\tag{5}$$

In particular $h\le p/100$ and $\sum|g_j|\le10$ are impossible. This applies whether or not the corresponding norm against $X^p-2$ is small.

From the product formula and $q_i>2^{20}$,

$$2079/1312 < \log_2 3 < A/p < \log_2(3+2^{-20}) <65/41.$$

The strict endpoints are exact integer comparisons $2^{2079}<3^{1312}$ and $(3\cdot 2^{20}+1)^{41}<2^{65+820}$. Since $19/12<2079/1312$ and $65/41<609/384$, the integers $c_1=12A-19p$ and $c_2=65p-41A$ both belong to $(0,p/32)$. The two polynomials

$$Q_1=2^{19}X^{c_1}-3^{12},\qquad Q_2=3^{41}X^{c_2}-2^{65}$$

vanish at $x\bmod D$. They have no common complex root: such a root would give $(3^{12}/2^{19})^{c_2}=(2^{65}/3^{41})^{c_1}$, whose sides have opposite valuations at 2. Both coefficient sums are $<2^{67}$.

Factor $G=b\prod_i P_i$ over the integers, with primitive irreducible factors repeated with multiplicity. For each $P_i$ choose a $Q_j$ with no common complex root. The nonzero integer $R_i=\operatorname{Res}(P_i,Q_j)$ is an integer-polynomial combination of $P_i,Q_j$ (Sylvester adjugate). Thus $\gcd(D,P_i(x))\mid R_i$ for any integer lift of $x$. At each prime of $D$, divisibility $D\mid b\prod_iP_i(x)$ implies $D\mid |b|\prod_i |R_i|$ by adding the truncated valuations. For a root $\alpha$ of $P_i$,

$$|Q_j(\alpha)|\le \|Q_j\|_1\max(1,|\alpha|)^{c_j}.$$

The root product for the resultant yields $|R_i|\le M(P_i)^{c_j}\|Q_j\|_1^{\deg P_i}$. Each primitive $M(P_i)\ge1$ and $p/32>1$. Multiply, using multiplicativity of $M$, to obtain (5), including constant $G$. Jensen's unit-circle formula gives $M(G)\le\|G\|_1$ (equivalently apply the usual one-variable Mahler bound). Under the displayed numerical hypotheses the bound is $\le 10^{p/32}2^{67p/100}<2^p$, since $10<2^4$ and $4/32+67/100<1$. This contradicts (3).

## 5. Periodic blocks of raised residues

**CF4.** Suppose the elevated set is a disjoint progression of equally long intervals, $[u+jt,u+jt+w)$ for $0\le j<m$, with $0<u$, $1\le w<t$, $m\ge1$, unit elevation and zero elsewhere. If the six exponents $0,t,u+w,u,u+mt+w,u+mt$ are distinct and at most $p/4$, this whole family is excluded. Indeed in $R$ one obtains

$$(1-X^t)(X-1)F=(1-X^t)+X^u(X^w-1)(1-X^{mt}).$$

All six nonzero coefficients have absolute value one; their weighted squared sum is at most $1+5\sqrt2<(2999/1000)^2$. Apply (1) and (3). The degree and distinctness assumptions here can be replaced by the actual weighted coefficient inequality after collecting the terms.

This allows unbounded $m$ even near the critical slope. For example take upper continued-fraction convergents $A/p$ to the irrational $\log_2 3$ and use $w=2,t=4,u=1$, with $m$ tending to infinity subject to $4m+3\le p/4$. All elevated residues lie below $s$ for large $p$; (2) gives positive literal gaps because all heights belong to $\{0,1\}$. Thus these do define rational positive cycles with $D>0$. Their odd states can have arbitrarily large minimum: at any odd rotation the normalized discrepancies divided by $p$ are differences of two numbers in $[0,2)$, so $d_i-Ai/p>-2$. Then each numerator term is at least $3^{p-1}/4$ as $2^{A/p}>3$. The minimum is at least $p/(12(e^\Lambda-1))$, which diverges along these convergents. The profile obstruction is genuine even for large-minimum rational cycles.

## 6. Arbitrary support inside short bands

**CF5 (complete, no pattern assumption inside the band).** No nontrivial positive integer cycle with these coprime counts has all its elevations supported in $1\le r\le10^6$. Indeed $W=10^6<s$ by $A/p>3/2$ and the published odd-period bound. Also $W<p-s$ since $s<3p/5$. For every $r\le W$, $r'=r+p-s>W$ and (2) forces $k_r\le1$. Thus $G=(X-1)F=1+(X-1)\sum_{r\le W,\, k_r=1}X^r$ has degree $\le W+1$ and every coefficient has absolute value at most one. It is nonzero. Consequently $\|G\|_1\le W+2<2^{20}$ and $\deg G\le p/200$. Inequality (5) gives $D<2^{(20/32+67/200)p}<2^p$, contradicting (3). The same argument in the pure zero profile has $G=1$.

**CF6 (effective asymptotic obstruction).** Fix real $0<\epsilon<1$ and $K>0$. For every sufficiently large coprime period $p$ of a nontrivial positive integer cycle, its full-modulus root cannot annihilate any nonzero integer polynomial $G$ simultaneously satisfying $\deg G\le p^{1-\epsilon}$ and $\|G\|_1\le p^K$. The cutoff is effective in these parameters using an effective linear-forms theorem. Thus every sufficiently large such cycle has some positive elevation beyond $p^{1-\epsilon}$, even without restrictions on the profile inside that band. As usual changing the cutoff or passing to an arbitrary sequence of fixed epsilons requires keeping the quantifiers above.

Here is a proof. Because the counts are coprime, the word has its minimal period: a repeat would divide both counts. All $p$ odd states $q_i$ are therefore distinct. Ordering these integers and bounding them below by $1,2,\ldots,p$ in order gives

$$0<\Lambda=\sum_i\log(1+1/(3q_i))\le(1+\log p)/3.\tag{6}$$

Write $\alpha=\log 3/\log 2$ and $B=p^{\epsilon/2}$. There are effective constants $c>0,\kappa\ge1$ with $|a-b\alpha|\ge c b^{-\kappa}$ for all positive integers $a,b$ with $a/b$ in $[1,2]$. This is the standard two-logarithm *arbitrary coefficient* bound for $a\log2-b\log3$, for example from E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64 (2000), 1217–1269, Corollary 2.3, [DOI](https://doi.org/10.1070/IM2000v064n06ABEH000314). This input is stronger in quantifier scope than the cycle-specific Lemma 12 quoted in §2. Any finite effective irrationality measure suffices here.

Let $a_n/b_n$ be the last convergent to $\alpha$ with $b_n\le B$. For large $p$ use it and the preceding convergent. The next denominator is $>B$ and $c b_n^{-\kappa}\le|a_n-b_n\alpha|<1/b_{n+1}$, so $b_n>(cB)^{1/\kappa}$. Both selected pairs $(a,b)$ have $a,b=O(B)$ and approximation errors $|a-b\alpha|<1/b_n=O(B^{-1/\kappa})$ (for the last pair use its next denominator). Thus by (6),

$$|ap-bA|=O(p B^{-1/\kappa}+B\log p)=o(p/\log p).$$

The exponent is nonzero since $0<b<p$ and $\gcd(A,p)=1$. Each $x^{ap-bA}=2^a3^{-b}$ in the unit group modulo $D$ gives an integer binomial with degree $|ap-bA|$ and coefficient sum $2^a+3^b=\exp(O(B))$, inverting the relation if its exponent is negative. These two binomials have no common complex root: powering up would make the rational numbers $2^{a_1}3^{-b_1}$ and $2^{a_2}3^{-b_2}$ multiplicatively dependent, contrary to the determinant $\pm1$ of the consecutive convergents. Applying the same factorwise resultant argument as (5) gives

$$\log D\le o(p/\log p)\log\|G\|_1+O(B)\deg G=o(p),$$

contradicting (3). Every asymptotic comparison here follows from explicit powers and the effective constants of the cited theorem. This is a sufficiently-large-period result, not a complete check of its finite remainder. For the stated profile consequence use $W=\lfloor p^{1-\epsilon}\rfloor$, which eventually lies below both $s$ and $p-s$. Then (2) forces every elevation in that band to be at most one, and the polynomial used in CF5 has degree $\le W+1$ and coefficient sum $\le W+2$. Apply the polynomial criterion with, for example, $\epsilon/2$ to absorb the additive endpoint.

**Why CF6 cannot simply say every sublinear degree.** For every modulus $1<M<4^p$ and every residue $x$, take $h=\lceil2p/\log_2 p\rceil$ for $p\ge4$. More than $M$ polynomial coefficient strings in $\{0,\ldots,p\}^{h+1}$ have to take the same values modulo $M$ in at least one pair. Their nonzero difference has degree $\le h=o(p)$, coefficient sum at most $p(h+1)\le p^3$, and vanishes at $x$. This general pigeonhole obstruction applies at the size of cycle denominators since $A<2p$. It is independent of the existence of a nontrivial cycle.

## 7. The reduced-clock obstruction for every primitive cycle

**CF7.** Take the *least actual period* of any nontrivial positive integer cycle. Put $g=\gcd(A,p)$, $a=A/g$, $b=p/g$, $D_1=2^a-3^b$. For every fixed $0<\epsilon<1$, every sufficiently large such period has some normalized defect at a reduced residue $r>b^{1-\epsilon}$. This includes unbounded and noncoprime clock gcds. Its proof only needs the principal factor of the complete denominator: failure of divisibility by even one *necessary* factor excludes the integer cycle.

Indeed $D_1>0$ divides $D$, so $D_1\mid C$. As $a,b$ are coprime there is a root $x^b=2$, $x^a=3\bmod D_1$. Rotate the $p$ odd positions at a minimum of $b d_i-a i$. Write $e_i=b d_i-a i=r_i+b k_i$ with $k_i\ge0$ and $0\le r_i<b$. Each residue $r_i=-a i\bmod b$ is visited $g$ times. The heights at different visits can differ. Put

$$F_1=\sum_{i=0}^{p-1}2^{k_i}X^{r_i}.$$

Since $x^{e_i}=2^{d_i}3^{-i}$, one has $F_1(x)=0\bmod D_1$. This is the principal-component evaluation of PR191, TCP-4. Other cyclotomic factors can have zero norms and need no cancellation assumption here.

Write $\lambda_1=a\log2-b\log3=\Lambda/g$. The odd states of a least-period cycle are distinct, so (6) still holds. Consequently

$$0<\lambda_1\le(1+\log(gb))/(3g)\le(1+\log b)/3.$$

The arbitrary-coefficient lower bound in §6 gives $\lambda_1\ge c' b^{-\kappa}$ because $1<a/b<2$. It follows that $D_1=3^b(e^{\lambda_1}-1)\ge3^b c' b^{-\kappa}$. Moreover $g c' b^{-\kappa}\le (1+\log(gb))/3\le 2\sqrt{gb}/3$, hence $g\le C b^{2\kappa+1}$. In particular $b$ grows when the primitive $p$ grows. Apply the two-convergent proof of CF6 with $(p,A,D,\Lambda)$ replaced by $(b,a,D_1,\lambda_1)$. The required upper approximation error and positive exponential denominator lower bound have both just been proved. Thus $x\bmod D_1$ cannot annihilate a nonzero $G$ with degree $\le b^{1-\eta}$ and coefficient sum $\le b^K$, for fixed $\eta,K>0$ and all sufficiently large $b$ (take $\eta<1$).

Finally let $W=\lfloor b^{1-\epsilon}\rfloor$, assume all elevations have $r_i\le W$, and set $s'=a-b$. Since $3/2<a/b<8/5$, eventually $W<\min(s',b-s')$. The gap identity (2) applies visit by visit with $b,s'$ and successive heights $k_i,k_{i+1}$. A visit with $r_i\le W$ has $r_{i+1}=r_i+b-s'>W$, so $k_{i+1}=0$ and positivity gives $k_i\le1$. Consequently in $\mathbb Z[X]/(X^b-2)$,

$$(X-1)F_1=g+(X-1)\sum_{i:k_i=1}X^{r_i}.$$

The right-hand side is a nonzero ordinary polynomial (its value at 1 is $g$), with degree $\le W+1<b$ eventually and coefficient sum at most $g+2p$. The polynomial bound on $g$ makes this at most $b^K$ for an effective fixed $K$. Taking $\eta=\epsilon/2$ contradicts the reduced-clock obstruction. No finite remainder is asserted checked. Widely spread profiles, including ones with a single sufficiently distant defect, are outside this result.

## Scope

These proofs exclude specified full profile classes from positive integer cycles. The two-binomial criterion needs a sufficiently small residual polynomial; no construction supplies one for every profile. Without coprime clocks the full-modulus root of §§1–6 is not supplied by PR188; §7 uses only the principal component. PR191 at `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, TCP-4, instead gives cyclotomic components with possible zero norms and shared prime powers. The unrestricted cycle question and divergent trajectories remain open. The accompanying exact controls check constants and small-data identities; the external analytic inputs, norm estimates and complete family theorem are written mathematics. Lean coverage is restricted to the declarations in `CycleDefectFilters.lean`.


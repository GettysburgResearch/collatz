# Multiplicative dependence of actual Collatz local minima

**PROPOSED written theorems.** Across all positive integer orbits there are only finitely many transitions between multiplicatively dependent consecutive local minima greater than one, even when their common base varies. The second must be the primitive integer base of the first. In particular every nontrivial primitive ordinary cycle contains a pair of multiplicatively independent local minima, even if the number of intervening odd phases is arbitrarily large. More generally, across the entire ordinary graph, there is a uniform finite bound on the number of distinct starting values in a prescribed multiplicative coset that can reach a second prescribed coset in a fixed number of mountains. The individual lengths of both runs in each mountain are unrestricted. The bound depends only on the two ranks and the number of mountains. The general exclusion of nontrivial cycles and escape is open.

Use the shortcut map which halves an even positive integer and sends an odd one to $(3x+1)/2$. For any odd start $x$, follow $k=v_2(x+1)\ge1$ consecutive odd steps to an even peak, then $l\ge1$ consecutive even steps to the next odd integer $y$. Call this complete segment a mountain and write $y=V(x)$. In a periodic trajectory the entries of these mountains are exactly the local minima. With $x+1=2^k a$, $a$ odd, the exact peak and endpoint equations are

$$
3^ka-1=2^l y,\qquad 2^{k+l}y=3^kx+3^k-2^k.\tag{1}
$$

The first formula also proves that $k$ is the exact length of the odd run. These are the classical chain equations of Simons and de Weger. [Primary paper, §2.1](https://doi.org/10.4064/aa117-1-3)

## A dependent transition determines its target

Let $x,y>1$ be successive mountain entries. If they are multiplicatively dependent, unique factorization gives a unique common integer base $b>1$ which is not a proper integer power, with $x=b^s,\ y=b^t$ and $s,t\ge1$. Indeed their vectors of prime exponents lie on the same positive rational ray and its primitive integral vector gives $b$. Here $b$ is odd, so $b\ge3$.

Equation (1) gives $b^{\min(s,t)}\mid 3^k-2^k$. If $s$ is even, $b^s\equiv1\pmod4$, hence $k=1$, contrary to $b\mid 3-2$. Thus $s$ is odd. The quotient $(b^s+1)/(b+1)$ is an alternating sum of an odd number of odd integers and is odd. Consequently $k=v_2(b+1)$, and $k=1$ is again impossible. For $k\ge2$, $3^k\le(2^k-1)^2$: equality holds at $k=2$, and $3(u-1)^2<(2u-1)^2$ for $u\ge1$ proves the induction. Therefore

$$
0<3^k-2^k<b^2,\qquad \min(s,t)=1.\tag{2}
$$

If $s=1$, the peak plus one equals $(3/2)^k(b+1)< (b+1)^2$, since $(3/2)^k<2^k\le b+1$. At least one halving follows. Hence $y<(b+1)^2/2<b^2$ for $b\ge3$, forcing $t=1$. In all cases **$y=b$**. For two consecutive dependent transitions among values greater than one the middle value is already primitive, so the following value equals it. Every increasing transition between such local minima has multiplicatively independent endpoints.

On a primitive ordinary cycle a proper period cannot contain two equal local minima. If all its minima lie in one rank-one group, the preceding argument makes the cyclic list weakly decreasing, hence constant. The cycle has one mountain. Steiner’s one-circuit theorem excludes it unless it is $1\to2\to1$. This uses a theorem on the complete one-circuit return. For a general primitive parity word of length $A$ with $P$ odd bits and carry $C$, the condition remains $(2^A-3^P)\mid C$ and $2^A>3^P$. None of the divisibilities in (2) substitutes for it. [Steiner’s account, pp. 285–286](https://www.fq.math.ca/Scanned/19-3/steiner.pdf) · [Simons and de Weger, §2.1](https://doi.org/10.4064/aa117-1-3)

## Only finitely many dependent edges in the entire graph

For a dependent edge let $U=2^k$, $W=3^k$, $a=(b+1)/U$, and $c=(W-U)/b$. These are positive integers by (1)–(2). Since $b\ge U-1$ and $W<U^2$, the identity $bc+U=W$ forces $c<U$. Also $Uc\le(b+1)c=W-U+c<W$. The two integer relations give

$$
W+c=U(ac+1),\qquad 0<\frac cU<\frac W{U^2}=\left(\frac34\right)^k.\tag{6}
$$

Thus $(3/2)^k$ is within $(3/4)^k$ of an integer. Mahler’s fractional-parts theorem says that for relatively prime integers $u>v\ge2$ and every $\epsilon>0$, the distance of $(u/v)^k$ to the nearest integer is less than $e^{-\epsilon k}$ for only finitely many $k$. Apply it at $(u,v)=(3,2)$ with $\epsilon=\log(4/3)$. Each remaining $k$ determines at most one possible $b$: $c$ is the unique integer in $[1,U-1]$ congruent to $-W$ modulo $U$, and $b=(W-U)/c$. For fixed $b$, (3) below with $h=1$ and $G_0=G_1=\langle b\rangle$ leaves only finitely many sources $b^s$. This proves the finiteness claim without fixing the base in advance. [Mahler, *On the fractional parts of the powers of a rational number (II)*, Theorem 2](https://doi.org/10.1112/S0025579300001170)

To identify the precise Waring condition, divide $W=Uq+r$ with $0<r<U$. Then $c=U-r$ and (6) gives $q=ac$. Here $a>1$. Indeed $a=1$ would give $b=2^k-1$ and $b\mid3^k-1$. For even $k$ this is impossible modulo 3. For odd $k\ge3$, $b\equiv7\pmod{12}$, so quadratic reciprocity gives Jacobi symbol $(3/b)=-1$. Yet $3^k\equiv1\pmod b$ would make $3$ a square modulo $b$, with square root $3^{(k+1)/2}$. Thus $q+r-U=(a-1)c>0$. A dependent pair would force the strict exceptional branch of the integer inequality in the ideal Waring problem. It would also require $c\mid q$ and the actual Collatz endpoint equation (1).

Kubina and Wunderlich's published computation covers the ideal-Waring range through $471{,}600{,}000$. Habsieger explicitly records the fractional-part inequality verified on that range in §1, (1.1). Thus a nontrivial dependent pair would require **$k>471{,}600{,}000$**. This is an imported computation. Zudilin’s effective lower bound $0.5803^k$ after an effectively computable threshold is smaller than the exponential threshold $(3/4)^k$ in (6). These bounds leave the possible exceptional exponents above the verification range undecided. [Kubina and Wunderlich](https://www.jstor.org/stable/2008448) · [Habsieger, §1](https://www.impan.pl/shop/en/publication/transaction/download/product/82203) · [Zudilin, Theorem 1](https://doi.org/10.5802/JTNB.588)

In particular, along any single escaping positive orbit **every sufficiently late pair** of consecutive local minima is multiplicatively independent. Only finitely many distinct primitive ordinary cycles could contain even one dependent edge with both entries greater than one. Mahler’s theorem in this form supplies no explicit largest exceptional $k$. A finite exact filter below rules out $2\le k\le4096$ by checking $Uc<W$ on the unique residue. This checks a height range, without asserting that the global exceptional set is empty.

## A bound on the full numerical gcd at every mountain

For every ordinary mountain $x\to y$, write $g=\gcd(x,y)$, $u=x/g$, $v=y/g$ and $c=(3^k-2^k)/g$. These are positive integers by (1), and
$$
                       3^k u+c=2^{k+l}v.\tag{7}
$$
The three signed terms give a primitive integer zero-sum tuple: $c$ is coprime to six, and a prime outside $\{2,3\}$ common to the tuple would divide both $u$ and $v$. Positivity excludes any proper zero subsum. Evertse's Corollary 1 for $S=\{2,3\}$ implies, for every $0<\epsilon<1$, that the product of the prime-to-$S$ parts is at least $C_\epsilon$ times the maximum coordinate absolute value to the power $1-\epsilon$. Its finite exceptional tuples can be absorbed by lowering $C_\epsilon>0$. Here the product is at most $uvc$ and the height is at least $3^ku$. Therefore $vc\ge C_\epsilon\,3^k(3^ku)^{-\epsilon}$. As $vc=y(3^k-2^k)/g^2$, we obtain
$$
                 g^2\le C_\epsilon^{-1} y(3^kx)^\epsilon.
$$
Since $2^k\le x+1$ and $y<(x+1)^{\log_2 3}$, this gives $g\le\sqrt y\,x^{o(1)}$ and $x/g\ge x^{1-(\log_2 3)/2-o(1)}$, uniformly over all positive odd sources as $x\to\infty$. Thus each mountain sheds a positive power of its initial value even if the initial and terminal values have arbitrary prime supports. It can acquire new factors in its target. [Evertse, *On sums of S-units and linear recurrences*, Corollary 1, p. 227](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

## A uniform return bound with arbitrary run lengths

Let $h\ge1$, let $G_0,G_1\subset\mathbb Q_{>0}^{\times}$ have finite ranks $r_0,r_1$, and let $a_0,a_1>0$ be rational. Write $r=r_0+r_1$, $T=8h$, and define

$$
 E_j(r)=\exp\!\left((6(2j+1))^{3(2j+1)}(r+2j+1)\right),\qquad
 B_h(r)=T+E_h(r)+T\sum_{1\le j<h}E_j(r).
$$

Then

$$
\#\{x\text{ positive odd}: x\in a_0G_0,\ V^h(x)\in a_1G_1\}\ \le B_h(r).\tag{3}
$$

This is an absolute count over all ordinary sources. The groups and coset representatives can be selected after the sources have been observed, provided the same pair is used for the count.

**Signed relation.** For $j$ mountains write $x=x_0,\ldots,x_j=z$, odd-run lengths $k_i$, even-run lengths $l_i$, prefix odd counts $P_i=\sum_{v<i}k_v$, and prefix clocks $A_i=\sum_{v<i}(k_v+l_v)$. Put $P=P_j, A=A_j$. Define the two positive boundary weights of each odd run by

$$
u_i=2^{A_i}3^{P-P_i},\qquad v_i=2^{A_i+k_i}3^{P-P_i-k_i}.
$$

Telescoping (1) gives the entire signed relation

$$
3^P x+\sum_{i<j}(u_i-v_i)-2^A z=0.\tag{4}
$$

All $2j$ signed terms inside the sum have distinct dyadic valuations because $k_i,l_i\ge1$. Every nonempty subcollection of those terms has a unique lowest dyadic valuation, so its signed sum is nonzero.

**Checking every vanishing subsum.** Suppose that the entry valleys $x_0,\ldots,x_{j-1}$ are greater than $T$, with $j\le h$. The final $z$ may be small. The scaled initial endpoint is $M=3^P x$. If $p_i$ is the even peak, then

$$
 v_i(p_i+1)=u_i(x_i+1),\qquad u_{i+1}x_{i+1}=v_i p_i
$$

where $u_j=2^A$. The scaled state at the start of the next mountain is at most $(1+1/T)$ times the preceding scaled valley. This also bounds the intervening scaled peak. Since $p_i>x_i>T$, each $u_i,v_i$ is smaller than $2M/T$ using $(1+1/T)^h\le e^{1/8}<2$. Consequently the sum of the absolute values of all $2j$ interior terms is less than $4hM/T<M$. A zero subsum containing the initial endpoint must include the final endpoint. A zero subsum containing the final endpoint alone would give one containing the initial endpoint alone by complementation. A proper zero subsum containing both would leave a nonempty atom-only zero subsum. The whole tuple (4) is therefore nondegenerate, including when the final endpoint is small or happens to equal the initial source.

**Applying the unit equation.** Divide by $u_0=3^P$ and move its term to the right to get a single equation with right side one and $n=2j+1$ nonzero left coordinates. Write $x=a_0g$, $z=a_1g'$ and absorb signs and the two fixed coset representatives in the coefficients. The tuple of variables lies in a subgroup of $(\mathbb Q^\times)^n$ of rank at most $r+2j$. To see the joint rank, let the $2j$ clock exponents $k_i,l_i$ vary over all integers in the monomial expressions. This defines a homomorphism from $\mathbb Z^{2j}$. Adjoin the initial coordinate group $G_0$ and the terminal coordinate group $G_1$ independently. Each tuple determines $x$ by its first coordinate $g$. Evertse–Schlickewei–Schmidt's nondegenerate unit-equation theorem gives at most $E_j(r)$ tuples. The bound counts sources, so injectivity in the run lengths is unnecessary. The theorem allows all fixed rational coefficients here. [Evertse–Schlickewei–Schmidt, Theorem 1.1 in the printed paper](https://arxiv.org/pdf/math/0409604)

**Small intermediate entries.** At most $T$ starting integers have $x\le T$. For the other starts, either all $h$ entry valleys exceed $T$, already counted, or the first small entry occurs after $1\le j<h$ mountains. Fix its value from the at most $T$ possibilities. Apply (4) to the prefix with this fixed endpoint as a coset of the trivial group. All its entry valleys exceed $T$. Summing the bounds gives (3), with no assumption about the remaining run lengths. This use of finitely many small integers is specific to ordinary sources.

## Minima on one source and the remaining global question

Take $M$ distinct consecutive mountain entries on one positive trajectory, or once around a primitive cycle. Suppose at least $\delta M$ entries are in a union of $s$ cosets of a common rank-$r$ group. With $H=\lceil 4/\delta\rceil$, at most $M/H$ gaps between successively selected entries exceed $H$ in mountain count. For $M\ge4/\delta$ there are therefore at least $\delta M/2$ distinct selected starting entries whose next selected entry is within $H$ mountains. Applying (3) to all ordered pairs of cosets and all these distances gives

$$
\delta M/2\ \le\ s^2\sum_{h=1}^{H}B_h(2r).\tag{5}
$$

The right side is at most $s^2\exp(O_\delta(r+1))$. In particular any positive-proportion selection of local minima generates rank at least $c_\delta\log M-O_\delta(1)$. For a fixed finite union of finite-rank cosets on an escaping trajectory, gaps between successive visits tend to infinity in mountain count. Infinite escape indeed has infinitely many mountains since each positive entry has finite odd and even run lengths. The bound permits the minima to occupy a vanishing fraction of ordinary odd time. For each fixed rank only finitely many distinct primitive ordinary cycles can have all minima of that rank or lower: (5) bounds the number of local minima and the classical fixed-number-of-minima theorem bounds the periods. The quantitative constants in (3) are counts and do not locate the exceptional sources. [Simons and de Weger, Theorem 3](https://doi.org/10.4064/aa117-1-3)

Weaver gives rank and coset restrictions for positive-density selections in *odd-step time* and compares them to Yang’s earlier bounds. PR192 already proves the one-sided bound on total shortcut length across a fixed number of monochromatic runs and superlogarithmic growth of the number of runs on long ordinary cycles. Applying that bound to a segment cut at $y$, then using $2^{A_-}y\ge3^{P_-}x$, already charges $P_-\log3+A_+\log2$ to $\log y+o(\log x)$ as $x\to\infty$. The two-place clock charge by itself does not give (3), which is independent of starting heights, jump lengths and the actual prime pools. [Yang](https://doi.org/10.5281/zenodo.22554650) · [Weaver, results 1–3](https://rstation.ai/problems/collatz/papers/138/v1) · [PR192, fixed-window theorem (2)](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/CYCLE_EXTENSION.md)

**First unsupported implication.** Neither positivity nor the complete divisor identity gives an upper bound on the ranks of a positive proportion of local minima. At a single mountain the integer carry only gives the common divisibility in (2). Primes dividing the endpoint may be entirely new. For instance $7\mapsto13\mapsto5\mapsto1$ in mountain time begins with independent pairs. The inverse minimizing inequalities for synchronous classes concern sizes and cumulative valuations and supply no bound on these same groups. Proving that every escaping orbit has positive upper mountain density in a finite union of finite-rank cosets would contradict (5). For cycles, even a uniform rank bound would initially leave finitely many possibilities and require another effective or structural exclusion. The rank-one case above is the class for which that exclusion is completed.

The [Lean file](MountainReturns.lean) checks the unbounded-list carry expansion and the signed least-valuation argument for arbitrary selected terms. It also checks the ternary square bound, common-carry divisibility, the exact integer rounding step (6), and primitive-target deduction from its clock and size hypotheses. The identification of the common integer base and its odd-power valuation are written steps. The applications of Mahler, Evertse, and the unit-equation theorem, the real dominance estimate, and the one-circuit theorem are written mathematics. The [replay](check.py) tests the actual shortcut dynamics and arithmetic on finite ranges. Lean 4.34.1 compiled all six printed declarations, using only standard axioms. Both ordinary and optimized Python runs checked 5,000 exact windows, including 4,571 high-entry tuples and 294 high-entry tuples with low endpoints, and 5,215 integer power starts.

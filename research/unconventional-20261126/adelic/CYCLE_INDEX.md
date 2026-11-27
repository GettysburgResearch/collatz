# The determinant, the periodic-point zeta function, and the cost of a rational denominator

**Status.** Proposed mathematics with proofs. The finite controls are separate. The positive integer cycle conjecture remains open. The quantities below count exact fixed points of the indicated iterate, so a cycle of least period dividing the clock contributes all of its vertices. The last section distinguishes exact-period counts.

Let $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$. Extend parity to rationals of odd reduced denominator. Write $d(x)$ for that denominator and $m(x)$ for the least real value on the cycle of a positive periodic point. For a set $S$ of primes let $\mathcal R_S$ consist of the positive rationals integral at 2 and at every prime of $S$. Put $\beta=\log 2/\log 3$, $H(u)=-u\log_2 u-(1-u)\log_2(1-u)$, and $\theta=H(\beta)=0.949955\ldots$. The exponential rates use $\log_2 0=-\infty$.

## 1. What the ordinary trace detects

Each length-$n$ binary word $w$ of weight $p$ composes to
\[
 F_w(x)=\frac{3^p x+A(w)}{2^n},\qquad
 A(w)=\sum_{j:w_j=1}2^j3^{\sum_{k>j}w_k}.
\]
Its unique rational fixed point is $A(w)/D$, where $D=2^n-3^p\ne0$. The zero word gives zero. For $p>0$, positivity is exactly $D>0$. This fixed point actually has the specified native word. The numerator of each cyclic rotation is integral, and twice the next numerator equals $3^{w_j}$ times the current numerator plus $w_jD$. Since $D$ is odd, the current numerator has parity $w_j$. Also $\gcd(D,6)=1$ when $p>0$, so all rotations have the same reduced denominator dividing $D$. A length-$L$ native word determines one source class in $\mathbb Z_2/2^L$: iterating the displayed affine identity gives $3^p x+A(w)\equiv0\pmod{2^L}$, with $3^p$ invertible. These are classical facts. [Lagarias, Acta Arith. 56 (1990), Theorem 2.1](https://doi.org/10.4064/aa-56-1-33-53)

For any positive rational cycle fixed by $T^n$, taking the product of the $n$ individual height ratios gives
\[
 0<\delta=n\log2-p\log3
 =\sum_{j:w_j=1}\log(1+1/(3x_j))\le n/(3m(x)).
 \tag{1}
\]
The classical two-logarithm bound $|n\log2-p\log3|\ge c n^{-A}$ holds for absolute effectively computable $c,A>0$ and $n\ge2$. Thus every such cycle has $m(x)\le C n^{A+1}$, uniformly in its denominator. At each fixed denominator $d$, distinct cycles have distinct minimum numerators bounded by $Cdn^{A+1}$, and each contributes at most $n$ marked points. In particular the **ordinary integer fixed-point count** satisfies $F_n\le C n^{A+2}$. [Lagarias, proof of Theorem 3.2](https://matwbn.icm.edu.pl/ksiazki/aa/aa56/aa5614.pdf)

The ordinary Artin–Mazur zeta function
\[
 Z_{\mathbb N}(z)=\exp\left(\sum_{n\ge1}F_n z^n/n\right)
 =\prod_{\text{positive integer cycles }C}(1-z^{|C|})^{-1}
 \tag{2}
\]
has radius exactly one. The polynomial bound gives convergence on the open unit disk and the known cycle supplies a singularity at 1 by positivity. The formal Euler product has nonnegative integer coefficients. If there are finitely many cycles it is rational and has pole order at 1 equal to their number. If there are infinitely many cycles, the product over any $k$ chosen cycles grows on the positive radius as a positive constant times $(1-z)^{-k}$. The full function therefore exceeds every fixed pole order and is not rational. The Pólya–Carlson theorem now makes the **whole unit circle a natural boundary**. In particular analytic continuation through any arc would prove finiteness. It would leave the order of the pole, and hence uniqueness, to be determined. [F. Carlson, Math. Z. 9 (1921), 1–13](https://doi.org/10.1007/BF01378331)

For comparison, the finite ordinary graph on $[1,N]$ with outgoing edges killed at exit has weighted determinant
\[
 \det(I-zP_N)=\prod_{C\subset[1,N]}
       (1-z^{|C|}3^{p(C)}/2^{|C|}),
 \qquad (P_N)_{x,T(x)}=3^{x\bmod2}/2.
 \tag{3}
\]
Order the recurrent cycles first and order the remaining vertices by their time to a cycle or exit. The transient block is triangular with zero diagonal and each weighted cyclic-permutation block gives its displayed factor. At $z=1$ the full numerator $2^{|C|}-3^{p(C)}$ survives on each cycle. Replacing the weights by 1 gives the reciprocal Euler product on this finite graph. The unweighted determinantal reformulation has long-standing prior art. An anchored trace at vertex 1 counts returns to its own cycle only. Neither (2) nor (3) imports compactness or a trace identity from a different operator. [Alves, Graça, Sousa Dias and Ramos, Linear Algebra Appl. (2005)](https://doi.org/10.1016/j.laa.2004.07.008)

## 2. An arithmetic bound at each reduced denominator

Set $\mathcal F_n(S,R)=\{x\in\mathcal R_S:T^n x=x,\ m(x)\ge R\}$ and
\[
 B_n(S,R,s)=\sum_{x\in\mathcal F_n(S,R)}d(x)^{-s},\qquad s\ge0 .
\]
The weight appears once per marked fixed point, including when the least period divides $n$. For $R=0$ the real minimum is unrestricted.

**Fixed-denominator bound.** For $R\ge1$ put $\beta_R=\log 2/\log(3+1/R)$ and $h_R=H(\beta_R)$. Then
\[
 \#\{x\in\mathcal F_n(S,R):d(x)=d\}
 \le C' n^{A+2} d^{h_R}.
 \tag{4}
\]
For $R=0$ use the same estimate with exponent one. The bound holds for every $S$ and, in particular, without any local restrictions other than native parity.

To prove (4), anchor each cycle at its least real vertex $a/d$. Choose $L=\lceil\log_2(Cdn^{A+1}+1)\rceil$, enlarging $C$ if necessary. Distinct admissible minimum numerators $a$ give distinct length-$L$ words since $a$ lies in an interval of length less than $2^L$ and $d$ is odd. The endpoint is at least the start, including when $L>n$ and the orbit wraps around. Every vertex is at least $R$. If $j$ of these $L$ steps are odd, their multiplicative height ratios are at most $(3+1/R)/2$, and the even ratio is $1/2$. Hence $j\ge\beta_R L$. The number of binary words in that tail is at most $2^{h_R L}$ by the elementary binomial entropy inequality, valid also when $\beta_R=1/2$. Multiply by at most $n$ marked vertices per cycle and apply $0<h_R\le1$. This proves (4).

All relevant denominators divide one of at most $n$ positive $D=2^n-3^p<2^n$. The number of their distinct divisors is $2^{o(n)}$ uniformly. For an elementary proof of the last estimate, fix $e>0$. For primes $q\ge 2^{1/e}$ and $a\ge1$ one has $a+1\le2^a\le q^{ea}$. For the finitely many smaller primes, each $\sup_{a\ge0}(a+1)/q^{ea}$ is finite. Thus $\tau(D)\ll_e D^e$. Equation (4) yields
\[
 \limsup_{n\to\infty}\frac{\log_2 B_n(S,R,s)}n
 \le (h_R-s)_+,\qquad t_+=\max(t,0).
 \tag{5}
\]
For the unrestricted case use 1 in place of $h_R$.

**Unrestricted pressure.** For any fixed finite $S$,
\[
 \limsup_n n^{-1}\log_2 B_n(S,0,s)=(1-s)_+ .
 \tag{6}
\]
Take $M$ divisible by $\ell-1$ for every $\ell\in S$, $\ell>3$, and $n=2Mk$, $p=Mk+1$. For large $k$, $0<3^p<2^n$ and the full determinant is $-2$ modulo each tested prime $>3$. Every word of this weight gives a positive fixed point in $\mathcal R_S$ and $d<2^n$. There are $2^{n-o(n)}$ such words by Stirling. This gives the lower exponent $1-s$ and the known integer cycle gives the lower exponent zero along even $n$. The matching upper bound is (5) with unrestricted real minimum.

In particular the ordinary, unweighted zetas $Z_{\mathcal R_S}$ all have radius $1/2$ for fixed finite $S$. Indeed their log series have that radius by (6), the exponential converges inside it, and $Z_{\mathcal R_S}$ coefficientwise dominates its log series since the latter has nonnegative coefficients. As $S$ exhausts the primes, these zetas converge coefficientwise to $Z_{\mathbb N}$. For each fixed $n$ only finitely many individual rational fixed points occur and each noninteger has a prime in its denominator. Equation (2) and (6) show that the convergence radii jump from $1/2$ to one at this intersection.

## 3. The sharp high-minimum rate

For every finite prime set $S$ and every $s\ge0$,
\[
 \boxed{\displaystyle
 \lim_{R\to\infty}\limsup_{n\to\infty}
    n^{-1}\log_2 B_n(S,R,s)=(\theta-s)_+.}
 \tag{7}
\]
The same identity holds for all $s\ge0$ with the growing prime sets $S_n= S\cup\{\ell:\ell\text{ prime},\ \ell\le n^a\}$ whenever $0<a<1/4$. The proof of the zero lower rate in this case uses a growing sequence of rational cycles and carefully chosen multiples of their least periods.

The lower-bound construction is stronger than required by (7). Given $a<1/4$ positive, a fixed finite $S$, and $0<e<1$, infinitely many coprime clocks and grades $(n,p)$ give at least $2^{(\theta-e)n}$ distinct **least-period-$n$ marked positive rational points** with all the following properties for sufficiently large clocks in the constructed subsequence.

* Every reduced denominator is prime to every prime of $S_n$ and exceeds $2^{(1-e)n}$.
* The full determinant is $D=2^n-3^p>0$ with $D/2^n=1-\exp(-\delta)\to0$.
* All phases have real size comparable to $n/\delta$ with constants independent of $n$. In particular the minimum is $\gg n^2$.
* Every pair of distinct phases in any one of these cycles differs in the real absolute value by $\gg n^c$ for an absolute $c>0$. The implicit constant may depend on $e$.

Here $e$ is a tolerance in the two base-two exponents.

### 3.1. Clocks, real height, and real spacing

Take the infinitely many continued-fraction convergents $p/n$ to $\beta$ from below. For them $0<\delta=(n\beta-p)\log3<\log3/n$, $\gcd(n,p)=1$, and $|j\beta-k|\ge n\beta-p$ for $0<j<n$, $k\in\mathbb Z$, by the best-approximation property of convergents. Finite initial exceptions may be discarded. No special distribution of these convergents in residue classes is used.

Fix a large integer block width $K$. Cut $[0,n)$ into complete $K$-blocks and one possible shorter final block. At each boundary $t$ prescribe cumulative grade $\lfloor tp/n\rfloor$ including the terminal grade $p$. Permute letters freely within each block subject to its grade. The prescribed cumulative discrepancy is less than one at boundaries and at most $K+1$ everywhere. On each cyclic arc of length $j\le n$ and weight $q$, this gives $|q-jp/n|\le 2K+2$. Thus its multiplier $3^q/2^j$ lies between two fixed positive constants. Its affine offset in the normalized map is
\[
 b=\tfrac12\sum_{i\text{ odd step on arc}} (\text{multiplier of the arc strictly after }i).
\]
Consequently $b\le C_K j$ always and $b\ge c_K j$ for all $j\ge J_K$, since every such arc has $\gg j$ odd steps. Applying this at one complete period from any phase shows $x=b/(1-e^{-\delta})\asymp_K n/\delta$.

For two distinct phases, the log defects of the two complementary arcs sum to $\delta$. Each is nonzero by unique factorization and each has absolute value at least $\delta$ by best approximation. Hence at least one arc has multiplier greater than one. Along that arc the height increase is at least its nonnegative affine offset. If the smaller cyclic time separation is $t\ge J_K$, this already gives an absolute height separation $\ge c_Kt$. On the shorter arc of length $t$, the two-log bound and the bounded multiplier give $|r-1|\ge c_K t^{-A}$ after enlarging $A\ge1$, and $b\le C_Kt$. Its endpoint difference in absolute value is at least $c'_K n^2t^{-A}-C_Kt$. For $t\le c''_K n^{2/(A+1)}$ this is $\gg_K n^{2/(A+1)}$ with small enough $c''_K$. For larger $t$ use the expanding arc. This proves the real spacing claim.

For any $\varepsilon>0$, $K$ can be chosen so that both values $q\in\{\lfloor Kp/n\rfloor,\lceil Kp/n\rceil\}$ have $K^{-1}\log_2\binom Kq\ge\theta-\varepsilon$ for all large $n$. This follows by Stirling and continuity, since $p/n\to\beta$. All these complete block grades satisfy $1\le q\le K-1$. The possible leftover block can be fixed arbitrarily. Coprime $n,p$ force every word to have least period $n$.

### 3.2. Cancelling the prime powers actually present in the determinant

Let $Y\mid D$ with $\log(2Y)=o(\sqrt n)$. A patch of $O_K((\log(2Y))^2)$ complete blocks suffices to force $Y\mid A(w)$ for every fixed choice of the other blocks, preserving all prescribed grades. The case $Y=1$ needs no patch.

In each patch block place the pair $01$ or $10$ first and the same fixed suffix of grade $q_j-1$ afterwards. A swap changes $A(w)$ by a signed monomial
\[
 t_j=2^{jK}3^{p-P_j-1},
\]
where $P_j$ is the prescribed count before block $j$. Taking consecutive blocks starting at $j=0$, these are units modulo $Y$ and $3^{q_j} t_{j+1}=2^K t_j$. The contributions to $A(w)$ from different swaps add, because each complete block has fixed grade.

To prove all residues occur, toss independent fair choices within the patch for this counting argument. At a nonzero additive character $u\bmod Y$ the magnitude of its Fourier coefficient is $\prod_j|\cos(\pi u t_j/Y)|$. Let $y_j$ be the centered integral representative of $ut_j$ modulo $Y$. It does not vanish. Set $\eta_K=1/(2(3^K+2^K))$. If $h+1$ consecutive representatives have absolute value $<\eta_KY$, then for $h$ consecutive transitions the integer $3^{q_j}y_{j+1}-2^K y_j$ is divisible by $Y$ and has size $<Y$. It vanishes. Iteration and coprimality force $3^{q_j+\cdots+q_{j+h-1}}\mid y_j$, which is impossible for $h>\log_3Y$. Thus each block of $2+\lceil\log_3Y\rceil$ consecutive indices contains a factor at most $\rho_K=\cos(\pi\eta_K)<1$. For a sufficiently large $K$-dependent constant times $(\log(2Y))^2$ choices, the product is $<1/(2Y)$ uniformly at nonzero characters. Fourier inversion gives probability $>1/(2Y)$ for every residue, in particular the one needed to cancel the outside contribution.

Take $Y$ equal to the full $S_n$-part of $D$. The 2- and 3-parts are trivial. For $\ell\ge5$, Kunrui Yu's bound of §0.1 at degree one, with the fixed rational bases 2 and 3 and exponents $n,-p$, gives
\[
 v_\ell(2^n-3^p)\ll \ell(1+\log\ell)^C\log(2n)
\]
with absolute constants. In Yu's displayed formula $f_\ell=1$, the two heights can be chosen $O(1+\log\ell)$, and $B\le\max(n,3)$. The two bases are multiplicatively independent. Therefore $\log(2Y)\ll_{S} n^{2a}(\log(2n))^{C+2}$ by summing even over all integers up to $n^a$. For $a<1/4$ the patch occupies $o(n)$ bits at fixed $K$. This proves integrality at all requested primes while leaving at least $2^{(\theta-2\varepsilon)n}$ marked points. The assertion concerns the prime powers in the **actual integer determinant**. [Kunrui Yu, *Linear forms in p-adic logarithms III*, Compos. Math. 91 (1994), 241–276, §0.1](https://www.numdam.org/article/CM_1994__91_3_241_0.pdf)

To remove small reduced denominators, all constructed cycles have minimum at least $c_Kn^2$. Apply (4) with this threshold, for which $h_R\to\theta$. Summing over the $2^{o(n)}$ candidate divisors $d\le2^{(1-e)n}$ bounds the discarded count by $2^{((1-e)\theta+o(1))n}$. Choose $2\varepsilon<\min(e,\theta e)/2$. At least $2^{(\theta-e)n}$ survive for all large clocks. The positive rational vertices are genuinely nonintegral and sufficiently separated to satisfy the elementary spacing condition on distinct ordinary integer vertices.

Finally these points give lower exponent $\theta-s$ for the marked trace, since $d\le2^n$. For fixed finite $S$ and any fixed $R$, one can also take just one of the constructed cycles above $R$ and count its positive contribution at every multiple of its period. This gives lower exponent zero for the marked trace. For a growing sieve choose $a<b<1/4$ and construct the cycles with the stronger cutoff $n_0^b$ at their least periods $n_0$. Put $L=\lfloor n_0^{(b/a-1)/2}\rfloor$ and count each cycle at $n=Ln_0$. Then $n^a\le n_0^b$, $L\to\infty$, and its weight $d^{-s}\ge2^{-sn_0}$ gives lower rate at least $-s/L\to0$. The minimum still exceeds $R$. Since $h_R\to\theta$ as $R\to\infty$, (5) proves (7) also for the growing sieve.

## 4. The remaining pointwise obstruction

Every ordinary cycle corresponds to the exact divisibility $D\mid A(w)$. The Fourier patch above solves congruences with $\log(2Y)=o(\sqrt n)$, whereas the real two-log bound yields $\log_2 D=n-O(\log n)$ on positive words. Its mixing length applied to $Y=D$ is quadratic in the available clock. Independently of the mixing estimate, an almost-critical fixed-grade family with $2^{(\theta+o(1))n}$ words cannot hit every residue modulo such a $D$ because $\theta<1$. The residue zero still requires a pointwise argument.

The ordinary bound (4) at $d=1$ remains polynomial. Finitely many additional primitive cycles change (2) by finitely many Euler factors and leave the convergence radius one. For any proposed finite list of extra periods, the abstract product of their factors has nonnegative integer coefficients, satisfies the periodic trace divisibility rules and passes every exponential estimate here. Such a formal test makes no assertion that those cycles exist in the ordinary graph. Proving meromorphic continuation at one would settle finiteness, and proving pole order one would settle positive cycle uniqueness. No such continuation or pole-order bound is obtained by the present arithmetic estimates.

When only least-period-$n$ points are counted, the construction gives lower growth $\theta-s$ even with the growing sieve, and (5) gives the upper growth $(\theta-s)_+$ after sending the minimum to infinity. These agree for $0\le s\le\theta$. For $s>\theta$ the repeated-cycle lower bound is unavailable. The integral row $d=1$ is particularly sensitive to a single cycle: its exact-period trace at that one period changes by the entire cycle length, while any finite change leaves the limiting exponential rate unchanged.

Lagarias's 1990 paper already studies the distribution of rational Collatz cycles among their reduced denominators, proves large fibers at central grade and treats maximal numerator congruence concentration. Its §3.5 explicitly cautions against independence of the numerator congruences of rotations. Here the additional conclusions are the weighted rates (6)–(7), the high-minimum per-denominator bound (4) and the joint nearcritical, separated, growing-prime controls. The finite graph determinant and the native rational-word correspondence are background, as are the two independent linear-forms estimates. [Lagarias, §§3.3–4](https://matwbn.icm.edu.pl/ksiazki/aa/aa56/aa5614.pdf)

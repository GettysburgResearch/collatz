# A Subspace Theorem estimate for the even-step clock

**PROPOSED, written proof conditional only on the classical Subspace Theorem as cited below.** The source $n$ in the first result varies over ordinary positive integers. The number of terms is fixed. In the last result the source is fixed and the number of terms tends to infinity.

## 1. Uniformity in arbitrary exponents at fixed arity

Fix rational coefficients $c_1,\ldots,c_m$ and $\epsilon>0$. For all sufficiently large positive integers $n$ and every set of nonnegative integers $u_1,\ldots,u_m$,

$$
 v_2\left(n+\sum_{i=1}^m c_i(2/3)^{u_i}\right)
 \le (1+\epsilon)\log_2 n .
$$

The onset may depend on the coefficients and on $\epsilon$. Its effectiveness is not asserted. The lower range must be excluded for general signed coefficients. For example $1-1+(2/3)^u$ has valuation $u$.

**Proof.** Induct on the number of nonzero coefficients, allowing arbitrary fixed rational replacements at smaller arity. The case of no terms follows from $2^{v_2(n)}\le n$. Suppose infinitely many distinct $n$ violate the assertion. Set $h=\lfloor(1+\epsilon)\log_2 n\rfloor+1$. Terms with $u_i+v_2(c_i)\ge h$ are invisible modulo $2^h$. Remove them, and pass to a subsequence with the same retained indices. If every term is removed then $v_2(n)\ge h$ is impossible. Let $U$ be the maximum retained exponent. It satisfies $U\le h+O_c(1)$. Set

$$
 X_0=3^U n,\qquad X_i=2^{u_i}3^{U-u_i}
$$

for the retained indices. Use the coordinate forms at $\infty$ and $3$. At 2 use $X_0+\sum_i c_iX_i$ and the nonroot coordinates $X_i$. All systems are independent, with determinant of absolute value 1. The product of all evaluations, over these three places and all forms there, is at most $n2^{-h}$. Indeed each $X_i$, $i>0$, is a $\{2,3\}$-unit. The root's archimedean and 3-adic factors multiply to at most $n$, and the 2-adic sum has norm at most $2^{-h}$.

Dividing all coordinates by their integer gcd preserves this local product, because the gcd divides a nonroot $\{2,3\}$-unit. The primitive height $H$ satisfies $H\le 3^U n\ll_c n^{1+(1+\epsilon)\log_2 3}$. Also $H\to\infty$, since some $X_i/X_0=(2/3)^{u_i}/n$ is positive and at most $1/n$. Consequently the product is at most $H^{-\delta}$ on a final subsequence for a fixed $\delta>0$ depending only on $\epsilon$. The rational nonarchimedean Subspace Theorem places those primitive vectors in finitely many proper rational subspaces. Pass to one relation

$$
 \lambda_0 n+\sum_i\lambda_i(2/3)^{u_i}=0.
$$

If $\lambda_0\ne0$, its right-hand sum is bounded in the real absolute value, forcing bounded $n$. Otherwise solve for a nonroot with nonzero coefficient and eliminate it from the approximation. This leaves an expression of smaller arity with fixed rational coefficients and the same value (after the earlier removal, the same congruence modulo $2^h$). The inductive theorem now rules out infinitely many such $n$. This proves the estimate.

The Subspace Theorem supplies finitely many exceptional subspaces **at each fixed dimension**. The cited quantitative theorem bounds their number but does not give the single linear-in-arity estimate in [the global criterion](PIN_APPROXIMATION.md). [Evertse and Ferretti, Annals of Mathematics (2013), Theorem 3.1 and its rational specialization](https://doi.org/10.4007/annals.2013.177.2.4).

## 2. Each fixed number of even inputs costs at most one bit length

Retain $D_e$ from the pin representation. For each fixed $r\ge0$ and $\epsilon>0$, there exists $C_{r,\epsilon}$ such that every ordinary $n\ge1$ satisfies

$$
 D_r(n)\le (1+\epsilon)\log_2(n+1)+C_{r,\epsilon}.
$$

Apply Section 1 with $n+1$ as root and coefficients $2^j$, $0\le j<r$. For finitely many small roots the maxima exist by the greedy construction. The leading coefficient 1 is sharp even for $r=0$, by taking $n=2^k-1$.

In particular, if $g_0,g_1$ are the first two successive runs of odd steps, with one even step between them and a subsequent even step at time $g_0+1+g_1$, then

$$
 g_0+g_1+1\le(1+\epsilon)\log_2(n+1)+C_{1,\epsilon}.
$$

This excludes repeated spending of the full initial bit length on successive odd runs.

## 3. A genuine constraint as the number of terms tends to infinity

For every fixed positive integer $n$,

$$
 \lim_{e\to\infty}\frac{\log(1+D_e(n))}{e}=0 .
$$

To see this, take any fixed integer $r\ge1$ and split the actual path into consecutive blocks, each ending just after its $r$-th even input. If a block starts at $x$, its length is $D_{r-1}(x)+1$. Every odd step multiplies the shifted state $x+1$ by $3/2$, while an even step does not increase the shifted state. Write $m=\log_2(x+1)$ and fix, for example, $\epsilon=1$. By Section 2 the next block starts at $x'$ with

$$
 \log_2(x'+1)\le \Theta m+O_r(1),
 \qquad \Theta=1+2\log_2(3/2)>1 .
$$

After $q$ blocks the logarithm of the shifted state is at most $O_{r,n}(\Theta^q)$. The sum of the first $q$ block lengths has the same bound, by a geometric series. Since $D_e$ is increasing, this implies $\limsup_e \log(1+D_e(n))/e\le\log\Theta/r$. Take $r$ arbitrarily large. The limit inferior is nonnegative.

Thus each fixed ordinary source has subexponential maximal approximation depth as the arity grows. The required slope bound $D_e\le 2.36 e+O_n(1)$ is much stronger. The proof cannot take $r$ proportional to $e$ since the onset and the projected coefficient families depend on $r$.

**Relation to prior work.** This argument gives a direct fixed-arity application of the classical theorem to the positive rational sums singled out by the exact maximum. A 2026 public manuscript develops the stronger effective lower order $\log t\log\log t$ for the number of odd-map exponents at least two, as well as a sharp fixed-budget excursion bound for general periodic dictionaries. Each such odd-map exponent accounts for at least one even shortcut input. That manuscript's scope and the different clock are recorded in [the primary-source map](PRIMARY_SOURCES.md). No priority claim is made for subexponential growth.

## 4. Separation of macroscopic odd runs

For a positive nonperiodic orbit, let $x_0=n$ and let $x_{i+1}$ be the state immediately after the next even input starting from $x_i$. Write $g_i=v_2(x_i+1)$ for the number of odd inputs before that even one, and $B_i=\log_2(x_i+1)$. A nonperiodic positive orbit visits each integer at most once, so $B_i\to\infty$. With $c=\log_2(3/2)$, the exact update is

$$
 x_{i+1}+1=\frac{(3/2)^{g_i}(x_i+1)+1}{2},
 \quad B_{i+1}=B_i+c g_i-1+o(1).
$$

Fix $r\ge1$. Section 2 at the varying source $x_i$ gives $\sum_{j=i}^{i+r-1} g_j \le (1+\epsilon)B_i+O_{r,\epsilon}(1)$ for all $i$. After letting $i$ increase and then $\epsilon$ decrease, telescoping the updates gives $\limsup_i B_{i+r}/B_i\le 1+c$.

**Proposition.** For every $\delta>0$ and fixed $r$, every sufficiently late window of $r$ such runs contains at most

$$
 \left\lfloor\frac{\log(1+c)}{\log(1+c\delta)}\right\rfloor
$$

indices $j$ with $g_j\ge\delta B_j$. Indeed the product of the $r$ consecutive ratios $B_{j+1}/B_j$ is $B_{i+r}/B_i$. A marked ratio is at least $1+c\delta-o(1)$; every other ratio is at least $1-o(1)$. If $m$ marks recur in infinitely many such windows, this proves $(1+c\delta)^m\le 1+c$.

At $\delta=1/2$ the cap is one, since $(1+c/2)^2=1+c+c^2/4>1+c$. Consequently the number of even inputs between successive half-bit-length odd runs tends to infinity if infinitely many such runs occur. The assertion is uniform in the cap but its onset may depend on the fixed window length. A nonperiodic counterexample might have many much shorter runs and would still satisfy the separation theorem.

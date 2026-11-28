# Positive-sided saturation at 95 rational centers of the standard parity permutation

Let $M_k=2^{5k}$, $N_k=2^k$, and let $Q_m$ count odd departures of the usual shortcut map. Put $H=\langle2\rangle\subset(\mathbb Z/191\mathbb Z)^\times$. This subgroup has 95 elements and contains 3. We prove that for **each** $j\in\{1,\ldots,190\}$ with $-j\bmod191\in H$,
\[
 \#\left\{r\in\mathbb Z:\ \frac{j M_k}{191}<r\le
 \frac{j M_k+N_k}{191},\quad Q_{5k}(r)\ge 0.501(5k)\right\}
       =N_k/191-o(N_k).                                           \tag{1}
\]
Thus the right-hand direction, positive ordinary integer inputs, exponential window scale, clock, threshold and the standard parity permutation can all be retained while changing the asymptotic behavior sought at the origin. This is a method obstruction. It gives no estimate at $j=0$.

## Arithmetic control on a positive parameter

Write $b=191$ and $T_b(x)=x/2$ for $x$ even, $(3x+b)/2$ for $x$ odd. For each $n\bmod191\in H$, the entire positive orbit remains in $H$ since both branches multiply by $2^{-1}$ and the odd branch also multiplies by 3 modulo 191. Finite checks used here are
\[
 |H|=95,\quad 3\in H,\qquad T_b^{40}(961)=961,\qquad Q^{(b)}_{40}(961)=25 ,
\]
and every $n\le B=80b$ in $H$ reaches this cycle. The 7,600 actual eligible inputs reach the cycle within 252 steps. [check_rational_arcs.py](check_rational_arcs.py) verifies these finite facts by integer computation.

Let $N=2^k$, $m=5k$ and let $\tau$ be the first visit to $[1,B]$, infinite if necessary. If $\tau>m$, then
\[
 1\le T_b^m(n)\le 2^{-4k}(3+1/80)^{Q_m^{(b)}(n)} .
\]
The resulting lower bound is $Q_m^{(b)}(n)\ge [4/\log_2(3+1/80)]k>2.514k$.

When $\tau\le m$, all departures before $\tau$ are distinct, since a repetition would prevent the first visit. Along this prefix the correction in the multiplicative formula obeys
\[
 \sum_{\substack{0\le i<\tau\\ T_b^i(n)\ {\rm odd}}}
 \log(1+b/(3T_b^i(n)))\le (b/3)(1+\log(m+1)).
\]
Indeed at most $m$ distinct positive integers occur. With $q=Q_\tau^{(b)}(n)$ and $T_b^\tau(n)\ge1$ this gives $\tau\le k+q\log_2 3+O_b(\log(k+1))$. After $\tau$, the finite certificate supplies $Q_{m-\tau}^{(b)}(T_b^\tau n)\ge (5/8)(m-\tau)-O_b(1)$, uniformly in phase. Hence
\[
 Q_m^{(b)}(n)\ge 2.5k+
        [1-(5/8)\log_2 3]q-O_b(\log(k+1)).                       \tag{2}
\]
Once $q\ge0.54k$, the linear coefficient is $2.505075156\ldots>2.505$. The strict margin absorbs the error as $k\to\infty$. The two threshold comparisons with $2.505$ have exact certificates $241^{501}<80^{501}2^{800}$ and $3^{135}<2^{214}$.

## Few inputs reach the finite set with fewer than $0.54k$ odd departures

First we need a crude universal multiplicity estimate. From a positive terminal state $y$ there is always the inverse $2y$. An odd inverse can occur only when $2y\equiv b\bmod3$. At such a branching node the even child $2y\equiv b\bmod3$ cannot itself branch since $3\nmid b$. Suppressing this forced edge bounds the largest multiplicity at depth $d$ by the Fibonacci number $F_{d+2}$, with $F_0=0,F_1=1$. Formally the branching bound is $L_{d+1}\le L_d+L_{d-1}$ for the largest inverse multiplicity $L_d$, where the nonbranching case contributes only $L_d$. The initial bounds are $L_0\le1,L_1\le2$. In particular $L_k=O(\varphi^k)$ with $\log_2\varphi<0.7$.

The first $k$ parities on $1\le n\le2^k$ contain each word once, also for every odd $b$: appending one source bit toggles the next parity because the affine coefficient numerator is odd. Thus with $o(2^k)$ exceptions,
\[
 .499k\le Q_k^{(b)}(n)\le .501k .
\]
We can delete the same exceptional set before restricting $n$ to the fixed positive-density coset. If $\tau<k$, then $T_b^k(n)$ lies in the finite union of the forward orbits of the eligible states through $B$. This case has $O_b(\varphi^k)=o(2^k)$ sources.

It remains to consider $k\le\tau\le5k$, $q<.54k$ and a typical first count. Write $y=T_b^k(n)$ and $e=q-Q_k^{(b)}(n)<.0411k$. For a word of length $k$ and weight $r$, its real affine intercept is at most $b((3/2)^r-1)$ by moving all odd steps to the end. Consequently
\[
 y\le (1+b)3^{.501k}.
\]
All departures from $y$ prior to the first hit are above $B$, so the suffix length $s=\tau-k$ satisfies
\[
  s\le\log_2 y+e\log_2(3+1/80)<.9k
\]
for sufficiently large $k$. Each terminal value through $B$ and each suffix word determine at most one $y$. There are therefore at most $2^{.27k+o(k)}$ possible $y$. Indeed, enlarge $\lfloor e\rfloor$ to $\lceil.045k\rceil$ and $s$ to $\lceil.9k\rceil$. Counting words of all such lengths and weights costs a polynomial times $\binom{\lceil.9k\rceil}{\lceil.045k\rceil}$, whose base-two logarithm is at most $(.045\log_2(20\,\mathrm e)+o(1))k<.27k$. Each $y$ has $O(\varphi^k)$ physical sources. Their total is $o(2^k)$.

Combining these estimates with (2), all except $o(2^k)$ sources in $H$ satisfy $Q_{5k}^{(191)}(n)\ge .501(5k)$. The argument does not require a positive-density theorem or a clock limit law for $3x+191$.

## Transfer back to the standard polynomial

For an odd parameter $b$, multiplication by $b$ conjugates the standard shortcut and $T_b$ on the binary integers; indeed $T_b(bx)=bT_1(x)$ on either parity branch. Finite parity words depend only on the source modulo $2^m$. Therefore
\[
 Q_m^{(191)}(n)=Q_m(r),\qquad r=191^{-1}n\bmod M_k .
\]
Write $r=(jM_k+n)/191$ with $0\le j<191$. Then $j\equiv-n M_k^{-1}\bmod191$. Since $2\in H$, a fixed $j\in-H$ corresponds to one eligible source class $n\bmod191$. The eligible $r$ in its right-hand interval of (1) are consecutive. Deleting $o(N_k)$ exceptions from the union deletes $o(N_k)$ from each class, and each class contains $N_k/191+O(1)$ integers. This proves (1).

For the Fourier polynomial in [README.md](README.md), changing the positive offset from 1 to 191 permutes the frequencies $h\mapsto191h\bmod 2^{5k}$, because the binary representative attached to a fixed word is multiplied by 191. Consequently neither the permutation-invariant Fourier data nor a bound uniform over positive one-sided rational centers can give the desired small upper tail at the **integer** origin. The denominator-one phase pairing remains open.

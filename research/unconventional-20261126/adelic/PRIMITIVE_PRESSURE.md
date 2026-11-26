# Primitive rational cycles with subexponential reduced denominator

**Status.** Proposed mathematics with a complete constructive proof. The source map is the shortcut Collatz map on positive rationals of odd denominator. The paper [CYCLE_INDEX.md](CYCLE_INDEX.md) fixes the normalization. The construction below counts native cycles at their actual least periods. The positive integer cycle question is open.

Write $d(x)$ for the reduced denominator and $m(x)$ for the least real value around a cycle. Let $B_n^*(S_n,R,s)$ denote the sum of $d(x)^{-s}$ over marked points of **least** period $n$, with $m(x)\ge R$ and $d(x)$ prime to all primes in $S_n$. Put $\theta=H_2(\log_3 2)$. Empty sums have logarithm $-\infty$.

**Theorem 1.** Given any finite prime set $S$, any $0<a<1/2$ and $s\ge0$, put $S_n=S\cup\{\ell\text{ prime}:\ell\le n^a\}$. Then
\[
 \lim_{R\to\infty}\limsup_{n\to\infty}\frac{\log_2 B_n^*(S_n,R,s)}{n}
      =(\theta-s)_+.
 \tag{1}
\]
The argument for the lower value zero exhibits nonintegral cycles whose least periods tend to infinity. Their real minima grow without bound, $\log_2d(x)/n\to0$, and every prime of the **exact reduced denominator** exceeds the cutoff. In fact the construction of this lower value works for any fixed cutoff $c\sqrt n$, $c>0$. This last assertion concerns the lower value zero only.

## Two independently periodic swap choices

Let $q/m$ run through the continued-fraction convergents to $\beta=\log_3 2$ from below. Set
\[
 B=2^m,\qquad A=3^q,\qquad D=B-A,\qquad \delta=\log(B/A).
\]
Then $\gcd(m,q)=1$, $0<\delta<\log(3)/m$, and $D$ is positive, odd and prime to $3$. Use the length-$m$ word with digits $\lfloor(j+1)q/m\rfloor-\lfloor jq/m\rfloor$, $0\le j<m$. For large $m$, zeros are isolated even on the cyclic word because $q/m>1/2$. There are $m-q$ of them. In particular there are two disjoint internal pairs $10$. Mark two such pairs. A flag reverses its designated pair to $01$. For any of the four possible blocks, the grade is $q$ and every prefix grade differs from $jq/m$ by at most two. This follows since only a prefix ending between the two letters of one designated pair can change its grade.

The four exact affine maps are
\[
 x\longmapsto (Ax+C_0+c_1e+c_2f)/B,\qquad e,f\in\{0,1\}.
 \tag{2}
\]
Here $C_0$ is the initial block numerator and $c_i=2^{j_i}3^{h_i}>0$, where $j_i$ is the first index of the pair and $h_i$ is the grade strictly after the pair. Indeed $10$ contributes $2^{j_i}3^{h_i}$ where $01$ contributes twice that value. All other terms retain their weights because the pair grade is fixed. Each $c_i$ is a unit modulo any divisor of $B^u-A^u$.

Take distinct primes $r,t>D$ and greater than $3$. We will choose an integer $1\le k<r$. At block time $j$, use the flags
\[
 e_j={\bf1}_{j\bmod r<k},\qquad f_j={\bf1}_{j\bmod t=0}.
\]
The word formed by the first $rt$ blocks has full clock $n=mrt$ and full grade $qrt$. Its unique periodic rational point is positive and has its specified native parity by the affine-word identity in [CYCLE_INDEX.md, §1](CYCLE_INDEX.md). Its least period is exactly $mrt$. Indeed if $n_0\mid n$ is the least period, the native grade fraction of that period is $q/m$, so $m\mid n_0$. At multiples of $m$ the two flags are individually recoverable from the two labelled pairs of digits. Both flag sequences are nonconstant and have prime least periods $r$ and $t$, so $rt\mid n_0/m$.

## The exact denominator

For $h\ge1$ put $D_h=B^h-A^h$ and $Q_h=D_h/D=\sum_{j<h}B^jA^{h-1-j}$. The periodic scalar solution at block boundary zero, obtained by summing the three periodic forcings in (2), is
\[
 x_0=\frac{C_0}{D}+
  \frac{c_1 A^{r-k}Q_k}{D_r}+
  \frac{c_2 A^{t-1}}{D_t}.
 \tag{3}
\]
For the $r$-periodic forcing the contributions in its first period are precisely $c_1\sum_{j=0}^{k-1}B^j A^{r-1-j}$, giving the middle numerator. Each of the three periodic solutions is also $rt$-periodic and their sum solves the recurrence; the $rt$-periodic solution is unique because $(A/B)^{rt}<1$.

The integers $D,Q_r,Q_t$ are pairwise coprime. In fact $Q_r\equiv rA^{r-1}\pmod D$, with both factors units. If $\ell\mid Q_r$, it is prime to $6D$, so the multiplicative order of $B/A$ modulo $\ell$ is exactly $r$. Order $t$ applies to the prime divisors of $Q_t$ in the same way. It follows also that $\gcd(Q_k,Q_r)=1$ because $0<k<r$. Thus the last two terms in (3) have denominator divisible by the full $Q_r$ and $Q_t$, respectively, and neither factor can cancel in their sum. Reducing $D x_0$ modulo $D$ in the localizations where $Q_r Q_t$ are units gives
\[
 D x_0\equiv C_0+c_1 k/r+c_2/t\pmod D.
\]
Choose the unique $k$ in $[1,D]$ solving this congruence with right hand side zero. It exists since $c_1,r,t$ are units and it satisfies $k<r$. If $D=1$ take $k=1$. Consequently the common reduced denominator of every native phase is **exactly**
\[
 d=Q_rQ_t>1,\qquad \frac{\log_2d}{mrt}\le \frac1r+\frac1t .
 \tag{4}
\]
Here $Q_h\le B^h$ since $D\ge1$. Every prime divisor of $Q_r$ is $1$ modulo $r$, and each divisor of $Q_t$ is $1$ modulo $t$. This includes all of their prime powers in (4).

## All real phases and the sieve

Every multiplier of a subword contained in a single block lies between two absolute positive constants, uniformly in $m$ and the flags. Indeed subword grade differs from $jq/m$ by a bounded amount, $0\le j\le m$, and $j\delta/m\le\delta$. In its normalized affine map every odd digit contributes half the multiplier of the remaining suffix. Each complete block therefore has normalized additive offset in $[c m,Cm]$, with $c,C>0$ absolute. At block boundaries the common slope is $A/B=e^{-\delta}$, so iteration backwards around the positive periodic solution gives
\[
  \frac{cm}{1-e^{-\delta}}\le x_j\le\frac{Cm}{1-e^{-\delta}}.
\]
An internal prefix has bounded multiplier and nonnegative offset $O(m)$. All physical phases are thus $\asymp m/\delta\gg m^2$ with absolute constants independent of $r,t,k$.

For $a<1/2$ take $r,t\in[N,4N]$ distinct primes via Bertrand's postulate. With $m$ fixed and $N$ sufficiently large, their minimum exceeds both $(mrt)^a$ and the largest fixed tested prime. In particular the full denominator (4) passes the growing sieve. This part uses no prime-distribution result for varying moduli.

For the optional stronger lower-value control, fix $c>0$, $m$, and an integer $K>c\sqrt{2m}$. There are arbitrarily large distinct primes $r<t\le2r$ both $1$ modulo $\operatorname{lcm}(2,\ldots,K+1)$, by the classical prime number theorem in a **fixed** arithmetic progression. For each $1\le j\le K$, $jr+1$ is divisible by $j+1$ and is larger than $j+1$; the same is true with $t$. Every prime factor of (4) therefore exceeds $Kr>c\sqrt{mrt}$. For each fixed $c$ and $m$ one can let $r,t$ tend to infinity. A diagonal choice also lets $m\to\infty$. [Bennett, Martin, O'Bryant and Rechnitzer, *Explicit bounds for primes in arithmetic progressions*, introduction](https://personal.math.ubc.ca/~gerg/papers/downloads/EBPAP.pdf)

For any fixed floor $R$ choose such an $m$ sufficiently large. Equations (3)–(4) give $B_n^*\ge d^{-s}$ for infinitely many least periods $n$, so the lower exponential rate is at least zero. The lower rate $\theta-s$ follows from the positive-entropy, near-full-denominator construction of [CYCLE_INDEX.md, §3](CYCLE_INDEX.md) with the carry-sequence refinement in [the independent sieve review](../renewal/CYCLE_SIEVE_REVIEW.md). The latter permits $a<1/2$. The upper bound is (5) of [CYCLE_INDEX.md](CYCLE_INDEX.md) and applies to every subset of the marked fixed points. Sending $R\to\infty$ proves (1).

## The ordinary obstruction that survives

The small denominator in (4) comes from additive superposition of periodic *affine offsets at a common slope*. The large clock is the exact least common multiple of the two independent flag periods. A universal lower bound $\log d\ge\varepsilon n$ for high-minimum primitive rational cycles fails even after testing primes up to $c\sqrt n$. An ordinary cycle would require $d=1$. Every displayed construction has $d=Q_rQ_t>1$.

The real phases of these examples also fail an ordinary integer spacing test. For each fixed $m$ their $rt$ distinct block-boundary phases lie in an interval of length $O(m/\delta)$ independent of $r,t$. Their minimum mutual real distance is at most $O(m/(\delta(rt-1)))$, which tends to zero. Choosing $r,t$ sufficiently large at each successive $m$ retains this failure while $m(x)\to\infty$. No simultaneous small-denominator and unit real spacing theorem for primitive cycles is claimed here. The large-denominator examples of [CYCLE_INDEX.md, §3](CYCLE_INDEX.md) do pass that spacing test.

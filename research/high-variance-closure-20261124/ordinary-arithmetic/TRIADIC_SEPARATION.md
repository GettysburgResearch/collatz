# Binary separation from every triadic rational

**PROPOSED written theorem.** Let $D$ be the dyadic companion in [DYADIC_COMPANION.md](DYADIC_COMPANION.md). For every positive ordinary $n$, every $A\in\mathbb Z$, and every $h\ge0$, put
\[
 a=A/3^h,\qquad
 N=5+h+\left\lceil\log_2(n+1)\right\rceil+
               \left\lceil\log_2(|A|+2)\right\rceil .
\]
Then either $D(n)=a$ or
\[
                         v_2(D(n)-a)\le 10^6 N.
\]
The constant is deliberately coarse. The result applies to the actual value at the supplied ordinary integer even if its trajectory is unknown. In particular it bounds how long an incorrect candidate can agree with the actual dyadic digits. It uses no limiting parity frequency.

## A trial with sufficiently many correct bits stays on the physical branches

Assume $v_2(D(n)-a)>10^6N$. At clock $i$ let $x_i=T^i(n)$, and form the rational trial $s_i=(a-B_i)/A_i$ with the finite physical weights from the companion note. It satisfies the same rational linear updates as the true companion. For $i\le K=430000N$,
\[
 v_2(s_i-D(x_i))=v_2(a-D(n))-i-p_i\ge 10^6N-2K>2.
\]
If the difference is zero the assertion is finished, so the valuations here may be taken finite. Each trial is binary integral, and it has the required even or $1\bmod4$ class at its actual step. The recurrence introduces no primes into the denominator beyond those of $a$ because its divisors are powers of two and the trial is binary integral. Every step also consumes one remaining denominator factor of three. Thus $s_i$ is an integer divisible by three for $h+1\le i\le K$.

Inductively $x_i\le2^i n$ and $|s_i|+2\le2^i(|a|+2)$; the latter follows separately from the two rational updates. In particular both $x_i$ and $|s_i|$ are at most $2^{i+N}$.

Set $j=160N$. If no physical state has dropped below 20 by clock $j$, the pinned high-prefix estimate gives
\[
 A_j^5\ge(256/243)^j/n^3>2^{7N}.
\]
Here $(256/243)^{16}>2$ by integer arithmetic, and $n<2^N$. It follows that $A_j>2^N+1$ because $N\ge5$. The finite identity $2B_j=3A_j-3+\sum_{i<j} A_i$ gives $B_j>|a|$. From clock $j$ onward the trial is negative and remains negative under either forward branch. Thus $w_i=-s_i/3$ is a positive integer from $j$ through $K$.

## A fixed finite physical base is reached

At clock $j$ the positive integer $H_j=x_j^2w_j^3$ is at most $2^{5(j+N)}=2^{805N}$. On every step with $x_i\ge20$ and $w_i\ge64$, the common contraction factor is at most
\[
 \theta=\frac{26750481097}{26843545600},\qquad 2\theta^{256}<1.
\]
The even factor $27/32$ is smaller. The second comparison is an exact integer power inequality. Within $256\cdot805N=206080N$ more clocks some $x_i<20$ or $w_i<64$, since a positive integer height cannot drop below one. This happens by $J=210000N$, including the earlier alternative before $j$.

A small integral $2\le w_i<64$ reaches its forbidden class in at most 17 clocks. This contradicts the available precision up to $K$. If $w_i=1$, all subsequent legal physical inputs are odd. A run of $\ell$ odd inputs requires $2^\ell\mid x_i+1$. As $x_i+1\le2^{J+N}+1$, a run lasting $K-J$ steps is impossible. There is enough precision for these steps since $K-J=220000N>J+N+1$. Thus, under the long-agreement assumption, **some physical $x_t<20$ occurs by $t\le J$**. This uses the arithmetic of one actual trial and one actual orbit, not a small representative from a changing progression.

## Agreement past this base forces equality

The physical finite base proves every $1\le b<20$ reaches 1 by at most 31 clocks. Because $D(1)=9$ and $D(x)=e+(2^{1+e}/3)D(Tx)$, each such $D(b)$ has odd denominator at most $3^{31}<2^{50}$ and absolute value at most $12(4/3)^{31}<2^{20}$. For the latter bound sum the maximal geometric prefix and the terminal $9(4/3)^{31}$. Also $s_t$ has odd denominator at most $3^h<2^{2N}$ and absolute value at most $2^{t+N}$.

If $s_t\ne D(x_t)$, putting them over the product of those denominators gives a nonzero integer numerator of absolute value at most
\[
 2^{2N+50}(2^{t+N}+2^{20})\le 2^{t+3N+71}.
\]
The binary valuation is no greater than the logarithm of this bound. Therefore
\[
 v_2(D(n)-a)
 =t+p_t+v_2(D(x_t)-s_t)
 \le 3J+3N+71 <10^6 N,
\]
contrary to the assumption. Thus $s_t=D(x_t)$ and the finite splitting identity yields $D(n)=a$.

In computational terms, $10^6N+1$ binary digits determine whether the specified triadic rational is exactly the companion of the specified input. This explicit bound concerns one candidate. Searching upwards over all denominator exponents and numerators gives no bound on the successful candidate for an arbitrary $n$.

## Why the separation estimate alone cannot give rationality

For comparison take $\alpha=\sqrt{17}\in\mathbb Z_2$, using either 2-adic square root (an odd integer equal to one modulo eight is a binary square). It is irrational over $\mathbb Q$. For every triadic $a=A/3^h$, the nonzero integer $A^2-17\cdot3^{2h}$ gives
\[
 v_2(\alpha-a)
 \le v_2(A^2-17\cdot3^{2h})
 \le \log_2|A^2-17\cdot3^{2h}|,
\]
since $\alpha+a$ is binary integral and $3$ is a binary unit. This is itself linear in $1+h+\log_2(|A|+2)$. The comparison scalar is not claimed to arise as an ordinary companion. It shows why this proved approximation exponent, by itself, cannot imply the missing arithmetic membership.

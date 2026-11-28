# Complete denominators for a bounded number of moving powered templates

Let a primitive positive rational cycle of length $n$ and odd count $u$ have common reduced denominator $q$ and determinant $D=2^n-3^u>0$. Suppose its cyclic parity word has the form
$$            W=A_1^{k_1} B_1 A_2^{k_2} B_2\cdots A_r^{k_r} B_r,  $$
where the number $r$ is fixed, each $A_i$ is nonempty, $k_i\ge1$, and
$$                     \sum_{i=1}^r(|A_i|+|B_i|)=o(n).              $$
Every template and connector can change with $n$. Then
$$                     \liminf\frac{\log q}{n\log 2}\ \ge\ 1/r.    $$
Every subsequential limit of the quotient is rational, with reduced denominator dividing $\gcd(n,u)$ on a further subsequence attaining it. In particular $\log_2 q/n\to1$ for coprime clock counts or when every fixed prime eventually misses their gcd. The proof uses the external moving-target gcd theorem through the [moving sparse-sum bound](MOVING_SPARSE_SUMS.md).

The fixed-dictionary multiple-piece result, the case of two moving template types, and the qualitative motivation are in PR212. The real-source estimate in PR214 obtains ordinary non-return path height using moving templates. The result here extends the **quantitative reduced rational denominator rate** to a bounded number of arbitrary moving template types and sublinear moving connectors. [PR212, 505d3fe782922904e86477990cc5d41e9110edda, POWERED_LANGUAGES.md](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/POWERED_LANGUAGES.md) · [PR214, a26638861210fd6e8da83f4cf36afc8e7858b957, POWERED_WORD_HEIGHT.md](https://github.com/GettysburgResearch/collatz/blob/a26638861210fd6e8da83f4cf36afc8e7858b957/research/astra-critical-rigidity-20261128/literature/POWERED_WORD_HEIGHT.md)

**Reduction to macroscopic pieces.** Begin on any subsequence where the normalized denominator logarithm converges. Pass further so that all $k_i|A_i|/n$ converge. At least one limit is positive. Absorb each piece of zero limiting fraction, and its connector, into the preceding surviving piece's connector in cyclic order. The total absorbed length is $o(n)$ since $r$ is fixed. Renumber the surviving pieces $1,\ldots,s$, $1\le s\le r$. The beginning clocks of cyclically consecutive powered pieces are separated by a positive limiting fraction of $n$. Rotate to the first such beginning.

For any word $A$ let its formal affine action be
$$        T_A(x)=\alpha_A x+\beta_A,
       \qquad \alpha_A=3^{u_A}/2^{|A|},\quad \beta_A=C_A/2^{|A|}. $$
The fixed point $s_A=C_A/(2^{|A|}-3^{u_A})$ exists since $|A|>0$. Its height is $O(|A|+1)$, by the explicit affine formula. This includes the centers $0$ for all-even and $-1$ for all-odd templates. The center stays fixed by $T_A^k$ for every $k$. Write $s_i=s_{A_i}$ with $s_{s+1}=s_1$ and
$$                        \kappa_i=T_{B_i}(s_i)-s_{i+1}.             $$
The heights of all nonzero $\kappa_i$ are $o(n)$. Let $x_i$ be the physical state at the beginning of piece $i$, cyclically $x_{s+1}=x_1$. Put $U_0=1$ and $U_i=2^{\ell_i}3^{-h_i}$ for the clock and weight of the prefix through the end of connector $B_i$, so $U_s=X=2^n3^{-u}$. Affine composition about the fixed center gives
$$ U_i(x_{i+1}-s_{i+1})=U_{i-1}(x_i-s_i)+U_i\kappa_i . $$
Telescoping and subtracting the last boundary term yields the exact identity
$$     (X-1)(x_1-s_1-\kappa_s)=V,\qquad
       V=\kappa_s+\sum_{i=1}^{s-1}\kappa_i U_i.                    \tag{1}$$

If every $\kappa_i=0$, then $x_1=s_1$. The actual first copy of the nonempty template $A_1$ would return to $x_1$ after $|A_1|=o(n)$ clocks, contradicting least period $n$ for all sufficiently large $n$. Thus after discarding zero coefficients, $V$ has $1\le t\le s$ terms. Each distinct pair of dates in $\{0,\ell_1,\ldots,\ell_{s-1}\}$ has cyclic distance at least a positive multiple of $n$. Each valuation correction $v_2(\kappa_i)$ is $o(n)$ in absolute value. Hence the adjusted dates of the remaining terms are pairwise distinct modulo $n$ eventually. The second case of the [sparse-sum theorem](MOVING_SPARSE_SUMS.md) applies, without a common sign hypothesis.

To compare complete denominators, clear all rational coefficient denominators in $V$ by one positive integer $H$ with $\log H=o(n)$. At each prime $p\nmid6$ the monomials $U_i$ are units and $v_p(HV)\ge0$. The outside-six denominator of $HV/(X-1)$ is therefore exactly $d_V$, with shared prime powers included. Dividing by $H$ changes its denominator logarithm by at most $\log H$. Adding $s_1+\kappa_s$ then changes the logarithm by at most the logarithm of this summand's denominator, which is also $o(n)$: if $z-z'=a/b$ then each reduced denominator divides $b$ times the other. Finally $x_1$ has reduced denominator $q\mid D$ and so has no denominator at two or three. Equation (1) consequently gives $\log q=\log d_V+o(n)$. Apply the lower bound $1/t\ge1/r$ and the quantization conclusion. With $s=t=1$ the same proof uses the single nonzero coefficient at date zero.

[Exact control program](moving_power_controls.py) checks 1,398 positive three-template displays with their physical affine numerators, signed coefficient jumps, and both directions of the denominator comparison. A primitive $(n,u)=(26,16)$ example with two distinct equal-type half words has $C_A=73213$, $C_B=14201$ and full $C=596685085$. The difference equals $4(2^{13}+3^8)$, so the entire nonprincipal factor $14753$ cancels and the reduced denominator is $1631$. This finite arithmetic rejects an unrestricted nonprincipal noncancellation assertion for primitive prime-gcd words. It does not test an asymptotic threshold.

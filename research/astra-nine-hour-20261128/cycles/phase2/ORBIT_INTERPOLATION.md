# What an integer successor polynomial costs on a closed orbit

**PROPOSED written results.** For a primitive positive rational shortcut cycle use its distinct positive cleared numerators $a_i$ and common reduced denominator $d$. Let $F\in\mathbb Q[X]$ interpolate the actual numerator successors: $F(a_i)=a_{i+1}$. Such a polynomial exists by interpolation. Its degree is unrestricted. For every positive integer $H$ with $HF\in\mathbb Z[X]$ we obtain divisibilities stated below. Write $u$ for the odd count and $n$ for the least physical period.

For ordinary cycles along any sequence $n\to\infty$,
$$
          \log H\ \ge\ (\log_3 2+o(1))\, n\log n .                 \tag{1}
$$
The estimate applies to *every* interpolant, without a congruence-compatibility hypothesis. It is far larger than $\log(2^n-3^u)<n\log 2$. The determinant controls the fixed-point coordinates of a word. A bound of that size for a polynomial realizing the permutation of the individual state coordinates would be a separate new theorem. Genuine ordinary path controls and positive rational closed controls below rule out two ways to obtain it.

## The exact integral ideal

Let $E(X)=\prod_{b\ {\rm even}}(X-b)$ and $O(X)=\prod_{a\ {\rm odd}}(X-a)$, with the products taken over the actual phases. In $\mathbb Z[X]/(E,O)$ let $h_*$ be the additive order of the class of $2X+d$. This order is finite, since the two monic polynomials have disjoint root sets and their nonzero integer resultant belongs to the ideal. Equivalently $h_*$ is the least positive $h$ for which $h(2X+d)\in(E,O)$.

**Exact criterion.** There is a polynomial interpolating all values $h(2a_{i+1}-a_i)$ with integer coefficients if and only if $h_*\mid h$. Necessity follows because its value vanishes on even inputs and equals $h(2a+d)$ on odd inputs. The two respective differences are divisible in $\mathbb Z[X]$ by the corresponding monic root products. Conversely, write $h(2X+d)=EQ+OR$ over $\mathbb Z[X]$. Then $EQ$ has the required values. If a successor interpolant with denominator $H$ exists, $h_*\mid H$. Conversely $(h_* X+EQ)/(2h_*)$ interpolates the successors using the preceding decomposition with $h=h_*$. The least clearing denominator for the unscaled successors is therefore either $h_*$ or $2h_*$ (the set of admissible clearing multipliers is an ideal of $\mathbb Z$).

Evaluating those monic divisibilities at each opposite-color root gives
$$
 \prod_{a\ {\rm odd}}|e-a|\ \mid H(2e+d)\quad(e\ {\rm even}),\qquad
 \prod_{e\ {\rm even}}|a-e|\ \mid H(2a+d)\quad(a\ {\rm odd}).       \tag{2}
$$
Unlike checking all pairs separately, the **entire product** in each row divides the displayed integer. If a prime $\ell$ does not divide $H$, reduction of the ideal criterion also shows
$$
               \gcd(\overline E,\overline O)\mid 2X+d
                         \quad\text{in }\mathbb F_\ell[X].          \tag{3}
$$
For odd $\ell$ at most one residue may mix parities, the class $-d/2$. At that class at most one root of the rarer parity occurs, keeping multiplicities. In addition reduction modulo $\ell$ is compatible, since $\bar F$ then gives the actual numerical successor as a function of the residue.

When the reduction is noninjective, the [modular-quotient proof](../MODULAR_QUOTIENTS.md) puts all variation in just one column modulo its projected period $s$. The roots in that column are distinct physical phases. By (3) its rarer symbol occurs just once. Thus the shift by $s$ has precisely two mismatches. The published ordinary lower bound of 42 in PR212 consequently implies that **every odd prime $\ell<n$ divides $H$** for any nontrivial positive ordinary cycle of least period $n$. For $\ell=2$, even without (3), a polynomial with odd clearing denominator would make the next parity a deterministic function of the current parity. An entire primitive parity cycle of length $n>2$ cannot then occur. This prime-factor consequence imports PR212's stated large-period and numerical verification inputs. Estimate (1) below does not need them.

## An unconditional factorial obstruction

The minimum numerator $a_*$ is odd, and the first ensuing even phase $e$ occurs after $L\ge1$ odd steps. On consecutive odd steps the shifted recurrence reads $2(a_{i+1}+d)=3(a_i+d)$. Thus $2^L\mid a_*+d$ and
$$
          e+d=(3/2)^L(a_*+d)\le (a_*+d)^{\log_2 3}.
$$
For an ordinary cycle $d=1$ the polynomial minimum bound in [the first note](../MODULAR_QUOTIENTS.md) gives $\log(2e+1)=O(\log n)$. At most two odd integers have a particular positive distance from $e$, and all these distances are odd. If $u$ such distinct roots occur, their distance product is at least
$$
          \prod_{j=1}^{u} \big(2\lfloor(j-1)/2\rfloor+1\big)
                      \ge \frac{u!}{2^u}.
$$
For the last inequality the $j$-th factor is at least $j/2$. Equation (2) gives $\log H\ge u\log u-O(u+\log n)$, by Stirling or the elementary integral bound on $\log(u!)$. Finally the exact cycle gap equals $\sum_{a\ {\rm odd}}\log(1+1/(3a))$. Summing reciprocals of $u$ distinct positive odd integers bounds it by $O(\log n)$, so $u=n\log_3 2+O(\log n)$. This proves (1). The factorial argument itself supplies a bound with the actual $e$ and $d$ even at a different odd density.

## Controls for a proposed determinant upper bound

**Positive ordinary, finite and near the critical slope.** Take $k\ge2$, $j=\lceil k(\log_2 3-1)\rceil$, and a positive odd $t$ with $3^k t\equiv1\bmod 2^j$. The start $2^k t-1$ follows $k$ odd shortcuts and then at least $j$ even shortcuts. The printed $k+j$-bit word has positive determinant $2^{k+j}-3^k$. Its first even phase is $e=3^k t-1$, and its preceding odd phases are $a_i=2^{k-i}3^i t-1$ for $0\le i<k$. Their distinctness and all branch parities follow directly. Equation (2) only needs these $k$ odd edges and the first even edge. Since $3^i\mid e-a_i$ and $3\nmid 2e+1$, every clearing denominator is divisible by $3^{k(k-1)/2}$. This already exceeds the size of the positive word determinant for all sufficiently large $k$. These are actual integer edges. The starting height may grow exponentially, and exact full return is not imposed.

**Positive rational with an exact return.** The word with one odd bit followed by $n-1$ even bits has $d=2^n-3$, minimum numerator $a=1$ and even numerators $2,4,\ldots,2^{n-1}$, in reverse execution order. For $n\ge2$ these are literal distinct phases. Row (2) gives
$$
                  \prod_{j=1}^{n-1}(2^j-1)\mid H(2^n-1).
$$
Thus $\log H\ge(\log2)n(n-1)/2-O(n)$ even though the positive full determinant is just $2^n-3$. This example has exponentially large $d$. In the signed ordinary setting the $-17$ cycle has least period 11 and absolute raw determinant 139. Every odd prime below 11 is incompatible by the prime-period argument and must divide $H$, so $H\mid139$ is false there as well.

**Remaining question.** Ordinary positivity, full closure and coefficient-height control would have to be used together to prove a sufficiently small representation. General interpolation, integer path recurrence alone, and positivity plus rational closure do not do so. Equation (1) is a necessary condition on any nontrivial ordinary cycle and an obstruction to a particular proof strategy. It does not itself give the missing upper bound.

The translated-product result in PR211, `4b44cded44af5bb7c3ce67fb16a70c898ad505d5`, `research/astra-reciprocal-rigidity-20261127/cycles/ARITHMETIC.md`, recovers endpoint-multiset equality from enough scalar translated products. Here the polynomial acts on phase coordinates and must represent the specific outgoing permutation, with coefficient denominators retained. PR212, `505d3fe782922904e86477990cc5d41e9110edda`, `research/astra-infinite-descent-20261127/cycles/ALL_SHIFT_HEIGHTS.md`, supplies the separately cited two-mismatch exclusion, with its external inputs.

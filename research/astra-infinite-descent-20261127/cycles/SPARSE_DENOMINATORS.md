# Full denominators for cycles with a fixed number of odd runs

**PROPOSED written theorem.** Use the shortcut map on rationals of odd reduced denominator, dividing by two on an even numerator and sending an odd input to $(3x+1)/2$. Suppose a positive cycle has a displayed word of $h$ shortcut steps, $p$ ones and $k\ge1$ maximal cyclic runs of ones. Write $q$ for its complete reduced denominator. Along any sequence with fixed $k$ and $h\to\infty$,
$$
                 \liminf \frac{\log_2 q}{h}\ \ge\ \frac1k.                 \tag{1}
$$
The bound includes repeated words. It is sharp for displayed words. The repetition $(10^{n-1})^k$ has $h=kn$ and $q=2^n-3$ for $n\ge2$. For **primitive words with two runs** the lower limit improves to **one**. More generally (1) improves to one whenever $h,p$ are coprime, or more generally when their gcd has no bounded prime divisor along the sequence. The onset is ineffective.

Finiteness of ordinary cycles with any fixed number of local minima already follows from classical work, which also gives effective and much stronger information for particular integer cases. Here the estimates measure the entire moving rational denominator. The unrestricted number of runs of a putative integer cycle remains open. [Simons and de Weger, *Theoretical and computational bounds for m-cycles*](https://doi.org/10.4064/aa117-1-3) · [Hercher, *There are no Collatz-m-cycles with m ≤ 91*](https://arxiv.org/abs/2201.00406) · [Halbeisen and Hungerbühler on rational cycles](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)

## A sparse integer numerator

Write $D=2^h-3^p>0$ and $X=2^h/3^p$. For a bit word with ones at dates $i$, and $k_i$ ones strictly before date $i$, its fixed point is $C/D$, where
$$
 C=\sum_{i:\,w_i=1}2^i3^{p-k_i-1},\qquad q=D/\gcd(C,D).
$$
Reading parities at successive rotated cuts recovers the entire rational cycle, and multiplication by the units two and three preserves $q$. The absolute logarithmic Weil height $\mathrm h(X)=h\log2$. A classical two-logarithm lower bound for the nonzero $h\log2-p\log3$ gives $\log D=h\log2+o(h)$ uniformly for positive $D$ and $p\le h$. Lagarias, Lemma 2.2(1), gives a polynomial separation with explicit constants. [Lagarias, *Ternary expansions of powers of 2*](https://arxiv.org/abs/math/0512006)

First consider any signed sum
$$
 C_*=\sum_{j=1}^s c_j\, 2^{i_j}3^{b_j},
 \qquad 0\le i_1<\cdots<i_s<h,\qquad 0\le b_j\le O(h),              \tag{2}
$$
with $s$ fixed and fixed nonzero odd integral coefficients $c_j$. Its unique least dyadic valuation gives $C_*\ne0$. Put $g=\gcd(D,C_*)$. Then
$$
 \liminf_{h\to\infty}\frac{\log_2(D/g)}h\ge\frac1s.                \tag{3}
$$
If the reduced denominator of every $(i_j-i_l)/h$, $j\ne l$, tends to infinity, the right side is one. This includes the case of increasingly rough $h$.

## The exceptional torus components

Take an infinite subsequence of any proposed violation with a fixed positive margin. Set $Y_j=2^{i_j}3^{b_j}$. By Laurent's torus theorem choose a connected torus translate of least dimension containing infinitely many of the tuples $(X,Y_1,\ldots,Y_s)$. A proper closed subset of this translate contains only finitely many retained tuples. Its intersection with the ambient finitely generated group lies in finitely many translates of lower dimension. Heights of all original coordinates are $O(h)$, and $X$ is nonconstant since its dyadic exponent is $h$. Take one retained rational point as origin of the translate. The integral character lattice of its split subtorus admits a basis with
$$
 X=cT^d,\qquad Y_j=c'_jT^{m_j}Z^{u_j},\qquad d\ge1.               \tag{4}
$$
Here $T$ is a primitive character, $Z$ denotes the remaining basis characters, and $u_j$ are integral vectors. All constants are fixed rational $\{2,3\}$-units. At the retained points $T,Z_l$ are rational $\{2,3\}$-units of height $O(h)$, since the restricted characters lift to ambient integral characters. Also $\mathrm h(T)=h\log2/d+O(1)$. [Laurent, *Équations diophantiennes exponentielles*, Théorème 1](https://doi.org/10.1007/BF01388597)

Let $F=cT^d-1$ and $G=\sum_j c_jc'_j T^{m_j}Z^{u_j}$ in the Laurent polynomial ring. Work over the fixed number field splitting $F$. Write $R(T)$ for the monic product of the $M$ distinct factors $T-\lambda$ of $F$ dividing $G$. It is their entire common factor since $F$ is squarefree. The residual factors $F/R,G/R$ are coprime. Clear negative exponents of $G/R$ with a monomial, a unit outside places over 2 and 3. The polynomial $F/R$ has a nonzero constant term. Levin's multivariable gcd theorem bounds the logarithmic gcd of the residual factors outside these primes by $o(h)$ on this subsequence. Apply the theorem with each fixed positive tolerance to the evaluated $T,Z_l$. Their heights are $O(h)$ and the proper exceptional closed set contains only finitely many retained points. All coefficients before division are integral outside 2 and 3. Monic division by $R$, whose roots are units there, retains that integrality. The contribution of $R(T)$ to the outside gcd is at most $\mathrm h(R(T))\le M\,\mathrm h(T)+O(1)$, using normalized places over the fixed splitting field. Since $D$ is coprime to six, this gives
$$
                     \log g\le (M/d)h\log2+o(h).                    \tag{5}
$$
This argument includes translated subtori and every integral prime power. The dimension-one case also follows from the univariate resultant. [Levin, *Greatest common divisors and Vojta's conjecture for blowups of algebraic tori*](https://doi.org/10.1007/s00222-018-0831-z) · [Author's statement of the multivariable polynomial bound](https://www.math.columbia.edu/~goldfeld/JNT-ALevin.pdf)

## How many common roots can occur?

Group the terms by equal $u_j$ in (4). Fix any nonempty group of size $s_0$, one root $\lambda_0$ of $cT^d=1$, and a primitive $d$th root of unity $\zeta$. At $\lambda_0\zeta^t$ this group's coefficient of its $Z$ monomial is
$$
    \sum_{r\bmod d} A_r\zeta^{rt},\qquad
    A_r=\sum_{j:\,m_j\equiv r\pmod d}c_jc'_j\lambda_0^{m_j},
$$
with the inner sum confined to this group. Every occupied $A_r$ is nonzero. For two terms in the same residue, the difference of their valuations above two at $T=\lambda_0$, normalized by $v_2(2)=1$, is
$$
          i_j-i_l-\frac{m_j-m_l}{d}h.                               \tag{6}
$$
The coefficients $c_j$ are odd, all terms share $Z^{u_j}$, and $v_2(T)-v_2(\lambda_0)=h/d$ at a retained point. The quotient $(m_j-m_l)/d$ is integral in this residue class. Since the $i_j$ are distinct in one interval of length $h$, (6) cannot vanish. Every nonempty subsum within an occupied residue therefore has a unique least valuation.

If $m$ residues occur, their $m$ bases $\zeta^r$ are distinct and nonzero. A sum with these nonzero coefficients cannot vanish at $m$ consecutive exponents $t$, by the invertibility of the Vandermonde matrix. Counting all $d$ cyclic windows of length $m$, each nonzero sample accounts for exactly $m$ windows. Hence at least $d/m\ge d/s_0$ samples are nonzero. Each one excludes a common factor of $F,G$, giving $1-M/d\ge1/s_0$. This proves (3). It is enough to use the smallest group. For the rough-clock assertion, one common root requires a tie for the least dyadic valuation among terms of any chosen group at that root. Formula (6), now for arbitrary $m_j,m_l$, then forces the reduced denominator of $(i_j-i_l)/h$ to divide the fixed $d$, contrary to the stated separation.

## The exponent on a fixed translate and the two clocks

The common monic $R$ is rational. The set of its roots is invariant under all automorphisms over $\mathbb Q$, because (4), $F$ and every coefficient of $G$ as a polynomial in $Z$ are rational. Put $J=d-M$. Both $R$ and $F/R$ are integral outside 2 and 3, and their positive outside valuations add to $\log D=h\log2+o(h)$ at the retained point. Their respective upper bounds are $M\,\mathrm h(T)+O(1)$ and $J\,\mathrm h(T)+O(1)$. These add to $h\log2+O(1)$. Each outside valuation sum must therefore attain its own upper bound up to $o(h)$. Since $R$ divides $G$ over the same integral Laurent ring and the residual gcd contributes $o(h)$ by (5), we obtain the exact limit on the retained subsequence
$$
            \frac{\log(D/g)}{h\log2}\ \longrightarrow\ J/d.           \tag{8}
$$

The denominator of the rational fraction $J/d$ divides both clock counts $h,p$ at every retained point. Indeed every root of $F$ has valuation $-v_\ell(c)/d$ at $\ell=2,3$. The monic rational factor underlying $F/R$ has degree $J$ and its nonzero rational constant has valuation $-Jv_\ell(c)/d$. Thus $d\mid Jv_\ell(c)$. Since $X=cT^d$ with rational $T$, this implies $d\mid Jh$ and $d\mid Jp$. The character-sum proof gives $J>0$. If $h,p$ are coprime then $J=d$, so the exponent in (8) is one. The same argument applies if for every fixed prime $\ell$, eventually $\ell\nmid\gcd(h,p)$. More generally, every subsequential limit in (3) is rational, and its reduced denominator divides $\gcd(h,p)$ on a further subsequence. This claim is about a fixed number of terms with fixed coefficients. No uniform list of translate degrees is required.

## Getting the sharp count of odd runs

Cut the word at the first one following a longest even run, placing all $2k$ odd-run boundaries at distinct dates in $[0,h)$. A run of $a$ ones starting at date $i$ with $j$ earlier ones contributes exactly
$$
                       2^i3^{p-j}-2^{i+a}3^{p-j-a}.                 \tag{7}
$$
This telescopes the consecutive summands for its ones. Thus (2) applies with $2k$ coefficients $+1,-1$. If $p$ stays bounded, pass to a subsequence with the odd-run lengths and $p$ fixed. Combine each run into one term $2^i3^{p-j-a}(3^a-2^a)$ with fixed odd coefficient. Applying (3) with $s=k$ gives (1).

If $p\to\infty$, the final even run of length $L$ has $L\ge(h-p)/k\gg h$, since $p/h<\log_3 2<1$. Its endpoints correspond to the last negative monomial $2^{h-L}$ and the first positive monomial $3^p$ in (7). If these terms lie in the same $u$-group on the translate, their ratio equals $c'T^m$. Comparing its 3-adic order with that of $X=cT^d$ gives $-p=-(m/d)p+O(1)$, hence $m=d$. Comparing dyadic orders now gives $h-L=h+O(1)$, contradicting $L\to\infty$. There are at least two groups. The smallest contains at most $k$ terms, so (5) and the character bound give (1). The coprime-clock consequence of (8) and the rough-clock clause of (3) apply directly to (7).

## Primitive words with two runs

Write the word as $1^a0^e1^b0^f$ with all four lengths positive. First take $p=a+b\to\infty$. At least two groups occur among the four boundary terms by the preceding argument. If $M>0$, there is no singleton group, so there are exactly two pairs. At a common root a two-term cancellation forces equality of its constituents' valuations above 2 and above 3. By (6) and its 3-adic counterpart, the chord between their endpoint dates and cumulative one-counts is exactly proportional to $(h,p)$. This is invariant on replacing a chord by its cyclic complement. Endpoints of any single run cannot be paired because its chord has slope 0 or 1 and $0<p/h<1$. The only matching pairs the two starts and the two ends. This forces
$$
                  (a+e)p=ah,\qquad(e+b)p=bh.
$$
It follows that $a=b$ and $e=f$. Thus a primitive word has $M=0$, and (5) gives $\log q=h\log2-o(h)$.

If $p$ stays bounded, fix $a,b$ on a subsequence. Put $A=3^a-2^a$ and $B=3^b-2^b$. The numerator is $C=3^bA+2^{a+e}B$. If $a\ne b$, the quotient $B/A$ has a nonzero valuation at a prime outside $\{2,3\}$ because both positive, distinct integers are coprime to six. Thus $X$ and $-2^{a+e}B/(3^b A)$ are multiplicatively independent. Corvaja and Zannier, Proposition 2, applied in the fixed group enlarged by primes of $AB$, gives $\log\gcd(D,C)=o(h)$. Its bound uses all places. Normalizing by $3^b A$ changes the positive valuations outside 2 and 3 by at most the fixed divisor of $A$. If $a=b$, remove the fixed factor $A$. The units $X$ and $-2^{a+e}/3^a$ are multiplicatively dependent only if $(a+e)p=ah$, forcing $e=f$. Thus every primitive two-run sequence has full exponential denominator. [Corvaja and Zannier, Proposition 2](https://arxiv.org/pdf/math/0311030)

## Verification and remaining obligation

[Collected Lean identities](SparseCarry.lean) derive (7) for arbitrary lists of odd and even run lengths and the exact two-edit identity. [Finite character-sum lemma](FourierSupport.lean) proves that distinct bases with a nonzero coefficient cannot vanish on an entire block of the specified length. The algebraic torus, height, valuation and cyclic-window counting arguments above are written proofs. Levin's gcd theorem, Laurent's theorem and the two-logarithm estimate are external. Fixed-$k$ finiteness at denominator one supplies no estimate uniform over growing $k$. A complete cycle argument needs to eliminate actual integer words with unbounded numbers of runs.

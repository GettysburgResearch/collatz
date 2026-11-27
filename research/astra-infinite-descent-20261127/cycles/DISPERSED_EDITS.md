# Denominators after dispersed adjacent swaps

**PROPOSED written theorem.** Start with any positive rooted rational shortcut cycle of length $h$ and grade $p$, with determinant $D=2^h-3^p>0$. Reverse $b$ disjoint mixed adjacent pairs, which can be arbitrarily distant around the cyclic word. Use a cut outside the interiors of the edited pairs. Write $q_0,q_1$ for the original and edited complete denominators, and $Q$ for the reduced denominator of the difference between the two rational fixed points at this cut. Then $Q\mid\operatorname{lcm}(q_0,q_1)$, and if $q_0=1$ then $q_1=Q$.

For fixed $b\ge1$ and growing $h$,
$$
              \liminf \frac{\log_2 Q}{h}\ge\frac1b.
$$
Every possible limit is rational. Its reduced denominator divides $\gcd(h,p)$ along a further subsequence. In particular if $\gcd(h,p)=1$ or its least prime factor tends to infinity, $\log_2 Q/h\to1$. A full-exponent difference forces $q_1=2^{h-o(h)}$ if $q_0=2^{o(h)}$. This concerns every choice of $b$ disjoint swaps in the word and allows a nonprimitive displayed lap. [Sparse numerator theorem and proof](SPARSE_DENOMINATORS.md)

A change $10\longmapsto01$ adds $2^i3^{p-k_i-1}$ to the raw carry, where $i$ is the first date of the pair and $k_i$ is the preceding one-count. The reverse change subtracts this quantity. Edits on disjoint pairs leave the date and preceding grade of every other pair unchanged. The resulting signed sum $S$ therefore has $b$ distinct dyadic exponents in $[0,h)$. Since the change in fixed points is $S/D$, its exact reduced denominator is $Q=D/\gcd(D,S)$. This proves the conclusions from (3) and (8) of the sparse theorem. For one swap, the signed increment itself is a $\{2,3\}$-unit, so $Q=D$ exactly. The previously established one-swap formula and the bound for a sublinear contiguous replacement apply in their own scopes. [Prior adjacent-swap calculation](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-universal-descent-20261124/HIGH_COMPLEXITY_CONTROLS.md) · [PR193 contiguous surgery](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/arithmetic/CYCLE_SURGERY.md)

## Two swaps with the complete resonance formula

Let $A$ be the difference in starting dates of the two pairs and $B$ the difference in their preceding one-counts. Thus $0<A<h$ and $0<B<p$. Let $\sigma=+1$ if the edits have opposite signs and $\sigma=-1$ if they have equal signs. The exact cancellation is
$$
                   g=\gcd(D,\,2^A-\sigma3^B),\qquad Q=D/g .
$$
If $Ap\ne Bh$ then $\log_2 Q/h\to1$ uniformly on this class as $h\to\infty$. Apply Corvaja and Zannier, Proposition 2, to the multiplicatively independent rational units $2^h3^{-p}$ and $\sigma 2^A3^{-B}$. Their heights are $O(h)$; the logarithmic gcd outside two and three is exactly $\log g$. [Corvaja and Zannier, Proposition 2](https://arxiv.org/pdf/math/0311030)

For $Ap=Bh$, let $G=\gcd(h,p)$, take the integer $0<l<G$ with $(A,B)=l(h,p)/G$, and put $e=\gcd(G,l)$, $m=G/e$, $n=l/e$, $U=2^{eh/G}$, $V=3^{ep/G}$. Then
$$
g=\begin{cases}
 U-V &\sigma=+1,\\
 U+V &\sigma=-1,\quad m\ \text{even},\\
 1   &\sigma=-1,\quad m\ \text{odd}.
\end{cases}
$$
To see this at every prime power simultaneously, $g$ is odd and $U,V$ are units modulo $g$. The ratio $z=U/V$ there satisfies $z^m=1$ and $z^n=\sigma$, with $\gcd(m,n)=1$. For $\sigma=1$, Bézout gives $z=1$. For $\sigma=-1$ and odd $m$, raising the second equality to $m$ forces $g\mid2$. For even $m$ the coefficient of $n$ in a Bézout identity $um+vn=1$ is odd, hence $z=-1$. Conversely the indicated $U-V$ or $U+V$ divides both inputs directly. This proves the formula, including imprimitive clocks.

The $1/b$ lower bound is sharp over displayed words even when the original source is the positive integer 1. Start from $(10)^{bn}$, reverse the first $10$ in each of the $b$ identical blocks $(10)^n$, and take $n\to\infty$. The new word is $b$ repetitions of a single one-swap block. Its reduced denominator is exactly the one-block determinant $4^n-3^n$, giving the ratio $1/b$. A claim of nearly complete denominator after *all* dispersed edits would fail on this example.

## A primitive four-run obstruction to a stronger assertion

Some primitive fixed-run words genuinely cancel an exponential part of the determinant. Take four odd-to-odd exponents $n,n+1,n,n-1$ for $n\ge3$, a shortcut lap of $h=4n$, $p=4$ with four singleton odd runs. The four-letter exponent word is primitive. With $T=2^n$, the literal carry and determinant are
$$
              C=27+9T+6T^2+2T^3=(T+3)(2T^2+9),\qquad
              D=T^4-81=(T+3)(T-3)(T^2+9).
$$
The displayed cofactors have no common polynomial root. Their evaluated gcd is bounded by the fixed nonzero integer resultant. Thus $\log_2 q/h\to3/4$. This illustrates both the rational degree fraction in (8) and the need for its clock qualification. The result concerns rational cycles, while the decision for unrestricted ordinary cycles remains open.

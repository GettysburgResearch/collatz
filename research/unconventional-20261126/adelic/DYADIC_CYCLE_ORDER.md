# An integer-coordinate inversion count on the odd cycle's dyadic lifts

**Status.** Proposed theorem. This tries to compare phases with *different* native halving clocks, which the equal-grade synchronized comparison in [ORDER_REVERSALS.md](ORDER_REVERSALS.md) cannot do. It yields a numerical obstruction in the noncoprime sector, with an exact parity law. It does not exclude the full integer determinant in either sector.

Let $V$ be the distinct odd phases of a primitive positive integer cycle, of odd period $p$. Write $N=\sum_{x\in V}v_2(3x+1)$ for its native period and $g=\gcd(N,p)$. Count ordered pairs by
\[
 I(V)=\#\{(x,y,k):x,y\in V,\ k\ge1,\ y=2^kx+j,\quad 0<3j<2^k-1\} .            \tag{1}
\]
For a given ordered pair there is at most one such $k$ since the intervals $[2^kx,2^k(x+1/3))$ are disjoint. Then
\[
                 I(V)\ge g-1,\qquad I(V)\equiv g-1\pmod2.                      \tag{2}
\]
Each witness has $k\ge3$ and $y>8x$. The binary digits of $y$ start with the entire binary word of $x$ and the remaining $k$ bits form the positive integer $j<(2^k-1)/3$. In particular a noncoprime ordinary cycle needs at least $g-1$ such ordered phase pairs. Every cycle whose odd maximum is at most eight times its odd minimum has coprime grade and clock. Neither converse is asserted.

## Lift and displacement

Index the discrete ordered set $\{2^s x:s\in\mathbb Z,x\in V\}$ increasingly as $(z_i)_{i\in\mathbb Z}$, with $z_{i+p}=2z_i$. Odd representatives are unique. The lift
\[
                      F(2^s x)=2^s(3x+1)
\]
is a bijection of this set, because the odd part of $3x+1$ permutes $V$ in a single cycle and all its powers of two are present. Write $F(z_i)=z_{f(i)}$. Then $f(i+p)=f(i)+p$. On the quotient modulo $p$ this is one $p$-cycle. Its average displacement is exactly $N$. Indeed write $f(i)=r_i+pq_i$ for $0\le i<p$, $0\le r_i<p$. The $r_i$ form a permutation, so the average is $\sum_iq_i$, and
\[
   2^{\sum_iq_i}=\prod_{0\le i<p}\frac{F(z_i)}{z_i}
     =\prod_{x\in V}\frac{3x+1}{x}=2^N.
\]

The inversions $(i,j)$ with $i<j$ and $f(i)>f(j)$ have only finitely many classes modulo simultaneous translation by $p$, since $f(i)-i$ is bounded. Each is a term of (1): write $z_i=2^s x$, $z_j=2^t y$. Then $2^{s-t}x<y$ whereas $2^{s-t}(3x+1)>3y+1$. These are impossible for $s-t\le0$, by subtraction, and for $k=s-t>0$ they give precisely $0<3(y-2^kx)<2^k-1$. Conversely every (1) supplies exactly one simultaneous-doubling class of such inversions.

For $p\ge2$, any adjacent descent of $f$ can be removed by interchanging the images at those two positions and at all their period translates. These are disjoint adjacent transpositions on $\mathbb Z$. This removes exactly one inversion class: each swapped pair loses its own inversion, and comparisons across two disjoint ordered blocks (a swapped pair or a singleton) collectively see the same two value multisets as before. This description applies also to the pair across the boundary of a fundamental interval. Average displacement is unchanged, since one may take a length-$p$ interval containing the selected pair and only its residue class of swaps. Each removal composes the quotient permutation with one transposition. After exactly $I(V)$ removals the lift is an increasing bijection of the integers, hence $f(i)=i+N$ by its displacement. The latter quotient permutation has exactly $g$ cycles. One transposition changes the cycle count by precisely one up or down. It takes at least $g-1$ of them to get from one cycle to $g$, with the parity in (2). For $p=1$ the lift was a translation at the outset and both statements hold immediately.

## A structural feature that uses the ordinary denominator one

For every odd phase form the half-open interval $[3x,3x+1)$ and divide its endpoints by $2^{\lfloor\log_2(3x)\rfloor}$ into $[1,2)$. These are exact binary prefix intervals. Any two have disjoint interiors or one contains the other. Distinct phases cannot have the same left endpoints, since their odd representatives are distinct. Equality of their normalized right endpoints would give the same odd part $U(x)$, impossible on one primitive cycle. The strict containments are therefore counted exactly by (1). For nested intervals coming from $x,y$, their relative lengths are $2^{-k}$ with $k\ge3$. This gives a concrete denominator-one constraint at every physical phase of the cycle. Using numerators $x$ of a denominator-$d$ rational cycle changes the intervals to $[3x,3x+d)$ and the right side of the crossing inequality to $d(2^k-1)$. The normalization no longer necessarily gives binary prefix intervals for $d>1$.

The arithmetic still permits the obstruction's separate ingredients. On a single genuine positive trajectory, $41$ reaches $5$ in 39 odd steps and then $1$. These two odd states exhibit $41=8\cdot5+1$ with $3<7$. Thus positivity, integral spacing, membership in one actual orbit, and eventual entry into the known cycle do not preclude a strict nesting. In the coprime sector, the positive rational cycle with odd numerator sequence $19,31,49$ over denominator $5$ has odd period $3$, clock $5$ and no dyadic-lift inversions. Its native period word is a rotation of `00111`, which contains both `00` and `11`; pure rotation on the dyadic-lift order therefore does not force a balanced native parity word. The rational example does not itself satisfy denominator one. The integer theory in (2) still lacks an upper bound below $g-1$ in general, and at $g=1$ its lower bound is zero.

The ordinary state-rank breakpoint estimates in Paper 22 concern the permutation of the odd states in their usual increasing real order. Here the permutation is lifted to *all* dyadic scales, and the forbidden pairs compare actual odd states near a power-of-two multiple. The finite octave-order theorem of Paper 222 gives a separate sharp description of odd trajectories inside a single factor-of-two band. [Ordinary state-order bounds](https://rstation.ai/problems/collatz/papers/22) · [Order of odd states in a single octave](https://rstation.ai/problems/collatz/papers/222)

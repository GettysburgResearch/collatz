# Multiplication by three determines the whole conjecture

**PROPOSED, unconditional.** For the positive shortcut Collatz map $T$ write $f(n)$ for the component of $n$ under eventual meeting at independent clocks. Then
$$
 \bigl(\forall n\ge1,\ n\text{ reaches }1\bigr)
 \quad\Longleftrightarrow\quad
 \bigl(\forall n\ge1,\ f(3n)=f(n)\bigr).
$$
The same equivalence holds if the right side is required only for all sufficiently large odd $n$. Moreover, if Collatz is false, the number $B(X)$ of parameters $t\le X$ for which $t$ and $5t+1$ never meet satisfies $B(X)/\log X\to\infty$. Thus even $B(X)=O(\log X)$ along an unbounded sequence of cutoffs would suffice for full convergence. No such upper bound is proved here.

## From exact multiplication by three to descent

Write $g(y)=f(y-1)$ for $y\ge2$. Assume $f(3n)=f(n)$ for every $n$. We always have $f(2n)=f(n)$. The ordinary paths $T(2h-1)=3h-1$ and $T(3(8h-1))=4(9h-1)$ give $g(2h)=g(3h)$ and $g(8h)=g(9h)$. Consequently $g(4h)=g(6h)=g(9h)=g(8h)$. By doubling and then exchanging factors of two for factors of three,
$$
 g(4h)=g(2^i3^j h) \qquad(i+j\ge2).
$$

Two explicit classes supply the required adjacent merger. For $y=8k+5$, both $y-1$ and $y$ reach $3k+2$ in three steps. For $y=16k+3$, both reach $9k+2$ in four steps. The odd residues modulo $16$ split into the two multiplication-by-three cycles $(1,3,9,11)$ and $(5,15,13,7)$. Each cycle visits at least one of these merger classes.

Write $h=2^v u$ with $u$ odd. For every $j\ge v+2$, doubling $4h$ exactly $j-v-2$ times preserves $g$, and $j$ exchanges $2z\mapsto3z$ then show $g(4h)=g(3^j u)$. Choose $j$ between $v+2$ and $v+5$ with $y=3^j u$ in a merger class. Adding any multiple of four to $j$ preserves that class. It follows that
$$
 f(4h-1)=g(4h)=g(y)=f(y)=f(h).
$$

Strong induction now settles all starts under the assumption. Evens halve and odds $n>1$ congruent to 1 modulo 4 reach $(3n+1)/4<n$ in two steps. For $n=4h-1$ the displayed equality gives the smaller component representative $h$. The component of 1 consists precisely of starts that visit its cycle. Conversely full convergence makes the component label constant.

## Finitely many exceptional odd multipliers suffice

Assume that only finitely many odd $x$ have $f(3x)\ne f(x)$. For every $x$, the sequence $f(3^jx)$ is eventually constant. Write $F(x)$ for its eventual label. We have $F(2x)=F(3x)=F(x)$. Also $F$ and $f$ differ on at most finitely many odd parts. Indeed, if $f(x)\ne F(x)$, some $3^jx$ has an odd part in the finite failure set, so the odd part of $x$ divides an element of that set.

For all sufficiently large $h$, the two $g$ relations used above still give $g(4h)=g(8h)$, since $f(3(8h-1))=f(8h-1)$ for every sufficiently large odd input $8h-1$. For each such $h=2^v u$ with $u$ odd, doubling at $h,2h,\ldots$ and swapping twos for threes gives $g(4h)=g(3^j u)$ for every $j\ge v+2$. Choose arbitrarily large $j$ in one of the explicit merger classes above, so $g(4h)=f(3^j u)=F(h)$.

This implies $f(x)=F(x)$ for **every** $x$ prime to three, even at small $x$. Take arbitrarily large $a$ with $2^a x\equiv1\pmod3$. Then $w=(2^a x-1)/3$ is large, positive and odd, so $f(3w)=f(w)=f(2^{a-1}x)=f(x)$. But $f(3w)=g(2^a x)=F(2^{a-2}x)=F(x)$ by the preceding paragraph.

## Eliminating the last possible exceptional odd part

If $f$ ever differs from $F$, let $x$ be the largest odd integer on which they differ. Then $3\mid x$. Write $H(y)=F(y+1)$. Whenever $4h+1>x$, we have $H(4h)=H(3h)$. Indeed $T^2(4h+1)=3h+1$. The odd input exceeds $x$, and the output is prime to three, so $f$ agrees with $F$ at both ends.

For every $9s>x$, this identity gives $H(9s)=H(12s)=H(16s)$. To connect $H(16s)$ to $H(18s)$, use
$$
 T^2(3(16s+1))=4(27s+2),\qquad T(18s+1)=27s+2.
$$
The odd inputs $3(16s+1)$ and $18s+1$ exceed $x$, so $f$ equals $F$ at both. They meet after divisions by two, and $F(3(16s+1))=F(16s+1)$. Thus $H(16s)=H(18s)$ as claimed. This proves $H(y)=H(2y)$ whenever $9\mid y$ and $y>x$. In particular $H(3x)=H(4^i3x)$ for every $i\ge0$. Both $4^i3x+1$ and $3^{i+1}x+1$ are units modulo three and the first reaches the second in $2i$ steps. Consequently
$$
 f(x)=f(3x+1)=H(3x)=H(3^{i+1}x)=f(3^i x)=F(x)
$$
for all large $i$, where $3^i x$ is odd. This contradicts the choice of $x$. Hence $f=F$ everywhere, multiplication by three preserves every component, and the first theorem gives full convergence.

## Counting failures on the five-ray

Let $B(X)$ count actual failures of $t\sim5t+1$ up to $X$. For each odd $x$ with $f(3x)\ne f(x)$ and every $a\ge2$, at least one of $2^a x$ and $3\cdot2^{a-2}x$ is a five-ray failure, by $T^2(20u+1)=15u+1$. Across any fixed finite set of odd $x$ and all $a$, a parameter is counted at most twice. Its odd part is either $x$ or $3x$. Dividing the resulting count by $\log_2 X$ gives a lower limit at least half the size of this finite set. [Single-witness count](EVENTUAL_FIVE_RAY.md#lifting-a-failed-multiplication-by-three)

If Collatz is false, the preceding theorem gives infinitely many distinct odd $x$ with $f(3x)\ne f(x)$, proving $B(X)/\log X\to\infty$. To apply the criterion toward full convergence, it would suffice to bound this ratio along infinitely many cutoffs or separately prove eventual invariance under multiplication by three.

# Multiplication by three determines the whole conjecture

**PROPOSED, unconditional.** For the positive shortcut Collatz map $T$ write $f(n)$ for the component of $n$ under eventual meeting at independent clocks. Then
$$
 \bigl(\forall n\ge1,\ n\text{ reaches }1\bigr)
 \quad\Longleftrightarrow\quad
 \bigl(\forall n\ge1,\ f(3n)=f(n)\bigr).
$$
Moreover, if Collatz is false, the number $B(X)$ of parameters $t\le X$ for which $t$ and $5t+1$ never meet satisfies $B(X)/\log X\to\infty$. Thus even $B(X)=O(\log X)$ along an unbounded sequence of cutoffs would suffice for full convergence. No such upper bound is proved here.

## From exact multiplication by three to descent

Write $g(y)=f(y-1)$ for $y\ge2$. Assume $f(3n)=f(n)$ for every $n$. We always have $f(2n)=f(n)$. The ordinary paths $T(2h-1)=3h-1$ and $T(3(8h-1))=4(9h-1)$ give $g(2h)=g(3h)$ and $g(8h)=g(9h)$. Consequently $g(4h)=g(6h)=g(9h)=g(8h)$. By doubling and then exchanging factors of two for factors of three,
$$
 g(4h)=g(2^i3^j h) \qquad(i+j\ge2).
$$

We use one finite synchronization input proved constructively in this packet. In every binary residue class for $y$ there is a subclass on which the pair $(y-1,y)$ meets for every positive lift. The statement permits any initially prescribed class. [Arbitrary-state extension for a fixed gap](PREFIX_COMPRESSION.md#extending-any-already-prescribed-pair-of-paths)

For fixed $h=2^v u$ with $u$ odd, the values $3^j h$ attain every residue congruent to $h$ modulo $2^{v+3}$ at every higher binary precision. Indeed powers of 9 run through the $1\bmod8$ units modulo $2^m$ since $v_2(9^{2^a}-1)=a+3$. Each represented residue occurs at arbitrarily large $j$. Apply synchronization in this initial class and choose $j\ge2$ with $y=3^j h$ in its successful subclass. It follows that
$$
 f(4h-1)=g(4h)=g(y)=f(y)=f(h).
$$

Strong induction now settles all starts under the assumption. Evens halve and odds $n>1$ congruent to 1 modulo 4 reach $(3n+1)/4<n$ in two steps. For $n=4h-1$ the displayed equality gives the smaller component representative $h$. The component of 1 consists precisely of starts that visit its cycle. Conversely full convergence makes the component label constant.

## If failures on the five-ray grow only logarithmically along a subsequence

Suppose $B(X)/\log X$ has finite lower limit. First, only finitely many *odd* $x$ can have $f(3x)\ne f(x)$. For each such $x$ and every $a\ge2$, at least one of $2^a x,3\cdot2^{a-2}x$ is a five-ray failure, by $T^2(20u+1)=15u+1$. Across any fixed finite set of odd $x$ and all $a$, a parameter is counted at most twice: its odd part is either $x$ or $3x$. Dividing the resulting count by $\log_2 X$ gives a lower limit at least half the size of this finite set. [Single-witness count](EVENTUAL_FIVE_RAY.md#lifting-a-failed-multiplication-by-three)

For every $x$, the sequence $f(3^j x)$ is therefore eventually constant. Write $F(x)$ for that eventual label. We have $F(2x)=F(3x)=F(x)$. Also $F$ and $f$ differ on at most finitely many odd parts: if $f(x)\ne F(x)$, some $3^j x$ has an odd part in the finite failure set, so the odd part of $x$ divides an element of that set.

In fact $F(5x)=F(x)$ everywhere. Otherwise strip off powers of two and take an odd witness $x$. For $t=4^i3^j x$, $f(t)=F(x)$ whenever $j$ is large. The two-step identity gives $f(5t+1)=f(5\cdot3^{i+j}x+1)=f(5\cdot3^{i+j-1}x)=F(5x)$ when $i+j$ is large, using an odd input in the middle equality. Independent choices in $i,j$ yield $B(X)\gg_x(\log X)^2$, contradicting the finite lower limit.

For all sufficiently large $h$, the two $g$ relations used above still give $g(4h)=g(8h)$, since $f(3(8h-1))=f(8h-1)$ for every sufficiently large odd input $8h-1$. For each such $h$, $g(4h)=g(3^j h)$ for every $j\ge2$, by doubling at $h,2h,\ldots$ and swapping twos for threes. Use the same binary synchronization subclass at an arbitrarily large $j$ and obtain $g(4h)=F(h)$.

This implies $f(x)=F(x)$ for **every** $x$ prime to three, even at small $x$. Take arbitrarily large $a$ with $2^a x\equiv1\pmod3$. Then $w=(2^a x-1)/3$ is large, positive and odd, so $f(3w)=f(w)=f(2^{a-1}x)=f(x)$. But $f(3w)=g(2^a x)=F(2^{a-2}x)=F(x)$ by the preceding paragraph.

## Eliminating the last possible exceptional odd part

If $f$ ever differs from $F$, let $x$ be the largest odd integer on which they differ. Then $3\mid x$. Write $H(y)=F(y+1)$. Three comparisons apply above $x$:
$$
 H(4h)=H(3h),\quad H(10h)=H(9h),\quad H(16h)=H(15h)
$$
when $4h+1>x$, $10h+1>x$, $16h+1>x$, respectively. For the first, apply $T^2(4h+1)=3h+1$. For the next two, start at the odd integers $3(10h+1)$ and $5(16h+1)$, and use $3[3(10h+1)]+1=10(9h+1)$ and $3[5(16h+1)]+1=16(15h+1)$. The left odd inputs exceed $x$, so their $f$ and $F$ agree. The right endpoints, including the displayed multipliers 10 and 16, are prime to three, so their $f$ and $F$ also agree. The multipliers 2, 3 and 5 may then be removed from $F$.

For $9s>x$, these identities in order connect the arguments
$$
 9s,\quad12s,\quad16s,\quad15s,\quad20s,\quad18s
$$
without changing $H$. Thus $H(y)=H(2y)$ whenever $9\mid y$ and $y>x$. In particular $H(3x)=H(4^i3x)$ for every $i\ge0$. Both $4^i3x+1$ and $3^{i+1}x+1$ are units modulo three and the first reaches the second in $2i$ steps. Consequently
$$
 f(x)=f(3x+1)=H(3x)=H(3^{i+1}x)=f(3^i x)=F(x)
$$
for all large $i$, where $3^i x$ is odd. This contradicts the choice of $x$. Hence $f=F$ everywhere, multiplication by three preserves every component, and the first theorem gives full convergence.

The conclusion leaves a quantitative problem about actual permanent failures. To use this criterion one must provide an upper bound on $B(X)$ along infinitely many cutoffs or separately show exact invariance under multiplication by three.

# Every failed multiplication by three forces a larger failure

**PROPOSED, unconditional.** Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Write $f(n)$ for its component under eventual meeting at independent finite clocks. Call an odd positive integer $x$ a defect if $f(x)\ne f(3x)$. Every defect forces a further defect in $(x,27x]$. The proof gives a finite list of possible successors for each $x$.

Consequently, if Collatz is false and $B(N)$ counts the positive integers $t\le N$ for which $t$ and $5t+1$ never meet, then
$$
 \liminf_{N\to\infty}\frac{B(N)}{(\log N)^2}
 \ \ge\ \frac{1}{2\log 2\,\log 32}.
$$
Logs in this statement are natural. The implication for full convergence uses the result in this packet that global equality $f(x)=f(3x)$ implies full Collatz convergence. [Multiplication by three and descent](THREE_RAY.md#from-exact-multiplication-by-three-to-descent)

## When three divides the defect

Write $J(y)=f(y+1)$. For every positive $s$, the ordinary identity $T^2(4u+1)=3u+1$, used at $u=3s,4s$, gives
$$
 J(9s)=J(12s)=J(16s).
$$
If $16s+1$ is free of defects, then $f(16s+1)=f(48s+3)$. Two ordinary steps send $48s+3$ to $72s+5$ and then to $108s+8=4(27s+2)$. Also $T(18s+1)=27s+2$. Hence $J(9s)=J(18s)$ whenever $16s+1$ is free of defects.

Suppose $x$ is odd and $3\mid x$. Set $y=3x$. If $16x/3+1$ and $32x/3+1$ are both free of defects, the comparison at $s=x/3$ and $s=2x/3$ gives $J(y)=J(2y)=J(4y)$. One more ordinary two-step identity gives $J(4y)=J(3y)$. Since $x$ and $3x$ are odd, $f(x)=J(3x)$ and $f(3x)=J(9x)$. Thus $f(x)=f(3x)$. In particular, a defect at $x$ forces one at
$$
 \frac{16x}{3}+1 \quad\text{or}\quad \frac{32x}{3}+1.
$$
Both are odd and in $(x,11x]$, since $x\ge3$.

## When three does not divide the defect

The integer $1$ is free of defects because $3\to5\to8\to4\to2\to1$. Take odd $x>1$ prime to three. Choose $L\in\{2,3\}$ with $2^Lx\equiv1\pmod3$ and put $z=(2^Lx-1)/3$. Then $z$ is odd, $x<z<3x$, and $T(z)=2^{L-1}x$. Set $g(y)=f(y-1)$ for $y\ge2$. If $z$ is free of defects then
$$
 f(x)=f(z)=f(3z)=g(2^L x)=g(3^L x).
$$
The last step repeatedly uses the unconditional equality $g(2u)=g(3u)$ from $T(2u-1)=3u-1$.

For any $Q\ge1$, $g(4Q)=g(9Q)$ by this same equality. If $8Q-1$ is free of defects, then $g(8Q)=g(9Q)$ because $T(3(8Q-1))=4(9Q-1)$. Also $g(8Q)=g(27Q)$ by three unconditional exchanges. Thus $g(9Q)=g(27Q)$ whenever $8Q-1$ is free of defects. Using $Q=x,3x$ shows
$$
 g(3^2x)=g(3^3x)=g(3^4x)
$$
provided $8x-1,24x-1$ are free of defects.

First take $x\equiv1\pmod{16}$ and write $x=16m+1$. The two starts $6x-1=96m+5$ and $6x=96m+6$ both reach $27m+2$ after five steps. Because $g(9x)=g(6x)$ by an unconditional exchange, we get $f(x)=g(6x)=f(6x)=f(3x)$.

For every other odd residue of $x$ modulo 16, some $j\in\{2,3,4\}$ gives $Y=3^j x\equiv3\pmod{16}$ or $Y\equiv5\pmod8$. Indeed, on the coset $\{5,7,13,15\}$, multiplication by three alternates between 5 and 7 modulo 8. On the subgroup $\{1,3,9,11\}$ the preimages of 3 under $3^2,3^3,3^4$ are $11,9,3$, respectively. In the successful classes $f(Y-1)=f(Y)$ by exact ordinary paths. For $Y=16m+3$, the paths from $16m+2$ and $16m+3$ both reach $9m+2$ after four steps. For $Y=8m+5$, the paths from $8m+4$ and $8m+5$ both reach $3m+2$ after three steps. These formulas hold for every $m\ge0$.

It follows that $f(x)=g(Y)=f(Y)$. If $3x,9x,27x$ are also free of defects, the equalities $f(3^a x)=f(3^{a+1}x)$ for $1\le a<j$ identify $f(Y)$ with $f(3x)$. In particular, a defect at $x$ forces one at a member of the list
$$
 z,\quad 8x-1,\quad24x-1,\quad3x,\quad9x,\quad27x.
$$
Every member is odd and lies in $(x,27x]$.

## Counting distinct five-ray failures

If Collatz is false, the cited descent theorem supplies a defect $x_0$, since $f(2u)=f(u)$ permits stripping every power of two. Iterating the local result gives odd defects $x_i$ with
$$
 x_i<x_{i+1}\le27x_i,\qquad x_i\le27^i x_0.
$$
In particular, for every real $R\ge x_0$, the least $x_i>R$ lies in $(R,27R]$.

To give the pairs used in the count distinct parameters, retain the first defect in the chain and thereafter the first successor strictly greater than three times the last retained defect. Denote successive retained defects by $w,w'$. Then
$$
 3w<w'\le32w+1.
$$
Here the local successor at each step may be chosen from just those inputs used by its residue class in the proof. If $w'$ immediately follows $w$, it is at most $27w$. Otherwise let $t$ directly precede $w'$ in the original chain, so $w<t\le3w$. If $3\mid t$, the multiple-of-three rule gives $w'\le32t/3+1\le32w+1$. If $3\nmid t$, the only way it could have been reached without passing $3w$ was as $z=(2^L u-1)/3$ from an earlier defect $u\ge w$. Every other successor in the two lists either exceeds $3w$ or is a multiple of three. Since $u$ is odd, $z$ is 1 or 9 modulo 16 for $L=2$, and 13 modulo 16 for $L=3$. At residue 1 the proof uses $g(6t)$, at residue 9 it uses $j=3$, and at residue 13 it uses $j=2$. In each of these three cases only $z,8t-1,3t,9t$ can be needed as successor candidates, with $z$ now computed from $t$. Thus $w'\le9t\le27w$ in this last case. Writing the retained sequence as $w_0,w_1,\ldots$, the displayed recurrence yields $w_i\le32^i(w_0+1/31)$.

For every retained defect $w$ and integer $a\ge2$, at least one of $t=2^a w$ and $t'=3\cdot2^{a-2}w$ contributes to $B$. Their own component labels are $f(w)$ and $f(3w)$, whereas $T^2(5t+1)=5t'+1$. Also $t'<t$. Every comparison has two parameters distinct from those of every other comparison. Indeed their odd parts belong to $\{w,3w\}$, and these sets are disjoint for distinct retained $w$ by the strict factor-three separation. For fixed $w$, the odd part determines which of the two positions a parameter occupies and its binary valuation then determines $a$.

Put $A=\log(N/(w_0+1/31))$, $b=\log32$ and $k=\lfloor A/b\rfloor$ for $N\ge w_0+1/31$. Using the upper bound on $w_i$ to count the allowable $a$ gives
$$
 B(N)\ \ge\ \sum_{i=0}^k
 \max\!\left(0,\left\lfloor\log_2\frac{N}{32^i(w_0+1/31)}\right\rfloor-1\right)
 \ \ge\ \frac{A^2}{2b\log 2}-O(A+1).
$$
Indeed the summands before rounding are $(A-ib)/\log2$, whose sum is $A^2/(2b\log2)+O(A+1)$. This proves the lower limit. A counterexample consequently requires permanent five-ray failures on this scale. Proving an upper bound below the stated lower limit along an unbounded sequence of cutoffs remains open.

## What a successful interval certifies below it

The propagation proof works for **any** labeling constant along ordinary shortcut steps. Thus, after identifying the actual components joined by the tripling pairs with odd parameters in $(R,27R]$, every odd tripling edge at a parameter $x\le R$ also has equal labels. Otherwise its increasing path of failures would cross the proposed interval. This is a statement about the finite list of comparisons identified, even if they join different true components.

In particular, if every tripling pair in the interval really meets, all the smaller tripling pairs meet. At the finite scale, every $n\le M$ then reaches 1 provided $81\lfloor(M+1)/4\rfloor\le R$. To see the bound, write any start requiring descent as $4h-1$, with $h\le (M+1)/4$. For even $h=2q$, the single test at $8q-1$ suffices for $f(8q-1)=f(4q-1)$, a strict reduction. For odd $h$, pass from $g(4h)=g(9h)$ to $g(3^jh)$ for some $2\le j\le5$ for which $3^jh$ equals 3 or 5 modulo 16. This needs only the odd tests at $8h-1,24h-1,72h-1$. The adjacent-word identity and the tests at $h,3h,9h,27h,81h$ then give $f(4h-1)=f(h)$. Evens halve and the $1\bmod4$ odds above 1 descend in two steps. Strong induction gives the asserted finite guarantee.

More generally, any $k$ distinct true components must be joined by at least $k-1$ failed tripling edges in $(R,27R]$ for every sufficiently large $R$. Here “joined” allows intermediate components. Indeed the graph obtained by adding **all** tripling edges to ordinary components is connected, since its component labeling has tripling invariance and therefore the same descent to 1 as above. Fix finitely many connecting paths for representatives of the $k$ components in this graph. Take $R$ beyond every odd part of a tripling parameter on those paths. The interval identifications already connect all these representatives, by the first paragraph. A finite graph that connects $k$ distinct vertices needs at least $k-1$ edges between distinct vertices. In particular, infinitely many components would force the number of failed odd tripling pairs in these fixed-ratio intervals to tend to infinity.

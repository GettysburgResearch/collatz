# How many ternary depths permit a small excess?

**PROPOSED.** Use the positive shortcut map and the meeting convention of the [checkpoint theorem](NEGATIVE_FIVE_CHECKPOINT.md). Call a depth $A\ge1$ exceptional at tolerance $E$ if there exist $k\ge1$, $3^A\mid n$, $8^k\mid n+5$, and $0<m<n$ with $T^j(m)=T^i(n)$, $0\le i\le3k$, and $s_j(m)-s_i(n)\le A+E$. No bound is imposed on $j$, and all witnesses may vary with $A$.

There exist absolute constants $a,d,C>0$ such that, in **any interval of $N$ consecutive positive integers**, at most $CN/(\log N)^d$ depths are exceptional at tolerance $\lfloor a\log\log N\rfloor$ for sufficiently large $N$. With the classical two-logarithm theorem of Baker and Wüstholz, the same argument gives the stronger bounds **tolerance $\lfloor a'\log N\rfloor$ and at most $C'N^{1-d'}$ exceptional depths**, for absolute positive constants. Thus the estimate controls the excess uniformly as the interval and the tolerance grow. Throughout the note $\log$ denotes the natural logarithm.

## The possible signed endpoints occupy little space

Let $M$ be a signed magnitude in the checkpoint suffix, so that the positive map $S(x)=x/2$ on even inputs and $(3x-1)/2$ on odd inputs takes $M$ to 5 in $3k+b$ steps with $2k$ odd inputs, $b\ge0$. Put $y=5-M/2^b$. Only $y\in[0,5]$ is needed. Let $K$ be the closure of all these $y$ in $[0,5]$. There exists an absolute $\eta>0$ such that the ordinary length of its $\delta$-neighborhood satisfies

$$
 |K_\delta|\ll\delta^\eta\qquad(0<\delta<1/2). \tag{1}
$$

Stop the path at its first hit of 5. The removed part consists of whole periods $5,7,10$, so the remaining odd count $h$ is even and the remaining length is $l=b+3h/2$. No input before this first hit is below 5. Each transient odd input is at least 9 except possibly 7, whose next two steps lead directly to 5. Telescoping the step ratios gives
$$
 \frac{2^l5}{M}=\prod_{x\ {\rm odd}}(3-1/x).
$$
For $x\ge9$ each factor is at least $26/9$ and for $x=7$ it exceeds $\sqrt8$. Consequently $M/2^b\le5\theta^{-(h-1)}$ for $h\ge1$, with $\theta=26/(9\sqrt8)>1$. Because $h$ is even, every nonzero $h$ gives $y\ge y_*=5(1-1/\theta)>0$. When $h=0$ the path consists entirely of halvings and $y=0$.

For odd inputs at positions $0\le t_1<\dots<t_h<l$, the affine formula for $S$ gives
$$
 \frac{M}{2^b}
 =\left(\frac{\sqrt8}{3}\right)^h
   \left(5+\sum_{j=1}^h 3^{h-j}2^{-(l-t_j)}\right). \tag{2}
$$
This also holds at $h=0$ with the sum empty. Take $s=\lceil\log_2(1/\delta)\rceil$, $H=\lfloor s/16\rfloor$ and $D=2s$. The tail $h>H$ lies in one interval of length $O(\theta^{-H})$ next to 5 in the $y$ coordinate. For $h\le H$, discard the terms with $l-t_j>D$ in (2). Their combined size is at most $3^H2^{-D}\le\delta$. They form an initial segment, and the retained coefficients are precisely $3^{r-1},\ldots,1$ for a retained length $r$. Thus $h$ and a subset of $\{1,\ldots,D\}$ of cardinality at most $H$ determine the truncated value. For large $s$ the number of centers needed is at most
$$
 (H+1)\sum_{r=0}^H\binom{D}{r}
 \ \le\ (H+1)^2(eD/H)^H\ \le\ 2^{s/2}.
$$
The last inequality follows from $\log_2(32e)/16<1/2$. The $\delta$-neighborhood is therefore covered by intervals of total length $O(\delta^{1/2}+\theta^{-H})$, including after closure. This proves (1), for example with $\eta=(\log_2\theta)/16$.

## A uniform bound on the moving phase

Set $U=(3/2)^E$. The checkpoint theorem gives $s_j(m)-s_i(n)=A+e$ with $1\le e\le E$. Its ordinary witness construction supplies a positive start $\beta<5U$, a clock $J$ with $s_J(\beta)=A$, and a suffix parameter $b$ such that
$$
 c=T^J(\beta)=5\cdot2^b-M,\quad
 g=3^A/2^J,\quad \alpha=2^b/g<U.
$$
In particular $y=c/2^b\in K$. Write $D_A(\beta)=c/g$. This quantity is determined by $A$ and $\beta$ alone. An even step leaves it unchanged and each odd step from $x$ multiplies it by $1+1/(3x)$. Every positive orbit has infinitely many odd steps, since repeated divisions by two from a positive integer eventually reach an odd input. Hence for fixed $\beta$, $D_A(\beta)$ is defined for all $A$, is nondecreasing, and starts at $D_0=\beta$. At every exceptional witness,
$$
 1\le\beta\le D_A(\beta)=\alpha y<5U,\qquad y>1/U. \tag{3}
$$
In particular $w_A=\min\{\log_2 D_A(\beta),\log_2(5U)\}$ is monotone with total variation $O(E+1)$ and equals $\log_2D_A(\beta)$ at these witnesses. This controls periodic and divergent trajectories in the same way.

Let $F$ be the image of $K\cap[y_*,5]$ under $y\mapsto\log_2 y\pmod1$. From $c=gD_A$ we obtain the necessary circle condition
$$
 A\log_2 3+w_A\pmod1\ \in F. \tag{4}
$$
A circle neighborhood of $F$ of radius $\delta$ has length $O(\delta^\eta)$. Indeed the corresponding real logarithms are the logarithms of positive numbers within $C\delta$ of $K$ and at least $y_*/2$, for an absolute $C$ and small $\delta$. The logarithm on that range has bounded derivative, and projection modulo one can only reduce measure. By (1), one can cover the $\delta$-neighborhood of $F$ by $O(1/\delta)$ arcs on a regular grid whose total length is $O(\delta^\eta)$, by enclosing it in a slightly larger neighborhood.

## Counting the exceptional depths

For any interval of $L$ consecutive integers and any circle arc $I$, the Erdős–Turán discrepancy inequality and the finite geometric sum give, for $R\ge2$,
$$
 \left|\#\{A:A\log_2 3\bmod1\in I\}-L|I|\right|
 \ll L/R+B(R),\qquad
 B(R)=\sum_{q=1}^R\frac{1}{q\,\|q\log_2 3\|}.
$$
Here $\|x\|$ is the distance to the nearest integer. The bound is uniform in the location of each interval and arc. If $p$ is nearest to $q\log_2 3$, the distinct integers $2^p,3^q$ differ by at least one. Integrating $1/x$ between them gives $\|q\log_2 3\|\gg 3^{-q}$ and $B(R)\ll3^R$. Take $R=\lfloor(\log N)/(4\log3)\rfloor$, so that $B(R)\ll N^{1/4}$.

For each possible $\beta$, partition the depth interval according to the grid bins of width $\delta$ containing $w_A$. Monotonicity and (3) give $O((E+1)/\delta)$ contiguous pieces. On each piece translate $F$ by the negative of the left endpoint of its occupied phase bin and enlarge by $\delta$ to impose (4). Sum the arc discrepancy estimate over the pieces and at most $5U$ seeds. Dividing by $N$ bounds the exceptional fraction by
$$
 O\left(U\delta^\eta+\frac{U}{R\delta}
       +\frac{U(E+1)B(R)}{N\delta^2}\right). \tag{5}
$$
Choose $\delta=R^{-1/2}$ and $E\le\eta\log R/(8\log(3/2))$. Then $U\le R^{\eta/8}$, and (5) is $O(R^{-\eta/4})$. This proves the elementary estimate.

For the stronger version, the theorem on linear forms in logarithms applied to $q\log3-p\log2\ne0$ gives $\|q\log_2 3\|\gg q^{-B}$ for an absolute effective $B\ge1$, since $p=O(q)$. Hence $B(R)\ll R^{B+1}$. Take $R=\lfloor N^{1/(4(B+1))}\rfloor$ in (5) and use the same $\delta$ and tolerance choice. Again $B(R)\ll N^{1/4}$, and $R^{-\eta/4}$ is now a negative power of $N$. This is the only use of the two-logarithm theorem. [Baker and Wüstholz, *Logarithmic forms and group varieties*, 1993](https://doi.org/10.1515/crll.1993.442.19)

Both conclusions leave individual exceptional depths undecided. Their quantifier concerns the divisibility depths $A$, and a single ordinary start can satisfy divisibility conditions at more than one depth.

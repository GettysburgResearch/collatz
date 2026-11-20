# Smaller tripling comparisons and their necessary clocks

**PROPOSED, unconditional.** Let $T(x)=x/2$ on even inputs and $T(x)=(3x+1)/2$ on odds. Write $f(x)$ for the eventual-merger component at independent clocks, and $P(n)$ for $f(n)=f(3n)$. Universal $P$ is equivalent to full Collatz by the [three-ray theorem](THREE_RAY.md).

## Every parameter congruent to seven modulo eight reduces

For each positive $n\equiv7\pmod8$, the hypotheses $P(t)$ for $1\le t<n$ imply $P(n)$. Consequently a least failure of the three-ray comparison must be odd and congruent to $1,3$ or $5\pmod8$. Even failures reduce by halving both arms.

The following seven pairs of words prove the implication for all parameters in their indicated classes. In each row write $n=r+mu$ with $u\ge0$. The first word starts at $n$ and the second starts at $3n$. Read letters from left to right.

| $r$ | $m$ | From $n$ | From $3n$ | Common final value |
|---:|---:|---|---|---:|
| 7 | 72 | DIVOOE | OEEIIVOD | $36u+4$ |
| 23 | 24 | IMO | OEEIDD | $72u+68$ |
| 23 | 32 | OOOE | OEEEOD | $54u+40$ |
| 31 | 72 | DIIMOE | OEEIDDI | $144u+61$ |
| 15 | 48 | VOEEIMO | OEEIIMOEEI | $18u+5$ |
| 39 | 96 | VOEEIM | OEEEEIDI | $24u+9$ |
| 55 | 72 | ODDIIVOEO | OEEIIVODD | $72u+56$ |

$D$ doubles and $I$ takes the positive odd preimage $(2x-1)/3$. $E$ and $O$ perform ordinary even and odd shortcut steps. All four preserve $f$. $M$ triples its input and $V$ divides by three. For these two letters the smaller endpoint $t$ is strictly below $n$, so the applicable hypothesis $P(t)$ preserves $f$.

For example at $n\equiv23\pmod{24}$ the left arm takes the odd preimage $(2n-1)/3$, triples this smaller input, and takes an odd step to $3n-1$. The right arm takes three steps to $(9n+1)/8$, takes an odd preimage and doubles twice to reach the same $3n-1$.

The table can be verified using just pairs of integer coefficients. Propagate $a u+b$ on each arm. At $I$ check that both coefficients of $2(au+b)-1$ divide by three and the result is odd. At $E,O$ check the input parity for every $u$ using the slope and intercept. At $M,V$ check that the smaller endpoint $a'u+b'$ has $0<a'\le m$ and $0<b'<r$. Every intermediate has positive intercept and slope. These checks establish each row even at $u=0$. The row moduli divide 288, and the displayed classes cover all 36 residues $7\pmod8$ in that period. [Exact certificate verifier](check_three_smaller.py)

## A finite range of tripling comparisons suffices for a finite range of convergence

For each $h\ge1$, the assumptions $P(t)$ for all $1\le t\le81h$ imply $f(4h-1)=f(h)$. Hence, for integer $X\ge3$, $P(t)$ through $81\lfloor(X+1)/4\rfloor$ implies that every start up to $X$ reaches 1.

Put $g(y)=f(y-1)$ for $y\ge2$. The orbit identity $T(2s-1)=3s-1$ always gives $g(2s)=g(3s)$. Also $T(3(8s-1))=4(9s-1)$, so $P(8s-1)$ gives $g(8s)=g(9s)=g(6s)=g(4s)$. First take $h$ odd. At clock four the pairs $(y-1,y)$ with $y\equiv3,5,13\pmod{16}$ have a common endpoint and the same odd count. At the respective base values the profiles (endpoint, odd count) are $(2,2),(1,1),(8,2)$. Adding $16u$ to a start adds $3^q u$ to its endpoint for the same four-step word of odd count $q$.

For $h\equiv1,3,5,7,9,11,13,15\pmod{16}$ choose $j=5,4,2,3,3,2,2,3$, respectively. Then $y=3^jh$ is in one of the three successful classes. Repeatedly use $g(4s)=g(8s)$ to obtain $g(4h)=g(2^j h)$, at tripling inputs no larger than $2^j h-1\le32h-1$. Exchange all the factors of 2 for factors of 3 to reach $g(y)$. The successful adjacent pair gives $g(y)=f(y)$, and $P(h),\ldots,P(3^{j-1}h)$ give $f(y)=f(h)$ with all these indices at most $81h$.

For even $h=2^v w$ with $w$ odd, connect $g(4h)$ to $g(4w)$ by the same doubling identity at indices no larger than $4h-1$, and use $f(w)=f(h)$. The finite convergence claim now follows by strong induction. Evens halve, odds $n>1$ congruent to 1 modulo 4 descend after two steps, and for $n=4h-1$ the equality just proved gives the smaller representative $h$.

## A universal bound on the number of ordinary steps is impossible

Consider an undirected proof graph on positive integers for one parameter $n$. It has every ordinary edge $x\leftrightarrow T(x)$ and all extra edges $t\leftrightarrow3t$ for $1\le t<n$. A path from $3n$ to $n$ in this graph is a sufficient certificate for the inductive implication. For arbitrarily large $n$, any such path, if it exists, needs at least $\log_6 n$ ordinary edges before its first extra edge or before reaching $n$. There is no restriction on the number of extra edges that might subsequently be used.

Here is the signed fixed-point bound behind the obstruction. Suppose $2^i\mid X+1$ and $3^A\mid X$, with $X>0$. If $0<z<X$ meets $T^i(X)$ after $L$ steps from $z$, its odd count exceeds $i+A$. Write $X=2^i t-1$ so $T^i(X)=3^it-1=Y$. The first $i$ inputs from $X$ are odd. The signed fixed point $-1$ supplies the same parity word.

For any path ending at $Y$ with $q\le i$ odds, length $l$, and starting value $w$, reverse the same word also from $-1$. Its difference from the ordinary endpoint starts at $3^i t$, doubles at an even inverse and is multiplied by $2/3$ at an odd inverse. A factor of three is available at each required division. Each signed inverse is integral and stays at most $-1$. Calling the resulting start $-M$, we have $M\ge1$ and $w+M=2^l3^{i-q}t$. Along the signed path the magnitude of an odd input cannot decrease, since $(3x-1)/2\ge x$ for $x\ge1$. Each even step halves the magnitude. Thus $2^l\ge M2^q$, giving
$$
 w+M\ge M(3/2)^{i-q}(X+1),\qquad w\ge X.
$$
For $q=i$ one has $l=i+b$ with $b\ge0$ and $w=2^bX+c$, $c=2^b-M\ge0$.

It remains to consider an alleged path from $z<X$ with $i+d$ odds, $1\le d\le A$. Split it just after the first $d$ odds, at time $J$ and state $w$. The suffix gives the last formula. Reverse the initial word from both $w$ and $c$; its endpoint difference $2^bX$ is divisible by $3^d$, giving integral inverses throughout. Starting this inverse from $c=0$ would fail at the first odd inverse, so $c>0$ and the resulting ordinary start $\beta$ is positive. Then $z=\alpha X+\beta$ with $\alpha=2^{J+b}/3^d<1$. Over the rationals reverse the same initial word from $-M$. Its output is $\beta-\alpha$ because $c+M=2^b$. The inverse maps $y\mapsto2y$ and $y\mapsto(2y-1)/3$ both preserve $y\le-1$, which contradicts $\beta-\alpha>0$. This proves the fixed-point bound, also for an empty ordinary prefix $i=0$.

For any $H\ge1$, take the least positive $n$ satisfying $3^H\mid n$ and $3n\equiv-1\pmod{2^H}$. The Chinese remainder theorem gives $3^H\le n\le6^H$. Any ordinary walk of length at most $H$ from $X=3n$ to a smaller $z$ would give a meeting $T^i(X)=T^L(z)$ at clocks at most $H$. Indeed, delete each backward step followed by a forward step, which returns to the same vertex. What remains goes forward then backward. The fixed-point bound with $A=H$ rules out this meeting, since $z$ has at most $H$ odd inputs. Both endpoints of every smaller tripling edge lie below $3n$. The same holds for the destination $n$. Thus the ordinary portion before the first such edge or before the destination must exceed $H$ steps.

For each fixed $H$, the obstructing residue class even contains infinitely many $n$ for which $n$ and $3n$ both reach 1. In the class $n=r+6^H v$, the two slopes $6^H,3\cdot6^H$ differ by three. The [affine synchronization theorem](AFFINE_RAYS.md#classification-and-a-constructive-bound) supplies a binary subclass of $v$ with a common endpoint at fixed clocks. Its slope in the remaining free parameter is a power of three, upon using the normalization in that proof; extra fixed binary digits could instead contribute a power of two. One may take a further common shortcut word to remove any such binary factor. The intercept is prime to three since both starts are odd and each forward odd step yields a ternary unit. If necessary extend both clocks after the merger to include an odd step. The powers of two generate the units modulo every power of three, so infinitely many sufficiently large powers of two occur as these common endpoints. The obstruction limits the number of ordinary steps that a proof by smaller comparisons may require. It leaves open comparisons with clocks adapted to the individual parameter.

The [checker](check_three_smaller.py) verifies the seven affine certificates and the four-step adjacent profiles. Separately it enumerates all bounded inverse paths at two members of each obstructing class through $H=12$. The unbounded clock lower bound follows from the argument above.

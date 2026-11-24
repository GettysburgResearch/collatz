# Odd steps after a shared prefix and the sizes of moving marks

**PROPOSED written results. The universal directed transfer remains open.**
PR193 at cc800b9041efdeee43bb89df21088a81e1f44a74 studies simultaneous
ordinary endpoints of $x,9x+2$, including the directed question for
$x=9k+2$. We tried to use its diagonal first landings and its source-preserving
return to supply the successful child certificate in [the fixed-source
argument](README.md). The arithmetic estimate extends to both unequal marks
and unknown moving targets, independently of whether either mark reaches 1.

## Size of a moving target after boundedly many odd letters

Fix $n>0$, write $x_r=T^r n$, and let $P=P_r$ be the number of odd inputs
before $r$. Consider any positive ordinary lift $m=n+2^r k$ with $k$
positive odd. The two inputs share exactly $r$ native parity bits. Suppose
that after this prefix a segment of length $t\ge0$ from the lift reaches
a positive integer $Z$ with $q\le Q$ odd inputs. For every fixed
$0<\epsilon<1$ and all $r$ after the first odd input of $n$,
\[
                k^\epsilon Z x_r \ \ge\
                    c_{Q,\epsilon}\,3^{(1-\epsilon)P}.               \tag{1}
\]
The constant is independent of $Z,n,r,k,t$ for the indicated $r$.
The first odd input exists by positivity, and all subsequent physical states
are units modulo 3.

At the end of the shared prefix the lifted state is $x_r+3^P k$. Clearing
the following segment, with odd positions $d_0<\cdots<d_{q-1}$ numbered
from zero, gives
\[
  2^t Z-k3^{P+q}-3^q x_r-\sum_{i<q}2^{d_i}3^{q-1-i}=0.
\]
No proper nonempty subsum vanishes. The leading term is the only positive
one. The maximum entry in absolute value is $2^t Z\ge k3^P$. Let $g$
be the gcd of all entries. When $q\ge1$, the last carry term is a pure
power of two, and $k3^{P+q}$ is odd, so $g=1$.
When $q=0$, the three entries have odd gcd coprime to 3 because $k$ is odd
and $3\nmid x_r$. Consequently $g\mid Z,k,x_r$ and the product of their
parts outside $\{2,3\}$, after division of each entry by $g$, is at most
$Zkx_r/g^3$. This case can genuinely have $g>1$. For example $n=27,r=4$,
$P=3,x_r=k=47$ gives $m=779$. One further even step gives $Z=658$ and
the three entries are $1316,-1269,-47$.

For the primitive tuple Evertse's Corollary 1 bounds that outside product
below by $c_{Q,\epsilon}(k3^P/g)^{1-\epsilon}$. There are only the
dimensions for $q+3$ entries with $0\le q\le Q$, as in the fixed-target
proof. For $q=0$ rearrangement even gains $g^{2+\epsilon}$ on the right
of (1). For $q\ge1$ its factor is one and the outside product is at most
$Zkx_r$. This proves (1).
[Evertse, Corollary 1, printed p. 227, (9)–(12)](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

Take any sequence $r\to\infty$, fixed $n,Q,A$ and $k\le\exp(Ar)$.
Since $P\le r$, taking logs in (1) and then sending $\epsilon$ to zero
gives
\[
 \liminf_{r\to\infty}\frac{\log Z+\log x_r-P\log3}{r}\ \ge 0 .
\]
The ordinary all-source bound $x_r\le\sqrt3\,n\,3^{P-r/2}$ therefore gives
$\liminf(\log Z)/r\ge(\log3)/2$. This constant is sharp. For $n=k=1$
and even $r$ one has $x_r=1$, $P=r/2$ and the lift state
$1+3^{r/2}$. One even step reaches $Z=(1+3^{r/2})/2$, with $q=0$.
In particular, approximating a fixed pair $(x,9x+2)$ with lifts
$x'=x+2^r k$, $k\le e^{Ar}$, and then reaching any two fixed positive
marks after that prefix forces the remaining odd counts on **both**
arms to tend to infinity. Apply (1) separately to the lifts with
quotients $k$ and $9k$. The marks need not belong to a known basin.
For a fixed mark $Z$, a hit before $r$ is itself impossible for large $r$:
$2^h Z\ge m>2^r$ forces $r-h<\log_2 Z$ if $h<r$. Then $T^rm$ is in the
finite list of bounded-step successors of $Z$, whereas $T^rm\ge3^P$
and $P\to\infty$.

## A linear remaining odd count at a hypothetical failure

Fix an actual directed failure $x\in C$, $n=9x+2\notin C$, with
$x=9k_0+2$. Denote the two prefix counts by $P_r,Q_r$ and physical
states by $X_r,Y_r$. Then
$P_r=r/2+O_x(1)$ by the terminal cycle, whereas
$Q_r\ge(3/5)r-O_x(1)$. For the latter, all states of the right arm are
at least 20 by verified convergence below 20. The product formula yields
$2^r\le n(61/20)^{Q_r}$ and $(61/20)^3<2^5$.

For $x'=x+2^r k$ with any $k\ge1$, the two lifted prefix endpoints are
$U=X_r+3^{P_r}k$ and $V=Y_r+9\cdot3^{Q_r}k$. Their ratio is
\[
             V/U=3^{Q_r-P_r}\bigl(9+o_x(1)\bigr)
\]
uniformly in $k$, by the normalized two-clock estimate on each fixed
source. If $t$ further steps reach fixed positive ordered marks $(A,B)$
with remaining odd counts $a,b$ respectively, then
$2^t A\le4^a U$ and $2^t B\ge3^b V$. Consequently
\[
        a\log4-b\log3 \ \ge\ \tfrac1{10}r\log3-O_{x,A,B}(1).
\]
This holds without any upper bound on the lift height. If the two forward
affine maps are identical on a binary cylinder at their common clock, their
slopes give the stronger equality $a-b=2+Q_r-P_r$: the original right
source has slope 9 in the left parameter. Pointwise equality of two
numerical endpoints alone does not imply this latter identity. The
linear bound concerns the letters still required after the two actual
prefixes; PR193's $h\le S_h^2+6S_h+4$ concerns the entire clock and
the sum of both full grades.

## Can the routed diagonal supply those lifts?

PR193 transports the positive common-landing cohort, including its
unconditional lower bound of order $(X/M)^{2/5}$, through $k'=64w+12$.
Thus its left coordinate $x'=9k'+2$ is $46\bmod64$. A failing fixed $x$
cannot be in this cylinder, where the two forward arms coincide at clock
six. For every member of the entire cohort, regardless of the target and
scale, its child's precision against the prescribed child is precisely
\[
                 v_2\big((9x'+2)-(9x+2)\big)=v_2(x-46)\le5 .
\]
The upper part of the diagonal fiber also has the exact child form
$(2^h Z-32)/3$ when $x'=(2^h Z-38)/27$. For any fixed positive child
$n$, its precision against $n$ is exactly $v_2(3n+32)$ whenever
$h>v_2(3n+32)$, uniformly over all positive $Z$ on this branch.

The source-preserving twelve-step inverse return of PR193 does allow the
routed class to move. Even arbitrarily many legal repetitions of this
particular branch do not give unbounded precision. Write
$R(y)=(4096y-146)/81$ and $L=v_2(4015x-146)$, finite at every positive
integer $x$. For all $j\ge0$,
\[
       4015 R^j(y)-146=(4096/81)^j(4015y-146).
\]
If $12j>L$, any positive integral output has precision exactly $L$ against
$x$. If $12j\le L$, sharing $12j+6$ initial bits with a legal $R^j(y)$
from $y\equiv46\bmod64$ would force $x$ itself through the same $j$
twelve-step affine returns followed by the exact six-step merger. Indeed
the common prefix preserves the next input modulo the remaining power
of two, and the two affine forms of each return hold on its full branch
cylinder. This contradicts failure. Thus the precision of **every**
such child is at most $L+5$, independently of the number of inverse
returns and the target choice.

An unbounded collection of different return words could move the center.
The refreshed constructions establish neither cofinally deep lift
precision with the post-prefix controls above nor a power-of-two
congruence of linear-size exponent for the unlifted child. The directed
transfer has not been proved.

## Frozen sources

PR193 at cc800b9041efdeee43bb89df21088a81e1f44a74,
research/astra-pointwise-resolution-20261124/transfer/README.md,
sections “The unique upper part of the diagonal” and “Why this does not yet
transport the marked basin”, and renewal/README.md, §§2–5. The fixed
source's original basin equivalence is PR193 at
67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e, research/astra-global-resolution-20261124/rewriting/SingleReturn.lean.
The positive floor and high prefix bounds used for the linear estimate
are PR182 at 234fd2ece3a17c8950dce452291198705b4e6e60,
research/high-variance-closure-20261124/ordinary-arithmetic/DYADIC_COMPANION.md
and the Lean sources it pins. These addendum results are written
arguments; the existing arithmetic Lean file supplies the paired-clock
estimate in their hypotheses.

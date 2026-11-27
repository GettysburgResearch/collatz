# A constructive cylinder synchronizing a whole block

**PROPOSED elementary written proof.** There are absolute constants
$C,A$ such that, for every $M\ge2$, some odd binary residue $r$ at
a clock $h\le C M^A$ makes the $M$ ordinary arms $x+j$, $0\le j<M$,
have the same physical endpoint and the same odd count at $h$, for
every positive $x\equiv r\pmod{2^h}$. This existence bound is weaker
than the $O(\log^2 M)$ median in [PR146, pinned proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md).
We reconstruct its short compression stage below. Our subsequent
steering is deterministic and does not invoke the pair absorption
tail, the whole-interval synchronization bound, or inverse renewal.

Write $T(y)=y/2$ for even $y$ and $(3y+1)/2$ for odd $y$.
On fixing the first $h$ binary bits, put $x=r+2^h w$, $0\le r<2^h$.
Every arm is $3^{p_j}w+B_j$ with integer $B_j\ge0$ and $p_j$ its
actual count of odd inputs. A new bit fixes $w\bmod 2$ and leaves a
free integer quotient. The odd coefficient permits either parity
of any **one** designated arm. Any equality of affine forms persists
with equal grades through every later bit. Nonnegative auxiliary
representatives, including zero, are used only to define these forms.
Every positive lift follows the indicated ordinary words.

## Compression with a short common clock

Start by setting the first bit to one. More generally maintain an
exact common real center $U$ so the current arms are
$3^{p_j}(w+U)+e_j$, $e_j\ge0$. Initially $U=0$ and $e_j=j$.
When $w=v+2w'$ and an arm sees parity $\epsilon\in\{0,1\}$, the
next center is $(v+U)/2$ and the next error is
$(3^\epsilon e_j+\epsilon)/2$. Keep one representative of each
distinct affine form with its grade. Equal forms have equal errors,
so deleting copies never increases the sum $D=\sum_j\sqrt{e_j}$.
Let $K$ count the retained forms. Given each prefix, a fair new
binary digit gives a fair parity at each arm individually. Hence for
$j$ fresh bits, by $\sqrt{u+v}\le\sqrt u+\sqrt v$ and iteration,
$$
 \mathbb E(D'\mid\text{prefix})\le \rho^jD + C_0 K,\qquad
 \rho=(1+\sqrt3)/(2\sqrt2)<1 .
$$
The sum can first be taken over the old representatives without any
deletions during the block. Independence between arms is unnecessary.
After the forced first bit $K\le M$, $D\ll M^{3/2}$. At a specified
clock $h$, for one grade $p$ the points $3^p U+e_j=B_j$ are distinct
integers for surviving representatives. Thus for any $B\ge1$,
$$
 K\le(h+1)(B+1)+D/\sqrt B .
$$

Here are the constants and iteration needed to reach $K=O(\log M)$.
Set $P=\lceil\log(2M)\rceil$, $a_0=2P$, $a_l=(3/4)^l a_0$. In round
$l$ with $a_l>1$ expose $j_l=\lceil D_0 a_l\rceil$ digits, selecting
a continuation with $D'$ at most the conditional mean. Total clock
is at most $C_{D_0}P$, including rounding. Choose $D_0$ sufficiently
large that $\rho^{j_l}\exp(a_l/3)\le1/2$. At the start of each round
maintain
$$
 K\le C_1 P e^{a_l},\qquad D\le C_2 P e^{4a_l/3}.
$$
These bounds hold initially. With $C_2\ge 2C_0C_1$ the selected
continuation has $D'\le C_2 P e^{a_l}$, the next error budget. Taking
$B=\max(1,(D'/P)^{2/3})$ in the integer packing inequality gives
$$
 K'\le C'_{D_0}\{P+P^{1/3}(D')^{2/3}\}
    \le C'_{D_0}(1+C_2^{2/3})P e^{2a_l/3}.
$$
First fix $D_0$, take $C_2$ a fixed sufficiently large multiple of
$C_1$, and then choose $C_1$ large enough that the last coefficient
is at most $C_1$. This closes the induction since $a_{l+1}=3a_l/4$.
The first $a_l\le1$ leaves $K=O(P)$ at $h=O(P)$.

## A deterministic merger of any two current forms

At clock $h$ orient different grades as $Y=3^sX+d$, with $s>0$ and
$d\in\mathbb Z$ possibly negative. Here $X$ has odd free coefficient,
so each prescribed parity of $X$ can be imposed at the next bit.
When $d$ is odd choose $X$ odd, $Y$ even. The new higher-slope form
has grade difference $s-1$ and disparity $(d-3^{s-1})/2$ in
$Y'=3^{s-1}X'+(d-3^{s-1})/2$.
For even $d$, put $L=\nu_2(3^s-1)$. If $d\ne0$ and
$\nu_2(d)\le L$, choose both even until $d$ becomes odd. Otherwise,
including $d=0$, choose both odd once. The new disparity
$(3d+1-3^s)/2$ has valuation exactly $L-1$. Choose both even another
$L-1$ times. Thus at most $L+1$ bits decrease the grade difference
by one while keeping the physical affine equations exact. For odd
$s$, $L=1$. For even $s$, $L=2+\nu_2(s)$ by factoring the odd
exponent and successive differences of squares. The full sum of
$L+1$ over the drops is at most $4s$ since
$\sum_{j\le s}\nu_2(j)\le s$. The parity setup is a reversal of
the upward steering calculation in [PR192, feasible openings](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-diagonal-closure-20261125/joint/FEASIBLE_OPENINGS.md);
the terminal equal-grade case is essential here.

At equal grades order the arms by endpoint so $Y=X+d$, $d\ge0$.
Stop at $d=0$. If $d>0$ is even, one joint-even step gives $d/2$.
For odd $d$, choose $X$ even, $Y$ odd. Then $Y'=3X'+c$,
$c=(3d+1)/2>0$. Choose both even $v=\nu_2(c)$ times, then choose
the lower-slope arm odd and the higher even. The grades agree
again and the new nonnegative difference is exactly
$$
 d'=\frac{c/2^v-1}{2},\qquad
 2^v(4d'+2)=3d+1 .
$$
For $d'>0$, $4\,2^v d'\le3d-1$, whence
$\log(d/d')\ge v\log 2+\log(4/3)$. This pays the $2+v$ bits.
The final macro with $d'=0$ costs $O(1+\log(d+1))$ since
$2^v=c$. Together with the even halvings this telescopes to
$O(1+\log(d_{\rm initial}+1))$ bits. This argument includes $d=1$,
which merges in three steps.

Initially $s\le h$, so after the grade drops the clock is at most
$5h$. At any clock $H$ the nonnegative endpoints of the canonical
lift $0\le r_H<2^H$ satisfy
$B_j+1\le(3/2)^H(2^H+M+1)$ by direct iteration of $T(y)+1\le
(3/2)(y+1)$. Their equal-grade discrepancy therefore has logarithm
$O(H+\log(2M))$. A merger of one pair increases $h+\log(2M)$
by at most an absolute multiplicative constant. Each merger
removes at least one distinct affine form permanently. Starting
after compression gives at most $O(\log(2M))$ mergers and final
$h\le C M^A$. More explicitly there are absolute constants $D>1,C_3,C_4$ for
which $h_{l+1}+P\le D(h_l+P)$, $h_0+P\le C_3P$, and
the initial survivor count is at most $C_4P$, with
$P=\lceil\log(2M)\rceil$. Hence
$h_{\rm final}\le C_3 P D^{C_4 P}\le C M^A$; one may use
$A=1+C_4\log D$, enlarging $C$ to absorb rounding and the fixed
factor $2^A$. The resulting exponent is absolute and unoptimized.
This proves the stated simultaneous cylinder bound.

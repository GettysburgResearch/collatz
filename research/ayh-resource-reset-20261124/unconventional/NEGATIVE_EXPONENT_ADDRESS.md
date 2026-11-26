# A rational exponent that separates every earlier peak

Let $j=11+162m$, $M_j=2^j-1$, $P_n=3^n-1$, and $T$ be the shortcut map. For every
ordinary $m\ge1$, every $k\ge0$ with $2^k\mid 27m+2$, and **every**
earlier exponent $0\le n<j$, the following two clocks cannot meet:
$$
  T^i(P_j)\ne T^t(P_n)
  \qquad\text{if}\qquad i\le k+3,\quad 3t\le j.                 \tag{1}
$$
The clocks can differ, and $n$ may depend on the source and both clocks.
For $k\ge2$, each such $m$ also fails to be an integer power of
exponent at least two. The progression $27m+2\equiv0\bmod 2^k$ is a
single ordinary residue class for every $k$.

The kernel verifies (1), the proper-power exclusion, and an explicit
positive representative at every precision. Its ordinary argument works
by recovering two integer coefficients. The signed argument explains the
address that led to them. [Formal proof](NegativeExponentAddress.lean)

## The signed address

The rational binary parameter $m_*=-2/27$ makes $j_*=-1$. The signed
peak $3^{-1}-1=-2/3$ follows an even and then an odd step to zero.
Every strictly lower signed peak $x=3^{-1-d}-1$, $d\ge1$, avoids zero
forever. Its first input is even and $x/2\in(-1/2,-4/9]$. Either
shortcut branch at this state puts the next value in $(-1/3,0)$.
Future halvings remain strictly inside that interval, and an odd input
makes the next value positive. Positivity is then preserved. Both branches
are understood on the rationals of odd denominator, using numerator parity.

For an ordinary exponent, put $u=27m+2$. Since $j+1=6u$,
$$
 v_2(3^{j+1}-1)=v_2(u)+3 .
$$
This follows by squaring $9=1+8$, with each subsequent squaring adding
one to the initial valuation, and taking an odd power. Since $j$ is
odd, $P_j$ starts with an even step and an odd step. As long as
$2\le i\le k+3$, its value is exactly $(3^{j+1}-1)/2^i$. Its initial
two steps agree in parity with the signed peak.

## Two coefficients distinguish unequal clocks

If an earlier peak $P_n$ reaches $y$ in $t$ steps with $p$ odd
inputs, its affine word has
$$
 2^t y=3^{n+p}+C,\qquad -3^t\le C\le3^t-2^t .
$$
The carry begins at $-1$, stays fixed on an even input and becomes
$3C+2^\ell$ on an odd input at clock $\ell$. The bounds follow
by induction.

Suppose also $2^i y+1=3^{j+1}$ and $2(i+t+1)<j$. Since
$T(x)+1\le3(x+1)$ one has $y+1\le3^{n+t}$, and therefore
$3^{j+1}\le3^{i+t+n}$. Thus $n>i+t+1$. Expanding the proposed
equality gives
$$
  3^n\bigl(2^t3^{j+1-n}-2^i3^p\bigr)=2^t+2^i C .
$$
The absolute value on the right is at most $2^t+2^i3^t<3^n$.
Both sides vanish. Unique binary valuations force $i=t$, after which
$p=j+1-n\ge2$ and $C=-1$.

A carry ending at $-1$ has at most one odd input. Before a last odd
input at positive clock $\ell$, the incoming carry is negative and
odd, hence is $-1$ by the signed-carry classification. The last odd
can return it to $-1$ only at $\ell=1$. The first branch must then
have been even. A last odd at clock zero cannot produce $-1$. Any
following even steps preserve the carry. This contradicts $p\ge2$.
[Existing kernel-checked signed-carry classification](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/unbounded-queries/AllMersenneCarries.lean)

For $i<2$, advance both arms by $2-i$ clocks. The new upper clock
$i'$ is at most $k+3$ and the new lower clock $t'$ is at most
$j/3+2$. Now $2k\le2^k\le27m+2$ and $m\ge1$ imply
$2(i'+t'+1)<j$, as required in the preceding calculation. This proves
(1), including lower exponent zero. For $k\ge2$, the residue of $m$
is two modulo four. Any even proper power is divisible by four.

## Simultaneous ordinary survivors of bounded searches

The physical upper estimate for inverse queries holds uniformly in any
ordinary progression $m=a+Qr$ with $a\ge0$, $Q\ge1$, $3\nmid Q$.
Indeed every charged ternary cylinder in $m$ becomes a single cylinder
of the same period in $r$. It contributes at most its mass times $N$
plus one to any interval of $N$ consecutive indices. The rounding
calculation and its constants do not depend on $a,Q$. The number of
discarded small ordinary $m$ is also bounded independently of the
progression because its terms are distinct. This proves the progression
extension for the same surplus bound $D_N$ and constant
$c_0=1/(27\cdot2^{65})$. [Physical counting theorem and surplus horizon](INVERSE_COVERAGE.md)

At each $K\ge2$, take the least $0\le a_K<2^K$ with
$27a_K+2\equiv0\bmod2^K$. For $N$ consecutive nonnegative
indices $r$, all but at most $(c_0+o(1))N$ of the actual parameters
$m=a_K+2^K r$ satisfy **all three** properties below, uniformly in
$K$ and the location of the interval.

1. The parameter $m$ is no proper integer power.
2. Every earlier $P_n$ avoids the top $P_j$ through the entire
   rectangle $i\le K+3,\ 3t\le j$. More generally, for every
   $x<M_j$ with $n_x=v_2(x+1)$, the same upper clocks avoid all
   $T^h x$ with $0\le h\le n_x+j-3i-11$.
   [Full smaller-source clock theorem](ALL_SOURCE_CLOCKS.md)
3. At every phase $0\le u\le j$ of the original Mersenne ascent, every
   positive physical query $w$ meeting that phase and satisfying
   $2^{40}w<z$ has more than $D_N$ surplus odd inputs. Here $z$
   is the actual original parent, $81z+271=128\cdot2^j$.

For example fix $0<\beta<1$, take
$K=\lfloor\beta\log_2 N/(1-\beta)\rfloor$, and restrict $N\le r<2N$.
Since $2^K N\le m<2^{K+1}N$, we have
$K=\beta\log_2m+O(1)$ and
$\log_3 N=(1-\beta)\log_3 m+O(1)$. This gives infinitely many
ordinary nonpowers for which the upper-clock exclusion and the inverse
surplus exclusion are both logarithmic in the same actual $m$, while
the lower-clock exclusion extends through $j/3$. The corresponding
leading inverse coefficient is $(1-\beta)/H_2(\log_3 2)$.

These are restrictions on the clocks or surplus needed by specified
merger searches. The ordinary parameters have no asserted defect status.
Unrestricted mergers and inverse queries remain open on each surviving
parameter. The progression statement and the combined counting
corollary are written deductions from the physical estimate.

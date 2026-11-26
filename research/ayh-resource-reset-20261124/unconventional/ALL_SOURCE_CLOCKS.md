# Clocks needed by every smaller ordinary source

Put $M_j=2^j-1$ and $P_j=3^j-1=T^jM_j$. For an arbitrary
smaller ordinary input $0\le x<M_j$, write $x+1=2^n b$ with $b$ odd.
These first $n$ steps are consecutive odd steps, reaching $3^n b-1$.
The following two bounds retain this same $x$ throughout.

* For $j=11+162m$, $m\ge1$, take any $k$ with $2^k\mid27m+2$.
  For **every** $0\le i\le k+3$, one has
  $T^i(P_j)\ne T^h x$ throughout the physical clock interval
  $0\le h\le n+j-3i-11$. One also has the simpler full rectangle
  $0\le h\le n+\lfloor j/3\rfloor$ for the same $i$. Both
  intervals include every clock before the smaller source's ascent ends.
  [Kernel theorems full_margin and full_clock](NegativeExponentAddress.lean)
* For any $j\ge1$, any positive $a$ not divisible by three, and
  $0\le u\le j$, put $Y_u=3^u2^{j-u}a-1$. If
  $x<2^j a-1$ and $T^h x=Y_u$, then $h>n+u$. This bound on
  every merger anywhere along a Mersenne ascent extends to arbitrary
  ternary-unit cofactors. [Kernel theorem prepeak_clock](NegativeExponentAddress.lean)

## Every cofactor and physical clock near the signed zero

After the $n$ initial odds, suppose $t$ more physical steps (with $p$
odd inputs) reach $y$. Write $q=n+p$. If $2^I y+1=3^{j+1}$ for
$2\le I\le k+3$, the affine equation supplies a signed carry $C$ with
$$
 2^t y=b\,3^q+C,\qquad -3^t\le C\le3^t-2^t .
$$
The physical height bound follows branch by branch. On odd inputs
$T(v)+1=(3/2)(v+1)$, and on even inputs $T(v)+1\le v+1$.
Thus $2^q(y+1)\le3^q(x+1)<3^q2^j$. Comparing to the upper
endpoint gives $j<q+2I$, since $(3/2)^2>2$.

Set $D=\min(j+1,q)$. Subtract the two affine equations to obtain
$$
   3^D\left(2^t3^{j+1-D}-2^I b\,3^{q-D}\right)
          =2^t+2^I C .                                             \tag{1}
$$
The right side has absolute value less than $3^{I+t+1}$. If
$3I+t+1\le j$, then $D>I+t+1$, so both sides vanish. Since $b$ is
odd, their leading coefficients give $t=I$ by binary valuation. The
carry is then $C=-1$, which allows at most one odd input in this
post-ascent word. But $b3^p=3^{j+1-n}$ with $p\le1$ contradicts
$b<2^{j-n}\le3^{j-n}$. This proves the stronger bound for all
post-ascent clocks. An upper clock $i<2$ can be advanced to $I=2$,
advancing the lower clock by the same amount. The safe constant eleven
in the headline includes this extension.

For a lower clock $H<n$, its endpoint has $y+1=3^H2^{n-H}b$.
As $H<n<j$, the identity $2^I y+1=3^{j+1}$ gives
$3^H\mid2^I-1$. Thus $H\le I$. The elementary upper bound
$y+1\le3^H(x+1)$ now gives $3^{j+1}\le2^I3^I2^j$,
impossible since $5I\le j$ and $6\cdot2^5<3^5$. Here $5I\le j$
follows from $2k\le2^k\le27m+2$. If extending an upper clock
$i<2$ advances the lower arm through its peak, at most one
post-ascent step has elapsed and the post-ascent result applies.
This proves the full ordinary-clock statement.

## Every original ascent phase for every ternary-unit cofactor

Consider an actual equality $T^h x=Y_u$. Let $q$ be the total number
of odd inputs from $x$ to this meeting. By the height bound just used,
$$
   (3/2)^u\,2^j a=Y_u+1\le(3/2)^q(x+1)<(3/2)^q\,2^j a .
$$
Therefore $q>u$. If $h\le n$, the lower path is still on its initial
ascent, $q=h$ and $Y_u+1=3^h2^{n-h}b$. This would imply
$3\mid 2^{j-u}a$, contradicting $3\nmid a$.

Consequently $h=n+t$ with $t>0$. The post-ascent carry satisfies
$$
    3^u \mid 2^t+C
$$
because $2^t+C=2^{j-u+t}3^u a-b3^q$ and $q>u$.
The right side is nonzero: equality to zero would again force
$3\mid2^{j-u+t}a$. The strict carry bound
$C<3^t-2^t$ holds by induction from $C_0=-1$, with the same
even and odd updates as above. Since $C\ge-3^t$, we have
$|2^t+C|<3^t$. Hence $3^u<3^t$, proving $t>u$.
This argument has no dependence on source density, the $e6$ exponent
row, or an assumption of convergence.

The underlying signed-carry comparison predates this packet. In
particular an earlier denominator argument compares pure Mersenne
sources at two specific rank-three checkpoints. Here the comparison
uses the total number of odd steps on an arbitrary supplied smaller
source, at the ordinary indicated clock. [Earlier simultaneous
checkpoint comparison](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/paired-reductions/SIMULTANEOUS_CHECKPOINT_DELAY.md)

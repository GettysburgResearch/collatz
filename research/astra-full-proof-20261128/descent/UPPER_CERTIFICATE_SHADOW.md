# The signed integer exposed by a finite upper certificate

**PROPOSED written theorem.** Let $T$ be the positive shortcut map, also
acting on signed rationals with odd denominator by their binary parity.
Start with a genuine native word for $3z\to1$ having $r\ge1$ odd
departures at $0\le u_1<\cdots<u_r=L-1$ and total length $H$.
Fix the positions of these odd departures and allow the terminal
halving run to vary. Set

$$
C=\sum_{i=1}^r 3^{r-i}2^{u_i},\qquad Q=3^{r+1},\qquad
z_H=(2^H-C)/Q,\qquad \xi=-C/Q.
$$

The results apply to each individual $H\ge L$ with $z_H$ a positive
integer. Restrict further to $z_H\equiv17\bmod48$ when working with
canonical defects. Binary congruence to the original upper source through
$L$ preserves its entire prefix. Its endpoint is $2^{H-L}$, followed
by the specified halvings. The ternary numerator of $C$ is a unit
because its last term is a power of two. Thus $\xi$ has exact
denominator $Q$.

## Release at an actual lower clock

Follow the one signed rational $\xi$ until it becomes an ordinary
integer $s=T^t\xi$. Each odd departure consumes exactly one remaining
factor of three. Even departures preserve that denominator. At positive
remaining denominator the current rational is nonzero and a finite
string of halvings exposes an odd numerator. Hence $t$ exists and is
the date immediately after the $(r+1)$st odd departure.

At every admissible $H\ge t$, $z_H$ and $\xi$ have the same binary
parities through $H$. At release and for $0\le i\le H-t$ this gives

$$
T^t z_H=2^{H-t}+s,\qquad
T^{t+i}z_H=2^{H-t-i}3^{p_i(s)}+T^i s. \tag{1}
$$

Here $p_i(s)$ counts the first $i$ odd departures of the signed
integer $s$. On a common parity prefix the endpoints' difference is
the starting difference times $3^p/2^i$, which proves both identities.
An in-range negative release entails $0<-s<2^{H-t}$.

## Every nonnegative signed release

Let $K=98304$. The upstream reduction turns any bad positive $w$
into a canonical reverse defect at most $Kw$. In particular the
appearance of a bad $w<z_H/K$ rules out leastness at $z_H$.
[PR 201 bounded-defect theorem](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/coupling/OptimizedBank.lean)

If $s=0$, (1) takes $z_H$ to a power of two and proves convergence
for **every** admissible $H\ge t$ on this row.

If $s>0$, there are two exhaustive possibilities.

* If $s$ is bad, an actual canonical reverse defect is at most $Ks$,
  strictly below $z_H$ whenever $2^H>C+QKs$.
* If $s$ reaches one in $l$ steps with $p$ odd departures, put
  $h=H-t\ge l$. At $H$ the actual lower source has endpoint at most
  $2+3^{p+\lceil(h-l)/2\rceil}$ by (1) and the $1,2$ cycle. In
  particular it is strictly below $z_H/K$ provided
  $KQ(2+3^{p+\lceil(h-l)/2\rceil})<2^H-C$.
  For a monotone effective sufficient cutoff take any $H_0\ge t+l$
  with $2^{H_0}>C+4KQ$ and
  $(2^{H_0}-C)^2>4K^2 Q^2 3^{2p+H_0-t-l+1}$.
  Both inequalities persist for $H\ge H_0$. Such an $H_0$ exists since
  $4>3$. If $z_H$ were bad its smaller endpoint would be bad and would
  supply a strictly smaller canonical reverse defect.

Thus every fixed upper itinerary with nonnegative release, of arbitrary
odd rank, eliminates all sufficiently long terminal tails as candidates
for the least reverse defect. In the positive convergent-seed case the
cutoff uses its finite stopping certificate. Comparing different $H$
does not replace the original lower source in either argument.

## What a negative integer enforces through the upper hit

Put $s=-A<0$, $s_i=T^i(-A)$, and $R_i=3^{p_i(-A)}/2^i$.
All $s_i\le-1$. The even branch halves the magnitude and the odd branch
sends $a$ to $(3a-1)/2$. Consequently $1\le|s_i|\le A R_i$ at
every clock, without assuming periodicity of any signed orbit.
Equation (1) therefore gives

$$
T^{t+i}z_H\ge (2^{H-t}-A)R_i
\ge (2^{H-t}-A)/A,\qquad 0\le i\le H-t. \tag{2}
$$

The source-local inequality $x\le A T^k x$ whenever $2^k\mid x+A$ is also kernel checked in SignedFloor.lean. Lean 4.34.1 reports only propext and Quot.sound for the all-clock ratio and floor theorems. Its standard-library imports are sufficient.

Whenever the right side is at least $z_H/K$, literal ordinary halving
floor descent cannot close the interval from release to the upper
endpoint. The first $t$ dates remain separately checkable.

For the canonical three-odd row $C=271,Q=81$ the release occurs at
$t=6,s=-2$. One further lower step gives $2^{H-7}-1$. Every admissible
large $H$ has the long compulsory ascent of this Mersenne source. Its
positive lower future beyond the terminal hit is the unresolved issue.
[PR 206 original Mersenne row](https://github.com/GettysburgResearch/collatz/blob/6bcf4f0b32d15678ab6775bdcc6e20d83736512d/research/clock-itineraries/ReturnDescent.md)

## Padding the *same* finite certificate

Keep $z_H$ fixed and append one $1\to2\to1$ upper lap. Its new pair
is $(H+2,r+1)$, and its new signed center is
$\xi'=\xi-2^H/3^{r+2}$. It follows exactly the old center's parities
through $H$. Suppose $t\le H$ released $-A<0$, and write $m=H-t$.
At the old release the new center is $-A-2^m/3$. Set
$j=v_2(A)<m$. Its next $j$ departures are even and its following
departure is odd. Thus the new release $s'=-A'$ and remaining time are

$$
t'=t+j+1\le H,\qquad m'=m+1-j,\qquad
A'=\frac{(2^m+3A)/2^j-1}{2}>0. \tag{3}
$$

The quotient before subtracting one is an odd integer greater than one.
The new ordinary positive lower endpoint is
$B'=2^{m'}-A'$, so $A'<2^{m'}$. Iteration proves strict negative
release for **every** padded certificate. The normalized recurrence is

$$
A'/2^{m'}=1/4+(3/4)A/2^m-2^{-m'-1}.
$$

In physical coordinates $B=2^m-A$, one has $v_2(B)=j$ and
$B'=(3(B/2^j)+1)/2$. Thus each upper lap advances the very same
lower trajectory through its even prefix and one odd departure.
Negative signed release persists even for convergent lower sources.
For example $z=3233$ is known to converge. Repeating the upper
cycle cannot turn its negative release into a nonnegative one.

The unresolved case requires a different ordinary merger or a
post-hit theorem about the original lower $B$. Sign persistence proves
no nonconvergence. The formulas cover terminal padding of a given
native upper certificate. They assert no invariance under replacing
the upper trajectory by a different preimage construction.

## Every hypothetical bad original source eventually has negative release

This also covers starting certificates with $t>H$. Suppose the original
positive lower orbit stays at least $F>1$ at every clock. Every bad
source satisfies this with $F=2$. The product of the actual shortcut
ratios gives, for all $i$,

$$
2^i T^i z\le z(3+1/F)^{p_i(z)}.
$$

After $d$ upper laps let $U=H+2d$ and $P=r+d+1$. Whenever
$2^U>z(3+1/F)^P$, the lower orbit has at least $P$ odd departures by
$U$, since otherwise its positive endpoint would be strictly below one.
At its $P$th odd release $t_d\le U$, the actual endpoint
$B_d=T^{t_d}z$ is strictly less than $2^{U-t_d}$ by the same product
bound. Thus the release is in range and strictly negative. The
sufficient inequality persists for every later $d$ because $3+1/F<4$.
In fact, with $m_d=U-t_d$,

$$
0<B_d/2^{m_d}\le [z(3+1/F)^{r+1}/2^H]\big((3+1/F)/4\big)^d .
$$

Since $B_d\ge F$, $m_d$ grows at least linearly in $d$ up to an
additive constant. This places every possible fixed defect, cyclic or
escaping, inside the negative chart at an explicitly bounded padding.
It leaves the genuine trajectory $B_d$ as the obstruction.

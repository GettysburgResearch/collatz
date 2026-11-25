# What a short meeting can do on a tall ternary tower

We use the ordinary shortcut map, with one halving at an even input and
\((3n+1)/2\) at an odd input. Write \(x=3^rw\), where \(w>0\) and
\(\gcd(w,6)=1\). The literal lower sources are \(3^j b\) with
\(0<b<w\), or with \(b=w\) and \(j<r\). The smooth reservoir also
permits a free factor \(2^i\) on any such source.

**Result.** If \(2H\le r\), every literal meeting through at most \(H\)
steps on each arm uses the same base and the same clock. An exact finite
test for existence uses only the parity prefix of \(x\). Every possible
lower base is covered, with either parity at the shared endpoint. For
arbitrarily large \(H\), there are ordinary arithmetic progressions on
which even the full smooth reservoir misses at clocks up to \(H\) but
a strictly smaller positive base is reached at clock \(6H+3\).
Universal convergence remains open.

## The finite test

For a chronological bit word \(v\) of length \(t\), let \(k(v)\) count
the ones. Build its nonnegative integer constant \(B(v)\) from zero.
At position \(i\), counted from zero, a zero leaves the constant fixed
and a one replaces it by \(3B+2^i\). An ordinary path with word \(v\)
from \(n\) to \(y\) satisfies
\[
              2^t y=3^{k(v)} n+B(v).
\]
Conversely this equality at nonnegative integers forces every step of
the stated word. Reduction modulo two determines the first bit. Divide
out that step and continue by induction. Also
\(B(v)+2^t\le3^t\). The all-ones word attains equality.

Let \(u_f\) be the actual length-\(f\) word of \(x\). When \(2H\le r\),
a literal meeting within the two budgets exists **if and only if**
there are \(f\le H\) and a word \(v\) of length \(f\) such that
\[
                 B(v)=B(u_f),\qquad k(v)>k(u_f).
\]
For the forward construction, take \(d=k(v)-k(u_f)\). The alternative
word is physically legal at \(3^{r-d} w\) and reaches \(T^f x\).
Here \(d\le f\le r\). For example, the words 10001 and 11100 both
have constant 19, and the second has one extra odd input. Consequently
\(T^5(96u+69)=T^5(32u+23)=27u+20\) for all nonnegative \(u\). At any height
the same construction works whenever \(d\le r\).

For necessity, suppose \(T^f x=T^h z\), where \(z=3^j b\) and
\(0<b\le w\). Scale both affine identities to the common denominator
\(2^H\). Each scaled slope lies between 1 and \(3^H\), and each
scaled constant lies in \([0,3^H)\). Consequently
\[
                       3^r w<3^H(3^j b+1).
\]
If \(j<H\), then \(H+j+1\le r\) and
\(3^H(3^j b+1)\le3^{H+j+1}w\), a contradiction. Thus both initial
values are multiples of \(3^H\). The two scaled constants agree modulo
\(3^H\), so the bounds give **exact equality**. Subtract them. With
\(a=k(u_f)\) and \(c\) the source word's odd count, the result is
\[
             2^{H-f}3^{a+r}w=2^{H-h}3^{c+j}b.
\]
Coprimality gives \(w\mid b\), hence \(b=w\). Cancel \(w\) and
compare powers of two to obtain \(f=h\). Then \(a+r=c+j\), proving
the criterion. On an actual first bad tower, every prefix through
clock \(r\) must have maximum odd count within its own constant fiber.
This stronger necessary condition follows from the constructive direction
alone and the certified goodness of all earlier powers. The converse
classification of all bounded meetings above uses \(2H\le r\).

## An ordinary return beyond the clock obstruction

For any \(H\ge1\), put \(r=2H\), \(m=H+1\), \(e=5H+2\).
Choose \(a>0\) satisfying
\[
  2^m a\equiv1+3^r\pmod{3^{r+1}},\qquad
  3^m a\equiv1+2^e\pmod{2^{e+1}}.
\]
Each multiplier is a unit for its modulus. The Chinese remainder
theorem therefore gives one class of \(a\) modulo
\(3^{r+1}2^{e+1}\). Positive lifts give arbitrarily large ordinary
bases
\[
         w=(2^m a-1)/3^r,\qquad b=(3^m a-1)/2^e.
\]
The first congruence gives \(w\equiv1\pmod3\). It is odd since
\(m>0\). The second makes both \(a\) and \(b\) odd.

Every prefix through \(H\) consists entirely of odd steps and ends at
an odd integer because \(2^{H+1}\mid x+1\). No word can be heavier
than the all-ones word. The finite test rules out every literal meeting
through \(H\). A source with an additional factor \(2^i\) that reaches
an odd endpoint must have completed all those halvings within its source
clock. Hence the same exclusion holds for the full smooth reservoir. For a
general even endpoint that extension fails. For example, take \(H=1,
r=2,w=9709\). Then \(T(87381)=131072=2^{17}\cdot1\). A free power
of two gives an immediate smooth meeting despite the absence of a
heavier one-bit word.

At clock \(m\) the value is \(3^m a-1=2^e b\). The next \(e\) steps
reach \(b\). To check strict descent with the additive terms retained,
the two run identities give
\[
             2^{m+e} b+2^m=3^{m+r}w+3^m .
\]
Here \(2^{m+e}=8\cdot64^H\ge 6\cdot27^H=2\cdot3^{m+r}\).
Also \(3^m\le3^{m+r}w\). These inequalities imply \(0<b<w\),
where positivity also follows from \(3^m a=2^e b+1\) and \(m>0\).
The first direct entry into the full smooth reservoir is already at
clock \(m=H+1\), at the integer \(2^e b\). The displayed descent to
the smaller integer \(b\) has clock \(6H+3=3r+3\). For \(H=1\), one
solution is \(w=1675,a=3769,b=265\), giving \(T^9(15075)=265\).
The return excludes every member of these progressions from serving as
the first bad tower.

The argument applies more generally to two consecutive runs satisfying
the displayed integer identities and \(2\cdot3^{m+r}\le2^{m+e}\).
The length of the even run is a genuine arithmetic condition. Its
required lower bound is unproved for an arbitrary first bad tower, even
if one allows the two runs to start later.

## A limit of the finite test at unrestricted clocks

The ordinary pair \(x=15, w=5, r=1\) satisfies the numerical frontier
guards of PR192. Indeed \(15+1=2^4\cdot1\) and \(3^4\equiv1\pmod{16}\).
The only eligible lower exponent is zero. No length has a word with
the same constant and exactly one more odd input. Such a word would
be the actual word from 5. At each of the first eleven clock positions
the path from 5 has at most the odd count from 15. At clock 11 both
are at 2 and both have used five odd steps, after which their counts
agree forever. There is nevertheless a literal earlier-power meeting,
\(T^8(15)=5\). This refutes an all-clock heavier-word cover even on a
single ordinary convergent input passing the frontier guards.

## Evidence and dependencies

[TowerClock.lean](TowerClock.lean) proves the word semantics, both directions
of the short-clock characterization, the full smooth exclusion for the
specified odd cylinder, the all-clock example, and the physical delayed
return under the two displayed integer identities. The CRT construction
and its infinitude are proved above. The exact checker supplies ordinary
representatives and independently compares the finite test to backward
trees through clock 8. Run `python -B check.py` or
`python -O -B check.py` in this directory. [Exact control code](check.py)

The only project import is
[SourceDeletion.lean](../../round9/vendor/SourceDeletion.lean) at PR195
`51e2c43a60950e446eabe782c5b1cb1d0ae11bab`. The contextual
first-tower application uses PR192 at
`a0d7c6e36c378bbb6c826002039aef486bbe0383`, specifically `FirstTower.smaller` and
`FirstTower.earlier` from
`research/astra-universal-closure-20261124/global/SmoothCore.lean`;
the arithmetic theorems take no basin hypothesis. PR197's quantitative
localization at `b27a6fe31a487adf5615e173329ad009b975a3cd` concerns
an ordered reverse failure. Its higher-rank progress hypothesis remains
open and is independent of these equal-constant identities.

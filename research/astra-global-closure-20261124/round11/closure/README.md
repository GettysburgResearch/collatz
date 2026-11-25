# Ordinary descent from periodic anchors

A transfer through phase 1 of the positive cycle can replace a tower source by a point over a smaller base and a strictly *larger* ternary exponent. Every such phase-1 transfer into a smaller ternary base already places the actual forward orbit below its original base at the meeting clock. The transfer has a precise size restriction. At a fixed odd base, a finite set of signed periodic target phases supplies immediate certificates to a smaller base or an earlier exponent at only finitely many exponents, even with arbitrary preperiod anchors and unlimited terminal halvings.

The positive ordinary map is $T(2u)=u$, $T(2u+1)=3u+2$. Write $x=3^r w$ for the supplied source. A first bad tower at $(w,r)$ would have $w$ positive, odd and prime to three, with every $3^s b$ over $0<b<w$ good. The following source-dependent sufficient conditions are unconditional. The complete pointwise question stays open.

## A strictly smaller base at every requested pair of exponents

Let $d>0$, $b>0$ and let the positive anchor $a=3^{r+d}b$ actually reach 1 at clock $h$. For every $t\ge0$ put
\[
 w=3^db+2^h4^d t,\qquad v=b+2^h t.
\]
Then $0<v<w$ and
\[
 T^{h+2d}(3^r w)=T^h(3^{r+d}v),\qquad T^h(3^r w)<w .
\]
This gives a physical smaller-base certificate for the supplied $w$ whenever the displayed congruence holds. The clock and both exponents may be arbitrarily large. For every $r,d$ as above there is an explicit positive anchor: take $h=2\cdot3^{r+d}$ and $b=(2^h-1)/3^{r+d+1}$. Successive cubing proves the divisibility. The anchor has one odd input, followed by halvings to 1. The parameter $t$ then gives a whole progression of ordinary bases. [Kernel proofs (grade_gain), (grade_gain_native), (all_exponents)](AnchorDescent.lean)

Indeed, if $p$ counts the odd inputs before the hit from $a$, the physical lift identity gives $T^h(a+2^h u)=1+3^p u$. On the positive cycle, $T^{2d}(1+4^d u)=1+3^d u$. Their composition gives the displayed merger. Further, $3^p a\le 2^h$, so
\[
 aT^h(a+2^h u)\le a+2^h u.
\]
Here $a>3^r$, which already proves the native descent at $h$.

## All positive anchors that find an immediate smaller ternary base

Take **any** $a>0$ reaching 1 in $h$ steps, $d,t>0$, and any $s,b$ satisfying
\[
 x=3^r w=a+2^h4^d t,\qquad y=3^s b=a+2^h3^d t,\qquad b<w.
\]
Then both
\[
 T^{h+2d}(x)=T^h(y)<w,\qquad 3^r<w.
\]
The proof imposes no upper bound on the anchor, the hitting clock, the saved cycle work or the target exponent. An integer lift with $t<0$ cannot give a positive $x$, since $a\le2^h$. At $t=0$ the two sources coincide, which cannot lower the base of a 3-free $w$. [Kernel proofs (positive_anchor_native), (positive_anchor_scale)](AnchorDescent.lean)

Write $k=\min(r,s)$. Subtracting $x-y$ and using $3\nmid 2^h(4^d-3^d)$ gives $3^k\mid t$ and then $3^k\mid a$. Thus $3^k\le a\le2^h$ and $3^k\le t$. The anchor contraction above gives $aT^h(y)\le y$. If $s\le r$, use $y=3^s b\le ab<aw$. If $r\le s$, use $y<x=3^r w\le aw$. This proves the strict ordinary endpoint bound.

The size restriction holds more generally for $w>0$ and $b\le w$, including earlier same-base exponents. In fact $x>4^d3^{2k}$. If $k=r$, then $2^d3^k\ge3^r$. In the other case $k=s$, observe $3^d x\le 4^d y$ and $b\le w$. Cancellation gives $3^d3^r\le4^d3^s$ and hence $3^r\le2^d3^k$. Squaring yields $3^{2r}<x=3^r w$.

## Negative integer cycles of arbitrary period

Let the signed shortcut map send $-m$ to $-C$ in $h$ steps, with $m,C>0$. Suppose $-C$ returns to itself in $e>0$ steps containing $p$ odd inputs. For $t>0$, use the two ordinary integer sources
\[
 x+m=2^h2^e t,\qquad y+m=2^h3^p t.
\]
When both sources are positive they satisfy $T^{h+e}x=T^h y$. If $x=3^r w$ and $y=3^s b$ with $w>0$ and $b\le w$, then $3^r\le Cw$. The period can contain any positive number of laps, and the hitting clock of the signed phase is unbounded. [Kernel proofs (negative_meeting), (negative_anchor_scale)](AnchorDescent.lean)

On negative magnitudes the odd step sends $m$ to $(3m-1)/2$. The actual lap therefore gives $2^e\le3^p$, and parity gives strict inequality. The finite lift from the negative representative is exact: if $u+m=2^h v$, then $T^h u+|T^h(-m)|=3^j v$, where $j$ counts odd inputs on that negative prefix. Applying this to both sources and to the signed lap gives the ordinary meeting.

Since $y>x$, even $b\le w$ forces $s>r$. The difference $y-x=2^h(3^p-2^e)t$ gives $3^r\mid t$ and $3^r\mid m$. We have $m\le2^h C$. If $3^r\le C$, the conclusion follows from $w\ge1$. Otherwise $t\ge3^r$, $2^e\ge2$, and
\[
 3^r w=2^{h+e}t-m\ge2^{h+1}3^r-2^h C\ge2^h3^r.
\]
Now $3^r\le m\le2^h C\le w C$.

As an ordinary control, $x=3^6\cdot5=3645$ first falls below 5 at clock 29, reaching 4. But $3^6>136\cdot5$. Thus no positive anchor of the stated form and no negative anchor reaching a phase of magnitude at most 136 can give an immediate smaller ternary base, even with unrestricted clocks. The three signed cycles containing $-1,-5,-17$ have maximum magnitudes $1,10,136$ respectively. [Kernel arithmetic and first-hit control](AnchorDescent.lean) · [Independent finite replay](../../../../reports/astra-global-closure-20261124/round11/closure/finite.json)

## Allowing every final halving

**Source-qualified written theorem.** Fix any positive odd $w$ and any finite set of nonzero integer periodic target phases. Allow any signed integer anchor reaching one of those phases after an arbitrary preperiod, any positive number of positive-length complete laps there, and a nonzero integral displacement from the anchor. The set of exponents $r$ for which the resulting ordinary replacement $y$ has the form $2^i3^s b$ with $i,s\ge0$ and $0<b\le w$ is finite. In particular this includes the entire immediate lower cone, with either $b<w$ or $b=w$ and $s<r$. Hence all sufficiently large exponents at that *same base* are outside these immediate certificates. No convergence verdict for those uncovered sources follows. On an odd 3-free base, zero displacement leaves $x$ unchanged and cannot give a strict lower-cone representation. Additional odd moves after replacement and chains of distinct transfers are outside the assertion.

The signed target is $\pm C$, $C>0$. At a positive target put $x=a+2^h2^e t$, $y=a+2^h3^p t$, where $h$ is the preperiod and $e,p$ are the length and odd count of the chosen laps. At a negative target use the earlier formulas centered at $-m$. Positive ordinary $x,y$ are required throughout. For a nonzero cycle the target magnitude is prime to 3: the cycle has an odd step and all states after an odd step are prime to 3. The physical proof by finite lifts applies verbatim at any integer target with the stated period. The results at positive phase 1 and all negative phases above are kernel proofs. The general positive-phase estimate and the use of the multiplicative-group theorem below are written arguments. [Evertse, Schlickewei and Schmidt, Annals of Mathematics 155 (2002), 807–836](https://annals.math.princeton.edu/2002/155-3/p04)

For $h>0$, the replacement has the parity of the odd $x$, so $i=0$. The negative bound above applies at any negative phase. At a positive phase $C$, the lap satisfies $3^p<2^e\le4^p$. For the first inequality its affine carry is positive. For the second, every odd numerator $3n+1$ is at most $4n$ on positive integers. Write $k=\min(r,s)$. Subtracting the two source equations shows $3^k\mid t$ and $3^k\mid a$. When $t>0$, $a\le C2^h$ gives
\[
 Cx>2^e3^{2k}.
\]
If $r\le s$, the right-hand side is at least $3^{2r}$. Otherwise $3^px\le2^e y$ and $b\le w$ give $3^p3^r\le2^e3^s$. Squaring and using $2^e\le4^p\le3^{2p}$ gives $3^{2r}\le2^e3^{2s}$. Thus $3^r<Cw$ in both cases. When $t<0$, the replacement is larger than $x$, so $b\le w$ implies $s>r$. Then $3^r\mid t$ and $2^{h+e}|t|<a\le C2^h$, which bounds $3^r<C$ outright. The positive and negative estimates cover all preperiods uniformly.

It remains to allow unbounded terminal halvings at $h=0$. Let $E,P$ be the least period and its odd count at a chosen phase, and write $q=2^E/3^P$. Every return has some positive number $\ell$ of full laps. At a positive phase $C$ the replacement $y=C+3^{P\ell}t$ is prime to three. Write $y=2^i b$. Eliminating $t$ gives
\[
 (w/C)3^r+q^\ell-(b/C)2^i q^\ell=1,\qquad q>1.
\]
The coordinates $(3^r,q^\ell,2^i q^\ell)$ lie in the group generated by $(3,1,1),(1,q,q),(1,1,2)$, of rank at most three. The cited theorem bounds the number of nondegenerate solutions for each $C,w,b$. A cancellation of the first and last terms would give $q^\ell=1$. A cancellation of the second and last would force $w3^r=C$, determining at most one exponent. The two positive terms cannot cancel. This also covers either sign of $t$.

At a negative phase $-C$, again $y=3^{P\ell}t-C$ is prime to three. Now
\[
 -(w/C)3^r+q^\ell+(b/C)2^i q^\ell=1,\qquad q<1.
\]
Use the same three generators for nondegenerate solutions. Cancellation of the first and last terms would give $q^\ell=1$. Cancellation of the first two gives $w3^r=Cq^\ell<C$, a finite exponent range. These exhaust vanishing proper subsums. There are finitely many choices of phase and $b$, and the first coordinate of each solution records $r$. The argument bounds cardinality without giving the location of the exceptional exponents.

The same primary theorem distinguishes tower exponents from upper-certificate odd counts. For fixed $w,y>0$ and $K$, only boundedly many $r$ have $T^h(3^r w)=y$ with at most $K$ odd inputs, uniformly in $w,y$. For exactly $j$ odd inputs at positions $0\le u_1<\cdots<u_j<h$, division of the affine trajectory identity by $2^h y$ gives a positive unit equation with coordinates $3^r2^{-h},2^{u_1-h},\ldots,2^{u_j-h}$ and coefficients $3^j w/y,3^{j-1}/y,\ldots,1/y$. Its group has rank at most $j+2$. Positivity excludes every vanishing subsum and the first coordinate recovers $r$ by its 3-adic valuation. For $j=0$ that coordinate is uniquely determined. This bounds the *number* of admitted exponents, not their largest value uniformly over the coefficients.

## Relation to the pointwise question

PR192's positive and negative paired transfers can reduce the odd work in a particular upper certificate. PR197 supplies a smaller reverse defect with a good upper arm at controlled height, but the return theorem does not bound the new upper certificate's odd count by that of the old one. PR209 finds one base for a simultaneous block of exponents and supplies a separate exact test at clock 1024. The variable base in that block and the unknown clock for each prescribed reverse defect prevent those results from completing pointwise descent. [PR192 transfer source at 570476be](https://github.com/GettysburgResearch/collatz/blob/570476be82f706122cdd23ebd7a00f3d4ff90cd8/research/astra-ultra-closure-20261125/bridge/PairedReturn.lean) · [PR197 closing consumer at 156652e](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/source-progress/FinalProgressProposal.lean) · [PR209 at 2d0230a](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/machinery/TowerCertificate.lean)

The unproved step is still an ordinary lower-base or earlier-exponent merger at the actual first bad tower, or a contradiction for that particular configuration. The size bounds and the finite-exponent theorem delimit one-step anchor transfers. They leave open nonperiodic comparison words, several successive anchor transfers, and other source-dependent descents.

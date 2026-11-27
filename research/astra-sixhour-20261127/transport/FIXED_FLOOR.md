# Which fixed-source information survives a synchronous compressor?

**PROPOSED application of the corrected-height cocycle.** A compression
from \(y\) to \(z\) in this note means an actual common-clock merger
\(T^h y=T^h z\) with equal odd counts \(q_h(y)=q_h(z)\).
A joint compression satisfies these conditions on each of its two arms.
The conclusions apply already to the indicated individual arm.

## Escaping lower component

On a positive escaping component write
\[
 P(x)=x\prod_{j:\,T^jx\ {\rm odd}}\left(1+\frac1{3T^jx}\right).
\]
The infinite product exists and \(x\le P(x)\le Cx\), with the independent
absolute choice \(C=512\) from [the shell calculation](../../astra-unconventional-20261126/operator/SUFFIX_MASS.md).
The sharper ordinary lower floor assertions there are also available.
Splitting the product at a physical clock gives
\[
                     P(T^h x)=3^{q_h(x)}2^{-h}P(x).                 \tag{1}
\]
This corrected height and its component minima are prior work:
[fixed-clock competition](../../astra-universal-step-20261124/arithmetic.md)
and [anchored siblings](../../astra-fixed-atom-20261124/arithmetic.md).

Each synchronous compression preserves \(P\) exactly. The entire class
of any fixed \(z\), including arbitrary repetitions of compressions or
their reversals, is therefore contained in
\[
                         [P(z)/C,\ P(z)]\cap\mathbb N .              \tag{2}
\]
In particular **unbounded amplification of one fixed escaping anchor
inside the relation preserved by the compressor is impossible**.
If \(m\) is the ordinary minimum of its whole escaping component,
the class at \(m\) is contained in
\([m,m+O(m^\theta\log(2m))]\), where \(\theta<1\) is any exponent
in the uniform translated-interval orbit bound
\(\#({\rm Orb}(x)\cap I)\ll |I|^\theta\log(2|I|)\) for intervals of
length at least two. Indeed its whole ray remains above \(m\);
sum reciprocals in successive dyadic shells and exponentiate the
resulting \(O(m^{\theta-1}\log(2m))\) bound for \(\log(P(m)/m)\).
The previous [ordinary operator note](../../astra-unconventional-20261126/operator/README.md)
gives the source of this translated bound.

Suppose the amplification instead uses a meeting
\(T^{h_y}y=T^{h_z}z\) with odd counts \(p_y,p_z\).
Then \(P(y)=\lambda P(z)\) with \(\lambda=2^{h_y-h_z}3^{p_z-p_y}\).
After *any number* of subsequent synchronous compressions,
the lower endpoint has physical height at least \(\lambda P(z)/C\).
If this exceeds \(z\), such compression alone can never return below
the original floor. A large population of such copies has the same
obstruction, one copy at a time. An additional physical operation
changing the corrected-height level could still cross that floor.

## Cyclic lower component

Fix a positive cycle, one specified vertex \(c\), period \(\ell\),
number \(q>0\) of odd departures per lap, and cycle minimum \(m_C\).
For each source in its basin let \(\tau_x\) be its first hit at \(c\)
and \(\nu_x\) its odd count through that hit. The integer
\[
                           I(x)=q\tau_x-\ell\nu_x
\]
has the same value if any later hit at \(c\) is selected. A synchronous
equal-grade merger of \(x,z\) preserves \(I\): append the same tail
from their meeting to \(c\), and remove any whole laps on each arm.
On the first-hit path the distortion \(D_x\in[1,C]\) because the
departing vertices are distinct, including when the path first enters
the cycle at a vertex other than \(c\). Thus
\[
 \log(x/c)=\tau_x\log2-\nu_x\log3-\log D_x
     =g\,\tau_x + I(x)\log3/\ell-\log D_x,
 \qquad g=\log2-(q/\ell)\log3>0 .
\]
The positivity of \(g\) follows from the positive distortion on the
cycle. The exact one-lap identity further gives
\[
 0<g=\ell^{-1}\!\!\sum_{v\ {\rm odd\ on\ cycle}}\log(1+1/(3v))
 \le q/(3\ell m_C)\le1/(3m_C).
\]
Consequently every copy of one fixed anchor \(z\) that compresses to
it at a common clock \(h\) has
\[
                 h\ge g^{-1}\log x-O_{z,C}(1).                     \tag{3}
\]
Indeed \(\tau_x\le h+\tau_z+\ell\): by clock \(h\), the fixed anchor
either has a remaining prefix to \(c\) of length at most \(\tau_z\)
or is on the cycle. The first-hit identity with \(I(x)=I(z)\) proves
(3). In particular one-step same-clock equal-grade copies merging to
this fixed anchor by \(A\log x\), \(A<1/g\), have bounded height.
This clock conclusion concerns the full merger to the fixed anchor;
several local compressions can have an unbounded cumulative clock.

## Actual upper-certificate slices

For positive \(u\) which reaches 1 write \(Q(u)\) for its odd count
before the first hit of 1. Along any single positive path there is at
most one odd \(u>1\) of a given \(Q(u)>0\): the first departure from
such a vertex spends an odd step and the remaining count decreases.
For the canonical hard family
\(z_m=(2^{m+7}-271)/81,\ m=11+162j\), the ordinary
[upper prefix](../../astra-unconventional-20261126/descent/SIGNED_MERSENNE.md)
ends at \(2^{m-2}\) in nine clocks with three odds. Thus the odd
\(3z_m\) all have \(Q=3\). After their first odd departure the
upper states \(U_m=3X_m-1\), \(X_m=(2^{m+6}-122)/27\), are odd
and have \(Q=2\). Their ordinary predecessor sets are pairwise
disjoint as \(m\) varies. A paired source can visit at most one
of these literal targets even if the lower and upper clocks are
allowed to differ. The known mergers farther downstream on the
powers of two do not require visiting those literal targets.

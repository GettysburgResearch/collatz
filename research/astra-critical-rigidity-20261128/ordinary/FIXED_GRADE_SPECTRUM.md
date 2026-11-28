# The exact fixed-grade joint count for two marked targets

**PROPOSED written theorem.** On positive integers use the shortcut $T$ and count odd departures. Fix targets $a,b>0$ and a nonnegative integer $G$. Let $J_G(X)$ count *all* integers $s\in[X,2X)$ for which $s$ visits $a$ and $3s$ visits $b$, with total grade at most $G$ through those two visits. Equivalently, use the two first visits. Logarithms below are base two. Constants in error terms may depend on $a,b,G$. The asymptotic takes $X\to\infty$ at fixed $G$.

## A control with both targets equal to 1

If $a=b=1$ and $G<5$, then $J_G(X)$ is eventually a constant integer. For $G\ge5$ put $p=\lfloor(G-5)/2\rfloor$. Then

$$
 J_G(X)=\frac{(\log_2 X)^{p+1}}{18\,3^p(p+1)!}
              +O_G\big((\log_2 X)^p\big).                         \tag{1}
$$

For example, at grades five and six the coefficient of $\log_2 X$ is $1/18$. Each additional pair of allowed odd departures adds one power of the logarithm. This coefficient comes from ordinary first visits and an explicit residue class.

## Fixed distinct targets

If either target is a multiple of three, or if neither target visits the other, then $J_G(X)$ is eventually a constant integer for every fixed $G$.

For comparable ternary units consider each possible direction $u\to v$ among the two marked targets for which $u$ visits $v$. Keep the single direction $u=v$ when the targets agree. Discard a direction if $v=2^j u$ for some integer $j\ge1$. Such a $v$ would be visited first on the long final string of halvings to $u$. If a direction is discarded, its reverse is available with zero odd cost. The retained directions therefore form a nonempty set. Let $h_u$ be the odd count through the first visit of $u$ to $v$, including $h_u=0$ for equal targets. Set $h=\min h_u$ over retained directions. When the targets are distinct and comparable in just one direction, that direction is always retained.

If $G<5+h$, then $J_G(X)$ is eventually a constant integer. Otherwise put

$$
 p=\left\lfloor\frac{G-5-h}{2}\right\rfloor,\qquad
 m_*=\#\{u\to v\text{ retained}:5+2p+h_u\le G\}.
$$

Then

$$
 J_G(X)=\frac{m_*\,(\log_2 X)^{p+1}}{18\,3^p(p+1)!}
             +O_{a,b,G}\big((\log_2 X)^p\big).                     \tag{2}
$$

In particular the threshold grade at which the joint octave count becomes unbounded is exactly $5+h$.

## Why a large odd source has a fixed early common cylinder

Write $s$ for the **odd** source core in this paragraph. By the [ordinary unmatched-clock bound](PAIRED_SOURCE_GRADES.md), a pair with total grade at most $G$ can remain at distinct states at every common clock through $k$ only if $k\le K=(2G+3)G$. Above the fixed cutoff $2^{K+1}\max(a,b)$ both marked visits take more than $K+1$ native steps because a step retains at least half the input. The pair must meet by $K+1$ and before either visit. At this first common clock $t$ each arm has a physical affine numerator. Its equality reads

$$
             3^g s+C=3^{g'+1}s+C'.
$$

There are finitely many words and clocks at this fixed cutoff. If slopes differ, a pair of words permits at most one value of $s$, so all those accidental equalities together cost only finitely many cores. In the remaining cylinders $g=g'+1$ and $C=C'$. Both starts are odd, so $g'\ge1$. If $g'=1$, its intercept is one whereas the two-odd intercept on the first arm is at least five. Thus a genuine common cylinder spends at least five odd departures, and every larger admissible cost is at least seven.

There is exactly one *first*-meeting cylinder of cost five. Let the odd departure positions be $0,u,v$ on the first arm and $0,w$ on the second, with $0<u<v$ and $w>0$. Intercept equality forces

$$
             2^w=6+3\,2^u+2^v.
$$

If $u\ge2$ the right side is two modulo four and exceeds two. Thus $u=1$ and $2^w=12+2^v$. For $v\ge3$ the right side is four modulo eight and exceeds four. Therefore $(u,v,w)=(1,2,4)$. At date five both parity words are fully specified, and the first five parities specify one class modulo 32. The direct cylinder is

$$
 s=23+32t,\qquad T^5s=T^5(3s)=z=20+27t.
$$

Its two paths are distinct until that meeting. Any proposed longer first-meeting word of cost five has this same prefix and has already met. Every other genuine first-meeting cylinder also parametrizes its common endpoint injectively by the free source parameter. This follows from the positive affine slope.

## The exponent calendar on the common tail

Suppose the large odd core has already synchronized, and let $u$ be the first of the marked targets hit from its common state $z$. A path to the other target costs $h_u$ odd departures on the appropriate arm. Write $m$ for the number of odd departures from $z$ to this first hit. They cost $2m$ across the pair.

A path from $z$ to $u$ with exactly $m$ odd departures has a unique calendar once its physical path and final clock are fixed. For $m\ge1$ it can be written backward as

$$
 x_m=u,\qquad x_{j-1}=(2^{e_j}x_j-1)/3\ (j=m,\ldots,1),
       \qquad z=2^{e_0}x_0.
$$

Here $e_0\ge0$, $e_j\ge1$ for $j\ge1$, and all $x_0,\ldots,x_{m-1}$ must be positive odd integers. In the case $m=0$ this is $z=2^{e_0}u$. If $u$ is even, the final exponent ends exactly at $u$; it can be recovered by subtracting $v_2(u)$ from the valuation at that odd departure. For $m\ge1$ and fixed $u,m,z$, the initial even exponent is determined by the odd part of $z$, then the actual successive odd departures determine every subsequent exponent. A revisit to $u$ with the same $m$ and a different clock is impossible on positive integers because another return uses an odd departure.

For any legal calendar, writing $E=\sum e_i$ gives $2^E u/4^m\le z\le 2^E u/3^m$, using $3x+1\le4x$ at each positive odd source. Thus at any fixed early cylinder the source cutoff $s\le X$ is the exponent cutoff $E\le\log_2 X+O(1)$ up to a boundary of bounded thickness. Even without imposing a residue on $z$, there are $O((\log X)^{m+1})$ possibilities. Imposing a fixed upper bound on at least one specified exponent saves one power. These bounds also apply to $m=0$.

To keep *first* visits, it suffices for the main term to consider all $e_i$ larger than a fixed constant depending on the targets and $m$. Outside this range the whole count is $O((\log X)^m)$. When $m\ge1$, the last odd predecessor is then larger than both marked targets. The earlier odd predecessors increase strictly as one proceeds backward. Every earlier even segment stays above its next odd source. Therefore only the final consecutive halvings to $u$ can visit another marked target earlier. They do so precisely when $v=2^j u$, $j\ge1$. The same description holds when $m=0$. In particular any earlier return to $u$, including a lap at 1, is absent from these large calendars.

For a discarded direction all apparent first arrivals with more than bounded exponent at each coordinate are therefore impossible. Its true contribution is $O((\log X)^m)$, with $m\le\lfloor(G-5-h_u)/2\rfloor$. Whenever a direction is discarded its reverse has $h=0$, so this error never reaches the leading degree in (2). Below the proposed threshold a discarded direction cannot give unbounded growth: its reverse has $h=0$ and hence $G<5$.

Every nondominant genuine cylinder costs at least seven. Its upper bound loses at least one logarithmic power against (2). On the unique grade-five cylinder, $m<p$ has the same lesser order. If the targets are mutually reachable, assign by the *first* marked target reached after the common prefix, so the retained orientations are disjoint. Each of the $m_*$ contributing orientations in (2) has exactly $m=p$ on its common tail.

## Counting the leading residue classes

For the grade-five cylinder the endpoint congruence is $z\equiv20\pmod{27}$. It forces $x_0$ to be a ternary unit. Every other backward intermediate is also a unit because the preceding odd inverse exists. Given any positive ternary unit $x_j$, an ordinary ternary-unit odd inverse requires $2^{e_j}x_j\equiv4$ or $7\bmod9$. This admits two of the six exponent classes modulo six. After these choices, exactly one class of $e_0\bmod18$ places $2^{e_0}x_0$ at $20\bmod27$.

For clarity, the full test is a union of residue classes of the vector $(e_m,\ldots,e_1,e_0)$ modulo $M=2\cdot3^{m+2}$ in each coordinate. Two is a primitive root modulo $3^l$ for $l\ge1$, since $v_3(4^{3^j}-1)=j+1$ by induction. Knowing the exponents modulo $M$ permits backward computation of each $x_j$ modulo $3^{3+j}$, losing exactly one available trit at each division. Assign the coordinates in backward order. A fraction $1/3$ of the choices at each odd inverse preserve a unit, independently *in count* of the residues already assigned. The final fraction is $1/18$. The admissible class fraction is exactly $1/(18\cdot3^m)$. Positivity of every inverse holds on the large calendars used for the leading term.

For each class, the number of exponent vectors with $E\le L$ is $L^{m+1}/(M^{m+1}(m+1)!)+O_m(L^m)$ with the constant allowed to depend on this fixed $M$. Subtract the fixed residues and use the elementary simplex count. Shifting $L$ by a bounded constant has the same error. Distinct valid calendars on the leading range give distinct $z$ and hence distinct odd cores. Consequently each eligible orientation supplies precisely the coefficient in (2) for *odd cores up to* $X$. If $G<5+h$, only finitely many odd cores remain. The same finiteness for incomparable targets follows directly from (1) of the [clock paper](PAIRED_SOURCE_GRADES.md).

## Returning to all inputs in one octave

Every odd core with a witness supplies every dyadic lift at the same grade. A core at most $X$ supplies exactly one lift in $[X,2X)$. The extra cores in $(X,2X)$ contribute at most the difference of the cumulative counts at $2X$ and $X$, which is $O((\log X)^p)$ by the just-proved asymptotic. If either marked target is even, a lifted input can hit it during its initial halvings. In that event the odd core of the first arm is either the odd part of $a$ or one third the odd part of $b$, so there are at most two extra core rays. On any one ray membership is upward closed in the dyadic exponent and stabilizes. This costs $O(1)$ and likewise gives exact eventual constancy whenever only finitely many cores occur. If either target is divisible by three, its entire predecessor set is its dyadic ray, so the same conclusion holds directly.

**Boundary.** The error constants and the first-merge cutoff depend on $G$. Summing (2) over a growing grade range is a different problem. For the comparable targets themselves a fixed ordinary link supplies the positive coefficient. For incomparable targets the argument restricts grades of their joint visitors; it does not exclude such visitors at unbounded grade.

## Exact finite controls

The [integer checker](check_grade_spectrum.py) compared inverse exponent calendars to direct physical first-hit grades for eight targets and all $1\le s\le12{,}288$. All 98,304 comparisons agreed through grade nine. The seven marked pair tests include $(1,1),(1,2),(8,2),(5,8),(2,5),(113,509),(3,9)$. The separate simplex test used exact residues and counted all allowed exponent vectors, including the short-coordinate boundary. At total exponent cutoff 2,304 its counts and leading terms were as follows.

| Common odd count | Exact calendar count | Leading term |
| ---: | ---: | ---: |
| 0 | 128 | 128 |
| 1 | 49,194 | 49,152 |
| 2 | 12,591,083 | 12,582,912 |

The normal and optimized Python runs yielded byte-identical [control output](GRADE_SPECTRUM_CONTROLS.json). These experiments test the fixed definitions and residue coefficients; the large-$X$ assertion uses the proof above.

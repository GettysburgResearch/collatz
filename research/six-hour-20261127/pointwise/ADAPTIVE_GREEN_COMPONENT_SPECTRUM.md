# The ordinary adaptive Green current and the maximum inverse gain

For the ordinary positive odd map $U(v)=(3v+1)/2^{e(v)}$, $e(v)=v_2(3v+1)$, write $v_i=U^i(v)$ and $A_i=\sum_{h<i}e(v_h)$. An actual path of length $k$ ending at $y$ has homogeneous gain $g=3^k/2^{A_k}$. Let
$$
 q(y)=\frac1y\max_{v,k:U^k(v)=y}g,
 \qquad s=3/2,\qquad
 b(r)=1+\frac1{2D}+\frac1{12D^2},\quad D=\max(13,r),\quad B=b(13).
$$
The empty path is included. Each nonempty affine path has $y>gv$, and each complete cycle lap multiplies the gain by a number strictly below one. Thus the maximum is attained among first arrivals from the finitely many odd $v\le y$.

For $i\ge1$, let $r_i(v)$ be the least positive odd representative of $v_i\bmod3^i$, and set $r_0(v)=1$. Along an actual word the prefix determines this representative. Use the unrounded and rounded normalized currents of PR193:
$$
 u(y)=\sum_{v,k:U^k(v)=y}(g/y)^s\prod_{i<k} b(r_i(v)),\qquad
 u_{\mathbb Q}(y)=\sum_{v,k:U^k(v)=y}
   3^{-(k\bmod2)/2}2^{-(A_k\bmod2)/2}(g/y)^s\prod_{i<k} b(r_i(v)).
 \tag{1}
$$
The word condition on a positive odd terminal in PR193 is equivalent to a unique actual positive odd starting integer: at each inverse step $x=(2^e y-1)/3$ is positive and odd when integral, and the terminal residue condition enforces every division by three. In particular (1) uses all ordinary preimages with their true gaps. Let $u^{(1)},u_{\mathbb Q}^{(1)}$ retain only the first arrival from each $v$, including the empty path from $y$.

**Theorem.** There is an absolute $C$ such that on every positive odd target
$$
 q(y)^s\le u^{(1)}(y)\le Cq(y)^{s-1},\qquad
 6^{-1/2}u^{(1)}(y)\le u_{\mathbb Q}^{(1)}(y)\le u^{(1)}(y). \tag{2}
$$
The same inequalities hold for the full currents at every nonperiodic target. An odd target is nonperiodic when no positive iterate returns to it. In particular a transient target of a bounded orbit is nonperiodic. The part of either first-arrival current furnished by $v>M$ is $O(M^{1-s})$ uniformly in the target and $M\ge1$, including all nonperiodic full currents. On a nontrivial ordinary cycle the full current can have infinitely many visits and actually diverges as PR193 proves.

Each escaping forward-meeting component $C_0$ has one positive unrounded current limit $h_{C_0}$, with $\sum_{C_0}h_{C_0}<\infty$, and between one and four positive rounded current limits from its recurrent clock parities. The positive limit values at infinity through nonperiodic positive odd targets are exactly the union of these component values in each respective model. Both strict and weak positive superlevels differ by finitely many targets from the corresponding finite unions of full escaping tails (unrounded) or recurrent parity subsequences of tails (rounded) whose limiting value is **strictly greater** than the threshold. The same spectrum and superlevel conclusions hold for first-arrival currents on all positive odd targets. Zero is always a limit. On a component with minimum corrected height $P$, the unrounded limit satisfies $P^{-s}\le h_{C_0}\le CP^{1-s}$.

## The source estimate before canonical birth

For the initial integer $v=1+2l$, put $\tau(v)=\min\{i:l<2^{A_i}\}$ and
$$
 a(v)=\prod_{0\le i<\tau(v)} b(r_i(v)).
$$
Indeed a word of length $i$ and total $A$ has one odd source cylinder modulo $2^{A+1}$. If its least positive odd source is $m$, all its positive sources are $m+2^{A+1}j$, and their actual terminals are $U^im+2\cdot3^i j$. The principal terminal is the least positive odd representative of that ternary class. The least positive odd representative $r\le2\cdot3^i$ in the terminal class has a positive odd inverse for the word, and the strict inequality $r>3^i v/2^A$ puts that inverse below $2^{A+1}$. It is therefore $m$. The empty word gives $m=r=1$ outright. Hence $r_i(v)=v_i$ exactly for $i\ge\tau(v)$.

For independent positive geometric letters of law $\Pr(e)=2^{-e}$, let $m(w)$ denote the principal dyadic source and $r(w)$ its true principal terminal at length $j$. We need only the first moment
$$
 \sum_{|w|=j}\frac1{m(w)}\le j+1,\qquad
 \sum_{|w|=j}2^{-A(w)}\frac1{r(w)}\le (j+1)3^{-j}.                   \tag{3}
$$
For the first inequality, the actual next letter of each principal parent retains its own $m$. Writing its other children's sources $m+2^{A+1}t$, each nonprincipal minimal $t$ lies in one of the dyadic sibling classes obtained by successively testing the next bit. Their reciprocals sum to at most two, by the exact sibling bound of PR201, equations (7)–(8). Thus these other children add at most $2^{-A}$, and all parent probabilities total one. The second inequality follows termwise from $r(w)\ge 3^j m(w)/2^{A(w)}$. This is the original, unconditioned word law.

For every $p>0$ with $B^p<3$, the physical sources satisfy
$$
 \sum_{1\le v\le V,\ v\ {\rm odd}} a(v)^p\le C_p V \qquad (V\ge1).     \tag{4}
$$
Telescope the product $a(v)^p$ at its own prebirth dates, bounding its product up to index $j$ by $B^{pj}$. Since $b(r)^p-1\le c_p/r$ by the mean value theorem on $[1,B]$, the date-$j$ increment summed over all $v\le V$ is at most
$$
 c_p B^{pj}\sum_{v\le V:\,j<\tau(v)}\frac1{r_j(v)}
 \le c_p V(j+1)(B^p/3)^j.                                             \tag{5}
$$
Indeed on a fixed word of total $A$, prebirth requires at least the second positive representative, so $V>2^{A+1}$. Its exact dyadic cylinder contains at most $1+V/2^{A+1}\le V 2^{-A}$ positive sources through $V$. Use the second inequality of (3) after this count. The sum in (5) converges. In particular one may take $C_1=1+(7/12)(1-B/3)^{-2}$ since $b(r)-1\le 7/(12r)$.

## Transferring the estimate to a physical target

Any finite simple positive odd path obeys $\sum_{i<k}1/v_i\le C_*$ for an absolute constant. Here is a finite-length version of the reciprocal packing argument. Insert intermediate even values for the shortcut map $T(x)=(3x+1)/2$ at odd $x$ and $T(x)=x/2$ otherwise. The resulting path is injective: repetition among even intermediates would repeat their next odd vertex, or would repeat within one strictly decreasing even chain. For $Y\ge2$, let $d=\lfloor\log_2Y\rfloor$. At most $d$ final window starts lack $d$ available future steps. The length-$d$ parity words of odd count greater than $3d/5$ occupy at most $2^{dH_2(3/5)}$ classes modulo $2^d$, each with at most two starts up through $Y$. All other words take a start $\le Y$ to at most $3^{3d/5}Y/2^d+(3/2)^d$, by the affine formula and the all-odd bound on its constant term. These endpoints are distinct. Consequently the number of sites up through $Y$ is at most $C(1+\log Y+Y^\alpha)$ for $\alpha=\max(H_2(3/5),(3/5)\log_2 3,\log_2(3/2))<1$. Sum on dyadic shells. This argument is uniform even on a finite prefix of a bounded orbit ending at first arrival.

Since $\log b(v_i)\le7/(12v_i)$, the postbirth product on any first-arrival path is bounded by $\exp(7C_*/12)$. Its raw product in (1) is therefore at most $C' a(v)$, even when the path ends before birth. Also $g/y\le\min(1/v,q(y))$. A maximizing path can be chosen to be a first arrival, and all of its boosts are at least one. These facts give the lower inequality in (2) and the upper bound
$$
 u^{(1)}(y)\le C'\sum_{v\ {\rm odd}}a(v)\min(1/v,q(y))^s.
$$
Apply (4) up through $V=1/q(y)\ge1$ and sum the dyadic shells $v>V$ to conclude (2). Summing shells directly from $v>M$ gives the stated $O(M^{1-s})$ uniform tail. The rounded sandwich follows from the single rounding factor on the entire word in (1). A nonperiodic target can receive each source at most once.

## Limit currents on an actual escaping component

For an escaping component $C_0$ fix any ordinary ray $x_t=U^t(x)$ there. Its ancestors increase with $t$ and exhaust $C_0$. Every member's orbit is injective and avoids $1,3,5,7,9,11$, which all reach one. Define
$$
 c(v)=v^{-s}\prod_{i\ge0} b(r_i(v))
       \left(\frac{3v_i}{3v_i+1}\right)^s,\qquad
 h_{C_0}=\sum_{v\in C_0}c(v).
$$
The product exists and is positive: its finite prebirth part is positive and after birth the absolute logarithms are bounded by a constant times $1/v_i$, summable by packing. The bound $c(v)\le C'a(v)v^{-s}$ is global. In particular the positive component currents sum to a finite number by (4). At every high site $n\ge13$ one has $b(r_i)\ge b(n)>(1+1/(3n))^s$ as in PR193 (squaring the two sides gives a strictly positive difference). Each finite contribution from a fixed ancestor thus strictly increases when the endpoint advances along the ray, by the affine path identity
$$
 (g/y)^s\prod_{i<k}b(r_i)=v^{-s}\prod_{i<k}b(r_i)
       (3v_i/(3v_i+1))^s.
$$
For all sufficiently large dates it occurs, and its limit is $c(v)$. Dominated convergence proves $u(x_t)\uparrow h_{C_0}$ strictly from below.

For each $v\in C_0$ there are signed integers $j_v,d_v$ such that for every sufficiently large $t$ its unique visit to $x_t$ has length $t+j_v$ and total $A_t(x)+d_v$. They are obtained by subtracting the two cumulative clocks at any common point and are independent of which later common point is used. For $a,b\in\{0,1\}$ set
$$
 h_{C_0}^{ab}(x)=\sum_{v\in C_0}
  3^{-((a+j_v)\bmod2)/2}\,2^{-((b+d_v)\bmod2)/2}c(v).
$$
Among the four values retain exactly those corresponding to recurrent pairs $(t\bmod2,A_t(x)\bmod2)$. On a fixed recurrent pair, every retained source has constant rounding factor. Its contribution strictly increases on future returns to that pair, new sources have positive weight and the same majorant applies. Hence $u_{\mathbb Q}(x_t)$ increases strictly to $h_{C_0}^{ab}(x)$ along that subsequence. Choosing another reference ray in the component changes the two parity labels by one fixed translation once the rays merge, preserving the set of recurrent limit values. Always $h_{C_0}/\sqrt6\le h_{C_0}^{ab}(x)\le h_{C_0}$.

Finally (2) puts any positive superlevel of the first-arrival current on a positive superlevel of $q$. A maximizing visitor for $q(y)\ge c$ starts at an odd $v\le1/c$, so that whole superlevel lies on finitely many genuine forward orbits. Bounded orbits supply finitely many targets; escaping orbits merge within each component. Each component with limiting value strictly above a given positive level really has infinitely many such targets, so this finite list captures all of them. Strict increase from below excludes equality at the limiting threshold for both comparison conventions. These facts also give the asserted positive limit spectra. At positive odd multiples of three there is no incoming edge, so the current is exactly $y^{-s}$, tending to zero. The corrected-height formula of Paper 207 and the inverse-gain spectrum give $q(x_t)\to1/P$; taking limits in (2) proves the bound on $h_{C_0}$.

The estimates improve the cutoff exponent $1-s+\log_2 B$ of PR193 to $1-s$ on nonperiodic targets and identify the individual ordinary limit profiles. They give a positive component current for each escaping component, with finite total allowed. The vanishing of all those currents and the exclusion of nontrivial positive cycles remain open.

**Inputs.** PR193 fixed weight and adaptive normalization at commit 67e5cdb3c1689836bf1dc01a57a7e46b85449dcd, PR201 sibling bound at commit 807d67ab049f1646398d8ca8c20948cdc1d87742, Weaver Paper 207 for corrected heights, and the independently reviewed inverse-gain component spectrum c75d046300078cf11c2c5eecaf60a4ba7f53506514ecb1c128be2ac5085f66b2. [Adaptive Green criterion](https://github.com/GettysburgResearch/collatz/blob/67e5cdb3c1689836bf1dc01a57a7e46b85449dcd/research/astra-six-hour-20261127/global/ADAPTIVE_GREEN.md) · [Global prefix trace](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md) · [Corrected height](https://rstation.ai/problems/collatz/papers/207/v1)

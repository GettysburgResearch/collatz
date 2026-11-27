# An integer label and the complete denominator of inverse-basin differences

**PROPOSED.** For a positive odd rational cycle of coprime periods, every positive odd ancestor in its denominator lattice has an integer label. The difference of *any* two ancestors whose labels differ by one has exactly the cycle's full reduced denominator. Ancestors with the same label differ by an even integer, also on a nonordinary cycle. The labels determine how deeply a search for real near-collisions must go.

Write $p$ for the odd period and $s$ for the minimum. Combine **all** odd endpoints and all inverse paths of depth at most $K$ whose odd departures stay at least $s/3$. Their odd rational sources are pairwise at distance at least 2 whenever
$$
             2p/3+2K+6 < s\log(2)/p.                                      \tag{1}
$$
The result allows arbitrary positive valuation exponents, repeated laps and arbitrarily high intermediate and starting values. In the ordinary bounded least-disagreement alternative, every positive ancestor satisfies the floor. Along hypothetical candidates with $p^2=o(s)$, the protected depth is of order $s/p$, exceeding any fixed multiple of the period eventually. On an explicit nonordinary cycle with a 301,971-bit reduced denominator, (1) holds through **762,148 odd steps**, four entire laps, simultaneously at every endpoint. On that example the theorem concerns paths meeting the indicated floor. It makes no assertion about other paths in its basin.

## Residue and real height of an ancestor

Use $U(x)=(3x+1)/2^{v_2(3x+1)}$ on odd positive rationals with denominator prime to six. Let $x_0=s,x_1,\ldots,x_{p-1}$ be a primitive physical lap, $A_i$ its cumulative valuations, $h=A_p$, and assume $\gcd(h,p)=1$. The affine carry $C$ at $s$ gives $s=C/D$ with $D=2^h-3^p>0$. Each phase has the same reduced denominator $d=D/\gcd(D,C)$. An ancestor throughout this note lies in this same lattice: $z=n_z/d$ with odd positive numerator, allowed to be a multiple of three. A physical step preserves coprimality of the numerator with $d$, hence every such ancestor of the cycle is reduced. For $d=1$ all statements about fractional parts use the unique residue modulo one.

For $d>1$ choose integers $a,b$ with $ap+bh=1$ and put $u=2^a3^b\bmod d$. Since $2^h=3^p\bmod d$, $u^p=2$ and $u^h=3$ there. Negative powers use the unit group. This is the same rank unit as the full-determinant calculation in PR195, reduced modulo the *actual* denominator. If a source $z$ reaches $x_i$ after $k$ odd departures with total valuation $B$, define
$$
                 L(z)=(i-k)h+(B-A_i)p .                                  \tag{2}
$$
Extending the terminal segment around the lap leaves (2) unchanged, including the seam where $A_p=h$. The deterministic forward orbit makes any two choices of terminal cycle hit comparable by continuation. This proves independence of the hit and its depth. Reducing the step identities modulo $d$ gives $n_{x_i}=3^i2^{-A_i}n_s$ and $n_z=2^B3^{-k}n_{x_i}$. Therefore $n_z=n_su^{L(z)}\bmod d$.

For another source $z'$, set $t=|L(z')-L(z)|$. The exact formula, with $\operatorname{den}(0)=1$, is
$$
              \operatorname{den}(z'-z)=
                      \frac{d}{\gcd(d,u^t-1)}.                            \tag{3}
$$
Indeed the numerator difference is, up to sign and multiplication by a unit, $u^t-1$ modulo $d$. Taking the integer gcd accounts for repeated and shared prime factors. When $t=1$ every divisor common to $u-1$ and $d$ divides $u^p-1=2-1\bmod d$. Thus the whole reduced denominator survives. When $t=0$ the difference is integral and its even numerator over odd $d$ makes it even. In particular, for the sorted dyadic mantissa array with the usual factor four clearing dyadic divisions, **each individual adjacent lifted gap** retains $d$: its labels in numerator residue differ by one, since its normalized ranks are the exponents of $u$ modulo $d$, including the doubled seam. This last specialization assumes the physical rank ordering from the prior bounded-branch theorem; (2)–(3) need no sorting hypothesis.

A small-label estimate also follows as in the cyclic subgroup argument of PR195. If $t>0$ and $g=\gcd(d,u^t-1)>1$, $\langle u\rangle$ modulo $g$ has at most $t$ elements. It contains every $2^a3^b$ for $0\le a,b\le\lfloor\sqrt t\rfloor$. Two distinct such integers coincide modulo $g$, by counting and unique factorization. Hence $g\le6^{\lfloor\sqrt t\rfloor}$. This bounds how much of the complete denominator two labels can lose.

For the real constraint write $\alpha=\log_2 3$ and $\delta=(h/p)\ln2-\ln3$. On a physical step of odd valuation $e$ from $w$, the difference $\ln(U(w)/w)-\ln 3+e\ln2$ is $\ln(1+1/(3w))$. This is in $(0,1/(3s)]$ on the lap, whose mean correction is $\delta$. On a rival with every departure at least $s/3$, each correction is at most $1/s$. Summing from the anchor to $x_i$ and subtracting the sum from $z$ to $x_i$ gives
$$
 \left|\ln(z/s)-\frac{L(z)}p\ln2\right|
                 \le \frac{p/3+k}{s}.                                    \tag{4}
$$
Indeed the native $i$-term correction sum differs from $i\delta$ by at most $p/(3s)$, and the rival $k$-term sum differs from $k\delta$ by at most $k/s$. For two such points $z,z'\ge s/3$, the mean value theorem also gives $|\ln z-\ln z'|\le3|z-z'|/s$. Consequently
$$
 \frac{s\ln2}{p}|L(z)-L(z')|
              \le 2p/3+k+k'+3|z-z'|.                                    \tag{5}
$$
Under (1) a gap smaller than 2 forces equal labels. Formula (3) then forces the points to coincide. More generally for a positive integer $m$ prime to $d$, in any one rational residue class modulo $m$ there is no positive gap smaller than $m$ if $2p/3+2K+3m<s\ln2/p$. At equal labels the integral difference is divisible by $m$ because its two residues agree. This proves the simultaneous spacing statement over the whole collection, including comparisons between different depths and different endpoints.

## Exact example over four laps

Take $p=190537,h=301994$ and the cyclic mechanical valuation word with cumulative sums $A_i=\lfloor ih/p\rfloor$. Its positive periodic rational realizer has the stated exact valuations: the lap denominator and all rotated carry numerators are odd. The orbit is primitive because $p,h$ are coprime. At a base rank $r$, the prefix sums are $\lfloor(r+ih)/p\rfloor$ for $0\le r<p$. Each carry is at least the one at rank zero and less than twice it. The minimum is therefore the rank-zero phase and the odd width is less than two. The rank-one carry differs from the rank-zero carry in exactly one term because multiplication by $h$ permutes the ranks. This difference is a power of two times a power of three, coprime to $D$. The gcd with $D$ at each rank is the same by the step identity. Thus $d=D$. The Christoffel-word high-cycle exclusion is classical; here the example quantifies a property of its inverse basin. [Knight, *Collatz high cycles do not exist*, Discrete Mathematics 349 (2026)](https://doi.org/10.1016/j.disc.2025.114812)

Since $2^{h/p}>3$, each $2^{\lfloor ih/p\rfloor}\ge3^i/2$. Hence $s\ge p3^p/(6D)$. The checker certifies $3^p>81pD$ by exact integer arithmetic, so $s>(27/2)p^2$. The elementary bound $\ln2>2/3$ follows by integrating the tangent to $1/x$ at $3/2$ over $[1,2]$. With $K=4p$ and $m\le\lfloor p/10\rfloor=19053$, (5) gives the stated spacing in every residue class prime to $d$. This proof covers the full floor-clipped inverse tree to those depths without enumerating it. The data also compare (3) on 47,571 pairs of actual rational sources of three smaller cycles; all three give adjacent-label pairs, and two exhibit proper partial denominator loss.

## Searching all exponents on a supplied ordinary window

For the least tripling disagreement $q$, put $s=(3q-1)/2$. Every bad positive ancestor obeys $4z\ge3s+1$, and every bad multiple of three is at least $2s+1$. In a reverse search for the **first violation**, the departures after the initial source in forward order satisfy the ordinary floor. The initial departure still satisfies $3z\ge s$ for $s\ge3$, since its successor $w$ obeys $4w\ge3s+1$ and $3z=2^e w-1\ge2w-1$. The violating source has $z\le2s$.

For a forward path from $z$ to $y$ with $k$ odd departures of height at least $s/3$ and valuation sum $B$, the following integer inequalities hold for $12k\le s$, $s>0$, $z\le2s$:
$$
                3^k z\ \le\ 2^B y\ \le\ 3^k(z+3k).                      \tag{6}
$$
One proof multiplies the correction bound $1+1/s$ and uses $(1+1/s)^k\le s/(s-k)$ for $k<s$. The stronger integer inequality $(s-k)2^B y\le s3^kz$ follows directly by induction, also formalized. The bound $z\le2s$ then gives (6). There is no constraint on the maximum height of the rival.

For a native path of the same $k,y$ from $x\in[s,2s)$ staying in that single octave, let $A$ be its cost. Its correction uses the stronger floor $s$, so $x\le2^Ay/3^k\le x+k$ by the same argument with floor parameter $3s$. With the preceding first-crossing bounds, $2^{B-A}$ lies strictly between $1/8$ and $4$. Indeed the two positive ideal starting values lie respectively in $[s/3,2s+3k]$ and $[s,2s+k]$. Thus $j=B-A\in\{-2,-1,0,1\}$, and
$$
                       |z-2^j x|\le3k.                                   \tag{7}
$$
The two errors have the same sign; subtracting them costs at most their larger bound. For a general native strip $x\in[s,6s]$ there are still only boundedly many $j$ and $O(k)$ offsets, by the same argument. For fixed ordinary $x$ it suffices to replay forward from the resulting $O(k)$ source integers, stopping as soon as the clock budget cannot hold. This takes $O(k^2)$ odd-step operations per supplied depth and endpoint. The claim is about arithmetic operation counts; input integers, moduli and long shifts have nonconstant bit cost.

[The checker](check.py) constructs a whole ordinary progression with cumulative native exponents $\lfloor i\log_2 3\rfloor$ around its central minimum. It tests every depth through 384 at the eight endpoints at times zero through seven. It starts one native phase earlier than required and chooses a binary lift stride with enough factors of two and three to preserve every shifted source residue. Both intercepts and slopes put all native phases in the single octave. For each $j$ the algorithm retains every potentially illicit source in (7), including boundary equalities. Along a lift each source has the exact prescribed slope $2^j$ times the native starting slope. Its low $B+1$ bits and residue modulo three are fixed. An intermediate floor or terminal source rejection must hold on the entire progression. If the $k$ valuations sum to $B$, endpoint slopes coincide, so base equality is the only remaining merger test. No forbidden ancestor appeared. This extends a finite ordinary avoidance control; these are varying positive sources with a common finite description, and none is asserted bad or periodic.

## Evidence, literature and remaining inference

Applegate and Lagarias study physical inverse trees cut by clock and residue; their Theorem 4.1 supplies a certificate for a ones ratio of $14/29$. The theorem does not ensure a competitor below the floor at one chosen least bad endpoint. The argument here instead compares arbitrary ordinary or rational inverse paths to the actual full cycle, retaining complete denominator residues and real height together. [Primary paper, §§2–4](https://arxiv.org/abs/math/0103054)

The bounded ordinary strip, coprimality and $p^2=o(s)$ are inherited from the pinned PR205 and the PR195 rank proof. PR195 round 11 provides a two-filter local whole-divisor test, and round 12 bounds determinant absorption by low-complexity factors. Formula (3) measures the full denominator of a difference of arbitrary ancestors and (5) controls when their real coordinates can come close. The known goodness of $x-1$ on every bounded bad-cycle phase is already in PR195 round 9. The earlier PR193 mechanical test checks 60 depths at eight endpoints. [PR205 height bound](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md) · [PR195 rank order](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round9/critical/README.md) · [PR195 round 11](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round11/cycle/README.md) · [PR195 round 12](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/cycle/README.md) · [PR193 mechanical comparison](https://github.com/GettysburgResearch/collatz/blob/aa0b01234735683b413098b81afdf764de503730/research/astra-closure-20261125/cycles/MERGER.md)

The Lean file proves the unrolled integer distortion and source interval, the first-crossing lower bound, same-clock cancellation, the full gcd of a labeled numerator difference in the stated orientation, and the adjacent-label unit assertion. The global label construction, logarithmic estimate, packing theorem, mechanical-word derivation and asymptotic application have written proofs. Universal bounded-cycle exclusion remains **OPEN**: no argument forces a bad cycle to have a forbidden ancestor, a nonintegral adjacent-label difference, or a sufficiently deep cross-label near-collision. The first-crossing alternative outside this cycle remains open independently. [Lean kernels](InverseOffsets.lean) · [Finite controls](../../../reports/astra-literature-closure-20261125/cycle/control.json) · [Strict Lean output](../../../reports/astra-literature-closure-20261125/cycle/lean.log)

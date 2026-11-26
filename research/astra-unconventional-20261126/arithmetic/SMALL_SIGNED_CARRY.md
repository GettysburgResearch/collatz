# A nonzero polylogarithmic signed carry on every bounded candidate

Use the increasing folded ranks $Z_r$, physical marks $c_r$, rank period $p$, shortcut period $h$ and odd minimum $s$ of [the bounded-branch theorem](README.md). Extend both arrays to all $r\in\mathbb Z$ by $Z_{r+p}=2Z_r$, $c_{r+p}=2c_r$. Write $T$ for the rank shift $Tf(r)=f(r+1)$. Then $T^h Z=3Z+c$ exactly.

**Proposition.** Along any such family $p\to\infty$, there exist a nonzero signed rank jump $t$, an integer $1\le\ell=O(\log p)$ and a nonzero polynomial $Q$ of degree $L=O(\log p)$ with coefficients in $\{-1,0,1\}$ such that $t\equiv\ell h\pmod p$, $L|t|<p/2$, and
$$
 H=2Q(T^t)Z,\qquad J=2Q(T^t)c
$$
are integral on base ranks $0\le r<p$, obey the same twisted extension and satisfy
$$
 H\ne0,\qquad \max_r |H_r|=O((\log p)^3),\qquad
 \max_r |J_r|=O(\log p),\qquad T^hH=3H+J .
$$
Constants may use the pinned polynomial bound $s\ll p^{5.12}$. The stencil is identical at every phase of the physical cycle. The resulting arrays are signed. In particular $H$ need not consist of positive ordinary Collatz states.

Choose $L=\lceil10\log_2 p\rceil$ and $U=4L$. Applying the pigeonhole principle to $0,h/p,\ldots,Uh/p$ modulo one gives $1\le\ell\le U$ with $\|\ell h/p\|\le1/U$. The rank/period coprimality and $U<p$ give a nonzero signed residue $t$ with $|t|\le p/U$. Put $\beta=2^{t/p}$. All powers $\beta^j$ for $0\le j\le L$ lie in $[2^{-1/4},2^{1/4}]$. The $2^{L+1}$ real subset sums of these powers lie in an interval of length $O(L)$. Two sums are within $O(L)2^{-L}$, giving a nonzero integer polynomial $Q$ with coefficients in $\{-1,0,1\}$ and $|Q(\beta)|\ll L2^{-L}$. Distinct subsets cannot have exactly equal sums here, as shown below.

For fixed $r$ and $0\le j\le L$, rank $r+jt$ is reached after $j\ell$ chronological odd steps, up to a whole rank period. The normalized amplitude $Z_r2^{-r/p}$ is periodic in rank. Its change along these $j\ell$ chronological steps is $O(j\ell)$ by the frozen-amplitude one-step bound. Since $(r+jt)/p$ stays in $[-1/4,5/4]$ on the base period, this gives
$$
 Z_{r+jt}=\beta^j Z_r+O(j\ell).
$$
Summing over the stencil yields $|Q(T^t)Z_r|\ll sL2^{-L}+\ell L^2$. Every shifted rank lies in the preceding, current, or following period. The fixed multiplier 2 clears all negative-rank denominators and $|Q(T^t)c_r|\ll L$. Translations commute on the lifted arrays, so applying $2Q(T^t)$ to $T^h Z=3Z+c$ gives the stated recurrence, including seams. On base ranks it reads $2^{\lfloor(r+h)/p\rfloor} H_{(r+h)\bmod p}=3H_r+J_r$.

It remains to verify that $Q(T^t)$ cannot annihilate the physical array. On the $p$-dimensional rational space of twisted arrays, $T^p=2$ and $T$ is diagonalizable over $\mathbb C$, with eigenvalues the roots of $X^p-2$ (the companion matrix in the base-rank coordinates). Put $g=\gcd(p,|t|)$, $q=p/g$ and $a=t/g$. The numbers $\alpha^t$ as $\alpha$ ranges over these roots are the $q$ roots of $Y^q-2^a$. The field $\mathbb Q(2^{a/q})$ equals $\mathbb Q(2^{1/q})$ by Bézout and $\gcd(a,q)=1$, including negative $a$. The latter field has degree $q$ by Eisenstein for $X^q-2$. Thus all the $\alpha^t$ have degree $q\ge p/|t|\ge U>L$, and no one is a root of $Q$. The stencil is an invertible operator on the twisted arrays. The original $Z$ is nonzero, hence so is $H$.

There are $O((\log p)^3)$ potential signed carry values across the $p$ physical phase indices. The small alphabet does not force deterministic evolution of $H$: the term $J_r$ is a sum of physical marks at the stencil positions, and its possible values permit branching. A period bound for positive Collatz cycles does not follow from this small-height recurrence.

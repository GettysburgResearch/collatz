# A common real shift for cyclic arc intersections

Let $x_0,\ldots,x_{h-1}$ be the distinct positive states of a primitive shortcut Collatz cycle. Write $b_i\in\{0,1\}$ for its parity, $2x_{i+1}=3^{b_i}x_i+b_i$, $p=\sum b_i$ and $g=h\log 2-p\log 3$. Indices belong to $\mathbb Z/h$. Sections 1–3 also hold for positive cycles with rational odd denominator and the same native branches. All statements concern actual affine states. Sections 1 and 2 allow coprime $h,p$ and arbitrarily many mismatches between any two rotations.

For any two proper lags $r,s$, two length-$r$ arcs at cyclic distance $s$ have exactly equal multiplicative losses after adding **one common number** $t\in[1/4,1/2]$ to all four endpoint heights. This $t$ has degree at most two. The shift generally depends on both lags and the phase. In every primitive integer cycle, the crossing shifts already required for $r=1$ and distinct unoriented $s$ are pairwise different quadratic irrationals.

## 1. Transport of the loss vector

For $0<t<1$ define

\[
 \ell_i(t)=\log\frac{2(x_{i+1}+t)}{3^{b_i}(x_i+t)},\qquad
 d(x)=\log\frac{x+1/2}{x+1/4}.
\]

The gain inside the logarithm is $1+t/(x_i+t)$ on an even branch and $1+(1-t)/(3(x_i+t))$ on an odd branch. Both losses are strictly positive. The full lap telescopes to $\sum_i\ell_i(t)=g$. The exact affine identity $4x_{i+1}+1=3^{b_i}(2x_i+1)$ gives

\[
 \ell_i(1/4)=d(x_i),\qquad \ell_i(1/2)=d(x_{i+1}).                       \tag{1}
\]

The first equality follows by inserting $x_{i+1}+1/4=3^{b_i}(x_i+1/2)/2$. In the second equality the same substitution cancels the denominator $3^{b_i}(x_i+1/2)$. The underlying integer identity appears in the packet's [shifted-step kernel](../root/CofactorDescent.lean).

Let $K=(k_0,\ldots,k_{h-1})$ be any real filter, and put $F_i(t)=\sum_j k_j\ell_{i+j}(t)-g\sum_j k_j/h$. Then $\sum_i F_i(t)=0$ and $F_i(1/2)=F_{i+1}(1/4)$. The finite list $F_i(1/4)$ either has a zero or contains consecutive terms of opposite signs, including the wrap-around edge. Continuity gives some $i$ and $t\in[1/4,1/2]$ with $F_i(t)=0$.

## 2. Single arcs and pairs of arcs

Write $u_{i,r}=\sum_{0\le j<r}b_{i+j}$. Apply the filter principle to an $r$-block. For every $0<r<h$ some $i,t$ satisfy

\[
 \frac{x_{i+r}+t}{x_i+t}=3^{u_{i,r}-rp/h}.                               \tag{2}
\]

If $h\mid rp$, its exponent is a nonzero integer, since the two states differ. Writing $x<y$ for the two integer states and $k=|u_{i,r}-rp/h|$, this yields

\[
 y=3^k x+d,\qquad (3^k-1)/4\le d\le(3^k-1)/2,\qquad d\in\mathbb Z.        \tag{3}
\]

For $k=1$, necessarily $d=1$ and $t=1/2$. The smaller $x$ is even, since an odd $x$ and $3x+1$ have the same shortcut successor. When $h\nmid rp$, write the exponent in lowest terms with denominator $n=h/\gcd(h,rp)$. The ratio in (2) has degree $n$ over $\mathbb Q$. Indeed a Bézout identity recovers $3^{1/n}$ from the ratio and rational powers of $3$, and $X^n-3$ is Eisenstein. The distinct rational endpoints make the ratio an invertible fractional linear function of $t$. Consequently $t$ itself has degree exactly $n$. A bounded degree in (2) cannot be asserted at general coprime clocks.

Instead apply the difference of the length-$r$ filters starting at offsets $0$ and $s$. For **every** $0<r,s<h$ some phase $i$ and a common real $t\in[1/4,1/2]$ satisfy

\[
 (x_{i+r}+t)(x_{i+s}+t)
   =3^{u_{i,r}-u_{i+s,r}}(x_i+t)(x_{i+s+r}+t).                            \tag{4}
\]

The resulting polynomial has rational coefficients and degree at most two. It is nonzero. Different leading coefficients settle the case of a nonzero exponent. If the exponent vanishes, an identically zero polynomial would give identical unordered pairs of roots and therefore place $i$ in $\{i+r,i+s\}$, contrary to both lags being proper. Hence the witness has degree at most two for every clock. A zero exponent gives a unique rational shift and the exact near-product relation

\[
  |x_{i+r}x_{i+s}-x_ix_{i+s+r}|
   = t\,|x_{i+r}+x_{i+s}-x_i-x_{i+s+r}|.                                \tag{5}
\]

A zero exponent is substantive. For the positive primitive rational circle with denominator $101$ and successive numerators $304,152,76,38,19,79,169$, take $r=2,s=3$. Its physical word is $0000111$, with coprime $h=7,p=3$. Among phases with equal odd counts the only candidate root is $-75/58$. The theorem still gives an in-interval witness with unequal counts. This example has four distinct arc endpoints. For integer cycles the elementary obstruction in §3 also applies at $r=1$.

## 3. Rigidity and noncoordination for one-step arcs

Fix $r=1$ on a primitive positive integer cycle. Two even losses are unequal because $x\mapsto t/(x+t)$ is strictly decreasing. The same argument holds for two odd losses. Write $e$ for the even and $o$ for the odd state in a crossing pair. Equality of the two losses is exactly

\[
 P_{e,o}(t)=4t^2+(e+3o-1)t-e=0.                                           \tag{6}
\]

This polynomial is strictly increasing for $t\ge0$. Its values at $1/4$ and $1/2$ are $3(o-e)/4$ and $(3o+1-e)/2$. Thus there is an in-interval crossing precisely for $o\le e\le3o+1$. Distinct parity excludes $o=e$. The endpoint $e=3o+1$ is impossible on a cycle because it would give $T(e)=T(o)$. Every crossing therefore has

\[
 o<e<3o+1,\qquad 1/4<t<1/2.
\]

The rational-root theorem would force the denominator of a rational $t$ to divide $4$. There is no such rational in this open interval. Thus every crossing is a quadratic irrational. Moreover, two monic normalizations of (6) sharing this irrational root must coincide. The constant coefficient recovers $e$, and the linear coefficient then recovers $o$. A fixed $t$ witnesses at most one unordered pair, even when all positive integers across all cycles are considered. In the rescaled coordinate $v=2t$, the witness is an algebraic integer with norm $-e$ and lies strictly between $1/2$ and $1$.

For every unoriented proper lag class $\{s,-s\}$, (4) supplies a crossing pair. Distinct lag classes require distinct pairs and hence distinct $t$. Every primitive integer cycle has at least $\lfloor h/2\rfloor$ distinct quadratic shifts already on its one-step arcs. In particular two lag classes cannot be synchronized by allowing their phases to vary. The known cycle $(1,2)$ gives $P(t)=4t^2+4t-2$ and $t=(\sqrt3-1)/2$.

## 4. Fixed rational shifts and equal counts

At $t=1/3$ all four factors $3x+1$ in (4) are units modulo $3$. Therefore any exact pair collision at this fixed shift must have $u_{i,r}=u_{j,r}$. In the affine formula $2^r x_{i+r}=3^u x_i+C_i$ put

\[
 H_i=2^r+3C_i-3^u>0,\qquad
 \frac{2^r(3x_{i+r}+1)}{3^u(3x_i+1)}=1+\frac{H_i}{3^u(3x_i+1)}.            \tag{7}
\]

Positivity follows from the native losses. For equal counts, equality at this shift is equivalent to $(3x_i+1)/(3x_j+1)=H_i/H_j$. Identical $r$-words have $H_i=H_j$ and cannot collide at distinct phases. Thus an exact collision at $1/3$ would identify a ratio of distinct affine carries with a ratio of actual integer cofactors. The variable-shift theorem does not force such a collision. At $r=1$ it proves that none occurs. No upper bound on the physical diagonal moment or full-denominator exclusion for arbitrary primitive integer words follows from (4).

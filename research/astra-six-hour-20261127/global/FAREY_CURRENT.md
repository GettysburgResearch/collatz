# Integer Farey intervals on a complete cycle or escaping ray

**PROPOSED, written deduction.** Write $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. Each edge $x\to y$ has $d=2^{v_2(3x+1)}$ and
$$d y-3x=1.$$
Thus $3/y<d/x$ are reduced Farey neighbours. This ordinary unimodularity is lost by clearing a common denominator $D>1$ on a rational cycle: the resulting determinant is $D$ before any primitive cancellations. The conclusions below retain the actual states and their actual clocks.

## The cone at every integer scale

For every integer $t\ge0$ one has
$$
 \left\lfloor{dt\over x}\right\rfloor-
 \left\lfloor{3t\over y}\right\rfloor
 =\#\{(r,s)\in\mathbb Z^2:r\ge1,\ s\ge0,\ t=rx+sy\}.                    \tag{1}
$$
The integers $j$ between the two slopes, excluding the lower and including the upper boundary, correspond by $r=yj-3t$, $s=dt-xj$ to the indicated nonnegative coordinates. The inverse is $(t,j)=(rx+sy,rd+3s)$. In particular the level $t=x$ is the first positive level with a nonzero count; it counts one. The entire local generating function is $z^x/((1-z^x)(1-z^y))$.

On a simple positive cycle $x_i$ (cyclic indices) equation (1) sums to the exact positive current
$$
 \sum_i\left(\left\lfloor{d_i t\over x_i}\right\rfloor-
                   \left\lfloor{3t\over x_i}\right\rfloor\right)
 =\sum_i\#\{r\ge1,s\ge0:t=rx_i+sx_{i+1}\}.                              \tag{2}
$$
It vanishes identically for $t<N=\min x_i$ and equals one at $t=N$. For an infinite injective odd ray $x_0,x_1,\ldots$, (2) instead has the extra term $+\lfloor3t/x_0\rfloor$ on the left. Both sides are finite at each $t$: the ray tends to infinity and $d_i/x_i=3/x_{i+1}+1/(x_i x_{i+1})$. Thus its pointwise sums first telescope on an actual finite path. No interchange in a probability law is involved.

## A positive angular sum with an unbounded torsion order

Put $e(z)=\exp(2\pi i z)$. For every finite path,
$$
 \prod_i{e(d_i/x_i)\over e(3/x_{i+1})}
     =e(\Delta),\qquad
 \Delta=\sum_i{1\over x_i x_{i+1}}>0.                                    \tag{3}
$$
When the states are odd units modulo three, the two phases compared on its edge are primitive roots of respective orders $x_i,x_{i+1}$. Their quotient is primitive of order **exactly** $x_i x_{i+1}$ by the determinant identity. The two endpoint cyclotomic fields are linearly disjoint. At an edge with $x_i,x_{i+1}>1$, $1-e(1/(x_i x_{i+1}))$ is a global cyclotomic unit, because $x_i,x_{i+1}$ are coprime and their product is not a prime power. These properties concern every physical edge, including edges at which $d_i$ is unbounded.

For a simple cycle, or any nonempty interval of an injective ray whose states are all at least $N>2$, the whole angular sum satisfies
$$
 0<\Delta \le\sum_{j\ge0}(N+2j)^{-2}
 \le N^{-2}+{1\over 2N} < {1\over N}.
$$
Here $N$ can be taken odd. The estimate uses $1/(xy)\le(x^{-2}+y^{-2})/2$ and counts each distinct odd state at most twice with weight one-half. With $Q$ the reduced denominator of $\Delta$, this proves **$Q>N$**, uniformly in the number of physical edges. Since each adjacent pair is coprime, $Q$ divides the least common multiple of all the states, hence is prime to six on an odd-unit path. Over a full cycle the same phase is the exact product $\prod_i e((d_i-3)/x_i)$.

This gives an obstruction to retaining the small principal angle while using a bounded torsion field. If $e(\Delta)$ lay in a multiquadratic field, its cyclotomic Galois group would have exponent at most two. An odd prime $p\mid Q$ must then have $p-1\le2$, incompatible with $(Q,6)=1$. Even $\cos(2\pi\Delta)$ cannot lie in a multiquadratic field for $N\ge5$. Indeed its field is the maximal real cyclotomic subfield. At an odd prime power $p^a\mid Q$, the real quotient of the cyclic group of order $\varphi(p^a)$ must have exponent at most two. As $p\ge5$, this permits only $p^a=5$, forcing $Q\mid5$. More generally the orders of both $2$ and $3$ modulo $Q$ grow at least as $\log_2(Q+1)$ and $\log_3(Q+1)$ respectively. At fixed $Q$ the norms of the two clocks' multiplicative phase ratios across the group they generate are one. This conjugate averaging cannot assert that the small principal angle is zero.

This global calculation tests a possible replacement for PR192's two-place Rogers correction. The genuine integer Farey relation supplies a small positive torsion angle on every proposed high cycle, but its torsion order must grow, whereas the multiquadratic Rogers argument requires a fixed gap. This does not prove that all other regulator constructions fail.

## What the positive modular word records

Let $L=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $R=\begin{pmatrix}1&0\\1&1\end{pmatrix}$. Put $k=\lfloor x/d\rfloor=\lfloor y/3\rfloor$. The two exact positive factorizations are
$$
 \begin{pmatrix}d&3\\ x&y\end{pmatrix}
 =
 \begin{cases}
 R^k L^3 R^{(d-1)/3},& d\equiv1\pmod3,\\
 R^k L R L R^{(d-2)/3},&d\equiv2\pmod3 .
 \end{cases}                                                            \tag{4}
$$
In the first case $y=3k+1$, $x=dk+(d-1)/3$. In the second $y=3k+2$, $x=dk+(2d-1)/3$. In particular the long Euclidean quotient is exactly the next ordinary state divided by three and rounded down. The elementary Dedekind reciprocity for this matrix reduces to
$$12\bigl(s(d,x)-s(3,y)\bigr)=x/y+y/x+1/(xy)-3.$$
Here $s$ is the classical Dedekind sum. This follows from ordinary reciprocity for $s(x,y)+s(y,x)$, $x^{-1}\equiv-3\pmod y$, $y^{-1}\equiv d\pmod x$ and the oddness of the first argument. Both (4) and the reciprocity identity already hold on one edge. Multiplying the positive modular matrices around a cycle does not make their product the identity.

The first missing global input is a sign or arithmetic restriction on the complete ordinary current that conflicts with (2) or (3). The floor positivity is a consequence of the Farey determinant, and the Galois average discards the principal sign. A full positive cycle or an escaping ordinary source is not excluded here.

### Sources

* PR192, ed7a6fe30b8602407f77855ceb74ce0489ce9c10, [two-place construction](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/adelic/REGULATOR_REPAIR.md), R1–R4, and [local units](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/adelic/LOCAL_UNITS.md), U5–U7. The Bloch boundary and the angle (3) are different objects.

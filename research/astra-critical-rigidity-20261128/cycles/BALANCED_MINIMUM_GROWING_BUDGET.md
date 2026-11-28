# A diverging mismatch multiple above the ordinary balanced-minimum threshold

Let \(m\) be the least odd state of a primitive positive integer Collatz cycle of odd period \(p\). Let \(m_{\rm bal}\) be the minimum of the positive rational floor-mechanical cycle at the same odd period and total division count, allowing repeated floor phases. With the same pinned ordinary pressure constant as in the [balanced-minimum theorem](BALANCED_MINIMUM_ROTATIONS.md), for every fixed \(\epsilon>0\) on growing periods,
\[
    m/m_{\rm bal}\ge 0.96355/2+\epsilon
        \quad\Longrightarrow\quad
         \min_{\ell\ne0}\frac{s_\ell\log p}{p}\longrightarrow\infty .    \tag{1}
\]
More precisely, if \(s_\ell\log p=O(p)\) along a sequence, rotation orders \(M=p/\gcd(p,\ell)\to\infty\) give \(m/m_{\rm bal}\to0\). At each fixed order \(M\ge2\),
\[
                \limsup m/m_{\rm bal} \le (1-2\log(2)u)/M
                                      <0.96355/M,                         \tag{2}
\]
where \(u>263/10000\) is the cost threshold in the PR213 pressure proof and \(\log\) is natural in the constant. The preceding theorem required \(s_\ell\log p=o(p)\) for (2), yielding a positive lower multiple instead of (1)'s divergence. The hypothesis of a large minimum relative to the floor cycle remains necessary for this deduction.

As before, positive ordinary minima tend to infinity with the least period, \(m\ll p^{5.116201}\) by the published two-logarithm bound, and the true lap product compared with the balanced reference gives
\[
              m/m_{\rm bal}=2\log(2)\,\frac1p\sum_i m/x_i+o(1).           \tag{3}
\]
The previous proof supplies these statements uniformly in the highest state. [Balanced angle and reciprocal identities](BALANCED_MINIMUM_ROTATIONS.md) · [BLS, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

Assume \(s_\ell\log p=O(p)\). By the [uniform paired-height theorem](UNIFORM_ROTATION_HEIGHT.md), at any fixed polynomial cutoff \(Y_0=p^C\) the fraction of odd dates with both \(x_i,x_{i+\ell}\le Y_0\) tends to zero. Its translate estimate applies at the same cutoff. For orders tending to infinity it gives \(\#\{i:x_i\le p^{12}\}=o(p)\), so (3) and \(m/p^{12}=o(1)\) prove the growing-order assertion.

For fixed \(M\), write \(d=p/M\). Take the least state \(z_r\) in each fiber \(\{r+jd:0\le j<M\}\), indexed by \(r\bmod d\). Only \(o(d)\) fibers contain two states below any chosen fixed polynomial cutoff, by testing each of the finitely many nontrivial \(j\ell\) in the paired-height theorem. The other fibers have all their nonminimal states above \(p^{12}\). It follows that
\[
                \frac1p\sum_i m/x_i=\frac1p\sum_r m/z_r+o(1).            \tag{4}
\]

Call the departure \(r\) a join if the physical successor of \(z_r\) is different from \(z_{r+1}\). On a column where all exponents agree, their common affine map has positive slope and preserves the minimum. The number of joins is therefore at most \(s_\ell/2=o(d)\), since a nonconstant circular list of exponents in a fiber has at least two adjacent mismatches in the order induced by \(\ell\). In all cases \(z_{r+1}+1\le(3/2)(z_r+1)\). At a join, both the successor of \(z_r\) and the new minimum \(z_{r+1}\) are distinct actual states in the arrival fiber.

Write \(f_r=\{\log_2(z_r/m)\}\), \(G_r=\lfloor\log_2(z_r/m)\rfloor\), \(D_r=(1-2^{-G_r})2^{-f_r}\). Away from actual joins, the angles advance modulo one by \(\log_2 3+O(1/m)\); the proportion of joins tends to zero. The empirical angles tend to Haar by the fixed-character telescoping argument in the preceding balanced-minimum theorem. In particular \(\frac1d\sum 2^{-f_r}\to1/(2\log2)\).

## Covering the joins on the pressure window scale

The input from PR213 is the following count on the original ordinary cycle. For \(n=\lceil\log_3 m\rceil+2\), among all \(p\) origins only \(o(p)\) have mean \(D\)-cost at most \(u\) on their next \(n\) actual odd states. This statement retains the individual ordinary origins. [PR213 at 5ac2b4a, pressure proof and exact constant](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/ODD_HEIGHT_PRESSURE.md)

Choose this \(u\) below \(1/4\), as permitted by the cited threshold. Put \(Y=p^{12}\). Since \(m\ll p^{5.116201}\), one has \((3/2)^{n+1}=O(p^2)\). All intervals below are cyclic intervals on the \(d\) fiber columns; eventually \(n<d\).

* At a join with departure \(z_r\le Y\), the two distinct arrival states just described and all their next \(n-1\) separate successors have size \(O(p^{14})\), by one-step growth. At each date they occupy the same fiber, with distinct labels by primitivity. Hence the union of the forward intervals \([r+1,r+n]\) over such joins has size \(o(d)\), because every such fiber contains two states below \(p^{15}\). The union of \([r+1-n,r]\) has the same size, by translating all intervals by \(-n\). This covers all origins whose \(n\)-state window crosses a join of this kind.
* At a join with \(z_r>Y\), every \(t\in[r+1-n,r]\) satisfies \(z_t+1\ge(z_r+1)/(3/2)^n\gg p^{10}\). On the union \(E\) of these backwards intervals one has \(D_t=2^{-f_t}-m/z_t\ge1/2-o(1)\) uniformly. The starts of \(n\)-state windows meeting \(E\) lie in \(E-\{0,\ldots,n-1\}\), whose size is at most \(2|E|\). Indeed each interval \([r+1-n,r]\) enlarged on its left by \(n-1\) is covered by that interval and its translate by \(1-n\). This also accounts for arbitrary clustering of the joins.

For every start outside the two exceptional unions, its whole window consists of actual physical edges of the original integer cycle, and every state in that window lies outside \(E\). Its initial phase \(z_t\) is different at different columns. The original pressure count leaves only \(o(p)=o(d)\) further starts whose window has mean cost at most \(u\). Summing over the remaining windows charges each cost outside \(E\) at most \(n\) times. Therefore
\[
 \sum_{t\notin E}D_t\ge u(d-2|E|-o(d)),\qquad
 \sum_{t\in E}D_t\ge (1/2-o(1))|E|.
\]
Since \(2u<1/2\), the total lower bound is \(ud-o(d)\). This argument only uses a negligible union at the joins whose departure is polynomially small. It allows the total number of all joins times \(n\) to be comparable to \(d\).

Now \(m/z_r=2^{-f_r}-D_r\). The Haar limit and (3)–(4) give (2). To prove the uniform statement (1), a sequence of lags with \(s_\ell\log p/p\) bounded has a subsequence of constant order or of order tending to infinity, both contradicting the given strict margin.

[Exact join-window checker](check_uniform_rotation_height.py) · [Finite receipt](uniform_rotation_height_controls.json). It exercises 4,617 cyclic low/high buffer systems on actual reduced rational orbits, including 799 nonempty high buffers, 3,992 nonempty low buffers and 197 retained windows meeting the finite test threshold. The analytic pressure input concerns ordinary integers.

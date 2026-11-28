# The ordinary endpoint cloud on the actual physical clock

**PROPOSED, source-qualified written theorem.** For the uniform positive source through \(X\), write \(p_t(y)=P_X(T^t n=y)\). Put \(D_0=\log(4/3)\), \(\kappa=D_0/2\), \(L=\log X\), \(\mu=1/\kappa\), \(b=\sigma\sqrt L\), \(\sigma^2=2(\log3)^2/D_0^3\). Suppose \((t-\mu L)/b\to v\in[-\infty,+\infty]\). For every real \(q>1\),
\[
 b^{q-1}\sum_{y\ {\rm nonperiodic}}p_t(y)^q
   \longrightarrow
    \left(\int_{-\infty}^{v}\phi(z)^q\,dz\right)
     \sum_{C\ {\rm escaping}}\int_0^1 K_C(\theta)^q\,d\theta ,          \tag{1}
\]
where \(\phi\) is the standard Gaussian density. For each escaping component \(C\), the continuous positive one-periodic function \(K_C\) has mean equal to its ordinary source density \(d_C\). It retains the exact positive affine correction. If \(p_t\) is replaced by the time average \(W^{-1}\sum_{h=0}^{W-1}p_{t+h}\), for any integers \(W\to\infty\), \(W=o(b)\), the same formula holds with \(\int K_C^q\) replaced by \(d_C^q\). Earlier work gave the uniform upper order and a matching positive lower order at supercritical clocks under escape. Equation (1) gives the coefficient and includes the critical window and uncrossed population. [PR213, native endpoint atoms](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md)

## Local physical-clock profile

Choose a reference odd ternary unit \(a\) on an escaping component. Let \(P(a)=a/F(a)\), where \(F(a)\) is the convergent entire future product of \(3x/(3x+1)\) on its odd departures. Let \(H_C>0\) be the limiting stationary charge and \(\eta_C\) its canonical bilateral product law. These are the normalization and probability measure of the native marked-row inputs. They satisfy \(\operatorname{supp}\eta_C\subset[c,1]\) for an absolute \(c>0\), and \(\eta_C\) is atomless. Define
\[
 A(\theta,u)=\sum_{k\in\mathbb Z}3^{\theta-k}{\bf1}_{u3^{\theta-k}\le1},
 \qquad
 K_C(\theta)=\frac{H_C\log3}{\kappa}\int A(\theta,u)\,d\eta_C(u).       \tag{2}
\]
The geometric sum lies in \([1/(2u),3/(2u)]\). Its circle mean is \(1/(u\log3)\). Atomlessness and dominated convergence give continuity in \(\theta\); the phase shift from changing the reference is accounted for by its height \(P(a)\). The signed physical clock \(D_C(n)=i-j\) is defined by \(T^in=T^ja\). Uniformly for integers \(s\) with \(|s-\mu L|\le B b\), at each fixed \(B\),
\[
 bP_X(n\in C,\ D_C(n)=s)=
   \phi((s-\mu L)/b)K_C\!\left(\log_3(P(a)2^s/X)\right)+o(1).         \tag{3}
\]
The unbounded physical height enters only inside the displayed phase; it can equivalently be evaluated by reducing its logarithm modulo one.

To prove (3), use an odd physical waypoint \(w=T^Ja\) on the same ray, with \(J\) initially fixed. On \(B_w\), \(D_C=\tau_w-J\). For odd starts, the first-hit row at odd grade \(k\) and physical time \(s'=s+J\) has true count divided by \(p=w2^{s'}/3^k\) asymptotic to \((h(w)/w)g_k(s')\) on compact standardized central ranges. Here \(g_k(s')=2^{-s'}\binom{s'-1}{k-1}\). The row-normalized real mark \(x/p\) tends to a common probability \(V_w\) independently of the bounded standardized total. The scaled law \(F(w)V_w\), meaning pushforward by multiplication by \(F(w)\), is denoted \(\nu_w\). The fixed-root mark is atomless, and along the ray \(\nu_w\to\eta_C\) in total variation and \(h(w)/P(w)\to H_C\). The fixed-root convergence of distribution functions is uniform in the cut point by continuity of the limiting distribution. Compact standardized ranges are uniform by the subsequence form of the row input. [PR213 fixed-root marks, atomlessness and along-ray convergence](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/collision_source_marks.md) · [Pinned-root bridge including the real mark](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/inverse/pinned_root_bridge.md)

Fix \(\epsilon>0\). For \(\epsilon X\le p\le X/c\) there are \(O_{\epsilon,c}(1)\) grades at any single clock; \(k=L/D_0+O_B(\sqrt L)\) and \(s'-2k=O_B(\sqrt k)\) there. Stirling's formula, with \(z=(s-\mu L)/b\), gives uniformly on these grades
\[
          b g_k(s')=(\log3/D_0)\phi(z)+o(1).
\]
There is no contribution through \(X\) from \(p>X/c\). For \(p<\epsilon X\) all the corresponding starts lie below \(\epsilon X\). Their count divided by \(X\) is \(O(\epsilon/b)\) for fixed \(\epsilon\), by the uniform first-clock atom bound applied at \(\epsilon X\) (with an absolute eventual constant). On the limiting side the omitted geometric sum is \(O(\epsilon)\). Thus summing the single-clock rows gives the odd-source contribution via the factor \(A(\log_3(w2^{s'}/X),u)\) integrated against \(V_w\).

For all positive sources, decompose \(n=2^e x\), \(x\) odd. At fixed \(e\) the odd-source cutoff is \(X/2^e\) and its clock \(s'-e\), so **the phase is exactly the same**:
\[
    w2^{s'-e}/(X/2^e)=w2^{s'}/X .
\]
The corresponding ordinary count normalization acquires \(2^{-e}\). For \(e>E\) with \(2^e\le\sqrt X\), the uniform clock bound at \(X/2^e\) gives total \(O(2^{-E}/b)\). Larger \(e\) cost \(O(X^{-1/2})\). Letting \(E\to\infty\) gives a factor two, hence the coefficient \(\log3/\kappa\). In this calculation the odd rows count their actual positive inputs divided by \(X\), without separately normalizing to all odds.

Write \(\theta=\log_3(P(a)2^s/X)\). The true multiplicative identity \(P(w)2^J=P(a)3^{F_J(a)}\), where \(F_J(a)\) is the number of odd departures, shows that the first-hit profile just obtained on \(B_w\) is
\[
 \phi(z)\frac{\log3}{\kappa}\frac{h(w)}{P(w)}
                         \int A(\theta,u)\,d\nu_w(u).
\]
Indeed \(w=F(w)P(w)\), so shifting \(\theta\) by \(\log_3 F(w)\) changes the factor and the mark by exactly the multiplier \(F(w)\). The integer part \(F_J(a)\) leaves the geometric periodization unchanged. The scaled probability on \(C\setminus B_w\) is at most \(C_0(d_C-d_w)+o(1)\) by the [clock atom estimate](NATIVE_CLOCK_ATOMS.md). Along this ray \(d_w\uparrow d_C\). Sending \(J\to\infty\) after the source limit proves (3), with uniform convergence of the displayed profile by the bounded kernel and total-variation convergence of the marks.

The normalized signed clock on \(C\) has weak Gaussian mass \(d_C\). Indeed on fixed \(B_w\) the first-visit Gaussian supplies \(d_w\), while the total omitted ordinary mass tends to \(d_C-d_w\). Send \(J\to\infty\). Sum (3) on compact \(z\)-intervals. The phase progresses by the irrational \(\lambda=\log_3 2\) at each integer clock, so its continuous functions average uniformly in the starting phase on growing consecutive date intervals. Riemann sums, or finite subdivisions of the \(z\)-interval, therefore identify \(\int_0^1K_C=d_C\). In particular
\[
     (\log3)d_C/2\le K_C(\theta)\le (3\log3)d_C/2.                    \tag{4}
\]
All component coefficient sums in (1) converge absolutely.

## Summing actual endpoint atoms

By the [uniform clock atom estimate](NATIVE_CLOCK_ATOMS.md), \(b p_t(y)\le C d_y+o(1)\) for every nonperiodic \(y\), uniformly over all tested dates. Outside the futures of finitely many fixed sources we can make \(d_y<\delta\). These omitted vertices contribute at most \((C\delta+o(1))^{q-1}\) to (1), using their total mass at most one. Each finite set of additional transient vertices contributes \(O(1/b)\). The remaining futures are finitely many disjoint eventual escaping rays, one per represented escaping component, after removing or adding finitely many initial vertices. Include a ray of each of any prescribed finite family of components by enlarging the seed set.

On one indicated ray write \(y_j=T^ja\), \(j\ge0\). At every date \(t\),
\[
 p_t(y_j)=P_X(n\in B_{y_j},\ D_C(n)=t-j).
\]
For \(j\ge J\) the replacement of \(B_{y_j}\) by all of \(C\) in this equation costs at most \((C_0(d_C-d_{y_J})+o(1))/b\), uniformly in \(j,t\), by the signed clock estimate and nesting. Thus on \(|t-j-\mu L|\le B b\) the sequence \(bp_t(y_j)\) has the local profile (3), up to a uniform error tending to zero as first \(X\), then \(J\) tend to infinity. Finitely many omitted \(j<J\) have zero effect at the collision scale. For the remaining tails, the sum of the \(p_t(y_j)\) at \(|t-j-\mu L|>Bb\) is bounded by the corresponding signed-clock tail mass on \(C\), since the tested signed dates are distinct. Its upper limit tends to zero as \(B\to\infty\) by the weak Gaussian just proved. A uniform \(O(1/b)\) point bound handles its scaled \(q\)-mass.

On the central part sum the \(q\)-th power of (3) by the same irrational rotation. The restriction \(j\ge0\) is \((t-j-\mu L)/b\le (t-\mu L)/b\). Riemann sums yield the factor \(\int_{-\infty}^v\phi^q\). At \(v=-\infty\) the compact central interval is eventually empty. At \(v=+\infty\) it is eventually unrestricted. Add the finite component contributions, then let \(\delta\downarrow0\) and exhaust the countable family. This proves (1).

For the time average, the uniform central replacement remains valid over \(0\le h<W\). The Gaussian argument varies by \(o(1)\), and the phase \(\theta+h\lambda\) averages \(K_C\) to \(d_C\) uniformly because \(W\to\infty\). The tail estimate still holds: after dividing by \(W\), any one signed date is counted at most once in the sum over the tested consecutive windows, with the central cutoff shifted by at most \(W=o(b)\). The same Riemann sum proves the time-averaged formula.

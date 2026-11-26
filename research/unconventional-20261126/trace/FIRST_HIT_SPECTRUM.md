# Global first-hit trace moments identify the escaping components

**Status.** Proposed, source-qualified. The limits below exist whether or not an escaping positive integer orbit exists. They express two families of finite arithmetic measurements in terms of the masses of the actual escaping merge components. Their numerical values are undetermined.

Use the same odd map, original Syracuse cylinder densities \(\rho_k\), integer trace \(h\), predecessor densities \(d_a\), and source qualifications as in [the profile theorem](ESCAPE_TRACE_PROFILE.md). For \(k\ge1\), let \(L_k(a)\) sum the weights \(3^k/2^D\) of the positive odd sources whose **first** hit of the positive odd target \(a\) has odd time \(k\); \(D\) is the actual sum of division exponents. Define
\[
 u_n(a)=L_n(a)/a,\qquad v_n(a)=\frac1{an}\sum_{k=1}^nL_k(a).
\]
At a nonperiodic target, \(L_k(a)=\rho_k(a)\). At a periodic target of primitive odd period \(p\) and cycle multiplier \(\lambda\),
\[
 L_k(a)=\rho_k(a)-1_{k\ge p}\lambda\,\rho_{k-p}(a).
\]
This is the exact decomposition by the first visit, with \(L_0=\rho_0=1\). Repeated visits at cycles must be removed.

Let \(\mathcal C_{\rm esc}\) be the set of merge components whose orbits are injective, where two odd sources belong to the same component when their forward paths meet, possibly at different times. For \(C\in\mathcal C_{\rm esc}\), let \(b_C=\lim_i h(a_i)/a_i>0\) along any ray of \(C\). The profile theorem proves existence and independence of the chosen ray. For every \(p>1\),
\[
 \begin{split}
 \lim_{n\to\infty}\frac1n\sum_{a>0\ {\rm odd}}u_n(a)^p
     &=\sum_{C\in\mathcal C_{\rm esc}} b_C^p,\\
 \lim_{n\to\infty}\frac1n\sum_{a>0\ {\rm odd}}v_n(a)^p
     &=\frac1{p+1}\sum_{C\in\mathcal C_{\rm esc}} b_C^p .
 \end{split}                                                     \tag{1}
\]
Both left-hand limits are unchanged if the sums are truncated at \(a\le3^n\). The first identity uses Valbuena's fixed-integer Cesàro **absolute** trace from the envelope paper. The second only uses the ordinary signed Cesàro limit and the earlier first-hit and density inputs. No full Collatz conclusion follows without evaluating the right side.

## 1. Uniform estimates on all ordinary targets

Two extra input bounds are taken from Weaver, paper 12/v1, §7, including the paragraph treating periodic targets, and Theorem 11:
\[
 L_k(a)\le C\,a d_a \quad(k\ge1),\qquad
 \sup_{a:\,\mathcal P(a)\cap[1,M]=\varnothing}d_a
 \le\delta(M)\longrightarrow0.                                 \tag{2}
\]
The first bound is on first visits at periodic targets. At multiples of three \(L_k=0\) for \(k\ge1\). The second uses an actual ordinary ancestor, including the target itself; for odd targets an even ancestor can be replaced by its odd part. This is an unconditional implication with the quoted analytic inputs, uniform in the target. The stronger stated logarithmic rates are unnecessary. Valbuena's finite cylinder-energy criterion and large-minimum-ancestor estimate precede (1). [Weaver, §§7 and 12](https://rstation.ai/problems/collatz/papers/12/v1) · [Valbuena, basin paper](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex)

For \(1\le k\le n\), the following bound has an absolute constant:
\[
 \sum_{a\le3^n,\ a\ {\rm odd}}\frac{\rho_k(a)}a\le C_1 n.       \tag{3}
\]
In the inverse words of total clock \(D\le8n\), a compatible \(a\) has a positive odd source \(x\le2^{8n}3^n\). The affine formula with positive offset gives \(3^k2^{-D}/a\le1/x\). At the fixed depth \(k\), an \(x\) determines its entire word and endpoint, so this portion is bounded by the harmonic sum through \(2^{8n}3^n\). For \(D>8n\), use the crude bound \(1+n\log3\) for the sum of \(1/a\) in any admissible residue class below \(3^n\). The total weight of such words is \(3^kP(D_k>8n)\), for an auxiliary sum of \(k\) independent geometric variables \(P(e=j)=2^{-j}\). Since \(\mathbb E(4/3)^e=2\), it is at most \([6(3/4)^8]^n\), an exponentially decreasing term. This use of independent variables counts all words before imposing the compatibility condition.

Beyond \(Q=3^n\), both \(u_n(a)\) and \(v_n(a)\) are bounded by \(R(a)/a\), taking \(R=\rho_n\) or \(R=n^{-1}\sum_{k=1}^n\rho_k\), respectively. In either case \(R\ge0\) is \(Q\)-periodic and its sum on a full period is \(Q\). For every \(p>1\), its sum of \(p\)-th powers on that period is at most \(Q^p\). Therefore
\[
 \sum_{a>Q,\ a\ {\rm odd}}(R(a)/a)^p\le\sum_{j\ge1} j^{-p}.     \tag{4}
\]
This controls the discarded infinite range, with no rate needed for convergence of individual ordinary traces.

Let \(F_M\) be the union of forward odd orbits of all positive odd sources at most \(M\). Equations (2) and (3) give, for either \(w_n=u_n\) or \(v_n\),
\[
 \sum_{a\le3^n,\ a\notin F_M,\ a\ {\rm odd}} w_n(a)^p
 \le(C\delta(M))^{p-1} C_1 n.                                   \tag{5}
\]
The bound on the power \(p-1\) uses (2); the one remaining factor uses the total mass bound (3). No summability of \(1/a\) on the entire positive odd line is assumed.

## 2. Contributions on the finitely many represented components

For fixed \(M\), \(F_M\) is a finite set together with one disjoint infinite tail for each escaping component reachable from a source at most \(M\). Indeed two paths in the same merge component share one tail, and finitely many periodic paths are finite as sets. Each fixed finite set contributes \(O_M(1)\) to either power sum by (2).

Consider one of these tails \(a_0,a_1,\ldots\), with charge \(b=b_C\). All terms with \(i\le n\) satisfy \(a_i\le3^n\) once \(n\) is large because \(a_i+1\le(3/2)^i(a_0+1)\). Their raw values are
\[
 u_n(a_i)=\frac{h(a_i)}{a_i}\,V_i(n-i-1).
\]
The uniform row convergence, \(h(a_i)/a_i\to b\), and Cesàro absolute convergence on the right of \(V\) imply
\[
 \frac1n\sum_{0\le i<n}|u_n(a_i)-b|\to0.
\]
To justify the diagonal, discard any fixed number of initial \(i\); on the rest, replacing \(V_i\) by \(V\) and \(h(a_i)/a_i\) by \(b\) costs uniformly little when the fixed cutoff is large. Then \(n-i-1\) traverses distinct consecutive nonnegative arguments of the one profile \(V\). The bounded range (2) allows taking any fixed power \(p>1\), giving \(b^p\).

For the averaged row, the uniform ramp (4) of the profile theorem gives
\[
 v_n(a_i)=\frac{h(a_i)}{a_i}\big[(1-i/n)_++o_{i\to\infty}(1)\big],
\]
where the error is uniform in \(n\). The same finite initial deletion and a Riemann sum give \(b^p\int_0^1(1-t)^pdt=b^p/(p+1)\) from \(0\le i<n\).

The remote tail \(i\ge n\) requires a separate bound: it cannot be discarded just because a single value is small. For every \(\eta>0\) there is \(J\) such that, for large \(n\), \(u_n(a_i)\le\eta\) for every \(i\ge n+J\), by uniform profile convergence and its zero left tail. In the averaged case the ramp gives this bound already for \(i\ge n\) and \(n\) large. Within \(a_i\le3^n\) the sum of \(p\)-th powers over these indices is at most \(\eta^{p-1}C_1 n\) by (3). The intervening \(J\) terms cost \(O(J)\). Let \(\eta\downarrow0\). Equation (4) handles the range \(a_i>3^n\) uniformly. All contributions asserted for a single tail are now proved.

## 3. Summing the components

For finitely many distinct escaping components, the predecessor basins at any choices of one vertex per component are disjoint. Finite additivity and \(h(a_i)/a_i\le c_*d_{a_i}\) give
\[
 \sum_{C\in\mathcal C_{\rm esc}} b_C\le c_*
\]
by taking the limit on each of finitely many rays and then taking the supremum over finite families. Thus the series in (1) converges. As \(M\to\infty\), each escaping component is represented eventually. Formula (5) controls the omitted part, (4) controls the untruncated range, and §2 identifies the represented part. This proves both identities (1).

A threshold formulation follows without taking any power. For all \(t>0\),
\[
 \lim_{n\to\infty}\frac1n\#\{a>0\text{ odd}:v_n(a)>t\}
     =\sum_{C:b_C>t}(1-t/b_C).
\]
For \(u_n\), if \(t\) is distinct from each \(b_C\), the limit is \(\#\{C:b_C>t\}\). Fix \(M\) with \(C\delta(M)<t\) to remove all unrepresented components pointwise, and apply the same finite-tail arguments, or infer the threshold laws by approximating indicators at the continuity points of the respective limiting distributions. In the raw law, a threshold \(t=b_C\) can cut at a limiting atom, so no count identity is asserted there.

## 4. What the mass bound cannot decide

There are arbitrarily large odd units \(q\) in the known basin of 1 that have no smaller **unit** ancestor. Otherwise induction on the integer would put every good odd unit in the orbits of finitely many such minimal units. Those orbits are finite. But there are infinitely many good odd units; for instance \(x=(4^j-1)/3\) satisfies \(U(x)=1\), and \(j\equiv1\pmod3\) gives a unit. If an odd nonunit \(r\) reaches a chosen \(q\), then \(r\ne q\) and \(4r+1\) is an odd unit sharing its very next state, so \(4r+1\ge q\). Even starts yield the same bound after stripping twos. Thus \(q\) has no ancestor at most \(M=\lfloor(q-2)/4\rfloor\). The reciprocal predecessor floor gives \(d_q\ge c/q\). Any uniform bound of the form in (2) therefore satisfies \(\limsup_{M\to\infty}M\delta(M)>0\) already on good roots. This obstruction concerns the minimum of the predecessor set; estimates for a forward path avoiding a small floor are different.

The first missing inference for escape exclusion here is an upper bound \(o(n)\) on one actual first-hit power sum, or any other argument forcing all \(b_C\) to vanish. Taking \(p\to\infty\) in (1) recovers the largest component charge when escape exists. The bound on the sum of the charges permits a positive charge of arbitrary small size. Finite positive cycles contribute zero to (1), so their exclusion is independent.

Weaver's October 22 discussion gives the earlier one-spine lower coefficient, including the factor \(1/3\) in the Cesàro quadratic lower bound. Valbuena's basin paper gives the finite energy criterion and small-ancestor reduction. Equations (1) identify the complete limiting value and every component contribution, with the appropriate first-hit modification at cycles. [Weaver, earlier lower bounds](https://rstation.ai/r/collatz/posts/19?after=roCqImbLfooaN0CB) · [Valbuena, research and verification summary](https://github.com/x1xhlol/collatz-two-coordinate-obstruction)

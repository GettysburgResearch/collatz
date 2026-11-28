# Logarithmic damping does not rescue an atomic anchor majorant

**Self-contained extension of the atomic-pole obstruction.** The subcritical theorem has an apparent escape route: at the critical ternary factor three, the affine anchor pushforward no longer multiplies atomic mass by a factor greater than one. One could damp the critical pole logarithmically to restore integrability and sublinear values. This note rules out that natural class as well. The remaining obstruction is irreversible growth of dyadic denominators.

The result is a restriction on a proposed proof method. It excludes neither a non-atomic joint real/ternary potential nor Weaver's existing real-distance-dependent critical potential. It proves no Collatz convergence theorem.

## 1. A monotone critical kernel

Fix a real \(p>1\), and define

\[
 \Phi_p(v)=\sum_{k=1}^v\frac{3^k}{k^p},\qquad \Phi_p(0)=0.
\]

This is a monotone version of a ternary pole with logarithmic damping. At large \(v\), it has order \(3^v/(v+1)^p\). For a dyadic rational anchor \(\zeta=r/q\) in lowest terms, with \(q\) a positive power of two, write

\[
 K_\zeta(a)=\Phi_p(v_3(a-\zeta)),\qquad H_\zeta=q+|r|.
\]

As before, no anchor is a positive odd integer. Let \(h\) depend on one fixed residue modulo \(3^m\), and suppose

\[
 \sum_\zeta |c_\zeta|H_\zeta<\infty,
 \qquad g(a)=h(a)+\sum_\zeta c_\zeta K_\zeta(a).               \tag{1}
\]

Use the full ordinary inverse density operator

\[
 (Lg)(a)=\sum_{\substack{e\ge1\\2^ea\equiv1\ (3)}}
      \frac3{2^e}g\!\left(\frac{2^ea-1}{3}\right).             \tag{2}
\]

**Theorem.** If \(g\ge0\) and \(Lg\le g\) at every positive odd integer, then every coefficient in (1) is zero and \(h=0\). Signed weights satisfying the absolute moment condition are allowed.

The moment in (1) would have delivered the desired type of global upper estimate. The elementary bound

\[
 \Phi_p(v)\le C_p\frac{3^v}{(1+v)^p}
\]

and \(3^{v_3(a-\zeta)}\le|qa-r|\le H_\zeta a\) give

\[
 |g(a)|\le\|h\|_\infty+
   C_p\frac a{(1+\log a)^p}\sum_\zeta|c_\zeta|H_\zeta
       =o(a).                                                \tag{3}
\]

A constant depending only on \(p\) covers the bounded range in which \(t/(1+\log t)^p\) is not increasing. The series and its transfer in (2) converge absolutely: the exponent-\(e\) parent has order \(2^ea\), and (3) leaves a summable tail of order \(a\sum_e(e+1+\log a)^{-p}\).

## 2. Ordinary averages and the critical exponent tail

For Haar measure on \(\mathbb Z_3\),

\[
                       \int K_\zeta\,dm_3=\sum_{k\ge1}k^{-p}
                       =\zeta(p)<\infty.                    \tag{4}
\]

Let \(\mathbb E_X\) denote the average over positive odd integers through \(X\). The expansion

\[
 K_\zeta(a)=\sum_{k\ge1}\frac{3^k}{k^p}
                         1_{a\equiv\zeta\ (3^k)}
\]

stops by \(k\le\log_3(qX+|r|)\). Counting a class by its proportional size plus one gives

\[
 \mathbb E_XK_\zeta
 \le\zeta(p)+C_p\frac{H_\zeta}
                         {(1+\log(H_\zeta X))^p}.             \tag{5}
\]

For each fixed anchor and fixed ternary cylinder \(B\), the same truncation proves

\[
             \mathbb E_X[1_BK_\zeta]\longrightarrow
                       \int_BK_\zeta\,dm_3.                 \tag{6}
\]

Indeed the first finitely many levels have their exact limiting frequencies; the upper limiting tail is bounded by \(\sum_{k>J}k^{-p}\), while the rounding term in (5) vanishes.

There is a genuine issue at the next step. The Markov pushforward of anchors,

\[
 F_e(\zeta)=(3\zeta+1)/2^e,\qquad
 Q\mu=\sum_{e\ge1}2^{-e}(F_e)_*\mu,
\]

need not preserve the first height moment. It would be incorrect simply to reuse the subcritical proof's moment inequality.

The logarithmic damping supplies the required replacement. Put

\[
 \Psi_p(v)=
 \begin{cases}\Phi_p(v-1),&v\ge1,\\0,&v=0.\end{cases}
\]

The exact branch identity is

\[
                 LK_\zeta(a)=\sum_{e\ge1}\frac3{2^e}
                    \Psi_p(v_3(a-F_e(\zeta))).                \tag{7}
\]

It includes inadmissible branches through their zero term. For the unreduced fraction representing \(F_e(\zeta)\), set

\[
 H_e=2^eq+|3r+q|,
 \qquad 2^e\le H_e\le4\cdot2^eH_\zeta.
\]

Apply the same integer level count to \(\Psi_p\). Its Haar integral is \(\zeta(p)/3\), and the weighted rounding error is at most

\[
 \frac3{2^e}C_p\frac{H_e}{(1+\log(H_eX))^p}
       \le C'_p\frac{H_\zeta}{(1+e+\log X)^p}.                \tag{8}
\]

Summing this bound gives

\[
 \sum_{e\ge1}\text{rounding error}
       \le C''_pH_\zeta(1+\log X)^{1-p}\longrightarrow0       \tag{9}
\]

for a fixed anchor. The limiting main terms beyond a fixed exponent \(E\) are bounded by \(\zeta(p)\sum_{e>E}2^{-e}\). Taking \(X\to\infty\) first and then \(E\to\infty\) therefore proves the analogue of (6) for \(LK_\zeta\). The argument is unchanged after inserting \(1_B\), since the discarded kernel tails are nonnegative.

Bounds (5) and (9) are dominated by \(C_p(1+H_\zeta)\), uniformly for \(X\ge2\). The absolute first moment in (1) thus permits the countable signed sum. Both ordinary cylinder averages of \(g\) and \(Lg\) converge to their Haar integrals.

## 3. Ordinary positivity forces Haar harmonicity

The ordinary inequalities consequently imply

\[
                  g\ge0,\qquad g-Lg\ge0\quad m_3\text{-a.e.}
\]

This follows by integrating on every ternary cylinder and using that finite cylinder unions approximate measurable sets. The density transfer \(L\) preserves Haar integral, by the branch Jacobian calculation in the [subcritical theorem](ATOMIC_ANCHOR_MAJORANT_OBSTRUCTION.md). All functions are integrable by (4) and (1). Hence

\[
                               Lg=g\quad m_3\text{-a.e.}      \tag{10}
\]

This step rests on (5)–(9). Mere density of the positive integers in \(\mathbb Z_3\) would not justify it.

## 4. Critical small-ball averages recover atoms

Let

\[
 B_j(\zeta)=\zeta+3^j\mathbb Z_3,\qquad
 A_j=\Phi_p(j)+3^j\sum_{k>j}k^{-p}.
\]

The normalized Haar average of \(K_\eta\) on \(B_j(\zeta)\) equals \(A_j\) if \(\eta\in B_j(\zeta)\), and equals \(\Phi_p(v_3(\eta-\zeta))\) otherwise. Moreover

\[
 A_j\sim\frac{3^jj^{1-p}}{p-1},\qquad
                 \frac{3A_{j-1}}{A_j}\longrightarrow1.       \tag{11}
\]

The first term \(\Phi_p(j)=O_p(3^jj^{-p})\) is lower order, and the integral comparison for \(\sum_{k>j}k^{-p}\) gives the asymptotic.

Put \(\mu=\sum c_\eta\delta_\eta\). The normalized kernel average divided by \(A_j\) is between zero and one, and tends to zero for each fixed \(\eta\ne\zeta\). Dominated convergence against the finite measure \(|\mu|\) yields

\[
 \lim_{j\to\infty}\frac1{A_j}\operatorname{avg}_{B_j(\zeta)}g
                              =\mu(\{\zeta\}).               \tag{12}
\]

Since \(g\ge0\) almost everywhere, every atomic coefficient is nonnegative. Thus the signed option in (1) does not avoid the obstruction.

For an admissible exponent at \(\zeta\), let \(x_e=(2^e\zeta-1)/3\). The branch maps the normalized Haar measure of \(B_j(\zeta)\) to that of \(B_{j-1}(x_e)\). Therefore

\[
 \operatorname{avg}_{B_j(\zeta)} Lg
 =\sum_{\substack{e\ge1\\2^e\zeta\equiv1\ (3)}}
        \frac3{2^e}\operatorname{avg}_{B_{j-1}(x_e)}g.         \tag{13}
\]

The absolute average of \(g\) over any level-\((j-1)\) ball is bounded by \(\|h\|_\infty+A_{j-1}|\mu|(\mathbb Z_3)\), uniformly in the center. Thus (11) permits dominated convergence in the geometric sum in (13). Divide by \(A_j\), use (10) and (12), and obtain

\[
 \mu(\{\zeta\})=
       \sum_{\substack{e\ge1\\2^e\zeta\equiv1\ (3)}}
                    2^{-e}\mu(\{x_e\})=(Q\mu)(\{\zeta\}).    \tag{14}
\]

Both sides are purely atomic measures on dyadic rationals. Consequently

\[
                              \mu=Q\mu.                      \tag{15}
\]

The critical case has indeed removed the subcritical factor \(3/\kappa>1\). What remains is still impossible for a finite nonzero positive atomic measure on this anchor space.

## 5. No invariant probability lives on the dyadic anchors

Write a dyadic rational in reduced form and let \(d\ge0\) be its denominator exponent. If \(d\ge1\), its numerator is odd, and

\[
                d(F_e(\zeta))=d(\zeta)+e.                    \tag{16}
\]

It therefore never returns to the integers, and its denominator height strictly grows at every step.

At an integer \(z\), the nonzero integer \(3z+1\) has finite binary valuation \(v\). The probability of choosing \(e>v\), and therefore leaving the integers irreversibly, is \(2^{-v}>0\). If a finite positive measure is \(Q\)-stationary, its total integer mass can have no such positive loss: there is no inflow from nonintegral dyadics. Hence its integer mass is zero.

Next, mass at denominator exponent one can only arrive from integers, so it is zero. Inductively, mass at exponent \(d\) can only arrive from integers or smaller positive exponents. Every level has zero mass. Their countable union is the full dyadic state space, proving that the only finite positive \(Q\)-stationary measure there is zero.

Equations (12) and (15) therefore force \(\mu=0\).

## 6. Completion and scope

Now \(g=h\) is a bounded nonnegative locally constant inverse-harmonic function. The exact all-one inverse chains and Chinese-remainder argument in [Section 6 of the subcritical theorem](ATOMIC_ANCHOR_MAJORANT_OBSTRUCTION.md) force \(h=0\). This completes the proof.

Thus a positive floor plus a sublinear bound cannot be obtained by assigning absolutely first-height-summable weights to these critically damped atomic poles, even with signed renormalization. The statement does not apply to non-atomic stationary anchor measures (see the [primary joint affine law](https://rstation.ai/r/collatz/posts/33)), or to series without the absolute moment in (1). Nor does it apply to kernels whose real-distance factor depends on the target, as in Weaver's prior joint potential. The latter's unresolved ordinary limit is identified separately by the [Green-tail defect theorem](ANCHOR_GREEN_TAIL_DEFECT.md).

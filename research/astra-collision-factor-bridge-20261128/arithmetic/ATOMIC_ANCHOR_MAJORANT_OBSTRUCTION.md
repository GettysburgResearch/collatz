# Why an absolutely summable valuation-pole majorant cannot close Collatz

**Self-contained obstruction for an explicit proposed certificate class.** A natural irregular candidate is a sum of ternary valuation spikes at rational affine anchors. Such a function can have a positive floor, remain bounded on many large integers, and grow sublinearly everywhere. Those features evade the elementary power and monotonicity obstructions. Nevertheless, the certificate class below contains no nonzero nonnegative inverse supersolution.

The obstruction includes countably many anchors and absolutely summable signed weights. It does not exclude conditionally convergent renormalizations, critical nonintegrable kernels, a non-atomic representation, or the canonical integer trace. It is not a Collatz convergence theorem.

## 1. Statement and the reason for the height condition

Let

\[
 1<\kappa<3,\qquad \theta=\log_3\kappa<1,\qquad
 K_\zeta(a)=\kappa^{v_3(a-\zeta)}-1.
\]

The anchors \(\zeta=p_\zeta/q_\zeta\) are distinct dyadic rationals in lowest terms, with \(q_\zeta\ge1\) a power of two. No anchor is a positive odd integer. Write

\[
 H_\zeta=q_\zeta+|p_\zeta|\ge1.
\]

Let \(h\) be a real function of one fixed residue modulo \(3^m\). Suppose

\[
 \sum_\zeta |c_\zeta|H_\zeta^\theta<\infty,\qquad
 g(a)=h(a\bmod3^m)+\sum_\zeta c_\zeta K_\zeta(a)              \tag{1}
\]

for every positive odd integer \(a\). The usual inverse density operator is

\[
 (Lg)(a)=\sum_{\substack{e\ge1\\2^ea\equiv1\ (3)}}
       \frac3{2^e}g\!\left(\frac{2^ea-1}{3}\right).           \tag{2}
\]

**Theorem.** If \(g(a)\ge0\) and \((Lg)(a)\le g(a)\) at every positive odd integer, then \(c_\zeta=0\) for every anchor and \(h=0\). In particular no function in (1) is a positive majorant for the canonical trace.

The moment assumption in (1) is the direct height control one would try to prove when constructing a sublinear barrier. Indeed \(q_\zeta a-p_\zeta\) is a nonzero integer, so

\[
 \kappa^{v_3(a-\zeta)}
 \le |q_\zeta a-p_\zeta|^\theta
 \le H_\zeta^\theta a^\theta.
\]

Consequently (1) converges absolutely at every ordinary target and gives \(|g(a)|\le\|h\|_\infty+Ca^\theta=o(a)\). The theorem shows that proving precisely this natural summability estimate would also destroy the proposed supersolution inequality.

## 2. The first new anchor already defeats a single pole

For illustration, take \(g(a)=\kappa^{v_3(a+1)}\). For every even \(k\ge2\), the positive odd integer

\[
 a_k=\frac{5\cdot3^k-1}{4}
\]

satisfies \(v_3(a_k+1)=1\). Its exponent-three inverse parent is

\[
 x_k=\frac{8a_k-1}{3}=10\cdot3^{k-1}-1,
 \qquad v_3(x_k+1)=k-1.
\]

Therefore

\[
 \frac{(Lg)(a_k)}{g(a_k)}\ge\frac38\kappa^{k-2}\longrightarrow\infty.
\]

The missing pole is \(-1/4\). Repeated closure under the affine anchor maps produces infinitely many rational anchors. The theorem addresses that infinite closure, rather than stopping at this finite counterexample.

## 3. Exact centered transfer

Set

\[
 F_e(\zeta)=\frac{3\zeta+1}{2^e},\quad
 \rho_1(a)=(L1)(a)=
 \begin{cases}0,&a\equiv0\pmod3,\\1,&a\equiv1\pmod3,\\2,&a\equiv2\pmod3.
 \end{cases}
\]

For every anchor and ordinary odd target, the exact identity is

\[
 \boxed{\displaystyle
 LK_\zeta=\frac3\kappa\sum_{e\ge1}2^{-e}K_{F_e(\zeta)}
                  -\frac{\kappa-1}{\kappa}\rho_1.}           \tag{3}
\]

If the branch is admissible and \(a'=(2^ea-1)/3\), then

\[
 v_3(a-F_e(\zeta))=1+v_3(a'-\zeta).
\]

If it is inadmissible, the left-hand valuation is zero. Substituting into the centered kernel proves (3), including its background correction. Omitting that correction would give the wrong operator.

The anchor family avoiding positive odd integers is closed under all \(F_e\). A nonintegral dyadic rational has odd numerator and an even denominator; its new numerator remains odd, so its denominator cannot cancel. A positive even integer acquires an odd numerator over a nontrivial power of two. A nonpositive integer either remains nonpositive integral or becomes a nonintegral dyadic rational. Thus no new pole occurs at an ordinary target.

Let \(\mu=\sum_\zeta c_\zeta\delta_\zeta\), and define the mass-preserving affine Markov pushforward

\[
                 Q\mu=\sum_{e\ge1}2^{-e}(F_e)_*\mu.
\]

The height moment remains finite under \(Q\). Before reducing the fraction,

\[
 H_{F_e(\zeta)}\le4\cdot2^eH_\zeta,
\]

so

\[
 \int H^\theta\,d|Q\mu|
 \le\frac{4^\theta}{2^{1-\theta}-1}
               \int H^\theta\,d|\mu|<\infty.                 \tag{4}
\]

## 4. Why ordinary inequalities legitimately pass to Haar integrals here

This passage is not automatic for a statement on countably many integers. The explicit height moment supplies the missing justification.

Let \(\mathbb E_X\) average over positive odd \(a\le X\). For one fixed rational anchor,

\[
 K_\zeta(a)=(\kappa-1)
       \sum_{j\ge1}\kappa^{j-1}1_{a\equiv\zeta\ (3^j)}.       \tag{5}
\]

The sum stops by \(j\le\log_3(q_\zeta X+|p_\zeta|)\). Each ternary class contains at most its proportional number of these odd integers plus one. Thus

\[
 \mathbb E_X K_\zeta
 \le C_\kappa\bigl(1+H_\zeta^\theta X^{\theta-1}\bigr)
 \le C_\kappa(1+H_\zeta^\theta).                              \tag{6}
\]

For fixed \(J\), the first \(J\) terms of (5) have their exact limiting Haar frequencies. The upper limiting average of the remaining terms is at most \(C_\kappa(\kappa/3)^J\), since the rounding contribution in (6) tends to zero at the fixed anchor. Hence the ordinary average of \(1_BK_\zeta\) converges to its Haar integral for every fixed ternary cylinder \(B\). Inserting \(1_B\) only decreases the nonnegative tail estimate.

Equation (6) and (1) permit dominated convergence over the countable anchors, including signed coefficients. Equation (4) permits the same step for \(Q\mu\). Identity (3) therefore proves, for every such cylinder,

\[
 \lim_{X\to\infty}\mathbb E_X[1_Bg]=\int_Bg\,dm_3,
 \qquad
 \lim_{X\to\infty}\mathbb E_X[1_BLg]=\int_BLg\,dm_3.           \tag{7}
\]

The background \(h\) is locally constant, and so is \(Lh\), now modulo \(3^{m+1}\); these pieces need no singular-kernel estimate.

Consequently ordinary nonnegativity and the ordinary supersolution inequality imply \(g\ge0\) and \(g-Lg\ge0\) Haar-almost everywhere. One may see this by integrating over every ternary cylinder and then approximating a negative level set by finite unions of cylinders.

The transfer preserves Haar integral. Indeed \(x\mapsto(3x+1)/2^e\) maps \(\mathbb Z_3\) onto one cylinder of measure \(1/3\), and the coefficient \(3/2^e\) cancels that Jacobian. Summing \(2^{-e}\) gives one. Since \(1<\kappa<3\), all the kernels are integrable, with

\[
 \int K_\zeta\,dm_3=\frac{\kappa-1}{3-\kappa}.
\]

Thus \(\int(g-Lg)=0\), and the nonnegative difference must vanish:

\[
                              Lg=g\quad m_3\text{-a.e.}       \tag{8}
\]

## 5. A small-ball average recovers every atomic coefficient

For any finite signed measure \(\sigma\) on \(\mathbb Z_3\), write

\[
 \mathcal K\sigma(a)=\int K_\eta(a)\,d\sigma(\eta).
\]

For the normalized Haar average on \(B_j=\zeta+3^j\mathbb Z_3\),

\[
 \boxed{\displaystyle
 \lim_{j\to\infty}\kappa^{-j}
       \frac1{m_3(B_j)}\int_{B_j}\mathcal K\sigma\,dm_3
       =\frac2{3-\kappa}\sigma(\{\zeta\}).}                  \tag{9}
\]

If \(\eta\in B_j\), the normalized kernel average is
\(2/(3-\kappa)-\kappa^{-j}\). If \(\eta\notin B_j\), it is
\(\kappa^{-j}(\kappa^{v_3(\eta-\zeta)}-1)\), which tends to zero for fixed \(\eta\ne\zeta\). Both are bounded in absolute value by \(2/(3-\kappa)\). Dominated convergence against \(|\sigma|\) proves (9).

Apply (9) first to \(g=h+\mathcal K\mu\). The bounded \(h\) disappears after normalization. The nonnegativity obtained in (7) implies every atom of \(\mu\) is nonnegative. Hence even if signed coefficients were initially allowed, their values after combining repeated anchors satisfy

\[
                              c_\zeta\ge0.                    \tag{10}
\]

Let \(M=\mu(\mathbb Z_3)\). Equations (3) and (8) imply

\[
 \mathcal K\left(\mu-\frac3\kappa Q\mu\right)
          =Lh-h-\frac{\kappa-1}{\kappa}M\rho_1.               \tag{11}
\]

The right side is bounded. By (9), the signed measure on the left has no atoms. It is purely atomic, so it is zero. Taking its total mass gives

\[
                    M=\frac3\kappa M,
\]

which forces \(M=0\), because \(\kappa<3\). Together with (10), this proves every coefficient vanishes.

## 6. The bounded residue background must also vanish

Now \(g=h\). Since \(h\) and \(Lh\) are locally constant, their almost-everywhere equality is an everywhere equality on \(\mathbb Z_3\). Nonnegativity holds everywhere as well, because every ternary cylinder contains positive odd integers.

Suppose \(h(b)>0\) at some unit residue. For any \(k\ge1\), choose by the Chinese remainder theorem a positive odd \(b_k\) such that

\[
 b_k\equiv b\pmod{3^m},\qquad b_k\equiv-1\pmod{2^{k+1}}.
\]

Write \(d=(b_k+1)/2^k\), an even positive integer, and set

\[
 a_i=2^i3^{k-i}d-1\quad(0\le i\le k).
\]

These are positive odd integers, \(a_k=b_k\), and
\((2a_i-1)/3=a_{i+1}\) for \(i<k\). Positivity and the exponent-one term of the inverse equation give

\[
 \|h\|_\infty\ge h(a_0)
       \ge(3/2)^kh(b_k)=(3/2)^kh(b),
\]

a contradiction as \(k\to\infty\). At nonunit residues \(Lh=0\), so those values vanish too. This finishes the theorem.

## 7. What remains outside the obstruction

The hypothesis in (1) is substantive. A countable ordinary modification may be invisible to Haar integrals when no valid ordinary-to-Haar averaging estimate is available; the [harmonic atom](HARMONIC_BOUNDARY_ATOM.md) illustrates that boundary. Here (6)–(7) justify the passage explicitly.

The theorem rules out both finite pole lists and an infinite positive or absolutely summable signed closure whose denominator-height moment would deliver a power sublinear bound. It does not rule out a representation with divergent absolute height moment, a non-atomic anchor measure, a conditionally convergent renormalization, or a kernel at \(\kappa=3\), where the Haar integral used above diverges.

The last alternative is relevant to Weaver's existing joint potential: its ternary factor is exactly critical, and its real denominator and positive-anchor boundary matter. That construction is separately evaluated in [the exact Green-tail defect](ANCHOR_GREEN_TAIL_DEFECT.md), with the original construction credited there. The current theorem supplies no estimate on that unresolved defect.

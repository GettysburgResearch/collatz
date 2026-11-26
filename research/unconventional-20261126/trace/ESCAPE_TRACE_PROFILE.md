# The depth profile of the ordinary inverse trace on an escaping orbit

**Status.** Proposed deductions from the source-qualified analytic inputs below. One positive ordinary escaping orbit is the hypothesis. The conclusions describe the trace on that orbit.

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on odd positive integers. Let \(\rho_k\) be the additive Haar-normalized Syracuse density on the residue classes modulo \(3^k\), with \(\rho_0=1\). A depth counts applications of \(U\). Let \(h\) be the ordinary Cesàro trace. Fix an injective orbit \(a_i=U^i(a_0)\). Discard the first state if it is divisible by three. All remaining states are odd units. Define
\[
 e_i=v_2(3a_i+1),\quad M_i=3^i2^{-\sum_{j<i}e_j},\quad H_i=h(a_i)/M_i.
\]

## 1. How much weight follows the orbit backwards?

Weaver, *First-landing bounds and canonical inverse laws for Collatz*, paper 12/v1, Theorem 6 and Corollary 7, gives
\[
 h(a)=c_*a\beta_a\quad\text{at nonperiodic units},\qquad
 0<\beta_a\le d_a\le1,\qquad c_*=\tfrac12\log(4/3).
\]
Here \(d_a\) is relative odd natural predecessor density. The source credits the trace to Valbuena. Its probability kernel on odd units is
\[
 P(a,x)=\frac{3}{2^{v_2(3x+1)}}\frac{h(x)}{h(a)}
 \quad(Ux=a).
\]
For \(f=\rho_1/h\) on units there is one \(B<\infty\) with \(0\le f\le B\) and
\[
 (P^{k-1} f)(a)=\rho_k(a)/h(a)\qquad(k\ge1).
\]
Indeed \(\rho_1\) takes the values 1 and 2 on the two unit classes, and \(h\) has a uniform positive lower bound there. A parent divisible by three has \(\rho_1=h=0\). The observable \(\rho_1\) includes the final inverse step from an unrestricted odd source, which accounts for the shift by one. [Weaver, §§8–10](https://rstation.ai/problems/collatz/papers/12/v1)

The ordinary orbit-packing theorem gives \(\sum_i1/a_i<\infty\). In fact finite distinct shortcut segments have a uniform reciprocal bound, and any repeated intervening shortcut state would force repeated odd states. Thus
\[
 a_i/M_i=a_0\prod_{j<i}(1+1/(3a_j))\uparrow L<\infty.
\]
The one-parent term of harmonicity gives \(H_i\le H_{i+1}\). The trace formula bounds \(H_i\le c_*a_i/M_i\le c_*L\). Consequently \(H_i\uparrow H_\infty\in(0,\infty)\), and
\[
 h(a_i)/a_i\longrightarrow b=H_\infty/L>0.                    \tag{1}
\]
Two rays in the same merge component share \(b\), since they eventually coincide after a finite index shift. [Resident orbitwise reciprocal bound](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/integrated/orbitwise-boundaries/README.md)

For \(0\le m\le i\), multiplying the actual probabilities of retracing \(a_i,a_{i-1},\ldots,a_m\) gives exactly \(H_m/H_i\). With \(\epsilon_m=1-H_m/H_\infty\),
\[
 P_{a_i}(\text{depart from this segment before reaching }a_m)
 \le\epsilon_m\downarrow0\qquad\text{uniformly in }i\ge m.      \tag{2}
\]
These are finite path probabilities at the displayed changing roots.

## 2. The centered profile

Define a row \(V_i:\mathbb Z\to[0,B]\) by \(V_i(s)=\rho_{i+s+1}(a_i)/h(a_i)\) for \(i+s\ge0\), and by zero otherwise. For \(s\ge-m\), (2) and the Markov property compare expectations of the same bounded nonnegative observable:
\[
 |V_i(s)-V_m(s)|\le B\epsilon_m\qquad(i\ge m).
\]
For \(-i\le s<-m\), follow only the first \(i+s\) inverse steps. The distinguished path terminates at \(a_{-s}\) and has probability at least \(1-\epsilon_m\). Hence
\[
 V_i(s)\le B\epsilon_m+\sup_{r\ge m} f(a_r).
\]
The supremum tends to zero by (1), distinctness, and \(\rho_1\le2\). Both rows vanish for \(s<-i\). Thus \(V_i\to V\) uniformly on all of \(\mathbb Z\), and
\[
 \lim_{s\to-\infty}V(s)=0,\qquad
 \lim_{N\to\infty}N^{-1}\sum_{s=0}^{N-1}V(s)=1.               \tag{3}
\]
For the second limit, fix \(m\), use the fixed-integer Cesàro trace at \(a_m\) for its shifted row, then let \(m\to\infty\). With the additional input in §3 one also gets \(N^{-1}\sum_{s=0}^{N-1}|V(s)-1|\to0\) by the same argument.

Write \(A_K(a)=K^{-1}\sum_{k=1}^K\rho_k(a)\). Then
\[
 \sup_{K\ge1}\left|\frac{A_K(a_i)}{h(a_i)}
                 -\left(1-\frac{i}{K}\right)_+\right|\to0.     \tag{4}
\]
Replacing the row by \(V\) costs at most its uniform error. For \(K\le i/2\) all contributing indices are at most \(-i/2\). For \(K>i/2\), the sum of \(V\) over all negative indices from \(-i\) to \(-1\) is \(o(i)\). When \(K>i\), the rest is \(K-i+o(K-i)\) as \(K-i\to\infty\), and bounded lengths cost \(O(1/K)\). This proves (4) also for \(K\) varying arbitrarily with \(i\).

For \(0<\eta<1\), let \(K_\eta(a)=\min\{K\ge1:A_K(a)\ge\eta h(a)\}\). Then \(K_\eta(a_i)/i\to(1-\eta)^{-1}\). Use (4) at all smaller clocks and at one clock just above the proposed limit, since the averages need not be monotone.

## 3. A bounded additive width for the single-depth transition

Valbuena's *A positive semicontinuous density for the Syracuse stationary law* (8 October 2026), stationary-envelope theorem and integer corollary, gives a greatest lower semicontinuous density \(E\) for the ternary law. It agrees with the canonical trace at every positive integer and satisfies
\[
 \liminf_k\rho_k(a)\ge h(a),\qquad
 N^{-1}\sum_{k=1}^N|\rho_k(a)-h(a)|\to0
\]
at each fixed positive integer. Its Lean development was not rebuilt here. [Valbuena, statement and integer corollary](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex)

For every \(0<\eta<1\) there is a finite \(J=J(a_0,\eta)\) such that for all sufficiently large \(i\),
\[
 \begin{array}{ll}
 \rho_k(a_i)<\eta h(a_i)&(1\le k\le i-J),\\
 \rho_k(a_i)>\eta h(a_i)&(k\ge i+J).
 \end{array}                                                    \tag{5}
\]
The first bound follows from the left tail in (3). For the second choose \(m\) with \(1-\epsilon_m\) sufficiently close to one. The distinguished inverse prefix gives
\[
 \rho_k(a_i)/h(a_i)\ge(H_m/H_i)\rho_{k-i+m}(a_m)/h(a_m)
 \qquad(k-i+m\ge1).
\]
Now use the fixed-root liminf at \(a_m\) to choose \(J\). No moving-root error rate is used.

In particular, for any fixed \(0<t<b\), the first \(k\ge1\) with \(\rho_k(a_i)\ge t a_i\) is \(i+O_{a_0,t}(1)\). Apply (1) and (5) with fixed fractions on both sides of \(t/b\). The comparison in this detector involves a rational, finitely computable cylinder density and the ordinary target.

There is also a spatial statement. Let \(J_k(a)\) be the essential infimum of \(E\) on \(a+3^k\mathbb Z_3\). Then \(J_k(a)\le\rho_k(a)\) and \(J_k(a)\uparrow h(a)\) at each fixed positive odd \(a\): lower semicontinuity gives the lower limit, and \(J_k\le\rho_k\) and the fixed-root Cesàro trace give the upper limit. Stationarity gives
\[
 E(F_e z)\ge(3/2^e)E(z)\quad\text{for Haar-almost every }z\in\mathbb Z_3,\qquad
 F_e(z)=(3z+1)/2^e .
\]
This follows by taking one positive branch, with probability \(2^{-e}\) and ternary Jacobian \(1/3\). Composing the actual \(i-m\) gaps maps the entire cylinder \(a_m+3^\ell\mathbb Z_3\) bijectively to \(a_i+3^{\ell+i-m}\mathbb Z_3\) and preserves null sets in both directions. Consequently
\[
 J_{\ell+i-m}(a_i)/h(a_i)
 \ge (H_m/H_i)J_\ell(a_m)/h(a_m).
\]
The same bounded-width statement (5) holds with \(J_k\) in place of \(\rho_k\). The upper estimate uses \(J_k\le\rho_k\), and the lower estimate fixes \(m\) before using convergence of \(J_\ell(a_m)\). Thus a complete ternary neighborhood carries the large trace, in the essential-infimum sense, at depth \(i+O_{a_0,\eta}(1)\).

## 4. Scope

PR200 gives a lower bound in terms of \(\log a_i\) and low-depth ordinary octave discrepancies. Weaver's October 22 comment already follows the distinguished segment to obtain a one-sided linear lower bound on global quadratic energy. The uniform centered profile, exact ramp, and bounded additive transition window use the fact that the *total* probability of every competing history on the tail tends to zero. [PR200, quantitative onset](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md) · [Weaver, October 22 discussion](https://rstation.ai/r/collatz/posts/19?after=roCqImbLfooaN0CB)

The Haar weak-\(L^2\) bound permits a cylinder of mass \(3^{-i+O(1)}\) to have density of order \(a_i\). Its lower contribution to a quadratic integral is of order \(a_i^2 3^{-i}\), and \(a_i\le(a_0+1)(3/2)^i\). These lower contributions have a summable upper envelope \(O_{a_0}((3/4)^i)\). Thus the local transition window alone gives no contradiction.

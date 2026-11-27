# A determinant for one ordinary orbit at several clocks

**PROPOSED written theorems.** Fix a positive ordinary integer \(n\) with injective shortcut Collatz orbit \(x_i=T^i n\). Let \(G_i\) be the whole factor cancelled from the companion denominator when its first \(i\) physical bits are periodically closed. Call a clock exceptional when \(\log G_i\ge\epsilon i\), with \(\epsilon>0\) fixed.

* If \(x_i=O_n((2+i)^C)\) for fixed \(C\), there are \(O_{n,C,\epsilon}((\log(2+X))^2)\) exceptional clocks up to \(X\).
* If \(\log(x_i+1)=O_n(i^\beta)\), \(0<\beta<1\), there are \(O_{n,\beta,\epsilon}(X^\beta)\) up to \(X\), allowing dependence on the height constant.
* On an arbitrary escape, (5) gives a local alternative. Enough separated exceptional clocks in a short multiplicative interval with small real companion trials force two specified ordinary states among the marked endpoints and the initial source to agree modulo a large power of two. This applies at physical record heights without a growth hypothesis.

These statements require no algebraicity of the genuine dyadic scalar. There is a further individual-clock theorem. A positive fractional loss infinitely often at clocks with subexponential real trial forces the genuine scalar of the fixed source to be transcendental. Such trial control holds at all clocks of any escape having a limiting exponential growth rate and at all physical record heights of every escape. The round-six density theorem controls fixed additive windows and permits arbitrarily many exceptions with growing separations in a multiplicative window. [Round six](../../round6/arithmetic/README.md) · [Individual-clock theorem](ALGEBRAIC.md)

## Two exact coordinates and their physical meaning

Write \(e_i=x_i\bmod 2\), \(p_i=\sum_{j<i}e_j\) and put
\[
 Q_i=3^i,\quad a_i=i+p_i,\quad A_i=2^{a_i},\quad
 C_i=\sum_{j<i} e_j2^{j+p_j}3^{i-1-j},\quad U_i=A_i/Q_i,\quad W_i=C_i/A_i .
\]
The zero-trial companion \(W_i\) satisfies \(2^{1+e_i}W_{i+1}=3W_i+e_i\). The closed rational companion phase is \(C_i/(A_i-Q_i)\), with reduced denominator \(|A_i-Q_i|/G_i\) for \(G_i=\gcd(|A_i-Q_i|,C_i)\). This cancellation is prime to six for \(i\ge1\).

Use the actual dyadic value \(D(x)=\sum_{j\ge0}e_j2^{j+p_j}/3^j\) calculated on the parity stream from \(x\). Put
\[
 \alpha=D(n)/3,\qquad s_i=-D(x_i)/3,\qquad C_i=\alpha Q_i+A_i s_i .          \tag{1}
\]
This is exact prefix splitting in \(\mathbb Q_2\), with \(\alpha,s_i\in\mathbb Z_2\). For distinct ordinary \(x,y\), their parity streams agree for exactly \(t=v_2(x-y)\) bits, since each shared branch reduces the difference valuation by one. At the first disagreement their companion digits have opposite parity, and each earlier shared bit contributes one plus that bit to the difference valuation. Hence \(v_2(D(x)-D(y))=t+p_t(x)\le2t\). The \(s_i\) are therefore distinct and \(s_i+\alpha\ne0\) for \(i>0\) on the fixed escape. [PR182, dyadic splitting and rationality](https://github.com/GettysburgResearch/collatz/blob/234fd2ece3a17c8950dce452291198705b4e6e60/research/high-variance-closure-20261124/ordinary-arithmetic/DYADIC_COMPANION.md) · [Round-six agreement](../../round6/arithmetic/COMPANION.md)

The physical record gives a uniform real estimate. Every input on an escape exceeds 5, by finite convergence below six. On an even edge \(2x_{j+1}=x_j\), and on an odd edge \((2x_{j+1})^3=(3x_j+1)^3\le32x_j^3\), since \(19^3<32\cdot6^3\) at \(x_j\ge6\). Multiplying on a segment of length \(h=i-j\) with \(p\) odd bits gives \((2^h x_i)^3\le 2^{5p}x_j^3\). With \(\kappa=\log(256/243)/5>0\), this implies
\[
 U_i/U_j\ge e^{\kappa(i-j)}(x_i/x_j)^{3/5},\qquad
 W_i=\tfrac13\sum_{j<i} e_j U_j/U_i
 \ \le\ \frac{1}{3(e^\kappa-1)}
       \left(\frac{\max_{j\le i}x_j}{x_i}\right)^{3/5}.                    \tag{2}
\]
Taking \(j=0\) gives \(U_i\to\infty\). At a physical record the trial has an absolute upper bound.

## Integral determinant and local size

Fix degree \(d\ge1\). The space \(V\) of degree-\(d\) homogeneous forms in \(Q,A,C\) vanishing at \(R=(1:1:0)\) has dimension \(M=(d+1)(d+2)/2-1\). Use its integral basis \(Q^u(A-Q)^v C^w\), where \(u+v+w=d,\ v+w>0\). At \((Q_i,A_i,C_i)\) the gcd of the entire row is exactly \(G_i\). Every entry contains \(A_i-Q_i\) or \(C_i\). Conversely the entries include \((A_i-Q_i)^d,Q_i^{d-1}(A_i-Q_i),Q_i^{d-1}C_i\), and \(\gcd(Q_i,A_i-Q_i)=1\). This proves the converse for every prime power, also for \(d=1\).

Take \(M\) positive clocks \(N\le i_1<\cdots<i_M\le N+K\). Let \(J\) be the determinant of their evaluation rows, and put \(E=\binom{d+2}{3}\), the sum of the exponents of a single variable across all degree-\(d\) monomials, by symmetry or direct summation. Write \(w=\max_t\log^+ W_{i_t}\), with \(\log^+0=0\). Whenever \(J\ne0\) and \(N\) is sufficiently large,
\[
 \sum_t\log G_{i_t}\le d\log A_N+
          E\bigl((\log48)K+w\bigr)+O_{n,d}(1).                             \tag{3}
\]

In each unrestricted local monomial basis choose a pivot \(b_p\) nonzero at \(R\). The \(b_j-b_j(R)b_p/b_p(R)\) for \(j\ne p\) form a basis of \(V\) by their coefficients away from the pivot. Changing from the integral basis contributes fixed nonzero local determinant factors. At 2 the change is unimodular over \(\mathbb Z_2\), since the triangular change \(C\mapsto C-\alpha Q\) and its inverse are integral, the pivot evaluates to one, and eliminating this pivot splits off the evaluation at \(R\). The corresponding changes at three and infinity between the two integral monomial bases have determinant \(\pm1\). Write \(Q_-=Q_N,\ Q_+=Q_{N+K},\ A_-=A_N,\ A_+=A_{N+K}\). The bounds below apply to the determinant after the indicated column changes.

| Place | Coordinate basis and omitted pivot | Upper bound |
|---|---|---|
| Real | \(Q,A,C\), pivot \(Q^d\) | \(2^M M! (Q_+ A_+^2 e^w)^E/Q_+^d\) |
| 2 | \(Q,A,C-\alpha Q\), pivot \(A^d\) | \(A_-^{-2E+d}\) |
| 3 | \(Q,A,C\), pivot \(Q^d\) | \(Q_-^{-E+d}\) |

At infinity \(A_+\ge Q_+\) eventually by (2), and only the monomials without \(C\) need a subtraction. On those columns the pivot's size is at most the column bound. At 2, both \(A\) and \(C-\alpha Q\) have norm at most \(A_-^{-1}\) and the subtraction coefficient is dyadically integral. At 3 all the coordinates are integral and \(|Q|_3\le Q_-^{-1}\). Ultrametric determinant bounds have no factorial loss. Multiplication gives (3) since \(A_+/A_-\le4^K,\ Q_+/Q_-=3^K\). Indeed the integer \(J\) is divisible by \(\prod_t G_{i_t}\), which is coprime to six, so \(|J|_\infty |J|_2 |J|_3\ge\prod_t G_{i_t}\). These bounds allow an arbitrary, possibly transcendental \(\alpha\).

## Why the determinant is nonzero

Put \(t_0=0,\ t_j=i_j\) for \(1\le j\le M\), and define
\[
 r=\max_{0\le j<l\le M}v_2(x_{t_j}-x_{t_l}),\qquad
 g=\min\bigl(N,\min_{1\le j<M}(i_{j+1}-i_j)\bigr).
\]
The degree-group sizes are \(m_k=k+1\) for \(0\le k<d\), and \(m_d=d\). Then
\[
 B_d=2\left(d+\sum_{k=0}^{d}\binom{m_k}{2}\right),
 \qquad\qquad g>B_d r\ \Longrightarrow\ J\ne0 .                            \tag{4}
\]

Divide row \(i\) locally by its dyadic unit \(Q_i^d\). In the preceding dyadic basis the columns of degree \(k<d\), indexed by \(0\le j\le k\), are exactly \(U_i^k s_i^j-(-\alpha)^j U_i^d\). The top columns \(1\le j\le d\) are \(U_i^d(s_i^j-(-\alpha)^j)\). Temporarily ignore the lower columns' correction terms. The smallest possible sum of exponents of two from the \(U_i\) in a determinant term is
\[
 T=\min_\pi\sum_{t=1}^{M} a_{i_t} k_{\pi(t)} .
\]
It pairs the largest degrees with the smallest clocks. Every permutation violating these degree groups costs at least \(T+g\), because swapping an inverted pair decreases its sum by \((a_{i_l}-a_{i_j})(k_{\pi(l)}-k_{\pi(j)})\ge g\). Every term taking a correction from a lower column also costs at least \(T+g\). Its uncorrected assignment already costs at least \(T\), and the new exponent increases by \((d-k)a_i\ge N\). All other factors are dyadically integral.

Sum the terms respecting the minimal degree groups before taking valuations. After factoring the fixed powers of \(U_i\) from each assigned row, the result up to sign is a product of ordinary Vandermonde determinants in the \(s_i\) within each group. Every top-block row additionally contributes \(s_i+\alpha\), since \((s^j-b^j)/(s-b)\), for \(b=-\alpha,\ 1\le j\le d\), are monic of successive degrees \(0,\ldots,d-1\). The leading sum's valuation is \(T\) plus the valuations of precisely these pairwise differences and top-row factors. By (1) the extra valuation is at most \(B_d r\). Under (4) all remaining terms have strictly higher valuation, proving nonvanishing.

## Consequences for actual escape clocks

Choose \(d\) so \(d\log4<M\epsilon/2\), then choose a fixed \(0<\delta<1\) such that \(E(\log48+1)\delta<M\epsilon/4\). For all large \(N\), there cannot be \(M\) exceptional clocks satisfying all three conditions
\[
 K\le\delta N,\qquad w\le\delta N,\qquad g>B_d r .                          \tag{5}
\]
Otherwise (3) and (4), with \(A_N\le4^N\), contradict \(\sum_t\log G_{i_t}\ge M\epsilon N\). Thus \(M\) such losses satisfying the first two conditions force some marked pair, possibly involving \(n\), to have at least \(g/B_d\) identical physical parity bits. This local conclusion holds without any bound on the orbit growth.

For the counts put \(h_N=1+\max_{j\le2N}\log_2(1+x_j)\), so \(r<h_N\). In the stated growth ranges \(h_N=o(N)\), and (2) gives \(w=o(N)\). Greedily selecting exceptional clocks in \([N,N+\lfloor\delta N\rfloor]\), each more than \(B_dh_N\) after the preceding selection, gives at most \(M-1\) marks by (5), since \(N>B_dh_N\) eventually. The exceptions there are covered by at most \(M-1\) intervals of length \(1+\lceil B_dh_N\rceil\). Each dyadic shell \([2^j,2^{j+1}]\) requires \(O_\delta(1)\) multiplicative intervals, allowing for endpoint rounding. Under polynomial growth this gives \(O(j+1)\) exceptional clocks in that shell. Under the second growth bound it gives \(O(2^{j\beta})\). Summing proves both counts, and the covering argument applies more generally to subexponential heights. Along these escapes the separate physical cancellation satisfies \(\log G_i^{\rm phys}\le\log|x_i-n|=o(i)\) directly.

The results require no exceptional clock to exist. Reduced denominators of rational periodizations may grow on an escape. At a complete physical lap \(x_L=n\), the dyadic factor \(s_L+\alpha\) vanishes. Distinctness and the nonvanishing proof fail at that exact return. A positive source on the standard cycle supplies an actual repeated phase. Proving unavoidable losses and ruling out their accompanying long physical agreements, or proving triadic membership of the genuine scalar directly, remains open.

The Lean module verifies complete row content, the physical path inequality, the local kernel coordinate check, the inversion debit and the general top-block determinant with its extra product. The rearrangement across several degree blocks, local height estimates and infinite consequences are written proofs. The exact checker evaluates 230 integer determinants. It checks 117 leading valuations, exercises the strict spacing criterion in all three tested degrees and includes returns of the standard cycle with zero determinant. All tests concern finite inputs. [Lean module](CompanionContent.lean) · [Exact checks](check.py)

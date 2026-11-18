# Finite synchronous coalescence in every interval

Paper 28 obtains a stronger power for labelled images at a squared-logarithmic clock. Its two-window estimate also yields a labelled logarithmic-clock refinement when a linearly growing threshold is used. [Comparison and deduction](PRIOR_WORK.md)

**PROPOSED.** Throughout, \(T\) is the shortcut Collatz map and positive integers are the inputs. For \(X\ge2\), put \(L(X)=\lfloor\log_2 X\rfloor\). Set \(p=\log_3 2,\ h=H_2(p)\), and \(\kappa=\log(p/(1-p))/\log 3\). Fix \(\rho\) with
\[
 \max(\kappa,1-h)<\rho<1 .
\]
For example \(\rho=3/4\) works. For every integer \(j\ge0\), every real interval \(I\) of length \(X\ge16\), and every integer \(r\ge jL(X)\),
\[
 \# T^r(I\cap\mathbb N_{>0})
 \ \le\ C_\rho\,\frac{X^{h+e_0\rho^j}}{(\log X)^{3/2}},
 \qquad e_0=2(1-h).                                          \tag{1}
\]
The constant is independent of \(j,r\) and the location of the interval. In particular the exponent penalty is bounded by a constant factor once \(j\ge\log(\log X)/|\log\rho|\). Thus a common clock \(O(\log X\log\log X)\) suffices for the critical translated-window estimate. Images at later times can only lose cardinality.

## Proof

Use the [critical window proof](CRITICAL_MOMENT.md) for the curved-barrier estimate, affine endpoint interval, and parity word count. Let \(F(X)=X^h/(\log X)^{3/2}\). The case \(j=0\) follows from the trivial count \(X+1\), since \(h+e_0>1\). Bounded initial scales may use the trivial count uniformly over all \(j\).

Suppose (1) holds at stage \(j-1\), write \(e=e_0\rho^{j-1}\), and take \(X\) large. With \(L=L(X)\), \(u(t)=\min(t,L-t)\), and \(c_u=K(u+1)^2\), capture a source at any lag \(1\le t\le L\) with
\[
 2\cdot 3^{q_t-pt}\le X^{-e}/c_{u(t)}.
\]
The uncaptured words satisfy the symmetric curved barrier with lower bound at both ends \(-a\), where \(a=\log_3(2K)+e\log_3 X\). The logarithmic curvature coefficient is fixed. Keeping the dependence on \(a\) in the word count gives
\[
 \#\{\text{uncaptured sources}\}
 \le C_p\,\frac{X^h}{L^{3/2}}(1+a)
          \sum_{d\ge-a} e^{-\lambda d}(1+a+d)
 \le C_K F(X)(1+e\log X)X^{\kappa e},
 \quad \lambda=\log(p/(1-p)).
\]
Here \(d=q_L-pL\) runs on a unit lattice, and the shifted geometric sum costs \(O(e^{\lambda a})\). Since \(\rho>\kappa\), the last bound is at most \(C_{K,\rho} F(X)X^{\rho e}\), with a constant uniform down to \(e=0\). At most two starting values occupy each length-\(L\) parity cylinder in \(I\).

For each captured pair \((t,q_t=q)\), all endpoints lie in an interval of width \(Y=2\cdot3^{q-pt}X\le X^{1-e}/c_{u(t)}\). This follows from the fixed-weight affine bound in the critical proof. The number of distinct endpoints at the final clock via this pair is at most the image cardinality of the entire new interval after \(r-t\) steps. When \(Y\ge\sqrt X\), the remaining clock satisfies
\[
 r-t\ge(j-1)L(X)\ge(j-1)L(Y).
\]
Apply the induction hypothesis. Since \((1-e)(h+e)\le h+(1-h)e\le h+\rho e\), and summing the geometric widths over \(q\) costs at most \(1/(1-3^{-h})\),
\[
 \sum_{t,q:\,Y\ge\sqrt X}\frac{Y^{h+e}}{(\log Y)^{3/2}}
 \ \le\ \frac{2^{5/2}\sum_{u\ge0}c_u^{-h}}{1-3^{-h}}\,
           F(X)X^{\rho e}.
\]
Choose \(K\) once so the coefficient is below \(1/2\). Smaller intervals cost \(O(L^2(1+\sqrt X))=o(F(X))\) in total, by trivial counting before any remaining steps. Choose the common multiplier at least twice the nonrecursive constants. The induction is complete. All costs count unions of final image sets and allow unlimited collisions. No exponent loss or constant compounds with \(j\).

## Component and lower-source consequences

For an interval containing \(n\) positive integers, choose one representative for each distinct value at the common clock \(r\). Every other input merges at that clock with its own representative. Choosing each representative as the smallest input in its fiber certifies a strictly smaller source in the same interval for every nonrepresentative. For \(n\) comparable to the large width \(X\), the number of exceptions is \(O(F(X))\) at the critical clock and the fraction is \(O(X^{h-1}/(\log X)^{3/2})\).

If the fiber sizes are \(m_y\), Cauchy–Schwarz gives \(\sum_y m_y^2\ge n^2/\#T^r(I)\). In particular some fiber contains \(\gg X^{1-h}(\log X)^{3/2}\) inputs when \(n\) is comparable to \(X\). Summation includes ordered pairs and the diagonal. The estimates identify neither a prescribed collision partner nor a specified terminal value.

A set on which all \(T^r\) are injective therefore satisfies the critical translated-window bound, even without forward invariance: apply (1) to the interval and use injectivity at the displayed single final clock. The same reasoning covers a finite cohort collision-free only through that clock. Different equal-time classes may belong to the same connected component, since two sources can reach the same state at unequal lags. A universal lower-source merger, an upper bound on the basin of a particular divergent trajectory, and Collatz itself remain open.

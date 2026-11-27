# A fixed predecessor-density floor reduces to finitely many ordinary seeds

Let \(T\) be the positive shortcut map, \(\mathcal P(v)\) the set of starts whose orbit visits \(v\), and \(d(v)\) any common subsequential predecessor-density profile as in [the sibling-share lemma](SIBLING_SHARES.md). For odd targets the ordinary and shortcut predecessor sets coincide. We use two external results. Positive odd targets prime to three have positive lower predecessor density. The natural density at every odd target exists, and Weaver's Theorem 11 gives the following uniform estimate, for each \(A>0\), with \(C_A\) independent of \(M\) and \(v\):

\[
 \mathcal P(v)\cap[1,M]=\varnothing
 \quad\Longrightarrow\quad
 d(v)\le C_A(\log M)^{-A},\qquad M\ge2.
\]

The value at an odd target is therefore the same in every common profile. Weaver derives this estimate from the cited uniform first-passage and minimum-tail inputs. These external analytic results are used as stated. The elementary deductions below have a written proof. [Mazur, fixed-target positivity](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) · [Weaver, Paper 12, Theorem 11, equation (35) and the ensuing basin estimate](https://rstation.ai/problems/collatz/papers/12)

Fix \(\eta>0\) and choose an integer \(M_\eta\ge2\) with \(C_1/\log M_\eta<\eta\). Then

\[
 \{v\text{ odd}:3\nmid v,\ d(v)\ge\eta\}
 \ \subseteq\ \bigcup_{q=1}^{M_\eta}\{T^j(q):j\ge0\}.                 \tag{1}
\]

Indeed a high-mass target has a positive predecessor \(q\le M_\eta\), by contraposition of the uniform bound. If every ordinary orbit is bounded, each orbit on the right is eventually periodic and has finitely many distinct states. This proves finiteness of the whole left side for each \(\eta\), including in the possible presence of nontrivial positive cycles. Conversely an escaping path has an odd ternary-unit seed \(s\), with \(d(s)>0\), and infinitely many distinct subsequent odd ternary units \(x_j\). Nesting gives \(d(x_j)\ge d(s)\) at every index. Thus the high-mass sector is infinite for some fixed \(\eta>0\) exactly when an escaping orbit exists.

For a common profile consider the following proposed comparison. For every \(\eta>0\) there should be constants \(c_\eta>0\) and \(X_\eta\) such that every odd ternary unit \(x\ge X_\eta\) with \(d(x)\ge\eta\) satisfies

\[
 \frac{d(3x+1)}{d(Tx)}\ge\frac{c_\eta}{\log(2+x)}.                   \tag{2}
\]

Under the external inputs, (2) holds for some common profile **if and only if every positive ordinary orbit is bounded**. With all orbits bounded, (1) makes (2) vacuous above the largest high-mass state, for each \(\eta\) and every common profile. With an escaping orbit, take \(\eta=d(s)\). The sibling-share lemma gives \(\liminf_j\log(2+x_j)\,d(3x_j+1)/d(Tx_j)=0\) on that path for every common profile. The states \(x_j\) tend to infinity. Hence (2) fails for this fixed \(\eta\), at arbitrarily large states, for any chosen \(c_\eta>0\). The common-subsequence argument accommodates the even targets in the ratio directly. An independent construction of an unbounded sequence of counterexamples at fixed positive mass would itself establish existence of an escaping ordinary orbit.

Valbuena established the general equivalence between sublinearity of the canonical trace and eventual periodicity, with fixed-target predecessor positivity. Wren's Proposition 4 credits that equivalence and gives quantitative forward-excursion variants. The deduction here identifies which ordinary seed orbits can witness failure of the full even-parent comparison. Weaver's Paper 202 examples have \(d(x)\asymp(\log x)^D/x\to0\) for each fixed \(D\), so they address the unrestricted comparison. The value of the boundedness assertion in (2) remains unknown. [Valbuena, *Collatz basin densities and canonical traces from first-passage stabilization*](https://doi.org/10.5281/zenodo.23025885) · [Wren, Paper 105 v2, Proposition 4](https://rstation.ai/problems/collatz/papers/105/v2) · [Weaver, Paper 202 v1, Corollary 2](https://rstation.ai/problems/collatz/papers/202/v1)

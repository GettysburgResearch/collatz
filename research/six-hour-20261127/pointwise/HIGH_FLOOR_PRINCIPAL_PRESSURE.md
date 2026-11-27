# Exact principal-source moment rates above a physical floor

Use the original independent Syracuse letters with probabilities \(2^{-e}\). For a word of length \(n\) let \(A_i\) be its cumulative division clock, \(A=A_n\), \(m\) its least positive odd source, \(x_i=U^i(m)\), \(y=x_n\), and \(G=\sum_{i<n}2^{A_i}/3^{i+1}\). Set
\[
 Z_n(z)=\frac{2^A}{m+zG},\quad
 F_{H,n}=\{x_i>H\text{ for }0\le i\le n\},\quad
 W_n=\{4A_i\le7i\text{ for }1\le i\le n\}.
\]
Here \(z\ge0\) and the real physical floor \(H\ge0\) are fixed. For an ordinary positive odd cycle \(C\) of odd period \(P_C\) and division sum \(A_C\) put \(r_C=2^{A_C/P_C}\). Define
\[
 R_H=\sup\bigl(\{3\}\cup\{r_C:\min C>H\}\bigr),\qquad
 R_H(z)=\begin{cases}R_H&z=0,\\3&z>0.\end{cases}
\]
All these suprema are finite, as \(r_C\le4\).

**Theorem.** For every fixed real \(p>1\),
\[
 \lim_{n\to\infty}\frac1n\log\mathbb E[\mathbf1_{F_{H,n}} Z_n(z)^p]
       =(p-1)\log R_H(z).                                           \tag{1}
\]
Moreover \(\gamma=(7/8)(7/6)^{3/4}\) gives
\[
 \lim_{n\to\infty}\frac1n\log\left(
  \Pr(W_n)^{1-1/p}\|\mathbf1_{F_{H,n}} Z_n(z)\|_p\right)
       =(1-1/p)\log(\gamma R_H(z))>0.                               \tag{2}
\]
Even choosing \(p=p_n\ge1\) arbitrarily cannot make the separated expression converge to zero. For \(H=1\), the centered rate in (1) is strictly greater than the positive-tilt rate exactly when there exists a nontrivial ordinary cycle. Formula (1) leaves that centered value unevaluated. The separated expression is a product of two marginals; the windows giving its source lower bound need not satisfy the prefix gate. Its growth proves no survival of a fixed gated source.

## The ordinary octave lower bound

Write \(\lambda=\log_2 3\), \(b=2-\lambda=\log_2(4/3)\). Fix \(b<t<2\), choose \(k=\lfloor tn\rfloor\), and use odd sources \(v\in[2^k,2^{k+1})\). For every fixed sufficiently small \(\epsilon>0\), outside a vanishing fraction of that octave simultaneously for all \(0\le i\le n\),
\[
 |\log_2 U^i v-\log_2 v+bi|\le\epsilon\log_2 v.                    \tag{3}
\]
This is Inselmann's odd-Syracuse Theorem 3.8, arXiv:2402.03276v3, which has the explicit time range \(i\le\log_2v/\log_2(4/3)\) and both multiplicative error factors \(v^{\pm\epsilon}\). Since \(t>b\), the full specified horizon lies in that range eventually. The theorem's power-saving exceptional bound among odd integers up through a height implies a vanishing fraction in every dyadic octave by applying it at the octave's upper endpoint. Equation (5) of the permanent-entry manuscript with empty exceptional target set is an alternative written finite-ordinary proof of the same shorter-clock input by consecutive blocks. No assumption of independent physical parity after the source bits run out occurs in either application. [Inselmann, Theorem 3.8, p. 29](https://arxiv.org/pdf/2402.03276v3)

All intermediate heights on these paths exceed \(2^{cn}\) for some \(c>0\) on choosing \(\epsilon\) small in terms of \(t-b\). The true product identities give
\[
 A=n\lambda+\log_2 v-\log_2 U^n v+
       \sum_{i<n}\log_2(1+1/(3U^iv))
       =2n+O(\epsilon t n)+O(1),
 \qquad G/v=\prod_{i<n}(1+1/(3U^iv))-1=o(1) .
\]
The error constant in the clock bound can be taken absolute for fixed \(t\in(b,2)\). Since \(t<2\), this implies \(v<2^{A+1}\) for all large \(n\), so each of these actual sources is the principal representative of its own length-\(n\) word. Different such sources produce different words. Their reciprocal sum is bounded below by an absolute constant, since asymptotically all the odd sources of the octave qualify. Each satisfies \(F_{H,n}\) and
\[
 Z_n(z)\ge 2^{(2-t-O(\epsilon t))n-O(1)} .
\]
For fixed \(z\) the sum of \(1/(v+zG)\) over these sources stays bounded below, say by \(c_0>0\). The original mass of a word is \(2^{-A}\), so its contribution to the moment is exactly \(Z_n(z)^{p-1}/(v+zG)\). Keeping these distinct terms, letting \(n\to\infty\) first, then \(\epsilon\downarrow0\) and \(t\downarrow b\), proves the lower exponent \((p-1)\log3\). The post-window futures of these sources have no restrictions.

## The upper envelope and the centered cycle term

The unfiltered principal first moment satisfies \(\mathbb E Z_n(z)\le \mathbb E Z_n(0)\le n+1\) by the sibling bound of PR 201. The affine identity \(2^Ay=3^n(m+G)\) gives \(Z_n(z)\le 3^n\max(1,1/z)\) at every \(z>0\). This yields the matching upper bound for all positive tilts.

At \(z=0\) use
\[
 Z_n(0)=\frac{3^n}{y}\prod_{i<n}\left(1+\frac1{3x_i}\right).
\]
The correction product on every **simple** finite segment, over its departing odd states, is bounded by one absolute constant \(K\) by the uniform finite simple-trajectory reciprocal bound. This argument allows arbitrary initial height, length and final height. A repeated state implies a complete ordinary cycle was traversed. Split the prefix into a simple preperiod, complete laps, and a final simple portion of one lap. Every such cycle in \(F_{H,n}\) has all its odd sites above \(H\). The correction product over its complete lap is exactly \((r_C/3)^{P_C}\) by the cycle product identity, and \(r_C>3\). The simple pieces together cost at most \(K^2\), independently of the cycle or its period. Hence \(Z_n(0)\le K^2 R_H^n\) everywhere on \(F_{H,n}\). Multiplying its \((p-1)\)st power by the unfiltered first moment bounds the upper exponential rate in (1). For the opposite inequality, fix any cycle wholly above the floor and any odd phase \(v\) in it. Its true length-\(n\) word is eventually principal at \(v\) because its dyadic modulus goes to infinity. Its one centered moment contribution is \(v^{-p}2^{(p-1)A_n}\), with \(A_n/n\to A_C/P_C\). Taking the supremum over these cycles and combining with the physical octave bound proves (1), including the case that the collection of cycles is empty. The upper bound \(r_C\le4\) follows from \(3(1+1/(3x_i))\le4\) at every positive site. [Finite simple-path reciprocal estimate](https://github.com/GettysburgResearch/collatz/blob/cd1b3689e8d37fc4232945072e2faf6bd5ee47bd/research/astra-three-routes/pass3/FINITE_RECORDS.md)

## The separated gate probability

Let \(D=\lfloor 7n/4\rfloor\). Every composition of \(D\) into \(n\) positive parts has a cyclic rotation passing the gate. Start where the prefix sum \(4A_j-7j\) is maximal; for a wrapped prefix the total drift \(4D-7n\le0\) gives the same inequality. Each accepted word can represent at most \(n\) rotations. Consequently
\[
 \Pr(W_n)\ge \binom{D-1}{n-1}2^{-D}/n .
\]
Stirling's formula gives exponential base \(\gamma\). For the upper bound use \(W_n\subset\{A\le7n/4\}\) and \(\mathbb E(6/7)^e=3/4\), giving \(\Pr(W_n)\le\gamma^n\). Equation (2) follows. Its rate is positive already because the all-one word implies \(\gamma\ge1/2\) and \(R_H(z)\ge3\).

For varying \(p_n\ge1\), take \(t=1\) and a sufficiently small fixed tolerance in the octave lower bound to get \(Z_n(z)\ge2^{0.9n}\) and \(\sum1/(v+zG)\ge c_0\) at every large \(n\). The same gate computation gives \(\Pr(W_n)\ge(9/10)^n\) eventually (or use the earlier 512-letter explicit bound). Hence the separated expression is at least
\[
 c_0^{1/p_n}\big[(9/10)2^{0.9}\big]^{n(1-1/p_n)}
 \ \ge\min(1,c_0)>0 .
\]
This proof covers every finite \(p_n\), and the supremum norm endpoint follows from the same pointwise witnesses if desired.

The preceding elementary inverse-tree certificate for \(p\ge4/3\) retains a separate property: every window furnishing its bound can be chosen to go to one on the very next odd step. The sharper result here imports the physical density envelope and imposes no post-window condition. The relation between centered and positive-tilt growth isolates possible cycles but supplies no argument evaluating the centered pressure at a high floor, excluding a cycle, or eliminating an escaping ordinary orbit.

Prepared by the binary-energy reviewer, 27 November 2026 UTC.

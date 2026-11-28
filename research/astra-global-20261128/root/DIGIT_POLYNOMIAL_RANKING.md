# No polynomially position-weighted local digit ranking in any integer base

**Written theorem, with an external classical equidistribution input.** The argument below concerns the actual positive-integer shortcut map
\[
 T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]
It is a restriction on a family of termination proofs. It proves neither convergence nor divergence of a Collatz orbit.

Fix an integer radix \(p\ge2\), a finite window radius \(r\), and a finite polynomial degree \(D\ge0\). Write the terminating base-\(p\) numeral of \(n\ge1\) as \(d_0\ldots d_{L-1}\), least significant digit first. Use two distinct sentinels below position zero and above position \(L-1\), respectively. At each genuine digit position let \(w_i(n)\) be its radius-\(r\) window. For arbitrary real coefficient functions \(A_0,\ldots,A_D\) on these finitely many windows, and an arbitrary bounded real function \(b\), put
\[
 F(n)=b(n)+\sum_{i=0}^{L(n)-1}\sum_{j=0}^D i^j A_j(w_i(n)).             \tag{1}
\]
The coefficient functions, radius, degree and bound on \(b\) are fixed independently of \(n\). Interpret \(i^0=1\), including at zero.

## The theorem

There is a structural statement without any lower-bound assumption: **if both actual branches have a finite uniform upper bound on their change in \(F\), then \(F(n)=\gamma L(n)+O(1)\) for some real \(\gamma\)**. All polynomially weighted local terms reduce to this linear length term and a bounded correction.

If \(F\) is bounded below on the positive integers, there do not exist a real constant \(a\), a positive constant \(\epsilon\), and a floor \(X_0\) such that both
\[
 \begin{split}
 F(n/2)-F(n)&\le a &&(n>X_0\text{ even}),\\
 F((3n+1)/2)-F(n)&\le-\epsilon &&(n>X_0\text{ odd}).
 \end{split}                                                        \tag{2}
\]
Thus **every fixed width and every fixed polynomial degree fail in every integer base**, even with a bounded correction. In particular no lower-bounded score in (1) can satisfy a parity price \(a-b(n\bmod2)\) with \(a<b\). This includes all the prices in the descent criterion of Paper 189, and also prices which would not by themselves prove descent.

Without a lower bound on \(F\), there is a sharp classification: a score of the form (1) satisfying (2) exists **if and only if**
\[
                 a\ge\epsilon\frac{\log2}{\log(3/2)}.                 \tag{2a}
\]
At and above this boundary the simple score \(F(n)=-c\log n\) works for a suitable positive \(c\). Below it, no radius, degree, radix or bounded correction helps. In the price notation \(a-b(n\bmod2)\), with \(b>0\) and \(a<b\), the boundary is exactly \(a/b=\log_3 2\).

The conclusion allows either sign for the even-step allowance. A term \(c\log n\), for any real \(c\), is already covered: it equals \(c(\log p)L(n)\) plus a uniformly bounded function. Fixed polynomials in numeral length times a fixed leading-digit function are also representable by the top sentinel window, after increasing the fixed radius. Products of independent global digit statistics and arbitrary unbounded corrections are outside the stated class.

### Relation to the current literature

[Paper 189, current version 2 of 23 November 2026](https://rstation.ai/problems/collatz/papers/189) gives exact finite balanced-step certificates for position-weighted ternary windows of widths one and three above every floor, and width five at the floor 64. Its Section 6 still leaves wider windows and larger floors for width five open. We checked both the original and current versions. Those certificates do not require a lower bound on the potential and do not allow an arbitrary bounded correction. The sharp boundary (2a) here needs no lower bound either and handles all widths, polynomial degrees and bounded corrections. The stronger impossibility for every even allowance does require lower-boundedness. The analytic obstruction in this manuscript alone does not supply finite balanced-step certificates: infeasibility of an infinite family of halfspaces is not, without an additional argument, a finite Farkas certificate. The companion [finite-witness theorem](../escape/DIGIT_RANKING_FINITE_WITNESSES.md) supplies that argument through unit-core recession neutrality and a coercive finite subcover, and proves finite integer certificates at every width, degree, radix and floor.

The entropy-to-coboundary method is prior work. Nashida and [Paper 98, Lemmas 2–3](https://rstation.ai/problems/collatz/papers/98) use it for unweighted binary window scores, including valuation terms. Here the new steps are the polynomially weighted invariant-measure limit, the reduction of the leading polynomial degree, and the treatment of the leading-digit boundary by an actual odd-edge average. The proof extends the argument across all integer radices; it does not include the valuation terms of Paper 98.

The only non-elementary input used below is the following established equidistribution theorem: if a circle probability is invariant, ergodic and has positive entropy for multiplication by \(p\), then almost every point is normal for multiplication by any multiplicatively independent integer \(q\). We checked the exact statement in [Hochman, *A short proof of Host's equidistribution theorem*, Theorem 1.1, corrected version 2](https://arxiv.org/html/2103.08938v2). Host proved the coprime case; Lindenstrauss and Hochman–Shmerkin extended it, as credited there. No unproved Collatz density, randomness or convergence statement enters this argument.

## 1. A weighted digit limit under an invariant measure

Let \(M_c(u)=cu\bmod1\) on the circle. For an interior window weight \(B\) of width \(2r+1\), let \(\widetilde B\) be the corresponding step function on the leading \(2r+1\) fractional base-\(p\) digits. Reverse their order when necessary to match our least-to-most-significant window convention. Define
\[
 \Lambda_B(\nu)=\int\widetilde B\,d\nu.
\]
It is a bounded function with finitely many discontinuities. If \(F\) has degree at most \(D\) in (1), write \(B=A_D\) on the interior windows; sentinel windows are omitted from \(B\).

**Lemma 1.** Suppose \(\nu\) is a non-atomic \(M_p\)-invariant circle probability, \(U\sim\nu\), and \(X_L=\lfloor p^L U\rfloor\). Extend \(F\) arbitrarily to zero. For fixed integers \(c\ge1\) and \(q\ge0\),
\[
 \lim_{L\to\infty}\frac{\mathbb E F(cX_L+q)}{L^{D+1}}
       =\frac{\Lambda_B((M_c)_*\nu)}{D+1}.                            \tag{3}
\]

**Proof.** First consider \(Z_L=\lfloor p^L cU\rfloor\). Below its bounded integer prefix, its \(L\) fractional digits come from the circle point \(M_c U\), whose law \(\nu_c=(M_c)_*\nu\) is still non-atomic and \(M_p\)-invariant. Every interior block in these fractional digits has the same expected weight \(\Lambda_B(\nu_c)\). Consequently their expected position-weighted sum is
\[
 \Lambda_B(\nu_c)\sum_{i=0}^{L-1} i^D+O_c(L^D).
\]
The bounded number of boundary windows and integer-prefix digits costs \(O_c(L^D)\). All lower polynomial degrees together cost \(O(L^D)\). When \(cU<1\), an initial string of zero digits is absent from the canonical numeral. For almost every \(U\) its length is finite and independent of \(L\) once \(L\) is large. Its contribution divided by \(L^{D+1}\) tends to zero; the uniform \(O(L^{D+1})\) bound permits dominated convergence. The null cases where \(cU\) is an integer do not matter. Since \(L^{-D-1}\sum_{i<L}i^D\to1/(D+1)\), this proves (3) for \(Z_L\).

The difference between \(cX_L+q\) and \(Z_L\) has absolute value at most a fixed integer \(C\). Fix a digit cutoff \(K\). A bounded addition can alter a digit at or above position \(K\) only if
\[
 \{p^{L-K}cU\}\in [0,(C+1)p^{-K}]\ \cup\ [1-(C+1)p^{-K},1).
\]
By invariance this event has probability at most \(\nu_c(J_K)\), independently of \(L\ge K\), where \(J_K\) is the displayed neighborhood of the circle point zero. Non-atomicity gives \(\nu_c(J_K)\to0\). Off this event the two integers have identical high digits; only \(O_r(K+1)\) low-position windows can change, at total cost \(O_r((K+1)^{D+1})\). If both integers are below \(p^K\), the same bound applies to their whole numerals. On the exceptional event use \(O_c(L^{D+1})\). Taking \(L\to\infty\), then \(K\to\infty\), proves that the bounded addition changes the normalized expectation by zero. The arbitrary bounded term in (1) also disappears. This proves the lemma. \(\square\)

This argument uses exact digit stationarity and a non-atomic carry estimate. It makes no independence assertion about the digits of \(U\), or about an integer's Collatz trajectory.

## 2. The top interior coefficient is a constant plus a finite coboundary

Assume (2). For each fixed \(j\), iteration of the even inequality gives
\[
 F(2^j x)-F(x)\ge-ja
\]
for sufficiently large \(x\). The finitely many remaining \(x\) can be absorbed in a constant depending on \(j\). Lemma 1 therefore gives, for every non-atomic \(M_p\)-invariant \(\nu\),
\[
       \Lambda_B((M_{2^j})_*\nu)\ge\Lambda_B(\nu).                    \tag{4}
\]

If \(p\) is not a power of two, \(p\) and two are multiplicatively independent. Take \(\mu\) to be the circle image of any stationary full-support Markov measure on the base-\(p\) digits of order \(2r\). Its finite transition graph is irreducible and aperiodic, so this measure is ergodic for \(M_p\); its entropy is positive, and it has no atoms. The equidistribution input says that the Cesàro averages of \((M_{2^j})_*\mu\) converge weakly to Lebesgue measure. Integration of \(\widetilde B\) passes to the limit because its discontinuities form a finite Lebesgue-null set. Equation (4) yields
\[
                  \Lambda_B(\mathrm{Leb})\ge\Lambda_B(\mu).           \tag{5}
\]

For completeness the powers of two have a separate route. Write \(p=2^k\), \(k\ge1\). The actual odd identity \(T(2x+1)=3x+2\) and Lemma 1 give
\[
                 \Lambda_B((M_3)_*\nu)\le\Lambda_B((M_2)_*\nu).      \tag{6}
\]
Apply (6) successively to the non-atomic invariant measures
\((M_{3^i2^{k-1-i}})_*\nu\), \(i=0,\ldots,k-1\). Commutativity makes the intermediate terms telescope, yielding
\[
 \Lambda_B((M_{3^k})_*\nu)\le\Lambda_B((M_{2^k})_*\nu)=\Lambda_B(\nu).
\]
Iterate this inequality. The equidistribution input applies to \(p=2^k\) and \(3^k\), so the same Markov measures now give (5) with the opposite inequality. Either direction is sufficient below.

The stationary width-\((2r+1)\) block probabilities are precisely the normalized nonnegative circulations on the de Bruijn graph. Its vertices are length-\(2r\) digit words; an edge is a length-\((2r+1)\) word, joining its overlapping prefix and suffix. A strictly positive circulation gives the full-support Markov measure just used. The uniform circulation is strictly positive and hence lies in the relative interior of their affine space. The linear functional \(\pi\mapsto\sum_w B(w)\pi(w)\) has a maximum or minimum there by (5), and must therefore be constant on that affine space.

Put \(\beta=p^{-(2r+1)}\sum_w B(w)\). The circulation conclusion means that \(B-\beta\) has sum zero around every directed cycle. To see this for any particular cycle, perturb the uniform circulation a sufficiently small amount toward or away from its normalized cycle flow. Choose a reference vertex and define \(h\) by summing \(B-\beta\) along a path from the reference. The value is independent of the path: close two candidate paths by the same return path, and use the zero cycle sums. The graph is strongly connected. With a choice of orientation we obtain the exact identity
\[
                   B(w)=\beta+h(w^+)-h(w^-).                         \tag{7}
\]
For radius zero the graph has one vertex, and (7) just says that every interior digit coefficient is the same. This is finite graph cohomology, rather than a measurable approximation.

## 3. Exact reduction to one leading-digit boundary term

For \(D\ge1\), (7) and discrete summation by parts give
\[
 F(n)=\beta S_D(L)+L^D H(u(n))+G(n),\qquad
 S_D(L)=\sum_{i=0}^{L-1}i^D,\qquad
 u(n)=\log_p n-(L-1).                                                 \tag{8}
\]
Here \(H\) is a bounded step function on \([0,1)\), determined by finitely many leading digits, and \(G\) is again of form (1), with degree at most \(D-1\), possibly with a larger fixed radius and a different bounded correction. We verify the exact closure because boundary terms of order \(L^D\) cannot simply be discarded.

On an interior interval of positions \(a\le i\le b\), the relevant identity is
\[
 \sum_{i=a}^b i^D(h_{i+1}-h_i)
 =b^D h_{b+1}-a^D h_a
       -\sum_{i=a+1}^b\bigl(i^D-(i-1)^D\bigr)h_i.                   \tag{9}
\]
The difference polynomial in the sum has degree at most \(D-1\). Each \(h_i\) reads a shorter fixed local word, so that sum is a permitted lower-degree score. At the bottom, all omitted positions have bounded index and contribute a bounded function. At the top, every position is \(i=L-c\) for one of finitely many fixed \(c\). Expand
\((L-c)^D=L^D+Q_c(L)\), where \(Q_c\) has degree at most \(D-1\). The coefficients of \(L^D\), including the original upper sentinel windows and the upper endpoint in (9), combine to give \(H\). The other terms are polynomials of degree at most \(D-1\) in \(L\), with coefficients reading a fixed leading tuple.

These latter terms belong to the claimed lower-degree class exactly. Enlarge the radius so the topmost genuine window sees the entire required leading tuple and the first upper sentinel. That window uniquely identifies the top position \(i=L-1\). Put its desired polynomial coefficient \(Q_c(i+1)\) there and put zero at the other positions. Small numerals form a finite exceptional set and may be absorbed in the bounded correction. This proves (8). The canonical digit convention makes \(H\) right-continuous on its finite partition into half-open leading-digit intervals, expressed in the logarithmic coordinate \(u\).

In particular \(F(n)=\beta L^{D+1}/(D+1)+O(L^D)\), uniformly in all numerals of length \(L\). Lower-boundedness would force \(\beta\ge0\), but the next section obtains that sign directly from actual even edges and therefore does not need that assumption.

## 4. An actual odd-edge average removes that boundary term

We need one elementary counting fact about the lower-degree score \(G\) in (8). Fix a nonempty real interval \(I\subset(1,p)\) whose closure stays away from the finitely many relevant leading-digit boundaries, both before and after multiplication by \(3/2\), and from changes of length. Choose \(n\) uniformly among the odd integers in \(p^{L-1}I\), and set \(y=T(n)=(3n+1)/2\). Then
\[
                         \mathbb E[G(y)-G(n)]=O_I(L^{D-1}).             \tag{11}
\]

To prove this, write \(n=2m+1\) and \(y=3m+2\). The range of \(m\) is an interval of \(\asymp_I p^L\) consecutive integers. Away from the lowest finitely many positions, the mean of each interior window weight under either progression is its uniform digit mean, with error
\(O_{I,r}(p^{i+r+1-L})\). Indeed a window at positions \(i-r,\ldots,i+r\) is read modulo \(p^{i+r+1}\). If the progression stride two or three is coprime to \(p\), it permutes the residues. If it is not, its fixed common divisor divides \(p^{i-r}\) once \(i-r\ge1\); every block specifying the window then contains the same number of accessible residues. In either case progression counting gives the stated error.

The two means therefore cancel at all their common interior positions. Multiplication by \(3/2\) changes the length by at most one. The finitely many unmatched or top boundary positions cost \(O(L^{D-1})\). At the low boundary the positions are bounded. Summing the interior errors after multiplying by \(i^j\), \(j\le D-1\), gives \(O_I(L^{D-1})\) by a geometric series. The bounded correction costs \(O(1)\). This proves (11) for any integer radix, including radices divisible by two or three. The identical argument works for the actual even pair \(n=2m\), \(y=m\), using progression strides two and one and choosing the interval away from the corresponding top boundaries.

Apply that even version to (8). Put \(v_2=\log_p2\in(0,1]\). Average the even inequality in (2), divide by \(L^D\), and shrink the fixed mantissa interval around a point outside the finite boundary set. The result is
\[
       \beta\lfloor u-v_2\rfloor+H(\{u-v_2\})-H(u)\le0
                  \quad\text{for almost every }u\in[0,1).
\]
Integration gives \(-\beta v_2\le0\). Hence, with no lower-bound hypothesis,
\[
                               \beta\ge0.                              \tag{10}
\]

Put \(v=\log_p(3/2)\), so \(0<v<1\). For almost every \(u\), choose a sufficiently small interval \(I\) around the real mantissa \(p^u\) as above. Its source and target values of \(H\), and its length change \(m=\lfloor u+v\rfloor\), are constant for all large \(L\). The added \(1/2\) in the actual odd edge is harmless because the closed interval has a fixed positive distance from the excluded boundaries. We have
\[
 S_D(L+m)-S_D(L)=mL^D+O(L^{D-1}).
\]
Use (8), average the odd inequality in (2), apply (11), and divide by \(L^D\). Letting \(L\to\infty\) yields
\[
       \beta\lfloor u+v\rfloor+H(\{u+v\})-H(u)\le0
                  \quad\text{for almost every }u\in[0,1).             \tag{12}
\]
Integrate with respect to uniform \(u\). The two \(H\) integrals cancel under rotation, and \(\int_0^1\lfloor u+v\rfloor\,du=v\). Thus \(\beta v\le0\). Together with (10),
\[
                               \beta=0.                                \tag{13}
\]
Equation (12) now says \(H(u+v)\le H(u)\) almost everywhere. The integral is unchanged, so equality holds almost everywhere. The rotation by \(v\) is irrational: a rational equation \(v=s/t>0\) would give the impossible integer identity \(p^s=(3/2)^t\). Ergodicity of irrational rotation makes \(H\) constant almost everywhere. Since \(H\) is a finite step function with its canonical half-open convention, it is constant on every leading-digit cell, including the assigned endpoints. Write this constant as \(h_0\).

Finally
\[
                  L^D=\sum_{i=0}^{L-1}\bigl((i+1)^D-i^D\bigr).         \tag{14}
\]
The polynomial inside the sum has degree at most \(D-1\). Hence \(h_0L^D\) can be absorbed into the lower-degree local coefficients in (8). **The very same function \(F\) has a representation of degree at most \(D-1\)**, with a fixed enlarged radius and a bounded correction. Its inequalities (2) are unchanged. All normalized inequalities used in the reduction remain valid if the odd upper bound is any finite real number; its negative sign is needed only in the final obstruction.

## 5. End of the induction on polynomial degree

Repeat Sections 1–4 finitely many times. At degree zero, Section 2 still applies. The exact coboundary (7) now telescopes without position weights, and there are only finitely many boundary windows. We obtain
\[
                         F(n)=\gamma L(n)+O(1)                          \tag{15}
\]
uniformly for all positive integers. This proves the structural rigidity statement, even without a lower bound on \(F\). If \(F\) is lower-bounded, it also gives \(\gamma\ge0\).

For each \(J\ge1\), the actual positive orbit beginning at \(2^J-1\) has \(J\) consecutive odd departures,
\[
       T^j(2^J-1)=3^j2^{J-j}-1\quad(0\le j\le J),\qquad
       T^J(2^J-1)=3^J-1.                                                \tag{16}
\]
All these sources exceed \(X_0\) for large \(J\). Summing the odd inequality gives
\[
                   F(3^J-1)-F(2^J-1)\le-\epsilon J.                  \tag{17}
\]
But (15) gives
\[
 F(3^J-1)-F(2^J-1)
       =\gamma J\log_p(3/2)+O(1)\ge-O(1),                             \tag{18}
\]
which contradicts (17) when \(\gamma\ge0\). This proves the lower-bounded impossibility. The constructed paths can converge after the displayed segment; they are witnesses against a ranking inequality, not divergent orbits.

For the classification without lower-boundedness, (17) and (15) instead imply
\(\gamma\log_p(3/2)\le-\epsilon\). Fix any integer \(z>X_0\). The true even path from \(2^Jz\) down to \(z\) remains above the floor throughout its \(J\) departures. Summing the even inequality and using (15) gives
\[
 -\gamma J\log_p2+O(1)=F(z)-F(2^Jz)\le aJ.
\]
Thus \(-\gamma\log_p2\le a\). These two bounds require (2a). Conversely, if (2a) holds, choose
\[
        \frac{\epsilon}{\log(3/2)}\le c\le\frac a{\log2}
\]
and put \(F(n)=-c\log n\). On an even step its increase is exactly \(c\log2\le a\). On an odd step its change is
\(-c\log((3+1/n)/2)\le-c\log(3/2)\le-\epsilon\). This is a degree-zero member of (1), since \(-c\log n=-c(\log p)L(n)+b(n)\) with bounded \(b\). The construction works above every floor and includes equality in (2a). This proves the sharp classification. \(\square\)

## Verification boundary and provenance

The proof is a written mathematical argument. Its non-elementary measure-equidistribution input is the explicitly identified classical theorem; the argument does not claim to formalize that theorem in Lean. The weighted digit limit, carry control, exact boundary reduction, progression average, and degree induction are supplied here rather than inferred from finite experiments.

[DigitRankingKernel.lean](DigitRankingKernel.lean) formalizes the finite algebra and the final actual-orbit obstruction. Its ten public endpoints retain both summation-by-parts boundaries, expand monomial first differences, express length powers as sums of lower-degree weights, prove the native identity $T^J(2^Jq-1)=3^Jq-1$ for every positive $q$, sum a proposed odd loss along that run above any floor, and rule out a bounded perturbation of any monotone height with a uniform negative odd drift. The kernel does not assume the analytic reduction as a custom axiom. Its strict build and complete declaration audit are recorded in the checkpoint replay. The extension to genuine infinite digit memory with a quantitative continuity modulus is proved separately in [the infinite-context manuscript](../broad/INFINITE_DIGIT_CONTEXT_RANKING.md).

The root lane developed the polynomial reduction and odd-edge mantissa argument. The broad-machinery lane independently supplied the direct invariant-expectation proof of Lemma 1, checked the finite-radius closure, and identified the all-radix extension and the stronger range of parity prices. The escape lane independently audited that proof and identified the even-edge average which removes the lower-bound assumption from the reduction and gives the sharp price classification. Formal finite algebra and actual-orbit identities are recorded separately, with their own build and axiom receipts. Any final review receipt must distinguish those Lean kernels from the complete analytic theorem.

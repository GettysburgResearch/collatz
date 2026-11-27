# Many incoming phases at one fixed ordinary source

**Written theorem.** For each fixed positive odd integer \(q\) coprime to 3, consider genuine backward ordinary trajectories \(y_0=q,\ U(y_j)=y_{j-1}\). Among trajectories with gaps in \(\{3,\ldots,14\}\), the incoming amplitudes
\[
       I=\lim_{j\to\infty} 3^j y_j\,2^{-E_j},
       \qquad E_j=\sum_{i=1}^j v_2(3y_i+1),
\]
form a set of Hausdorff dimension at least \(1/4\). All the rays built here consist of positive odd integers and stay in the component of the single specified \(q\). The amplitudes lie in \([q-1/5,q)\). Their logarithms modulo \(\log 2\) are distinct whenever the amplitudes are distinct.

This addresses a possible inference from the summable two-sided component budget in [ARITHMETIC_COST.md](ARITHMETIC_COST.md). Absolute convergence of log corrections along every two-sided ordinary history allows real incoming constants, but need not make the incoming constant at the root independent of the chosen past. The theorem applies inside the component of 1 unconditionally and to any potential nonperiodic component at any odd state after the first odd step.

## Constructing actual histories

At \(y\) with \(3\nmid y\) take every exponent \(e\in\{3,\ldots,14\}\) for which \(2^e y\bmod9\in\{4,7\}\). The child \(y'=(2^e y-1)/3\) is a positive odd integer coprime to three and \(U(y')=y\) with exact exponent \(e\). The powers of two modulo nine cycle through all six units. Thus each consecutive block of six exponents contains exactly two choices: they have the required parity, and one of the three exponents of that parity is excluded because the child would be a multiple of three. In each of the two blocks the first and second legal exponents are at most \(6,8\) and \(12,14\), respectively. Every child exceeds \(y\).

Let \(E_0=0\). The one-step identity gives the telescope
\[
   3^j y_j\,2^{-E_j}
       =q-\sum_{h=1}^j 3^{h-1}2^{-E_h}.
\]
The total offset \(D=q-I\) lies in \((0,1/5]\) because each gap is at least three. After the first choice at a node, the offset from that node has the form \(2^{-e}+\rho_e D'\), \(\rho_e=3/2^e\), where \(0\le D'\le1/5\) is the offset on the child subtree. Its full range is inside \([2^{-e},(8/5)2^{-e}]\). Any other legal exponent at this node differs by at least two. The ranges of siblings are disjoint with gap at least \(g=(3/5)2^{-14}>0\). Distinct infinite histories therefore give different amplitudes. The full interval of possible positive amplitudes has ratio of endpoints at most \(5/4<2\), even at \(q=1\).

## Dimension estimate

Inductively split mass at a node among its legal choices in proportion to \(\rho_e^{1/4}\). The sum of these weights is greater than one at every node:
\[
  3^{1/4}(2^{-6/4}+2^{-8/4}+2^{-12/4}+2^{-14/4})>1.
\]
For an elementary check, \(3^{1/4}>13/10\), \(2^{-6/4}>7/20\), \(2^{-8/4}=1/4\), \(2^{-12/4}=1/8\), and \(2^{-14/4}>7/80\). Their product bound is \( (13/10)(13/16)>1\). Thus a cylinder with cumulative similarity factor \(r=\prod\rho_e\) has mass at most \(r^{1/4}\). The recursively specified cylinder probabilities give a probability measure on the infinite branch space, hence one on the compact set of amplitudes by the continuous limit formula.

For \(0<h<1\), stop each branch at the first cylinder with factor \(r<h\); this occurs because all factors are at most \(3/8\). Distinct stopping cylinders are incomparable. Their longest common prefix has factor at least \(h\); the sibling separation at that prefix gives distance at least \(gh\) between their amplitude sets. An interval of length \(h\) meets at most \(1+1/g\) stopping cylinders and hence has mass at most \((1+1/g)h^{1/4}\). Summing over any cover by sufficiently short intervals proves that the Hausdorff \(1/4\)-measure is positive. Translation and reflection from offsets to amplitudes preserve the estimate. No statistical hypothesis about ordinary forward Collatz orbits is used.

The angular width is bounded on an absolute amplitude scale, so its relative size at a large \(q\) is of order at most \(1/q\). This is compatible with the larger allowed component-wide upper bound of order \(M^{\theta-1}/\sqrt{\log(2M)}\) for a component of minimum \(M\le q\). The construction establishes history-dependence at a fixed root and supplies no contradiction for forward escape. The dimension estimate is a written proof.

# Exact corrected-height defects on fixed integer towers

**PROPOSED.** Use \(P,F,b,C\) from the [ordinary Hardy equation](ORDINARY_HARDY.md), with zero \(b\) off the single escaping component. Choose a reference odd ray in \(C\). Give every vertex its odd-step grade \(g\): an odd step increases it by one, and an even step preserves it. A path into the reference ray defines this integer uniquely because the ray is injective. On the same component
\[
 \frac{P(y)}{P(x)}=3^{g(y)-g(x)}2^j,\qquad j\in\mathbb Z.              \tag{1}
\]
For \(g(y)\to+\infty\), \(F(y)\to1\) uniformly. For each fixed \(M\), the finitely many odd component states at most \(M\) have a greatest grade when the list is nonempty. Above that grade every odd state on a future path exceeds \(M\). Apply the uniform reciprocal tail in the Hardy note and let \(M\to\infty\). This includes the nonunit odd leaves and all the even multiples on the full shortcut graph. The corresponding fixed-grade statement was established for ternary units in the [graded correction theorem](../../astra-six-hour-20261127/escape/GRADED_CORRECTION_SETS.md).

For every fixed positive odd \(p\in C\),
\[
          \#\{j\ge0:b(3^j p)=b(p)\}<\infty .                           \tag{2}
\]
A matching value is positive, puts \(3^j p\) in \(C\), and implies \(P(3^jp)=3^jP(p)\). Multiplicative independence in (1) gives \(g(3^jp)=g(p)+j\). Infinitely many such \(j\) would give \(F(p)=1\), whereas its factor at \(p\) is strictly below one.

In particular some fixed odd \(q=3^j p\) has \(\Delta=|b(3q)-b(q)|>0\). For every sufficiently large \(k\), at least one of the adjacent defects at \(2^kq-1,\ 3\cdot2^{k-1}q-1\) has size at least \(\Delta/3\). Indeed \(T(2^kq-1)=3\cdot2^{k-1}q-1\), and the normalized values along this odd edge differ by \(O(2^{-k}/q)\), also off \(C\). The two right neighbours have their fixed values \(b(q)\) and \(b(3q)\). This part uses only the actual path and the packing estimate.

## Counted fusion on the geometric family and the dyadic exception

On a counted shortcut fusion of two physical integers their membership in \(C\) agrees, and their \(P\)'s agree exactly if supported. In particular a counted fusion of \(3u,3u+1\) for an odd positive \(u\) gives \(b(3u)=b(u)\): \(P(3u+1)=3P(u)\) in the supported case. Thus the counted-fusion theorem gives exact tripling invariance for a density-one set of \(u\), also on the power family \(u=3^j p\) for density-one exponents \(j\). For the latter, \(3^{2j}\) is equidistributed in \(1+8\mathbb Z_2\), since \(v_2(9^{2^k}-1)=k+3\); the two exponent parities give two clopen cosets. The complement of the open counted-fusion cylinders has Haar measure zero. The intersection of these success cylinders with each coset can be approximated from within by finite unions of cylinders. Translation by a fixed offset preserves this property.

For the same fixed \(p\in C\), the neighbouring ordinary integers
\[
                   2^k p-1,\quad 2^k p                                \tag{3}
\]
fail to count-fuse, at **any** future common time, for a density-one set of exponents \(k\). They have different ordinary coefficients \(m\) for these \(k\). To see this, \(3^k p-1,3^kp\) count-fuse for density-one \(k\) by the preceding argument. Follow the left member in (3) for its first \(k\) odd shortcut departures to \(3^k p-1\); the right member strips \(k\) twos to \(p\). If their coefficients agreed, the left one would be supported, with \(P(2^kp-1)=2^kP(p)\). Thus \(P(3^kp-1)=3^kP(p)\), and its counted fusion gives \(P(3^kp)=3^kP(p)\). By (2) this happens only finitely often. Unequal coefficients preclude counted fusion. This conclusion concerns exact coefficient inequality. The fixed-size conclusion uses the two neighbouring towers above and need not occur at (3) alone. [Weaver, counted fusion and exact cylinders](https://rstation.ai/problems/collatz/papers/124/v1).

The sharp unweighted adjacent counted nonfusion probability at finite shortcut time \(t\) is asymptotic to a positive constant times \(t^{-1/2}\) for a Haar binary source, according to Leen's Theorem A. A complete block modulo \(2^k\) reproduces its \(k\)-tick survival proportion. Thus the raw finite-deadline bound cannot yield a summable rate over the physical dyadic scales \(k\). Unequal corrected coefficients can form a smaller set than this finite-deadline exception. Proving sufficiently fast decay of their actual oscillation, or amplifying a tower defect into a contradictory population, remains open. [Leen, *Exact rates in Collatz synchronization*](https://doi.org/10.5281/zenodo.23268751) · [Weaver, stated rate and exact reference](https://rstation.ai/problems/collatz/papers/13/v1).

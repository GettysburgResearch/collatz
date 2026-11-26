# An arbitrary fixed contraction at the native entropy cost

**PROPOSED written theorem.** Let \(f\) be a binary invariant of the positive ordinary shortcut map. Fix \(0<q<1\). On every sufficiently large original octave \([X,2X)\), except for

\[
 O_q\!\left(\frac{X^{h_2(s)}}{\sqrt{\log X}}\right),
 \qquad s=\log_3 2,\quad
 h_2(s)=-s\log_2s-(1-s)\log_2(1-s),
\]

original integers, every actual tripling disagreement forces an ordinary witness \(y\le qX\), in each of the classes \(11\bmod32\) and \(17\bmod48\), with ordered labels

\[
 (f(y),f(3y))=(1-f(1),f(1)).
\]

The binary values in this display are read as zero and one. The conclusion uses the finite directed substitution in [BOUNDED_DIRECTED_ELEVEN.md](BOUNDED_DIRECTED_ELEVEN.md) and the pinned PR146 directed descent. The asymptotic exponent is about \(0.949956\). The exceptional inputs here are counted on the original octave; no claim concerns a fresh distribution at the selected witness.

## Proof on the original source grid

Put \(k=\lfloor\log_2X\rfloor\). For a parity word with \(p\) odd steps,

\[
 T^k(n)=3^p2^{-k}n+E,\qquad
 0\le E\le (3/2)^k-1.
\]

The length-\(k\) parity map is a permutation of residues modulo \(2^k\). At the next step its two lifts have opposite parities, since the high coefficient is odd. Multiplication by three also permutes this grid. Covering the original octave by a bounded number of whole binary periods bounds the upper-tail counts for both \(x\) and \(3x\), using a union bound on the same original variable.

There is a fixed constant \(K_0\) such that any positive ordinary \(n\) with \(f(n)\ne f(1)\) gives a witness in either target residue of height at most \(K_0n\). Indeed the PR146 26-leaf certificate descends by a factor at most \(9/10\) in batches of at most 61 ordinary or additional edges. Intermediate values in a batch have a uniformly bounded ratio to its starting value. Iterating until 1, the first change to its color occurs at a forward tripling on an odd multiple of three. The ordinary two-successor exchange transfers that ordered change to \(1\bmod16\), and the new finite bank transfers it to the requested residue. This argument requires no uniform bound on the number of batches.

Choose a fixed integer \(C_q\) so that \(6K_0 3^{-C_q}<q/2\). Whenever both odd counts satisfy \(p\le sk-C_q\), the two actual endpoints satisfy

\[
 T^k(x),T^k(3x)\le 6X3^{-C_q}+O(X^{\log_2(3/2)}).
\]

For a genuine defect these endpoints still have different colors. One differs from \(f(1)\); applying the preceding directed path and localization gives the claimed height at most \(qX\) for all sufficiently large \(X\).

The first excluded integer odd count is \(sk+O_q(1)\). Stirling's formula bounds its binomial coefficient by \(O_q(2^{kh_2(s)}/\sqrt{k})\). Since \(s>1/2\), successive upper-tail terms have ratio bounded strictly below one for large \(k\). Summing that geometric tail and the two original-ray counts proves the exceptional estimate.

## Relation to existing stopping estimates

The [resident native no-descent theorem](../../integrated/exceptional-mass/README.md) already has the explicit \(19/20\) bound and this entropy threshold for its one-ray problem. The new conclusion is the actual directed comparison witness in a prescribed residue, with either an arbitrary fixed contraction as above or the sublinear powers in the main note. The parity calculation is credited to the existing native-grid method. The [independent reconstruction](../../../reports/ayh-resource-reset-20261124/directed-return/STRICT_ORDINARY_RETURN_REVIEW.md) also checks the exact integer controls for both sublinear parameter choices.

The number \(h_2(s)\) is greater than \(0.84\). A selected smaller witness can belong to the next exceptional set, and many originals can select the same witness. Neither this theorem nor its repeated application at successive eligible inputs provides universal descent or a summable pullback bound. Those are the remaining requirements for this route.

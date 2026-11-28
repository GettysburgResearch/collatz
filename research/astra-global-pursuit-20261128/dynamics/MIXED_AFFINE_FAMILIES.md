# Sparse affine families and simultaneous radix intervals

The elementary compression proof in [GROWING_BLOCKS.md](GROWING_BLOCKS.md) allows arbitrary centers, repeated coefficient grades, and a spread of source sizes. This gives a genuine joint-future assertion for every member of exponentially many complete intervals about the same ordinary anchor.

## Sparse-family estimate

Let the arms be \(3^{Q_i}x+c_i\) for \(1\le i\le M\), with nonnegative integer \(Q_i\), integer \(c_i\), and Haar \(x\in\mathbb Z_2\). Give arm \(i\) initial effective grade \(Q_i\). Let \(T\) denote the first common shortcut date with all endpoints and effective grades equal. Put \(K=\max Q_i-\min Q_i\). For any real center \(\beta\) and fixed \(0<\alpha<1\), write
\[
 V=\sum_i(1+|c_i-3^{Q_i}\beta|^\alpha),\qquad
 L=1+\log(2+V),\qquad A=1+\log(2M).
\]
Then
\[
              \Pr(T>t)\ll_\alpha
      \frac{1+K+\min\{L,\sqrt{LA}\}}{\sqrt{1+t}}.       \tag{1}
\]
The constants are uniform in the family and the center. Real centering allows arbitrarily distant translates of a tight collection at a single grade, or nearby normalized centers across grades.

**Proof.** On the prefix \(x=r+2^jz\) each retained label is \((q,c)\) with endpoint \(3^qz+c\), where \(q=Q_i+q_j(3^{Q_i}x+c_i)\) on that cylinder. Put
\[
                 R=c-3^q(r+\beta)/2^j.
\]
Its exact digit update remains \(R'=(3^bR+b)/2\). Subadditivity for \(|\cdot|^\alpha\) gives the same drift
\[
 \mathbb E(|R'|^\alpha\mid r)\le\chi|R|^\alpha+2^{-1-\alpha},
 \quad \chi=(2^{-\alpha}+(3/2)^\alpha)/2<1.
\]
At each grade retained residuals belong to a unit-spaced translate of the integers. If \(B_j\) is the grade range (maximum minus minimum over retained labels), the count of labels with \(|R|<H\) is at most \((2H+1)(1+B_j)\). Thus the corresponding total weight \(W_j=\sum(1+|R|^\alpha)\) satisfies
\[
 \mathbb EW_{j+1}\le\rho\mathbb EW_j+C_\alpha\mathbb E(1+B_j),
 \qquad \rho<1.
\]
Here \(H\) is a sufficiently large constant depending only on \(\alpha\). Every original arm is Haar because its slope is odd, and its shortcut parity string of length \(j\) is uniform by the parity-cylinder bijection. Thus every individual added grade is binomial \((j,1/2)\). A union bound over all original arms, followed by integration of Hoeffding's tail, gives
\[
 \mathbb E B_j\le K+C\min\{j,\sqrt{j\log(2M)}\}.
\]
The same bound would apply without any fusion between arms. Duplicating or deleting identical labels leaves the grade extrema unchanged.

Take \(m=\lceil C_\alpha L\rceil\) so \(\rho^mV\le1\). The inhomogeneous term is nondecreasing in \(j\), and summing the geometric weights gives \(\mathbb EW_m\ll_\alpha 1+K+\min\{L,\sqrt{LA}\}\). Sort the remaining arms by grade. The grade gaps telescope to \(B_m\). For neighboring arms separated by \(k\) grades, the normalized offset is \(3^{-k}R_{i+1}-R_i\), whose \(\alpha\)-power is bounded by \(|R_i|^\alpha+|R_{i+1}|^\alpha\). The scalar absorption bound (2) of [GROWING_BLOCKS.md](GROWING_BLOCKS.md) gives a conditional tail bounded by \(C_\alpha(B_m+2W_m)/\sqrt{1+s}\) at date \(m+s\). Take expectations to obtain (1) for \(t\ge2m\). For earlier dates the numerator in (1) dominates \(\sqrt{L}\), so the trivial bound suffices. This is one argument for each fixed center; it also allows an externally chosen minimizing center.

In particular, if \(U=\max_i|c_i-3^{Q_i}\beta|\), replace \(L\) in (1) by \(C(1+\log(2M)+\log(2+U))\). With fixed \(M\), bounded \(K\), and large spread, the time scale from (1) is \(O(\log(2+U))\). With \(D\) consecutive offsets at grade zero the time scale is \(O((\log(2+D))^2)\).

## Simultaneous ordinary intervals

For each \(h\ge1\), consider *all* ordinary starts
\[
          2^a3^bn+r,\qquad 0\le a,b\le h,\qquad
          0\le r<2^a3^b.
\]
For every interval of \(X\) consecutive positive anchors \(n\), all but a fraction
\[
        C(1+h)/\sqrt{t+1}+2^t/X                               \tag{2}
\]
have the following property: all these starts, including \(n\) itself, reach one and the same ordinary integer within at most \(h+t\) shortcut steps of each start. The date of arrival is allowed to differ across the original starts. For \(t=\lfloor\delta\log_2 X\rfloor\), \(0<\delta<1\), the conclusion applies simultaneously at density one to every dyadic, ternary, and mixed-radix descendant interval of depths \(a,b\le h=o(\sqrt{\log X})\).

Indeed the first \(a\) parities of a start are determined by \(r\). After these \(a\) steps its endpoint is
\[
              3^{b+k}n+T^a(r),\quad k=q_a(r)\le a .
\]
This follows directly from the parity-cylinder affine identity for the starting difference \(2^a3^bn\); \(r\) is allowed to exceed \(2^a\). These resulting affine arms have \(Q_i\le2h\), \(M\le(\sum_{a=0}^h2^a)(\sum_{b=0}^h3^b)\), and \(T^a(r)+1\le(3/2)^a(r+1)\le(3/2)^h6^h\) by both shortcut branches. Use center zero in (1). The agreement event is a union of length-\(t\) prefix cylinders for \(n\); any incomplete period accounts for the last term of (2). The original physical times may be \(a+t\) for different \(a\), while the endpoints at the end of their common affine phase are actually equal.

This conclusion has arbitrary simultaneous selection within all the displayed intervals. It still allows the finite-defect visit-to-5 coloring on fixed fractional native horizons: uniformly over this family of starts, the first \(h+t\) steps can only reach a value at least \(X/2^{h+t}\) for anchors in \([X,2X]\). The power of \(X\) in this lower bound is positive for the stated depth range and fixed \(\delta<1\).

[check_mixed_families.py](check_mixed_families.py) produced identical results in normal and optimized Python. Its exact controls include 4,590 signed centered updates, 1,781 normalized cancellations, 72 binomial marginals checked against full binary periods, and 137,592 independently computed ordinary mixed-radix lifts.

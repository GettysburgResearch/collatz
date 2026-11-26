# Shared prime-adic precision on an ordinary Collatz trajectory

**Status.** Proposed written deductions using cited Diophantine approximation theorems. The finite identities identified in the last section have companion Lean proofs. Each path below starts at an ordinary positive integer and follows its actual forward branches.

A contemporaneous PR193 packet proves a stronger general integer estimate using the prime-to-six part of the separation. Its result implies the fixed-form bound used here for distinct displacements; equal displacements satisfy the elementary separate divisibility estimate. The proof below is an independent direct derivation. The delayed, oriented physical endpoints and the local denominator windows are applications. [PR193 moving-center estimate, 5cf2ea9d](https://github.com/GettysburgResearch/collatz/blob/5cf2ea9dda23470b600a72a2fab20d929f668e5d/research/astra-unconventional-20261126/arithmetic/MOVING_CENTERS.md)

## An all-clock estimate with directed endpoints

Use the odd map \(A(q)=(3q+1)/2^{v_2(3q+1)}\). From an odd integer \(u=q_0>0\), put \(q_{i+1}=A(q_i)\), \(v=q_m\), and \(s=\sum_{i<m}v_2(3q_i+1)\). Write the physical affine identity as
\[
2^s v=3^m u+C.
\]
Choose fixed rational labels \(a/d,b/d\), with \(d>0\) and integers \(a,b\). Define the nonzero displacements \(A=du-a\), \(B=dv-b\) and put
\[
U=2^s B,\quad V=3^m A,\quad E=U-V=dC+3^ma-2^sb,\quad H=\max(|U|,|V|).
\]
For a nonzero integer \(t\), write \([t]_p=p^{v_p(t)}\). For every \(\varepsilon>0\) the two endpoints share the bound
\[
 [A]_3[B]_2
 \le K_\varepsilon H^\varepsilon(1+|E|)
 \min\bigl(|A|/2^s,|B|/3^m\bigr).                 \tag{1}
\]
The constant in (1) depends only on \(\varepsilon\). In particular, for every \(\delta>0\),
\[
 \log[A]_3+\log[B]_2
 \le(1+\delta)\log(u+1)+(\log(3/2)+\delta)m+
 O_{\delta,a,b,d}(1).                                 \tag{2}
\]
These estimates charge ternary precision at the earlier odd integer and binary precision at the later odd integer. The intervening word is unrestricted.

**A two-variable Diophantine estimate.** For disjoint finite sets of primes \(P,Q\), let \([t]_P=\prod_{p\in P}[t]_p\). For all ordinary nonzero integers \(U,V\),
\[
 [U]_P[V]_Q\le K_{\varepsilon,P,Q}\min(|U|,|V|)(1+|U-V|)H^\varepsilon.
                                                               \tag{3}
\]
To prove this, first take the archimedean forms \(X,X-Y\) and the coordinate forms \(X,Y\) at each prime in \(S=P\cup Q\). Their product of absolute values at \((U,V)\) is
\[
 \frac{|U||U-V|}{[U]_S[V]_S}.
\]
On dividing the vector by its positive gcd \(g\), the product is divided by \((g/[g]_S)^2\ge1\). Thus if the displayed product is less than \(H^{-\varepsilon}\), the primitive vector satisfies the two-variable \(S\)-adic Subspace Theorem with the same exponent. Its exceptions lie on finitely many fixed rational lines. Interchange \(X,Y\) at infinity and repeat to handle the smaller ordinary coordinate. Off the union of both exceptional families, the result follows from \([U]_P[V]_Q\le[U]_S[V]_S\). On an exceptional line write \((U,V)=w(c,e)\), with a fixed primitive integer pair and \(cew\ne0\). Disjointness gives \([w]_P[w]_Q\le |w|\), whence \([U]_P[V]_Q\le[c]_P[e]_Q|w|\). This proves (3), including \(U=V\) and both choices of signs. The constants from this argument are ineffective. The fixed-place theorem is Schlickewei's \(p\)-adic Subspace Theorem, as stated by Evertse in Theorem 1.1 and illustrated with two coordinates immediately afterwards. [Evertse, May 2011, pp. 1–2](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

Apply (3) with \(P=\{2\},Q=\{3\}\). Since \([U]_2=2^s[B]_2\) and \([V]_3=3^m[A]_3\), division by \(2^s3^m\) proves (1). Each odd step has real slope at most \(3/2\) and intercept at most \(1/2\), so \(C/2^s\le(3/2)^m-1\). Also
\[
 2^s v=u\prod_{i<m}(3+1/q_i)\le4^m u.
\]
It follows that \(H\le c4^m(u+1)\) and \((1+|E|)/2^s\le c(3/2)^m\), for a label-dependent constant \(c\). Use the first argument of the minimum and choose \(\varepsilon\) so that \(\varepsilon\le\delta\) and \(\varepsilon\log4\le\delta\). This proves (2).

For example, a unit odd step satisfies \(q_{i+1}+1=3(q_i+1)/2\). If \(k\) consecutive unit steps end at \(u\) and \(h\) consecutive unit steps begin at \(v\), the left side of (2) for the two labels \(-1\) is at least \(k\log3+(h+1)\log2\). This conclusion uses both ends of the same physical segment. Its leading-order consequence for marked unit runs also follows by starting the longer prefix before the first run in the existing joint rise-group concentration result. [Paper 174, Theorem 5](https://rstation.ai/problems/collatz/papers/174) With \(m=0\), \(u=2^h3^k-1\) attains \([u+1]_3[u+1]_2=u+1\), which fixes the leading height coefficient in (2). Direction matters for long windows. From \(u=2^m-1\), the first \(m-1\) odd steps have gap one and the states \(3^j2^{m-j}-1\) for \(j<m\). Large binary precision at the source and ternary precision at the terminal can be created by these same steps.

## Independently chosen observation times and algebraic targets

Let \(T(n)=n/2\) for even \(n\), \(T(n)=(3n+1)/2\) for odd \(n\). Choose a finite set of primes \(P\). For each \(p\in P\) fix a finite nonempty set \(F_p\) of algebraic numbers in \(\mathbb Q_p\). For any sequence of ordinary positive integers \(x\to\infty\), and any shortcut window \(L=o(\log x)\), one has
\[
 \limsup_{x\to\infty}
 \frac1{\log x}\sum_{p\in P}
 \max_{0\le j\le L,\ \alpha\in F_p}
 \log^+ |T^j(x)-\alpha|_p^{-1}\le1.                  \tag{4}
\]
In particular, one may take \(x\) to be any sequence of large odd records of a common positive trajectory. Different primes may choose different times, in any order, after the entire window has been observed. A finite initial set of indices suffices to discard exact collisions, since \(T^jx\ge x/2^L\to\infty\).

For each prime and each index, choose a maximizing pair \(j_p,\alpha_p\). The actual prefix to \(j_p\) has the row
\[
  2^{j_p}T^{j_p}(x)=3^{r_p}x+C_p,\qquad 0\le r_p\le j_p,\quad0\le C_p\le3^{j_p}.
\]
The bound on \(C_p\) follows either by induction on the first branch or from the companion Lean theorem. Pull \(\alpha_p\) back to \(\xi_p=(2^{j_p}\alpha_p-C_p)/3^{r_p}\). The absolute logarithmic heights satisfy \(h(\xi_p)=O(L+1)=o(\log x)\). The change in positive logarithmic proximity under this pullback is \(O(L)\) at each prime, since the two differences differ by \(3^{r_p}/2^{j_p}\).

Use a fixed finite Galois field \(K/\mathbb Q\) containing representatives of the algebraic labels. For each \(p\) fix an embedding in \(\overline{\mathbb Q}_p\) and choose representatives for \(F_p\) in this embedding. The field embeds in the algebraic closure of \(\mathbb Q_p\), and the chosen local labels themselves lie in \(\mathbb Q_p\). At each place \(w|p\) use the appropriate conjugate of \(\xi_p\) so that its local value under the embedding defining \(w\) is the specified \(p\)-adic pullback. Take the moving hyperplanes \(X-\xi_wY\) for these places and the fixed hyperplane \(Y\). The sequence of points in the projective line is \([x:1]\). Every hyperplane has height \(o(\log x)\), and any fixed rational expression in their coefficient functions has the same height bound wherever defined. Thus on any infinite coherent subsequence \(x,1\) are linearly independent over the associated moving-coefficient field. Indeed a nonzero relation would express the ordinary integer \(x\), of height \(\log x\), by such an expression.

Apply the Ru–Vojta moving-target Subspace Theorem with its collection of singleton sets of hyperplanes, where the required general-position condition holds even if some chosen targets coincide. For the normalized sum over all infinite places use \(Y\) at each, contributing \(\log x\). For \(w|p\) use its own hyperplane. Since \(|x|_p\le1\), the local Weil function in max norm contributes at least \(\log^+|x-\xi_p|_p^{-1}\) before weighting. In fact its value is \(\log\max(1,|\xi_p|_p)-\log|x-\xi_p|_p\), a nonnegative number. The weights \([K_w:\mathbb Q_p]/[K:\mathbb Q]\) sum to one for every \(p\). The upper bound for all these contributions together is \((2+\varepsilon)\log x+O(1)\). Subtract the archimedean contribution, account for the \(O(L)\) pullback costs, and let \(\varepsilon\) decrease to zero. This proves (4). The same proof allows labels selected anew at every index in a fixed Galois field, with \(h(\alpha_p)=o(\log x)\) under the chosen identifications. An exact collision would contradict this height condition because \(T^jx\ge x/2^L\). [Vojta, *Nevanlinna Theory and Diophantine Approximation*, Theorem 7.7, pp. 553–554](https://library.slmath.org/books/Book37/files/vojta.pdf)

## Interface with an escaping positive integer

An infinite injective positive trajectory has arbitrarily large sources, so both the physical-window results apply at its large records. Compactness of ternary record limits alone places no lower bound of order \(\log x\) on the precision reached at a given height. A proof of a contradiction using (2) or (4) requires a lower bound on the combined local precision of records on the same orbit that exceeds the displayed budget. The current argument supplies the upper bounds independently of the existence of such records.

The finite arithmetic companion `RecordPrecision.lean` uses the original `NonunitExit.iterD 1` and `gradeD 1` shortcut functions. It establishes the forward affine row, the grade and sharp fixed-count carry inequalities, the signed shifted row, the integral parameter for an exact rational arc, and the two exact prime-divisibility statements for a rational closing, and the disjoint-powers estimate on one integer. The cited Diophantine estimates enter only the written deductions.

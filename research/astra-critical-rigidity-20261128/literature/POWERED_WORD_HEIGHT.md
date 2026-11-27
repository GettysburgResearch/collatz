# Positive source height for a few powered parity words

**Status: PROPOSED, with a classical external theorem.** The map is the shortcut Collatz map on positive ordinary integers. Time counts every shortcut step. All logarithms in the argument are base two. No density or independence assumption enters.

## The claim

Consider an actual parity prefix
\[
 w_1^{r_1}w_2^{r_2}\cdots w_k^{r_k}
\]
where the binary words are nonempty and the repetition counts are positive. Let \(D=\sum_j r_j|w_j|\) be its physical length and \(B=\sum_j|w_j|\) the total length of the supplied words before repetition. The words may depend on the source and the prefix. Write \(x_0\) for the starting integer, and \(x_i\) for the physical state after piece \(i\). Require that no piece starts at its own affine fixed point. At a positive integer, such equality is exactly a return to that same state after one actual copy of its word.

**Theorem.** For any sequence of such prefixes with \(D\to\infty\), bounded \(k\), and \(B=o(D)\),
\[
       \liminf \frac{\log x_0}{D}\ \ge\ 1.                         \tag{1}
\]
Equivalently, for fixed \(K\) and \(\eta>0\) there are \(\delta>0\) and \(D_0\) such that any prefix of length \(D\ge D_0\) with \(k\le K\) and \(\log x_0\le(1-\eta)D\) must have \(B\ge\delta D\), unless it includes the specified exact return. The proof supplies no effective values of \(\delta,D_0\).

For parity words with at most \(K\) constant runs, take each template to be the single bit 0 or 1. Their centers are respectively 0 and \(-1\), so the return exception is impossible for positive sources. If \(m(w)\) is the least *positive* realizer of a length-\(D\) word, then
\[
 \min_{|w|=D,\,\#\mathrm{runs}(w)\le K}\frac{\log m(w)}{D}\longrightarrow 1.
\]
Every parity prefix specifies one residue class modulo \(2^D\), hence \(m(w)\le 2^D\). The word \(1^D\) has least positive realizer \(2^D-1\), and \(0^D\) has least positive realizer \(2^D\). These also establish sharpness of the coefficient in (1). A long alternating word realized by 1 shows why powered templates need the actual-return exception.

## Algebra at the original source

For a template of length \(d\), weight \(s\), and positions \(t_1<\dots<t_s\) of its ones (zero based), its affine action is \((3^sx+C)/2^d\) with \(C=\sum_{j=1}^s2^{t_j}3^{s-j}\). Its center \(\alpha=C/(2^d-3^s)\) has odd denominator and height \(H(\alpha)\le 12^d\), where \(H(p/q)=\max(|p|,q)\) in lowest terms and \(H(0)=1\). Indeed \(C\le d\,2^d3^d\), \(d\le2^d\), and the denominator has absolute value at most \(3^d\).

Let \(d_i=r_i|w_i|\), \(q_i=r_i\#1(w_i)\), and put \(D_i=\sum_{j\le i}d_j, Q_i=\sum_{j\le i}q_j, U_i=2^{D_i}/3^{Q_i}\), with \(U_0=1\). Subtracting the center gives
\[
   U_i(x_i-\alpha_i)=U_{i-1}(x_{i-1}-\alpha_i).
\]
Adding these identities gives the original-source sum
\[
 L=x_0-\alpha_1+\sum_{i=1}^{k-1}(\alpha_i-\alpha_{i+1})U_i
      =U_k(x_k-\alpha_k),\qquad |L|_2\le2^{-D}.              \tag{2}
\]
The exponent covers the entire physical clock, including long even runs. The total ordinary cancellation is retained.

Write \(\alpha_i=p_i/h_i\) in lowest terms with \(h_i>0\) odd. The exact integer identity
\[
 2^{d_i}(h_ix_i-p_i)=3^{q_i}(h_ix_{i-1}-p_i)
\]
implies \(2^{d_i}\mid h_ix_{i-1}-p_i\). By the center exclusion the latter integer is nonzero, so
\[
 d_i\le \log(x_{i-1}+1)+\log H(\alpha_i).                     \tag{3}
\]
Also \(x_i+1\le 2^{d_i}(x_{i-1}+1)\), by the two single-step rules. Thus from any boundary, the remaining at most \(K\) pieces consume at most \(C_K(\log(x_i+1)+B)\) steps. This follows by iterating these two displayed bounds a fixed number of times.

## The height and the exceptional subspaces

Suppose (1) fails by a fixed margin \(\eta\in(0,1)\) along infinitely many prefixes. Pass to a fixed number of pieces. By (3) and the last bound, \(\log(x_0+1)\gg_K D\), since \(B=o(D)\). Every \(\log(x_i+1)/D\) is bounded by the elementary growth bound, so pass to a subsequence on which each has a limit. If an *internal* boundary has limit zero, truncate at the first such boundary. Its remaining suffix has length \(o(D)\) by (3), and truncation preserves a strict violating margin, for example \(\eta/2\). Renaming the truncated clock \(D\), all boundaries \(0\le i<k\) now have \(x_i\ge 2^{cD}\) for one positive \(c\) along the subsequence. There is no condition on the last state.

Each center or difference of centers has height \(2^{o(D)}\), using \(H(a-b)\le2H(a)H(b)\). At the retained interior boundaries the center identities imply
\[
 \frac{U_i x_i}{x_0}
 =\prod_{j=1}^{i}\frac{1-\alpha_j/x_{j-1}}{1-\alpha_j/x_j}=1+o(1)
 \quad(1\le i<k).
\]
Thus each non-source summand in the left side of (2) is \(o(x_0)\) in the real absolute value. Each has the form \(z=c\,2^a/3^b\), with \(0\le a,b\le D\), \(H(c)=2^{o(D)}\). This includes the constant term \(-\alpha_1\). Drop zero coordinates, passing to a fixed support. If none survive, (2) gives \(2^D\mid x_0\), contrary to the violating margin.

Use the following standard rational case of the \(p\)-adic Subspace Theorem. For \(S=\{\infty,2,3\}\), take \(n\) independent fixed rational linear forms at each place. Primitive integral vectors \(v\) with \(\prod_{p\in S}\prod_j|L_{j,p}(v)|_p\le \|v\|_\infty^{-\epsilon}\), for fixed \(\epsilon>0\), lie in finitely many proper rational subspaces. See [Schlickewei, *The quantitative subspace theorem for number fields*](https://www.numdam.org/item/CM_1992__82_3_245_0/) and [Evertse, Theorem 1.1, for this normalization](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf).

Initially use coordinates \((x_0,z_1,\ldots,z_{n-1})\) from (2). Take coordinate forms at infinity and three. At two replace only the source coordinate by \(x_0+\sum_j z_j=L\). The determinant is one. The same construction below permits arbitrary **fixed rational** coefficients of the remaining coordinates in this linear form, with the coefficient of \(x_0\) kept equal to one.

For every \(z=c2^a/3^b\) as above, \(\prod_{p\in S}|z|_p=\prod_{p\in S}|c|_p\le H(c)^2=2^{o(D)}\): powers of two and three cancel. Indeed for \(c=P/Q\) reduced the product is the ratio of the parts of \(|P|\) and \(Q\) coprime to 6. The product of forms on the rational vector is therefore at most \(x_0 2^{-D+o(D)}\), since \(|x_0|_3\le1\). Scale to a primitive integer vector. Multiplication by \(3^D\prod_j\mathrm{den}(c_j)\) clears all denominators. The 3-power leaves the three-place product invariant, and the denominators change it by at most \(2^{o(D)}\) since dimension is bounded. Division by the integral common gcd can only lower that product (the product of its three norms is its positive part coprime to 6). Every primitive coordinate has size at most \(2^{C D}\) for an absolute \(C\) on this subsequence: before division, use \(a,b\le D\), \(x_0\le2^D\), and the common clearing factor just displayed. Hence for large \(D\) the product is at most \(2^{-\eta D/3}\le\|v\|_\infty^{-\epsilon}\) for a fixed small \(\epsilon>0\).

An infinite subsequence belongs to one proper rational subspace. Choose a nonzero fixed linear relation vanishing there. A nonzero source coefficient is impossible, because division by \(x_0\) leaves all other coordinates tending to zero. Therefore solve for one non-source coordinate and substitute the result *into the two-adic sum*. Keep the other coordinates, delete the solved coordinate, and keep the original source coefficient one. Equation (2) and its exact right side still hold. The other coordinates retain their original small coefficient heights and real bounds. Reapply the same theorem to the new fixed forms on this subsequence. Every step lowers the dimension; dimension one would give \(|x_0|_2=|L|_2\le 2^{-D}\), contradicting positivity and \(x_0<2^D\). This proves (1).

## What would decide an orbit

Every divergent positive source and every simple first-crossing path meets the no-return condition. A general nontrivial cycle can replay a dictionary word, so apply the result only to a segment without such a return. If an orbit that never terminates necessarily had arbitrarily long simple windows exceeding their starting bit length by a fixed proportion and admitting a bounded number of powered blocks with total template length negligible against window length, (1) would exclude it. There is no proof of that compression assertion for the actual orbit. A parity prefix with a linear literal cost makes the condition vacuous; finite-word legality alone cannot supply it. Nor can the qualitative finite-union theorem provide a uniform threshold as the number of pieces increases.

Weaver's [Paper 15 v2, Theorems 1, 2 and 9 and Proposition 8](https://rstation.ai/problems/collatz/papers/15/v2) is the nearest comparison located. It obtains sharp maximum excursion exponent \(\log_2 3\) at fixed dictionary cost and explicit description-complexity bounds for adaptive dictionaries. Its Proposition 8 displays cancellation at a center change. The quantity in (1) is instead the **full dyadic precision of the original source** across actual center changes, with a sharp coefficient for physical time and variable height-small centers. The proof here does not assert priority over every result in the literature. Its quantitative constants come from neither of Weaver's effective estimates.

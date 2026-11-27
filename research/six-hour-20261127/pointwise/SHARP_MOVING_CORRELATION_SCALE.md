# The sharp calendar scale for critical countermodels

Fix \(p=\log_3 2\) and \(B>1\). The maximal-dimension countermodels in the companion moving-lag manuscript (SHA-256 85cdf780817e0a9c0aa3882e6f092b068a27b4cd0f560c017eb12bfa8839abae) can satisfy every one of its moving \(r\)-point Bernoulli tests whenever the tested calendar length \(\ell\) satisfies \(\ell/\log n\to\infty\), uniformly over all positions and distinct offsets among the first \(n\) shortcut letters. This is the sharp scale in the little-oh sense. For any binary string family, uniform convergence of just its one-point and two-point tables to Bernoulli-\(p\) tables on *all* calendars of length \(\ell(n)\) forces \(\log n=o(\ell(n))\).

The countermodels have dimension \(H_2(p)\) in the 2-adic starting point. One can take every source transcendental. Every prefix is strictly coefficient-supercritical, its affine coefficient is \(n^{B+o(1)}\), and the positive real affine orbit from each prescribed positive input has that polynomial height and finite reciprocal sum. Every finite word has a positive ordinary realization terminating at one, whereas its least positive cylinder seed is \(2^{n-o(n)}\). The stronger local statistics stated here keep all these properties. In particular the threshold is an obstruction about an entire family of symbolic tests. It supplies no example of an escaping positive ordinary trajectory.

## Reference permutations and sparse forced bits

Use the companion's independent fixed-weight permutations, with block lengths \(L_j=1+\lfloor\sqrt{\log_2(j+1)}\rfloor\) and weights tending to the success fraction \(p\). Keep the finite early ones-first blocks. At every late square block, force the required first bit by swapping it with exactly one occurrence of the opposite value if necessary. This suffices to kill the old least source and changes at most two letters per square. The sparse adaptive changes affect a length-\(\ell\) interval in at most \(O(1+\sqrt\ell)\) positions. Indeed it meets at most \(\ell+1\) consecutive block indices, containing at most \(1+\sqrt{\ell+1}\) squares. The corresponding bound for the union of \(r\) translated test intervals is \(O_r(1+\sqrt\ell)\).

For one ordered pattern, offsets and interval, write \(N\) for its number of occurrences before these edits. Reveal just the distinct reference coordinates on which \(N\) depends, at most \(r\ell\) bits, in any predetermined order. Within each block a reveal samples without replacement. Conditional on all previous reveals, the conditional expectations for the two possible next bits differ by at most \(2r\). To see this, couple the completions conditioned on next bit zero and next bit one by swapping that site with a uniformly chosen currently unrevealed one in the first completion. The resulting completion has the second conditional uniform law because both sides of this swapping relation have constant degrees. Other blocks can be held identical. Two changed coordinates affect at most \(2r\) starting positions. A forced reveal has range zero. The bounded-range martingale inequality now gives
\[
 \Pr(|N-\mathbb EN|>u)\le 2\exp[-u^2/(2r^3\ell)] .                       \tag{1}
\]
There are at most \(2^rn^{r+2}\) choices of the test at size \(n\). At \(u=\sqrt{2r^3(r+5)\ell\ln n}\) the union bound is summable. By Borel–Cantelli, almost surely for each fixed \(r\) all tests meet this common discrepancy bound at all large \(n\).

Uniformly for \(\ell\ge\ln n\), the expected fraction equals its Bernoulli target plus \(o_r(1)\). Delete start dates at which any selected position lies below \(\sqrt{\ln n}\), costing at most \(r(1+\sqrt{\ln n})/\ell\). At every remaining tuple, any group of positions in the same reference block samples at most \(r\) bits from a population of growing length and success fraction tending uniformly to \(p\); different blocks are independent. Adding the square edits gives, almost surely and simultaneously in the choices,
\[
 \left|N_{\mathrm{edited}}/\ell
       -p^{|u|_1}(1-p)^{r-|u|_1}\right|
  \le o_r(1)+\sqrt{2r^3(r+5)\ln n/\ell}+O_r(\ell^{-1/2}).          \tag{2}
\]
The \(o_r(1)\) is uniform at \(\ell\ge\ln n\). Thus the *same* full-measure set works along every sequence \(\ell/\log n\to\infty\), including arbitrarily slow divergence. Conditioning on complete unedited permutations gives the mass bound \(2^{-nH_2(p)+o(n)}\) on all edited cylinders, exactly as in the companion. The critical frequency gives the matching dimension upper bound. Eliminating the countable algebraic sources and imposing (2) preserve full measure.

## No binary process improves the scale

Take words of lengths \(n\to\infty\) that pass the claimed uniform one- and two-point law at one specified calendar length \(d=\ell(n)\). Set \(M=n-d+1\). Each of the \(M\) windows gives a vector \(w_i=(b_{i+j}-p)_{0\le j<d}\). Using the common start calendar \(0\le j<d\) and offsets \(i\), respectively \(i,k\), their squared lengths are \((p(1-p)+o(1))d\) and all their off-diagonal inner products are \(o(d)\), uniformly. After normalization, the \(M\) unit vectors in \(\mathbb R^d\) have absolute off-diagonal inner products tending uniformly to zero. Bounded \(d\) is impossible along an infinite subsequence because there would be repeated windows.

Here is the elementary rank estimate for this last situation. Fix \(0<\epsilon<1/4\). For all sufficiently large \(n\) the absolute inner products are at most \(\epsilon\). Form the Gram matrix for their symmetric \(k\)th tensor powers. Its rank is at most \(R=\binom{d+k-1}{k}\), its diagonal is one, and its off-diagonal entries have absolute value at most \(\epsilon^k\). The trace/Frobenius inequality therefore gives
\[
 M/[1+(M-1)\epsilon^{2k}]\le R.
\]
Take \(k=\lceil4e\epsilon^2d\rceil\), with \(e\) Euler's number. Since \(R\le[e(1+d/k)]^k\), we have \(R\epsilon^{2k}\le(e\epsilon^2+1/4)^k\le1/2\), so \(M\le2R\). Dividing the logarithm by \(d\) and taking an upper limit gives
\[
 \limsup (\ln M)/d\le4e\epsilon^2\ln\bigl(e(1+(4e\epsilon^2)^{-1})\bigr).
\]
Letting \(\epsilon\downarrow0\) shows \(\ln M=o(d)\). If \(d\le n/2\) then \(M\ge n/2\), and for \(d>n/2\) the desired conclusion holds directly. Thus \(\ln n=o(d)\) in every case. The tensor-rank principle for almost orthogonal vectors is classical. [Alon, *Perturbed Identity Matrices Have High Rank*, 2009](https://doi.org/10.1017/S0963548307008917)

## Independent review of the preceding result

The fixed-weight blocks in the frozen companion have increasing lengths, vanishing maximal length relative to log time and endpoint discrepancy fixed by the target ceiling. Thus the finite early ordering and the unrestricted late ordering give the claimed all-prefix growth. The unedited block bounded-differences calculation at the companion's larger scale \((\ln n)^2\) is valid directly; the sum of squared block ranges is at most \(r^2\ell L_{\max}\). Independent permutations and sampling without replacement give the required uniform reference mean. Adaptive square edits remain sparse on each translated interval. A cylinder specifies every fully observed unedited block permutation, yielding the stated pointwise upper mass bound without any independence assumption on the edited outputs. The cylinder isometry carries both dimension bounds to \(\mathbb Z_2\), and removing the countably many algebraic points preserves the result. The real model, positive finite lifts and principal growth retain their distinct quantifiers. The full frozen companion is accepted.

Prepared by the binary-energy reviewer, 27 November 2026 UTC. The analytic arguments are written proofs.

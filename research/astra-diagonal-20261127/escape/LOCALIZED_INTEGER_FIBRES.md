# What real localization pays at an ordinary word

Use the original iid gaps with probabilities \(2^{-e}\). For a word of length \(j\), write \(S_i\) for its successive totals in reverse order, \(\omega=3^j2^{-S_j}\), and
\[
 B_j=\sum_{i=1}^j3^{i-1}2^{-S_i}.
\]
Weaver 9 v2, Theorem 16, bounds the \(L^q(\mathbb Z_3)\) norm of the stationary subdensity on the shell \(B<R\le2B\) by \(C_qB^{1-2/q}\log(eB)^{1-1/q}\), for \(B\ge1\) and each fixed \(1\le q<\infty\). Equation (B4) also gives a pointwise \(O((1+B)j)\) bound on every depth-\(j\) ternary prefix subdensity with \(B_j\le B\). [Weaver, *Ternary Syracuse laws*, Appendix B](https://rstation.ai/problems/collatz/papers/9).

A specified word contributes density \(\omega\) on its depth-\(j\) cylinder, of Haar mass \(3^{-j}\). Imposing any stationary real-shell restriction only decreases its contribution to that cylinder average. Suppose \(B\le B_j\le2B\), \(B\ge1\). The last summand and the minimum gap 1 give
\[
 \omega\le3B_j\le6B,\qquad
 B_j\le (3/2)^j-1.
\]
For that one word the ratio of its contribution to the \(q\)-th power of the cylinder norm, to the \(q\)-th power of the shell scale in Theorem 16, is therefore at most
\[
 \frac{3^{-j}\omega^q}{B^{q-2}[\log(eB)]^{q-1}}
       \le 6^q B^2 3^{-j}\le 6^q(3/4)^j .                         \tag{1}
\]
This is a bound for the **single word's cylinder average**, with unrestricted mass used as an upper bound even after selection. It does not give a bound on the \(L^q\) cost of all conditional *subcylinders* or on all words at its residue. If \(B_j<1\), its unselected contribution is at most \(3^q3^{-j}\). In the original law the stationary real variable decomposes as \(R=B_j+\omega R'\) with an independent stationary tail, so an arbitrary tail can indeed cross real shells. The ratio (1) quantifies the spare room at the prefix and is not a claimed lower bound after that crossing. A pointwise application of (B4) likewise pays more than the single allowed slope \(\omega\). Weaver 146 obtains the stronger unrestricted weak-\(L^2\) estimate and linear collision energy; the same single cylinder costs at most \((3/4)^j\) in the squared norm because \(\omega\le(3/2)^j\). [Weaver, *Exact critical tail and linear collision energy for the ternary Syracuse law*, Theorem and Corollary](https://rstation.ai/problems/collatz/papers/146).

## A maximum over tilted cylinders on the integer section

Let \(\sigma\) be the ternary law of the same series with iid mass \(3\cdot4^{-e}\). Weaver 9 Proposition 11 gives the exact fixed-site identity \(3^j\sigma(y+3^j\mathbb Z_3)=\sum_{U^j x=y}\omega_j(x)^2\) at all odd \(y>0\). It also bounds the sum over \(j\) by \(\pi^2 y^2/8\) at nonperiodic sites, with a lap correction at periodic sites. Define the normalized maximal cylinder average
\[
 M(y)=\sup_{j\ge0}\frac{3^j\sigma(y+3^j\mathbb Z_3)}{y^2}
     =\sup_{j\ge0}\sum_{U^jx=y}\frac{f_j(x)^2}{x^2},\qquad
 f_j(x)=\frac{\omega_j(x)x}{y}.
\]
Then \(M(y)\le\pi^2/8\) for every positive odd \(y\), and
\[
 M(y)\to0\quad(y\to\infty\ \text{through the positive odds})
 \quad\Longleftrightarrow\quad
 \text{every positive orbit is eventually periodic}.                 \tag{2}
\]
Indeed, if all orbits are bounded, fix \(T\); the union of the orbits of the finitely many positive odd \(x\le T\) is finite. Beyond its maximum, \(M(y)\le\sum_{x>T}x^{-2}\), which tends to zero as \(T\to\infty\). For a fixed escaping odd \(x\), the uniform reciprocal packing of simple segments gives \(f_\infty(x)>0\). On \(y_j=U^j x\to\infty\), its original word alone gives \(M(y_j)\ge f_\infty(x)^2/x^2\). The argument allows any number of finite cycles. Weaver 176 Theorem 3 already detects escape by the *global single-period tilted moment* at every fixed power \(s>1\). Here (2) tests a height tail of the maximal individual cylinder average of the same law.

On one escaping ray, the time-summed version has the exact limit
\[
 \frac1{y_j^2}\sum_{n\ge0}3^n\sigma(y_j+3^n\mathbb Z_3)
     \longrightarrow
 \sum_{x\in C}\frac{f_\infty(x)^2}{x^2}>0,                          \tag{3}
\]
where \(C\) is the full component feeding this ray. Each source reaches a nonperiodic \(y_j\) at most once. For a source in \(C\) its eventual hitting times of \(y_j\) grow without bound; the product tends to \(f_\infty(x)\). Every source outside \(C\) contributes zero. Domination by \(x^{-2}\) proves (3). In particular the quadratic scale in the existing fixed-target trace budget is the precise scale on every hypothetical escaping component. A uniform little-oh improvement would exclude escape. Under the cited uniform distinct-orbit interval count \(\#(\mathcal O(x)\cap[Y,2Y])\ll Y^\theta\) for a fixed \(\theta<1\), one already has \(\sum_{Y\le y\le2Y}M(y)\ll Y^\theta\): drop the time supremum by counting each visited site once for each source and sum \(x^{-2}\). This averaged estimate is compatible with the actual moving lower bound. [Weaver 9, Proposition 11](https://rstation.ai/problems/collatz/papers/9) · [Weaver 176, Theorem 3 and reciprocal packing inputs](https://rstation.ai/problems/collatz/papers/176) · [Weaver 175, orbit interval count](https://rstation.ai/problems/collatz/papers/175).

## A unit dilation that keeps the localized random law and fails the cropped test

The separate positive odd map \(U_5(x)=\operatorname{oddpart}(3x+5)\) has affine iid word data \((5B_j,\omega)\) and stationary pair \((5R,5Z)\). Multiplication by 5 preserves Haar measure on \(\mathbb Z_3\), so the same fixed-shell \(L^q\) estimates hold with \(B\) replaced by \(B/5\) and harmless fixed constants on bounded shells. Its finite density is \(\rho_j^{(5)}(y)=\rho_j(5^{-1}y\bmod3^j)\). The same pushforward statement holds exactly for the squared tilted ternary law. In both models, every original word with ternary residue \(y\) from a positive odd target \(y\) recovers an integer predecessor at every inverse step, but for the comparison model at small \(y\) positivity of every such predecessor need not hold in general. At target 5 and throughout its actual odd inverse tree positivity holds by exact scaling.

On the ordinary positive graph \(U_5(5x)=5U(x)\), and \(5\mid U_5(x)\) if and only if \(5\mid x\). In particular 1 and 5 are separate fixed points; each finite-depth odd ancestor of 5 is a multiple of 5. Put \(w_x^{(5)}=3x/(3x+5)\). Every branch ending at 5 thus has multiplicative defect at least \((3/4)^j\) at depth \(j\). At \(t_j=(3/4)^{j+1}\), the depth-\(j\) CDF at 5 gives zero mass. The constant path \(5,\ldots,5\) at depth \(j+1\) has exactly this defect and original CDF mass \((3/4)^{j+1}\rho_1^{(5)}(5)=(3/4)^{j+1}\). Eventually \(t_j\le1/(j+1)\). Hence its positive cropped difference at the ordinary site 5 exceeds the required polynomial multiple of \((2/3)^j\) along every unbounded sequence, while the paired-law marginal regularity persists.

This example tests a proposed inference using the marginal regularity and the actual scaled root. It changes the integer affine offset and does not disprove an estimate exploiting its specific value \(+1\). The [Lean module](ScaledSource.lean) checks scaled ordinary dynamics at every clock, invariance and reflection of divisibility by 5, the two fixed points, and the impossibility of a scaled source reaching 1.

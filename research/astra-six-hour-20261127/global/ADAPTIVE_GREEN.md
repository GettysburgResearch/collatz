# An arithmetic Green function without a logarithmic first-hit premise

**PROPOSED.** The criterion below is equivalent to positive Collatz convergence. Its finite levels are computable rational functions on finite ternary residue rings. The proof gives uniform bounds on all nonperiodic ordinary targets away from the forward trajectories of a fixed finite source set. The bound needed on those particular trajectories remains open.

The fixed exponential time multiplier in [the first Green test](TILTED_GREEN.md) is stronger than convergence alone. Finiteness at 1 would already force every terminating odd source \(n\) to have first odd hitting time \(O(\log(2n))\). Indeed its genuine first-hit contribution bounds \(t^{k}(f_k(n)/n)^s\) from above, while simple-path packing bounds \(f_k(n)\) below uniformly. This uniform clock remains open. Weaver's 14.3 lower coefficient uses the shortcut clock and is fixed. [Paper 127, Corollary 10](https://rstation.ai/problems/collatz/papers/127) · [Paper 222, §7.9](https://rstation.ai/problems/collatz/papers/222)

## Prefix-dependent rational weights

Put \(s=3/2\). For each positive odd integer \(r\), write
\[
    d=\max(r,13),\qquad b(r)=1+\frac1{2d}+\frac1{12d^2},
    \qquad B=b(13)<26/25 .
\]
This multiplier is nonincreasing. For any chronological word \((e_1,\ldots,e_k)\), set \(A_i=\sum_{j\le i}e_j\), \(F_e(z)=(3z+1)/2^e\) on \(\mathbb Z_3\), and \(F_{[i]}=F_{e_i}\circ\cdots\circ F_{e_1}\). Let \(r_i\) be the least positive odd representative of \(F_{[i]}(0)\bmod 3^i\), with \(r_0=1\). The actual weight of the word in the rational test is
\[
    a_w^{\mathbb Q}
    =\frac{3^{\lfloor 3k/2\rfloor}}{2^{\lceil 3A_k/2\rceil}}
       \prod_{0\le i<k} b(r_i).
\]
For an upper comparison define \(a_w=(3^k2^{-A_k})^s\prod b(r_i)\). Then \(a_w/\sqrt6\le a_w^{\mathbb Q}\le a_w\), with only one bounded rounding factor for the entire word. Write
\[
 G^{\mathbb Q}(z)=\sum_{k\ge0}\sum_{|w|=k}a_w^{\mathbb Q}
                   \mathbf1_{z\in F_{[k]}(0)+3^k\mathbb Z_3},
 \qquad G(z)=\sum_{k,w}a_w\mathbf1_{z\in F_{[k]}(0)+3^k\mathbb Z_3}.
                                                                    \tag{1}
\]
At fixed \(k>0\), take \(L=2\cdot3^{k-1}\). Reduce each positive \(e\) to its representative in \(1,\ldots,L\) modulo \(L\). This preserves every prefix residue \(r_i\) and the terminal residue. Adding \(mL\) to a gap increases the rounded binary exponent by \(3mL/2\). Thus the rational depth-\(k\) sum is the sum over the finite alphabet \(1,\ldots,L\), multiplied by \((1-2^{-3L/2})^{-k}\). This is an exact, potentially very large finite computation.

Both functions are integrable for ternary Haar probability:
\[
    \int G^{\mathbb Q}\le \int G\le
       \sum_{k\ge0}(B\lambda_s)^k<\infty,
    \qquad \lambda_s=\frac{\sqrt3}{2\sqrt2-1}.
\]
Each word ball costs \(3^{-k}\). For the strict inequality one may use \(B<26/25\), \(\sqrt3<26/15\) and \(\sqrt2>141/100\). Every finite level and both increasing infinite sums use precisely the displayed prefix law.

## Ordinary sources pay only before their initial binary digits are consumed

For positive odd \(x\) use the true map \(U(x)=(3x+1)/2^{v_2(3x+1)}\); put \(x_i=U^ix\), \(w_x=3x/(3x+1)\). For any word in (1) compatible with a positive odd target \(y\), its inverse is a unique positive odd integer \(x\) with exactly these gaps and \(x_k=y\). The normalized contribution to \(u(y)=G(y)/y^s\) is
\[
       x^{-s}\prod_{i<k} b(r_i)w_{x_i}^{s}.                               \tag{2}
\]
Always \(r_i\le x_i\). On the row \(x=1+2l\), the [canonical birth identity](CANONICAL_BIRTHS.md) states
\[
        r_i=x_i\quad\Longleftrightarrow\quad l<2^{A_i}.
\]
Once true, this remains true. It fails at no more than \(1+\log_2 x\) indices, since \(A_i\ge i\). At each failing index the boost is at most \(B\).

At an exact index with \(x_i\ge13\), the normalized multiplier satisfies
\[
        1 < b(x_i)w_{x_i}^s \le 1+\frac1{12x_i^2}.                     \tag{3}
\]
For the lower inequality put \(v=1/(3x_i)\), and square \(1+3v/2+3v^2/4\) to compare it with \((1+v)^3\); their difference is strictly positive. For the upper inequality, \((1+v)^{3/2}\ge1+3v/2\). At \(x_i<13\) the multiplier is at most one: \(w_{x_i}\le33/34\), and \(B^2(33/34)^3<1\). Hence the product in (2) along **any finite simple positive path** is at most
\[
      \frac{14}{13}B\,x^{\beta},
      \qquad \beta=\log_2 B<s-1.                                       \tag{4}
\]
For each integer \(n\ge1\),
\[
  1+\frac1{12n^2}\le\frac{(n+1)^2}{n(n+2)}
     =\frac{1+1/n}{1+1/(n+1)}.
\]
The factors on the right are at least one. The product over distinct high indices is bounded by the product over every integer from 13 through the largest index, which is less than \(14/13\). This proves (4) uniformly in the path length.

Consequently at every nonperiodic target \(y\), unconditionally, \(u(y)\le C\sum_{x\text{ odd}}x^{-s+\beta}<\infty\), uniformly in \(y\). A source can reach a nonperiodic target at most once, through a simple path. If \(y\) lies outside the full forward orbits of all odd starts through \(M\), then \(u(y)\le C' M^{1-s+\beta}\) uniformly at nonperiodic \(y\). This polynomial bound controls all remaining ordinary sources together.

## Exact equivalence

The following two statements are equivalent:

1. Every positive integer reaches one.
2. \(G^{\mathbb Q}(y)<\infty\) at every positive odd \(y\), and \(G^{\mathbb Q}(y)/y^{3/2}\to0\) through positive odd integers.

If all orbits reach one, each source visits any \(y>1\) at most once and visits only finitely many such targets. The bound (4) gives a summable majorant over sources. Dominated convergence as \(y\to\infty\) proves the asserted decay. At its first entry to 1 the source has already undergone canonical birth, since the endpoint is the least representative. Further laps have constant multiplier \(B(3/4)^s<1\). The geometric lap sum and the same majorant give finiteness at 1.

Conversely a nontrivial positive cycle has all odd states at least 13, because \(1,3,5,7,9,11\) each reaches one. Start at any phase of such a cycle. At all sufficiently late steps the representative equals the physical state. By (3) the product on a full lap is greater than one. The repeated word makes \(G(y)=\infty\) at each phase. On an escaping path take its fixed positive odd source \(x\). All its states exceed 11, and the actual product after birth is at least one. Equation (2) yields \(u(U^k x)\ge c_x>0\) for every sufficiently large \(k\), while the distinct states tend to infinity. The one-time rounding sandwich transfers both conclusions to (1). An even positive start reduces to its odd part by ordinary halvings.

## Positive ordinary recursion and the total cost of prefix rounding

Write \(u_k\) for the normalized unrounded depth-\(k\) term, and \(r_k(x)\) for the least positive odd representative of \(x\bmod3^k\). Appending the last edge gives the exact identity
\[
 u_{k+1}(y)=\sum_{Ux=y} b(r_k(x))w_x^s u_k(x).
\]
Here every prefix ending at \(x\) has that same representative. Since \(r_k(x)\le x\), monotonicity of \(b\) gives a genuine ordinary positive transfer with a nonnegative source error. For \(D(x)=b(x)w_x^s\) and \((Lv)(y)=\sum_{Ux=y}D(x)v(x)\), one has pointwise, allowing infinity on both sides,
\[
      u(y)=y^{-s}+(Lu)(y)+R(y),\qquad
      R(y)=\sum_{k\ge0}\sum_{Ux=y}[b(r_k(x))-b(x)]w_x^s u_k(x)\ge0 .
\]
Moreover \(R\in\ell^1\) unconditionally. A nonzero summand has \(r_k(x)<x\). Every original source \(n=1+2l\) contributing to that \(x\) is still before birth, hence \(l\ge2^{A_k}\ge2^k\). Its normalized prefix weight is at most \(B^k n^{-s}\). Summing first over all possible ordinary targets, and then over all original \(n>2^k\), bounds the depth-\(k\) source error by \(C_s B(B2^{1-s})^k\). The displayed base is strictly below one. In particular the word-defined law differs from the recursive ordinary law only by summable nonnegative injections. The persistence of an individual source on an escaping trajectory is compatible with both this bound and the Haar estimate in (1). An upper bound ruling out that persistence remains to be proved.

## Comparison with the finite rational energy

For a positive odd integer \(n\), set \(d(n)=1/4\) below 13 and
\(d(n)=1+1/(32n^2)\) otherwise. At every prefix of an authentic path,
\[
       d(x_i)\le b(r_i)^2w_{x_i}^{3}.
\]
Indeed, \(b(r_i)\ge b(x_i)\), and at a high state \(n\) the exact squared surplus equals
\[
 b(n)^2 w_n^3-1=\frac{36n^2+20n+3}{16n(3n+1)^3}\ge\frac1{32n^2}.
\]
At all positive odd states \(b(r_i)\ge1\) and \(w_{x_i}^3\ge(3/4)^3>1/4\).
For any finite depth and height cutoffs \(K,H\), the [rational energy](../root/RationalEnergy.lean) consequently satisfies
\[
 E(K,H,y)=\sum_{\substack{k\le K,\ 1\le x\le H\text{ odd}\\ U^kx=y}}
  x^{-3}\prod_{i<k}d(U^ix)
  \ \le\ \left(\frac{G(y)}{y^{3/2}}\right)^2
  \ \le\ 6\left(\frac{G^{\mathbb Q}(y)}{y^{3/2}}\right)^2.
\]
The first inequality follows by summing the squares of the nonnegative contributions in (2) and retaining their nonnegative cross terms in the square of the whole sum. The second uses the single rounding loss. [Finite coefficient lemmas](AdaptiveGreen.lean).

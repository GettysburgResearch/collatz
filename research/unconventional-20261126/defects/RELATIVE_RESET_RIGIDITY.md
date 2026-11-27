# A relative arithmetic cost for crossing Syracuse resets above a floor

**Status.** Proposed ordinary-integer theorem. The analytic input for Theorem A is Matveev's real logarithmic-forms theorem. The retention bound in Theorem B is elementary. Both apply to individual trajectories and permit the factorization test to be selected after the two actual endpoints are known. No existence of a nonconvergent trajectory is assumed in either theorem.

Write the Syracuse trajectory on positive odd integers as
\[
   2^{a_i}x_{i+1}=3x_i+1,\qquad y_i=x_i+1,\qquad
   A=\sum_{i<k}a_i.
\]
Count a reset when \(a_i\ge2\), and write \(R\) for their number. If \(R\ge1\), put
\[
   F=\min_{i<k:\ a_i\ge2}y_{i+1}.
\]
Only actual reset outputs enter this minimum. At a positive rational \(v\), let \(h(v)=\log\max(\operatorname{num}(v),\operatorname{den}(v))\) in lowest terms. All unlabeled logarithms are natural.

## A. An arbitrary number of resets and an adaptive endpoint test

Remove the factors 2 and 3 from \(y_k/y_0\) after cancelling the common numerator and denominator factors. Call the resulting positive rational \(\rho\). For every positive ordinary segment with \(R\ge1\), one absolute effective constant \(C\) satisfies
\[
\begin{split}
 \log F &\le C (1+h(\rho))\log(2+k+\log y_0),\\
 \log F &\le C (1+h(\rho))\{R+\log(2+\log y_0)\}.          \tag{1}
\end{split}
\]
In particular the size, rank and prime factors of a common endpoint divisor cost nothing.

A finite set \(S\) of \(r\) additional primes may be chosen separately for each segment, including after both endpoints have been seen. Delete its prime powers from \(\rho\) too and call the result \(\rho_S\). Both assertions of (1) hold with \(C(1+h(\rho))\) replaced by
\[
  C(r)\,(1+h(\rho_S))\prod_{p\in S}\max(1,\log p).          \tag{2}
\]
Here \(C(r)\) is effective and independent of the selected primes, both ordinary endpoints, their common divisor, the elapsed time and all the individual division exponents. The displays intentionally charge the heights of primes in a moving set. A bound on their number alone would erase real arithmetic information.

### The signed error is strictly nonzero

There is an exact reciprocal product
\[
 W=\frac{3^k y_0}{2^A y_k}
   =\prod_{i<k}(1-d_i),\qquad
 d_i=\frac{1-2^{1-a_i}}{y_{i+1}}.
\]
Indeed \(3y_i=2^{a_i}y_{i+1}-(2^{a_i}-2)\). At a match \(d_i=0\). At a reset \(0<d_i<1/y_{i+1}\). Therefore
\[
             0<1-W\le\sum_i d_i< R/F                 \tag{3}
\]
whenever \(R>0\). This holds also when \(R/F\) exceeds one. It needs neither distinct states nor an upper bound on time or valuations. When \(R=0\), \(W=1\) exactly. For instance the first \(m-1\) transitions from \(2^m-1\) have \(y_j=2^{m-j}3^j\), so including this case in (1) with a growing initial floor would be false.

Write \(y_k/y_0=2^u3^v\rho\). Then \(W=2^{-(A+u)}3^{k-v}\rho^{-1}\). Even when \(\rho=1\) or a displayed exponent vanishes, (3) proves that the remaining product is unequal to 1. The standard rational-field specialization of the real logarithmic-forms estimate is as follows. For a positive rational product \(W=\prod_{j=1}^s\gamma_j^{b_j}\ne1\), with \(B\ge\max(3,|b_1|,\ldots,|b_s|)\),
\[
    -\log |1-W|\le C_s\log B\prod_j\max(1,h(\gamma_j)).   \tag{4}
\]
One can delete unit bases and zero exponents. For one remaining base the same bound also follows by the elementary separation of a positive rational from one and monotonicity in the integer exponent. For two or more bases (4) is a deliberately weakened rational positive-real form of Matveev's theorem. A bound on \(|\log W|\) gives the stated product bound at \(0<W<1\) by considering separately \(W\le1/2\) and \(W>1/2\). This use has no multiplicative-independence hypothesis. [Matveev, 2000, Corollary 2.3](https://doi.org/10.1070/IM2000v064n06ABEH000314) · [Rational-product formulation, Theorem 2.1](https://doi.org/10.1007/s12188-025-00293-9)

At every step \(y_{i+1}\le(3/2)y_i\). Multiplying \(2^{a_i}x_{i+1}\le4x_i\) gives \(A\le 2k+\log_2 x_0\). Every prime valuation of either shifted endpoint is at most \(\log_2 y_0+k\). Consequently \(B\ll 2+k+\log y_0\) works both for the three-base expression and after peeling off every prime in \(S\). The residual base occurs with exponent \(-1\). Combining (3) and (4), then absorbing \(\log R\le\log k\), proves the first line of (1) and its adaptive form.

### Converting an odd clock to a reset clock

Set \(\alpha=\log_2 3\). At the start of a complete block let \(y=2^t w\) with \(w\) odd. The block has \(t\) odd steps, the first \(t-1\) of exponent one. Its final step is a reset, with some exponent \(b+1\), where \(b=v_2(3^t w-1)\ge1\). Its output \(z\) obeys
\[
                       2^b z=3^t w-1.                         \tag{5}
\]
Thus \(z+1\le3^t w\le y^\alpha\) and every earlier shifted state in the block is also at most \(y^\alpha\). Its length \(t\) is at most \(\log_2 y\). After the \(R\) complete blocks a final string of matches, potentially empty, costs at most the logarithm of its entrance. It follows that
\[
       k\le (1+\alpha+\cdots+\alpha^R)\log_2 y_0.              \tag{6}
\]
This proves the second line of (1) including the single-reset case. The restriction \(R>0\) was used in (3), not in (6).

### Time separation, reset separation and the ordinary least disagreement

Suppose \(F\to\infty\), \(y_0\le F^D\) for a fixed \(D\), and the multiplier in (2) stays bounded. This includes completely arbitrary pairs with the same prime-to-six part and completely arbitrary common part. The first line of (1) gives \(k\gg F^c\) for some \(c>0\); the second gives \(R\gg\log F\). More generally \(1+h(\rho)\ll(\log F)^\theta\), with \(0\le\theta<1\), gives \(\log k\gg(\log F)^{1-\theta}\).

With one additional source-qualified input the last case forces
\[
                 R\gg (\log F)^{1-\theta}\log\log F.           \tag{7}
\]
For this inference the path must avoid 1 as an input. This is automatic if its minimum actual state tends to infinity; if the initial state is 1 then its reset output is also 1 and \(F=2\), and a later first visit to 1 must be a reset. Apply Weaver's finite dictionary-duration inequality with the singleton dictionary consisting of the one-letter word \((2)\). Its only positive center is 1. Each reset is an allowed singleton piece and strings of ones are free, so the minimal dictionary cost is at most \(R\). Equation (1) of that source implies, for every integer \(m\ge1\),
\[
 \log\!\frac{k+1}{\log(x_0+G)}
 \le \log(R+1)+(R/m+1)\log 2+e^{C_0m}+O(1)
\]
with absolute constants for this fixed dictionary. The left side is \((1-o(1))\log k\) by \(y_0\le F^D\) and the just-proved lower bound on \(\log k\). If \(R\ge(\log k)^2\), (7) follows directly. Otherwise take \(m=\lfloor\log\log k/(2C_0)\rfloor\), which tends to infinity. The first and exponential terms are \(o(\log k)\), so \(R\gg\log k\log\log k\), giving (7). No threshold for a fixed entrance has been applied at changing entrances. [Weaver, Paper 15, Theorem 1, equation (1)](https://rstation.ai/problems/collatz/papers/15)

For a hypothetical least tripling disagreement \(s\) from PR192, start this segment at the nonconvergent odd value \(x_0=3s\). All positive integers through \(s\) converge. Thus every true odd state on this one orbit exceeds \(s\). For **every** prefix containing a reset, (1) yields
\[
  1+h(\rho) \ge c\frac{\log(s+1)}{R+\log(2+\log(3s+1))}.     \tag{8}
\]
The same inference at the minimum of each forward tail applies on a hypothetical escaping orbit, since an injective sequence of positive integers tends to infinity and its future tail attains a minimum. Equation (8) describes one orbit, without choosing any further source bits. A return with bounded relative cofactor on such a protected segment costs at least order \(\log(s+1)\log\log(s+2)\) resets asymptotically. The estimate is uniform as the floor increases. At a single fixed floor it gives a finite lower bound. [PR192 ordinary least-disagreement hypotheses](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/minimal/MinimumFailure.lean)

## B. How much odd content can survive the next reset?

For the complete block (5) put
\[
      g=\gcd(w,z+1)=\gcd(w,2^b-1).
\]
The equality holds since \(w\) is odd and \(2^b(z+1)=3^t w+2^b-1\). This is precisely the gcd of the odd parts of \(x+1\) and \(z+1\), including any common factor three. For any positive divisor of this gcd,
\[
              z<\left(\frac{x+1}{g}\right)^{\alpha}.            \tag{9}
\]
Indeed \(g\le w\), \(g<2^b\) and \(gz<3^t w\). Thus
\[
 z<(3/2)^t\frac{x+1}{g}
   =(2^t)^{\alpha-1}\frac{x+1}{g}
   \le\left(\frac{x+1}{g}\right)^\alpha.
\]
If \(z\ge\lambda(x+1)\) for fixed \(\lambda>0\), then
\[
   g<\lambda^{-1/\alpha}(x+1)^{1-\log_3 2}.
\]
The exponent \(1-\log_3 2\) is approximately 0.369071. The sharp asymptotic exponent at this same floor is approximately 0.269577, using the Subspace Theorem and a matching ordinary construction. [Sharp reset retention](SHARP_RESET_RETENTION.md) In particular sufficiently large inherited odd content forces a genuine drop at that reset. This condition involves the next physical valuation and the odd part of the initial shifted source. Its satisfaction at arbitrary sources has not been proved.

**Kernel scope.** The accompanying Lean file proves the nonnegative cross-multiplied version of (3), including strict positivity exactly when at least one reset occurred, by induction over arbitrary exact ordinary paths. It also proves the single-reset divisibility and the exact integer version \(z^d g^m<(x+1)^m\) of (9) for *every* positive rational upper approximation \(m/d\) with \(3^d\le2^m\). For example \((m,d)=(8,5)\) gives \(z^5g^8<(x+1)^8\). The analytic input, the real logarithm manipulation and the imported duration estimate are written arguments.

## Related work and scope

The earlier centered-defect argument treats periodic centers and any bounded number of mismatches, using endpoint membership in fixed finite-rank families and the unit-equation theorem. Here the special center \(-1\) makes every correction at a true reset strictly positive. This gives an effective estimate on the *quotient* of the two shifted endpoints, with unrestricted time, unrestricted reset count, and no arithmetic restriction on their common part. The smooth-source height theorem instead uses dyadic logarithms to protect an initial range starting with a shifted smooth integer. Equations (1)–(9) place no smoothness requirement on the initial integer. Quantitative time-versus-floor comparisons for unshifted near returns occur in Paper 147. The ordinary ascent bound and dictionary estimate have precedents in Paper 15. [Unshifted precise returns, Paper 147](https://rstation.ai/problems/collatz/papers/147) · [Dictionary height and duration, Paper 15](https://rstation.ai/problems/collatz/papers/15)

The first unsupported implication toward Collatz is that a surviving ordinary orbit has to retain a sufficiently large odd divisor at some reset, or make a low-cost return of the shifted endpoint quotient within the corresponding clock bound. The dynamical identities require neither event. An orbit that keeps replacing old odd factors with large new factors meets every obstruction above. No descent theorem for every ordinary source or exclusion of all positive cycles follows.

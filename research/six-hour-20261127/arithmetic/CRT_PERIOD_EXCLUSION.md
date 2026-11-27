# All 25 remaining period pairs excluded by located CRT addresses

**PROPOSED finite theorem, with exact integer replay.** Let a primitive ordinary positive odd cycle satisfy
\[
 2^{e_i}x_{i+1}=3x_i+1,\quad e_i\in\{1,2\},\quad
 s=\min_i x_i\ge 2^{71},\quad \max_i x_i\le(16s+7)/3 .
\]
Then its odd period \(p\) exceeds \(10^{1000}\). The earlier finite screen left 25 clock pairs in this range. For each one, the two local addresses of an ordinary phase occupy too few positions in a required real interval. The argument counts the actual intersection on a single CRT circle. [Earlier period screen, exact enumeration and hypotheses](PERIOD_GAP.md)

With Barina's independently reported trajectory verification for all positive integers below \(2^{71}\), this excludes the entire period range for a nontrivial cycle on the bounded least-tripling-disagreement alternative. Barina's computation is an external input for dropping the minimum-height hypothesis. The present finite replay uses integral comparisons, a directed logarithm enclosure and the preceding enumeration. It does not run that trajectory verification. [Barina, *Improved verification limit for the convergence of the Collatz conjecture*, §6](https://doi.org/10.1007/s11227-025-07337-0)

## Additive coordinates on the full product modulus

Fix a normalized source band \(a/b\le y/s<(a+1)/b\), a length \(k\) for its past word and a length \(f\) for its future. In each word start with \(E_0=0\). For pasts read the exponents outwards, beginning with the edge immediately preceding \(y\). For futures they are chronological. Retain the prefix inequalities for these respective directions in the earlier screen, which are necessary throughout the physical strip. At each row a choice of the new total \(E_j\) and the previous total specifies the edge.

Fix the terminal *future* total \(A\), and put \(P=3^k,\ Q=2^{A+1},\ M\ge1\). A past determines the middle phase modulo \(P\) by
\[
 a_-=\sum_{j=1}^k 3^{j-1}2^{-E_j}\pmod P .
\]
Indeed the reverse recurrence has cumulative numerator \(2^{E_j}y-C_j\) over \(3^j\), with \(C_0=0,\ C_j=2^{e_j}C_{j-1}+3^{j-1}\). A future determines
\[
 a_+=2^A-\sum_{j=1}^f 2^{E_{j-1}}3^{-j}\pmod Q
\]
by iterating the forward affine equation and requiring the last site odd. The term \(3^{-f}2^A\) equals \(2^A\bmod Q\).

The location of the combined residue on the real circle \(\mathbb R/\mathbb Z\) is exactly
\[
 \frac{y}{PQ}\equiv
  \frac{a_- (Q^{-1}\bmod P)}{P}
  +\frac{a_+ (P^{-1}\bmod Q)}{Q}\pmod1.                         \tag{1}
\]
The first numerator in the CRT sum equals \(a_-\) at \(P\) after multiplication by \(PQ\), and vanishes at \(Q\). The second does the reverse. Invertibility is used only at the respective coprime modulus.

For each edge of each word replace its signed contribution in (1) by the residue \(\delta\in[0,1)\), then by the circular integer \(\lfloor M\delta\rfloor\bmod M\). Each new slot is obtained by a cyclic row shift and the addition of rows arriving at the same exponent total. The \(2^A\) term contributes a common half-turn, since \(P^{-1}\bmod Q\) is odd. It may be suppressed when taking a supremum over locations. Add the final past histograms over all grades to obtain \(H\). Take the final future histogram of grade \(A\) to obtain \(K\). These are integer histograms of *all* retained words; shifts at a given time depend only on the cumulative exponents and \(P,Q\). The constants \(P,Q\) stay fixed during both passes for this grade.

Let \(n=\sum H_i,\ m=\sum K_i\). For any circular sum slot \(z\), centering both rows in \(\sum_i H_i K_{z-i}\) and using Cauchy–Schwarz gives the peak bound
\[
 B=\left\lfloor\frac{nm+
      \sqrt{(M\sum H_i^2-n^2)(M\sum K_i^2-m^2)}}{M}\right\rfloor .        \tag{2}
\]
An integer square root before division gives exactly this floor.

For every word pair, the true angular location is its quantized circular sum plus the common half-turn and a displacement in \([0,(k+f)/M)\) (at positive depth). Thus any interval of real source values of width \(W\) contains at most
\[
          \big(\lfloor MW/(PQ)\rfloor+k+f+2\big)\,B                 \tag{3}
\]
sources at this grade. To account for integer lifts when \(W\ge PQ\), periodically extend all circular sum slots to the real line. Translate by the common half-turn and enlarge the rescaled interval at its lower end by \(k+f\) slots. Each lifted slot has at most \(B\) covered word pairs. For a fixed pair and starting slot lift, the angular error is fixed, so at most one physical representative can be charged there. The interval contains at most the displayed number of integer slots, also for open or closed endpoints. Equation (3) is uniform in the **unknown location** of the physical band. No equidistribution of either row is assumed; both centered moments in (2) are measured exactly.

## The physical rank comparison

Use \(b_0=12,\ 12\le a<24\) for a chosen normalized rank interval \([a/12,(a+1)/12)\). For band \(j=0,1,2\), the actual physical ratio \(y/s\) has denominator \(b=12/2^j\) in the interval above. Omit it only when its lower boundary exceeds the rational strip bound from the preceding screen. For an upper bound \(s\le S\), take \(W=S/b\) in (3), sum over future grades, then over the retained physical bands.

Write \(\epsilon=h/p-\log_2 3\) where \(h\) is the native shortcut clock. If directed logarithms give \(0<\epsilon_-\le\epsilon\le\epsilon_+\), choose
\[
 S=\left\lceil\frac7{20\epsilon_-}\right\rceil,\qquad
 s_0=\max\left(2^{71},\left\lfloor\frac{1/\epsilon_+-8}{16}\right\rfloor\right).
\]
The ordinary cycle product and \(\log(1+t)\ge t/(1+t)\) give \(\epsilon\ge1/((16s+8)\ln2)>1/(16s+8)\), hence \(s\ge s_0\). The upper bound \(s\le S\) follows from (6) of the preceding period screen once \(1000\le p\le s_0/100\), which is checked for every pair. Equation (7) there forces the rank population to be at least
\[
 \left\lceil\frac{2884p}{1000(2a+1)}-\frac{p^2}{s_0}-2\right\rceil .       \tag{4}
\]
This demand strictly exceeds the upper count at every one of the 25 pairs. At the largest surviving odd period \(31\,150\,961\,018\,190\,238\,869\,556\) the upper count is \(1\,246\,981\,053\,162\,858\,257\,508\) and the required count is \(1\,996\,430\,479\,476\,903\,308\,883\). The closest of the 25 comparisons is \(7\,219\,532\,352<8\,814\,019\,611\) at odd period \(137\,528\,045\,312\). [All 25 exact comparisons](CRT_PERIOD_CONTROLS.json) · [Integer verifier](check_crt_histograms.py)

The verifier imports the preceding directed logarithm bounds and reads its complete period-pair list. It separately enumerates 78 short past/future pairs, computes the ordinary residue from the two exact affine equations, compares every histogram bucket and checks the cyclic enclosure and interval caps including wraps. All checker conditions are explicit and run in optimized Python. Lean checks the additive CRT identity, the accumulation of rounding error and the centered convolution inequality over integer histograms. The analytic rank estimate, finite search in the predecessor packet and the present dynamic programming link are written and computational components. [Lean kernel](CRTAddress.lean)

**Remaining obligation.** This finite exclusion supplies no uniform decay of the centered second moments as the physical height and the required quantization precision grow. It permits periods above the tested limit and does not treat the separate first-crossing alternative.

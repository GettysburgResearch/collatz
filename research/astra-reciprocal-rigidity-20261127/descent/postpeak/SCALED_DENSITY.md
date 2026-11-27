# A common ternary set for every scaled ramp and every maximal postpeak word

The full common set contains at least **259/960 of all ternary classes**, and at least 3/20 of all classes lie in its zero residue. The source threshold below has the strictly improved alternative $2n\ge K(1+3^K)$. The ordinary source-specific classification at that threshold is kernel checked through the executable Boolean $\mathtt{decideScale}$. The universal common-set cardinality uses the written counting proof below. [Exact selector](SELECTOR.md) · [Lean specification](DecideSelector.lean)

**Written theorem.** For every integer \(K\ge1\) there is a finite, computable set \(F_K\subset\mathbb Z/3^K\mathbb Z\) containing at least \((3/20)3^K\) residues. All are multiples of three. Suppose \(n>0\), its residue belongs to \(F_K\), and

\[
                      n+1\ \ge\ 2(9/2)^K.                         \tag{1}
\]

For **every** pair of nonnegative integers \(j,\delta\) with \(2^j\mid 2^\delta(n+1)\), suppose the integer \(Y\) satisfies

\[
                      2^j(Y+1)=3^j 2^\delta(n+1).
\]

Every positive \(m<n\) that visits \(Y\), at an arbitrary ordinary shortcut clock, spends more than \(j+K\) odd departures. In particular \(\delta=0\) covers the whole initial odd ramp of each actual \(n\), including its first shortcut when it is odd. No lower bound on \(j\) is needed. Formula (1) applies even when the scale or ramp length grows independently of \(K\).

For the actual upper source \(n=2^Hv-1\) with positive \(v\), let \(w\) be a physical postpeak word from \(P=3^Hv-1\), of weight \(f\) and even count \(q\). Suppose \(H\ge21q+9K+3\) and \(w\) is maximal among the equally long words with its signed offset. Then every positive smaller visitor at its endpoint costs **more than \(H+f+K\)**. This follows by applying the kernel-checked paid-peak theorem and the all-scales protection above. The same ternary source set works simultaneously for all such words.

## Exact extraction and the height cutoff

The shortcut map sends an odd input \(x\) to \((3x+1)/2\) and an even input to \(x/2\). On positive paths an odd step multiplies \(x+1\) by \(3/2\) and an even step weakly decreases it. The prescribed \(Y+1=(3/2)^j2^\delta(n+1)\) therefore forces every lower path from \(m<n\) to use strictly more than \(j\) odd departures, and hence to have physical clock greater than \(j\).

Write the lower odd count as \(j+b\), and suppose \(1\le b\le K\). For \(j\ge1\), cut this path immediately **before the first of its final \(j\) odd departures**. The prefix contains \(b\) odd departures. Any even steps between the \(b\)-th and \((b+1)\)-st odds are part of the prefix. Thus the suffix starts at an odd positive integer \(z\), contains \(j\) odds and some \(\ell\) evens, and ends at \(Y\). Write its unsigned intercept \(A\) via \(2^{j+\ell}Y=3^j z+A\). Then

\[
 z=2^{\ell+\delta}(n+1)-M,\qquad M=(2^{j+\ell}+A)/3^j.
\]

The first equality makes \(M\) an integer. The formal suffix takes \(-M\) to \(-1\). An integral endpoint of a prescribed shortcut word from an integral input forces every indicated parity, so this is an actual signed native path. In particular \(M\) is odd because the suffix begins with an odd departure. Reversing a signed even step doubles the positive magnitude, while reversing a signed odd step sends a magnitude \(y\ge1\) to \((2y+1)/3\le y\). Consequently \(1\le M\le2^\ell\), and under the mirror map \(S(y)=y/2\) on evens, \(S(y)=(3y-1)/2\) on odds, \(M\) reaches 1 with exactly \(\ell\) even departures. For \(j=0\), take the empty suffix at \(Y\) with \(\ell=0,M=1\); the prefix is the complete lower path.

Let \(d\) be the prefix clock. Reading its reverse branch formulas at the formal source \(-M\) gives a negative rational \(-B\). At every reverse step its magnitude stays at least 1, and only the \(d-b\) even inverses can increase it. Rational affine evaluation here does not assert an ordinary signed path for this prefix. The actual positive source has the exact expression

\[
 m=D(n+1)-B,\qquad D=2^{d+\ell+\delta}/3^b,\qquad
 1\le B\le2^{d-b}M\le D(3/2)^b.
\]

If \(D\ge1\), unique factorization and \(b\ge1\) give \(D>1\) and \(D-1\ge3^{-b}\). Since \(m<n\),

\[
 n+1 < \frac{B-1}{D-1}
 \le \frac{D}{D-1}(3/2)^b
 \le (1+3^b)(3/2)^b
 \le 2(9/2)^K .
\]

This contradicts (1). Every relevant visitor therefore supplies a strict coefficient contraction \(D<1\). No convergence or stopping-time bound was used.

## The finite inverse-word count

Fix \(\ell,\delta,M\) as above and put \(a=\ell+\delta\). Start reversing the actual lower prefix from \(z=2^a(n+1)-M\). Initially its leading coefficient in \(n+1\) equals \(2^a\ge1\). Stop at the **first** reverse prefix of length \(d'\), with \(b'\) odd inverses, for which \(D'=2^{a+d'}/3^{b'}<1\). The preceding extraction guarantees that the stop occurs. It has \(1\le b'\le b\le K\).

The point reached by this shorter reversal is one of the original positive ordinary states. Reversing the same formal branch formulas at \(-M\) gives magnitude \(B'\ge1\), so that point equals \(D'(n+1)-B'<n\). The remaining original path to \(Y\) goes through the very same \(z\) and the same signed-suffix parameter \(M\). Thus taking the first crossing preserves a genuine smaller visitor.

For any fixed reverse word, the existence of this integer source selects at most one residue of \(n\bmod3^{b'}\). Indeed the defining affine equality has coefficient \(2^{a+d'}\) on \(n\) and denominator \(3^{b'}\). That binary coefficient is invertible modulo \(3^{b'}\). Every such residue occupies exactly \(3^{K-b'}\) classes modulo \(3^K\). We use a union bound across different words, parameters and grades. Coinciding or nested ternary cylinders simply make the bound less sharp.

For a fixed starting exponent \(a\), the reverse words stopped at their first strict contraction form a prefix-free set. In a binary tree assigning branch probabilities \(3/4\) to an odd inverse and \(1/4\) to an even inverse, a word of length \(d'\) and grade \(b'\) has weight \(3^{b'}4^{-d'}\). The sum of weights of prefix-free words is at most one, since their descendant cylinders at any common terminal depth are disjoint. Here every relevant depth is finite, since \(2^{a+d'}<3^K\). For each stopped word,

\[
           3^{-b'}=4^{-a}(D')^2\,3^{b'}4^{-d'}\le4^{-a}3^{b'}4^{-d'}.
\]

Therefore at fixed \((\ell,\delta,M)\) the fraction of potentially productive ternary classes is at most \(4^{-\ell-\delta}\). This is the stopped squared-gain/Kraft bound from Weaver, adapted here to the coarse source conditioning and explicit scaled height comparison.

If \(z\equiv0\bmod3\), it has only the ordinary inverse \(2z\), and every repeated doubling remains divisible by three. It has no inverse history with a positive odd count. If \(z\equiv1\bmod3\), its first inverse must be even, since \((2z-1)/3\) is nonintegral. Restart the first-crossing count at \(2z=2^{a+1}(n+1)-2M\). This forced first step cannot cross below one and spends no odd departure. The same cylinder argument now bounds the fraction by \(4^{-a-1}\), without an extra ternary digit or an additional restriction on \(K\).

## Summing all scales

Restrict attention to the one-third of ternary source residues with \(3\mid n\). Then \(z\equiv2^{\ell+\delta}-M\bmod3\). The mirror first-hit sets through three even departures are easy to check by reversing from 1. Omit the stationary odd inverse from 1. One even gives 2, two give 4 and its odd predecessor 3, and three give 8 and 6, neither with an integral odd predecessor. Thus the only **odd** magnitudes for \(\ell=0,1,2,3\) are, respectively, \(\{1\},\varnothing,\{3\},\varnothing\).

* At \(\ell=0,M=1\), even \(\delta\) gives \(z\equiv0\), while odd \(\delta\) gives \(z\equiv1\), forcing an initial even inverse. The total fraction removed is at most \(\sum_{\delta\ {\rm odd}}4^{-\delta-1}=1/15\).
* At \(\ell=2,M=3\), even \(\delta\) gives \(z\equiv1\), while odd \(\delta\) gives \(z\equiv2\). Summing \(4^{-2-\delta-1}\) on even scales and \(4^{-2-\delta}\) on odd scales costs at most \(1/30\).
* At every \(\ell\ge4\) there are at most \(2^{\ell-1}\) odd \(M\) in \([1,2^\ell]\). The total cost over all these \(\ell\) and all \(\delta\ge0\) is at most \(\sum_{\ell\ge4}2^{\ell-1}4^{-\ell}\sum_{\delta\ge0}4^{-\delta}=1/12\).

These fractions use the measure of the full ternary space throughout. Removing the union from \(3\mathbb Z_3\) leaves at least \(1/3-1/15-1/30-1/12=3/20\). To compute an explicit \(F_K\), enumerate only first crossings with \(b'\le K\), \(\ell+\delta+d'<K\log_2 3\), using the stated supersets of signed magnitudes if desired. The complement of their union inside the zero residue modulo three has the required size. There is no limiting process in the finite-class statement.

## A common set exceeding one quarter of all ternary residues

A second count allows both source residues \(0,1\bmod3\) at once. Their initial mass is \(2/3\). For \(\ell=0,M=1\) and fixed \(\delta\), the two possible values of \(z=2^\delta(n+1)-1\bmod3\) are 0 and 1. The zero case cannot cross. In the unit case the first odd inverse must be preceded by an odd number of even inverses, because repeated inverse \(E\)'s alternate the unit residue and the odd inverse requires residue 2. Every first-crossing word has a first odd inverse. Under the same biased tree law, the mass of words with this first-odd parity is at most
\[
       (3/4)\sum_{r\ge0}(1/4)^{2r+1}=1/5.
\]
Hence all scales at \(\ell=0\) remove at most \(4/15\) of the full ternary space. No extra factor for choosing the unit-producing source residue is needed: the individual ternary cylinders already impose that condition.

At \(\ell=2\) the sole odd magnitude 3 costs at most \((4/3)4^{-2}=1/12\), and \(\ell=1,3\) have none. At \(\ell=4\), the signed inverse tree continues from 6 or 8 by an even inverse to 12 or 16. The only further integral odd chain is \(16\mapsto11\), and 11 has no integral odd predecessor. Thus the sole odd magnitude is 11, contributing at most \(1/192\) over all scales. The geometric sum starting at \(\ell=5\) costs at most \(1/24\). The resulting set has relative size at least
\[
       \frac23-\frac4{15}-\frac1{12}-\frac1{192}-\frac1{24}
                     =\frac{259}{960}>\frac14 .
\]
This set and the \(3/20\) set inside the zero class can both be taken from the same exact finite complement of all potentially productive words. At every precision \(K\), that complement has at least \((259/960)3^K\) total classes and includes at least \((3/20)3^K\) classes congruent to zero. Consequently at least \((259/1920-o(1))N\) actual **odd** starts in every shell \([N,2N)\) have the stated logarithmic excess-price lower bound.

The finite exact enumeration in `scale_residues.py` tests the union for \(1\le K\le14\). It prunes a reverse prefix only when even all remaining permitted odd inverses cannot make its coefficient less than one. For \(K=14\) the complement contains 1,421,629 zero classes and 898,010 one classes out of 4,782,969 total ternary classes, with no two classes. Distinct fixed prefix costs and scales can produce the same residue. The program computes their union. The universal lower bounds use the preceding proof instead of extrapolating these controls. [Finite controls](SCALE_COUNTS.txt)

## Ordinary integers and postpeak words

Taking \(K=\lfloor\log_{9/2}(N/2)\rfloor\) in \([N,2N)\) satisfies (1). Since \(3^K=O(N^{\log_{9/2}3})=o(N)\), counting odd members of the surviving classes gives at least \((3/40-o(1))N\) ordinary integers in each such shell. Every smaller visitor to the \(i\)-th shortcut of each of these starts uses more than \(i+K\) odds throughout the entire initial odd run. Prescribing \(j\) initial odds instead of just one gives at least \((3/20-o(1))N/2^j\) representatives whenever \(2^j3^K=o(N)\). These numerical witnesses can be certified entirely from finite ternary classes. They assert a price lower bound whether a higher-cost visitor exists or not.

For the maximal-postpeak statement, discounts are excluded by the checked exact word criterion. If a competing grade is \(H+f+b\) with \(0\le b\le K\), `paid_peak` returns an equally long same-offset word of weight \(u\) and an actual earlier visit to \(3^{H+f-u}v-1\) with \(H+f-u+b\) odds. Maximality gives \(\delta=f-u\ge0\). This is the scaled ramp in the theorem with \(j=H+\delta\). Protection for the common \(F_K\) gives the contradiction. The condition \(H\ge21q+9K+3\) applies here, not in the standalone scaled-ramp estimate.

## Comparison with earlier results

Weaver's Paper 178/v1, *The first meeting with a smaller Collatz orbit*, §2, (3), and §7, Theorem 4, (5)–(6), already gives the stopped squared-gain argument, the pure-ramp signed origins \(2^\ell(n+1)-M\), and the stronger pure-ramp limiting protection proportion \(p_\infty>0.510269713938\). That fixed-ramp natural-density protection covers every visitor cost. The present calculation does not improve that pure-ramp proportion. It supplies a simultaneous coarse-modulus lower bound on one common source set for every additional binary scale, an explicit pointwise height threshold at finite ternary precision, and a transfer to arbitrary maximal postpeak words through the new even-count cone. [Paper 178/v1](https://rstation.ai/problems/collatz/papers/178/v1)

PR201 at `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`, `research/six-hour-20261127/escape/UNRESTRICTED_VISITORS.md`, conditions on \(3^{128}\mid n\) to obtain a relative proportion above \(0.99\) protecting a different language of full odd exponents. Its common ternary event (3) already bounds every shifted site \(2^D n+c\) with odd \(0<c\le5(2^D-1)\), and therefore implicitly covers the scaled signed origins here. The present absolute \(3/20\) estimate requires only \(3\mid n\). Maximal words can include arbitrarily long even coasts, outside that prescribed language.

The finite selector leaves open arbitrary larger-cost visitors and the Collatz conjecture. No passage from positive Haar measure to an all-cost statement at an individual positive integer is used.

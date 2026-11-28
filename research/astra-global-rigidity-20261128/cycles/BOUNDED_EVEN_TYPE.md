# A bounded even-step budget has exactly one seed's worth of clock

For fixed \(k\ge0\), let \(M_k(N)\) be the largest length of a shortcut prefix from any positive \(n\le N\) having at most \(k\) even departures. Then
\[
                           M_k(N)=(1+o_k(1))\log_2 N .                \tag{1}
\]
Thus at each fixed beyond-seed clock \(t=\lfloor\kappa\log_2 N\rfloor\), \(\kappa>1\), the least number of even departures among **all** positive \(n\le N\) tends to infinity. The odd extreme is tested on original unstopped trajectories. The dependence and onset are ineffective. A fixed positive fraction of even departures, as would follow in the negative-counting-exponent sector of the full fair upper R6 bound, remains open here.

The lower bound uses \(n=2^a-1\) with \(a=\lfloor\log_2(N+1)\rfloor\), whose first \(a\) departures are odd. The same identity shows any ordinary positive source eventually has another even departure after any supplied time: an all-odd run of length \(b\) from \(x\) requires \(2^b\mid x+1\). Thus each \(M_k(N)\) exists and bounded source values cannot occur along any sequence of arbitrarily long prefixes with this fixed budget.

For the upper bound suppose along a sequence \(t\to\infty\) that \(\log_2(n+1)\le(1-\eta)t\), with fixed \(\eta>0\). By taking a subsequence the number of even departures is a fixed \(j\le k\). Put \(q=t-j\), and list the even dates \(0\le b_1<\cdots<b_j<t\). Let \(q_i=b_i-(i-1)\) be the odd count strictly before \(b_i\). The ordinary shifted trajectory satisfies \(2(Tx+1)=3(x+1)\) on odd departures and \(2(Tx+1)=(x+1)+1\) on even departures. Composition gives positive integer coordinates
\[
 X_0=3^q(n+1),\qquad X_i=2^{b_i}3^{q-q_i},\qquad
 X_0+\sum_{i=1}^j X_i=2^t(T^tn+1).                                  \tag{2}
\]
In particular \(X_i/X_0=3^{i-1}(2/3)^{b_i}/(n+1)\le3^k/(n+1)\to0\), since bounded seeds have already been excluded. All coordinates are at most \(2^{Ct}\) for an absolute \(C\) for large \(t\).

Use the rational fixed-place Subspace Theorem with \(S=\{\infty,2,3\}\). More generally suppose a current vector consists of \(X_0\) and any subcollection of the other positive coordinates, with a fixed rational linear form \(B=X_0+\sum c_iX_i\) equal to the full left side of (2) along the subsequence. At infinity and at three use the coordinate forms. At two use \(B\) in place of \(X_0\), keeping the other coordinate forms. These systems are independent, and every evaluated form is nonzero. Their product of absolute values is
\[
 X_0|X_0|_3 |B|_2\prod_{i\ge1}X_i|X_i|_2|X_i|_3
 \le (n+1)2^{-t}\le 2^{-\eta t}.                                     \tag{3}
\]
When at least one of the other coordinates remains, the common integer gcd has primes only in \(\{2,3\}\); dividing by it preserves the product in (3) by the product formula. The primitive maximum norm is at most \(2^{Ct}\), hence (3) is smaller than the negative fixed power \(H^{-\eta/(2C)}\) of that norm for large \(t\). The theorem puts these vectors in finitely many proper rational hyperplanes. At least one contains a subsequence. Its relation cannot have a nonzero coefficient of \(X_0\), by the ratio bound following (2). Eliminate any other coordinate with nonzero coefficient, using that relation. This retains exactly the displayed coefficient one of \(X_0\) in \(B\), and the unchanged positive value of \(B\) even if a new coefficient is negative. Repeat at lower dimension. At dimension two there is no rational hyperplane relation among the sole remaining positive coordinate alone. Equivalently, if no other coordinate remains, the exact form is \(B=X_0\), and \(2^t\mid X_0\) forces \(2^t\mid n+1\), contradicting its size. This completes the proof, including \(j=0\). [Schlickewei, rational fixed-place Subspace Theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Varjú, Theorem 5, rational statement](https://arxiv.org/pdf/2104.04367v2)

The critical difference from an arbitrary sparse signed expression is the positivity of the supplied ordinary seed. It makes its marked coordinate exceed every pure \(S\)-unit carry by a factor tending to infinity for fixed \(k\). This remains true under each exceptional-hyperplane reduction. It does not give a uniform theorem with a linearly growing number of coordinates. For context, the real-source compression in PR213 gives an entropy gain at every fixed large odd fraction with a dimension loss, and the R6 lower-edge result treats a different regime with many positive witnesses. [PR213, higher odd fractions](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/LINEAR_NATIVE_SOURCE_LOSS.md) · [Lower edge](NATIVE_LOWER_TYPE.md).

## Verification scope

Root independently checked the marked-coordinate product, preservation of its coefficient under each exceptional-hyperplane reduction, and the S-unit common-divisor normalization. The rational S-adic theorem was read in Varjú’s primary Theorem 5; the original 1977 DOI was inaccessible in this session. The Subspace Theorem is an external mathematical premise, not a new Lean theorem.

# A Wiener law on arbitrarily short translated populations of ordinary multipliers

Choose \(x\) uniformly from an arbitrary interval of \(N\) consecutive positive integers and put \(t=\lfloor\log_2N\rfloor\). Choose \(m=m_t\to\infty\), positive odd \(A=A_t\) and positive even \(D=D_t\) with \(v_2(D)=o(\sqrt t)\). Form
\[
         a_i=A+Di,\qquad y_i=a_i x+b_i,\qquad 0\le i<m,
\]
where the \(b_i\) are arbitrary individual integers such that every arm is positive on the sampling interval. The magnitudes of \(A,D,b_i\) and the sampling-interval origin are unrestricted. In particular \(m_t\) can tend to infinity arbitrarily slowly.

**Proposed theorem.** Let \(\gamma=\log_23,\ b=1-\gamma/2\), and let \(Y_i\) be the linearly interpolated actual path
\[
        Y_i(k/t)=\frac{\log_2T^k y_i-\log_2 y_i+bk}{\gamma\sqrt t},
              \qquad 0\le k\le t .
\]
The uniform empirical measure \(m^{-1}\sum_i\delta_{Y_i}\) converges weakly in probability to Wiener measure of variance rate \(1/4\). The largest proportion of these arms sharing an actual numerical endpoint at time \(t\) tends to zero in probability. These conclusions hold along every sequence of the indicated progressions and interval placements. For pure multipliers \(y_i=a_i x\) the Wiener conclusion also holds on every interval of consecutive positive integer multipliers of length tending to infinity, even when it includes even multipliers.

The argument permits an exceptional collection of pairs. It removes these pairs using the arithmetic of differences along the progression. The preceding [moving-height theorem](MOVING_MULTIPLIER_PATHS.md) instead gives joint path limits for each prescribed pair when the prime-to-six heights are small.

## A short sum of ternary powers cannot have a linearly large binary valuation

Fix \(s,C\) and let \(B\to\infty\). Consider at most \(s\) terms \(u_i3^{h_i}\), with integer exponents \(|h_i|\le CB\) and nonzero integer coefficients \(\max_i\log(2+|u_i|)=o(B)\). If their sum is nonzero, then
\[
                       v_2\Big(\sum_i u_i3^{h_i}\Big)=o(B)               \tag{1}
\]
in the upper-bound sense. This is an ineffective, uniform sequential statement, allowing all coefficients and exponents to move.

To prove it suppose the valuation exceeds \(cB\) on a sequence, for some fixed \(c>0\). Multiplying by a common three-power translates the exponents into \([0,2CB]\), preserving the valuation. Pass to a fixed number \(s'\) of terms and induct on that number. For one term the bound is immediate. For two or more set \(z_i=u_i3^{h_i}\) after translation, and use the rational Subspace Theorem with places \(\infty,2,3\). At infinity and three take all coordinate forms. At two replace the first coordinate form by the sum. The forms are independent at each place. The product of all their values in the three norms is at most
\[
               \prod_i |u_i| \cdot 2^{-cB+v_2(u_1)}
                       =\exp[-cB\log2+o(B)] .
\]
Clear the common positive integer gcd of the vector. This multiplies the product by at most one, by the product formula at the three selected places. The primitive height is at most \(\exp(O_C(B))\). Thus the product beats a fixed negative power of that height. The Subspace Theorem gives finitely many proper rational subspaces, and bounded primitive vectors also lie on finitely many rational lines. Pass to a fixed nonzero rational relation \(\sum l_i z_i=0\). Clear the denominators of its coefficients and choose \(l_k\ne0\). The integer combination \(\sum_{i\ne k}(l_k-l_i)z_i=l_k\sum_i z_i\) is still nonzero and has valuation at least \(cB\). Discard zero terms. The coefficients still have logarithmic size \(o(B)\) and there are fewer terms, a contradiction. This proves (1). [Schlickewei, original Subspace Theorem](https://www.numdam.org/item/CM_1992__82_3_245_0/) · [Evertse, Theorem 1.1, primitive normalization](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf) · [Related fixed-form argument](POWERED_WORD_HEIGHT.md)

## Counting the exceptional pairs on a short progression

First suppose \(m\le\lceil\sqrt t\rceil\) and set \(B=\sqrt t\). For fixed \(\varepsilon,R>0\) call \(i,j\) a bad pair if \(i\ne j\) and some integer \(|h_j|\le RB\) satisfies
\[
                         v_2(a_j/a_i-3^{h_j})\ge\varepsilon B.            \tag{2}
\]
Treat exact equality as infinite valuation. Membership is symmetric by inversion. Choose one admissible exponent for each bad neighbor at the fixed vertex \(i\). Put \(d_j=j-i\). The congruences are
\[
                    Dd_j\equiv a_i(3^{h_j}-1)\pmod{2^{\lceil\varepsilon B\rceil}}.
\]
No neighbor can have \(h_j=0\), since \(v_2(Dd_j)=o(B)\). Two different neighbors cannot have the same \(h_j\) for the same reason. For any two bad neighbors \(j,k\), eliminate \(a_i\) and cancel \(D\) to get
\[
 v_2\{d_j3^{h_k}-d_k3^{h_j}+d_k-d_j\}
               \ge\varepsilon B-v_2(D).
\]
All three coefficients have size at most \(2m\), and both exponents have size \(O_R(B)\). Consequently (1) forces **exact rational equality** for every such pair of neighbors at all sufficiently large \(t\). Uniformity follows by choosing a violating pair along a subsequence if necessary. For fixed \(\varepsilon,R\) this imposes no effective onset.

If there are at least two bad neighbors, there is therefore a single nonzero rational \(u\) with
\[
                       d_j=u(3^{h_j}-1)
\]
for all of them. Order the distinct \(h_j\) increasingly. The values \(|u|3^{h_j}\) have integer nonzero differences in absolute value and lie in an interval of length at most \(2m\). The second value is at least one, and successive values increase by a factor of at least three. Hence there are at most \(2+\log_3(2m+1)\) of them. This bounds the maximum degree of the bad-pair graph, including vertices with zero or one neighbor. The probability that two independent uniform indices coincide or form a bad pair is \(O(\log(2m)/m)\). In particular, a typical pair avoids (2) for every fixed \(R,\varepsilon\) in the sequential in-probability sense.

## Raw occupations at the random pair

Here is the deterministic criterion used to pass from the graph estimate to trajectories. Let \(\alpha_t\) be any sequence of odd dyadic units such that for every fixed \(R>0\),
\[
             B^{-1}\max_{h\in\mathbb Z,\,|h|\le RB}v_2(\alpha_t3^h-1)
                         \longrightarrow 0,\qquad B=\sqrt t.              \tag{3}
\]
With level zero initially and **any** initial dyadic offset, the fraction of native raw dates with odd offset tends to one half in probability. The conclusion also holds along every deterministic positive fraction of the horizon. As in the [compact-kernel proof](INDEPENDENT_MULTIPLIER_PATHS.md), pass to a convergent subsequence \(\alpha_t\to\alpha\); every random limit of raw occupations is stationary for \(P_\alpha\). Only an atom at a solution of \(\alpha3^{s_*}=1\) could differ from product Haar. In this coset the moving levels \(s_{*,t}\) converge to \(s_*\).

To exclude the atom, stop the embedded direction walk on leaving \(|h|\le RB\). The chance of such an exit through native time \(t\) is \(O(e^{-cR^2})\) for large fixed \(R\), since the direction signs are independent and fair, and there are at most \(t\) of them. If an unreachable or never-exited exact level occurs outside this region it has no effect before the exit. Inside the region every conditional holding mean is bounded by \(v_2(\alpha_t3^h-1)+2\). For a fixed precision \(r\ge1\), the sum of these bounds over the moving precision-\(r\) level class on each \(B\)-sized block is \(O((r+1)B2^{-r}+r)+o_R(B)\), by (3) and one candidate residue at every finer precision. The simple-walk Gaussian local-time bound, summed over the blocks, gives an expected native proportion bounded in the limit by \(C(r+1)2^{-r}+O(e^{-cR^2})\), with the first constant independent of \(R\). First pass to the occupation limit, then send \(R,r\) to infinity. This excludes the stationary atom and proves the criterion. If some moving \(\alpha_t\) is an exact three-power, (3) places its exact integer level outside every fixed \(RB\) eventually. The stopped proof covers this situation too.

For a uniform distinct pair let \(\alpha_t=a_j/a_i\). Multiplication by a dyadic unit preserves the valuation, so avoiding (2) is exactly the needed truncated upper bound in (3), with the exponent sign reversed. For each fixed integer \(R\), the left side of (3) tends to zero in probability over the indices. From any subsequence extract a further one on which (3) holds almost surely for all integer \(R\), using a common probability space for the independent index draws and diagonal extraction. Conditional on the indices, the starting raw offset \(b_j-(a_j/a_i)b_i\) is dyadically integral and can be arbitrary. Apply the deterministic criterion. The exact normalized cross bracket of the two grade paths tends to zero uniformly in time, by testing at a finite time mesh. Each diagonal bracket has rate \(1/4\). Martingale convergence yields two independent Brownian motions for the pair. The argument works for any fixed number of independently sampled indices by discarding all bad edges between them.

## Actual heights and actual endpoint collisions

The shortened-word transfer at \(t-\lceil2\log_2(t+2)\rceil\) works for all these arms at once because each slope is odd. The full-horizon error in normalized grades is \(O(\log t/\sqrt t)\). For each arm its own initial value \(y_i\) is at least \(2^{(1-\epsilon)t}\) except on an \(O(2^{-\epsilon t})\) fraction of the interval, uniformly in \(i\) and the coefficients: successive positive input values give positive integers at increasing separation at least one. The half-time odd-grade bound and exact correction estimate in the [release theorem](DYADIC_MULTIPLIER_RELEASE.md) now turn the grade limit into the centered ordinary log-height limit. It is enough to apply these statements to the fixed number of sampled indices. The random-index first and second moments, and tightness of the one-arm laws, prove convergence in probability of the empirical path measures.

Let \(X\) be the right endpoint of the input interval. On its final \(1-\eta\) fraction, for any fixed \(0<\eta<1\) and sufficiently large \(N\), one has
\[
       \tfrac12\eta(a_iX+b_i)\le a_ix+b_i\le a_iX+b_i
\]
simultaneously for all \(i\), by positivity and linear interpolation between interval endpoints. Conditional on a tested good index pair, its initial log ratio therefore differs from the deterministic log ratio at \(X\) by \(O(\log(2/\eta))\) outside a fraction at most \(\eta+O(1/N)\). If the two terminal values agree, \(Y_i(1)-Y_j(1)\) must consequently be within \(O_\eta(t^{-1/2})\) of the negative normalized log ratio at \(X\). Under (3) this random variable converges to a centered normal of variance \(1/2\). The probability of such a shrinking interval tends to zero uniformly in its deterministic center, by tightness and continuity of that normal law. Send \(\eta\downarrow0\) and average over the index draws as above. The resulting coincidence probability is the expectation of the sum of squared endpoint-fibre masses, which bounds the expected squared largest mass.

## Removing the restriction on progression length

If \(m>\lceil\sqrt t\rceil\), partition the progression into contiguous blocks whose lengths are between \(\lfloor\sqrt t/2\rfloor\) and \(\lceil\sqrt t\rceil\) for large \(t\). Every such block satisfies the preceding results uniformly in its translated origin and offsets: a sequence of worst blocks would itself be an admissible sequence. The complete empirical measure is their weighted average. For each bounded continuous test, its expected absolute deviation from the Wiener integral is bounded by the maximum for those blocks. Tightness again follows from the one-arm laws. Each full-population endpoint fibre has mass at most the same weighted average of the individual blocks' largest fibre masses, whose expectation tends to zero uniformly. This proves both claims for arbitrary \(m\).

For an interval of unrestricted consecutive multipliers with zero offsets, split by their exact binary valuation \(r\). For each fixed \(r\), the divided multipliers are consecutive positive odd integers in a block whose size tends to infinity. The first \(r\) ordinary steps merely remove their common \(2^r\), producing the original odd-multiplier trajectories with a fixed clock shift and \(O(r/\sqrt t)\) error in the normalized, own-source-centered log heights. The portion with \(r>r_0\) has mass bounded by \(2^{-r_0}+O(1/m)\), uniformly in the interval origin. Letting \(r_0\to\infty\) proves the stated Wiener conclusion. The sampled integer can be common to all the arms; it is never replaced by independent ordinary inputs.

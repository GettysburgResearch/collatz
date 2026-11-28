# Sparse rank separations between the low and high odd states are impossible above width four

**Proposed written theorem.** Use the odd minimum \(m\), maximum \(X\), primitive odd period \(p\), and total division exponent \(A\) of a positive **ordinary** cycle. Write \(\gamma=\log_2 3\), \(e=2-\gamma\). Fix \(4\le R\le4.37\), suppose \(X/m\le R\), and set
\[
 \omega=\log_2(R/4),\quad F=e-\omega,\qquad
 \Theta_R=\gamma^{-1}D(1-2F,F),\qquad
 D(s,f)=\max\{3(s+\gamma f)/5,\ 9s/16+5\gamma f/8\}.
\]
Use the unique sorted dyadic lifts of the odd phases, with \(Z_{u+p}=2Z_u\) and \(Z_u=c_u x_u\), where \(x_u\) is an actual odd phase and \(c_{u+p}=2c_u\). The choice of first fundamental rank changes only a translation of this infinite ordered array. For \(0\le\kappa\le0.1\) use \(W=\lfloor p^{1-\kappa}/(\log p)^5\rfloor\) and define
\[
 \mathcal D_W=\{1\le d\le W:\ \text{for some }u\in\mathbb Z,\
                   c_u/c_{u+d}\in\{4,1/4\}\}.
\]
Then, along every such sequence with \(p\to\infty\),
\[
 \frac{\log(1+|\mathcal D_W|)}{\log p}\ \ge\
      1-\kappa-\Theta_R\left(\frac{\log m}{\log p}-\kappa\right)-o(1).  \tag{1}
\]
Every counted \(d\) witnesses a pair of actual odd states with larger-to-smaller ratio \(4(1+O_R(W/p+p/m))\). Different \(d\)'s witness distinct unordered state pairs. Thus (1) restricts actual high and low phases of one cycle.

If \(\mu(\gamma)\le3\), the right side of (1) is at least \(1-3\Theta_R-(1-\Theta_R)\kappa-o(1)\). This is positive at sufficiently small \(\kappa\) for every fixed \(4\le R<R_* =4.36867375\ldots\). At \(R=4.2,\ \kappa=0\) the exponent exceeds \(0.02298\). At widths tending to four, the limiting base exponent is \(0.04088656\ldots\), and positive exponents persist up to \(\kappa<0.06010118\ldots\). Consequently, at that limiting width, polynomially many close-to-four pairs are required even when both their smaller members and larger members are restricted to relative \(o(1)\) neighborhoods of \(m\) and \(4m\), respectively. More quantitatively, every growing ordinary sequence satisfies under the same approximation input
\[
                 X/m\ \ge\ 4-O_\kappa(p^{-\kappa})
             \qquad (0<\kappa<0.06010118).                              \tag{2}
\]
For fixed widths above four, (1) excludes the subclass with too few distinct low/high separations. Exclusion of the entire band above four would also require controlling the alternative with many such separations.

## The genuine sorted chart across three grades

Since \(X<9m+2\), the [zero-inversion theorem](RESIDUE_FIBER_INVERSIONS.md) at full denominator one gives **strict physical order on the complete dyadic lift**, with true successor \(N(Z)=3Z+c\) commuting with doubling and permuting the ordered rays. An increasing bijection of this discrete grid translates ranks. Its translation is \(A\) by summing the full-lap windings, and \(\gcd(A,p)=1\) by primitivity. Thus \(Z_{u+A}=3Z_u+c_u\). In particular the comparison visits every base rank on this one sheet.

Fix a sufficiently small \(v>0\), with \(v+\omega<e\), and choose the fundamental octave \([L,2L)\), \(L=2^{2-v}m\). At large periods only tags one, two and four occur there, since \(L>X/2\) and \(2L<8m\). The empirical angle \(\log_2(Z_r/L)\) for \(0\le r<p\) has uniform limiting distribution, because actual native increments modulo one equal \(\gamma+O(1/m)\), \(m\to\infty\), and the irrational rotation has unique invariant probability. Since the labels are sorted, \(\log_2(Z_r/L)=r/p+o(1)\) uniformly. Near the fundamental left endpoint all tags are at most two because \(L<4m\) strictly. Across a right-end wrap, after doubling these left tags are two or four. Accordingly every unwrapped short row \(\{c_{r+j}:0\le j\le p/(\log p)^5\}\), \(0\le r<p\), has tags in \(\{1,2,4\}\). A tag one in such a row requires \(r/p\le v+\omega+o(1)\), since its label is at most \(X\).

For a preliminary height estimate use all \(M_0=1+\lfloor p/(\log p)^5\rfloor\) starts as columns with base ranks \(r_t=tA\bmod p\), over \(n_0=\lceil\log_3(32m)\rceil+4\) consecutive odd dates. A complete tag word distinguishes its initial integer label by the genuine affine recurrence modulo \(2^{\lfloor n_0 A/p\rfloor}\), larger than \(8m\). The unchanged binary/two-or-four rows have at most two choices, the other rows at most three. The fraction of these other rows is at most \(v+\omega+o(1)\) by the uniform moving-rotation average, since \(A/p\to\gamma\). Hence, letting \(v\downarrow0\),
\[
  \liminf\frac{\log m}{\log p}\ge
                \frac{\gamma}{1+\omega\log_2(3/2)}>1.45.              \tag{3}
\]
Here and below the moving-rotation average follows by bounding each fixed nonzero exponential average by \(2/(n|1-\exp(2\pi i h A/p)|)\), then approximating interval indicators. The angular drift bound \(A/p-\gamma\le1/(3m\ln2)\) and the [published two-logarithm estimate](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) also supply a fixed upper bound on \(\log m/\log p\). This legitimizes shrinking fixed phase margins in normalized exponent inequalities.

We now have a quantitative estimate for all ranks. For \(0\le t<p\), sum the exact log increments \(\gamma+\log_2(1+1/(3x_{r_t}))\) of the unfolded grid from rank zero to rank \(tA\). Subtract \(tA/p\) and use the exact octave extension. Since every error per date is \(O(1/m)\),
\[
          \log_2(Z_r/Z_0)=r/p+O(p/m)\qquad(0\le r<p).                  \tag{4}
\]
The same bound on differences covers every wrap. This proves the asserted near-four physical ratio for a counted offset, and \(W<p/2\) makes the short separation unique for any given unordered pair of phases. By (3), \(p/m=o(p^{-0.1})\).

## Every independent set has an integer binary normalization at every date

Form the graph on the offsets \(0,\ldots,W\) by joining two whose positive difference belongs to \(\mathcal D_W\). A greedy independent set \(S\) has size
\[
                    |S|\ge (W+1)/(2|\mathcal D_W|+1).                 \tag{5}
\]
At each temporal base \(r_t\), the tags on columns from \(S\) cannot contain both one and four. Divide the **entire row** by \(s_t=1\) if it contains a one, and by \(s_t=2\) otherwise. Then
\[
 Y_{t,j}=Z_{r_t+j}/s_t \in\mathbb Z,\qquad
 C_{t,j}=c_{r_t+j}/s_t\in\{1,2\},\qquad
 2^{h'_t}Y_{t+1,j}=3Y_{t,j}+C_{t,j},
\]
where \(h'_t=\lfloor(r_t+A)/p\rfloor+\log_2s_{t+1}-\log_2s_t\) is a nonnegative integer. This normalization is allowed to change from date to date. Each true native exponent is \(h'_t+\log_2 C_{t+1,j}-\log_2 C_{t,j}\).

Any pair-sum comparison of these columns has an integer height and signed forcing of absolute value at most two. A nonzero sign persists strictly. Thus a zero at any date forces zero at every date, including after multiplying back by \(s_t\). For two different unordered pairs of offsets their comparison polynomial \(Q\ne0\) has degree at most \(W<p\). The exact one-sheet identity
\[
 \sum_{r=0}^{p-1}2^{-r/p}Q(E)Z_r
       =Q(2^{1/p})\sum_{r=0}^{p-1}2^{-r/p}Z_r
\]
contradicts an everywhere-zero comparison, by Eisenstein for \(T^p-2\). This argument uses four shifts of one ordinary integer array. The [four-sheet rational construction](FOUR_SHEET_PAIR_COLLISIONS.md) explains the importance of this last hypothesis.

By (4), all initial labels on \(S\) lie in an interval of length \(O_R(mW/p+p)\), which is \(O_R(mp^{-\kappa})\) by (3). Take \(n=\lceil\log_3(C_R m p^{-\kappa})\rceil+4\) successive dates with \(C_R\) large enough. The total adjusted winding differs from \(\lfloor nA/p\rfloor\) by at most one. If two unordered pairs of binary tag words have the same coordinate sums, their initial signed height is divisible by \(2^{\sum_{t<n}h'_t}\), exceeding the absolute height by (4) and the chosen constant. Thus the two pairs are identical. This is a genuine binary Sidon code for \(S\).

Keep all \(n\) binary rows. Pair an original winding-one departure with its successor if both scales are two. Original winding ones have asymptotic density \(e\), and their successors have rank fraction at least \(A/p-1\to\gamma-1>v+\omega\), so the successor scale is two. A departure scale of one occurs only in the angle interval \([0,v+\omega+o(1)]\). Hence there are at least \((e-v-\omega-o(1))n\) disjoint usable pairs, up to one terminal edge. On them the adjusted winding is one, so the three configurations \(00,01,11\) are the only possibilities. For any fixed \(f'<e-v-\omega\), keep exactly \(\lfloor f'n\rfloor\) of the pairs and treat all remaining rows as singleton binary coordinates. The [mixed-alphabet Sidon bound](MATCHED_SIDON_CODES.md) gives \(\log_2|S|\le(D(1-2f',f')+o(1))n\). Send \(f'\uparrow e-v-\omega\), then \(v\downarrow0\). Combining this inequality with (5) proves (1); the underlying difference set is defined on the whole dyadic lift and so is independent of the choice of \(v\).

## Numerical thresholds and the lower edge of the band

With \(\mu(\gamma)\le3\), the actual positive clock inequality and its coprime denominator give \(m\le p^{3+o(1)}\). The two affine functions in \(D(1-2F,F)\) are \(3/5-(3/5)(2-\gamma)F\) and \(9/16-(9/8-5\gamma/8)F\). They are both less than \(\gamma/3\) precisely when
\[
 F>\max\left\{\frac{3/5-\gamma/3}{(3/5)(2-\gamma)},\
               \frac{9/16-\gamma/3}{9/8-5\gamma/8}\right\}=:F_* .
\]
Thus \(R_*=4\,2^{e-F_*}\). At \(R=4\), \(1-3\Theta_R=0.0408865663\ldots\) and \((1-3\Theta_R)/(1-\Theta_R)=0.0601011839\ldots\). Along widths approaching four from either side, apply (1) at an arbitrary slightly larger \(R\) before letting it decrease to four. For every \(\kappa\) strictly below this last threshold, (1) forces at least one actual pair with ratio at least \(4(1-O(W/p+p/m))\). To prove (2), it suffices to consider the subsequence with \(X/m\le4\), where the fixed \(R=4\) estimate applies directly. The remaining cycles already exceed four. For the extreme layers when \(X/m\to4\), the smaller state of each counted pair belongs to \([m,(1+o(1))m]\) and its larger state to \([(4-o(1))m,(4+o(1))m]\); (1) counts different pairs even if some individual states repeat among them.

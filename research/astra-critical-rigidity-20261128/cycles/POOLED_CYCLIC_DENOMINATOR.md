# A single logarithmic loss for the complete denominator of a near-octave cycle

**Proposed written theorem.** Let \(m,X,p,A,q,P,r,D\) be as in the [chronological degree theorem](NEAR_OCTAVE_CYCLE_DENOMINATORS.md). Thus \(m,X\) bound the actual odd states of one primitive positive rational cycle, \(q\) is its complete reduced denominator, \(P=p/\gcd(A,p)\), and \(r\) is the least degree of a nonzero rational shift polynomial annihilating its true unfolded sequence \(V_t=2^{E_t}x_t\). Take \(D=\min(r,m)\), or use the explicit \(D=\min(P,m)\). Write \(\gamma=\log_2 3,\ \kappa=\mu_0-1\) for any fixed \(\mu_0\ge\mu(\gamma)\). If \(m\to\infty\), \(X/m\le2^{1+\eta}\) and \(\eta\ll(\log D)^{-\alpha}\) for a fixed \(\alpha>\kappa\), then
\[
                            \log(2q)\gg \frac{D}{\log D}.               \tag{1}
\]
The constants may depend on the fixed width bound and the Diophantine input. In particular the result applies to every \(\alpha>4.116201\) with the classical published bound and to every \(\alpha>2\) with the audited exponent-three input. When \(g=\gcd(A,p)\) equals one or is a prime power, the same conclusion holds with \(D\) replaced by \(\min(p,m)\), since \(r\ge p/4\) in those cases. On these sheets at \(m\gg p\) the upper bound \(\log q=O(p)\) and lower bound (1) differ by at most one power of \(\log p\). No hypothesis on the number of exceptional valuations under a rotation is used. [Reduced-clock degree and single-cell denominator proof](NEAR_OCTAVE_CYCLE_DENOMINATORS.md) · [Classical BLS input](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [Modern logarithm source](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

Two properties of the actual cycle let all consecutive shifts \(0\le s<D/2\) contribute. Their positive log corrections have a common linear approximation, with an error small even at \(s\asymp m\). Different angular cells may then use cyclic calendars with different origins; at any given native date, variation occurs in only a bounded number of those cells. We count the total binary information available to those cells over one shared denominator-dependent duration.

## Uniform local averages of the actual correction

For the physical angle and one-edge correction put
\[
         \theta_t=\{\log_2(x_t/m)\},\qquad
                    d_t=\log_2(1+1/(3x_t)).
\]
They satisfy \(\theta_{t+1}=\theta_t+\gamma+d_t\bmod1\). With \(f(u)=2^{-u}/(3\log 2)\) on \(0\le u<1\), and \(c_*=\int_0^1 f(u)\,du=1/[6(\log2)^2]\), the native states give
\[
                 |m d_t-f(\theta_t)|\le C/m+C\,1_{[0,\eta]}(\theta_t).
                                                                         \tag{2}
\]
In fact \(x_t=m2^{\theta_t}\) unless \(\log_2(x_t/m)\in[1,1+\eta]\); there \(x_t=2m2^{\theta_t}\), with the angle in the indicated exceptional interval. The Taylor remainder of \(m\log_2(1+1/(3x_t))\) is \(O(1/m)\) throughout.

There is a fixed \(\delta>0\) such that for every start \(i\) and every integer \(0\le s\le m\),
\[
       \left|\sum_{t=i}^{i+s-1} d_t-\frac{s c_*}{m}\right|
                  \le C(\eta+m^{-\delta}).                              \tag{3}
\]
Here is an explicit discrepancy proof, uniform over the initial true phase and over the location of the window, including all laps. Choose any \(\kappa'>\kappa\), so \(\|b\gamma\|\ge c b^{-\kappa'}\). Put \(H=\lfloor\sqrt m\rfloor\), and let \(b\le\sqrt H<b'\) be consecutive continued-fraction denominators of \(\gamma\). Then \(b\gg H^{1/(2\kappa')}\), by \(\|b\gamma\|<1/b'\). In any block of \(b\) consecutive iterates of the irrational rotation, compare the points to a translate of the exact grid of its reduced convergent: each phase moves by at most \(1/b'\le1/b\), so the count in any interval differs from \(b\) times its length by \(O(1)\), also across an endpoint of the circle. Splitting \(H\) into these blocks plus a tail gives normalized interval discrepancy \(O(1/b+b/H)\). In a block of \(H\) true phases, the displacement from this irrational orbit is \(O(H/m)\), summing true \(d_t\)'s. Enlarging and shrinking the test interval by that amount proves the normalized discrepancy is \(O(m^{-\delta})\) for some \(\delta>0\). This bounds the average error for \(f\) by the same order, since \(f\) is bounded and monotone on the unit interval (integrate its interval level sets). It bounds the average of the exceptional indicator by \(\eta+O(m^{-\delta})\). Formula (2) now gives a signed \(O((H/m)(\eta+m^{-\delta}))\) error on a complete block. Divide the length \(s\le m\) into such blocks and a remaining segment shorter than \(H\); the remaining contribution is \(O(H/m)\). Decrease \(\delta\) if necessary to obtain (3).

In particular with \(\sigma=\gamma+c_*/m\), the genuine unfolded states satisfy
\[
          \log_2(V_{i+s}/V_i)=s\sigma+O(\eta+m^{-\delta})
                     \qquad(i\in\mathbb Z,\ 0\le s\le m).              \tag{4}
\]
Only \(\gamma\) requires a Diophantine hypothesis. The auxiliary slope \(\sigma\) is used solely to partition finitely many shifts by angle.

## A separate true calendar for each cell

Write \(x=\log D\). Choose constants \(\kappa'>\kappa,\ u>1,\ c\) with \(u\kappa'<c<\alpha\). Let \(L=\lfloor x^u\rfloor,\ b_0=\lceil x^c\rceil\), \(v=1/b_0\) and \(S=\{0,\ldots,\lfloor D/2\rfloor-1\}\). Partition the fractional parts \(\{s\sigma\}\), \(s\in S\), into the \(b_0\) half-open intervals of width \(v\). Write \(C_j\subseteq S\) for the corresponding classes and \(a_j=jv\) for the left endpoints. For \(s\in C_j\), set \(k_s=\lfloor s\sigma\rfloor\), and use
\[
 J=m\sqrt{2^{1+\eta}},\qquad
 F_{i,j}=\lfloor\log_2(V_i/J)+a_j\rfloor,\qquad
         Y_{i,s}=2^{-F_{i,j}-k_s}V_{i+s},\quad
         C_{i,s}=2^{-F_{i,j}-k_s+E_{i+s}}.
\]
Indeed \(Y_{i,s}=C_{i,s}x_{i+s}\). Each multiplier is an integral power of two before any cancellation. From (4),
\[
 \log_2(Y_{i,s}/J)=\{\log_2(V_i/J)+a_j\}
              +(\{s\sigma\}-a_j)+O(\eta+m^{-\delta}).
\]
The total angular error is \(O(v+\eta+m^{-\delta})=O(v)\), since \(D\le m\), \(D\to\infty\), and \(c<\alpha\). The interval \([J,2J)\) stays a fixed relative distance from \(2^{1+\eta}m/2\) and \(4m\). Thus \(2^{1+\eta}m/2<Y_{i,s}<4m\) and \(C_{i,s}\in\{1,2\}\) for all cells and all native dates. For each cell its normalized labels are \(p\)-periodic, since \(F_{i+p,j}=F_{i,j}+A\).

Call a cell active at \(i\) if both its tag values occur there. Its shifted base angle \(\{\log_2(V_i/J)+a_j\}\) must belong to an enlargement by \(O(v)\) of \([\log_2(2m/J),\log_2(2^{1+\eta}m/J)]\), of length \(\eta=O(v)\). All constants are independent of the cell or date. At a fixed \(i\) the full set of shifted base angles is a translate of the regular \(b_0\)-point circle grid, so **at most \(C\) cells are active at any date**, for an absolute constant at all sufficiently large \(m\). In each fixed cell two active rows must be at least \(L\) native dates apart: for \(1\le t<L\), the true angle shift differs from \(t\gamma\) by \(O(L/m)\), whereas
\[
                        v+L/m=o(L^{-\kappa'}),\qquad
                     \|t\gamma\|\gg_{\kappa'} L^{-\kappa'} .
\]
These two conclusions concern different indices; the first counts cells across an actual row, the second counts times within one cell.

## Summing the capacities of the actual cell codes

Take a single common order \(h=|S|\) and duration \(n=\lceil\log_3(64hqm)\rceil+4\). We have \(h<3^L\) for large \(D\). For any fixed nonempty cell, two different \(h\)-term multisets with equal label sums at date zero would yield the nonzero rational polynomial \(\sum_{s\in C_j} c_s 2^{-k_s}S_{\rm sh}^{\,s}\), in the chronological shift \(S_{\rm sh}\). Its degree is \(<D/2\le r\), even when two offsets have the same cell or the same fractional phase. Writing \(H_i=\sum c_sY_{i,s}\), \(d_i=\sum c_sC_{i,s}\) for the signed difference, its complete native equation is
\[
  2^{F_{i+1,j}-F_{i,j}}H_{i+1}=3H_i+d_i,\qquad
                           qH_i\in\mathbb Z,\quad |d_i|\le h .
\]
At an active row the preceding \(L-1\) inactive edges give \(3^{L-1}\mid qH_i\); hence if \(H_{i+1}=0\) then \(3^L\mid qd_i\). This forces \(d_i=H_i=0\) since \(3\nmid q\) and \(h<3^L\). At an inactive row the forcing already vanishes. Induct backwards over the true period: one equality forces the polynomial to annihilate \(V\) at every date, contradicting its degree. This proves multiset injectivity for the actual labels in every cell.

Use its true binary tags (subtracting one) over the same \(n\) consecutive edges beginning at zero. Equal \(h\)-sums of coordinate words give \(2^{F_{n,j}-F_{0,j}}\mid qH_0\), since the homogeneous native recurrence holds on all \(n\) dates. This power is at least \(3^n/2\), also when the coding interval wraps arbitrarily many times. The complete integer \(qH_0\) has absolute value at most \(4hqm\), so the initial physical sums agree. Thus every cell word code is \(B_h\). Its individual labels and words are distinct by the same argument, or by padding individual comparisons with any repeated member of the cell.

Let \(K_j=|C_j|\) and \(k_j\) be the number of its active dates in the common coding window. In each nonempty cell designate one index as a reference. For each subset of its other \(K_j-1\) indices, take each chosen word once and pad with enough copies of the reference to reach exactly \(h\) terms. This is possible since \(K_j\le h\). The resulting \(2^{K_j-1}\) multisets are different, hence have different coordinatewise sums. Inactive coordinates are constant, and each active sum has at most \(h+1\) choices. Therefore
\[
        \sum_{j:K_j>0}(K_j-1)\log 2
                   \le \log(h+1)\sum_j k_j
                   \le C n\log(h+1).
\]
The left side is at least \((|S|-b_0)\log 2\gg D\). This gives \(n\gg D/\log D\). Finally the true clock implies \(\log m=O(\log D)\), as proved in the chronological degree theorem, and \(\log h=O(\log D)\). Subtracting these costs from \(n\) proves (1) for the original complete denominator. No global ordering between different cells or different rational sheets was assumed.

# A three-letter observable already violates the fair upper bound beyond every seed horizon

Use actual shortcut digits \(b_i(n)=T^i(n)\bmod2\). For \(t\ge3\) put
\[
  M_t(n)=\sum_{i=0}^{t-3}1_{\{b_i(n)\ne b_{i+2}(n)\}} .
\]
For any fixed \(\kappa>1\), with \(L=\log_2 N\), \(t=\lfloor\kappa L\rfloor\), there are constants \(p\in(0,1/2)\), \(c>0\) such that for all large \(N\),
\[
 \#\{N/2<n\le N: M_t(n)\le p(t-2)\}\ \ge N^{c-o(1)},
 \qquad 0<1-\kappa(1-H_2(p))<c.
\]
Under fair independent parity digits, \(M_t\) is exactly binomial with \(t-2\) fair trials. Thus the complete unstopped trajectories violate its fair lower-tail **upper** bound by a fixed positive counting exponent. Both the true cohort and the predicted count are polynomial in \(N\). This disproves a full local-word-statistics strengthening of R6 for every \(\kappa>1\), while the book's stated single-letter parity-count upper bound remains open in general. [Polson–Sokolov, R6 at its book source pin](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex#L783-L785)

Indeed, given \(b_0,b_1\), the \(t-2\) disagreement bits determine all remaining \(b_i\) successively by XOR, so the fair vector is uniform on the full disagreement cube. On a full ordinary binary residue period, the same assertion follows from the parity bijection.

Take \(q=\lfloor cL\rfloor\). Beginning with the odd root one, take \(q\) accelerated inverse steps \(y\mapsto (2^e y-1)/3\). At each encountered odd unit exactly two \(e\in\{3,\ldots,8\}\) yield integral odd unit children, since two generates the six units modulo nine. Each child strictly exceeds its parent by \(e\ge3\). Forward iteration recovers every choice up to the first visit to one. Thus there are \(2^q\) distinct odd sources \(u\), all of height at most \(2^{8q}\), and each reaches one within \(8q\) native steps. Take \(c<1/8\) and lift each to \(n=2^k u\), \(k=\lfloor\log_2(N/u)\rfloor\). These \(n\) are distinct and lie in \((N/2,N]\). Their infinite native digits are an initial constant zero word, at most \(8q\) other digits, and then \(1,0,1,0,\ldots\). A discrepancy can occur only across this middle interval or its two boundaries, so \(M_t(n)\le8q+4\) for every \(t\), including cuts inside it. This population and its bound are elementary and use only terminating inputs.

Let \(p_*\in(0,1/2)\) be the unique solution \(1-\kappa(1-H_2(p_*))=0\). Choose \(0<c<\min(1/8,\kappa p_*/16)\). By continuity and strict increase, choose \(p>p_*\) so close that \(0<1-\kappa(1-H_2(p))<c\). Then \(8q+4<p(t-2)\) for all large \(N\). The fair Chernoff bound gives the asserted comparison, and Stirling gives the same expected-count exponent for the exact binomial tail. For instance a single source \(2^k\) also has at most two lag-two disagreements, but the construction above gives exponentially many in \(L\) at an interior positive-count threshold.

All constructed sources have initial binary padding and are sampled from the full ordinary octave. The conclusion supplies no upper or lower on the critical return experiment conditional on a true gate, whose starting digit is necessarily odd.

[UnitInverseFork.lean](UnitInverseFork.lean) checks the two legal unit branches and bounded-exponent target uniqueness. [Exact finite controls](check_inverse_population.py) reconstruct the cohorts, actual cuts and fair XOR bijection. The population asymptotics remain the written proof above.

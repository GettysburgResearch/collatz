# What a second use of the interval estimate can establish

Let \(A(k)\) count a set of actual ordinary states in its most populated interval of width \(2^k\). The proofs here split at horizon \(T=k+\lfloor ek\rfloor\) into a high-odd-count group estimated by a tilted symbolic law and a low group injectively mapping to strictly shorter intervals. Permitting small strict margins, the recurrence has the form
\[
 A(k)\le C\,2^{[h-(d-h)e+C'\eta]k}+C k A(\lceil(1-c_\eta)k\rceil).
\]
Here \(h\) is the critical entropy per step of the **unconditioned symbolic family**, and the genuine canonical source concentration is \(2^{-d(T-k)}\). The established estimate on \(A\) can improve control of the second term but leaves the first term unchanged. For any fixed positive high-group exponent \(r\), a sequence of size \(2^{rk}\) is itself compatible with this upper recurrence for a sufficiently large leading constant. Reusing an upper bound on actual states as the entropy of symbolic bridge paths would impose an additional conditional-concentration statement. Restricting a probability distribution to a sparse set selected by its canonical source can concentrate it entirely in one cell.

Even at the idealized dimension \(d=1\), the necessary forward oversampling threshold for a *negative* high-group exponent would be \(e>h/(1-h)\). This threshold is about \(0.4724\) for dimers and \(18.98\) for unrestricted critical binary words. The universal low-group proof uses the additive interval width \((3/2)^T\), and consequently requires \(e<1/\log_2(3/2)-1=0.70951\ldots\). The actual proven dimer precision band is much shallower; the concrete witness takes \(e=10^{-9}\). In the reverse avoid-5 proof the analogous ideal clearance threshold is \(h_5/(1-h_5)=1.6159\ldots\) in the macro exponent \(b=(1+e)k\), and the additive width requires \((4/3)^b<3^k\). These are necessary scale comparisons for these recurrences only.

There is a sharper support obstruction at every precision. A uniform slice of \(N\) words is nonempty, so some cell has mass at least \(1/N\), irrespective of its width. In the fixed-type dimer slice \(N=2^{h_D T+o(T)}\) at criticality. A bound on the *maximum over all positions* of the form \(2^{-dP+o(T)}\) must satisfy \(dP\le h_DT+o(T)\). It cannot give a negative exponent when multiplied back by that same family size. Equality could yield a bounded list, which would still require an arithmetic argument about its individual members. An occupancy upper bound with a strictly positive power allows an isolated orbit throughout.

A distinct check is the nesting of the source constraints: for the first \(j\) actual departures of a fixed word \(w\), its canonical source modulo \(2^j\) is exactly \(r(w)\bmod2^j\). Once a horizon longer than \(\log_2 X\) pins an ordinary source in a specified width-\(X\) interval, its later forward bits are determined. Counting later fresh independent symbolic choices after conditioning on that source is unjustified. A legitimate extra condition is a genuine backward ternary mask at the initial cut as shown in [REVERSE_MASK.md](REVERSE_MASK.md). For a known admissible history, the same masks at subsequent internal cuts are inherited from the concatenated path. Once \(H\) earlier odd steps are inside the word, an \(H\)-step mask check for the later state is already automatic. These statements explain why direct iteration supplies neither a zero exponent nor exclusion of a single orbit.

### Two sharper quantitative limits

The additive bounds in the preceding paragraph are sufficient cutoffs in the published recurrence, not intrinsic horizon limits. At fixed odd count \(q\), moving all zero bits before all one bits maximizes the affine intercept, so
\[
                  C(w)/2^T\le(3/2)^q-1 .
\]
Indeed exchanging adjacent 10 for 01 increases the local intercept from 1 to 2 without changing its multiplier. At the critical low-group boundary \(q\le p_*T\), the error is at most \(2^{(1-p_*)T}\); this suffices for any \(e<p_* /(1-p_*)=1.7095\ldots\). Under no 111, every suffix of length \(l\) contains at most \(2l/3+2\) ones. Each term of \(C/2^T\) is bounded by a constant times \(2^{(2\alpha/3-1)l}\) for its corresponding suffix, so summing the geometric series gives \(C/2^T\ll 2^{(2\alpha/3-1)T}\). This leaves an even larger additive horizon for the dimer and avoid-7 languages. For backwards exponents 1,2, if \(r=s-b\) of the \(b\) exponents are 2, the inverse additive term is
\[
     C/3^b=\tfrac13\sum_{i=0}^{b-1}2^{s_i}/3^i
                 \ll (4/3)^r,
\]
where \(s_i\) is the sum of the first \(i\) exponents. The bound follows by placing all \(r\) twos first and summing the rising and falling geometric series. These refinements do not provide the required canonical concentration at the enlarged horizon.

There is also an exact square-root barrier to the *specific Fourier certificate* used in the small-arc proofs. In a fixed bridge environment, suppose independent chunk measures \(\nu_i\) of total masses \(m_i\) have finite support sizes \(N_i\) in the common discrete quantization group. On its compact dual with probability Haar measure, for all \(q_i\ge2\),
\[
      \|\widehat\nu_i\|_{q_i}\ge \|\widehat\nu_i\|_2
        =\left(\sum_x\nu_i(x)^2\right)^{1/2}\ge m_i/\sqrt{N_i}.
\]
Consequently the product of norms supplied by Hölder, with \(\sum_i1/q_i=1\), can be no smaller than \((\prod_i m_i)/\sqrt{\prod_i N_i}\). If all combinations of permitted local choices concatenate to distinct words from a global source of \(N\) words, then \(\prod_i N_i\le N\) (quantizing can reduce support). Thus this certificate, even with perfect local moment estimates and no rounding cost, is at least \((\prod_i m_i)/\sqrt N\). Further independent probability factors cost no mass. Averaging over bridge environments, or partitioning into good and bad product terms, preserves this floor multiplied by the total mass of the terms estimated in this fashion. In the dimer fixed-composition model the terms with sufficiently many good chunks have mass tending to one.

It follows that an argument which counts \(N\) equiprobable high-type words by multiplying by this position-uniform Hölder certificate cannot certify a list shorter than order \(\sqrt N\), even if every arithmetic separation and mixing constant is improved. For critical dimer words this leaves exponent at least \(h_DT/2+o(T)\) at the level of that certificate. The actual maximum cell mass can of course be much smaller. Removing the barrier would require further information, for example a signed Fourier estimate at the specified location or a direct arithmetic exclusion for the surviving candidates.

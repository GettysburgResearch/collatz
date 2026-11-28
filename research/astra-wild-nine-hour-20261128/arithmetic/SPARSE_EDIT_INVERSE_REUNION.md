# How far inverse Collatz paths must travel to rejoin after a sparse ternary edit

**Proposed written theorem.** Put \(\gamma=\log_2 3\) and
\[
       b=\frac{\log3}{\log(1+1/\sqrt3)}=2.41057812\ldots.
\]
A legal inverse gap is \(I_e(x)=(2^e x-1)/3\), \(e\ge1\), with consecutive states in the ternary units. A word of \(n\) gaps and total \(S\) has odd depth \(n\) and native cost \(S\). Include the empty word with both zero. We study reunion to precision \(W\), meaning equality of the two terminal residues modulo \(3^W\).

1. Fix \(0<c<b\), \(C=\lfloor cW\rfloor\), and any \(h_W=o(W)\). Except for a set of unit roots \(x\) of Haar probability \(e^{-\Omega_c(W)}\), the following holds simultaneously for **every** \(y\) differing from \(x\) in at most \(h_W\) of the first \(W+C\) ternary digits. If two inverse paths from \(x,y\) of combined native cost at most \(C\) rejoin to precision \(W\), their odd depths coincide and their costs coincide. Edits, inserted exponents and stopping times may all depend on the observed root. The same exponential exceptional bound holds when \(x\) is sampled instead from any fixed geometric Syracuse law of **full ternary entropy dimension**, including the critical law.
2. For such a reunion with common depth \(n\) and cost \(S\), suppose \(x,y\) genuinely differ modulo \(3^{W+n}\) and at most \(h\) of their first \(W+n\) digits differ. For **every root**,
\[
                             (h+1)S\ \ge\ \gamma(W-2h)+n .             \tag{1}
\]
In particular, after any single changed digit among the first \(W\), reunion to \(W\)-digit precision costs at least \((\gamma-o(1))W\) in combined native cost at almost every root, uniformly in the location and direction of the change, when no other relevant trit changes. For edits restricted to the initial \(o(W)\) digits, every nonzero resulting displacement needs combined cost at least \((b-o(1))W\) at almost every root. These are lower bounds.
3. For a fixed nonzero **ordinary integer** displacement \(d\), two finite inverse paths from \(x\) and \(x+d\) can meet exactly only if \(x\) is rational. This last exact consequence reflects the already known absence of an integer-translation identity between two forward coding cylinders in PR215. It also follows directly from the arithmetic below.

Part 1 excludes an off-clock repair even if the edit is chosen adversarially from a set of subexponential size. Parts 1–2 exclude a sublinear-cost prefix repair of even one edit that restores a common long tail. They do not compare the costs of different optimal continuations from the two endpoints. For growing \(h=o(W)\), a synchronized repair with \(S=o(W)\) is still possible under (1) when \(hS\) is sufficiently large.

## The unsynchronized congruence

Write \(u=(e_1,\ldots,e_n)\), \(S_i=\sum_{j\le i}e_j\), \(S=S_n\). Define
\[
 B_u=\sum_{i=1}^n3^{i-1}2^{S-S_i},\qquad
 I_u(x)=\frac{2^Sx-B_u}{3^n}.
\]
These are inverse steps from the given root in the displayed order. Empty words have numerator zero. At any fixed \((n,S)\), \(B_u\bmod2^S\) determines the complete word. Indeed the corresponding chronological shortcut word consists of the reversed gaps \(e_n,\ldots,e_1\), each one odd bit followed by its prescribed even bits. Its numerator is \(B_u\), and its unique starting binary residue is \(-3^{-n}B_u\bmod2^S\). Iterating from that residue recovers the complete shortcut word and hence its gaps. For nonempty words,
\[
                  0<B_u/3^n\le 2^S((3/2)^n-1)/3^n < 2^{S-n}.         \tag{2}
\]
Use \(S_i\ge i\) and sum the geometric progression. The bounds needed below also hold for the empty numerator.

Take words \(u,v\) with lengths \(n,m\), totals \(S,T\). Let \(y\equiv x+d\bmod 3^{W+C}\), \(S+T\le C\). Ignoring legality only enlarges the set of possible \(x\). Reunion requires
\[
  (3^m2^S-3^n2^T)x
     \equiv 3^mB_u+3^n2^T d-3^nB_v\pmod {3^{W+n+m}}.                \tag{3}
\]
The reduction uses \(W+C\ge W+m\). For \(n\ne m\), the coefficient has ternary valuation \(\min(n,m)\), so the solutions lie in at most one residue modulo \(3^{W+\max(n,m)}\). For \(n=m,\ S\ne T\), its valuation equals \(n+v_3(2^{|S-T|}-1)\). This last valuation is zero for odd difference, and for even difference equals \(1+v_3(|S-T|/2)\). This follows by factoring \(4^\ell-1\): a positive \(\ell\) prime to three leaves valuation one by its binomial expansion, and every tripling of the exponent adds one by \(a^3-1=(a-1)(a^2+a+1)\) at \(a\equiv1\bmod3\). Hence in all unequal cases the additive Haar probability of (3) is at most
\[
                  3(C+1)\,3^{-W-\max(n,m)}
              \ \le\ 3(C+1)\,3^{-W}3^{-(n+m)/2}.                     \tag{4}
\]
Solubility when the right side of (3) lacks the necessary divisibility is not needed.

Let \(u_0=3^{-1/2}\). Positive compositions give, for \(S\ge1\),
\[
 \sum_{\|u\|=S}3^{-|u|/2}
    =\sum_{n=1}^S\binom{S-1}{n-1}u_0^n
    =u_0(1+u_0)^{S-1}\le (1+u_0)^S .
\]
At \(S=0\) the empty word contributes one. Thus the weighted sum for \(S+T\le C\) is at most \((C+1)^2(1+u_0)^C\). A difference of at most \(h\) ternary digits in \(N=W+C\) positions is represented by
\[
 d=\sum_{j\in J}t_j3^j,\quad |J|\le h,\quad t_j\in\{-2,-1,1,2\}.
\]
Ignoring consistency of the signed edits with \(x\) gives at most \(K(N,h)=\sum_{i=0}^{\min(h,N)}\binom Ni4^i\) displacements. Taking a union in (4) shows that the exceptional event lies in a union of \(N\)-digit cells with additive Haar mass at most
\[
                 3(C+1)^3 K(N,h)\,3^{-W}(1+1/\sqrt3)^C.             \tag{5}
\]
The congruences actually depend on at most \(W+\max(n,m)\le N\) digits of \(x\) after the common power of three on both sides of (3) is divided out. This also verifies that the selected \(N\)-digit displacement suffices. Unit Haar costs a factor at most \(3/2\). At \(C\le cW\) and \(h=o(W)\), \(\log K(N,h)=o(W)\) by the binomial entropy bound, whereas \(\log3-c\log(1+1/\sqrt3)>0\). This proves the Haar assertion.

For the other source laws in part 1, let \(\mu_N\) be the residue law. The [permutation-mixture argument](ROBUST_BRANCH_FIBRES.md) gives, for any \(\varepsilon>0\), an order \(q>1\) such that \(H_q(\mu_N)\ge N(\log_2 3-\varepsilon)\) eventually. If a union of \(N\)-digit cells has additive Haar mass \(a_N\), Hölder’s inequality gives it \(\mu_N\)-mass at most \((a_N 2^{\varepsilon N})^{1-1/q}\). In (5), \(N\le(1+c)W\). Choose \(\varepsilon\) sufficiently small before taking the resulting fixed \(q\). This retains exponential decay under \(\mu_N\). In either law the exceptional probabilities are summable in \(W\), giving the asserted almost-sure consequences via Borel–Cantelli and a countable choice of \(c\uparrow b\). The same finite proportions under Haar apply to uniform ordinary representatives over a complete ternary period. The inverse steps are ordinary Syracuse predecessors on positive odd integer unit roots when the word is legal.

## Equal clocks force gaps in the signed ternary expansion to be short

Assume \(n=m,\ S=T\), with \(x\not\equiv y\bmod3^{W+n}\). The paths cannot use the same word, because their endpoint difference would be \(2^S(x-y)/3^n\). Reduce the signed digit difference to positions below \(W+n\), and write its \(h'\ge1\) nonzero positions as \(j_1<\cdots<j_{h'}\), \(h'\le h\). Put \(j_{h'+1}=W+n\), \(D_i=\sum_{\ell\le i}t_{j_\ell}3^{j_\ell}\), \(D_0=0\), and
\[
                        L_i=2^S D_i+B_u-B_v.
\]
Here every \(L_i\ne0\) because its residue modulo \(2^S\) is \(B_u-B_v\ne0\), by the fixed-clock binary injection. From (3), \(3^{j_{i+1}}\mid L_i\) for \(0\le i\le h'\). In particular \(j_1\le B:=n+(S-n)/\gamma\) by (2). For \(i\ge1\), \(|D_i|<3^{j_i+1}\), so
\[
 3^{j_{i+1}}\le |L_i| \le 2^S 3^{j_i+1}+3^B,\qquad
 j_{i+1}\le\max(j_i+1+S/\gamma,B)+\log_3 2 .
\]
Induction gives \(W+n\le B+h'(2+S/\gamma)\). Rearranging proves (1), also with \(h\ge h'\). The use of every partial displacement prevents cancellation by a handful of widely separated edited digits.

For a single edited trit, (1) yields \(2S\ge\gamma(W-2)+n\). In conjunction with the almost-sure unequal-clock bound, since \(b>\gamma\), this proves the single-edit assertion. For edits all below position \(o(W)\), use the full displacement bound \(|d|\le 3^{o(W)}\) directly. If a synchronous reunion with total cost \(2S\le cW\) held, (2) would give
\[
  0< |2^S d+B_u-B_v|/3^n
       \le 2^S |d|/3^n+2^{S-n}
       \le 2^{cW/2}3^{o(W)}+2^{cW/2}<3^W
\]
for \(c<b<2\gamma\). Nonvanishing for \(u=v\) follows separately from \(d\ne0\). This contradicts (3). For a fixed ordinary integer \(d\), the same size proof applies for large \(W\). In the unequal-clock bound one can include that single integer directly in (5), without a sparse representation or restriction on carries in \(x+d\).

For **exact** equality at a nonzero fixed integer displacement and unequal clocks, (3) becomes an equality in \(\mathbb Q_3\) of integer affine expressions. Its nonzero coefficient forces \(x\in\mathbb Q\). At equal clocks it would require \(2^S d+B_u-B_v=0\), contradicting the binary injection or \(d\ne0\) on identical words. This proves part 3.

**Relationship to existing results.** Weaver’s Paper 118 Lemma 4 uses numerator growth and binary decoding to separate different equal-total words at a single unchanged supplied source with bounded individual exponents. Leen’s proof of noncontraction for the forward transfer of a ternary dipole already separates unequal slopes by the same valuation and equal-clock offsets by binary decoding. It fixes the transfer depth and clock cutoff before sending the perturbed digit to high precision. Here inverse path depths and costs may grow linearly with precision and may be selected after seeing the source and the edit. PR215 proves a stronger qualitative classification of exact affine overlap for the critical measure, including singularity under every nonzero integer translation, and gives nonintegral displacements with positive overlap. Its inverse-cost note exhibits the pair \(-1,-7\) with one changed ternary digit and a linear difference in optimal cost. The new finite estimates address a different question. They are uniform over sparse changes of the observed window, arbitrary legal gap sizes within a **total** budget, and competing words of different clocks. The analytic input occurs only in the extension from Haar to full-dimensional geometric laws. Nothing here implies that independently reoptimized paths must have different limiting costs. [Leen, *Tilted 3-adic Syracuse laws*, Section 7, fixed-power noncontraction proposition](https://doi.org/10.5281/zenodo.23268832) · [Weaver, Paper 118 v1, Lemma 4](https://rstation.ai/problems/collatz/papers/118/v1) · [PR215 exact affine overlaps](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md) · [PR215 critical inverse costs and the one-trit example](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase4/CRITICAL_REVERSE_ENTROPY.md)

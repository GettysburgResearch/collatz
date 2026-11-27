# Clock sums above a height cut and occupation of wide cycles

Let \(m\) and \(p\) be the smallest odd value and least odd period of a hypothetical nontrivial positive Collatz cycle. More than \(p/10{,}000\) of its distinct odd values exceed \(2.08m\). At least two fifths of the values above any threshold \(H\ge32\) have incoming valuation one. In particular more than \(p/25{,}000\) distinct phases both exceed \(2.08m\) and are reached by a one-gap rise. Each is \(2\bmod 3\) by its ordinary incoming equation.

The explicit occupation fraction uses the published minimum and period bounds cited below. The cut inequalities themselves apply to every ordinary path or closed walk without external inputs. Lean proves the clipping and rise bounds, the mixed-window encoding, the cyclic count, and both explicit occupation conclusions at all periods. The separate asymptotic statement for larger thresholds below is a written deduction. [Clock and finite-window proofs](CycleFrontier.lean) · [All-period occupation and ternary-residue proofs](CycleFrontierCounting.lean)

## Clipping the physical trajectory

For a finite actual odd path \(x_0,\ldots,x_k\), write \(2^{e_i}x_{i+1}=3x_i+1\). For an integer \(H>0\), let \(r_+\) and \(s_+\) be the number and sum of incoming valuations with \(x_{i+1}>H\). Let \(r_-,s_-\) use the complementary targets. Then

\[
 H^{r_+}2^{s_+}\max(H,x_k)\le(3H+1)^{r_+}\max(H,x_0),\qquad
 (3H+1)^{r_-}\min(H,x_0)\le H^{r_-}2^{s_-}\min(H,x_k).
\]

For a high target, \(H\,2^{e_i}\max(H,x_{i+1})=H(3x_i+1)\le(3H+1)\max(H,x_i)\). For a low target the maximum can only decrease. Multiplying gives the first inequality. The analogous comparison with the minimum on the low-target edges gives the second. On a closed positive walk the endpoint factors cancel for each cut separately. On any path starting at or below \(H\), the first bound gives \(s_+\le2r_+\) since \(3H+1\le4H\). These estimates place no upper bound on intervening heights. [Lean statements upper_clock, lower_clock, closed_cut and high_gap_budget](CycleFrontier.lean)

If \(H\ge32\), then \((3+1/H)^5\le(97/32)^5<2^8\). On a closed walk this gives \(5s_+\le8r_+\). If \(a\) of the selected valuations equal one, their sum is at least \(2r_+-a\), yielding \(5a\ge2r_+\). The threshold selects the target of each gap. The origin of a complete lap may be chosen arbitrarily. [Lean statement upper_tail_rises](CycleFrontier.lean)

## The effective fraction above \(2.08m\)

Use the consequences \(m\ge10{,}000\), \(p\ge10^{11}\), and \(m^2\le2^{18}p^{29}\). Simons and de Weger's Lemma 12 gives the last inequality after substitution in the exact lap product. Hercher's Corollary 29 and Barina's finite verification give the first two. The substitutions and chosen verification limit are recorded in the earlier width proof. [OrbitAttack.md](OrbitAttack.md) · [Simons and de Weger](https://www.impan.pl/shop/en/publication/transaction/download/product/82263) · [Hercher](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html) · [Barina](https://doi.org/10.1007/s11227-025-07337-0)

Choose \(k\) least with \(2m\le3^k\), so \(3^k<6m\) and \(1000k\le m\). Let \(h\) count the \(p\) distinct phases above \(2.08m\). At most \((k+1)h\) of the \(p\) cyclic window endpoints have a high site somewhere in their preceding \(k\)-gap window. Every other window lies in the band. Its distinct endpoints number at most \(c=109\cdot2^{\lceil k/12\rceil}\), with \(c^{19}\le250^{19}m\) by the earlier terminal count. Thus \(p\le c+(k+1)h\). Combining the numerical inputs gives \(10c<9p\), hence \(p<10(k+1)h\). When \(p\le10^{30}\) the height inequality gives \(k<1000\) and therefore \(p<10{,}000h\). These inequalities and the circular indexing, including \(k>p\), are formalized. [Lean statements cycle_cover, cycle_occupation and finite_occupation](CycleFrontier.lean)

Suppose now \(p\ge10^{30}\) and \(10{,}000h\le p\). Set \(H=\lfloor2.08m\rfloor\). Keep the \(k\)-gap cyclic windows with both endpoints low and at most \(k/1000\) high targets. At most \(2h\) windows lose an endpoint. Summing high-target counts over the \(p\) windows gives exactly \(kh\), so at most \(1000h\) windows exceed the target limit. At least \(g\ge3p/4\) windows remain. Their terminal values are distinct because a cyclic shift permutes the \(p\) phases.

Use the starting-height bin \(b=\lfloor100x_0/m\rfloor\in[100,208]\). At every **low** target \(x_i\), the same possible cumulative clocks as in the narrow-band count satisfy

\[
 b3^i\le208\,2^{S_i},\qquad 100000\,2^{S_i}\le1001(b+1)3^i .
\]

The intermediate targets may exceed the band. Indeed \(\prod_{j<i}(1+1/(3x_j))\le(1+1/(3m))^k\le1001/1000\) uses only the global lower bound \(m\). The remaining inequalities use the start bin and the two bounds on the **current** target. For a fixed bin there are at most two clock slots per index, with two slots at most once per twelve consecutive positions. This slot separation is a statement about those two arithmetic inequalities. It holds on the complete set of indices before any high-target positions are removed. [Finite clock slots and integer separation](OrbitAttack.lean)

For fixed positions of \(r\) high targets, store the cumulative clock at every low target and the incoming gap at each high target. Starting at \(S_0=0\), this reconstructs the whole clock tuple and gap word. The clipped bound gives a sum at most \(2r\) for the \(r\) stored positive gaps. Their partial sums are distinct members of \(\{1,\ldots,2r\}\), giving at most \(4^r\) lists. This includes the empty list at \(r=0\). Each gap word fixes the terminal modulo \(3^k\), and the low terminal interval has width \(1.08m<3^k\). The resulting bound, proved by the Lean theorem \(\mathtt{mixed\_terminal\_count}\), is

\[
 g\le109\,2^{\lceil k/12\rceil} S,\qquad
 S=\sum_{0\le r\le k/1000}\binom kr 4^r .
\]

For \(z=2^{-13}\), the binomial theorem gives \(S\le 2^{13k/1000}(1+1/2048)^k\). The exact inequalities \(2049^{1000}<2\cdot2048^{1000}\) and \(2^{4672}<3^{3000}\) give
\[
 S^{1000}\le2^{14k},\qquad
 g^{16}\le218^{16}3^k<218^{16}\,6m .
\]
For the second comparison use \(16(1/12+14/1000)=4672/3000\) and \(2^{\lceil k/12\rceil}\le2\cdot2^{k/12}\). Squaring and combining \(3p\le4g\) with the published height bound yields \(3^{32}p^3\le4^{32}218^{32}6^2\,2^{18}\), which fails already at \(p=10^{30}\). This proves the claimed all-period fraction; rotating the incoming list by one position gives the associated fraction of ternary residue two in the original list of distinct odd phases. [All-period Lean theorems](CycleFrontierCounting.lean)

## Positive occupation beyond larger cutoffs

The same argument strengthens a width restriction to an occupation restriction. Write \(L=5.1163051\). For fixed \(2<K<2\cdot3^{1/L}\), let \(h_K\) count phases above \(Km\). With natural logarithms and \(H_2(t)=-t\log t-(1-t)\log(1-t)\), every \(0<t<1/2\) satisfying

\[
 \log(K/2)+H_2(t)+t\log4 < \log(3)/L
\]

gives \(\liminf h_K/p\ge t/(1+2t)\) along any sequence of distinct nontrivial cycles. For example \(K=2.4,\ t=1/250\) gives a limiting lower fraction of at least \(1/252\). At every fixed \(K\) below \(2.47904859\ldots\), the strict inequality allows some \(t>0\).

Choose \(k=\lceil\log_3(Km)\rceil\). If \(h_K/p\le d<t/(1+2t)\), a fraction at least \(1-2d-d/t>0\) of the windows have low endpoints and at most \(tk\) high targets. A fixed sufficiently fine starting-phase bin permits at most \(2^{(\log_2 K-1+\eta)k}\) low-target slot assignments, for any fixed \(\eta>0\) and large \(m\). This is the uniform rotation count of PR #209. It uses only the global lower floor to control accumulated affine error and uses the upper cutoff solely at the indices being counted. The same \(4^r\) coding of the high arrivals applies. Summing over high positions costs at most \((k+1)\exp(k[H_2(t)+t\log4])\). Equal gap words again have at most one low terminal. Wu and Wang's Theorem 1 applied to the full lap gives \(\log m\le(L+\epsilon)\log p+O_\epsilon(1)\). Taking \(\eta,\epsilon\) sufficiently small contradicts the positive fraction of retained windows by the displayed strict inequality. Distinct cycles have minima tending to infinity by determinism. This asymptotic statement is a written deduction. [PR #209, fixed-head uniform phase count and source substitution](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/arithmetic/README.md) · [Wu and Wang, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

PR #193 proves an asymptotic fraction above \(2m\) with a stronger fraction at that threshold. PR #209 controls cycles contained entirely in a fixed band. Here the clock sum on high arrivals also controls windows that leave and reenter the band; the maximum height of an excursion can be arbitrary. A wide cycle with these occupation and clock distributions still satisfies the derived necessary conditions. [PR #193, fixed-head occupation proof](https://github.com/GettysburgResearch/collatz/blob/24cdd0e5471d4421716cfce6bd88916f858f994c/research/astra-universal-proof-20261124/critical/CYCLE_OCCUPATION.md)

## Why the phase distribution still permits wide cycles

There are explicit positive rational cycles demonstrating the first obstruction. Put \(\alpha=\log_2 3\). For arbitrarily large integers \(j\), choose \(p\ge j^2\) such that \(1/j\le\lceil p\alpha\rceil-p\alpha\le2/j\), possible by density of the irrational rotation. Let \(A=\lceil p\alpha\rceil,\ s=A-p,\ r=2p-A\), and take \(r\) gaps of one followed by \(s\) gaps of two. Set \(g=3^p/2^A\). The least value and the greatest value \(X\) on its positive rational cycle satisfy

\[
 m=\frac{1+g-2(3/4)^s}{1-g},\qquad X+1=(3/2)^r(m+1),\qquad
 m-1=(3/4)^s(X-1).
\]

These identities follow by iterating \(x+1\) on rises and \(x-1\) on falls. Here \(m\) is of order \(j\); the sequence increases strictly along its first run and decreases strictly along its second. Every rotation has the ordinary affine closing numerator \(\sum_{i<p}3^{p-1-i}2^{S_i}\), which is odd, and denominator \(2^A-3^p\), which is coprime to six. Hence the valuations and ternary classes make sense at all these rational phases.

For each fixed \(K>1\), only \(O_K(1)\) states from either end of these two geometric runs can lie below \(Km\). The proportion above \(Km\) tends to one. The fractional parts of their logarithms are asymptotically uniformly distributed: within each fixed-length window their increments differ from \(\alpha\bmod 1\) by \(O(1/m)\); apply uniform distribution of the irrational rotation on translated windows, then increase the window length. Thus broad real-phase distribution and even almost-total occupation above any fixed multiple of the minimum are compatible at the rational level. If such a cycle consisted of ordinary integers, the \(r\) successive rises would force \(2^r\mid m+1\), impossible for large \(j\) since \(m=O(j)\) and \(r\asymp p\ge j^2\). A general positive-integer cycle may distribute its rises over many runs. The first missing implication is an arithmetic obstruction for that unrestricted word, beyond the phase and height distributions.

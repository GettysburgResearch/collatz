# A smaller ordinary merger or a first exit from a wider starting band

**Written theorem with external inputs.** Use the positive ordinary shortcut map \(T(2x)=x,\ T(2x+1)=3x+2\). Let \(X\) be a sufficiently large positive integer. Choose one row from the table. By \(O_\epsilon(X^{\rho/3+\epsilon})\) shortcuts, the orbit of \(X\) has met the orbit of some positive integer strictly below \(X\), or has exited its closed starting band \([X,RX]\). In the latter alternative, if no smaller merger has yet occurred, the observed homogeneous coefficients \(g_i=3^{u_i}/2^i\) have the same first-exit time and direction from \([1,R]\). Here \(u_i\) counts the odd departures before clock \(i\). The bounds require a fixed positive \(\epsilon\) small enough that \(\rho/3+\epsilon<1/3\).

| \(R\) | Reversible local exclusion | Four-copy rate cap \(\rho\) | Located exponent before \(\epsilon\) |
|---|---|---:|---:|
| \(9/2\) | \(OEE\) | \(0.818622\ldots\) | \(0.272873965\ldots\) |
| \(81/16\) | \(OEE\) | \(0.907614\ldots\) | \(0.302538283\ldots\) |
| \(2^{5/2}=5.656854\ldots\) | \(OEE\) | \(992/1000\) | \(0.330666667\ldots\) |
| \(2^{51/20}=5.856343\ldots\) | \(OEE\) | \(997/1000\) | \(0.332333333\ldots\) |

At \(R=81/16\), compare the *closed physical band* with the homogeneous interval **\([1,R)\)**. Four initial odd departures have coefficient exactly \(R\), while the positive additive correction puts the true endpoint strictly above \(RX\). The half-open endpoint accounts for every exact upper resonance. The other three rows have no attainable upper resonance. The height threshold and constants from the external asymptotic estimates are ineffective.

The three ingredients are an ordinary smaller-parent identity, a fourth-moment count on a more restricted word language, and the residence-to-first-exit argument from the sprint's cycles branch. The count adapts Weaver 181/v1 §4. Its fixed-place Subspace Theorem step is external. The logarithmic order comparison uses the reported Chudnovsky bound \(\mu(\log 2/\log 3)\le3\). The baseline first-exit and unfiltered band-language results are due to Weaver 223/v1. The sprint theorem for the unfiltered \(9/2\) band already gives unconditional agreement there at exponent \(8/25\). Here the alternative permits an actual smaller ordinary partner and extends to the displayed wider bands. [Weaver 181/v1 §§4.1–4.3](https://rstation.ai/problems/collatz/papers/181/v1) · [Weaver 223/v1 §7](https://rstation.ai/problems/collatz/papers/223/v1) · [Chudnovsky, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11) · [First-exit proof in this packet](../../../cycles/FIRST_EXIT.md)

## Why a surviving path has no consecutive evens

Suppose an \(OEE\) factor starts from the odd integer \(x\). Its third endpoint is \(y=(3x+1)/8\). Physical parity gives \(x\equiv5\bmod8\). The positive odd integer \(m=(x-1)/4\) has \(T(m)=y\). If the factor lies in \([X,RX]\) for \(R\le6\), its first endpoint obeys \((3x+1)/2\le6X\), whence \(x<4X\) and \(m<X\). This is a visit to the original orbit from a strictly smaller source.

A nonempty, in-band path from \(X\) must start odd, since the first even step would leave below \(X\). Its first pair of consecutive even departures, if one occurs, is preceded by an odd departure. Thus a full prefix avoiding all smaller mergers contains no \(EE\), and the same holds for its internal subwindows. Located-window counting below asks for arbitrary starting integers *inside the prescribed band* whose next \(N\) steps are confined and whose word has no \(EE\). It does not assume those internal starting integers coincide with \(X\).

## Single-source language at \(R=9/2\)

Write \(\alpha=\log_3 2\), \(a=1-\alpha\), \(p_0=3a-1\). Weaver 223 shows that at the original start, every homogeneous-band word through \(t\) is obtained from \(b_i=\lceil i\alpha\rceil-\lceil(i-1)\alpha\rceil\) by deciding independently at each zero whether to move that zero one place right. A final zero may move beyond the observed prefix. Its \(z=t-\lceil t\alpha\rceil\) zeros have gaps two or three. No two gaps of two share a zero: three zeros in five consecutive positions would contradict \(5a<2\). If \(p\) gaps have length two, avoiding \(EE\) excludes one of the four choices at each of these disjoint pairs. The exact count is
\[
                     2^{z-2p}3^p,\qquad p=p_0t+O(1).
\]
Thus this particular local exclusion leaves entropy \(a+p_0\log_2(3/4)=0.324573769\ldots\), below the unfiltered \(a=0.369070246\ldots\). This is a word count. A bound on located integer states requires the next argument.

## Rotation description for arbitrary entry phase

Take a window \(x_0,\ldots,x_N\) anywhere in \([X,RX]\), with \(N\asymp\log X\). The standard product identity gives
\[
      \log_3(x_i/x_0)=h_i-i\alpha+c_i,\qquad
      0\le c_i\le \eta_X=N/(3X\log3).
\]
Consequently all integers \(h_i\) fit in a strip \([\phi-W+i\alpha,\phi+i\alpha]\), where \(W=\log_3 R+\eta_X\) and \(\phi\) varies in a bounded interval. Put \(H_i=\lfloor i\alpha+\phi\rfloor\), \(f_i=\{i\alpha+\phi\}\), \(d=\log_3(R/3)\). The upper allowed grade is \(H_i\). The only other possible grade is \(H_i-1\), allowed only if \(f_i\le d+\eta_X\). For the displayed radii \(d<\alpha\), hence \(d+\eta_X<\alpha\) for large \(X\). A zero increment of the baseline \(H\) ends at \(f_i\in[\alpha,1)\), which therefore fixes the actual grade \(h_i=H_i\). Partial groups at the two ends contribute \(O(1)\) bits.

Between consecutive baseline zeros the support is a run of one or two baseline ones followed by a zero. All admissible choices place a single zero in this support. A drop of the grade inside the run cannot be undone before its end, since that would require an increment of two. The forms are \(A=\{01,10\}\) on length two and \(B=\{011,101,110\}\) on length three. At restricted three-letter supports the earliest zero is unavailable, reducing \(B\) to \(B'=\{101,110\}\). The last form applies when the first internal grade cannot be lowered.

More explicitly set \(r=(f_i-\alpha)/a\in[0,1)\) at a baseline zero, \(q=1/a-2\), and denote
\[
       t=1-q,\qquad s=(d-1+2a)/a .
\]
The phase at the next baseline zero is \(r+q\bmod1\). When \(r<t\) it occurs two clocks later, giving \(A\). When \(r>t\) it occurs three clocks later, and the intermediate phase after the first of the three letters is \(1-2a+ar\). Thus \(t<r<s\) gives \(B\), and \(s<r<1\) gives \(B'\). This description applies for \(a\le d<\alpha\), with endpoint cases treated as limits. The smaller \(9/2\) case is \(d=a\). For \(R=2^{k/l}\), \(s=(k/l-2)(q+1)\).

The physical correction \(\eta_X\) can enlarge \(B'\) to \(B\) only within \(O(\eta_X)\) of \(s\). Uniform irrational rotation counting over intervals shows that in any length comparable to \(N\), the number of such exceptions is \(o(N)\), uniformly in the entry phase. The same applies to singleton phase breakpoints and to blocks within a vanishing distance of any of their finitely many fixed-length partition endpoints. At each exceptional block we allow the full unfiltered choices. Their total exponential cost is \(2^{o(N)}\). An explicit elementary justification of uniformity fixes an arbitrary small mesh, sandwiches the small intervals by mesh intervals, applies geometric-sum equidistribution uniformly in the phase, then lets the mesh shrink. The number of strip phase cells needed to specify all ordinary, restricted, and exceptional categories is \(O(N)\) for the whole window, including endpoints. Their union therefore also costs \(2^{o(N)}\).

## Exact fourth-copy transfer for a block

Consider four copies of a fixed family of \(A,B,B'\) supports. The early/late boundary grades and every support odd count agree across copies. For a word with odds at zero-based positions \(i_1<\cdots<i_b\), its local numerator is \(F=\sum_j2^{i_j}3^{b-j}\). The numerator values are \(\{1,2\}\) for \(A\) and \(\{5,7,10\}\) for \(B\); \(B'\) uses a subset. All unordered pair sums for \(A\) are distinct modulo three and all for \(B\) are distinct modulo nine. Read a four-copy congruence \(F_1+F_2\equiv F_3+F_4\bmod3^b\) backwards one support at a time. The following supports have already canceled as exact integers. At the last outstanding support its binary multiplier is a unit, and the preceding supports vanish modulo the local ternary modulus. Hence the local unordered choices on the two sides match, and their exact numerator contributions cancel. Induction proves this property at every support.

For \(L\) consecutive supports allow only words without consecutive zero letters *within this block*. Let \(k\) be the number of allowed words and \(E\) the number of ordered colliding quadruples of them. The exact modular fourth collision probability is \(E/k^4\). To calculate \(E\), record four flags telling whether each copy ended its preceding support on zero. For each ordered pair of allowed zero positions \(i,j\), the other two copies use \(i,j\) in either order, counted only once when \(i=j\). Reject choices with zero first in a copy whose incoming flag was set. The outgoing flags mark which copies chose the final position. Start with all flags zero and sum the sixteen terminal counts.

At \(R=2^{5/2}\), all 65 open phase types of 32 successive supports satisfy \(E^{1000}<2^{992T}\), where \(T\) is their total clock. At \(R=2^{51/20}\), all 441 open phase types of 220 supports satisfy \(E^{1000}<2^{997T}\). The checker partitions the rotation circle at the translates of \(0,t,s\). It compares every phase exactly by the sign of
\[
  A+Bq,\quad \text{equivalently}\quad
  (A-B)\log3+(2B-A)\log2,
\]
using integer powers after clearing denominators. Repeated types impose only one check. The displayed decimal maxima in the output are diagnostic; the certified caps use the stated integer inequalities. [Exact phase and energy verifier](band_energy.py) · [32-support receipt](ENERGY_5_2.txt) · [220-support receipt](ENERGY_51_20.txt)

## Smaller radii with elementary support counts

At \(d=a\), the movable supports are copies of \(A\) at density \(a\) per physical clock. Consecutive \(A,A\) supports occur with density \(p_0\). Their four-letter block permits \(\{0101,0110,1010\}\) after excluding \(EE\). Its local two-odd numerators \(\{14,10,7\}\) have distinct unordered sums modulo nine. Its ordered fourth collision **count** is \(15\), and a lone \(A\) has count \(6\). There are \((a-2p_0)N+o(N)\) lone \(A\) and \(p_0N+o(N)\) paired blocks, uniformly on long subsegments. Hence \(\rho=(a-2p_0)\log_2 6+p_0\log_2 15\).

At \(R=81/16\) one has \(d=a+p_0\). The extra optional sites extend precisely the left member of each former gap-two pair into a \(B\). In the baseline \(d=a\) description, an optional site has \(f_i=v\in[0,a)\), and the gap to the next optional site is two precisely for \(v\in[0,p_0)\). The new optional site just before it has phase \(v+a\in[a,a+p_0)\). The preceding support, at clock \(i-3\), has phase \(v+p_0\). It is a lone \(A\) touching the new \(B\). No short gap occurs two gap indices earlier: otherwise four zeros in eight bits would contradict \(8a<3\). Consequently the resulting \(ABA\) blocks are mutually disjoint, and the remaining lone \(A\)'s have density \(a-3p_0\). In an \(ABA\) the eight allowed words have numerators \(\{238,206,202,170,146,175,143,119\}\). Their modular ordered fourth energy is 160. Thus \(\rho=(a-3p_0)\log_2 6+p_0\log_2 160\). Strip boundary discrepancies have density zero, as above.

## From word energy to located ordinary starts

Partition the full word into independent product blocks of a fixed size \(L\) supports (or the disjoint analytical blocks in the preceding two rows). Allow every internally \(EE\)-free choice independently across blocks, including choices creating \(EE\) across a join. This is a superfamily of every actual window. Each block fixes both its clock and its odd grade, so changing block choices changes only internal grades. Every product word stays within a bounded-width homogeneous strip. Exceptional blocks and incomplete boundary pieces have bounded clock and can use unrestricted choices.

Use Weaver 181 §4.2–4.3 at the confined depth
\[
 N=\left\lceil\frac{4+\sigma}{3+\sigma}\log_2(\lceil(R-1)X\rceil+1)\right\rceil,
 \qquad p=\lfloor N/(4+\sigma)\rfloor .
\]
For any small fixed \(\sigma>0\), take four consecutive, disjoint, block-aligned segments of lengths \((1-\sigma)p+O_L(1)\) with the same separation margins as in §4.3. The first segment begins at a boundary at or after \(3\sigma p\). Rounding now costs \(O_L(1)\) per boundary instead of three clocks. All clocks and grades at segment cuts are fixed for each product family. The bounded strip gives the required upper bound on its segment numerators. The same fixed-place integral Subspace Theorem argument bounds the quantized fourth moment of each segment by its exact fourth congruence probability, at sufficiently large \(X\); it uses four independent uniform choices of the whole segment. The number of representations of the fixed data is subexponential.

For completeness, if a segment contains blocks of sizes \(k_i\) and ordered energies \(E_i\), its exact fourth probability is \(\prod_i E_i/k_i^4\), by the support-by-support cancellation. Fourier inversion and Hölder applied to the four independent segments bound an atom of their combined quantized law by the product of the fourth roots of their four collision probabilities. Multiplying by the whole product family's cardinality cancels every \(k_i\) inside those segments. The exterior blocks occupy \(O(\sigma N)+O_L(1)\) clocks and cost at most \(2^{O(\sigma N)+O_L(1)}\). Thus the number of actual integer starts in \([X,RX]\) with a confined, \(EE\)-free \(N\)-window is
\[
      2^{\rho N/4+O(\sigma N)+o(N)}
       = O_\epsilon(X^{\rho/3+\epsilon})
\]
on choosing \(\sigma\) small. Here the arc of normalized source residues has length at most \(2^{-p}\), the quantization error is absorbed by a bounded number of grid cells, and each integer in the band gives a distinct residue modulo \(2^N\). These are the same location and concentration steps as Weaver §4.3; simply counting global words would give a different estimate.

## From located starts to a finite physical exit or merger

Let \(B\) be the actual number in this located-start set. Put \(U=N+B\). If the original \(X\)-orbit remains in band and avoids all smaller visitors through \(U\), it has no \(EE\). The \(B+1\) starts at clocks \(0,\ldots,B\) each have a confined, \(EE\)-free window of the required length, so two coincide. Their nonempty returning subarc of clock \(t\le B\) and odd grade \(u\) satisfies
\[
  |u\log3-t\log2|\le t/(3X).
\]
For \(\rho/3+\epsilon<1/3\), select \(\kappa>2\) close enough to 2 that \((\rho/3+\epsilon)(1+\kappa)<1\). The cited two-log estimate gives \(|u\log3-t\log2|\ge c_\kappa t^{-\kappa}\), contradicting that inequality at sufficiently large \(X\). Thus an earlier ordinary smaller visitor or an actual first exit must occur by \(U\).

If a first exit occurs without a preceding merger, its date is within this bound, and the accumulated log correction is at most \(U/(3X)\), including the first exterior observation. Its comparison to zero agrees with the homogeneous log. For the algebraic radii \(R=2^{k/l}\), the comparison to \(\log R\) reduces after multiplying by \(l\) to \(lu\log3-(lt+k)\log2\). Exact equality is impossible since \(k>0\) and \(lt+k>0\). The lower bound beats the perturbation uniformly. At \(R=9/2\) subtract \(2\log3-\log2\); the possible equality \((t,u)=(1,2)\) is inadmissible. At \(R=81/16\) subtract \(4\log3-4\log2\). The only exact equality is \((t,u)=(4,4)\), already handled by a half-open homogeneous upper end. Every other sign is separated for the same reason, with fixed coefficient shifts. This proves the date and direction claim.

An upward exit admits no subsequent descent conclusion. The result also permits a merger into a smaller source whose eventual convergence requires separate information. The hypotheses in the universal Collatz conjecture are not discharged by an upper bound on the number of surviving words.


## A longer forbidden factor with no consecutive evens

The upper word `OOEOOEOOEOOEOEOEOOEOEOOOEOEOO` has length 29 and nineteen odds. Whenever it occurs at a positive local source \(x\), the integer \(m=(x+3)/2\) follows `OOOOOOOOOOOOEOEOEOOOEOEOEEEE` for 28 steps to the same ordinary endpoint, also with nineteen odds. More explicitly the source cylinder is \(x\equiv29253627\bmod 2^{29}\). The upper and lower numerators at the common endpoint are, respectively, \(3^{19}x+5895447367\) and \(3^{19}m+1204331483\), with denominators \(2^{29}\) and \(2^{28}\). An integral affine endpoint forces all parities of the indicated word.

At the upper eleventh state \(P\), one has \(2048P=6561x+12325\) and \(6561m=1024P+3679\). Thus \(2P\le9X\) gives \(m<X\) for every \(X\ge2\). This proves an ordinary smaller visit without using a limiting coefficient or any assumed meeting. The two displayed finite prefixes intersect only at the pair of clocks (29,28), for every positive lift of the cylinder. The exact replay checks all 870 pairs of prefix clocks by solving the integer affine equality in the nonnegative lift parameter. The same factor works at any fixed band ratio below \(6561/1024\) for sufficiently large \(X\). The transfer bounds above use only the shorter \(OEE\) rule. [Both native smaller-parent theorems](BandParents.lean) · [Lean execution archive](../../../../../reports/astra-reciprocal-rigidity-20261127/checkpoint4/README.md)

The same verifier checks a bank of 446 ordinary upper factors containing no consecutive evens. For every listed factor, regardless of its position in the original orbit, the stated lower word gives a positive smaller source whenever the designated upper comparison state is at most $6X$ and $X\ge61$. The maximum strict lower bound on $X$ is $783/13$. These are individual certificates, found by a finite search and rechecked with exact arithmetic. The bank does not exhaust longer factors or by itself prove a sixfold exit estimate. [Finite bank](SIXFOLD_MOTIFS.tsv) · [Exact verifier](motif_controls.py) · [Verified counts](MOTIF_CONTROLS.txt)

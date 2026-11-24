# Ordinary descent from two intervening light blocks

Use the shortcut Collatz map \(T(x)=x/2\) at even \(x\), \(T(x)=(3x+1)/2\) at odd \(x\). The light block \(L\) has exact odd gaps \(2,1\) and obeys \(8q'=9q+7\). The paid block \(P\) has gaps \(1,4\) and obeys \(32q'=9q+5\). All original floors below are ordinary odd boundary or intermediate values.

## Two light blocks suffice for mixed singleton and pair clusters

**Kernel-checked.** On any one positive ordinary infinite L/P input whose consecutive paid clusters have length one or two and are separated by at least **two** L's, every boundary and its odd intermediate have a strictly smaller positive odd ordinary nonconverger. The theorem quantifies over each individual position, including initial partial clusters. The smaller source can follow different later gaps. PR193 proves the corresponding raw-label theorem for three intervening lights. Its numerator \(183q+1\) also works with two after a change of scale in the comparison. [TwoLight.lean](TwoLight.lean) · [PR193 mixed comparison at a137949](https://github.com/GettysburgResearch/collatz/blob/a1379492dbaae85e0d16662b41ccc7176ab3c66e/research/astra-global-synthesis-20261124/merger/mixed.md)

Put \(F(q)=(183q+1)/128=(183/128)(q+7)-10\). At any boundary followed by LL, composing the two light equations gives \(64(q_2+7)=81(q+7)\). Oddness of \(q_2\) implies \(128\mid q+7\), so \(F(q)\) is integral and greater than two. At such a boundary, if the third upcoming block is L use the single-light tile. Otherwise use LLP or LLPP according to the cluster length. The raw spacing rules guarantee that the new tile boundary is again followed by LL. For a source tile with \(2^Aq'=3^p q+C\), the table gives genuine target parity words satisfying \(2^AF(q')=3^pF(q)+K\).

| Tile | Clocks | Odd inputs | Source carry | Target carry | Comparison bits |
|---|---:|---:|---:|---:|---|
| L | 3 | 2 | 7 | 10 | 011 |
| LLP | 11 | 6 | 1391 | 1999 | 10110011100 |
| LLPP | 16 | 8 | 22759 | 32999 | 1011011100001100 |

The target boundaries exceed two forever, so none reaches the \(1,2\) cycle. If at least three L's start at the prescribed source, \(1024\mid q+7\), and \(m=F(q)/2=(183q+1)/256\) is positive and odd. The ordinary step \(T(F(q))=m\) transfers nonconvergence. The exact saving below the original light intermediate is
\[
 (3q+1)/4-m=9(q+7)/256.
\]
With zero, one or two initial L's, the boundary immediately after the first P is itself below both original floors. These cases retain the nonconvergence of the actual source trajectory. The raw Lean hypotheses are odd boundaries, their two exact equations, and the Boolean rules that PP is followed by L and PL is followed by L.

## Longer tiles can be mixed indefinitely

**Kernel-checked finite data and general theorem.** A reset tile has a source parity word, a target word of equal length \(A\ge3\) and the same odd count \(p\), and carries \(C,K\) with \(183C+2^A=3^p+128K\). Three future tile equations on the same prescribed infinite ordinary trajectory force \(128\mid183q+1\) everywhere. Indeed each binary divisor is a multiple of eight while the multiplier is odd, successively forcing divisibility by 8, 64 and 128. Literal realization of the binary words gives a single physical comparison throughout. The generic Lean theorem allows unbounded lengths of certified tiles. At a starting boundary with \(1024\mid q+7\), it yields the same smaller odd \(m\). [ResetTiles.lean](ResetTiles.lean)

The compiled catalog admits any indefinite mixture of the three previous tiles and the following three. Thus paid runs of three and four and separations of a single light may recur arbitrarily often in this grammar.

| Additional tile | Target carry | Clocks | Odd inputs | Literal comparison bits |
|---|---:|---:|---:|---|
| LLPLPP | 8038775 | 24 | 12 | 101100110111001100001100 |
| LLPPPLPLPP | 1998418881143 | 42 | 20 | 101101110011101011000011000110000101001100 |
| LLPPPPLLLLP | 18222978432559 | 43 | 22 | 1011011100111011010101100001000001101001101 |

**All-position corollary, written.** At any catalog boundary the next two blocks are L. Three upcoming lights give the kernel theorem. If the third is P, its endpoint supplies the smaller actual source. Strictly inside a nonsingleton tile the next P follows at most four initial L's, since every nonsingleton ends in P and its longest light run has length four. After \(h\le4\) lights and a P its boundary \(w\) obeys \(32w=9(9/8)^h(q+7)-58\). On a light start \(q\equiv9\bmod16\), hence \(q\ge9\). Substitution of \(h=4,q=9\) and comparison of the slopes give \(w<(3q+1)/4<q\). On an immediate P its endpoint is below \(q\) and the paid intermediate. These later source boundaries are nonconvergent because their future contains infinitely many ordinary tile boundaries greater than two.

The thirteen finite header cases in PR192 require no tail restriction. Each of its other three five-letter headers \(W=\mathrm{PPLLL},\mathrm{PLLPP},\mathrm{PLLPL}\), preceded by two lights, already belongs to the language generated by L, LLP and LLPP. Their decompositions are, respectively, LLPP·L·L·L, LLP·LLPP, and LLP·LLP·L. Thus a word starting \(L^rW\) followed by any infinite catalog tiling has the original-floor conclusion for **all sixteen headers**. When \(r\ge2\), the residual case splits into complete tiles from the original source. For \(r<2\) use its first paid endpoint. This is an infinite-tail statement; the common target in the next section is a separate finite conclusion. [PR192 all-headers comparison at 045be43](https://github.com/GettysburgResearch/collatz/blob/045be43632f274dd64faf15714e42cc8de27a2e9/research/astra-high-variance-20261124/DESCENT_ALL_HEADERS.md)

## A finite descent for every exit in an explicit range

**Kernel-checked.** Suppose a finite actual source starts \(L^r(\mathrm{PLL})^sP\), \(r\ge3\), and
\[
5\,9^r729^s\le13\,8^r2048^s .
\]
The boundary \(w\) immediately after this final P is odd, positive, below \(q_0\), and below its original first light intermediate. Any later exit now has the ordinary smaller source \(w\) on the original path. This includes the formerly missing PLLL and PPP exits, with unrestricted continuation. In particular \(r\le 8s+8\) suffices because \(5\cdot9^8<13\cdot8^8\) and \(729\cdot9^8<2048\cdot8^8\). The displayed integral condition retains a larger range. [LoopCone.lean](LoopCone.lean)

One PLL sends \(z\) to \(z'\) with \(2048z'=729z+4213\), so \(2048^sz_s\le729^sz_0+4\cdot2048^s\). The initial light run gives \(8^r(z_0+7)=9^r(q_0+7)\). Combining both with \(32w=9z_s+5\) and the cone gives \(160w\le117q_0+1024\). The first three light blocks force \(q_0+7\) positive and divisible by 1024. The strict floor inequalities follow. For fixed \(s\) with \(r\) growing, the direct multiplier has no uniform saving.

**Additional finite merger outside the cone, written.** In the earlier four-state transport, state \(C(q)=(9q-11)/2\) also accepts PPLLL in 18 clocks, with eight odd inputs, carry 888536 and bits 000100010101101101. For \(s\equiv2,3\bmod4\) that state was already available. To also reach C when \(4\mid s,\ s\ge4\), write \(q_0+7=2\cdot8^rv,\ q+7=2\cdot9^rv\) at the first P as in the original transport. For \(r\ge2\) choose \(m=3\cdot2^{3r-4}v-5\). Its positive odd size is below the original light floor since \(m+5=3(q_0+7)/32\). Following signed magnitude 5 through \(3r-4\) clocks and \(2r-2\) odd inputs brings \(m\) to \(E(q)=(q-53)/6\). One PLL transports E to the old state \(D(q')=(q'+1)/6\) in eleven clocks, with six odd inputs, carry 7483 and bits 10010010111. After that, \(D\to A\to B\to C\to D\), so every positive multiple of four ends at C. Consequently PPP and PPLLL admit original-floor finite mergers at \(s\equiv0,2,3\bmod4,\ s\ge1\). The \(s\equiv1\) cases and general PLLL outside the cone remain unresolved by these charts. [Four-state transport at 07aa512](https://github.com/GettysburgResearch/collatz/blob/07aa5124f7ca482b6665d61355fac0af5f6e55b2/research/astra-global-closure-20261124/closing/descent/PLL_TRANSPORT.md)

The [reset avoidance proof](RESET_AVOIDANCE.md) produces positive-growth nonperiodic symbolic families on which this same affine comparison cannot reset again. Every finite prefix has positive ordinary realizations. Its attempted long-run nonconvergence inference fails an ordinary source-height bound. The open problem is to control the original smaller comparison or supply a new one on each actual persistent defect, with an argument beyond this two-letter alphabet still needed. [Execution record](../../../../reports/astra-global-closure-20261124/round3/descent/EXECUTION.md)

# A complete ternary certificate at the original parent

Let $T(2v)=v$, $T(2v+1)=3v+2$, $M_m=2^m-1$ and $N=2^m$. For the original hard family $m=11+162j$, put $81z+271=128N$. Whenever $3^{12}\mid z+1$, there is a smaller positive integer $w\equiv17\bmod48$ with an ordinary lower path to $M_m$. Its triple has an ordinary path either below the forty-bit floor $z/2^{40}$ or to the peak of an already paid earlier Mersenne. Every parameter in this ternary ball is included. The exceptional initial index $m=11$ has $z=3233$ and $v_3(z+1)=1$.

Write $\mathrm{Good}(y)$ for an ordinary trajectory from $y$ to 1. The implication $\mathrm{Good}(z)$ uses these two hypotheses at the same parent $z$.

1. Every positive $y$ with $2^{40}y<z$ is good.
2. For every $0<w<z$ with $w\equiv17\bmod48$, $\mathrm{Good}(3w)$ implies $\mathrm{Good}(w)$.

These are the least-source consequences consumed by the prior PR197 forty-bit return and the earlier offset packet. The finite-prefix assertions themselves require neither hypothesis. This covers one specified congruence class in either original parameter, not the general Collatz conjecture. [Earlier offset theorem](EARLIER_OFFSETS.md) · [PR197 quantitative return](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean)

## Ordinary affine certificates

Write $m=173+162j'$ and $X=2^{m-100}$. Because $81(z+1)=2(64N-95)$, the input is characterized by
\[
                 X=3221021+3^{16}v\qquad (v\ge0).
\]
Indeed $2^{106}X\equiv95\bmod3^{16}$ and $3221021$ is its least solution. A node $(x,S)$ represents every $X=x+St$ with $t\ge0$. Its three children have $(x+iS,3S)$ for $i=0,1,2$. The explicit tree terminates in 123 leaves, the longest at 14 ternary digits beyond the root. Each leaf gives $(D,e,b,h,p,\sigma)$, where $F=D+e$, $\delta=h-F$, $g=p+1-D$, and the signed upper constant is $c=\sigma-1$. Its ordinary positive query is
\[
                w=\frac{2^FN-b}{3^D}.
\]
The local certificate verifies $0<w<z$, $w\equiv17\bmod48$ and the following full physical prefixes.

| Start | Clock | Odd departures | Endpoint |
|---|---:|---:|---|
| $w$ | $F$ | $D$ | $N-1$ |
| $3w$ | $h$ | $p$ | $2^{m-\delta}3^g+c$ |

At the least ordinary representative $X=x$, both rows are directly iterated. Increasing $t$ by one adds $A=2^{100+F}S/3^D$ to $w$. The checks include $2^F\mid A$, $2^h\mid3A$, and $48\mid A$. The two words therefore stay legal for all $t$, and their slopes are verified separately:
\[
  3^D A/2^F=2^{100}S,\qquad
 3^p(3A)/2^h=3^g2^{100-\delta}S .
\]
The positive base and coefficient inequality preserve the strict source budget. In the entire tree $16\le D\le29$, $F\le45$, $h\le72$, $\delta\le28$, and $g\le9$. These are physical shortcut clocks and actual odd departures.

## Paying the upper path

| Upper constant | Leaves | Additional physical route |
|---:|---:|---|
| $-1$ | 34 | $v=m-\delta$ successive odd departures reach $3^{v+g}-1=T^{v+g}M_{v+g}$. Every leaf has $\delta-g\ge6$. The earlier-offset theorem already covers all indices through $m-5$ under the two displayed hypotheses. |
| $0$ | 2 | The $v$ even departures reach $3^g$. Each leaf satisfies $2^{40}3^g<2^{173}\le N<z$. |
| $+1$ | 87 | Put $m-\delta=2n+r$, $r\in\{0,1\}$. Another $2n$ physical steps give $2^r3^{g+n}+1$ by $T^{2n}(4^na+1)=3^na+1$. |

For each positive leaf, the strict forty-bit inequality is checked at $m=173$. An increase of 162 in $m$ multiplies the exponential term in the final height by $3^{81}$ and $N$ by $4^{81}$, preserving strictness. Every negative leaf uses the general earlier-offset result. The argument also verifies $T^7z=M_m$. Thus the upper path makes $3w$ good, canonicality makes $w$ good, and the actual lower merger makes $z$ good.

## A single explicit row at a deeper address

If $3^{15}\mid z+1$, put $A=(z+1)/3^{14}$ and $w=2^{22}A-79$. Then $3\mid A$, $0<w<z$ and $w\equiv17\bmod48$. The lower route reaches $z$ after 22 steps and $M_m$ after 29. The upper route reaches $2^{m-7}+1$ after 36 steps with 17 odd departures. To verify the latter, $3^{18}A+190=2^{14}\cdot2^{m-7}$ gives $A\equiv10034\bmod16384$. The representative $3w_0=126256938771$ reaches $237266675$ at clock 36, and a lift by the verified parity word gives the claimed endpoint for every $A$. The positive-turn identity then supplies the forty-bit floor. This one row corresponds to $(D,e,b,h,p,\sigma)=(18,11,31403136391,36,17,2)$. [Single-row kernel proof](DeepFifteen.lean)

## Parameter counts, evidence and priority

The earlier ternary isometry gives the root parameter $j\equiv131291\bmod177147$ and, on $m=12\cdot2^{18k}-1$, $k\equiv43954\bmod177147$. Both moduli equal $3^{11}$. More explicitly, $j\mapsto(2^{17+162j}-95)/3^5$ and $k\mapsto2(2^{18k}-1)/27$ each induce bijections modulo every $3^a$ by LTE. The new ball and the previous disjoint single-unit shells $6\le s=v_3(64N-95)\le15$ have combined natural density
\[
 \sum_{s=6}^{15}3^{-(s-2)}+3^{-11}
 =\frac1{54}+\frac{17}{18\cdot3^{11}}
 =\frac{29533}{1594323}
\]
in either parameter. This is the density of the stated explicit union. Other paid classes can overlap or enlarge it. The previous all-unit cutoff was $3^{69}\mid z+1$. [Previous ternary proof and parameter isometries](TERNARY_PUMP.md)

[ValuationCharts.lean](ValuationCharts.lean) provides ordinary chart transport, a generic proof that a checked three-child tree exhausts every nonnegative parameter, and the conditional parent return. [ValuationCover.lean](ValuationCover.lean) instantiates the complete tree, its root congruence, the two ordinary witnesses and the parent return. [The independent checker](check_valuation_cover.py) reads the explicit tree, recovers every lower inverse word from its positive orbit, checks both full parity words at two representatives, verifies both compensated slopes, and checks the leaf masses exactly. It also materializes the original positive parent at $m=21269153$, the least root exponent, and directly iterates its two selected prefixes and $T^7z$. The grade histogram, addresses, row and bounds are in [the archived control](VALUATION_COVER_CONTROLS.json).

PR195 at full head 3fa7ef4a0011b35447a70f587b400878d5ea8ebe already proves the ordinary common upper $T^{a+1}(3V_a)=(z-1)/2$ for $V_a=2^a(z+1)/3^a-1$, $a\ge2$, followed on this hard family by a fixed route to $2^{m-7}+1$. Its bounded even-minimum theorem assumes a least bad source and its stronger bounded cycle floor. The canonical smaller sources and ternary branches above supply a different comparison at the original parent, under the explicit forty-bit hypotheses only. The new ternary tree uses the general earlier-offset deduction, the ordinary positive-turn identity, and ordinary parity-word lifting from the preceding packets. [PR195 common ordinary upper](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/ordinary/EVEN_MINIMUM.md) · [PR195 physical ancestor exchange](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/ordinary/AncestorExchange.lean)

The argument leaves the remaining units at shallow valuations open. In particular, membership in a larger-density set of delayed indices would still allow an exceptional least parent.

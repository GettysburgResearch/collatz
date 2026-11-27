# A positive or negative carry against the same physical upper hit

Let \(T\) be the positive shortcut, \(P_h\) the odd count, \(s\) the least nonbasin integer, and \(z\) the least \(17\bmod48\) nonbasin integer whose triple belongs to the basin of one. A *binary alignment of length \(h\)* between \(x\) and \(c\) means \(x\equiv c\bmod2^h\). Their next \(h\) parities are identical. The statements below concern actual finite ordinary trajectories except where the negative control is explicitly specified.

## A sharp restriction at the original least source

If \(x=c+2^h u\), \(u\ge0\), \(T^h c=v\), and \(T^h x\ge s\), then
\[
       \boxed{\;cs\le xv.\;}                                                \tag{1}
\]
In fact \(T^h x=v+3^{P_h(c)}u\), and the ordinary affine correction has nonnegative sign, so \(3^{P_h(c)}c\le2^h v\). Multiplication and substitution prove (1). Equality can occur on an all-even prefix. If instead \(c>x\), the binary translation in the other direction gives \(T^h c\ge T^h x\ge s\). Thus that ordering cannot give \(v=1\) when \(s>1\). This proof also applies to any positive lower floor certified for the specified endpoint of \(x\). [CarryAlignment.lean](CarryAlignment.lean)

In particular a full aligned good certificate at the **original** \(z\) has \(c\le z/s\le 2^{40}\). In the bounded alternative, the pinned estimate \(243(z-1)\le1024(s-1)\) gives \(z<5s\), whether or not \(z\) lies on the bad cycle. Therefore \(c\le4\). If \(h=0\) the hit gives \(c=1\). If \(h=1\), its only positive predecessor at one is two, which has the wrong initial parity. If \(h\ge2\), \(c\equiv z\equiv1\bmod4\) leaves only one. **The only positive control whose complete first-hit certificate aligns at this original \(z\) is \(c=1\).** Its zero-clock certificate is always available. [Kernel statement canonical_aligned_one](CarryAlignment.lean) · [PR195, original bounded ratio](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/CANONICAL_FLOOR.md) · [PR197, unconditional quantitative return](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean)

At any physical phase of a restricted odd cycle with native exponents in \(\{1,2\}\), every completely aligned positive control is one or two. Every positive path from \(c>2\) to one contains two consecutive even departures, since its first entry into \(\{1,2\}\) must be \(4\to2\), followed by \(2\to1\). The target cycle has no multiple of four and hence no such pair. This also proves the result for \(c>x\) by using the common parity word. An odd phase admits only one. At an even phase, two genuinely aligns for one clock.

An ordinary walk on a good control can use the two directed edges between one and two in opposite ways, so its very last edge need not use the first-hitting forward branch. Before first reaching \(\{1,2\}\), deleting backtracks gives the unique simple approach to the cycle. For a non-power-of-two good control this approach itself contains \(8\to4\to2\). Indeed its last odd \(w>1\) satisfies \(3w+1=2^a\) with \(a\ge4\), and its next state is \(2^{a-1}\). Even allowing all ordinary reverse edges cannot lift that full approach on the restricted bad cycle. A first intersection with the upper word strictly before this terminal approach remains possible.

Every good original \(3z>4\) visits \(8,4,2,1\) in its actual first-hit suffix. The proper target four always allows a nontrivial positive control at a canonical source: \(5\to8\to4\) shares both first parity bits with \(z\equiv1\bmod4\). It pays only \(5s\le4z\). On a restricted lower, the full backward list into 4 through paths with no consecutive even inputs is \(\{4,8,5,10,3,6\}\). The sole predecessor is 8, whose only next legal predecessor is 5. The latter has predecessors 10 and 3; 3 has predecessor 6, while 10 and 6 admit no odd predecessor and cannot be preceded by another even. Thus at an odd canonical phase only the nonempty word from five can end at four. Replacing the target by any bounded set \(v\le V\) at a bounded least \(z\) still forces \(c<5V\) by (1), even when \(z\) is off cycle. An actually varying unbounded upper target, or a different use of the original leastness hypothesis, is required to escape this finite set of positive controls.

## Opposite signs spend actual odd departures

Suppose a positive trajectory beginning at \(x\) and the signed shortcut from \(-m<0\) have the same parity for a finite prefix. Let \(x_i\) and \(m_i\) denote their positive magnitudes. At an even input the ratio \(R_i=m_i/x_i\) is constant. At a common odd departure both divide by two after applying \(3x_i+1\) and \(3m_i-1\), respectively. Hence
\[
 R_i-R_{i+1}=\frac{1+R_i}{3x_i+1}.
\]
If all positive odd inputs on the prefix are at most \(M\), this yields
\[
     \frac{m_h}{x_h}+\frac{P_h(x)}{3M+1}\le\frac{m}{x}.                \tag{2}
\]
The negative orbit remains strictly negative at every clock, so its terminal magnitude is positive. No conjecture about the dynamics of \(3m-1\) is used. [Kernel statement opposite_budget](CarryAlignment.lean)

On a restricted cycle the positive odd ceiling is \(M=(16s+7)/3\). If \(2^d\mid x+m\), then the signed control \(-m\) matches \(x\) for \(d\) clocks, with at least \(\lfloor d/2\rfloor\) odd departures because even departures are isolated. Thus
\[
        \lfloor d/2\rfloor < (16s+8)m/x\le (16+8/s)m.                   \tag{3}
\]
This proves a linear bound in the magnitude of **any** negative control, including ones with an unknown signed future. Formula (2) is a physical comparison at denominator one. The proof also works on any single bounded matching segment.

## Which terms a fixed upper certificate pays

Use one supplied positive upper word from \(3z\). After its \(k\)-th odd departure at clock \(j\), take the clock \(t\) just after the lower's \((k+1)\)-st odd departure, whenever \(t\le j\). Write
\[
              X=T^t z=2^dY+C,\qquad d=j-t,\quad Y=T^j(3z).
\]
Here the full signed construction at a terminal hit is a special case with \(Y=1\). The intermediate \(Y\)'s are suffixes of the same original certificate. An upper even departure replaces \(Y\) by \(Y/2\), increases \(d\) by one, and leaves \(C,X\) exactly fixed. At an upper odd departure, suppose \(a\) lower even inputs precede its next odd. With the predeparture \(d\) as displayed, a paid next rank requires \(a\le d\), and
\[
  d'=d-a,\quad X'=(3X+2^a)/2^{a+1},\quad Y'=(3Y+1)/2,\quad
  C'=(3C+2^a-2^d)/2^{a+1}.                                               \tag{4}
\]
These are exact identities in the physical lower and upper trajectories. A negative center remains negative at every successively paid rank. Its magnitude acquires the extra positive term \((2^d-2^a)/2^{a+1}\). At any two successive aligned ranks, the ratio \(Q=2^dY/X\) satisfies
\[
       Q'/Q=\frac{1+1/(3Y)}{1+1/(3(X/2^a))}.                              \tag{5}
\]
Thus along any paid tail with upper odd states below \(s\), \(Q\) increases at each odd step. This is why the decrease (2) for a single unchanged negative control does not telescope across successive upper odd departures: (4) creates new magnitude precisely on this same fixed certificate. A positive good control may meet an earlier actual upper target \(v\) before visiting one. Bound (1) applies at that meeting, but it only pays the factor \(v\). Establishing a sequence of such meetings that forces a physical lower value below the original floor, or furnishes a smaller canonical bad lower with a good triple, remains open.

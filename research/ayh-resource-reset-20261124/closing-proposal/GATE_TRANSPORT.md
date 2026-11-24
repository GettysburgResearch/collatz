# The clock available after a fixed ordinary gate

Write \(T(2n)=n\), \(T(2n+1)=3n+2\). If an actual positive \(x\ge2^k\) has \(T^e x=a\), having taken \(p\) odd steps, then
\[
                  2^{e}a\ \ge\ 3^p x\ \ge\ 3^p2^k .
\]
Indeed each even step multiplies the state by \(1/2\), and each odd step multiplies it by \(3/2\) and adds \(1/2\). This proves
\[
                   k-e\ \le\ \log_2 a-p\log_2 3 .
\]
The same inequality holds after conditioning on any actual endpoint history or basin labels. A fixed target with growing odd count lies increasingly far beyond the one-octave native clock. Even a fixed target at small odd count leaves at most a constant number of native clocks after it. For a further block of \(b\) native clocks a necessary condition is \(a\ge 2^b3^p\). It supplies no independence. Once a target is fixed, its entire forward continuation is identical for all its ancestors.

There is a further problem with direct paired inversion. The image of an odd shortcut step is \(2\bmod3\), and both types of steps preserve the set of inputs prime to three. Consequently every positive predecessor of a multiple of three is obtained by doubling alone. If \(T^j(3y)=3q\), then \(y=2^j q\). For odd \(y,q\) this forces \(j=0\). To amplify a literal tripling failure with paired ancestors one must change the target pair or its representation. For odd \(q\), the genuine next pair is \(a=(3q+1)/2,\ 3a-1\), both prime to three. This shifted pair admits physical return words. For example \((4t+1,12t+2)\) maps in two steps on both arms to \((3t+1,9t+2)\) for every nonnegative \(t\). At a return to a fixed gate, the clock inequality above still applies.

The post-descent estimates at PR197 extend the time interval beyond the native clock for most original integers. Put \(\gamma=\log_2(2/\sqrt3)\) and \(d=\log_2 R\). Up to \(h=\lfloor(1-\alpha)d/\gamma\rfloor\), the scalar envelope for any fixed \(0<\eta<\alpha/4\) bounds each physical value through clock \(h\) below by \(cR^{\alpha-\eta}\), outside \(O(R^{1-c_*})\) original sources. A family of ancestors that visits a fixed gate by \(h\) is therefore **entirely in this scalar exception** once \(R\) is large. If it reaches the gate later, the cited precritical envelope supplies no bound on the inherited post-gate marks. The corresponding threshold for a mark in BALLISTIC_COLOR uses its own fixed altitude and test deadline. The exceptional set can contain a targeted population with either color.

The PR197 fixed-factor contraction is an original-octave estimate. It does not bound the inverse multiplicity of its chosen smaller witness or its membership in the next exception. PR204's same-clock theorem gives at least \(c_qX^{1/5}/\log X\) ancestors in one row for a literal ratio-five pair, without a prescribed central balance. PR206's prescribed prefix itineraries at one bad gate share the same post-gate suffix, which already contains the forced whole-row surplus of short gaps. PR205 distinguishes minorization for a random inverse chain from the deterministic future of its ordinary root. None proves an upper bound on the multiplicity of a moving discordant gate charged by the original source population. This is the remaining closing estimate in this attempted combination. No complete Collatz proof follows.

## A control with all clocks and bounded ordinary backtracking

Let \(s=\log_3 2\), \(s\le p<1\), and \(H_2\) be the binary entropy. In each octave \([2^k,2^{k+1})\), at least \(c_p 2^{kH_2(p)}/k^{3/2}\) integers \(x\equiv17\bmod48\) obey
\[
       T^j x\ge c'_p x \qquad(0\le j\le \lfloor p(\log_2 3)k\rfloor)
\]
for some fixed positive constants. This is an unconditional statement about ordinary source values. The proof fixes the four low bits \(x\equiv1\bmod16\) and prescribes the next \(m=k-7\) parity digits with exactly \(b=\lceil pm\rceil\) odd steps. Every binary word of that weight has a cyclic shift whose every prefix of length \(t\) has at least \(tb/m\) odd entries: rotate just after a minimum of the cumulative deviations from \(tb/m\). Each shifted word has at most \(m\) originals. Stirling gives the stated count. Every resulting \(k-3\)-digit parity word determines one class modulo \(2^{k-3}\). Its eight lifts in the octave include a representative \(2\bmod3\). Up through \(k-3\) clocks, the odd count is at least \(pj-O(1)\), and \(p\log_2 3\ge1\). At clock \(k-3\) the multiplicative height above the original is at least a constant times \(2^{(p\log_2 3-1)k}\). All subsequent clocks through the stated horizon can at worst halve on every step.

More generally, a walk from \(x\) to \(y\) using at most \(F\) ordinary forward and \(B\) ordinary reverse edges has \(T^ix=T^jy\) with \(i\le F,\ j\le B\). Induct along the walk, consuming an outstanding \(j\) on a forward edge when positive, otherwise increasing \(i\); a reverse edge increments \(j\). Since \(T(v)+1\le(3/2)(v+1)\), the displayed population obeys \(y+1\ge (2/3)^B c'_p x\) for **every** such walk through the allowed forward horizon. With bounded \(B\) this obstructs arbitrary fixed-factor drops, and with \(B=o(k)\) it obstructs fixed-power drops. At \(F\approx1.15k\) the lower exponent \(H_2(1.15\log_3 2)\approx0.84775\) still exceeds \(0.84\). These sources need not be actual tripling defects; the result controls exactly what an argument that discards the labels can distinguish.

## Sources

- The scalar inequality also appears as [OffsetDescent.linear_lower](https://github.com/GettysburgResearch/collatz/blob/7ad81ec56947146fac854d2586651ca0c934a536/research/ayh-resource-reset-20261124/positive-section/vendor/OffsetDescent.lean#L74).
- [PR197, fixed-factor return](https://github.com/GettysburgResearch/collatz/blob/7ad81ec56947146fac854d2586651ca0c934a536/research/ayh-resource-reset-20261124/directed-return/STRICT_RETURN_REFINEMENT.md) and the earlier [source-multiplicity envelope](https://github.com/GettysburgResearch/collatz/blob/7ad81ec56947146fac854d2586651ca0c934a536/research/ayh-resource-reset-20261124/literature-step/POST_DESCENT_TRANSFER.md) and [actual ballistic separation](https://github.com/GettysburgResearch/collatz/blob/7ad81ec56947146fac854d2586651ca0c934a536/research/ayh-resource-reset-20261124/literature-step/BALLISTIC_COLOR.md).
- [PR204, exact supplied-target paired pressure](https://github.com/GettysburgResearch/collatz/blob/5d4698b692ec102b44cf77a59930a2a80b4104fd/research/astra-joint-closure-20261124/pressure/WEIGHTED_POINTWISE_ROWS.md).
- [PR205, scoped inverse-law and actual least-source excursion](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/README.md).
- [PR206, fixed-gate prefix bank and common suffix](https://github.com/GettysburgResearch/collatz/blob/37d2b5d644664a746891042c199e58cfb06f1176/research/clock-itineraries/README.md).
- The external scalar comparison is also [Inselmann, Theorems 2.18 and 3.3](https://arxiv.org/abs/2402.03276). [Tao's Theorem 1.3](https://doi.org/10.1017/fmp.2022.8) concerns orbit minima for a logarithmically sampled ordinary start. It supplies no pointwise law at a supplied gate.

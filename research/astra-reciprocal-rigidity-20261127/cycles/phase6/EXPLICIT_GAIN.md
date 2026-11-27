# A common explicit exponent gain for the two ordinary survivor sets

One may take \(\gamma=\gamma_5=10^{-12}\) in [the forward dimer](STRICT_DIMER_SAVING.md) and [the bi-infinite two-gap](STRICT_REVERSE_SAVING.md) interval estimates. The power is specified; the eventual threshold and multiplicative constant remain ineffective. The computation below uses four independent signed copies at each moment, followed by the written Subspace Theorem argument. [Exact rational calculations](check_markov.py)

### Four-copy certificates

In the dimer chain let \(a,b,c\) count the copies in states \(0,1,2\), with \(a+b+c=4\) and \(b\) active coins. If exactly \(j\) coins choose a second 1, the next state counts are \((4-a-j,a,j)\). Matching a prescribed signed numerator bit restricts \(j\) to one of its two parities, determined by the full preceding history and the target. For \(\beta\in[.70,.72]\), an upper bound for the probability weight of that transition is \(\binom bj(72/100)^j(30/100)^{b-j}\). Use the following positive potential \(V(a,b)\), with entries in increasing order of \(b=0,\ldots,4-a\).

| \(a\) | \(V(a,b)\) |
|---:|---|
| 0 | 1000, 300, 396, 303, 539 |
| 1 | 404, 128, 126, 187 |
| 2 | 434, 130, 319 |
| 3 | 255, 297 |
| 4 | 734 |

The weighted sum of the possible next values of \(V\) in either parity class is at most \((37/50)V(a,b)\). The largest of the 30 exact row ratios is \(25857/35000\). Induction on the number of bits, uniformly in the incoming carry histories, shows that the chance of matching any \(T\) prescribed sum bits is at most \((1000/126)(37/50)^T\). After conditioning the four inputs to their target compositions the bound costs at most \((r+1)^4\). Since \(2^{21}37^{50}<50^{50}\), this gives signed dimension \(d_2=.42\) for all sufficiently large \(T\).

In the two-gap chain let \(b\) be the number of active copies (the preceding bit was 1). If \(j\) of them emit a zero then the next active count is \(4-j\). For \(.58\le\beta\le.59\) the probability weights are bounded by \(\binom bj(59/100)^j(42/100)^{b-j}\). The potential at \(b=0,\ldots,4\) equals \(1000,468,469,443,558\). Every parity row has weighted sum at most \(14/25\) times its current potential; the largest of the ten exact ratios is \(26137/46800\). One initial deterministic bit can be omitted. This gives dimension \(d_2=.80\), by \(2^4 14^5<25^5\), also after exact-composition conditioning. The certificate uses only upper transition probabilities and so allows the bit parity restriction to be chosen separately at each history.

### Explicit canonical-arc bands

Use the parameters of [CANONICAL_ARCS.md](CANONICAL_ARCS.md) and its endpoint counterpart, with
\[
 \eta=1/100,\quad \omega=1/1000,\quad \tau=1/4000,\quad
 N=8{,}000{,}010,\quad c_2=1/20{,}000{,}100 .
\]
Here \(r=\lfloor .96P/(2+\beta_*)\rfloor\) for dimers and \(r=\lfloor .96P/(1+\beta_5)\rfloor\) for two-gap words. In both cases \(P/3\le r\le P\) eventually. If a chunk passes the prefix deviation test with allowance \(P/1000\), its internal proportion differs from the relevant critical tilt by at most .003. The comparisons \(.709<\beta_*<.710\), \(.584<\beta_5<.586\) put its actual proportion in the four-copy certificate interval. Its physical length lies between \(.94P\) and \(.97P\) eventually. A suffix has at most \(.002P+O(1)\) excess binary logarithmic growth over its physical length, by the two coefficient formulas in the arc proofs. Thus its affine numerator is at most \(2^{.99P}\) eventually. A fixed signed sum of four has the required exponential margin as well.

At an unconditioned tilt within \(\tau\) of critical, the drift error across the entire chunk is at most \(P/4000\). A union bound over \(r\le P\) prefix lengths using Hoeffding at threshold \(P/2000\) bounds the bad probability by \(2P\exp[-P/2{,}000{,}000]\le\exp[-P/4{,}000{,}000]\) eventually. The selected chunks use at most \(NP\le N c_2 M<M/2\) macro slots; integer rounding leaves the specified two outer quarters for all sufficiently large \(M\). Fewer than four good chunks has unconditioned probability at most \(2^N\exp[-(N-3)P/4{,}000{,}000]\) with \((N-3)/4{,}000{,}000>2\log2\).

The signed rates at the guaranteed local length give \(.42\cdot .94>.38>.35\) in the dimer case and \(.80\cdot .94>.72>.67\) in the two-gap case. Use \(d_1=.38,d=.35\) for the source circle and \(d_1=.72,d=.67\) for the endpoint circle. These strict margins absorb polynomial type costs and bounded arc quantization costs on each band with \(P\ge c_1 M\). The near-unit-dimensional qualitative result uses larger moments for general \(d\); this explicit choice suffices for both survivor exponents.

### Explicit physical oversampling and entropy slack

Use \(e=10^{-9}\) for the relative extension of the word horizon and \(\eta'=10^{-13}\) for the high/low odd-count or total-gap slack. At every sufficiently large composition under consideration the required (possibly rounded or shifted by at most two bits) circle precision divided by its macro length lies between \(e/2\) and \(4e<c_2\). This follows from \(M\in[T/3-O(1),T]\) in the dimer construction and \(P=\lfloor\alpha(b-k)\rfloor\) in the two-gap construction.

For the dimer high group, the change in \(\beta=(2q-T-s)/(T-q)\) at its lower threshold is at most \(10\eta'+O(1/k)\) away from \(\beta_*\). Use the derivative \(1/(1-p)^2\le9+o(1)\) of \((2p-1)/(1-p)\) on the admissible range \(p\le2/3+O(1/T)\). On the small near-critical interval \(|(H_2(\beta)/(2+\beta))'|<2\), while above \(\beta_*\) this derivative is at most \(-1/3\), since \(H_2'(\beta)\le-1\) there. Similarly \(|H_2'(\beta)|<2\) near \(\beta_5\) and \(H_2'(\beta)\le-1/3\) above \(\beta_5\). For the far upper composition groups, their entropy losses of at least \(\tau/3\) absorb \(e\) and the stated saving. For the remaining high groups the printed \(C\eta'\) allowance in each transfer can thus be taken as \(100\eta'+O(1/k)\).

For a rational check of exponent sizes, the integer powers \(2^{158496}<3^{100000}<2^{158497}\) enclose \(\alpha\). Bounding \(H_2\) above by cross entropy at fixed \(.71,\ .585\) respectively gives
\[
        h_D\le 72581/225750<.322,\qquad
        h_5\le 24523/39624<.619 .
\]
The script checks the rational logarithm enclosures by integer powers. Therefore
\[
 \begin{split}
       (.35-h_D)e-100\eta'(1+e)&>5\cdot 10^{-12},\\
       \alpha(.67-h_5)e-100\eta'(1+e)&>5\alpha\cdot10^{-12}.
 \end{split}
\]
The margin absorbs all polynomial slice counts, all bounded rounding terms and the loss between \(2\gamma\) and \(\gamma\) in the final induction. The low group produces a strictly smaller scale because \(\eta'>0\) and \((1+e)\log_2(3/2)<1\) (forward) or \((1+e)\log_3(4/3)<1\) (backward). The small numerical size of this scale saving changes its onset, not the admissible exponent in the induction.

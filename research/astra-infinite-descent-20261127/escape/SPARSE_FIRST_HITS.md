# An elementary count for dilute physical first hits

Let \(T\) denote the shortcut Collatz map and \(y\) any positive odd integer with \(3\nmid y\). Let \(N_{\rm all}(m,d;y)\) count positive ternary-unit \(n\) with \(T^m n=y\) and \(d\) odd departures before time \(m\). Let \(N_{\rm first}\) count the same sources whose first visit is at \(m\). Here \(d\ge1\), including when \(y=1\). Fix \(L\ge3\) and let \(N_{\rm ann}\) count the first-hit sources satisfying
\[
 \frac{2^m}{3^d}\left(y-\frac{8}{5}2^{-L}\right)
        \le n\le \frac{2^m}{3^d}y.
\]
Without a mixing or density assumption,
\[
 { \lfloor(m-L-5d)/3\rfloor\choose d}
 \ \le N_{\rm ann}\le N_{\rm first}\le N_{\rm all}
 \ \le { \lfloor(m+5d)/3\rfloor\choose d}. \tag{1}
\]
An upper entry less than \(d\), including a negative upper entry, gives zero. Thus all three counts are \((1+o(1))(m/3)^d/d!\) uniformly in \(y\) when \((d^2+dL)/m\to0\). The annulus is tied to a specific grade and time.

Every positive odd target unit \(v\) has precisely two unit-preserving inverse exponents in each six consecutive integers. In fact the two possible values of \(2^e v\bmod9\) are \(4,7\), and 2 generates the six units. Each such \(e\ge1\) gives exactly one positive odd unit \(x=(2^e v-1)/3\) and one ordinary shortcut segment of length \(e\). Conversely if a unit source reaches \(v\) with one odd departure between consecutive odd states, its exponent is in this list. Starting at any cutoff \(E\ge1\), write the allowed exponents in increasing order, indexed by \(a=1,2,\ldots\). Splitting into consecutive six-element blocks gives
\[
 E+3a-6\le e(a)\le E+3a+2. \tag{2}
\]
The actual exponent at rank \(a\) depends on the current ordinary state, and the bounds are uniform in that state.

Read a rank tuple \((a_1,\ldots,a_d)\) outwards from \(y\). If the total exponent \(S\) is at most \(m\), take the resulting last odd source \(x\) and make the initial lift \(n=2^{m-S}x\). Its forward path has the required grade and clock. This construction is injective for a fixed rule for the cutoffs. Indeed the valuation of \(n\) recovers the initial lift, and the deterministic indices of the odd states in the remaining path recover all the exponents, states and ranks in reverse order. With unrestricted cutoff 1 this is a bijection onto every path counted in \(N_{\rm all}\). Since (2) yields \(S\ge3\sum a_i-5d\) there, the upper bound follows from the number \({R\choose d}\) of positive ordered rank tuples with \(\sum a_i\le R\), by the usual partial-sum bijection with \(d\)-subsets of \(\{1,\ldots,R\}\).

For the lower bound impose \(E=L\) on the first reverse gap and \(E=3\) on all subsequent gaps. By (2) the resulting sum is at most \(3\sum a_i+L+5d\). Every such odd inverse edge increases the ordinary value strictly, because \(2^e v>3v+1\) for \(v\ge1,\ e\ge3\). Hence every subsequent odd endpoint is larger than \(y\), all intermediate even integers differ from \(y\), and the constructed visit is a first hit. For \(S_i=e_1+\cdots+e_i\), the exact affine defect is
\[
 y-\frac{3^d n}{2^m}=\sum_{i=1}^d3^{i-1}2^{-S_i}
 \le 2^{-L}\sum_{j\ge0}(3/8)^j=\frac85\,2^{-L}.
\]
This proves the annulus lower bound and (1). For the asymptotic, write each binomial as a falling product. Across all \(d\) factors the total relative displacement from \(m/3\) is \(O((d^2+dL)/m)\), which proves the claim whenever this tends to zero.

The same argument gives the limiting distribution of the first reverse gap in this elementary range. Replacing the first unrestricted cutoff by \(L\) in the upper count yields the upper binomial with top \(\lfloor(m-L+5d+1)/3\rfloor\). For fixed \(d\) and \(L/m\to\lambda\in[0,1)\), the fraction of all first-hit sources with \(e_1\ge L\) tends to \((1-\lambda)^d\). For \(d\to\infty,\ d=o(\sqrt m)\) and \(Ld/m\to t\) it tends to \(e^{-t}\). Taking the remaining gaps at least 3 only changes either asymptotic by relative \(o(1)\). On those paths the defect is between \(2^{-e_1}\) and \((8/5)2^{-e_1}\). This places the sources in a shrinking physical interval immediately below the indicated monomial scale.

These are written integer counting arguments. The finite one-path inverse construction and its affine defect are checked in [InverseSpreading.lean](InverseSpreading.lean). A Fourier argument extends the pointwise fixed-clock counts and the defect distribution through polynomial sparse grade ranges in [SPARSE_TILT.md](SPARSE_TILT.md). The underlying inverse-word and initial-doubling dictionary is classical. [Wirsching](https://doi.org/10.3934/dcds.2003.9.771) · [Wren, §5](https://rstation.ai/problems/collatz/papers/10/v3).

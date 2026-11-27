# The tilted ternary scenery of a coherent ordinary spine

**PROPOSED.** Suppose \(a_n=U^n a\) is an ordinary escaping odd ray in a component \(C\). Assign grade \(g(a_n)=n\) and extend by \(g(Ux)=g(x)+1\). Use \(P\) from the [ordinary Hardy equation](ORDINARY_HARDY.md). Let \(S_n\) be the cumulative binary exponent from \(a\) to \(a_n\). On each grade \(v\), the ratios \(P(x)/P(x')\) are powers of two. Set \(M_t(x)=P(x)^{-t}\) for \(t>1\). This mass is summable on the whole physical component because \(P(x)>x\). The geometric ternary law \(\nu_t\) in the [Riesz transfer](RIESZ_TRANSFER.md) is defined for all these \(t\), regardless of its real drift. Write \(W_t=3^t/(2^t-1)\).

## The profile in every depth

For \(k\ge0\) define
\[
 A_{t,k}(z)=W_t^k\nu_t(z+3^k\mathbb Z_3),\qquad
 p_t(v)=\sum_{x\in C,\ g(x)=v}M_t(x).
\]
Put \(h_n(v)=0\) if \(v>n\), and otherwise \(h_n(v)=A_{t,n-v}(a_n)/P(a_n)^t\).
Then for all integers \(v\),
\[
 h_n(v)=\sum_{\substack{x\in\operatorname{Anc}(a_n)\\g(x)=v}}M_t(x).
\]
Here \(\operatorname{Anc}\) includes the root. Each compatible word is a unique ordinary positive source; its gain is \(P(a_n)/P(x)\). The source's grade fixes its unique depth. Since these ancestor sets increase to \(C\), the profiles increase pointwise and
\[
 \|h_n-p_t\|_{\ell^1(\mathbb Z)}
 =\sum_{x\in C\setminus\operatorname{Anc}(a_n)}M_t(x)\longrightarrow0.       \tag{1}
\]
This gives summability over all depth offsets and a simultaneous error bound on every subset of offsets.

## The entire conditional law of the next ternary digits

For each populated grade \(v\) fix a reference vertex \(c_v\), and write \(P(x)=2^{b_v(x)}P(c_v)\) on that grade. For all sufficiently large \(n\), the path from \(c_v\) to \(a_n\) has length \(n-v\). Write \(D_{n,v}\) for its total binary exponent. Put \(k=n-v\), restrict \(\nu_t\) to \(a_n+3^k\mathbb Z_3\), and push this restricted measure forward by
\[
                    z\longmapsto 2^{D_{n,v}}(z-a_n)/3^k.
\]
Multiply its mass by \(W_t^k/P(a_n)^t\), calling the resulting measure \(K_{n,v,t}\). With \(Z\) of law \(\nu_t\),
\[
 K_{n,v,t}
 =\sum_{\substack{g(x)=v\\x\in\operatorname{Anc}(a_n)}}M_t(x)
             \,\mathcal L\!\left(2^{-b_v(x)}(Z-x)\right).                  \tag{2}
\]
To prove (2), a length-\(k\) coding prefix \(w\) for \(x\) has total \(D_{n,v}+b_v(x)\) and probability \(\alpha_w^t/W_t^k\). Its image of a suffix \(Z\) differs from \(a_n=\phi_w(x)\) by \(3^k2^{-D_{n,v}-b_v(x)}(Z-x)\). The remaining coding letters are independent within that prefix. Summing all compatible alternatives proves (2) even when the prefix cells coincide. Consequently the measures increase to the full-grade mixture \(K_{v,t}\) obtained by dropping the ancestry condition. Their total-variation error is precisely the omitted grade mass. Equation (1) bounds the sum of the errors over every collection of grades for which the chosen reference paths have already met the target.

For \(v=0,c_0=a\), the word of a single fixed ordinary seed always contributes \(P(a)^{-t}\mathcal L(Z-a)\). This is a positive comparison of measures on **all** subsequent ternary digits. In unrecentered coordinates it holds at the end of a long run of zero ternary digits: the ordinary representative \(a_n\) is at most \((a+1)(3/2)^n\), by induction from \(U(x)+1\le3(x+1)/2\). Its highest nonzero ternary digit therefore lies below position \(n\log_3(3/2)+O_a(1)\), while (2) conditions to depth \(n\).

For each fixed \(v\), after only recentering by \(a_n\), the discarded rotation is multiplication by the ternary unit \(2^{-D_{n,v}}\). Thus every convergent subsequence of those units gives a weak limit by rotating \(K_{v,t}\), and every subsequential weak limit is of this form. Strong convergence in (2) is after applying the actual rotation. No continuity in total variation of rotations of a singular measure is used.

## Ordinary incidence inside the limiting scenery

Suppose \(c_0=a\) minimizes \(P\) over \(C\). Write \(P=P(a)\) and let \(\mathcal M=\{x:g(x)=0,\ P(x)=P\}\). This finite nonempty set contains all global minimizers: equality of two corrected heights forces equal odd grades. The normalized full-grade law satisfies, as \(t\to\infty\),
\[
                 P^t K_{0,t}\ \Longrightarrow\
                 \sum_{x\in\mathcal M}\delta_{-1-x}.                       \tag{3}
\]
By the dyadic grade property every other weight is \(2^{-t b_0(x)}\) with \(b_0(x)\ge1\). Their total tends to zero by dominated convergence, using \(t\ge2\) and \(\sum_x(P/P(x))^2<\infty\). For a fixed ternary depth \(j\), the first \(j\) tilted letters all equal one with probability \((1-2^{-t})^j\to1\). Their cell is \(-1+3^j\mathbb Z_3\), since \(\phi_1(-1)=-1\), proving \(\nu_t\Rightarrow\delta_{-1}\). The remaining terms yield (3). In fact the convergence persists jointly as \(n,t\to\infty\): every minimizer has joined \(a_n\) for all sufficiently large \(n\), while the same bound controls the nonminimal tail uniformly in \(n\). The atoms \(-1-x\) are ordinary negative even integers determined by the actual positive minimizers. These are limiting sceneries, not atoms of the individual tilted laws.

The pointwise first-hit bound (3) of the Riesz note gives finite total normalized depth mass at every nonperiodic positive target. On an escaping spine the mass in (1) stays concentrated on a translating profile; its value at offset zero stays positive despite the long zero suffix. To exclude it by a zero-digit estimate one would need an upper bound \(A_{t,n}(a_n)=o(a_n^t)\) on a subsequence, or an incompatible limit shape in (2). Existence of the limit shape does not give either restriction. The unrounded adaptive Green and maximum-gain total-current spectra previously characterized the positive limit values after summation or maximization over clocks. Here the individual depths and the full conditional ternary law are retained. [PR200 component current](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/ADAPTIVE_GREEN_COMPONENT_SPECTRUM.md) · [PR200 inverse gain](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/INVERSE_GAIN_ESCAPE_SPECTRUM.md).

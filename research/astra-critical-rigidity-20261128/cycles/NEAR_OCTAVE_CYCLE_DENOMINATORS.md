# Almost linear growth of the log denominator for narrow rational cycles

**Proposed written theorem.** Consider a primitive positive rational odd Collatz cycle, with real odd minimum \(m\), maximum \(X\), primitive odd period \(p\), complete reduced denominator \(q\) prime to six, and total division exponent \(A\). Write \(g=\gcd(A,p),\ P=p/g,\ a=A/g,\ \gamma=\log_2 3\). Use the bi-infinite genuine lifted sequence \(V_t=2^{E_t}x_t\) with \(E_0=0\), so \(V_{t+p}=2^A V_t\). Let \(r\) be the least degree of a nonzero polynomial over \(\mathbb Q\) annihilating \(V\) under chronological shifts, and put \(D=\min(r,m)\). The bounds below also hold with \(D=\min(P,m)\), an explicit choice requiring no computation of the annihilator.

Assume \(\mu(\gamma)\le\mu_0\), set \(\kappa=\mu_0-1\), fix \(\alpha>\kappa\), and suppose \(m\to\infty\) and
\[
               X/m\le 2^{1+\eta},\qquad 0\le\eta\ll(\log D)^{-\alpha}.
\]
Then for each \(\epsilon>0\),
\[
              \log(2q)\gg_{\epsilon,\alpha,\mu_0}
                           \frac{D}{(\log D)^{2\kappa+\epsilon}}.       \tag{1}
\]
Constants may also depend on the fixed coefficient in the width bound. If \(m\ge r(\log r)^{\kappa+\epsilon}\), then
\[
                     \log(2q)\gg
                           \frac{r}{(\log r)^{\kappa+\epsilon}}.       \tag{2}
\]
The analogous statement with \(P\) in place of \(r\) follows by taking the explicit lower degree only. For \(g=1\) one has \(r=p\). If \(g\) is a prime power, \(r\ge p/4\). In particular (1) is within powers of \(\log p\) of linear in \(p\) for every such family with \(m\gg p\). The complete raw denominator has at most \(O(p)\) logarithm for these widths and large minima, since it divides \(2^A-3^p\) and \(A/p\to\gamma\).

At any fixed width bound \(2<R<4\) there is also a fixed-order inequality. Put \(\eta=\log_2(R/2)\), \(L=\min\{i\ge1:\|i\gamma\|\le\eta\}\), and \(I_h=\log_2(4^h/\binom{2h}{h})\). For every \(2\le h<3^L\),
\[
           \liminf_{m\to\infty,\ X/m\le R}
                 \frac{\log(qm)}{\log D}
                    \ \ge\ \frac{\gamma h}{\eta I_h}.                  \tag{3}
\]
In particular the right side grows at least as a positive constant times \(3^L/(\eta L)\) when \(\eta\downarrow0\), taking the large-minimum limit at each fixed width. The prior full-denominator matched-grid theorem gives bounds of order \(1/\eta\) in this limit. Its hypotheses allow all positive cyclic valuation words and the same is true here. The present proof uses one local chronological set of shifts and an exact global polynomial relation. It does not require global geometric order among all rational sheets. [Earlier full-denominator bound](MATCHED_RATIONAL_DENOMINATORS.md) · [Fixed-rotation mismatch theorem](ALL_FIXED_ROTATION_DENOMINATORS.md) · [Classical BLS input](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) · [Modern exponent-three source](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md)

## The degree retained by the true cycle

The polynomial \(S^p-2^A\) annihilates \(V\); hence \(r\le p\). Write \(\xi=2^{a/P}\), and \(W_t=\xi^{-t}V_t\). This is a positive, \(p\)-periodic sequence. Its period is exactly \(p\): if \(W_{t+d}=W_t\) for every \(t\), then \(\xi^d=V_{t+d}/V_t\) is rational. Unique prime factorization and \(\gcd(a,P)=1\) imply \(P\mid d\), so \(\xi^d\) is an integral power of two. Comparing the powers of two in \(q x_{t+d}\) and \(q x_t\), both odd integers, gives \(x_{t+d}=x_t\) for all \(t\). Primitivity then implies \(p\mid d\).

Let \(\zeta=e^{2\pi i/p}\), and expand \(W_t=\sum_{k=0}^{p-1} b_k\zeta^{kt}\). Any rational annihilator \(J\) of \(V\) satisfies \(J(\xi\zeta^k)=0\) whenever \(b_k\ne0\), by Fourier uniqueness. The constant coefficient \(b_0>0\) forces \(J(\xi)=0\). This element generates \(\mathbb Q(2^{1/P})\) by Bézout using \(a,P\), so its degree is \(P\) by Eisenstein. In particular \(r\ge P\).

For \(g>1\), let \(\ell^v\) be any exact prime-power divisor of \(g\). The shift by \(P\) on \(W\) has order \(g\) since \(W\) has least period \(p\). The least common multiple of the orders of the \(\zeta^{kP}\) for \(b_k\ne0\) thus equals \(g\). Choose an active \(k\) for which \(d=\operatorname{ord}(\zeta^{kP})\) is divisible by \(\ell^v\). With \(z=\xi\zeta^k\), the identity \(z^P=2^a\zeta^{kP}\) puts \(K=\mathbb Q(\zeta^{kP})\) inside \(\mathbb Q(z)\).

Over the maximal abelian extension \(\mathbb Q^{\rm ab}\), the degree of \(z\) is at least \(P/2\). Indeed its root of unity is already in that field, and \(\xi\) generates the same extension as \(2^{1/P}\). Adjoining \(b=2^{1/P}\) there is a cyclic Kummer extension since every \(P\)-th root of unity is available; its Galois group acts by multiplication on \(b\). If its order is \(e\mid P\), then \(b^e=2^{1/(P/e)}\) belongs to \(\mathbb Q^{\rm ab}\). Its real field over \(\mathbb Q\) is therefore Galois. For \(P/e>2\) its Eisenstein minimal polynomial has nonreal roots, contradicting normality. Thus \(e\ge P/2\). Extending the base from \(K\) to \(\mathbb Q^{\rm ab}\) can only lower degree. We have proved
\[
                  r\ge[\mathbb Q(z):\mathbb Q]\ge
                   (P/2)\varphi(d)\ge (P/2)\varphi(\ell^v).
\]
For \(g=\ell^v\) this gives \(r\ge p/4\). This is the positive radical degree argument used in the [fixed-grade spectrum proof](../ordinary/DECIDABLE_FIXED_GRADE_SPECTRUM.md), applied here to active chronological modes.

Finally \(0<A/p-\gamma\le C/m\) follows by multiplying the true edge identities around the cycle. By the irrationality hypothesis, \(m\le P^{\mu_0+o(1)}\) as \(m\to\infty\), and \(P,D\to\infty\). Thus \(\log m=O(\log D)\) for either choice of \(D\). This also follows by applying \(\|P\gamma\|\gg P^{-\kappa'}\) for any fixed \(\kappa'>\kappa\).

## A short polynomial cannot give even one physical equality

For a positive \(U<r\), partition \(\{t\gamma\}\), \(0\le t<U\), into intervals of width at most \(v\) and comparable to \(v\), \(0<v<1/10\). Retain the most populated interval and subtract the smallest retained time \(t_*\). The resulting set \(\mathcal S\subset[0,U)\) has \(K\gg Uv\) elements. Write
\[
 k_s=\lfloor(t_*+s)\gamma\rfloor-\lfloor t_*\gamma\rfloor,\qquad
 D_s=2^{-k_s}\operatorname{shift}^s,\qquad z_s=3^s2^{-k_s}.
\]
Its log displacement satisfies \(|\log_2 z_s|\le v\). On the entire bi-infinite native cycle let \(F_i=\lfloor\log_2(V_i/J)\rfloor\), \(J=m\sqrt R\), using the fixed or moving upper width \(R\). Define
\[
                  Y_{i,s}=2^{-F_i}D_sV_i=C_{i,s}x_{i+s},
       \qquad C_{i,s}=2^{-F_i-k_s+E_{i+s}} .
\]
The logarithmic difference of \(Y_{i,s}\) from the common base \(2^{-F_i}V_i\) is \(O(v+U/m)\), uniformly in *every* \(i\), by summing the true log correction only over the forward \(s\) steps. If \(v+U/m=o(1)\), the inequalities \(Rm/2<J<2m\) with fixed margins give \(C_{i,s}\in\{1,2\}\), hence \(qY_{i,s}\in\mathbb Z\). A row can have both tags only when its base angle \(\{\log_2(V_i/J)\}\) belongs to a circle interval of length \(\eta+O(v+U/m)\). For \(1\le t<L\) the base angle increment equals \(t\gamma+O(L/m)\) modulo one. Consequently all rows with both tags are separated by at least \(L\) whenever the enlarged length plus the drift is strictly smaller than \(\min_{1\le t<L}\|t\gamma\|\). At \(L=1\) this needs no inequality. The labels and tags are \(p\)-periodic in \(i\) even though \(V_i\) is unfolded.

Suppose two different \(h\)-term multisets of actual normalized labels at one base \(i_0\) have equal sum, for some \(2\le h<3^L\). Cancel common occurrences, write \(c_s\) for the remaining signed multiplicities, and \(J_0(S)=\sum c_s 2^{-k_s}S^s\). This is a nonzero rational polynomial of degree \(<U<r\). With \(H_i=\sum c_sY_{i,s}\) and \(e_i=\sum c_s C_{i,s}\), the genuine equation is \(2^{F_{i+1}-F_i}H_{i+1}=3H_i+e_i\), \(qH_i\in\mathbb Z,\ |e_i|\le h\). If \(H_{i+1}=0\) at a variable row, the preceding \(L-1\) inactive rows give \(3^{L-1}\mid qH_i\), whence \(3^L\mid q e_i\). Coprimality of \(q\) with three forces \(e_i=H_i=0\). This backward step is immediate on an inactive row as well. The genuine cycle supplies as many guard dates as needed. From \(H_{i_0}=0\) we get \(H_i=0\) for every \(i\) by periodicity. Thus \(J_0(S)V=0\), contradicting its degree. Every chosen base label set is therefore \(B_h\), independently of the numerator heights and the size of the denominator.

Take \(n=\lceil\log_3(64hq m)\rceil+4\) genuine forward edges from any base, allowing arbitrarily many traversals of the actual lap. Encode each offset by its tags minus one at the variable dates. Coordinatewise equal \(h\)-sums of words force all \(n\) signed edge forcings to vanish, so \(2^{F_{i+n}-F_i}\mid qH_i\). The divisor is at least \(3^n/2\) and the full scaled height has absolute value at most \(4hmq\). Therefore the initial label sums agree, and the preceding argument recovers their multisets. The words are distinct, since equal individual labels at any base require equal odd physical states after comparing dyadic valuations; the distinct offsets are less than \(p\). The number of variable rows is \(\le1+n/L\). Applying the finite binary \(B_h\) Fourier inequality to this code gives
\[
       \log K\le\log h+\frac{1+n/L}{h}\log(2h+1),                     \tag{4}
\]
using \(\log(h!)/h\le\log h\) and \(\binom{2h}{h}\ge4^h/(2h+1)\). With \(k\) variable rows the more precise second term is \(kI_h(\log 2)/h\). [Gu, Proposition 3.8](https://arxiv.org/abs/1809.07364) · [Finite proof and full-denominator decoding](HIGH_ORDER_NATIVE_RESIDENCE.md)

## Choosing the angular resolution and additive order

For (3) choose \(U=\lfloor D/(\log D)^2\rfloor,\ v=(\log D)^{-2}\), so \(\log K=(1+o(1))\log D\); the fixed strict return gaps make the preceding proof applicable. Along any subsequence with \(\log(qm)/\log D\) bounded, \(n=O(\log D)=o(m)\); over the coding interval the true angle differs from an irrational rotation by \(O(n/m)=o(1)\). The number of variable rows is at most \((\eta+o(1))n\) by uniform rotation equidistribution and fixed interval enlargement followed by a limit. The precise version of (4) now gives (3). Subsequences of unbounded ratio with a finite liminf are handled by restricting to a bounded-ratio subsequence realizing that liminf. Finally \(I_h\le\log_2(2h+1)\) and \(h=3^L-1\) give the asserted fixed-width growth as \(L\to\infty\).

For (1), write \(x=\log D\), take \(\kappa'>\kappa\), \(u>1\), and \(c<\kappa+\epsilon/2\) such that
\[
                   u\kappa'<\min(\alpha,c).
\]
This is possible by taking the first two numbers sufficiently close to \(\kappa,1\), respectively. Use \(L=\lfloor x^u\rfloor,\ U=\lfloor D/x^c\rfloor,\ v=x^{-c}\). We have \(K\gg D/x^{2c}\), \(U<r\), and
\[
              \eta+v+(U+L)/m=o(L^{-\kappa'}).
\]
The gap test follows since \(\|t\gamma\|\gg_{\kappa'}t^{-\kappa'}\). Choose \(h=\lfloor K/4\rfloor\); then \(h\to\infty\), \(h<3^L\), \(\log(2h+1)\asymp x\), and \(\log K-\log h\ge\log4\). Formula (4) implies \(n\gg K L/x\gg K\). Subtracting \(O(\log(hm))=O(x)\) in the definition of \(n\) leaves \(\log(2q)\gg D/x^{2c}\). This proves (1) with its stated power.

Under the additional hypothesis in (2), use \(D=r\) and \(U=\lfloor r/2\rfloor\), while keeping \(v=x^{-c}\); indeed \(U/m=O(x^{-(\kappa+\epsilon)})\). Then \(K\gg r/x^c\) and the same proof gives (2). Replacing \(r\) by \(P\le r\) in all these choices proves the explicit reduced-clock assertions as well. Neither (1) nor (2) prescribes the number or pattern of mismatches under any rotation.

# Simultaneous Archimedean and predecessor restrictions on a dimer source

Throughout, the shortcut map is even division by two and odd division of \(3x+1\) by two. The odd map takes one odd source to the next, with exponent \(a=v_2(3x+1)\). Dimer words have blocks \(10,110\), equivalently odd-map exponents in \(\{1,2\}\) with no consecutive 1's. We use the actual canonical source
\[
 r(w)=[-3^{-u}C(w)]_{2^T},\qquad
 C(w)=\sum_{i:w_i=1}2^i3^{u-1-U_i},\quad U_i=\sum_{j<i}w_j.
\]
The proof of the joint estimate below adapts Weaver's mixed real and ternary separation to this dependent finite-state law. Weaver 73 already uses both a real and a ternary precision; our integral canonical representative and the ordinary backward dimer mask are the application here. [Weaver 73, §§2–4](https://rstation.ai/problems/collatz/papers/73)

## Joint law

Choose uniformly \(M\) ordered dimer blocks of exact composition \(j\) copies of \(110\); write \(T=2M+j, u=M+j\). Put \(\alpha=\log_2 3,\ p_*=1/\alpha,\ \beta_*=(2p_*-1)/(1-p_*)\). For each fixed \(0<d<1\), there are \(\tau,c_2>0\) such that, for any fixed \(0<c_1<c_2\), if \(|j/M-\beta_*|\le\tau\), and integers \(p,H\ge0\) satisfy
\[
               c_1M\le P=p+\alpha H\le c_2M ,
\]
then uniformly over circle arcs \(I\) of length \(2^{-p}\) and residue classes \(b\bmod3^H\),
\[
       \Pr\{r(w)/2^T\in I,\quad r(w)\equiv b\pmod{3^H}\}
                         \ll 2^{-dP}.                                  \tag{1}
\]
Here the finite constant and onset can depend on the fixed parameters. The onset is ineffective.

Use the chunks, good paths, exceptional-probability accounting and signed moment estimate from [the canonical arc proof](../phase6/CANONICAL_ARCS.md). Real \(P\) changes all chunk lengths by bounded rounding errors. Write \(B\) for one local ordinary affine numerator, \(m=T-L_0, a=U_0+v\) for its ambient exponents. In a fixed environment the local raw *integer* contribution to \(r(w)\) is \(2^{L_0}Z\), where \(Z=[-3^{-a}B]_{2^m}\). All raw contributions and a fixed exterior representative add modulo \(2^T\). Each normalized raw contribution is in \([0,1)\). With \(N\) chunks the total lift therefore needs at most \(N+2\) integer carry choices. This statement is deterministic.

Quantize this chunk into the discrete group \(\mathbb Z/3^H\mathbb Z\times\mathbb Z\) by
\[
     \big(2^{L_0}Z\bmod 3^H,\quad \lfloor 2^p Z/2^m\rfloor\big).
\]
The second coordinate has no wraparound. In a collision of two equal-sized sums of \(Q/2\) independent copies of this one chunk, the signed raw sum \(S=\sum\pm Z\) is a multiple \(3^H Z'\), and its ordinary size is at most \(Q2^{m-p}\). For \(D=\sum\pm B\) we obtain integers satisfying
\[
 D=2^m A-3^{a+H} Z',\qquad |D|\le Q2^{(1-\eta)P},
 \qquad |Z'|\le Q2^{m-P}.
\]
The good-chunk bound and fixed guards give \(2^m,3^a\ge2^P\); \(m,a,H=O(M)\). Fixed-place Subspace Theorem separation gives \(D=0\), exactly as in the linked proof with \(a+H\) substituted for \(a\). In particular the real, 2-adic and 3-adic form product is bounded by \(|D||Z'|2^{-m}\), and nonzero \(3^{a+H}Z'\) has absolute value at least \(2^P\). The signed moment bound then controls each conditional good submeasure's \(Q\)-fold energy. Fourier integration is on the compact dual of the displayed discrete group; finite support justifies inversion directly. Hölder bounds each atom of the convolution of \(Q\) such good measures.

Fix all other raw contributions. For a specified carry, the required ternary coordinate of their sum is fixed. The interval condition on the normalized raw sum restricts its integer quantization to at most \(Q+2\) cells for a real interval of length \(2^{-p}\); a circle arc can be split into two intervals. The at most \(N+2\) carry choices multiply the bound by a fixed constant. Use the same good/bad expansion, iid exceptional tail and global type conditioning as in the canonical arc proof. This proves (1), including \(p=0\) and \(H=0\).

## The exact backward mask

For every odd exponent history of \(H\) steps, the affine equation of that history is \(2^s y=3^H z+C\). Its target occupies exactly one formal residue modulo \(3^H\). Conversely, from a valid residue, its last exponent in \(\{1,2\}\) is forced modulo 3, and its penultimate endpoint is forced modulo \(3^{H-1}\) by \((2^a y-1)/3\). Iterating shows all \(2^H\) two-gap histories have pairwise distinct target residues. This recursion also constructs an odd positive predecessor history for any sufficiently large odd integer in the prescribed class: every division has an odd positive numerator and integral odd output. For positivity at the intermediate stages the lower threshold may depend on the finite history.

Restricting to exponent words with no consecutive 1's therefore gives exactly \(F_{H+2}\) formal target classes, where \(F_1=F_2=1\). Call their union \(E_H\). Finite backwards admissibility only supplies a necessary condition for a bi-infinite trajectory. For any arc and any translate of the mask, (1) gives
\[
  \Pr\{r(w)/2^T\in I,\ r(w)\bmod3^H\in b+E_H\}
   \ll 2^{-dp}\,3^{-(d-\log_3\varphi)H},\quad
                                 \varphi=(1+\sqrt5)/2.                 \tag{2}
\]
The condition concerns the canonical integer representative. An actual location shift of a source interval of width at most \(2^T\) introduces at most two translates since \(x=r(w)+t2^T\). No equidistribution at full precision is invoked.

## Strict ordinary count at the original time horizon

Write \(h_D=H_2(\beta_*)/(2+\beta_*)\), where \(H_2\) denotes binary entropy. There exists \(\gamma>0\) such that every interval of length \(X\ge2\) contains \(O(X^{h_D-\gamma})\) odd states with a bi-infinite ordinary dimer history. This proof takes **exactly** \(k\) forward shortcut steps at width \(2^k\), without oversampling the forward parity.

Indeed, for a factor of length \(k\) beginning at an odd state, use its parsing into \(M\) complete dimers and \(s\in\{0,1,2\}\) final 1's. The full odd count \(q=k-M\), and the complete blocks have \(j=k-s-2M\) second blocks. For each fixed \((q,s)\), the possible complete words number \(\binom Mj\). Their word length is \(T=k-s\). A width-\(2^k\) interval has at most \(2^s+1\) lifts per representative and at most \(2^s+2\) possible translates of the backward mask. Fix \(d>\log_3\varphi\) and take \(H=\lfloor\epsilon k\rfloor\) with fixed sufficiently small \(\epsilon>0\), \(p=0\). Near critical composition, (2) gains \((d-\log_3\varphi)\alpha\epsilon k+O(1)\) binary exponent. On this near-critical range the binomial count is at most \(2^{h_Dk+C\eta' k+O(1)}\) for \(q\ge p_* k-\eta' k\), since \(\beta=j/M\) is increasing with \(q\) and the entropy per physical bit \(H_2(\beta)/(2+\beta)\) decreases for \(\beta\ge\beta_*\). The fixed far-upper range has a strict entropy gap by the same monotonicity. Choose \(\eta'>0\) sufficiently small after \(\epsilon\), and absorb all polynomial factors.

For \(q<p_*k-\eta' k\), the actual image is in a fixed interval for that \(q\) of width at most \(3^q+(3/2)^k+1\le2^{(1-c)k}\) for a fixed \(c>0\) and all sufficiently large \(k\). This uses \(C(w)<3^k\) and the forward affine equation. Physical-time images are injective on odd dimer survivors. Each odd image remains bi-infinite in the dimer family, and an even image is twice an odd state in that family. Summing over \(O(k)\) values of \(q\) therefore gives the usual smaller-width induction, with a positive exponent margin. [Fixed-time injection and uniform interval induction](../phase5/INTERVAL_COUNTS.md)

The result here has the stronger bi-infinite premise; the one-sided strict saving is proved separately in [STRICT_DIMER_SAVING.md](../phase6/STRICT_DIMER_SAVING.md). At fixed total precision, spending one bit on the backward mask costs \(\log_3\varphi\) bits of possible target entropy, whereas a forward oversampling bit costs \(h_D\). Thus this proof alone gives no comparison of best attainable positive savings from the two methods.

## Compatibility at later cuts

In any specified admissible forward segment with a valid \(H\)-step past at its initial odd state, all internal odd states inherit their \(H\)-step past from the concatenation, provided the junction is admissible. If an internal state has at least \(H\) earlier odd steps inside the forward segment, its mask condition already follows from that segment alone. There is only one new left history in these finite-window tests. Multiplying the single-mask factor in (2) every \(H\) steps would count determined information repeatedly.

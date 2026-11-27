# The dual power saving for bi-infinite ordinary avoid-5 states

Let \(S_5\) consist of positive odd integers on bi-infinite ordinary Syracuse trajectories with division exponents only 1 and 2. This includes all cycles avoiding 5 modulo 8. With \(\alpha=\log_2 3\), \(\beta_5=\alpha-1\) and \(h_5=H_2(\beta_5)/\alpha=0.6177244\ldots\), there exist fixed \(\gamma_5>0\), \(K_5<\infty\) such that for every interval \(I\) of length \(X\ge1\),
\[
                       \#(I\cap S_5)\le K_5 X^{h_5-\gamma_5}.          \tag{1}
\]
The backward history remains an essential premise. As with the dimer saving, the imported fixed-place Subspace Theorem gives an ineffective onset.

### Signed moments for the two-gap input

A word with \(b\) odd steps and \(j\) gaps of size 2 has total physical length \(T=b+j\). Its complete physical blocks are \(A=1\), \(B=10\), and the uniform law at fixed \(j\) is the uniform order law for these blocks. The signed numerator bound in [MARKOV_MOMENTS.md](MARKOV_MOMENTS.md) holds with this change of dictionary, uniformly for \(j/b\) in any compact subinterval of \((0,1)\).

Indeed under iid macro bias \(\beta=j/b\) the first physical bit is 1. After 1, the next bit is 0 with probability \(\beta\) and 1 otherwise. After 0, 1 is forced. These transitions describe the emitted bits of the iid concatenation, with the pending gap choice exposed only when needed. The chain is irreducible and aperiodic because there is a state-1 loop. State 1 supplies the fresh coin, with \(|1-2\beta|<1\) uniformly on the compact parameter interval. The proof of (2) in [MARKOV_MOMENTS.md](MARKOV_MOMENTS.md) now applies with these two states, discarding at most one initial bit. Conditioning the first \(b\) macro letters to have exactly \(j\) long gaps costs at most \((b+1)^Q\). This proves the signed bound at every fixed dimension \(d_2<1\) with a sufficiently large even \(Q\).

### Canonical endpoint concentration

The relevant point of \(\mathbb R/\mathbb Z\) is now
\[
                Y=\frac{[2^{-T}C(w)]_{3^b}}{3^b}.
\]
The affine formula \(2^Ty=3^b z+C(w)\) puts every genuine odd endpoint \(y\) in the residue \(3^bY\bmod3^b\). For each \(0<d<1\) there are \(\tau,c_2>0\) such that, at any fixed shallow band \(c_1b\le P\le c_2b\), \(0<c_1<c_2\), uniformly over \(|j/b-\beta_5|\le\tau\),
\[
                \sup_{|J|=2^{-P}}\Pr(Y\in J)\ll 2^{-dP}.              \tag{2}
\]

Here are the changes to [CANONICAL_ARCS.md](CANONICAL_ARCS.md). Use chunks of \(r=\lfloor(1-4\eta)P/(1+\beta_5)\rfloor\) whole gaps. If \(J_i\) is the long-gap count through \(i\) letters, a good chunk has \(|J_i-\beta_5i|\le\omega P\) throughout. For each complete-gap segment,
\[
               \alpha U-L=-(\#B-\beta_5\#\text{gaps}).
\]
The own physical length \(\ell=r+J_r\) obeys \((1-6\eta)P\le\ell\le(1-3\eta)P\), and the suffix expansion of its numerator gives \(C_{\rm loc}\le2^{(1-\eta)P}\) exactly as in that note. The good-total bias range stays compact; the uniform bad-chunk tail is \(e^{-cP}\). Select enough disjoint chunks centrally and leave at least \(b/4\) unselected gaps at both ends. Fixing the exterior and the long-gap counts leaves independent uniform internal slices.

If \(L_0,U_0\) are the physical start and earlier odd count of a chunk with \(r\) odds, write \(m=T-L_0,\ a=U_0+r\). After the exact factor \(2^{L_0}3^{b-a}\) in the full numerator is removed, its contribution to the terminal circle is
\[
                     Y_{\rm loc}=[2^{-m}C_{\rm loc}]_{3^a}/3^a .
\]
All contributions add modulo one, including the fixed exterior. The padding gives \(2^m,3^a\ge2^P\), and \(m,a=O(b)\).

A collision of two \(Q/2\)-fold sums of good quantized outputs gives an integer \(A\) with \(|A|\le Q3^a2^{-P}\), representing the signed sum of the numerators of \(Y_{\rm loc}\) modulo \(3^a\). The signed local affine sum \(D\) therefore satisfies \(D=2^m A-3^a Z\), \(|Z|\ll_Q2^m\), \(|D|\le Q2^{(1-\eta)P}\). For \(X=2^mA,\ Y'=3^aZ\) take \(X-Y',X\) at infinity and the coordinate forms at 2 and 3. Their product is bounded by \(|D||A|3^{-a}\le Q^2 2^{-\eta P}\). Zero coordinates force \(D=0\); otherwise \(|D/X|\le Q2^{-\eta P}\) gives the diagonal after the fixed-place Subspace Theorem. This is the other small-coordinate alternative in Weaver 73, (11). The signed estimate on \(D=0\), Hölder on the good chunk subprobabilities, the iid tail for too many bad chunks, and global mode conditioning now give (2), with the same strict dimensional margins as in the source-circle proof. [Weaver 73, §2.3](https://rstation.ai/problems/collatz/papers/73), [Bilu, Theorem 2.3](https://www.numdam.org/item/AST_2008__317__1_0.pdf)

### Oversampling the backward history

In an interval \([a_0,a_0+3^k)\), choose \(b=k+\lfloor e k\rfloor\) preceding odd steps for each eligible target, with \(e>0\) small and fixed. At fixed total physical gap sum \(s\), the long-gap proportion is \(\beta=s/b-1\). Each of the \(\binom{b}{s-b}\) words determines at most one integer in the interval, because \(3^b>3^k\). To give any target its canonical endpoint must occupy the image of the interval divided by \(3^b\), of length \(3^{k-b}\le2^{-P}\) with \(P=\lfloor\alpha(b-k)\rfloor\).

Fix \(h_5<d<1\). Take \(e\) small enough that \(P\) lies in the linear band of (2). For \(s\ge\alpha b-\eta'k\), either \(\beta>\beta_5+\tau\), which gives a fixed raw entropy saving as \(H_2\) decreases for \(\beta>\beta_5>1/2\), or \(|\beta-\beta_5|\le\tau\) after \(\eta'\) is made small. In the latter case \(H_2(\beta)\le H_2(\beta_5)+C\eta'\). The arc-mass bound therefore counts at most
\[
                  O\bigl(2^{[H_2(\beta_5)+C\eta']b-dP}\bigr)
\]
per slice. Decrease \(e\) if necessary to preserve the fixed far-tail entropy gap, then choose \(\eta'\) small relative to \((d-h_5)e\). Since \(H_2(\beta_5)=\alpha h_5\), the bound summed over these \(O(k)\) slices is \(O(3^{(h_5-2\gamma_5)k})\) for some \(0<2\gamma_5<h_5\).

At each smaller \(s\), the predecessors \(z=(2^s y-C)/3^b\) occupy a translated interval of length at most \(2^s3^{k-b}+(4/3)^b+1\). We used \(C\le4^b-3^b\) from the two-gap restriction. The first term is at most \(3^k2^{-\eta'k}\); the second is a strict smaller power of \(3^k\) when \(e\) is small. These predecessors are in \(S_5\), and each determines its target by \(b\) forward odd steps. This gives the same strictly smaller scale recursion as in [STRICT_DIMER_SAVING.md](STRICT_DIMER_SAVING.md), proving (1). All arguments concern ordinary positive histories. This does not bound unrestricted one-sided avoid-5 starts by (1).

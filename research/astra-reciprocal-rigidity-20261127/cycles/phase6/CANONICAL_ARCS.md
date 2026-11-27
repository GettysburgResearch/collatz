# Small-arc concentration for the actual dimer source residue

Fix \(d<1\), \(d>0\), and write \(\beta_*=(2\log_32-1)/(1-\log_32)\). There are \(\tau>0\) and \(c_2>0\) such that, for every fixed \(c_1\in(0,c_2)\), the following holds at sufficiently large \(M\). Choose uniformly an ordering of \(M\) dimer blocks with \(j\) copies of \(110\), \(|j/M-\beta_*|\le\tau\). Write \(T=2M+j,\ u=M+j\). Define the normalized canonical source on \(\mathbb R/\mathbb Z\) by
\[
              R=\frac{[-3^{-u}C(w)]_{2^T}}{2^T}\pmod1 ,
\]
where brackets take the least nonnegative residue. If \(c_1M\le P\le c_2M\) is an integer, then
\[
       \sup_{\substack{I\ {\rm circle\ arc}\\|I|=2^{-P}}}
                                  \Pr(R\in I)\ll 2^{-dP}.              \tag{1}
\]
Constants and onset may depend on the fixed parameters, with an ineffective onset coming from the Subspace Theorem. Every ordinary source with these parity bits occupies the canonical residue \(2^T R\) modulo \(2^T\). The estimate is at shallow linear precision in the word length; it is compatible with sparsity of the full-precision support.

We use the signed finite-state input in [MARKOV_MOMENTS.md](MARKOV_MOMENTS.md). The arithmetic separation and the convolution strategy follow Weaver 28 v3 and Weaver 73, §§2–4. Both those papers treat the critically geometric gap law. Here the probability model is the exact dimer block composition and the additive group is the source circle alone. [Weaver 28 v3](https://rstation.ai/problems/collatz/papers/28), [Weaver 73, formulas (9), (11), (22)–(23)](https://rstation.ai/problems/collatz/papers/73)

### Arithmetic separation

Fix positive \(c,C,\eta,Q\). At all sufficiently large \(M\) the following implication holds. Let \(P,m,a\) be nonnegative integers with \(cM\le P\le CM\), \(m,a\le CM\), \(2^m,3^a\ge2^P\). If integers \(D,A,Z\) satisfy
\[
 D=2^m A-3^a Z,\quad |Z|\le Q2^{m-P},\quad |A|\le Q'3^a,\quad
                 |D|\le Q2^{(1-\eta)P},                               \tag{2}
\]
for a fixed \(Q'>0\), then \(D=0\).

To see this, for \(X=2^m A,\ Y=3^a Z\), take \(X-Y,Y\) at the real place and the coordinate forms at 2 and 3. Their product of absolute values is at most \(|D||Y|2^{-m}3^{-a}\le Q^2 2^{-\eta P}\). The maximum coordinate is \(e^{O(M)}\). If either coordinate vanishes, the lower bounds on \(2^m,3^a\) force \(D=0\) for large \(M\). Otherwise the fixed-place integral Subspace Theorem puts the vectors in finitely many rational lines. Since \(|D/Y|\le Q2^{-\eta P}\to0\), only the diagonal can persist. This is the real source case of Weaver 73, (11), at zero auxiliary ternary precision. [Bilu, *The many faces of the Subspace Theorem*, Theorem 2.3](https://www.numdam.org/item/AST_2008__317__1_0.pdf)

### Free middle blocks with fixed physical lengths

Choose \(d<d_1<d_2<1\) and a small \(\eta>0\) so that \(d_2(1-6\eta)>d_1\). Select the even number \(Q\) supplied by the signed moment theorem at exponent \(d_2\), uniformly over a fixed compact interval in \((0,1)\) containing \(\beta_*\) in its interior. A chunk consists of
\[
                  r=\left\lfloor\frac{(1-4\eta)P}{2+\beta_*}\right\rfloor
\]
macro letters. In a chunk let \(J_i\) count second blocks in its first \(i\) letters. Call the chunk good if \(\max_{0\le i\le r}|J_i-\beta_* i|\le\omega P\), for a fixed \(\omega>0\) small relative to \(\eta\). Its **own** length is \(\ell=2r+J_r\), and its own odd count is \(v=r+J_r\). For sufficiently small \(\omega\) and large \(P\),
\[
 (1-6\eta)P\le\ell\le(1-3\eta)P,\qquad C_{\rm loc}\le2^{(1-\eta)P}. \tag{3}
\]

Indeed every complete-block suffix of the chunk has second-block excess of magnitude at most \(2\omega P\). Its log-base-two slope \(\alpha U-L\), \(\alpha=\log_23\), equals \((\alpha-1)(\#B-\beta_*\#\text{blocks})\), using \(\alpha(1+\beta_*)=2+\beta_*\). Cutting a suffix inside a block costs at most a constant in this estimate. The term starting at physical position \(i\) in \(C_{\rm loc}\) is bounded by \(2^{\ell+2|\alpha-1|\omega P+O(1)}\), by writing its exponent as \(\ell\) plus the slope excess of its terminal segment. Summing at most \(\ell\) terms gives (3).

Under the unconditioned iid macro law with \(\Pr(B)=\beta'\) and \(|\beta'-\beta_*|\le\tau\), choose \(\tau\) small so that \(|\beta'-\beta_*|r\le\omega P/2\). The maximal binomial deviation bound, or a union bound over the \(r\) prefix lengths and Hoeffding's inequality, gives probability at most \(e^{-c_3 P}\) for a bad chunk, with fixed \(c_3>0\). At any good total \(J_r\) the value \(J_r/r\) lies in the compact interval used for the signed estimate.

Choose a fixed \(N\ge Q\) large enough that \(c_3(N-Q+1)>2\log2\). Now choose \(c_2>0\) small enough to place \(N\) disjoint, consecutive chunks of \(r\) macro letters centrally, leaving at least \(M/4\) macro letters on both sides. Also require \(c_2<1/8\). Condition on the macro letters outside these chunks and each chunk's second-block count. The internal arrangements are then independent uniform slices. For a given chunk, let \(L_0,U_0\) be its physical start index and earlier odd count. In the full numerator its coefficient is \(2^{L_0}3^{u-U_0-v}\). Consequently its **actual additive contribution** to \(R\) on the circle is
\[
        R_{\rm loc}=\frac{[-3^{-a}C_{\rm loc}]_{2^m}}{2^m},
        \qquad m=T-L_0,\qquad a=U_0+v .                              \tag{4}
\]
The contributions of all selected chunks and a fixed exterior add modulo one. This uses ordinary congruence addition, with no independent-carry assumption. The ambient exponent \(m\) includes the unselected suffix and differs from the local length \(\ell\) in (3). The exponent \(a\) includes the unselected prefix. The two margins ensure \(2^m,3^a\ge2^P\); all exponents are \(O(M)\).

### Moment separation and averaging

In the fixed environment restrict a chunk measure to its good internal words, as a subprobability. Quantize (4) into the group \(\mathbb Z/2^P\mathbb Z\) by \(\lfloor2^P R_{\rm loc}\rfloor\). A collision of two sums of \(Q/2\) independent copies gives a signed sum of the real circle contributions of distance at most \(Q2^{-P}\) from zero. Choosing a representative \(Z\) of the signed sum of the numerators of (4) modulo \(2^m\) gives \(|Z|\le Q2^{m-P}\). With \(D\) the corresponding signed sum of \(Q\) local affine numerators, the congruence in (4) gives \(D=2^m A-3^a Z\) for some integer \(A\). Equations (3) bound \(|D|\le Q2^{(1-\eta)P}\), and the equation gives \(|A|\le 2Q3^a\) eventually. The separation lemma forces \(D=0\).

The signed estimate (1) of [MARKOV_MOMENTS.md](MARKOV_MOMENTS.md) bounds the probability of \(D=0\), dropping the good-word restrictions, by \(O(2^{-d_2\ell})\ll 2^{-d_1 P}\). A chunk with no good words has zero subprobability and already satisfies this bound. Normalized Fourier summation on \(\mathbb Z/2^P\mathbb Z\) now gives \(\int|\widehat\mu|^Q\ll2^{-d_1P}\) for every quantized good chunk measure \(\mu\). For any \(Q\) different good chunk measures, Hölder and inversion bound every convolution atom by \(O(2^{-d_1P})\). If their real sum on the circle falls in a fixed arc of length \(2^{-P}\), the sum of their quantized coordinates belongs to at most \(Q+2\) cells. Further independent subprobability convolutions and arbitrary translations preserve the arc bound up to this constant.

Expand the \(N\) conditional measures into good and bad parts. Terms with at least \(Q\) good parts obey the arc bound; there are at most \(2^N\) terms. Average the remaining terms over the iid law **before** imposing the global composition. The chance of \(N-Q+1\) or more bad chunks is at most \(2^N e^{-c_3P(N-Q+1)}\), since these events use disjoint iid macro letters. Finally take \(\beta'=j/M\) and condition its global count to be \(j\), of probability at least \(1/(M+1)\). The resulting polynomial factor is absorbed in the margin \(d_1-d\), since \(P\ge c_1M\). This proves (1).

# Fixed block dictionaries and the positive-entropy \(\{2,12\}\) family

Use a fixed finite alphabet of nonempty binary blocks \(A_i\), \(1\le i\le J\), with shortcut lengths \(l_i\), odd counts \(u_i\), and affine intercepts \(c_i\). Build a word by arranging \(m\) labelled blocks uniformly with prescribed multiplicities \(m_i\) satisfying \(m_i/m\ge\epsilon>0\). Its total binary length \(n=\sum m_i l_i\), total odd count \(u=\sum m_i u_i\), and determinant \(D=|2^n-3^u|\) are fixed across the stratum. Assume \(0<u<n\). Counts may vary with \(m\). The probability space consists of arrangements of labelled blocks. Different arrangements need not be distinguished as binary strings unless a coding or parsing guarantee is also available.

Write
\[
 \kappa_{ij}=C(A_jA_i)-C(A_iA_j)
       =(3^{u_i}-2^{l_i})c_j+(2^{l_j}-3^{u_j})c_i .
\]
Its sign convention will have no effect on the laws. Let \(H=\gcd_{i,j}|\kappa_{ij}|\). It is positive exactly when some pair of blocks fails to commute as binary words. Indeed both concatenations have the same total length and weight, and affine numerator injectivity at those two fixed counts detects equality. If \(H=0\), every pair commutes, so all arrangements give exactly the same binary word and numerator. In what follows assume \(H>0\). Choose any arrangement in the stratum, with full numerator \(c_*\).

**Theorem.** For every modulus \(g\) coprime to 6, let \(h_g=\gcd(g,H)\). For every \(a\bmod g\),
\[
 \left|\Pr(C=a\bmod g)-
              {\bf1}_{a=c_*\bmod h_g}\frac{h_g}{g}\right|
       \le C e^{-c\sqrt m}.                                           \tag{1}
\]
Constants depend only on the fixed dictionary and the lower frequency bound. If \(R\) is uniform on residues modulo \(D\) with \(R\equiv c_*\pmod {h_D}\), then
\[
 d_{\rm TV}({\cal L}(\gcd(C,D)),{\cal L}(\gcd(R,D)))
                  \ \le C e^{-c\sqrt m}.                              \tag{2}
\]
In particular the full reduced denominator \(D/\gcd(C,D)\) has the model obtained by projecting that uniform coset, and
\[
 \mathbb E\log\gcd(C,D)
  =\sum_{\ell^e\mid D}(\log\ell)\,
     {\bf1}_{h_{\ell^e}\mid c_*}\frac{h_{\ell^e}}{\ell^e}
       +O(m e^{-c\sqrt m})=O(\log(m+2)).
\]
As in [DENOMINATOR_LAW.md](DENOMINATOR_LAW.md), the sum uses prime powers. This theorem includes short local obstructions like a fixed prime dividing every swap difference. The choice of \(c_*\) does not change any model probability: exchanges of neighboring blocks connect all arrangements, and change every full numerator by a multiple of \(H\).

## Proof of the coset law

Choose macro letters independently with probabilities \(p_i=m_i/m\), then condition on their multiplicities. The conditioning event has probability at least \((m+1)^{-J}\). Indeed the target is a multivariate binomial mode: if a different occupation vector has \(m'_i>m_i\) and \(m'_j<m_j\), moving one count from \(i\) to \(j\) multiplies its mass by \((m'_i/(m'_j+1))(m_j/m_i)>1\). There are at most \((m+1)^J\) possible count vectors.

Group the macro sites in consecutive pairs, omitting a terminal singleton when necessary. Given the unordered pair contents and the singleton, the orientations of unequal pairs are independent and fair. For a nontrivial character \(k\bmod g\), the characters with \(g\mid kH\) are constant on the support, at the value \(\exp(2\pi i k c_*/g)\). Those are precisely the characters of the fixed coset's annihilator.

For any other character choose a target pair \(A_i,A_j\) with \(g\nmid k\kappa_{ij}\). At pair-start \(b\) let \(P_b,U_b\) be the accumulated binary length and odd count. Define the nonzero modular frequency
\[
 K_b=k\kappa_{ij}2^{P_b}3^{u-U_b-u_i-u_j}\pmod g
\]
also on the unconditioned process, using modular inverse powers if required. The phase change on that actual target pair at total weight \(u\) is \(K_b\). Every pair, including those of other types, advances the frequency by
\[
               3^{v_b}K_{b+1}=2^{t_b}K_b\pmod g,
\]
where \(t_b,v_b\) are its total binary length and odd count. Both are predictable after that pair's unordered contents are learned; \(t_b\ge2\) and \(t_b,v_b\le2L_*\) for \(L_*=\max l_i\). Define \(M_*=2(2^{2L_*}+3^{2L_*})\). For \(1+\lceil\log_4 g\rceil\) consecutive pair-starts, all centered representatives cannot have magnitude below \(g/M_*\). If so all transitions are exact integer equalities and their product implies \(4^{\lceil\log_4 g\rceil}\mid K_{\rm last}\), which contradicts its nonzero small magnitude.

The first frequency outside that small interval in each group is determined by earlier pairs. The actual unordered pair there is the target pair with probability \(2p_ip_j\ge2\epsilon^2\). On this event the fair orientation reduces the Fourier product in absolute value by a factor at most \(\cos(\pi/M_*)\). All other orientations contribute factors of absolute value at most one. The proof of (5) in [DENOMINATOR_LAW.md](DENOMINATOR_LAW.md) now gives
\[
 |\widehat\mu_g(k)|
    \le (m+1)^J [1-2\epsilon^2(1-\cos(\pi/M_*))]^{
       \lfloor\lfloor m/2\rfloor/(1+\lceil\log_4g\rceil)\rfloor}
\]
for every character outside the annihilator. Fourier inversion yields (1) for \(g\le e^{\sqrt m}\).

For larger moduli fix one noncommuting pair type \(A_i,A_j\), independent of the character. In an initial segment of \(s=\min(\lfloor m/2\rfloor,\lfloor\log_3g/(2L_*)\rfloor)\) complete macro pairs, reveal all unordered contents and all other data including the orientations of nontarget pairs. With \(b\) target pairs, their \(2^b\) orientation choices give distinct binary strings, since the two orientations differ within disjoint equal-length physical intervals. All have identical physical length and weight, and their block numerators are distinct and smaller than \(3^{2sL_*}\le g\). Every outside contribution is fixed, and the local multiplier is a unit mod \(g\). Hence at most one set of these fair orientations yields a prescribed residue. Under the iid model \(b\) has the binomial law with parameter \(2p_ip_j\) at \(s\) trials. The mean of \(2^{-b}\) is \((1-p_ip_j)^s\). Conditioning the counts costs at most \((m+1)^J\). This bounds the mass at any residue by \(O(e^{-c\sqrt m})\), while \(h_g/g\le H/g\) satisfies the same bound. This proves (1) in all cases.

For every \(g\mid D\) the proposed coset model has \(\Pr(g\mid R)={\bf1}_{h_g\mid c_*}h_g/g\) by the Chinese remainder theorem. This is at most \(H/g\). The truncated inclusion–exclusion proof of [DENOMINATOR_LAW.md, §4](DENOMINATOR_LAW.md) applies verbatim with this actual model, multiplying its upper remainder estimates by at most the fixed \(H\). Also \(\log D=O(m)\). This proves (2) and the expected logarithmic cancellation. Conditioning on primitive macro arrangements changes invariant statistics by an exponentially small amount. Each imprimitive macro type of repetition order \(j\ge2\) has at most \(e^{(m/j)H(\mathbf p)}\) arrangements, while the total multinomial type has at least \(e^{mH(\mathbf p)}/(m+1)^J\).

## A positive-entropy critical family with no local correction

Take Syracuse exponent tokens \(2\) and \(12\), whose shortcut strings are \(A=10\), \(B=110\). Their lengths are 2, 3, their odd counts 1, 2, and \(c_A=1,\ c_B=5\). Thus \(\kappa_{AB}=-6\). Every \(D\) is prime to 6 and \(h_D=1\). Formula (2) gives the uncorrected \(\varphi(e)/D\) distribution for reduced denominator \(e\mid D\). Each macro block ends in its sole zero, so the zero sites delimit the macro parsing uniquely on the circle. A binary word in this family has a proper binary period if and only if its macro necklace has a proper macro period. Uniform primitive macro necklaces therefore give the same distribution for the corresponding primitive binary necklaces.

If \(b\) of the \(m\) symbols are \(B\), the complete type is \(n=2m+b,\ u=m+b\). Its odd density approaches the critical \(\log_3 2\) when \(b/m\to(2\log_3 2-1)/(1-\log_3 2)\), strictly between zero and one. Positive determinant requires choosing the side with \(3^u<2^n\). This family was singled out as a positive-entropy cycle exclusion challenge. Its denominator law here is statistical and allows individual ordinary exceptions. [rStation discussion of the \(\{2,12\}\) family](https://rstation.ai/r/collatz/posts/44)

## A stratum with a forced factor of seven

For \(A=1\), \(B=000\), the sole swap magnitude is \(H=7\). Take six \(A\)'s and three \(B\)'s. All 84 labelled arrangements have \(n=15,\ u=6,\ D=32039=7\cdot4577\). The arrangement \(A^6B^3\) has \(C=3^6-2^6=665\), divisible by 7. Thus every arrangement has \(7\mid C\), while a uniform residue would have this probability \(1/7\). More generally \(m_A\equiv0\bmod6\) gives \(7\mid D,C\) for every arrangement, for arbitrary positive \(m_B\). Both multiplicities can grow at positive rates. The coset correction survives at all scales.

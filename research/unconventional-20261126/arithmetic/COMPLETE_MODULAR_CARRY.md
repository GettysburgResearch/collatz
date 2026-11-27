# Which simultaneous local cancellations can a primitive positive cycle realize?

**Status.** Proposed written theorems for review. We classify all finite-modulus carry conditions at any prescribed common divisor of the clocks. The realizers are positive **rational** cycles with quadratically growing minima and exponentially large reduced denominators. A separate restriction bounds the total cancellation for a localized perturbation. Positive ordinary cycle exclusion remains open.

For positive odd phases use \(2^{e_i}x_{i+1}=3x_i+1\), with exact integers \(e_i\ge1\). Put
\[
 E_0=0,\quad E_j=\sum_{i<j}e_i,\quad A=E_p,\quad
 D=2^A-3^p,\quad C=\sum_{i<p}3^{p-1-i}2^{E_i}.
\]
For \(D>0\) the cyclic word gives the positive fixed point \(C/D\). Every rotated carry is odd, as is \(D\). The cyclic affine identities then prove the precise odd valuations and equality of the reduced denominators across all phases. Write \(G=\gcd(D,C)\) for the cancellation and \(d=D/G\) for the actual reduced denominator. Ordinary realization requires \(d=1\).

**Theorem MC1.** Fix an integer \(M>1\) prime to six, a positive integer \(g\), and any residue \(h\bmod M\). Let \(U_M=\langle2,3\rangle\subseteq(\mathbb Z/M)^\times\). Write its invariant factors as \(C_u\times C_v\) with \(u\mid v\), permitting \(u=1\). The following are equivalent.

1. \(u\mid g\).
2. There are positive clocks with \(\gcd(A,p)=g\) and \(M\mid 2^A-3^p\).
3. Infinitely many primitive positive rational cycles of unbounded least odd period \(p\) satisfy, at a specified phase,
\[
 \gcd(A,p)=g,\qquad M\mid D,\qquad C\equiv h\pmod M,\qquad
 A-p\log_2 3\asymp_{M,g}p^{-1}.
\]
Every phase of these cycles has real size \(\asymp_{M,g}p^2\), and their full reduced denominators satisfy
\[
                 \log d=p\log3-o(p).
\]

With \(h=0\), every prime power in \(M\) cancels simultaneously. With other \(h\), it is \(\gcd(M,h)\) that is guaranteed to cancel. The asymptotic concerns the actual reduced denominator after **all** numerical cancellation, including primes not named in \(M\).

### 1. The clock obstruction is exact

Write \(A=ga,p=gs\) with \(\gcd(a,s)=1\). Modulo \(M\), the relation \((2^g)^a=(3^g)^s\) and Bézout give one common generator for \(2^g,3^g\): if \(bs+ca=1\), the unit \(z=(2^g)^b(3^g)^c\) obeys \(z^s=2^g,z^a=3^g\). Thus the subgroup of \(g\)-th powers of \(U_M\) is cyclic. Its invariant factors are \(u/\gcd(u,g)\) and \(v/\gcd(v,g)\), in divisibility order, so this happens exactly when \(u\mid g\).

Conversely suppose \(u\mid g\). Choose a generator \(z\) of \(\langle2^g,3^g\rangle\), of order \(L\), and integers \(s_0,a_0\) with \(z^{s_0}=2^g,z^{a_0}=3^g\). The two powers generate the entire group, so \(\gcd(s_0,a_0,L)=1\). The trivial group uses \(L=1\). Every pair \((a,s)\equiv(a_0,s_0)\bmod L\) satisfies the clock congruence.

For completeness we reconstruct the primitive near-critical choice for this arbitrary residue pair. Let \(P/Q>\alpha=\log_2 3\) be any sufficiently late upper continued-fraction convergent, with preceding lower convergent \(P'/Q'\). Then \(PQ'-P'Q=1\), and \(0<P-Q\alpha<1/Q\), \(0<Q'\alpha-P'<1/Q\). The vectors \(v=(P,Q)\), \(w=(P-P',Q-Q')\) are a unimodular basis. Write the target residue in that basis as \(b_0v+c_0w\bmod L\). No prime dividing \(L\) divides both coefficients. Choose \(1\le b\le L\) representing \(b_0\). Let \(K\) be the product of the primes dividing \(b\) but not \(L\). Choose \(1\le c\le LK\le L^2\) with \(c\equiv c_0\bmod L\), \(c\equiv1\bmod K\). Then \(\gcd(b,c)=1\). Put \((a,s)=bv+cw\). This is primitive, has the required residues, and satisfies
\[
 Q\le s\le2L^2Q,\qquad \frac{1}{Q}<a-s\alpha<\frac{3L^2}{Q}.
\]
Indeed \(aQ-sP=c>0\); the upper bound follows from the two convergent errors. Thus the total excess is \(\asymp_{M,g}1/p\). This adapts the congruence construction in [R1](ROUGH_DENOMINATORS.md) and needs no assertion about prime denominators of approximants.

### 2. How many carry residues can be specified at fixed clocks?

If a set \(J\subseteq\{1,\ldots,p-1\}\) of selected odd dates is advanced by one, so that \(E'_i=E_i+1_{i\in J}\), the exact difference of carries is
\[
                  C'-C=\sum_{i\in J} 3^{p-1-i}2^{E_i}.                 \tag{1}
\]
Each summand is an additive generator modulo \(M\), since it is a multiplicative unit. In any list of \(M-1\) such changes the subset sums cover every residue. Starting from \(S=\{0\}\), the next unit \(b\) replaces \(S\) by \(S\cup(S+b)\). Failure to enlarge a proper nonempty finite set would make it invariant under the additive generator \(b\), impossible. This proves the assertion without a common increment assumption.

**Theorem MC2 (finite pointwise capacity).** At *every* pair of clocks with \(3p/2<A<2p\), every \(M>1\) prime to six with \(M\le2p-A\), and every \(h\bmod M\), there is a primitive gap word with these clocks and \(C\equiv h\bmod M\). If \(M\mid D\) and \(h=0\), the entire modulus cancels. Positivity of the rational cycle requires the additional \(D>0\).

Start with the cyclic mechanical dates \(E_i=\lceil iA/p\rceil\). The gaps are ones and twos, with no consecutive ones, since the sum of two consecutive gaps is at least \(\lfloor2A/p\rfloor\ge3\). There are \(2p-A\) ones, hence exactly \(2p-A\) cyclic centers with incoming/outgoing pair \(12\), and \(2A-3p>0\) centers with pair \(22\). Rotate to put a \(22\) center at date index 1. Force its date forward one, creating an incoming 3 and an outgoing 1. As free switches take any original \(12\) center except the seam index 0. Index 1 was a \(22\); index 2 cannot have incoming 1. No two \(12\) centers are adjacent. Therefore the free switches act on disjoint gap pairs and avoid the forced pair, changing each selected \(12\) into \(21\). The unique 3 proves that the gap word is primitive. At least \(2p-A-1\) free switches remain. Use (1) after the forced change and the subset-sum argument. The span of every rotated cumulative clock about its linear profile is less than two bits regardless of the number of switches, since the date error over the original mechanical dates lies in \(\{0,1\}\). This finite result allows a different modulus at each pair of clocks. It gives no bound on unspecified cancellations.

### 3. A two-coordinate restriction on complete cancellation

Take the **unrotated** upper dates \(E_i=\lceil ia/s\rceil\) on \(p=gs\) phases. For \(0\le i<s\) let \(r_i=sE_i-ai\), a permutation of \(0,\ldots,s-1\). Choose a nonempty set \(J\subseteq\{1,\ldots,s-1\}\), entirely within the first lap, and advance only the dates in \(J\). Assume the resulting gaps are positive. Put \(T=\max J\), \(R=1+\max_{i\in J}r_i\), \(t=|J|\), and assume \(1<a/s<2\), \(D_0=2^a-3^s>1\), \(H=D/D_0\).

**Theorem MC3.** For any integer \(1\le N<s\), the complete cancellation of this word satisfies, with an absolute constant,
\[
 \log G\ \le\ O(T+\log(1+t))
       +O(RN)+\frac{s}{N}\log(g+2t).                                  \tag{2}
\]
The first term bounds \(\log\gcd(H,C')\); the other two bound \(\log\gcd(D_0,C')\). The latter bound may also be replaced by \(\log D_0\). This distinction matters when the common clock divisor grows. No coprimality between \(H\) and \(D_0\) is required.

Indeed the base word consists of \(g\) identical laps, so its carry is \(H\) times the single-lap carry. In (1), pull out \(3^{p-1-T}\); the remaining positive integer is at most \(t3^T2^{2T}\), since \(E_i\le2i\). The extracted power is coprime to \(H\), giving the first term. Positivity of (1) prevents exact disappearance of this residual.

Modulo \(D_0\), use \(z^s=2,z^a=3\) from the coprime-clock Bézout formula. A base term after removing the unit \(3^{p-1}\) equals \(z^{r_i}\); all ranks occur \(g\) times. The relation \((z-1)(1+z+\cdots+z^{s-1})=1\) gives
\[
 \gcd(D_0,C')=\gcd(D_0,F(z)),\qquad
 F(X)=g+(X-1)\sum_{i\in J}X^{r_i}.
\]
Both the degree bound \(\deg F\le R\) and coefficient norm \(\|F\|_1\le g+2t\) hold. The residues \(r_i\) are distinct. For \(0<x<1\) their finite sum is strictly less than \((1-x)^{-1}\), and for \(x\ge1\) the correction is nonnegative. Hence \(F(x)>0\) on the entire positive real axis.

We give the short resultant step because \(F(0)\) need not be a unit when \(g>1\). Pigeonhole on the circle for the \(N+1\) residues \(ja/s\), \(0\le j\le N\), produces \(|v|\le N\), \(v\ne0\), and \(u\) with \(0<|su+av|\le s/N\), \(|u|\le2N+1\). The lower inequality uses \(N<s\) and coprimality. Divide \((u,v)\) by their gcd and reverse signs if necessary to get \(q=su+av>0\). Write the positive rational \(2^u3^v=d_1/c_1\) in lowest terms. The binomial \(c_1X^q-d_1\) vanishes at \(z\bmod D_0\). It is irreducible over \(\mathbb Q\): if the positive root \(\theta\) has degree \(k\), taking the field norm of \(\theta^q=2^u3^v\) gives \(q\mid ku,kv\) via its valuations at 2 and 3. Therefore \(q\mid k\), since \(\gcd(u,v)=1\), and \(k=q\). Since \(F(\theta)>0\), the integral resultant is nonzero. Its Bézout identity shows that it is divisible by \(\gcd(D_0,F(z))\), even at composite moduli or repeated prime powers. Each complex binomial root has modulus \((d_1/c_1)^{1/q}\), so the absolute resultant is at most
\[
              \max(c_1,d_1)^R\|F\|_1^q .
\]
This gives (2), since \(\log\max(c_1,d_1)=O(N)\) and \(\gcd(ab,c)\le\gcd(a,c)\gcd(b,c)\). The coprime discrepancy mask and prior short-binomial bound for monic subproducts already appear in [PR mask-denominator, §§1–2a](https://github.com/GettysburgResearch/collatz/blob/a5c0eaa979170ff0ba8f85809cb904e78e657ccd/research/astra-ordinary-boundary-20261124/arithmetic/README.md). Here one estimates both integer factors of the actual denominator after destroying repeated laps.

### 4. Attaining all residues with negligible total cancellation

Use the unbounded clocks of §1, keeping \(g,M\) fixed. In the first lap one can select \(M\) distinct dates \(1\le i<s\) with both \(\max i=o(s)\) and \(\max r_i=o(s)\). For each desired precision \(1/k\), the irrational rotation gives \(M\) distinct fixed positive indices with \(0<\{-i\alpha\}<1/k\). As \(a/s\to\alpha\) these same indices have \(0<r_i/s=\{-ia/s\}<2/k\) for every sufficiently late clock, and their maximal index is below \(s/k\). Use successively growing thresholds for \(k\) to obtain both little-oh assertions along the same sequence.

At such slots the two original gaps are \(12\). In detail, \(r_i<\min(a-s,2s-a)\) eventually, so the predecessor rank equals \(r_i+a-s\), giving incoming gap 1, and the successor rank equals \(r_i+2s-a\), giving outgoing gap 2. All these switches are disjoint. Force one of them, and use the remaining \(M-1\) to obtain the required residue \(h\). The switch set \(J\) is nonempty and still lies in the first lap.

A proper period \(b\mid p\) of the changed word would have total exponent \(bA/p=ba/s\) over that period; integrality forces \(s\mid b\). Both changed and base cumulative dates would then increase by the same amount across \(b\) positions. Their difference \(1_{i\in J}\) would be \(b\)-periodic, impossible for a nonempty support confined to one lap of length \(s\): for \(i\in J\), \(i+b<p\) and \(i+b\) is outside that lap. For \(g=1\), no proper multiple of \(s\) divides \(p\). This proves physical least odd period \(p\).

In (2) choose \(N=\max(1,\lfloor\sqrt{s/R}\rfloor)\) once \(s\) is large. Since \(R=o(s)\), \(T=o(s)\), and \(t\le M\), this yields \(\log G=o(s)\). Also \(D=3^p(2^{A-p\alpha}-1)\), so \(\log D=p\log3-O_{M,g}(\log p)\). Thus \(\log d=p\log3-o(p)\). To check every rotating height, the cumulative profile error \(E'_i-iA/p\) lies in \([0,2)\) periodically. Every rotated prefix sum differs from its linear value by less than two, so its carry lies between \(1/4\) and \(4\) times the ideal geometric sum \(D/(2^{A/p}-3)\). Since \(A/p-\alpha\asymp_{M,g}p^{-2}\), all phase heights have the stated quadratic growth. This finishes MC1.

### 5. What finite prime tests can and cannot impose

For \(M=35\), reduction to the square-class quotients modulo 5 and 7 sends \(2,3\) to two independent vectors: 2 is a nonsquare modulo 5 and a square modulo 7, whereas 3 is a nonsquare at both. Thus \(U_{35}\) is not cyclic. In fact it is all of \(C_4\times C_6\): 2 has order 12, its subgroup has index two, and 3 is outside this subgroup by square classes. The invariant factors are \(2,12\). Simultaneous cancellation at 5 and 7 is impossible for odd \(g\), and possible for every even \(g\). For any single prime power \(\ell^j\), \(\ell>3\), the ambient unit group is cyclic, so every \(g\) is possible. More generally (MC1) gives the exact condition for every finite joint modulus.

Even a **fixed cubic discrepancy** allows arbitrarily deep partial cancellation at one prime. For each \(e,L\ge1\) there are infinitely many coprime contracting clock pairs and primitive, positive rational cycles for which
\[
                    v_5(G)=e,\qquad v_5(d)\ge L,\qquad
                    \log d=p\log3-o(p).
\]
Advance the single first-lap date with rank \(r_i=2\). For large clocks it is a \(12\) switch and its polynomial is \(F(X)=X^3-X^2+1\). Modulo 5 this has a simple root 2, and its unique lift modulo 25 is 17. Since \(17^4=21\bmod25\), every integer congruent to 17 modulo 25 generates the units modulo every power of 5: order modulo 5 is four and the valuation of its \(4\cdot5^k\)-th power minus one is exactly \(k+1\) by binomial expansion. For \(e\ge2\), lift the simple root to modulus \(5^e\), then choose any lift other than the unique root modulo \(5^{e+1}\). The resulting integer \(z_*\equiv17\bmod25\) has \(v_5(F(z_*))=e\). For \(e=1\) take \(z_*=2\), again a generator, with \(F(2)=5\).

Choose \(s_0,a_0\) as the logs of 2 and 3 to base \(z_*\) modulo \(5^{e+L}\); 2 itself generates these units so the log pair is primitive modulo the order. Section 1 supplies the coprime clocks \((A,p)\). Then \(5^{e+L}\mid D\), and the canonical Bézout root reduces to \(z_*\) there. The gcd formula gives \(v_5(G)=e\) exactly. Since \(g=1\) one has \(H=1\); the second estimate in (2) alone, with fixed degree 3 and \(N\asymp\sqrt p\), gives \(\log G=O(\sqrt p)\) independently of the index of the switched date. This example rules out bounded cancellation and complete coprimality as replacements for a subexponential bound, even with a fixed discrepancy polynomial. It does not put \(d=1\).

The exact checks include the following positive cycles. At \((p,A)=(106,170)\) the same mechanical rotation, with the forced marker and free date 8 switched, has \(G=35\) and a 165-bit reduced denominator. Switching free dates 8 and 11 instead gives \(C=11\bmod35\), \(G=1\), and a 170-bit reduced denominator. For the fixed cubic, direct integer replay gives

| Odd period | Total divisions | Switched date | Complete cancellation \(G\) | Retained valuation \(v_5(d)\) |
|---:|---:|---:|---:|---:|
| 41 | 67 | 22 | 5 | 1 |
| 297 | 479 | 62 | 25 | 1 |
| 1537 | 2459 | 10 | 125 | 1 |

**Remaining arithmetic step.** For a hypothetical nontrivial positive ordinary cycle, its word must satisfy \(G=D\). The two factors controlled in (2) cover localized perturbations of a repeated mechanical schedule. An arbitrary word need not admit such a perturbation, and \(g\) need not be one. MC1 shows exactly which finite simultaneous prime-power demands can be met by quadratically large near-critical positive countermodels with \(d\) still exponential. Bounding the unprescribed part of \(G\) for every actual candidate, or proving a different ordinary obstruction, remains open.

**Verification scope.** [ModularCarry.lean](ModularCarry.lean) formalizes the finite subset-sum growth through saturation for every modulus and the exact sum of switched carry terms. [The finite check](check_modular_carry.py) uses direct group enumeration, integer carries and rotated forward replay. The group classification, asymptotic clock selection, positive-root resultant and complete denominator bound above are written proofs. Lagarias gives the classical rational-cycle correspondence; balanced-word minimum extrema are due to Halbeisen and Hungerbühler. [Lagarias (1990)](https://doi.org/10.4064/aa-56-1-33-53) · [Halbeisen and Hungerbühler (1997)](https://doi.org/10.4064/aa-78-3-227-239)

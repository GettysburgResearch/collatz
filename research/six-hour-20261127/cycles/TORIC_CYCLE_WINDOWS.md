# Quantitative denominator loss from sparse cyclic clock differences

**Proposed extension, 26 November 2026.** For a bounded number of exceptional windows, the largest gap in their support forces the same positive proportion of the full reduced cycle denominator on the logarithmic scale. Fixed clock gcd quantizes that proportion in steps of its reciprocal. Coprime clocks preserve the entire leading denominator. These conclusions allow mixed signs and exactly resonant window clocks. The underlying odd residual and the qualitative sparse-multiple obstruction are prior work. The new quantitative step estimates the degree of each retained common factor by specializing along prime valuations on the exceptional subtorus.

## 1. Clocks and conclusions

Let the positive gaps of a cyclic Syracuse word be \(e_0,\ldots,e_{p-1}\). Extend the gaps periodically. Write \(E_0=0,\ E_{i+1}-E_i=e_i,\ A=E_p\), and put
\[
 D=2^A-3^p>0,\qquad C=\sum_{i=0}^{p-1}3^{p-1-i}2^{E_i},\qquad d=D/\gcd(D,C).
\]
The phase is \(C/D\). Its reduced denominator is the same at every rotation because \(D\) is prime to six and \(2^{e_i}x_{i+1}=3x_i+1\). The odd rotated numerators ensure that these positive rational phases have exactly the specified gaps. Assume \(A\le Lp\) for some fixed \(L\). One can take \(L=2\) for positive integer cycles.

Choose \(1\le v<p\) and \(u\in\mathbb Z\), and let
\[
 B_i=E_{i+v}-E_i,\qquad J=\{i\bmod p:B_i\ne u\}.
\]
Suppose \(1\le m=|J|\le M\) for a fixed \(M\). Its largest cyclic spacing \(h\) is at least \(p/m\), with \(h=p\) for a singleton. The word, common clock \(u\), window length \(v\), gap magnitudes and locations can vary with \(p\). Since \(m\) is bounded, \(u\) occurs among the \(B_i\) for sufficiently large \(p\). In particular \(0<u<A\).

**Theorem 1 (denominator fraction).** Along every such sequence with \(p\to\infty\),
\[
 \liminf\left(\frac{\log d}{\log D}-\frac hp\right)\ge0.
 \tag{T1}
\]
In particular \(\liminf\log d/\log D\ge1/M\) with unrestricted clock gcd. If \(\gcd(A,p)=g\) is fixed and \(\lambda=\liminf h/p\), then
\[
 \liminf\frac{\log d}{\log D}\ge \frac{\lceil g\lambda\rceil}{g}
 \ \ge\ \frac{\lceil g/M\rceil}{g}.
 \tag{T2}
\]
In the coprime case \(\log\gcd(D,C)=o(p)\), hence \(\log d=A\log2-o(p)\). Every choice admits \(pu=Av\) or \(pu\ne Av\), and no sign or small-drift hypothesis is imposed. The outside-\(S\) theorem supplies no effective onset in this argument.

For a primitive word of period \(p>1\), \(J\) is always nonempty. Indeed \(J=\varnothing\) implies \(e_{i+v}=e_i\) for all \(i\). Consequently, along hypothetical ordinary primitive cycles of increasing period, the minimum of \(|J|\) over **all** proper windows and common clocks tends to infinity. Theorem 4 of the prior manuscript below already gives the qualitative conclusion for the Farey window. Its proof and Lemma 3 give it for other windows by the same odd residual. The numerical denominator fraction is the strengthening proposed here.

## 2. Prior exact residual

Lyapunov Weaver, Cassian Mahler and Fourier Wren, Paper 22 v4, Theorems 1 and 5, give the cyclic numerator difference, oddness after normalization, and the sparse-arc size bound. Their Lemma 3 treats any nonzero fixed-length signed sparse multiple whose ternary exponents omit a positive fraction of the clock. It descends to a minimal coset and uses a multivariate gcd theorem to retain the entire binomial when full divisibility holds. Their proof explicitly allows cancellation and noncoprime clocks. We use that argument for partial gcds and record the algebraic step that gives the missing fraction. [Paper 22 v4, §§1–5](https://rstation.ai/problems/collatz/papers/22/v4)

For clarity, work in \(\mathbb Z[1/6]/D\). Set \(s_i=2^{E_i}3^{-i}\), \(U=2^A3^{-p}\), \(w=2^u3^{-v}\). Then \(s_{i+p}=Us_i\equiv s_i\) and \(C=3^{p-1}\sum_{i<p}s_i\). Subtracting the cyclically shifted sum gives
\[
 (w-1)3^{1-p}C\equiv\sum_{i\in J}(2^u-2^{B_i})2^{E_i}3^{-(i+v)}.
 \tag{1}
\]
After rotating just past a largest gap, \(J\subseteq[0,R]\) with \(R=p-h\) and \(0,R\in J\). Put \(b_*=\min(u,B_0)\), and multiply (1) by \(3^{R+v}2^{-b_*}\). Its right-hand side becomes the integer
\[
 Z=\sum_{i\in J}3^{R-i}
     \left(2^{E_i+u-b_*}-2^{E_{i+v}-b_*}\right).
 \tag{2}
\]
The valuation of its \(i\)th row equals \(\min(E_i+u,E_{i+v})-b_*\). These values are strictly increasing because both arguments increase strictly, and the first is zero. Thus \(Z\) is odd and nonzero independent of signs and resonance. All \(2m\) powers of two in (2) have exponents in \([0,2A]\) and the ternary exponents lie in \([0,p-h]\). Every prime power in \(\gcd(D,C)\) divides \(Z\), including when \(w-1\) is not a unit.

## 3. Fractional sparse-multiple estimate

Consider more generally \(Z=\sum_{j=1}^N\epsilon_j2^{a_j}3^{b_j}\ne0\), with \(N\) fixed, \(\epsilon_j=\pm1,\ 0\le a_j,b_j=O(p)\), and \(D=2^A-3^p>0,\ A\le Lp\). Let \(R_3=\max b_j-\min b_j\). We claim
\[
 \limsup\left(\frac{\log\gcd(D,Z)}{\log D}-\frac{R_3}{p}\right)\le0.
 \tag{3}
\]
The corresponding binary claim uses \(R_2=\max a_j-\min a_j\) and \(R_2/A\). The proof gives their joint directional version below. Linear forms in the logarithms of 2 and 3 give \(\log D=A\log2-O_L(\log(2p))\) whenever \(D>0\). [Matveev (2000)](https://doi.org/10.1070/IM2000v064n06ABEH000314)

Fix any subsequence on which all the bounded normalized quantities of interest converge, and fix the signs by passing to a subsequence. Use torus coordinates \(U=2^A3^{-p}\) and \(Z_j=2^{a_j}3^{b_j}\); these belong to the fixed group of rational \(\{2,3\}\)-units. On this torus put \(f=U-1\) and \(z=\sum\epsilon_j Z_j\). Choose among connected translates having infinitely many retained points one of least dimension \(T\), pass to points on it and fix one such \(P_0\). The torus is split, since character lattices here are integral sublattices in a split character lattice. Translation by \(P_0\) is rational. Choose split coordinates \(t\) by extending a saturated lattice basis. These are products of powers of the original ratios to \(P_0\), and have logarithmic height \(O_T(p)\). Every proper translate inside \(T\) contains at most finitely many of our chosen points. This is the minimal-coset selection used in Paper 22, Lemma 3.

The restrictions have \(f=cV^q-1\), where \(c=U(P_0)=2^{A_0}3^{-p_0}\) and \(V\) is a primitive character in the translated coordinates. The character part is nonconstant because \(p\to\infty\). Take \(V\) as the first split coordinate. Since \(z(P)=Z\ne0\), \(z|_T\) is nonzero. Their greatest common Laurent factor \(G\) can be taken to be a fixed polynomial in \(V\) of degree \(j\le q\), with nonzero constant term. Indeed each irreducible factor of the univariate binomial remains prime after adjoining independent Laurent variables. Put \(f'=f/G,\ z'=z/G\).

Apply the outside-\(S\) gcd estimate to the coprime pair \(f',z'\) on this fixed \(T\), with \(S=\{\infty,2,3\}\). Laurent monomials are units outside \(S\); one can clear monomial denominators and remove common monomial factors. Every tolerance excludes only finitely many proper translates, each meeting our sequence finitely. Since coordinate heights are \(O_T(p)\), their outside-\(S\) gcd height is \(o(p)\). Fixed rational coefficient denominators cost \(O_T(1)\). This version has no condition at the coordinate origin. [Levin and Wang, Theorem 1.13(1)](https://doi.org/10.1515/crelle-2019-0033) [Levin, Inventiones 215 (2019), 493–533](https://doi.org/10.1007/s00222-018-0831-z)

At each prime outside \(S\), positive parts in \(\min(v(f),v(z))=v(G)+\min(v(f'),v(z'))\) bound the full gcd by these residual contributions and the numerator height of \(G(V)\). The latter is at most \(j h(V)+O_T(1)=(j/q) A\log2+O_T(1)\), since \(h(U)=A\log2\) and \(U=cV^q\). Evaluating \(f=U-1,\ z=Z\) recovers the integer gcd away from six, and \(D\) is prime to six. Thus
\[
       \log\gcd(D,Z)\le (j/q) A\log2+o(p).                 \tag{4}
\]
This is the partial-gcd use of equation (19) in Paper 22 before imposing \(D\mid Z\).

**Valuation specialization.** For each retained \(P\), in the fixed split coordinates define a Laurent path over \(\mathbb Q\) by
\[
        t_\ell(y)=t_\ell(P)\,y^{v_3(t_\ell(P)/t_\ell(P_0))}.
\]
For every torus monomial \(H\) times a rational constant, its evaluation is \(H(P)y^{v_3(H(P)/H(P_0))}\). Thus \(U\) acquires exponent \(-(p-p_0)\), \(V\) acquires exponent \(-(p-p_0)/q\), and \(Z_j\) acquires exponent \(b_j-b_{j,0}\). The image \(z(y)\) is nonzero at \(1\), and its Laurent width (largest minus smallest nonzero exponent) is at most \(R_3+O_T(1)\). The fixed reference exponents are the only error. Its divisor \(G(V(y))\) has width exactly \(j(p-p_0)/q\) because \(G\) has both endpoints nonzero. Laurent widths add under multiplication of nonzero one-variable Laurent polynomials over a field, by their extreme coefficients. Consequently
\[
         \frac{j}{q}(p-p_0)\le R_3+O_T(1).                \tag{5}
\]
Taking limits in (4) and (5) proves (3). The same proof with \(v_2\) gives the binary bound. None of these inequalities requires irreducibility of the full binomial.

For a general integer direction \((a,b)\), use \(a v_2+b v_3\) in place of \(v_3\). Then on the same subsequence
\[
 \frac jq\,|a(A-A_0)-b(p-p_0)|
 \le \max_i(aa_i+bb_i)-\min_i(aa_i+bb_i)+O_{T,a,b}(1).
 \tag{6}
\]
Alternatively specialize simultaneously in two variables. The Newton polygon of the **surviving** Laurent polynomial contains a translate of the common-factor segment from \((0,0)\) to \((j/q)(A-A_0,-p+p_0)\), because it is a Minkowski sum with that segment. The raw exponent hull only bounds the surviving support after the fixed reference shifts and possible cancellations. Equations (3) and (5) need just the ternary projection.

**Fixed-gcd quantization.** For any complex root \(\xi\) of \(cX^q-1\), let \(t=[\mathbb Q(\xi):\mathbb Q]\). Taking norms of \(\xi^q=c^{-1}\) and valuations gives \(q\mid tA_0,\ q\mid tp_0\). Therefore \(q/e\mid t\) for \(e=\gcd(q,A_0,p_0)\). Since \(A-A_0\) and \(p-p_0\) are multiples of \(q\) on \(T\), \(e\mid \gcd(A,p)\) at every retained point. The degree \(j\), a sum of irreducible factor degrees, is a multiple of \(q/e\); thus \(j/q\in(1/e)\mathbb Z\). For fixed clock gcd \(g\), \(j/q\in (1/g)\mathbb Z\). In particular the polynomial is irreducible at coprime clocks. For (2), (5) gives \(j/q\le1-\lim h/p\) and (4) gives \(\liminf\log d/\log D\ge1-j/q\). The coset argument can start on any limiting subsequence, proving (T1) and (T2).

**Exact slope on the selected coset.** The reverse inequality to (4) holds to an \(o(p)\) error for the sparse residual \(Z\). For each prime outside \(S\), the deficiency
\[
 v_\ell(f(P))-\min(v_\ell(f(P)),v_\ell(z(P)))
 =\max(v_\ell(f'(P))-v_\ell(z'(P)),0)
\]
is at most \(v_\ell(f'(P))_++b_\ell\). Here \(b_\ell\ge0\) bounds the denominator valuation of the fixed Laurent polynomial \(z'\) at \(S\)-unit points and vanishes at all but finitely many primes. The complement \(f'=(cV^q-1)/G\) is a polynomial of degree \(q-j\) in \(V\). Summing gives
\[
 \log D-\log\gcd(D,Z)\le h(f'(P))+O_T(1)
 \le (1-j/q)A\log2+O_T(1).
\]
Together with (4), this identifies \(\lim\log\gcd(D,Z)/\log D=j/q\) on the selected sequence. Every accumulation point for a fixed number of sparse terms is therefore rational, and for a fixed clock gcd \(g\) it belongs to \(\{0,1/g,\ldots,1\}\). The conclusions for \(\gcd(D,C)\) in (T1) and (T2) use only its upper bound by the residual gcd. To transfer the *exact* spectrum to \(d\), one sufficient additional condition is
\(0<|pu-Av|=o(p)\). Indeed the possible discrepancy in the two logarithmic gcds is at most \(\log\gcd(D,2^u-3^v)\) by (1). This gcd divides \(2^{|pu-Av|}-1\) by raising \(w=1\) to the \(p\)th power and using \(U=1\) modulo the gcd. Hence in this sector every accumulation point of \(\log d/\log D\) is rational, and for fixed \(g\) lies on the same \(1/g\) grid. Exact resonance does not supply this last comparison.

## 4. Boundary and prior interfaces

The fixed variable count is essential in Levin's theorem. Section 5 gives a primitive rational construction that defeats any proposed period-independent positive exponential rate once the allowed number of exceptions tends to infinity, however slowly. No argument here bounds the number of exceptions from above on an arbitrary ordinary cycle. A complete ordinary-cycle exclusion is therefore open.

Paper 22 v4, Theorems 1 and 5, already supplies the unweighted sparse-arc obstruction and the asymptotic square-root bound on exceptions for upper windows with small determinant, including noncoprime counts. It credits Solomon §§5.2 and 5.4 for the coprime predecessor. Section 6 records the geometric-sum constant and the statistic that removes the \(g\) mechanical seams from a coprime lift. The square-root scale itself is prior. Paper 22, Theorem 9, also excludes every balanced two-letter ordinary cycle. Project templates provide the earlier one-interval norm and localized switch bounds. [Paper 22 v4](https://rstation.ai/problems/collatz/papers/22/v4) [PR188, residue norm RN3](https://github.com/GettysburgResearch/collatz/blob/beed685ab713923191ae40c9559bf7400298d2d3/research/scalar-carry-cocycle-20261124/RESIDUE_NORM.md) [PR200, complete modular carry MC3](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/arithmetic/COMPLETE_MODULAR_CARRY.md)

The main result uses no reciprocal distinct-path estimate. Such an estimate is an independently sourced project input in PR201, and is unnecessary here because (5) permits exact resonance and arbitrary positive drift. Earlier papers on native Hamming distances between cycle shifts and on a single rotational exception concern different counting statistics. [PR201, cycle cofactors](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/renewal/CYCLE_COFACTORS.md) [Prior project note on native-shift distances](https://github.com/GettysburgResearch/collatz/blob/711a9bb05c240ac3a8e89ce1b541fb59495ddb56/research/cyclic-shift-distance/HEIGHT_AND_ALMOST_PERIODS.md)

The adjoining project work addresses different obstructions. PR192 studies local units, Pell equations and a regulator obstruction in varying number fields. PR195 gives Haar and finite-cover barriers for affine renormalization. PR201's dyadic cycle-order work counts reversals of shifted or sorted physical states. None of those arguments is an input to the valuation specialization in (5). [PR192 at ed7a6fe3, regulator repair](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/adelic/REGULATOR_REPAIR.md) [PR195 at 51d97cbe, Haar barrier](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/HAAR_BARRIER.md) [PR201 at 21bed7ac, dyadic cycle order](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/adelic/DYADIC_CYCLE_ORDER.md)

The public discussion behind Paper 22 also used the real fractional discrepancy \(iA/p-E_i\) to sharpen the signed-size estimate. Its use in §6 is credited there. [Paper 22 author discussion, Post 37](https://rstation.ai/r/collatz/posts/37)

## 5. No constant exponential saving at any prescribed growing exception allowance

Let \(f\) be any increasing function with \(f(t)\to\infty\). There are primitive, positive rational cycles of unbounded period with \(\Delta\to0^+\), all physical phase values tending uniformly to infinity, and a one-sided nonresonant test \(v=u=1\) having at most \(f(p)\) exceptions, while \(1<d=\exp(o(p))\). Their clock gcd grows. This does not settle a growing-exception test restricted to coprime clocks or a weaker universal assertion \(d>1\).

The construction specializes the independent periodic switches in [the earlier near-full rotation-gcd example](https://github.com/GettysburgResearch/collatz/blob/ebf2682a0cefb8d66ef43c822f19ac4c1c97bbd4/research/unrestricted-cycle-denominator/NEAR_FULL_GCD.md). Choose distinct primes \(q,r\ge5\) both tending to infinity and put \(n=qr\). Choose an upper convergent \(b/a>\log_2 3\) with \(a\) arbitrarily large *after* choosing the primes, so \(0<b-a\log_2 3<1/a\), \(n/a\to0\), and \(f(an)\ge3n\). In block \(j\bmod n\) encode independently the bits \(1_{q\mid j},1_{r\mid j}\), in that order, using shortcut pair \(10\) for zero and \(01\) for one. Append \(a-2\) ones and \(b-a-2\) zeros. Every block has \(b\) bits and \(a\) ones. Both long terminal runs exceed six; the transition with six ones before and six zeros after is unique in each block, at a common offset. A cyclic period must carry block boundaries to block boundaries, and the two labels then force block period \(qr\). Hence native period is \(bn\), odd period is \(p=an\), and the clock gcd equals \(n\). At least \(a-3\) of the odd gaps per block are one, from the long run alone. Thus \(1\le|J|\le3n\le f(p)\), with nonresonance \(p-A\ne0\). The full drift is less than \(n\log2/a\).

At block boundaries put \(P=3^a, Q=2^b\). The recurrence reads \(Qx_{j+1}=Px_j+c+u\,1_{q\mid j}+v\,1_{r\mid j}\), where \(c>0\) and \(u,v\) are positive products of powers of two and three. Each switch increases its own pair numerator by one, with a fixed smooth multiplier from the rest of the block. Linearity gives
\[
 x_0=\frac c{Q-P}+\frac{uP^{q-1}}{Q^q-P^q}+\frac{vP^{r-1}}{Q^r-P^r}.
\]
The common denominator consequently has \(\log d=O(b(1+q+r))=o(an)\). It is nontrivial explicitly. The geometric factor \((Q^q-P^q)/(Q-P)>q\) has a prime divisor \(s\nmid Q-P\): any prime dividing both is \(q\), and when \(q\mid Q-P\), the geometric factor has \(q\)-valuation exactly one by binomial expansion. At \(s\), \(Q/P\) has order \(q\), so only the \(q\)-term has negative valuation, and its numerator is an \(s\)-unit. This proves \(d>1\).

For the height check the contribution of the first pair to the affine block offset is at least \((P/Q)/3\). Thus all boundary phases are at least \((P/Q)/(3(1-P/Q))\to\infty\). Inside the two encoded pairs every prefix multiplier is bounded below by an absolute constant. Along the final ones the multiplier increases and along the final zeros it decreases to \(P/Q\to1\), so all interior phases also tend uniformly to infinity. Native parities follow directly from the unique fixed point over an odd denominator. The obstruction to a fixed exponential rate therefore survives high positive real phases and arbitrarily slow allowance growth; these are exact rational cycles, not integer ones.

### The leading fraction and a primitive equality family

For **fixed** distinct primes \(q,r\ge5\) and increasing upper convergents \(b/a\), the same construction gives
\[
 \lim_{a\to\infty}\frac{\log d}{\log D}=\frac{q+r-1}{qr}.
 \tag{S1}
\]
Here the fixed clock gcd is \(qr\). Write \(\delta_0=Q-P\), \(F_t=(Q^t-P^t)/(Q-P)\). The two shortcut pairs encode initial numerators \(7+3\,1_{q\mid j}+4\,1_{r\mid j}\) over \(16\). Iterating the odd shortcut \(y\mapsto(3y+1)/2\) for \(a-2\) steps, then appending the terminal zeros, gives exactly
\[
 c=23\cdot3^{a-2}-4\cdot2^a,\qquad u=3^{a-1},\qquad v=4\cdot3^{a-2}.
\]
The fraction at block zero has numerator \(N=cF_qF_r+uP^{q-1}F_r+vP^{r-1}F_q\) over \(\delta_0F_qF_r\). We have \(\gcd(F_q,F_r)=1\): at a common prime the unit \(Q/P\) would have order dividing both \(q\) and \(r\), hence would equal one; then that prime would divide both \(q\) and \(r\). Since the other numerator coefficients are units at the primes of these factors, \(\gcd(N,F_qF_r)=1\). Modulo \(\delta_0\), \(F_t\equiv tP^{t-1}\), so
\[
 \gcd(N,\delta_0)=\gcd(\delta_0,qr c+r u+q v)
 =\gcd\bigl(\delta_0,\,2^b(23qr+3r+4q)-36qr\,2^a\bigr).
\]
The second equality uses multiplication by the unit \(9\). The second entry of the last gcd is nonzero for all sufficiently large \(a\), and is a fixed finite signed sum with **zero ternary width** when \(q,r\) are fixed (expand the two integer coefficients if needed). Equation (3) gives \(\log\gcd(N,\delta_0)=o(a)\). Linear forms in two logarithms give \(\log(Q^t-P^t)=tb\log2-O_{t}(\log a)\) for fixed \(t\ge1\). The product \(\delta_0F_qF_r\) therefore has logarithm \((q+r-1)b\log2+o(a)\), while the native determinant has logarithm \(qrb\log2+o(a)\). This proves (S1). A block-boundary value can be even; the odd denominator prime to six is preserved at every shortcut step, so this computation gives the same \(d\) as the cyclic odd numerator.

To attain the correlation with the **largest gap** in (T1), keep \(r\) fixed and let prime \(q\) tend to infinity. Choose \(1\le t<qr\) with \(t\equiv0\bmod r,\ t\equiv1\bmod q\), and compare the odd window \(v=at\) with native target \(u=bt\). This window has \(pu=Av\). In block \(j\), the native positions of its first two odd dates are \(bj+1_{q\mid j}\), \(bj+2+1_{r\mid j}\); all remaining odd dates have fixed block offsets. A shift by \(at\) odd dates advances exactly \(t\) blocks and leaves the second label invariant. Hence the exceptional starts are exactly the first odd dates of blocks \(j\equiv0,-1\bmod q\). Their number is \(2r\) independent of \(q\); their signs are mixed, and their largest cyclic spacing is \(h=a(q-1)\). For each \(q\), choose a sufficiently late convergent in (S1) so the error is at most \(1/q\), and require \(a>q^2r^2\) for small drift. Then the resulting **primitive** rational cycles have
\[
     \frac hp=\frac{q-1}{qr}\longrightarrow\frac1r,\qquad
     \frac{\log d}{\log D}\longrightarrow\frac1r .
 \tag{S2}
\]
Thus the largest-gap fraction in (T1) is attained asymptotically even with a fixed bound on the support, exact resonance, both defect signs, positive high phases, and growing clock gcd.

For arbitrary presentations the pure \(1/M\) corollary is also sharp. Repeat \(M\) times a coprime balanced mechanical word of odd length \(a\) and native clock \(b\), taking a growing sequence of upper convergents. Its right Farey window has exactly one defect per copy: the change of the residue \((-bi\bmod a)\) by one has exactly one wrap. On the primitive coprime word (T1) gives full leading denominator. Repetition preserves those phases and multiplies the leading log determinant by \(M\). The resulting ratio tends to \(1/M\). This last example has least odd period \(a\), in contrast to the primitive construction (S2).

## 6. An elementary variable-complexity bound on the full denominator

The following result allows any number of exceptions, either sign, every clock gcd, and even a resonant comparison. No gcd theorem on algebraic tori enters it.

Let \(\theta=A/p\), \(\sigma=u-\theta v\), and put \(\eta_i=E_i-\theta i\), periodically in \(i\). Write \(W=\max_i\eta_i-\min_i\eta_i\). Suppose that the positive window length \(v<p\) and integer \(u\) give \(J\ne\varnothing\); let \(m=|J|\). The largest positive cyclic spacing between consecutive elements of \(J\) is \(h\), with \(h=p\) if \(m=1\). In particular \(h\ge p/m\). Then
\[
 \boxed{\quad d\ \ge \frac{(1-3^p/2^A)\,2^{\theta h-W-|\sigma|}}
 {\min\{m,(1-3/2^\theta)^{-1}\}}.\quad}                           \tag{7}
\]
A candidate ordinary cycle must satisfy the same inequality with \(d=1\). The multiplicative loss \(1-3^p/2^A\) is displayed exactly, so (7) has a finite, effective form independently of lower bounds for logarithmic forms.

Rotate to make the first exceptional index after a largest gap equal to zero. Put \(R=p-h\). All exceptional indices are in \([0,R]\), with \(R\) itself an exception. Rotation preserves \(D\) and \(d\). It leaves \(W\) unchanged since the new discrepancy sequence is a translate of the previous one. Let \(m_0=\min(u,B_0)\), and here assume \(u\ge0\) as for every window comparison above. Multiply (1) by \(3^{R+v}2^{-m_0}\) to obtain the signed integer
\[
 Z=\sum_{i\in J}3^{R-i}\,2^{E_i-m_0}(2^u-2^{B_i}).               \tag{8}
\]
Each term is interpreted after extracting \(2^{\min(u,B_i)}\), so it is integral even if \(E_i-m_0<0\). Its exact dyadic valuation is
\[
 E_i+\min(u,B_i)-m_0=\min(E_i+u,E_{i+v})-m_0.
\]
Both arguments of this minimum rise strictly as \(i\) increases. Thus the first summand is odd, every later one is even, and \(Z\ne0\), irrespective of the signs. This is the place where chronological order retains a constraint lost by an unrestricted signed sparse polynomial. Since (8) differs from (1) by an \(S\)-unit, the complete \(\gcd(D,C)\) divides this nonzero integer.

Each summand has modulus at most \(3^{R-i}2^{E_i+\max(u,B_i)-m_0}\). Since the cut has \(\eta_0=0\), subtraction of \(\theta i\) from its binary exponent gives
\[
 \max(\eta_i+\sigma,\eta_{i+v})-\min(\sigma,\eta_v)\le W+|\sigma|.
\]
For example \(\eta_i+\sigma-\eta_v\le W+|\sigma|\), while \(\eta_{i+v}-\sigma\le W+|\sigma|\) since zero is in the range of \(\eta\); the other two differences are at most \(W\). Set \(t=3/2^\theta<1\). We obtain
\[
 |Z|\le 2^{\theta R+W+|\sigma|}\sum_{i\in J}t^{R-i}
 \le 2^{\theta R+W+|\sigma|}\min(m,(1-t)^{-1}).
\]
Taking \(d\ge D/|Z|\) proves (7).

A useful asymptotic form only loses a logarithm of the *reduced* odd clock. Write \(\theta=a/s\) in lowest terms and assume \(\theta\le L\). The nonzero linear form \(a\log2-s\log3\) is \(\gg_L (2s)^{-C}\) by Matveev. Since \(1-e^{-z}\gg\min(z,1)\) for positive \(z\), both \(1-t\) and \(1-3^p/2^A\ge1-t\) are \(\gg_L(2s)^{-C'}\). Thus
\[
             \log_2 d\ge \theta h-W-|\sigma|-O_L(\log(2s)).          \tag{9}
\]
In particular bounded discrepancy \(W\) and a stated window attaining \(u\) give \(|\sigma|\le W\), so \(m=o(p/\log(2s))\) forces \(d\to\infty\) when \(p/m\to\infty\). Integer-only applications of (7) retain the true geometric factor and need no large-period test.

### A square-root obstruction and all noncoprime clocks

In a primitive nonstandard ordinary cycle, \(\log_2 3<\theta<2\), since every odd phase exceeds one. Let \(g=\gcd(A,p)\), so \(p=gs\) and \(s\ge2\). Take **any** \(1\le v<p\) coprime to \(p\) with \(av\equiv-1\bmod s\). Such a lift exists: choose the inverse residue modulo \(s\), then prescribe one modulo each prime dividing \(p\) but not \(s\) by the Chinese remainder theorem. For \(r_i=(-ai\bmod s)\), define the integer level \(k_i=E_i-\lceil ai/s\rceil\); it is periodic in \(i\). Let
\[
    K=\#\{i\bmod p:k_{i+v}\ne k_i\}.
\]
Set \(u=(av+1)/s\). The number of exceptional windows is at most \(K+g\), because the baseline window equals \(u\) except at the \(g\) seams \(r_i=s-1\). It is at least one, since \(\sum B_i=Av\ne pu\). As \(v\) permutes all phases in one cycle, the number of integer levels is at most \(\max(1,K)\). A one-step transition in physical order lowers the level by at most one, because \(e_i\ge1\) and a baseline step has length at most two. The directed graph of occupied levels is strongly connected. Taking a simple path from maximum to minimum proves the level range is at most \(\max(1,K)-1\). Since \(\eta_i=k_i+r_i/s\), we have \(W<\max(1,K)\). Also \(|\sigma|=1/s\). Formula (9) with \(d=1\) gives
\[
       \frac{\theta p}{g+K}\le K+O(\log(2s)),\qquad
       K\ge \frac{\sqrt{g^2+4\theta p}-g}{2}
                        -O(\log(2s)).                                  \tag{10}
\]
For the second implication, the function \(x\mapsto x-\theta p/(g+x)\) increases with slope at least one for \(x\ge0\). The constants here can be absolute since \(L=2\). There is no restriction on how \(g\) grows with \(p\).

At coprime clocks, \(v\) increments the residue by one, so \(K\) is exactly the number of jumps in residue order. Along hypothetical ordinary cycles with \(g=o(\sqrt p)\), the lower bound is \((\sqrt{\log_2 3}-o(1))\sqrt p\). If \(g/\sqrt p\to\infty\) and \(s\to\infty\), it is \((\theta-o(1))s\). The latter reduced-clock growth holds along any infinite sequence of distinct ordinary cycles: their minima tend to infinity, \(\theta\to\log_2 3\) by the elementary product estimate, and rationals of bounded denominator cannot tend to that irrational number in a compact interval. These cycle-specific consequences use no distinct-path estimate. They force genuine growing complexity, but do not exclude a word with sufficiently many level changes.

## 7. Prior comparison and verification

| Claim | Earlier status | Status in this note |
|---|---|---|
| Cyclic shift residual, strictly rising row valuations, nonzero odd cut | Paper 22 v4, Theorems 1 and 5 | Reproduced as (1) and (2), with the target \(u\) arbitrary |
| Fixed sparse multiple cannot have full divisibility if ternary exponents omit a linear interval | Paper 22 v4, Lemma 3 and Theorem 4 | The earlier qualitative conclusion follows from (3) |
| Minimal connected coset, restricted binomial factor and upper bound (4) | Paper 22 v4, Lemma 3, through its equation (19), using Levin | Imported architecture with explicit outside-\(S\) hypotheses |
| Common-factor degree bounded by the ternary, binary or directional width even under partial cancellation | The prior proof compares exponent differences after deducing divisibility by the whole binomial | Valuation specialization (5)–(6), even when a proper factor alone survives |
| Quantified numerical denominator fraction, fixed-gcd grid and sparse-gcd limit spectrum | Paper 22's lemma only concludes qualitative finiteness in the full-divisibility case | (T1), (T2), and the complement-factor calculation |
| Square-root count for upper windows of small determinant | Paper 22 v4, Theorems 1 and 5 plus its canonical-width refinement; coprime predecessors credited there | The scale is prior. Equation (7) retains the geometric multiplier; (10) counts seam-excluded jumps for any unit lift |
| Independent switch families with near-full cancellation | The pinned project construction in §5 | The arbitrarily slow allowance, fixed-gcd fractions (S1), and primitive fixed-sparsity equality (S2) |
| General Collatz convergence or exclusion of all ordinary cycles | Open | A cycle with sufficiently many exceptions is still allowed |

The proof of the toric estimate invokes published Diophantine approximation and standard split-torus character algebra. Its descent and existence bounds are written mathematics, not a formal proof. The finite Lean kernel checks the cyclic-difference identity, strict row valuations, odd cut and the degree-times-valuation bound for a surviving univariate multiple. Levin's theorem and the asymptotic passage are mathematical inputs to the paper. Its audit reports only standard Lean axioms. The exact Python controls recompute rotation numerators and replay primitive rational trajectories. They also check (S1)'s **exact** integer denominator formula, the support size and spacing in (S2), and fixture parity. The asymptotic limits have the written proofs above.

Checked with Lean 4.34.1 in strict warning-as-error mode against mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. Reproduction from this work directory uses

~~~sh
python leanrun.py ToricWindow.lean
python -B check_toric_windows.py
python -O -B check_toric_windows.py
~~~

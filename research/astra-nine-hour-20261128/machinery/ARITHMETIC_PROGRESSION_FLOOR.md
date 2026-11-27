# Collatz predecessors in every moderately growing arithmetic progression

**PROPOSED, source-qualified written theorem.** There are absolute \(c,\delta>0\) and \(C\) with the following property. If \(a\) is any positive odd integer prime to three, \(X\ge Ca\), and \(M\) is any odd integer satisfying \(M\le (X/a)^\delta\), then, for every \(u\bmod M\),
\[
 \#\{x\le X:x\text{ odd},\;x\equiv u\bmod M,\;U^j x=a
                    \text{ for some }j\ge0\}\ \ge\ cX/(aM).       \tag{1}
\]
The constants are uniform in the supplied target, progression and its residue. We obtain a true inverse path into every odd residue modulo every odd modulus with total valuation \(O(1+\log M)\), common odd length \(n=O(1+\log M)\), exact total \(2n\), and largest single valuation at most \((3/2)\log_2(n+1)+O(1)\). The same inverse reachability in \(O(1+\log M)\) total valuation holds for every modulus and every odd-compatible class, by appending a deterministic binary suffix. The fixed-total conclusion here is for odd moduli.

The proof extends Tao's triangle argument and uses the **written** quantitative stopped-renewal, finer-modulus collision and selected-prefix atom-floor arguments of Weaver and Wren. Those external analytic proofs and the following application have not undergone a full independent Lean formalization here. The fixed-modulus finite graph identities in the accompanying Lean files are separate. The earlier unconditional linear predecessor bound \(cX/a\) is the case \(M=1\). The earlier logarithmic routing budget for \(M=3^k\) and the classical all-modulus back-tracing theorem have different scopes. [Wren, paper 10 v3](https://rstation.ai/problems/collatz/papers/10/v3) · [Weaver and Wren, paper 48 v2, equations (58)–(83)](https://rstation.ai/problems/collatz/papers/48) · [Monks et al., Theorem 4.1](https://arxiv.org/html/1204.3904v2)

## A mixed-conductor Fourier estimate

Let \(e_1,\ldots,e_N\) have probabilities \(\Pr(e_i=t)=2^{-t}\), independently. Put \(S_N=\sum e_i\), \(\beta_N=\sum_{i=1}^N3^{i-1}2^{-S_i}\), and write \(e(t)=\exp(2\pi i t)\). All dyadic rationals reduce modulo odd integers. Suppose \(Q\) is coprime to six, \(Q>1\), and \(\chi\) is a character modulo \(3^m Q\) with **nontrivial** \(Q\)-part. For every \(A>0\) there is \(\eta_A>0\) such that
\[
 \left|\mathbb E[\chi(\beta_N)\gamma(S_N)]\right|\ll_A N^{-A}
 \quad\text{if}\quad (m-N)_++\log Q\le\eta_A N,\qquad|\gamma|\le1. \tag{2}
\]
Small ternary conductor, including the trivial ternary character, is allowed.

Write the mixed character angle at the pair position \((j,l)\) as the balanced representative of
\[
 \chi\big(3^{2j-2}2^{1-l}\big)\quad\text{in }\mathbb R/\mathbb Z,
\]
using additive notation for the angle. Define it on the entire half-plane \(j\ge1,\ l\in\mathbb Z\). Multiplication by nine in the horizontal direction and by two in the downward direction give exactly Tao's local relations (7.12)–(7.15). The angle is nonzero at all sites because the \(Q\)-part has order prime to six, while the other part has order a power of three. At a given \(j\) its denominator divides \(Q3^{(m-2j+2)_+}\). Thus no infinite upward line can stay black, since the real angles would halve while remaining bounded away from zero.

With a sufficiently small fixed absolute black threshold \(\epsilon\), Tao's top-left-corner construction and his three local separation cases now apply on the half-plane. For precision, at a black point move up until the next point is white, then left until either the boundary \(j=1\) or a white predecessor. If the corner is \((d,b)\), set \(\sigma=\log(\epsilon/|\theta(d,b)|)\). Its black triangle consists of all \(j\ge d,l\le b\) with \((j-d)\log9+(b-l)\log2\le\sigma\). Tao's proof of the white margin around this triangle uses only the local identities and the maximal choices in these two directions. The two uses of primitive ternary conductor in his proof are the right-edge bound (7.16) and exclusion of infinite upward black rays. We supplied the latter above and replace the former next. [Tao, Lemma 7.4, its proof and Remark 7.5](https://doi.org/10.1017/fmp.2022.8)

Write \(H=\lfloor N/2\rfloor\). Retain every whole triangle whose corner has \(d\le H\). This agrees with the original black set through column \(H\). The bound on nonzero denominators gives
\[
 d+\sigma/\log9
 \le d+\tfrac12(m-2d+2)_++\log_9 Q
 \le \max(H,m/2+1)+\log_9 Q .
\]
Keep these complete separated triangles in a larger strip of integer width
\[
 J=\lceil\max(H,m/2+1)+\log_9 Q\rceil+C_\epsilon ,
\]
where \(C_\epsilon\) supplies a right margin larger than the fixed triangle separation. Declare the complement of the retained triangles white in this larger strip. Only the colors up to \(H\) will be observed.

Conditional on adjacent pair totals and the last singleton, reversing the two possible letters of a pair of sum three changes the angle by precisely the displayed pair angle. Other pairs' contributions depend only on their preceding totals. The factor \(\gamma(S_N)\) is fixed on the conditioning. Therefore the same absolute discount product and holding law as in the pure ternary argument bound the left side of (2). This step averages the two actual letter orders before taking absolute values. The earlier stopped renewal proof uses only the family of complete separated triangles, the fixed right margin and the holding law. Apply its equation (60) with nominal conductor \(2J\), stopping line \(H\) and omitted width \(R=J-H\). In its notation, for any \(P\ge1\) the bound is
\[
 \left[\frac{C\max(e^{D(P+1)},20(R+1))}{2J}\right]^P+Ce^{-cJ}.
\]
Indeed the induction's white and short-black cases retain all discounts through \(H\), and the long-black case uses the whole triangles in the enlarged strip. These are exactly the hypotheses in the abstract triangle formulation. Choose \(P=\lfloor c_0\log N\rfloor\) with \(c_0\) sufficiently small, then choose \(\eta_A\) sufficiently small depending only on \(A\). The bracket is at most \(\exp(-2(A+1)/c_0)\) for large \(N\); increasing an implied constant handles bounded \(N\). This proves (2) with no power loss in \(Q\). [Weaver and Wren, paper 48 v2, Lemma 5](https://rstation.ai/problems/collatz/papers/48) · [Paper 50 v1, §2, abstract geometric scope, and §5, stopped proof](https://rstation.ai/problems/collatz/papers/50)

## Joint mixing with the full ternary cell and the exact clock retained

Let \(m=N+K,\ K\ge0,\ D=3^mQ\). Let \(h_s(z,v)\) be the mass of \(\beta_N=(z,v)\) modulo \(3^m,Q\) with \(S_N=s\), and write \(h_s(z)=\sum_v h_s(z,v)\). For every \(A>0\) there is \(\delta_A>0\) such that
\[
 \sum_{s,z,v}\left|h_s(z,v)-Q^{-1}h_s(z)\right|
 \ll_A N^{-A}\quad(K+\log Q\le\delta_A N).                       \tag{3}
\]
Here is the part of the collision proof where a growing \(Q\) matters. Split after \(r=\lfloor17N/20\rfloor\) letters, retaining only prefix totals \(d\ge d_0=\lceil\log_2 D\rceil\). For fixed \(d\), distinct words have distinct positive integer numerators \(C_w=2^d\beta_w\), by iterated binary valuation peeling. In any one residue class mod \(D\), if there are \(L\) of them then \(L^2\le L+2\sum_w C_w/D\), by ordering their spacings. Consequently for \(t=1+1/(4N)\) and prefix mass vectors \(f_d\) on the whole group,
\[
 D\sum_{d\ge d_0,v}t^d f_d(v)^2=O(N).
\]
To verify the constant, the diagonal sum is at most \(\mathbb E t^{S_r}=O(1)\), since \(D\le2^d\). The off-diagonal sum is at most \(2\sum_w t^{S_r}4^{-S_r} C_w=O(N)\) by the mixed moment in the proof of Weaver's Proposition 13. This term is unchanged by the modulus. Since \(2r/N\to1.7>\log_2 3\), the discarded prefix has mass \(O(e^{-cN})\) for small enough \(\delta_A\). [Weaver, paper 9 v2, Proposition 13, equations (38)–(40)](https://rstation.ai/problems/collatz/papers/9)

Spatial Plancherel of the difference in (3) keeps exactly characters with nontrivial \(Q\)-part. In the suffix their \(Q\)-part remains nontrivial after multiplication by \(3^r2^{-d}\), and their ternary conductor depth is at most \(m-r=(N-r)+K\). Equation (2) gives \(\varepsilon_N\ll_A N^{-A-3}\) for every suffix transform with a clock twist. Parseval in that twist bounds the sum of squares of the exact-total suffix transforms by \(\varepsilon_N^2\). Weighted Cauchy–Schwarz in \(d\), using \(\sum_{d\ge d_0}t^{-d}=O(N)\), now bounds the squared sum over all retained frequencies and clocks by \(O(N^2\varepsilon_N^2)\). Cauchy–Schwarz over \(s\le4N\) gives \(O(N^{3/2}\varepsilon_N)\) in the left side of (3). The omitted \(s\)-tail has exponentially small geometric-sum probability. This is the calculation of equations (65)–(69) of paper 48 with the new spacing modulus \(D\). There is no remaining factor \(Q\). The factor \(D\) in unnormalized Fourier Plancherel is exactly the one paid in the numerator estimate.

## A uniform atom floor for actual roots

There are absolute \(c,\delta,F,C_0>0\) such that for every large \(n\), \(k\ge0,\ k+\log Q\le\delta n\), integer \(|s-2n|\le\sqrt n\), ternary unit \(z\bmod3^{n+k}\), and \(v\bmod Q\),
\[
 3^{n+k}Q\Pr\{\beta_n=(z,v)\bmod(3^{n+k},Q),\ S_n=s,\
                 \beta_n\le F,\ \max e_i\le\tfrac32\log_2(n+1)+C_0\}
      \ \ge\ c\,\pi_n(s),                                         \tag{4}
\]
where \(\pi_n(s)=2^{-s}\binom{s-1}{n-1}\). The expression \(\beta_n\le F\) is an ordinary real inequality.

Start inside the fixed unit cylinder of paper 48, Lemma 7. Use its very same selected prefix family \(\Gamma_j^J\) just before the final free tail. Write \(t=n-d_j\), \(b=b_j\), \(h=t+k\). Its inequalities (78) give \(t\ge n/1616,\ t<1.2525b,\ n<202b\). The scalar selected assembly up to this point and all old truncations are unchanged. In the final free tail compare the mixed exact-total density \((2/3)3^hQ h_\tau(z,v)\) to its scalar marginal \((2/3)3^hh_\tau(z)\). By (3), at \(A=3\) the sum of normalized full-group means of the absolute differences over \(\tau\) is \(O(n^{-3})\), provided \(\delta\) is sufficiently small.

For a requested full beta class choose an integer lift \(y\) mod \(3^{n+k}Q\). At fixed prefix length and total \(D'\), the valid intermediate arguments \(y_w=(y-\beta_w)/\omega_w\) are distinct integers in an interval of length at most \(B_*/\omega_w\), where \(\omega_w=3^{d_j}2^{-D'}\). This follows from the same numerator injection and bounded selected-prefix real offsets as (72). The condition \(y\equiv\beta_w\bmod3^{d_j}\) gives their integrality. Thus the supremum of the selected-prefix sum acting on absolute test functions is at most
\[
 (B_*+3^h Q\,16^{b_0-b})\sum_{D'}\langle |f_{D'}|\rangle_{3^hQ}.
\]
The bracket is uniformly bounded since \(h<1.2525b+k\), \(n<202b\), and \(k+\log Q\le\delta n\). Distinct prefix totals correspond to distinct remaining totals. Multiplication by this bound transports (3) into an \(O(n^{-3})\) *supremum* error, uniform even at one true target. Division by the central \(\pi_n(s)\gg n^{-1/2}\) preserves a vanishing relative error.

For clarity, the scalar comparison is to the selected-prefix assembly with its **free last tail before capping**. It dominates the original fully capped scalar assembly, hence has the scalar floor. Impose the old cap \(J=\lceil(3/2)\log_2(n+1)+C_0\rceil\) on the mixed last tail afterward. Its total rejected mean over all exact slices is at most \(t2^{-J}\); the same mixed selected-prefix bound makes the normalized loss \(O(n^{3/2}2^{-J})\). Increase \(C_0\) once. The bounded real offset of the assembled mixed words is inherited from the selected prefix and the deterministic bound in the original Lemma 7. This gives (4) in the fixed unit cylinder, initially even for \(|s-2n|\le2\sqrt n\). Prepend one bounded exponent as in the proof of paper 48, Theorem 8, to reach any ternary unit. The affine change on the \(Q\) coordinate is bijective. The changed total stays within the larger central window and its negative-binomial mass is uniformly comparable. The fixed weight of the new first letter is bounded below. This proves (4).

## Positive ordinary rows, counts, and the original grade

Write \(M=3^kQ\), with \((Q,6)=1\). Given an actual odd unit \(a\), a residue \(u\bmod M\), a central \(s\), and the desired odd depth \(n\), prescribe
\[
 \beta_n\equiv a-3^n2^{-s}u\pmod {3^{n+k}Q}.
\]
The ternary component is a unit. Every selected word of total \(s\) is integral at every inverse step. Indeed, \(C_w=2^s\beta_w=2^{s-e_1}+3C_{w'}\) for the suffix \(w'\). Full divisibility first gives \(3\mid 2^{e_1}a-1\). This numerator is positive and odd because \(a\ge1\) and \(e_1\ge1\), so its integral quotient \(a_1\) is a positive odd integer. Substitution gives \(2^sa-C_w=3(2^{s-e_1}a_1-C_{w'})\), hence the exact same divisibility condition for the suffix. Induction proves positivity and oddness through the terminal value even when \(a\le F\). The real inequality \(\beta_n<a\) follows from this induction. Finally \(3I_e(y)+1=2^e y\) verifies every true outgoing valuation. Its endpoint \(x=2^s(a-\beta_n)/3^n\) lies in the progression and satisfies \(x\le2^sa/3^n\). Distinct words at a fixed length have distinct sources since the forward map is deterministic with unique outgoing valuations. Thus (4) gives at least
\[
 c\,2^s/(3^nM\sqrt n)                                             \tag{5}
\]
such sources on each central slice. The \(Q=1\) case is the original ternary floor. Summing the geometric masses over \(s\) gives \(\eta_n^a(u\bmod M)\ge c/M\) for \(k+\log Q\le\delta n\). In particular \(s=2n\) gives the stated logarithmic routing cost. For a \(2^{b+1}\) component, append the reversed first \(b\) true valuations from a representative of the desired odd binary residue as in the elementary note. The suffix costs at most \(3b+1\); require the appropriate unique preceding \(Q\)-class and preceding ternary precision \(k+b\). This yields \(O(1+\log M)\) total cost for general moduli.

For (1), first take an aperiodic root \(a\). Let \(L=\log_2(X/a)\), \(n_* =L/(2-\log_2 3)\), and take all integers \(|n-n_*|\le c_0\sqrt{n_*}\) for small fixed \(c_0>0\). Set \(s_n=\lfloor L+n\log_2 3\rfloor\). These totals are central for all large \(L\), and \(X/(2a)<2^{s_n}/3^n\le X/a\) up to equality at the lower endpoint, which is harmless. All of (5)'s sources lie below \(X\). The depth sets are disjoint, since any coincidence between different depths would make \(a\) periodic. Summing across \(\gg\sqrt L\) depths proves (1). For arbitrary \(a\), among the same-parity legal exponents in \(1,\ldots,6\), two of the three yield different unit predecessors. This follows from the three residues modulo nine obtained by multiplying an initial \(2^e a\) by \(1,4,7\). At most one can lie on the cycle through \(a\); if \(a\) is cyclic, select a nonperiodic one, \(a'\le64a/3\). Then its ancestors all reach \(a\). Increasing the absolute onset \(C\) and decreasing the exponent \(\delta\) absorbs this fixed ratio. This completes (1).

The modulus budget is absolute and retains the specified ordinary target. Normalization of an individual row divides the \(c/M\) absolute floor by its true mass \(\rho_n(a)\). Along an escaping target \(a_j\) at zero overshoot, the pinned physical trace gives \(\rho_j(a_j)\asymp P(a_j)\to\infty\). Formula (1) likewise pays \(1/a\) even if the full basin density of \(a\) is much larger. A uniform relative estimate for a specified initial sibling of such a high-mass \(a\) would require control of this loss. [Original physical trace and the normalization obstruction](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-diagonal-20261127/escape/FIRST_POWER_HAAR.md)

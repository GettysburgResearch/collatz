# Adaptive fair-pair windows at a charged ordinary gate

**Status.** Written obstruction for two specified laws. The conditional gate statement uses the pinned ordinary density and first-passage inputs. A separate estimate for the original finite ternary law uses only positive integer arithmetic. Neither proves that a charged ordinary component exists or that its charge must vanish.

## A single late history occupies almost the entire gate posterior

Suppose an ordinary component \(C\) escapes, and fix its actual native shortcut ray \(a_j=T^ja_0\). For a numerical barrier \(X\), put \(z_X=a_{k(X)}\) at its first exit. Choose a source \(1\le x<X\) conditional on first exiting at \(z_X\), with probability proportional to \(w_{z_X}(x)/x\). The positivity theorem makes the total normalized weight of this gate tend to \(\beta_C>0\). Write \(D_v\) for the ordinary weighted first-hit density and \(W(v)\) for the full future survival. At every *fixed* \(m\), the probability that the last \(k(X)-m\) native letters of the sampled history equal the actual segment starting at \(a_m\) tends to
\[
                         p_m=\frac{W(a_m)D_{a_m}}{\beta_C},
 \qquad                         p_m\longrightarrow1.                \tag{1}
\]
An insufficiently long history receives a cemetery mark. The second limit takes \(m\to\infty\) after the first limit in \(X\).

Indeed a gate and a complete native word determine at most one ordinary initial integer by the affine equation. Thus the designated last word occurs precisely when the source hits \(a_m\) before its exit, once \(X\) exceeds the initial finite segment and \(k(X)>m\). Its normalized weight equals the harmonic first-hit mean to \(a_m\) **before exit**, multiplied by the weight along the fixed ray from \(a_m\) up to \(z_X\).

The unrestricted harmonic first-hit mean tends to \(D_{a_m}\), by the fixed-target natural density and partial summation. Passage to the stopped mean uses the physical prelanding peak input. Given a bottom cutoff \(R\), up to normalized harmonic mass with limiting upper bound \(e(R)\to0\), a source hits a bottom state through \(R\) before its first exit. If this source ever hits \(a_m\), it either already did so, or one of these finitely many bottom states subsequently hits \(a_m\). At fixed \(R,m\) every such finite continuation has a finite maximum. For all sufficiently large \(X\) it also precedes the exit. The discrepancy of the two means is bounded by the exceptional probability. Send \(X\to\infty\), then \(R\to\infty\). The ray weight through the gate tends to \(W(a_m)\). Finally, the normalized total gate mass tends to \(\beta_C\) at the named gate, and on the component \(W(a_m)\to1\) and \(D_{a_m}\to\beta_C\). These are exactly the source-qualified inputs from [the critical gate theorem](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/trace/CRITICAL_EXIT_GATES.md) and [the ordinary annular current](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/unconventional-20261126/trace/ANNULAR_ESCAPE_CURRENT.md).

## An entropy bound uniform over all distances

For a finitely supported probability \(\nu\) on the real line, let \(c_\ell(\nu)\) be the largest total weight of fair two-point laws with separation in \([2^{-\ell},2^{1-\ell})\) whose sum is a submeasure of \(\nu\). Write \(H(\nu)\) for its ordinary discrete Shannon entropy in nats. Then
\[
                         \sum_{\ell\in\mathbb Z}c_\ell(\nu)
                              \le \frac4{\log2}H(\nu).                \tag{2}
\]
This uses the pair-weight definition of the cited self-similar manuscript. Its proof here is elementary.

Fix a finite band of indices and use nested dyadic intervals translated by one common uniform shift, modulo the largest grid spacing needed in the band. At \(r=2^{-\ell}\) the two atoms of any eligible fair pair lie in different \(r\)-cells. With probability at least \(1/2\) they lie in the same \(4r\)-cell. The pair's mean conditional entropy of the finer grid given the coarser one is therefore at least \((\log2)/2\). Conditional entropy is concave in the joint law. Applying it to an optimizing decomposition, including its residual, gives
\[
 \mathbb E[H_r(\nu)-H_{4r}(\nu)]\ge(\log2)c_\ell(\nu)/2 .
\]
Each nonnegative single-level entropy increment occurs at most twice after summing a finite band. The total is at most \(2H(\nu)\). Increase the band to obtain (2).

Fix \(m\) large. Inside the last \(k(X)-m\) native clocks choose any block of length \(1\le L=L(X)\le k(X)-m\) and any deterministic real-valued encoding of its letters. The position and the encoding may depend on \(X\). An insufficient history can again have one cemetery mark. The block has at most \(2^L+1\) possible distinct outputs and one output has mass at least \(1-\epsilon_{m,X}\), with \(\epsilon_{m,X}\to1-p_m\) from (1). For \(\epsilon_{m,X}<1/2\) its entropy is at most
\[
              h(\epsilon_{m,X})+\epsilon_{m,X}L\log2 ,
 \qquad h(t)=-t\log t-(1-t)\log(1-t).
\]
Consequently, uniformly over positions, encodings and all bands of physical distances, the late block law \(\nu_{m,X,L}\) satisfies
\[
 \lim_{m\to\infty}\limsup_{X\to\infty}
      \sup_{1\le L\le k(X)-m}
        \frac1L\sum_\ell c_\ell(\nu_{m,X,L})=0 .                     \tag{3}
\]
Any suprema over deterministic encodings and in-range positions can be inserted inside the same bound. For an environment-dependent encoding one can first condition on the environment, so long as the observation is still a deterministic encoding of this same fixed-position block given the environment. The mean conditional entropy of its original letter word is bounded by the unconditional entropy. This remains a bound on mean gain, not on every exceptional conditioned environment. If the window position itself uses extra source information, its selection can carry information and must be accounted for separately.

OpenAI's Result 148 chooses the next block size after previously selected fine-band endpoints are known. Its linear lower bound for fair-pair weight and its conditional convolution identity let many disjoint bands contribute to one bounded entropy budget. Neither an estimate for how quickly the upper endpoints grow nor independence between selected windows is necessary there. Here (3) controls even the sum over *all* distances. These particular physical gate block laws fail the required positive linear lower bound under the hypothesis of one charge. Merely placing bands farther apart cannot repair it. An independent arithmetic lower bound directly contradicting (3), or a different law with a proved transfer back to this posterior, would be a new closing input. [Result 148, pair-band proposition](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/build/sections/types.tex) · [conditional gain and disjoint windows](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/build/sections/windows.tex).

## All suffix alternatives after one ordinary source prefix

A separate finite estimate goes in the other direction, conditioning on a true *initial* binary prefix and summing over every possible ternary terminal. Consider all words of \(n\) positive odd return exponents \(e_1,\ldots,e_n\), write \(S=\sum e_i\), and use the original geometric script probability \(2^{-S}\). Each word specifies one residue modulo \(3^n\). Let \(r_w\) be its least positive odd representative, \(1\le r_w<2\cdot3^n\). Backward lifting determines one positive odd source \(b_w\) with exactly these exponents and \(U^nb_w=r_w\). Indeed the ternary congruence is precisely inverse integrality, and each positive integral inverse is odd and positive. The assignment \(w\mapsto b_w\) is injective by physical determinism. Its raw harmonic word weight is
\[
           H_n(w)=\frac{3^n 2^{-S}}{r_w}
                 =\frac{w^{(n)}(b_w)}{b_w}\le\frac1{b_w},           \tag{4}
\]
where \(w^{(n)}\) is the product to the indicated **clock**, even if the target was encountered earlier. Thus these weights sum to the original raw harmonic trace, with repeated visits retained.

Fix an odd integer \(a\), integers \(1\le L\le n\) and \(a<2^L\). Among all scripts whose first \(L\) native letters agree with those of \(a\), discard the one whose source is \(a\), if present. The total of the other raw harmonic word weights is at most
\[
 2^{-L}\big[1+(10n+1)\log2\big]
           +\big[9(2/3)^{10}\big]^n .                              \tag{5}
\]
The common prefix gives \(b_w\equiv a\pmod {2^L}\), using the ordinary parity-cylinder bijection. If \(S\le10n\), positivity of the affine offset gives \(b_w\le 2^S r_w/3^n<2^{10n+1}\). All other such sources are distinct and of the form \(a+t2^L\), \(t\ge1\). Their reciprocal sum is at most the first term in (5). At \(S>10n\), drop the denominator \(r_w\ge1\) in (4) and all restrictions. The unrestricted geometric law has \(\mathbb E(3/2)^e=3\), giving the second term by Markov's inequality. This proof does not use trace or density asymptotics.

For every sufficiently large \(n\), the true word of \(a\) is present with \(b_w=a\), because its positive terminal \(U^n a<(3/2)^n(a+1)<2\cdot3^n\). On a fixed escape its weight is at least \(W(a)/a>0\) by the source-qualified distinct-path reciprocal bound. Consequently \(L=\lceil2\log_2(n+1)\rceil\) initial native bits suffice to make the *total* harmonic posterior mass of all other words in this cylinder \(O_a(1/n)\) at large \(n\). This statement sums over all terminal residues and all suffix lengths allowed by the odd depth. Its true-source atom, viewed inside the full unconditioned row of total order \(n\), has only order \(1/n\) normalized mass.

There is also a displacement consequence for equal aggregate-clock substitutions. If an alternative with the common initial prefix has total exponent equal to that of the true word, then its least representative satisfies
\[
             r_{w'}\ge (3^n/2^S)b_{w'}
                   \ge (2^L/P(a))\, U^n a,
 \qquad P(a)=a/W(a).
\]
The first inequality uses the ordinary positive affine intercept. The last uses \(U^n a\le (3^n/2^S)P(a)\), which follows by the survival telescope. Thus local fair switches far down a fixed positive ordinary script can have comparable *prior* probabilities yet radically different least positive representatives and harmonic weights. This is a distinct obstacle from arbitrary lack of quantitative rates. Windows crossing the early coalescence region, differently weighted laws, and arithmetic estimates on the retained deep labels remain open.

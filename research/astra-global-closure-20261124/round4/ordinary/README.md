# Multiplicative independence in logarithmic Collatz prefixes, uniformly in interval location

**PROPOSED.** Let \(U(q)=(3q+1)/2^{v_2(3q+1)}\) on positive odd integers. For an interval \(I=\{M+1,\ldots,M+L\}\), \(M\ge0\), let \(E_t(I)\) count odd sources \(x\in I\) for which at least one of \(q_0=x,q_1=U(x),\ldots,q_{t-1}=U^{t-1}(x)\) satisfies
\[
 v_p(q_j)\le\sum_{i\ne j}v_p(q_i)\quad\text{for every prime }p.
\]
Call such a position covered. At every source outside \(E_t\) each position has a prime whose valuation strictly exceeds the sum of its valuations at all the other positions. These primes are distinct. The states are multiplicatively independent, since an integral relation, tested at the witness prime of a largest absolute nonzero coefficient, violates the triangle inequality.

1. For every fixed \(0<\delta<1/4\) there is a \(\kappa_\delta>0\) such that \(E_t(I)\ll_\delta L^{1-\kappa_\delta}\) for all \(2\le t\le\delta\log_2 L\). In particular, with \(t=\lfloor(\log_2L)/16\rfloor\), one has \(E_t(I)\ll L^{4/5}\).
2. Suppose \(t=o(\log L)\) and \(\limsup\log t/\log\log L\le\beta\) for \(0\le\beta\le1\). Then \(E_t(I)\le L^{\beta/(1+\beta)+o(1)}\). Thus the exceptional count stays subpower throughout \(t=(\log L)^{o(1)}\), and is at most \(L^{1/2+o(1)}\) throughout \(t=o(\log L)\).
3. For every fixed positive odd \(b\) coprime to three, at least \((1-o(1))X^{0.84}/(1+\lfloor\log_2X\rfloor)\) odd sources up to \(X\) reach \(b\) and have a strictly dominating prime at **every** position of their first \(\lfloor(\log_2X)/16\rfloor\) odd states. This uses the published Krasikov–Lagarias inverse-orbit theorem. It applies also to any such target on a hypothetical nonconvergent component.

The constants and the errors in 1–2 are uniform over all \(M\), even when \(M\) grows arbitrarily fast with \(L\). The count concerns original sources, and allows their words, witnessing positions and witnessing primes to differ. An individual fixed orbit can still be exceptional at a specified window.

## Counting divisors in a translated interval

For \(P,Y\ge1\) set \(D(P,Y)=\#\{g\mid P:g\le Y\}\), and let \(\omega(P)\) count its distinct prime divisors. If \(S\) is any set of positive divisors of \(P\) of diameter at most \(Y\), then
\[
 |S|\le(1+\omega(P))D(P,Y).                                      \tag{1}
\]
Small elements give the first term. For each \(d>Y\) in \(S\), multiply its prime factors in nondecreasing order, with multiplicity, until the first partial product \(gp>Y\). Here \(g\mid P\), \(g\le Y\), and \(p\mid P\) is prime. Two distinct elements of \(S\) cannot be multiples of the same \(gp\) because their difference would exceed its diameter. This proves (1) for intervals of any location, including \(P=1\).

For fixed \(0<\sigma<1\), uniformly in \(P,Y\), put \(J=\max(3,\log P)\). Rankin's elementary inequality and a prime split give
\[
 D(P,Y)\le Y^\sigma\sum_{d\mid P}d^{-\sigma}
 \le Y^\sigma\exp\!\left[C_\sigma (J/\log J)^{1-\sigma}\right].   \tag{2}
\]
The sum is bounded by the product of \((1-p^{-\sigma})^{-1}\) over \(p\mid P\). Its log is at most \((1-2^{-\sigma})^{-1}\sum_{p\mid P}p^{-\sigma}\). Through \(Z=\max(2,J/\log J)\), even the sum over all integers is \(O_\sigma(Z^{1-\sigma})\). Above \(Z\) there are at most \(J/\log Z\) prime factors, each contributing at most \(Z^{-\sigma}\). For large \(J\), \(\log Z\asymp\log J\). Bounded \(J\) is absorbed in the constant. No estimate for the distribution of primes in progressions enters.

## A finite count from the ordinary source

Write \(s=t-1\), and let \(a_i=v_2(3q_i+1)\), \(A_{ij}=\sum_{i\le u<j}a_u\), \(A_j=A_{0j}\). For every physical gap word,
\[
 2^{A_{ij}}q_j=3^{j-i}q_i+C_{ij},\qquad
 C_{ij}=\sum_{i\le u<j}3^{j-1-u}2^{A_{iu}}.
\]
Consequently \(\gcd(q_i,q_j)\mid C_{ij}\). If \(j\) is covered, the valuations give \(q_j\mid\prod_{i\ne j}\gcd(q_i,q_j)\): truncating each competing valuation at \(v_p(q_j)\) still leaves their sum at least that threshold. Thus \(q_j\) divides the positive integer \(P_j(w)=\prod_{i\ne j}C_{\min(i,j),\max(i,j)}\). These are the original fixed-word identities at PR195 `8edc24b576e7c7da56f99d882ce6fd1e014ee730`, in `round3/analytic/README.md` and `FixedWord.lean`. The domination and gcd criteria are also in [Weaver, Paper 137, Lemma 4 and equation (12)](https://rstation.ai/problems/collatz/papers/137/v1). Weaver's [Paper 138, Theorems 1–2](https://rstation.ai/problems/collatz/papers/138/v1) gives rank and coset-visit estimates along one trajectory. Here the counting variable is the starting integer in an arbitrary translated interval.

Choose an integer \(s\le K\le\lfloor\log_2 L\rfloor\) and real \(\Lambda\ge1\). Set \(Y=\lceil\Lambda L\rceil\), \(J_0=s(K\log 2+s\log 3)\) and \(H=\lceil L/2^K\rceil\). One finite bound is
\[
 E_t(I)\le H\sum_{i=0}^s {K\choose i}
       + H\,2^K/\Lambda
       +t{K\choose s}\left(1+J_0/\log2\right)
                    \max_{1\le P\le e^{J_0}}D(P,Y).              \tag{3}
\]
The middle term can be omitted altogether if \(\Lambda\ge(3/2)^s\).

If \(A_s>K\), the first \(K\) chronological shortcut inputs have at most \(s\) odd states: the \((s+1)\)-st is at clock \(A_s\). Each parity word has a single residue class modulo \(2^K\) and hence at most \(H\) representatives in \(I\). Indeed its positive odd affine slope numerator and its carry determine the starting residue by reducing its endpoint equation modulo \(2^K\). This accounts for the first term, with no use of \(M\) as a clock budget.

For \(A_s\le K\), the \(s\) increasing positive partial sums select one of \({K\choose s}\) words. Each carry above is at most \(2^K3^s\), so \(\log P_j\le J_0\) and \(\omega(P_j)\le J_0/\log2\). At a fixed word and index the map \(x\mapsto q_j\) is injective and affine of slope \(3^j/2^{A_j}\), including the identity at \(j=0\). If the slope is at most \(\Lambda\), its image has diameter at most \(Y\), regardless of its location. Apply (1) and sum over words and positions. Deterministically every one of these slopes is at most \((3/2)^s\), since \(A_j\ge j\).

For smaller \(\Lambda\), estimate all words reaching a larger prefix slope within \(K\) shortcut clocks. On a length-\(h\) word with \(u\) odd inputs, the ratio between its Bernoulli-\(3/4\) probability and its fair binary probability is \(3^u/2^h\). The first prefixes to reach slope at least \(\Lambda\) form disjoint cylinders, so their fair mass is at most \(1/\Lambda\). There are at most \(2^K/\Lambda\) length-\(K\) extensions in total, giving the middle term of (3). This uses finite cylinder arithmetic on the original sources. No distribution is restarted at a moving endpoint.

## Passing to logarithmic lengths

All following logarithms in entropy exponents are base two. Let \(H_2(z)=-z\log_2z-(1-z)\log_2(1-z)\), with \(H_2(0)=0\). For \(s\le K/2\), \(\sum_{i\le s}{K\choose i}\le 2^{K H_2(s/K)}\), by summing fair words against Bernoulli weights with parameter \(s/K\).

For fixed \(\delta<1/4\), first choose \(2\delta<\alpha<1/2\) and \(0<\eta<1-2\alpha\). Put \(K=\lfloor\alpha\log_2 L\rfloor\) and \(\Lambda=L^\eta\). Here \(J_0=O((\log L)^2)\). At \(\sigma=1/2\) the exponential correction in (2) is \(\exp(O(\log L/\sqrt{\log\log L}))=L^{o(1)}\). The three terms of (3) have exponents at most
\[
 1-\alpha+\alpha H_2(\delta/\alpha),\qquad 1-\eta,\qquad
 (1+\eta)/2+\alpha H_2(\delta/\alpha)+o(1).
\]
All have strict limiting upper bound below one. One may take half the smallest of their limiting gaps as \(\kappa_\delta\).

For the explicit corollary take \(\delta=1/16\), \(\alpha=1/2\), \(\Lambda=(3/2)^s\), omitting the middle term. The two exponents are at most \(1/2+H_2(1/8)/2+o(1)\) and \((1+\log_2(3/2)/16)/2+H_2(1/8)/2+o(1)\). Here \(\log_2(3/2)<3/5\) and \(H_2(1/8)<11/20\), by \(3^5<2^8\) and \(8^{40}<2^{22}7^{35}\). Both limiting exponents are below \(4/5\).

For the sublogarithmic assertion take \(K=\lfloor\log_2 L\rfloor\), \(\Lambda=(3/2)^s\). Both the count of gap words and the entire first term of (3) are \(L^{o(1)}\), since \(s/K\to0\). Now \(Y=L^{1+o(1)}\) and \(J_0\le(\log L)^{1+\beta+o(1)}\). For each fixed \(\sigma>\beta/(1+\beta)\), \(\sigma<1\), the error in (2) is \(L^{o(1)}\) and (3) is at most \(L^{\sigma+o(1)}\). Take the limsup before letting \(\sigma\) decrease. All estimates are translation-uniform. An equivalent formulation of the first result is that every interval of \(L\) consecutive positives contains \((1/2+o(1))L\) odd sources with all the stated prime witnesses at any one of these logarithmic horizons.

## Fixed-target consequence and the remaining closure question

Krasikov and Lagarias prove that for each fixed positive \(b\) coprime to three, at least \(X^{0.84}\) positive integers up to \(X\) reach \(b\) for all sufficiently large \(X\) depending on \(b\). When \(b\) is odd, stripping initial powers of two retains that target and loses a factor at most \(1+\lfloor\log_2X\rfloor\) in the count. Subtract the explicit \(O(X^{4/5})\) exceptional bound to obtain conclusion 3. We use the published computer-aided predecessor result as an external input. The new estimates 1–2 and the interval divisor lemma do not use it. [Krasikov–Lagarias, *Acta Arithmetica* 109 (2003), Theorem 6.1](https://arxiv.org/pdf/math/0205002)

If a nonconvergent ordinary orbit exists, take an odd ternary-unit target on it; one accelerated step from any odd source is such a unit. Conclusion 3 then places logarithmic independent prefixes in that particular nonconvergent predecessor basin. The same conclusion with \(b=1\) gives terminating examples. Thus these witnesses alone do not distinguish forward behaviors. Proving a sufficiently smaller upper count of **nonconvergent** inputs among these independent prefixes, or proving that the one prescribed forward orbit necessarily reaches a covered window while its actual heights still force an original-floor drop, would require a new argument. The population theorem establishes neither inference. The earlier pointwise floor certificate retains its original hypotheses. [PR195, round 3, Theorem 2](../../round3/analytic/README.md)

There is a separate local consequence with a common endpoint. Fix \(H_2(\log_3 2)<d<1\). PR193 bounds the number of distinct outputs at one common odd clock \(R=\lceil K_d\log_2(2L)\rceil\) of all the odd cores in any length-\(L\) interval by \(C_dL^d\). Apply this bound to the \((1/2+o(1))L\) good odd sources supplied here, and choose their most frequent output. At least \(c_d L^{1-d}\) of those **distinct original odd sources** in the interval have individually independent prefixes of length \(\lfloor\delta\log_2L\rfloor\) and the same actual odd value at clock \(R\). One may increase \(K_d\) to put the common clock past the tested prefixes. This argument allows the shared endpoint to depend on the interval. Conclusion 3 instead prescribes \(b\) in advance without specifying a common clock. [PR193, `ebeec2cda24b1deafff17cb2a9ce6e1bed7d9784`, `research/astra-universal-descent-20261124/escape.md`, (1a)](https://github.com/GettysburgResearch/collatz/blob/ebeec2cda24b1deafff17cb2a9ce6e1bed7d9784/research/astra-universal-descent-20261124/escape.md)

[TruncatedDivisors.lean](TruncatedDivisors.lean) proves (1), the finite Rankin inequality, and the width/injectivity bound for a translated physical affine row. [DyadicCutoff.lean](DyadicCutoff.lean) proves the first-passage inequality on the complete binary tree, the physical affine law, the single-residue implication, and the resulting integer-threshold maximal estimate on sources in an arbitrarily translated binary period. The prime split, entropy estimates, combination of the cuts, and the basin and synchronization applications are written arguments. [Finite arithmetic and execution record](../../../../reports/astra-global-closure-20261124/round4/ordinary/EXECUTION.md)

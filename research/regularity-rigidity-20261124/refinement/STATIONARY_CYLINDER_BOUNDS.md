# Review of the earlier logarithmic entropy deficit and ordinary upper bounds

**Prior result, independently reconstructed.** PR 195, 0e8a7f9f965416189b30b57b8aa818fbcb7757c7, research/astra-global-closure-20261124/round5/renewal/README.md, §§1–3 (blob 73f1b77a25150f54d7448d2acb04f82c46c82404), already proves stronger estimates for the stationary law \(\nu\) of PR 200's full marked ratio-five dictionary. Its almost-sure and entropy conclusions are verified conditional on PR 200's reverse-prefix bound. Almost every depth-\(k\) cylinder has mass \(3^{-k}\) up to polynomial factors in \(k\), and

\[
 0\le k\log 3-H(\nu_k)=O(\log(k+1)).
\]

For every positive ordinary target, PR 195 also gives a nearly Haar upper cylinder bound. Its finite real moments give a uniform upper exponent below one half even on arbitrary ternary cells. The ordinary inverse-fiber target requires a lower bound at an exact physical and odd clock with height control.

## The sharper estimate already in PR 195

Cut the reverse stream at its \(k\)th one, before requiring a completed mark. If this clock is \(e\), the corresponding chronological suffix starts odd, has precisely \(k\) ones, and gives \(G=2^e/3^k,\ R_k=C/2^e\). For fixed bounded real offset \(R_k\le B\), distinct eligible carries in one ternary residue form a subset of one congruence class modulo \(3^k\) in \([0,B2^e]\), of size at most \(1+BG\). Since \(R_k\ge1/(3G)\), a nonempty such family has size at most \(4BG\). At a fixed **positive ordinary endpoint** \(q\), choose that exact lift. Every integral source obeys the prescribed parity row by backward cancellation modulo 2 at each step, and it is positive since both inverse branches of a positive integer, when integral, are positive. Distinct words at the same \(e\) give distinct ordinary sources \(0<x=G(q-R_k)<Gq\). At this endpoint the count is thus at most \(Gq\) without truncating \(R_k\).

Multiply these counts by the reverse-prefix probability cap \(C(e+1)^2 2^{-e}\) for each possible \(e\le8k\). The longer event has at most \(k-1\) ones in \(8k\) bits. If \(S\) is fair binomial of length \(8k\), its probability is at most \(4^k\mathbb E[4^{-S}]=[4(5/8)^8]^k\). The base times 3 is strictly below one, absorbing the polynomial factor from (S2). Summing the short and long clocks verifies the source bounds

\[
 \Pr(Q\equiv r\bmod3^k,\ R_k\le B)\ll B(k+1)^3 3^{-k}\quad(B\ge1),
 \qquad \nu_k(q)\ll q(k+1)^3 3^{-k}\quad(q\in\mathbb N_{>0}).
\]

Write \(b_i\) for the reverse bits and \(S_i\) for their partial sums. For \(0<s<1\), the \(s\)th power of the nonnegative series \(\beta=\sum_i b_i 3^{S_{i-1}}2^{-i}\) is bounded by the sum of the powers of the individual terms. Applying (S2) to each length-\((i-1)\) cylinder bounds the expected term by \(C_s i^2\rho_s^{i-1}\) with \(\rho_s=(1+3^s)/2^{1+s}<1\), by strict concavity. Monotone convergence gives \(\mathbb E\beta^s<\infty\). Dyadically stratifying \(\beta\) by \(J\) where \(\beta\le2^J\), the moment gives \(\mathbb E J<\infty\) and \(H(J)<\infty\) by comparison with the geometric law \(2^{-j-1}\). If \(p_j=\Pr(J=j)>0\), every depth-\(k\) cell conditioned on \(J=j\) has mass at most \(C2^j(k+1)^3 3^{-k}/p_j\). Average the min-entropy lower bound over \(j\) and use conditioning to obtain PR 195's sharper \(k\log 3-H(\nu_k)\le3\log(k+1)+O(1)\). The source's heavy-cell cutoff \(k^{10}3^{-k}\), offset cap \(k^4\), half moment and light cutoff \(k^{-2}3^{-k}\) give the almost-sure logarithmic error.

One immediate reformulation of their estimates is useful for arbitrary residues. Writing \(\eta=|E|3^{-k}\), the sum over a residue set is bounded by \(C B(k+1)^3\eta+C_s B^{-s}\). If \(0<(k+1)^3\eta<1\), take \(B=((k+1)^3\eta)^{-1/(1+s)}\). Consequently

\[
 \nu_k(E)\ll_s\min(1,((k+1)^3|E|3^{-k})^{s/(1+s)}).
\]

At a singleton this gives the asserted uniform upper exponent below \(1/2\); PR 195's ordinary estimate supplies the stronger exponent one at each fixed positive integer with its height in the prefactor. None of these prefix estimates supplies a completed paired inverse at that integer. [Prior PR 195 proof](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round5/renewal/README.md)

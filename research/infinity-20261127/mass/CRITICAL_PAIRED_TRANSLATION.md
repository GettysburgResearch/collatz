# Positive-mass exact translations between two critical source populations

Use the shortcut Collatz map on positive rational numbers with odd denominator. Put \(\lambda=\log_2 3\), \(p=1/\lambda\). For \(K\ge2\) take
\[
 n=\lfloor\lambda(K-1)\rfloor+1,\quad Q=2^n,\quad D=3^K,\quad s_K=Q/D .
\]
Then \(K=\lceil pn\rceil\) and \(1/3<s_K<2/3\). The census \(S_K\) consists of all numerators \(Q/2\le a<13Q/2\), coprime to six, whose actual trajectory from \(a/D\) satisfies \(2^i\le3^{g_i}\) for every \(i\le n\), with \(g_i\) the first \(i\) odd departures. Write \(z_K(a)=T^n(a/D)\), an ordinary positive integer. This is precisely the passing population of the [critical source sector](../../six-hour-20261127/escape/CRITICAL_SOURCE_SECTOR.md) on the indicated sequence of depths. Probability below means cardinality divided by \(|S_K|\).

**Written theorem.** Fix \(q\equiv17\bmod48\), \(q>0\), a nonnegative integer \(r\), a real \(1\le x\le3/2\) and \(0<\epsilon<1/16\). For all sufficiently large \(K\) there are an integer \(d_K\ne0\) and \(A_K\subseteq S_K\) such that, for every \(a\in A_K\),
\[
 \begin{gathered}
 a+d_K\in S_K,\qquad z_K(a)=q,\qquad z_K(a+d_K)=3q,\\
  |a/D-x|,\; |(a+d_K)/D-x|<\epsilon,\quad
 2^r\mid d_K,\quad |d_K|/D<2\epsilon,\\
 |A_K|/|S_K|\ \ge \exp[-C(3/2)^r q]\,\epsilon^C .
 \end{gathered}                                                        \tag{1}
\]
Here and below \(C\) can be enlarged by an absolute factor. Both true physical paths start with at least \(r\) odd departures and execute one identical binary block of length \(n-O((3/2)^rq+\log(1/\epsilon))\) at the same absolute clocks. Branch one first becomes ordinary at \(n-1\), landing on \(2q\); branch two first becomes ordinary at \(n\), landing on \(3q\).

There is also a fixed-head version. For fixed \(q,r\), an infinite subsequence \(K_j\) has
\[
  |d_{K_j}|/3^{K_j}\longrightarrow0,\qquad 2^r\mid d_{K_j},
  \qquad |A_{K_j}|/|S_{K_j}|\ge\exp[-C(3/2)^r q].                   \tag{2}
\]
The bound in (2) stays positive as the real translation tends to zero, with \(q,r\) fixed. Neither (1) nor (2) identifies the two rational starts or their ordinary components.

## Constructing the two heads

For a binary word \(w\) of length \(P\) and grade \(J\), let \(C(w)=\sum_{i:e_i=1}2^i3^{J-g_{i+1}}\), \(G(w)=C(w)/3^J\), \(R(w)=2^P/3^J\). Then \(G(uv)=G(u)+R(u)G(v)\). Appending zero bits preserves \(G\). In gap notation a positive integer \(e\) represents the block \(1\,0^{e-1}\); thus a list of \(M\) gaps with clocks \(B_i=e_1+\cdots+e_i\) has carry \(\sum_{i=0}^{M-1}2^{B_i}/3^{i+1}\). If \(B_i\le\lambda i\) at every gap end, the entire binary block passes.

We construct heads of common grade and clock approximating the two numbers
\[
        V_i=s(y_i-2^{-h_i-1})-x,
 \qquad (y_1,h_1)=(q,1),\quad (y_2,h_2)=(3q,0),\quad 1/3\le s\le2/3 .
                                                                        \tag{3}
\]
Start with \(b=r+b_0\) unit gaps, where \(b_0\) is one absolute constant. Their carry and ratio are \(1-(2/3)^b\) and \((2/3)^b\). The normalized residual \(V=(V_i-1+(2/3)^b)(3/2)^b\) is positive and can be made uniformly larger than any fixed absolute threshold by choosing \(b_0\), since \(q\ge17\) and \(x\le3/2\). It is \(O((3/2)^rq)\).

Take a balanced list of \(M\) gaps with clocks \(B_j=\lfloor\lambda j\rfloor\), of ratio \(u=2^{B_M}/3^M\in(1/2,1]\) and carry \(G_M\). A disjoint swap \((2,1)\mapsto(1,2)\) at the internal clock \(i\) lowers only \(B_i\), reducing the carry by \(2^{B_i-1}/3^{i+1}\in(1/12,1/6]\). As \(\lambda>3/2\), consecutive unit gaps cannot occur. At least \((2-\lambda)M-1\) swappable pairs occur, since every unit gap except possibly the first follows a two. All swaps preserve the prefix gate. Add two unit gaps. Their carry contribution is \(5u/9\), and the new ratio is \(4u/9>2/9\).

Use four-gap blocks consisting of three ones and one two, with the two at any one of the four positions. Their ratios are \(\rho=32/81\), their carries \(c/81\) for \(c\in\{65,73,85,103\}\). The maps \(t\mapsto(c+32t)/81\) cover the interval \(I=[65/49,103/49]\) by their images of \(I\): the outside endpoints agree and the largest successive digit gap \(18\) satisfies \(18<32(103-65)/49\). Every \(t\in I\) can therefore be approximated by \(L\) actual blocks, with error at most \((103/49)\rho^L\). They all pass from the bank supplied by the preceding two units. Indeed at the block start this bank in clock units is at least \(2(\lambda-1)>1\); a partial block of length \(j\) in gaps has clock at most \(j+1\), and the full block increases the bank by \(4\lambda-5>0\).

For each \(M\), running through the allowed swaps one at a time, the translates of \((4u/9)I\) overlap because their width exceeds \((2/9)(38/49)>1/6\). Their union is an interval with upper endpoint
\[
 U_M=G_M+u\{5/9+(4/9)(103/49)\}
\]
and length at least \(((2-\lambda)M-1)/12\). The increments \(|U_{M+4}-U_M|\) are bounded by an absolute constant since each new carry term is at most \(1/3\) and \(1/2<u\le1\). Also \(M/6\le G_M\le M/3\). In every residue class modulo four, the first \(M\) above a fixed absolute threshold with \(U_M\ge V\) therefore has \(M\le6V+O(1)\) and puts \(V\) inside the union, for all sufficiently large \(V\). This proves coarse coverage at every required residue.

Choose the same residue \(M\bmod4\) for both heads. Choose their common grade \(J\) so that \(J-b-2-M_i=4L_i\), with \(\min_i L_i\) at least a sufficiently large constant times \(1+\log(1/\epsilon)\). Thus \(J=O((3/2)^r q+\log(1/\epsilon))\). Apply the finite digit construction to the two coarse representations. Each resulting head \(H_i\) has
\[
    |G(H_i)-V_i|\le(103/49)(2/3)^b(4u_i/9)\rho^{L_i},
    \qquad R(H_i)=(2/3)^b(4u_i/9)\rho^{L_i}.
\]
Pad the shorter head with zero bits to the longer clock \(P\). Both heads now have the same ratio \(R=2^P/3^J=\max_iR(H_i)\). The padded head continues to pass since \(P<\lambda J\). The padding preserves both carries. By increasing the coefficient of \(\log(1/\epsilon)+1\), \(R\) and both carry errors are less than \(\epsilon/(4+C_*)\), where \(C_*\) is the absolute bridge carry bound below.

## One common bridge and exact translation of actual sources

Put \(l=K-J-1\), \(m=\lfloor\lambda l\rfloor\). There are at least \(c2^{H_2(p)m}(m+1)^{-3/2}\) different binary middle words \(W\) of length \(m\), grade \(l\), passing the critical gate with \(G(W)\le C_*\). Indeed cyclic rotation at the minimum for slope \(l/m\ge p\) gives at least \(\binom ml/m\) passing bridges at that slope. Stirling gives the stated order, since \(l-pm\) is bounded. The exponential marked ballot bound (8) in the [critical source sector](../../six-hour-20261127/escape/CRITICAL_SOURCE_SECTOR.md), at slope \(l/m\) and endpoint zero, shows that at least half these passing bridges have bounded \(\sum_j3^{-(g_j-(l/m)j)}\) after an absolute choice of \(C_*\). Their actual carry is at most this sum.

Append to each padded head the *same* \(W\), then \(z_i=n-h_i-1-P-m\) zeros, one last odd bit and \(h_i\) zeros. These \(z_i\) are nonnegative for large \(K\): \(\lambda J-P=-\log_2 R\) can be fixed larger than four. The long final even stretch ends at grade \(K-1\) and clock \(n-h_i-1\le\lfloor\lambda(K-1)\rfloor\); all its prefixes pass. The last odd and terminal suffix pass since \(K\ge pn\). At the common final clock the exact source reaching \(y_i\) is
\[
 a_i/D=s_K(y_i-2^{-h_i-1})-G(H_i)-R\,G(W).                            \tag{4}
\]
In fact \(a_i=2^ny_i-C(\mathrm{word}_i)\) is integral and odd. Modulo three, \(a_i\equiv2^{n-h_i-1}(2^{h_i+1}y_i-1)\); \(2q\) and \(3q\) are both different from two modulo three, so the initial fraction is reduced. Reversing the prescribed bits gives the real forward parity at every step. The positive starts in (4) stay positive. Each odd before clearance drops exactly one denominator power, and each even preserves it. This proves the asserted first-clearance statements. With \(s=s_K\), (4) is within \(\epsilon\) of \(x\); \(1\le x\le3/2\), \(1/3<s_K<2/3\) put all these numerators in the genuine six-lift interval.

The common \(R\,G(W)\) cancels from the actual difference. In particular for the stated pair
\[
 d_K=2^{n-2}(8q-1)-3^{K-J}\big(C(H_2)-C(H_1)\big).                   \tag{5}
\]
This is one translation for every selected bridge. Determinism and the distinct endpoints give \(d_K\ne0\). The common initial \(b\) ones imply \(2^b\mid d_K\): the first \(b\) bits pick the same numerator residue modulo \(2^b\) at the common odd denominator. Different middle words produce distinct actual sources. Divide their count by \(|S_K|\asymp2^{H_2(p)n}(n+1)^{-3/2}\), proved in the critical sector. Since \(n-m=\lambda J+O(1)\), the paired fraction is at least \(\exp(-CJ)\). This proves (1), including the shared-clock length bound.

For (2), use \(s=1/2\), \(x=5/4\) and an absolute small tolerance to choose the two heads once. Set
\[
 s_*={G(H_2)-G(H_1)\over 2q-1/4}.
\]
By (3) and the carry error, \(s_*\) is in the interior of \((1/3,2/3)\) and \(|s_*-1/2|\ll\epsilon/q\). The phases \(s_K=(2/3)2^{-\{(K-1)\lambda\}}\) are dense by irrational rotation. Choose an increasing sequence \(K_j\) with \(s_{K_j}\to s_*\). The same heads and bridge count stay valid. The real sources remain inside the six-lift sector by (4) and the fixed interior margins. Equation (5) gives \(d_{K_j}/3^{K_j}=(2q-1/4)(s_{K_j}-s_*)\), proving (2).

## The norm this forces, and the missing upper bound

For any bounded ordinary label \(b\), put \(B_K(a)=b(z_K(a))\) and
\[
 {\cal V}_K(d)=|S_K|^{-1}
 \sum_{a\in S_K:\ a+d\in S_K}|B_K(a+d)-B_K(a)|.
\]
Equations (1) and (2) lower-bound this norm by their respective mass fractions times \(|b(3q)-b(q)|\). For a genuinely invariant ordinary component label, the finite measurement therefore retains the canonical disagreement on a uniform positive fraction at fixed \(q,r\), even along translations tending to zero in real scale. The shifts vary with \(K\); their fixed-\(r\) dyadic divisibility does not say their dyadic norms tend to zero. No translation upper bound for invariant labels on this actual *conditioned rational census* is supplied by the construction. A result about unconditioned ordinary source intervals requires a transfer argument.

The same argument applies to any two sufficiently large fixed \(y_i\) with \(h_i\in\{0,1\}\), \(2^{h_i}y_i\not\equiv2\bmod3\), and distinct \(y_i-2^{-h_i-1}\). For the control \(y_1=113,y_2=509,h_1=h_2=1\), the first target reaches one without visiting five and the second visits five. The visit-five label has an actual edge defect at \(5\to8\). This example gives positive variation for arbitrarily small real shifts on the very same census, even when the initial rational paths agree on the long middle and avoid five before both targets. Any regularity proof for invariant labels must use their zero edge defects.

[Lean arithmetic and physical replay](CriticalPairTransport.lean) · [Exact integer controls](check_critical_pairs.py). The all-size head-selection, marked bridge count, phase subsequence and population estimates above are written arguments.

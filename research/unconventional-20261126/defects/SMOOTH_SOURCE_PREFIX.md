# How long a shifted smooth source stays at its initial logarithmic height

Use the odd Syracuse map \(F(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers. Call a transition with exponent \(v_2(3x+1)\ge2\) a reset. For \(x>1\) a reset is a strict decrease of the odd map, and every other odd transition is a strict increase. A complete block consists of all successive exponent-one transitions up to and including the following reset. Every positive odd source has a next complete block, as shown below. Heights and asymptotic expressions in this note use natural logarithms.

## A uniform theorem for ordinary inputs

Fix a finite nonempty set \(S\) of odd primes, a constant \(B>0\), and \(0<\epsilon<1/2\). Let \(H\to\infty\) through positive integers with prime factors in \(S\), and set \(L=\log H\). Consider all odd positive ordinary sources of the form
\[
 x=\frac{uH+v}{d2^a},\qquad u,d\in\mathbb N_{>0},\ d\ \text{odd},\quad a\ge0,\quad v\in\mathbb Z,
\]
for which
\[
 h_0=1+\log(1+u)+\log(1+|v|)+\log d+a\log2
 \le [\log(2+L)]^B .
\]

**Theorem 3.** Uniformly over these inputs, every state \(q\) on each of the following two initial segments satisfies \(\log q=L+O_{S,B,\epsilon}(L^{1-\epsilon/2})\) for sufficiently large \(H\). Each segment includes its terminal state.

1. The first \(\lfloor(1-\epsilon)\log L/\log\log L\rfloor\) ordinary odd transitions.
2. The first \(\lfloor(1/2-\epsilon)\log L/\log\log L\rfloor\) complete blocks. The second assertion allows an unrestricted number of exponent-one transitions in every block.

In particular the logarithmic height is \((1+o(1))\log H\) throughout both segments. The constants are effective, though the proof gives no practical small cutoffs for these asymptotics.

### The arithmetic estimate

For fixed \(S\), integers \(U>0,V\), and \(UH+V\ne0\),
\[
 v_2(UH+V)\le C_S[1+\log(1+U)+\log(1+|V|)]\log(2+L). \tag{1}
\]
For \(V=0\) this follows from \(v_2(H)=0\). For nonzero \(V\), unequal dyadic valuations of \(U,V\) give their minimum. When they agree, factor out \(2^e\), where \(e=v_2(V)\), and apply Yu's Theorem 1 to the nonzero product difference \((-U/V)\prod_{p\in S}p^{n_p}-1\), where \(H=\prod p^{n_p}\). All bases are dyadic units. Work in \(K=\mathbb Q(\zeta_3)\) at a prime over 2, satisfying Yu's condition (1.2). Restricting the discrete valuation to rationals just multiplies \(v_2\) by the fixed ramification index. The finitely many fixed rational primes have bounded heights, and the logarithmic height of \(-U/V\) is at most \(\log\max(U,|V|)\). Yu's \(B\) in (1.8) can be \(\max(3,1,\max_p n_p)\), with \(n_p\le L/\log 3\). The product difference equals \(-(UH+V)/V\). Adding back \(v_2(V)=e\) proves (1). No multiplicative independence is required in this version of Theorem 1. [K. Yu, *p-adic logarithmic forms and group varieties II*, Acta Arith. 89 (1999), pp. 337–339, (1.2), (1.8), Theorem 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

### Exact updates and their coefficient heights

For one true odd transition from the displayed representation, write \(e=v_2(3x+1)\). Then
\[
 a+e=v_2(3uH+3v+d2^a),\quad
 (u',v',a')=(3u,3v+d2^a,a+e).
\]
The new denominator is \(d2^{a'}\). Its numerator is positive, since \(3x+1>0\). Formula (1) bounds \(a+e\) by \(C_S h\log(2+L)\), where \(h\) is the coefficient height defined as for \(h_0\). The logs of the new coefficients satisfy the same bound. Enlarging \(C_S\), one odd transition takes \(h\) to at most \(C_Sh\log(2+L)\).

For a whole block put \(t=v_2(x+1)\ge1\), \(w=(x+1)/2^t\). Its first \(t\) odd inputs are
\[
 x_j=3^j2^{t-j}w-1,\qquad 0\le j<t .
\]
They follow by substitution for \(j<t-1\), when the odd division exponent is one. The final odd input gives \(3x_{t-1}+1=2(3^tw-1)\). Since \(3^t w\ge3\) is odd, \(b=v_2(3^tw-1)\ge1\) is finite. Its exponent is \(b+1\), and its output is \((3^t w-1)/2^b\). Exact coefficient updates at the end of a whole block are therefore
\[
\begin{split}
 a+t&=v_2(uH+v+d2^a),\\
 u'&=3^t u,\qquad v'=3^t(v+d2^a)-d2^{a+t},\\
 a'&=a+t+b=v_2(u'H+v').
\end{split}
\]
Both applications of (1) have nonzero arguments because \(x+1>0\) and \(3^t w-1>0\). The first gives \(a+t\le C_Sh\log(2+L)\); then \(1+\log(1+u')+\log(1+|v'|)\le C(h+t)\). The second gives \(a'\le C_Sh[\log(2+L)]^2\). For each intermediate \(j<t\), the numerator coefficients are \(3^j u, 3^j(v+d2^a)-d2^{a+j}\) and the denominator is \(d2^{a+j}\). The same height bound holds for all states in the block. After increasing a constant, one complete block takes every intermediate height and its terminal height to at most \(C_Sh[\log(2+L)]^2\).

If the cost per step or block has exponent \(k=1\) or \(2\) respectively, after at most \(J\) such operations the heights are at most \(h_0(C_S[\log(2+L)]^k)^J\). With \(J=\lfloor(1/k-\epsilon)\log L/\log\log L\rfloor\), the logarithm of this upper bound is at most \((1-k\epsilon+o(1))\log L\). Thus all coefficient heights are at most \(L^{1-\epsilon/2}\) for sufficiently large \(L\). For each state \(q\), the positivity \(u\ge1\) and \(|v|\le\exp(h)=o(H)\) give \(H/2\le uH+v\le 2e^hH\). With \(1\le d2^a\le e^h\) this proves the asserted logarithmic height estimates.

## Ordinary descent from every sufficiently large Mersenne start

Let \(M_m=2^m-1\). Starting with \(w=1,t=m\), the first block is \(2^{m-j}3^j-1\) at the first \(m\) odd inputs. It ends at \(x=(3^m-1)/2^{v_2(3^m-1)}\). Set \(H=3^m\) and \(L=m\log 3\). Formula (1) bounds this initial denominator exponent by \(O(\log m)\), as also follows from elementary factorization. Thus \(u=1,v=-1,d=1\) and the hypotheses of Theorem 3 hold for all sufficiently large \(m\), for example with \(B=2\).

**Corollary 4.** Through its first complete block every preterminal odd state is at least \(M_m\). Following that block, all odd states throughout either of the following additional prefixes have size \(3^{m+O_{\epsilon}(m^{1-\epsilon/2})}>M_m\) for all sufficiently large \(m\).

* The first \(\lfloor(1-\epsilon)\log(m\log 3)/\log\log(m\log3)\rfloor\) odd transitions.
* The first \(\lfloor(1/2-\epsilon)\log(m\log 3)/\log\log(m\log3)\rfloor\) complete blocks and every odd state within them.

Consequently any first strict descent below \(M_m\) requires more than this many complete resets, even after excluding the initial Mersenne rise and its first reset from the count. No convergence hypothesis is needed for these two prefix statements. Any intermediate even shortcut states before the first smaller odd state lie at least as high as the following odd state, by repeated halving.

There is also an additive bound at the usual shortcut stopping time. Put \(T(n)=n/2\) for even \(n\) and \(T(n)=(3n+1)/2\) for odd \(n\). If the first strict descent occurs at time \(h\), and \(s\) of its inputs are odd, then \(T^h(M_m)\ge3^s M_m/2^h\), whence \(h>s\log_2 3\). The first Mersenne block uses \(m\) odd inputs, and all the additional individual odd transitions in Corollary 4 must also precede the first descent. Thus for every fixed \(\epsilon>0\), as \(m\to\infty\),
\[
 h>\log_2 3\left(m+\left\lfloor (1-\epsilon)\frac{\log(m\log 3)}{\log\log(m\log 3)}\right\rfloor\right).
\]
The leading bound \(m\log_2 3\) follows from the initial Mersenne run alone. The assertions here control a diverging number of subsequent true decreases and the size of their intermediate states. They do not imply that a further strict descent occurs.

Repository commit 0410811710af2f7da71522ec67233528048adb9a gave a lower bound on the number of individual odd steps needed to reach an endpoint whose log height is sublinear in the ternary exponent, via real logarithmic forms. A separate result there excludes earlier shifted-ternary-power mergers on selected congruence classes. The current argument uses a forward dyadic estimate for all smooth \(H\), keeps the logarithmic height near \(\log H\), and allows unrestricted intervening odd runs at fixed reset count. Repository commit 156652e03fe7a78f9cd4442039779cc622fdf3de studies two genuine post-ascent checkpoints on a specified least-defect row and finite ordinary merger tests. These scope comparisons do not assert historical priority. [Odd-cost proof](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/MERSENNE_ODD_COST.md) · [Two-checkpoint argument](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/source-progress/TWO_CHECKPOINT_RESCUE.md)

Theorem 2 of rStation paper 15 bounds the upper height on a fixed-budget periodic-dictionary segment in terms of a general starting integer. Its Corollary 4 bounds the dictionary complexity of long cycles. The lower-height bound here uses the special low-height linear representation in an odd smooth source to control a diverging number of actual blocks. Paper 21 constructs earlier-source mergers before descent for a density-one set of exponents on shifted-power families. Its source-removal conclusion has a different quantifier from Corollary 4 here, which controls size for every large exponent and does not assert any merger. [Paper 15](https://rstation.ai/problems/collatz/papers/15) · [Paper 21, Theorem 6 and Corollary 7](https://rstation.ai/problems/collatz/papers/21)

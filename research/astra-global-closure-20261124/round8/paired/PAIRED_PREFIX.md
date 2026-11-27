# Two ordinary profiles at the native binary clock

**R8-P3, unconditional written estimate.** The clock here is the length \(h\) of an aligned binary block. It is substantially earlier than H's polylogarithmic landing clock in [R8-P1](README.md). This estimate works on a block at **any** positive location, with no analytic input. It retains both parities' affine slopes under arbitrary further lifts of the same source. It gives smaller and larger partners in the two literal components even when those components differ.

Fix \(w>0\), \(N=2^h\), \(b\ge0\), and keep positive odd units \(x\in[bN,(b+1)N)\). Put
\[
 p=P_h(x),\quad p'=P_h(3x),\quad J=\max(p,1+p'),\qquad G_J=N/3^J.
\]
Apart from \(O_w(N/h^w)\) original starts, each \(x\) has at least \(\lfloor G_J/h^{C_w}\rfloor\) distinct strictly smaller units in its block and as many strictly larger ones in its block, all with the **same** \(x\bmod3\) and full four entries
\[
 (p,T^h x,p',T^h(3x)).
\]
Every selected partner is within \(G_J h^{C_w}\) of \(x\). One can take \(C_w=3w+8\). The constants are uniform in the block position. With a further \(O_w(N/h^w)\) exclusions, \(J=h/2+O_w(\sqrt{h\log h})\), so these families have size \(2^{(1-(\log_2 3)/2)h-O_w(\sqrt{h\log h})}\). The four-profile equalities persist on translating both starts by \(N t\), \(t\ge0\), by the physical parity-lift identity. Restrict \(t\bmod3\) when a common unit source class is desired after translation.

**Proof.** On the complete block of \(N\) consecutive integers, the first \(h\) parity bits of each individual arm are independent fair bits under the original uniform source, by the triangular parity bijection. Multiplication by 3 permutes the binary residues. Independence between arms is never needed. Let \(\beta\) be either arm's final real affine offset, initialized at zero, with update \(b'=(3^\epsilon b+\epsilon)/2\). The conditional expectation of \(\sqrt{b'}\) given this arm's parity past is at most
\[
 \lambda\sqrt b+1,\qquad \lambda=(\sqrt{1/2}+\sqrt{3/2})/2<1.
\]
Thus \(\mathbb E\sqrt\beta\le(1-\lambda)^{-1}\) at every depth. With \(R=h^{2w+2}\), remove \(O_w(N/h^{w+1})\) sources where either real offset exceeds \(R\), by Markov. Both endpoints are now of the form \(a(x/N)+\beta\) with slopes \(3^p\) and \(3^{1+p'}\). Let \(S=3^J\) and \(s\le S\) be the other slope. At fixed \(p,p'\) the larger-slope endpoint \(v\) is in an interval of length \(S+R\) on the whole block. With \(v\) fixed, the smaller-slope endpoint belongs to \([(s/S)v-R,(s/S)v+R]\) after eliminating the same real input \(x/N\).

If \(S<R\), it is convenient to exclude this grade pair via the ordinary binomial tails. Away from \(O_w(N/h^w)\) sources both counts differ from \(h/2\) by at most \(c_w\sqrt{h\log h}\), by Hoeffding. This makes \(S\ge R\) for large \(h\), uniformly. There are then \(O(SR)\) possible integer endpoint pairs per grade pair. Split further into the two source classes modulo three after restricting to odd units. Mark the first and last \(m_J=\lfloor N/(S h^{C_w})\rfloor\) elements in each such class. The total marked over the \(O(h^2)\) grade pairs is
\[
 O\bigl(h^2 S R\,N/(S h^{C_w})\bigr)=O_w(N/h^w),
\]
where the factors \(S\) cancel separately within each grade pair. Every other source has the claimed strictly ordered partners among the unmarked-for-height sources with that four-profile. Equality on the larger-slope arm gives \(|u-x|\le NR/S\) since both real offsets lie in \([0,R]\). This proves the assertion. If the central grade window is fixed instead as \(|p-h/2|,|p'-h/2|\le\epsilon h\), its omitted binomial tail is exponentially small with a rate depending on \(\epsilon\). The shrinking-width result above only claims inverse powers of \(h\) as exceptional fractions.

The one-arm prefix representative estimate in PR146 groups by a single count and endpoint. The restriction to a shared real input bounds the number of **joint** endpoint pairs at the present two fixed grades by \(O(SR)\). Paper 19 treats a different word multiplicity for a stationary real/ternary affine measure. Its same-count rectangle geometry and conditional entropy conclusions do not give a count on a prescribed ordinary pair of components. [PR146, prefix representatives](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/PREFIX_REPRESENTATIVES.md) · [Weaver, paper 19 v2, sections 1–3](https://rstation.ai/problems/collatz/papers/19/v2)

## R8-P4. Strict contraction around an actual ordinary anchor

Let \(r\) be a positive odd unit and suppose its two actual starts \(r,3r\) are each in the \(1,2\) cycle by the same clock \(h\ge1\). Their phases at \(h\) may differ. For each \(t>0\), let
\[
 q=r+2^{h+2}t,\qquad q'=r+3\cdot2^h t.
\]
Then \(0<q'<q\), \(q'\) is an odd ternary unit, and
\[
 T^{h+2}(q)=T^h(q'),\qquad T^{h+2}(3q)=T^h(3q').
\]
Indeed the next two steps on the cycle fix each endpoint and add exactly one odd input. A lift by \(2^{h+2}t\) adds \(3^{P_h(r)+1}t\) at clock \(h+2\), the same increment as the \(3\cdot2^h t\) lift at clock \(h\). Replace \(r,t\) by \(3r,3t\) for the upper arm. This proves equality of the actual ordered components and the descent of any failure on an eligible \(q\). An original source \(q>r\) with \(v_2(q-r)=h+2j+d\), \(d\in\{0,1\}\), can take \(j\) such contractions from this anchor. The final difference from \(r\) has binary order \(h+d\). The \(r=1\) contraction includes PR146's \(1+16\cdot4t\) to \(1+16\cdot3t\) comparison. [PR146, stabilized core](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/STABILIZED_CORE_DESCENT.md)

**Coverage.** Every choice \(r,h\) requires both original anchor hits at or before that clock. No cover of all exceptional units by these cylinders has been established. In particular a symbolic same-clock merger of the two anchor arms on the whole cylinder may already give equal component labels throughout that cylinder. A dense supply of such cylinders does not decide the specified member of their complement. P3's aggregate counts also allow the least failed source to be exceptional. The independent unit review discusses the supercritical odd counts forced on its nonconvergent arm.

[Finite kernel](PairedProfiles.lean) · [Native and anchor controls](check.py)

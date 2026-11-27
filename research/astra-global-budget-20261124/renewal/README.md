# Concentrated paired predecessors of every fixed ordinary target

**PROPOSED, source-qualified.** Write \(T(n)=n/2\) on even positive integers and \(T(n)=(3n+1)/2\) on odd ones. A unit is a positive odd integer prime to three. For **every fixed unit** \(q\) there are unbounded real \(X\) and intervals \([X-H,X]\) in which at least \(cH/\log\log X\) distinct units \(x\) reach the pair \((q,5q)\) from \((x,5x)\). All the retained sources in one interval use the **same shortcut clock and the same odd count on both arms**, via concatenations of genuine completed ratio-five returns. With natural logs,
\[
 H=(\log X)^{\kappa+O(1/\sqrt{\log\log X})},\qquad
 \kappa=\frac{\log(4/3)}{\log 3}.
\]
The first segment of each path is nearly central in its clock and has bounded real offset. The final segment imports the one prescribed ordinary pair. Consequently the clusters also carry the same ordered pair of orbit-invariant colors as the fixed target. The estimate does not require the target or its companion to be nonperiodic.

There are also many clusters at every large scale. For all sufficiently large \(Y\), the interval \([Y,Y^2]\) contains \(\gg\log Y/\log\log Y\) disjoint intervals of a common length \(H_Y\), where \(c_1\log\log Y\le\log H_Y\le c_2\log\log Y\) with positive absolute constants. Each contains \(\gg H_Y/\log\log Y\) such paired predecessors of the prescribed \(q\).

PR202's growing blocks follow one ordinary arm. PR146 gives whole consecutive blocks for both arms at the smaller guaranteed length \(\exp(c\sqrt{\log\log X})\). Here both arms are retained at larger local length along the displayed sequence, with occupancy \(\gg 1/\log\log X\). These comparisons leave PR202's single-arm and PR146's consecutivity conclusions intact.

## 1. Row lower mass for completed returns

Use the source-qualified iid marked-block law of PR200. From an odd source sample the fair parity bits after its prescribed initial odd bit. A block ends at the first positive same-ratio, equal-odd-count return, followed by all common even steps up to the next odd sentinel. A chronological concatenation with length \(e\), odd count \(p\) and affine carry \(C\) has probability \(2^{-e}\), with a unique parsing given the terminal sentinel. The iid lengths \(L_i\) have \(c/\sqrt t\le\Pr(L_i>t)\le C_0/\sqrt t\) for large \(t\), by PR146's two-sided first-return bound and geometric padding. Write \(S_j=\sum_{i\le j}L_i\).

For every large integer \(N\), there exist one pair \((p,e)\) and a set \(\mathcal W\) of distinct chronological **complete** words of this row such that
\[
 c_0N\le e\le C_1N,\quad |p-e/2|\le K\sqrt N,\quad
 0<C_w/2^e\le B,\quad
 |\mathcal W|2^{-e}\ge c_3/N.                                      \tag{1}
\]
All constants, including the real cutoff \(B\ge1\), are absolute.

Indeed, for every integer \(j\in[\sqrt N,2\sqrt N]\), a sufficiently small fixed \(c_0>0\) gives \(\Pr(S_j<c_0N)\le\Pr(\max_{i\le j}L_i<c_0N)<1/8\). For a sufficiently large fixed \(C_1\), putting \(u=C_1N\) gives
\[
 \Pr(S_j>u)\le j\Pr(L>u)+j\,\mathbb E[L\mathbf1_{L\le u}]/u
 \ll j/\sqrt u<1/8.
\]
The underlying forward parity bits after the first are fair. The maximal inequality for centered independent sums bounds the probability of \(|p_t-t/2|>K\sqrt N\) at **any** \(t\le C_1N\) by less than \(1/8\) on increasing \(K\). This covers \(t=S_j\) on the retained length event without conditioning the fair bits on a mark. At deterministic mark index \(j\), the real offset from input zero has in distribution the real affine series truncated after \(j\) outermost blocks: iid block order is reversible in distribution. That truncation is bounded by the positive infinite series, whose square-root moment is finite by PR195 round 5, renewal §3. Another \(1/8\) exception therefore suffices for the common fixed cutoff \(B\).

The union bound leaves probability at least \(1/2\) for each such \(j\). Sum over the \(\asymp\sqrt N\) indices. A complete length-\(e\) word with terminal odd sentinel can occur at only one of these indices, by the deterministic parsing. There are \(O(N^{3/2})\) candidate rows in this window. Averaging proves (1). No bounded-width assertion about \(e-2p\) is used.

## 2. From symbolic mass to populated ordinary cells

Put \(G=2^e/3^p\), which grows exponentially in \(N\) by (1), and \(m=3^{p+1}\). For each of the \(2\cdot3^p\) unit residues \(r\bmod m\), let \(M_r\) count the words in (1) for which
\[
    2^e r=C_w\pmod {3^p},\qquad 2^e r\ne C_w\pmod {3^{p+1}}.         \tag{2}
\]
Every word hits exactly **two** residues, both units, since its carry is a unit mod three. Thus the mean of \(M_r\) is \(|\mathcal W|3^{-p}\ge c_3G/N\). For **each positive odd lift** \(Q\) of a given unit residue, each counted word has
\[
     x=(2^eQ-C_w)/3^p\in[G(Q-B),GQ).
\]
The whole-word integral lifting lemma gives a positive integer with exactly the prescribed parities. The first bit and the second condition in (2) make it an odd unit. The mark cylinders certify the second arm as well, and \(Q\) is an odd terminal sentinel. Different words of one fixed clock give different ordinary sources. In particular \(M_r\le BG+1\), uniformly in the chosen lift. Splitting the mean at \(c_3G/(2N)\) proves that a fraction \(\gg 1/N\) of all these residues have
\[
       M_r\ge c_3G/(2N).                                               \tag{3}
\]
Every positive odd lift of **every such residue** has this many actual synchronized predecessors in the indicated short interval. (3) is a lower estimate for completed returns on ordinary cells. It is stronger there than stationary full support; it does not say an arbitrary prescribed cell is among them.

There is a conditional-on-prefix form for **every** prescribed ternary unit class \(v\bmod3^s\), \(s\ge1\). Fix an odd lift of \(v\) and invert the six-step branch of the next section \(j=\lceil s/2\rceil\) times, choosing each padded exponent from \([6,23]\) to leave the intermediate an odd unit (primitive-root order modulo 27). The resulting fixed composition of forward blocks maps *all* ternary units under \(F(y)=(3^{2j}y+C)/2^D\) into \(v\bmod3^s\), since it maps the selected inverse endpoint to the chosen lift and \(D\le23j\). Every good cell \(r\) from (3) gives a different cell \(F(r)\bmod3^{p+1+2j}\). Every odd ordinary lift of that output has an integral odd-unit inverse \(y\) belonging to \(r\), by the affine congruence including the unit digit and the whole-word decoding lemma. The occupied fraction of all extensions of \(v\) to that precision is \(\gg1/N\): the number of good input cells is \(\gg3^p/N\), and the number of extensions is \(3^{p+1+2j-s}\le 9\cdot3^p\). Their paths have total row \((p+2j,e+D)\), and at least \(c_3G/(2N)\) distinct ordinary unit sources. For \(s=O(\log N)\) the extra height factor \(2^D/3^{2j}\) is at most polynomial in \(N\). This permits arbitrary coarse low digits with polynomial loss, while leaving the high digits of a prescribed ordinary target undecided.

## 3. Transfer to one fixed ordinary pair

The first-return cylinder \(49\bmod64\) has length six, two odd inputs and carry seven; its companion has the same count and returns in ratio five. For each good residue \(r\bmod3^{p+1}\), choose \(h\) in the interval \([P,2P)\), \(P=2\cdot3^{p+2}\), such that
\[
 2^h q\equiv 9r+7\pmod {3^{p+3}}.
\]
The right side is a unit, and two generates the whole unit group modulo this power of three. Each \(r\) determines exactly one such \(h\); distinct \(r\) give distinct exponents. The integer \(Q_h=(2^h q-7)/9\) is a positive odd unit in the chosen cell. It lies in \(49\bmod64\), reaches \(2^{h-6}q\) after six steps, then undergoes exactly \(h-6\) common halvings to the odd sentinel. Thus (3) supplies sources of a **single prescribed target**, at total clock \(e+h\) and odd count \(p+2\), equal on the two arms. At the intermediate clock \(e\), both arms are at \((Q_h,5Q_h)\).

Take \(X_h=GQ_h\), \(H=BG\). The intervals are disjoint for all sufficiently large \(N\), since successive integer exponents at least double \(Q_h\), whereas each interval has the same width \(BG\). There are \(\gg3^p/N\) good choices per full period. Here \(\log\log X_h=p\log3+O_q(1)\) and \(\log H=p\log(4/3)+O(\sqrt p)\) by (1); this proves the stated exponent along unbounded scales. All clocks after the initial near-central segment are included in the count.

For the every-scale statement choose \(N=\lfloor c_4\log\log Y\rfloor\) for a sufficiently small fixed \(c_4>0\) that \(P=o(\log Y)\). In the integer exponent interval \([\tfrac54\log_2Y,\tfrac74\log_2Y]\), every full period of length \(P\) has the same fraction \(\gg1/N\) of good exponents. There are therefore \(\gg\log Y/N\) suitable exponents. The factor \(G=\exp(O(N))\), the fixed \(q\), and the width \(BG\) leave every cluster inside \([Y,Y^2]\) for large \(Y\). The lower bound on \(\log H_Y\) follows from \(e\ge c_0N\).

### Amplifying the number of occupied intervals from the same root

The finite-branch pressure certificate of PR200, `RATIO_PRESSURE.md`, §3, also applies to a fixed pair of arbitrary colors: growth, disjointness and the common odd sentinel do not use those colors. First take a sufficiently large paired ancestor of the prescribed \(q\) using the padded six-step branch. Thus for every large \(Y\) its stopped ordinary tree supplies \(\gg_q Y^{1/9}\) different unit intermediates \(a\in[Y/2^{400},Y]\), each with a known complete paired path to \(q\). This paragraph additionally imports that finite pressure certificate.

Use the same row \(N=\lfloor c_4\log\log Y\rfloor\) for all these intermediates. For each \(a\) choose one good \(h\in[P,2P)\) and put \(Q=(2^h a-7)/9\) as above. Each \(Q\) determines both \(h=v_2(9Q+7)\) and its odd factor \(a\). All the selected \(Q\)'s are therefore distinct positive integers. Their intervals have centers \(GQ\) and common width \(BG\); greedily keeping disjoint intervals loses at most \(2\lceil B\rceil+1\) candidate centers per selection. For sufficiently large \(Y\) all the intervals lie in
\[
 [Y,\,Y\exp(O(P+N))]=[Y,Y^{1+o(1)}],
\]
since \(P\to\infty\) and \(P=o(\log Y)\). We obtain \(\gg_q Y^{1/9}\) disjoint intervals of common polylogarithmic length, each occupied at proportion \(\gg1/\log\log Y\) by actual paired predecessors of the same fixed \(q\). In any one interval the appended known path from \(a\) has the same clock and odd count for every retained source. The result supplies many separate intervals; the exponent-one global pressure is still missing.

## 4. The cost the argument still pays

For one prescribed unit \(q\), the row estimate would give \(\gg G/N\) ancestors below \(qG\) if its own residue were good. The constructed intermediate \(Q_h\) ensures the needed cell but changes the upper cutoff to \(GQ_h\). In the displayed single-period construction \(\log Q_h=\Theta_q(3^p)\), while \(\log G=\Theta(p)\). The local count is therefore not a near-linear count under the full height cutoff for \(q\).

To remove this cost along a sequence, it would already suffice to route \((q,5q)\) backwards to some good \(Q\) of height \(\exp(o(p))\), through any legal completed words: (3) would give \(X^{1-o(1)}\) distinct paired predecessors below \(X=GQ\) on that sequence. A polynomial height in \(p\) retains a logarithmic loss. The cardinality of the good cells alone offers neither hitting bound: in the one-block discrete-log cycle any prescribed initial string of \(o(3^p)\) exponents can be deleted at negligible cost to the possible good-cell count. Additional distribution in this order or another actual paired route is needed. Even a near-linear paired count would still require an opposing estimate on the actual failure population for a contradiction. No fixed-floor hitting or head-mass summability is proved.

## Pins and finite checks

* PR146, `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md` (two-sided first-return tail and conditional renewal), and `WHOLE_INTERVAL_SYNCHRONIZATION.md` in the same directory (comparison only).
* PR200, `39918be724038ac550d77c7fc95d17e05251dfc6`, `research/regularity-rigidity-20261124/continuation/REVERSE_RENEWAL.md`, §§1–3, exact dictionary; `RATIO_PRESSURE.md`, §§1–2, padded-word arithmetic, and §3, the stopped ordinary finite-branch pressure bound for the amplified count.
* PR195, `1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97`, `research/astra-global-closure-20261124/round5/renewal/README.md`, §§2–3, whole-word lifting and finite real moments.
* PR202, `3b10b24d12d4b349cb20f4cbc83086c8a09f807e`, `research/synchronized-long-basin-blocks-20261124/README.md`, §§1–2, explicitly single-arm target comparison.

The [finite control](check.py) enumerates short completed rows, checks the exact all-unit-residue incidence count, and replays the full paired import at sample targets. The [Lean kernel](CellPressure.lean) verifies the mean-to-heavy-cells step and the affine arithmetic of the two segments.

# Information in the ordinary colors of four-trit truncations

**Status.** PROPOSED written theorem, relative to the source-qualified finite pair-merger bound and ordinary regeneration cited below. The physical parameter update and ternary truncation are kernel-checked in `PredictablePhysicalArms.lean`. The information estimates are written proofs. Collatz remains OPEN.

Fix an orbit-invariant binary color for the shortcut map. Use a fixed suffix \(r\), the ordinary parents \(n\) of the heads \(7R\le 81n+r<8R\), \(R=81^j\), and \(d=\log_2 R\). At \(3d\le t\le3.1d\) retain the coarse integer \(m=\lfloor 3^{k_0}2^{-t_0}n\rfloor\) of `LATE_WITNESS_TRACKS.md`, with \(t_0=\lfloor2.9d\rfloor,\ k_0=\lfloor t_0/2\rfloor,\ \Delta_t=t-t_0\). Write \(B_i\) for the \(i\)-th least significant bit of \(m\), starting at \(i=1\). All entropies use natural logarithms.

**Local information theorem.** Fix a nonempty open interval \(J\subset(7,8)\), and use the ordinary regeneration envelope on a compactly interior subarc of \(J\), with mark frequency \(\eta>0\). There are constants \(h\in\mathbb N,\ \gamma>0,\ C\) independent of the row. Let \(I\) be any \(D\ge(\log d)^6\) consecutive late clocks. Let \(S\) be any nonempty subset of genuinely discordant good parents in this suffix, of relative size \(w=|S|/N\) among its \(N=R/81\) parents. Sample uniformly from \(S\). The good envelope discards \(O_A(Rd^{-A})\) original heads across the full row. Set \(H=\max_{t\in I}\Delta_t+h\). One can give the following initial data \(U\) to an observer:

* the native residue \(n\bmod 2^{\lfloor d/2\rfloor}\) and the **entire** exterior quotient \(\lfloor m/2^H\rfloor\);
* both physical arms' effective exponents and bounded-by-a-power-of-\(d\) integer corrections at the first clock of \(I\).

At time \(t\), from \(P_t=(U,B_1,\ldots,B_{\Delta_t})\) and at most \(8+\lceil\log_2(1+s)\rceil\) binary orbit-color answers \(L_t\) on **ordinary trit truncations of the current larger-grade physical arm**, a specified procedure selects a bounded-correction positive head in \(\bigcup_{j\ge0}81^jJ\). Here \(s=O(\sqrt{d\log d})\) is the physical grade difference. A null selection is allowed. The answers at each clock start anew. On every \(n\in S\) the procedure selects a genuinely discordant head in this prescribed arc at every regeneration clock. Its choice may differ from the incidence construction's head.

For \(F_t=(B_{\Delta_t+1},\ldots,B_{\Delta_t+h})\), the **present** answers themselves satisfy
\[
 \sum_{t\in I} I(L_t;F_t\mid P_t)
       \ \ge\ \gamma D-h\log(Cd^C/w).                                      \tag{1}
\]
In particular, on any polynomial-density such subset a fixed positive fraction of its \(D\) clocks have \(I(L_t;F_t\mid P_t)\ge\gamma/2\) for sufficiently large \(d\). Each term is at most \(h\log 2\). The observer uses only the current clock's answers in addition to the public data. The entropy refers to random ordinary sources at these clocks. Early disclosure of every exterior high digit makes the identity of the tested future block precise.

## One-bit-lag physical transport

At the first clock \(\tau\), for either actual value \(Y=T^\tau(y)\), \(y=n\) or \(81n+r\), the scalar intercept bound in `HEAD_INCIDENCE.md` gives
\[
 Y=\lfloor 3^{g_Y}m/2^{\Delta_\tau}\rfloor+b_Y,\qquad 0\le b_Y\le d^C.
\]
Here \(g_Y=p_y(\tau)+4{\bf1}_{y=81n+r}-k_0\), with \(p_y(\tau)\) counting odd steps. The suffix contribution and the dropped coarse fraction are each \(O(1)\) by the late exponent envelope. Hence the two pairs of seed values have at most \(d^C\) possible joint values after adjusting \(C\). At every clock write \(m=l+2^{\Delta_t}q\) with \(l\) public. The representation is exactly \(Y=3^gq+c\), where \(c\) is public, though it may be much larger than \(b_Y\). If \(q=2q'+e\), the next newly exposed bit is \(e\). For \(u=3^ge+c\), the successor is
\[
             T(Y)=3^{g+(u\bmod2)}q'+T(u).
\]
Both updated coefficients are available at the next clock. Thus the whole arithmetic history of the two arms, expressed in the still unrevealed quotient, has no repeated oracle cost. The grade difference is the difference of the current exponents. For \(0\le v\le g\),
\[
 \lfloor Y/3^v\rfloor
   =3^{g-v}q+\lfloor c/3^v\rfloor
   =\lfloor 3^{g-v}m/2^{\Delta_t}\rfloor+b_v .
\]
The exact integer \(b_v=\lfloor c/3^v\rfloor-\lfloor 3^{g-v}l/2^{\Delta_t}\rfloor\) is public.

Use the larger exponent arm \(Y\), breaking ties arbitrarily, and let \(s\) be its excess over the other. For each \(i=0,1,2,3\) form the possible chain with \(v=i,i+4,\ldots,i+4\lfloor(s-i)/4\rfloor\), when it has an edge. Discard a chain if some child falls outside the deterministic exponent/correction bounds (2)–(3) of `LATE_WITNESS_TRACKS.md`, including \(g-v\ge4\). This check uses the public coefficients only. At each regeneration clock the certified chain survives. All its children have the same bounded upper-arm correction estimate after division and exponents between the two physical envelopes. Also retain a chain only if all its child values are certainly in \(\bigcup_{j\ge0}81^j J\). This is a public check. For each child, bound its ordinary floor formula on the entire exterior cell \([2^H\lfloor m/2^H\rfloor,2^H(\lfloor m/2^H\rfloor+1))\) with the public bounded correction. Every original \(m\gg 2^{.39d}\) and \(H<.31d\), so the relative variation in this range is \(O(2^{-.08d}+1/z)\) at the true child \(z\), uniformly in the candidate exponent. The regeneration chain's children have a fixed interior mantissa margin and exponentially large heights; all pass for large \(d\). Query the endpoint colors of the at most four remaining chains. In the first chain whose answers differ, bisect the index interval, querying the middle color and retaining endpoints of opposite colors. This reaches a true discordant edge after at most \(\lceil\log_2(1+s)\rceil\) further queries. Return its exponent and correction, or a dummy if no chain qualified. The procedure uses no test for a physical meeting or for a mantissa mark. Regeneration counts its successes. Each query asks for the value of the fixed color at an ordinary integer specified by its public affine description and the hidden quotient.

## A local entropy calculation on the original row

For a fixed public prefix, selecting any single allowed parameter pair \((g,b)\) specifies the head \(z=3^gq+c_l\), its parent \(3^{g-4}q+\lfloor c_l/81\rfloor\) and its fixed suffix. On a uniform fresh \(h\)-bit block the parent varies bijectively modulo \(2^h\). The finite failure to merge the pair by clock \(h\) has probability at most \(C_0/\sqrt h\), uniformly in the selected pair. A true discordance implies this failure. Assign the dummy a test that always returns false. Fix \(h\) large enough that \(p_0=C_0/\sqrt h<\eta/2\). It is fixed before choosing \(d,I,S\). Ordinary good regeneration guarantees at least \(\eta D\) true selections for every \(n\in S\). If \(p_t\) is the actual probability of passing the finite failure test, then \(\sum p_t\ge\eta D\).

The total conditional bit-entropy deficit satisfies
\[
 \mathcal E=H\log 2-\operatorname H(B_1,\ldots,B_H\mid U)
       \le \log(Cd^C/w).                                                     \tag{2}
\]
Indeed, before adding the arm seeds, each triple \((n\bmod2^{\lfloor d/2\rfloor},\lfloor m/2^H\rfloor,m\bmod2^H)\) comes from at most \(C c_0^{-1}2^{-\lfloor d/2\rfloor}\) ordinary parents, \(c_0=3^{k_0}2^{-t_0}\). There are at most \(M/2^H+2\) possible exterior quotients with \(M=c_0N+O(1)>2^{.39d}\) intersecting cells and \(H<.31d\) for sufficiently large \(d\). Relative to the product of independent uniforms on the native residue, on this list of exterior quotients, and on the \(H\)-bit vector, the density after conditioning on \(S\) is at most \(C/w\), including the endpoint cells. Its KL divergence is at most \(\log(C/w)\). The entropy chain rule bounds the conditional deficit by that divergence. Disclosing a further \(d^C\)-valued seed raises it by at most \(C\log d\), proving (2).

Compare the actual joint law of \((P_t,L_t,F_t)\) with the law keeping \((P_t,L_t)\) and replacing only \(F_t\) by an independent uniform \(h\)-bit vector. The procedure gives its chosen parameters from \((P_t,L_t)\), so the latter law passes the finite failure test with probability at most \(p_0\). By data processing for KL, after averaging over \(t\) the sum of these divergences is at least \(D\,\mathrm{kl}(\eta,p_0)\), where \(\mathrm{kl}\) denotes binary KL. Indeed, include a uniform clock index in both laws and project to a single pass/fail bit. The projected success probabilities are at least \(\eta\) and at most \(p_0\), respectively. Each summand is exactly
\[
 I(L_t;F_t\mid P_t) +h\log2-\operatorname H(F_t\mid P_t).
\]
By the conditional entropy chain rule the second terms sum to at most \(h\mathcal E\). Each bit's nonnegative conditional deficit given \(U\) and all lower bits occurs at most \(h\) times. This proves (1) with \(\gamma=\mathrm{kl}(\eta,p_0)>0\). For polynomial \(w\), the right side is at least \(3\gamma D/4\) eventually. The uniform upper bound \(h\log2\) gives a positive fraction above \(\gamma/2\).

## Signed column identity and remaining issue

For zero-correction columns \(X_{t,g}=\lfloor 3^g m/2^{\Delta_t}\rfloor\), set \(C_{t,g}=f(X_{t,g})\), with colors regarded as zero and one. Since \(X_{t+1,g}=\lfloor X_{t,g}/2\rfloor\) and \(f(2n)=f(n)\),
\[
 J_{t,g}:=C_{t+1,g}-C_{t,g}
   ={\bf1}_{X_{t,g}\ {\rm odd}}\bigl(f(X_{t,g}-1)-f(X_{t,g})\bigr).
\]
Thus the change in the signed true four-trit difference \(C_{t,g}-C_{t,g-4}\) equals \(J_{t,g}-J_{t,g-4}\). Bounded rounding corrections contribute corresponding adjacent differences. The identity supplies no upper bound for weights depending on future colors. Likewise, (1) gives a necessary dependence of the selected ordinary color observations on nearby coarse bits. An upper bound below (1) for the remaining discordant sources is open. The polynomial density hypothesis applies row by row, and (1) retains the explicit cost for smaller densities.

**Inputs.** PR 197, `2c1397d2adcadc620381bca20c465f3bf31a6f8e`, `crossing-step/LATE_WITNESS_TRACKS.md` (ordinary projection (2)–(5), uniform regeneration), `two-class-descent/HEAD_INCIDENCE.md` (scalar intercept), `two-class-descent/ROUNDED_HEAD_DESCENT.md` (physical chains and endpoint meetings), relative to `research/ayh-resource-reset-20261124/`. The finite pair bound is PR 146, `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md`, for the bounded suffix family. James L. Massey's [Causality, Feedback and Directed Information](https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI532.pdf), ISITA 1990, equation (7), motivates the separation of available prefixes from later information. Formula (1) is an overlapping fixed-block conditional mutual-information calculation proved here.

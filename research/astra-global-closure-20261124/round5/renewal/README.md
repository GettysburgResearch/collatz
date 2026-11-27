# Ordinary target cylinders in the ratio-five return law

**PROPOSED written proof.** The exact first-return law and its reverse cylinder estimate are source-qualified inputs from PR200. The local count below gives an upper bound at every positive ordinary target. A new real-offset estimate gives logarithmic entropy deficit for the entire law. The ordinary descendant count at the end requires a lower estimate at completed marks and remains OPEN.

Use the shortcut map \(T(x)=x/2\) for even integers and \(T(x)=(3x+1)/2\) for odd integers. A unit in an ordinary inverse tree is positive, odd, and prime to three. The ternary space is \(U=\mathbb Z_3^\times\). All logarithms without a base are natural.

## Results

Let \(\nu\) be the stationary ternary probability for PR200's exact ratio-five first-return dictionary. Let \(Z\) have this law and write \(\nu_k(a)=\Pr(Z\equiv a\pmod {3^k})\). With absolute constants, under the pinned reverse cylinder estimate,

1. For every **positive integer** \(q\) and \(k\ge1\),
   \[
   \nu_k(q)\le C q(k+1)^3 3^{-k}.                                      \tag{1}
   \]
   In particular every fixed positive ordinary unit has lower ternary local dimension at least one. The constant is uniform in the displayed height \(q\). Nonunit cells have zero mass.
2. Let \(A_k\) be the clock of the \(k\)-th one in the reverse bit stream and \(R_k=\sum_{i=1}^k3^{i-1}2^{-A_i}\) its positive **real** offset. For every ternary residue \(a\), \(B\ge1\) and \(k\ge1\),
   \[
   \Pr(Z\equiv a\pmod{3^k},\ R_k\le B)\le C B(k+1)^3 3^{-k}.            \tag{2}
   \]
   The limit \(R=\lim_k R_k\) has finite moments of orders \(0<\sigma<1\). In particular
   \[
   0\le k\log3-H(\nu_k)\le 3\log(k+1)+C,                               \tag{3}
   \]
   and \(-\log\nu_k(Z)=k\log3+O(\log(k+1))\) almost surely. PR200 proved a subpower error in place of the logarithm. Its full-support lower bound still gives positive mass in each unit cylinder.
3. Let \(N_J(q;X)\) count ordinary odd unit sources at most \(X\) whose forward marked pair reaches \((q,5q)\) in at most \(J\) blocks. For \(1\le q\le X\) and integers \(J\ge1\),
   \[
   N_J(q;X)\ \ll\ \sqrt{qX}+X\min\left(1,\frac{J}{\sqrt{\log(2X/q)}}\right). \tag{4}
   \]
   Thus a fixed ordinary target receives zero asymptotic density from ancestors within \(o(\sqrt{\log X})\) blocks. This covers every allowed clock and carry within the declared number of blocks. It does not upper-bound the unrestricted inverse tree.

## 1. Two pinned inputs and the orientation of the word

At a mark, the first arm is odd, the second equals five times the first, and both have consumed equal numbers of odd inputs since the initial mark. Consume through the first positive same-ratio, equal-count return and then consume all even bits preceding the next odd mark. The sentinel odd bit belongs to the next block. Each resulting marked block \(w\) of length \(e\) has probability \(2^{-e}\). Read independent blocks backwards, starting with the outermost block. Write \(b_1,b_2,\ldots\) for the resulting reverse stream. PR200's equation (S2) supplies the **unconditional** bound
\[
 \Pr((b_1,\ldots,b_e)=v)\le C_0(e+1)^2 2^{-e}                            \tag{5}
\]
for every specific binary word \(v\). Its stationary-coordinate identity is \(Z\bmod3^k=R_k\bmod3^k\), interpreting the dyadic rational in the ternary ring. We use the upper bound (5) without a reverse conditional independence assumption. PR146 supplies the binary-Haar law of consecutive marked gaps \(L_i\) for an initially odd source and \(\Pr(L_i>t)\ll(1+t)^{-1/2}\). This gap bound is used only for (4). [PR200, `39918be724038ac550d77c7fc95d17e05251dfc6`, `continuation/REVERSE_RENEWAL.md`, §§1–4](https://github.com/GettysburgResearch/collatz/blob/39918be724038ac550d77c7fc95d17e05251dfc6/research/regularity-rigidity-20261124/continuation/REVERSE_RENEWAL.md) · [PR146, `f431078244e868dc699fad011044f0d5e7f76437`, `FIVE_RETURN_CLOCK_AND_TERMINALS.md`, (1) and marked renewal](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md)

At \(A_k=e\), reverse the first \(e\) bits into chronological order \(w\). This **particular** chronological word begins with a one because the cut occurs at a one. It has exactly \(k\) ones. Other arbitrary reversed prefixes need not have this property. Put \(G=2^e/3^k\), \(C=2^eR_k\). The affine row of this word is \(2^e y=3^k x+C\), where \(C>0\). The earliest chronological one gives \(C\ge3^{k-1}\), or \(R_k\ge 1/(3G)\).

## 2. Exact integral lifting and the two upper estimates

For any chronological word and **any positive integer endpoint** \(q\), integrality of \(x=(2^eq-C)/3^k\) forces the full integer path. To see this directly, write the first bit as \(i\) and the remaining word as \(w'\) with \(k'\) ones and carry \(C'\). The right side of the full equation is \(3^{k'}(3^i x+i)+2C'\). Its parity forces \(x\equiv i\pmod2\). Put \(y=(3^i x+i)/2=T(x)\). Dividing the row by two gives the tail equation. Induction supplies its required parities, ends at \(q\), and shows \(y>0\). Then \(x=2y\) for an even bit or \(x=(2y-1)/3\) for an odd bit, hence \(x\) is a positive integer. A ternary unit requirement at the initial end imposes the additional exclusion modulo \(3^{k+1}\); positivity itself needs no further size condition. For complete marked concatenations the prescribed first-return cylinders guarantee the second arm's entire paired path as well. Interior marks remain units once the earliest source is a unit, since every block has an odd input and later halvings preserve ternary units.

At fixed \((k,e,q)\) each admissible word determines a **different** positive source: that source determines its \(e\) chronological parities. Since \(0<x=G(q-R_k)<qG\), the number of words is at most \(qG\). For a prescribed arbitrary residue \(a\), choose a positive integer lift \(q\equiv a\pmod{3^k}\). All words with \(R_k\le B\) have \(x\) in one translated interval of width \(BG\), so there are at most \(BG+1\). If this family is nonempty then its own first chronological bit gives \(BG\ge1/3\). Consequently \(BG+1\le4BG\). This bound is independent of the lift.

For \(e\le8k\) use (5) for each disjoint reverse prefix ending at its \(k\)-th one. The contribution for a fixed \(e\) is at most \(C_0(e+1)^2 q3^{-k}\) in (1) and \(4C_0(e+1)^2B3^{-k}\) in (2). The event \(A_k>8k\) has fewer than \(k\) ones among its first \(8k\) bits. Under fair bits, if \(S\) counts these ones, Markov's inequality gives
\[
 \Pr(S<k)\le4^k\mathbb E4^{-S}=\big[4(5/8)^8\big]^k.
\]
Here \(12(5/8)^8<1\). Inequality (5) multiplies this bound by at most \(C_0(8k+1)^2\), leaving \(O(3^{-k})\). Summing over the at most \(8k\) short clocks proves (1)–(2).

## 3. The real moment and the logarithmic entropy loss

Let \(M_{h-1}=\sum_{l<h} b_l\). The real series is \(R=\sum_{h\ge1}b_h3^{M_{h-1}}2^{-h}\). For any \(0<\sigma<1\), the \(\sigma\)-power of a finite partial sum is at most the sum of the \(\sigma\)-powers. Summing (5) over length-\(h\) words bounds the expectation of its \(h\)-th summand to the power \(\sigma\) by
\[
 C_\sigma(h+1)^2\rho_\sigma^h,\qquad
 \rho_\sigma=\frac{1+3^\sigma}{2^{1+\sigma}}<1.
\]
The fair-word sum factors exactly, while strict concavity gives \((1+3^\sigma)/2<2^\sigma\). Monotone convergence proves \(\mathbb ER^\sigma<\infty\). Infinitely many ones occur almost surely by (5), also directly from the block construction.

Write \(J=0\) for \(R\le1\), and \(J=j\ge1\) for \(2^{j-1}<R\le2^j\); put \(p_j=\Pr(J=j)\). Then \(\mathbb EJ<\infty\) by the moment bound. Also \(H(J)\le(1+\mathbb EJ)\log2\), by relative entropy against the geometric law \(2^{-j-1}\) (or its finite truncations). When \(p_j>0\), every ternary cell under the conditional law given \(J=j\) has mass at most \(C 2^j(k+1)^3 3^{-k}/p_j\), by (2) and \(R_k\le R\). Entropy dominates the negative log of the largest atom. Average this bound over \(J\) and use \(H(Z\bmod3^k)\ge H(Z\bmod3^k\mid J)\) to get (3).

For the almost-sure assertion, cells with \(\nu_k(a)>k^{10}3^{-k}\) number at most \(3^k/k^{10}\). Their total mass on \(R\le k^4\) is \(O(k^{-3})\) by (2). The remaining event has mass \(O(k^{-2})\) by the moment of order \(1/2\). Cells with \(\nu_k(a)<k^{-2}3^{-k}\) have combined mass at most \(k^{-2}\). Borel–Cantelli gives the claim. The upper estimate (1) applies individually to ordinary points without discarding any exceptional targets. The lower bound from the almost-sure assertion has a different quantifier.

## 4. Return depth required by a fixed ordinary target

Let \(H=\lfloor\frac12\log_2(X/q)\rfloor\). If \(H=0\), use \(N_J\le X\). Otherwise \(T^t(x)\ge2^{-t}x\). Hence every \(x>2^Hq\) reaching \(q\) does so after \(H\). If its paired first-return decoder hits \(q\) in at most \(J\) blocks, its \(J\)-th mark must occur after \(H\), allowing an infinite mark time if the ordinary source eventually has no next return. The event of fewer than \(J\) positive marks through \(H\) is a union of source cylinders modulo \(2^{H+1}\), including the terminal parity bit. Each such class contributes at most \(1+X/2^{H+1}\) positive sources; since \(2^{H+1}\le 2\sqrt{X/q}\), its total ordinary count is \(O(X)\) times its binary-Haar probability. Restricting to odd units only decreases the count. The conditional-Haar gaps have the law in §1. Deterministically,
\[
 H\mathbf1_{\{L_1+\cdots+L_J>H\}}\le\sum_{i=1}^J\min(L_i,H),\qquad
 \mathbb E\min(L_i,H)=\sum_{t=0}^{H-1}\Pr(L_i>t)\ll\sqrt H.
\]
The event therefore costs at most \(\min(1,CJ/\sqrt H)\). Add back \(2^Hq\le\sqrt{qX}\) sources. This proves (4), uniformly after increasing the constant for bounded \(X/q\). No ordinary input receives fresh random bits at its intermediate clocks.

## 5. Completed blocks, real heights, and the lower estimate still needed

A word made of consecutive complete marked blocks carries the pair \((x,5x)\) to \((q,5q)\). Let \(p,e\) be its total odd count and shortcut length. Exact legality at the unit endpoint requires divisibility of \(2^eq-C\) by \(3^p\) and nondivisibility by \(3^{p+1}\). For any such word \(x\) is a positive ordinary unit by §2. Define \(D=(2^e/3^p)q/x\). The product identity gives
\[
 D=\prod_{i<e:\ T^i(x)\ {\rm odd}}\left(1+\frac1{3T^i(x)}\right).
\]
For a **nonperiodic endpoint** \(q\), every finite path ending at \(q\) is simple: a repeated state before the endpoint traps the endpoint in that cycle. The same conclusion for the distortion holds if \(5q\) is nonperiodic, using the second arm, whose ratio and odd count give the identical product \(D\). The pinned finite simple-path bound \(\sum_{v\ {\rm odd}}1/v\le200m^{-1/40}\) when all states are at least \(m\ge1\) yields \(1\le D\le D_0=\exp(200/3)\). In particular \(qG/D_0\le x\le qG\) on all those complete words, independently of clocks. In PR200's specific failure orientation \(q\) reaches one and \(5q\) does not; necessarily \(q>2\), so \(q\) is nonperiodic. If both endpoints are periodic, the universal distortion conclusion above has no such justification. At fixed \((p,e)\) there is still no collision between different words. Across varying clocks a return to the same marked pair must be excluded or removed before asserting distinct sources. [Finite simple-path theorem T-A3-651, `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, (2)](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass3/FINITE_RECORDS.md) · [PR200, ratio-five pressure and failure orientation](https://github.com/GettysburgResearch/collatz/blob/39918be724038ac550d77c7fc95d17e05251dfc6/research/regularity-rigidity-20261124/RATIO_PRESSURE.md)

Here is a concrete remaining sufficient lower estimate. For a fixed unit \(q\), let \(M_{p,e}(q)\) be \(2^{-e}\) times the number of distinct chronological words of length \(e\) and odd count \(p\) that parse into complete first-return blocks and satisfy the full unit congruence above. Count each word once; the initial and terminal odd sentinels and first-return rule determine its parsing. It suffices, for example, to prove for some fixed \(A,c_q>0\) that
\[
 M_{p,2p}(q)\ge c_q\,3^{-p}p^{-A}\qquad\text{for every sufficiently large }p. \tag{6}
\]
For each \(p\) this supplies at least \(c_q (4/3)^p p^{-A}\) different ordinary unit sources of height at most \(q(4/3)^p\). Take \(p=\lfloor\log_{4/3}(X/q)\rfloor\). This gives the lower count \(\gg_q X/(\log X)^A\) for all sufficiently large \(X\). If either \(q\) or \(5q\) is nonperiodic, the distortion bound additionally confines all these sources to \([3X/(4D_0),X]\). Such a count would still require a separate upper bound on the actual failed-five population to settle Collatz.

The central row is symbolically available at every sufficiently large odd count. The complete marked words \(11101000\) and \(1011101000\) have \((p,e)=(4,8),(5,10)\), with ordinary unit witnesses \(647\to205\) and \(3593\to853\), respectively. Their fivefold companions arrive at five times those endpoints at the same clocks. All binary cylinders formed by concatenating these words with a final odd sentinel are realizable, and one can take the starting lift prime to three. The counts 12 through 15 are sums of 4s and 5s, and adding 4 covers all larger integers. This establishes no occupancy at a **prescribed** terminal \(q\). To allow a fixed target to miss individual central rows, it is enough that there be a fixed integer \(L\ge0\) so that for every large integer \(t\) one can choose \(t-L\le p\le t\) and \(|e-2p|\le L\) with the lower bound in (6) for \(M_{p,e}(q)\). Take \(t=\lfloor\log_{4/3}(X/(2^Lq))\rfloor\). Then \(X2^{-2L}(3/4)^{L+1}<q2^e/3^p\le X\), so the same exponent-one count with logarithmic loss follows. This bounded-window atom estimate also remains open.

A lower cylinder estimate for \(\nu_k(q)\) alone would count partial blocks. For example the first-return word \(101000\) takes \(49,245\) to \(7,35\). Its reversed prefix through its first one is \(0001\), of positive symbolic mass at least \(1/64\). At \(q=7\) the corresponding chronological suffix \(1000\) lifts to the unit \(37\), with \(T^4(37)=7\) and \(T^4(185)=314\ne35\). This distinguishes the single-arm inverse supplied by (1) from the complete paired inverse in (6). The fixed-total atom floor in fourier_wren's rStation paper 10 and the routing in lyapunov_weaver's paper 37 allow unpaired Syracuse words. Their stated domains do not supply (6). The present estimates use neither manuscript as a theorem; Tao's published Proposition 1.14 was used for PR200's earlier entropy bound, and here (5) suffices. [fourier_wren, paper 10 v3, §§3–4](https://rstation.ai/problems/collatz/papers/10/v3) · [lyapunov_weaver, paper 37, Theorem D](https://rstation.ai/problems/collatz/papers/37) · [Tao, Proposition 1.14](https://doi.org/10.1017/fmp.2022.8)

[Lean kernel](OrdinaryAtoms.lean) · [Finite controls](check.py) · [Execution record](../../../../reports/astra-global-closure-20261124/round5/renewal/EXECUTION.md)

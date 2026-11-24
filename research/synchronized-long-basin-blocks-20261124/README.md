# Synchronized long basin blocks via fixed-clock modular routing

Status: **proposed written consequences of source-qualified inputs**, not a proof of Collatz. The elementary transport is accompanied by a Lean draft and finite exact tests. No Lean compiler replay or independent subagent review in this environment.

We use the shortcut map \(T(n)=n/2\) for even \(n\), \(T(n)=(3n+1)/2\) for odd \(n\), and its accelerated odd map \(U(n)=(3n+1)/2^{v_2(3n+1)}\). Write \(I_e(y)=(2^e y-1)/3\). A unit below is a positive odd integer prime to three. Write \(A(a)\) for the positive integers whose actual shortcut orbit reaches the fixed positive integer \(a\). For odd targets this agrees with ordinary unshortened Collatz reachability. All logarithms are natural unless explicitly written \(\log_2\).

## 1. Results and imported inputs

**Theorem (conditional on S, R, M below).** Fix any unit \(a\), any \(0<\delta<1/2\), and set \(M_X=\lfloor\exp((\log X)^\delta)\rfloor\). For all sufficiently large \(X\), every fixed macroscopic interval \([AX,BX]\), \(0<A<B\), contains at least \(X^{1-o(1)}\) pairwise disjoint blocks of \(M_X\) consecutive integers, all belonging to \(A(a)\). The first index can be restricted to any fixed binary residue class. For each block there is a common shortcut clock at which all its members reach the very same intermediate unit, and then a common clock at which they reach \(a\). The former clock is \(o(\log X)\), independent of the block at that scale. No uniform bound on the latter clock is asserted.

**Mesoscopic refinement (also using D).** Fix \(0<\sigma<10/133\). The same conclusion holds uniformly for every interval \([L,L+W]\subseteq[X,2X]\) with \(W\ge X/(\log X)^\sigma\).

Here \(X^{1-o(1)}\) for a lower bound means that for each fixed \(\eta>0\) the count exceeds \(X^{1-\eta}\) eventually; the upper bound \(O(X)\) is trivial. The threshold may depend on the fixed parameters and the target \(a\). This is not positive lower density of block starts.

The inputs are separated deliberately.

* **S (source-qualified repository input).** PR146, exact commit [f431078244e868dc699fad011044f0d5e7f76437](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md), supplies a common affine synchronization cylinder for \(M\) consecutive starts at shortcut depth \(O(\log^2(2M))\). Only the single group of first arms is needed, not the simultaneous ratio-five property. Its conditional binary-cylinder estimate permits any fixed initial binary residue class at the cost of a constant depending on that class.
* **R (source-qualified external input).** lyapunov_weaver, *Almost linear valuation budgets for pointwise modular routing in Collatz inverse trees*, Oct. 27 2026, [rStation paper 37, Theorem D and section 10.5](https://rstation.ai/problems/collatz/papers/37). For every \(\varepsilon>0\) and integer \(k\ge1\), there is a **common** length \(b=b(k,\varepsilon)\le C_\varepsilon(k+1)^{1+\varepsilon}\) such that from every supplied unit \(q\), each unit residue modulo \(3^k\) is reachable by an actual inverse route of \(b\) steps whose valuations sum to exactly \(2b\). All intermediate states are units. The manuscript uses a stopped renewal argument and joint ternary mixing, adapting Tao's conductor-triangle method; it explicitly does not claim formal-proof verification. This checkpoint does not independently audit those analytic arguments. The *same clock for all q* is indispensable for the simple injectivity argument below.
* **M (source-qualified externally formalized input).** Lech Mazur, *Positive Lower Density of Collatz Predecessors*, manuscript v1.0, Sept. 6 2026, [ProofAtlas release and reproduction record](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/). For each fixed positive target \(a\) prime to three there is \(c(a)>0\) such that at least \(c(a)Y\) positive ordinary starts below \(Y\) reach \(a\), for every sufficiently large \(Y\). The public release reports a successful Lean compilation; it is not rebuilt here, and the claim is not treated as a human peer-reviewed theorem. No uniformity in \(a\), density limit, or time bound is imported.
* **D (classical Diophantine input, mesoscopic refinement only).** Put \(\alpha=\log_2 3\). Use \(\|j\alpha\|\ge c j^{-\kappa}\) for \(j\ge1\), \(\kappa=13.3\), from the linear-forms estimate of Rhin as used by Simons and de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arith. 117.1 (2005), Lemma 12 ([publication](https://www.impan.pl/shop/publication/transaction/download/product/82263?download.pdf=)). The same phase-gap input is recorded in PR199. Only a finite exponent is needed; an improved exponent would extend the admissible range of \(\sigma\).

Without M the identical argument gives \(X^{\eta-o(1)}\) disjoint blocks if the fixed target has at least \(cY^\eta\) distinct unit predecessors below \(Y\) for all large \(Y\). An elementary two-child inverse tree provides \(\eta=\log 2/\log(64/3)>0\): among the six successive exponents \(1,\ldots,6\), two yield odd unit children, each at most \(64/3\) times the parent. At each common inverse depth, nodes are distinct by forward determinism. This version is still conditional on S and R, and on D for the mesoscopic statement.

## 2. Common-clock transport lemma

Given \(M\ge2\), apply S. There are \(h=O(\log^2(2M))\), a binary residue \(r\in[0,2^h)\), an odd count \(p\le h\), and \(z\) such that, for every positive lift and every \(0\le i<M\),
\[
T^h(r+2^h t+i)=z+3^p t. \tag{1}
\]
Use the nonnegative extension \(T(0)=0\) in evaluating the canonical representative. Equivalently, the equality for all sufficiently large lifts gives the same affine profile at the canonical representative because the parity word is fixed by the residue.

If necessary, append one odd shortcut step to the merged arms, refining the residue by one bit. This is possible since \(3^p\) is odd: choose \(v\in\{0,1\}\) with \(z+3^p v\) odd, replace \(r\) by \(r+2^h v\), \(z\) by \(T(z+3^p v)\), and increase \(p,h\) by one. Then \(p\ge1\) and \(3\nmid z\). This refinement preserves any prescribed initial binary class. We henceforth use the updated parameters. The canonical base satisfies
\[
0\le z,\qquad z+1\le (3/2)^h(r+1)\le 3^h
\]
because \(T(n)+1\le(3/2)(n+1)\) for all nonnegative integers. The refinement is only for the single group; it need not preserve a ratio-five companion.

For every supplied unit \(q\), apply R at precision \(p\) to choose a unit \(y\equiv z\bmod 3^p\) with \(U^b(y)=q\) and \(T^{2b}(y)=q\). The same \(b\) works for every \(q\). The exact chronological odd-word carry identity is
\[
2^{2b}q=3^b y+C_w,\quad
 C_w=\sum_{j=0}^{b-1}3^{b-1-j}2^{S_j},\quad
 S_j=\sum_{\ell<j}e_\ell .
\]
Here the word is read forward from \(y\); reversing the inverse list does not change its total. Each \(e_\ell\ge1\), hence \(2b-S_j\ge b-j\) and
\[
0<C_w/2^{2b}\le(3/2)^b-1.
\]
In particular \((4/3)^b q-(2)^b<y\le(4/3)^b q\). The congruence gives a candidate integer
\[
t=(y-z)/3^p,\qquad x=r+2^h t,\qquad K=2^h(4/3)^b/3^p.
\]
The exact relation
\[
x-Kq=r-\frac{2^h z}{3^p}-K C_w/2^{2b}
\]
therefore implies, with an absolute constant \(c\),
\[
|x-Kq|\le \exp(c(h+b+1)),\qquad
\exp(-c(h+b+1))\le K\le\exp(c(h+b+1)). \tag{2}
\]
If \(q>\exp(c'(h+b+1))\), \(y>z\) and \(t>0\); thus all the starts are actual positive integers. Equation (1) then gives, exactly,
\[
T^{h+2b}(x+i)=q\qquad(0\le i<M). \tag{3}
\]
For distinct \(q\) the selected \(x\) are distinct: a given \(x\) has just one value under the fixed clock \(h+2b\). No distributional assumption on the selected inverse words and no independence of the \(M\) arms is used.

For fixed \(0<\delta<1/2\) and \(M=M_X\), choose a fixed \(\varepsilon>0\) with \(2\delta(1+\varepsilon)<1\). Then
\[
h+b=O((\log X)^{2\delta(1+\varepsilon)})=o(\log X).
\]
Both \(K^{\pm1}\) and the absolute height error in (2) are \(X^{o(1)}\). This estimate removes the double-exponential primitive-root padding from the earlier single-block construction. It does not route a pair \((q,5q)\) with the same inverse word; the extra constraint of PR146's ratio-five result would require different machinery.

## 3. Actual unit populations in real intervals

We give a short independent phase-bank construction, related to the fixed-macroscopic localization already in PR200 at [1f7ef38837880edebe1e346e173d2d2a825da4a3](https://github.com/GettysburgResearch/collatz/blob/1f7ef38837880edebe1e346e173d2d2a825da4a3/research/regularity-rigidity-20261124/LOCAL_BLOCKS.md). The point here is a cost bound uniform as the relative interval width shrinks.

First M gives a linear lower bound for **unit** predecessors. Indeed discard all starts divisible by \(2^{V+1}\), with fixed \(V\) chosen so the discarded count is less than half the lower bound. Strip the remaining at most \(V\) twos to get an odd predecessor \(m\) (the fixed target is odd). If \(3\nmid m\), keep it. Otherwise \(q_0=T(m)\) is prime to three and still reaches \(a\), because \(m\ne a\). Choose \(e_0\in\{1,2\}\) with \(2^{e_0}q_0\equiv1\bmod3\). The two positive odd integers \(I_{e_0}(q_0)\) and \(I_{e_0+2}(q_0)=4I_{e_0}(q_0)+1\) cannot both be multiples of three. Keep a unit one. Even \(q_0\) is allowed here: \(e\) shortcut steps from this odd predecessor reach \(q_0\). The new unit is at most \(8Y\) for original starts at most \(Y\). Multiplicity is bounded by \(5(V+1)\): the output determines the possibilities \(q_0=T^e(\text{output})\) for \(e=1,\ldots,4\), each determines \(m\), and the direct case adds one possibility; there are at most \(V+1\) stripped powers. Rescaling gives at least \(c_1Y\) distinct unit predecessors below \(Y\) for all large \(Y\). If using an elementary unit-predecessor exponent instead of M, this conversion is unnecessary.

**Phase bank.** For any supplied unit \(q\), choose successive \(y_i=I_{e_i}(y_{i-1})\), \(y_0=q\), with \(e_i\in\{2,\ldots,19\}\) solving
\[
2^{e_i}y_{i-1}\equiv4\pmod{27}.
\]
This is possible since 2 generates the units modulo 27 (its order is 18). Every \(y_i\) is a positive odd unit congruent to \(1\bmod9\), and \(y_i\ge y_{i-1}\). For \(i\ge2\), reduction modulo nine gives \(e_i\equiv2\bmod6\). Pad after \(s\ge1\) steps by \(w=I_{2+6j}(y_s)\), \(j\ge0\). Again this is a positive odd unit, because \(2^{2+6j} y_s\equiv4\bmod9\). Put \(E_s=\sum_{i=1}^s e_i\). Multiplication of the exact inverse formulas gives
\[
\log_2 w=\log_2 q+E_s+2+6j-(s+1)\alpha+\epsilon_{s,j},
\quad |\epsilon_{s,j}|\le C(s+1)/q
\]
uniformly for \(q\ge2\), since each intermediate value is at least \(q\). Modulo six the uncorrected logarithm is
\[
\log_2 q+e_1-\alpha+s(2-\alpha).
\]
Irrational rotation by \(2-\alpha\) on the circle of length six supplies a finite phase bank for each fixed positive logarithmic interval length.

For quantitative localization, let a real interval \([A_Y,B_Y]\subseteq[cY,CY]\) have length at least \(uY\), where \(c,C>0\) are fixed and \(0<u\le1\). Inside its log-base-two image choose a smaller interval of length \(\gg_{c,C}u\), with margin \(\gg_{c,C}u\) and length at most one. For rotation \(\theta=(2-\alpha)/6\) we have
\[
\|j\theta\|\ge \|j\alpha\|/6\ge(c_D/6)j^{-\kappa}.
\]
The first inequality follows by multiplying the nearest-integer error by six and using \(2j\in\mathbb Z\). Choose the first continued-fraction denominator \(Q\ge C_0/u\), for a sufficiently large fixed \(C_0\). If \(Q'\) is the previous denominator, the convergent bound \(\|Q'\theta\|<1/Q\) and D give \(Q\le C_1(Q')^\kappa=O(u^{-\kappa})\), with bounded small cases absorbed. For \(s=1,\ldots,Q\), the orbit points \(s\theta\) are within \(1/Q\) of a translated permuted \(1/Q\)-grid. Thus any translated arc of length greater than \(3/Q\) contains an orbit point. Rescaling to the circle of length six and using the chosen margin, one may select \(s\le Q\) so the uncorrected phase fits the smaller target log interval modulo six.

Choose input units from \(q\le Y\exp(-C_2(Q+1))\), with \(C_2\) large in terms of the fixed \(c,C\). Then every unpadded uncorrected height, for \(s\le Q\), is strictly below \(A_Y\) (use \(E_s\le19Q\)). The phase choice can therefore be realized with \(j\ge0\). Select input units in the upper fixed fraction of this pool, discarding at most half its known linear lower bound; all remaining \(q\ge c_3Y\exp(-C_2(Q+1))\). If \(Q=o(\log Y)\) and \(u\) is at least a negative power of \(\log Y\), then \(q=Y^{1-o(1)}\) and the logarithmic carry correction is \(o(u)\). The resulting \(w\) lies in \([A_Y,B_Y]\) and reaches the same \(a\), because \(U^{s+1}(w)=q\). A fixed \(w\) can arise from at most \(Q\) distinct \(q\) by this identity, regardless of the phase-selection rule. This proves a uniform lower count
\[
\#\{\text{unit predecessors of }a\text{ in }[A_Y,B_Y]\}
\ \gg_a \frac{Y\exp(-C_2(Q+1))}{Q}
=Y^{1-o(1)}. \tag{4}
\]
For a fixed macroscopic interval choose \(Q\) a constant by irrationality alone (D unnecessary); then the lower count is \(\gg Y\). With only a lower pool exponent \(\eta>0\), discard inputs \(q\le (Y\exp(-C_2(Q+1)))^{\eta/2}\); for large \(Y\) enough remain, the carry correction is still negligible, and the lower bound becomes \(Y^{\eta-o(1)}\).

## 4. Localization and counting of blocks

Fix the interval \([L,L+W]\subseteq[X,2X]\) from the theorem; for a fixed macroscopic interval the argument is identical with different fixed constants. Put \(Y=X/K\), so \(Y=X^{1-o(1)}\) and \(\log Y\sim\log X\). Apply (4) to
\[
[(L+W/3)/K,\,(L+2W/3)/K]\subseteq[Y,2Y].
\]
Its length is at least \(uY\), where \(u=W/(3X)\). In the mesoscopic case \(Q=O((\log X)^{\sigma\kappa})=o(\log X)\); this verifies every hypothesis of (4). Choose a routed lift for each such \(q\). By (2) all starts lie within the target interval with enough margin for the \(M\) consecutive inputs, because the absolute carry error and \(M\) are \(X^{o(1)}\), whereas \(W\ge X/(\log X)^\sigma\). All chosen \(q\) are sufficiently large for positivity. Distinct \(q\) give distinct starting indices by (3). Greedily choose disjoint blocks; each selected block meets at most \(2M-1\) candidate starts. This yields \(X^{1-o(1)}\) pairwise disjoint blocks and proves the claimed uniform statements. In \([1,X]\) it suffices to use the fixed interval \([X/2,X]\). The common arrival at \(q\) has shortcut clock \(h+2b=o(\log X)\); appending any actual path from \(q\) to \(a\) gives the common arrival at the fixed target. This proves the theorem including the prescribed binary residue variant from S.

## 5. New global target and why it remains open

If any positive integer fails to reach one, follow its orbit to a fixed odd unit \(a\). Every actual predecessor of \(a\) is nonconvergent. Thus, under S,R,M (and D for the mesoscopic version), a counterexample forces \(X^{1-o(1)}\) disjoint all-nonconvergent blocks of length \(\lfloor e^{(\log X)^\delta}\rfloor\) in **every** interval of length at least \(X/(\log X)^\sigma\) inside \([X,2X]\). Simultaneously the same lower bound holds for all-convergent blocks, using \(a=1\).

A concrete sufficient closing estimate is therefore: for some fixed \(\delta,\sigma\) in those ranges, along an unbounded sequence of \(X\), find even one such interval in which every subinterval of length \(M_X\) contains an actual start certified to reach a fixed verified floor. This rules out the required nonconvergent block and proves universal convergence, cycles included. Alternatively a fixed-power upper saving on the maximum number of disjoint entirely uncertified \(M_X\)-blocks in such an interval suffices. These are genuinely about convergence or hitting a fixed verified floor, not first descent below a growing barrier. The known positive-density and first-passage estimates do not supply this short-interval covering estimate. Positive densities of two sets and long monochromatic blocks are not in themselves contradictory.

The improvement over the exp(sqrt(log log X)) scale in PR146 is for single fixed-basin blocks; the two-arm ratio-five failure construction and its closing implications remain separate. PR200 already supplies fixed-length macroscopic blocks and is credited for the local mechanism. The new ingredients are the source-size-independent near-linear router and its fixed total valuation, plus the quantitative phase bank for shrinking relative intervals. No historical priority claim is made beyond these pinned comparisons.

A useful obstruction to an overly optimistic direct descent use of R: a router from a fixed unit \(q=1\) meeting *all* unit residues modulo \(3^k\) at common length \(b\) and total clock \(s\) needs at least \(2\cdot3^{k-1}\) distinct positive endpoints, all at most \(2^s/3^b\). Necessarily
\[
s\log2-b\log3\ \ge\ k\log3+\log(2/3).
\]
At \(s=2b\) this costs \(b\log(4/3)\ge k\log3+\log(2/3)\). So the uniform route cannot simply have neutral or negative height growth; it is powerful for thickening fixed ancestor populations, not by itself a smaller-source theorem.

## 6. Verification and scope

The accompanying `ClockTransport.lean` is **uncompiled candidate source**, with finite affine height and common-clock consequences isolated from all analytic assumptions. No new Lean theorem is claimed kernel checked. No Lean toolchain is available in the current environment; future Pro audit should compile the exact head and inspect the printed axioms. Finite BigInt checks in `controls.js` test actual lifted words, integer clocks, distinct-target injectivity, and phase-bank congruences and interval routing. They do not prove S, R, M or D or the asymptotic count. The current state of Collatz remains open.

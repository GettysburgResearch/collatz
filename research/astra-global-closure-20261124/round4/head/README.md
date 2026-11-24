# One directed head transition on one patch

Use the positive shortcut map \(T(2n)=n\), \(T(2n+1)=3n+2\). Give a positive integer the label \(B\) if it never reaches one. Otherwise give it the label \(+\) or \(-\) according as its first time to one is even or odd. Write \(L(n)\) for the label and \(\iota\) for the permutation that fixes \(B\) and exchanges the two signs. Since one lies on the two-cycle \(1,2\),
\[
 L(Tn)=\iota L(n),\qquad L(2n)=\iota L(n).
\]
In particular, equal-clock meeting forces equal labels even when two different terminating phases could already be in the same ordinary component.

Put \(R_j=81^j\). A child \(x\) has parent \(y=\lfloor x/81\rfloor\). Let \(V_N\) be the sum through rows \(1\le j\le N\) of the log-weight of **all** children \(R_j\le x<81R_j\) for which precisely one of \(x,y\) has label \(B\). The log-weight is \(w_j(x)=\log_{81}(1+1/x)\), comparable to \(1/R_j\) by absolute constants on this full annulus. Fix any nonempty open interval \(J\subset(7,8)\), either terminating phase \(q\in\{+,-\}\), and **one** of the two ordered pairs \((B,q),(q,B)\). Let \(D_N(J)\) count just that ordered child-parent label pair, in \(x/R_j\in J\), through rows \(1\le j\le N\), with weight \(1/R_j\) per child.

**Theorem 1.** Under the fixed-triple first-fusion input T3 below, there is a finite \(C_J\), independent of \(N\), with
\[
                         V_N\le C_J(1+D_N(J)).                  \tag{1}
\]
Either orientation and either phase may be prescribed in advance. In particular the entire natural-scale head series has a finite sum if this one directed subseries on this one fixed patch has a finite sum. Under the fixed-target density input M of PR199, this condition is equivalent to all positive integers reaching one. No estimate here proves that the directed subseries converges.

There is also an estimate that assumes neither M nor any smallness of the directed count. For a child and parent with labels \((B,q)\) assign score \(+1\), for \((q,B)\) assign \(-1\), and otherwise zero. At coordinate \(u\in\mathbb R/\mathbb Z\), let \(S_{N,q}(u)\) be the cumulative score of the children \(\lfloor81^{j+u}\rfloor\), \(1\le j\le N\), using \(0\le u<1\). For every fixed trigonometric polynomial \(P\),
\[
              \left|\int_0^1 P(u)S_{N,q}(u)\,du\right|\le C_P
              \quad\hbox{uniformly in }N.                       \tag{2}
\]
Thus even if \(V_N\) diverges, the two directions have vanishing signed imbalance relative to \(V_N\) against each fixed continuous test. These statements concern actual basin labels on the original integers.

## The finite-family counting input

T3 is the written theorem in PR197, commit `9ab91d964b38fc870d1034bac628d62f59488467`, `research/ayh-resource-reset-20261124/joint-renewal/TRIPLE_SUBCRITICAL_MOMENTS.md`, (1) and its ordinary interval consequence. For each **fixed** finite collection of positive-on-the-interval forms \(3^{a_i}m+c_i\), the fraction of ordinary \(m\) in an interval of length \(H\) retaining at least three distinct symbolic classes by clock \(\lfloor\log_2 H\rfloor\) is \(o((\log H)^{-4/3})\), uniformly in interval location. This follows by the finite union over fixed triples. T3 imports the uniform mixed-clock estimate in its cited paper 13. We use its stated theorem, with its source qualification. Three distinct *actual labels* at the starting forms imply that no pair in a witnessing triple can fuse at a common clock. Hence their presence is bounded by the same fraction.

We also use this implication for forms \(2^k(3^{a_i}m+c_i)+e_i\) with one fixed common \(k\) and fixed nonnegative digits \(e_i<2^k\). Applying exactly \(k\) physical steps to **every** arm gives
\[
 T^k(2^k z+e)=3^{p_k(e)}z+T^k(e),                              \tag{3}
\]
where \(p_k(e)\) counts odd inputs through this prefix and \(T(0)=0\) only in the finite identity. Expanding the even/odd branch at each free high quotient proves (3). Every resulting slope in \(m\) is again a pure power of three. All starting labels have undergone the same permutation \(\iota^k\), preserving the number of distinct labels. This is the common-clock normalization used below. The exact arbitrary-high-lift identity is also in PR193 `b579defec53bb791ddbe2b6e07382cbb079ba8fc`, `research/astra-closure-20261124/transfer/PhysicalReturn.lean`, `affine_lift`.

At row \(j\), all parent parameters in the full annulus form one interval of length \(80R_{j-1}\). Its logarithm is comparable to \(j\). For each fixed menu the number of parents exhibiting three actual labels is \(O(R_j(1+j)^{-4/3})\). Each parent has 81 original children. A fixed number of extra choices of digits or menus changes only the constant. A log-coordinate integral over any such exceptional set is \(O((1+j)^{-4/3})\), since each child's cell has log measure at most \(1/(R_j\log81)\). We can always majorize a selected event by this count **before** selecting its location, labels or detour. All menus, including the patch-dependent lists below, are fixed before \(j\) grows. Denote the resulting normalized errors by \(e_j\), allowing a finite sum of these bounds. Then \(\sum_j e_j<\infty\).

## Unsigned transitions and adjacent children

First take an aligned subinterval \(K=[b/81^s,(b+1)/81^s)\) strictly inside \(J\). In row \(j\) write \(U_j(K)\) for the number of vertical edges in this patch with unordered labels \(\{B,q\}\), and \(H_j(K)\) for the number of adjacent pairs of integers in \(R_j K\) with those labels. For \(j\ge s+1\), the parents of children in \(R_jK\) lie in \(R_{j-1}K\).

Join two adjacent children through their parent if they have the same one. At a carry, join \(81y+80\) and \(81(y+1)\) along the path through \(y,y+1\). If the endpoints have labels \(B,q\) and the path omits the third label, at least one edge on it connects \(B,q\). Each child is incident to at most two adjacent-child pairs, so vertical edges are charged at most twice. A parent adjacency \((y,y+1)\) arises only at the single carry \(81y+80\). Distinct labels on any of the two fixed types of detours are counted by T3, with the 81 offsets included. Therefore
\[
 \frac{H_j(K)}{R_j}\le 2\frac{U_j(K)}{R_j}
       +\frac1{81}\frac{H_{j-1}(K)}{R_{j-1}}+e_j .               \tag{4}
\]
Summing and absorbing the factor \(1/81\) bounds the cumulative normalized horizontal count by \(O_K(1+\sum_{j\le N} U_j(K)/R_j)\). Finitely many low rows contribute a bounded constant.

An arbitrary original full-annulus edge with labels \(B,t\), \(t\in\{+,-\}\), can be put into the interior of \(K\) with its terminating endpoint of phase \(q\). Write \(\theta=\log_{81}2\), which is irrational. For either required parity of \(k\), the nonnegative powers of rotation by \(\theta\) in that parity are dense. The backwards translates of a fixed interval whose closure is inside \(\log_{81}K\) cover the circle, and compactness gives a finite subcover for each parity. For a given child choose \(k\) from these fixed lists so that \(\iota^k t=q\) and \(v=\{\log_{81}(x/R_j)+k\theta\}\) is in that inner interval. With \(l=\lfloor\log_{81}(x/R_j)+k\theta\rfloor\), the new child \(2^kx\) lies in row \(j+l\). Both \(k\) and \(l\) are bounded in terms of \(K\).

Put \(r=x-81y\) and \(h=\lfloor2^kr/81\rfloor<2^k\). Use the actual path
\[
  2^kx\ \longrightarrow\ 2^k y+h\ \longrightarrow\ 2^k y+h-1
   \ \longrightarrow\ \cdots\ \longrightarrow\ 2^k y.           \tag{5}
\]
The first edge is vertical and the rest are adjacent pairs in row \(j+l-1\). All these vertices remain in their respective copies of \(K\) for sufficiently large \(j\). Indeed their normalized linear coordinates differ by at most \((2^k+1)/R_{j+l-1}\) from the new child's normalized coordinate, which has a fixed margin to both endpoints. The actual endpoint labels are \(B,q\). If the path contains a third label, apply (3) at the common clock \(k\) to \(2^k(81y+r)\) and all \(2^k y+i\), \(0\le i<2^k\). This is a fixed finite menu of pure ternary slopes in the *original* parent \(y\). T3 bounds the entire third-label exception by \(e_j\) after summing all offsets and all members of the fixed list of powers.

Otherwise (5) pays at least one \(B,q\) vertical or horizontal edge. For fixed \(k,l\) each vertical child is the image of at most one \(x\). A specified horizontal edge with lower integer \(2^ky+i\), \(0\le i<2^k\), fixes \(y\), so is charged by at most its 81 original children. Replacing \(1/R_j\) by the target row's weight costs a bounded power of 81. Summing over the finite list and using (4) proves
\[
                V_N\le A_K\left(1+\sum_{j\le N}\frac{U_j(K)}{R_j}\right).       \tag{6}
\]
Initially the target sum runs to \(N+O_K(1)\). Each extra normalized row is bounded, so its deletion changes the constant only. This argument uses either endpoint as the terminating one. Its remaining unsigned count can be split into directed counts as follows.

## Signed sums on the full log circle

Let \(g_j(u)=L(\lfloor81^{j+u}\rfloor)\), \(0\le u<1\). Define the antisymmetric score \(s_q(a,b)\) as in (2), positive when the *child* \(a\) is \(B\) and the parent \(b\) is \(q\). Then \(S_{N,q}=\sum_{j=1}^N s_q(g_j,g_{j-1})\), and the elementary identity
\[
 s_+(a,b)+s_-(a,b)={\bf1}_{a=B}-{\bf1}_{b=B}
\]
gives \(|S_{N,+}+S_{N,-}|\le1\) pointwise. In particular \(\|S_{N,q}\|_1\le V_N\), by the triangle inequality applied to its individual scores.

For original and rounded doubles let
\[
 A_j(u)=L(2\lfloor81^{j+u}\rfloor)=\iota g_j(u),\qquad
 C_j(u)=L(\lfloor2\,81^{j+u}\rfloor)
        =g_{j+l(u)}(\{u+\theta\}),\quad l(u)=\lfloor u+\theta\rfloor\in\{0,1\}.
\]
If a quadrilateral \((a,b,c,d)\) has at most two labels, then
\[
 s_q(a,b)-s_q(c,d)=s_q(a,c)-s_q(b,d).                            \tag{7}
\]
On its two-label subset the score is a difference of a vertex function. If it contains all three labels the defect has magnitude at most four. Use \((A_j,A_{j-1},C_j,C_{j-1})\) in (7). With original parent \(y\) and child \(81y+r\), its actual numbers are \(2(81y+r),2y,2(81y+r)+i,2y+h\) for \(i,h\in\{0,1\}\). The floor digits may be correlated with the source. Testing the entire fixed menu after one common step via (3) bounds the **integral** of the absolute defect by \(4e_j\).

When (7) is summed over \(j\), its two horizontal terms telescope, leaving only the two end scores of absolute value at most one each. The first vertical sum is \(S_{N,\iota q}(u)\). The second differs from \(S_{N,q}(\{u+\theta\})\) by at most two pointwise, since the index shift \(l(u)\) is independent of \(j\). Thus
\[
 \|S_{N,\iota q}-S_{N,q}(\,\cdot+\theta)\|_1
     \le 4+4\sum_{j\ge1} e_j .                                   \tag{8}
\]
Combining with the bounded sum of the two phase scores proves a uniform bound on \(\|S_{N,q}(\,\cdot+\theta)+S_{N,q}\|_1\). For integer \(m\), rotation preserves Lebesgue measure, so the absolute Fourier coefficient of the latter function is \(|1+\exp(2\pi i m\theta)|\,|\widehat S_{N,q}(m)|\). The multiplier never vanishes, including at \(m=0\). This proves (2) term by term for every fixed trigonometric polynomial. It supplies no uniform bound over arbitrarily high frequencies.

## One direction on one patch

Choose a continuous bump \(0\le\phi\le1\) on the log circle supported strictly inside \(\log_{81}J\), equal to one on a neighborhood of \(\log_{81}\overline K\). Each child with \(x/R_j\in K\) then has \(\phi=1\) on its whole log cell at all sufficiently large levels. Conversely, a log cell meeting the support has \(x/R_j\in J\) at all sufficiently large levels. These two margins avoid boundary atoms or a changing test function.

For arbitrary \(\epsilon>0\) choose one real trigonometric polynomial \(P\) with \(\|\phi-P\|_\infty<\epsilon\). Equation (2) and \(\|S_{N,q}\|_1\le V_N\) give
\[
             |\int\phi S_{N,q}|\le C_P+\epsilon V_N.               \tag{9}
\]
In the nonnegative \(\phi\)-weighted log sum the two directed contributions have difference \(\int\phi S_{N,q}\). Their sum is at most **twice either one** plus the absolute difference. The log weight of each patch cell is comparable with \(1/R_j\). The support and one-region of \(\phi\), followed by (9), therefore give for absolute constants \(c,C>0\)
\[
 c\sum_{j\le N}U_j(K)/R_j\le C_J+C D_N(J)+C_P+\epsilon V_N .     \tag{10}
\]
Insert (10) into (6). Choose \(\epsilon<c/(2A_K)\) first and then its one fixed polynomial. Absorbing the resulting term proves (1), with constants independent of the terminal row. This proof also gives the stated continuous-test consequence of (2) by dividing (9) by \(V_N\) and then letting \(\epsilon\) decrease.

## What remains on the physical pair and at first passage

PR199, `d868f8e8405c08b8c501236853bea495ca593824`, `research/optimal-critical-ancestors-20261124/FIRST_PASSAGE.md`, section 1, proves the one-head closure argument using M, namely positive lower natural density for ordinary predecessors of every fixed positive odd ternary unit. Its argument applies to the basin-of-one indicator directly as reconstructed in PR201, `3c9e444e3f2f2e457b25cd827dc9a29f981e9de2`, `research/killed-green-head-closure-20261124/README.md`, (KG11). The proof uses (1) to infer summability of **actual unphased color changes**, hence convergence of the head indicator in \(L^1\). Exact dyadic returns force its limit to be constant. M excludes a zero-density minority when there is a counterexample. Universal convergence makes the selected directed count identically zero.

For example fix in advance only **nonconvergent children with even-time-to-one parents** in one chosen patch. This additional profile refinement uses PR201's pair-chain input P, namely PR146 `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/THREE_RAY_UPPER.md`, with the survival, holding and boundary estimates specified in PR201. At PR201's common clock the discarded complement of `GOODPROFILE` has summable normalized error over all levels of the `[7,8)` head, by (KG8), the signed-level concentration in section 3, (KG6), and their original-source transfer (KG7). At any fixed finite list of ordinary affine comparison arms, T3 discards three or more surviving symbolic classes at that same clock at summable cost, using its tail at \(t_j\asymp j\) and the full-grid upper bound over original parents of length \(R_j/81\) with \(2^{t_j}\le R_j/81\). Thus it suffices to sum just the indicated directed mass on the remaining mesoscopic two-class profiles in the chosen patch. This is a new sufficient subpopulation. Its size is open.

If counted via the timely first entrances of PR197 `joint-renewal/LANDING_WEIGHT_TRANSFER.md` at `9ab91d964b38fc870d1034bac628d62f59488467`, the parent's original phase on a hit at clock \(s\) and height \(w\) is \(\iota^s L(w)\). Keep \(s\bmod2\), the patch, and any common-clock profile restriction in the original-source multiplicity. The unmarked pair weights \(W_j(v,w)\) alone do not give the directed phase. Neither the joint modular-clock error bounds in PR197 nor either marginal entrance cap imply a summable estimate for this selected mass. The reductions above never replace the pair by independent samples. T3's probabilistic source and M's external verification were not independently rebuilt here.

`PhaseCut.lean` proves the finite label identities, the path-crossing statement, exact summation of the comparison squares, and the normalized horizontal recurrence estimate. The rotation, ordinary multiplicities, transfer, and conclusion (1) are written mathematics.

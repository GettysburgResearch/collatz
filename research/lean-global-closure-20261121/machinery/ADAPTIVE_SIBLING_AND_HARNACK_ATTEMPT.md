# Adaptive sibling transport and the Harnack closing attempt

Date: 2026-11-22. **Outcome: the needed sibling-leakage lower bound remains OPEN.** The finite-depth construction below does change inverse words and improves on literal-prefix copying, but its proved cost does not close the estimate. The reversible recurrence calculation explains why ordinary electrical recurrence cannot substitute for the missing directed comparison. No new Lean theorem or Collatz closure is claimed.

## 1. Exact closing target and inputs

Use the accelerated odd map U on nonperiodic positive odd ternary units. Forward motion is killed on entering a periodic vertex. Retain the frozen critical inverse operator P, unit obstacle u, least excessive envelope V, harmonicization G, and ordinary harmonic flow ν:

\[
V^{[0]}=u,\qquad V^{[r+1]}=\max(u,PV^{[r]}),\qquad
V^{[r]}\uparrow V,\qquad G\le V\le2\chi G,
\]
\[
L\nu=\nu,\qquad 0<\delta\nu\le G/\mathrm{id}\le\nu\le A.
\]

The operator is
\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
\frac3{2^e}f((2^e q-1)/3).
\]
Nonunit parents have zero obstacle and envelope and can be omitted.

For B(n)=64n+21 the actual siblings satisfy U(Bn)=U(n). PR180's current-through-siblings argument gives, on every hypothetical escaping path q_k=U^k p,
\[
G(q_k)\ge\delta\nu(p)q_k,\qquad
\sum_k\mathscr L_G(q_k)<\infty,
\qquad
\mathscr L_G(n)=\sum_{j\ge1}64^{-j}\frac{G(B^j n)}{G(n)}.
\tag{1}
\]

The direct objective was its OPEN-S estimate: for each η>0, find c_η>0 and Q_η such that
\[
G(n)\ge\eta n,\quad n\ge Q_\eta
\quad\Longrightarrow\quad
\mathscr L_G(n)\ge\frac{c_\eta}{\log(2+n)}.
\tag{2 -- OPEN}
\]
The actual upper growth q_k+1≤(3/2)^k(p+1) would make this lower series diverge, contradicting (1). This is the previously stated closing target, not a new reduction.

## 2. An actual adaptive inverse-tree injection

Literal copying keeps the same valuations and therefore fails deep ternary integrality. Instead, let x,y be retained positive odd units with x≡y mod3. There is a unique
\[
d(x,y)\in\{0,2,4\},\qquad 2^{d(x,y)}y\equiv x\pmod9,
\tag{3}
\]
because the powers 2^0,2^2,2^4 are the three units congruent to one modulo three.

For every actual unit parent
\[
x'=(2^e x-1)/3,
\]
use the changed exponent e'=e+d(x,y) at y. Then
\[
y'=(2^{e'}y-1)/3,\qquad
y'-x'=\frac{2^e(2^{d(x,y)}y-x)}3\equiv0\pmod3.
\tag{4}
\]
Both parents are positive odd integers; y' is a ternary unit because x' is. Both remain nonperiodic because their roots are nonperiodic. The map on parent exponents is injective, and its critical coefficient ratio is exactly 2^(-d), at least 1/16. Repeating the construction produces an injection of the entire rooted inverse tree, preserving depth, prefix extension, and the unit status of every vertex. It does not identify the endpoint of the changed word with the old endpoint.

Consequently, by induction on the Bellman recursion,
\[
\boxed{V^{[r]}(y)\ge16^{-r}V^{[r]}(x)\qquad(r\ge0).}
\tag{5}
\]
For the induction step, apply the previous-depth inequality to every paired parent in (4), sum with its actual coefficient, and use the inclusion of the image among y's parents. The obstacle value one is also at least 16^(-(r+1)) times the old obstacle. Taking the maximum proves the next level. Interchanging x,y gives the reverse comparison with the same factor.

This construction changes the physical word. In contrast to the fixed-word lift's sibling index 3^(r−1), it works at the first sibling B(n) at every finite depth. It does not supply a depth-independent comparison of G.

### Why the certified cost is still insufficient

The raw row sum satisfies P1≤2. Thus V^[r]≤2^r, and any level that can witness V^[r](n)≥ηn necessarily has
\[
r\ge\log_2(\eta n).
\tag{6}
\]
When both n and Bn are retained, as they are on every escaping component, and V^[r](n)≥V(n)/2, (5) gives only
\[
\frac{G(Bn)}{G(n)}\ge\frac{16^{-r}}{4\chi}.
\tag{7}
\]
The guaranteed coefficient 16^(-r) at depths allowed by (6) is at most (ηn)^(-4). This is a limitation of this lower-bound certificate, **not an upper bound on the true sibling ratio**. It cannot imply (2). There is also no established upper bound on the depth at which V^[r](n) approximates V(n).

## 3. The attempted amortization, with the remaining quantity retained

A less wasteful complete parent bijection is possible. In each allowed exponent class modulo six, replace its representative a∈{1,...,6} by the representative of a+d in the same set and retain the nonnegative six-step quotient. This changes an exponent by either d or d−6, so some edges have a coefficient gain. The image classes are precisely the unit-parent classes at y, and (4) still gives matching unit residues. The map a↦a+d modulo six carries exactly the unit-parent exponent classes at x to those at y: 2^(a+d)y≡2^a x mod9. Thus it is a bijection of the two allowed classes, including their unchanged nonnegative six-step quotients.

Let x_0=x,y_0=y be the paired roots, x_j,y_j their paired inverse paths, and a_j,b_j their actual exponents. Put
\[
A_r=\sum_{j=1}^r a_j,\qquad B_r=\sum_{j=1}^r b_j,
\qquad
\Lambda_x=\prod_{j=1}^r\frac{3x_j}{3x_j+1},\quad
\Lambda_y=\prod_{j=1}^r\frac{3y_j}{3y_j+1}.
\]
The complete physical edge identities telescope to
\[
\boxed{
2^{B_r-A_r}
=\frac{y_r}{x_r}\frac{x_0}{y_0}\frac{\Lambda_x}{\Lambda_y}.}
\tag{8}
\]
Both products lie in [δ,1] by the pinned nonperiodic reciprocal-orbit bound. Therefore amortizing the accumulated exponent cost requires control of the **paired terminal-height ratio**, not merely control of each residue repair.

I tried to use the signed per-edge gains in this bijection to bound (8) on the actual stopping trees responsible for a high V-value. No polynomial-in-depth bound, suitable averaged height-ratio bound, or bound in terms of log n was obtained. Replacing those stopping trees by independent geometric digits would change the measure to which (2) applies. The available path-law comparisons preserve this issue: they compare two laws on the same root's tree, not the paired endpoint heights of these two different inverse branches.

In particular, a polynomial-in-depth repair cost by itself would still need a quantitative statement about an adequate obstacle depth. The attempted closing argument has not supplied either input.

## 4. What the reversible potential theory actually says

The natural Harnack strategy was to use the short undirected path n→U(n)←B(n). Its inverse kernel
\[
K(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)}
\]
only moves backward. Distinct siblings have disjoint inverse subtrees, so this two-edge route is not a path of K. Passing to a reversible chain changes the equation.

Here is the exact reversible calculation on a hypothetical escaping component C. Write c_C=lim_k ν(U^k p)>0 and choose its integer clock ℓ with ℓ(Un)=ℓ(n)+1 and ℓ(p)=0. Every clock level has the same finite mass:
\[
\boxed{\sum_{n\in C:\ell(n)=j}\nu(n)=c_C\qquad(j\in\mathbb Z).}
\tag{9}
\]
Indeed, for large k the level-j sources that have joined q_k are exactly its depth-(k−j) predecessors and have mass ν(q_k). These sets increase and exhaust the whole level. Monotone convergence gives (9).

Let Ff(n)=f(Un), and let S=(F+K)/2. Then S is an irreducible reversible Markov chain with vertex measure ν and edge detailed balance
\[
\nu(n)S(n,Un)=\nu(Un)S(Un,n)=\nu(n)/2.
\tag{10}
\]
Its clock coordinate is simple symmetric random walk: forward and backward moves each have probability one half. Every clock level is hit again almost surely. The trace chain on a fixed level is reversible for the finite measure in (9), by reversing each finite excursion path. Normalizing that measure gives an invariant probability for the trace. Poincaré recurrence of its stationary path law then makes every state recurrent. Hence S is recurrent on C, even though the stipulated ordinary forward orbit escapes.

An equivalent energy calculation is particularly transparent. Give the undirected edge {n,Un} conductance ν(n), and for an integer M≥1 define
\[
\chi_M(n)=\max(0,1-|\ell(n)|/M).
\]
Then
\[
\sum_n\nu(n)\chi_M(n)^2<\infty,
\qquad
\boxed{\sum_n\nu(n)(\chi_M(n)-\chi_M(Un))^2=2c_C/M.}
\tag{11}
\]
These are cutoff functions on finitely many clock levels, not finite vertex sets. Finite vertex truncations converge in L²(ν); the bounded gradient operator makes their energy errors tend to zero too. Thus they also supply finite-support recurrence cutoffs.

For the canonical Green potential R∈[0,1] of finite U-energy, the same cutoffs give
\[
\mathcal D_U(R-R\chi_M)\longrightarrow0
\tag{12}
\]
on this component. To check it, expand the edge difference of (1−χ_M)R. Its squared energy is at most
\[
2\sum_n\nu(n)(1-\chi_M(n))^2|R(n)-R(Un)|^2
+2\mathcal D_U(\chi_M).
\]
The first term vanishes by domination with the finite R-energy, and the second by (11). Thus energy approximation by an appropriate cutoff already coexists with escape. It must not be confused with the particular finite-Green approximation or the sharp moving-average rate whose defect is the surviving escape charge.

### The literature hypothesis test

Delmotte's parabolic Harnack characterization is for reversible weighted graphs with its specified volume regularity, Poincaré inequality, and local transition lower bound. See the primary paper's Section 1.1 and main theorem in Section 1.4. The actual inverse kernel fails reversibility. For S, every vertex has infinitely many positive unit-parent transitions whose probabilities sum to one half, so the required uniform positive bound on adjacent transition probabilities fails. Moreover G is P-harmonic, not asserted to be S-harmonic.

Electrical recurrence and recurrent-chain Liouville conclusions do not remove these distinctions. Equations (9)–(12) show directly that obtaining recurrence of S would not contradict the escaping component used to define it. The needed conclusion is the arithmetic directed leakage (2), not recurrence of an auxiliary walk.

## 5. Frozen references and scope

- PR180 `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`, `research/central-step-20261122/CRITICAL_BOUNDARY.md`, §6: actual sibling current, OPEN-S, OPEN-F and fixed-word cost.
- PR176 `5cb67181758186b372944ef60a1bd09416b97f89`, `research/lean-global-resolvent-20261121/overview/central/FIXED_SOURCE_SIBLING_LIFTS.md`: literal-prefix integrality and source-weight costs.
- PR185 `4b0c2c27812db555061f5d9006de82a87e7e364f`, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`: ν, bounded harmonic comparison and path-product input.
- T. Delmotte, *Parabolic Harnack inequality and estimates of Markov chains on graphs*, Rev. Mat. Iberoam. 15 (1999), 181–232, https://doi.org/10.4171/RMI/254; primary text https://ems.press/content/serial-article-files/37954?nt=1 . The theorem hypotheses and stated equivalence were checked; no new application outside them is claimed.
- R. Lyons and Y. Peres, *Probability on Trees and Networks*, §2.5, https://rdlyons.pages.iu.edu/prbtree/ . The electrical viewpoint motivated the test; the countable-state recurrence calculation above is supplied directly, so a locally finite cutset theorem is not silently applied to infinite-degree vertices.

The new finite-depth injection and the conditional reversible calculations are proved above. They do not establish (2), a uniform obstacle-depth bound, or Collatz convergence. No old Lean build or numerical enumeration was performed for this note.

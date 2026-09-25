# Arithmetic component rigidity for the shortcut Collatz map

**Date:** 25 September 2026.  
**Status:** PROPOSED research manuscript with proofs; not independently reviewed.  
**Verdict:** No complete Collatz proof is claimed. The regularity estimate in Section 7 is OPEN. No external priority claim is made for the elementary lemmas or this assembly.

## 0. The change of object and the inspected baseline

The object is not another catalogue of successful parity cylinders. It is the algebra of functions on the **ordinary positive integers** that are constant on merger components. The intended closing theorem is a rigidity theorem for that algebra. The discrete derivative of an invariant function exposes exactly what a nontrivial component partition would have to do at every arithmetic scale.

Use the unabsorbed shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Thus 1 and 2 form a two-cycle. Every clock below is a shortcut clock, and every displayed inverse is a positive ordinary integer with a physical parity word.

Repository inspection: `GettysburgResearch/collatz`, main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; README, AGENTS, research map and integrated errata were read. The detailed recent source reading includes:

* PR #133 at `9ad7b5b9c0eafacbecb1b185616ae52e573998cf`, `research/astra-exit-merging/pointwise-signatures/PROOF.md`: fixed-point versus uniform-family obstructions, primitive point-preserving lifts and derivative escape.
* PR #134 at `025f2683c19bfedc3eeff0303206b20c889c8005`, `research/paired-comparison/endpoint-transplant/PROOF.md`, Sections EPT-001/002 and their synchronizer: thickness of every original component, endpoint transplantation and its height bill.
* Live descriptions of the other recent stacked proposals through #136 were inspected. That is not an independent review of every proof, artifact or later source head.

The current project already distinguishes finite ordinary witnesses from one fixed all-time integer, fresh-shell contraction from transported distributions, and guarded mergers from complete selectors. This packet does not reuse a corrected statement without its hypotheses. Its proofs below require none of the project's pending SC*/FC*, transport, rank, or affine-compiler statements.

Graph/sufficient-set and functional-equation approaches are not new. See Monks et al., *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, arXiv:1204.3904, and Bell–Lagarias, *3x+1 inverse orbit generating functions almost always have natural boundaries*, arXiv:1408.6884. The contribution attempted here is a specific combination of ordinary component geometry, exact boundary conservation and quantitative scale-variation constraints, not the invention of graph connectedness or functional reformulation.

## 1. The invariant algebra and its exact boundary equations

Write n ~ m when there are finite a,b >= 0 with T^a(n)=T^b(m). This is an equivalence relation. For transitivity, advance the two meeting states far enough along the middle source's forward orbit to reach a common state.

An invariant Boolean function is a function b:N_{>0}->{0,1} satisfying b(T(n))=b(n). It is exactly a union-of-components indicator. Therefore:

**CR-001 (exact equivalence).** Collatz holds if and only if the only invariant Boolean function with b(1)=0 is b=0.

Indeed, convergence sends every b(n) to b(1). Conversely, if N does not reach 1, the indicator of its merger component is a nonzero invariant with value zero at 1. A component meeting 1 must converge: the forward orbit of 1 is contained in {1,2}.

For the rest of this section let

\[
d_n=b(n+1)-b(n),\qquad n\ge1.
\]

The two invariances are

\[
b(2n)=b(n)\quad(n\ge1),\qquad
b(2n+1)=b(3n+2)\quad(n\ge0).
\]

Their exact discrete-derivative form is

\[
\boxed{d_n=d_{2n}+d_{2n+1}\quad(n\ge1)}\tag{D2}
\]

and

\[
\boxed{d_{2n+1}+d_{2n+2}
 =d_{3n+2}+d_{3n+3}+d_{3n+4}\quad(n\ge0).}\tag{D3}
\]

The boundary condition is d_1=0. In addition the primitive must remain Boolean:

\[
b(1)=0,\qquad b(n)=\sum_{j=1}^{n-1}d_j\in\{0,1\}.
\]

This last condition cannot be dropped. Merely solving the two linear current equations is a larger problem.

**CR-002 (converse, including boundaries).** These current equations, boundary and Boolean-primitive condition imply all the original invariances.

*Proof.* Let E(n)=b(2n)-b(n). Equation D2 says E(n+1)-E(n)=0. Since E(1)=d_1=0, all E(n)=0. Let O(n)=b(3n+2)-b(2n+1). Equation D3 says O(n+1)-O(n)=0. Again O(0)=d_1=0, so all O(n)=0. This also proves the forward implication by taking differences. ∎

There is an exact finite version. On 1..H retain every edge n->T(n) with both endpoints <=H, without assigning any exterior port a color. Then finite invariance is equivalent to d_1=0 together with D2 for 1<=n<=floor((H-2)/2), and D3 for 0<=n<=floor((H-5)/3). Empty ranges are omitted and H=1 has no constraint. The same telescoping proof applies. This is useful for checking ALL possible boundary colorings, not only a supplied convergent orbit.

## 2. A conservation law for boundary creation

Define the variation in the k-th dyadic shell by

\[
V_k=\sum_{n=2^k}^{2^{k+1}-1}|d_n|.
\]

This counts changes of component color between neighboring integers across the shell, including its right endpoint. The scale k is a **binary height scale**, not an orbit clock.

For a Boolean primitive, d_n belongs to {-1,0,1}. Equation D2 forces:

* if d_n=1, its children are (1,0) or (0,1);
* if d_n=-1, its children are (-1,0) or (0,-1);
* if d_n=0, its children are (0,0), (1,-1), or (-1,1).

Let B_k be the number of n in [2^k,2^{k+1}) for which d_n=0 and the two children are opposite nonzero signs. These are paired boundary births. Equivalently, b(n)=b(n+1) differs from b(2n+1).

**CR-003 (exact birth identity).**

\[
\boxed{V_{k+1}=V_k+2B_k.}\tag{B}
\]

*Proof.* At each parent the sum of the two child absolute values equals the parent absolute value, except at a birth where it exceeds it by two. Sum over the shell; the child pairs partition the next shell. ∎

In particular V_k is nondecreasing. Since V_0=|d_1|=0,

\[
V_k=2\sum_{j=0}^{k-1}B_j.\tag{B'}
\]

This is not a decreasing rank. No estimate limiting the total births is being inferred from conservation alone. Equation D3 is the extra arithmetic compatibility that an eventual rigidity proof must exploit.

## 3. A growing inverse ladder in every ordinary component

### 3.1 A uniformly controlled inverse choice

For any positive y>=2 with 3 not dividing y, choose k from

\[
\{2,4\}\quad\text{if }y\equiv1\pmod3,\qquad
\{3,5\}\quad\text{if }y\equiv2\pmod3,
\]

so that

\[
z=\frac{2^ky-1}{3}
\]

is not divisible by three. Choose the smaller admissible k for a deterministic rule.

Both candidate numerators are divisible by three. They cannot both be divisible by nine: increasing k by two multiplies 2^ky by four, and if that quantity is 1 modulo nine, four times it is 4, not 1. Thus the choice always exists. The result z is a positive odd ternary unit and

\[
T^k(z)=y,
\]

with exact word 1 followed by k-1 zeros. Moreover

\[
\boxed{\frac54y\le z\le\frac{32}{3}y<16y.}\tag{G}
\]

For the only possibly tight case k=2, y is 1 modulo three and y>=4, so (4y-1)/3 >= 5y/4. The other cases have stronger growth.

Every original N has a unit y_0>=2 in its component with y_0<=5N. For a unit N>=2 take y_0=N. For N=1 take y_0=5, using T^4(5)=1. If 3 divides N, write N=2^v u with u odd and take y_0=(3u+1)/2 after v halvings and one odd step. This target is 2 modulo three and <=2N. These are explicit finite links, not assumptions about eventual convergence.

Iterating the inverse choice gives y_0,y_1,..., where every y_j is in the same original component and

\[
2(5/4)^j\le y_j\le5N\,16^j.
\]

For a unit original N>=2 these are pure ancestors of N. For a multiple of three they are linked through the supplied short forward arm. That distinction is retained.

### 3.2 Deterministic logarithmic equidistribution

Let K_j be the sum of the inverse clocks through stage j, and put alpha=log_2(3). The inverse identity gives

\[
\log_2 y_j=\log_2 y_0+K_j-j\alpha+e_j,
\]

where

\[
e_j=\sum_{i<j}\log_2\left(1-\frac1{2^{k_i}y_i}\right).
\]

These errors converge absolutely. Since k_i>=2, y_i>=2, and -log_2(1-u)<=2u for 0<=u<=1/8,

\[
|e_\infty-e_j|
 \le\sum_{i\ge j}\frac1{2y_i}
 \le\frac5{2y_j}
 \le\frac54(4/5)^j.\tag{E}
\]

The number alpha is irrational: a rational identity alpha=p/q would imply 3^q=2^p. Modulo one, the integer K_j disappears. Thus the phases log_2(y_j) are an irrational rotation plus an error tending to a constant.

**CR-004 (inverse-ladder equidistribution).** The fractional parts of log_2(y_j) are uniformly distributed in [0,1).

*Proof.* For each nonzero integer h, the average of exp(-2*pi*i*h*j*alpha) tends to zero by the geometric-series formula. Multiplying by the phase exp(2*pi*i*h*e_j), which converges, preserves this limit: the average error from replacing it by its limit tends to zero. The elementary Fourier criterion for uniform distribution gives the result. ∎

This is a theorem about one explicitly constructed **backward** ladder, not a claim that arbitrary forward trajectories are random or Benford-distributed.

## 4. Uniform relative-gap geometry and exact certificates

Normalize a positive real number modulo multiplication by powers of two into [1,2). For a finite nonempty set of phases, sort representatives a_1<...<a_r and define its maximum circular multiplicative gap

\[
G=\max(a_2/a_1,\ldots,a_r/a_{r-1},2a_1/a_r).
\]

All representatives of integer nodes are exact rational numbers. If G<R, then doubling the nodes gives a point in every [X,RX] once X is at least the largest node. Indeed, the circular phase arc from X to RX cannot be empty, and the corresponding power of two is nonnegative at that height.

A uniform-in-N version has a finite arithmetic certificate. Let G_Q be the maximum gap of the normalized numbers 3^j, 0<=j<=Q. Reciprocal phases have the same maximum gap. Choose M>=0 and R>1 such that

\[
c_M=\frac58(4/5)^M,\qquad
\boxed{\frac{G_Q}{1-c_M}<R.}\tag{U}
\]

Such M,Q exist for every R>1, by irrational-rotation density and c_M->0. They can be found and checked with rational arithmetic.

For completeness, define E_j=2^{e_j}. The sum of the multiplicative losses from index M onward is at most c_M:

\[
\sum_{i\ge M}\frac1{2^{k_i}y_i}\le c_M.
\]

The elementary inequality product(1-u_i)>=1-sum(u_i), applied to finite products and then a limit, gives

\[
1\le E_j/E_\infty\le(1-c_M)^{-1}\quad(j\ge M).
\]

Consequently the phases of y_M,...,y_{M+Q} are a common rotation of the reciprocal powers of three, with each phase shifted forward multiplicatively by a factor in [1,(1-c_M)^{-1}]. A one-sided perturbation of that size increases the maximum circular gap by at most the same factor. To see this, an empty perturbed arc (a,b) would imply an empty unperturbed arc (a,b(1-c_M)); hence b/a<=G_Q/(1-c_M). Equation U therefore certifies the required net for every original N.

**CR-005 (uniform relative-gap theorem).** For every R>1 there is an effective C_R, independent of N, such that

\[
\boxed{\forall N\ge1\;\forall X\ge C_RN:\quad
[N]\cap[X,RX]\ne\varnothing.}\tag{RG}
\]

Here [N] is the original merger component. One admissible constant from a certificate U is

\[
C_R=5\,16^{M+Q}.
\]

*Proof.* Every node in the certified segment has size at most this constant times N by G. Apply the finite-net/doubling argument. Every resulting integer is linked to the original N by explicitly composable physical paths. ∎

The file `net_certificates.json` contains the exact rational inequalities for

| R | Q | M | Admissible C_R |
|---|---:|---:|---:|
| 11/10 | 11 | 14 | 5 * 2^100 |
| 101/100 | 146 | 32 | 5 * 2^712 |

These constants are intentionally conservative, not optimal or practical. The significance is the order of quantifiers: **one constant works for all ordinary original sources**. The 1% statement, for example, is that every original component meets every [X,1.01X] for X>=5*2^712*N. It does not claim positive natural density or additive bounded gaps.

### 4.1 A macroscopic-block closing criterion

Let C be the set of integers that reach 1.

**CR-006.** If there is some fixed R>1 and an unbounded sequence X_j for which every integer in [X_j,RX_j] belongs to C, then Collatz holds.

*Proof.* Fix any N. For large enough j, X_j>=C_RN. The relative-gap theorem supplies a member of [N] inside the convergent block. Thus [N] is the component of 1. This works for each N. ∎

This is stronger as a sufficiency reduction than merely observing that eventual bounded gaps in C would suffice. It needs only arbitrarily high **proportionally wide** convergent blocks, not a bounded-gap theorem everywhere. However, no such block sequence is constructed here. Arbitrarily long blocks whose lengths divided by their locations tend to zero do not meet the criterion. In particular, the thickness result in PR #134 cannot be silently substituted for it.

## 5. Quantitative rigidity: nontrivial components require rough boundaries

The relative-gap theorem already implies that, if b is a nonconstant invariant Boolean function, both colors occur in every sufficiently high interval of any fixed relative width. Thus no fixed-width angular interval in a normalized dyadic shell can remain monochromatic. In particular V_k cannot stay bounded.

The logarithmic error estimate gives a stronger, quantitative conclusion.

**CR-007 (scale-variation obstruction).** For every nonconstant invariant Boolean b,

\[
\boxed{\limsup_{k\to\infty}\frac{V_k}{k}\ge\frac1{32}.}\tag{VR}
\]

Equivalently, with b(1)=0,

\[
\limsup_{k\to\infty}\frac1k\sum_{j<k}B_j\ge\frac1{64}.
\]

Only a limsup is asserted; no bounded-partial-quotient property of log_2(3) is assumed.

*Proof.* Choose N with b(N) different from b(1). Use the inverse ladders linked to 1 and N. Let p/q run through the continued-fraction convergents to alpha=log_2(3), so |alpha-p/q|<1/q^2, gcd(p,q)=1, and q tends to infinity.

Choose M=M(q) so that (5/4)(4/5)^M<=1/q. Then M=O(log q). For j=M+i, 0<=i<q, equation E puts the logarithmic phases of either ladder within 1/q of a translate of -i*alpha. Replacing alpha by p/q moves each point by less than another 1/q. Since multiplication by p permutes the residues modulo q, these points are within circular distance 2/q of an equally spaced q-point grid. Their largest circular additive gap is therefore at most 5/q.

Set

\[
k_q=\lceil\log_2(5N)\rceil+4(M+q).
\]

All selected nodes of both ladders are <=2^{k_q}. Doubling them into [2^{k_q},2^{k_q+1}) preserves their colors and phases. Partition the logarithmic circle into L=floor(q/8) equal arcs. For large q every arc has length at least 8/q>5/q, so its corresponding integer interval contains both colors. It therefore contains at least one adjacent color change. The arcs have disjoint interiors, so the changes are distinct and V_{k_q}>=floor(q/8).

Finally k_q/q tends to 4. Hence the limsup is at least (1/8)/4=1/32. The birth formulation follows from B'. ∎

An analogous argument for an arbitrary real-valued invariant f gives

\[
\limsup V_k(f)/k\ge |f(N)-f(M)|/32
\]

for any two fixed sources M,N; the shell height offset is enlarged to accommodate both. Taking the supremum over pairs gives the oscillation of f on the right. This is a genuine Liouville criterion for a specified regularity class, not unrestricted Liouville rigidity.

**Corollary.** Every invariant f with V_k(f)=o(k) is constant. In particular, every invariant Boolean coloring with bounded dyadic variation is constant.

The lower bound uses only two fixed original components and finite positive inverse paths. There is no Haar-typical-point argument or exchange of an ordinary source for a favorable nearby source.

## 6. A control that the eventual closing argument must distinguish

For the shortcut 5x+1 map, the following are three disjoint physical positive cycles:

    1 -> 3 -> 8 -> 4 -> 2 -> 1
    13 -> 33 -> 83 -> 208 -> 104 -> 52 -> 26 -> 13
    17 -> 43 -> 108 -> 54 -> 27 -> 68 -> 34 -> 17.

Their basins give nonconstant invariant Boolean functions, without any conjecture about other 5x+1 trajectories. Exact cycle replay and separation are included in the experiment.

The dyadic current law and birth identity still hold. The odd-branch law becomes b(2n+1)=b(5n+3), so the second current law is

\[
d_{2n+1}+d_{2n+2}=\sum_{j=0}^{4}d_{5n+3+j},
\]

with its corresponding boundary b(3)=b(1), in addition to b(2)=b(1).

Growing inverse ladders and dense logarithmic phases are also possible in those components. For a unit modulo five, choose k in two sufficiently large admissible classes differing by four. Two generates the units modulo five; multiplying by 16 changes 1 modulo 25 to 16, so at least one predecessor remains a unit modulo five. The phases are an irrational rotation by -log_2(5) plus a summable error, just as above.

Therefore the assertion “multiplicatively independent scales or dense normalized components force global connectedness” is false. Nor does the birth identity alone imply sublinear births. The eventual upper estimate must use the actual THREE-term law and its arithmetic offsets; a formal argument that also proves the same result for this 5x+1 control has made an unsupported inference.

## 7. The first unsupported step and the theory-building programme

A precise sufficient target is:

> **OPEN regularity target.** Every globally defined invariant Boolean b for the actual 3x+1 map, with b(1)=0, satisfies V_k=o(k).

Equivalently, total boundary births through scale k are o(k). CR-007 would then force b=0 and prove Collatz. The target may be weakened to the particular invariant indicator of nonconvergence; no sublinear estimate is proved here for that indicator either.

The new task is **not** to assume this regularity, to deduce it from irrationality alone, or to discover another equivalent formula and declare the gap smaller. It is to derive an upper bound from the full arithmetic current equations, with Boolean primitiveness and original-source information retained. The present theorem supplies a rigorous lower-growth barrier against which any proposed upper estimate can be tested.

There is also a geometric route: construct unbounded macroscopic convergent blocks as in CR-006. Existing finite-family gates become relevant only when their location-versus-width bill is controlled. More blocks at much larger heights do not automatically progress toward that target.

A disciplined next computation should test inequalities on **all compatible finite boundary assignments**, not only on a single known-convergent coloring (which is identically zero). Finite graph components parameterize all such assignments. Exterior ports must remain unassigned; wiring them to the core silently assumes the desired conclusion. A finite coloring need not extend to an infinite one, so it can refute a purported finite local inequality but cannot by itself refute an infinite-only theorem.

For an original least-source variant, fix b(1)=...=b(N-1)=0 and b(N)=1, and retain those constraints as scale grows. This keeps source order rather than allowing the first nonzero point to move with the window. The target is a boundary-aware coercive inequality or an actual renormalization law that rules out the forced roughness. None has been supplied in this packet.

## 8. Exact executed evidence and what it does not establish

`experiment.py` uses only the Python standard library. The executed normal and optimized runs produced byte-identical `results.json`.

* All 262,143 Boolean assignments with b(1)=0 on heights 1 through 18 were checked for equivalence between finite graph invariance and the finite current system. All 76 admissible assignments in that combined inventory were retained.
* 160 additional nonzero local colorings on heights 64,256,1024,4096,16384 retained every unresolved exterior component. They gave 1,440 exact shell birth checks. These colorings are local controls, not asserted infinite separators.
* 4,096 original sources each received a 96-edge inverse ladder: 393,216 physical inverse edges, each checked for integrality, positivity, original linkage, growth and literal parity.
* Six separately retained 512-edge ladders give exact finite 1% nets. Ninety-six displayed window witnesses were fully replayed. The maximum-gap proof makes each finite net an all-sufficiently-high-window certificate, not a sampling extrapolation.
* Two finite rational certificates verify the universal constants in Section 4.
* Three disjoint 5x+1 cycles and seven direct negative controls were checked.

The separate `verify_certificates.py` imports neither the generator nor any project module. In both normal and optimized execution it checked the two universal arithmetic inputs, all six retained nets, 3,072 inverse edges, 96 complete window arms, and rejected six semantic mutations. This is same-author implementation diversity, not independent mathematical review.

The semantic experiment hash is `d43c7b75ccc8e6144e40d65d3805f29776750aaf1053c455183505d965605258`. Full executed file hashes and commands are in `validation.json` and `SHA256SUMS.txt`.

No complete-checkout repository validation, remote CI, Lean build, full independent literature-priority audit, or independent mathematical peer review was performed. No repository branch, PR, canonical status, main file, workflow or setting was changed. The files form a standalone proposed research packet.

## References and source pins

1. Repository baseline: `https://github.com/GettysburgResearch/collatz/tree/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
2. Pointwise signatures: `https://github.com/GettysburgResearch/collatz/blob/9ad7b5b9c0eafacbecb1b185616ae52e573998cf/research/astra-exit-merging/pointwise-signatures/PROOF.md`.
3. Endpoint transplantation: `https://github.com/GettysburgResearch/collatz/blob/025f2683c19bfedc3eeff0303206b20c889c8005/research/paired-comparison/endpoint-transplant/PROOF.md`.
4. K. Monks, K. G. Monks, K. M. Monks, M. Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, `https://arxiv.org/abs/1204.3904`.
5. J. P. Bell, J. C. Lagarias, *3x+1 inverse orbit generating functions almost always have natural boundaries*, Acta Arith. 170 (2015), 101–120; `https://arxiv.org/abs/1408.6884`.

External references establish context, not premises for the elementary proofs here. Their presence is not a claim that a comprehensive novelty search has been completed.

# Linear harmonic spikes and tiny doubling gains on the unchanged integer graph

**PROPOSED written obstruction, with a finite arithmetic kernel.** The map in this note is the genuine Collatz map. Every displayed integer orbit converges to 1. The object we modify is an inverse-harmonic **profile**, not the actual predecessor density or the canonical Cesàro trace.

There are nonnegative pointwise finite inverse-harmonic profiles with linear-sized values on arbitrarily large positive integers and zero normalized gain along actual first-doubling segments. Adding such a profile to the canonical trace preserves strict positivity and exact inverse harmonicity. After the correct affine cocycle is removed, the added profile is a fixed boundary atom. Its doubling gains still violate every uniform inverse-logarithmic lower bound along a subsequence.

This gives a precise obstruction to deriving the surviving positive-density gain conjecture from positivity, a large ordinary-integer profile and inverse harmonicity alone. The canonical selection and its nonatomic fixed-root boundary law are necessary additional information. It is **not** a counterexample to the gain conjecture for actual predecessor densities.

## 1. A bounded-exponent inverse ray with repeated genuine first doublings

Write

\[
 U(v)=\frac{3v+1}{2^{v_2(3v+1)}},\qquad
 I_e(v)=\frac{2^e v-1}{3}.
\]

Start with \(A_0=5\). Given an odd \(A_j\equiv2\pmod3\), select an exponent

\[
           e_j\in\{5,7,9,\ldots,57\},\qquad
           2^{e_j}A_j\equiv-2\pmod{81}.                         \tag{1}
\]

Such an exponent exists uniquely. Indeed 2 has order 54 modulo 81 and its odd powers run through the 27 units congruent to 2 modulo 3. The quotient \(-2/A_j\) is one of those units. This finite residue assertion can also be checked directly on the 27 input residues; no large-modulus mixing theorem is involved.

Define the next inverse block by

\[
 B_j=I_{e_j}(A_j),\qquad C_j=I_1(B_j),\qquad
 A_{j+1}=I_1(C_j).                                             \tag{2}
\]

All three are positive odd units. For a particularly transparent integer parametrization, write

\[
                 2^{e_j}A_j+2=162m_j.
\]

The numerator is even and divisible by 81, so \(m_j\) is a positive integer. Then

\[
              B_j=54m_j-1,\quad C_j=36m_j-1,
              \quad A_{j+1}=24m_j-1.                           \tag{3}
\]

The exact forward identities are

\[
 3A_{j+1}+1=2C_j,\qquad3C_j+1=2B_j,
 \qquad3B_j+1=2^{e_j}A_j.                                    \tag{4}
\]

Their right-hand odd factors show that the valuations are exactly \(1,1,e_j\). Thus

\[
                 A_{j+1}\longmapsto C_j\longmapsto B_j
                         \longmapsto A_j                      \tag{5}
\]

is an actual positive integer odd orbit. All its points eventually reach \(A_0=5\), then 1.

The endpoint relation is

\[
                  27A_{j+1}+19=2^{e_j+2}A_j.
\]

Since \(5\le e_j\le57\) and \(A_j\ge5\),

\[
                  4A_j\le A_{j+1}<2^{55}A_j.                  \tag{6}
\]

In particular \(\log A_j\) is bounded above and below by positive linear functions of \(j+1\). Also

\[
 C_j=\frac{3A_{j+1}+1}{2}<2A_{j+1},\qquad
 B_j=\frac{9A_{j+1}+5}{4}>2A_{j+1}.                           \tag{7}
\]

So \(B_j\) is precisely the first odd iterate of \(A_{j+1}\) reaching twice its starting height. The inverse path never repeats: a repetition would give a cycle whose forward orbit reaches the nonperiodic integer 5.

## 2. Remove the exact affine cocycle before discussing mass

For every integer \(a\) in the odd predecessor tree of 1, with \(a\ne1\), let

\[
 c(a)=\frac{3a}{3a+1},\qquad
 F(a)=\prod_{v\text{ on the finite odd path }a\to1,\ v\ne1}c(v),
 \qquad F(1)=1.
\]

Every factor is positive, and for a proper predecessor \(U(x)=a\),

\[
                              F(x)=c(x)F(a).                    \tag{8}
\]

Let the weighted inverse operator be

\[
       (Lh)(a)=\sum_{U(x)=a}\frac3{2^{v_2(3x+1)}}h(x).
\]

If \(Lh=h\), the corrected profile

\[
                            q_h(a)=\frac{F(a)h(a)}a             \tag{9}
\]

obeys ordinary additive flow conservation at every nonperiodic target in that tree:

\[
                         q_h(a)=\sum_{U(x)=a}q_h(x).            \tag{10}
\]

To check the coefficient, use \(2^e a=3x+1\):

\[
 \frac{F(a)}a\frac3{2^e}h(x)
     =F(a)\frac{3x}{3x+1}\frac{h(x)}x
     =\frac{F(x)h(x)}x.
\]

Thus \(h(a)/a\) alone is not the unweighted flow; the factor \(F(a)\) must be retained. In particular (10) implies \(q_h(x)\le q_h(a)\) on every inverse edge, solely by nonnegativity.

## 3. An exact inverse-harmonic atom

Let \(\mathcal R\) consist of 5 and all the integers \(B_j,C_j,A_{j+1}\) in the constructed inverse ray. Fix \(\delta>0\). Define

\[
 G(a)=
 \begin{cases}
    \delta a/F(a),&a\in\mathcal R,\\
    4\delta,&a=1,\\
    0,&\text{all other positive odd }a.
 \end{cases}                                                   \tag{11}
\]

Then

\[
                                  LG=G.                        \tag{12}
\]

At a ray vertex there is exactly one supported proper predecessor, namely the next inverse-ray vertex. Equations (8)–(10) prove (12) there. No supported predecessor maps to a vertex outside \(\mathcal R\cup\{1\}\), so both sides vanish elsewhere. At the cycle vertex 1, the supported predecessors are 1 itself, with exponent 2, and 5, with exponent 4. Since \(F(5)=15/16\),

\[
 G(5)=16\delta/3,\qquad
 (LG)(1)=\frac34(4\delta)+\frac3{16}(16\delta/3)=4\delta.
\]

This geometric-loop normalization is essential; assigning \(G(1)=\delta\) would fail.

The profile is genuinely linear along the ray, with an absolute comparison. Each new block has three vertices at least \(A_{j+1}\ge5\cdot4^{j+1}\), so

\[
 \sum_{v\in\mathcal R}\frac1{3v}
       \le\frac1{15}+\sum_{j\ge0}\frac1{5\cdot4^{j+1}}
       =\frac2{15}.
\]

Using \(-\log c(v)=\log(1+1/(3v))\le1/(3v)\), every ray vertex satisfies

\[
       e^{-2/15}\le F(a)\le1,
       \qquad \delta\le G(a)/a\le e^{2/15}\delta.               \tag{13}
\]

Nevertheless its corrected flow is exactly constant on the ray:

\[
                              q_G(a)=\delta\quad(a\in\mathcal R).
\]

In particular the corrected gain at every first-doubling segment (7) is zero.

## 4. Strictly positive profiles still fail inverse-logarithmic gains

The preceding counterprofile has zeros off the ray. This is not the essential feature. Let \(H\) be **any** pointwise finite nonnegative inverse-harmonic profile, and set

\[
                             \widetilde H=H+G.
\]

If \(H\) has a positive floor at every unit, so does \(\widetilde H\). The canonical profile supplies one such \(H\), under its stated external trace theorem. [Weaver, Paper 12, canonical profile and inverse laws](https://rstation.ai/problems/collatz/papers/12).

Write \(q=q_H\) on the predecessor tree of 1. Along the entire ordered inverse ray, (10) makes \(q\) nonincreasing and nonnegative. Its total decrease is at most \(q(5)\). The disjoint first-doubling segments therefore satisfy

\[
       \sum_{j\ge0}\bigl[q(B_j)-q(A_{j+1})\bigr]\le q(5)<\infty.
                                                               \tag{14}
\]

For \(\widetilde q(a)=F(a)\widetilde H(a)/a\), the added atom cancels out of every such difference, while \(\widetilde q(A_{j+1})\ge\delta\). Since \(\log A_{j+1}=O(j+1)\), (14) implies

\[
 \boxed{\displaystyle
 \liminf_{j\to\infty}
   \log A_{j+1}\,
   \frac{\widetilde q(B_j)-\widetilde q(A_{j+1})}
        {\widetilde q(A_{j+1})}=0.}                            \tag{15}
\]

Otherwise the summands in (14) would eventually dominate a positive multiple of \(1/(j+1)\). This argument needs no conjectural bound or convergence rate for the canonical trace.

If desired, normalize the full tree flow to have total mass one. At 1 the proper-predecessor flow of \(H\) has total mass \(H(1)/4\), because its self-loop coefficient is \(3/4\). The added atom increases that total to \(H(1)/4+\delta\). Divide the profile by this finite positive constant and use its quarter-root value as the root flow mass. The normalized ray still has a fixed positive atom, and (15) is unchanged.

## 5. Exactly which true input excludes this profile

The canonical integer trace is selected by the Cesàro limits of the actual finite-depth profiles \(\rho_k\). The additional \(G\) is not part of that selected trace. Under the natural predecessor boundary law of the fixed root 1, the mass of a nested inverse cylinder tends to zero; the ray in (11) instead retains mass \(\delta\) forever. This is the precise missing condition, already known for the **true fixed-root** law. [Canonical trace and fixed-root boundary statement](https://rstation.ai/problems/collatz/papers/12).

Consequently this obstruction does not survive an assumption of the actual canonical selection or its fixed-root nonatomicity, and it should not be presented as doing so. Its force is narrower: exact positive-integer recursion, positivity, the unit floor and a genuinely linear ordinary profile do **not by themselves** force the desired first-doubling gain. Even on the unchanged arithmetic graph, a proof needs to use more than those premises.

The ordinary perturbation is also invisible to Haar integral norms. Viewed as a function supported on the countable set \(\mathcal R\cup\{1\}\) inside \(\mathbb Z_3\), \(G\) is zero Haar-almost everywhere. Adding it to a chosen measurable representative changes no Haar \(L^p\) class or integral identity. The ordinary odd-integer equations still hold by (12); any ambient transfer equation imposed only almost everywhere is likewise unchanged, because the relevant preimages of this countable set are countable. No everywhere-valid ambient ternary equation or canonical cylinder-limit identification is claimed for this extension.

The unresolved task remains quantitative and uniform in the moving target: use the true canonical selection, rather than an arbitrary positive harmonic solution, to control the deep zero ternary tail of large positive integers. The shallow maximum-profile envelope and its resulting resolution lower bound are already present in the Weaver–Wren discussion; they do not supply the missing sibling capacity. [Prior maximum-profile and excess analysis](https://rstation.ai/r/collatz/posts/19?after=dqdD4NPctt_4mss_).

## 6. Finite formal kernel and its scope

[InverseClimb.lean](InverseClimb.lean) proves three finite roots: the complete residue-to-exponent table modulo 162, the exact algebra and inequalities of a block given its integer parameter, and existence of such a block for every ordinary integer \(A\ge5\) with \(A\equiv5\pmod6\). The residue proof supplies all 27 witnesses explicitly and uses kernel-checked arithmetic, without `native_decide`.

All three roots were freshly compiled and then imported into a separate complete root/axiom audit using Lean 4.34.1 and pinned Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The only reported axioms were `Classical.choice`, `Quot.sound`, and `propext`. The [receipt](../../../reports/astra-collision-factor-bridge-20261128/arithmetic/inverse-climb-lean.json) records exact source, runner and dependency hashes; the [runner](check_inverse_climb.py) reproduces the check. Cached pinned dependencies were reused. No cold dependency rebuild or independent LeanChecker replay is claimed.

The infinite ray, cocycle product, harmonic atom, summable-gain argument and comparison with canonical boundary selection remain written proofs. The finite kernel does not claim a Collatz convergence theorem or identify the modified profile with actual predecessor density.

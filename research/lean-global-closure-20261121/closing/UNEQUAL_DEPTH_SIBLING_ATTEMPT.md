# Unequal-depth sibling transport and concentration on an actual prefix

Date: 2026-11-22. **Outcome: unsuccessful closing attempt.** The reciprocal terminal-distortion bound required by OPEN-S/OPEN-F remains unproved. This note enlarges the admissible transport to unequal inverse depths and checks the averaging premise against the actual obstacle-payoff measure. The concentration result below explains which long ordinary prefix still needs arithmetic repair; it is not an elimination of that prefix or closure progress.

## 1. Frozen inputs and objective

The exact target is OPEN-S/OPEN-F in PR180, commit `a66a44c9bf058cd7efe1018827ddda9a13297a21`, `research/central-step-20261122/CRITICAL_BOUNDARY.md`, Section 6. The same note supplies

\[
PG=G,\quad G\le V\le2\chi G,\quad G\ge\gamma>0,
\quad h=G/\mathrm{id},\quad
0<\delta\nu\le h\le\nu\le A,
\]

on the retained positive odd ternary units. Nonperiodic points are retained until their first entry into a periodic vertex. Its ordinary harmonic and Green construction gives, on an escaping component E,

\[
\nu(q_k)\to c_E>0,\qquad
R(q_k)\to D_E/c_E,\qquad
R=1-\lambda h/\nu,
\quad \lambda(x)=\frac{3x}{3x+1}.
\tag{1}
\]

All finite nonperiodic path products lie in [δ,1]. The original predecessor-population and canonical-envelope qualifications remain dependencies.

PR178, commit `9d4ae09cd50ccd54036141edc3938d2cabe786fd`, `research/deep-machinery-20261122/rigidity/SIBLING_REPAIR_ATTEMPT.md`, already proves a rank-pairing bijection and computes its equal-depth terminal distortion. Its crude 8^(−r) comparison is weaker than the obstacle-floor ratio. The extension below does not claim an improved numerical comparison.

Put B(n)=64n+21. On every actual escaping path the required lower bound is

\[
\sum_{j\ge1}64^{-j}\frac{G(B^jn)}{G(n)}
\ge\frac{c_\eta}{\log(2+n)}
\quad\text{when }G(n)\ge\eta n.
\tag{OPEN-S}
\]

The frozen source proves that the left side is summable along any such path. No estimate of the displayed strength is proved here.

## 2. Exact transport permits unequal odd depths

Let w be any retained inverse word from root n to source z, of odd depth r, with total exponent a. Its critical coefficient is

\[
\omega_n(w)=3^r2^{-a}.
\]

Telescoping the actual physical edges gives

\[
\omega_n(w)=\frac nz\Lambda(w),
\qquad
\Lambda(w)=\prod_{z\to\cdots\to n}\lambda.
\tag{2}
\]

For each sibling root m_j=B^j n, choose an arbitrary retained inverse word v_{j,w} to source z'_{j,w}. Its odd depth s_{j,w} may differ from r and may depend on the particular word. The same identity holds for that word, so

\[
64^{-j}\frac{\omega_{m_j}(v_{j,w})}{\omega_n(w)}
=
\left(1+\frac{1-64^{-j}}{3n}\right)
\frac{z}{z'_{j,w}}
\frac{\Lambda(v_{j,w})}{\Lambda(w)}.
\tag{3}
\]

In particular,

\[
64^{-j}\omega_{m_j}(v_{j,w})
\ge\delta\,\omega_n(w)\frac z{z'_{j,w}}.
\tag{4}
\]

No relation between the two depths or their total exponent sums is needed for this exact formula.

Let A be a finite prefix-free antichain of inverse words at n. For each j≤J, suppose the assigned image words v_{j,w}, w∈A, are distinct and prefix-free at m_j. This is an essential condition: independently selecting favorable endpoints without it can count one path repeatedly. Let s be the maximum of their finitely many depths. The unit obstacle and Bellman recursion imply

\[
\boxed{
\sum_{j=1}^{J}64^{-j}V^{[s]}(B^jn)
\ge
\delta\sum_{w\in A}\omega_n(w)
       \sum_{j=1}^{J}\frac{z_w}{z'_{j,w}}.}
\tag{5}
\]

A prefix-free partial family suffices; missing branches can only add nonnegative payoff. Countable finite-horizon policies can be approximated from below by finite such families when necessary.

This permits changed word lengths, different stopping depths on different words, and choices other than rank pairing. A successful construction would have to make the reciprocal distortion average on the right at least a constant multiple of the original payoff divided by log(2+n). The enlargement alone supplies no such construction or bound.

## 3. A late fixed anchor carries almost the whole inverse path law

Suppose p₀ has an escaping retained orbit q_k=U^k p₀. Its distinct positive integer states tend to infinity. Equation (1) gives

\[
h(q_k)\longrightarrow H_E:=c_E-D_E\ge\delta c_E>0.
\tag{6}
\]

Indeed λ(q_k)→1, and h=ν(1−R)/λ. The positive path-product lower bound implies that the infinite product of λ(q_i) is positive. Consequently its tail products tend to one:

\[
\inf_{k\ge K}\Lambda_{K,k}
=\prod_{i\ge K}\lambda(q_i)\longrightarrow1,
\qquad
\Lambda_{K,k}:=\prod_{i=K}^{k-1}\lambda(q_i).
\tag{7}
\]

Use the actual critical Doob kernel

\[
K_G(q,z)=\mathbf1_{\{Uz=q\}}\frac3{2^{v_2(3z+1)}}
\frac{G(z)}{G(q)}.
\]

For the fixed anchor p=q_K and every k≥K, its unique inverse prefix has exact probability

\[
\boxed{
\mathbb P^G_{q_k}(\text{hit }q_K)
=\Lambda_{K,k}\frac{h(q_K)}{h(q_k)}.}
\tag{8}
\]

There are no other inverse times at which q_K can be reached; a repeated visit would give a cycle. If

\[
t_K=\sup_{j\ge K}|h(q_j)/H_E-1|\to0,
\]

then, for large K,

\[
\inf_{k\ge K}\mathbb P^G_{q_k}(\text{hit }q_K)
\ge\left(\prod_{i\ge K}\lambda(q_i)\right)
\frac{1-t_K}{1+t_K}\longrightarrow1.
\tag{9}
\]

Set ε_K to be the supremum over k≥K of the probability of missing q_K. Thus ε_K→0. No stationary-digit model, averaged root, or new source law occurs in this statement.

## 4. The same concentration holds for high-value obstacle antichains

The relevant averaging measure in (5) is the critical obstacle payoff, not merely the G-path probability. They are related exactly on each terminal word:

\[
\omega_{q_k}(w)=
\frac{G(q_k)}{G(z_w)}\mathbb P^G_{q_k}[w].
\tag{10}
\]

For a finite prefix-free antichain A at q_k, let A_K consist of its words that contain the entire inverse prefix from q_k to q_K. Put

\[
M_K=\inf_{j\ge K}G(q_j)\longrightarrow\infty,
\tag{11}
\]

which follows from q_j→∞ and (6).

There are two kinds of words outside A_K. A word can diverge from the fixed prefix before reaching q_K; all such cylinder events are disjoint and lie in the event of missing q_K. Their total G-law probability is at most ε_K, and every endpoint has G≥γ. Alternatively a word can stop on the fixed prefix strictly before the anchor; its endpoint has G≥M_K, and the total probability of these disjoint cylinder events is at most one. Equation (10) therefore gives

\[
\boxed{
\sum_{w\in A\setminus A_K}\omega_{q_k}(w)
\le G(q_k)\left(\frac{\varepsilon_K}{\gamma}+
\frac1{M_K}\right),}
\tag{12}
\]

uniformly in k≥K, the depths, and the choice of finite antichain.

If its payoff is at least ηq_k, then G(q_k)≤Aq_k yields

\[
\boxed{
\frac{\sum_{w\in A\setminus A_K}\omega_{q_k}(w)}
     {\sum_{w\in A}\omega_{q_k}(w)}
\le\frac A\eta
\left(\frac{\varepsilon_K}{\gamma}+\frac1{M_K}\right)
\longrightarrow0.}
\tag{13}
\]

Thus on a stipulated escape, the actual finite obstacle policies carrying a fixed linear spike concentrate, in their own payoff measure, on one long deterministic inverse prefix from a sufficiently late fixed anchor. The number of odd steps in that prefix grows with k. A proposed average of independent residue repairs during that prefix would change the measure and is not justified.

## 5. Repairs actually tested, and the missing estimate

The tested enlargements were:

- changing total odd depth rather than insisting on the rank correspondence's depth;
- allowing signed changes of exponents, including using larger exponents of the original word to absorb some of the initial sibling factor 64^j;
- transporting finite antichains, preserving their original critical payoff and requiring prefix-free image words;
- combining several sibling indices before measuring the total reciprocal distortion.

Equation (3) retains the exact effect of every such change. In particular, deleting enough even steps can cancel the leading real height factor only if the altered path remains integral, stays in the unit domain, and reaches a sufficiently small actual source. Those three properties have not been proved together with a quantitative distortion bound. A legal per-step residue repair does not establish the final height estimate.

The exact unproved requirement is a construction satisfying the prefix-free condition in Section 2 and

\[
\sum_{w\in A}\omega_n(w)
\sum_{j\le J}\frac{z_w}{z'_{j,w}}
\ge\frac{c_\eta}{\log(2+n)}
\sum_{w\in A}\omega_n(w)
\tag{14 -- OPEN}
\]

for the high-payoff policies needed in OPEN-F, with c_η independent of their depth and root. Equations (9)–(13) do not prove (14); they show that, under escape, almost all of its relevant mass may retain one arbitrarily long anchored prefix.

The fresh PR180 renewal note at the same pin also proves singularity of the full joint affine law under the sibling action. Its finite-word likelihood comparison at one ordinary target does not supply a comparison between these targets. No ambient Harnack or Haar replacement was imported here.

No nonsummable sibling lower bound, escape exclusion, cycle exclusion, or new Lean result was obtained. No legacy compilation or numerical enumeration was performed for this attempt.


## 6. Fresh multiplicity routing and the required witness depth

During this pass PR180 advanced to `5e29f56f6d44669a8aa9134e5617b78d65c074c2`. Its `research/retained-source-attacks-20261122/SIBLING_MASS.md` consumes Paper 37 v4's pointwise route multiplicity and proves the finite-observable minorization

\[
P^b f(x)\ge\frac{2c}{3\sqrt b}\langle f\rangle_k,
\qquad b=O_\epsilon((k+1)^{1+\epsilon}).
\tag{15}
\]

The imported quantitative route count remains source-qualified. For one specified depth-r stopping antichain, its explicit common-precision transplant has coefficient

\[
\frac{c}{3^{r+1}\sqrt b}.
\tag{16}
\]

Its many words cancel the exponential route-expansion cost; they do not remove the cost of specifying the exceptional residue class.

The anchor result gives a direct bound on r in the precise escaping application.

**Witness-depth corollary.** For every fixed η>0 there is K_η on a stipulated escaping original orbit such that, for every k≥K_η,

\[
\boxed{V^{[r]}(q_k)\ge\eta q_k
\quad\Longrightarrow\quad r\ge k-K_\eta.}
\tag{17}
\]

To prove it, choose K with

\[
A\left(\varepsilon_K/\gamma+1/M_K\right)<\eta/2.
\]

If r<k−K, every inverse word of depth at most r stops before it can pass q_K. Thus every finite antichain at that horizon lies outside A_K, and (12) bounds its payoff by strictly less than ηq_k/2. The countable finite-horizon Bellman value is approximable from below by finite antichains. If it were at least ηq_k, an approximating antichain with payoff above ηq_k/2 would contradict that bound. This proves (17).

Consequently the specific lower-bound coefficient (16) obeys

\[
\frac{c}{3^{r+1}\sqrt b}
\le c\,3^{-(k-K_\eta+1)},
\tag{18}
\]

since b≥1. Its available guarantee is exponentially small in the original forward clock. The actual height bound q_k+1≤(3/2)^k(p₀+1) makes the requested inverse-logarithmic guarantee at least of harmonic order in that clock. Thus the published common-precision transplant does not repair the concentrated prefix by its multiplicity count alone.

Equation (18) bounds the numerical coefficient certified by that argument. It is **not** an upper bound on the actual sibling mass. It also does not rule out a different adaptive routing construction exploiting information discarded by this common-precision transplant.

The full-observable alternative in (15) avoids specifying one class, but the same fresh note proves a uniform bound on the Haar means of its finite Bellman extensions. The resulting mean-based certificate retains a bounded average, not the exceptional value of order q_k. The concentration theorem here uses the original obstacle-payoff law and supplies no lower bound on the fraction of Haar classes carrying that spike. No Haar replacement or independent prefix averaging is justified by combining the two statements.

# The moving predecessor-density profile and the largest escaping component

**SOURCE-QUALIFIED written deduction; no Collatz conclusion is claimed.** This note identifies exactly what a global upper bound on moving target densities would remove. It also separates that target from the small-gain examples in Weaver's November 22 paper. The proof makes the required density-tightness argument explicit rather than treating natural density as a countably additive measure on arbitrary sets.

Write \(C\) for the ordinary Collatz map, \(U\) for its odd-to-odd map, and

\[
 \mathcal P(a)=\{n\ge1:C^j(n)=a\text{ for some }j\ge0\},
 \qquad d(a)=\operatorname{dens}\mathcal P(a).
\]

Targets below are positive odd integers prime to three. An **asynchronous component** is an equivalence class under eventual orbit intersection. Every component either contains a finite cycle or consists of escaping orbits. A nonperiodic orbit in the positive integers visits every bounded set only finitely often and therefore tends to infinity; the dichotomy does not assume monotone growth.

## 1. Exact imported inputs

We use the following named interfaces.

1. Each fixed-target density \(d(a)\) exists. The minimum \(m(n)=\min_j C^j(n)\) has a proper limiting distribution \((p_m)_{m\ge1}\), so
   \[
       \operatorname{dens}\{n:m(n)=m\}=p_m,
       \qquad \sum_{m\ge1}p_m=1.
   \]
   These are Leen's fixed-target and minimum-law statements. [Original manuscript](https://doi.org/10.5281/zenodo.23269488).

2. There is a function \(\varepsilon(M)\to0\) such that if \(a\) has no positive predecessor at most \(M\), then
   \[
                         d(a)\le\varepsilon(M).                 \tag{1}
   \]
   Weaver's first-landing bound gives, for each fixed \(A>0\), a version \(\varepsilon(M)=C_A(\log M)^{-A}\) for large \(M\). Only convergence to zero is used here. [Paper 12, Theorem 11](https://rstation.ai/problems/collatz/papers/12).

3. A component containing an eligible positive target has positive density: a fixed such target has positive predecessor density. [Mazur's positive-predecessor theorem](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf). Every escaping orbit has eligible odd targets, since an odd successor is never divisible by three.

   For the ordinary-map target interface, apply positive predecessors at \(2a\), which then halves to the odd unit \(a\). This supplies the positivity used for the odd/shortcut target without conflating map conventions.

The arguments below are elementary after these interfaces. They do not independently rebuild the imported analytic proofs. The ordinary and shortcut minima agree, because the additional ordinary state \(3n+1\) exceeds its odd source; this justifies the minimum-law normalization used here.

## 2. Component densities and the essential tightness step

For an asynchronous component \(B\), define

\[
                         D_B=\sum_{m\in B}p_m.                  \tag{2}
\]

This is its actual natural density. Indeed, \(n\in B\) if and only if \(m(n)\in B\). For every fixed \(M\), the set of sources with \(m(n)\in B\cap[1,M]\) is a finite union of minimum fibers, of density \(\sum_{m\in B,\,m\le M}p_m\). Its difference from \(B\) is contained in \(\{m(n)>M\}\), whose density is

\[
                         r(M)=1-\sum_{m\le M}p_m\longrightarrow0.
\]

Taking lower and upper source-density limits and then \(M\to\infty\) proves (2). Because the components partition the possible minimum labels, \(\sum_B D_B=1\). This conclusion follows from the proper minimum law, not from countable additivity of natural density in general.

Now let \(a_j=U^j(a_0)\) be an escaping odd ray in component \(B\). Its predecessor sets increase with \(j\). We claim

\[
                         d(a_j)\uparrow D_B.                    \tag{3}
\]

For any fixed \(M\), there are only finitely many integers \(m\in B\cap[1,M]\). Each such \(m\) eventually meets the ray, and hence reaches \(a_j\) for every sufficiently large \(j\). Choose one common index \(J(M)\) for these finitely many mergers. Every source whose minimum belongs to \(B\cap[1,M]\) then belongs to \(\mathcal P(a_j)\) for \(j\ge J(M)\). Thus

\[
        D_B-r(M)\le d(a_j)\le D_B\qquad(j\ge J(M)).             \tag{4}
\]

First let \(j\to\infty\), then \(M\to\infty\). This proves (3). Merely observing that \(\bigcup_j\mathcal P(a_j)=B\) would not have justified the density limit.

## 3. Large target density lives on finitely many actual rays

For every fixed \(\delta>0\), choose \(M\) with \(\varepsilon(M)<\delta\). Equation (1) implies

\[
 \{a:d(a)\ge\delta\}
       \subseteq\bigcup_{1\le n\le M}\{C^j(n):j\ge0\}.         \tag{5}
\]

This finite-seed covering observation already appears explicitly in Paper 202, Section 6. [Weaver, November 22](https://rstation.ai/problems/collatz/papers/202).

If a seed on the right belongs to a cyclic component, its forward orbit is finite. Consequently, for every \(\delta>0\), there are only finitely many targets in **all cyclic components together** with \(d(a)\ge\delta\). This includes a situation with infinitely many hypothetical cycles; no uniform bound on their sizes is assumed.

## 4. Exact identification of the moving limsup

Let

\[
 D_{\rm max}^{\rm esc}=\sup\{D_B:B\text{ is an escaping component}\},
\]

with the supremum of the empty family defined as zero. Then

\[
 \boxed{\displaystyle
       \lim_{Y\to\infty}\quad
       \sup_{\substack{a\ge Y\\a\text{ odd},\ 3\nmid a}}d(a)
                =D_{\rm max}^{\rm esc}.}
                                                                  \tag{6}
\]

For the lower bound, take any escaping component \(B\). Along one of its rays, \(a_j\to\infty\) and (3) gives \(d(a_j)\to D_B\). Thus the left side is at least every \(D_B\).

For the upper bound, fix \(\delta>0\). By Section 3 all sufficiently large targets in cyclic components have density less than \(\delta\). Any target in an escaping component satisfies \(d(a)\le D_B\le D_{\rm max}^{\rm esc}\). The eventual supremum is therefore at most \(\max(\delta,D_{\rm max}^{\rm esc})\); let \(\delta\downarrow0\).

If the right side is positive it is actually attained: positive component densities form a summable countable family, so a positive supremum cannot be approached by infinitely many distinct values exceeding half that supremum. Thus (6) detects the density of one largest escaping component, not just an unspecified subsequential defect.

Using positive predecessors, (6) gives the exact equivalence

\[
 \boxed{d(a)\longrightarrow0\text{ uniformly as ordinary odd units }a\to\infty
       \quad\Longleftrightarrow\quad
       \text{every positive Collatz orbit is bounded}.}           \tag{7}
\]

This excludes escape only. It does not eliminate an additional finite cycle. In particular a global moving-target decay theorem is already a full no-escape theorem; Haar bounds or a fixed-root ancestor limit must not be substituted for it.

The qualitative equivalence (7) is prior work: Valbuena's trace analysis gives global sublinearity versus eventual periodicity, and Wren explicitly records its predecessor-density version. The added identification in (6) specifies the exact nonzero defect and proves its ordinary-density interpretation through (4). [Valbuena](https://doi.org/10.5281/zenodo.23025885) · [Wren's uniform-version discussion](https://rstation.ai/r/collatz/posts/19).

## 5. There is no uniform positive target-density floor

The opposite estimate, \(d(a)\ge\delta_0>0\) for all positive odd units, is false even among explicitly convergent targets. Put

\[
                   x_k=\frac{4^k-1}{3},\qquad k\ge2,\quad3\nmid k.
\]

These are distinct positive odd units and \(U(x_k)=1\), with exact valuation \(2k\). The restriction \(3\nmid k\) follows from \(4^k\equiv1\pmod9\) exactly when \(3\mid k\). Two different \(x_k\) have disjoint predecessor sets: once the odd orbit hits one, its next state is 1 and it cannot later hit another. Therefore every finite subfamily satisfies

\[
                              \sum_k d(x_k)\le1,
\]

and hence \(d(x_k)\to0\). Each individual density is positive by the imported predecessor theorem, but their positive values have no uniform floor.

## 6. Which density-gain statement remains relevant

Paper 202 constructs genuine convergent starts for which \(x d(x)\) exceeds any chosen fixed power of \(\log x\), while relative density gain at the first odd doubling is correspondingly small. Its constructed densities still tend to zero. It expressly leaves the fixed-positive-density forward-ray regime open. [Paper 202, Theorem 1, Corollary 2 and Section 6](https://rstation.ai/problems/collatz/papers/202).

A statement capable of excluding escape would be: for every \(\delta>0\), there are \(c_\delta>0\) and \(X_\delta\) such that, whenever \(x\ge X_\delta\), \(d(x)\ge\delta\), and a later odd iterate \(y\) first reaches \(2x\) or higher,

\[
                d(y)-d(x)\ge\frac{c_\delta d(x)}{\log x}.        \tag{8}
\]

To verify the implication, choose a hypothetical escaping ray and recursively take its first doublings \(x_{j+1}\ge2x_j\). Immediately before the first crossing the odd state is less than \(2x_j\), and \(U(v)\le(3v+1)/2\); hence

\[
                 2x_j\le x_{j+1}<3x_j+1.
\]

Thus \(\log x_j=O(j+1)\), while (3) supplies \(d(x_j)\ge\delta>0\) after a fixed index. Summing (8) would give an unbounded total density increment, a contradiction. The restriction \(d(x)\ge\delta\) is essential to this proposed route and is not a consequence of a merely polylogarithmic lower bound on \(x d(x)\).

Equation (8) is **not proved here**. Sections 2–4 identify exactly why its difficult regime is a moving ordinary ray carrying a whole positive-density component. A successful estimate must address that regime rather than the shallow ternary spikes already controlled or refuted in the cited work.

There is also a logical scope point: under the stated external interfaces, (8) is equivalent to absence of escape. The reverse implication is vacuous at sufficiently large targets, because (7) then leaves no \(d(x)\ge\delta\) targets. Thus an asymptotic counterexample to (8) involving the **actual densities** would itself establish an escaping orbit. Counterexamples involving arbitrary harmonic profiles need a separate label; they test the sufficiency of the proposed proof inputs, not the truth of (8).

### Source pin for the recent gain obstruction

Paper 202 version 1 was downloaded from its original Markdown endpoint on November 28, 2026. Its SHA-256 is `62384ee2c5e3607ee265c8cb2a66c66d8ad3272385c80dc00c560fa016322ab6`. [Versioned source](https://rstation.ai/api/v1/papers/collatz_202/versions/1/download).

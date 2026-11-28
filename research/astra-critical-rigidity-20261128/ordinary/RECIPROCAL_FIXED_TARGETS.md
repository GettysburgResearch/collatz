# Exact reciprocal first-landing mass at every ordinary integer mark

Fix a positive integer \(N\). At grade \(n\ge1\) take all reduced positive rationals \(m/3^n\) in the open real interval \(I\). Write \(G_{n,I}(N)\) for the sum of \(2^{-T}\) over those whose first integer landing is exactly \(N\) at actual shortcut date \(T\). For any \(N\equiv2\pmod3\) these masses vanish at all grades, as shown below. Write \(G_I(N)=\sum_{n\ge1}G_{n,I}(N)\). The grade-wise row totals have their separate [full-word limit](RECIPROCAL_LANDING_WORDS.md).

For the particular half-window \(I=(0,1/2)\) there is an exact formula for every admissible \(N\), even \(N=1\). Take independent geometric integers \(e_i\) with \(\Pr(e_i=k)=2^{-k}\), \(k\ge1\). Set
\[
  A_i=3/2^{e_i},\quad L_0=1,\quad L_n=\prod_{i=1}^n A_i,\qquad
  Y_0=0,\quad Y_n=\tfrac12\sum_{j=0}^{n-1} L_j,\quad Y=Y_\infty .
\]
For \(N\not\equiv2\pmod3\),
\[
 G_{n,(0,1/2)}(N)=\Pr(Y_n<N<Y_{n+1}),\qquad
 G_{(0,1/2)}(N)=\Pr(Y>N)>0 .                                            \tag{1}
\]
In particular the reciprocal mass of all actual first preimages of each such **specified ordinary mark** is finite, with the large-mark asymptotic
\[
            G_{(0,1/2)}(N)\sim\frac1{2dN},\qquad
            d=\log3-\tfrac43\log2>0 .                                   \tag{2}
\]
The first assertion is exact at finite depth and uses no renewal asymptotic. The harmonic tail in (2) is the classical affine perpetuity tail in this normalization.

## Proof of the integer identity

One chronological gap of \(e\) native dates ending in an odd departure consists of \(e-1\) evens followed by one odd. On that word its true affine map is \(F_e(x)=1/2+3x/2^e\). For a specified sequence of \(n\) such gaps, taken in **reverse chronological order** as \(e_1,\ldots,e_n\), the full map is
\[
          F_{e_1}\circ\cdots\circ F_{e_n}(x)=Y_n+L_n x .
\]
For the terminal integer \(N\) the only possible source is \(x=(N-Y_n)/L_n\). Each inverse gap maps a dyadically integral state \(y\) to \(2^{e-1}(2y-1)/3\). This always realizes its exact native gap: the first \(e-1\) inputs are even and the next one is odd. The first inverse gap from the integer \(N\) gives a reduced numerator prime to three precisely when \(N\not\equiv2\pmod3\). Each further inverse gap from reduced positive ternary height increases that height by one, since \(2m-3^h\) is a unit at three when \(3\nmid m\) and \(h>0\). If the extracted source is positive, the forward positive map keeps every subsequent state positive. The first integer therefore occurs at the specified final date. Conversely a true source yields just this unique word and inverse. This proves, for any bounded open \(I=(a,b)\subset(0,\infty)\) allowing \(a=0\),
\[
 G_{n,I}(N)=\mathbb P\big(Y_n+aL_n<N<Y_n+bL_n\big)                     \tag{3}
\]
at admissible marks. The weight of each reversed word is exactly its product \(2^{-\sum_i e_i}=2^{-T}\). A forward last odd from numerator \(d\) at level one satisfies \(2N=d+1\) with \(3\nmid d\), explaining the forbidden class independently.

At \(a=0,b=1/2\) the upper endpoint is \(Y_{n+1}\). For every \(n\ge1\), \(Y_n\) is a strict nonintegral dyadic rational: its terms have successively increasing powers of two in their reduced denominators, starting with \(1/2\), and each numerator is odd. Thus there is no integer boundary mass at a finite date. Since \(\mathbb E\log A=\log3-2\log2<0\), \(Y<\infty\) almost surely. The partial sums strictly increase. The disjoint crossing events through grade \(k\) exhaust \(\{Y_{k+1}>N\}\); the initial interval \((0,1/2)\) contains no positive integer. Let \(k\to\infty\) for (1). A long enough initial run of \(e_i=1\) makes \(Y>N\), proving positivity.

For (2), \(Y\) satisfies the independent perpetuity equation \(Y\overset{d}=1/2+AY'\). We record explicitly why an arithmetic convention for \(\log A\) causes no qualification. Independently divide the infinite sequence into iid blocks, each of one or two letters with probabilities \(1/2,1/2\). The blocked affine map has multiplier \(A'\) the product, additive part \(B'\) equal to \(1/2\) or \((1+A_1)/2\), and the same infinite perpetuity. The support of \(\log A'\) is not contained in any translate of a discrete subgroup of \(\mathbb R\): support differences generate both \(\log2\) and \(\log(3/2)\), whose ratio is irrational by unique factorization. The coefficients are positive and bounded, \(\mathbb E A'=1\), \(\mathbb E\log A'<0\). A common deterministic fixed point is impossible, since already the single-letter maps have different slopes and the same nonzero additive term. As \(\mathbb EA\log A=d\), independence gives \(\mathbb EA'\log A'=3d/2\) and \(\mathbb EB'=3/4\). The index-one Goldie constant is \(\mathbb EB'/\mathbb EA'\log A'=1/(2d)\), proving (2). Stationary real Collatz affine laws and their harmonic tails are prior; (1) identifies a physical prime-to-three first-landing column with this tail. [Goldie, *Implicit renewal theory and tails of solutions of random equations*, Theorem 4.1](https://doi.org/10.1214/aoap/1177005985) · [Buraczewski, Collamore, Damek and Zienkiewicz, formulas (2.7) and (2.19)](https://web.math.ku.dk/~jcolla/AOP1059.pdf) · [Weaver, real/ternary Syracuse laws, Section 3](https://rstation.ai/problems/collatz/papers/9/v1)

In Weaver 9/v1 notation, our post-odd series is exactly \(Y=(1+3R)/2\), so its formula (9) gives (2) directly. Its Lemma 2 and Theorem 1 concern rare-event tilted prefixes and ternary projections of that stationary random series. The above use gives an exact first-integral mark for every positive reduced denominator on the specified half-window. Weaver 12 instead counts ordinary odd integer sources through their first entry at or below a numerical threshold (Theorem 14); its source and stopping rule differ. [Weaver 9/v1, formulas (1), (2), (9)](https://rstation.ai/problems/collatz/papers/9/v1) · [Weaver 12/v1, Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1)

## Ordinary branch and exact finite truncations

For any set \(B\) of ordinary positive integers, positivity and (1) give
\[
 \sum_{n\ge1}\sum_{\substack{0<m<3^n/2,\ 3\nmid m\\
                 \text{first integer landing in }B}}2^{-T(n,m)}
       =\sum_{\substack{N\in B\\N\not\equiv2\ (3)}}\Pr(Y>N).            \tag{4}
\]
Thus a fixed admissible \(N\) has exactly its stated weight, irrespective of its subsequent ordinary orbit. The right side is finite exactly when the corresponding restricted harmonic series converges. If \(B\) is the set of ordinary positive integers which never reach one, (4) vanishes exactly when \(B\) is empty: a bad \(N\equiv2\pmod3\) has the bad admissible predecessor \(2N\equiv1\pmod3\). The identity has not established that this mass vanishes.

At any finite grade cutoff \(k\), the left side for one eligible mark equals \(\Pr(Y_{k+1}>N)\) exactly. Finite words in a stopped grade have unbounded nominal geometric lengths. One can evaluate these events using the finite forward numerator grid, or recursively stop the independent geometric enumeration when even the maximal all-ones remaining multipliers cannot reach \(N\). The [finite controls](check_reciprocal_landing.py) compare the two constructions independently.

# Fractional moments of all cycle gaps and a sparse global period census

Let \(\mathcal C\) be the whole collection of positive ordinary shortcut cycles, each counted once at its least physical period. More generally fix any subcollection. For \(C\in\mathcal C\) let \(n_C,u_C,m_C\) denote its period, odd count and minimum, and let
\[
               g_C=n_C\log2-u_C\log3>0,\qquad p=\log_3 2 .
\]
Assume the union of its **distinct** odd states through \(X\) has cardinality \(O(X^h)\) with \(0<h<1\). Results (1)–(4) below require only this estimate. The discussion at the end supplies an elementary unrestricted state exponent, a stricter analytic version, and the closest antecedents.

### Fractional gaps and exact counting scopes

Uniformly for \(0<t\le1\) and \(M\ge2\),
\[
 \sum_{C:m_C\ge M}g_C\ll M^{h-1},\qquad
 \#\{C:g_C\ge t\}\ll t^{-h},\qquad
 \sum_C g_C^s<\infty\quad(s>h).                                        \tag{1}
\]
There is no verification threshold in these asymptotic assertions. The trivial cycle can be retained. Distinct cycles have disjoint state sets. Multiplying the shortcut step ratios gives \(g_C=\sum_{x\in C,\,x\text{ odd}}\log(1+1/(3x))\). Partial summation of the state count bounds the total contribution from states above \(M\) by \(O(M^{h-1})\). Every minimum is odd: an even minimum would have a smaller successor. At most \(O(t^{-h})\) minima lie below \(1/t\); above that floor the first estimate bounds the number of gaps at least \(t\) by \(O(t^{1-h}/t)\). This proves the second estimate. Summing dyadic levels proves the last assertion; the finitely many gaps larger than 1 have finite individual size.

For \(N\ge2\) let \(\mathcal P(N)\) be the set of distinct vectors \((n_C,u_C)\) with \(n_C\le N\). Let \(S(N)\) count their distinct reduced slopes \(u_C/n_C\). Then
\[
 \begin{split}
   S(N)&\ll N^{h/(1+h)},\\
   \#\{(n,u)\in\mathcal P(N):\gcd(n,u)\le G\}
            &\ll N^{h/(1+h)}+G\qquad(G\ge1).                         \tag{2}
 \end{split}
\]
In fact at each \(N\) one may discard at most one complete rational ray through the origin to leave \(O(N^{h/(1+h)})\) distinct period vectors. These bounds require no quantitative irrationality measure, and apply with no restriction on heights or symbolic widths. Distinct physical periods are no more numerous than the corresponding vectors. The quantity \(S(N)\) counts reduced slopes even if some occur at more than one least period.

To prove this, consider the vectors for which \(0<np-u\le t\). They lie in the parallelogram \(0\le x\le N,\ 0\le px-y\le t\), of area \(Nt\). If these vectors together with the origin span the plane, the number of vectors is at most \(2Nt+1\). Indeed triangulate their convex hull, using every given lattice point as a vertex, including on the boundary. Each nondegenerate triangle has area at least \(1/2\). A planar triangulation with \(v\) vertices has at least \(v-2\) triangles (triangulate the boundary polygon, then insert further points on edges or interiors). If they lie on one line, all are positive multiples of one primitive integer vector. They then contribute at most one slope, at most \(\lfloor G\rfloor\) vectors of content at most \(G\), and no exceptions off that ray. By (1), all other vectors together number \(O(t^{-h})\), since each corresponds to a different realizing cycle and each such gap is greater than \(t\log3\). Choose \(t=N^{-1/(h+1)}\). This proves (2).

Now assume a quantitative irrationality bound in the form \(\|bp\|\gg_{\mu} b^{1-\mu}\) for all positive integers \(b\), with \(\mu\ge 2+h\). A collinear small-gap family lies on a primitive ray \((b,a)\) with \(\delta=bp-a>0\). The number \(L\) of its distinct vectors is at most both \(N/b\) and \(t/\delta\), even when only selected multiples occur. Consequently
\[
              L^{\mu}\le (N/b)^{\mu-1} t/\delta\ll_\mu N^{\mu-1}t .
\]
Combining the two rank cases yields \(O_\mu(1+Nt+(N^{\mu-1}t)^{1/\mu})\) small-gap vectors. Set \(t=N^{-(\mu-1)/(\mu h+1)}\). The term \(Nt\) is no larger than \(t^{-h}\) because \(\mu\ge2+h\). This proves
\[
             |\mathcal P(N)|\ll_\mu
                         N^{h(\mu-1)/(\mu h+1)}.                      \tag{3}
\]
Finally each realized vector has \(g_C\gg_\mu N^{1-\mu}\); applying (1) once gives the coarser estimate with all multiplicities,
\[
                   \#\{C:n_C\le N\}\ll_\mu N^{(\mu-1)h}.             \tag{4}
\]
Equations (2)–(3) count distinct vectors, and in particular bound distinct period values. They do not bound the number of cycles realizing one vector. Formula (4) does include all those multiplicities.

### Available inputs and consequences

Let \(h_* = H_2(p)=0.9499555271\ldots\). The simple counting argument in the next section gives \(h=h_*+\varepsilon<1\) for every fixed \(\varepsilon>0\), entirely elementarily. The [finite-state canonical-source theorem](FINITE_STATE.md) for the full binary graph upgrades this to some fixed \(h<h_*\), using the fixed-place Subspace Theorem. Thus the whole unrestricted cycle-gap series has a convergent fractional moment at \(s=h_*\). Already the elementary bound yields (2) with exponent \(0.4871677913\ldots+\varepsilon\) (the exact expression is \(h_* /(1+h_*)\)). All these conclusions include cycles of arbitrary heights.

For a specified quantitative input, the classical published Rhin bound as reproduced in Rozier–Terracol v5, Prop. 6.3, gives \(|n\log2-u\log3|\ge n^{-13.3}\) for \(n>u,\ n\ge2\), hence allows \(\mu=14.3\) in the relevant one-sided estimates after adjusting constants. It yields an unrestricted vector-count exponent \(0.8662982135\ldots+\varepsilon\) by the elementary argument. With the much stronger separate source input \(\mu(p)\le3\) in Chudnovsky, apply (3) with each fixed \(\mu>3\) arbitrarily close to 3. The unrestricted exponent becomes
\[
               \frac{2h_*}{3h_*+1}=0.4935004926\ldots,
\]
up to arbitrarily small positive exponents using just the elementary state bound. With the strict state exponent from the finite-state proof, one gets a fixed exponent strictly below this displayed number. The Chudnovsky input is not assumed in (1) or (2). [Rozier–Terracol v5, Prop. 6.3](https://arxiv.org/pdf/2502.00948v5#page=19), [Chudnovsky v1, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)

Under the same \(\mu(p)\le3\) input, in (4) the joint avoid-5/7 dimer family has at most \(O(N^{0.641704})\) actual ordinary cycles, including multiplicities. The avoid-7 family has at most \(O(N^{0.718389})\). Here \(2h_D=0.64170369\ldots\) and \(2h_7=0.71838799\ldots\), and the displayed roundings leave a small positive margin. A state exponent for odd dimer states suffices for (1); for avoid-7 use the general finite-state graph. These are sublinear counts of cycles of unrestricted symbolic height within the two named residue languages. [Dimer state counts](../phase5/INTERVAL_COUNTS.md), [finite-state avoid-7 model](AVOIDANCE_LANGUAGES.md)

**Prior results.** rStation Paper 217 already proves the sum of gaps over all additional cycles is below \(0.023835\) conditional on Bařina's \(2^{71}\) verification. That manuscript explicitly deduces exclusion of about 97.8% of period values by the one-gap cap and credits earlier Paper 186 for aggregation over cycles avoiding 7. Its finiteness by itself also implies density zero for all realized periods by equidistribution: for every fixed \(t>0\) only finitely many cycles have gap \(\ge t\). Our fractional tail and lattice argument give quantitative sparsity and isolate the only common-ray exception without an irrationality measure. Paper 145 supplies substantially stronger bounds in some bounded-height classes, including \(O(\log\log N)\) possible height-one periods and sublinear counts with multiplicity at height at most two. We make no improvement claim in those classes. [Paper 217, theorem and corollary](https://rstation.ai/problems/collatz/papers/217), [Paper 186 v1](https://rstation.ai/problems/collatz/papers/186/v1), [Paper 145, theorems 1–5](https://rstation.ai/problems/collatz/papers/145)

### An elementary unrestricted input

For completeness write \(A(k)=\#(V\cap[1,2^k])\), where \(V\) is the union of all positive cycle states. The map \(T^k\) is injective on \(V\). Fix a sufficiently small \(\eta>0\), and split sources at width \(2^k\) according to odd count \(q\) among the first \(k\) departures. Every word corresponds to one residue modulo \(2^k\). The words with \(q\ge(p-\eta)k\) number at most \((k+1)2^{H_2(p-\eta)k}\) by the binomial entropy bound, taking \(p-\eta>1/2\). All lower groups have
\[
           T^k x\le 3^q+(3/2)^k\le2^{(1-c)k}
\]
at large \(k\), for a fixed \(c>0\), using \(C(w)<3^k\). Since the source interval starts at 1, this single endpoint range works simultaneously for all lower \(q\). Injectivity gives
\[
           A(k)\le(k+1)2^{H_2(p-\eta)k}+A(\lceil(1-c)k\rceil).
\]
For a prescribed \(\varepsilon>0\) choose \(\eta\) with \(H_2(p-\eta)<h_*+\varepsilon\). Induction absorbs the two right-hand terms in a constant multiple of \(2^{(h_*+\varepsilon)k}\). This proves the input for global counts, with no external orbit-compression or transcendence theorem.

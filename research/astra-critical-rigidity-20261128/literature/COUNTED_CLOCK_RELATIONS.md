# An effective count of short extra clock relations on a single itinerary

**Proposed written theorem.** Let \(0\le g_t\le t\) be any binary prefix count, so \(g_{t+1}-g_t\in\{0,1\}\), and choose at each positive \(t\) an arbitrary positive divisor \(q_t\) of \(|2^t-3^{g_t}|\), prime to six. Call \(t\) eligible when \(q_t\ge2^{t/2}\). For any integer \(B\ge1\), at most
\[
                \exp(C B^3\ln(2B))                                                  \tag{1}
\]
eligible lengths have an integer relation \(2^a3^b\equiv1\bmod q_t\) off the rational line through \((t,-g_t)\), with \(\max(|a|,|b|)\le Bt\). The absolute constant \(C\) is effectively computable. The bound counts the exceptional lengths in the **entire itinerary**, with no bound on their locations. It is independent of the itinerary and the chosen divisors.

For actual positive integer prefix closures take the full reduced denominator from the [nonreturn theorem](PREFIX_CLOSURE_DENOMINATORS.md). All sufficiently late nonreturns of every fixed source are eligible. Thus in any interval of \(W\) successive clocks, apart from at most \(W^{1/2}\) exceptions, every eligible clock has
\[
 \min_{\substack{(a,b)\in\mathcal L_t\\(a,b)\notin\mathbb Q(t,-g_t)}}
       \max(|a|,|b|)
   \ >\ c\,t\left(\frac{\ln W}{\ln\ln W}\right)^{1/3}                             \tag{2}
\]
for large \(W\), with an absolute effective \(c>0\). In such a band at least \(\lfloor W/2\rfloor\) clocks are nonreturns. For each fixed ordinary source, once the nonreturn bound exceeds the eligibility cutoff, (2) supplies actual nonreturn dates in every sufficiently long band. In particular any unequal-slope rational merger of such a center requires a gap exceeding the right side. These conclusions concern a fixed ordinary trajectory; they do not select its own pair of merging iterates.

A November 8, 2026 preprint of Armand Noubissie bounds the number and degrees of exceptional hypersurfaces for the gcd at almost \(S\)-units. His Remark 3 treats a common exponent in \(a^n-1,b^n-1\). Here the second exponents vary separately, \(g_t\) is the actual binary prefix count, and a translated torus can contain many admissible independent pairs. We use the exceptional-hypersurface strategy with a rectangular family of monomials and an elementary bound for how often a single integer can contain these chronological divisors. The proof below uses two published quantitative theorems and does not depend on verification of the new preprint. [Noubissie, Theorem 9 and Remark 3, arXiv:2611.11341v1](https://arxiv.org/abs/2611.11341v1)

## A product of fixed forms with a rectangular set of monomials

At a bad length choose one witness \((a,b)\). Write \(U=2^t3^{-g_t}\), \(V=2^a3^b\), and take \(S=\{\infty,2,3\}\). Both are positive rational \(S\)-units, congruent to one modulo \(q_t\). Their independence over the multiplicative group of positive rationals follows from noncollinearity of the two exponent vectors. For a reduced fraction \(w\) write \(h_2(w)=\log_2\max(|\operatorname{num}(w)|,\operatorname{den}(w))\). We have \(t\le h_2(U)<2t\) and \(h_2(V)<3Bt\).

Take \(I=64B,\ J=16\), \(R=\{0,\ldots,I\}\times\{0,\ldots,J\}\) and \(k=|R|-1=1088B+16\). Set \(Z_{ij}=U^iV^j\), \(X_{ij}=Z_{ij}-1\) for \((i,j)\ne(0,0)\), with the convention \(X_{00}=0\). Distinct monomials have distinct values by independence. Put \(A=Ih_2(U)+Jh_2(V)<176Bt\). For the projective sup height \(H(X)=\prod_v\|X\|_v\) of the nonzero \(k\)-vector,
\[
                      2^{t-1}\le H(X)\le 2^{1+A}.                                  \tag{3}
\]
The upper bound follows at each place by taking local maxima of \(1,|U|_v\) and \(1,|V|_v\) with the displayed exponents, with a factor two at infinity. For the lower bound note \(X_{20}/X_{10}=U+1\). The rational height of a coordinate ratio is at most \(H(X)\), and \(H(U)\le2H(U+1)\).

At each \(v\in S\) choose a pivot \(s\in R\) minimizing \(|Z_s|_v\). Use as a basis the \(k\) forms \(L_{r,v}=X_r-X_s\) for \(r\ne s\). Their coefficient matrices have determinant of absolute value one, by elementary basis change from the original differences against zero. At infinity \(|L_{r,\infty}|\le2|Z_r|_\infty\), and the nonarchimedean bound costs no factor two. The product formula for each \(Z_r\), which is a unit outside \(S\), yields
\[
 \prod_{v\in S}\prod_{r\ne s(v)}|L_{r,v}(X)|_v
 \le 2^k\prod_{v\in S}\left(\min_{r\in R}|Z_r|_v\right)^{-1}
 = 2^{k+A}. 
\]
The last equality uses the exact rectangle, so the minimum is \(\min(1,|U|_v)^I\min(1,|V|_v)^J\). At every prime outside \(S\), all the \(X_r\) are integral and are divisible in the local ring by \(q_t\). Therefore \(\prod_{v\notin S}\|X\|_v\le1/q_t\). Dividing by the \(S\)-norms gives the normalized product
\[
  \prod_{v\in S}\prod_{r\ne s(v)}
                  \frac{|L_{r,v}(X)|_v}{\|X\|_v}
       \le H(X)^{-k}\, 2^{k+A}q_t^{-k}
       \le H(X)^{-k-1}\qquad(t\ge16).                                             \tag{4}
\]
Indeed \(k+A-kt/2\le -1-A\), since \(k\ge1088B,\ k\le1104B\) and \(A<176Bt\). No omission of prime factors in projective normalization is permitted in (4).

For each fixed pivot triple apply the quantitative Subspace Theorem for (4) with \(\varepsilon=1/2\). The coefficient field is \(\mathbb Q\), the forms are rational differences or coordinates of inhomogeneous height one, and the product of local basis determinants is one. The Galois maximum in the theorem is trivial. Above \(H(X)\ge k^{10k}\), the number of rational proper subspaces needed is at most \(\exp(C_1 k\ln(2k))\) for an absolute effective \(C_1\). This deliberately loose height cutoff follows also directly from Theorem 3.1 by the elementary exponent discretization given below. By (3) only \(O(k\ln(2k))\) lengths have smaller projective height. There are at most \((k+1)^3\) pivot triples. Each proper subspace supplies a nonzero rational linear equation among \(X_r\), hence a nonzero polynomial \(P(U,V)=0\) supported on the rectangle, with at most \(k+1\) terms. The polynomials \(Z_r-1\), considered formally as polynomials in two indeterminates, are linearly independent. [Evertse and Ferretti, *Annals of Mathematics* 177 (2013), Theorem 3.1 and Corollary 3.2](https://arxiv.org/pdf/1008.2340)

Here is the discretization with the published explicit threshold. Fix the archimedean pivot \(s_\infty\) and use \(Y_r=Z_r-Z_{s_\infty}\) as permanent coordinates. Every \(\|Y\|_p=\|X\|_p\) at finite primes, by unimodularity. At infinity all monomials are positive, so \(\|Y\|_\infty\) is their full range and \(\|X\|_\infty\le\|Y\|_\infty\le2\|X\|_\infty\). The archimedean forms are now the coordinates themselves. The finite-place forms in these coordinates are differences or coordinates. All normalized values \(|L_{r,v}(Y)|_v/\|Y\|_v\) lie in \((0,1]\), and the determinant factor for every basis is one. The same estimate as (4) bounds their product by \(H(Y)^{-k-1}\), since \(H(Y)\le2^{2+A}\) and the numerical margin \(k+A-kt/2\le-2-A\) holds at \(t\ge16\).

For each of these \(3k\) ratios take its exponent in base \(H(Y)\), clip below at \(-2k\), and round upward to the grid of step \(1/(16k)\). The initial exponent sum is at most \(-k-1\). If clipping occurs, the sum after clipping is at most \(-2k\), since all other exponents are nonpositive. Rounding adds at most \(3/16\) to the sum and preserves nonpositivity. Scale the rounded exponents toward zero to make the sum exactly \(-k-1/2\). At most \((32k^2+1)^{3k}\) systems occur. Theorem 3.1 with \(D=1,\ R_{\rm forms}\le3k,\ \varepsilon=1/2\) and \(H^*=1\) applies when \(H(Y)> k^{2k}\). Its displayed number of subspaces per system is \(\exp(O(k))\). This proves the required count by that theorem alone.

## Uniformly few exceptional translates, whatever their defining coefficients

For one polynomial \(P\), take a minimal nonempty vanishing subsum among its terms at \((U,V)\). Its support has size at least two. Choose the lexicographically first monomial in that subsum, move this term to the other side and divide by it. The result is a nondegenerate equation \(\sum_{i=1}^r c_i y_i=1\), where all \(c_i\) are fixed nonzero rationals and all \(y_i\) are positive rational \(S\)-units of the form \(U^{u_i}V^{v_i}\). The number of possible tuples is at most \((2^{35}r^2)^{3r^3}\) for \(r\ge2\), and at most one for \(r=1\). The supports cost at most \(2^{k+1}\). For each tuple retain just its first coordinate to obtain a translated equation
\[
                         U^u V^v=c,\qquad |u|\le I,\ |v|\le J,\ (u,v)\ne(0,0).       \tag{5}
\]
Across all polynomials the number of these equations is at most \(\exp(C_2 k^3\ln(2k))\), with an absolute effective constant. Their coefficients and their translated heights need not be effectively located. The unit equation theorem does not charge the heights of the fixed coefficients \(c_i\). [Evertse, *The number of solutions of decomposable form equations*, *Inventiones* 122 (1995), Theorem 3](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0122/LOG_0037.pdf)

## Packing one unknown translate along an actual clock

For an admissible independent pair in (5), \(c\ne1\). Let \(D\) be the absolute numerator of \(c-1\) in lowest terms and \(s=\log_2 D\). Both monomials are congruent to one at \(q_t\), so \(q_t\mid D\). In particular \(s\ge t/2>0\). Since \(c\) is positive, \(s\le h_2(c)\le I h_2(U)+J h_2(V)<176Bt\). Put \(A_0=176B\). Every possible length on this translate lies in \([s/A_0,2s]\).

If \(t'>t\) are lengths on the same itinerary, their common divisor divides \(|2^{t'-t}-3^{g_{t'}-g_t}|\le3^{t'-t}\). This is the only point requiring chronological consistency of \(g_t\). Partition \([s/A_0,2s]\) into at most \(2+128A_0^2\) half-open pieces of length at most \(s/(64A_0^2)\), assigning the rightmost endpoint to its last piece. No piece contains \(r=\lceil4A_0\rceil\) distinct admissible lengths. Otherwise their log lcm is at least
\[
       r\,\frac{s}{2A_0}
        -\binom r2(\log_2 3)\frac{s}{64A_0^2}
             >s,
\]
using \(r\le5A_0\) and \(\log_2 3<2\). This contradicts divisibility of their lcm into \(D\). Thus the number of dates per translated equation is \(O(B^3)\) with an absolute explicit bound, including when the center \(c\) has enormous height. This completes (1).

Take \(B\) equal to the integer part of a sufficiently small positive constant times \((\ln W/\ln\ln W)^{1/3}\) to get (2), decreasing \(c\) to absorb rounding. Restricting to dyadic bands and summing their square-root exceptional counts gives natural density zero of eligible lengths violating the analogous bound with \(W=t\). In particular, for the explicit thin rational centers \(1/(2^t-3)\), \(t\ge3\), take \(g_t=1\) for \(t\ge1\). Their full denominator satisfies eligibility, so for all but \(O(\sqrt N)\) dates \(N\le t<2N\) one has \(\operatorname{ord}_{2^t-3}(3)>ct(\ln N/\ln\ln N)^{1/3}\). This applies directly to the thin-cycle family in [the universal merger construction](../ordinary/UNIVERSAL_RATIONAL_MERGERS.md). It leaves open the order at individual exceptional lengths and any matching upper law.

For an orbit with distinct departure states one may compute a sufficient onset of eligibility directly from \(4800nt^{14}\le2^{t/2}\). For a trajectory which has repeated, the analogous finite test uses its observed maximum; no algorithm for computing the eventual maximum from the initial integer alone is needed or asserted. The density count supplies dates with expensive second relations. It does not force matched parity blocks, even when a rational phase is always available. The limits of the source-specific return argument and Paper 236's separate recurrence hypotheses therefore remain in force.

The [finite checker](check_counted_clock_relations.py) computes the projective height, prime-to-six content and exact three-place products in 72 rectangles, including 36 with negative secondary dyadic exponents. It verifies 2,376 evaluated difference forms, 512 full-size numerical margins and 286 packs of shared divisors carrying 1,373 eligible lengths in total. Normal and optimized Python give identical output. The external counting theorems are invoked in the written proof.

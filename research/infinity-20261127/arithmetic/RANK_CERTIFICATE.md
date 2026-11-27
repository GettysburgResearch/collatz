# A finite all-period exclusion at squareclass rank 31

**PROPOSED, with explicit dependencies.** For every nontrivial positive ordinary cycle, the affine span modulo rational squares of its adjacent odd-state products \(x_i x_{i+1}\) has dimension at least 32. This also forces affine state rank at least 32: if all states are in \(v+U\), all their adjacent products belong to \(U\). Unlike a bound on the rank of a multiplicative subgroup of rationals, the conclusion survives division of every product by its own arbitrary square. The valuations can be arbitrarily large.

Use \(P\) for the primitive odd period, \(s,M\) for the minimum and maximum odd state, and \(r\) for the affine squareclass rank of the edge products. We use the elementary square-gap lemma [PR192 A1 at ae48a04](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-unconventional-20261126/adelic/README.md), the [Pell spacing proof](PELL_RETURN_PACKING.md), and two published computational results. Barina reports convergence below \(2^{71}\); the endpoint itself is a power of two. Hercher's Corollary 29 and Remark 30 give at least \(137{,}500{,}000{,}000\) odd members after verifying the range through \(3\cdot2^{69}\), contained in Barina's range. Hercher's corrigendum addresses a step in Theorem 21. The published searches are inputs, not computations replayed here. [Barina, §6](https://doi.org/10.1007/s11227-025-07337-0) · [Hercher's paper and corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html)

## Bounding the odd maximum from a short square relation

Cut \(m\) odd transitions before a maximum \(x_m=M\) and write \(n=x_0\), with cyclic wrapping if necessary. Put \(A_j=\sum_{i<j}a_i\) for the dyadic clock. The exact normalized odd states satisfy
\[
 \frac{2^{A_j}x_j}{3^j}=n+t_j,\qquad
 b_j=3^m t_j=\sum_{h<j}3^{m-1-h}2^{A_h}.
\]
The \(b_j\) increase strictly. Write \(\xi_j=[2^{A_j}x_j/3^j]\). By the path identity in [the packing theorem](PELL_RETURN_PACKING.md), the state classes lie in a translate of a space of dimension at most \(r+1\). Adjoining \([2],[3]\) puts the \(\xi_j\) in an affine space of dimension at most \(r+3\), so the augmented vectors \((\xi_j,1)\) span a linear space of dimension at most \(r+4\).

Any nonempty vanishing sum of \(\ell\) distinct augmented rows selects an even number of rows. Its normalized product is a rational square. Multiplication by \(3^{m\ell}\) makes the product \(\prod_{j\in I}(3^m n+b_j)\) an integer square. Here the rational square root of an integer is integral. The A1 square-gap lemma gives
\[
        3^m n\le(64(b_m+1))^{\ell+2}.                                      \tag{1}
\]

For the general height estimate take \(m=r+4\). Linear dependence of \(m+1\) rows gives \(\ell\le m+1\). Telescoping the positive ratios yields
\[
  2^{A_m}=\frac nM\prod_{i<m}(3+1/x_i)\le4^m,\qquad
  2^{A_h}\le2^{m+h}\quad(0\le h\le m).
\]
The second inequality uses \(A_m-A_h\ge m-h\). Hence \(b_m\le2^m(3^m-2^m)<6^m\). Also \(M\le2^m n\) since each odd step grows by at most two. Formula (1) gives \(\log_2 M=O((r+1)^2)\). On a fixed-source finite prefix cut at its largest odd state. If fewer than \(m\) edges precede it, then \(M\le2^m x_{\rm initial}\); otherwise the same argument applies. This proves the general estimate used in the packing theorem.

## An exact numerical instance

Suppose \(r\le31\). Take \(m=44\), retaining 45 rows. The \(\sum_{j=0}^{12}\binom{45}{j}\) subsets of up to 12 rows outnumber the \(2^{35}\) possible vector sums. A collision gives a nonempty even symmetric difference of length at most 24. On a nontrivial cycle \(s\ge2^{71}\); putting \(S=2^{71}\), direct integer comparisons give
\[
 (3S+1)^{44}<2^{70}S^{44},\qquad (3S+1)^{44}<2(3S)^{44}.
\]
The first bounds \(A_{44}\le69\) by the product identity. The second gives \(3^{44}n>2^{43}M\) because each edge ratio is at most \((3+1/S)/2\). Isolating the \(h=0\) summand of \(b_m\) and bounding \(A_h\le69-44+h\) for \(h\ge1\) yields
\[
 B=3^{43}+2^{26}(3^{43}-2^{43})\ge b_{44},\qquad
 M<2^{-43}(64(B+1))^{26}<2^{2561}.                                         \tag{2}
\]

To count the possible periods, note that every cycle state is odd and a unit modulo three. For an edge \(x\to y\), its discriminant is \(D=3\cdot2^e d\) with \(d=\operatorname{sf}(xy)\) coprime to six and \(e=a\bmod2\). The possible \(d\)'s are in an affine squareclass space. Extend its direction space to dimension 31 within the coordinates of primes at least five if needed. Select 31 prime coordinates where projection on the direction space has rank 31. Such a finite selection exists by ordinary row reduction on a finite-support basis. Projection of the affine space is a bijection with all subsets \(J\) of the 31 pivots. If \(p_j\) denotes the \(j\)-th prime beginning with five, the \(j\)-th chosen pivot is at least \(p_j\). Thus \(D\ge 3\cdot2^e\prod_{j\in J}p_j\).

There are at most \(1+\lfloor 2561/\log_2\max(\rho,4D)\rfloor\) occurrences of this discriminant by (1) of the packing theorem and (2) above. For exact lower denominators set \(Q=64,\ w(v)=\lfloor\log_2(v^Q)\rfloor\) for integers \(v\ge1\). Write \(c(t)\) for the coefficient of \(z^t\) in \(\prod_{j=1}^{31}(1+z^{w(p_j)})\). Summing over every possible fingerprint, including unrealized ones, gives the integer upper bound
\[
 P\le\sum_t c(t)\sum_{e=0}^1
 \left(1+\left\lfloor\frac{2561Q}
 {\max(7Q,w(12)+eQ+t)}\right\rfloor\right)
 =127{,}901{,}154{,}889.
\]
The strict height gap \(\rho>2^7\) and the factor \(4D\) justify both entries in the maximum. The integer total is below the published odd-period floor. This excludes \(r\le31\).

The [exact script](check_pell_returns.py) computes \(w\) by integer bit length, verifies the Hamming, clock and height comparisons, expands the 31-factor polynomial by integer coefficient addition, and tests actual single edges and returning trajectories. Its [output](PELL_CONTROLS.json) records the arithmetic. This work does not repeat the published initial verification or Hercher's exhaustive search.

The pivot argument also gives the asymptotic improvement \(P=O(2^r(r+1)/\log(r+2))\) on primitive laps. Among the \(2^r\) pivot masks, the fraction with fewer than \(r/4\) marked positions is exponentially small by the elementary binomial tail bound. Every remaining mask forces \(d\) to contain at least \(\lfloor r/4\rfloor\) distinct primes; their product is at least \(\lfloor r/4\rfloor!\). Thus, for these masks, the denominator \(\log_2(4D)\) in the count is \(\gg r\log(r+2)\). For the others use its constant lower bound. Combining the \(O(r^2)\) height logarithm with both counts proves the estimate as \(r\to\infty\). Small \(r\) can be absorbed in the absolute constant.

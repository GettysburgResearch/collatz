# A boundary-corrected triadic construction and the exact Subspace cost

**23 November 2026. Status: a direct construction attempt; universal
construction remains OPEN.** This note tries to construct the witness in
the preceding triadic convergence theorem. It gives an explicit candidate
stream, isolates its uncancelled 3-denominator, and computes the full
Subspace-Theorem normalization of the most natural alternative stream.
Neither computation supplies the missing universal height saving.

The starting theorem and finite certificate are in
[TRIADIC_RANK.md](../../global-closure-20261123/duality/TRIADIC_RANK.md),
at PR178 commit `4e204f54136c79cf8c9393b34e3330594f99ae0a`.
All sources, finite identities and failed transfers below keep one fixed
positive ordinary input. The Subspace Theorem is not treated as an axiom
asserting that the unknown dual is algebraic.

## 1. The construction target

Use the shortcut map T(x)=x/2 on even integers and T(x)=(3x+1)/2 on odd
integers. Fix n>0, write x_K=T^K(n), and put e_K=1 if x_K is odd and
e_K=0 otherwise. Let

\[
p_K=\sum_{i<K}e_i,\qquad b_K=K-p_K,
\]

\[
\begin{split}
C_0=D_0&=0,\\
C_{K+1}&=3^{e_K}C_K+e_K2^K,\\
D_{K+1}&=3^{1-e_K}D_K+(1-e_K)2^K.
\end{split}                                                    \tag{1}
\]

The original source gives

\[
                     3^{p_K}n+C_K=2^Kx_K.                     \tag{2}
\]

Let alpha=Omega(n) denote its unique 2-adic complementary-parity point.
The published framework is Monks--Yazinski, *The autoconjugacy of the
3x+1 function*, Theorem 2.1 and the inverse-parity formula in Section 1:
[author PDF](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
[DOI](https://doi.org/10.1016/S0012-365X(03)00125-0).
Rationality on all positive integers is already equivalent to absence of
divergent orbits; it is not supplied by that theorem. The stronger target
alpha in Z[1/3] gives full convergence by the preceding packet.

Its finite sufficient condition is to find K,a,r with

\[
2^K\mid 3^{b_K}a+3^rD_K,
\quad
K\ge8\operatorname{bl}(n)+(9r+8)
  \operatorname{bl}(\max(1,|a|,3^r))+2.                       \tag{3}
\]

Here bl(m) is the least positive L with m<2^L. The dependence of the
required clock on the proposed witness's own numerator and denominator
is essential.

## 2. Match the terminal boundary to the actual parity

A zero terminal dual produces the prefix candidate -D_K/3^b_K. That
choice retains a large boundary error even on the known cycle. Replace
it by the member of the standard complementary cycle with the correct
terminal parity:

\[
c_K=1+e_K,\qquad d_K=2-e_K,
\]

\[
\boxed{
A_K=2^Kc_K-D_K,\quad
\eta_K=\frac{A_K}{3^{b_K}}.
}                                                            \tag{4}
\]

The inverse complementary word takes c_K back to eta_K. Consequently
eta_K has the correct complementary parity for the first K clocks, and
also at the terminal clock because c_K is opposite to x_K. This is a
triadic witness to every supplied finite prefix, not an all-time witness.
In the 2-adic metric,

\[
                   |\eta_K-\alpha|_2\le2^{-(K+1)}.           \tag{5}
\]

For comparison, pull the standard original terminal state backward too:

\[
B_K=2^Kd_K-C_K,\qquad \xi_K=B_K/3^{p_K}.
\]

Then (2) gives

\[
                n-\xi_K=\frac{2^K(x_K-d_K)}{3^{p_K}},       \tag{6}
\]

so xi_K also agrees with its known 2-adic target through K+1 bits.

### Exact defect recurrences

Put sigma_K=e_K+e_(K+1)-1. It is +1 at odd-to-odd transitions, -1 at
even-to-even transitions, and zero at alternating transitions. Equation
(1) gives

\[
\begin{split}
A_{K+1}&=3^{1-e_K}A_K+2^{K+1}\sigma_K,\\
B_{K+1}&=3^{e_K}B_K-2^{K+1}\sigma_K.
\end{split}                                                    \tag{7}
\]

After dividing by their exact denominators,

\[
\boxed{
\eta_{K+1}-\eta_K=\frac{2^{K+1}\sigma_K}{3^{b_{K+1}}},
\qquad
\xi_{K+1}-\xi_K=-\frac{2^{K+1}\sigma_K}{3^{p_{K+1}}}.
}                                                            \tag{8}
\]

Thus the new construction is driven only by failures of alternation.
Once an actual orbit enters 1,2, the candidate eta_K is exactly constant,
equal to the true triadic dual. Conversely, eventual constancy of eta_K
forces sigma_K=0 eventually, hence an alternating original tail. Such a
positive ordinary tail reaches the standard cycle: at its odd clocks,
u_(j+1)-1=(3/4)(u_j-1), and a positive integer u_j-1 cannot remain positive
under indefinite contraction. This converse is not used as a substitute
for constructing constancy.

At every defect, the paired real increments satisfy the exact identity

\[
       (\xi_{K+1}-\xi_K)(\eta_{K+1}-\eta_K)
                          =-(4/3)^{K+1}.                    \tag{9}
\]

The reason is p_(K+1)+b_(K+1)=K+1 and sigma_K squared is one. Hence
simultaneous real-small-increment reasoning cannot be taken for granted.
Both streams converge 2-adically; (9) concerns their ordinary real
increments and does not identify a real limit with a 2-adic limit.

The finite numerator recurrences (7) and the defect cases are checked in
[TriadicBoundary.lean](lean/TriadicBoundary.lean). The interpretation of
the stream, (5), and the eventual-tail argument have written-proof scope.

## 3. Exactly what must cancel at 3

Reduce eta_K by powers of 3. Its numerator A_K is nonzero: the inverse
maps below preserve nonzero elements of Z[1/3], since 1/2 is not in that
ring. Put

\[
t_K=\min(b_K,v_3(A_K)),\quad
r_K=b_K-t_K,\quad a_K=A_K/3^{t_K}.
\]

The concrete hope is that this one stream supplies a K for which
(K,a_K,r_K) satisfies the height inequality in (3). This requires both
the uncancelled exponent r_K and the reduced numerator a_K to be small
enough. Merely knowing eta_K is triadic for each K provides neither.

There is an exact backward description of the denominator.
Start z_K=c_K and pull backward through the **same** actual prefix:

\[
 z_i=\begin{cases}
       2z_{i+1},&e_i=1,\\
       (2z_{i+1}-1)/3,&e_i=0.
      \end{cases}                                           \tag{10}
\]

Then z_0=eta_K. While z_(i+1) is integral, the original-odd inverse
preserves integrality. The original-even inverse is integral exactly
when z_(i+1) is 2 modulo 3.

**Denominator persistence.** Once z_(i+1)=u/3^r is reduced with r>0,
neither backward operation can cancel a factor of 3:

\[
 2z_{i+1}=2u/3^r,
 \qquad
 (2z_{i+1}-1)/3=(2u-3^r)/3^{r+1}.                            \tag{11}
\]

Both new numerators are units modulo 3. Thus the exponent stays r on an
original-odd inverse and becomes r+1 on an original-even inverse. The
fractional identities and nondivisibility assertions in (11) are Lean
checked.

If the first backward integrality failure occurs at index j, then e_j=0
and r_K=b_(j+1). Equivalently, the number of cancelled denominator factors
is exactly the number of original-even letters in the maximal final
suffix whose complementary inverse trajectory stays integral. If no
failure occurs, r_K=0.

This is a global description of the reduced denominator for every finite
prefix. It does not say that the integral suffix eventually reaches the
original source. The original inverse trajectory being integral certifies
the other coordinate of the pair.

### Attempted elimination using the ordinary source

To transfer the strong source identity (2), I used the complete paired
determinant

\[
                    W_K=3^{b_K}C_K-3^{p_K}D_K.
\]

Keeping the terminal correction gives the exact relation

\[
\boxed{
3^{p_K}A_K=3^K n+
 2^K(3^{p_K}c_K-3^{b_K}x_K)+W_K.
}                                                            \tag{12}
\]

After each carry has received its first nonzero term, C_K and D_K are
units modulo 3: an active update is 3 times the old carry plus a power
of two, and the inactive update leaves it unchanged. Therefore, whenever
p_K differs from b_K,

\[
                        v_3(W_K)=\min(p_K,b_K).              \tag{13}
\]

The original identity enforces the cancellation in (12) needed to reach
the displayed factor 3^p_K. It does not give the additional valuation
v_3(A_K) needed by (3). Substituting W_K's defining carry expression into
(12) returns (2), rather than an independent cancellation estimate.
No source-dependent upper bound for r_K or the reduced numerator was
obtained from this attempted determinant elimination. This conclusion
is about this calculation; it does not rule out a different invariant.

## 4. The full S-adic cost of raw truncations

The deep theorem considered was the p-adic Subspace Theorem. Its relevant
fixed-form case says that primitive integer vectors whose product of
independent algebraic linear forms over a fixed finite set of places is
at most a negative power of their height lie in finitely many proper
rational subspaces. The forms, dimension and positive exponent are fixed.
See Schlickewei, *The quantitative subspace theorem for number fields*,
Compositio Mathematica 82 (1992), pp. 245--247, especially (1.3):
[primary paper](https://www.numdam.org/item/CM_1992__82_3_245_0.pdf).
The rational-vector normalization used here is also stated explicitly
in Evertse's [Theorem 1.1 and the restricted-denominator example](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf).

First try the natural integer vector

\[
                       (X,Y)=(D_K,3^{b_K}).                  \tag{14}
\]

After the first original-even step, this vector is primitive, by the
3-unit property above. Suppose temporarily that alpha is algebraic, so
that the forms are admissible. At infinity and 3 choose X,Y; at 2 choose
X+alpha Y,Y. The full product is **exactly**

\[
\begin{split}
\mathcal P_K
 &=|D_K3^{b_K}|_\infty |D_K3^{b_K}|_3
     |(D_K+3^{b_K}\alpha)3^{b_K}|_2\\
 &=D_K|D_K+3^{b_K}\alpha|_2\\
 &=\frac{D_K}{2^K}|\Omega(x_K)|_2.                          \tag{15}
\end{split}
\]

The 3-adic gain cancels its archimedean denominator cost exactly. The
mere prefix accuracy only gives P_K<=D_K/2^K. A negative-height-power
saving is an additional arithmetic statement, not a theorem obtained
by omitting the large real numerator.

There is also a separate logical problem: alpha's algebraicity is not
known for arbitrary n. The Subspace Theorem cannot be invoked with an
unproved algebraic coefficient and then used to establish that same
coefficient's rationality.

### Exact control on the known ordinary source 1

This failure of automatic power saving is already visible on a solved
source. For n=1 and K=2m, one has b_K=m, alpha=2, and

\[
D_{2m}=2(4^m-3^m),\qquad
D_{2m}+2\cdot3^m=2\cdot4^m.
\]

The finite carry and residual identities are checked in Lean. Therefore

\[
                  \boxed{\mathcal P_{2m}=1-(3/4)^m\to1.}    \tag{16}
\]

The height of (14) tends to infinity. For every fixed delta>0 and C>0,
the inequality P_(2m)<=C H_(2m)^(-delta) eventually fails. Thus even
perfect knowledge that the original source reaches 1 does not produce
the proposed negative-power estimate for the raw zero-tail truncations.
The boundary-corrected stream fixes this specific artifact: eta_K=2
identically on this source. It still needs the denominator/height theorem
in Section 3 for arbitrary n.

## 5. What the literature can and cannot supply here

The following distinctions determined where this attempt stopped.

1. **Rigidity does not construct approximants.** Roth/Ridout/Subspace
   arguments can exploit an independently proved approximation surplus
   to a known algebraic target. They do not supply the candidate sizes
   required by (3). Equation (15) computes the surplus actually missing
   in one tempting application.
2. **A fixed S-unit group is not a fixed-dimensional equation.** The
   defect expansion (8) has terms supported at 2 and 3, but the number
   of nonzero terms is the number of actual parity defects. No bound on
   that number, no fixed-length nondegenerate equation, and no uniform
   compression of the terms was proved. Standard S-unit finiteness
   cannot be applied to an equation of silently increasing dimension.
   The dependence on both dimension and group rank is explicit in
   Evertse--Schlickewei--Schmidt,
   [*Linear equations in variables which lie in a multiplicative group*,
   Theorem 1.1](https://arxiv.org/pdf/math/0409604).
3. **A real limit is a separate object.** Edgington's
   [*The autoconjugacy of a generalized Collatz map*, Theorem 2](https://arxiv.org/pdf/1206.0553)
   proves a real-limit statement under a lower even-density hypothesis
   greater than log_m(2), and identifies it with the 2-adic value under
   an additional periodic-parity hypothesis. For m=3 the density
   threshold exceeds 1/2, whereas the positive standard cycle has even
   density 1/2. That theorem does not establish a universal real-valued
   dual for the ordinary Collatz problem. Its terminal completion is
   also different from (4).

The older repository already has carefully scoped factor-complexity
screens. This note does not infer a low-complexity bound on every ordinary
orbit, nor import a real-to-2-adic equality from another paper. The
constant-code exception recorded in the repository errata remains intact.

## 6. Outcome and precise remaining mathematical step

The explicit construction tried here is (4), with cancellation performed
before evaluating the height budget. Its defects obey the coupled exact
identities (7)--(9), and its reduced denominator has the complete inverse
description (10)--(11). These are useful arithmetic data for a prospective
source-dependent theorem. They are not that theorem.

The remaining task is to prove that, for each fixed positive n, at least
one corrected candidate (or a different construction) satisfies (3).
For this particular stream, this means enough cancellation in A_K at 3
**and** enough control of the resulting signed numerator. Neither the
ordinary determinant identity nor the inspected Subspace machinery
establishes those bounds. Full Collatz remains OPEN.

The finite Lean module checks ten theorem declarations. It does not
formalize the Subspace Theorem, the infinite 2-adic construction, the
global denominator description, or any universal witness existence.
The [execution receipt](../../../reports/2026-11-23-profound-step/arithmetic-lean-receipt.json)
and [source ledger](../../../reports/2026-11-23-profound-step/arithmetic-sources.json)
record that boundary.

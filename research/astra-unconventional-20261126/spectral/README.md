# The complete essential spectrum of ordinary mass transport

**PROPOSED written theorem. Universal Collatz convergence remains OPEN.**
This is a boundary on a proposed operator proof, not an exclusion of an
ordinary orbit. The elementary physical cylinders and a finite telescoping
identity are formalized separately. The Banach-space argument below is written
mathematics. No historical priority claim is made.

Use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\qquad n\ge1.
\]

The **forward mass operator** is

\[
 (Pf)(m)=\sum_{T(n)=m}f(n),\qquad P\delta_n=\delta_{T(n)}.
\]

This specifies the operator completely. It is not the Koopman composition
operator, and no random choice of the odd-division exponent is made.

## 1. Statement

Let \(w(n)>0\). Assume discrete regular variation of index \(\alpha\in\mathbb R\):
whenever \(n_j\to\infty\) and \(m_j/n_j\to c\in(0,\infty)\),

\[
                 w(m_j)/w(n_j)\longrightarrow c^\alpha.       \tag{RV}
\]

In particular, positive power weights \(n^\alpha\) satisfy this assumption.
The usual measurable regularly varying weights restricted to the positive
integers satisfy it as well. Work over the complex Banach space

\[
       \ell^1_w=\{f:\sum_{n\ge1}w(n)|f(n)|<\infty\}.
\]

For a fixed integer \(M\ge0\), define absorption by

\[
P_M\delta_n=\begin{cases}
\delta_{T(n)}&n>M\text{ and }T(n)>M,\\
0&\text{otherwise}.
\end{cases}
\]

**S1.** With essential spectrum meaning the Fredholm essential spectrum,

\[
\boxed{\quad
\sigma(P_M)=\sigma_{\rm ess}(P_M)
=\{z\in\mathbb C:|z|\le R_\alpha\},\qquad
R_\alpha=\max\{2^{-\alpha},(3/2)^\alpha\}.
\quad}                                                       \tag{1}
\]

The same formula includes \(P=P_0\). In particular \(R_\alpha\ge1\).
Thus these operators have no gap between their spectral and essential radii,
for any finite absorbing floor. The conclusion survives replacing the norm
by any equivalent norm, including a weight comparable to \(w\).

**S2.** The essential disk also survives compact perturbations and the addition
of finitely many auxiliary coordinates with bounded couplings. Such changes
cannot make 1 an isolated leading eigenvalue separated from the entire rest
of the spectrum inside the unit disk. Compact perturbations may add discrete
eigenvalues outside the disk; (1) is not claimed for their full spectrum.

Both conclusions hold without assuming either convergence or escape of any
unspecified integer. Every long path used in the proof is a finite ordinary
cylinder, with its source chosen after its length.

## 2. Exact norm modulo compact operators

For any proper map \(F:\mathbb N_{>0}\to\mathbb N_{>0}\), its mass operator
\(A\delta_n=\delta_{F(n)}\) on \(\ell^1_w\), when bounded, satisfies

\[
 \|A\|=\sup_n\frac{w(F(n))}{w(n)},\qquad
 \|A\|_{\rm ess}=\limsup_{n\to\infty}\frac{w(F(n))}{w(n)}.       \tag{2}
\]

The norm statement follows by the triangle inequality and by testing each
normalized point mass. Truncating the input to its first \(N\) coordinates
is finite rank, which proves the upper essential-norm bound. For the lower
bound, let \(Q_B\) remove the first \(B\) output coordinates. On a compact
subset of \(\ell^1_w\), the tails tend uniformly to zero, so
\(\|Q_B K\|\to0\) for every compact operator \(K\). Properness implies
that only finitely many inputs have \(F(n)\le B\). Therefore

\[
 \|A-K\|\ge\|Q_BA\|-\|Q_BK\|
 \longrightarrow\limsup_n w(F(n))/w(n).
\]

This argument deliberately does not assert that the unit vectors of
\(\ell^1\) converge weakly to zero; that assertion would be false.

On each residue modulo \(2^k\), the exact affine formula is

\[
             T^k(n)=\frac{3^q}{2^k}n+\frac{C}{2^k},
             \qquad 0\le q\le k,
\]

where \(q,C\) are fixed on the residue. The all-even and all-odd words
occur on ordinary cylinders, so both extreme slopes occur. By (RV), (2)
gives the exact formula

\[
             \|P^k\|_{\rm ess}
              =\max\{2^{-\alpha k},(3/2)^{\alpha k}\}
              =R_\alpha^k.                                  \tag{3}
\]

Every iterate is proper since \(T^k(n)\ge n/2^k\). Also \(P-P_M\) has
finite rank: only finitely many \(n\le M\) or \(T(n)\le M\) occur. Thus
(3) has the same essential-radius consequence after absorption.

## 3. The inner disk has infinite-dimensional eigenspaces

For each \(\ell\ge0\), set

\[
 a_\ell=72\ell+10,\qquad b_\ell=24\ell+3,\qquad c_\ell=36\ell+5.
\]

Exactly \(T(a_\ell)=T(b_\ell)=c_\ell\). If \(|\lambda|<2^{-\alpha}\),
the vector

\[
 f_{\ell,\lambda}
 =\sum_{j\ge0}\lambda^j
       (\delta_{2^j a_\ell}-\delta_{2^j b_\ell})               \tag{4}
\]

belongs to \(\ell^1_w\). Indeed (RV), or its elementary power-envelope
consequence, gives \(w(2^j a)\le C_{a,\epsilon}2^{j(\alpha+\epsilon)}\),
and one can choose \(\epsilon>0\) so the geometric series converges.
Applying \(P\) to (4), the two \(j=0\) images cancel and the remaining
terms give \(P f_{\ell,\lambda}=\lambda f_{\ell,\lambda}\).

The dyadic supports for different \(\ell\) are disjoint. Their odd parts
are \(36\ell+5\equiv5\pmod{12}\) and \(24\ell+3\equiv3\pmod{12}\),
and each of these two lists is injective. Thus the eigenspace is infinite
dimensional. For \(P_M\), discard the finitely many \(\ell\) with one of
\(a_\ell,b_\ell,c_\ell\le M\); exactly the same proof applies.

Consequently every \(|\lambda|<2^{-\alpha}\) belongs to the Fredholm
essential spectrum, and its closed disk does as well. This already fills
the claimed disk when \(\alpha\le0\).

## 4. Periodic finite cylinders fill the remaining annulus

Suppose \(\alpha>0\). Fix any parity word of length \(k\ge1\) with \(q\)
odd letters and write \(a=3^q/2^k\). Choose any complex \(\lambda\) with

\[
                       |\lambda|=a^{\alpha/k}.               \tag{5}
\]

For each \(N\), realize \(N\) repetitions of the word on its ordinary
binary cylinder of length \(L=kN\). One may then choose the source as high
as desired within that cylinder. Denote the resulting states by
\(x_0,\ldots,x_L\). If \(q_j\) is the number of odd letters before time
\(j\), put \(A_j=3^{q_j}/2^j\). As the source tends to infinity in this
fixed cylinder,

\[
 x_j/x_0\to A_j,\qquad w(x_j)/w(x_0)\to A_j^\alpha
                         \quad(0\le j\le L).                \tag{6}
\]

The slopes \(A_j\) are distinct: equality at distinct times would equate
a nonzero power of 2 with a power of 3. Consequently all the actual states
are distinct when the source is sufficiently high. Choose it high enough
also to put every state above \(M\) and to make (6) as accurate as needed
at this finite list of times.

Define the finite vector

\[
               g_N=\sum_{j=0}^{L-1}\lambda^{-j}\delta_{x_j}.
\]

The exact boundary identity is

\[
       (P_M-\lambda I)g_N
       =\lambda^{1-L}\delta_{x_L}-\lambda\delta_{x_0}.         \tag{7}
\]

Because the word is periodic, \(A_{j+k}=aA_j\), and (5) implies
\(|\lambda|^{-j}A_j^\alpha\) is positive and \(k\)-periodic. Its finite
period has a positive minimum and finite maximum. Choose the accuracy in
(6) so these bounds change by at most a factor two. Then

\[
          \|g_N\|_w\asymp Lw(x_0),\qquad
          \|(P_M-\lambda I)g_N\|_w=O(w(x_0)),                 \tag{8}
\]

with constants depending on the chosen word and \(\alpha\), but not on
\(N\). Thus the normalized residual tends to zero. At each successive
\(N\), the source can be chosen so large that the entire new support is
above all preceding supports.

These disjointly supported normalized vectors have no norm-convergent
subsequence. If \(P_M-\lambda I\) were Fredholm, closed range and finite
dimensional kernel would give

\[
 \operatorname{dist}(f,\ker(P_M-\lambda I))
                  \le C\|(P_M-\lambda I)f\|.
\]

Applied to (8), this would put a subsequence arbitrarily close to a bounded
subset of a finite dimensional space, a contradiction. Hence every circle
in (5) is essential spectrum. The rational numbers \(q/k\) are dense in
\([0,1]\), so closedness fills the annulus from \(2^{-\alpha}\) to
\((3/2)^\alpha\). Together with (4) this is the entire disk in (1).

## 5. No spectrum outside the disk

Here is the needed uniform upper bound, including sources that depend on
the horizon. Discrete (RV) implies the usual power envelope: for every
\(\epsilon>0\) there is \(C_\epsilon\) such that for all positive integers
\(m,n\),

\[
 \frac{w(m)}{w(n)}\le C_\epsilon
  \max\{(m/n)^{\alpha+\epsilon},(m/n)^{\alpha-\epsilon}\}.      \tag{9}
\]

For completeness, uniformity of (RV) on ratios in \([1,2]\) follows by
contradiction and a convergent subsequence of ratios. Bound successive
doublings by \(2^{\alpha\pm\epsilon}\), compare the final ratio in
\([1,2]\), and invert when \(m<n\). The finite small arguments are absorbed
into the constant. This proves (9), with an arbitrarily small enlargement
of \(\epsilon\) if necessary.

The elementary physical envelope is

\[
       2^{-k}n\le T^k(n)\le(3/2)^k(n+1)-1
                            \le2(3/2)^k n.                  \tag{10}
\]

For every exponent \(\beta\), the supremum of \(r^\beta\) on the interval
of ratios in (10) is at one endpoint. Inserting (10) into (9), then taking
\(k\)-th roots, gives

\[
 r(P)\le\max\{2^{-\alpha+\epsilon},(3/2)^{\alpha+\epsilon},1\}.
\]

Let \(\epsilon\downarrow0\). Absorption satisfies
\(|P_M^k f|\le P^k|f|\) pointwise, so the same bound applies to \(P_M\).
The essential disk already proved supplies the reverse inclusion. This
finishes S1. Invariance of Fredholm essential spectrum under compact
perturbations and equivalent norms proves S2; finite dimensional blocks
and their couplings are finite rank relative to the infinite block.

## 6. What a successful spectral route still needs

On unweighted \(\ell^1\), if Collatz holds, every finitely supported vector
is eventually killed by \(P_M\) for \(M\ge2\). Nevertheless its entire
spectrum is the unit disk by S1. Pointwise extinction of each ordinary
source and uniform norm contraction are different statements.

Anisotropic norms that are not equivalent to these weighted norms are not
excluded here. Any use of such a space must check that the actual point
masses being used belong to it, that the operator preserves it, and that
the functional detecting surviving ordinary mass is continuous. A spectral
gap for an averaged exponent law or a quotient that loses that functional
does not establish extinction of a supplied ordinary source. This packet
does not construct the needed alternative space or prove local resolvent
regularity for every source.

## Sources and verification boundary

The mass-operator setup, its unweighted norm, and connections with orbit
averages are established background; see Leventides and Poulios,
[*Koopman Operators and the 3x+1-Dynamical System*, §§4–6](https://arxiv.org/abs/2010.12987).
The proof above is an explicit weighted and finite-floor calculation and
does not import a conclusion of that paper about divergent trajectories.
Béhani's [*Linear dynamics of an operator associated to the Collatz map*](https://arxiv.org/abs/2303.03203)
proves hypercyclicity independently of the truth of Collatz, an additional
reason to distinguish a functional-analytic property from a stopping proof.
The Berg–Meinardus functional equation and the natural-boundary theorem of
[Bell and Lagarias](https://arxiv.org/abs/1408.6884) also do not furnish a
finite-dimensional two-base Mahler system for an arbitrary basin indicator.

[OrdinaryCylinders.lean](OrdinaryCylinders.lean) checks the explicit even and
odd finite cylinders, every intervening floor guard, and the collision
pairs used in (4). [ChainBoundary.lean](ChainBoundary.lean) checks the finite
linear telescoping identity behind (7). [InfiniteKernel.lean](InfiniteKernel.lean)
proves that the algebraic mass pushforward on finitely supported vectors
over any field has an infinite linearly independent family in its kernel,
and consequently that its kernel is not a finite module. Its witnesses
are the positive collision pairs in (4). None of these files asserts S1
or S2 as a Lean theorem. The exact checker exercises parity realization, finite
eigenvector truncations, and the endpoint residuals on actual ordinary
paths; these checks support the stated finite identities, not the infinite
functional-analysis proof.

# Higher-rank limits and arithmetic rationality attacks

23 November 2026. **Full Collatz remains OPEN.** This continuation followed
the [finite triadic and residual-denominator checkpoint](../README.md),
published at `e5313208c09e5c47bb8592189975825842b19158`.
It tests three substantial literature mechanisms at their actual arithmetic
and dynamical interfaces. The strongest new consequence is a positive Haar
component in an explicitly constructed higher-rank limit of the canonical
boundary law. The required transfer to ordinary endpoints remains open.

## 1. Higher-rank rigidity reaches an actual derived limit

The [higher-rank note](HIGHER_RANK_BOUNDARY_ATTACK.md) starts with the
canonical common real-boundary law from PR180, retaining its positive floor,
selection, and information-dimension qualifications. Write its lower
information dimension as `d0 > 0`. For one hypothetical escaping odd source,
let `q_j = U^j(p)`, `A_j` be the actual accumulated division exponent, and
`chi_j = 3^j / 2^A_j`.

On the compact solenoid

\[
X_6=(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)/
\operatorname{diag}\mathbb Z[1/6],
\]

let `sigma_j` be the common-boundary law of `iota(-chi_j Z)`. The exact
orbit identity yields, for the specified dyadic averaging

\[
\lambda_{N,L}=\frac1{NL}\sum_{j<N}\sum_{\ell<L}
(\times2^\ell)_*\sigma_j,
\]

\[
d_{TV}((\times2)_*\lambda_{N,L},\lambda_{N,L})\le1/L,
\qquad
d_{TV}((\times3)_*\lambda_{N,L},\lambda_{N,L})
\le\frac{A_N}{NL}+\frac1N.
\]

The explicit schedule **`L = N^2`** also preserves positive entropy.
Scaling and reduction modulo one lose only `O_p(N)` bits, uniformly over
the moving roots, while the input entropy is evaluated at precision `N^2`.
A finite block argument and a boundary-atom correction give the required
positive doubling entropy in every weak limit.

Einsiedler–Lindenstrauss, Theorem 1.2, then applies to the established joint
action. Every weak limit has the form

\[
\boxed{\lambda=c\,m_{X_6}+(1-c)\lambda_0,\qquad c\ge d_0,}
\]

where the remainder has zero entropy on all jointly ergodic components.
This is a source-qualified written theorem about this exact enlarged
average. It does not claim pure Haar measure or equidistribution of the
unthickened ordinary orbit.

The same note applies Einsiedler–Kleinbock's exceptional-set theorem directly
to the actual boundary: almost surely,

\[
\liminf_{Q\to\infty}Q|Q|_\ell\,\|QZ\|=0
\]

for every prime `ell`. The deduction uses the stronger information-dimension
statement for every fixed absolutely continuous reweighting, together with
the primary theorem's countable-union box-dimension-zero exceptional sets.

The first conversion problem is explicit. The original conditional fibres
have weight only `p0/N^2` in the enlarged average, and no result places them
inside its Haar part. More fundamentally, before taking the compact
quotient, the multiplication and affine Collatz maps satisfy
`D A = A D + (1,1,1)`. The discarded diagonal translation changes the
ordinary endpoint by one. The compact coordinate therefore loses an
integer carry required by the target ternary law. The Diophantine theorem
likewise does not require its good approximants to have the exact numerator,
dyadic denominator, and intermediate states of a legal inverse word.

## 2. Arithmetic rationality at one fixed ordinary source

The [Borel–Dwork attack](BOREL_DWORK_ACTUAL_PARITY_ATTEMPT.md) constructs
the actual rational-coefficient series

\[
B_n(z)=\sum_{k\ge0}\frac{e_k}{3^{p_{k+1}}}z^k,
\qquad
A_n(z)=\sum_{k\ge0}\frac{T^k(n)}{3^{p_k}}z^k,
\]

where `e_k` is the actual shortcut parity and `p_k` its cumulative odd count.
Their exact identity is `(2-z) A_n = 2n + z B_n`, and `B_n(2)=-n` in
the 2-adic completion. Under hypothetical escape, the same series has the
positive real value `n (Lambda_infinity^(-1)-1)` at 2.

Bost–Chambert-Loir's arithmetic formal-model condition holds. The directly
available radius product is nevertheless

\[
\prod_vR_v(B_n)=3^{\rho_- -\rho_+}\le1.
\]

The attempt to remove the actual core denominator `3-z^2` leaves the relevant
radii unchanged on an escape. Neither the isolated rational specialization
nor its rational tail transforms supply the missing meromorphic extension
with positive capacity. More general continuation domains remain possible;
the note does not rule them out. Rationality would initially prove eventual
periodicity, still requiring positive-cycle classification.

## 3. Hankel determinants and arithmetic holonomicity

The [Hankel and holonomicity note](HANKEL_AND_HOLONOMICITY_ATTACK.md)
targets the integer fibre after the new superpolynomial denominator bound.
For the exact weighted cyclic forcing sequence `u` and state sequence `h`,
the full-rank Hankel determinant is the residual resultant:

\[
\Delta_n(u)=\pm\operatorname{Res}(F_0,Q_0),\qquad
\Delta_n(u)=(-1)^nF_0(3)\Delta_n(h).
\]

It therefore does not resolve the previously identified wrong-conjugate
cancellation. The first bordered determinant is a nonzero multiple of
the original distinguished-fibre equation `F_0(3)t+Q_0(3)=0`.

The arithmetic-holonomicity test uses the actual quantitative theorem of
Calegari–Dimitrov–Tang. Normalizing the cyclic coefficients makes their
archimedean size depend on the minimum `m`, but restoring algebraic
integrality at 2 incurs a height cost governed by the maximum orbit value
`M`. The note derives that cost exactly. The known polynomial bound on
`m` therefore cannot be substituted for control of `M`.

The proposed minimum-versus-residual-degree estimate remains an explicit
open target. No determinant or holonomicity theorem here proves full
numerical nondivisibility.

## Evidence

These are written mathematical arguments with primary-source theorem
interfaces and internal independent reconstruction. The new infinite
rigidity results and arithmetic determinant arguments are not claimed as
Lean theorems. The preceding 26-theorem Lean audit remains unchanged.
See the [execution and review report](../../../../reports/lean-global-closure-20261121/nov23/risk24/literature/README.md)
for exact source hashes, scopes, and the publication gate.

# A compact strict-Green correction with an entire resolvent

**Status: SOURCE-QUALIFIED.** Complete written operator deduction under the
pinned ordinary path-count input. The finite path cancellation is checked
in `lean/StrictGreenKernel.lean`, and the explicit ordinary inverse ladder
is checked in `lean/OddDepthLadder.lean`. This note does not
assert that the full ordinary transport has a spectral gap or that Collatz
converges.

The latest PR180 proves compactness of the actual Green map from an
unweighted source space into a weighted output space, and shows that raw
forward transport is not closable on that output space. There is a
different, naturally occurring operator for which a same-space resolvent
argument is valid: the strict Green correction carrying the exact
immigration factor `1/(3n+1)`. Its powers satisfy a factorial bound, and
its resolvent is entire. This settles the correction operator completely
while leaving the ordinary harmonic escape channels explicit.

## 1. Domain and the one quantitative input

Let `N` be the positive odd ternary units that are not themselves periodic
under the ordinary odd Collatz map `U`. Transport is killed on first
entering a periodic state. Every retained forward path has distinct
states. Membership of this mathematical domain is not asserted decidable.

Write

\[
(La)(q)=\sum_{Ux=q}a(x),\qquad
(Sa)(q)=\sum_{j\ge0}L^ja(q).
\]

All sums use the retained domain. The input, from PR180
`cfe70e02f246119a55fb5bf8fd573f148d746beb`,
`research/lean-critical-20261122/POTENTIAL_ATTACK.md`, P3--P7, is

\[
\#\{j:q_j\le X\}\le5X^\theta,\qquad\theta=39/40,
\tag{1}
\]

for each retained actual path. Its complete occupation consequence is

\[
\sum_jq_j^{-s}\le C_s:=\frac{5s}{s-\theta},\qquad
\sum_{q_j>X}q_j^{-s}\le C_sX^{\theta-s}
\quad(s>\theta).
\tag{2}
\]

In particular `C_1=200`. These are retained-source path estimates; no
inverse words are resampled. The pinned upstream proof of (1) and its
evidence level remain attached to this import.

For `s>0` set

\[
X_s=\ell^1(\mathcal N,n^{-s}),\qquad
\|a\|_s=\sum_n|a(n)|n^{-s},\qquad
\omega(n)=\frac1{3n+1},\qquad (Da)(n)=\omega(n)a(n).
\]

The operator studied here is

\[
\boxed{K=SLD,\qquad
Ka(q)=\sum_{n\prec q}\omega(n)a(n),}
\tag{3}
\]

where `n≺q` means a strictly positive retained forward hitting depth.
Each source contributes once at each strictly later endpoint. The
time-zero term is excluded from `K` and retained in `I+K`.

## 2. Compactness on one space

Fix `theta<s<=1`. Then

\[
\|D a\|_{\ell^1}\le\frac13\|a\|_s,
\]

because `n^s/(3n+1)<=1/3`. Raw `L` is a contraction on **unweighted**
source `ell^1`; (2) makes `S:ell^1->X_s` compact. These are compatible
domains, so

\[
\boxed{K:X_s\to X_s\text{ is compact},\qquad
\|K\|\le A_s:=C_s/3.}
\tag{4}
\]

If `Q_X` retains output heights at most `X`, the explicit error is

\[
\|(I-Q_X)K\|_{X_s\to X_s}\le A_sX^{\theta-s}.
\tag{5}
\]

There is no use of raw `L` as a bounded operator on `X_s`.

## 3. Factorial powers from actual ordered paths

Fix one source `n`, and list its retained path as
`q_0=n,q_1,q_2,...`, stopping if it is killed. For `j>=1` and `ell>=1`,
the exact matrix coefficient of `K^j` is

\[
K^j\delta_n(q_\ell)
=\omega(n)\!\sum_{1\le i_1<\cdots<i_{j-1}<\ell}
             \prod_{a=1}^{j-1}\omega(q_{i_a}).
\tag{6}
\]

For `j=1` the empty product is one; an impossible index set contributes
zero. Equation (6) retains every intermediate immigration choice on the
unique physical path. It follows by induction on the number of `K`
applications, or by splitting an increasing sequence at its last choice.
Different original sources may collide and are still summed linearly.

For nonnegative numbers `w_i`, expansion of `(sum_i w_i)^k` includes
each product at distinct increasing indices exactly `k!` times; its
other terms are nonnegative. Hence the inner sum in (6) is at most

\[
\frac1{(j-1)!}\left(\sum_{i\ge1}\omega(q_i)\right)^{j-1}
\le\frac{C^{j-1}}{(j-1)!},\qquad C=200/3.
\tag{7}
\]

Use finite path segments first and increase them; all terms are
nonnegative. Multiplying (6) by `q_ell^(-s)`, summing the **whole** path,
and applying (2) gives

\[
\|K^j\delta_n\|_s
\le\omega(n)C_s\frac{C^{j-1}}{(j-1)!}.
\]

The column norm divided by `||delta_n||_s=n^(-s)` is uniformly bounded.
The positive-kernel column criterion for weighted `ell^1` therefore yields

\[
\boxed{\|K^j\|_{X_s\to X_s}
\le A_s\frac{C^{j-1}}{(j-1)!}\quad(j\ge1).}
\tag{8}
\]

This proof does not require a globally ordered list of all ordinary
states. Each individual forward path supplies the order used in (6).

## 4. Entire resolvent and its physical kernel

For every complex `z`, the series

\[
R(z)=I+\sum_{j\ge1}(-z)^jK^j
\tag{9}
\]

converges absolutely in operator norm, uniformly on every bounded set of
parameters. Equations (8) and the exponential series give

\[
\boxed{\|R(z)\|\le1+|z|A_s e^{C|z|}.}
\tag{10}
\]

Multiplying finite partial sums by `I+zK` leaves only the last geometric
remainder; (8) sends that remainder to zero. Both products therefore give
the identity:

\[
\boxed{R(z)=(I+zK)^{-1}\quad\text{for every }z\in\mathbb C.}
\tag{11}
\]

Thus `K` has spectral radius zero. It is a compact Volterra-type operator,
and this particular correction has no finite parameter pole.

Summing (6) over the possible intermediate subsets gives a closed kernel:

\[
\boxed{
R(z)a(q)=a(q)-z\sum_{n\prec q}\omega(n)a(n)
       \prod_{n\prec u\prec q}(1-z\omega(u)).}
\tag{12}
\]

The product is over the finitely many interior states of the actual
source-target path. Every source-target hitting depth is unique. For
infinite source sets, the operator-norm convergence above and the
positive majorant `prod(1+|z|omega)<=exp(|z|C)` justify the formula by
finite-source approximation. No sum over possible unrelated histories
replaces a physical path.

At `z=1`, the factors in (12) are exactly
`lambda(u)=3u/(3u+1)`, the ordinary multiplicative correction already in
the repository. For the canonical functions in PR185/182, the established
identity is

\[
\nu=h+SL(Dh)=(I+K)h.
\]

Their pinned moment bounds put both functions in `X_s`. Consequently

\[
\boxed{h=R(1)\nu}
\tag{13}
\]

uniquely in that space. This is a bounded invertible change between the
critical and ordinary harmonic representatives already constructed.
It does not assert positivity of `R(1)a` for an arbitrary positive input.

## 5. Finite sources, finite outputs, and finite clocks

For `theta<s<1`, let `P_Y` retain input heights at most `Y`. The same
factorization gives the additional bound

\[
\|K(I-P_Y)\|\le A_sY^{s-1},
\]

and hence

\[
\boxed{\|K-Q_XKP_Y\|
\le A_s\bigl(X^{\theta-s}+Y^{s-1}\bigr).}
\tag{14}
\]

The balanced choice `s=79/80` gives exponent `1/80` in both cutoffs and
`A_s=395/3`. This is a finite matrix approximation to `K` in operator
norm. Its entries still involve actual all-time hitting; (14) alone
does not decide a missing entry effectively.

For `N>=0`, put

\[
K_N=\sum_{j=1}^N L^jD.
\]

All are bounded on `X_s`, and `0<=K_N<=K` as kernels. The bounds in
(14) also dominate their omitted input/output pieces uniformly in `N`.
For a fixed finite pair of source and target sets, every entry of
`Q_XK_NP_Y` stabilizes: either the source never reaches the target, or it
does so once at its finite hitting depth. There are finitely many pairs,
so a common stabilizing depth exists. First choose `X,Y` using (14), then
that depth. This proves

\[
\boxed{\|K-K_N\|_{X_s\to X_s}\to0\quad(\theta<s<1).}
\tag{15}
\]

The same argument works for literal shortcut-clock truncation. No
effective uniform rate is extracted for the finite middle matrix.

Every `K_N` and every finite projection above has the same path-selection
majorant (8). Resolvent identity and (10) therefore give, with any such
approximation `K'`,

\[
\|(I+zK)^{-1}-(I+zK')^{-1}\|
\le |z|\bigl(1+|z|A_se^{C|z|}\bigr)^2\|K-K'\|.
\tag{16}
\]

Thus the correction resolvents also converge in operator norm, uniformly
on compact parameter sets. Source identities and clock distinctions are
preserved throughout.

## 6. Why the endpoint weight is different

The existing explicit convergent ladder

\[
n_j=(40\,64^j-1)/3,\qquad U(n_j)=5
\]

shows `K delta_(n_j)(5)=omega(n_j)`. Thus for `s>1`, the ratio of output
to input norms is at least
`5^(-s)n_j^s/(3n_j+1)`, which tends to infinity. This `K` is unbounded
on `X_s` for `s>1`.

At `s=1`, the same family prevents source-height truncations from
converging in operator norm: the ratio tends to `1/15`. Arbitrarily
long **odd-depth** convergent inverse ladders also prevent uniform odd-
clock truncation at this endpoint. An explicit one is obtained by
choosing a unit parent of each positive odd unit `q` as follows:

| `q mod 9` | exponent `e` | parent in terms of `q=9t+r` |
|---|---:|---|
| 1 | 4 | `48t+5` |
| 2 | 3 | `24t+5` |
| 4 | 6 | `192t+85` |
| 5 | 3 | `24t+13` |
| 7 | 4 | `48t+37` |
| 8 | 5 | `96t+85` |

Each parent is a positive odd unit `p>=2q`, with `3p+1=2^e q`.
Starting from 5 and iterating this parent construction gives `n_j>=5*2^j`
whose first odd hit of 5 is exactly at depth `j`. These sources all have
explicit convergent paths. For `j>N`, the coefficient of `K_N` at target
5 is zero while the full coefficient is `omega(n_j)`. Consequently

\[
\boxed{\|K-K_N\|_{X_1\to X_1}\ge1/15
\quad\text{for every fixed }N,}
\tag{17}
\]

where the lower bound is the supremum over increasingly large `j`.
It is compatible with the norm convergence in (15), whose hypothesis is
strictly `s<1`. No statement about `0<s<=theta` is made here.

## 7. Consequence for the attempted full proof

The raw transport obstruction from PR180 is respected. Smoothing its
input by the **actual** immigration factor yields a compact same-space
operator, a complete entire resolvent, and genuine finite-clock norm
approximation below the endpoint weight. This is a constructive repair
of that operator interface.

It does not force the ordinary harmonic flow to vanish. Equation (13)
is an invertible correction, so a surviving ordinary channel is carried
to a critical harmonic representative. The operator `K` does not
propagate an unchanged atom at every clock; it charges `omega` at each
selected immigration state. Its quasinilpotence cannot be substituted
for decay of the original `L` or for absence of the bilateral channels
identified in PR183. Nontrivial cycles are killed out of this domain
and remain a separate obligation.

The positive new interface is that the correction and its finite clock
approximations are controlled in one Banach space. A full proof must
still constrain the unsmoothed harmonic boundary or the actual excursion
mass. This note does not replace that remaining statement by an axiom.

## 8. Formal scope and literature connection

`lean/StrictGreenKernel.lean` checks five finite identities and bounds:
the exact path-product telescoping identity, off-diagonal inverse
cancellation, the complete subset polynomial, the unit-interval survival bound, and its exponential
absolute majorant. `lean/OddDepthLadder.lean` checks twenty declarations
including the six-case parent map, exact odd and shortcut realization,
exponential height growth, unique first odd hitting depth, and ordinary
convergence through 5 to 1. Neither module assumes a universal Collatz
statement or formalizes the imported path count or Banach-space argument.

The operator-theoretic inspiration is the factorial behavior of iterated
Volterra operators; see F. Leon-Saavedra and A. Piqueras-Lerena,
[*Cyclic properties of Volterra operator*](https://msp.org/pjm/2003/211-1/pjm-v211-n1-p09-p.pdf),
Pacific Journal of Mathematics 211 (2003), Section 2. The present operator
acts on a weighted sequence space and uses actual discrete Collatz paths.
Its estimates and inverse are derived directly above; a theorem about
the classical integration operator is not imported as a Collatz result.

The companion `EXCURSION_RESOLVENT_INTERFACE.md` proves the more precise
positive identity `(I+K)^(-1)S eta=S_T eta` for every finite nonnegative
original source measure. That identity retains the possible last-contact
escape sector explicitly.

`HARMONIC_KERNEL_FACTORIZATION.md` extends the correction to the exact
maximal transport domain. It proves
`I-T_z=(I-L)(I+zK)`, equality of the actual stationary ranges, and
`ker(I-T_z)=R(z)ker(I-L)`. At `z=1` the positive harmonic cones are
order-isomorphic and `||R(1)||<=1+A_s`. These are right-factorization
statements, with no assertion of full transport similarity.

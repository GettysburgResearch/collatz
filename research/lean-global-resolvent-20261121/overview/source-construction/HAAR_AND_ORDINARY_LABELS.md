# Unthickened Haar limits and the ordinary endpoint label

23 November 2026. **Status: written conditional theorem, exact finite
identities, and a direct closing attempt.** No escaping ordinary orbit is
constructed or excluded. Rajchman regularity of the actual boundary is an
explicit additional hypothesis in Section 3, not a conclusion of the repo's
information-dimension results.

The attempt was to use the new higher-rank boundary rigidity result to
supply the original orbit's missing ternary collision upper bound. The
calculation below identifies what happens even if the real boundary has
enough Fourier decay to give pure Haar convergence without thickening.

## 1. The retained source and inspected inputs

Use the actual escaping odd-unit orbit and common boundary normalization
from PR175, commit `53ba1e1ffc46bf022433c2124a62682ad8dd4739`,
`research/lean-global-closure-20261121/risk24/literature/HIGHER_RANK_BOUNDARY_ATTACK.md`,
Sections 1--5. This note uses its source-qualified common path law; it does
not independently reconstruct that infinite analytic construction.

Write

\[
 q_j=U^j(q_0),\quad A_j=\sum_{i<j}v_2(3q_i+1),\quad
 \chi_j=3^j2^{-A_j},\quad Z\sim\mu.
\]

The fixed common real law has compact positive support. The actual
conditional law at root `q_j` is `mu_j`, and
`d_TV(mu_j,mu)<=1-p_j ->0`. Under `mu_j`, the actual inverse intercept
and compact class are

\[
 R_j=q_j-\chi_j Z,\qquad
 X_j=[(R_j,q_j,q_j)]=\iota(-\chi_j Z)
\]

in

\[
 X_6=(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)
          /\operatorname{diag}\mathbb Z[1/6],
 \qquad\iota(t)=[(t,0,0)].
\]

Under the common law `mu`, the same affine expression is a comparison
coordinate. It is not an assertion that every such pair is a legal inverse
path from `q_j`.

The original orbit escapes, and the retained positive correction product
gives `chi_j -> infinity`. Also `A_j<=j log_2(3)+C` for a fixed source
constant `C>=0`. These are supplied physical inputs.

Two other inspected source files are PR180 at
`a436db7b85f37abafea25f42d6f34afed02a29c0`,
`research/whole-source-20261123/COLLISION_CORE.md`, Sections 3--8, and PR182
at `a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/ACTUAL_COLLISION.md`, Sections 2--7.
The former's strict collision gap concerns the actual ternary time-limit
law; the latter retains the complete carry and original source quotient.
Neither supplies the mixed-observable estimate in Section 4 below.

## 2. The long dyadic average removes the valuation clock from the averaging shape

Let `T_2,T_3` be multiplication on `X_6` and put
`sigma_0=iota(-.)_*mu`. The exact source cocycle is

\[
 \sigma_j=(T_3^jT_2^{-A_j})_*\sigma_0.
\]

For positive integers `N,L`, compare the actual thickened average

\[
 \lambda_{N,L}=\frac1{NL}\sum_{j<N}\sum_{\ell<L}
                  (T_2^{\ell-A_j}T_3^j)_*\sigma_0
\]

with the ordinary rectangular semigroup average of the same initial law

\[
 \rho_{N,L}=\frac1{NL}\sum_{j<N}\sum_{\ell<L}
                  (T_2^\ell T_3^j)_*\sigma_0.
\]

**Finite comparison.** With probability total variation defined as
`sup_E |alpha(E)-beta(E)|`,

\[
 \boxed{d_{\rm TV}(\lambda_{N,L},\rho_{N,L})
 \le\frac1N\sum_{j<N}\min\{1,A_j/L\}
 \le\frac1{NL}\sum_{j<N}A_j.}
 \tag{1}
\]

For each `j`, the two integer intervals of exponents have `L-min(L,A_j)`
terms in common. Cancel those probability measures. Each remaining
average has mass `min(1,A_j/L)`, which bounds their probability total
variation. Average over `j`; no independence or measure regularity is used.

In particular,

\[
 d_{\rm TV}(\lambda_{N,N^2},\rho_{N,N^2})
 \le\frac{\log_2 3\,(N-1)}{2N^2}+\frac C{N^2}\longrightarrow0.
 \tag{2}
\]

Thus these two averages have exactly the same weak limits. The dependence
on the particular valuation clock disappears from this averaging shape.
The initial law `mu` can still depend on the ordinary component; (1) does
not remove that dependence or replace it by an arbitrary canonical law.

This comparison leaves PR175's positive-Haar-component theorem intact.
It specifies how much of the actual chronological word is retained by its
chosen thickening.

## 3. A stronger real regularity hypothesis still leaves the endpoint marginal intact

Use the convention
`mu_hat(t)=integral exp(-2*pi*i*t*z) dmu(z)`. Call `mu` Rajchman if
`mu_hat(t)->0` as `|t|->infinity`. In particular an integrable density has
this property by the Riemann--Lebesgue lemma. No such property is asserted
for the actual canonical boundary here.

Retain the actual ordinary endpoint as a second coordinate:

\[
 J_N=\frac1N\sum_{j<N}
       (z\mapsto(\iota(-\chi_jz),q_j))_*\mu
       \quad\hbox{on }X_6\times\mathbb Z_3^\times.
\]

**Conditional theorem.** If `mu` is Rajchman, then for every subsequence
on which the actual ternary time laws converge to `nu`,

\[
 \boxed{J_{N_i}\ \Longrightarrow\ m_{X_6}\otimes\nu.}
 \tag{3}
\]

The same statement holds with the actual conditional laws `mu_j` in place
of `mu` in the summands. No dyadic thickening is required.

**Proof.** The characters of `X_6` are indexed by
`xi in Z[1/6]`, and on the real leaf they satisfy
`e_xi(iota(t))=exp(2*pi*i*xi*t)`. For a continuous bounded endpoint test
`f`, the mixed integral is

\[
 \int e_\xi(x)f(v)\,dJ_N(x,v)
   =\frac1N\sum_{j<N} f(q_j)\widehat\mu(\xi\chi_j).
 \tag{4}
\]

For `xi!=0`, `|xi|chi_j ->infinity`, so the right side tends to zero,
even after multiplication by the bounded deterministic endpoint test.
For `xi=0` it is exactly the actual endpoint average, with limit
`integral f dnu`. Finite linear combinations of these product tests are
dense in the continuous functions on the compact product, proving (3).

For the actual conditional laws, the difference against any bounded test
is at most twice its supremum norm times
`N^(-1) sum_(j<N) d_TV(mu_j,mu)`, which tends to zero. The tests may depend
on `j`; the total-variation estimate is uniform over such bounded tests.
This proves the stated transfer. Square.

Consequently, even proving absolute continuity of the actual real boundary
and pure unthickened Haar convergence would not, through this compact
projection alone, impose a new constraint on the actual subsequential
endpoint law `nu`. Formula (3) retains that law as its second marginal.
It does not claim that every abstract `nu` is realizable by an ordinary
escaping orbit, nor does it construct a canonical boundary with a density.

## 4. The exact endpoint observable keeps both phases

The missing information has an exact finite expression. Put `Q=3^m` and
let `h` be an integer. On every supplied source-boundary pair,

\[
 \boxed{
 e^{2\pi i hR_j/Q}\,
       \overline{e_{h/Q}(X_j)}=e^{2\pi i hq_j/Q}.}
 \tag{5}
\]

Indeed `R_j=q_j-chi_j Z` and
`e_(h/Q)(X_j)=exp(-2*pi*i*h*chi_j*Z/Q)`. The two occurrences of the
same boundary variable cancel pointwise. This is not an independence
approximation. It holds under the common law or under every actual
conditional law.

For the original time law `pi_N=N^(-1)sum_(j<N)delta_(q_j)`, finite Fourier
orthogonality therefore gives exactly

\[
 \operatorname{Col}_Q(\pi_N)
 =\frac1Q\sum_{h=0}^{Q-1}
 \left|\frac1N\sum_{j<N}
   \mathbb E\left[e^{2\pi i hR_j/Q}
                    \overline{e_{h/Q}(X_j)}\right]\right|^2.
 \tag{6}
\]

Separate decay of the compact-character expectation does not estimate the
mixed expectation. Replacing it by a product of expectations removes the
shared variable whose cancellation is exactly the endpoint label. The
real phase in (5) is defined using the physical representative; it is not
a continuous function of the compact class alone.

The actual complete-carry/source-box identity in the pinned PR182 is a
discrete way of retaining this missing lift. Its within-box injection does
not bound the cross-box terms in (6). An estimate for this same original
observable remains the first missing closing input.

## 5. Literature application attempted

The coordinator opened and inspected Einsiedler--Lindenstrauss,
*Rigidity properties for commuting automorphisms on tori and solenoids*,
Theorem 1.2, at
<https://arxiv.org/pdf/2101.11120>. It classifies positive-entropy ergodic
probabilities for a totally irreducible, non-virtually-cyclic joint action.
The new PR175 constructs a law with those action hypotheses. It does not
make the ordinary endpoint a factor of that commuting action.

Hochman--Shmerkin, *Equidistribution from fractal measures*, Theorem 1.1,
was inspected at
<https://math.huji.ac.il/~mhochman/preprints/normality.pdf>. Its normality
criterion requires a nontrivial ergodic distribution generated by the
measure's scenery and the stated absence of resonant eigenvalues. Positive
information dimension by itself supplies neither hypothesis. No such
scenery-generation or spectral statement was proved for the canonical
boundary in this attempt.

Even if an appropriate stronger real equidistribution or Fourier theorem
were established, (3)--(6) show why the original endpoint still has to be
retained in its consumer. This pass supplies that exact test and no
same-limit collision upper bound. The results here are written arguments;
they are not claimed to be newly formalized in Lean.

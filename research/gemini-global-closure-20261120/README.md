# Gemini's five routes: actual transport, exact algebra, and the global boundary

**Collatz is not resolved.** This packet audits the complete supplied proposal,
then pursues its potentially useful change of function space on the actual
ordinary-integer return dynamics. The new results have written proofs and
bounded independent arithmetic checks; they are **PROPOSED** for mathematical
review, not additions to the accepted integrated baseline.

The map throughout is the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Main is frozen at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The current
source comparison also freezes PR146 at
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, PR147 at
`b74b2d466f58844a742a6ed6bcdf06844269f361`, PR148 at
`6ff18e4f63be8f3bece76215fcfe44d83b001d7f`, and PR149 at
`92c0129e794dde3ec55ceec470a12d51ba3f7e2f`. Later heads are outside this
review. These branches are context, not wholesale imported dependencies.

## 1. The useful positive result: an actual invariant input domain

The resident moving-rank construction has a total acceleration `A`, a proper
integer rank `R`, a quarter-safe set `G`, and a complementary unsafe set `U`.
Its map `B` takes one unsafe step and eliminates the subsequent finite safe
excursion. Let `H` push mass along this **actual** return, killing at 1.

The existing unsafe family sends rank proportional to `x` to rank proportional
to `x^2`. We show that it destroys **every positive power moment**: for every
`p>0`, some positive full-support summable input has finite `R^p` moment and
infinite output `R^p` moment. In particular, the proposed square-root change
does not repair the actual transport problem.

There is nevertheless a valid repair. For

\[
\ell(n)=\log(R(n)+6),\qquad
\psi(n)=1+\log\ell(n),
\]

the exact physical return satisfies

\[
\ell(Bn)\le6\ell(n),\qquad
\psi(Bn)\le\psi(n)+\log6
\]

whenever it survives. Thus every positive power of a logarithmic rank moment
is preserved after every finite number of returns. Safe occupation and its
truncation error can be controlled in these same reusable domains. There is
no resampling of digits or replacement of the transported input by a fresh
distribution. [Definitions, full proofs, and precise bounds](ACTUAL_TRANSPORT.md).

This is an operator-domain result, not a decreasing rank. Its constants still
permit indefinitely many unsafe returns.

## 2. The exact spectral boundary of that repaired space

On `X=ell^1(psi)`, the same ordinary operator has

\[
\|H^j\|\le1+j\log6/\psi_*,\qquad
\|H^j\|_{\mathrm{ess}}=1\quad(j\ge1),\qquad
r(H)=r_{\mathrm{ess}}(H)=1.
\]

The lower bound comes from infinitely many **finite positive ordinary**
`111010` shadows already constructed in the resident unsafe-return packet.
They also give approximate eigenvectors at spectral point 1 with disjoint
escaping supports. These facts survive killing any fixed finite floor.

Consequently a strict spectral gap in this particular repaired space cannot
be the missing proof. This does not decide whether each fixed integer is
eventually absorbed: arbitrarily long finite transients are compatible with
termination of every individual source. The distinction between point-mass
absorption, unweighted strong stability, and weighted strong stability is
spelled out in [the transport proof](ACTUAL_TRANSPORT.md) and
[the source-persistent target](SOURCE_PERSISTENT_TARGET.md).

## 3. The full-solution target keeps the same initial atoms

For one fixed summable input `f>0` on every unsafe state, form
`mu_N=N^(-1) sum_(j<N) H^j f`. Let `D` denote its nonabsorbing, nonperiodic
starting states. The resident rank count `N_R(X)<9 sqrt(X)` gives the exact
inequality

\[
\|\mu_N\|_\psi\ge L_N\sum_{u\in D}f(u),\qquad
L_N\sim\log\log N.
\]

An actual `o(log log N)` Cesaro moment bound would therefore exclude every
divergent ordinary orbit. A complete exclusion of nonabsorbing finite cycles
would then finish Collatz. Neither is proved. The available additive return
budget gives only `O(N)` for this average. Alternatively, uniform Cesaro
tightness together with cycle exclusion is an exact conditional closure
criterion. [Proof and the additional excursion condition hidden in weighted
strong stability](SOURCE_PERSISTENT_TARGET.md).

These statements identify the remaining quantified estimate. They do not
replace it with small Haar measure, changing finite witnesses, or a numerical
matrix radius.

## 4. What survives of each supplied route

| Supplied route | Valid content | Missing or incorrect step |
|---|---|---|
| 1: affine mergers | The 43 whole-cylinder identities and their `41/256` measure replay; the factor-five obstruction is correct. | Affine certificates are stronger than ordinary meeting. Known convergent parameters never enter this certificate class. Descent of `5t+1` below `t` alone does not merge their orbits. |
| 2: inverse compiler | The finite Bellman inequalities can be checked exactly. Our primal/dual replacement proves optimal slopes **1 optimistic, 3 robust** for the supplied mod-27 graph. | Choosing the next unseen ternary lift does not control a fixed ordinary source. A global minimum cycle is insufficient without reachability; iteration timeout is not a negative certificate. |
| 3: fractional moments | The randomized binary matrix has exact radius `(2^-alpha+(3/2)^alpha)/2`, strictly below 1 for `0<alpha<1`. | The killed matrix removes every even current state and has radius exactly `(3/2)^alpha/2` at every precision. It kills the wrong event for a fixed original floor. Actual `R^p` moment failure remains for every `p>0`. |
| 4: SC/FC and Padé | The conditional SC+FC implication and elementary affine identities are valid. | FC is Terras's coefficient-stopping-time conjecture. The radical prototype uses the wrong Taylor sign and is an exact binomial power, not the native partial-theta approximant. The claimed period-through-twelve evaluation was not performed. |
| 5: transducer and Lean | The `959/1024` finite-prefix forward-descent measure and `121 -> 182 -> 91` replay. | No composable merging transducer, total mode semantics, or reset proof is implemented. The tuple validator even accepts a negative rank coordinate. The Lean file is an uncompiled skeleton in this pass. |

[Routes 1 and 5](ROUTES_1_5_AUDIT.md) ·
[Exact binary spectra and inverse-game certificates](AVERAGED_CHAIN_AUDIT.md) ·
[Route 4 and the complete radical-family classification](HERMITE_PADE_AUDIT.md).

## 5. A complete algebraic audit of the proposed Padé family

The supplied cubic example is exactly
`((1+z)^(1/3)-1)^8`. More generally, put `y=(1-z)^(1/m)`. With equal degree
budgets `d`, every nonzero maximal-contact form in the full basis
`1,y,...,y^(m-1)` is `c(y-1)^(m(d+1)-1)`.

For **arbitrary unequal budgets**, the support of exponents gives an explicit
Vandermonde formula for the unique maximal-contact polynomial. In primitive
integer normalization,

\[
R_S(y)=(y-1)^{|S|-1}Q(y),\qquad
Q\in\mathbb Z_{\ge0}[y],\quad Q(0)\ge1.
\]

Thus `Q(y)>=1` on the entire nonnegative real axis: asymmetric budgets do not
create a second small real factor. The proof includes an elementary positive
branching identity for generalized Vandermonde quotients. The determinant norm
contains the entire known difference-of-powers factor. These are statements
about this precise maximal-contact radical family; other approximation spaces,
lower-contact constructions, and the native partial-theta program remain open.

## Reproduce and review

The [unmodified input archive](../../archive/gemini-proposals-20261120/README.md)
preserves all fifteen supplied files and their hashes. Its original five
scripts passed, and the original receipt was reproduced byte-for-byte. That
fact does not validate every sentence of their documents.

Run the three scoped arithmetic checkers in normal and optimized Python:

```bash
python -X utf8 -B research/gemini-global-closure-20261120/run_checks.py
```

They use only the standard library. Optional `--replay-upload` also reruns the
original five scripts in a temporary copy and requires NumPy, as the upload
does. Bounded checks support the written proofs; they are not formal proof
verification or a convergence census. No Lean executable was available in
this environment, and no Lean build is claimed.

[Review and execution record](../../reports/2026-11-20-gemini-closure/README.md).
The repository validation receipt is tied to a separate scientific-content
commit; it does not self-certify the later receipt commit.

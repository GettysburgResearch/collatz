# Attempts to turn shifted-core arithmetic into global closure

**Status: OPEN.** The companion `SHIFTED_CORE_TRANSITIONS.md` contains a
source-qualified positive result: a uniform finite bound for distinct
ordinary defect transitions with a prescribed ordered pair of shifted
cores. This note records the attempted closing steps, including an
exact local failure and the remaining fixed-source obligations. Neither
an infinite counterexample nor a full Collatz proof has been found.

## 1. Frozen research inputs and the actual difference in scope

| Input inspected | Exact pin and scope used |
| --- | --- |
| PR154 | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0`, `research/structural-reset-20261120/adelic/PRIME_HEIGHT_ESCAPE.md`, ADEL-001–ADEL-007; `CLOSING_ATTEMPT.md`; `ADELIC_LEDGER.md`. These concern prime height of the actual odd states `n_j`. |
| PR156 | `c5cb84502c7289705d59a8781a65fd845b9b6b14`, `research/global-rigidity-20261120/SHIFTED_LINEARIZATION.md`, equations (1)–(8); `FIXED_SOURCE_CLOSURE.md`, FS1–FS3. These give the exact shifted approximation product and preserve its unproved algebraicity and power-saving requirements. |
| PR145 | `dd245a712f985909f541590e3f6c179b7ba011e4`, `research/pointwise-run-defects/COMPRESSED_DESCENT.md`, final growing-number-of-powers consequence. This is the separately stated optional input for the superlogarithmic defect count. `research/unsafe-return-weights/VALUATION_ONE_RUNS.md` was also read; its displayed total-excess result must not be substituted for a count of non-one exponents. |
| Concurrent PR157 | `64361ecca770092d6c8242dc6211e38818af2e50`, `research/global-closure-20261120/arithmetic.md`, GA-001–GA-005. Its exact long legal blocks and its valuation-three recharge example already show why local arithmetic constraints and a simple recharge budget do not settle the fixed-source problem. |

The new interface is shifted: remove the primes in a fixed pool from
`n_j+1`, then count **defect edges** connecting prescribed cores. Its
uniform S-unit count is not a new version of the prime-height theorem
for `n_j`, and it does not improve every multiplicative-rank theorem.

For an external comparison, the primary text of
[Prime-power returns and multiplicative complexity of Collatz orbits,
rStation Paper 138, version 1](https://rstation.ai/problems/collatz/papers/138)
was inspected. Its Theorems 1–2 give uniform visits to multiplicative
cosets and strong rank growth for positive-density samples of the
unshifted odd states. Its later results give prime-free cofactor
restrictions. Those are substantial precedents, not prerequisites of
the present argument. Its statements are not independently approved
here as a whole. A shifted-core edge count and an unshifted-state rank
count are different observables; no overall dominance or broad novelty
claim is made.

The external load-bearing input here is Evertse's Theorem 3, with its
precise parameters stated and checked in the companion proof. The
coordinates `n+1=2^sigma 3^tau q`, the finite run of ones, and classical
S-unit finiteness are established tools, not inventions of this packet.

## 2. Attempt A: a finite renewal graph, and the exact missing bound

Let `m=n+1` and initially take the pool `P={2,3}`. The shifted core
`q=m/(2^sigma 3^tau)` stays unchanged during exponent-one runs. At a
defect `a>=2`, one has `sigma=1`, and the exact relation is

\[
 2^{a-1}m'=3^{\tau+1}q+(2^{a-1}-1).                 \tag{1}
\]

Consequently

\[
 \gcd(q,q')\mid 2^{a-1}-1.                          \tag{2}
\]

The same divisibility holds for any finite prime pool containing 2 and
3. To prove it, a common core divisor is coprime to 2 and 3 and divides
both shifted endpoints; (1) then makes it divide the last summand.

The hoped-for route was to view defects as transitions on a graph of
cores, prove that one ordinary source can access only a bounded amount
of that graph, and use the finite transition theorem. The positive
part succeeds: every ordered pair of vertices supports at most `B_s`
distinct actual defect edges, with no valuation cutoff. A finite vertex
set therefore cannot support an escaping ordinary orbit.

The first unsupported step is the proposed bound on the **accessible
vertex set**. Equation (2) bounds retained common factors, not newly
created factors. In particular it supplies no finite outdegree theorem.

### A1: exact one-defect creation of arbitrarily large outside cores

Fix any finite prime pool `P` containing 2 and 3. For an integer
`k>=1`, put

\[
 n=2\cdot3^{2k}-1,\qquad
 n'=\frac{3^{2k+1}-1}{2}.                            \tag{3}
\]

Then

\[
 a(n)=2,\qquad U(n)=n',\qquad
 n+1=2\cdot3^{2k},\qquad
 n'+1=2\,\frac{3^{2k+1}+1}{4}.                      \tag{4}
\]

Indeed, `3^(2k+1)=3 mod 8`, so `v_2(3n+1)=2` and
`v_2(n'+1)=1`; also `3` does not divide `n'+1`.

Choose `k` to be a positive multiple of every `ord_p(3)` for
`p in P` other than 2 and 3. This is a fixed nonempty arithmetic
progression; if there are no such primes take every positive `k`.
For each extra prime,

\[
 \frac{3^{2k+1}+1}{4}\equiv1\pmod p.
\]

It follows exactly that

\[
 R_P(n+1)=1,\qquad
 R_P(n'+1)=\frac{3^{2k+1}+1}{4}\longrightarrow\infty. \tag{5}
\]

Thus one defect of the fixed size `a=2` transfers an arbitrarily large
amount of shifted logarithmic height into primes outside **any
prescribed finite pool**, even though the incoming shifted core is
one. No factorization of the large endpoint is needed. The input and
output are genuine ordinary integers and the edge is exactly legal.

This refutes a proposed local charge of the form

\[
 \log R_P(n'+1)\le F(R_P(n+1),a(n),P)                \tag{6}
\]

for any fixed finite-valued function `F`: its right side is the single
constant `F(1,2,P)` along (3), and its left side is unbounded. In
particular a fixed valuation cost cannot pay for new core height.

The ordinary source in (3) varies with `k`. This family does **not**
refute an accumulated bound for one fixed source, establish an
escaping orbit, or show that every member converges. Its scope is the
specific one-step attempted bound (6).

The mechanism differs from PR157 GA-005, which creates an arbitrarily
long next binary run using one valuation-three step. Both statements
show that a resource can be replenished at bounded local division cost;
the present resource is outside-pool shifted prime height. GA-005 is
credited as the prior recharge obstruction, rather than relabeled as
a new broad impossibility result here.

## 3. Attempt B: allow the prime pool to grow with the observed prefix

The uniformity of Evertse's theorem genuinely permits this finite
operation. For a simple `N`-transition prefix, let `P_N` be the union
of 2, 3, and every prime dividing any shifted value `n_j+1`,
`0<=j<=N`. Put `s_N=|P_N|`. All the corresponding cores are one, so
SC2 gives

\[
 D_N\le(9\cdot2^{35})^{27(s_N+1)}.                  \tag{7}
\]

Whenever `D_N>=1`,

\[
 s_N\ge\frac{\log D_N}{27\log(9\cdot2^{35})}-1.    \tag{8}
\]

This uses one pool for the entire prefix, not a separate pool for each
state. It retains the actual coefficients in the unit equation and
does not need a hidden bound on their sizes.

The bound proves a required growth of shifted prime support. It gives
no contradiction: a growing ordinary history can keep acquiring primes.
PR154's height dispersion concerns the factorization of `n_j`, whereas
(8) concerns the union of primes in `n_j+1`. Neither theorem supplies
an upper bound on the other's resource. Even a prime-free cofactor
lower bound or an unbounded number of independent prime coordinates
is compatible with both conclusions.

The first unsupported implication is an upper bound on the same
growing prime pool, or a bound on the number of cores, strong enough
to conflict with these lower bounds. The finiteness of each individual
integer's factorization does not provide such a bound for one infinite
history.

## 4. Attempt C: combine the exact shifted core with the real limit

For a hypothetical nonperiodic odd ternary-unit orbit, retain the
normalization of PR156:

\[
 \lambda_j=2^{A_j}/3^j,\quad
 L_j=\lambda_j n_j\uparrow L<\infty,\quad
 M_j=\lambda_j(n_j+1)\uparrow L.
\]

Existence of this finite limit uses the reciprocal-sum theorem pinned
in PR156; it is not re-proved by SC1. Write `q_j=R_{\{2,3\}}(n_j+1)`.
PR156's exactly primitive two-coordinate product is

\[
 \mathcal P'_j
 =\frac{L-M_j}{\lambda_j2^{\sigma_j}3^{\tau_j}}
 =q_j\frac{L-M_j}{M_j}.                             \tag{9}
\]

The second equality is immediate from the core factorization and
keeps the entire outside-prime cofactor. It shows exactly what the new
core information would need to control: the product of core size and
the relative error at the **same time**.

The primitive coordinates remain

\[
 p_j=\frac{2^{A_j}(n_j+1)}{3^{\min(j,\tau_j)}},\quad
 d_j=3^{j-\min(j,\tau_j)},\quad
 H'_j=\max(p_j,d_j).                                \tag{10}
\]

Here `d_j` is the rational denominator, and `q_j` in (9) remains the
shifted core. In particular the possible 3-adic cancellation when
`tau_j>j` is retained.

For a Subspace-Theorem contradiction with those fixed forms, the two
open inputs are still:

1. the actual limit `L` is algebraic;
2. for some fixed `eta>0`, infinitely many actual times satisfy
   `q_j (L-M_j)/M_j <= (H'_j)^(-eta)`.

SC1 bypasses the unknown algebraicity in proving finite core-pair
transitions, because its unit equation has fixed rational coefficients.
It does not prove either input above. A lower bound on the number of
different cores does not give an upper bound on the error correlated
with those cores. Moreover, every core can grow while the relative
error shrinks; the separate limits do not compare their rates.

Adding all primes of the current core to the list of places would
formally remove its factor from the product, leaving the relative
error alone. But this changes the set of places with time. The fixed
set required by the invoked theorem has then been lost, and every
new finite prime consumes the parameter in (7). Treating that removal
as a free simultaneous saving would drop precisely the arithmetic
resource the transition theorem says must grow.

Replacing `L` by a fixed algebraic constant different from `L` has
already been checked in PR156 equation (8): the product has a positive
liminf. Using a new algebraic approximation at every time introduces
moving forms and coefficient heights. No estimate paying those costs
was obtained here. The natural periodic pin likewise retains the exact
positive integer factor of FS1; it yields no independent gain from
its complete reduced denominator.

## 5. Current outcome and remaining full-proof obligation

The successful result is uniform finiteness for prescribed shifted
core **transitions**, including an explicit bound independent of the
core values and of the division exponents. It gives actual escape
exclusion under finite shifted prime support, a finite-prefix defect
complexity inequality, and a quantitative growth requirement on every
hypothetical ordinary escape.

The global attempt remains open at a source-persistent control of
new cores, or another arithmetic mechanism that excludes their
unbounded creation. The one-step family (3) shows why the most direct
local charge cannot provide that control. The exact approximation
identity (9) states the alternative missing correlation without
discarding primitive normalization or substituting changing rational
completions for one fixed integer.

These arguments also leave arbitrary nontrivial positive cycles open.
Their finite core graphs satisfy the finite edge count, and no complete
cycle denominator has been shown impossible. A proof of eventual
periodicity under an additional support hypothesis is not a proof of
arrival at 1.

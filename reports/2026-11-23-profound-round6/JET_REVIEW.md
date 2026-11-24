# Independent review of the actual arithmetic-germ criterion

Reviewer: `collision_renyi6`. Date: 23 November 2026.
Parent checkpoint: `afe6f4d1a661b377c9daa4623bdd732ba478386b`.

**Verdict: VERIFIED written cycle-prime and pole claims; VERIFIED
source-qualified conditional J3 consumer at the frozen identities below.
No unconditional construction of J3 or limiting parity density is
verified. Full Collatz remains OPEN.**

The reviewer independently reconstructed the arithmetic, polynomial,
local-radius, and potential-matrix arguments. Agreement between the two
author lanes is not used as evidence. This review does not claim a Lean
formalization of the analytic rationality theorem.

## 1. Content and dependency boundaries

The new files were reviewed by these exact Git blob identities, before
their enclosing round-six commit. A later file with the same path is
outside this review unless its content is unchanged.

| New local file | Reviewed blob |
|---|---|
| `research/profound-round6-20261123/RATIONAL_SELECTION.md` | `54d7949ac80ec6b8286f0d03d579f9f6e0efe95f` |
| `research/profound-round6-20261123/RationalSelection.lean` | `844bcb91635d41a7bbe03dffc38e55508edb0600` |
| `research/profound-round6-20261123/CYCLE_ARITHMETIC.md` | `3b406dc7a71a1a43fa6f3771a9ddab1f5f237713` |
| `research/profound-round6-20261123/CycleArithmetic.lean` | `431231784098ef63fd356d8bc4b5f9eb442fec1b` |

Whitespace normalization: the reviewed rational-selection note originally
had blob `9d8a10ed4266e07f2a54dc050c624cea33c19f6a`. A byte comparison
against that version in the Git index verified that the new blob above
removes exactly one extra final newline, from 17,582 to 17,581 bytes;
all remaining bytes are identical. The mathematical review is unchanged.

The exact external repository inputs read for this review were:

| PR and full head | Path and blob |
|---|---|
| PR178, `398b3a04da071e96362005792417bd5cf8cc6497` | `research/literature-push-20261123/rigidity/GENERAL_DENSITY_JET.md`, `5a4250dfc3b976dd5eb552d4a4b008ec19a120ee`: the stated theorem and complete small-hole/game argument. |
| Same PR178 head | `research/literature-push-20261123/rigidity/SCALAR_BOUNDARY_AND_SECOND_CENTER.md`, `951a88535220cf0673dd7a9186b0751368c76ce6`: actual series, full Jet definition, local domains, and critical matrix. |
| PR180, `7cfd911d35382d9d3bc988060ba88ade78a4267e` | `research/profound-step-20261123/HOLONOMICITY.md`, `01a5d159730960894e903cd91e04550b05ba1d64`: Sections 3--4, the elementary rational-series to eventual ordinary periodicity consumer. |

The review applies to the stated claims in these paths, not neighboring
claims, complete PRs, or their later heads.

## 2. Ordinary source, full numerator, and every conjugate pole

**R6-SEL-1: VERIFIED.** The actual preperiod and repeated word give

\[
B_n(z)=\frac{C_a(z)(3^p-z^A)+z^hC_w(z)}{3^s(3^p-z^A)}.
\]

The carry-polynomial recursion and concatenation keep chronological
order. At `r=3^(p/A)>0`, the numerator becomes `r^h C_w(r)>0` because
the period has an odd input. Thus the complete rational expression has
a genuine positive real pole. Its actual finite preperiod cannot
cancel it. This directly addresses full polynomial cancellation; a
numerical denominator factor at `z=2` is not assumed to survive.

With `g=gcd(A,p),u=A/g,v=p/g`, the factor `F(z)=z^u-3^v` is
irreducible. I checked both author arguments. A monic rational factor
of degree `d` is integral. Its nonzero constant term has three-adic
valuation `dv/u`, since every root has valuation `v/u`. Integrality of
that valuation and `gcd(u,v)=1` force `u|d`. Equivalently, the complex
absolute value of that constant term gives the same divisibility by
unique prime factorization. Hence no proper factor exists.

The minimal polynomial `F` must divide the reduced denominator of
`B_n`; otherwise the positive root would not be a pole. The reduced
numerator is coprime to `F`. Bezout's identity remains valid after
extension of fields, so **every** conjugate root remains a pole over
every characteristic-zero completion. No favorable conjugate is chosen
before establishing this fact.

## 3. Complete prime-power obstruction and the ordinary cycle

**R6-SEL-2 and R6-SEL-3: VERIFIED.** Let
`D_red=2^u-3^v>0` and let a prime `ell` divide it. Such a prime is
different from two and three. Every root `alpha_i` of `F` is an
`ell`-adic unit, and every `2-alpha_i` has nonnegative valuation.
Their complete product is `F(2)`, so

\[
\sum_{i=1}^u v_\ell(2-\alpha_i)=v_\ell(D_{\rm red}).
\]

Some translated root therefore has valuation at least
`v_ell(D_red)/u>0`. It is still a pole by Section 2. If the Taylor
series at two converged on a larger disc, its formal identity with the
reduced rational function could be evaluated at that root; it would
force the reduced numerator to vanish there. This is a contradiction.

[Conrad, *Infinite series in p-adic fields*, Theorem 3.7](https://kconrad.math.uconn.edu/blurbs/gradnumthy/infseriespadic.pdf)
was checked in its original statement: over a complete nonarchimedean
field, the reciprocal convergence radius is the limsup of the roots of
the coefficient absolute values. It applies after passing to a complete
extension containing the pole. Consequently

\[
\limsup_{j\to\infty}
\frac{v_\ell(\operatorname{den}(c_j))}{j}
\ge\frac{v_\ell(D_{\rm red})}{u}>0.
\]

This keeps the entire prime power in `D_red`, not only its radical.
Membership of all coefficients in `Z[1/M]` therefore forces every prime
divisor of `D_red` to divide `M`.

**Cycle classification and R6-SEL-4: VERIFIED.** The actual positive
ordinary cycle equations give

\[
3^p<2^A=\prod_i(3+1/q_i)\le4^p,
\]

and the final equality holds only if every odd state is one. Positivity
and ordinary integrality are used here; this inequality would be false
for arbitrary small positive rational states. If `D_red=1`, reduction
modulo eight forces `(u,v)=(2,1)`, hence `A=2p` and equality in the
product bound. The cycle is therefore the standard shortcut cycle.
A nonstandard positive cycle has `D_red>1` coprime to six and supplies
a forbidden prime when `M=3`. This proves the claimed equivalence for
sources already known to be eventually periodic.

## 4. Primary rationality theorem: hypotheses actually needed

I read [Chambert-Loir--Noûs, *Potentiel et rationalité*](https://arxiv.org/pdf/2305.17210),
Sections 2.3 and 4.1--4.3, and confirmed from its
[arXiv record](https://arxiv.org/abs/2305.17210) that the inspected version
is v2 of 31 August 2026. Theorem 4.3 concerns formal functions at finitely
many rational points of a smooth geometrically connected projective
curve over a number field. At every place, one meromorphic function on
an analytic neighborhood must realize all those germs. It requires a
proper smooth integral model over a finitely generated ring, formal
integrality there, and the prescribed reduction neighborhoods outside
the exceptional primes. A strictly positive potential-game value then
gives one rational function. Section 2.3 permits disconnected analytic
domains; it does not require complex gluing across disjoint components.

The older [Bost--Chambert-Loir theorem](https://webusers.imj-prg.fr/~marco.maculan/java/2016/files/BostChambertLoir.pdf),
Theorem 7.9, requires the local meromorphic extensions, A-analyticity of
the formal graph, and strictly positive capacitary degree. Its following
condition `2'` supplies a sufficient integral-model hypothesis. I checked
that statement and Example 7.10. It is background for the multipoint
consumer, not a replacement by an equality-case theorem.

These primary statements are used as external theorems. Their entire
general proofs are not newly formalized or audited by this report.

## 5. Independent reconstruction of the J3 consumer

**R6-SEL-5: VERIFIED as a source-qualified conditional implication.**
The exact assumptions remain:

1. The parity density of this fixed actual source has a limit
   `p_k/k -> rho`; a subsequential density is insufficient.
2. The entire literal binary germ `J_n(t)=B_n(2+t)` has coefficients
   in `Z[1/3]`.
3. This same rational-coefficient series has positive radius at the
   complex place and at three.

The scalar value `c_0=-n` alone supplies neither item 2 nor item 3.
At two, the actual original series converges on the unit disc, so it
realizes both full germs there. At all other finite places, the two
unit discs are disjoint except for the finitely many smaller discs
specified in the source. The ring condition supplies the common
integral model over `Z[1/6]` for J3. These are the source's own objects,
not a newly selected series agreeing only at the constant coefficient.

Writing `R=3^rho`, the original complex and ternary radii are `R` and
`1/R`. There are infinitely many odd inputs in a positive ordinary
orbit; hence the root test along those nonzero coefficients gives the
stated exact radii even at endpoint densities.

I rechecked the potential matrix, with `L=log2`:

\[
\begin{pmatrix}a_\epsilon&L\\L&b_\epsilon\end{pmatrix},
\qquad b_\epsilon=\log\epsilon+C.
\]

For `R<=2`, disjoint complex discs make
`a_epsilon=-O(epsilon)`, and their product with `b_epsilon` tends to
zero. For `R>2`, removing a disc around two from the first complex
component is legitimate: the two local realizations are then defined
on disjoint components. The maximum-principle comparison in the source
gives a loss `delta_epsilon` satisfying

\[
\limsup_{\epsilon\downarrow0}
 \delta_\epsilon|\log\epsilon|
\le(\log(R/2))^2.
\]

I checked its two boundary estimates, the harmonic extension through
zero of the Green-function difference, and the comparison with the
Green function having pole at the removed center. They give the stated
bound without assuming an asymptotic capacity formula. Since `R<=3`,

\[
\limsup a_\epsilon b_\epsilon
\le(\log(3/2))^2<(\log2)^2=L^2.
\]

For negative diagonal entries the source's row weight is in `(0,1)`
and yields the positive payoff
`(L^2-a_epsilon b_epsilon)/(2L-a_epsilon-b_epsilon)` against either
column. Thus the strict game hypothesis is supplied under the three
listed assumptions, and the external theorem yields rational `B_n`.

The subsequent arithmetic consumer was also reconstructed, rather
than inferred from rationality alone. A constant recurrence for the
rational series, multiplied by `3^(p_k)`, has a normalized window
depending only on a fixed finite parity block. Its last nonzero
coefficient determines at most one next bit, so the finite block graph
is eventually periodic. For a repeated block, the full denominator
identity then makes arbitrarily large powers of two divide one fixed
ordinary integer. That integer is zero, forcing state periodicity.
The all-even tail would force a zero state and is excluded by positivity.

Section 3 now excludes every nonstandard positive cycle. The limiting
density is retained throughout this implication; this review does not
prove that it exists for every source.

## 6. Converse, cancellation control, and proof boundary

**The reverse direction and the common denominator: VERIFIED.** If the
actual source hits one after a prefix with `s` odd inputs, then

\[
3^sJ_n(t)=C_a(2+t)-\frac{(2+t)^h}{1+4t+t^2}\in\mathbb Z[[t]].
\]

The denominator has constant coefficient one. The complex radius is
at least `2-sqrt(3)`, the ternary radius is at least one, and the
eventual parity density is `1/2`. Thus actual convergence supplies all
three assumptions above. The same positive integer `3^s` clears every
Taylor denominator, which is stronger than J3.

I also checked the complete rational fixture `w=110000`: it gives
`B(z)=(3+z)/(9-z^6)`, `B(2)=-1/11`, and
`B'(2)=181/605`. The prime five disappears at the constant value but
appears in the actual derivative, as claimed. The fixture is explicitly
a rational cycle, not an ordinary counterexample. The cocycle
`2d(Tx)=3^(x mod2)d(x)+Tx` and the displayed zero `d(85)=0` are
consistent with the differentiated actual tail identity.

The finite Lean files have the stated narrower scope: chronological
carry-polynomial positivity and noncancellation, and actual positive
cycle clock/prime arithmetic. This report inspected their statements
and attachment; the root's integration receipt is responsible for the
fresh compilation and full axiom audit. No claims about that later
execution are made here.

**First unsupported step:** construct J3 for an arbitrary fixed positive
ordinary source, together with a limiting parity density, or replace
those inputs by an actually proved source condition. Rationality of the
first unknown derivative is not known here. The new result removes the
separate nonstandard-cycle obligation from this conditional route; it
does not discharge the germ-construction obligation.

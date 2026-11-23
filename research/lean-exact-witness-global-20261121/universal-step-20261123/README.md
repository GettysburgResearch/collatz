# Three attacks on the universal construction and ordinary closure

23 November 2026. **Full Collatz, the residue-512 implication, and
`FloorIntervalStep` remain OPEN.** This checkpoint continues PR177 from
`f47a5ec51aa5853f104013a6d5046d6220ff7423`, after reading the changed
interfaces in PR176, PR178, PR180, and PR182 at their frozen latest heads.
Three parallel lanes pursued candidate construction, ordinary escape,
and complete integer-cycle exclusion. A coordinating argument extends
the cycle result to contracting blocks with unequal shapes.

The positive results are a polynomial-time exact candidate recognizer,
an all-period ordinary cycle exclusion for unbounded block families,
and a complete ordinary inverse-tree transport. The escape lane also
derives a necessary summability law on one unchanged forward source.
None of these supplies universal candidate existence, the missing
source-specific comparison, or coverage of arbitrary cycle words.

## 1. Exact recognition in the numerator's binary length

The [candidate theorem](candidate/NEGATIVE_NUMERATOR_RECOGNITION.md)
uses the first sign crossing of the actual complementary pair. For a
reduced negative candidate `-A/3^r`, with `A>0`, every compatible step
that stays negative and retains a positive denominator satisfies

\[
 2|w_{j+1}|\le |w_j|.
\]

A successful candidate has the forced terminal segment

\[
 (8,-1/9)\longrightarrow(4,1/3)\longrightarrow(2,1)
 \longrightarrow(1,2).
\]

It therefore has the new bounds

\[
 \boxed{\tau(n)\le\operatorname{bl}(A)+2,\qquad
 A\ge3^r-2^{r+1},\qquad 3^r\le9A.}
\]

The sharp height equality is attained exactly by `n=2^(r+1)`, `r>=2`.
The only nonnegative accepted values are `(n,Omega(n))=(1,2),(2,1),(4,1/3)`.

The [total recognizer](candidate/negative_candidate.py) reduces the
presentation, filters a giant binary exponent before constructing its
power, and performs at most `bl(A)` paired transitions. It accepts only
the exact first crossing `(4,1,1)` in numerator/exponent coordinates.
It emits an ordinary hit and, for odd inputs, the full increasing
exponent tuple satisfying the user's original equation.

This removes the old quadratic `log F(r)` charge from **exact candidate
verification**. It is not a shorter congruence-only theorem: the wrong
candidate `(n,a,r)=(24,-1,2)` matches three initial parity bits but is
rejected at its wrong crossing. A supplied candidate is decided in
polynomial bit complexity; no successful candidate is constructed for
an arbitrary original target.

[NegativeCandidate.lean](candidate/NegativeCandidate.lean) proves thirteen
finite declarations: literal halving, clock and sharp backward-code
bounds, executable ordinary-hit soundness, and completeness for literal
first-crossing certificates. The full equality-to-Omega interpretation
uses the pinned previous rigidity theorem and the written forced-tail
argument. It is not counted as a newly formalized infinite-conjugacy result.

## 2. Full denominator and ordinary lattice exclude arbitrary block mixtures

For equal-shape parity blocks with `A>0`, `p>0`, write `P=3^p`, `Q=2^A`.
Let their carry span be `Delta>0`, and let `G>0` divide every carry
difference. The [new capacity theorem](cycles/BLOCK_CARRY_CAPACITY.md)
proves that a nonconstant positive integer boundary cycle of any block
length `N` must satisfy

\[
 \boxed{\Delta\gcd(G,Q^N-P^N)\ge G(P+Q).}
\]

The whole denominator forces all boundary differences into a common
integer lattice. An edge entering the global minimum and an edge leaving
its minimum plateau then pay at least one lattice step on each side.
This proves an all-word statement, not a finite period census.

For two distinct blocks, let `delta` be their carry difference and let
`delta_*` be its part coprime to six. Every mixed cycle must have

\[
 \gcd(\delta,Q^N-P^N)\ge P+Q,\qquad \delta_*\ge P+Q.
\]

Thus `delta_*<P+Q` excludes every mixed concatenation. This covers all
adjacent-transposition pairs with arbitrary common prefix/suffix, whole
homogeneous-run transpositions, and additional nonsmooth differences.
In particular **every cyclic word over** `11101010` and `11011010` is
nonintegral, including arbitrary switches and repetitions. This resolves
the entire two-block language that obstructed the preceding local-energy
attempt, while retaining its nonintegral rational cycles.

[BlockMixture.lean](cycles/BlockMixture.lean) proves eight all-length
finite declarations, including the arbitrary closed integer-path
exclusion when the carry difference is `2^u3^v`. The larger gcd-capacity
theorem is written mathematics, with its formal boundary explicit.

### Different block lengths and odd counts

The [coordinating extension](commutator/UNEQUAL_BLOCK_COMMUTATOR.md)
handles arbitrary finite dictionaries of contracting blocks
`f_i(x)=(P_i x+C_i)/Q_i`, with `d_i=Q_i-P_i>0`.
Set `E_ij=d_i C_j-d_j C_i`, and choose a 6-smooth `s` dividing all
these cross-carry quantities. If

\[
 0<E_{ij}<s(Q_iQ_j-P_iP_j)
 \quad\text{whenever }E_{ij}>0,
\]

every closed integer boundary path over the dictionary is constant.
The proof allows repeated minima and explicitly handles pure-even blocks
using one odd reference block. For two blocks, the part of `|E_12|`
coprime to six must pay the full two-block denominator.

It also proves an unbounded sparse-defect consequence: for a contracting
word `u` and a fixed word `t` with distinct fixed-point expression,
every sufficiently large fixed `k` excludes mixed cycles over
`{u,u^k t}`. No union over changing `k` is silently substituted.

Arbitrary possible cycle words need not admit these dictionary forms.
Expanding blocks and one-block fixed points remain separate. No global
cycle exclusion is claimed.

## 3. An unchanged escaping source would force sibling mass collapse

The [ordinary basin argument](escape/SIBLING_BASIN_COLLAPSE.md)
retains the existing pressure probability `mu_s` on a hypothetical
escaping unit component. Put

\[
 A(q)=\mu_s(\operatorname{Pred}(q))=\mu_s(q)Z_s(q).
\]

For the actual ray `q_j=U^j(q_0)`, its predecessor basins increase to
the same component, so `A(q_j)` increases to one. All upper-sibling
basins `Pred(S^h q_j)`, with `S(q)=64q+21`, `h>=1`, are simultaneously
disjoint. Their exact measure scaling gives

\[
 \boxed{\sum_{j\ge0}\sum_{h\ge1}64^{-hs}
 \frac{Z_s(S^h q_j)}{Z_s(q_j)}
 \le\frac{1-A(q_0)}{A(q_0)}.}
\]

In particular each fixed-sibling ratio is summable on the unchanged
ordinary ray. An ordinary lower comparison at the nonsummable scale

\[
 Z_s(64q+21)\ \gtrsim\
 \frac{Z_s(q)}{(1+\log(q+1))\log(2+\log(q+1))}
\]

would exclude escape. The estimate is an explicit **open** closing input.

The [complete inverse-tree compiler](escape/BALANCED_INVERSE_TRANSPORT.md)
constructs a positive ordinary bijection between all finite inverse paths
from any two unit roots in the same class modulo three. It pairs the
unique parent addresses `(colour c, quotient j)` in
`e=e_c(q)+6j`. Every paired edge is legal, its signed exponent difference
lies in `{-4,-2,0,2,4}`, and the full pressure cost is exactly

\[
 W_s(\alpha,q')=2^{-s\Delta(\alpha;q,q')}W_s(\alpha,q).
\]

This compares the fixed sibling `64q+21` at every depth, with all exponents
and original source vertices retained. The remaining task is an amortized
bound on this signed cost under the actual predecessor pressure law.
The per-edge bound alone gives an exponentially discounted Green function
and does not prove the required comparison.

## Evidence and remaining goal

The [execution and review report](../../../reports/lean-exact-witness-global-20261121/universal-step-20261123/README.md)
records the **21 new core-Lean declarations**, strict compiler/axiom
audits, four new exact checkers run normally and with optimization, and
hash-bound internal reconstructions. These are distinct from the required
repository integrity gate. No historical proof corpus was rerun.

For the original implication, the construction still needs to produce a
candidate for `n=(x+1)/2` whose finite negative trace reaches exactly
`(4,1,1)`, using the unrestricted complete source witness for `x`.
The new recognizer verifies and emits the output tuple once that candidate
is supplied. It does not establish that such a candidate always exists.

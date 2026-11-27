# Independent coordinator reconstruction

This report reviews the named claims in this continuation of PR 201 from
`73a145ca99448a78219bd149e273f33b6e3fda4b`. It does not certify the entire
repository or assert the Collatz conjecture. Three GPT-6.2 Astra lanes worked
on the finite-row argument, directed affine covers, and Lean verification;
the coordinator reconstructed the load-bearing arithmetic separately.

## Exact-clock finite-row dichotomy

**Verdict: VERIFIED as a written implication, within the displayed scope.**
The outstanding upper bound is not proved. The arithmetic proof does not use
the external inverse floor F or the pair-renewal input R.

The coordinator checked the following steps of
`research/killed-green-head-closure-20261124/escape-analysis/README.md`:

1. For each positive odd ternary unit, exactly two gaps among 1,...,6
   lead to positive odd unit inverse children. This follows by multiplying
   the six units modulo nine and retaining residues four and seven.
   Deterministic forward valuation reading makes equal-depth inverse
   words injective, including when the endpoint is periodic.
2. The chronological two-gap word (f,t-f) has numerator
   `9x = 2^t z - 2^f - 3`. Prescribing x modulo `3^K` is precisely the
   stated power-of-two congruence modulo `3^(K+2)`. The order of two is
   `2*3^(K+1)`, so t above that order leaves both gaps positive. Composite
   divisibility forces both individual inverse steps, their positivity,
   oddness, unit status, and actual forward valuations. No terminal lift
   is changed.
3. A nonconverging odd unit ray has every state at least five. Therefore
   the actual suffix consumes at most
   `i*log2(16/5) + log2(q0/q_i)` shortcut steps. Choosing the tree depth
   between `ceil(b/32)` and `floor(b/16)` leaves at least
   `b/32 + 17/5 - log2(q0)` steps for the two-gap correction. The integer
   inequality `5^10 > 8*4^10` supplies the strict logarithmic slack.
4. The actual suffix has relative carry at least `1/(3*q0+1)` after its
   first odd step. A positive earlier word cannot reduce it. All paths
   end at the same actual q_i in each construction, at exactly b odd
   steps and exactly 2b shortcut steps. Equal split positions prevent
   duplicate sources. Each prescribed source class receives its own
   full family; this is not a sum over classes or averaged terminals.
5. The convergence direction uses finite simple-path sparsity, not a
   claim about a transported random law. Its proof is reconstructed
   below. A high-relative-carry path must visit a fixed finite low set.
   Assuming convergence, the complete forward images of that finite set
   are finite. This is exactly where convergence is used; it does not
   provide an independent upper estimate.

The moving terminal and its clock window are essential. This theorem does
not establish the older fixed-terminal inner liminf from the two-ended
bridge. The explicit counterexample implication covers nontrivial cycles
as well as escape, whereas the old relative-offset criterion addressed
eventual periodicity and assumed F.

The final row-only version was also checked: on escape, the linear
window of distinct actual terminals includes terminals above b/64;
on a nontrivial cycle, the fixed phase supplies a repeated state in
the recorded suffix. Under convergence, all paths ending at q>1 are
simple and the finite low-state gate makes their eligible terminals
bounded. The resulting R_b maximum therefore has the claimed
zero-versus-exponential dichotomy. It needs no forward test beyond
the recorded terminal. The fixed high-carry threshold for periodicity
follows from `exp(200/3)<2^100` on simple paths and the growing
distortion of repeated full cycle laps.

## Reconstructed finite simple-path bound

Source: T-A3-651, `research/astra-three-routes/pass3/FINITE_RECORDS.md`,
at main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The source's original
status remains preserved. The following narrow proof has been checked
independently for use here.

For a finite simple shortcut path, discard its last d odd states before
using d-step odd endpoints. With `d=floor((3/5)log2(X))` and
`M=floor(5d/3)`, the remaining low-total words have total A at most M.
Each fixes a single residue modulo `2^(A+1)`, and `2^M<=X` bounds the
number of sources in that residue by `(3/2)X*2^(-A)`. The geometric
composition sum at z=4/5 is at most `rho^d`, where
`rho^3=3125/3456`. In the high-total case, the distinct ordinary odd
endpoints are below `sigma^d X+(3/2)^d-1`, where `sigma^3=27/32`.
Endpoint injectivity bounds this population without any invariance
assumption about the truncated path.

Including the discarded terminal states gives
`2X*rho^d+(3/2)^d/2+d`. The exact inequalities
`8*3125^24 < 3456^24`, `rho>2/3`, and `sigma<rho`, together with
`log2(X)<=2sqrt(X)`, bound this by `5X^(39/40)`. The cases d=0 and fewer
than d odd states use the direct count. Integrating the finite counting
function against `dt/t^2` gives `sum(1/x)<=200m^(-1/40)` when all states
are at least m. No limiting orbit, regeneration, independent bits, or
statistical mixing is used. Repeated cycle states must not be counted
with multiplicity in this argument.

## Directed single-residue affine covers

The coordinator read the independent checker, reconstructed its five
affine rules, and checked why its finite tree covers whole progressions.
At a node `n=M*t+b`, a binary or ternary split partitions all `t>=0`
into disjoint subprogressions. Each leaf verifies all affine coefficients
and congruences through the full trace, not a sampled integer. Its final
pair is exactly `(3M,3b)`. The ordinary moves are equality edges for any
Collatz-invariant label. The extra move goes only from u to 3u with u
in one specified odd unit class, independently for the two classes.

Every queried affine function has positive slope and positive intercept.
Consequently it is injective on its leaf progression, and its ratio to
the original n lies between the two endpoint ratios recorded by the
checker. A finite collection of such maps has bounded multiplicity and
bounded scale distortion. A binary-label difference across the trace
forces a query with the same ordered labels; opposite directions cannot
be silently interchanged. This proves the stated finite-transfer
implication. Quantitative consequences importing another repository
variation theorem or a literature predecessor bound retain those named
dependencies. They are not consequences of checking the table alone.

## The earlier analytic interface stays conditional

The current primary text of rStation paper 48 was inspected at Lemma 7
(76) and Theorem 8. The bounded leading-gap change, central-total shift,
and full extra-precision congruence do give the earlier count version F
**if the reported joint floor is valid**. The renewal and selected-block
analytic proof was not independently rebuilt here. It remains an
explicit external assumption in the earlier packets. The new finite-row
dichotomy does not import it.

## Formal and computational scope

See the Lean execution report for exact source hashes, imports, printed
axiom dependencies and repaired-copy scope. The original four candidates
remain unchanged. Successful finite compilation does not formalize the
analytic assumptions or the whole-conjecture upper bound.

The four earlier BigInt controls were rerun from their published sources
and compared with their original result payloads. The replay wrapper
initially treated the differently shaped historical receipt wrappers as
result objects; this wrapper error was corrected without changing any
original control or numerical expectation. The exact constant checks
above are also in that replay. New row and affine-cover controls have
separate receipts. Repository validation is a structural check only.

The completed Lean receipt records 13 successful process executions,
46 distinct theorem declarations and 24 other axiom-audited
declarations. The original import-only warnings are retained. Final
verified modules and both generated certificate inputs have no
diagnostics. Their complete transitive axiom union is confined to
`propext`, `Classical.choice` and `Quot.sound`; the two closed finite
certificate decisions use none. The coordinator inspected the new
gap-word model, shortcut attachment, two-gap router, semantic checker,
table-to-Lean generator and the parsed receipt. This is not a fresh
independent second rebuild of the compiler or mathlib cache.

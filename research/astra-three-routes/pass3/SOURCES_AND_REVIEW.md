# Third-pass provenance, status, and adversarial review targets

All new theorem-level claims are **PROPOSED pending independent review**.
Author derivation, same-session checking, and a published commit do not promote
a mathematical claim to independently verified status.

## Frozen repository state

- Canonical main: `9704bcf1ff33cc9e2b729e0c40137a1e55b95397` (re-queried).
- PR #92 branch: `agent/astra-three-routes-01/three-route-offense`.
- Exact parent: `48e043c2822dbeea4f91c801ac2d3fc531af1466` (re-queried).
- PR #92 had no discussion/review comments when this pass began.
- No older proof or finite experiment is rewritten. New files live in pass3,
  X-ASTRA3-003, and the new report; the parent index gets an additive pointer.

Parent files, all at the exact PR #92 parent:

1. `research/astra-three-routes/ROUTE1_MELLIN.md`: killed mass convention,
   H=64 odd-predecessor eligibility, and the 69/200 sufficient ceiling.
2. `research/astra-three-routes/pass2/ORBIT_MELLIN.md`: orbit-sparsity split,
   exact parity-cylinder modulus, explicit rho certificate, and invariant-set
   recurrence. T-A3-651 supplies the missing finite-terminal correction.
3. `research/astra-three-routes/pass2/SC_TAIL_AND_ECHO.md`: qualitative
   SC-infinite-tail extraction and its source-location-versus-time boundary.
   The new finite-window clock is a separate conditional theorem.
4. `research/astra-three-routes/pass2/NONLINEAR_PROFILE_RANKS.md`: previous
   separable nonlinear-profile obstruction. The new joint-feature proof is
   independent of its coefficient-transport argument.
5. `research/astra-three-routes/CARRY_NORMALIZATION.md`: the exact whole-run
   macro. The new shadow calculation rederives its required special branches.
6. `AGENTS.md`: branch safety, scope, proof/experiment distinction, and
   independent review requirements. Its main blob remains unchanged.

The PR #91 common-rank repayment families, inspected in the preceding pass at
`b8c88843726ee7ac11cf91323c69bf911ca50706`, are context only. Their number of
returns need not be bounded, so the new bounded-macro theorem does not rule
them out. Neither that PR nor its competing README is imported or edited.
PR #90's mass work is likewise not a dependency of the new three proofs.

## External literature and priority boundary

Garcia and Tal, *A note on the generalized 3n+1 problem*, Acta Arithmetica
90(3) (1999), 245--250, is prior context for orbit-sparsity arguments. The
bibliographic record was reconfirmed at https://eudml.org/doc/207326.
This pass does not newly inspect the paper's full proof and makes no priority
claim for orbit sparsity or summable reciprocals. The explicit finite-path
argument is written locally, retaining the discarded q terminal states.
The earlier source list also credits the July 2026 public discussion of
reciprocal summability and coefficient escape. No such discussion is used
as a theorem dependency here.

No external predecessor exponent, logarithmic-form theorem, Lean build,
or unreplayed large certificate is required for the new local implications.
A complete literature novelty audit is not claimed for the boundary-charge,
record-window, or joint-feature formulations either.

## Claim matrix

| Claim | Exact scope | Main review risk | Open downstream use |
|---|---|---|---|
| T-A3-601 | Exact first surviving ordinary AP for every finite parity word | Strict floor/equality, prefix inequalities, zero residue | No all-time ordinary extraction |
| T-A3-602 | Signed residue defects for positive convex power tails, with controlled infinite remainder | Triple indexing, color dependence, omitted eligibility mass G_k | Signed all-depth cancellation |
| T-A3-603 | Uniform H>=32*2^k bias bound and fixed-floor conditional criterion | Moving floor versus fixed floor; cofinal versus finite times | No cofinal fixed-H estimate |
| T-A3-651 | Uniform finite SIMPLE-path counts and reciprocal mass | Discard terminal q odd states; never count repeated cycles with multiplicity | No basin multiplicity control |
| T-A3-652 | Coefficient records lie in an explicit near-source window | Bound location, not unconditional time | Finite local SC inputs missing |
| T-A3-653 | Local SC certificates imply descent OR repetition within R(n)N | Endpoint indexing and R(n)+1 records | Cycle exclusion still required |
| T-A3-701 | Arbitrary joint finite polynomial-valuation/residue correction fails fixed-block nonincrease | One rational center avoids ALL finite polynomial roots | Does not rule out every rank |
| T-A3-702 | Same class fails every total bounded-macro-count selector | Selector may use full n; construct K+B packets before applying it | Unbounded grouping remains open |
| T-A3-703 | Actual positive CRT shadows with identical observations and linear logarithmic growth | p-integrality at every observed prime; final endpoint odd; h=o(K) | Distinct n_K, no infinite witness |

## Failed strengthenings preserved

1. Dropping negative boundary contributions makes a sufficient bound fail
   already at k=3, H=64. This does not refute the actual bias ceiling.
2. Even the inexpensive signed root/first-curvature majorant loses the H=64
   finite pilot at k=9; retaining the full controlled curvature sum still
   certifies the ceiling through k=12. It is not a depth record.
3. H growing with 2^k does not provide one convergent fixed floor at all times.
4. A near-source record window is not known to have universal local SC bounds.
5. The finite path theorem excludes repeated states from its premise. It may
   not be summed over arbitrarily many laps of a cycle.
6. Adding arbitrary joint interactions to finitely many valuation features
   does not repair the scalar rank. Unbounded grouping or different information
   is not refuted merely by this failure.

## Computational and publication boundaries

The independent verifier uses exhaustive ordinary residues for the cylinders,
expanded second differences for the signed defects, a reciprocal square-root
integer algorithm for weights, direct orbit coefficients for records, literal
shortcut runs for macro shadows, and direct polynomial evaluation. It does
not import the generator. The implementations have the same author.

Eight report modifications are resealed and rejected, including inflated scope,
missing dictionary coverage, changed source/endpoint data, changed interval
bounds, and erased counts. The old large inverse-cone calculation, external
Lean builds/payloads, and the full-repository validator are not rerun. The
lightweight local checks do not certify any open all-time assertion.

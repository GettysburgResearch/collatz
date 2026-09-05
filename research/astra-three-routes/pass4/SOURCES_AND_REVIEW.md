# Frozen sources, mathematical scope, and adversarial review targets

Agent `astra-three-routes-04`, 2026-09-05. All new claims are PROPOSED.
This source record is not an independent mathematical verdict.

## Exact repository state used

- Current contribution: PR #92 at `7d0397c92879545609aa4097f89f5497cd53026d`.
  Its first three packets, AGENTS.md, current PR metadata, and discussion were
  read. The parent tree is `5d78e9b3647b17340dbb43f6cbb199a1a78f0b86`.
- The unchanged PR base is main `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
  No write in this contribution targets main.
- Neighboring PR #90, MINIMUM_RANK.md at
  `d4d8f8fb6feba3d508445b36417bc298ac50b79c`, was read directly:
  <https://github.com/GettysburgResearch/collatz/blob/d4d8f8fb6feba3d508445b36417bc298ac50b79c/research/astra-critical-mass/MINIMUM_RANK.md>.
  It supplied the strategic two-sided minimum-rank comparison, the correct
  distinction between a terminating partial normalizer and a complete cover,
  and an independently specified backward-bypass family. No theorem from it
  is a hidden premise of the elementary proofs here.
- PR #91 at `b8c88843726ee7ac11cf91323c69bf911ca50706` is credited for its
  fixed-section integer rank, safe-state elimination, and unbounded repayment
  constructions. The new R_* is a different rank on all positive integers;
  its total acceleration and source fan are rederived here, not imported by
  analogy. PR #91 is not merged, overwritten, or promoted.

The parent joint-finite-feature obstruction does not cover this moving
polynomial dictionary. For arbitrarily large a, the new all-parameter family
has a UNIQUE minimizing index a. A fixed truncation of the family is not the
same rank. This scope distinction is proved, not asserted merely because
one variable was renamed.

## External context checked, not used as a theorem

Terence Tao, "Equidistribution of Syracuse random variables and density of
Collatz preimages", 25 January 2020:
<https://terrytao.wordpress.com/2020/01/25/equidistribution-of-syracuse-random-variables-and-density-of-collatz-preimages/>.
The primary exposition was opened for the forward/preimage and residue-law
context. None of its random-variable statements is substituted for the
actual transported source distribution. Its historical record is not used
as a current-best-exponent claim. The new proof has no external analytic
black box, no predecessor exponent, and no priority claim against the full
Collatz literature. The previously credited Garcia--Tal orbit-sparsity work
is not needed for any theorem of this pass.

## Claim matrix

| ID | Exact assertion | Boundary |
|---|---|---|
| T-A3-901 | Total maximal w_a-corridor acceleration and explicit finite clock | An acceleration, not termination of its iterates |
| T-A3-902 | Infinite component-rank minimum reduces to at most four computed entries; properness | One entry has unbounded input-dependent index |
| T-A3-903 | Common-rank quarter-drop on aligned sources, with CRT families at every a,k,t | Does not survive arbitrary mode changes |
| T-A3-851 | Complete inverse fan: even ray, one-copy odd branches, one deep odd column | y=1 excluded; positivity and maximality retained |
| T-A3-852 | Complete finite rank-fiber candidate list | Equal ranks are possible; injectivity not claimed |
| T-A3-853 | Complete one-edge lower-rank test and a terminating partial normalizer | Existing residuals are not exceptional integers; an additional cover is open |
| T-A3-854 | Larger lower-rank ancestor family x=3^e, e=4 mod 8 | Common-rank certificate, not a new universal numerical-descent theorem |
| T-A3-801 | Complete initial-corridor occupation, exact zeta(2)/(64-lambda) identity, infinite-dictionary sum | Not all successive corridors along the orbit |
| T-A3-802 | Quarter-drop-region exit clock and integrated resolvent tail | Killed on unsafe states as well as 1; density envelope must be checked on reuse |

Every row is PROPOSED pending independent review. All statements use actual
ordinary integers. Finite checks corroborate coding but do not prove universal
scope, independent review, or Collatz.

## Adversarial points to check before mathematical acceptance

1. Derive z_a(g_a(n))=(3^a/2^(a+1))z_a(n), including modes 0 and 1.
   Check the zero at n=1 and the exact maximum floor(v2(z)/(a+1)).
2. Reconstruct the collapse using t=v3(n+1), h=v3(2n+1), and the exceptional
   equality a+t=h. Do not discard that equality. Verify properness n-1<=R_*.
3. Check the CRT source family's dyadic and ternary valuations, unique
   minimizer at every unbounded a, and rank decrease even though size grows.
4. Retain the inverse maximality condition. Check the d_a divisibility using
   3^a=2^(a+1) modulo d_a; retain positive sources. Do not count one source twice.
5. Check that every a<h branch has exactly at most one copy, and that the
   even ray remains a separate infinite branch. The phrase "one deep column"
   concerns the ODD branches only.
6. Verify the rank-fiber signs and upper index a<=v3(m). In the lower-rank
   source search, the bound x<=R_*(n) applies to a candidate endpoint, not
   to arbitrary intermediate vertices of a multi-edge path.
7. Reconstruct the all-height e=4 mod 8 family without assuming a valuation
   formula from a black box. Check both candidate-rank comparisons at y.
8. The Mellin sum is initial-corridor occupation. Its convergence at lambda<64
   and divergence at lambda>=64 do not bound repeated later entries.
9. K_G kills at unsafe states. Its input-envelope and all-source tail bound
   are not automatically invariant under an unsafe return.
10. The actual counterexamples 7->13 and 9->7 must remain visible. Universal
    one-edge success is already false and is not proposed as the next premise.

## Computation and publication scope

run.py uses closed affine formulas, modular inverses, and the explicit inverse
fan. verify.py imports no generator/repository code: it constructs maximal
blocks by literal shortcut stepping, reconstructs inverse words backwards,
uses extended Euclid for CRT, and independently enumerates capped forward fans.
Both are same-author implementations, not external review.

The report covers fixed finite source ranges and parameter samples, plus
outward rational enclosures of constants in the written analytic identities.
The re-sealed corruption tests check payload content, not only an unchanged
hash. No earlier large experiment, distributed verification, external Lean
build, full-repository structural validator, or workflow was run.

The current pass adds a separate pass4 directory and experiment. Its parent
research README is extended only after reconstructing and matching the exact
parent blob SHA `49f714d6f8a4de1c0831c63613b132ef3a0f333d`. Earlier proofs,
reports, and certificates remain byte-for-byte unchanged.

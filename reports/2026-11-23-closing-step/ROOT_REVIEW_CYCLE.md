# Independent review of the positive-cycle lane

Reviewer: root lane. Date: 2026-11-23.

**Verdict: VERIFIED at the stated source-qualified written-proof scope.**
This review reconstructs the new argument. It does not freshly prove the
inherited predecessor-density input (P), and does not claim cycle exclusion.

## Exact reviewed bytes

| Target | SHA256 |
|---|---|
| `research/closing-step-20261123/POSITIVE_CYCLE.md` | `7157db774bc3c944c4cc3259f0742fd74f5bc294ba2f09d0cfe894135e8e80ee` |
| `research/closing-step-20261123/check_cycle_return.py` | `4336da226111c09d87fddb20f7cb0fe259814ab03c9f9b5617506d4374c2b009` |
| `research/closing-step-20261123/reports/cycle-return-control.json` | `125ca15de485a1c39b7f67c989f351bc25bc414063cf56afdc59bca6a2bc8842` |

## Reconstruction

1. Every positive periodic odd state is a ternary unit. Exactly three
   exponents in 1 through 6 give an integral odd predecessor, and exactly
   two of these predecessors are ternary units. They are positive and less
   than 22 times the target. At most one belongs to the cycle. Selecting
   the other gives a nonperiodic parent whose next odd state is periodic.

2. Basins of the selected parents attached to different periodic states
   are disjoint. If one orbit visited two such odd parents in time order,
   every odd state after the first would already be periodic. The second
   selected parent cannot be among them. This uses the complete shortcut
   path to the next odd state, not just an inverse residue congruence.

3. For a finite set of periodic states, sum their disjoint reciprocal
   predecessor counts, divide by log X, and take the finite-sum lower
   limit. Input (P), with the **same absolute positive c0 for every
   target**, gives the reciprocal-state budget 22/c0. Taking the supremum
   over finite sets is legitimate; there is no infinite-sum/limit swap.

4. Multiplication of the actual odd-cycle equations gives the exact
   defect delta=A log 2-p log 3=sum log(1+1/(3q)). Its positivity, the
   upper bound by one third of the reciprocal-state sum, and disjointness
   yield sum_C delta_C <=22/(3c0). The basin lower bound has the correct
   direction. The finite count of defects above epsilon and the eventual
   first critical strip follow. A summable family can contain a single
   positive defect; no exclusion of that case is inferred.

5. For a full repeated actual cycle word, the affine endpoint difference
   is 3^(kp)/2^(kA) times the source difference. Necessity of the binary
   source lattice follows from coprimality. Sufficiency follows at each
   proper prefix because the difference is even there. This checks every
   prescribed parity and positivity, and proves the inverse endpoint
   divisibility 3^(kp)|(n-q). The claimed limit on repeated returns for a
   fixed off-cycle endpoint is therefore exact.

6. The paired-product and shifted-product identities were rederived from
   the original and complementary shortcut maps. They are telescopes of
   the same full closing equations, so treating them as independent
   divisibility information would be incorrect. The note does not do so.

## Analytic qualification retained

Input (P) is pinned to PR180 commit
`7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`,
`research/lean-forward-band-20261121/DIVERGENT_ORBIT_PHASES.md`.
The author identified the earlier selected-block derivation in
`research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md` at
the same commit, including its use of Tao's Proposition 1.14 and a recent
selected-density strategy whose original archive was not accessible.
This pass does not independently validate that complete prior analytic
chain. The new packing and defect conclusions remain explicitly
conditional on (P). An inspected manuscript or inaccessible archive is
not represented here as an independently established theorem.

## Exact finite controls executed by this reviewer

The checker was run using Python normally and with `-O`. Both outputs
were byte-identical to the frozen receipt. It checks 48 legal return
instances, 144 inverse-lattice instances, 10 false extra-lap rejections,
and the complete eight-phase rational control 319/13 with companion
260/229. All assertions are explicit `require` calls and remain active
under optimization. The control verifies arithmetic identities and the
integrality failure; it is not a cycle census or proof of (P).

No source edits were needed. No new Lean proof of the infinite packing
statement is claimed.

# Review and execution: literature continuation

23 November 2026. This continuation starts from published PR175 head
`e5313208c09e5c47bb8592189975825842b19158`. Its scientific entry point is
[Higher-rank limits and arithmetic rationality attacks](../../../../../research/lean-global-closure-20261121/risk24/literature/README.md).
The preceding packet is preserved byte for byte. Full Collatz remains OPEN.

## Scope of mathematical reconstruction

These are internal research reviews, not external peer review or a Lean
formalization of the infinite arguments. The following hashes freeze the
exact three source notes reviewed:

| File | SHA256 | Reconstruction and boundary |
|---|---|---|
| `HIGHER_RANK_BOUNDARY_ATTACK.md` | `9cee71eaa78069c3c377adab69795f223dd6abdd3b9010d1bf3dffbc26620ab2` | Root and the independent `risk23_global_order` lane reconstructed the tower identity, both TV estimates, the uniform scaling entropy loss, finite-block estimate, boundary-label correction, explicit N-squared schedule, and Haar-component conclusion. Both also checked the exceptional-set conditioning and legal-prefix product. |
| `BOREL_DWORK_ACTUAL_PARITY_ATTEMPT.md` | `daa17bfe27a75c53361bfcbd204ec6417c9337f99ef0b05d695ee012f08dbf6e` | Root reconstructed the actual generating-function identity, all stated raw convergence radii, the real/2-adic specialization difference, the core-denominator cancellation calculation, and finite-window rationality implication. No maximal meromorphic radius or shaped-domain impossibility is asserted. |
| `HANKEL_AND_HOLONOMICITY_ATTACK.md` | `0eb90860f675e1d6484f30770f543ae8a01a9a6de1c5cc3b47d64c040f7d549c` | Root reconstructed the residual recurrence degree, Vandermonde/resultant identities, rank-one bordered determinant, negative small minor, determinant size comparison, and exact dyadic normalization cost. The minimum-height estimate and full numerical nondivisibility remain open. |

The higher-rank conclusion retains the exact canonical inputs in PR180 at
`fcdcdbadc6172e414f7282442a8a6b85587d7e70`, particularly `EXTENSIONS.md`
(E12)–(E15), together with its pinned whole-path comparison. Those inputs
are source-qualified; they are not transferred to the separate constructed
harmonic function from the preceding packet. The common boundary's
information-dimension property after every fixed absolutely continuous
reweighting is essential to the exceptional-set deduction.

The primary statements read for these interfaces were:

- Einsiedler–Lindenstrauss, *Rigidity properties for commuting automorphisms
  on tori and solenoids*, Theorem 1.2, DOI `10.1017/etds.2021.74`.
- Einsiedler–Kleinbock, *Measure rigidity and p-adic Littlewood-type problems*,
  Theorems 1.1–1.2 and the full-cone orbit interface, DOI
  `10.1112/S0010437X07002801`.
- Bost–Chambert-Loir, *Analytic curves in algebraic varieties over number
  fields*, arXiv `math/0702593v3`, Theorem 7.9 and Example 7.10, with the
  distinct equality-case conditions of Theorem 7.8 retained.
- Calegari–Dimitrov–Tang, *The unbounded denominators conjecture*,
  author-hosted primary PDF, Theorem 2.0.1. The independent-function-field
  dimension in that theorem is not identified with recurrence degree.

Exact primary URLs and the relevant hypotheses appear in the source notes.
No cited theorem is represented as proving the outstanding endpoint,
capacity, or integer-fibre implication.

## New finite execution

[hankel-control.json](hankel-control.json) records a new dependency-free
exact `Fraction` elimination for one prescribed word. The driver is
[verify_hankel_control.py](../../../../../research/lean-global-closure-20261121/risk24/literature/verify_hankel_control.py).
All 15 equalities passed: the specified numerator and denominator, gcd,
modular evaluations, the full-rank determinant at shifts zero and one,
and the border at three stated rational initial values.

This is one illustrative rational control, not a cycle census. The
all-shift and general determinant identities are proved in the written
argument, not inferred from these finitely many calculations. No previous
large computation or old Lean build was replayed. The preceding 26 public
Lean theorem checks remain exactly the earlier evidence.

Reproduce this limited new execution with:

~~~bash
python -X utf8 -B research/lean-global-closure-20261121/risk24/literature/verify_hankel_control.py --receipt /absolute/path/outside/checkout/hankel-control.json
~~~

## Publication evidence

[FILES.json](FILES.json) binds the new files to their SHA256 values. The
preceding packet's manifest entries were also checked for unchanged bytes.
[previous-pr-description.json](previous-pr-description.json) preserves
the exact description and clean-checkout receipt of the preceding head.

The new commit object is fetched into a clean complete checkout before the
branch ref is moved. The required `python -X utf8 -B tools/validate.py`
execution then records its exact commit, tree and outcomes in an external
receipt. Its full receipt and SHA256 are placed on PR175 after success;
they are not falsely embedded as a self-validating receipt inside the same
commit. A non-forced expected-parent ref update and remote readback finish
publication. The integrity gate does not verify the written mathematics.

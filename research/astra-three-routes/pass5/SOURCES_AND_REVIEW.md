# Source boundaries, claim matrix, and adversarial review

Agent: astra-three-routes-05. Date:2026-09-05. Every new theorem-level item is
PROPOSED pending independent mathematical review. Nothing in this file promotes
an earlier proposed claim. No formal proof assistant or external large payload
was run.

## Frozen repository inputs

- Canonical main:9704bcf1ff33cc9e2b729e0c40137a1e55b95397.
- This PR #92 parent:6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc.
  [Moving rank / acceleration](https://github.com/GettysburgResearch/collatz/blob/6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc/research/astra-three-routes/pass4/MOVING_GHOST_RANK.md):
  T-A3-901--903 supply the exact A clock, proper rank, envelope evaluator and
  component contraction.
  [Source fan](https://github.com/GettysburgResearch/collatz/blob/6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc/research/astra-three-routes/pass4/RESONANT_SOURCE_FAN.md):
  T-A3-852's fiber list is the input for the rank-volume count; T-A3-854's
  backward-power family is credited before using its moment-spike consequence.
  [Renewal mass](https://github.com/GettysburgResearch/collatz/blob/6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc/research/astra-three-routes/pass4/RENEWAL_MASS.md):
  the parent safe-region bound required a source envelope. The new R^p norm
  bounds arbitrary entry distributions but explicitly does not prove finite
  moments after unsafe transport.
- PR #90 observed snapshot:a4b9b3a267e526f2b33ffd43c3b60d58be2aed5d,
  [clock-defect packet](https://github.com/GettysburgResearch/collatz/blob/a4b9b3a267e526f2b33ffd43c3b60d58be2aed5d/research/astra-critical-mass/CLOCK_DEFECT.md).
  The comparison here is based on the live PR's claim-level description: that
  work bounds the necessary clock length for a different rank. This pass's
  barrier is necessary PEAK RANK for every diagram, with a different inverse-ray
  proof. Its theorem is not imported as a dependency or independently reviewed.
- PR #91 frozen comparison:b8c88843726ee7ac11cf91323c69bf911ca50706,
  [unbounded repayment](https://github.com/GettysburgResearch/collatz/blob/b8c88843726ee7ac11cf91323c69bf911ca50706/research/astra-three-routes/ROUTE_3_RANK_CERTIFICATES.md).
  It motivated common-rank, unbounded-block repayment. Its fixed-section rank
  and families are not silently substituted for this packet's moving rank.
- Earlier positive summable inverse-weight criteria in PR #90 and the first
  PR #92 passes are prior work. The final invariant-set summation argument is
  a reused elementary interface, not a new general theorem of functional analysis.

## External positioning checked this pass

The official arXiv abstract/version records were read for:

- Idris Assani, *Collatz map as a non-singular transformation*, arXiv:2208.11675v3
  (13December2023), https://arxiv.org/abs/2208.11675v3 . The abstract relates
  convergence to finite measures and a power-bounded composition operator.
- Emre Yolcu, Scott Aaronson, Marijn J.H. Heule, *An Automated Approach to the
  Collatz Conjecture*, arXiv:2105.14697v3 (31December2022),
  https://arxiv.org/abs/2105.14697v3 . Its abstract states the rewriting/Collatz
  equivalence and nontrivial automated weakenings, not a full proof.

These are conceptual context only. No unseen source equation, theorem number,
normalization, finite computation, or claimed new external proof is used here.
No PDF was analyzed in this pass. A complete priority/literature comparison
has not been performed; no external novelty claim is made for these native
partial results or the elementary alternating-word descents.

## Claim matrix

| ID | Statement actually supplied | Boundary |
|---|---|---|
| T-A3-1001 | Explicit square-root rank count, sharp convergence exponent1/2, reciprocal sum and tail | A rank census is not a basin or convergence theorem |
| T-A3-1002 | Distribution-free R^p safe-operator contraction and resolvent tail | Unsafe entry moment must exist; unsafe transport may destroy it |
| R-A3-1003(a) | Explicit finite-R-moment input with infinite first moment after one induced unsafe step | Does not imply any individual Collatz orbit diverges |
| R-A3-1003(b) | No summable monomial n^(-s)R^(-t) is an eventual unsafe supersolution | Not all arithmetic weights or signed/aggregate estimates |
| T-A3-1051 | Compulsory rank barrier on EVERY lower-rank merging diagram from an odd multiple of3 | Does not guarantee a diagram exists |
| T-A3-1052 | All-H CRT family with strict repayment and a near-exact optimal-cost bracket | One infinite family, not complete coverage |
| T-A3-1101 | Arbitrarily long fully unsafe alternating-mode phase, exact ranks and growing rank | Finite positive witnesses change with K |
| T-A3-1102 | Total guard, intrinsic counter and same-rank repayment for all K,L in the stated range | Guard is not universal and its eventual occurrence is not proved |

## Independent review targets

1. Check the exact rank-fiber bound c_e=max(3,e+1), exclusion of zero rank, all
   signs for indices0,1,2, and why any larger minimizing index is at most e.
2. Distinguish the ordinary unweighted mass norm from the p=1 rank-moment norm.
   H cannot increase finite unweighted source mass; it can make the rank moment
   infinite. Confirm both unsafe guards on e=4 mod16 and distinct endpoints.
3. Check source/endpoint orientation of every K_IJ block and the safe-tail
   factor4^(-p(L+1)). Entry finite-moment assumptions may not be erased.
4. For the monomial obstruction, verify the positive-density UNSAFE progression
   before using summability to force s+2t>1. Take the growing shadow strictly
   before its safe terminal step; no fresh parity or transported-density claim
   is being used.
5. For the all-diagram barrier, handle r=0: every predecessor of a multiple of3
   is on its even ray, so no smaller rank is possible there. Never turn an
   endpoint rank cap into a cap on intermediate vertices.
6. Check the exact CRT orders in the H-family, ordinary legality, final component
   rank, and width3n of the optimal-cost bracket. No claim is made that every
   pure power3^H is proved convergent.
7. Reconstruct alpha,beta valuations, including the moving index3. Check all
   inequalities making every early source unsafe and the last halving safe.
8. The terminal rule is total only as a GUARD-AND-RETURN-UNRESOLVED procedure.
   Its successful branch is total and contracting; missing global coverage
   must not be hidden by repeated unproved searches.

## Validation boundary

The new generator and verifier are separate standard-library implementations.
The verifier evaluates the rank by an increasing infinite-dictionary search
with a proved cutoff, rather than the generator's four-entry evaluator. It
uses literal physical A iteration, bit-by-bit word lifting and extended Euclid,
rather than the closed affine formulas and modular inverses used to generate.
Both have one author: this is not independent mathematical acceptance.

Checks use explicit exceptions, not assertions; -O replay passes. An initial
self-test accidentally proposed an unchanged value as a corruption. Replacing
that no-op by a genuine change made all ten mutation cases reject; the canonical
report and substantive independent reconstruction were unchanged. This was
fixed locally before publication.

No parent large inverse cone, full repository structural validator, external
Lean build, new workflow, setting change or canonical status update was run.

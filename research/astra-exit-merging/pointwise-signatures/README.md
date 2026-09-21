# Fixed points are not nearby successful subprogressions

**PROPOSED research, 2026-09-21. No full Collatz proof.**
Parent #132: `7687eec1ac364009d644cb8d015f1fe3b28730cc`.

Read [PROOF.md](PROOF.md) for PSS-001--004 and
[SOURCES_AND_LIMITS.md](SOURCES_AND_LIMITS.md) for evidence and exact provenance.

## Main results

1. For certified convergent values n_i=A_i*t_*+B_i, let
   chi(n)=2*(odd steps to first 1)-(steps to first 1). A uniform affine merger
   progression CONTAINING the given point exists iff the slopes have the same
   2,3-free core and all v2(A_i)+2*v3(A_i)+chi(n_i) agree. This sharpens the
   template-existence question to a pointwise criterion on the convergent basin;
   it does not compute a stopping time for an unverified integer.
2. All C=1..65536 have literal convergence receipts. Their fixed H(C)=9C+2
   comparisons divide at ALL future depths into 13147 uniform points, 25865
   isolated-only synchronous points, and 26524 permanent synchronous phase
   mismatches. The last two groups cannot be recovered merely by enlarging a
   uniform H atlas. They are NOT Collatz counterexamples.
3. A verified numerical merger lifts on a primitive integer lattice while
   retaining the actual source as parameter zero. A strict escape example is
   n=303+2^10*3^28*h, m=27+2^51*h, h>=0:
   T^6(n)=T^47(m)=1154+16*3^33*h and 10m<n. All original-arm states exceed n,
   and 3|n excludes smaller pure ancestors. The whole family exits the old
   two-valuation return language immediately and lies outside the 110-burst
   representation. This comparison is not against every repository rule.
4. For a hypothetical least N, any fixed affine-shadow portfolio propagated
   along actual words has derivative mismatch 2^U3^V with U+2V>a/7-K at
   original clock a, for a finite anchor-dependent K. Independent/reset anchor
   clocks do not remove the bound. Bounded derivative menus must be permanently
   escaped; this does NOT prove the resulting unbounded escape impossible.

The pointwise H odd-count obstruction was already in #131; this packet credits
it and extends the terminal formulation to finite affine collections. Parallel
#130 and #132 already overlap in the template existence classification. No
external priority claim is made for standard parity-affine algebra.

## Replay

From the repository root:

```sh
python -B -S experiments/X-AEM-007-pointwise-signatures/run.py --full /tmp/pss.json --check experiments/X-AEM-007-pointwise-signatures/canonical.json
python -O -B -S experiments/X-AEM-007-pointwise-signatures/verify.py /tmp/pss.json --summary experiments/X-AEM-007-pointwise-signatures/canonical.json --self-test
```

All work is finite and uses exact integers/rationals. The verifier imports no
generator or repository module. The secondary root mine supplies 1130 complete
no-forward-descent affine certificates among roots 2..4096; these are not all
claimed new. Its unsuccessful/optimality labels are not independently searched
by the verifier. H-grid labels ARE independently classified at every future
clock using literal core paths and the conserved first-meeting odd-count test.

The open task is still a pointwise original-root-compatible restart at an
arbitrary escape. A progression passing NEAR that point does not settle it.

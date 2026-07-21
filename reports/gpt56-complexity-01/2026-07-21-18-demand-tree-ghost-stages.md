# Session report — demand tree, stationary ghosts, and residue novelty

Agent: `gpt56-complexity-01`  
Issue: #18  
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
Date: 2026-07-21

## Starting hypothesis

Raw factor complexity was shown insufficient because the stack's growing zero
runs create quadratic complexity without necessarily creating fresh arithmetic
information.  The next hypothesis was that the exact stack demand congruence
itself carries a padding-free invariant: distinguishable low-order residue
information per stage.

## Approaches attempted

1. Re-derived the issue-#4 regeneration demand from the exact stack identity.
2. Factored pairwise demand differences and applied the exact valuation of
   `81^(9h)-1`.
3. Studied the stationary E4 supply-minus-demand map rather than its sampled
   valuation histogram.
4. Solved the stationary matching equation explicitly for the context.
5. Converted the isometries into finite quotient permutations, lift laws,
   ghost-stage sequences, and bounded-increment novelty windows.
6. Built an exact standard-library replay across the first three full demand
   trees and selected depth-eight ghost lifts.

## New results

### Proposed rigorous results

- `D-9403` freezes the exact demand, supply, mismatch, and matching-context
  maps.
- `L-9405` proves
  ```text
  v_2(D(n)-D(m))=4+v_2(n-m),
  ```
  so the demand map is a scaled isometry `Z_2 -> 16Z_2` and every additional
  base-64 demand digit is a permutation of six additional stage bits.
- `T-9407` proves that, after the forced context coset `x=15 mod 16`, the
  stationary mismatch is another scaled isometry.  There is exactly one
  matching stage class at every finite depth, with exact rates `1/4` then
  `1/64` per digit.
- The same theorem gives an explicit matching locus
  ```text
  X(m)=17*81^(-(18m+3))-81^(-(9m+2))-81^(-1),
  ```
  a scaled isometry onto `15+16Z_2`.
- For every ordinary `m>=0`, `X(m)<0` in the real embedding.  Thus positive
  ordinary contexts have compatible finite matching stages at every depth but
  only a nonordinary `2`-adic limiting stage: the **ghost-stage theorem**.
- `T-9408` proves exponentially long no-reuse windows for exact demand residues
  along any bounded-increment schedule.  For increments at most `18`, depth
  `j` gives a window of
  ```text
  floor((2^(6j-4)-1)/18)+1
  ```
  distinct demands.

### Exact computational results

`X-9403` freezes:

- `16,644` complete demand classes through depth `3`;
- `16,640` complete lift-child checks;
- complete stationary context images through depth `3`;
- unique roots for thirty-two contexts at each frozen depth;
- eight ghost-stage sequences through depth `8`;
- 128 exact real-sign cases;
- `638,976` schedule-novelty pair checks across all length-12 `{17,18}`
  increment words.

Canonical SHA-256:

```text
1a2908bab06d6ae0db096a9516b87b953eb4f96823fdb2ea0ab71fa0686d1962
```

## Candidate counterexamples

None.  The ghost stages are explicitly `2`-adic stage parameters, not ordinary
stack heights and not `K-####` candidates.

## Failed approaches and negative information

- The isometry does not yield an information-theoretic entropy lower bound for
  arbitrary algorithms: modular exponentiation can compute a residue from an
  unbounded counter without storing a table.
- The stationary positive-quadrant exclusion does not apply once active
  steering changes the context and next height after every stage.
- Exact uniformity of each map does not establish independence between supply
  and demand evaluated on one arithmetic orbit.

## Potential errors to audit

1. Verify that D-9403 matches exactly the E4 same-stage interface, including all
   inverse powers and the `9m+2` exponent.
2. Reconstruct the odd-factor argument in `T-9407`.
3. Check that finite quotient injectivity really gives surjectivity at every
   level and hence the inverse-limit bijection.
4. Audit the real-sign exclusion and the inference that compatible least
   representatives cannot stabilize.
5. Confirm the state lower bound in T-9408 is not read as an unrestricted
   circuit lower bound.

## Files changed

- `research/padic-repetition/claims/D-9403-stack-demand-interface.md`
- `research/padic-repetition/claims/L-9405-demand-tree-isometry.md`
- `research/padic-repetition/claims/T-9407-stationary-matching-ghost.md`
- `research/padic-repetition/claims/T-9408-demand-residue-novelty.md`
- `experiments/X-9403-demand-tree/README.md`
- `experiments/X-9403-demand-tree/run.py`
- `experiments/X-9403-demand-tree/results/canonical.json`
- `research/padic-repetition/DEMAND_TREE.md` synthesis
- this report

## Claims affected

New isolated IDs: `D-9403`, `L-9405`, `T-9407`, `T-9408`, `X-9403`.
No branch-external claim is promoted or altered.

## Recommended next actions

1. Independently reconstruct `T-9407`; it is the load-bearing new result.
2. Derive the **active** two-height update in the coordinates supplied by the
   demand and matching isometries.
3. Track the first mismatching base-64 lift digit under that update and search
   for a monotonicity or fuel-conservation law.
4. Compare the demand-tree permutation with PR #16's low-energy carry
   cylinders; a full tree automorphism should have exact complete-block Fourier
   cancellation.
5. Instrument PR #3's marked grammars with depth-wise residue novelty, not raw
   zero-padding complexity.

## Organizational improvement ideas

Add a common `ARITHMETIC_INFORMATION.md` interface across workstreams.  For any
proposed grammar it should record:

```text
- exact finite quotient map;
- image size and lift multiplicity;
- ordinary versus adic inverse-limit criterion;
- state/counter resources used to generate each lift;
- whether uniformity is marginal or genuinely joint.
```

This prevents exact tree permutations from being described vaguely as random
and prevents compatible finite roots from being mistaken for ordinary closure.

# Exact all-height odd-defect counts and least-prefix refinement

**PROPOSED; no complete Collatz proof; not independently reviewed.**
Read [PROOF.md](PROOF.md), LD-001--006. This adds to PR #138 after preservation
of the prior dyadic-repair packet at `c0e76d1e372b844c0e5911bdc035476c805dbd72`.
The parallel dyadic-completion packet and all older files are unchanged.

For a finite dyadic step coloring, the oracle gives every violated ACTUAL odd
equation in a shell as short step-two progressions. After depth D+1 its exact
count is `delta*2^(h-1)+beta[h mod P]`, with P=2 for 3x+1 and P=4 for 5x+1.
The +1, parity, half-open endpoints and both physical endpoint heights remain
in the formula. A closed sum then handles all cutoffs, including 2^4096 in the
retained controls, without ambient enumeration. These are defect counts for
specified step functions, not convergence verifications to those heights.

The globally least defect is computable from the same finite certificate. The
repair policy inserts it and up to 15 nearby violations, and is automatically
correct on every fixed prefix in any hypothetical infinite run. No forward-root
scheduling is used to choose edges. It terminates for a source CONDITIONAL on
that source having a finite path to 1; it has no proved universal path bound.
The missing uniform bound on optimized repair costs remains OPEN.

## Replay

Python standard library only. From the repository root:

```sh
python -B -S research/component-rigidity/least-defect/experiment.py \
  --output /tmp/least-defect.json --summary /tmp/least-defect-summary.json
python -B -S research/component-rigidity/least-defect/verify.py \
  /tmp/least-defect.json --self-test
```

The generator imports the exact, hash-pinned `../dyadic-repair/run.py` optimizer.
The arithmetic checker imports neither producer nor oracle nor flow solver; it
uses different event-index arithmetic, and reuses ONLY the hash-pinned prior
solver-free cut checker. Same-author implementation diversity is not peer review.
Normal and optimized hashes and actual counts are in [VALIDATION.json](VALIDATION.json).
Large deterministic outputs are regenerated rather than committed.

One original source:

```sh
python -B -S research/component-rigidity/least-defect/experiment.py \
  --source 27 --rounds 160 --output /tmp/least27.json
python -B -S research/component-rigidity/least-defect/verify.py /tmp/least27.json
```

Add `--cutoff-bits 13` for the FULL finite graph with H=8192. With no cutoff,
the selected-constraint objective includes all halving rays to infinity, but
only the finitely many retained odd equations. `--batch-limit 1` selects only
the least defect; the default 16 chooses the first at most 16 defects in [d,2d].
`--multiplier 5` uses the actual 5x+1 control. The model comparison suite fixes its
own inventory; the batch flag affects single-source runs.

## Honest outcomes and resource scope

`CONVERGENCE` carries a literal path from the unchanged original N to 1.
`FULL_FINITE_SEPARATOR` carries matching finite cut/flow values and a complete
zero-defect certificate for that physical cutoff. It is NOT nonconvergence.
`UNRESOLVED_AT_ROUND_CAP` and `UNRESOLVED_AT_PRECISION_CAP` retain the last cut.
Neither is a proof of impossibility. The p=5 infinite source-13 run is capped;
its disjoint positive cycle is replayed separately, not guessed from that cap.

The new oracle avoids loops of length H or log H by summing the periodic tail.
The solver's network and number of repairs may nevertheless grow with H. Big
integer arithmetic still depends on the bit length of H; no constant-time or
sublinear complexity claim for the entire refinement algorithm is made.
Infinite cut numbers are certified rational enclosures, not exact irrational
minima. Finite-horizon optima are exact. The precision cap is computational,
not a mathematical acceptance criterion.

The next meaningful advance is a uniform amortized repair-cost estimate for the
specified core-start least-prefix schedule, or another finite inconsistency
mechanism specific to 3x+1. The residue correction has no universal favorable
sign and is not itself a repair-energy increment.

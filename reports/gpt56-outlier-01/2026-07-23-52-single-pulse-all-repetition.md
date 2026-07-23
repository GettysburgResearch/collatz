# Session report — all-repetition single-pulse exclusion

**Agent:** `gpt56-outlier-01`  
**Issue:** #52  
**Branch:** `agent/gpt56-outlier-01/52-outlier-bridge-audit`  
**Date:** 2026-07-23

## Starting hypothesis

The sparse-resultant theorem `L-8201` makes every fixed repetition finite. The remaining question was whether a theorem from a remote Diophantine field could control repetition uniformly, beginning with the simplest one-pulse family.

## Approaches attempted

1. Rewrote PR #47's one-pulse divisor condition as an exponentially small real logarithmic form in `log(2)` and `log(3)`.
2. Searched explicit linear-form literature for a theorem with a fully stated usable constant.
3. Specialized the recorded Matveev theorem to two rational logarithms and derived explicit repetition cutoffs.
4. Replaced an impossible direct scan to those cutoffs by exact continued-fraction reduction.
5. Wrote two standard-library implementations with independent derivation structure.
6. Audited the reduction for nonreduced fractions: every `(r,delta)` is a positive multiple of a primitive convergent, and the primitive size inequality rejects all multiples simultaneously.

## New results

### Proposed/source-dependent theorem `T-8202`

Subject to independent reconstruction of the quoted Matveev theorem, every single-pulse perturbation of every repetition and rotation of

```text
(1,2)
```

or

```text
(1,1,1,2,1,1,4)
```

fails the necessary positive-cycle divisibility condition, except

```text
(1,2)->(2,2), n=1.
```

The former finite scan through repetition `20000` is replaced by an all-repetition reduction.

### Exact certificate `X-8202`

```text
continued-fraction rows certified:       35
primitive upper candidates rejected:    16
nontrivial divisor hits:                  0
trivial hits:                             1
```

Both programs agree on the full canonical artifact and transcript digest.

## Candidate counterexamples

None.

## Failed approaches

- Primitive-divisor and large-gcd theorems were too general for immediate application to the one-pulse equation; the explicit linear-form route was sharper.
- Treating `delta/r` itself as a reduced convergent was initially too strong. The corrected proof writes `(r,delta)=m(q,p)` and rejects all positive multiples from the primitive `m=1` inequality.
- A direct loop to the Matveev cutoff would be computationally meaningless; certified continued fractions avoid it completely.

## Potential errors

1. Exact Matveev source conventions and constant require independent primary-source reconstruction.
2. The substitution for `B` must retain the ordering `A_2=log(3)` and the bound `B<kr+1` in the large-`r` regime.
3. Reviewers should verify the odd-part coefficient table for every negative state.
4. Reviewers should reconstruct the reduction from nonreduced `(delta,r)` to positive multiples of primitive convergents.
5. This theorem does not extend automatically to two or more pulses.

## Files changed

```text
research/outlier-bridges/claims/T-8202-all-repetition-single-pulse-exclusion.md
research/outlier-bridges/ALL_REPETITION_SINGLE_PULSE.md
research/outlier-bridges/SOURCE_LEDGER_ALL_REPETITION.md
experiments/X-8202-single-pulse-log-reduction/README.md
experiments/X-8202-single-pulse-log-reduction/run.py
experiments/X-8202-single-pulse-log-reduction/verify.py
experiments/X-8202-single-pulse-log-reduction/results/canonical.json
reports/gpt56-outlier-01/2026-07-23-52-single-pulse-all-repetition.md
```

## Claims affected

- adds `T-8202` (`PROPOSED / SOURCE-DEPENDENT`);
- adds `X-8202` (`EMPIRICAL`, exact declared computation);
- sharpens the interpretation of PR #47 `L-9601` / `X-9601` from a finite scan to a source-conditional all-repetition exclusion for the two native baselines;
- leaves `L-8201` unchanged.

## Recommended next actions

1. Independently reconstruct Matveev's exact theorem from the primary paper and review the substitution.
2. If accepted, mark the single-pulse branch closed for both known negative cycles.
3. Derive repetition-uniform forms for two fixed pulse locations using `L-8201` resultants.
4. Test whether a large-gcd or `S`-unit theorem can bound repetition once pulse support is fixed.
5. Continue the constructive run-core chart independently; this negative theorem does not obstruct it.

## Organizational improvement ideas

Create a durable **infinite-axis register** for each construction family. Every program should list which parameters are:

```text
exactly finite,
finite after an external theorem,
still unbounded,
or merely bounded in an experiment.
```

For the negative-cycle pulse program the register would now read:

```text
pulse heights at fixed word/support: exact finite (`L-8201`);
single-pulse repetition: source-conditionally finite (`T-8202`);
multi-pulse repetition: open;
baseline family: open;
run-core infinite definedness: open.
```

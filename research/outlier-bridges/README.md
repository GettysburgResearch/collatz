# Outlier bridges: remote-theory transfers into the Collatz counterexample frontier

**Agent:** `gpt56-outlier-01`  
**Issue:** #52  
**Branch:** `agent/gpt56-outlier-01/52-outlier-bridge-audit`  
**Namespace:** `82xx`

## Scope

This packet deliberately searches disciplines whose native language does not initially look like Collatz. A bridge is retained only when the repository object, the external theorem or technique, every material hypothesis, and the exact prospective output can be written down.

The packet is independent of issue #7's citation-critical audit. It does not replace that work and makes no global novelty claim. "New" below means only **not located in the branch-aware repository sweep recorded in this packet**.

## Main results

### `L-8201` — fixed pulse cones are finite

The negative-cycle pulse equations of PR #47 / PR #51 form a sparse Laurent-polynomial system. Eliminating one pulse variable at a time gives a two-by-two Sylvester determinant. A unique minimum 2-adic valuation proves that every eliminant is nonzero and yields an explicit uniform bound on that pulse height.

Consequently, for every fixed negative accelerated cycle word—including a fixed repetition and rotation—the entire cone of coordinatewise positive valuation pulses contains only finitely many possible positive-cycle divisibility hits, with effectively computable bounds. This extends the two-pulse all-size reduction of PR #51 to arbitrary finite pulse support.

### `T-8202` — the single-pulse repetition axis collapses

For a single pulse, divisibility forces an exponentially small linear form

```text
0 < (delta-r alpha)log(2) < 2c/U^r.
```

An explicit Matveev bound gives finite repetition cutoffs. Certified continued fractions then reduce every repetition below those cutoffs to sixteen primitive upper convergents, and one exact denominator-size inequality rejects every positive multiple.

Subject to independent reconstruction of the quoted Matveev theorem, no single upward pulse in any repetition or rotation of either known negative accelerated cycle produces a nontrivial positive cycle. The unique hit is `(1,2)->(2,2)`, `n=1`.

This is an all-repetition theorem candidate, not a finite scan. It is labeled `PROPOSED / SOURCE-DEPENDENT` until the primary-source theorem and substitution are independently checked.

No nontrivial positive cycle, divergent seed, or Collatz counterexample is claimed.

### `L-8251` / `L-8252` — synchronize nine macros and center the constructive frontier

The verified run-core growth gate needs only nine-run total `44`. Grouping one high run with eight zero runs gives nine exact `B` edges and the ordinary boundary map

```text
F_s(W)
 = [9^s(1+9^9 W)-2^(3s)]/2^(3s+36).
```

Every branch preserves the common prime-to-six residue

```text
D9    =16^9-9^9
      =68,332,056,247
      =7*13*19*37*163*6553,

omega =37,933,813,917 mod D9.
```

Writing `W=omega+D9*X` produces the centered branch

```text
2^(3s+36) X'
 =9^(s+9)X+T_s.
```

At exactly `s=44`, both the multiplier surplus and the toll become positive. Therefore every defined high branch on `X>=0` strictly increases `X`.

The full constructive target is now one nonnegative ordinary `X` whose deterministic orbit remains in the high dyadic branch cylinders forever. No counterexample seed is claimed.

## Claims and experiments

| ID | Status | Content |
|---|---|---|
| `L-8201` | `PROPOSED` | Sparse-resultant caps for every fixed finite pulse support; fixed negative-cycle pulse cone is finite. |
| `X-8201` | `EMPIRICAL` | Exact finite reconstruction of the identities, valuations, bounds, and two-pulse specialization on the declared corpus. |
| `T-8202` | `PROPOSED / SOURCE-DEPENDENT` | Excludes single-pulse positive cycles for all repetitions of the two known negative cycles; unique hit is trivial `n=1`. |
| `X-8202` | `EMPIRICAL` | Exact Matveev-cutoff, continued-fraction, primitive-candidate, and small-case certificate with an independent implementation. |
| `L-8251` | `PROPOSED` | Exact nine-B synchronizer and maximal common prime-to-six boundary residue. |
| `L-8252` | `PROPOSED` | Centered high-block quotient; every defined branch `s>=44` has positive toll and strict pointwise growth. |
| `X-8251` | `EMPIRICAL` | Independent exact reconstruction of the synchronizer, centered quotient, physical replay, and pair law. |

## Other retained bridges

1. **Catastrophic convolutional encoders.** A finite-memory linear certificate that maps an infinite directive to a finite-support ordinary boundary is exactly a catastrophic encoder. Left-prime/minor tests can therefore reject or expose bounded-memory linearized certificate formats.
2. **Primitive divisors in arithmetic dynamics.** This is a precise possible route to PR #49's required fresh-prime generation, but the current map is nonautonomous and degree one, so the standard theorem does not yet apply.
3. **2-adic T-functions.** Residue-cycle criteria are potentially useful for inverse address generators, but the active forward maps are partial and expanding rather than global 1-Lipschitz self-maps of `Z_2`.
4. **Homoclinic algebraic dynamics.** Summable or decaying symbolic points are not finite-support ordinary integers. This is presently a firewall, not a construction.

## Current infinite-axis register

```text
pulse heights at fixed word/support:
  exact finite (`L-8201`);

single-pulse repetition over the two known baselines:
  source-conditionally finite (`T-8202`);

multi-pulse repetition:
  open;

negative-cycle baseline family:
  open;

pulse/run-core forever-defined positive state:
  reduced by `L-8251/L-8252` to one nonnegative ordinary centered quotient
  staying forever in high dyadic branch cylinders; open and constructive.
```

## Read first

1. `claims/L-8251-nine-b-two-place-synchronizer.md`
2. `claims/L-8252-centered-high-block-expansion.md`
3. `../../experiments/X-8251-nine-b-synchronizer/README.md`
4. `SOURCE_LEDGER_SYNCHRONIZER.md`
5. `claims/T-8202-all-repetition-single-pulse-exclusion.md`
6. `ALL_REPETITION_SINGLE_PULSE.md`
7. `../../experiments/X-8202-single-pulse-log-reduction/README.md`
8. `claims/L-8201-fixed-pulse-cone-resultant-caps.md`
9. `OUTLIER_BRIDGE_AUDIT.md`
10. `SOURCE_LEDGER.md`
11. `SOURCE_LEDGER_ALL_REPETITION.md`
12. `../../experiments/X-8201-pulse-resultant-caps/README.md`
13. `../../reports/gpt56-outlier-01/2026-07-23-52-nine-b-synchronizer.md`
14. `../../reports/gpt56-outlier-01/2026-07-23-52-single-pulse-all-repetition.md`
15. `../../reports/gpt56-outlier-01/2026-07-23-52-outlier-bridge-audit.md`

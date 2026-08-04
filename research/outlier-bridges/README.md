# Outlier bridges: remote-theory transfers into the Collatz counterexample frontier

**Agent:** `gpt56-outlier-01`  
**Issue:** #52  
**Branch:** `agent/gpt56-outlier-01/52-outlier-bridge-audit`  
**Namespace:** `82xx`

## Scope

This packet deliberately searches disciplines whose native language does not initially look like Collatz. A bridge is retained only when the repository object, the external theorem or technique, every material hypothesis, and the exact prospective output can be written down.

The packet is independent of issue #7's citation-critical audit. It does not replace that work and makes no global novelty claim. “New” below means only **not located in the branch-aware repository sweep recorded in this packet**.

## Main results

### `L-8201` — fixed pulse cones are finite

The negative-cycle pulse equations of PR #47 / PR #51 form a sparse Laurent-polynomial system. Eliminating one pulse variable at a time gives a two-by-two Sylvester determinant. A unique minimum 2-adic valuation proves that every eliminant is nonzero and yields an explicit uniform bound on that pulse height.

Consequently, for every fixed negative accelerated cycle word—including a fixed repetition and rotation—the entire cone of coordinatewise positive valuation pulses contains only finitely many possible positive-cycle divisibility hits, with effectively computable bounds.

### `T-8202` — the single-pulse repetition axis collapses

For one pulse, divisibility forces an exponentially small linear form in `log 2` and `log 3`. An explicit Matveev bound gives finite repetition cutoffs; certified continued fractions reduce the remaining infinite range to finitely many primitive upper convergents; exact size inequalities reject every positive multiple.

Subject to independent reconstruction of the quoted Matveev theorem, no single upward pulse in any repetition or rotation of either known negative accelerated cycle produces a nontrivial positive cycle. The unique hit is `(1,2)->(2,2)`, `n=1`.

### `T-8255` — the complete two-pulse repetition axis collapses

For two pulse locations, rotate the first pulse to zero and choose the shorter cyclic gap. If `t=d_1+d_2`, the exact correction gives the gap-uniform bound

```text
0<Lambda
 <2 c_* 3^floor(k r/2)/U^r,
Lambda=(t-r log_2(Q/U))log(2).
```

The same two-logarithm architecture now gives all-repetition cutoffs

```text
P3:  r < 100,000,000,000,
P11: r <  25,000,000,000.
```

Legendre reduction and certified continued fractions produce eighteen primitive upper families. Seventeen are excluded by one uniform size inequality; the exceptional `1/5` family is excluded exactly because two positive pulses force multiplicity at least two. The remaining small repetitions are exhausted using the nonzero two-pulse eliminants.

Subject to the same primary-source review boundary, **every two-pulse lift of every repetition, rotation, gap, and positive pulse-height pair over the two known negative cycles is excluded**, except

```text
(1,2,1,2) -> (2,2,2,2),
n=1.
```

This is an exhaustive infinite-class exclusion, not a larger bounded scan.

### `L-8251`–`L-8254` — constructive synchronizer and reset normal form

Grouping one high run with eight zero runs produces an exact nine-macro synchronizer. Centering at its common two-place residue yields positive pointwise expansion from run `44`, a Bézout-centered fixed 36-bit reset gate, and an exact exponent isometry compiling every finite high-run future.

These results do not extract an ordinary infinite seed. Their remaining obligation is finite-support closure of the infinite exponent address.

No nontrivial positive cycle, divergent seed, or Collatz counterexample is claimed.

## Claims and experiments

| ID | Status | Content |
|---|---|---|
| `L-8201` | `PROPOSED` | Sparse-resultant caps for every fixed finite pulse support; fixed negative-cycle pulse cone is finite. |
| `X-8201` | `EMPIRICAL` | Exact reconstruction of resultants, valuations, bounds, and two-pulse specialization. |
| `T-8202` | `PROPOSED / SOURCE-DEPENDENT` | All-repetition single-pulse exclusion over the two known negative cycles; unique hit `n=1`. |
| `X-8202` | `EMPIRICAL` | Exact cutoff, continued-fraction, candidate, and small-case certificate. |
| `T-8255` | `PROPOSED / SOURCE-DEPENDENT` | All-repetition two-pulse exclusion over every rotation, gap, and positive pulse-height pair; unique hit `n=1`. |
| `X-8255` | `EMPIRICAL` | Two independent exact implementations: 38 CF rows, 18 primitive families rejected, 898 small positive-denominator candidates, zero nontrivial hits. |
| `L-8251` | `PROPOSED` | Nine-B synchronizer and maximal common prime-to-six boundary residue. |
| `L-8252` | `PROPOSED` | Centered high-block quotient; every defined branch `s>=44` has positive toll and strict pointwise growth. |
| `L-8253` | `PROPOSED` | Bézout-centered 36-bit reset normal form. |
| `L-8254` | `PROPOSED` | Canonical exponent isometry and exact finite high-word compiler. |
| `X-8251` | `EMPIRICAL` | Independent exact synchronizer, centered quotient, physical replay, and pair-law audit. |

## Other retained bridges

1. **Catastrophic convolutional encoders.** A bounded-memory linear compiler mapping infinite directive data to finite support is exactly a catastrophic encoder; left-prime/minor tests can reject or expose that format.
2. **Primitive divisors in arithmetic dynamics.** A possible fresh-prime mechanism for PR #49, presently blocked by its nonautonomous degree-one form.
3. **2-adic T-functions.** Potentially useful for inverse address generators, not directly applicable to the partial expanding forward charts.
4. **Homoclinic algebraic dynamics.** Summability or decay is weaker than finite-support ordinary initialization; presently a firewall.

## Current infinite-axis register

```text
pulse heights at fixed word/support:
  exact finite by L-8201;

single-pulse repetition over the two known baselines:
  source-conditionally closed by T-8202;

two-pulse repetition over the two known baselines:
  source-conditionally closed by T-8255;

growing support with growing repetition:
  open;

negative-cycle baseline family:
  open;

pulse/run-core forever-defined positive state:
  reduced by L-8251--L-8254 to one ordinary finite-support closure problem;
  open and constructive.
```

## Read first

1. `claims/T-8255-all-repetition-two-pulse-exclusion.md`
2. `../../experiments/X-8255-two-pulse-all-repetition/README.md`
3. `../../reports/gpt56-outlier-01/2026-07-26-52-two-pulse-all-repetition.md`
4. `claims/T-8202-all-repetition-single-pulse-exclusion.md`
5. `ALL_REPETITION_SINGLE_PULSE.md`
6. `../../experiments/X-8202-single-pulse-log-reduction/README.md`
7. `claims/L-8201-fixed-pulse-cone-resultant-caps.md`
8. `claims/L-8251-nine-b-two-place-synchronizer.md`
9. `claims/L-8252-centered-high-block-expansion.md`
10. `claims/L-8253-bezout-reset-normal-form.md`
11. `claims/L-8254-canonical-exponent-isometry.md`
12. `OUTLIER_BRIDGE_AUDIT.md`
13. `SOURCE_LEDGER.md`
14. `SOURCE_LEDGER_ALL_REPETITION.md`

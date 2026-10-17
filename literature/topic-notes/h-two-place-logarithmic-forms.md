# H frontier: two-place logarithmic forms and S-unit proper-subsums

## Current native interfaces

The H program now has two exact ordinary-section coordinates.

1. The centered ghost rooms write a positive ordinary ghost as
   ```text
   P=4+4^(q+1)z,
   ```
   with fixed room index `q` and positive odd `z`.
2. Successive bridge cores satisfy an exact two-place equation of the shape
   ```text
   8^R 4^b Y - 9^R 3^a X = 9^R - 8^R.              (1)
   ```

The termination target is equivalently divergence of the monotone ordinary-section minimum `nu_K`.

## Two complementary external tools

### Explicit two-term p-adic logarithmic forms

When the native reduction produces a difference

```text
alpha^m-beta^n
```

of powers of fixed algebraic numbers, explicit two-term p-adic logarithmic-form estimates bound its valuation. Chim's 2025 theorem and Bugeaud's earlier `m`-adic theorem are the closest located sources.

The native file must specify:

- the algebraic numbers `alpha,beta`;
- the prime or composite `m`-adic valuation;
- multiplicative independence;
- exponent ranges;
- the exact upper valuation demanded by the H bridge;
- and every source constant.

### Nondegenerate S-unit finiteness

If `(1)` can be normalized to a fixed finite-rank multiplicative equation, `LIT-KTHM-0043` gives finiteness of nondegenerate solutions. The variables `X,Y` must first be split into:

```text
persistent prime support
+ fresh prime support.
```

The persistent part can lie in a fixed finite-rank group. Fresh primes must be controlled by the discounted budget or shown to force a proper-subsums contradiction.

## Suggested proof architecture

1. Freeze two adjacent core types and derive the exact normalized equation.
2. Enumerate every proper vanishing subsum.
3. Prove that an infinite chain cannot remain in a degenerate subsum family.
4. Apply S-unit finiteness to the nondegenerate cases.
5. For the surviving critical two-term cases, apply an explicit p-adic logarithmic-form estimate.
6. Convert the bound into growth of `nu_K` or a finite transformed-height trap.

## Why both tools are needed

The S-unit theorem is qualitative but handles several terms and finite-rank groups. Two-logarithm estimates are quantitative and can attack one critical near-equality. The H branch naturally splits into exactly these two regimes.

Neither tool may be invoked from the visual form of `(1)` alone. Prime support, nondegeneracy, and source hypotheses remain native obligations.

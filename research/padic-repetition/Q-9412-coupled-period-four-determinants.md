# Q-9412 — Coupled period-four completion-height determinant

Claim ID: `Q-9412`  
Title: Can a genuinely coupled phase determinant cross the period-four rationality threshold?  
Status: `IDEA` / primary periodic target after `T-9416`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-9410`, `L-9411`, `T-9416`, `R-9404`, `R-9405`  
Scope: primitive positive periodic words of minimal period four

## Exact boundary

The equal block Gaussian-binomial family has exponent

```text
mu_4=0.993714361875...,
```

missing the elementary rationality threshold by

```text
0.006285638124... .
```

`T-9416` now proves that no unequal phasewise root allocation can improve this
universal pre-reduction exponent. `R-9405` shows that the closest broad p-adic
q-series theorem cannot be imported directly because the stack parameter expands
at both the `2`-adic and archimedean places.

Thus the next construction must be genuinely coupled.

## Target A — adjacent-order Casoratian

Use several neighboring block-Padé pairs

```text
(A_n,B_n), (A_(n+1),B_(n+1)), ...
```

and shifts in the auxiliary block variable to align their first surviving
errors. Construct an exact determinant whose combined error cancels a number of
block coefficients growing proportionally to `n`.

A bounded number of extra cancellations changes valuation only by `O(n)` and
cannot repair an `O(n^2)` exponent deficit. The cancellation depth must itself
grow linearly with Padé order.

Every proposed determinant must prove:

```text
1. exact nonvanishing;
2. exact first surviving phase/block;
3. exact v_2 of the combined error;
4. a common odd denominator;
5. an upper bound for reduced global height;
6. a limiting exponent strictly greater than one.
```

## Target B — phase-sensitive Hermite–Padé

The universal denominator uses only the phase count. A stronger system may use
the actual transfer polynomial

```text
P_W(X)=sum_(j=0)^3 C_j X^j.
```

Search for polynomial vectors whose orthogonality conditions cancel the **sum**
of the four phases rather than each phase separately. This can be more efficient
than four independent windows, but its arithmetic height must be audited after
evaluation at `T=64/81`.

## Target C — completion-height numerator

PR #16's carry theorem and PR #33's block recurrence suggest a direct product-
formula route. Combine several phase errors into one ordinary integer `N_n` with

```text
v_2(N_n) > log_2 |N_n|.
```

A valid proof must show `N_n!=0` from exact phase/carry data. Merely exhibiting a
large `2`-adic valuation is insufficient.

## Target D — reduced-height saving

A common-factor theorem remains viable. The required asymptotic saving is only
`0.6286%` on the logarithmic scale. But `O-9401` found only tiny bounded gcds at
orders through three. A proof must give a quadratic lower bound for the gcd or a
different integral normalization; a longer table does not qualify.

## Cross-workstream interfaces

- **PR #16:** integral carry quantization and centered ordinary-section
  coordinates may provide nonvanishing or a completion-height numerator.
- **PR #33:** the exact new-block recurrence gives a finite state on which a
  determinant or trap potential may be expressed.
- **PR #3:** the forward quadratic ordinary bulk generator is a possible
  construction-side work tape, but residual cylinder membership is unproved.
- **Issue #21:** finite-state feedback collapses to an open-loop tail for ordinary
  integers, so a period-four value theorem is not bypassed by a hidden finite
  feedback implementation.

## Success outcomes

### Obstruction

Prove exponent `>1` for every primitive period-four word. Then `T-9415` extends
verbatim to every finite prefix followed by a period-four tail.

### Construction

If one period-four word yields eventual cylinder-block stabilization, reconstruct
its exact ordinary context, prove positivity of every stage, check the chart
class modulo `17`, replay the Collatz lift, and only then create a `K-####`
candidate.

## Falsification criteria

- Phasewise root redistribution is already closed by `T-9416`.
- Cancelling only `O(1)` additional block coefficients cannot change the
  quadratic exponent.
- A determinant with no nonvanishing proof is not an approximant.
- Pre-reduction height is not reduced height.
- A period-four theorem alone does not decide the balanced nonperiodic directive.
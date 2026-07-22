# Q-9411 — Period-four reduced-height saving

Claim ID: `Q-9411`  
Title: Can a genuinely coupled period-four construction recover the missing `0.6286%` logarithmic gain?  
Status: `NARROWED IDEA`; unequal phase allocation superseded by `T-9416`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-21  
Last updated: 2026-07-22  
Dependencies: `L-9410`, `L-9411`, `T-9416`, `R-9403`, `R-9404`  
Scope: primitive positive periodic height-increment words of minimal period four

## Current exact boundary

For the equal block Gaussian-binomial approximants of `L-9410`,

```text
mu_4=0.993714361875...,
1-mu_4=0.006285638124... .
```

The universal estimate misses the elementary rationality threshold by about

```text
0.6285638124%
```

on the logarithmic scale.

## Resolved route — phase reallocation

`L-9411` constructs the complete one-root-product family with arbitrary
phasewise cancellation counts. `T-9416` proves that equal allocation uniquely
maximizes its universal pre-reduction valuation-to-height shape.

Therefore this proposed repair is closed:

> Give more Gaussian-binomial roots to selected phases and fewer to the others.

Every such allocation has exponent at most `mu_4`. `R-9404` records the
refutation and its boundary.

## Remaining routes

### 1. Exact common-factor growth

Let

```text
A_n^clear,
B_n^clear
```

be the cleared integer numerator and denominator of a period-four approximant.
A sufficient target is a quadratic-scale common factor satisfying

```text
log gcd(A_n^clear,B_n^clear)
 >=(0.006286+epsilon)
   *log max(|A_n^clear|,|B_n^clear|)
```

along an infinite sequence. `O-9401` finds no bounded-order signal, but that is
not an asymptotic theorem.

### 2. Coupled adjacent-order determinant

Combine shifted neighboring Padé orders so their **combined** phase errors
cancel. The number of additional cancelled blocks must grow proportionally to
Padé order; cancelling only `O(1)` blocks changes valuation by `O(n)` and cannot
repair an `O(n^2)` deficit.

Every determinant must prove:

```text
- nonvanishing;
- exact first surviving block and phase;
- exact v_2;
- exact common denominator;
- reduced-height control.
```

### 3. Phase-sensitive Hermite–Padé

Exploit the actual transfer polynomial

```text
P_W(X)
```

and cancel the sum of the four phases rather than imposing independent windows.
This lies outside `T-9416` only if the construction is genuinely coupled.

### 4. Completion-height numerator

PR #16 and PR #33 supply compatible carry/block coordinates. Seek one nonzero
ordinary numerator built from several phase errors whose `2`-adic divisibility
outgrows its global height.

### 5. Construction signal

If one word exhibits eventual cylinder-block stabilization, replay its exact
ordinary context, prove positivity at every stage, check the chart class modulo
`17`, and only then promote a candidate.

## External-theorem boundary

`R-9405` audits Rochev's 2011 p-adic q-series theorem. The stack parameter expands
at both the `2`-adic and archimedean places, while the inspected theorem is
organized around one expanding place. The direct black-box route is therefore
not available.

## Verification program

`X-9410` exhausts 657,774 phase allocations and confirms the exact functional
bound. Future experiments should focus only on mechanisms outside the
root-product class:

1. coupled determinants;
2. exact reduced gcd growth;
3. phase-sensitive polynomial systems;
4. completion-height numerators.

## Success criteria

### Obstruction theorem

Prove exponent greater than one for every primitive period-four word. `T-9415`
then extends automatically to every finite prefix followed by such a tail.

### Construction

Produce one stabilized positive ordinary context with complete replay and chart
translation.

## Falsification criteria

- Phasewise root redistribution is already closed by `T-9416`.
- A bounded-order gcd pattern is not an asymptotic theorem.
- A determinant with no nonvanishing proof is not an approximant.
- Pre-reduction height is not reduced height.
- A period-four theorem does not decide the balanced nonperiodic directive.

## Relationship to the S-adic frontier

Any mechanism that genuinely repairs period four—coupled cancellation,
completion height, or reduced-height compression—is a plausible local building
block for adjacent continued-fraction standard words in the balanced directive.
See `Q-9412-coupled-period-four-determinants.md` for the frozen next target.
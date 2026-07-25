# Periodic extraction and the full-denominator boundary

**Agent:** `gpt56-complexity-01`  
**Issue:** `#59`  
**Status:** theorem-level claims are `PROPOSED`; no counterexample candidate

## Purpose

This packet steps away from finite-prefix amplification and asks one global question:

> What does ordinary-integer extraction become when the exact Collatz itinerary is eventually periodic?

The answer is complete. There is no residual compactness problem in this class; ordinary extraction is exactly the finite full-denominator cycle equation.

## Main theorem

For a finite shortcut parity word `w` of length `L`, with `s` odd branches,

```text
T_w(x)=(3^s x+C_w)/2^L.
```

The exact periodic completion is

```text
x_w=C_w/(2^L-3^s).
```

Therefore:

```text
3^s>2^L:
    x_w<0;
    the supercritical periodic schedule is a signed 2-adic completion ghost;

3^s<2^L:
    x_w is a positive ordinary integer
    iff 2^L-3^s divides C_w;
    then w is a positive cycle itinerary.
```

Every positive ordinary eventually periodic itinerary therefore eventually enters a positive integer cycle. A finite preperiod still requires exact replay.

## Consequences

- Every supercritical periodic schedule, at every period, is excluded as a positive divergent-orbit certificate.
- Every autonomous finite-state schedule-first certificate is excluded from producing divergence: its output is eventually periodic.
- A positive periodic hit is not another conditional amplifier; it is already the full-denominator finite-cycle certificate.
- The explicit `(1110)^infinity` ghost `-19/11` from PR `#57` is one instance of the general theorem.
- Genuinely aperiodic seed-first machines remain open and must be decided by bounded least roots, eventual residue stabilization, or an explicit all-time seed.

## Files

1. [`claims/T-7401-eventual-periodicity-full-denominator.md`](claims/T-7401-eventual-periodicity-full-denominator.md)
2. [`ARCHITECTURE_AUDIT.md`](ARCHITECTURE_AUDIT.md)
3. session report under `reports/gpt56-complexity-01/`

## Full-objective boundary

This theorem closes an exhaustive class strictly narrower than Collatz. It does not decide aperiodic itineraries.

The remaining accepted global targets are:

```text
ordinary-orbit side:
    prove one architecture's least roots bounded or divergent;

cycle side:
    prove C(w)=n(2^A-3^k) for the entire denominator and replay;

sanctuary side:
    produce one finite verified invariant ordinary language.
```

No new finite experiment is included because none is needed for the theorem.

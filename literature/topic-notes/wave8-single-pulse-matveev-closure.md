# Wave 8 addendum — PR #53 closes all repetitions in the single-pulse families

**Post-freeze source head:** `cd6cf9ca76fb028966b4a638d9fb19fd8934849f`  
**Native claim:** PR #53 `T-8202`  
**Status:** native `PROPOSED / SOURCE-DEPENDENT`; no promotion here

## Result appreciated

For either known primitive negative accelerated cycle, repeat the cycle an arbitrary number `r>=1` of times, rotate it arbitrarily, and increase one valuation by an arbitrary `delta>=1`.

The exact single-pulse condition reduces to

\[
 D_{r,\delta}=U^r2^\delta-Q^r
 \mid
 c_z(2^\delta-1).
\]

This forces the positive logarithmic form

\[
 \Lambda=(Ar+\delta)\log2-kr\log3
\]

to obey an exponentially small upper bound

\[
 0<\Lambda<2c_{\max}/U^r.
\]

PR #53 then uses Matveev's explicit lower bound to obtain a finite repetition cutoff. Below the cutoff, Legendre's theorem forces `delta/r` onto a certified finite list of upper continued-fraction convergents of

\[
 \alpha=k\log_2(3)-A.
\]

A final exact inequality excludes every positive multiple of every primitive convergent. The unique reduced divisor hit is the trivial transformation `(1,2)->(2,2)` giving `n=1`.

Subject to independent source-level reconstruction, this is an all-repetition theorem, not a bounded scan.

## Strategic meaning

This realizes the exact literature ladder proposed earlier:

```text
native divisibility
 -> exponentially close powers of 2 and 3
 -> explicit logarithmic-form cutoff
 -> certified continued fractions
 -> exact finite replay.
```

The next offense should generalize this architecture to fixed supports with two or more independently capped pulses.

## Generalization target

After `L-8201` caps every pulse height for one fixed support, freeze one surviving pulse vector and derive one repetition-only equation. Seek either:

1. one dominant real logarithmic form plus a correction small enough for Matveev/Legendre;
2. simultaneous real and `2`-adic logarithmic forms followed by de Weger lattice reduction;
3. a large-gcd contradiction for independent exponential sequences;
4. a proper vanishing subsum, promoted as a separate resonant constructive family.

The single-pulse theorem demonstrates that repetition length is not intrinsically beyond explicit Diophantine control.

## Source boundary

The located primary record is E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64 (2000), 1217–1269, DOI `10.1070/IM2000v064n06ABEH000314`.

The exact constant normalization and all rational interval arithmetic remain native PR #53 proof obligations and should be independently reconstructed.

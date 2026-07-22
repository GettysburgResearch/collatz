# Literature audit — centered rational powers and nearest-integer cylinders

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Date:** 2026-07-22  
**Status:** applicability audit; no native theorem is promoted by literature matching

## 1. Native object

`T-9315` identifies the ordinary section of the induced `64 -> 81` system with

\[
\mathcal Z^{\rm ctr}_{64,81}
=
\left\{
\xi>0:
\left\|
\xi(81/64)^n
\right\|
\le1/81
\quad\forall n\ge0
\right\}.
\]

This is a fixed-ratio nearest-integer problem, but it carries additional exact structure:

1. the nearest integers satisfy
   
   \[
   64B_{n+1}-81B_n
   =\varepsilon_n-arepsilon_{n+1};
   \]
2. the digit is the sign of the centered error;
3. the initial nearest integer is selected by one nested base-64 cylinder;
4. ordinary realization is eventual stabilization of that cylinder;
5. `81/64=(3/2)^4` gives the scheduled intermediate geometry of `L-9312`.

The literature below must be compared with this exact target, not with a generic phrase such as “Mahler-type problem.”

## 2. Schleischitz's rational centered bound

Johannes Schleischitz, *Integral powers of numbers in small intervals modulo 1: The cardinality gap phenomenon*, Uniform Distribution Theory 12 (2017), arXiv:1501.07176.

Theorem 2.7 states that for a nonintegral rational ratio

\[
\zeta=p/q>1,
\]

there is no nonzero `alpha` whose sufficiently late powers all lie in the centered interval

\[
[-1/(p+q),1/(p+q)]\pmod1.
\]

For

\[
p=81,
\qquad q=64,
\]

this excluded radius is

\[
\boxed{1/(p+q)=1/145.}
\]

The native critical radius is

\[
\boxed{1/81>1/145.}
\]

### Verdict

**KNOWN NEAR MISS / HYPOTHESIS TOO WEAK.**

The theorem proves emptiness for a strictly narrower centered strip. It does not exclude `T-9315`'s critical set.

A valid improvement route could try to use the extra three-state cylinder structure to strengthen `1/145` to `1/81`, but the published theorem cannot be quoted as already doing so.

## 3. Dubickas's nearest-integer limit points

Artūras Dubickas, *On the distance from a rational power to the nearest integer*, Journal of Number Theory 117 (2006), 222--239, DOI `10.1016/j.jnt.2005.07.004`.

The paper proves explicit large and small limit-point results for

\[
\left\|\xi(p/q)^n\right\|.
\]

The constants depend on `p,q` and are related to the Thue--Morse sequence.

### Verdict

**RELEVANT, EXACT CONSTANT AUDIT STILL REQUIRED.**

The abstract alone is insufficient to claim that its large-limit-point constant for `81/64` exceeds `1/81`. No such implication is imported in this packet.

Before using this paper as a black box, a reviewer must:

1. identify the exact theorem and constant for `p=81,q=64`;
2. verify all rational/irrational hypotheses on `xi`;
3. compare the constant to the closed critical radius `1/81`;
4. check whether the conclusion is a limsup, one limit point, or an all-time obstruction.

## 4. Flatto--Lagarias--Pollington range theorem

Leopold Flatto, Jeffrey C. Lagarias, Andrew D. Pollington, *On the range of fractional parts `{xi(p/q)^n}`*, Acta Arithmetica 70 (1995), 125--147, DOI `10.4064/aa-70-2-125-147`.

This work gives lower bounds for the Euclidean range of fractional parts of rational powers.

### Verdict

**METHOD AND CONTEXT; NO DIRECT TRANSFER.**

The native condition

\[
\|y\|\le1/81
\]

means

\[
\{y\}
\in
[0,1/81]
\cup
[80/81,1),
\]

which is a centered circle neighborhood represented by two endpoint intervals in `[0,1)`. Treating the total length as the length of one Euclidean interval changes the object.

After `L-9313`, there is a further boundary: every binary itinerary has a real centered-error path. The unresolved condition is arithmetic nearest-integer cylinder stabilization, which a range theorem for real fractional parts alone does not see.

## 5. Dubickas's forbidden two-interval theorem for `3/2`

Artūras Dubickas, *On the powers of 3/2 and other rational numbers*, Mathematische Nachrichten 281 (2008), 951--958, DOI `10.1002/mana.200510651`.

The paper proves, among other results, that no complete `3/2` orbit is contained in the fixed union

\[
[8/39,18/39]
\cup
[21/39,31/39].
\]

### Verdict

**GENUINE NEIGHBOR, TARGET SET MISMATCH.**

`L-9312` imposes a periodic four-phase schedule with different centers and radii, synchronized to the nearest-integer residue states `0,15,49`. It is not the fixed union in Dubickas's theorem.

No direct affine change of variables identifying the two targets is supplied. Therefore the theorem is not a nonexistence result for the repository schedule.

## 6. Negative rational powers — Lu and Zheng (2026)

Qing Lu and Weizhe Zheng, *Fractional parts of powers of negative rationals*, arXiv:2603.16794 (2026).

They prove a range lower bound for the fixed multiplier

\[
-p/q.
\]

### Verdict

**CURRENT LITERATURE, SIGN DYNAMICS MISMATCH.**

The centered error sign in `T-9315` changes according to the itinerary. Multiplying by the sign converts the absolute error to a positive number, but the resulting step multiplier is `+81/64` or `-81/64` depending on whether the itinerary keeps or flips sign. It is not one fixed negative rational multiplier.

The theorem cannot be imported without a new reduction from the variable-sign cocycle to the fixed-sign setting.

## 7. Cardinality-gap results

Schleischitz and related work distinguish radii for which the set of parameters is countable from radii for which it is uncountable.

### Verdict

**NOT A NONEXISTENCE THEOREM HERE.**

The ordinary section is already at most countable because every centered parameter reconstructs an ordinary starting integer by

\[
A_0=\lceil64\xi\rceil.
\]

Showing countability of the centered parameter set does not exclude any ordinary point.

## 8. Mahler's classical `3/2` problem

Mahler's classical `Z`-number problem asks for a positive real number whose complete `3/2` orbit remains in a fixed one-sided interval.

### Verdict

**EXACTLY RELATED AFTER `T-9315`, BUT NOT EQUIVALENT.**

The repository now has an exact centered rational-power formulation and a four-phase `3/2` schedule. However:

- the target is centered rather than one-sided;
- the phase sets vary periodically;
- the arc choice carries a nearest-integer residue state;
- the real error language has full symbolic support;
- ordinary realization is an inverse-limit stabilization property.

The phrase *generalized centered Z-number problem* is appropriate. Calling it Mahler's original problem, or importing an interval-width constant without a reduction, is not.

## 9. Reframed literature target

The highest-value external theorem would have one of these forms:

1. a nearest-integer limsup bound for `81/64` strictly larger than `1/81`;
2. a scheduled-union range theorem that retains the `0,15,49` state transitions;
3. a product-formula or Subspace-Theorem result for the shared real/`2`-adic coefficient series;
4. a theorem excluding ordinary values of the completion series
   
   \[
   -\sum_{n\ge0}
   (\varepsilon_n-\varepsilon_{n+1})
   64^n/81^{n+1}
   \]
   for every nontrivial binary itinerary;
5. a determinant theorem showing that eventual zero cylinder blocks force an impossible rational approximation exponent.

Until such a match is proved, the universal nonstabilization theorem remains native.

## 10. Source list

- Schleischitz, arXiv:1501.07176, published in *Uniform Distribution Theory*.
- Dubickas, DOI `10.1016/j.jnt.2005.07.004`.
- Flatto--Lagarias--Pollington, DOI `10.4064/aa-70-2-125-147`.
- Dubickas, DOI `10.1002/mana.200510651`.
- Lu--Zheng, arXiv:2603.16794.

No result in this audit promotes `Q-9301` or `Q-9303`.
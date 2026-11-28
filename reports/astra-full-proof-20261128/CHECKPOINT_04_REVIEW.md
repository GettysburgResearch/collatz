# Coordinator review: the signed average and the critical denominator band

28 November 2026. This is an interim checkpoint in the authorized three-hour
pass. **Collatz remains open in this packet.** This review reconstructs the
new deductions; it is not a claim that the full analytic arguments were
formalized.

## 1. The smaller sufficient analytic target

Let \(T\) be the shortcut map, \(Q_t(n)\) its number of odd departures before
date \(t\), and put

\[
 \lambda=\log_2 3,\quad D=1-\lambda/2,\quad
 M=\lfloor k/D\rfloor,\quad W=\sqrt{k\log(k+2)}.
\]

Choose even \(g\) with \(W=o(g)\) and \(g=o(k)\). The source measure is exactly
uniform on the original positive integers \(1,\ldots,2^k\). With
\(\beta=1/\log_2(10/3)\) and \(b=\beta-1/2>0\), the new written deduction is

\[
 \mathbb E[Q_{M+g}-(M+g)/2]
 \ge b g\,\Pr\{\tau_1>M+g\}-O_A(W+k^{1-A}).
\]

Also \(|\mathbb E(Q_M-M/2)|=O_A(W+k^{1-A})\). Thus a liminf at most zero
for the centered average on just the following \(g\) dates suffices for
universal convergence. A fixed bad target would have positive lower
predecessor density, contradicting the vanishing bad fraction obtained
along that subsequence. Both a nonstandard cycle and an escaping orbit
would supply such a target.

I checked the three interfaces separately:

1. [Weaver 191, version 2, Theorem 1 and Section 4](https://rstation.ai/problems/collatz/papers/191/v2)
   give a common actual polylogarithmic landing at
   \(u=M+O_A(W)\), with centered odd count \(O_A(W)\), outside
   \(O_A(k^{-A})\) of the source population. The displayed theorem really has
   \(\sqrt{LB}\), so choosing \(B=K_A\log L\) gives the stated \(W\).
   Simultaneous shortcut and ordinary passage clocks recover the odd
   count of the same crossing. No independent law is assigned after landing.
2. On every positive suffix the odd undivided multiplier is at most 4,
   so its centered count is at least minus half the logarithm of its
   initial height. If the source has not hit 1 by the final date, every
   odd state in this suffix is at least 3, and the multiplier improves
   to \(10/3\). This produces the strictly positive \(bg\) gap.
3. Exceptional sources contribute at most \(O(k)\) each to this finite
   statistic, and hence \(O_A(k^{1-A})\) to its mean. Mazur's theorem is
   used only after the actual-source estimate, with its provenance
   retained in the existing outside-input note.

This proof avoids the minimum-distribution and fixed-cycle clock theorems
used in some earlier candidates. The outside first-passage theorem is
still an analytic dependency, read here as a written argument.

Full arguments:
[FIRST_MOMENT.md](../../research/astra-full-proof-20261128/descent/FIRST_MOMENT.md)
and [MODERATE_PARITY_AT_ONE.md](../../research/astra-full-proof-20261128/mass/MODERATE_PARITY_AT_ONE.md).

## 2. The exact ordinary endpoint flux

For \(b(n)=n\bmod2\),

\[
 b(y)+b(Ty)-1=
 {\bf1}_{y\equiv3\pmod4}-{\bf1}_{y\equiv0\pmod4}.
\]

Pairing the \(g\) dates therefore identifies the normalized centered mean
with the signed difference of the masses at endpoints \(4j-1\) and \(4j\).
The endpoint masses are pushed forward from the original positive
interval. Both 1 and 2 have zero paired charge. This is a linear target
with no rare-event normalization.

The local EndpointFlux module verifies the identity, its finite
all-natural paired-count sum, and vanishing on the standard pair. It
does not prove the upper bound on the source average.

The fixed-frequency Fourier result in
[Wren and Weaver 95](https://rstation.ai/problems/collatz/papers/95)
does not supply that upper bound. For each fixed primitive odd \(c\),
the known diffusive band contributes the same limiting value to the
positive window and its reflected negative window after averaging the
postcritical dates. The normalized interval character tends to 1 in
both cases. On the reflected window the whole centered mean is bounded
below by \(1/\log_2(3)-1/2-o(1)>0\). Thus finitely many such bands cannot
settle the required sign.

I checked the reflected argument using the positive lift
\(2^L-n\), \(L=2(M+g+1)\). It agrees with \(-n\) through the entire clock.
The translated first-passage bound controls the affine slope; the
nonnegative real offset then makes the negative endpoint small in
absolute value at the same intermediate date. The negative odd
multiplier is at most 3, giving the displayed positive gap.

## 3. The denominator ladder is exact but still has a critical band

The parity lane's ladder compares the same marked finite clock on
positive grids of mesh \(3^{-r}\). Its increment has an exact representation
at the formal \(r\)-th odd departure by ordinary positive integers \(y\),
weighted by \(3{\bf1}_{y\equiv2\pmod3}-1\). The stop is on the unreduced
denominator; it is not always the first time the rational state becomes
integral.

The upper anchor follows from a fair native prefix and a binomial
tail. For \(r\) below \(r_*-\sqrt{k}\log k\), where
\(r_*=k/(2-\log_2(3))\), the real sampling interval is large outside a small
exceptional set. The pinned PR215 count-only starting-trit estimate then
removes those low increments. I checked the order of the exclusions:
long words and large real offsets are first bounded under their actual
source mass, before dividing by the interval length.

The result leaves only \(O(g)\) levels around and above \(r_*\). At those
levels the real interval can have exponentially small length \(Y\), and
the exact formula includes \(1/Y\). An additive small-ball or Fourier
error cannot be substituted for a relative estimate there.

The coordinator reran the denominator replay: all 45 specified finite
signed-level identities passed with exact rational dynamics. This finite
replay checks the identity, not decay of the critical sum.

## 4. Formalization and evidence

The expanded core replay was run from a fresh temporary object directory,
in dependency order, with Lean 4.34.1, one worker, and warnings as errors.
All eight modules compiled:

| Module | Printed roots |
|---|---:|
| ParityTail | 3 |
| ClosureConsumer | 3 |
| ExternalClaimChecks | 3 |
| CountedDeadline | 2 |
| Resonance | 5 |
| SignedFloor | 2 |
| EndpointFlux | 3 |
| RationalControl | 3 |

The total is 24. Printed axiom lists contain only the standard
propext, Classical.choice, and Quot.sound, or smaller lists.
RationalControl verifies the 40-step, 25-odd lap for the positive
denominator-191 control and eventual entry for the specified finite
eligible range. It is not a proof about all inputs of that rational map.

[ALL_LOCAL_LEAN.json](ALL_LOCAL_LEAN.json) records source and object
hashes and the actual output. The previously compiled SignedDeathClock
has a separate agent-produced local receipt including its two pinned
PR200 parents. Outside Lean reports remain explicitly separate: no
external analytic development was rebuilt by this replay.

## 5. Continuing question

The active attempt is to control the ordinary signed flux or the exact
critical denominator increment using a positive real entrance kernel.
A bound on the rationally sampled endpoint law alone does not transfer
to the original positive integer source. Any proposed closure must state
and prove that transfer with its normalizing factors. The later kernel
work will be reviewed separately; no success is assumed in this checkpoint.

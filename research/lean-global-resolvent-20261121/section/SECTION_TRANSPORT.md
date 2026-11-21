# Transporting source mass to the mandatory dyadic section

## Scope and inputs

This analysis uses PR173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec`.
The shortcut map is `T(n)=n/2` on even inputs and `(3n+1)/2` on odd inputs.
For `d=floor(log2 n)`, the marked set is

\[
\mathcal S=\{n\text{ odd}: (d+1)(n-2^d)\le70\,2^d\}.
\]

The upstream theorem gives a bounded first visit to this set on every positive
orbit. Its first positive return `R(n)` can exceed `C n` for every prescribed
constant `C`. Neither result asserts convergence after repeated returns.

The new analysis below targets a specific potential completion: use the density
bound for this mandatory section to contract the primitive source moment in
PR176. It identifies an exact transport obstruction. It does **not** establish
a complete Collatz proof.

## Exact source mass is conserved by the first visit

Put `w(n)=n^-4` for positive `n` and `w(0)=0`. Let `E(n)` be the first marked
point at or after clock zero, and define the weighted pushforward

\[
G(m)=\sum_{n:E(n)=m}w(n).
\]

All sums converge, and partitioning the sources into fibers gives

\[
\boxed{\sum_mG(m)=\sum_nw(n).}
\]

The corresponding first-positive-return pushforward is

\[
H(m)=\sum_{n\in\mathcal S:R(n)=m}w(n),
\qquad
\boxed{\sum_mH(m)=\sum_{n\in\mathcal S}w(n).}
\]

A source atom retains its original weight during this transport. In particular,
`G(E(n)) >= w(n)` and, for marked `n`, `H(R(n)) >= w(n)`. A small number of
available endpoints does not reduce these weights.

This is exactly the issue when composing the new forward section with PR176's
primitive moment: that moment is weighted by the original sources `b_w`, while
the section's counting theorem concerns the current endpoints `r_w`.

## No constant controls the endpoint density

For every integer `C>=0`, there is a marked `m` such that

\[
\boxed{H(m)>Cw(m)}
\qquad\text{and, possibly at another }m,\qquad
\boxed{G(m)>Cw(m).}
\]

For the first inequality take the upstream expanding return
`m=R(n)>(C+1)n`. Then

\[
H(m)\ge n^{-4}>(C+1)^4m^{-4}>C m^{-4}.
\]

For the first-visit inequality take an expanding return with
`m=R(n)>2(C+1)n` and start the first-visit map at `a=T(n)`. Since `a<=2n`
and `E(a)=R(n)`,

\[
G(m)\ge a^{-4}>C m^{-4}.
\]

Thus the candidate estimate `G(m) <= C m^-4` is false for every fixed `C`.
The failure already occurs before iterating the return map. The same reasoning
applies to any positive power weight, and to a weight comparable to one by
fixed positive constants. This does not exclude source-history-dependent
weights or an arithmetic estimate across several returns.

### A concrete finite atom

The exact integer computation in `check_return_transport.py` verifies

\[
n=2^{8179}\cdot8200-1,\qquad
R(n)=3^{53}\,2^{8126}\cdot8200-1.
\]

Both points are marked. The ordinary shortcut clocks `1,...,52` are unmarked,
and clock `53` is the first positive return. All these steps are odd steps.
The endpoint exceeds `2^31 n`, so the transported atom is more than `2^124`
times the endpoint's fourth-power weight. This finite calculation makes no
assumption about later convergence of either integer. It is a Python exact
integer check, not an additional Lean theorem.

## What the narrowing section does provide analytically

The section supports a summable weight at the ordinary critical power `1`:

\[
W(n)=\frac1{n(\lfloor\log_2n\rfloor+1)},\qquad n\in\mathcal S.
\]

In octave `[2^d,2^(d+1))`, the upstream proof has at most
`71*2^d/(d+1)` marked points. Every point in that octave has weight at most
`1/[2^d(d+1)]`, giving total octave weight at most

\[
\frac{71}{(d+1)^2}.
\]

Consequently `sum_{n in S} W(n)` converges. On the full set of positive integers
the same series diverges: each octave contains `2^d` integers and contributes
at least `1/[2(d+1)]`. This is a genuine gain from the section, and a possible
space for a future induced transfer argument. The displayed summability
argument is written mathematics; it is not yet added to the Lean module.

It still does not supply drift. For the odd inverse map, the leading
`1/n` weight from all legal inverse exponents is `1/n` on a target congruent
to `1 mod 3`, `2/n` on a target congruent to `2 mod 3`, and zero on a multiple
of three. Their average over all three residue classes is critical, not
strictly contractive. Restricting inverse sources to ternary units retains
critical average coefficient over the six unit classes modulo nine:

| Target modulo9 | Leading coefficient of the unit-predecessor harmonic mass |
|---|---:|
|1|20/21|
|2|40/21|
|4|17/21|
|5|10/21|
|7|5/21|
|8|34/21|

These six coefficients sum to6. They come from the two admissible exponent
classes modulo6 in the geometric series `3*sum 2^-a`; the excluded third class
would produce a predecessor divisible by3. They are leading coefficients as
the target tends to infinity in its residue class, not exact finite-target
values.

For the extra factor `1/(log2 n+1)`, write `L=log2 m+1`. Averaging over the
six unit target classes makes the leading exponent weights exactly `2^-a`,
whose total mass is1 and whose mean exponent is2. The leading averaged
inverse weight is therefore

\[
\frac1m\sum_{a\ge1}\frac{2^{-a}}{L+a-\log_2 3}
=\frac1{mL}\left(1-\frac{2-\log_2 3}{L}+O(L^{-2})\right).
\]

This suggests an averaged logarithmic drift. Passing from the average to each
actual survivor component is the missing arithmetic step. A component could
correlate with the classes having coefficients above one; neither the band
membership nor its global count controls that correlation.

A fixed finite residue correction cannot simply turn this into a pointwise
power-weight contraction. For a correction depending only on `m mod3^K`, a
target `m=-1 mod3^(K+1)` and its legal `a=1` predecessor are in the same
corrected residue state. That single inverse branch already has asymptotic
power-weight multiplier `(3/2)^s>1` for every `s>0`. The marked leading interval
contains such residue classes at sufficiently large heights, so the high-bit
restriction does not remove this issue.

## The attempted global estimate and its remaining boundary

For a positive summable weight on marked points, let

\[
(P^Kw)(m)=\sum_{n\in\mathcal S:R^K(n)=m}w(n).
\]

If some fixed `K>=1` and `rho<1` satisfied `(P^K w)(m)<=rho*w(m)` for every
marked `m>1`, any nonconvergent component would have positive finite weight
and would contradict this inequality when summed over its marked points.
The component is unchanged by taking `K` returns, so its original source mass
must be preserved. This is a sufficient global completion estimate; it is not
proved here. For `K=1` and power-comparable weights it is false by the result
above. A fixed larger `K`, or a different explicit history-sensitive weight,
requires new arithmetic information. Nothing in the counting bound supplies it.

The inverse-logarithmic width is also a critical shrinking-target scale: on a
hypothetical exponentially growing orbit, `log n_j=O(j)`, so a band width of
order `1/log n_j` is consistent with an angular target of order `1/j` and
infinitely many visits. This observation does not assume such an integer orbit
exists; it identifies why phase recurrence alone gives no contraction.

## Verification status

- Exact pinned `ShellCover.lean`, `ForwardSection.lean`, `SectionDynamics.lean`,
  and `RisingReturns.lean` were replayed with Lean4.34.1 and the pinned mathlib
  checkout. All completed successfully with warnings treated as errors; the
  principal results print only `propext`, `Classical.choice`, and `Quot.sound`.
- `check_return_transport.py` passed using exact integers.
- `SectionTransport.lean` passed with `lean -j1 -DwarningAsError=true`. Its four
  principal theorems (`returnMass_total`, `entryMass_total`,
  `no_uniform_endpoint_bound`, `no_uniform_entry_bound`) use only
  `propext`, `Classical.choice`, and `Quot.sound`. There are no admitted
  placeholders or additional interface assumptions.

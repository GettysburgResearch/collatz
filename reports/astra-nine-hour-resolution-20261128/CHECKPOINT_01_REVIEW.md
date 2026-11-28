# First substantive checkpoint: independent reconstruction

**2026-11-28, approximately 13:05 UTC. The pass remains active until 21:33:06 UTC.**
There is no complete Collatz proof in this checkpoint. The purpose of this
review is to preserve actual mathematics while the team continues the global
attacks. This report is not an acceptance of every neighboring result or later
revision in a source branch.

## Fixed-cone trace approximation

Source: coordinator commit `95dd309a79377470d896700f372d4a66fdd7c259`,
`research/astra-nine-hour-resolution-20261128/CONE_ENVELOPES.md`, C1 and C2;
the checkpoint also restricts the displayed layer-test interface to bounded
tests, exactly as in its application and pinned outside source.

The analytic lane independently reconstructed the primary Valbuena interface
at `a7275d5a73814d3d9a400c6fe6577de9542b03a3`,
`paper/positive-stationary-envelope.tex`. It checked the direct one-odd-step
access to every ternary class, the nonperiodic target inside a prescribed cone,
the finite first-hit error, the factor two from the odd periodic mask, and the
greatest-representative step. The argument works when the supplied eligible
target is even. The first-hit restriction makes the finite deletion cost
independent of the depth.

**Verdict: reconstructed, source-qualified written deduction.** The external
envelope and marked first-hit theorems retain their author's formalization
claims; this pass did not rebuild that bundle. No bound on the ordinary size
of the approximants has been obtained, and their ternary closeness does not
assert merger with the integer being approximated.

## Spatial trace excess

Source: analytic lane `aea9231417768ad13b898d312a354cae24c23b35`,
`research/astra-nine-hour-resolution-20261128/analysis/SPATIAL_ENVELOPE_EXCESS.md`,
equation (1), imported at `1bca7c3441a0db55a4ea40c7e6e02ad1c0b3258e`.

The coordinator read the pinned outside envelope and raw-occupation arguments.
First-hit concatenation gives a fixed positive lower bound for the weighted
density at every future state of an escaping ray. The first upward odd crossing
above an integer `Y` is strictly below `3Y/2`; distinct components provide
distinct sites. Subtracting a fixed bounded cylinder minorant at these sites
prevents double-counting the baseline. Taking the source-shell limit before
the conductor limit gives the displayed additive excess. The endpoint ratio
`c=3/2` works for integer `Y`.

**Verdict: reconstructed, source-qualified written deduction.** Valbuena's
earlier integrated raw-occupation excess is explicitly credited. This note's
observable is an unweighted spatial mean in every fixed-ratio shell. An upper
estimate is still required, and the consumer excludes escape only.

## Ordinary two-weight conformal measures

Source: arithmetic lane `4d6a881619c26e30a6e2b1a4785333b88cc46183`,
`research/astra-nine-hour-resolution-20261128/arithmetic/ORDINARY_CONFORMAL_PRESSURE.md`,
equations (2)–(5) and the physical slope-family classification, imported at
`ccbf4b35ea70c63eb2a886b99c516ef5ade3dbc8`.

The coordinator checked Weaver202/v1, section 2, input (2), at its actual
fixed-total and extra-conductor scope. Prescribing the extra inverse-source
trit retains odd units. A full integral inverse word at a positive odd target
is a genuine positive path, and distinct total clocks at a fixed odd depth
are disjoint. The deterministic odd map also makes rows at different targets
disjoint. Summing against the finite absolute mass therefore gives equation
(4). Selecting one side of the central window gives the curved exclusion;
one nonperiodic target and disjoint depths exclude the product boundary.

The corrected height has the stated exact even/odd ratios. Positive cycles
have slope product below one, forcing zero mass there. On an escaping
component, the edge equations make `m(n)H(n)^p` constant. Uniform packing
bounds `H(n)` by a constant times `n`, so positive predecessor density gives
the sharp summability threshold one. These checks preserve the classification
for complex masses by first taking absolute values.

**Verdict: reconstructed, source-qualified written deduction.** The pressure
region does not meet the physical slope family at any proved exponent above
one. Finite measures may lose their mass at infinity as the exponent tends
down to one. Neither fact is a contradiction.

## Persistent addresses and marked transport

Sources: independent lane `414337fa81d4218b6972aefdf75b63fca7e8a3d9`,
`wild/DYADIC_BOUNDARY_ADDRESSES.md` and `wild/check_boundary_addresses.py`;
then `486538a5f8ce673a930513a8cf754743ca147120`,
`wild/FIRST_CORNER_RETURN.md`. Both paths are under
`research/astra-nine-hour-resolution-20261128/`.

The coordinator reconstructed the unique persistent child of an unlike pair,
the all-length merger family, the paired-alphabet restriction, and the extra
twelve-bit forbidden word. The dyadic color extension and the literal images
of left endpoint, midpoint, and right endpoint have the stated formulas.
Their unlike marked intervals nest and shrink in the nondyadic case. The
intermediate equal-color brackets mean this is not an invariant closed set
under multiplication by three. New pairs of boundaries can be born inside
an equal-color parent; the review retains that distinction.

For a long return, `n=(B'-1)/2` is 3 modulo 4. Two shortcut steps from `n`
reach `(9n+5)/4`; three from `3B'` reach the same value. This directly checks
the claimed ordinary merger and opposite-color multiplier defect. It does not
make the defect smaller than the preceding one.

The coordinator ran the supplied finite checker once, exit zero:

```text
780 merger-family cases and 440 transported returns passed; full factor language through 25 bits checked
```

**Verdict: reconstructed elementary written statements, plus the stated finite
replay.** No Lean verification of these new statements is claimed. The finite
checker does not certify arbitrary future colorings or complete termination.

## Continuing research

The agents are pursuing the actual upper comparisons, ordinary weighted
spectra, and boundary-birth geometry, while remaining free to change direction.
The coordinator continues independent work and wider-source intake. A new
obstruction or a sharpened sufficient condition is not the end of this pass.

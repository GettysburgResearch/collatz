# Concurrent PR158--160: final source comparison

The final source check found three additional research packets published
while this work was in progress. Three agents read their respective source
routes; the root also read all three overviews. This is a source and overlap
assessment, not a new complete review of those packets or a replay of their
checkers. None is a load-bearing dependency of the theorems here.

## PR158: physical expanding returns and partial carry compilation

Frozen head: `cf49a68bf93e98c97a18dc3d1a4186faf534e422`,
[PR158](https://github.com/GettysburgResearch/collatz/pull/158).
Directory: `research/ordinary-basin-closure-20261120/`.

`CERTIFICATE_CARRY.md`, sections 1--3, gives a partial ordinary compiler
for companions `R_j(x)=2^j x-1`. Sections 4--5 exhibit a depth-two
antecedent whose companion becomes a Mersenne number, with the refreshed
PR146 overlap explicitly credited. This is related to the general
certificate-debt obstruction, which our packet likewise does not claim to
have originated. It does not replace the distinct multiplier-five identities
in CD1--CD3: our first reset is `(9x+1)/4`, and our full target path reaches
`5z_r` after `6r+8` shortcut clocks.

`EXPANDING_RETURNS.md` adds actual guard-surviving 38-clock expanding
Q-return cylinders and exact finite budgets for repeating a fixed return
word. `TWO_MACRO_NORMALIZATION.md` studies switching between two such
words. Its section 4 retains section avoidance and the broader physical
closure as open. The partial compiler and these return theorems do not
prove forward-five closure. An ordinary predecessor of our reset antecedent
cannot be multiplied by five and treated as a merger without proving the
very multiplier transport that is missing.

The root also inspected the overview's separate finite-endpoint analytic
reduction: its small tail does not prove the required bound on the positive
head, and that route would still need nontrivial-cycle exclusion. It is a
different operator target from CA1--CA3.

## PR159: unshifted prime support and exact directed circulation

Frozen head: `0e7d2841b1591073c6399f91f3b6944ebcdbdbd5`,
[PR159](https://github.com/GettysburgResearch/collatz/pull/159).
Directory: `research/allhands-global-closure-20261120/`.

`PRIME_SUPPORT_PEAKS.md` gives the bound
`max n_j <= max{4^s n_0,(s+1)^(64s)}` for a finite prefix whose actual
odd states use at most `s` primes, and a source-free cycle-height bound.
These are stronger unshifted-support restrictions than the earlier rough
height scale. They concern primes dividing `n_j`; SC1--SC4 instead concern
the cores of `n_j+1`. Section 5 of that source explicitly rejects an
automatic transfer of its gcd-tail estimate to shifted values. It supplies
neither an upper bound on shifted-core creation nor the upper estimate on
outside-class visits required by SE2.

`DIRECTED_BOUNDARY_CIRCULATION.md` constructs a common positive weight
balancing both orientations of the tripling defect for exact ordinary
invariant labels, whenever either oriented moment is finite. Its
subcritical functional consequences retain their pinned inputs. This is
complementary to our endpoint obstruction: our cutoff and fixed-mixture
examples do not satisfy exact odd-branch invariance, while our actual
composition-operator cutoffs are approximate invariants, not exact labels.
Balanced positive circulation does not alone remove a nonempty cut or
establish finiteness of the missing moment.

## PR160: ordered prime height and conditional critical component mass

Frozen head: `6d877e718f5ef9d57fe1830912c444359718747a`,
[PR160](https://github.com/GettysburgResearch/collatz/pull/160).
Directory: `research/closure-attacks-20261120/`.

`arithmetic/CLOCK_HEIGHT.md`, AR-CLOCK-001--006, controls accumulated
unshifted prime height using the ordered ordinary recurrence. Its
dispersion and cycle-height restrictions leave the prime-support size
unbounded. These statements do not bound shifted cores or the unweighted
visit count `C_N` in SE1--SE2.

`critical/CRITICAL_SINGULARITY.md`, CS-001--003, conditionally describes
hypothetical exact components using a pinned positive-density input. Their
mass grows at the critical limit while normalization loses fixed atoms;
the source does not infer either the existence or absence of such a
component. This overlaps the broad warning about losing a fixed source
under normalization. It does not subsume EC1--EC5's unconditional relaxed
examples or CA1--CA3's exact defect limit `log(2)/2` and joint harmonic
approximate invariants.

`merger/SINGLE_MULTIPLIER.md` gives another compact symmetric multiplier-five
criterion and credits PR157's stronger one-way criterion. Our 13-cell
certificate is also presented only as an alternative symmetric certificate.
`critical/SINGLE_SLICE_ENERGY.md` proves specified local variation and
transport statements; it explicitly leaves global energy propagation open.
No universal physical multiplier-five law or sufficient global arithmetic
upper bound is obtained there.

## Publication consequence

The frozen proofs and their hash-pinned reviews here are unchanged. The
new comparison adds attribution and preserves the relevant distinctions:
unshifted support versus shifted cores, conditional exact components versus
constructed approximate invariants, and partial return/carry rules versus
universal physical closure. It does not promote any claim in the accepted
baseline or claim full Collatz resolution.

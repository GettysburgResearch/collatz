# Independent review of the full ordinary-source projection

23 November 2026. Reviewer: `witness_construction`, independent of the
transport author. This review reconstructs the mathematics and inspects
the formal source and exact checker. It does not extend to any later
unlisted source hash.

## Frozen boundary and verdict

The retained parent is PR177, full commit
`3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`. The new files reviewed are:

| File under `research/lean-exact-witness-global-20261121/construction-attacks-20261123/transport/` | SHA256 |
|---|---|
| `FULL_SOURCE_FINITE_CERTIFICATE.md` | `380d70b3618ed5ffe2992b20ed6eb66d30fe325479bc8db9e82f7f3db0ffd58d` |
| `UnitProjection.lean` | `bd404caded2fb5f1d1c0ebf673d4d0c6208727a989d11fb8031e39a82ddbd1b4` |
| `check_unit_projection.py` | `32e96d5905c8896d074d19872d4f0f67010ff64a6ef61fd6dd0dacea7f73e52b` |

**VERIFIED** at the stated scope: FP1--FP7 and FP11--FP14, the six formal
declarations, and the checker coverage described below.

**VERIFIED WITH FIXES** for FP8--FP9 at the corrected hash above. The
initial manuscript hash
`a0caa6cd06cc274256f05b7049abcbed1f14d890c871bfa41c37091a91af705b`
omitted a literal nonempty-source hypothesis in Section 3. The reviewer
reported it, and the author applied it before this review was finalized.
The corrected source explicitly requires **nonempty finite** `G`, states
that `H` and `F` are nonempty and their masses positive, and requires
`N >= 1` in FP9. FP7 correctly continues to allow the empty set. The
normalized trial and logarithmic certificate are now stated on exactly
their valid domain, consistent with the parent CF7 hypothesis. This
verdict does not extend those normalized formulas to the empty set.

FP10 is accurately identified as **OPEN**. This review supplies no
construction of the required moving-target populations, no escape
exclusion, and no proof of the residue-512 implication or full Collatz.

## Reconstruction of the actual projection

Write each positive ordinary source uniquely as `n = 2^a m` with `m`
odd. If `m` is a ternary unit, strip the `a` initial halving steps. If
`3 | m`, take the complete next odd acceleration
`3m + 1 = 2^e u`, where `u` is odd and `e >= 1`. Reduction modulo three
shows `3` does not divide `u`. No abstract congruence-compatible word is
substituted for this actual path.

For FP2, the unit-odd endpoint cannot occur among the initial even
states, at an odd multiple of three, or among the even intermediate
states before `u`. Consequently the supplied finite hitting path must
contain the whole projection prefix. Removing that prefix retains the
identical ordinary endpoint. This also supplies the ordinary realization
needed before invoking the inverse-tree bijection in FP8.

For FP3, the unit case has `u = m <= n`. In the nonunit case, `m >= 3`
and `2u <= 3m + 1`. Thus `3u <= (9m + 3)/2 <= 5m <= 5n`.
The actual edge `3 -> 5` attains equality. The constant and the need to
allow a height increase are both correct.

## Exact fibers and the inverse-power certificate

The order of two modulo nine is six. Checking its six powers gives the
claimed table `1,2,4,5,7,8 -> 6,5,4,1,2,3`. Therefore an odd multiple
of three whose odd successor is the fixed unit `u` has exponent exactly
`e0(u) + 6b`, `b >= 0`; conversely each such exponent gives a positive
odd multiple of three. Since `u` is odd, its displayed exponent is the
exact valuation, not merely a lower bound.

Uniqueness of the odd part makes the dyadic unit family disjoint from
the dyadic nonunit family and fixes `a`. Within the nonunit family, the
exact valuation fixes `b`. This proves all of FP5, including the absence
of omitted collisions. The identity
`m_b = 64^b*m_0 + (64^b - 1)/3` and the height estimate give
`m_b >= 64^b*(3u/5)`. Summing these upper bounds on inverse powers gives
FP6 for every real `s > 0`. Both geometric sums converge. At `s = 2`,
the constant is exactly `111404/22113 < 6`.

Grouping a finite source sum by the actual disjoint fibers and then
deduplicating their images proves FP7. This genuinely controls weighted
multiplicity; an unweighted uniform fiber-size assertion would be false.
For nonempty `G`, the image and its inverse under `Phi` are nonempty
finite sets. Write `W = sum_(u in pi(G)) u^(-s)`. The parent explicit
trial bound is `F_q(sigma_F) <= K - log W`, with
`K = log(s/(s-1)) - s*log(64*c_*)`. Since
`W >= C_s^(-1) sum_(n in G) n^(-s) > 0`, monotonicity of the logarithm
gives exactly FP8. Distinct sources bounded above by `X` have inverse
power sum at least `N*X^(-s)`, yielding FP9 with the stated nonempty
correction. All constants have the correct signs.

The relative-scale count discussion also preserves its quantifiers:
when `gamma < s`, the guaranteed quantity
`c*v^(-gamma)*X^(gamma-s)` is largest at the smallest allowed `X`.
This evaluates that proposed lower bound; it does not upper-bound the
actual population or assert an external theorem with uniform constants.

## Pressure and Green comparison

For a nonunit odd fiber member, the exact edge weight relative to `u`
is `3/2^(e0+6b)`. The independent dyadic factor is `2^(-a)`.
Summing their `s`-powers yields precisely FP11. Taking the largest and
smallest of the six possible `e0` gives FP12 without replacing the
ordinary residue distribution by a uniform law.

FP2 and its immediate converse show that the full shortcut basin is
exactly the union of the complete fibers over its unit-odd basin.
Hence nonnegative summation proves FP13. For an escaping component and
`s > 1`, the parent unit mass is finite, so the comparison also proves
finiteness of the full mass.

At a nonperiodic root each ordinary ancestor has a unique hitting
depth. Along an even shortcut edge the weight ratio is `1/2`; along an
odd shortcut edge it is `3/2`. Telescoping gives the complete shortcut
Green identity `A_s^T(v) = r(v)^s Z_s^T(v)`. The same `r(v)` appears in
the unit Green identity. Applying the two-sided FP13 bound separately
at `Sq` and `q` and cancelling these root weights gives FP14. The
nonperiodicity hypothesis is essential to the no-duplicate-depth
identity and is present in the manuscript. No row normalization or
change of component occurs.

## Formal and computational evidence

I inspected the complete `UnitProjection.lean`. The proof removes actual
halving prefixes using parity, excludes a zero-length nonunit-to-unit
path by divisibility, and composes the remaining actual iterates. Its
height proof matches the integer inequality above. The finite mass
consumer correctly assumes a quantitative fiber bound and proves the
finite grouping step; it does not claim that the countable real-power
bound was formalized. The six `#print axioms` declarations correspond to
these scoped statements.

I inspected the complete exact checker. Its predecessor pools use the
actual two inverse shortcut possibilities and retain literal finite
paths. The fiber rectangles check both disjoint source families, exact
valuations, and the two geometric factors with rational arithmetic.
Its five failed-strengthening controls exercise distinct omitted-cost
errors. Explicit `require` checks survive Python `-O`.

The producer's strict Lean and normal/optimized Python execution receipts
were inspected and matched byte-for-byte to their saved outputs. The
strict Lean log has SHA256
`bfe04bf63b5434c9ed174cc20b10a23eaa8e885a25c9e9534e81e5879c25735c`;
both Python logs have SHA256
`5578e5b6df0b015bcbb2ba147009b0227705f6121dec784009ecf0a5f3dd6a0c`.
The six audits have only `propext`, `Classical.choice`, and `Quot.sound`
in their union, with no `sorryAx` or custom axiom. These are **producer
executions inspected by the reviewer**, not a fresh independent compiler
run by this reviewer. The normal and optimized executions were repeated
by the author after the manuscript correction; the strict Lean receipt
is retained for its unchanged formal source. The mathematical reconstruction above is
independent of those execution reports.

The relevant parent dependency sections were also reconstructed:

| Parent source | Reviewed scope | SHA256 |
|---|---|---|
| `profound-step-20261123/COMMON_DISPLACEMENT_AND_FREE_ENERGY.md` | CF5--CF9, including the explicit finite trial | `867cca98da500a7b1be5c24e9185ac877b56c508be2a7da12436e9f3b0046abb` |
| `repo-synthesis-20261123/escape/BASIN_PRESSURE_PACKING.md` | BP1--BP3 and the stated root-summability consumer | `257443f6c0800ab42e9f08c79c1daebc4d97c894833add6941b46389778349d2` |

Those parent formulas are treated as scoped dependencies; this review
does not claim a new independent audit of all their earlier inputs.

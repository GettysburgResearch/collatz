# Independent ordinary-source review of the general phase return

23 November 2026. Reviewer: `ordinary_selector8`.

**Verdict: VERIFIED for R10-P1--P5 as stated.** This is an independent
mathematical and execution supplement to `GENERAL_PHASE_REVIEW.md` by
`density_free_germ8`, which is preserved unchanged. A paid-return result
preserves a proposed equality. It does not accept that equality or prove
termination after repeatedly applying the transformer.

## Binding and fresh execution

Published parent: `c369ae3c426ec6aaf9a280ec9578b9910c2147d5`.
Reviewed paths are in `research/carry-tower-round10-20261123/`.

| File | Git blob |
| --- | --- |
| `GENERAL_PHASE_RETURN.md` | `df7c79ffabdd628b36db2b0e7478c35fe57c80d2` |
| `general_phase_controls.py` | `945bacbd3da14a894872eca517d6e37e491160df` |
| `GeneralPhaseReturn.lean` | `e728e06ecc19228fc9dd4d37aac3cb3e3bedb2d3` |

I independently ran the normal script, its optimized Python execution,
and two consecutive imported calls to `run_checks()`. All four results
were equal, with **16,541 exact checks**. The SHA256 of the normal script's
JSON stdout, including its final newline, was
`31d22a0fecd0303134184b8744a893fde6f76811c6aea56675919f3874f0b94e`.

Strict compilation succeeded with Lean 4.34.1 and Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`, using
`lake env lean -DwarningAsError=true -DautoImplicit=false -j1` at default
heartbeats. I read all fourteen theorem declarations. They formalize
finite guard, envelope, iteration, and high-run budget statements; the
note correctly leaves the real scalar and full ordinary departure
attachment to its written proof and pinned parent input.

## Independent reconstruction

For a canonical phase `p>1/2`, the necessary guard
`3(p+k)<=B+3` gives the integer inequality `3k<=B+1`. If k is positive,
then `k<=B-1`, including the smallest possible bit lengths. This and
the literal ordinary lower bound `q>=2^(B-1)` establish `q/2^k>=1`.
Thus this rank lower bound applies to a guarded finite candidate;
it does not assume the candidate's infinite equality.

The ordinary equation and candidate equation together give

`Y' = 3Y/2^(b+2k) + 1/2^(b+3k)`.

For positive carry, the complete expression is bounded by
`H(Y)=3Y/8+1/16`, and `Y>=1` gives `H(Y)<=7Y/16`. At a low-to-high
entry the canonical charge is two or three, and the exact normalized
entry is `(3x+1)/2^b`. Iterating the increasing affine map H about its
fixed point `1/10` gives the stated two paid envelopes, uniformly in
the intervening carries and length. The comparison source is the last
low state x, not the earlier supplied source q.

I independently reconstructed the binary departure proof using the
canonical rational fixed point `-C/D`. Both C and D are odd, and every
cyclic shift of the fixed point is an odd rational with the prescribed
binary valuation. If `T=v2(|Dq+C|)`, the perturbation after i canonical
transitions has valuation `T-A_i`. Comparing it with the next canonical
term distinguishes the strict interior case from cancellation at an
interval endpoint. The latter produces a scalar candidate at most
one half, even when the next phase is exactly `3/2`. In the interior
case, the entry carry is exactly `b_i-(T-A_i)` and is one or two.
This proves the gate from actual source arithmetic, without selecting
convenient gaps.

The endpoint and budget details are consistent. The first paid entry
occurs after `n+1<=T` steps. The next guarded high stage needs at most
`bl(s)-k` steps; `bl(s)<=B_0+n+1` and k is positive. The stated
`B_0+2T` budget is therefore conservative. For the height-only bound,
`|Dq+C|<2^(max(bl|D|+B_0,bl C)+1)` gives exactly the integer valuation
bound used in the note. If `Dq+C=0`, the separate literal cycle check
is sound; periodic scalar recurrence gives its candidate phase.

Backward substitution on any returned actual prefix yields
`h(q)-p_0 = 3^(-N)(h(r)-p_N)` even for a false initial candidate.
Neither guard success nor a returned source is an acceptance test for
the infinite equality.

For the denominator-1456 example I recomputed the canonical clock,
affine constants, and internal clock residues. The six forced initial
one-gaps imply `2^7 | q+1`, which is the needed source-height input
for the bound `3 bl(q)+26`. For `W^m V`, the full affine composition
has the displayed constant kappa. Its slope crosses one between
m=101 and m=102. The valuation `19m+7` provides the required whole-class
source lower bound for m>=2, while m=0 and m=1 are handled separately.
Thus the stated threshold concerns the complete literal W/V family.
The first paid low return occurs at `12m+8`; completing the remaining
four canonical transitions is an explicit choice for that family,
not a generic same-phase normalization of arbitrary returns.

## Separate finite departure checks

In addition to replaying the owner's controls, I independently formed
the canonical cycles and their affine constants from exact rational
arithmetic for all reduced canonical phases with denominator at most
36 and coprime to three. For each of the 290 phases, I used all 64
positive odd sources below 128. The shadow clocks, actual gap replay,
and first-departure cases were reconstructed independently before
comparison with the supplied transformer.

The run passed **93,987 checks** on **18,560 phase/source cases**:

| Boundary checked | Count |
| --- | ---: |
| Canonical phases with positive D | 9 |
| Canonical phases with negative D | 281 |
| Endpoint-cancellation gates | 7,647 |
| Interior-clock entry gates | 10,912 |
| Verified ordinary paid-return outputs | 224 |
| Soundly bounded rejection outputs | 18,335 |
| Literal canonical-cycle outputs | 1 |

For each return I separately checked its source budget, exact zero-run
length and entry carry, full affine envelope, and transported endpoint
candidate. A boundary fixture used phase `3/2` and q=13: the actual
gaps begin `(3,4)`, and `v2(-5q+1)=6` is the endpoint-cancellation
case with candidate exactly `1/2` at departure. These finite checks
support the implementation and boundary conventions; the universal
claims are the written arguments above.

## Cross-packet boundary

The general-phase first low endpoint can have a different phase.
The denominator-eight tower result uses its separately proved
normalization to a `7/8` boundary. These two endpoint conventions
must remain distinct. Neither argument selects a pressure maximum,
and neither moves a maximum through a phase change or ternary
denominator clearing.

The finite expanding towers in `RETURN_TOWER.md` have their actual
scalar strictly below `7/8`. They obstruct specified valuation-only
corrections to two candidate potentials, but they do not realize
exact denominator-eight rationality. Likewise the W/V cylinders
here have valid finite candidate phases without an asserted exact
infinite attachment. Increasing the prescribed cylinder length
changes its constructed ordinary source.

The unresolved fixed-source question is whether successive returns
can repeatedly offset their high-carry contraction by canonical
expansion and changes of phase. The total one-return transformer,
its source-height budget, and the exact W/V threshold preserve that
question rather than silently assuming its answer.

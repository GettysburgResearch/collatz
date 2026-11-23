# Independent reconstruction of the appended-word arithmetic and controls

Reviewer: the target-entry research agent, independently of the author of
the extension module and cycle-control script. Date: 23 November 2026.

**Verdict: VERIFIED at the following exact source hashes, within the scope
below.** This is an internal mathematical reconstruction, not external peer
review or a verdict on all surrounding analytic claims.

| File | SHA256 |
|---|---|
| `research/lean-exact-witness-global-20261121/lean/Collatz/NegativeCycleExtension.lean` | `f69070cfc0767d24a1e8305e431574e9aed62b7158b80694b7787df7e3330012` |
| `research/lean-exact-witness-global-20261121/atomic_cycle_controls.py` | `0a3de3f1d20d65cfa712916ad9966f069ba96ae669715a7096b34ba06f245fbb` |

## Three formal statements

For a literal front word F with length h, total A and correction C, append
L ones and a final gap e. Reconstructing the affine composition gives

`r=h+L+1`, `total=A+L+e`,

`C_extended + 2^(A+L+1) = 3^(L+1)*(C+2^A)`.

This is exactly `extension_data`. No word-length or exponent bound is
introduced. It is a data identity; on its own it does not assert physical
legality or positivity of every gap.

For `2^(A+L+e)+D=3^r` and a supplied actual prefix from n to an odd u,
the whole-word difference is

`C_extended+D*n = 2^A*3^(L+1)*(u+1)
                 -2^(A+L+1)-2^(A+L+e)*n`.

Every term on the right is divisible by `2^(A+1)` when e is positive.
The Lean proof keeps this as a natural-number identity before applying
divisibility cancellation. This verifies `extension_binary_guard`; no
subtraction in natural numbers is silently treated as signed subtraction.

Modulo `3^K`, when `K<=L+1`, the full numerator and denominator satisfy

`2^e*C_extended = 2*D mod 3^K`.

This is `extension_ternary_guard`. For the negative rational point
`-C_extended/D`, the unit-denominator interpretation gives the claimed
phase `-2^(1-e)`. The Lean statement itself is the cleared congruence;
it does not formalize rational division, primitive-root enumeration,
density, or CRT realization. Its natural D equation concerns the negative
cycle construction; the positive-sign construction remains written.

## Exact Python construction

The script retains `2^total-3^length` as the complete signed denominator
and replays every rational rotation using exact fractions. Positivity or
negativity is checked at every rotated state, as are unit membership and
the exact two-adic gap. The positive rational cycles are not asserted to
be integer cycles.

For the ordinary CRT paths, initial agreement through
`2^(total+precision+1)` pays the entire binary word and its terminal
precision. The endpoint difference from the rational root is multiplied
by `3^length/2^total`, which preserves the required terminal binary
congruence and increases ternary precision. These are positive ordinary
finite paths returning to a product cylinder, not ordinary periodic orbits.

The separate bridge construction chooses its initial binary residue from
the **full** affine equation for the requested terminal binary cylinder.
The retained original front forces the source binary cylinder. A long
one-gap block followed by e fixes the target ternary phase; CRT then
imposes the independent source ternary phase. Exact gap replay and all
four endpoint congruences are checked. No infinite orbit is extracted
from these varying finite realizations.

## Executed review checks

The reviewer separately compiled `NegativeCycleExtension.lean` with Lean
4.34.1 and `-DwarningAsError=true`: exit zero, no diagnostics. Existing
dependency objects were reused. The dedicated axiom audit is recorded
by the coordinating execution receipt rather than claimed as another
execution here.

The reviewer ran the exact Python script both normally and with `-O`.
The outputs were byte-identical, SHA256
`9d834d870fda7b248ce2244eee50346fa8c92864c3b969e688e0c1b6316e4599`.
They cover **24 rational cycles, 265 rotations, 72 ordinary CRT paths,
and 12 ordinary bridges**. All guards remain active under optimization.

The general density, cylinder routing, continuous-profile classification,
and global Riesz argument are written mathematics. These three Lean
declarations and finite executions do not by themselves formalize or
verify those entire analytic arguments, nor do they exclude positive
integer escape or nontrivial positive integer cycles.

# A collision-free route to pointwise pressure decay

**PROPOSED. F(t)->0 remains unproved.** Separate continuation of PR143
`41a408e5e617fb4e65142485f6f3ff3e6ef6c408`, which already contains PR140's
pass 4. No earlier proof, status registry, workflow, setting, license, or
main-branch file is changed.

Start with [DISSIPATION.md](DISSIPATION.md), L1--L5, for the direct arithmetic
loss inequality, then [PROOF.md](PROOF.md), D1--D6, and
[TRACE.md](TRACE.md), T1--T5.

## What changes

There is also a new UNCONDITIONAL direct energy--moment inequality:

    (E_q-E_(q+1))^2 D_q >= (441/16384) E_q^5.

It uses only the positive ordinary +1 loss, Holder's inequality and the
reciprocal-square source envelope. It does not require orbit packing or
killing cycles. Consequently

    E_Q <= [E_0^(-3/2)+(63/256)sum_(q<Q)D_q^(-1/2)]^(-2/3).

Divergence of that reciprocal-moment sum would force F(t)->0. Its divergence
is OPEN. A quadratic upper bound for D_q would suffice, with logarithmic
energy decay from this route and a stronger rate using the packing input
below. This direct inequality is not a proof of the missing upper bound.

The prior target was the quadratic collision moment S_q. It is sufficient
to control the smaller, collision-free quantity

    D_q=sum_(x positive odd) J_q(x)^4/U^q(x)^2.

Indeed S_q >= (17/15)D_q for q>=1, and equality holds at q=1. No reverse
comparison is asserted. A new finite-time coercivity inequality connects
D_q to ALL surviving source weight, not merely to a selected hypothetical
counterexample. For repeat-killed energy Ebar_Q and the explicit packing
input K=16,beta=19/20,

    Ebar_Q^3 <= [4*(59/19)*16^(40/19)]
                 *Q^(-59/19)*sum_(j<Q)D_j.

Thus a quadratic diagonal bound would give the quantitative decay
Ebar_Q=O(Q^(-2/57)) and force F(t)->0. The diagonal bound is OPEN; the
unconditional operator estimate remains exponential. This is not a proof
that the displayed energy actually tends to zero.

The full positive-integer D_q, E_q and S_q are also enclosed at finite clocks
using exact periodic ternary tables and rational reciprocal-square tails.
Both density powers are reconstructed through clock 12, including every
positive odd source. These are not finite-source lower approximations.
A separate prefix experiment retains incomplete trajectories and checks
the new energy inequality on finite source families.

## Replay

From the repository root:

```sh
python -B experiments/pressure-diagonal-20261031/run.py --depth 12 --output /tmp/diagonal.json
python -OO -B experiments/pressure-diagonal-20261031/run.py --depth 12 --output /tmp/diagonal-oo.json
python -B experiments/pressure-diagonal-20261031/verify.py /tmp/diagonal.json --output /tmp/diagonal-verify.json
python -OO -B experiments/pressure-diagonal-20261031/verify.py /tmp/diagonal-oo.json --output /tmp/diagonal-verify-oo.json
python -B experiments/pressure-diagonal-20261031/dissipation.py /tmp/diagonal.json --output /tmp/diagonal-loss.json
python -OO -B experiments/pressure-diagonal-20261031/dissipation.py /tmp/diagonal.json --output /tmp/diagonal-loss-oo.json
```

Python standard library only. The producer uses a 96-bit truncated-series
interval method; the verifier uses 128-bit full-cycle interval sweeps and
literal shortcut replay, with no producer imports. The complete 23,359-byte
output is regenerated; its hash and the actual execution boundaries are in
[receipt.json](../../reports/pressure-diagonal-20261031/receipt.json).
The [review](../../reports/pressure-diagonal-20261031/REVIEW.md) records what
was checked, what was not, the prior attachment, and remaining obligations.

## Exact remaining task

Prove a genuinely all-clock upper bound such as D_q=O(q^2), the weaker
Cesaro liminf condition D5(13), or the divergence condition L4(7). The finite tables, uniform interval averages,
and approximate operator eigenvectors do not imply it. Even proving this
would give eventual periodicity; excluding nontrivial positive cycles is
still a separate obligation.

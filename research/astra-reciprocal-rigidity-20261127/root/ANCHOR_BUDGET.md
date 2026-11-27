# Finite ordinary anchors that pay for all future merger clocks

**PROPOSED; the stated finite implication has a Lean kernel proof.** This
packet concerns the physical shortcut map `T(x)=x/2` for even `x` and
`T(x)=(3x+1)/2` for odd `x`. It establishes a resource barrier for a specified
infinite family. It does not establish universal convergence.

## A fully instantiated all-time theorem

Let `K≥84`, `s∈{0,1}`, `n>s`, and `3^K | n−s`. Suppose that the first `j`
shortcut departures from `n` are odd; equivalently `2^j | n+1`. If any
positive integer `m<n` reaches the same endpoint as this `j`-step ramp,
at any finite native clock `e`, then

\[
                 Q_e(m)>K+j+12.
\]

There is no restriction on `e`, the lower path's maximum height, or its
number of even steps. The source `n` is fixed throughout each assertion.
The theorem is not a statement about an inverse path selected in advance.
It excludes every smaller positive merging partner below this odd budget.

The exact Lean declaration is
[`CertifiedRamp.twelve_extra_odds`](CertifiedRamp.lean). It uses
[`RampShadow.prepaid_ramp`](../descent/PrepaidRamp.lean) with `b=12`, `L=22`.
Its finite input is checked in
[`AnchorCertificate.all_prefixes_648`](AnchorCertificate.lean), and its
extension beyond the checked trajectory is proved by
[`AnchorBudget.budgetCheck_sound`](AnchorBudget.lean). These declarations
print only `propext`, `Classical.choice`, and `Quot.sound` as proof axioms.
The final replay report records the actual compiler, imports, file hashes,
and executed commands; those receipts do not replace the mathematical
scope stated here.

### Why a finite calculation can cover arbitrary time

For a source `q`, define the native prefix excess

\[
       L(q)=\sup_{r\ge0}\bigl(2Q_r(q)-r\bigr).
\]

On the positive trivial cycle `1→2→1`, the excess changes by `+1,−1`.
Once a checked trajectory reaches 1, its entire future excess is therefore
known. The Boolean checker follows a supplied number of actual steps,
subtracting `+1` at odd departures and `−1` at even departures from a
reserve. It accepts only if every reserve is nonnegative and the remaining
reserve at 1 is at least one. A structural induction on the checker and
the physical path proves the all-time claim. Python supplies candidate
clocks; the kernel evaluates each finite assertion itself.

The certificate checks every positive integer through 648, and shows
`L(q)≤22` for all of them. This includes every source required by the
prepaid-ramp theorem, since `2^12 q<4·3^12` implies `q≤518`.
The exact threshold inequality is

\[
  3^{73}2^{23}3^{12}\le4^{73}2^{12},\qquad 73=84+1-12.
\]

Multiplying by powers of `3≤4` proves it at every larger precision.
No numerical extrapolation of observed trajectories occurs in this step.

The conjunction of all source checks is deliberately built from separate
kernel reductions. A single large recursive reduction consumed excessive
memory in the initial implementation. Splitting the proof changes neither
the proposition nor the trusted computing base.

## An exact budget curve beyond the kernel example

The standard-library program [prefix_budget.py](prefix_budget.py) computes
the finite input required at any requested `b≤36`. Its retained run stops
at `b=34` and at ordinary source 3,882,958. Odd acceleration is used to
memoize prefix maxima, with

\[
 L(1)=1,\qquad L(q)=\max\{1,2-a+L(U(q))\},
 \quad U(q)=(3q+1)/2^a\quad(q>1\text{ odd}).
\]

Initial even steps cannot raise the maximum beyond that of the smaller odd
source. Every extremizing source is also replayed with literal native
steps, independently of the accelerated recurrence. Every row includes
the exact integer power comparison and its first supported `K`.

| Extra odd budget `b` | Finite prefix bound `L` | One source attaining `L` | Every precision `K≥` |
|---:|---:|---:|---:|
| 1 | 2 | 3 | 9 |
| 4 | 4 | 15 | 21 |
| 5 | 21 | 27 | 65 |
| 10 | 21 | 27 | 77 |
| 12 | 22 | 327 | 84 |
| 20 | 37 | 13,255 | 139 |
| 25 | 47 | 77,031 | 175 |
| 30 | 68 | 626,331 | 238 |
| 34 | 80 | 3,732,423 | 277 |

The complete finite data are in
[PREFIX_BUDGET_CONTROLS.json](PREFIX_BUDGET_CONTROLS.json). The rows beyond
the explicit Lean example are exact Python computations consumed by the
written general theorem; they are not represented as kernel-rebuilt
million-source calculations.

## A different budget: visits to the anchor 1

The least native price `e_K` for an actual path with `K` odd departures
ending at 1 is treated in the [descent packet](../descent/README.md).
For a source reaching 1, let `p(q),t(q)` be its odd and native clocks at
the first arrival. Every later arrival has the same defect
`2p(q)−t(q)`, because a lap of the trivial cycle adds one odd and two
native steps. The same defect identity also compares earlier and later
supplied visits without assuming either is the first.

`AnchorBudget.visit_defect` and `budget_of_witness` kernel-check this
identity. They are useful for the least-price budget

\[
 b_K=\min\{b\ge0:2^{e_K+b}<3^{K+b}\}.
\]

If `b_K≤b`, a minimizing origin has
`q≤2^{e_K}/3^K<(3/2)^b`. If all such finite sources are checked and their
visit defects are at most `D`, then `e_K≥2K−D`. Therefore the exact
comparison `2^{2K−D+b}≥3^{K+b}` excludes `b_K≤b`. Once this comparison
holds it holds for every larger `K`. The proof does not infer that a
finite convergence ceiling grows with `K`.

The [anchor program](anchor_budget.py) and its
[retained data](ANCHOR_BUDGET_CONTROLS.json) give these separate bounds:
`b_K>12` for all `K≥46`, `b_K>20` for `K≥79`, and `b_K>34` for `K≥195`.
These are bounds for direct inverse ancestry at the original source;
they do not replace the larger prepaid-ramp thresholds above.

### A necessary distinction at source 27

The first arrival from 27 at 1 takes 70 native steps and 41 odd departures,
so its arrival defect is 12. Its largest prefix excess is **21**, already
at native clock 45. Replacing the prefix bound by the arrival defect would
underpay the intermediate path and invalidate the prepaid argument.
The two data files therefore retain different quantities and separate
consumers.

## Reproduction and remaining obligation

From this directory:

```bash
python -B make_anchor_certificate.py --check
python -B prefix_budget.py --check PREFIX_BUDGET_CONTROLS.json
python -B anchor_budget.py --check ANCHOR_BUDGET_CONTROLS.json
```

The Python guards remain active under `-O`. The complete packet's Lean
replay builds the local dependency chain in a fresh output directory.

Every fixed `b` uses a finite, concretely checkable source set. As proved
separately in `descent/PrefixMeaning.lean`, assuming these bounded-excess
oracles for **all** `b` is equivalent to universal positive convergence.
The present finite certificates cannot be promoted to that unbounded
premise. The global remaining task is to produce a smaller physical
merging partner for every residual source after its initial ramp, at the
resource cost that the unconditional barriers require.

# Unbounded ordinary queries and a wider least-defect exclusion

**Collatz remains OPEN.** This continuation proves an unbounded family of ordinary smaller queries, removes a residue restriction after an exact height threshold, and rescues a preassigned large checkpoint with an earlier Mersenne exponent outside the previous comparison grid. The new final Lean proposal attaches these exclusions to the original least reverse defect. Its remaining universal exclusion is explicitly unproved.

The starting checkpoint is PR197 at `10d87fee615d1095990d6b7ea329126b4cf7aa5a`. All trajectories below use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

Write C(x) for the ordinary orbit reaching 1. A reverse defect is an ordinary z with z≡17 modulo 48, C(3z), and not C(z). The existing reduction says that ruling out these defects proves Collatz. Its quantitative return turns any positive bad x into a reverse defect at most 2^40 x. Every use below retains the actual supplied integer and its finite physical word.

## 1. Arbitrarily deep paired queries with arbitrarily large savings

For the family

\[
j=11+162m,\qquad81z+271=128\cdot2^j,\qquad T^7z=2^j-1,
\]

the new construction proves that for every lap count n there are cofinally many actual m and positive w≡17 modulo 48 with

\[
w<z,\qquad T^{18+11n}w=2^j-1,\qquad T^{20+11n}(3w)=2^{j-2}.
\]

The lower and upper words have exactly 12+7n and 11+7n odd inputs. Thus any least reverse defect at one of these parents would produce a strictly smaller reverse defect. Moreover, for **every** prescribed factor F and lower parameter bound L, Lean proves the existence of m≥L and an actual query with Fw<z and both physical meetings. The depth and parameter are chosen after F; the theorem does not choose a successful depth for each already supplied arbitrary m.

The mechanism repeats the eleven-step negative cycle at phases −17 and −55. They arise simultaneously from the rational center −2399/81 after seven steps. Conjugating the older center −2692031/3^12 by this cycle gives centers of reduced denominator 3^(12+7n), with contraction 2048/2187 per lap. The final proof works directly with integral source and target equations; it does not assume that intermediate rational charts are ordinary comparison inputs.

For each depth, the narrow query class is exactly one progression for m modulo 3^(8+7n). The first new class is

\[
m\equiv534563\pmod{14348907}\qquad(n=1).
\]

All positive depths lie within m≡3122 modulo 19683, outside the seventeen previously covered residues. Different depths give disjoint classes. This is an infinite extension of the finite bank, with a specified remaining complement. The uniqueness and residue descriptions are written arithmetic; the cofinal witnesses, physical paths, counts, arbitrary savings and least-defect exclusion are Lean theorems. [Proof and class calculation](RATIONAL_CENTER_PUMP.md) · [RationalCenterPump.lean](RationalCenterPump.lean).

## 2. A stronger closure after 405 laps

At every n≥405, **any integral query satisfying the same physical start and target equations** is small enough for quantitative return:

\[
2^{40}w<z.
\]

There is no ternary residue requirement on w. If the parent z were bad, its ordinary lower merger would make w bad. Quantitative return at this w then produces a reverse defect y≤2^40w<z. This excludes the original least parent even when w itself is not a reverse defect.

The exact threshold uses

\[
2^{40}\,2048^{n+1}\le6561\,2187^n.
\]

Lean checks that this coefficient test fails at 404 and holds at 405, propagates it to all later n, and retains the additive terms needed for strict inequality. The coarser comparison would require 423 laps. The threshold 405 is sharp for this height argument on whole cofinal families; that last sharpness interpretation is written.

The admissible m progression widens from period 3^(8+7n) to period 3^(7+7n). One physical period shift changes w modulo 3 by a fixed nonzero digit. Three consecutive shifts give all three digits, adding two complete ordinary parameter classes at every n≥405. The Lean theorem `excluded_progression` proves exclusion for every member of a whole forward progression above any requested bound. [Proof](WIDE_CENTER_PUMP.md) · [WideCenterPump.lean](WideCenterPump.lean).

## 3. A fixed-cofactor rescue beyond the old grid

For every

\[
v=2^{128}(1+27\cdot2^{49}q),\qquad q\ge0,
\]

the actual second raw checkpoint has the physical identity

\[
T^{183}(32\,3^{42v-4}-17)
=T^{42v+21+178}(2^{42v+21}-1).
\]

The exponent 42v+21 lies below the original first bad exponent 66v−5. It is outside the previous grid of 32 even exponents 2vi. The theorem includes the **preassigned cofactor one**, q=0, without choosing a replacement input. Its parameter lies outside the old one-sixteenth, binary-cylinder and ternary rescue rows; exact overlaps for the full new family are checked in Lean.

`FixedCofactorLeastParent.leastExcluded` consumes the original equation 81z+527=1024·2^(66v−5), the actual defect, and global leastness. It derives the earlier-good range from the established quantitative return, transfers convergence through the displayed ordinary meeting, and obtains a contradiction at that same z. No unconditional convergence of all earlier exponents is assumed separately. [Full argument and overlap](ALL_EARLIER_MERSENNE_RESCUE.md) · [Physical identity](FixedCofactorRescue.lean) · [Original-parent consumer](FixedCofactorLeastParent.lean).

The same lane replaces the 32-exponent test by a written exact criterion over **all earlier peak exponents** in its stated clock window. Lean proves the formal carry realization and recognition rules for every finite clock. The main power separation in the all-exponent equivalence is a written proof. The criterion decides a supplied carry; it does not guarantee success for every source. [AllMersenneCarries.lean](AllMersenneCarries.lean).

## 4. Necessary denominator and tower clocks

The denominator result now handles arbitrary extra lower odd steps. At m=3^k t, a normalized shrinking lower-phase meeting must have denominator exponent d≥k+5. No upper-phase word is needed, and no comparison-clock bound is imposed. This removes the previous extra-odd alternative and shows that every bounded-denominator bank of this specified kind misses arbitrarily large parameters. A written fixed-center argument explains why one contracting periodic chart cannot accumulate at the ternary parameter address zero. It leaves changing centers and different comparisons open. [AllDepthCenter.lean](AllDepthCenter.lean).

For a positive z coprime to 6, a meeting

\[
T^i(3^rz)=T^j(3^sw),\qquad0<w<z,\qquad i,j\le H
\]

must satisfy 3^(r+P_i)<6^H, where P_i is the actual source odd count. At equal clocks it requires r+P_i<i. Applied to PR206's supplied 660-grade endpoint, a block beginning at rank m≥721 cannot give the smaller-base comparison at the same 1381 clocks; at m≥1592 no comparator clock up to 1381 works. The application retains the explicit upstream grade premise.

On the known convergent base 17, for every odd H≥17 and every rank cutoff there is a later adjacent tower edge whose **first asynchronous meeting deadline is exactly H+5**. Every earlier independent pair of clocks is excluded. This is a constructive ordinary example showing that long finite disjointness alone cannot imply a basin change at the original source. [Detailed proofs and upstream scope](FIXED_TOWER.md) · [Lower-cone theorem](TowerLowerCone.lean) · [Exact delayed merger](DelayedTowerMerger.lean).

## Final Lean proposal and replay

[UnboundedQueryProposal.lean](UnboundedQueryProposal.lean) extends the previous survivor record with the narrow pump, widened pump and fixed-cofactor exclusions. It proves

```lean
collatz_from_remaining (remaining : RemainingExclusion) : UniversalConvergence
collatz_iff_remaining : UniversalConvergence ↔ RemainingExclusion
```

`RemainingExclusion` is **OPEN**. It excludes every surviving actual least defect with no upper-rank, original-hit-clock or rational-denominator bound. The proposition is a stated mathematical obligation, not an additional axiom or an established result. A complete proof must supply a successful query or sufficient ordinary descent for each remaining source, or close another universal route such as the actual Fourier overshoot estimate.

The replay uses Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. From that built Mathlib environment:

```sh
lake env bash /path/to/research/ayh-resource-reset-20261124/unbounded-queries/check_lean.sh
python -B /path/to/research/ayh-resource-reset-20261124/unbounded-queries/check_rational_pump.py
python -B /path/to/research/ayh-resource-reset-20261124/unbounded-queries/check_all_earlier.py
python -B /path/to/research/ayh-resource-reset-20261124/unbounded-queries/check_fixed_tower.py
```

The Lean script rebuilds the entire local closure chain into fresh temporary storage. The Python programs also support `-O`. Exact execution receipts, independent cross-reviews, source comparisons and the combined declaration audit are in [the report](../../../reports/ayh-resource-reset-20261124/unbounded-queries/README.md). The full scientific claims remain separate from finite replays and repository integrity checks.

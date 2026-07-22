# Cross-repository sweep — 2026-07-22

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Purpose:** identify live results that can actually alter the ordinary-section or period-four proof strategy

All external claim IDs below retain their native branch status. This file does
not promote or import another branch's theorem as proved.

## 1. PR #33 — general cylinder blocks and finite traps

PR #33 (`gpt56-cylinder-01`) independently proves a general odd-affine cylinder
recurrence. Its new block formula is the abstract version of `T-9409`:

```text
finite directive -> one residue cylinder,
ordinary nonnegative completion <=> eventual zero of new blocks.
```

Its `T-9701` adds a useful nonstabilization theorem when every integral local map
is uniformly contracting in an archimedean height and the resulting finite trap
contains no legal transition.

### Relevance here

The exact stack transition of `L-9406` is

```text
x'=81^(9m+1)y+k_(m,n)
```

on the unused quotient. The odd multiplier is supercritical, and the equivalent
centered stage multiplier is not uniformly below one along a growing `17/18`
height schedule. Therefore the raw finite-trap theorem does not transfer.

The reusable lesson is structural: a successful completion proof needs either

```text
- a different height with uniform contraction;
- a finite impossible trap for a renormalized state;
- or a divisibility-vs-height squeeze on the new block recurrence.
```

This supports the period-four determinant program but does not itself close it.

## 2. PR #16 — carry rigidity and the fixed-room ordinary section

PR #16 independently reaches the same criticality constant

```text
kappa=1/(log_64(81)-1)=17.654847...
```

through integral reciprocal-phase carries. Long zero-carry runs create completion
agreement whose divisibility outruns the allowed height. The same branch now
supplies:

- all-depth weighted EQ in its Fourier program;
- a centered rational-power equivalence for ordinary `64 -> 81` survivors;
- an exact depth-46 nontrivial survivor minimum exceeding `2^227`.

### Relevance here

This independently confirms that the load-bearing mechanism in `T-9401`,
`L-9405`, and the Padé program is completion height rather than word complexity
alone. It also shows that an ordinary stack context, if it existed, would have to
survive a large fixed-room lower bound.

The finite lower bound does not change the asymptotic rationality threshold of a
Padé approximant: the target integer contributes only an additive constant to
`log height`. The carry theorem likewise controls long zero-carry runs but does
not supply the phase-coupled period-four cancellation missing from `L-9410`.

The strongest bridge is therefore a **coupled completion-height numerator**:
construct an integer from several phase errors or adjacent Padé orders whose
`2`-adic divisibility gains quadratically while its global height grows below the
period-four deficit.

## 3. PR #3 — ordinary quadratic bulk generator

PR #3 now has a forward ordinary sequence

```text
V_m=(3^(7*2^m)-1)/2^(m+2),
V_(m+1)=V_m+2^(m+1)V_m^2,
```

which generates every finite prefix of its inverse `2`-adic connector bulk and
has a positive bit-length surplus over the first connector demand.

### Relevance here

This is the most concrete construction-side resource in the repository: an
ordinary finite word manufactures new bits forward rather than reading a
preloaded inverse-limit tape. But the PR's own gap audit leaves exact residual
Montgomery-cylinder membership open.

For this branch, the useful question is whether a phase-coupled Padé determinant
or active-cylinder block can be expressed as a low-height affine/polynomial
function of such an ordinary generator. No such embedding is currently proved.
Bit surplus alone is not congruence routing.

## 4. Issue #21 — diagonal foundry collapse

The foundry program proves that strictly causal feedback selects one `2`-adic
completion. Its later tail-autonomy result shows that if the solution is an
ordinary integer, finite digit support kills the feedback and leaves one
open-loop tail.

### Relevance here

This validates the focus on tail classes. Finite-state feedback does not create a
secret escape from the periodic/S-adic value problem for ordinary integers. The
first genuinely new foundry frontier is again one-counter or pushdown autonomous
tails—the same class represented by this branch's stack directive.

## 5. Literature wave 3 — q-series theorems

The periodic stack value is exactly a finite vector of Tschakaloff-type phases.
Rochev's 2011 q-series theorem is the closest broad p-adic linear-independence
result located in the sweep.

`R-9405` records the decisive failed hypothesis: in the natural orientation

```text
q=(81/64)^(9S|W|),
```

both the `2`-adic and archimedean absolute values exceed one. Rochev's p-adic
proof is organized around one expanding place and nonexpansion at the others.
The theorem therefore cannot be quoted as a black box for the stack phase vector.

This failure explains why the native Padé exponent has to budget powers of both
`64` and `81` explicitly.

## 6. New result from the sweep

The most immediate proposed period-four repair was to reallocate the
Gaussian-binomial roots unequally among phases. `L-9411` constructs the entire
allocation family; `T-9416` proves equal allocation uniquely maximizes its
universal pre-reduction exponent. Thus

```text
period four remains <=0.993714361875...<1
```

throughout that class.

This is not merely negative. It sharply removes a large design space and proves
that the next mechanism must be genuinely coupled.

## 7. Consolidated next target

The surviving high-value routes are now:

1. **Adjacent-order Casoratian:** cancel a growing number of first surviving
   combined phase coefficients, not merely one fixed coefficient.
2. **Phase-sensitive Hermite–Padé:** use the actual transfer polynomial `P_W`
   rather than only the phase count.
3. **Reduced-height theorem:** prove a quadratic common factor after exact
   integer clearing; bounded gcd data are insufficient.
4. **Completion-height determinant:** combine PR #16's carry viewpoint with
   several Padé errors to build one nonzero ordinary numerator whose divisibility
   outruns its height.
5. **Construction dual:** embed the residual cylinder in PR #3's forward
   quadratic ordinary generator and replay it independently.

The period-four deficit is small, but `T-9416` proves that asymmetry alone cannot
recover it. The next contribution must create new cancellation or new arithmetic
height savings.
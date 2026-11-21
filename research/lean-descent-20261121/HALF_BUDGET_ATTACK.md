# Direct fixed-source attack: a linear odd-step budget

Status: the exact accounting, descent theorem, and implication to full Collatz are checked in Lean 4.34.1. The universal budget itself is OPEN. This is a direct all-integer attempt; no density or almost-everywhere conclusion is substituted for a pointwise claim.

## Exact route

Use the shortcut Collatz map T(n)=n/2 for even n and (3n+1)/2 for odd n. For a fixed ordinary source n, the Lean structure `Account` records the current value x, the multiplier A, denominator D, affine debt B, and odd count p. Initially these are `(n,1,1,0,0)`. An even step changes D to 2D. An odd step changes `(A,D,B,p)` to `(3A,2D,3B+D,p+1)`. In both cases x takes its actual ordinary step.

Lean proves, for every clock:

- D x = A n + B;
- D = 2^t and A = 3^p;
- x>0 for n>0.

Before the first clock at which D>2A, every prior D is at most 2A. The debt estimate

    3B ≤ 2pA

is an exact induction. At an odd step, multiply the old debt bound by three and use 3D≤6A for the new additive term. An even step preserves the bound.

Suppose the first half-crossing satisfies 2p≤3n. Then 3B≤3An, hence B≤An. If x≥n, the affine identity gives Dn≤An+B≤2An, contradicting D>2A and n>0. Therefore x<n.

`HalfBudget` is the universal assertion that for each n>1 such a first half-crossing occurs with 2p≤3n. The theorem `collatz_of_half_budget` uses strong induction on the original positive integer n: the crossing produces a smaller positive ordinary value, its basin certificate is supplied by induction, and ordinary steps propagate that certificate back to n. This argument excludes cycles and divergent orbits together; it assumes neither separate exclusion.

The parameter `H : HalfBudget` remains visible in the Lean theorem type. There is no Lean declaration claiming to prove it.

## The attempted completion

A finite parity word of length t has one source class modulo 2^t. Let r be its least positive representative and p its number of odd letters. The target combinatorial inequality is:

    If every coefficient prefix is at least one half, then r=1 or 3r≥2p.

Every other positive source lift of the same word already satisfies the required bound. When another parity bit is appended, the canonical source either stays fixed or receives the new binary place. The branch receiving that place is automatically large enough for the linear inequality. The unresolved branch is the one keeping r fixed. Its unbounded continuation is exactly the trajectory of that one ordinary integer, so a proof must establish why it cannot retain the coefficient inequality past the odd budget. Counting the whole prefix tree does not establish this.

The word 11100 has the positive rational cycle starting at 19/5. Its first half-crossing occurs at t=25 with p=15, violating the proposed odd budget for that rational source. Thus a proof using only real/rational inequalities, without ordinary integrality, cannot establish the budget. This repeated word supplies legal finite ordinary source classes at every depth, but it does not remain above the half threshold past t=24. Separately, the all-ones code does remain above the half threshold at every depth: its 2-adic completion is the negative fixed point −1, and its least positive ordinary source at depth t is 2^t−1. A proof must exclude stabilization at every positive ordinary root n>1; finite compatibility or a real debt estimate alone does not do so.

## Discovery calculation

An exact integer scan of n=2,...,199999 found a first half-crossing within the stated odd budget for every scanned input. The largest observed p/n was 40/27 at n=27. Its first half-crossing occurs at t=65, has p=40, and reaches x=10. The exact accounting is

    A = 12157665459056928801
    D = 36893488147419103232
    B = 40677914079653954693.

This finite scan motivated the candidate universal inequality. It is not evidence that every ordinary source satisfies it beyond the scanned range, nor a substitute for its proof. In particular, `HalfBudget` is stronger quantitative information than the bare Collatz assertion; no converse is claimed.

## Factor variants

The same argument at the first crossing D>K A gives 3B≤KpA. Actual descent follows whenever

    3n + Kp ≤ 3Kn.

Thus K=3 allows p≤2n. These variants can trade a later coefficient threshold for a larger odd-step budget; no universal bound for a variant is proved here.

## Sources and formal evidence

The imported dependency is PR174, commit 7034109ed60a26bc49824e1ed43c239ceca81194, `research/psi-closure-20261121/lean/Collatz/Closure.lean` and its exact `ReverseBasin146.lean` dependency. The new file is `Collatz/HalfCrossing.lean`.

Executed successfully:

    lake env lean -DwarningAsError=true Collatz/HalfCrossing.lean
    lake env lean -o .lake/build/lib/lean/Collatz/HalfCrossing.olean Collatz/HalfCrossing.lean
    lake env lean -DwarningAsError=true Audit.lean

The audit reports only `propext`, `Classical.choice`, and `Quot.sound` for `run_identity`, `run_debt`, `half_crossing_descent`, and `collatz_of_half_budget`. There is no `sorryAx` in those declarations. Axioms of the kernel foundation do not discharge the explicit parameter `H : HalfBudget`.

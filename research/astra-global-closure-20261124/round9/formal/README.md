# Final Lean proposal and its exact open obligation

**The explicit progression is proved. The universal cover is not proved.**
[FinalProposal.lean](FinalProposal.lean) uses the ordinary shortcut map on
natural numbers. Its three upstream dependencies are pinned in
[the vendor ledger](../vendor/SOURCES.json). The
[runner](../check_lean.py) rebuilds them and the five new modules from source.

Let Good(n) mean that some ordinary forward iterate of n equals 1.
PR192's LeastDiscordance(q) chooses the least positive odd integer for
which Good(q) differs from Good(3q). A failure of positive Collatz produces
such a q. At that witness q is good, 3q is bad, and these safe sets are proved:

* every positive z with 8z+1 < 9q;
* every positive multiple of three z < 3q.

ReturnCertificate(q) supplies a positive source in either set and actual
clocks at which it meets 3q. The theorem certificate_refutes transports
membership in the basin across that equality and contradicts minimality.
An inverse path is not accepted merely because its affine expression is integral.

## An unconditional certificate on an ordinary progression

For every natural number \(u\), put
\[
\begin{aligned}
q&=163815229+1377495072u,\\
s&=245722843+2066242608u,\\
z&=383076351+3221225472u.
\end{aligned}
\]
The compiled construction progressionCertificate(u) proves
\[
0<z<3q,\qquad 3\mid z,\qquad T^{30}z=T^4s=T^5(3q).
\]
The first meeting comes from the actual 26-step inverse progression
CriticalCycle.small_multiple(1+16u). The second is the ordinary identity
\(T^4(16m+11)=T^5(32m+23)\), at \(m=15357677+129140163u\).
Thus the formal conclusion is

~~~lean
theorem progression_excluded (u : Nat) :
    ¬LeastDiscordance (163815229 + 1377495072 * u)
~~~

This theorem has no cycle, strip, analytic floor, density, or assumed
termination hypothesis. It excludes these numbers as the **least odd
tripling disagreement**; it does not assert their convergence without
minimality. The comparison with selected earlier sufficient progressions
is recorded in the [independent review](../../../../reports/astra-global-closure-20261124/round9/critical/PROGRESSION_REVIEW.md).
That comparison is not a global novelty claim.

## What would finish the proposal

The open statement is

~~~lean
def CompleteReturnCover : Prop :=
  ∀ q, LeastDiscordance q → Nonempty (ReturnCertificate q)
~~~

The file checks the two exact types

~~~lean
collatz_of_complete_return_cover
  (cover : CompleteReturnCover) : OrdinaryCollatz

complete_return_cover_iff_collatz :
  CompleteReturnCover ↔ OrdinaryCollatz
~~~

The equivalence is deliberately explicit: the universal cover is as strong
as the desired conjecture. Naming it does not settle its outstanding
direction. A complete solution would have to provide an actual term of
CompleteReturnCover, or another unconditional proof of OrdinaryCollatz.
The packet supplies neither. No axiom or sorry is introduced for it, and
the displayed conditional theorem is not counted as a proof of Collatz.

## Verification scope

The source was compiled with Lean 4.34.1, warnings as errors, and a fresh
project output cache. Its eight selected axiom reports contain only
propext, Classical.choice and Quot.sound, or no axioms.
The [complete build receipt](../../../../reports/astra-global-closure-20261124/round9/lean/receipt.json)
binds every source and output hash. Existing Mathlib and package objects
were reused. The full geometric cycle theorem, ballot reflection count,
Evertse theorem, and asymptotic deductions remain written mathematics
with the narrower Lean lemmas documented in their own packets.

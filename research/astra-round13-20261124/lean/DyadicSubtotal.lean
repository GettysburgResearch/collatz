prelude
import Init.Data.Nat.Div.Basic
import Init.Data.Nat.Lemmas

/-! Exact integer recurrence for the finite dyadic-tail subtotal.
No native or external decision procedure is invoked. -/
namespace Collatz.DyadicSubtotal

structure Row where
  shell : Nat
  clock : Nat
  dyadic : Nat
  ternary : Nat
  upperTail : Nat
  boundary : Nat
  total : Nat

/-- At shell n, upperTail counts Bin(n-1,1/2) outcomes with at least clock
successes; boundary is choose(n-1,clock-1). total uses denominator 2^(n-1). -/
def next (r : Row) : Row := Id.run do
  let n := r.shell + 1
  let up := 3 * r.ternary ≤ 2 * r.dyadic
  let right := r.boundary * (r.shell - r.clock) / r.clock
  let tail := if up then 2 * r.upperTail - right else 2 * r.upperTail + r.boundary
  let edge := if up then r.boundary + right
              else r.boundary * r.shell / (r.shell - r.clock + 1)
  return { shell := n, clock := if up then r.clock + 1 else r.clock,
           dyadic := 2*r.dyadic, ternary := if up then 3*r.ternary else r.ternary,
           upperTail := tail, boundary := edge,
           total := 2*r.total + (if n ≥ 69 then tail else 0) }

def row : Nat → Row
  | 0 => ⟨4, 1, 4, 3, 7, 1, 0⟩
  | i+1 => next (row i)

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
theorem finite_subtotal :
    (row 507).shell = 511 ∧ 1000000 * (row 507).total < 335142 * 3 * 2 ^ 510 := by
  decide +kernel

theorem geometric_remainder :
    8 * 390625^64 * 497664 * 1000000 <
      9 * (497664 - 390625) * 497664^64 := by
  decide +kernel

#print axioms finite_subtotal
#print axioms geometric_remainder
end Collatz.DyadicSubtotal

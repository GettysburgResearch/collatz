import Mathlib.Tactic.Ring

/-! Two directed source exchanges for every ordinary invariant label. -/
namespace UnitResidueExchange

variable {α : Type*} (f : ℕ → α)
variable (he : ∀ n, f (2*n) = f n) (ho : ∀ n, f (2*n+1) = f (3*n+2))

include he in
private theorem ev (a b t : ℕ) : f ((2*a)*t+2*b) = f (a*t+b) := by
  convert he (a*t+b) using 1
  congr 1
  ring

include ho in
private theorem od (a b t : ℕ) : f ((2*a)*t+(2*b+1)) = f ((3*a)*t+(3*b+2)) := by
  convert ho (a*t+b) using 1 <;> congr 1 <;> ring

include he ho

/-- The class-1 ternary unit moves upward with both labels in order. -/
theorem unit_one_exchange (t : ℕ) :
    f (64*t+1) = f (48*t+1) ∧
    f (192*t+3) = f (144*t+3) := by
  constructor
  · calc
      f (64*t+1) = f (96*t+2) := od f ho 32 0 t
      _ = f (48*t+1) := ev f he 48 1 t
  · calc
      f (192*t+3) = f (288*t+5) := od f ho 96 1 t
      _ = f (432*t+8) := od f ho 144 2 t
      _ = f (216*t+4) := ev f he 216 4 t
      _ = f (108*t+2) := ev f he 108 2 t
      _ = f (54*t+1) := ev f he 54 1 t
      _ = f (81*t+2) := od f ho 27 0 t
      _ = f (162*t+4) := (ev f he 81 2 t).symm
      _ = f (324*t+8) := (ev f he 162 4 t).symm
      _ = f (216*t+5) := (od f ho 108 2 t).symm
      _ = f (144*t+3) := (od f ho 72 1 t).symm

/-- Every 17 mod 48 input has an ordered-label representative at 11 mod 32. -/
theorem residue17_descends (t : ℕ) :
    f (32*t+11) = f (48*t+17) ∧
    f (96*t+33) = f (144*t+51) := by
  constructor
  · exact od f ho 16 5 t
  · calc
      f (96*t+33) = f (144*t+50) := od f ho 48 16 t
      _ = f (72*t+25) := ev f he 72 25 t
      _ = f (108*t+38) := od f ho 36 12 t
      _ = f (54*t+19) := ev f he 54 19 t
      _ = f (81*t+29) := od f ho 27 9 t
      _ = f (162*t+58) := (ev f he 81 29 t).symm
      _ = f (324*t+116) := (ev f he 162 58 t).symm
      _ = f (216*t+77) := (od f ho 108 38 t).symm
      _ = f (144*t+51) := (od f ho 72 25 t).symm

#print axioms unit_one_exchange
#print axioms residue17_descends

end UnitResidueExchange

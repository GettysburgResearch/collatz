import MersenneCrests

/-!
The consecutive shifted-core equation comes from an actual finite shortcut
orbit. The binary divisor hypothesis permits any initial segment of the
halving run, including the complete run down to its odd part.
-/
namespace Collatz.ShiftedRampCores

open Collatz.MersenneCrests

theorem halving_run (f u q : Nat) : run (2^f*u,q) f = (u,q) := by
  induction f generalizing u with
  | zero => simp [run]
  | succ f ih =>
    change next (run (2^(f+1)*u,q) f) = (u,q)
    rw [Nat.pow_succ, Nat.mul_assoc, ih]
    simp [next]

theorem shifted_crest (x s h b q : Nat) (hb : 0 < b)
    (hx : x+1 = 2^s*(3^h*b)) :
    run (x,q) s = (3^(s+h)*b-1,q+s) := by
  have hx' : x = 2^s*(3^h*b)-1 := by omega
  rw [hx']
  simpa only [Nat.pow_add, Nat.mul_assoc] using
    initial_ramp s q (3^h*b) (Nat.mul_pos (Nat.pow_pos (by decide)) hb)

/-- The supplied factorization of the actual crest determines the observed
    endpoint and the exact number of odd departures through its return. -/
theorem crest_return (x s h b f u q : Nat) (hb : 0 < b)
    (hx : x+1 = 2^s*(3^h*b)) (hc : 3^(s+h)*b-1 = 2^f*u) :
    run (x,q) (s+f) = (u,q+s) := by
  rw [run_add, shifted_crest x s h b q hb hx, hc, halving_run]

/-- The shifted equation uses the next factorization of the actual endpoint.
    Taking the full binary valuation in the divisor hypothesis gives two
    consecutive odd ramps. No endpoint or clock is replaced by a model. -/
theorem adjacent_shifted_identity (x s h b f t k c q : Nat) (hb : 0 < b)
    (hx : x+1 = 2^s*(3^h*b)) (hdiv : 2^f ∣ 3^(s+h)*b-1)
    (hnext : (run (x,q) (s+f)).1+1 = 2^t*(3^k*c)) :
    3^(s+h)*b + 2^f - 1 = 2^(f+t)*(3^k*c) := by
  obtain ⟨u, hu⟩ := hdiv
  rw [crest_return x s h b f u q hb hx hu] at hnext
  change u+1 = 2^t*(3^k*c) at hnext
  have hpos : 0 < 3^(s+h)*b := Nat.mul_pos (Nat.pow_pos (by decide)) hb
  have hpow : 0 < (2:Nat)^f := Nat.pow_pos (by decide)
  calc
    _ = 2^f*(u+1) := by rw [Nat.mul_add, Nat.mul_one]; omega
    _ = _ := by rw [hnext, Nat.pow_add, Nat.mul_assoc]

end Collatz.ShiftedRampCores

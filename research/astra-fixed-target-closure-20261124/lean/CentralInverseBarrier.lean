import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
An exact obstruction to obtaining a smaller source from central inverse words.
No probabilistic or external analytic result is an axiom or hypothesis here.
The lower endpoint 3 excludes the fixed odd point 1. The note explains why
every positive odd inverse path to an odd target greater than 1 has this guard.
-/

namespace Collatz.CentralInverseBarrier

/-- A literal outward inverse word, with its odd depth and total valuation.
The equation and oddness force each positive gap to be its exact valuation
when the previous endpoint is odd. The inequality below is valid even without
requiring oddness of the initial target. -/
inductive GapWord (q : ℕ) : ℕ → ℕ → ℕ → Prop
  | nil (hq : 3 ≤ q) : GapWord q q 0 0
  | extend {x y b s e : ℕ} (previous : GapWord q x b s)
      (he : 1 ≤ e) (hy : y % 2 = 1)
      (equation : 2^e * x = 3*y+1) :
      GapWord q y (b+1) (s+e)

theorem inverse_at_least_three (x y e : ℕ)
    (hx : 3 ≤ x) (he : 1 ≤ e) (hy : y % 2 = 1)
    (h : 2^e*x = 3*y+1) : 3 ≤ y := by
  have hp : 2 ≤ 2^e := by
    simpa using (Nat.pow_le_pow_right (by decide : 0 < 2) he)
  have hsix : 6 ≤ 2^e*x := by nlinarith
  omega

theorem inverse_step_bound (x y e : ℕ)
    (hy : 3 ≤ y) (h : 2^e*x = 3*y+1) :
    3*2^e*x ≤ 10*y := by
  nlinarith

theorem word_bound {q y b s : ℕ} (w : GapWord q y b s) :
    3 ≤ y ∧ 3^b*2^s*q ≤ 10^b*y := by
  induction w with
  | nil hq => simp_all
  | @extend x y b s e previous he hy equation ih =>
    have hyt : 3 ≤ y := inverse_at_least_three x y e ih.1 he hy equation
    refine ⟨hyt, ?_⟩
    have hstep : 3*2^e*x ≤ 10*y := inverse_step_bound x y e hyt equation
    calc
      3^(b+1)*2^(s+e)*q = (3*2^e)*(3^b*2^s*q) := by
        rw [pow_succ, pow_add]
        ring
      _ ≤ (3*2^e)*(10^b*x) := Nat.mul_le_mul_left _ ih.2
      _ = 10^b*(3*2^e*x) := by ring
      _ ≤ 10^b*(10*y) := Nat.mul_le_mul_left _ hstep
      _ = 10^(b+1)*y := by rw [pow_succ]; ring

theorem central_product (b s : ℕ) (hb : 0 < b) (hs : 7*b ≤ 4*s) :
    10^b < 3^b*2^s := by
  have hfour : (10^b)^4 < (3^b*2^s)^4 := by
    calc
      (10^b)^4 = (10000 : ℕ)^b := by
        rw [← pow_mul, Nat.mul_comm b 4, pow_mul]
        norm_num
      _ < (10368 : ℕ)^b := Nat.pow_lt_pow_left (by decide) (by omega)
      _ = ((3 : ℕ)^4*2^7)^b := by norm_num
      _ = 3^(b*4)*2^(b*7) := by
        rw [mul_pow, ← pow_mul, ← pow_mul]
        simp only [Nat.mul_comm]
      _ ≤ 3^(b*4)*2^(s*4) := Nat.mul_le_mul_left _
        (Nat.pow_le_pow_right (by decide) (by omega))
      _ = (3^b*2^s)^4 := by rw [mul_pow, ← pow_mul, ← pow_mul]
  by_contra h
  have hle : 3^b*2^s ≤ 10^b := by omega
  have := Nat.pow_le_pow_left hle 4
  omega

theorem central_word_expands {q y b s : ℕ} (w : GapWord q y b s)
    (hq : 0 < q) (hb : 0 < b) (hs : 7*b ≤ 4*s) : q < y := by
  have hw := (word_bound w).2
  have hp := Nat.mul_lt_mul_of_pos_right (central_product b s hb hs) hq
  by_contra h
  have hyq : y ≤ q := by omega
  have hle := Nat.mul_le_mul_left (10^b) hyq
  omega

/-- The usual lower half of the central square-root window implies 4s≥7b
as soon as b≥16. Natural subtraction also permits any supercentral total. -/
theorem central_window_budget (b s : ℕ) (hb : 16 ≤ b)
    (hs : (2*b-s)^2 ≤ b) : 7*b ≤ 4*s := by
  have hsmall : 4*(2*b-s) ≤ b := by
    by_contra hn
    have ht : 4 ≤ 2*b-s := by omega
    nlinarith
  omega

theorem no_central_descent {q y b s : ℕ} (w : GapWord q y b s)
    (hq : 0 < q) (hb : 16 ≤ b) (hs : (2*b-s)^2 ≤ b) : q < y := by
  exact central_word_expands w hq (by omega) (central_window_budget b s hb hs)

end Collatz.CentralInverseBarrier

#print axioms Collatz.CentralInverseBarrier.inverse_at_least_three
#print axioms Collatz.CentralInverseBarrier.inverse_step_bound
#print axioms Collatz.CentralInverseBarrier.word_bound
#print axioms Collatz.CentralInverseBarrier.central_product
#print axioms Collatz.CentralInverseBarrier.central_word_expands
#print axioms Collatz.CentralInverseBarrier.central_window_budget
#print axioms Collatz.CentralInverseBarrier.no_central_descent

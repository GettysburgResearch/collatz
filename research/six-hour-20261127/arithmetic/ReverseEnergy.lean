import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.ReverseEnergy

/-- A zero signed numerator with a common future binary factor has an integral
normalized carry at the cut. The power of three is removed exactly. -/
theorem integral_cut {a L : ℕ} {acc suffix : ℤ}
    (zero : 3^a * acc + 2^L * suffix = 0) :
    ∃ z : ℤ, acc = -(2^L * z) := by
  have cop : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have h : (2 : ℤ)^L ∣ 3^a * acc := by
    refine ⟨-suffix, ?_⟩
    linarith
  obtain ⟨q, hq⟩ := cop.pow.dvd_of_dvd_mul_left h
  exact ⟨-q, by rw [hq]; ring⟩

/-- The raw ordinary recurrence, normalized at consecutive binary floors. -/
theorem reverse_step {L advance : ℕ} {P Q z w delta : ℤ}
    (hp : P = -(2^L*z)) (hq : Q = -(2^(L+advance)*w))
    (step : Q = 3*P+2^L*delta) :
    3*z = 2^advance*w+delta := by
  have hn : (2 : ℤ)^L ≠ 0 := by positivity
  apply mul_left_cancel₀ hn
  rw [hp, hq, pow_add] at step
  linear_combination step

/-- In a two-row slice, every true zero outgoing carry forces the signed
digit and preceding carry to vanish. -/
theorem two_rows {z d : ℤ} (h : 3*z = d) (lo : -2 ≤ d) (hi : d ≤ 2) :
    z = 0 ∧ d = 0 := by omega

/-- The hidden next trit belongs to the incoming carry itself. A decoder can
hold it fixed across all predecessors before taking its envelope. -/
theorem next_trit {z r T : ℤ} (h : T ∣ z-r) :
    ∃ t l : ℤ, 0 ≤ t ∧ t < 3 ∧ z = r+T*(t+3*l) := by
  obtain ⟨q, hq⟩ := h
  have split : q % 3 + 3*(q/3) = q := by omega
  exact ⟨q%3, q/3, by omega, by omega, by rw [split]; omega⟩

#print axioms integral_cut
#print axioms reverse_step
#print axioms two_rows
#print axioms next_trit

end Collatz.ReverseEnergy

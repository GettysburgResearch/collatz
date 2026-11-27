import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite ordinary height cutoffs and the all-odd excursion. -/
namespace Collatz.ReciprocalRigidity.FiniteTrace

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3*x+1)/2

/-- `orbit j n` is the state after `j` physical shortcut steps. -/
def orbit : ℕ → ℕ → ℕ
  | 0, n => n
  | j+1, n => orbit j (step n)

def reachesOneBelow (H n : ℕ) : Prop :=
  ∃ j, orbit j n = 1 ∧ ∀ i ≤ j, orbit i n ≤ H

private theorem odd_step {u : ℕ} (hu : 0 < u) :
    step (2*u-1) = 3*u-1 := by
  unfold step
  have hp : (2*u-1) % 2 = 1 := by omega
  simp only [hp, Nat.one_ne_zero, ite_false]
  omega

theorem odd_run (j h u : ℕ) (hu : 0 < u) :
    orbit j (2^(j+h)*u-1) + 1 = 3^j * 2^h * u := by
  induction j generalizing u with
  | zero =>
    simp only [Nat.zero_add, orbit, pow_zero, one_mul]
    have hp : 0 < 2^h * u := Nat.mul_pos (by positivity) hu
    omega
  | succ j ih =>
    have hp : 0 < 2^(j+h)*u := Nat.mul_pos (by positivity) hu
    have he : 2^(j+1+h)*u = 2*(2^(j+h)*u) := by
      rw [show j+1+h = (j+h)+1 by omega, pow_succ]; ring
    rw [he, orbit, odd_step hp, show 3*(2^(j+h)*u) = 2^(j+h)*(3*u) by ring]
    rw [ih (3*u) (by omega), pow_succ]; ring

theorem odd_run_prefix (k i : ℕ) (hi : i ≤ k) :
    orbit i (2^k-1) + 1 = 3^i * 2^(k-i) := by
  have h := odd_run i (k-i) 1 (by decide)
  simpa [Nat.add_sub_of_le hi] using h

theorem cutoff_obstruction {k H : ℕ} (hk : 2 ≤ k) (hH : H < 3^k-1) :
    ¬reachesOneBelow H (2^k-1) := by
  rintro ⟨j, hhit, hbound⟩
  by_cases hj : k ≤ j
  · have h := hbound k hj
    have he := odd_run_prefix k k (le_refl _)
    simp only [Nat.sub_self, pow_zero, mul_one] at he
    omega
  · have hji : j ≤ k := by omega
    have he := odd_run_prefix k j hji
    rw [hhit] at he
    have hpow : 2^k ≤ 3^j * 2^(k-j) := by
      calc
        2^k = 2^j * 2^(k-j) := by rw [← pow_add, Nat.add_sub_of_le hji]
        _ ≤ _ := Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide : 2 ≤ 3) j)
    have hl : 2^2 ≤ 2^k := Nat.pow_le_pow_right (by decide) hk
    omega

theorem finite_prefix_nonzero {k N H : ℕ} {a : ℕ → ℚ}
    (hk : 2 ≤ k) (hn : 2^k-1 ≤ N) (hNH : N ≤ H) (hH : H < 3^k-1)
    (hsupport : ∀ n, 0 < n → n ≤ H → (a n = 0 ↔ reachesOneBelow H n)) :
    ∃ n ≤ N, a n ≠ 0 := by
  refine ⟨2^k-1, hn, fun hz => cutoff_obstruction hk hH ?_⟩
  have hpow : 2^2 ≤ 2^k := Nat.pow_le_pow_right (by decide) hk
  exact (hsupport _ (by omega) (hn.trans hNH)).mp hz

end Collatz.ReciprocalRigidity.FiniteTrace

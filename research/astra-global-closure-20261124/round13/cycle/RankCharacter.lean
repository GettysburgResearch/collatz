import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace RankCharacter

/-- Short centered representatives turn this congruence into an equality. -/
theorem centered_step (g x y : ℤ) (b : ℕ) (hb : b = 1 ∨ b = 2)
    (hx : -g < 8*x ∧ 8*x < g) (hy : -g < 8*y ∧ 8*y < g)
    (cong : g ∣ 3*y-2^b*x) : 3*y = 2^b*x := by
  obtain ⟨k, hk⟩ := cong
  have bounds : -g < 3*y-2^b*x ∧ 3*y-2^b*x < g := by
    rcases hb with h | h <;> rw [h] <;> norm_num <;> omega
  have hg : 0 < g := by omega
  by_cases hp : 0 < k
  · have := Int.mul_le_mul_of_nonneg_left (show 1 ≤ k by omega) (le_of_lt hg)
    omega
  by_cases hn : k < 0
  · have := Int.mul_le_mul_of_nonneg_left (show k ≤ -1 by omega) (le_of_lt hg)
    omega
  have : k = 0 := by omega
  rw [this, mul_zero] at hk
  omega

def height (b : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => height b n + b n

theorem telescope (x : ℕ → ℤ) (b : ℕ → ℕ) (n : ℕ)
    (edges : ∀ i < n, 3*x (i+1) = 2^(b i)*x i) :
    3^n*x n = 2^(height b n)*x 0 := by
  induction n with
  | zero => simp [height]
  | succ n ih =>
    have first := ih (fun i hi => edges i (by omega))
    have last := edges n (by omega)
    calc
      3^(n+1)*x (n+1) = 3^n*(3*x (n+1)) := by rw [pow_succ]; ring
      _ = 2^(b n)*(3^n*x n) := by rw [last]; ring
      _ = 2^(height b (n+1))*x 0 := by rw [first, height, pow_add]; ring

/-- Every modular frequency whose starting representative is nonzero
and smaller than 3^n develops a macroscopic centered representative. -/
theorem frequency_escape (x : ℕ → ℤ) (b : ℕ → ℕ) (g : ℤ) (n : ℕ)
    (nonzero : x 0 ≠ 0) (initial : (x 0).natAbs < ((3 : ℤ)^n).natAbs)
    (letters : ∀ i < n, b i = 1 ∨ b i = 2)
    (steps : ∀ i < n, g ∣ 3*x (i+1)-2^(b i)*x i) :
    ∃ i ≤ n, 8*x i ≤ -g ∨ g ≤ 8*x i := by
  by_contra! small
  have exacts i (hi : i < n) := centered_step g (x i) (x (i+1)) (b i)
    (letters i hi) (by have := small i (by omega); omega)
    (by have := small (i+1) (by omega); omega) (steps i hi)
  have h := telescope x b n exacts
  have cop : Nat.Coprime (3^n) (2^(height b n)) :=
    ((show Nat.Coprime 3 2 by decide).pow_left n).pow_right _
  have absEq := congrArg Int.natAbs h
  simp only [Int.natAbs_mul, Int.natAbs_pow] at absEq
  have div : 3^n ∣ 2^(height b n)*(x 0).natAbs := ⟨(x n).natAbs, absEq.symm⟩
  have pos : 0 < (x 0).natAbs := Int.natAbs_pos.mpr nonzero
  have le := Nat.le_of_dvd pos (cop.dvd_of_dvd_mul_left div)
  rw [Int.natAbs_pow] at initial
  exact (Nat.not_lt_of_ge le) initial

/-- Two distinct middle bands at any prescribed time, with the very same
neighboring bands, use physical exponents in {1,2} on both edges. -/
theorem local_switch (b c : ℤ) (hb : b = 1 ∨ b = 2) (hc : c = 1 ∨ c = 2) :
    ∃ l r : ℤ, (l = 0 ∨ l = 1) ∧ (r = 0 ∨ r = 1) ∧
      ∀ k : ℤ, (k = 0 ∨ k = 1) →
        (1 ≤ b+l-k ∧ b+l-k ≤ 2) ∧ (1 ≤ c+k-r ∧ c+k-r ≤ 2) := by
  exact ⟨2-b, c-1, by omega, by omega, by intro k hk; omega⟩

/-- A changing legal edge and its reversed reflected copy cannot match at both ends. -/
theorem reflected_edge (b k l k' l' : ℤ)
    (hl : 1 ≤ b+k-l ∧ b+k-l ≤ 2) (hr : 1 ≤ b+l'-k' ∧ b+l'-k' ≤ 2)
    (changed : k ≠ l) : k ≠ k' ∨ l ≠ l' := by omega

/-- On an arc with one sign for all forward increments and the opposite
sign for the reflected ones, a positive coefficient detects its own increment. -/
theorem convolution_rigidity {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (I : Finset ℕ) (j : ℕ) (hj : j ∈ I)
    (A B x y : ℕ → K) (aj : 0 < A j)
    (ha : ∀ i ∈ I, 0 ≤ A i) (hb : ∀ i ∈ I, 0 ≤ B i)
    (hx : ∀ i ∈ I, 0 ≤ x i) (hy : ∀ i ∈ I, y i ≤ 0)
    (he : ∑ i ∈ I, A i*x i = ∑ i ∈ I, B i*y i) : x j = 0 := by
  have pos i (hi : i ∈ I) := mul_nonneg (ha i hi) (hx i hi)
  have neg i (hi : i ∈ I) := mul_nonpos_of_nonneg_of_nonpos (hb i hi) (hy i hi)
  have hzero := le_antisymm (he.le.trans (Finset.sum_nonpos neg)) (Finset.sum_nonneg pos)
  have hjzero := (Finset.sum_eq_zero_iff_of_nonneg pos).mp hzero j hj
  exact (mul_eq_zero.mp hjzero).resolve_left (ne_of_gt aj)

#print axioms convolution_rigidity
#print axioms centered_step
#print axioms telescope
#print axioms frequency_escape
#print axioms local_switch
#print axioms reflected_edge

end RankCharacter

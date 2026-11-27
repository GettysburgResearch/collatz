import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-! The changing-rank integer carry for two genuine shortcut trajectories. -/

namespace Collatz.PairedCapacity

set_option autoImplicit false

def bit (x : ℕ) := x % 2
def step (x : ℕ) := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2
def lowExp (a b : ℕ) := a - (b + 1)
def highExp (a b : ℕ) := b + 1 - a

def carry (a b x y : ℕ) : ℤ :=
  (3 : ℤ) ^ lowExp a b * y - 3 ^ highExp a b * x

def oddCount : ℕ → ℕ → ℕ
  | 0, _ => 0
  | t + 1, x => oddCount t x + bit (step^[t] x)

def rankSize (a b : ℕ) := max (lowExp a b) (highExp a b)

private theorem bit_le (x : ℕ) : bit x ≤ 1 := by unfold bit; omega

private theorem two_step (x : ℕ) : 2 * step x = 3 ^ bit x * x + bit x := by
  have h := bit_le x
  by_cases he : x % 2 = 0
  · simp [bit, step, he]; omega
  · have ho : x % 2 = 1 := by omega
    simp [bit, step, ho]; omega

private theorem step_unit {x : ℕ} (h : x % 3 ≠ 0 ∨ bit x = 1) : step x % 3 ≠ 0 := by
  by_cases he : x % 2 = 0
  · simp [bit, he] at h
    simp [step, he]
    omega
  · have ho : x % 2 = 1 := by omega
    simp [step, ho]
    omega

private theorem orbit_unit {x : ℕ} (h : x % 3 ≠ 0) (t : ℕ) : step^[t] x % 3 ≠ 0 := by
  induction t with
  | zero => exact h
  | succ t ih =>
    rw [Function.iterate_succ_apply']
    exact step_unit (Or.inl ih)

private theorem active_unit (x t : ℕ) (h : 0 < oddCount t x) : step^[t] x % 3 ≠ 0 := by
  induction t with
  | zero => simp [oddCount] at h
  | succ t ih =>
    simp only [oddCount] at h
    rw [Function.iterate_succ_apply']
    apply step_unit
    by_cases hp : 0 < oddCount t x
    · exact Or.inl (ih hp)
    · have hb := bit_le (step^[t] x)
      exact Or.inr (by omega)

private theorem carry_ne_zero (a b x y : ℕ) (hy : y % 3 ≠ 0)
    (hx : 0 < a → x % 3 ≠ 0) (hne : x ≠ y) : carry a b x y ≠ 0 := by
  intro hz
  have heq : 3 ^ lowExp a b * y = 3 ^ highExp a b * x := by
    unfold carry at hz
    exact_mod_cast (sub_eq_zero.mp hz)
  rcases lt_trichotomy a (b + 1) with hl | he | hg
  · have hlo : lowExp a b = 0 := by unfold lowExp; omega
    have hh : 0 < highExp a b := by unfold highExp; omega
    obtain ⟨j, hj⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hh)
    rw [hlo, hj, pow_zero, one_mul, pow_succ] at heq
    have hd : 3 ∣ y := ⟨3 ^ j * x, by rw [heq]; ring⟩
    exact hy (Nat.mod_eq_zero_of_dvd hd)
  · have hlo : lowExp a b = 0 := by unfold lowExp; omega
    have hhi : highExp a b = 0 := by unfold highExp; omega
    simp [hlo, hhi] at heq
    exact hne heq.symm
  · have hhi : highExp a b = 0 := by unfold highExp; omega
    have hl : 0 < lowExp a b := by unfold lowExp; omega
    obtain ⟨j, hj⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hl)
    rw [hhi, hj, pow_zero, one_mul, pow_succ] at heq
    have hd : 3 ∣ x := ⟨3 ^ j * y, by rw [← heq]; ring⟩
    exact hx (by omega) (Nat.mod_eq_zero_of_dvd hd)

/-- A vanishing normalized carry would force a true merger, including if the
lower input starts divisible by three. -/
theorem ordinary_carry_nonzero {Y t : ℕ} (hY : 0 < Y)
    (hne : step^[t] Y ≠ step^[t] (3 * Y - 1)) :
    carry (oddCount t Y) (oddCount t (3 * Y - 1)) (step^[t] Y) (step^[t] (3 * Y - 1)) ≠ 0 := by
  apply carry_ne_zero _ _ _ _ (orbit_unit (by omega) t) (active_unit Y t) hne

private theorem exponent_shift (a b e f : ℕ) (he : e ≤ 1) (hf : f ≤ 1) :
    ∃ j ≤ 1, lowExp (a + e) (b + f) + f = lowExp a b + j ∧
      highExp (a + e) (b + f) + e = highExp a b + j := by
  unfold lowExp highExp
  by_cases h : (a + e - (b + f + 1)) + f = (a - (b + 1))
  · exact ⟨0, by omega, by omega, by omega⟩
  · exact ⟨1, by omega, by omega, by omega⟩

/-- The exact update on actual physical edges. Its multiplier is one or three. -/
theorem carry_update (a b x y : ℕ) :
    ∃ j ≤ 1, 2 * carry (a + bit x) (b + bit y) (step x) (step y) =
      (3 : ℤ)^j * carry a b x y +
        (3^lowExp (a + bit x) (b + bit y) * bit y -
         3^highExp (a + bit x) (b + bit y) * bit x : ℤ) := by
  obtain ⟨j, hj, hlo, hhi⟩ := exponent_shift a b (bit x) (bit y) (bit_le x) (bit_le y)
  refine ⟨j, hj, ?_⟩
  have hqx : 2 * (step x : ℤ) = 3 ^ bit x * x + bit x := by exact_mod_cast two_step x
  have hqy : 2 * (step y : ℤ) = 3 ^ bit y * y + bit y := by exact_mod_cast two_step y
  have hl : (3 : ℤ)^lowExp (a + bit x) (b + bit y) * 3^bit y = 3^lowExp a b * 3^j := by
    rw [← pow_add, ← pow_add, hlo]
  have hh : (3 : ℤ)^highExp (a + bit x) (b + bit y) * 3^bit x = 3^highExp a b * 3^j := by
    rw [← pow_add, ← pow_add, hhi]
  unfold carry
  linear_combination (3 : ℤ)^lowExp (a + bit x) (b + bit y) * hqy -
      (3 : ℤ)^highExp (a + bit x) (b + bit y) * hqx + (y : ℤ) * hl - (x : ℤ) * hh

def cost (a b x y : ℕ) : ℤ :=
  if bit x = 0 ∧ bit y = 0 then 1 else 3 + (3 : ℤ)^rankSize (a + bit x) (b + bit y)

private theorem low_high_bounds (i k e : ℕ) (hi : i ≤ k) (he : e ≤ 1) :
    0 ≤ (3 : ℤ)^i * e ∧ (3 : ℤ)^i * e ≤ 3^k := by
  have hp : 0 ≤ (3 : ℤ)^i := by positivity
  have hmono : (3 : ℤ)^i ≤ 3^k := pow_le_pow_right₀ (by decide) hi
  have hl : (e : ℤ) ≤ 1 := by exact_mod_cast he
  exact ⟨by positivity, le_trans (by simpa using mul_le_mul_of_nonneg_left hl hp) hmono⟩

private theorem cost_pos (a b x y : ℕ) : 0 < cost a b x y := by
  unfold cost
  split <;> positivity

/-- Inactive clocks spend one unit of dyadic valuation; every other clock
has an explicit cost controlled by the post-step relative rank. -/
theorem one_clock_bound (a b x y : ℕ) (hc : carry a b x y ≠ 0) :
    2 * |carry (a + bit x) (b + bit y) (step x) (step y)| ≤
      cost a b x y * |carry a b x y| := by
  by_cases h : bit x = 0 ∧ bit y = 0
  · obtain ⟨hx, hy⟩ := h
    have hqx : 2 * (step x : ℤ) = x := by exact_mod_cast (by simpa [hx] using two_step x)
    have hqy : 2 * (step y : ℤ) = y := by exact_mod_cast (by simpa [hy] using two_step y)
    have hhol : 2 * carry a b (step x) (step y) = carry a b x y := by
      unfold carry
      linear_combination (3 : ℤ)^lowExp a b * hqy - (3 : ℤ)^highExp a b * hqx
    simp only [cost, hx, hy, and_self, ↓reduceIte, Nat.add_zero, one_mul]
    rw [← hhol, abs_mul]
    norm_num
  · obtain ⟨j, hj, hu⟩ := carry_update a b x y
    let A := a + bit x
    let B := b + bit y
    let M := (3 : ℤ)^rankSize A B
    have hM : 0 ≤ M := by unfold M; positivity
    have hlo := low_high_bounds (lowExp A B) (rankSize A B) (bit y) (le_max_left _ _) (bit_le y)
    have hhi := low_high_bounds (highExp A B) (rankSize A B) (bit x) (le_max_right _ _) (bit_le x)
    have hdiff : |(3 : ℤ)^lowExp A B * bit y - 3^highExp A B * bit x| ≤ M := by
      unfold M
      exact abs_le.mpr ⟨by omega, by omega⟩
    have hcoeff : |(3 : ℤ)^j| ≤ 3 := by
      rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hj with rfl | rfl <;> norm_num
    have hunit : 1 ≤ |carry a b x y| := by have := abs_pos.mpr hc; omega
    change 2 * |carry A B (step x) (step y)| ≤ cost a b x y * |carry a b x y|
    calc
      2 * |carry A B (step x) (step y)| = |2 * carry A B (step x) (step y)| := by
        rw [abs_mul]; norm_num
      _ ≤ |(3 : ℤ)^j * carry a b x y| +
          |(3 : ℤ)^lowExp A B * bit y - 3^highExp A B * bit x| := by
        rw [hu]
        exact abs_add_le _ _
      _ ≤ 3 * |carry a b x y| + M := by
        rw [abs_mul]
        exact add_le_add (mul_le_mul_of_nonneg_right hcoeff (abs_nonneg _)) hdiff
      _ ≤ cost a b x y * |carry a b x y| := by
        simp [cost, h]
        change 3 * |carry a b x y| + M ≤ (3 + M) * |carry a b x y|
        nlinarith [mul_nonneg hM (sub_nonneg.mpr hunit)]

def orbitCarry (Y t : ℕ) : ℤ :=
  carry (oddCount t Y) (oddCount t (3 * Y - 1)) (step^[t] Y) (step^[t] (3 * Y - 1))

def orbitCost (Y t : ℕ) : ℤ :=
  cost (oddCount t Y) (oddCount t (3 * Y - 1)) (step^[t] Y) (step^[t] (3 * Y - 1))

private theorem product_with_terminal_carry {Y t : ℕ} (hY : 0 < Y)
    (hne : step^[t] Y ≠ step^[t] (3 * Y - 1)) :
    2^t * |orbitCarry Y t| ≤ ∏ i ∈ Finset.range t, orbitCost Y i := by
  induction t with
  | zero =>
    have hcast : ((3 * Y - 1 : ℕ) : ℤ) = 3 * (Y : ℤ) - 1 := by omega
    simp [orbitCarry, carry, oddCount, lowExp, highExp, hcast]
  | succ t ih =>
    have hp : step^[t] Y ≠ step^[t] (3 * Y - 1) := by
      intro e
      apply hne
      simp only [Function.iterate_succ_apply', e]
    have hu : 2 * |orbitCarry Y (t + 1)| ≤ orbitCost Y t * |orbitCarry Y t| := by
      simpa only [orbitCarry, orbitCost, oddCount, Function.iterate_succ_apply'] using
        one_clock_bound _ _ _ _ (ordinary_carry_nonzero hY hp)
    have hw : 0 ≤ orbitCost Y t := (cost_pos _ _ _ _).le
    rw [Finset.prod_range_succ]
    calc
      2^(t + 1) * |orbitCarry Y (t + 1)| = 2^t * (2 * |orbitCarry Y (t + 1)|) := by ring
      _ ≤ 2^t * (orbitCost Y t * |orbitCarry Y t|) := mul_le_mul_of_nonneg_left hu (by positivity)
      _ = (2^t * |orbitCarry Y t|) * orbitCost Y t := by ring
      _ ≤ _ := mul_le_mul_of_nonneg_right (ih hp) hw

/-- Explicit product bound for every fixed ordinary pair whose two paths
are still distinct at the terminal clock. -/
theorem ordinary_clock_product {Y t : ℕ} (hY : 0 < Y)
    (hne : step^[t] Y ≠ step^[t] (3 * Y - 1)) :
    (2 : ℤ)^t ≤ ∏ i ∈ Finset.range t, orbitCost Y i := by
  have hpos : 0 < |orbitCarry Y t| := abs_pos.mpr (ordinary_carry_nonzero hY hne)
  have hh : (1 : ℤ) ≤ |orbitCarry Y t| := by omega
  exact le_trans (by simpa using mul_le_mul_of_nonneg_left hh (by positivity : 0 ≤ (2 : ℤ)^t))
    (product_with_terminal_carry hY hne)

private theorem rankSize_le {a b P : ℕ} (ha : a ≤ P) (hb : b ≤ P) :
    rankSize a b ≤ P + 1 := by
  unfold rankSize lowExp highExp
  omega

private theorem cost_grade_bound {a b x y P : ℕ} (ha : a + bit x ≤ P) (hb : b + bit y ≤ P) :
    cost a b x y ≤ (3 + (3 : ℤ)^(P + 1))^(bit x + bit y) := by
  by_cases h : bit x = 0 ∧ bit y = 0
  · simp [cost, h.1, h.2]
  · have hpos : 1 ≤ bit x + bit y := by omega
    have hbase : 1 ≤ 3 + (3 : ℤ)^(P+1) := by
      have h : 0 ≤ (3 : ℤ)^(P+1) := by positivity
      omega
    have hd : 3 + (3 : ℤ)^rankSize (a + bit x) (b + bit y) ≤ 3 + (3 : ℤ)^(P+1) := by
      exact add_le_add_right (pow_le_pow_right₀ (by decide) (rankSize_le ha hb)) _
    simp [cost, h]
    exact le_trans hd (by simpa using pow_le_pow_right₀ hbase hpos)

private theorem product_grade_bound (Y t P : ℕ) (ha : oddCount t Y ≤ P)
    (hb : oddCount t (3 * Y - 1) ≤ P) :
    (∏ i ∈ Finset.range t, orbitCost Y i) ≤
      (3 + (3 : ℤ)^(P+1))^(oddCount t Y + oddCount t (3 * Y - 1)) := by
  induction t with
  | zero => simp [oddCount]
  | succ t ih =>
    simp only [oddCount] at ha hb ⊢
    have hp := ih (by omega) (by omega)
    have hs := cost_grade_bound ha hb
    rw [Finset.prod_range_succ]
    calc
      (∏ i ∈ Finset.range t, orbitCost Y i) * orbitCost Y t ≤
          (3 + (3 : ℤ)^(P+1))^(oddCount t Y + oddCount t (3 * Y - 1)) *
          (3 + (3 : ℤ)^(P+1))^(bit (step^[t] Y) + bit (step^[t] (3*Y-1))) :=
        mul_le_mul hp hs (cost_pos _ _ _ _).le (by positivity)
      _ = _ := by rw [← pow_add]; congr 1; omega

/-- A height-independent quadratic clock bound in exponential form. Here the
two odd counts may differ. -/
theorem grade_clock_bound {Y t P : ℕ} (hY : 0 < Y) (ha : oddCount t Y ≤ P)
    (hb : oddCount t (3 * Y - 1) ≤ P) (hne : step^[t] Y ≠ step^[t] (3 * Y - 1)) :
    (2 : ℤ)^t ≤ (3 + (3 : ℤ)^(P+1))^(2*P) := by
  have hbase : 1 ≤ 3 + (3 : ℤ)^(P+1) := by
    have h : 0 ≤ (3 : ℤ)^(P+1) := by positivity
    omega
  exact (ordinary_clock_product hY hne).trans ((product_grade_bound Y t P ha hb).trans
    (pow_le_pow_right₀ hbase (by omega)))

private theorem one_step_inj {x y : ℕ} (hbit : bit x = bit y) (he : step x = step y) : x = y := by
  have hh : 3 ^ bit x * x + bit x = 3 ^ bit y * y + bit y := by rw [← two_step, ← two_step, he]
  rw [← hbit] at hh
  exact Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 3^bit x) (Nat.add_right_cancel hh)

/-- At a fixed clock and fixed ordinary terminal, the lower-arm parity word
determines at most one integer source. -/
theorem word_endpoint_injective {x y t : ℕ}
    (hword : ∀ i < t, bit (step^[i] x) = bit (step^[i] y))
    (hend : step^[t] x = step^[t] y) : x = y := by
  induction t generalizing x y with
  | zero => exact hend
  | succ t ih =>
    have hfirst : bit x = bit y := hword 0 (by omega)
    apply one_step_inj hfirst
    apply ih
    · intro i hi
      rw [← Function.iterate_succ_apply, ← Function.iterate_succ_apply]
      exact hword (i+1) (by omega)
    · simpa only [Function.iterate_succ_apply] using hend

end Collatz.PairedCapacity

#print axioms Collatz.PairedCapacity.ordinary_carry_nonzero
#print axioms Collatz.PairedCapacity.carry_update

#print axioms Collatz.PairedCapacity.one_clock_bound
#print axioms Collatz.PairedCapacity.ordinary_clock_product

#print axioms Collatz.PairedCapacity.grade_clock_bound
#print axioms Collatz.PairedCapacity.word_endpoint_injective

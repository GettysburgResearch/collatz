import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Exact comparison for the all-clock ascent argument. Coordinates are shifted
heights `x+1`. An odd inverse multiplies by `2/3`. An even inverse takes
`V` to `2*V-1`. The algebra holds for all words before testing physical
integrality on the supplied target.
-/
namespace Collatz.RampReference

abbrev Word := List Bool

def odds : Word → Nat
  | [] => 0
  | true :: rest => odds rest + 1
  | false :: rest => odds rest

def evens : Word → Nat
  | [] => 0
  | true :: rest => evens rest
  | false :: rest => evens rest + 1

def applyWord : Word → ℚ → ℚ
  | [], v => v
  | true :: rest, v => applyWord rest ((2/3)*v)
  | false :: rest, v => applyWord rest (2*v-1)

def slope (w : Word) : ℚ := (2/3)^odds w * 2^evens w

def loss : Word → ℚ
  | [] => 0
  | true :: rest => loss rest
  | false :: rest => loss rest + slope rest

theorem affine (w : Word) (v : ℚ) :
    applyWord w v = slope w * v - loss w := by
  induction w generalizing v with
  | nil => simp [applyWord, slope, odds, evens, loss]
  | cons b w ih =>
    cases b <;> simp only [applyWord, ih, slope, odds, evens, loss, pow_succ] <;> ring

theorem slope_nonneg (w : Word) : 0 ≤ slope w := by
  unfold slope
  positivity

theorem slope_le (w : Word) : slope w ≤ (2:ℚ)^evens w := by
  have h : (2/3:ℚ)^odds w ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
  have two : 0 ≤ (2:ℚ)^evens w := by positivity
  simpa [slope] using mul_le_mul_of_nonneg_right h two

theorem loss_bounds (w : Word) : 0 ≤ loss w ∧ loss w ≤ (2:ℚ)^evens w - 1 := by
  induction w with
  | nil => norm_num [loss, evens]
  | cons b w ih =>
    cases b with
    | true => exact ih
    | false =>
      simp only [loss, evens, pow_succ]
      exact ⟨add_nonneg ih.1 (slope_nonneg w), by linarith [ih.2, slope_le w]⟩

private theorem recip_cancel (n : Nat) : (2/3:ℚ)^n * (3/2:ℚ)^n = 1 := by
  rw [← mul_pow]
  norm_num

private theorem three_cancel (n : Nat) : (2/3:ℚ)^n * (3:ℚ)^n = 2^n := by
  rw [← mul_pow]
  norm_num

private theorem two_three (n : Nat) : (2:ℚ)^n * (3/2:ℚ)^n = 3^n := by
  rw [← mul_pow]
  norm_num

/-- The true cut depends only on its positive reference terminal, the common
    binary exponent and the supplied ternary displacement. -/
theorem translated_cut (w : Word) (i K δ : Nat) (u : ℚ) (h : odds w = i+K) :
    applyWord w (2^δ * (3/2)^i * (2+3^K*u)) =
    applyWord w (2^δ * (3/2)^i * 2) + 2^(K+evens w+δ)*u := by
  rw [affine, affine]
  have identity : slope w * (2^δ * (3/2)^i * (3^K*u)) = 2^(K+evens w+δ)*u := by
    unfold slope
    rw [h, pow_add (2/3:ℚ) i K]
    calc
      _ = (((2/3:ℚ)^i * (3/2)^i) * ((2/3:ℚ)^K * 3^K)) *
          (2^evens w * 2^δ * u) := by ring
      _ = _ := by rw [recip_cancel, three_cancel, pow_add, pow_add]; ring
  linarith only [identity, show slope w * (2^δ * (3/2)^i * (2+3^K*u)) =
    slope w * (2^δ * (3/2)^i * 2) + slope w * (2^δ * (3/2)^i * (3^K*u)) by ring]

/-- The integer-sized boundary after the dyadic denominator clears lies in
    a narrow interval adjacent to the mixed power `2^(δ+1)*3^d`. -/
theorem boundary_interval (w : Word) (δ : Nat) :
    let d := evens w
    let z := applyWord w (2^(δ+1)*(3/2)^(odds w + d)) - 1
    2^(δ+1)*(3:ℚ)^d - 2^d ≤ z ∧ z ≤ 2^(δ+1)*3^d - 1 := by
  dsimp only
  rw [affine]
  have leading : slope w * (2^(δ+1)*(3/2)^(odds w + evens w)) =
      2^(δ+1)*(3:ℚ)^evens w := by
    unfold slope
    rw [pow_add (3/2:ℚ) (odds w) (evens w)]
    calc
      _ = 2^(δ+1) * (((2/3:ℚ)^odds w * (3/2)^odds w) *
          ((2:ℚ)^evens w * (3/2)^evens w)) := by ring
      _ = _ := by rw [recip_cancel, two_three, one_mul]
  rw [leading]
  have hb := loss_bounds w
  constructor <;> linarith

end Collatz.RampReference

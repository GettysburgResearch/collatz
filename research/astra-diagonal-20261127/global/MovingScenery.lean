import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Exact sections of a genuine odd Collatz word and the forced cost of
an arbitrarily long positive all-ones rise. -/
namespace Collatz.Diagonal.MovingScenery

/-- Chronological accelerated odd steps with exact division exponents. -/
inductive Path : List ℕ → ℕ → ℕ → Prop
  | nil (x : ℕ) (hx : x % 2 = 1) : Path [] x x
  | cons {e x y z : ℕ} {w : List ℕ} (hx : x % 2 = 1)
      (hy : y % 2 = 1) (he : 3 * x + 1 = 2 ^ e * y) (tail : Path w y z) :
      Path (e :: w) x z

def affine (w : List ℕ) (z : ℚ) : ℚ :=
  match w with
  | [] => z
  | e :: es => affine es ((3 * z + 1) / 2 ^ e)

theorem affine_section (w : List ℕ) (z x : ℚ) :
    2 ^ w.sum * (affine w z - affine w x) = 3 ^ w.length * (z - x) := by
  induction w generalizing z x with
  | nil => simp [affine]
  | cons e w ih =>
    simp only [List.sum_cons, List.length_cons, affine, pow_add, pow_succ]
    rw [mul_assoc, ih]
    have hd : (2 : ℚ) ^ e ≠ 0 := by positivity
    rw [div_sub_div_same]
    calc
      _ = 3^w.length * (((3*z+1-(3*x+1))/2^e) * 2^e) := by ring
      _ = _ := by rw [div_mul_cancel₀ _ hd]; ring

theorem path_affine {w : List ℕ} {x y : ℕ} (p : Path w x y) :
    affine w x = y := by
  induction p with
  | nil => rfl
  | @cons e x u y w _hx _hu he _tail ih =>
    have heq : 3 * (x : ℚ) + 1 = 2 ^ e * (u : ℚ) := by exact_mod_cast he
    have hd : (2 : ℚ) ^ e ≠ 0 := by positivity
    simp only [affine, heq]
    rw [mul_div_cancel_left₀ _ hd]
    exact ih

/-- The polynomial identity underlying the rotated tangent measure, already
at an exact positive integer target. -/
theorem path_centered {w : List ℕ} {x y : ℕ} (p : Path w x y) (z : ℚ) :
    2 ^ w.sum * (affine w z - y) = 3 ^ w.length * (z - x) := by
  rw [← path_affine p]
  exact affine_section w z x

/-- The entire physical odd cylinder lifts, with the same exponents. -/
theorem lift_path {w : List ℕ} {x y : ℕ} (p : Path w x y) (j : ℕ) :
    Path w (x + 2 * 2 ^ w.sum * j) (y + 2 * 3 ^ w.length * j) := by
  induction p generalizing j with
  | nil x hx =>
    simp only [List.sum_nil, List.length_nil, pow_zero, mul_one]
    exact .nil _ (by omega)
  | @cons e x u y w hx hu he tail ih =>
    simp only [List.sum_cons, List.length_cons, pow_succ]
    have htail := ih (3*j)
    have heq : 3 * (x + 2 * 2 ^ (e + w.sum) * j) + 1 =
        2 ^ e * (u + 2 * 2 ^ w.sum * (3*j)) := by
      rw [pow_add]
      calc
        _ = 3*x+1 + 2^e*(2*2^w.sum*(3*j)) := by ring
        _ = _ := by rw [he]; ring
    have h₁ : (x + 2 * 2 ^ (e + w.sum) * j) % 2 = 1 := by
      rw [show 2 * 2 ^ (e + w.sum) * j = 2 * (2 ^ (e + w.sum) * j) by ring]
      omega
    have h₂ : (u + 2 * 2 ^ w.sum * (3*j)) % 2 = 1 := by
      rw [show 2 * 2 ^ w.sum * (3*j) = 2 * (2 ^ w.sum * (3*j)) by ring]
      omega
    convert Path.cons h₁ h₂ heq htail using 1
    ring

theorem all_ones (k u : ℕ) (hu : 0 < u) :
    Path (List.replicate k 1) (2^(k+1)*u-1) (2*3^k*u-1) := by
  induction k generalizing u with
  | zero =>
    simp only [List.replicate_zero, Nat.zero_add, pow_one, pow_zero, mul_one]
    exact .nil _ (by omega)
  | succ k ih =>
    have hu' : 0 < 3*u := by omega
    have hp := ih (3*u) hu'
    rw [List.replicate_succ]
    have ht : 2*3^k*(3*u)-1 = 2*3^(k+1)*u-1 := by rw [pow_succ]; ring_nf
    rw [ht] at hp
    have hn : 0 < 2^(k+1)*u := by positivity
    have ha : 2^(k+1+1)*u = 2*(2^(k+1)*u) := by rw [pow_succ]; ring
    have hb : 2^(k+1)*(3*u) = 3*(2^(k+1)*u) := by ring
    have hc : 2^(k+1)*(3*u) = 2*(2^k*(3*u)) := by rw [pow_succ]; ring
    have hx : (2^(k+1+1)*u-1)%2=1 := by rw [ha]; omega
    have hn' : 0 < 2^k*(3*u) := by positivity
    have hy : (2^(k+1)*(3*u)-1)%2=1 := by rw [hc]; omega
    have he : 3*(2^(k+1+1)*u-1)+1=2^1*(2^(k+1)*(3*u)-1) := by
      rw [ha, hb, pow_one]
      omega
    exact Path.cons hx hy he hp

/-- A positive row supersolution bounds the gain of each genuine path.
This uses only the necessary inequality for individual inverse edges. -/
theorem path_lyapunov (H : ℕ → ℚ) (lam : ℚ) (hlam : 0 ≤ lam)
    (row : ∀ {x y e : ℕ}, x%2=1 → y%2=1 → 3*x+1=2^e*y →
      9 * H x ≤ lam * (4 : ℚ)^e * H y)
    {w : List ℕ} {x y : ℕ} (p : Path w x y) :
    9^w.length * H x ≤ lam^w.length * 4^w.sum * H y := by
  induction p with
  | nil => simp
  | @cons e x u y w hx hu he _tail ih =>
    simp only [List.length_cons, List.sum_cons, pow_succ, pow_add]
    calc
      _ = (9:ℚ)^w.length * (9*H x) := by ring
      _ ≤ (9:ℚ)^w.length * (lam * 4^e * H u) :=
        mul_le_mul_of_nonneg_left (row hx hu he) (by positivity)
      _ = (lam * 4^e) * (9^w.length * H u) := by ring
      _ ≤ (lam * 4^e) * (lam^w.length * 4^w.sum * H y) :=
        mul_le_mul_of_nonneg_left ih (by positivity)
      _ = _ := by ring

end Collatz.Diagonal.MovingScenery

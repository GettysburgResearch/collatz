import Mathlib.Tactic

/-! Finite arithmetic for RETURN_TOWER.md. Actual scalar/cylinder attachment
and the valuation interpretation of the center remain written mathematics. -/
namespace Collatz.CarryTowerRoundTen.ReturnTower

set_option autoImplicit false

theorem shifted_paid_identity (x : ℚ) :
    (9 * x + 5) / 32 + 7 = (9 / 32 : ℚ) * (x + 7) + 83 / 16 := by
  ring

theorem shifted_paid_four_fifths (x : ℚ) (hx : 3 ≤ x) :
    (9 * x + 5) / 32 + 7 ≤ (4 / 5 : ℚ) * (x + 7) := by
  linarith

theorem least_source_paid_factor (X : ℚ) (hX : (2 : ℚ)^34 ≤ X) :
    (9 / 32 : ℚ) * X + 83 / 16 ≤
      (9 / 32 + 83 / (2 : ℚ)^38) * X := by
  norm_num at *
  linarith

theorem exact_growth_constants :
    (9 / 8 : ℚ)^5 < 2 ∧
    (9 / 32 + 83 / (2 : ℚ)^38) * (9 / 8 : ℚ)^10 < 1 ∧
    (1 : ℚ) < (9 / 32 + 83 / (2 : ℚ)^38) * (9 / 8 : ℚ)^11 := by
  norm_num

/-- Every finite sequence of complete return inequalities has its product bound. -/
theorem finite_tower_product (X : ℕ → ℚ) (m : ℕ → ℕ) (n : ℕ)
    (lambda rho : ℚ) (hlambda : 0 ≤ lambda) (hrho : 0 ≤ rho)
    (hstep : ∀ i < n, X (i + 1) ≤ rho * lambda^(m i) * X i) :
    X n ≤ X 0 * lambda^(∑ i ∈ Finset.range n, m i) * rho^n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hi := ih (fun i h => hstep i (by omega))
    have hs := hstep n (by omega)
    calc
      X (n + 1) ≤ rho * lambda^(m n) * X n := hs
      _ ≤ rho * lambda^(m n) *
          (X 0 * lambda^(∑ i ∈ Finset.range n, m i) * rho^n) :=
        mul_le_mul_of_nonneg_left hi (by positivity)
      _ = X 0 * lambda^(∑ i ∈ Finset.range (n + 1), m i) * rho^(n + 1) := by
        rw [Finset.sum_range_succ, pow_add, pow_succ]
        ring

/-- Fifth powers convert the actual height bound into an integer run budget. -/
theorem fifth_power_budget (X B M m : ℕ)
    (hlow : 2^(3*m+1) ≤ X) (hhigh : X^5 < 2^(5*B+M)) :
    15*m + 5 < 5*B + M := by
  have hp : (2^(3*m+1))^5 ≤ X^5 := by gcongr
  have he : (2^(3*m+1))^5 = (2 : ℕ)^(15*m+5) := by
    rw [← pow_mul]
    congr 1
    omega
  rw [he] at hp
  by_contra h
  have hh : 5*B + M ≤ 15*m + 5 := by omega
  have hm := pow_le_pow_right₀ (show (1 : ℕ) ≤ 2 by omega) hh
  omega

/-- A finite budget controls the accumulated charge independently of paid words. -/
theorem accumulated_budget (m : ℕ → ℕ) (C n : ℕ)
    (hbudget : ∀ j < n, 15*m j < 5*C + ∑ i ∈ Finset.range j, m i) :
    15^n * (5*C + ∑ i ∈ Finset.range n, m i) ≤ 5*C*16^n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hi := ih (fun j h => hbudget j (by omega))
    have hb := hbudget n (by omega)
    have hs : 15 * (5*C + (∑ i ∈ Finset.range n, m i) + m n) ≤
        16 * (5*C + ∑ i ∈ Finset.range n, m i) := by omega
    calc
      15^(n+1) * (5*C + ∑ i ∈ Finset.range (n+1), m i) =
          15^n * (15 * (5*C + (∑ i ∈ Finset.range n, m i) + m n)) := by
            rw [Finset.sum_range_succ, pow_succ]
            ring
      _ ≤ 15^n * (16 * (5*C + ∑ i ∈ Finset.range n, m i)) :=
        Nat.mul_le_mul_left _ hs
      _ = 16 * (15^n * (5*C + ∑ i ∈ Finset.range n, m i)) := by ring
      _ ≤ 16 * (5*C*16^n) := Nat.mul_le_mul_left _ hi
      _ = 5*C*16^(n+1) := by rw [pow_succ]; ring

/-- The explicit fixed-source run-growth theorem after the height attachment. -/
theorem run_growth_bound (m : ℕ → ℕ) (C n : ℕ)
    (hbudget : ∀ j ≤ n, 15*m j < 5*C + ∑ i ∈ Finset.range j, m i) :
    3*15^n*m n < C*16^n := by
  have ha := accumulated_budget m C n (fun j h => hbudget j (by omega))
  have hb := hbudget n (by omega)
  have hp : 0 < (15 : ℕ)^n := by positivity
  have hs := Nat.mul_lt_mul_of_pos_left hb hp
  have ht : 5 * (3*15^n*m n) < 5 * (C*16^n) := by
    nlinarith [ha, hs]
  omega

def center (q : ℤ) : ℤ := 7551629537*q + 1478790549031

/-- The complete affine numerator, including its constant, transports the center. -/
theorem center_transport (q r : ℤ)
    (hedge : 274877906944*r = 282429536481*q + 1478790549031) :
    274877906944 * center r = 282429536481 * center q := by
  dsimp [center]
  linear_combination 7551629537 * hedge

theorem iterated_center_transport (q : ℕ → ℤ) (n : ℕ)
    (hedge : ∀ i < n,
      274877906944*q (i+1) = 282429536481*q i + 1478790549031) :
    (274877906944 : ℤ)^n * center (q n) =
      (282429536481 : ℤ)^n * center (q 0) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hi := ih (fun i h => hedge i (by omega))
    have hs := center_transport (q n) (q (n+1)) (hedge n (by omega))
    calc
      (274877906944 : ℤ)^(n+1) * center (q (n+1)) =
          (274877906944 : ℤ)^n * (274877906944 * center (q (n+1))) := by
            rw [pow_succ]
            ring
      _ = (274877906944 : ℤ)^n * (282429536481 * center (q n)) := by rw [hs]
      _ = 282429536481 * ((274877906944 : ℤ)^n * center (q n)) := by ring
      _ = 282429536481 * ((282429536481 : ℤ)^n * center (q 0)) := by rw [hi]
      _ = (282429536481 : ℤ)^(n+1) * center (q 0) := by rw [pow_succ]; ring

theorem constant_return_expands (q r : ℤ) (hq : 0 < q)
    (hedge : 274877906944*r = 282429536481*q + 1478790549031) : q < r := by
  linarith

theorem actual_tail_exponential_bound (K : ℕ) :
    32*K + 108 < 3^(K+6) := by
  induction K with
  | zero => norm_num
  | succ K ih =>
    have hp : 3^(K+1+6) = 3*3^(K+6) := by
      rw [show K+1+6 = (K+6)+1 by omega, pow_succ]
      ring
    rw [hp]
    omega

end Collatz.CarryTowerRoundTen.ReturnTower

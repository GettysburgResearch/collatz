import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.Tactic

/-! Integer content of the homogeneous projection, the local basis change,
and an actual physical path estimate used in the companion denominator theorem. -/
namespace Collatz.CompanionContent

/-- The three exponents sum to the degree. At least one of the last two
coordinates occurs, so the pure first-coordinate power is omitted. -/
def CommonDivisor (q b c d g : ℕ) : Prop :=
  ∀ i j k : ℕ, i + j + k = d → 0 < j + k → g ∣ q ^ i * b ^ j * c ^ k

/-- This describes all common divisors, including every prime power. -/
theorem projected_content (q b c d g : ℕ) (hqb : Nat.Coprime q b) :
    CommonDivisor q b c (d + 1) g ↔ g ∣ Nat.gcd b c := by
  constructor
  · intro h
    have hpow : g ∣ b ^ (d + 1) := by
      simpa using h 0 (d + 1) 0 (by omega) (by omega)
    have hgb : g ∣ q ^ d * b := by
      simpa using h d 1 0 (by omega) (by omega)
    have hgc : g ∣ q ^ d * c := by
      simpa using h d 0 1 (by omega) (by omega)
    have hcop : Nat.Coprime g (q ^ d) :=
      (Nat.Coprime.of_dvd_left hpow (hqb.symm.pow_left (d + 1))).pow_right d
    exact Nat.dvd_gcd (hcop.dvd_of_dvd_mul_left hgb) (hcop.dvd_of_dvd_mul_left hgc)
  · intro h i j k _ hpos
    have hb : g ∣ b := h.trans (Nat.gcd_dvd_left b c)
    have hc : g ∣ c := h.trans (Nat.gcd_dvd_right b c)
    cases j with
    | zero =>
      cases k with
      | zero => omega
      | succ k =>
        rw [pow_succ]
        exact hc.trans (dvd_mul_of_dvd_right (dvd_mul_left c _) _)
    | succ j =>
      rw [pow_succ]
      exact hb.trans (dvd_mul_of_dvd_left (dvd_mul_of_dvd_right (dvd_mul_left b _) _) _)

/-- In a local monomial basis, subtract evaluation at the pivot divided by
its nonzero evaluation. These forms vanish at the chosen rational point. -/
theorem pivot_vanishes {K : Type*} [Field K] (v p : K) (hp : p ≠ 0) :
    v - (v / p) * p = 0 := by field_simp; ring

/-- Projection away from the pivot is injective on the evaluation kernel.
This gives the lower dimension and independence check for the local change. -/
theorem kernel_determined_off_pivot {ι K : Type*} [Fintype ι] [DecidableEq ι] [Field K]
    (w a b : ι → K) (p : ι) (hp : w p ≠ 0)
    (ha : ∑ i, a i * w i = 0) (hb : ∑ i, b i * w i = 0)
    (rest : ∀ i ≠ p, a i = b i) : a = b := by
  classical
  have he : ∑ i ∈ (Finset.univ.erase p), a i * w i =
      ∑ i ∈ (Finset.univ.erase p), b i * w i :=
    Finset.sum_congr rfl (fun i hi => by rw [rest i (Finset.mem_erase.mp hi).1])
  rw [← Finset.sum_erase_add _ _ (Finset.mem_univ p)] at ha hb
  funext i
  by_cases hi : i = p
  · subst i
    rw [he] at ha
    have heq : a p * w p = b p * w p := add_left_cancel (ha.trans hb.symm)
    exact mul_right_cancel₀ hp heq
  · exact rest i hi

def Edge (x y e : ℕ) : Prop :=
  (e = 0 ∧ 2 * y = x) ∨ (e = 1 ∧ 2 * y = 3 * x + 1)

/-- Both shortcut branches satisfy the fifth-power clock inequality above six. -/
theorem edge_bound (x y e : ℕ) (hx : 6 ≤ x) (h : Edge x y e) :
    (2 * y) ^ 3 ≤ 32 ^ e * x ^ 3 := by
  rcases h with ⟨rfl, hy⟩ | ⟨rfl, hy⟩
  · simp [hy]
  · simp only [hy, pow_one]
    obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hx
    ring_nf
    omega

/-- The telescoped estimate holds at every finite physical prefix whose
inputs lie above the indicated floor. Apply to each suffix for the record bound. -/
theorem path_bound (x e : ℕ → ℕ) (n : ℕ)
    (h : ∀ i < n, 6 ≤ x i ∧ Edge (x i) (x (i + 1)) (e i)) :
    (2 ^ n * x n) ^ 3 ≤ 32 ^ (∑ i ∈ Finset.range n, e i) * (x 0) ^ 3 := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hs := edge_bound _ _ _ (h n (by omega)).1 (h n (by omega)).2
    have hi := ih (fun i hlt => h i (by omega))
    rw [Finset.sum_range_succ, pow_add]
    calc
      (2 ^ (n + 1) * x (n + 1)) ^ 3 =
          (2 ^ n) ^ 3 * (2 * x (n + 1)) ^ 3 := by rw [pow_succ]; ring
      _ ≤ (2 ^ n) ^ 3 * (32 ^ e n * x n ^ 3) := Nat.mul_le_mul_left _ hs
      _ = 32 ^ e n * (2 ^ n * x n) ^ 3 := by ring
      _ ≤ 32 ^ e n * (32 ^ (∑ i ∈ Finset.range n, e i) * x 0 ^ 3) :=
        Nat.mul_le_mul_left _ hi
      _ = _ := by ring

/-- Swapping an inverted pair pays at least the clock separation. -/
theorem inversion_cost (a k h s gap : ℕ) (hg : gap ≤ h) (hs : 0 < s) :
    a * (k + s) + (a + h) * k + gap ≤ a * k + (a + h) * (k + s) := by
  have hh : gap ≤ h * s := hg.trans (by simpa using Nat.mul_le_mul_left h hs)
  calc
    _ ≤ a * (k + s) + (a + h) * k + h * s := Nat.add_le_add_left hh _
    _ = _ := by ring

/-- The top degree group retains the product of all differences from the
pivot, in addition to the ordinary Vandermonde determinant. -/
theorem top_block {R : Type*} [CommRing R] (n : ℕ) (s : Fin n → R) (b : R) :
    (Matrix.of (fun i j : Fin n => s i ^ (j.val + 1) - b ^ (j.val + 1))).det =
      (∏ i, (s i - b)) * (Matrix.vandermonde s).det := by
  cases n with
  | zero => simp
  | succ n =>
    rw [← Matrix.det_mul_column (fun i => s i - b) (Matrix.vandermonde s)]
    apply Matrix.det_eq_of_forall_col_eq_smul_add_pred (fun _ => b)
    · intro i
      simp [Matrix.vandermonde_apply]
    · intro i j
      simp only [Matrix.of_apply, Matrix.vandermonde_apply, Fin.val_succ, Fin.val_castSucc]
      simp only [pow_succ]
      ring

#print axioms projected_content
#print axioms pivot_vanishes
#print axioms kernel_determined_off_pivot
#print axioms edge_bound
#print axioms path_bound
#print axioms inversion_cost
#print axioms top_block
end Collatz.CompanionContent

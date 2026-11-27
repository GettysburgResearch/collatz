import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring

/-! Finite interpolation and complete composite-divisor bookkeeping for
periodically closed prefixes. The integral-points theorem is a written input. -/
namespace Collatz.PrefixInterpolation

/-- The local clock and local endpoint determine the two targets in a residue
ring, once the completed prefix clock and its endpoint close there. -/
theorem local_targets {R : Type*} [CommRing R]
    (U y a b c s t aInv bInv : R)
    (ha : aInv * a = 1) (hb : bInv * b = 1)
    (clock : a * U = b) (edge : a * t = b * y + c) (closes : t = s) :
    U = aInv * b ∧ y = bInv * (a * s - c) := by
  constructor
  · calc
      U = (aInv * a) * U := by rw [ha, one_mul]
      _ = aInv * b := by rw [mul_assoc, clock]
  · have hed : b * y = a * s - c := by rw [← closes, edge]; ring
    calc
      y = (bInv * b) * y := by rw [hb, one_mul]
      _ = bInv * (a * s - c) := by rw [mul_assoc, hed]

/-- A whole prime power common to two clock differences divides the local
clock difference, since the earlier physical or companion clock is a unit. -/
theorem clock_overlap {R : Type*} [CommRing R] (u v a b vInv : R)
    (unitClock : vInv * v = 1) (first : u = v) (later : a * u = b * v) :
    a = b := by
  calc
    a = vInv * (a * u) := by rw [first, ← mul_left_comm, unitClock, mul_one]
    _ = vInv * (b * v) := by rw [later]
    _ = b := by rw [← mul_left_comm, unitClock, mul_one]

/-- Bidegree less than `r` in each variable provides a nonzero rational
coefficient array through any `m < r*r` specified rational points. -/
theorem interpolate (m r : ℕ) (h : m < r * r) (u y : Fin m → ℚ) :
    ∃ c : Fin r × Fin r → ℚ, c ≠ 0 ∧ ∀ i,
      ∑ j, (u i ^ (j.1 : ℕ) * y i ^ (j.2 : ℕ)) * c j = 0 := by
  classical
  let M : Matrix (Fin m) (Fin r × Fin r) ℚ :=
    fun i j => u i ^ (j.1 : ℕ) * y i ^ (j.2 : ℕ)
  have hi : ¬ Function.Injective M.mulVecLin := by
    intro hinj
    have bd := LinearMap.finrank_le_finrank_of_injective hinj
    simp only [Module.finrank_fintype_fun_eq_card, Fintype.card_prod,
      Fintype.card_fin] at bd
    omega
  have hk : M.mulVecLin.ker ≠ ⊥ := fun heq => hi (LinearMap.ker_eq_bot.mp heq)
  obtain ⟨c, hc, hn⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hk
  refine ⟨c, hn, fun i => ?_⟩
  exact congrFun (LinearMap.mem_ker.mp hc) i

/-- Each pair is charged once, with its entire greatest common divisor. -/
def pairOverlap : List ℕ → ℕ
  | [] => 1
  | a :: xs => (xs.map (Nat.gcd a)).prod * pairOverlap xs

def common : List ℕ → ℕ
  | [] => 1
  | a :: xs => Nat.lcm a (common xs)

private theorem common_dvd {N : ℕ} (xs : List ℕ) (h : ∀ a ∈ xs, a ∣ N) :
    common xs ∣ N := by
  induction xs with
  | nil => simp [common]
  | cons a xs ih =>
    exact Nat.lcm_dvd (h a (by simp)) (ih (fun b hb => h b (by simp [hb])))

private theorem gcd_prod (a : ℕ) (xs : List ℕ) :
    Nat.gcd a xs.prod ∣ (xs.map (Nat.gcd a)).prod := by
  induction xs with
  | nil => simp
  | cons b xs ih =>
    simp only [List.prod_cons, List.map_cons]
    exact (Nat.gcd_mul_right_dvd_mul_gcd ..).trans (Nat.mul_dvd_mul_left _ ih)

private theorem common_dvd_product (xs : List ℕ) : common xs ∣ xs.prod := by
  induction xs with
  | nil => simp [common]
  | cons a xs ih =>
    exact Nat.lcm_dvd (dvd_mul_right a xs.prod) (ih.trans (dvd_mul_left xs.prod a))

private theorem product_dvd_common_overlap (xs : List ℕ) :
    xs.prod ∣ common xs * pairOverlap xs := by
  induction xs with
  | nil => simp [common, pairOverlap]
  | cons a xs ih =>
    have hg : Nat.gcd a (common xs) ∣ (xs.map (Nat.gcd a)).prod :=
      (Nat.gcd_dvd_gcd_of_dvd_right a (common_dvd_product xs)).trans (gcd_prod a xs)
    simp only [List.prod_cons, common, pairOverlap]
    apply (Nat.mul_dvd_mul_left a ih).trans
    calc
      a * (common xs * pairOverlap xs) =
          Nat.lcm a (common xs) * Nat.gcd a (common xs) * pairOverlap xs := by
            rw [mul_comm (Nat.lcm a (common xs)), Nat.gcd_mul_lcm, mul_assoc]
      _ ∣ Nat.lcm a (common xs) * ((xs.map (Nat.gcd a)).prod * pairOverlap xs) := by
        rw [mul_assoc]
        exact Nat.mul_dvd_mul_left _ (Nat.mul_dvd_mul_right hg _)

/-- All complete cancelled factors divide one interpolant value. The product
of factors divides that value times the pairwise-overlap debit, with no
squarefreeness or coprimality assumption. -/
theorem product_dvd_value_times_overlap (xs : List ℕ) (N : ℕ)
    (h : ∀ a ∈ xs, a ∣ N) : xs.prod ∣ N * pairOverlap xs :=
  (product_dvd_common_overlap xs).trans (Nat.mul_dvd_mul_right (common_dvd xs h) _)

#print axioms local_targets
#print axioms clock_overlap
#print axioms interpolate
#print axioms product_dvd_value_times_overlap

end Collatz.PrefixInterpolation

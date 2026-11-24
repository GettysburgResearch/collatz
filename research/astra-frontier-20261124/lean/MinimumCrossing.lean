module

public import CyclePacking
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

@[expose] public section
namespace Collatz.ElementaryPacking

/-- A first coefficient crossing that fails to descend at its endpoint
already yields the arithmetic inequality at its own source. -/
theorem nondescending_affine_gate {x y : ℕ} {w : List Bool}
    (legal : Follows w x y) (nondesc : x ≤ y) (prefixes : BeforeCrossing w) :
    3 * ((2 : ℕ) ^ w.length * x) ≤
      3 * (3 ^ ones w * x) + ones w * 3 ^ ones w := by
  have h1 := Nat.mul_le_mul_left (2 ^ w.length) nondesc
  rw [follows_affine legal] at h1
  have h2 := beforeCrossing_carry w prefixes
  omega

theorem nondescending_floor {x y : ℕ} {w : List Bool}
    (legal : Follows w x y) (nondesc : x ≤ y) (prefixes : BeforeCrossing w)
    (contracts : 3 ^ ones w < (2 : ℕ) ^ w.length) : x ≤ centerFloor (ones w) := by
  have h := Nat.mul_le_mul_left (2 ^ w.length) nondesc
  rw [follows_affine legal] at h
  unfold centerFloor
  rw [← firstCrossing_length w prefixes contracts]
  apply (Nat.le_div_iff_mul_le (Nat.sub_pos_of_lt contracts)).mpr
  have hm := congrArg (fun z : ℕ => z * x) (Nat.sub_add_cancel contracts.le)
  rw [Nat.add_mul] at hm
  rw [Nat.mul_comm x]
  have hend := beforeCrossing_envelope w prefixes
  omega

/-- No floating-point evaluation is involved in the logarithmic reduction. -/
theorem nondescending_log_gate {x y : ℕ} {w : List Bool} (hx : 0 < x)
    (legal : Follows w x y) (nondesc : x ≤ y) (prefixes : BeforeCrossing w)
    (contracts : 3 ^ ones w < (2 : ℕ) ^ w.length) :
    0 < (w.length : ℝ) * Real.log 2 - ones w * Real.log 3 ∧
    3 * (x : ℝ) * ((w.length : ℝ) * Real.log 2 - ones w * Real.log 3) < ones w := by
  let N := (2 : ℝ) ^ w.length
  let M := (3 : ℝ) ^ ones w
  have hcontract : M < N := by
    dsimp [M, N]
    exact_mod_cast contracts
  have hm : 0 < M := by dsimp [M]; positivity
  have hn : 0 < N := hm.trans hcontract
  have hr : 1 < N / M := (one_lt_div hm).mpr hcontract
  have ht : 3 * (N * (x : ℝ)) ≤ 3 * (M * x) + ones w * M := by
    dsimp [M, N]
    exact_mod_cast nondescending_affine_gate legal nondesc prefixes
  have hs : 3 * (x : ℝ) * (N / M - 1) ≤ ones w := by
    field_simp [hm.ne']
    nlinarith only [ht]
  have hlog := Real.log_lt_sub_one_of_pos (zero_lt_one.trans hr) hr.ne'
  have hmul := mul_lt_mul_of_pos_left hlog (by positivity : 0 < 3 * (x : ℝ))
  have heq : Real.log (N / M) = (w.length : ℝ) * Real.log 2 - ones w * Real.log 3 := by
    rw [Real.log_div hn.ne' hm.ne']
    simp [N, M, Real.log_pow]
  rw [← heq]
  exact ⟨Real.log_pos hr, hmul.trans_le hs⟩

/-- A strict rational between Farey neighbors has at least their numerator
sum and denominator sum, even for a fraction not in lowest terms. -/
theorem farey_coordinates (a b c d A p : ℤ) (hdet : b*c-a*d=1)
    (hl : a*p < b*A) (hu : d*A < c*p) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hc : 0 ≤ c) (hd : 0 ≤ d) : a + c ≤ A ∧ b + d ≤ p := by
  have h1 : 1 ≤ b*A-a*p := by omega
  have h2 : 1 ≤ c*p-d*A := by omega
  have hA : c * (b*A-a*p) + a * (c*p-d*A) = A := by
    calc
      _ = (b*c-a*d)*A := by ring
      _ = _ := by rw [hdet, one_mul]
  have hP : d * (b*A-a*p) + b * (c*p-d*A) = p := by
    calc
      _ = (b*c-a*d)*p := by ring
      _ = _ := by rw [hdet, one_mul]
  constructor
  · nlinarith only [mul_le_mul_of_nonneg_left h1 hc, mul_le_mul_of_nonneg_left h2 ha, hA]
  · nlinarith only [mul_le_mul_of_nonneg_left h1 hd, mul_le_mul_of_nonneg_left h2 hb, hP]

#print axioms nondescending_affine_gate
#print axioms nondescending_floor
#print axioms nondescending_log_gate
#print axioms farey_coordinates

end Collatz.ElementaryPacking

import Mathlib.Basic.Real.Basic
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Ring

/-! Integer normalization of physical odd Collatz sites and bounded variation of the
geometric amplitude along chronological segments. The asymptotic exponential-sum
and Diophantine estimates are in the accompanying paper. -/

namespace Collatz.Unconventional.Arithmetic

/-- An integer coordinate on the three dyadic bands. -/
def coord (x k : ℕ) : ℕ := 2 ^ (2 - k) * x

/-- The folded recurrence follows from the literal integer odd step. -/
theorem physical_fold {x y a b k l : ℕ}
    (ha : 1 ≤ a) (ha' : a ≤ 2) (hb : 1 ≤ b) (hb' : b ≤ 2)
    (hk : k ≤ 2) (hl : l ≤ 2) (hclock : a + l = b + k)
    (hodd : 2 ^ a * y = 3 * x + 1) :
    2 ^ b * coord y l = 3 * coord x k + 2 ^ (2 - k) := by
  interval_cases k <;> interval_cases l <;> interval_cases a <;> interval_cases b <;>
    norm_num [coord] at * <;> omega

/-- At an integer state in its prescribed band the folded coordinate is exactly
four times its real mantissa. -/
theorem coord_real (x k : ℕ) (hk : k ≤ 2) :
    (coord x k : ℝ) = 4 * ((x : ℝ) / (2 : ℝ) ^ k) := by
  interval_cases k <;> norm_num [coord] <;> ring

/-- Dividing a folded edge by its geometric rank gives the slowly varying amplitude.
All clocks are natural, even at the doubled seam. -/
theorem amplitude_edge {Z Z' c rho : ℝ} {p h r r' b : ℕ}
    (hpos : 0 < rho) (hbase : rho ^ p = 2)
    (hr : r + h = r' + p * b) (he : (2 : ℝ) ^ b * Z' = 3 * Z + c) :
    rho ^ h * (Z' / rho ^ r') = 3 * (Z / rho ^ r) + c / rho ^ r := by
  have hw : rho ^ r * rho ^ h = rho ^ r' * (2 : ℝ) ^ b := by
    calc
      rho ^ r * rho ^ h = rho ^ (r + h) := (pow_add _ _ _).symm
      _ = rho ^ (r' + p * b) := by rw [hr]
      _ = rho ^ r' * (2 : ℝ) ^ b := by rw [pow_add, pow_mul, hbase]
  field_simp
  nlinarith only [congrArg (fun u : ℝ => u * Z') hw,
    congrArg (fun u : ℝ => rho ^ r' * u) he]

/-- Numerical amplitude step bound under the strip's physical gain envelope. -/
theorem amplitude_step_bound {s L A A' u : ℝ}
    (hL : 3 ≤ L) (hgap : (L - 3) * s ≤ 1)
    (hA : 0 ≤ A) (hA' : A ≤ 8 * s) (hu : 0 ≤ u) (hu' : u ≤ 4)
    (he : L * A' = 3 * A + u) :
    |A' - A| ≤ 8 / 3 := by
  have hprod : (L - 3) * A ≤ 8 :=
    calc
      (L - 3) * A ≤ (L - 3) * (8 * s) :=
        mul_le_mul_of_nonneg_left hA' (by linarith)
      _ ≤ 8 := by linarith
  have hprod0 : 0 ≤ (L - 3) * A := mul_nonneg (by linarith) hA
  rw [abs_le]
  constructor
  · by_contra! hn
    have hh : L * (A - A') > 8 := by
      calc
        L * (A - A') ≥ 3 * (A - A') := by
          apply mul_le_mul_of_nonneg_right hL
          linarith
        _ > 8 := by linarith
    nlinarith
  · by_contra! hn
    have hh : L * (A' - A) > 8 := by
      calc
        L * (A' - A) ≥ 3 * (A' - A) := by
          apply mul_le_mul_of_nonneg_right hL
          linarith
        _ > 8 := by linarith
    nlinarith

/-- Uniform chronological freezing over an interval; the error involves the interval
length, independently of the lap length and its starting clock. -/
theorem freeze {A : ℕ → ℝ} {K : ℝ} (h : ∀ j, |A (j+1) - A j| ≤ K)
    (i n : ℕ) : |A (i+n) - A i| ≤ (n : ℝ) * K := by
  induction n with
  | zero => simp
  | succ n ih =>
    have htriangle := abs_add_le (A (i+n+1) - A (i+n)) (A (i+n) - A i)
    calc
      |A (i+(n+1)) - A i| ≤ |A (i+n+1) - A (i+n)| + |A (i+n) - A i| := by
        simpa [Nat.add_assoc] using htriangle
      _ ≤ K + (n : ℝ) * K := add_le_add (h (i+n)) ih
      _ = ((n+1 : ℕ) : ℝ) * K := by push_cast; ring


/-- Every actual incoming valuation word fixes its terminal numerator mod 3^k.
The addition constant is the common reduced denominator on a rational orbit. -/
theorem incoming_residue {d : ℕ} {x y a : ℕ → ℕ}
    (hx : ∀ j, 2 ^ a j * x (j+1) = 3 * x j + d)
    (hy : ∀ j, 2 ^ a j * y (j+1) = 3 * y j + d)
    (k : ℕ) : Nat.ModEq (3^k) (x k) (y k) := by
  induction k with
  | zero => simpa using (Nat.modEq_one (a := x 0) (b := y 0))
  | succ j ih =>
    apply Nat.ModEq.cancel_left_of_coprime
      (Nat.Coprime.pow (j+1) (a j) (by decide : Nat.Coprime 3 2))
    rw [hx, hy]
    simpa [pow_succ, Nat.mul_comm] using (ih.mul_left' 3).add_right d

/-- Equality of a full residue pins a real-model difference near an actual integer. -/
theorem residue_near_wrap {x y Q : ℕ} (hq : 0 < Q)
    (hmod : Nat.ModEq Q x y) {f g E : ℝ}
    (hx : |(x : ℝ) / Q - f| ≤ E) (hy : |(y : ℝ) / Q - g| ≤ E) :
    ∃ m : ℤ, |g - f - (m : ℝ)| ≤ 2 * E := by
  obtain ⟨m, hm⟩ := hmod.dvd
  refine ⟨m, ?_⟩
  have hr : (y : ℝ) - x = (Q : ℝ) * m := by exact_mod_cast hm
  have hqr : (Q : ℝ) ≠ 0 := by exact_mod_cast Nat.ne_of_gt hq
  have hin : (y : ℝ) / Q - (x : ℝ) / Q = m := by
    rw [← sub_div, hr]
    field_simp
  rcases abs_le.mp hx with ⟨hx1,hx2⟩
  rcases abs_le.mp hy with ⟨hy1,hy2⟩
  apply abs_le.mpr
  constructor <;> linarith

#print axioms incoming_residue
#print axioms residue_near_wrap
#print axioms physical_fold
#print axioms coord_real
#print axioms amplitude_edge
#print axioms amplitude_step_bound
#print axioms freeze

end Collatz.Unconventional.Arithmetic

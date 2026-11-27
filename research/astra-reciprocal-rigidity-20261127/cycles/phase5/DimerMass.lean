import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.Nat.Init
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Kernel arithmetic for the dimer reciprocal-mass proof.
`false` encodes the block 10, and `true` encodes 110.
-/
namespace CollatzResearch.DimerMass

def odds : List Bool → ℕ
  | [] => 0
  | false :: w => odds w + 1
  | true :: w => odds w + 2

/-- The mass 4^(number of ones) / 2^(physical length) of complete blocks. -/
def mass : List Bool → ℤ
  | [] => 1
  | false :: w => mass w
  | true :: w => 2 * mass w

/-- The complete block strings of each odd count. -/
def words : ℕ → List (List Bool)
  | 0 => [[]]
  | 1 => [[false]]
  | n + 2 => (words (n+1)).map (false :: ·) ++ (words n).map (true :: ·)

theorem mem_words (n : ℕ) (w : List Bool) : w ∈ words n ↔ odds w = n := by
  induction n using Nat.twoStepInduction generalizing w with
  | zero =>
    cases w with
    | nil => simp [words, odds]
    | cons b w => cases b <;> simp [words, odds]
  | one =>
    cases w with
    | nil => simp [words, odds]
    | cons b w =>
      cases b
      · cases w with
        | nil => simp [words, odds]
        | cons c w => cases c <;> simp [words, odds]
      · simp [words, odds]
  | more n hn hs =>
    cases w with
    | nil => simp [words, odds]
    | cons b w =>
      cases b <;> simp [words, odds, hn, hs]

def completeCoeff (n : ℕ) : ℤ := ((words n).map mass).sum

private theorem twice_sum (xs : List (List Bool)) :
    (xs.map (fun w => 2 * mass w)).sum = 2 * (xs.map mass).sum := by
  induction xs with
  | nil => simp
  | cons a xs ih => simp [ih, mul_add]

private theorem coeff_rec (n : ℕ) : completeCoeff (n+2) = completeCoeff (n+1) + 2*completeCoeff n := by
  unfold completeCoeff
  simp [words, List.map_map, Function.comp_def, mass, twice_sum]

/-- Closed formula for all complete-block masses, including the empty word. -/
theorem complete_mass (n : ℕ) : 3 * completeCoeff n = 2^(n+1) + (-1 : ℤ)^n := by
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more n hn hs =>
    rw [coeff_rec]
    calc
      3 * (completeCoeff (n+1) + 2 * completeCoeff n) =
          (3 * completeCoeff (n+1)) + 2 * (3*completeCoeff n) := by ring
      _ = 2^((n+1)+1) + (-1 : ℤ)^(n+1) + 2*(2^(n+1) + (-1 : ℤ)^n) := by rw [hs, hn]
      _ = _ := by simp only [pow_succ]; ring

/-- For q≥2 all three terminal runs are possible. -/
theorem factor_mass (n : ℕ) :
    completeCoeff (n+2) + 2 * completeCoeff (n+1) + 4 * completeCoeff n =
      2^(n+3) + (-1 : ℤ)^(n+2) := by
  have h0 := complete_mass n
  have h1 := complete_mass (n+1)
  have h2 := complete_mass (n+2)
  simp only [pow_succ] at h0 h1 h2 ⊢
  omega

/-- Peeling one odd count from the rational closed tail. -/
theorem tail_difference (q : ℕ) :
    (4 * (1/2 : ℚ)^q + (4/5 : ℚ)*(-1/4 : ℚ)^q) -
      (4 * (1/2 : ℚ)^(q+1) + (4/5 : ℚ)*(-1/4 : ℚ)^(q+1)) =
      2 * (1/2 : ℚ)^q + (-1/4 : ℚ)^q := by
  simp only [pow_succ]
  ring

theorem floor_certificate : 301^44 < 2^70 * 100^44 := by decide +kernel

theorem cutoff_tail :
    (4 * (1/2 : ℚ)^45 + (4/5 : ℚ)*(-1/4 : ℚ)^45)/3 < (1/2 : ℚ)^44 := by
  norm_num

#print axioms mem_words
#print axioms complete_mass
#print axioms factor_mass
#print axioms tail_difference
#print axioms floor_certificate
#print axioms cutoff_tail

end CollatzResearch.DimerMass

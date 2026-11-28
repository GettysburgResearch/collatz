import ParityTail

/-! A native first-hit deadline behind the finite counted-merger test.
This does not bound the first hit of an arbitrary lower source: the matching
terminal odd count is a substantive hypothesis. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FullProof.Deadline

open Parity

private theorem step_lower_product (n : ℕ) :
    3 ^ (n % 2) * n ≤ 2 * step n := by
  by_cases h : n % 2 = 0
  · have hs : 2 * step n = n := by simp [step, h]; omega
    rw [h, pow_zero, one_mul]
    exact le_of_eq hs.symm
  · have h₁ : n % 2 = 1 := by omega
    have hs : 2 * step n = 3 * n + 1 := by simp [step, h]; omega
    rw [h₁, pow_one]
    omega

theorem native_lower_product (n t : ℕ) :
    3 ^ count n t * n ≤ 2 ^ t * run n t := by
  induction t generalizing n with
  | zero => simp [count, run]
  | succ t ih =>
    have hs := step_lower_product n
    have hi := ih (step n)
    simp only [count, run, pow_succ]
    calc
      3 ^ (n % 2 + count (step n) t) * n
          = 3 ^ count (step n) t * (3 ^ (n % 2) * n) := by
            rw [pow_add]; ring
      _ ≤ 3 ^ count (step n) t * (2 * step n) :=
        Nat.mul_le_mul_left _ hs
      _ = 2 * (3 ^ count (step n) t * step n) := by ring
      _ ≤ 2 * (2 ^ t * run (step n) t) := Nat.mul_le_mul_left _ hi
      _ = 2 ^ t * 2 * run (step n) t := by ring

private theorem step_floor_two_product {n : ℕ} (hn : 2 ≤ n) :
    2 ^ (1 + n % 2) * step n ≤ n * 7 ^ (n % 2) := by
  by_cases h : n % 2 = 0
  · have hs : 2 * step n = n := by simp [step, h]; omega
    rw [h, add_zero, pow_one, pow_zero, mul_one]
    exact le_of_eq hs
  · have h₁ : n % 2 = 1 := by omega
    have hs : 2 * step n = 3 * n + 1 := by simp [step, h]; omega
    rw [h₁]
    norm_num
    omega

theorem native_floor_two_product (n t : ℕ)
    (floor : ∀ i : ℕ, i < t → 2 ≤ run n i) :
    2 ^ (t + count n t) * run n t ≤ n * 7 ^ count n t := by
  induction t generalizing n with
  | zero => simp [count, run]
  | succ t ih =>
    have hn : 2 ≤ n := by simpa [run] using floor 0 (by omega)
    have hs := step_floor_two_product hn
    have hi := ih (step n) (by
      intro i hi
      exact floor (i + 1) (by omega))
    simp only [count, run]
    calc
      2 ^ (t + 1 + (n % 2 + count (step n) t)) * run (step n) t
          = 2 ^ (1 + n % 2) *
              (2 ^ (t + count (step n) t) * run (step n) t) := by
            rw [← mul_assoc, ← pow_add]
            congr 2
            omega
      _ ≤ 2 ^ (1 + n % 2) * (step n * 7 ^ count (step n) t) :=
        Nat.mul_le_mul_left _ hi
      _ = (2 ^ (1 + n % 2) * step n) * 7 ^ count (step n) t := by ring
      _ ≤ (n * 7 ^ (n % 2)) * 7 ^ count (step n) t :=
        Nat.mul_le_mul_right _ hs
      _ = n * 7 ^ (n % 2 + count (step n) t) := by rw [pow_add]; ring

def FirstHit (n t : ℕ) : Prop :=
  run n t = 1 ∧ ∀ i : ℕ, i < t → run n i ≠ 1

theorem first_hit_product {n t : ℕ} (hn : 0 < n) (hit : FirstHit n t) :
    2 ^ (t + count n t) ≤ n * 7 ^ count n t := by
  have hp := native_floor_two_product n t (by
    intro i hi
    have hpos := run_positive hn i
    have hnot := hit.2 i hi
    omega)
  simpa only [hit.1, mul_one] using hp

private theorem strict_power_gap {R d : ℕ} (hR : 0 < R) (hd : 2 * R ≤ d) :
    7 ^ (R + d) < 6 ^ R * 8 ^ d := by
  obtain ⟨e, he⟩ := Nat.exists_eq_add_of_le hd
  have hleft : 7 ^ (R + d) = 343 ^ R * 7 ^ e := by
    rw [he, show R + (2 * R + e) = 3 * R + e by omega, pow_add, pow_mul]
    norm_num
  have hright : 6 ^ R * 8 ^ d = 384 ^ R * 8 ^ e := by
    rw [he, pow_add, pow_mul]
    norm_num
    rw [← mul_assoc, ← mul_pow]
    norm_num
  rw [hleft, hright]
  have hp : (343 : ℕ) ^ R < 384 ^ R := by gcongr; norm_num
  have he' : (7 : ℕ) ^ e ≤ 8 ^ e := by gcongr; norm_num
  exact lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_right hp (by positivity))
    (Nat.mul_le_mul_left _ he')

/-- A matching first-hit grade cannot occur two upper laps per initial grade late. -/
theorem matching_first_hit_deadline {n H R d : ℕ}
    (hn : 0 < n) (hR : 0 < R)
    (upper : 3 ^ R * n ≤ 2 ^ H)
    (hit : FirstHit n (H + 2 * d))
    (grade : count n (H + 2 * d) = R + d) :
    d < 2 * R := by
  have hp := first_hit_product hn hit
  rw [grade] at hp
  have hmul := Nat.mul_le_mul_left (3 ^ R) hp
  have hupper := Nat.mul_le_mul_right (7 ^ (R + d)) upper
  have hcombined : 3 ^ R * 2 ^ (H + 2 * d + (R + d)) ≤
      2 ^ H * 7 ^ (R + d) := by nlinarith
  have hfactor : 3 ^ R * 2 ^ (H + 2 * d + (R + d)) =
      2 ^ H * (6 ^ R * 8 ^ d) := by
    rw [show H + 2 * d + (R + d) = H + R + 3 * d by omega,
      pow_add, pow_add, pow_mul]
    norm_num
    rw [show (6 : ℕ) ^ R = 3 ^ R * 2 ^ R by rw [← mul_pow]; norm_num]
    ring
  rw [hfactor] at hcombined
  have hle : 6 ^ R * 8 ^ d ≤ 7 ^ (R + d) :=
    Nat.le_of_mul_le_mul_left hcombined (by positivity)
  by_contra h
  exact (not_lt_of_ge hle) (strict_power_gap hR (by omega))

theorem native_matching_first_hit_deadline {n H r d : ℕ}
    (hn : 0 < n) (upper : run (3 * n) H = 1)
    (upper_grade : count (3 * n) H = r)
    (hit : FirstHit n (H + 2 * d))
    (grade : count n (H + 2 * d) = r + 1 + d) :
    d < 2 * (r + 1) := by
  have hp := native_lower_product (3 * n) H
  rw [upper_grade, upper, mul_one] at hp
  apply matching_first_hit_deadline hn (by omega) _ hit grade
  simpa only [pow_succ, mul_assoc] using hp

#print axioms native_floor_two_product
#print axioms native_matching_first_hit_deadline

end Collatz.FullProof.Deadline

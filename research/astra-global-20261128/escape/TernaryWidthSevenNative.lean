import CoreBranching
import Mathlib.Data.Nat.Log
import Mathlib.Tactic.Ring

/-! A concrete sharp width-seven price on every native shortcut step.
Each cut contributes the base-three level reached by the scaled integer
input. The nineteen cyclic cut comparisons control the effect of doubling
at once, including all low inputs and all leading-digit boundaries. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.TernaryWidthSevenNative

def lowCuts : List ℕ := [246, 261, 276, 293, 310, 329, 348, 369, 391, 414, 439, 465]

def highCuts : List ℕ := [493, 522, 553, 586, 621, 658, 697]

def cuts : List ℕ := lowCuts ++ highCuts

def level (c n : ℕ) : ℕ := Nat.log 3 (729 * n / c)

def levels (cs : List ℕ) (n : ℕ) : ℕ :=
  (cs.map (fun c => level c n)).sum

def score (n : ℕ) : ℕ := levels cuts n

private theorem levels_append (cs ds : List ℕ) (n : ℕ) :
    levels (cs ++ ds) n = levels cs n + levels ds n := by
  simp [levels]

private theorem level_shift (c d a : ℕ) (hc : 0 < c) (hd : 0 < d)
    (shift : 2 * c ≤ 3 ^ a * d) (n : ℕ) :
    level d (2 * n) ≤ level c n + a := by
  have upper : 729 * n < 3 ^ (level c n + 1) * c :=
    (Nat.div_lt_iff_lt_mul hc).mp (Nat.lt_pow_succ_log_self (by decide : 1 < 3) _)
  have h : 729 * (2 * n) < 3 ^ ((level c n + a) + 1) * d := by
    calc
      729 * (2 * n) = (729 * n) * 2 := by ring
      _ < (3 ^ (level c n + 1) * c) * 2 := Nat.mul_lt_mul_of_pos_right upper (by decide)
      _ = 3 ^ (level c n + 1) * (2 * c) := by ring
      _ ≤ 3 ^ (level c n + 1) * (3 ^ a * d) := Nat.mul_le_mul_left _ shift
      _ = 3 ^ ((level c n + a) + 1) * d := by
        rw [show level c n + a + 1 = (level c n + 1) + a by omega, pow_add]
        ring
  exact Nat.lt_succ_iff.mp (Nat.log_lt_of_lt_pow' (by omega) ((Nat.div_lt_iff_lt_mul hd).mpr h))

private theorem level_triple (c n : ℕ) (hc : 0 < c) (hbound : c ≤ 729)
    (hn : 0 < n) : level c n + 1 ≤ level c (3 * n) := by
  have hpos : 0 < 729 * n / c := Nat.div_pos (by omega) hc
  have lower : 3 ^ level c n * c ≤ 729 * n :=
    (Nat.le_div_iff_mul_le hc).mp (Nat.pow_log_le_self 3 hpos.ne')
  apply Nat.le_log_of_pow_le (by decide : 1 < 3)
  apply (Nat.le_div_iff_mul_le hc).mpr
  calc
    3 ^ (level c n + 1) * c = (3 ^ level c n * c) * 3 := by rw [pow_succ]; ring
    _ ≤ (729 * n) * 3 := Nat.mul_le_mul_right _ lower
    _ = 729 * (3 * n) := by ring

private def pairs : List (ℕ × ℕ × ℕ) :=
  cuts.zip ((highCuts ++ lowCuts).zip (List.replicate 7 0 ++ List.replicate 12 1))

private theorem reduce_pairs (ps : List (ℕ × ℕ × ℕ)) (n : ℕ)
    (hr : ∀ r ∈ ps, 0 < r.1 ∧ 0 < r.2.1 ∧ 2 * r.1 ≤ 3 ^ r.2.2 * r.2.1) :
    levels (ps.map (fun r => r.2.1)) (2*n) ≤
      levels (ps.map Prod.fst) n + (ps.map (fun r => r.2.2)).sum := by
  induction ps with
  | nil => simp [levels]
  | cons r rest ih =>
    obtain ⟨hc, hd, hs⟩ := hr r (by simp)
    have ht := ih (fun v hv => hr v (by simp [hv]))
    have hw := level_shift r.1 r.2.1 r.2.2 hc hd hs n
    simp only [List.map_cons, List.sum_cons] at *
    simp only [levels, List.map_cons, List.sum_cons] at *
    omega

theorem double_price (n : ℕ) : score (2 * n) ≤ score n + 12 := by
  have compatible : pairs.all (fun r => decide
      (0 < r.1 ∧ 0 < r.2.1 ∧ 2 * r.1 ≤ 3 ^ r.2.2 * r.2.1)) = true := by decide
  have h := reduce_pairs pairs n (fun r hr => of_decide_eq_true (List.all_eq_true.mp compatible r hr))
  have hleft : pairs.map (fun r => r.2.1) = highCuts ++ lowCuts := by decide
  have hright : pairs.map Prod.fst = cuts := by decide
  have hsum : (pairs.map (fun r => r.2.2)).sum = 12 := by decide
  rw [hleft, hright, hsum, levels_append] at h
  change levels cuts (2 * n) ≤ levels cuts n + 12
  rw [cuts, levels_append, Nat.add_comm (levels lowCuts (2 * n))]
  exact h

private theorem triple_levels (cs : List ℕ) (n : ℕ) (hn : 0 < n)
    (hs : ∀ c ∈ cs, 0 < c ∧ c ≤ 729) :
    levels cs n + cs.length ≤ levels cs (3*n) := by
  induction cs with
  | nil => simp [levels]
  | cons c rest ih =>
    obtain ⟨hp, hb⟩ := hs c (by simp)
    have ht := ih (fun v hv => hs v (by simp [hv]))
    have hw := level_triple c n hp hb hn
    simp only [levels, List.map_cons, List.sum_cons, List.length_cons] at *
    omega

theorem triple_gain (n : ℕ) (hn : 0 < n) : score n + 19 ≤ score (3 * n) := by
  have good : cuts.all (fun c => decide (0 < c ∧ c ≤ 729)) = true := by decide
  have h := triple_levels cuts n hn (fun c hc => of_decide_eq_true (List.all_eq_true.mp good c hc))
  rw [show cuts.length = 19 by decide] at h
  exact h

private theorem levels_mono (cs : List ℕ) {n m : ℕ} (h : n ≤ m) :
    levels cs n ≤ levels cs m := by
  induction cs with
  | nil => simp [levels]
  | cons c rest ih =>
    have hh : level c n ≤ level c m :=
      Nat.log_monotone (Nat.div_le_div_right (Nat.mul_le_mul_left 729 h))
    exact Nat.add_le_add hh ih

/-- A single nonincreasing real ranking is obtained by dividing the
negative of this integer score by nineteen. This verifies its sharp
parity price on the actual ordinary map at every positive integer. -/
theorem native_price (n : ℕ) (hn : 0 < n) :
    score n + 19 * (n % 2) ≤ 12 + score (CoreBranching.step n) := by
  by_cases he : n % 2 = 0
  · have hg : 2 * (n / 2) = n := by omega
    have h := double_price (n / 2)
    rw [hg] at h
    simp [CoreBranching.step, he]
    omega
  · have ho : n % 2 = 1 := by omega
    have hg : 2 * CoreBranching.step n = 3*n+1 := by
      simp [CoreBranching.step, he]
      omega
    have hu := triple_gain n hn
    have hm : score (3*n) ≤ score (2 * CoreBranching.step n) :=
      levels_mono cuts (by rw [hg]; omega)
    have hd := double_price (CoreBranching.step n)
    rw [ho]
    omega

end Collatz.TernaryWidthSevenNative

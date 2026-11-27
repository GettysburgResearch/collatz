import Mathlib.Data.Finset.Card
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! A census on indices of one injective finite path. Every low-grade site uses
its own actual common-clock image; at most k last sites lack such an image. -/

namespace Collatz.TraceCensus

/-- The actual shortcut state and its number of odd departures. -/
def advance (w : ℕ × ℕ) : ℕ × ℕ :=
  if w.1 % 2 = 0 then (w.1 / 2,w.2) else ((3*w.1+1)/2,w.2+1)

def run (x : ℕ) : ℕ → ℕ × ℕ
  | 0 => (x,0)
  | t+1 => advance (run x t)

/-- Clears all denominators in the physical image bound used by the census. -/
theorem image_envelope (x k : ℕ) :
    3 * 2^k * (run x k).1 ≤ 3^(run x k).2 * (3*x + 2^k) := by
  induction k with
  | zero => simp [run]
  | succ k ih =>
    obtain ⟨y,p,hr⟩ : ∃ y p, run x k = (y,p) := ⟨_,_,rfl⟩
    rw [hr] at ih
    simp only at ih
    have step : run x (k+1) = advance (y,p) := by simp [run,hr]
    rw [step]
    by_cases he : y % 2 = 0
    · simp only [advance, he, ite_true, Nat.pow_succ]
      calc
        3 * (2^k*2) * (y/2) = 3*2^k*(2*(y/2)) := by ring
        _ ≤ 3*2^k*y := Nat.mul_le_mul_left _ (by omega)
        _ ≤ 3^p*(3*x+2^k) := ih
        _ ≤ 3^p*(3*x+2^k*2) := Nat.mul_le_mul_left _ (by omega)
    · simp only [advance, he, ite_false, Nat.pow_succ]
      have positive : 1 ≤ 3^p := Nat.one_le_pow p 3 (by decide)
      have extra : 3*2^k ≤ 3^p*(3*2^k) := Nat.le_mul_of_pos_left _ positive
      calc
        3*(2^k*2)*((3*y+1)/2) = 3*2^k*(2*((3*y+1)/2)) := by ring
        _ ≤ 3*2^k*(3*y+1) := Nat.mul_le_mul_left _ (by omega)
        _ = 3*(3*2^k*y)+3*2^k := by ring
        _ ≤ 3*(3^p*(3*x+2^k))+3^p*(3*2^k) :=
          Nat.add_le_add (Nat.mul_le_mul_left 3 ih) extra
        _ = 3^p*3*(3*x+2^k*2) := by ring

theorem shifted_census (sites images : Finset ℕ) (state : ℕ → ℕ)
    (n k : ℕ) (low : ℕ → Prop) [DecidablePred low]
    (indices : ∀ i ∈ sites, i ≤ n)
    (simple : ∀ i j, i ≤ n → j ≤ n → state i = state j → i = j)
    (small : ∀ i ∈ sites, low i → i + k ≤ n → state (i + k) ∈ images) :
    sites.card ≤ images.card + k + (sites.filter fun i => ¬low i).card := by
  classical
  let A := sites.filter fun i => low i ∧ i + k ≤ n
  let B := sites.filter fun i => n < i + k
  let C := sites.filter fun i => ¬low i
  have hA : A.card ≤ images.card := by
    apply Finset.card_le_card_of_injOn (fun i => state (i + k))
    · intro i hi
      obtain ⟨hit, good, time⟩ := Finset.mem_filter.mp hi
      exact small i hit good time
    · intro i hi j hj eq
      have hi' := (Finset.mem_filter.mp hi).2.2
      have hj' := (Finset.mem_filter.mp hj).2.2
      have e := simple (i+k) (j+k) hi' hj' eq
      omega
  have hB : B.card ≤ k := by
    rw [← Finset.card_range k]
    apply Finset.card_le_card_of_injOn (fun i => n - i)
    · intro i hi
      obtain ⟨hit, time⟩ := Finset.mem_filter.mp hi
      have bound := indices i hit
      apply Finset.mem_range.mpr
      change n - i < k
      omega
    · intro i hi j hj eq
      have hi' := indices i (Finset.mem_filter.mp hi).1
      have hj' := indices j (Finset.mem_filter.mp hj).1
      change n - i = n - j at eq
      omega
  have cover : sites ⊆ (A ∪ B) ∪ C := by
    intro i hi
    simp only [A, B, C, Finset.mem_union, Finset.mem_filter, hi, true_and]
    by_cases h : low i
    · by_cases t : i + k ≤ n
      · exact Or.inl (Or.inl ⟨h,t⟩)
      · exact Or.inl (Or.inr (by omega))
    · exact Or.inr h
  have card := Finset.card_le_card cover
  have hab := Finset.card_union_le A B
  have habc := Finset.card_union_le (A ∪ B) C
  change sites.card ≤ images.card + k + C.card
  omega

/-- Product of the one-step residuals, with chronological ordinary losses. -/
def residual : List ℚ → ℚ
  | [] => 1
  | a :: tail => (1-a)*residual tail

theorem residual_bounds (l : List ℚ) (legal : ∀ a ∈ l, 0 ≤ a ∧ a ≤ 1) :
    0 ≤ residual l ∧ residual l ≤ 1 ∧ 1 - residual l ≤ l.sum := by
  induction l with
  | nil => norm_num [residual]
  | cons a l ih =>
    obtain ⟨ha, ha'⟩ := legal a (.head _)
    obtain ⟨hr, hr', loss⟩ := ih (fun y hy => legal y (.tail _ hy))
    simp only [residual, List.sum_cons]
    refine ⟨mul_nonneg (by linarith) hr, ?_, ?_⟩
    · nlinarith [mul_nonneg ha hr]
    · nlinarith [mul_nonneg ha (sub_nonneg.mpr hr')]

theorem fifth_cutoff (l : List ℚ) (legal : ∀ a ∈ l, 0 ≤ a ∧ a ≤ 1)
    (budget : l.sum < 1/5) : 4/5 < residual l := by
  have h := (residual_bounds l legal).2.2
  linarith

theorem log_threshold_arithmetic :
    (593690 : ℚ)/(3 * 10^6) < 9/50 + (9/50)^2/2 + (9/50)^3/3 := by norm_num

theorem record_height_bits : 494114680693632162318569565806744468898092 < 2^139 := by decide

#print axioms image_envelope
#print axioms shifted_census
#print axioms log_threshold_arithmetic
#print axioms record_height_bits
#print axioms residual_bounds
#print axioms fifth_cutoff

end Collatz.TraceCensus

module

public import PassageAligned
import all PassageAligned
import all PassageClassification
import all PassageRouting
import all TowerFrontierAffine
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageAligned

open TowerFrontier PassageRouting
set_option autoImplicit false

private theorem first_step_count (h x : ℕ) : odds (h+1) x=odds h (step x)+x%2 := by
  unfold odds
  rw [track]
  split <;> rename_i e
  · simp [step,e]
  · have o : x%2=1 := by omega
    rw [tracked]; simp [step,o,odds]

private theorem halving_count (h b : ℕ) : odds h (2^h*b)=0 := by
  induction h with
  | zero => rfl
  | succ h ih =>
    rw [first_step_count,pow_succ,Nat.mul_right_comm,
      show (2^h*b*2)%2=0 by omega]
    simpa [step] using ih

private theorem suffix_clock {u H x b t : ℕ} (first : FirstLow H x 1) (uh : u≤H)
    (hit : run u x=b) (tail : FirstLow t b 1) : u+t=H := by
  by_contra ne
  rcases lt_or_gt_of_ne ne with early | late
  · have bad := first.2 (u+t) early
    rw [run_add,hit,tail.1] at bad
    omega
  · have bad := tail.2 (H-u) (by omega)
    have reach := first.1
    rw [show H=u+(H-u) by omega,run_add,hit] at reach
    omega

private theorem seven_cost (h x : ℕ) (floor : ∀ i<h, (run i x)%2≠0 → 7≤run i x) :
    2^h*7^(odds h x)*run h x≤x*22^(odds h x) := by
  induction h generalizing x with
  | zero => simp [odds,track,run]
  | succ h ih =>
    have next := ih (step x) (fun i hi => floor (i+1) (by omega))
    rw [first_step_count,pow_succ 2 h,run]
    by_cases e : x%2=0
    · rw [e,Nat.add_zero]
      have rule : 2*step x=x := by rw [step,if_pos e]; omega
      calc
        _ = 2*(2^h*7^(odds h (step x))*run h (step x)) := by ring
        _ ≤ 2*(step x*22^(odds h (step x))) := Nat.mul_le_mul_left 2 next
        _ = _ := by rw [←Nat.mul_assoc,rule]
    · have odd : x%2=1 := by omega
      have small := floor 0 (by omega) e
      change 7≤x at small
      have rule : 14*step x≤22*x := by rw [step,if_neg e]; omega
      rw [odd,pow_succ,pow_succ]
      calc
        _ = 14*(2^h*7^(odds h (step x))*run h (step x)) := by ring
        _ ≤ 14*(step x*22^(odds h (step x))) := Nat.mul_le_mul_left _ next
        _ ≤ _ := by
          rw [←Nat.mul_assoc,show x*(22^(odds h (step x))*22)=(22*x)*22^(odds h (step x)) by ring]
          exact Nat.mul_le_mul_right _ rule

/-- The third odd departure is impossible. Its forced visit to five would
require two earlier odd inputs of size at least seven, already too costly. -/
theorem root_two_odds {j x : ℕ} (upper : x<2^(j+1))
    (aligned : ∃ h, track (j+h) x 0=track h 1 0) :
    ∃ H, FirstLow H x 1 ∧ H=j+2*odds H x ∧ odds H x≤2 := by
  obtain ⟨H,first,time,small⟩ := root_profile_barrier upper aligned
  refine ⟨H,first,time,?_⟩
  by_contra! large
  have three : odds H x=3 := by omega
  have len : H=j+6 := by omega
  obtain ⟨five,two⟩ := three_visits_five first len three upper
  have floor (i : ℕ) (ih : i<j+2) (odd : run i x%2≠0) : 7≤run i x := by
    have positive := first.2 i (by omega)
    have n5 : run i x≠5 := by
      intro h5
      have endTime := suffix_clock first (by omega) h5
        (show FirstLow 4 5 1 by unfold FirstLow; decide)
      omega
    have n3 : run i x≠3 := by
      intro h3
      have endTime := suffix_clock first (by omega) h3
        (show FirstLow 5 3 1 by unfold FirstLow; decide)
      have source := PassageClassification.unique_ancestor i x 3 (by decide) h3
      have c0 : odds i x=0 := source ▸ halving_count i 3
      have c3 : odds 5 3=2 := by decide
      rw [←endTime,extend,h3,c0,c3] at three
      contradiction
    omega
  have bound := seven_cost (j+2) x floor
  rw [five,two,pow_add 2 j 2] at bound
  have strict := bound.trans_lt (Nat.mul_lt_mul_of_pos_right upper (by decide : 0<22^2))
  rw [pow_succ (2:ℕ) j] at strict
  simp only [Nat.mul_assoc] at strict
  have impossible := Nat.lt_of_mul_lt_mul_left strict
  norm_num at impossible

/-- Three candidate reference clocks decide every aligned root comparison. -/
theorem three_clocks {j x : ℕ} (upper : x<2^(j+1)) :
    (∃ h, track (j+h) x 0=track h 1 0) ↔ ∃ q≤2, track (j+2*q) x 0=(1,q) := by
  constructor
  · intro aligned
    obtain ⟨H,hit,bal,bound⟩ := root_two_odds upper aligned
    exact ⟨odds H x,bound,by rw [←bal,tracked,hit.1,Nat.add_zero]⟩
  · rintro ⟨q,cap,hit⟩
    exact (four_clocks upper).mpr ⟨q,by omega,hit⟩

theorem quadratic_cover (j : ℕ) : ∃ xs : List ℕ,
    xs.length≤1+(j+2)+(j+4).choose 2 ∧
    ∀ x<2^(j+1), (∃ h, track (j+h) x 0=track h 1 0) → x∈xs := by
  let row := fun q => inverseGrade (j+2*q) q 1
  refine ⟨row 0++row 1++row 2,?_,?_⟩
  · simp only [List.length_append]
    exact Nat.add_le_add (Nat.add_le_add (by simpa [row] using inverse_size j 0 1)
      (by simpa [row] using inverse_size (j+2) 1 1)) (inverse_size (j+4) 2 1)
  · intro x upper aligned
    obtain ⟨q,small,hit⟩ := (three_clocks upper).mp aligned
    rw [tracked,Nat.add_zero,Prod.mk.injEq] at hit
    have mem := inverse_mem (j+2*q) x
    rw [hit.1,hit.2] at mem
    change x∈row q at mem
    simp only [List.mem_append]
    interval_cases q <;> tauto

#print axioms root_two_odds
#print axioms three_clocks
#print axioms quadratic_cover
end Collatz.Itinerary.PassageAligned

import Mathlib.Data.Int.ConditionallyCompleteOrder
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Linarith

/-! Integer-valued Pliss selection on an entire future, with a prefix count.
Scaling a rational gap budget by its denominator gives such an integer path.
The statistical representation and the entropy dichotomy are written proofs. -/
namespace EscapePermanentSieve

def tailSet (B : ℕ → ℤ) (i : ℕ) : Set ℤ := {v | ∃ j ≥ i, B j = v}

noncomputable def floorAt (B : ℕ → ℤ) (i : ℕ) : ℤ := sInf (tailSet B i)

def permanent (B : ℕ → ℤ) (i : ℕ) : Prop := ∀ j ≥ i, B i ≤ B j

theorem tail_floor (B : ℕ → ℤ) (l : ℤ) (hl : ∀ j, l ≤ B j) (i : ℕ) :
    (∃ j ≥ i, B j = floorAt B i) ∧ ∀ j ≥ i, floorAt B i ≤ B j := by
  have hne : (tailSet B i).Nonempty := ⟨B i, i, le_rfl, rfl⟩
  have hbd : BddBelow (tailSet B i) := by
    refine ⟨l, ?_⟩
    rintro _ ⟨j, _, rfl⟩
    exact hl j
  exact ⟨Int.csInf_mem hne hbd,
    fun j hj => csInf_le hbd (show B j ∈ tailSet B i from ⟨j,hj,rfl⟩)⟩

theorem floor_rise (B : ℕ → ℤ) (l v : ℤ) (hl : ∀ j, l ≤ B j)
    (hinc : ∀ j, B (j+1) ≤ B j + v) (i : ℕ) :
    floorAt B (i+1) - floorAt B i ≤
      (if @decide (permanent B i) (Classical.propDecidable _) then v else 0) := by
  classical
  obtain ⟨⟨j,hij,hj⟩,hlo⟩ := tail_floor B l hl i
  obtain ⟨_,hnext⟩ := tail_floor B l hl (i+1)
  by_cases hp : permanent B i
  · have heq : B i = floorAt B i := le_antisymm (hj ▸ hp j hij) (hlo i le_rfl)
    have h := hnext (i+1) le_rfl
    have h' := hinc i
    simp [hp]
    omega
  · have hji : i+1 ≤ j := by
      by_contra! hn
      have hEq : j=i := by omega
      subst j
      exact hp (fun k hk => hj ▸ hlo k hk)
    have h := hnext j hji
    simp [hp]
    omega

noncomputable def permanentCount (B : ℕ → ℤ) (n : ℕ) : ℤ :=
  ∑ i ∈ Finset.range n, (if @decide (permanent B i) (Classical.propDecidable _) then 1 else 0)

theorem whole_future_count (B : ℕ → ℤ) (l v : ℤ) (hl : ∀ j, l ≤ B j)
    (hinc : ∀ j, B (j+1) ≤ B j + v) (n : ℕ) :
    floorAt B n - floorAt B 0 ≤ v * permanentCount B n := by
  classical
  induction n with
  | zero => simp [permanentCount]
  | succ n ih =>
    have h := floor_rise B l v hl hinc n
    unfold permanentCount at *
    rw [Finset.sum_range_succ, mul_add]
    by_cases hp : permanent B n <;> simp [hp] at h ih ⊢ <;> omega

theorem affine_lower_count (B : ℕ → ℤ) (l v growth c : ℤ)
    (hl : ∀ j, l ≤ B j) (hg : 0 ≤ growth)
    (hinc : ∀ j, B (j+1) ≤ B j + v) (htrend : ∀ j : ℕ, growth * j - c ≤ B j)
    (n : ℕ) : growth * n - c - floorAt B 0 ≤ v * permanentCount B n := by
  obtain ⟨⟨j,hnj,heq⟩,_⟩ := tail_floor B l hl n
  have hle : growth * (n:ℤ) ≤ growth * (j:ℤ) :=
    mul_le_mul_of_nonneg_left (by exact_mod_cast hnj) hg
  have h := htrend j
  have hcount := whole_future_count B l v hl hinc n
  omega

#print axioms tail_floor
#print axioms floor_rise
#print axioms whole_future_count
#print axioms affine_lower_count
end EscapePermanentSieve

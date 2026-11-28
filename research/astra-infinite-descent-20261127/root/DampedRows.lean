import TargetExtinction

/-! Reciprocal damping gives an elementary uniform source tail. Vanishing
of damped complete first-arrival rows with grade is equivalent to boundedness.
Neither side of that universal equivalence is asserted here. -/
set_option autoImplicit false
set_option warningAsError true

namespace DampedRows
open Finset CoreBranching PeakRigidity FairGrid ReciprocalTrace ActualPacking TargetExtinction

theorem mass_le_one {m d y : ℕ} (yp : 0<y) (A : Finset ℕ)
    (actual : ∀z∈A, 0<z ∧ run m z=y ∧ grade m z=d) :
    weight m d y*A.card≤1 := by
  have wp : 0≤weight m d y := by unfold weight; positivity
  by_cases ne : A.Nonempty
  · obtain ⟨v,hv⟩ := ne
    obtain ⟨vp,hit,gr⟩ := actual v hv
    have v1 : (1:ℝ)≤v := by exact_mod_cast vp
    have small : weight m d y≤1 :=
      (le_mul_of_one_le_right wp v1).trans (mark_le_one yp hit gr)
    have bound := interval_count A wp small (fun z hz => by
      obtain ⟨zp,zh,zg⟩ := actual z hz
      have z1 : (1:ℝ)≤z := by exact_mod_cast zp
      exact ⟨le_mul_of_one_le_right wp z1,mark_le_one yp zh zg⟩)
    linarith
  · simp only [not_nonempty_iff_eq_empty.mp ne,card_empty,Nat.cast_zero,mul_zero]
    norm_num

theorem damped_bound {m d y : ℕ} (yp : 0<y) (A : Finset ℕ)
    (actual : ∀z∈A, 0<z ∧ run m z=y ∧ grade m z=d)
    (φ : ℕ → ℝ) (B : ℝ) (bp : 0≤B) (cap : ∀z∈A, φ z≤B) :
    weight m d y*(∑z∈A,φ z)≤B := by
  have wp : 0≤weight m d y := by unfold weight; positivity
  have sum : (∑z∈A,φ z)≤A.card*B := by
    calc
      _ ≤ ∑_z∈A,B := sum_le_sum cap
      _ = _ := by simp
  have old := mass_le_one yp A actual
  calc
    _ ≤ weight m d y*(A.card*B) := mul_le_mul_of_nonneg_left sum wp
    _ = (weight m d y*A.card)*B := by ring
    _ ≤ 1*B := mul_le_mul_of_nonneg_right old bp
    _ = _ := one_mul B

theorem reciprocal_tail {m d y R : ℕ} (yp : 0<y) (A : Finset ℕ)
    (actual : ∀z∈A, 0<z ∧ run m z=y ∧ grade m z=d)
    (large : ∀z∈A, R<z) :
    weight m d y*(∑z∈A,1/(z:ℝ))≤1/((R:ℝ)+1) := by
  apply damped_bound yp A actual (fun z => 1/(z:ℝ)) (1/((R:ℝ)+1)) (by positivity)
  intro z hz
  have order : (R:ℝ)+1≤z := by exact_mod_cast (large z hz)
  exact one_div_le_one_div_of_le (by positivity) order

private theorem grade_le (m z : ℕ) : grade m z≤m := by
  induction m with
  | zero => simp [grade]
  | succ m ih =>
    have rem := Nat.mod_lt (run m z) (by decide : 0<2)
    simp only [grade]
    omega

theorem first_clock_le {m z y B : ℕ} (zp : 0<z) (hit : run m z=y)
    (first : ∀j<m, run j z≠y) (bounded : ∀j, run j z≤B) : m+1≤B := by
  have simple := first_simple hit first
  have count : ((range (m+1)).image (fun i => run i z)).card=m+1 := by
    rw [card_image_of_injOn]
    · exact card_range _
    · intro i hi j hj same
      exact simple i (by simpa using hi) j (by simpa using hj) same
  have sub : (range (m+1)).image (fun i => run i z)⊆Icc 1 B := by
    intro x hx
    obtain ⟨i,_,rfl⟩ := mem_image.mp hx
    exact mem_Icc.mpr ⟨run_pos i zp,bounded i⟩
  have bound := card_le_card sub
  simpa only [count,Nat.card_Icc,Nat.add_sub_cancel] using bound

private theorem finite_bounds (bounded : AllBounded) (R : ℕ) :
    ∃B : ℕ, ∀z : ℕ, 0<z → z≤R → ∀m, run m z≤B := by
  classical
  have bounds (i : ℕ) := bounded (i+1) (by omega)
  choose bound spec using bounds
  refine ⟨∑i∈range R,bound i,?_⟩
  intro z zp zr m
  obtain ⟨i,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt zp)
  exact (spec i m).trans (single_le_sum (fun _ _ => Nat.zero_le _)
    (mem_range.mpr (by omega)))

def GradeVanishing : Prop :=
  ∀ε : ℝ, 0<ε → ∃D : ℕ, ∀d : ℕ, D≤d → ∀m y : ℕ, 0<y → ∀A : Finset ℕ,
    (∀z∈A, 0<z ∧ run m z=y ∧ grade m z=d ∧ ∀j<m, run j z≠y) →
    weight m d y*(∑z∈A,1/(z:ℝ))<ε

theorem vanishing_of_bounded (bounded : AllBounded) : GradeVanishing := by
  intro ε ep
  obtain ⟨R,rLarge⟩ := exists_nat_gt (1/ε)
  have target : 1/((R:ℝ)+1)<ε := by
    apply (div_lt_iff₀ (by positivity : 0<(R:ℝ)+1)).mpr
    have old := (div_lt_iff₀ ep).mp rLarge
    nlinarith only [old,ep]
  obtain ⟨B,bound⟩ := finite_bounds bounded R
  refine ⟨B+1,?_⟩
  intro d high m y yp A actual
  have smallRow : ∀z∈A, 0<z ∧ run m z=y ∧ grade m z=d := by
    intro z hz
    obtain ⟨zp,hit,gr,_⟩ := actual z hz
    exact ⟨zp,hit,gr⟩
  have large : ∀z∈A, R<z := by
    intro z hz
    obtain ⟨zp,hit,gr,first⟩ := actual z hz
    by_contra! low
    have clock := first_clock_le zp hit first (bound z zp low)
    have count := grade_le m z
    omega
  exact (reciprocal_tail yp A smallRow large).trans_lt target

private theorem height (m z : ℕ) : run m z<3^(grade m z)*(z+1) := by
  have h := (PeakRigidity.shifted m z).1
  have pow : (3/2:ℚ)^(grade m z)≤3^(grade m z) :=
    pow_le_pow_left₀ (by norm_num) (by norm_num) _
  have both := h.trans (mul_le_mul_of_nonneg_right pow (by positivity : 0≤(z:ℚ)+1))
  have cast : run m z+1≤3^(grade m z)*(z+1) := by exact_mod_cast both
  omega

theorem bounded_of_vanishing (vanishing : GradeVanishing) : AllBounded := by
  intro z zp
  let ε := Real.exp (-262144)/(z:ℝ)/(z:ℝ)
  have zr : 0<(z:ℝ) := by exact_mod_cast zp
  have ep : 0<ε := by dsimp [ε]; positivity
  obtain ⟨D,small⟩ := vanishing ε ep
  refine ⟨3^D*(z+1),?_⟩
  intro t
  let y := run t z
  have yp : 0<y := run_pos t zp
  have reach : ∃j, run j z=y := ⟨t,rfl⟩
  let m := Nat.find reach
  have hit : run m z=y := Nat.find_spec reach
  have earlier : ∀j<m, run j z≠y := by
    intro j less same
    exact (Nat.not_lt_of_ge (Nat.find_min' reach same)) less
  have gradeBound : grade m z<D := by
    by_contra! high
    have actual : ∀x∈({z}:Finset ℕ),
        0<x ∧ run m x=y ∧ grade m x=grade m z ∧ ∀j<m, run j x≠y := by
      intro x hx
      rw [mem_singleton] at hx
      subst x
      exact ⟨zp,hit,rfl,earlier⟩
    have tiny := small (grade m z) high m y yp {z} actual
    simp only [sum_singleton,mul_one_div] at tiny
    have first : weight m (grade m z) y < Real.exp (-262144)/(z:ℝ) :=
      (div_lt_div_iff_of_pos_right zr).mp tiny
    have tooSmall := (lt_div_iff₀ zr).mp first
    have floor := first_floor zp hit rfl earlier
    linarith
  have h := height m z
  rw [hit] at h
  exact h.le.trans (Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) gradeBound.le))

theorem bounded_iff_grade_vanishing : AllBounded ↔ GradeVanishing :=
  ⟨vanishing_of_bounded,bounded_of_vanishing⟩

/-- The same criterion uses only complete, computably enumerated finite rows. -/
theorem bounded_iff_complete_damped : AllBounded ↔
    ∀ε : ℝ, 0<ε → ∃D : ℕ, ∀d : ℕ, D≤d → ∀m y : ℕ, 0<y →
      weight m d y*(∑z∈completeRow m d y,1/(z:ℝ))<ε := by
  rw [bounded_iff_grade_vanishing]
  constructor
  · intro all ε ep
    obtain ⟨D,small⟩ := all ε ep
    refine ⟨D,?_⟩
    intro d high m y yp
    exact small d high m y yp (completeRow m d y) (fun _ hz => mem_completeRow.mp hz)
  · intro all ε ep
    obtain ⟨D,small⟩ := all ε ep
    refine ⟨D,?_⟩
    intro d high m y yp A actual
    have sub : A⊆completeRow m d y := fun z hz => mem_completeRow.mpr (actual z hz)
    have sum : (∑z∈A,1/(z:ℝ))≤∑z∈completeRow m d y,1/(z:ℝ) :=
      sum_le_sum_of_subset_of_nonneg sub (fun _ _ _ => by positivity)
    have wp : 0≤weight m d y := by unfold weight; positivity
    exact (mul_le_mul_of_nonneg_left sum wp).trans_lt (small d high m y yp)

#print axioms mass_le_one
#print axioms damped_bound
#print axioms reciprocal_tail
#print axioms first_clock_le
#print axioms bounded_iff_grade_vanishing
#print axioms bounded_iff_complete_damped
end DampedRows

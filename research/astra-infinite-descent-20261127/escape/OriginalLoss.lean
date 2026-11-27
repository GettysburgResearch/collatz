import FirstHitFlux
import ReciprocalTrace

/-! The true 3^grade/2^clock weight at every ordinary odd departure,
including all recurrent visits. Multiplication by 1/(3*y+1) turns its
source-scaled weight into an exact loss of the affine mark. -/
set_option autoImplicit false
set_option warningAsError true
namespace OriginalLoss
open CoreBranching PeakRigidity FairGrid ReciprocalTrace FirstHitFlux FiniteExtinction

noncomputable def mark (m x : ℕ) : ℝ := weight m (grade m x) (run m x)*x
noncomputable def loss (m x : ℕ) : ℝ :=
  if run m x%2=1 then weight m (grade m x) (run m x)/(3*(run m x:ℝ)+1) else 0

private theorem ratio (v : ℕ) (P : 0<v) :
    (3:ℝ)^(v%2)*v/(2*(step v:ℝ))=
      if v%2=1 then (3*(v:ℝ))/(3*v+1) else 1 := by
  rcases Nat.mod_two_eq_zero_or_one v with e|o
  · have sv : 2*step v=v := by unfold step; simp only [e,ite_true]; omega
    have real : (2:ℝ)*step v=v := by exact_mod_cast sv
    simp [e,real,Nat.ne_of_gt P]
  · have sv : 2*step v=3*v+1 := by unfold step; simp only [o,reduceCtorEq,ite_false]; omega
    have real : (2:ℝ)*step v=3*v+1 := by exact_mod_cast sv
    simp [o,real]

private theorem evolve (m x : ℕ) (xp : 0<x) :
    mark (m+1) x=mark m x*((3:ℝ)^(run m x%2)*run m x/(2*step (run m x))) := by
  have vp:=run_pos m xp
  have sp:=step_pos vp
  have last : run (m+1) x=step (run m x) := by simpa [run] using run_add m 1 x
  unfold mark weight
  rw [last,grade,pow_add,pow_succ]
  field_simp

theorem one_step (m x : ℕ) (xp : 0<x) :
    mark m x=(x:ℝ)*loss m x+mark (m+1) x := by
  have vp:=run_pos m xp
  rw [evolve m x xp,ratio _ vp]
  unfold loss
  by_cases o : run m x%2=1
  · simp only [o,ite_true]
    unfold mark
    have den : (3*(run m x:ℝ)+1)≠0 := by positivity
    field_simp
    ring
  · simp [o]

private theorem loss_nonneg (m x : ℕ) : 0≤loss m x := by
  unfold loss weight
  split <;> positivity

private theorem mark_nonneg (m x : ℕ) : 0≤mark m x := by unfold mark weight; positivity

/-- Total selected measure along every finite ordinary segment is at most
one after scaling by its actual start. No uniqueness or no-return premise. -/
theorem telescope (H x : ℕ) (xp : 0<x) :
    (x:ℝ)*(∑m ∈ Finset.range H,loss m x)+mark H x=1 := by
  induction H with
  | zero => simp [mark,weight,grade,run,Nat.ne_of_gt xp]
  | succ H ih => rw [Finset.sum_range_succ,mul_add,add_assoc,←one_step H x xp,ih]

/-- Once the normalized endpoint mark enters [0,t], all the subsequent
weighted losses together cost at most t, uniformly through any finite clock. -/
theorem endpoint_band (H x : ℕ) (xp : 0<x) (t : ℝ) (tp : 0≤t) :
    (x:ℝ)*(∑m ∈ Finset.range H, if mark m x≤t then loss m x else 0)≤t := by
  have each (m : ℕ) : (x:ℝ)*(if mark m x≤t then loss m x else 0) ≤
      min t (mark m x)-min t (mark (m+1) x) := by
    have id:=one_step m x xp
    have lp:=loss_nonneg m x
    have xa : (0:ℝ)≤x := by positivity
    have down : mark (m+1) x≤mark m x := by nlinarith only [id,mul_nonneg xa lp]
    by_cases small : mark m x≤t
    · rw [ite_eq_left small,min_eq_right small,min_eq_right (down.trans small)]
      linarith
    · rw [ite_eq_right small,mul_zero]
      exact sub_nonneg.mpr (min_le_min_left t down)
  have all : (x:ℝ)*(∑m ∈ Finset.range H, if mark m x≤t then loss m x else 0) ≤
      min t (mark 0 x)-min t (mark H x) := by
    induction H with
    | zero => simp
    | succ H ih =>
      rw [Finset.sum_range_succ,mul_add]
      linarith only [ih,each H]
  exact all.trans ((sub_le_self _ (le_min tp (mark_nonneg H x))).trans (min_le_left _ _))

/-- The exact normalized losses at every paired physical clock of a counted
merged tail. Repeated vertices and both parities are retained. -/
theorem tail_scale {s L x y : ℕ} (meet : Merge s L x y) (e : ℕ) :
    (2:ℝ)^s * loss (L+s+e) x=3*loss (L+e) y := by
  obtain ⟨same,counts⟩:=meet
  have st : run (L+s+e) x=run (L+e) y := by rw [run_add (L+s) e x,run_add L e y,same]
  have gr : grade (L+s+e) x=grade (L+e) y+1 := by
    rw [grade_add (L+s) e x,grade_add L e y,counts,same]
    omega
  unfold loss
  rw [st,gr]
  by_cases odd : run (L+e) y%2=1
  · simp only [odd,ite_true]
    unfold weight
    rw [show L+s+e=L+e+s by omega,pow_add (2:ℝ),pow_succ (3:ℝ)]
    by_cases state : run (L+e) y=0
    · simp [state]
    · have nz : ((run (L+e) y:ℕ):ℝ)≠0 := by exact_mod_cast state
      field_simp
  · simp [odd]

#print axioms one_step
#print axioms telescope
#print axioms endpoint_band
#print axioms tail_scale
end OriginalLoss

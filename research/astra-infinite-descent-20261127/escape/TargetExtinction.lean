import ActualPacking
import Mathlib.Algebra.Order.Archimedean.Basic

/-! The fair exact-clock first-arrival row criterion for boundedness of every
ordinary positive orbit, using only the finite packing, correction and grid lemmas. -/
set_option autoImplicit false
set_option warningAsError true

namespace TargetExtinction
open CoreBranching PeakRigidity FairGrid ReciprocalPacking ReciprocalTrace ActualPacking

/-- Every positive shortcut orbit is bounded in ordinary height. -/
def AllBounded : Prop := ∀z : ℕ, 0<z → ∃B : ℕ, ∀m : ℕ, run m z≤B

/-- Every finite subset of the given exact first-arrival row has small fair
weight at all sufficiently high positive odd targets, uniformly in time and grade. -/
def Vanishing : Prop :=
  ∀ ε : ℝ, 0<ε → ∃Y : ℕ, ∀y : ℕ, Y<y → y%2=1 → ∀m d : ℕ, ∀A : Finset ℕ,
    (∀z∈A, 0<z ∧ run m z=y ∧ grade m z=d ∧ ∀j<m, run j z≠y) →
    weight m d y*A.card<ε

private theorem finite_bounds (bounded : AllBounded) (H : ℕ) :
    ∃Y : ℕ, ∀q : ℕ, 0<q → q≤H → ∀k : ℕ, run k q≤Y := by
  classical
  have bounds (i : ℕ) := bounded (i+1) (by omega)
  choose bound spec using bounds
  refine ⟨∑i∈Finset.range H,bound i,?_⟩
  intro q qp qH k
  obtain ⟨i,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt qp)
  exact (spec i k).trans (Finset.single_le_sum (fun _ _ => Nat.zero_le _)
    (Finset.mem_range.mpr (by omega)))

theorem vanishing_of_bounded (bounded : AllBounded) : Vanishing := by
  intro ε ep
  obtain ⟨K,hK⟩ := exists_pow_lt_of_lt_one (show 0<ε/262145 by positivity)
    (show ratio<1 by norm_num [ratio])
  obtain ⟨Y,cut⟩ := finite_bounds bounded (8192^K)
  refine ⟨Y,?_⟩
  intro y large _ m d A actual
  have yp : 0<y := Nat.zero_lt_of_lt large
  have above (z : ℕ) (hz : z∈A) (j : ℕ) (jm : j≤m) : 8192^K≤run j z := by
    by_contra! small
    obtain ⟨zp,hit,_,_⟩ := actual z hz
    have tail : run (m-j) (run j z)=y := by
      rw [←run_add,show j+(m-j)=m by omega,hit]
    have same := cut (run j z) (run_pos j zp) small.le (m-j)
    rw [tail] at same
    omega
  have row := row_bound yp A K actual above
  exact row.trans_lt (by linarith)

private theorem bounded_of_odd_bound (z B : ℕ)
    (odd : ∀m : ℕ, run m z%2=1 → run m z≤B) :
    ∀m : ℕ, run m z≤max z (3*B+1) := by
  intro m
  induction m with
  | zero => exact le_max_left _ _
  | succ m ih =>
    have last : run (m+1) z=step (run m z) := by simpa [run] using run_add m 1 z
    rw [last]
    rcases Nat.mod_two_eq_zero_or_one (run m z) with he|ho
    · simp only [step,he,ite_true]
      exact (Nat.div_le_self _ _).trans ih
    · have bound := odd m ho
      have no : run m z%2≠0 := by omega
      simp only [step,no,ite_false]
      exact (Nat.div_le_self _ _).trans ((by omega : 3*run m z+1≤3*B+1).trans (le_max_right _ _))

theorem bounded_of_vanishing (vanishing : Vanishing) : AllBounded := by
  intro z zp
  let ε := Real.exp (-262144)/(z:ℝ)
  have ep : 0<ε := by dsimp [ε]; positivity
  obtain ⟨Y,small⟩ := vanishing ε ep
  refine ⟨max z (3*Y+1), bounded_of_odd_bound z Y ?_⟩
  intro t odd
  by_contra! large
  let y := run t z
  have reach : ∃j : ℕ, run j z=y := ⟨t,rfl⟩
  let m := Nat.find reach
  have hit : run m z=y := Nat.find_spec reach
  have earlier : ∀j<m, run j z≠y := by
    intro j less same
    exact (Nat.not_lt_of_ge (Nat.find_min' reach same)) less
  let d := grade m z
  have subset : ∀x∈({z}:Finset ℕ), 0<x ∧ run m x=y ∧ grade m x=d ∧ ∀j<m, run j x≠y := by
    intro x hx
    rw [Finset.mem_singleton] at hx
    subst x
    exact ⟨zp,hit,rfl,earlier⟩
  have one := small y large odd m d {z} subset
  simp only [Finset.card_singleton,Nat.cast_one,mul_one] at one
  have floor := first_floor zp hit (show grade m z=d from rfl) earlier
  have value : weight m d y*(z:ℝ)<Real.exp (-262144) := (lt_div_iff₀ (by positivity)).mp one
  linarith

/-- An unconditional critical fair-row criterion. The finite witnesses use the
actual ordinary map, positive starts, first visits and their exact two clocks. -/
theorem bounded_iff_vanishing : AllBounded ↔ Vanishing :=
  ⟨vanishing_of_bounded,bounded_of_vanishing⟩

/-- The complete row is a finite computable set, with an explicit source
ceiling obtained from the affine formula and a bounded first-visit test. -/
def completeRow (m d y : ℕ) : Finset ℕ :=
  (Finset.range (2^m*y+1)).filter (fun z =>
    0<z ∧ run m z=y ∧ grade m z=d ∧ ∀j : Fin m, run j.val z≠y)

theorem mem_completeRow {m d y z : ℕ} : z∈completeRow m d y ↔
    0<z ∧ run m z=y ∧ grade m z=d ∧ ∀j<m, run j z≠y := by
  simp only [completeRow,Finset.mem_filter,Finset.mem_range]
  constructor
  · rintro ⟨_,zp,hit,gr,first⟩
    exact ⟨zp,hit,gr,fun j hj => first ⟨j,hj⟩⟩
  · rintro ⟨zp,hit,gr,first⟩
    have eqn := AsynchronousGuard.affine m z
    rw [hit,gr] at eqn
    have base : z≤3^d*z := Nat.le_mul_of_pos_left _ (by positivity)
    exact ⟨by omega,zp,hit,gr,fun j => first j j.isLt⟩

/-- Direct form with the cardinality of the complete finite ordinary row. -/
theorem bounded_iff_complete_rows : AllBounded ↔
    ∀ε : ℝ, 0<ε → ∃Y : ℕ, ∀y : ℕ, Y<y → y%2=1 → ∀m d : ℕ,
      weight m d y*(completeRow m d y).card<ε := by
  rw [bounded_iff_vanishing]
  constructor
  · intro all ε ep
    obtain ⟨Y,small⟩ := all ε ep
    refine ⟨Y,?_⟩
    intro y high odd m d
    exact small y high odd m d (completeRow m d y) (fun _ hz => mem_completeRow.mp hz)
  · intro all ε ep
    obtain ⟨Y,small⟩ := all ε ep
    refine ⟨Y,?_⟩
    intro y high odd m d A actual
    have sub : A⊆completeRow m d y := fun z hz => mem_completeRow.mpr (actual z hz)
    have count : (A.card:ℝ)≤(completeRow m d y).card := by
      exact_mod_cast Finset.card_le_card sub
    have wp : 0≤weight m d y := by unfold weight; positivity
    exact (mul_le_mul_of_nonneg_left count wp).trans_lt (small y high odd m d)

#print axioms mem_completeRow
#print axioms bounded_iff_complete_rows

#print axioms vanishing_of_bounded
#print axioms bounded_of_vanishing
#print axioms bounded_iff_vanishing
end TargetExtinction


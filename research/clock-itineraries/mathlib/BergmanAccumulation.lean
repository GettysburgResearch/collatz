module

public import BergmanSpectrum
import all BergmanRelative
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.BergmanRelative

set_option autoImplicit false

/-- An ordinary defect row exists arbitrarily high and arbitrarily
close to this real number. The integer L controls the inverse tolerance. -/
def defectCluster (k : ℕ) (x : ℝ) : Prop :=
  ∀ H L : ℕ, ∃ n, H<n ∧ n%3≠0 ∧ ¬Meet n (target n) ∧
    (L:ℝ)*|(mass k n:ℝ)-x|<1

private theorem finite_gap (s : Finset ℕ) (f : ℕ → ℝ) (x : ℝ)
    (miss : ∀ n∈s, f n≠x) : ∃ δ : ℝ, 0<δ ∧ ∀ n∈s, δ≤|f n-x| := by
  induction s using Finset.induction_on with
  | empty => exact ⟨1,by norm_num,by simp⟩
  | @insert a s fresh ih =>
    obtain ⟨δ,pos,old⟩ := ih (fun n hn => miss n (Finset.mem_insert_of_mem hn))
    have away : 0 < |f a-x| := abs_pos.mpr (sub_ne_zero.mpr (miss a (Finset.mem_insert_self ..)))
    refine ⟨min δ |f a-x|,lt_min pos away,?_⟩
    intro n hn
    rcases Finset.mem_insert.mp hn with rfl|prev
    · exact min_le_right ..
    · exact (min_le_left ..).trans (old _ prev)

private theorem real_row_error (k n : ℕ) :
    0≤((coefficients k n).1:ℝ)-(mass k n:ℝ) ∧
    ((coefficients k n).1:ℝ)-(mass k n:ℝ)≤(3:ℝ)^k/((n+1:ℕ):ℝ) := by
  constructor
  · exact sub_nonneg.mpr ((Rat.cast_le (K:=ℝ)).mpr (sub_nonneg.mp (row_error k n).1))
  · simpa only [Rat.cast_sub,Rat.cast_div,Rat.cast_pow,Rat.cast_ofNat,Rat.cast_natCast]
      using (Rat.cast_le (K:=ℝ)).mpr (row_error k n).2

/-- The complete set of cofinal ordinary defect-row limits on the real
line. In particular, no point outside the finite unit-slope table can
arise even if the witnessing residues change with the approximation. -/
theorem defect_cluster_iff (k : ℕ) (x : ℝ) :
    defectCluster k x ↔ ¬Universal ∧ ∃ r, r%3≠0 ∧ x=((coefficients k r).1:ℝ) := by
  constructor
  · intro cluster
    have fail : ¬Universal := by
      intro all
      obtain ⟨n,high,_,never,_⟩ := cluster 0 0
      obtain ⟨i,hi⟩ := all n high
      obtain ⟨j,hj⟩ := all (target n) (Nat.mul_pos (by positivity) high)
      exact never ⟨i,j,hi.trans hj.symm⟩
    refine ⟨fail,?_⟩
    by_contra! miss
    let s := (Finset.range (3^(k+1))).filter (fun n => n%3≠0)
    let f : ℕ → ℝ := fun n => (coefficients k n).1
    obtain ⟨δ,pos,away⟩ := finite_gap s f x (by
      intro n hn
      exact (miss n (Finset.mem_filter.mp hn).2).symm)
    obtain ⟨L,big⟩ := exists_nat_gt (2/δ)
    have product := (div_lt_iff₀ pos).mp big
    obtain ⟨n,tall,unit,_,near⟩ := cluster (L*3^k) L
    let r := n%(3^(k+1))
    have three : 3∣3^(k+1) := by rw [pow_succ]; exact dvd_mul_left ..
    have lower : 3^k∣3^(k+1) := by rw [pow_succ]; exact dvd_mul_right ..
    have rm : r∈s := Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (Nat.mod_lt _ (by positivity)),
      by simpa only [r,Nat.mod_mod_of_dvd _ three] using unit⟩
    have same : coefficients k n=coefficients k r := by
      rw [coefficients_residue k n,coefficients_residue k r]
      simp only [r,Nat.mod_mod_of_dvd _ lower]
    have err := real_row_error k n
    have high : (L:ℝ)*3^k<((n+1:ℕ):ℝ) := by exact_mod_cast (show L*3^k<n+1 by omega)
    have small : (L:ℝ)*(((coefficients k n).1:ℝ)-(mass k n:ℝ))<1 := by
      apply lt_of_le_of_lt (mul_le_mul_of_nonneg_left err.2 (by positivity))
      rw [←mul_div_assoc,div_lt_one (by positivity)]
      exact high
    have tri := abs_add_le (((coefficients k n).1:ℝ)-(mass k n:ℝ)) ((mass k n:ℝ)-x)
    rw [sub_add_sub_cancel,abs_of_nonneg err.1] at tri
    have sep := away r rm
    dsimp only [f] at sep
    rw [←same] at sep
    have bound := mul_le_mul_of_nonneg_left (sep.trans tri) (show 0≤(L:ℝ) by positivity)
    linarith only [product,small,near,bound]
  · rintro ⟨fail,r,unit,rfl⟩ H L
    obtain ⟨n,high,un,never,_,nn,near⟩ := mismatch_approximates fail unit k H L
    have nonneg := (Rat.cast_le (K:=ℝ)).mpr (sub_nonneg.mp nn)
    refine ⟨n,high,un,never,?_⟩
    rw [abs_sub_comm,abs_of_nonneg (sub_nonneg.mpr nonneg)]
    simpa only [Rat.cast_sub,Rat.cast_mul,Rat.cast_one,Rat.cast_natCast]
      using (Rat.cast_lt (K:=ℝ)).mpr near

#print axioms defect_cluster_iff
end Collatz.Itinerary.BergmanRelative

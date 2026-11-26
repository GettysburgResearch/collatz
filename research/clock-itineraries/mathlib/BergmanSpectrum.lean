module

public import BergmanDistance
public import Mathlib.Analysis.Normed.Operator.Basic
public import Mathlib.Analysis.Complex.Basic
import all BergmanRelative
import all BergmanDistance
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.BergmanRelative

set_option autoImplicit false

private theorem coefficient_caps (k a : ℕ) :
    (coefficients k a).1≤(3:ℚ)^k ∧ (coefficients k a).2≤(3:ℚ)^k := by
  induction k generalizing a with
  | zero => simp [coefficients]
  | succ k ih =>
    obtain ⟨ev,ec⟩ := ih (2*a)
    obtain ⟨od,oc⟩ := ih ((2*a-1)/3)
    simp only [coefficients,pow_succ]
    split <;> constructor <;> linarith only [ev,ec,od,oc,show 0≤(3:ℚ)^k by positivity]

theorem coefficients_residue (k a : ℕ) :
    coefficients k a=coefficients k (a%(3^k)) := by
  have h := coefficients_periodic k (a%(3^k)) (a/(3^k))
  rwa [Nat.mod_add_div] at h

/-- A uniform explicit error for replacing a finite ordinary fiber by
the ternary limiting row at the same residue. -/
theorem row_error (k a : ℕ) :
    0≤(coefficients k a).1-mass k a ∧
    (coefficients k a).1-mass k a ≤ (3:ℚ)^k/((a+1:ℕ):ℚ) := by
  rw [exact_row,sub_sub_cancel]
  exact ⟨div_nonneg (coefficient_signs ..).2 (by positivity),
    div_le_div_of_nonneg_right (coefficient_caps ..).2 (by positivity)⟩

/-- Every limiting unit row occurs to arbitrary precision on actual
component-crossing endpoints if the conjecture fails. -/
theorem mismatch_approximates (fail : ¬Universal) {r : ℕ} (unit : r%3≠0) (k H L : ℕ) :
    ∃ n, H<n ∧ n%3≠0 ∧ ¬Meet n (target n) ∧ n≡r [MOD 3^k] ∧
      0≤(coefficients k r).1-mass k n ∧
      (L:ℚ)*((coefficients k r).1-mass k n)<1 := by
  obtain ⟨n,large,un,co,never⟩ := mismatch_on_cylinder fail unit k (H+L*3^k)
  have eq : coefficients k n=coefficients k r := by
    rw [coefficients_residue k n,coefficients_residue k r]
    exact congrArg (coefficients k) co
  obtain ⟨nonneg,err⟩ := row_error k n
  rw [eq] at nonneg err
  refine ⟨n,by omega,un,never,co,nonneg,?_⟩
  have small : L*3^k<n+1 := by omega
  have cr : (L:ℚ)*3^k < ((n+1:ℕ):ℚ) := by exact_mod_cast small
  have upper := mul_le_mul_of_nonneg_left err (by positivity : 0≤(L:ℚ))
  apply lt_of_le_of_lt upper
  rw [←mul_div_assoc,div_lt_one (by positivity)]
  exact cr

def maximumSlope (k : ℕ) : ℚ :=
  (Finset.range (3^k)).sup' ⟨0,Finset.mem_range.mpr (by positivity)⟩
    (fun r => (coefficients k r).1)

private theorem slope_le (k a : ℕ) : (coefficients k a).1≤maximumSlope k := by
  rw [coefficients_residue k a]
  exact Finset.le_sup' (fun r => (coefficients k r).1)
    (Finset.mem_range.mpr (Nat.mod_lt _ (by positivity)))

private theorem slope_le_full (k r : ℕ) :
    ((coefficients k r).1:ℝ)≤squaredNorm k 0 (fun _ => True) := by
  by_contra! gap
  let N := squaredNorm k 0 (fun _ => True)
  let S : ℝ := (coefficients k r).1
  have pos : 0<S-N := by dsimp [N,S]; linarith
  obtain ⟨J,big⟩ := exists_nat_gt ((3:ℝ)^k/(S-N))
  let n := r+3^k*(J+3)
  have bound : J+3≤n := by
    have m := Nat.mul_le_mul_right (J+3) (Nat.pow_pos (n:=k) (by decide : 0<3))
    dsimp only [n]; omega
  have eq := coefficients_periodic k r (J+3)
  have err := (row_error k n).2
  change coefficients k n=coefficients k r at eq
  rw [eq] at err
  have realErr : S-(mass k n:ℝ)≤(3:ℝ)^k/((n+1:ℕ):ℝ) := by
    dsimp only [S]
    simpa only [Rat.cast_sub,Rat.cast_div,Rat.cast_pow,Rat.cast_ofNat,Rat.cast_natCast]
      using (Rat.cast_le (K:=ℝ)).mpr err
  have row : (mass k n:ℝ)≤N :=
    le_csSup (rowBdd ..) (Or.inr ⟨n,by omega,by omega,trivial,rfl⟩)
  have jn : (J:ℝ)<((n+1:ℕ):ℝ) := by exact_mod_cast (show J<n+1 by omega)
  have upper := (div_lt_iff₀ pos).mp (big.trans jn)
  have lower := (le_div_iff₀ (by positivity)).mp realErr
  nlinarith only [upper,lower,mul_le_mul_of_nonneg_right row
    (by positivity : 0≤((n+1:ℕ):ℝ))]

/-- The ordinary supremum equals the maximum of a finite ternary table
at every depth. This uses the actual finite-height rows on both sides. -/
theorem full_norm_finite (k : ℕ) :
    squaredNorm k 0 (fun _ => True)=(maximumSlope k:ℝ) := by
  apply le_antisymm
  · apply csSup_le (rowNonempty ..)
    rintro _ (rfl|⟨n,_,_,_,rfl⟩)
    · exact_mod_cast (le_trans (coefficient_signs k 1).1.le (slope_le k 1))
    · exact_mod_cast (le_trans (sub_nonneg.mp (row_error k n).1) (slope_le k n))
  · obtain ⟨r,_,val⟩ := Finset.exists_mem_eq_sup' (s:=Finset.range (3^k))
      (f:=fun r => (coefficients k r).1) ⟨0,Finset.mem_range.mpr (by positivity)⟩
    change maximumSlope k=(coefficients k r).1 at val
    rw [val]
    exact slope_le_full k r

/-- Clearing the ternary denominator makes the finite certificate natural-valued. -/
private def slopeNumerator : ℕ → ℕ → ℕ
  | 0,_ => 1
  | k+1,a => 6*slopeNumerator k (2*a) +
      if a%3=2 then 2*slopeNumerator k ((2*a-1)/3) else 0

private theorem slope_numerator (k a : ℕ) :
    (slopeNumerator k a:ℚ)=3^k*(coefficients k a).1 := by
  induction k generalizing a with
  | zero => simp [slopeNumerator,coefficients]
  | succ k ih =>
    simp only [slopeNumerator,coefficients,pow_succ]
    split <;> push_cast <;> rw [ih] <;> try rw [ih]
    all_goals ring

private theorem table_control {k p : ℕ}
    (upper : ∀ r : Fin (3^k), slopeNumerator k r≤p)
    (hit : slopeNumerator k (3^k-1)=p) : maximumSlope k=(p:ℚ)/3^k := by
  apply le_antisymm
  · obtain ⟨a,mem,atMax⟩ := Finset.exists_mem_eq_sup' (s:=Finset.range (3^k))
      (f:=fun r => (coefficients k r).1) ⟨0,Finset.mem_range.mpr (by positivity)⟩
    change maximumSlope k=(coefficients k a).1 at atMax
    rw [atMax]
    apply (le_div_iff₀ (by positivity)).mpr
    rw [mul_comm,←slope_numerator]
    exact_mod_cast upper ⟨a,Finset.mem_range.mp mem⟩
  · have eqn : (coefficients k (3^k-1)).1=(p:ℚ)/3^k := by
      apply (eq_div_iff (by positivity)).mpr
      rw [mul_comm,←slope_numerator,hit]
    rw [←eqn]
    exact slope_le ..

set_option maxRecDepth 16384 in
theorem finite_controls :
    maximumSlope 1=8/3 ∧ maximumSlope 2=52/9 ∧ maximumSlope 3=392/27 ∧
    maximumSlope 4=2512/81 := by
  refine ⟨?_,?_,?_,?_⟩
  · exact table_control (k:=1) (p:=8) (by decide) (by decide)
  · exact table_control (k:=2) (p:=52) (by decide) (by decide)
  · exact table_control (k:=3) (p:=392) (by decide) (by decide)
  · exact table_control (k:=4) (p:=2512) (by decide) (by decide)

/-- A contraction separating the two component blocks on a unit test
vector certifies an operator-norm distance, with a tolerated compact error.
A sequence of such tests with vanishing errors gives the same lower bound. -/
theorem distance_from_block_approximations {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℂ E] (T B C : E →L[ℂ] E) (R : ℝ)
    (tests : ∀ ε : ℝ, 0<ε → ∃ (x : E) (P : E →L[ℂ] E), ‖x‖≤1 ∧ ‖P‖≤1 ∧
      P (T x)=T x ∧ P (B x)=0 ∧ R-ε≤‖T x‖ ∧ ‖C x‖≤ε) :
    R≤‖T-(B+C)‖ := by
  by_contra! short
  let ε := (R-‖T-(B+C)‖)/3
  have positive : 0<ε := by dsimp [ε]; linarith
  obtain ⟨x,P,xu,pu,fix,kill,large,small⟩ := tests ε positive
  have node (z : E) : ‖P z‖≤‖z‖ :=
    (P.le_opNorm z).trans (by simpa using mul_le_mul_of_nonneg_right pu (_root_.norm_nonneg z))
  have piece := node ((T-(B+C)) x)
  simp only [sub_apply,add_apply,map_sub,map_add,
    fix,kill,zero_add] at piece
  have repair : ‖T x‖≤‖T x-P (C x)‖+‖P (C x)‖ := by
    simpa only [sub_add_cancel] using norm_add_le (T x-P (C x)) (P (C x))
  have combined := ((T-(B+C)).le_opNorm x).trans
    (by simpa using mul_le_mul_of_nonneg_left xu (_root_.norm_nonneg (T-(B+C))))
  simp only [sub_apply,add_apply] at combined
  have leftover := node (C x)
  dsimp [ε] at large small
  linarith only [large,small,piece,repair,combined,leftover,short]

/-- An undirected walk in the ordinary shortcut graph. Allowing 1 and 2
in a walk only strengthens the exclusion for the Bergman quotient. -/
inductive GraphWalk : ℕ → ℕ → ℕ → Prop where
  | nil (x : ℕ) : GraphWalk 0 x x
  | cons {d x y z : ℕ} (edge : step x=y ∨ step y=x) (tail : GraphWalk d y z) :
      GraphWalk (d+1) x z

theorem walk_meeting_clocks {d x y : ℕ} (path : GraphWalk d x y) :
    ∃ i≤d, ∃ j≤d, run i x=run j y := by
  induction path with
  | nil x => exact ⟨0,by omega,0,by omega,rfl⟩
  | @cons d x y z edge _ ih =>
    obtain ⟨i,bi,j,bj,eqn⟩ := ih
    rcases edge with forward|backward
    · exact ⟨i+1,by omega,j,by omega,by simpa only [run,forward] using eqn⟩
    · refine ⟨i,by omega,j+1,by omega,?_⟩
      calc
        run i x=run (i+1) y := by simp only [run,backward]
        _=run 1 (run i y) := run_add i 1 y
        _=run 1 (run j z) := by rw [eqn]
        _=run (j+1) z := (run_add j 1 z).symm

/-- The converging, widely separated controls alone attain the full
squared row supremum at each depth, height cutoff, and walk budget. -/
theorem finite_propagation_full (k H L : ℕ) :
    squaredNorm k H (fun n => target n=3*n ∧ ReachesOne n ∧ ReachesOne (target n) ∧
      ∀ d≤L, ¬GraphWalk d n (target n))=squaredNorm k 0 (fun _ => True) := by
  apply norm_eq_full
  intro a
  obtain ⟨n,high,_,tag,one,two,row,far⟩ := finite_horizon_control k a (max H 3) L
  refine ⟨n,high,⟨tag,one,two,?_⟩,row⟩
  intro d within path
  obtain ⟨i,bi,j,bj,eqn⟩ := walk_meeting_clocks path
  exact far i (bi.trans within) j (bj.trans within) eqn

#print axioms walk_meeting_clocks
#print axioms finite_propagation_full
#print axioms mismatch_approximates
#print axioms full_norm_finite
#print axioms finite_controls
#print axioms distance_from_block_approximations
end Collatz.Itinerary.BergmanRelative

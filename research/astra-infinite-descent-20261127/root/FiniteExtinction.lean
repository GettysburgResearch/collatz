import BirthReserve
import Mathlib.Algebra.Order.Archimedean.Basic

/-! Quantitative finite verification -> global finite-prefix mass, and the
previously written converse of PR201's full Collatz criterion.

No infinite density, external analytic theorem, or asserted vanishing
estimate occurs in the proofs. The final equivalence leaves both sides open. -/
set_option autoImplicit false
set_option warningAsError true

namespace FiniteExtinction
open CoreBranching PeakRigidity BinaryPrefixCriterion BinaryCylinder BirthReserve
open EarlierOffsets (Good)
open scoped BigOperators

theorem grade_add (a b x : ℕ) : grade (a+b) x=grade a x+grade b (run a x) := by
  induction b with
  | zero => simp [grade]
  | succ b ih =>
    change grade (a+b) x+run (a+b) x%2 =
      grade a x+(grade b (run a x)+run b (run a x)%2)
    rw [ih,run_add]
    omega

theorem run_one_even (k : ℕ) : run (2*k) 1=1 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [show 2*(k+1)=2*k+2 by omega,run_add,ih]
    rfl

theorem grade_one_even (k : ℕ) : grade (2*k) 1=k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [show 2*(k+1)=2*k+2 by omega,grade_add,ih,run_one_even]
    rfl

/-- A supplied ordinary hit at h forces failure of the 5/8 gate by 5h+2. -/
theorem gate_fails_after_hit (x h : ℕ) (hit : run h x=1) : ¬Gate (5*h+2) x := by
  intro gate
  have last := gate (5*h+2) (Finset.mem_range.mpr (by omega))
  rw [show 5*h+2=h+2*(2*h+1) by omega,grade_add,hit,grade_one_even] at last
  have count := grade_le h x
  omega

theorem mass_active (N : ℕ) : mass N=activeSum N (fun x => 1/(x:ℚ)) := by
  unfold mass survivors activeSum
  rw [Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro x _
  by_cases hx : x=0
  · simp [hx]
  · have hp : 0<x := Nat.pos_of_ne_zero hx
    simp [hp]

/-- Once all original low sources have failed, every retained term is a
genuine later birth. The depth is explicit in a supplied convergence budget. -/
theorem mass_eq_tail (M H N : ℕ)
    (verified : ∀ x : ℕ, 0<x → x<2^M → ∃ h, h≤H ∧ run h x=1)
    (late : 5*H+2≤N) : mass N=tail M N := by
  rw [mass_active]
  unfold tail activeSum
  apply Finset.sum_congr rfl
  intro x _
  by_cases hg : Gate N x
  · simp only [hg,ite_true]
    by_cases hx : x=0
    · simp [hx,tailWeight]
    · have high : 2^M≤x := by
        by_contra hlow
        obtain ⟨h,hh,hit⟩ := verified x (Nat.pos_of_ne_zero hx) (by omega)
        exact gate_fails_after_hit x h hit (gate_mono hg (by omega))
      simp [tailWeight,high]
  · simp [hg]

/-- A completely finite certificate with an unrestricted later depth. -/
theorem finite_verification_transfer (M H N : ℕ)
    (verified : ∀ x : ℕ, 0<x → x<2^M → ∃ h, h≤H ∧ run h x=1)
    (depth : M≤N) (late : 5*H+2≤N) :
    mass N+reserve N≤reserve M := by
  rw [mass_eq_tail M H N verified late]
  have h := tail_with_reserve M (N-M)
  simpa [Nat.add_sub_of_le depth] using h

theorem finite_verification_eighth (k H N : ℕ)
    (verified : ∀ x : ℕ, 0<x → x<2^(8*k) → ∃ h, h≤H ∧ run h x=1)
    (depth : 8*k≤N) (late : 5*H+2≤N) :
    mass N≤(24*(k:ℚ)+5)*(6561/8192:ℚ)^k := by
  have h := finite_verification_transfer (8*k) H N verified depth late
  have hn := reserve_nonneg N
  have he := reserve_eighth k
  linarith

theorem finite_hit_budget (M : ℕ) (all : ∀ x : ℕ, 0<x → Good x) :
    ∃ H : ℕ, ∀ x : ℕ, 0<x → x<2^M → ∃ h, h≤H ∧ run h x=1 := by
  classical
  have hits : ∀ x : ℕ, ∃ h : ℕ, 0<x → run h x=1 := by
    intro x
    by_cases hp : 0<x
    · obtain ⟨h,hh⟩ := all x hp
      exact ⟨h,fun _ => hh⟩
    · exact ⟨0,fun h => False.elim (hp h)⟩
  choose clock hclock using hits
  let H := ∑ x ∈ Finset.range (2^M), clock x
  refine ⟨H,?_⟩
  intro x hp hx
  refine ⟨clock x,?_,hclock x hp⟩
  exact Finset.single_le_sum (fun i _ => Nat.zero_le (clock i)) (Finset.mem_range.mpr hx)

def SmallMass : Prop :=
  ∀ B : ℕ, 0<B → ∃ N : ℕ, 0<N ∧ mass N<1/(B:ℚ)

/-- Necessity of the finite rational criterion, now with all source births
and the same actual map accounted for inside Lean. -/
theorem small_mass_of_collatz (all : ∀ x : ℕ, 0<x → Good x) : SmallMass := by
  intro B hB
  have bp : (0:ℚ)<B := by exact_mod_cast hB
  obtain ⟨k,hk⟩ := exists_pow_lt_of_lt_one
    (x := (1:ℚ)/(128*(B:ℚ))) (y := (31/32:ℚ)) (by positivity) (by norm_num)
  have pk : (31/32:ℚ)^(k+1)≤(31/32:ℚ)^k := by
    rw [pow_succ]
    exact mul_le_of_le_one_right (by positivity) (by norm_num)
  have small : 128*(31/32:ℚ)^(k+1)<1/(B:ℚ) := by
    have h := mul_lt_mul_of_pos_left (pk.trans_lt hk) (by norm_num : (0:ℚ)<128)
    convert h using 1
    field_simp
  obtain ⟨H,verified⟩ := finite_hit_budget (8*(k+1)) all
  let N := max (8*(k+1)) (5*H+2)
  have dep : 8*(k+1)≤N := le_max_left _ _
  have late : 5*H+2≤N := le_max_right _ _
  have h := finite_verification_transfer (8*(k+1)) H N verified dep late
  have nonneg := reserve_nonneg N
  have upper := reserve_geometric (k+1)
  refine ⟨N,by omega,?_⟩
  linarith

/-- A full equivalence, with neither side assumed or proved universally. -/
theorem collatz_iff_small_mass :
    (∀ x : ℕ, 0<x → Good x) ↔ SmallMass := by
  constructor
  · exact small_mass_of_collatz
  · exact collatz_of_small_finite_mass

#print axioms gate_fails_after_hit
#print axioms finite_verification_transfer
#print axioms finite_verification_eighth
#print axioms small_mass_of_collatz
#print axioms collatz_iff_small_mass
end FiniteExtinction

module

public import PassageGateReserve
import all PassageGateReserve
public import Mathlib.Analysis.Normed.Group.Tannery
public import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open Finset Filter Topology
set_option autoImplicit false

def present (N x : ℕ) : Prop := 0<x ∧ x<2^N ∧ binaryGate N x
def permanent (x : ℕ) : Prop := 0<x ∧ ∀ N, binaryGate N x

noncomputable def weightedTerm (w : ℕ→ℝ) (N x : ℕ) : ℝ := by
  classical exact if present N x then w x else 0

noncomputable def envelope (w : ℕ→ℝ) (x : ℕ) : ℝ := by
  classical exact if ∃ N, present N x then w x else 0

noncomputable def limitTerm (w : ℕ→ℝ) (x : ℕ) : ℝ := by
  classical exact if permanent x then w x else 0

noncomputable def weightedMass (w : ℕ→ℝ) (N : ℕ) : ℝ :=
  ∑ x ∈ range (2^N), weightedTerm w N x

private theorem term_limit (w : ℕ→ℝ) (x : ℕ) :
    Tendsto (fun N => weightedTerm w N x) atTop (𝓝 (limitTerm w x)) := by
  classical
  apply Filter.Tendsto.congr' _ tendsto_const_nhds
  by_cases px : permanent x
  · filter_upwards [eventually_ge_atTop x] with N late
    have seen : present N x := ⟨px.1,Nat.lt_of_le_of_lt late Nat.lt_two_pow_self,px.2 N⟩
    simp [weightedTerm,limitTerm,px,seen]
  · by_cases zero : x=0
    · subst x
      exact Eventually.of_forall (fun _ => by simp [weightedTerm,present,limitTerm,permanent])
    · have bad : ∃ j, ¬binaryGate j x := by
        by_contra! ok
        exact px ⟨Nat.pos_of_ne_zero zero,ok⟩
      obtain ⟨j,bad⟩ := bad
      filter_upwards [eventually_ge_atTop j] with N late
      have gone : ¬present N x := by
        intro h
        exact bad (fun i hi => h.2.2 i (hi.trans late))
      simp [weightedTerm,limitTerm,px,gone]

/-- For a summably dominated positive weight on all actual accepted
ordinary representatives, the finite physical-clock mass converges
to the sum of that same weight over permanent ordinary seeds. -/
theorem weighted_limit (w : ℕ→ℝ) (nonneg : ∀ x, 0≤w x)
    (sum : Summable (envelope w)) :
    Tendsto (weightedMass w) atTop (𝓝 (∑' x, limitTerm w x)) := by
  classical
  have all : (fun N => ∑' x, weightedTerm w N x)=weightedMass w := by
    funext N
    apply tsum_eq_sum
    intro x outside
    have gone : ¬present N x := fun h => outside (mem_range.mpr h.2.1)
    simp [weightedTerm,gone]
  rw [←all]
  apply tendsto_tsum_of_dominated_convergence sum (term_limit w)
  exact Eventually.of_forall (fun N x => by
    by_cases good : present N x
    · simp [weightedTerm,good,envelope,show ∃ j, present j x from ⟨N,good⟩,abs_of_nonneg (nonneg x)]
    · simp only [weightedTerm,ite_eq_right good,norm_zero,envelope]
      split <;> simp_all)

private theorem positive_mass_of_permanent (w : ℕ→ℝ) (positive : ∀ x, 0<x → 0<w x)
    (nonneg : ∀ x, 0≤w x) (sum : Summable (envelope w)) {x : ℕ} (px : permanent x) :
    0<∑' v, limitTerm w v := by
  classical
  have nonnegLimit (v : ℕ) : 0≤limitTerm w v := by unfold limitTerm; split <;> simp_all
  have fin : Summable (limitTerm w) := by
    apply Summable.of_norm_bounded sum
    intro v
    rw [Real.norm_eq_abs,abs_of_nonneg (nonnegLimit v)]
    by_cases pv : permanent v
    · have seen : ∃ N, present N v := ⟨v,pv.1,Nat.lt_two_pow_self,pv.2 v⟩
      simp [limitTerm,pv,envelope,seen]
    · simp only [limitTerm,ite_eq_right pv,envelope]
      split <;> simp_all
  apply lt_of_lt_of_le _ (fin.le_tsum x (fun v _ => nonnegLimit v))
  simpa [limitTerm,px] using positive x px.1

/-- The fractional boundary at the exact binary clock. The analytic
input displayed here is summability of the union of passing seeds
with the chosen weight. No convergence of the Collatz orbit is assumed. -/
theorem fractional_vanishing_iff (s : ℝ)
    (sum : Summable (envelope (fun x : ℕ => (x:ℝ)^(-s)))) :
    Tendsto (weightedMass (fun x : ℕ => (x:ℝ)^(-s))) atTop (𝓝 0) ↔
      ∀ x, ¬permanent x := by
  classical
  let w := fun x : ℕ => (x:ℝ)^(-s)
  have nn (x : ℕ) : 0≤w x := Real.rpow_nonneg (Nat.cast_nonneg _) _
  have tt := weighted_limit w nn sum
  constructor
  · intro limit x px
    have zero := tendsto_nhds_unique tt limit
    have pos := positive_mass_of_permanent w (fun v hv => Real.rpow_pos_of_pos (by exact_mod_cast hv) _)
      nn sum px
    linarith
  · intro dead
    have vanished (x : ℕ) : limitTerm w x=0 := by simp [limitTerm,dead x]
    simpa only [vanished,tsum_zero] using tt

#print axioms weighted_limit
#print axioms fractional_vanishing_iff
end Collatz.Itinerary.PassageGate

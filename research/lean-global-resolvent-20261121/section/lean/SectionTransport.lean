import RisingReturns
import Mathlib.Analysis.PSeries
import Mathlib.Topology.Algebra.InfiniteSum.Real

/-!
Source-weight transport through the mandatory dyadic section.

This file keeps the original source weight when moving its atom to the first
positive return.  The total source mass is conserved; endpoint weights need
not dominate the transported mass by any fixed constant.  These statements
are unconditional boundary information, not a convergence estimate.
-/

namespace CollatzShell.ForwardSection.Transport

noncomputable section

open scoped BigOperators

/-- The same fourth-power weight used by the primitive source criterion. -/
def weight (n : ℕ) : ℝ := ((n : ℝ)^4)⁻¹

theorem weight_nonneg (n : ℕ) : 0 ≤ weight n := by unfold weight; positivity

theorem weight_summable : Summable weight :=
  Real.summable_nat_pow_inv.mpr (by decide : 1 < 4)

/-- Mass at a marked source, before transporting it. -/
def sectionWeight (n : ℕ) : ℝ := if Marked n then weight n else 0

theorem sectionWeight_nonneg (n : ℕ) : 0 ≤ sectionWeight n := by
  unfold sectionWeight
  split <;> first | exact weight_nonneg _ | exact le_rfl

theorem sectionWeight_le (n : ℕ) : sectionWeight n ≤ weight n := by
  unfold sectionWeight
  split <;> first | exact le_rfl | exact weight_nonneg _

theorem sectionWeight_summable : Summable sectionWeight :=
  Summable.of_nonneg_of_le sectionWeight_nonneg sectionWeight_le weight_summable

/-- All marked sources landing at `m` on their first positive marked return. -/
def returnMass (m : ℕ) : ℝ := ∑' n : {n : ℕ // next n = m}, sectionWeight n.val

/-- A source atom survives transport at its full original weight. -/
theorem source_atom_le {n : ℕ} (hn : Marked n) : weight n ≤ returnMass (next n) := by
  have hs : Summable (fun x : {x : ℕ // next x = next n} => sectionWeight x.val) :=
    sectionWeight_summable.subtype _
  have h := hs.le_tsum ⟨n, rfl⟩ (fun x _ => sectionWeight_nonneg x.val)
  simpa only [sectionWeight, ite_eq_left hn, returnMass] using h

/-- Moving mass to return endpoints does not itself remove any mass. -/
theorem returnMass_total : (∑' m : ℕ, returnMass m) = ∑' n : ℕ, sectionWeight n := by
  exact (sectionWeight_summable.hasSum.tsum_fiberwise next).tsum_eq

/-- The algebraic comparison keeps the original atom weight. -/
theorem weight_lt_of_growth {n m C : ℕ} (hn : 0<n) (hg : (C+1)*n<m) :
    (C:ℝ)*weight m < weight n := by
  have np : (0 : ℝ) < n := by exact_mod_cast hn
  have mp : (0 : ℝ) < m := by exact_mod_cast (show 0<m by omega)
  have gr : ((C:ℝ)+1)*n < m := by exact_mod_cast hg
  have powers : (((C:ℝ)+1)*n)^4 < (m:ℝ)^4 :=
    pow_lt_pow_left₀ gr (by positivity) (by decide)
  have cp : (0:ℝ) ≤ C := Nat.cast_nonneg C
  have factor : (C:ℝ) < ((C:ℝ)+1)^4 :=
    (lt_add_one (C:ℝ)).trans_le (le_self_pow₀ (by linarith) (by decide))
  have bound : (C:ℝ)*(n:ℝ)^4 < (m:ℝ)^4 := by
    rw [mul_pow] at powers
    exact (mul_lt_mul_of_pos_right factor (by positivity)).trans powers
  unfold weight
  rw [← div_eq_mul_inv, inv_eq_one_div]
  exact (div_lt_div_iff₀ (by positivity : 0 < (m:ℝ)^4)
    (by positivity : 0 < (n:ℝ)^4)).mpr (by simpa using bound)

/-- Arbitrary first-return expansion defeats every uniform density bound
against the fourth-power weight of the endpoint. -/
theorem no_uniform_endpoint_bound (C : ℕ) :
    ∃ m, Marked m ∧ (C : ℝ) * weight m < returnMass m := by
  obtain ⟨n, hn, hm, hg⟩ := arbitrarily_large_first_return (C+1)
  exact ⟨next n, next_marked n (by omega),
    (weight_lt_of_growth (by omega) hg).trans_le (source_atom_le hm)⟩

/-- The first visit, including a visit at clock zero. -/
def entry (n : ℕ) : ℕ := orbit (firstVisit n) n

/-- Source-weight pushforward for the bounded first visit of every positive start. -/
def entryMass (m : ℕ) : ℝ := ∑' n : {n : ℕ // entry n = m}, weight n.val

theorem entryMass_total : (∑' m : ℕ, entryMass m) = ∑' n : ℕ, weight n := by
  exact (weight_summable.hasSum.tsum_fiberwise entry).tsum_eq

theorem entry_atom_le (n : ℕ) : weight n ≤ entryMass (entry n) := by
  have hs : Summable (fun x : {x : ℕ // entry x = entry n} => weight x.val) :=
    weight_summable.subtype _
  exact hs.le_tsum ⟨n, rfl⟩ (fun x _ => weight_nonneg x.val)

/-- The same obstruction already occurs for the bounded first visit, before
iterating any return map. -/
theorem no_uniform_entry_bound (C : ℕ) :
    ∃ m, Marked m ∧ (C:ℝ)*weight m < entryMass m := by
  obtain ⟨n, hn, _, hg⟩ := arbitrarily_large_first_return (2*(C+1))
  have ap : 0<step n := by unfold step; split <;> omega
  have ab : step n≤2*n := by unfold step; split <;> omega
  have growth : (C+1)*step n < next n := by nlinarith only [hg, Nat.mul_le_mul_left (C+1) ab]
  have eq : entry (step n)=next n := rfl
  refine ⟨next n, next_marked n (by omega), ?_⟩
  have atom := entry_atom_le (step n)
  rw [eq] at atom
  exact (weight_lt_of_growth ap growth).trans_le atom

#print axioms returnMass_total
#print axioms no_uniform_endpoint_bound
#print axioms entryMass_total
#print axioms no_uniform_entry_bound

end

end CollatzShell.ForwardSection.Transport

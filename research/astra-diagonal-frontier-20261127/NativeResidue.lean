import NativePersistence
import Mathlib.Basic.Real.Basic
import Mathlib.Topology.MetricSpace.Pseudo.Defs
import Mathlib.Topology.Instances.Real.Lemmas

/-!
The actual source mass has a real limit, equal to the sum of the reciprocal
masses of all positive sources passing every gate. The equality of that
limit to zero is precisely the remaining Collatz assertion.
-/
set_option autoImplicit false
set_option warningAsError true

open Filter
open scoped Topology

namespace Collatz.NativeGate

noncomputable def persistentTotal : ℝ := ⨆ k, (permanentMass k : ℝ)

theorem persistentTotal_bdd : BddAbove (Set.range (fun k => (permanentMass k : ℝ))) := by
  refine ⟨9, ?_⟩
  rintro _ ⟨k, rfl⟩
  change (permanentMass k : ℝ) ≤ 9
  exact_mod_cast permanentMass_bound k

theorem persistentTotal_lower (k : ℕ) : (permanentMass k : ℝ) ≤ persistentTotal :=
  le_ciSup persistentTotal_bdd k

theorem persistentTotal_upper (k : ℕ) :
    persistentTotal ≤ (permanentMass k : ℝ) + (reserve k : ℝ) := by
  apply ciSup_le
  intro n
  exact_mod_cast permanentMass_tail k n

theorem persistentTotal_nonnegative : 0 ≤ persistentTotal := by
  have h : (0:ℝ) ≤ (permanentMass 0 : ℝ) := by
    exact_mod_cast permanentMass_nonnegative 0
  exact h.trans (persistentTotal_lower 0)

theorem persistentTotal_at_most_nine : persistentTotal ≤ 9 := by
  apply ciSup_le
  intro k
  exact_mod_cast permanentMass_bound k

theorem persistentTotal_computable_upper (k : ℕ) :
    persistentTotal ≤ ((mass k+reserve k:ℚ):ℝ) := by
  have h1 := persistentTotal_upper k
  have h2 : (permanentMass k : ℝ) ≤ (mass k : ℝ) := by
    exact_mod_cast permanentMass_le_mass (show k ≤ k by omega)
  push_cast
  linarith

theorem permanent_atom_le_persistentTotal {x : ℕ} (hx : 0 < x) (hp : Permanent x) :
    (x:ℝ)⁻¹ ≤ persistentTotal := by
  have h1 := atom_le_permanentMass hx (native_cutoff x) hp
  have h2 : (x:ℝ)⁻¹ ≤ (permanentMass x : ℝ) := by
    have hh : (((x:ℚ)⁻¹:ℚ):ℝ) ≤ (permanentMass x : ℝ) := by exact_mod_cast h1
    simpa only [Rat.cast_inv, Rat.cast_natCast] using hh
  exact h2.trans (persistentTotal_lower x)

theorem persistentTotal_cutoff_error (k : ℕ) :
    0 ≤ persistentTotal - (permanentMass k : ℝ) ∧
    persistentTotal - (permanentMass k : ℝ) ≤ 48*(99/100:ℝ)^k := by
  have hlo := persistentTotal_lower k
  have hup := persistentTotal_upper k
  have hr : (reserve k : ℝ) ≤ 48*(99/100:ℝ)^k := by
    have hh : (reserve k : ℝ) ≤ ((48*(99/100:ℚ)^k:ℚ):ℝ) := by
      exact_mod_cast (show reserve k ≤ 48*(99/100:ℚ)^k from reserve_exponential_bound k)
    norm_num only [Rat.cast_mul, Rat.cast_pow, Rat.cast_div, Rat.cast_ofNat] at hh
    exact hh
  constructor <;> linarith

theorem eventual_mass_residue_bound (L : ℕ) (hL : 0 < L) :
    ∃ N, ∀ n ≥ N,
      |(mass n : ℝ)-persistentTotal| < (L:ℝ)⁻¹ := by
  let k := 4800*L
  obtain ⟨j, hj⟩ := eventual_permanent_sandwich k
  refine ⟨k+j, ?_⟩
  intro n hn
  have hnn : k+j+(n-(k+j)) = n := by omega
  have h1 := hj (n-(k+j))
  rw [hnn] at h1
  have hl : (permanentMass k : ℝ) ≤ (mass n : ℝ) := by exact_mod_cast h1.1
  have hu : (mass n : ℝ) ≤ (permanentMass k : ℝ)+(reserve k : ℝ) := by
    exact_mod_cast h1.2
  have hp := persistentTotal_lower k
  have hq := persistentTotal_upper k
  have hs : (reserve k : ℝ) < (L:ℝ)⁻¹ := by
    have hh : (reserve k : ℝ) < (((L:ℚ)⁻¹:ℚ):ℝ) := by
      exact_mod_cast (show reserve k < (L:ℚ)⁻¹ from reserve_small L hL)
    simpa only [Rat.cast_inv, Rat.cast_natCast] using hh
  exact abs_lt.mpr ⟨by linarith, by linarith⟩

theorem mass_tendsto_persistentTotal :
    Tendsto (fun n => (mass n : ℝ)) atTop (𝓝 persistentTotal) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨L, hL⟩ := exists_nat_gt (ε⁻¹)
  have hεi : (0:ℝ) < ε⁻¹ := inv_pos.mpr hε
  have hLn : 0 < L := by exact_mod_cast (hεi.trans hL)
  have hLi : (L:ℝ)⁻¹ < ε := by
    have hi := (inv_lt_inv₀ (hεi.trans hL) hεi).mpr hL
    simpa using hi
  obtain ⟨N, hN⟩ := eventual_mass_residue_bound L hLn
  refine ⟨N, ?_⟩
  intro n hn
  simpa only [Real.dist_eq] using (hN n hn).trans hLi

theorem collatz_iff_persistentTotal_zero : Universal ↔ persistentTotal = 0 := by
  constructor
  · intro h
    have hz := universal_iff_permanentMass_zero.mp h
    simp [persistentTotal, hz]
  · intro h
    apply universal_iff_permanentMass_zero.mpr
    intro k
    have hl := persistentTotal_lower k
    rw [h] at hl
    have hq : permanentMass k ≤ 0 := by exact_mod_cast hl
    exact le_antisymm hq (permanentMass_nonnegative k)

end Collatz.NativeGate

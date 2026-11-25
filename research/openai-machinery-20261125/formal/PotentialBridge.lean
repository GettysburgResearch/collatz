import OAI.Optimization.LinearProgramming.Farkas.Basic
import TernaryItinerary
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-! Exact potential certificates for a finite, explicitly supplied transition graph.
The alternative decides this finite system. It does not assert that a finite
graph faithfully contains every future transition of one ordinary source. -/

namespace Collatz.OpenAIPotential

open Matrix
open scoped BigOperators

def edgeMatrix {m d : Nat} (source target : Fin m → Fin d) : Matrix (Fin m) (Fin d) ℚ :=
  fun i => Pi.single (target i) 1 - Pi.single (source i) 1

def Potential {m d : Nat} (source target : Fin m → Fin d) (cost : Fin m → ℚ)
    (p : Fin d → ℚ) : Prop :=
  ∀ i, p (target i) - p (source i) ≤ -cost i

theorem potential_iff_feasible {m d : Nat} (source target : Fin m → Fin d)
    (cost : Fin m → ℚ) (p : Fin d → ℚ) :
    Potential source target cost p ↔ edgeMatrix source target *ᵥ p ≤ -cost := by
  have row (i : Fin m) : (edgeMatrix source target *ᵥ p) i =
      p (target i) - p (source i) := by
    change (Pi.single (target i) 1 - Pi.single (source i) 1) ⬝ᵥ p = _
    rw [sub_dotProduct]
    simp
  constructor <;> intro h i <;> simpa only [row, Pi.neg_apply] using h i

/-- An exact circulation carrying positive total cost is a Farkas certificate.
It excludes every rational potential in the chosen finite ansatz. -/
theorem circulation_excludes_potential {m d : Nat} (source target : Fin m → Fin d)
    (cost : Fin m → ℚ) (y : Fin m → ℚ) (nonnegative : 0 ≤ y)
    (balanced : (edgeMatrix source target).transpose *ᵥ y = 0)
    (positive : 0 < cost ⬝ᵥ y) :
    ¬ ∃ p, Potential source target cost p := by
  have h := OAI.Optimization.LinearProgramming.Farkas.certificate_excludes_feasible
    (edgeMatrix source target) (-cost) nonnegative balanced
    (by simpa only [neg_dotProduct] using neg_neg_of_pos positive)
  rintro ⟨p, hp⟩
  exact h ⟨p, (potential_iff_feasible source target cost p).mp hp⟩

/-- The imported sparse alternative supplies either a verified potential or
a normalized obstruction. The support bound concerns this finite matrix. -/
theorem potential_or_sparse_obstruction {m d : Nat} (source target : Fin m → Fin d)
    (cost : Fin m → ℚ) :
    (∃ p, Potential source target cost p) ∨
    ∃ y : Fin m → ℚ, 0 ≤ y ∧ (edgeMatrix source target).transpose *ᵥ y = 0 ∧
      cost ⬝ᵥ y = 1 ∧
      (Finset.univ.filter fun i => y i ≠ 0).card ≤ (edgeMatrix source target).rank + 1 := by
  rcases OAI.Optimization.LinearProgramming.Farkas.sparse_alternative
      (edgeMatrix source target) (-cost) with ⟨p, hp⟩ | ⟨y, hy, hA, hc, hs⟩
  · exact Or.inl ⟨p, (potential_iff_feasible source target cost p).mpr hp⟩
  · refine Or.inr ⟨y, hy, hA, ?_, hs⟩
    simpa only [neg_dotProduct, neg_inj] using hc

/-- A real ordinary one-step lift witnesses the expanding self-loop in
every residue-only abstraction. No 2-adic completion is used. -/
theorem ordinary_residue_self_loop (m : Nat) (hm : 0 < m) :
    let n := 4*m-1
    let y := 6*m-1
    0 < n ∧ n % 2 = 1 ∧ y % 2 = 1 ∧
      Collatz.Itinerary.step n = y ∧ n % m = m-1 ∧ y % m = m-1 := by
  dsimp
  have h4 : (4*m-1) % m = m-1 := by
    rw [show 4*m-1 = 3*m+(m-1) by omega]
    simp [Nat.add_mod, Nat.mod_eq_of_lt (show m-1 < m by omega)]
  have h6 : (6*m-1) % m = m-1 := by
    rw [show 6*m-1 = 5*m+(m-1) by omega]
    simp [Nat.add_mod, Nat.mod_eq_of_lt (show m-1 < m by omega)]
  refine ⟨by omega, by omega, by omega, ?_, h4, h6⟩
  simp only [Collatz.Itinerary.step]
  split <;> omega

/-- A finite residue correction cannot decrease at every odd-to-odd
ordinary step. This excludes an ansatz, not the Collatz conjecture. -/
theorem residue_only_strict_potential_impossible (m : Nat) (hm : 0 < m) :
    ¬ ∃ p : Nat → ℚ, ∀ n : Nat, 0 < n → n % 2 = 1 →
      (Collatz.Itinerary.step n) % 2 = 1 →
      p ((Collatz.Itinerary.step n) % m) - p (n % m) ≤ -1 := by
  rintro ⟨p, hp⟩
  obtain ⟨hn, ho, hy, hstep, hnm, hym⟩ := ordinary_residue_self_loop m hm
  have hy' : Collatz.Itinerary.step (4*m-1) % 2 = 1 := by simpa [hstep] using hy
  have bad := hp (4*m-1) hn ho hy'
  rw [hstep, hnm, hym, sub_self] at bad
  norm_num at bad

end Collatz.OpenAIPotential

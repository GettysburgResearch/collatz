import GlobalParityMinimum
import Mathlib.Data.Int.LeastGreatest
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StrictGateCocycle

open Collatz.MersenneCrests (State)
open Collatz.ParityRecordHorizon (grade odds)
open Collatz.GlobalParityMinimum (cutoff_covers_all)

/-- A genuine strictly future minimum at native date i. -/
def Gate (b : Nat → Int) (i : Nat) : Prop := ∀ t, i < t → b i < b t

/-- The absolute suffix floor is attained and bounds every future level. -/
def IsFloor (b : Nat → Int) (i : Nat) (v : Int) : Prop :=
  (∃ t, i ≤ t ∧ b t = v) ∧ ∀ t, i ≤ t → v ≤ b t

/-- The proved finite Collatz cutoff supplies attained floors on every suffix. -/
theorem grade_floors_exist (z : State) (hz : 0 < z.1) (K i : Nat)
    (cut : 4*z.1^2*3^K ≤ 4^K) : ∃ v, IsFloor (grade z) i v := by
  let P (v : Int) := ∃ t, i ≤ t ∧ grade z t = v
  have lower : ∀ t, -(K : Int) ≤ grade z t := by
    intro t
    obtain ⟨k, hk, hkt⟩ := cutoff_covers_all z hz K cut t
    have small : -(K : Int) ≤ grade z k := by
      unfold grade
      omega
    exact le_trans small hkt
  obtain ⟨v, hv, hmin⟩ := Int.exists_least_of_bdd (P := P)
    ⟨-(K : Int), fun v ⟨t, _, h⟩ => h ▸ lower t⟩
    ⟨grade z i, i, le_rfl, rfl⟩
  exact ⟨v, hv, fun t ht => hmin _ ⟨t, ht, rfl⟩⟩

theorem grade_step_upper (z : State) (t : Nat) :
    grade z (t+1) ≤ grade z t + 1 := by
  unfold grade
  rw [odds]
  split <;> omega

/-- An integer path with upward increments at most one gains one suffix-floor
unit exactly at its strict future minima. -/
theorem floor_jump (b R : Nat → Int) (floors : ∀ i, IsFloor b i (R i))
    (step : ∀ i, b (i+1) ≤ b i+1) (i : Nat) :
    (Gate b i → R (i+1) = R i+1) ∧ (¬ Gate b i → R (i+1) = R i) := by
  obtain ⟨⟨t, ht, hval⟩, hlo⟩ := floors i
  obtain ⟨⟨s, hs, hsval⟩, hnext⟩ := floors (i+1)
  have mono : R i ≤ R (i+1) := hsval ▸ hlo s (by omega)
  have upper := hnext (i+1) le_rfl
  have lower := hlo i le_rfl
  have inc := step i
  constructor
  · intro gate
    have hstrict := gate s (by omega)
    have initial : b i = R i := by
      by_cases hh : t = i
      · simpa only [hh] using hval
      · have hlt := gate t (by omega)
        omega
    omega
  · intro notGate
    by_contra hne
    apply notGate
    intro v hv
    have hlv := hnext v (by omega)
    by_cases hh : t = i
    · subst t
      omega
    · have hlt := hnext t (by omega)
      omega

noncomputable def visits (b : Nat → Int) (t : Nat) : Int := by
  classical
  exact ∑ i ∈ Finset.range t, if Gate b i then (1 : Int) else 0

/-- The actual native path's current grade, its deficit below the future, and
its accumulated strict-gate count satisfy an exact finite identity. -/
theorem native_cocycle (z : State) (hz : 0 < z.1) (K : Nat)
    (cut : 4*z.1^2*3^K ≤ 4^K) :
    ∃ R : Nat → Int, (∀ i, IsFloor (grade z) i (R i)) ∧
      ∀ t, grade z t = (grade z t - R t) + R 0 + visits (grade z) t := by
  classical
  choose R hR using fun i => grade_floors_exist z hz K i cut
  refine ⟨R, hR, ?_⟩
  have telescope (t : Nat) : R t = R 0 + visits (grade z) t := by
    induction t with
    | zero => simp [visits]
    | succ i ih =>
      have jump := floor_jump (grade z) R hR (grade_step_upper z) i
      have count : visits (grade z) (i+1) = visits (grade z) i +
          (if Gate (grade z) i then 1 else 0) := by
        simp only [visits, Finset.sum_range_succ]
      by_cases hg : Gate (grade z) i
      · rw [count, ite_eq_left hg, jump.1 hg]
        omega
      · rw [count, ite_eq_right hg, jump.2 hg]
        omega
  intro t
  have h := telescope t
  omega

end Collatz.StrictGateCocycle

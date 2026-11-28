import ShiftedSiblingCarries
import Mathlib.Tactic.Ring

/- Finite affine identities on actual positive trajectories. The Subspace
   Theorem, description-length threshold and regular-language consequences
   are proved in the accompanying written argument, not in this module. -/
namespace Collatz.RegularParityCenters

open Collatz.MersenneCrests (State next run run_add)
open Collatz.ShiftedSiblingCarries (multiplier slope carry carry_identity)

def bit (z : State) : Nat := z.1 % 2

theorem native_step (z : State) :
    2*(next z).1 = multiplier z*z.1 + bit z := by
  by_cases he : z.1 % 2 = 0
  · simp only [next, multiplier, bit, he, ite_true, Nat.one_mul, Nat.add_zero]
    omega
  · simp only [next, multiplier, bit, he, ite_false]
    omega

theorem native_affine (z : State) (l : Nat) :
    2^l*(run z l).1 = slope z l*z.1 + carry bit z l :=
  carry_identity (fun x => x) bit native_step z l

/-- Numerator of the distance from the rational fixed point C/(P−Q). -/
def centerMark (P Q C X : Int) : Int := (P-Q)*X-C

theorem center_transport (P Q C X Y : Int) (step : P*Y = Q*X+C) :
    P*centerMark P Q C Y = Q*centerMark P Q C X := by
  unfold centerMark
  calc
    _ = (P-Q)*(P*Y)-P*C := by ring
    _ = _ := by rw [step]; ring

theorem center_repeat (P Q C : Int) (x : Nat → Int) (a : Nat)
    (steps : ∀ i < a, P*x (i+1) = Q*x i + C) :
    P^a*centerMark P Q C (x a) = Q^a*centerMark P Q C (x 0) := by
  induction a with
  | zero => simp
  | succ a ih =>
    have hprev := ih (fun i hi => steps i (by omega))
    have hlast := center_transport P Q C (x a) (x (a+1)) (steps a (by omega))
    calc
      _ = P^a*(P*centerMark P Q C (x (a+1))) := by rw [pow_succ]; ring
      _ = Q*(P^a*centerMark P Q C (x a)) := by rw [hlast]; ring
      _ = _ := by rw [hprev, pow_succ]; ring

/-- Genuine repeated block boundaries. Equality of the measured multiplier
and carry at each observed copy is sufficient for the powered identity. -/
theorem native_repeated_center (z : State) (l a Q C : Nat)
    (multipliers : ∀ i < a, slope (run z (i*l)) l = Q)
    (carries : ∀ i < a, carry bit (run z (i*l)) l = C) :
    ((2^l : Nat) : Int)^a*centerMark (2^l : Nat) Q C (run z (a*l)).1 =
      (Q : Int)^a*centerMark (2^l : Nat) Q C z.1 := by
  have steps (i : Nat) (hi : i < a) :
      ((2^l : Nat) : Int)*((run z ((i+1)*l)).1 : Int) =
        (Q : Int)*((run z (i*l)).1 : Int) + (C : Int) := by
    have h := native_affine (run z (i*l)) l
    rw [multipliers i hi, carries i hi] at h
    rw [Nat.succ_mul, run_add]
    exact_mod_cast h
  simpa [run] using center_repeat (2^l : Nat) Q C
    (fun i => ((run z (i*l)).1 : Int)) a steps

end Collatz.RegularParityCenters

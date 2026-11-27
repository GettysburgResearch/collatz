import RankTwoControl
import Mathlib.Data.Nat.ModEq

/-! At a zero terminal of the native rational control, the signed carry
stops. Every alternative first bit is even. An odd letter at a sufficiently
late position gives a larger signed carry forever. -/
namespace Collatz.FrozenOffset
open Collatz.SourceDeletion

set_option maxRecDepth 30000
set_option maxHeartbeats 8000000
set_option exponentiation.threshold 4000

def carry (i : Nat) (c : Int) : List Bool → Int
  | [] => c
  | o::w => carry (i+1) (if o then 3*c+2^i else c) w

private theorem carry_mono (w : List Bool) (i : Nat) (c : Int)
    (ip : 1≤i) (cp : -1≤c) : c≤carry i c w := by
  induction w generalizing i c with
  | nil => rfl
  | cons o w ih =>
    have p : (2:Int)≤(2:Int)^i := by
      exact_mod_cast (show (2:Nat)^1≤2^i from Nat.pow_le_pow_right (by decide) ip)
    cases o
    · exact ih (i+1) c (by omega) cp
    · have grow : c≤3*c+2^(i:Nat) := by omega
      exact grow.trans (ih (i+1) _ (by omega) (by omega))

/-- Any suffix starting after the last affordable binary position is
entirely even, at arbitrary length. -/
theorem frozen_suffix (w : List Bool) (i : Nat) (c C : Int)
    (ip : 1≤i) (cp : -1≤c) (late : C+3<(2:Int)^i)
    (ends : carry i c w=C) : c=C ∧ w.count true=0 := by
  induction w generalizing i c with
  | nil => exact ⟨ends,rfl⟩
  | cons o w ih =>
    cases o
    · have pow : (0:Int)<2^i := by positivity
      have h:=ih (i+1) c (by omega) cp (by rw [pow_succ];omega) ends
      simpa using h
    · change carry (i+1) (3*c+2^i) w=C at ends
      have p : (2:Int)≤(2:Int)^i := by
        exact_mod_cast (show (2:Nat)^1≤2^i from Nat.pow_le_pow_right (by decide) ip)
      have next : -1≤3*c+2^i := by omega
      have g:=carry_mono w (i+1) (3*c+2^i) (by omega) next
      omega

def frozenC : Nat :=
  267203519953118404321999117996060733837301721716284200753849248536783269239472683250230608171699479135315356686324587853126259288870105170962382739565

def third (x : Nat) : Nat := (x+((3-x%3)%3)*2^498)/3

def residue : Nat → Nat
  | 0 => 3^173
  | d+1 => third (residue d)

theorem native498 :
    odds 498 (3^173-1)=240 ∧ 2^498*run 498 (3^173-1)=3^(173+240)+frozenC ∧
      frozenC+3<2^497 := by decide +kernel

/-- The division by three is exact at the indicated binary precision. -/
theorem third_spec (x : Nat) (bound : x<2^498) :
    third x<2^498 ∧ 3*third x ≡ x [MOD 2^498] := by
  have k : (2:Nat)^498%3=1 := by decide +kernel
  have d : (x+((3-x%3)%3)*2^498)%3=0 := by
    rw [Nat.add_mod,Nat.mul_mod,k]
    rcases (show x%3=0 ∨ x%3=1 ∨ x%3=2 by omega) with h|h|h <;> rw [h]
  have e : 3*third x=x+((3-x%3)%3)*2^498 := by
    unfold third
    have m:=Nat.mod_add_div (x+((3-x%3)%3)*2^498) 3
    omega
  have t : ((3-x%3)%3)*2^498≤2*2^498 := Nat.mul_le_mul_right _ (by omega)
  exact ⟨by omega, by rw [e];exact Nat.add_modEq_left_iff.mpr (dvd_mul_left _ _)⟩

theorem residue_spec (d : Nat) : residue d<2^498 ∧ 3^d*residue d ≡ 3^173 [MOD 2^498] := by
  induction d with
  | zero =>
    constructor
    · decide +kernel
    · decide +kernel
  | succ d ih =>
    obtain ⟨bound,con⟩:=third_spec (residue d) ih.1
    refine ⟨bound,?_⟩
    rw [residue,pow_succ 3 d, Nat.mul_assoc]
    exact (con.mul_left (3^d)).trans ih.2

def blocked (i : Fin 257) : Prop :=
  let d:=i.val+1
  let r:=residue d
  let q:=odds 498 (r-1)
  q≠240+d

private instance (i : Fin 257) : Decidable (blocked i) := by unfold blocked;infer_instance

/-- Complete arithmetic scan of the 257 possible positive savings. -/
theorem finite_scan : ∀ i : Fin 257, blocked i := by decide +kernel

#print axioms frozen_suffix
#print axioms native498
#print axioms third_spec
#print axioms residue_spec
#print axioms finite_scan
end Collatz.FrozenOffset

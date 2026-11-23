import CycleWordAlgebra
import Mathlib.Data.Nat.GCD.Basic

/-!
# Exact numerical cancellation under a whole-word moving-letter defect

This module uses the complete chronological carry from CycleWordAlgebra.
It proves a finite transport identity, including all denominator prime
powers. It does not prove the zero-fibre packing/window claims in the
accompanying note or exclude unrestricted positive integer cycles.
-/

namespace Collatz.HighVariance.CycleCancellation

open Collatz.HighVariance.CycleWordAlgebra

private theorem zeroes_ones (h : Nat) : ones (List.replicate h false) = 0 := by
  induction h with
  | zero => simp [ones]
  | succ h ih => simp [List.replicate_succ, ones, ih]

private theorem zeroes_carry (h : Nat) : carry (List.replicate h false) = 0 := by
  induction h with
  | zero => simp [carry]
  | succ h ih => simp [List.replicate_succ, carry, ih]

/-- All surrounding bits are retained when one bit moves across h zeroes. -/
theorem moving_one_carry (u v : List Bool) (h : Nat) :
    carry (u ++ List.replicate h false ++ [true] ++ v) =
      carry (u ++ [true] ++ List.replicate h false ++ v) +
        2 ^ u.length * 3 ^ ones v * (2 ^ h - 1) := by
  simp [carry_append, ones_append, zeroes_ones, zeroes_carry, ones, carry, pow_add]
  have ht : 2 ^ h = (2 ^ h - 1) + 1 := (Nat.sub_add_cancel Nat.one_le_two_pow).symm
  generalize 2 ^ h - 1 = t at *
  rw [ht]
  ring

/-- A positive Collatz denominator is a unit at both two and three.
The exponent hypotheses are explicit; no signed subtraction is hidden. -/
theorem denominator_coprime_two_three (A p : Nat) (hA : 0 < A) (hp : 0 < p)
    (h : 3 ^ p ≤ 2 ^ A) :
    (2 ^ A - 3 ^ p).Coprime 2 ∧ (2 ^ A - 3 ^ p).Coprime 3 := by
  have hc : (2 ^ A).Coprime (3 ^ p) :=
    ((by decide : Nat.Coprime 2 3).pow_left A).pow_right p
  constructor
  · apply (Nat.coprime_pow_right_iff hA _ 2).mp
    exact (Nat.coprime_self_sub_left h).mpr hc.symm
  · apply (Nat.coprime_pow_right_iff hp _ 3).mp
    exact (Nat.coprime_sub_self_left h).mpr hc

/-- General arithmetic core: replacing a zero residue by a unit times a
known displacement retains exactly the displacement's numerical gcd. -/
theorem gcd_after_unit_displacement (D C C' factor shift : Nat)
    (hC : D ∣ C) (hid : C = C' + factor * shift)
    (hf : D.Coprime factor) :
    Nat.gcd D C' = Nat.gcd D shift := by
  have hs : D ∣ C' + factor * shift := hid ▸ hC
  have hg : Nat.gcd D C' = Nat.gcd D (factor * shift) := by
    apply Nat.dvd_antisymm
    · apply Nat.dvd_gcd (Nat.gcd_dvd_left D C')
      exact (Nat.dvd_add_iff_right (Nat.gcd_dvd_right D C')).mpr
        ((Nat.gcd_dvd_left D C').trans hs)
    · apply Nat.dvd_gcd (Nat.gcd_dvd_left D (factor * shift))
      exact (Nat.dvd_add_iff_left (Nat.gcd_dvd_right D (factor * shift))).mpr
        ((Nat.gcd_dvd_left D (factor * shift)).trans hs)
  rw [hg, Nat.mul_comm factor shift]
  exact Nat.Coprime.gcd_mul_right_cancel_right shift hf.symm

/-- Complete-word form, conditional only on its original zero residue
and the explicitly stated two/three coprimalities. -/
theorem moving_one_gcd (u v : List Bool) (h D : Nat)
    (hD2 : D.Coprime 2) (hD3 : D.Coprime 3)
    (hzero : D ∣ carry (u ++ List.replicate h false ++ [true] ++ v)) :
    Nat.gcd D (carry (u ++ [true] ++ List.replicate h false ++ v)) =
      Nat.gcd D (2 ^ h - 1) := by
  apply gcd_after_unit_displacement D _ _ (2 ^ u.length * 3 ^ ones v) _ hzero
  · exact moving_one_carry u v h
  · exact (hD2.pow_right u.length).mul_right (hD3.pow_right (ones v))

/-- Full-denominator consumer: the two/three coprimalities are derived
from this word's own positive cycle denominator, not assumed separately. -/
theorem full_denominator_moving_one_gcd (u v : List Bool) (h : Nat) :
    let w := u ++ List.replicate h false ++ [true] ++ v
    let D := 2 ^ w.length - 3 ^ ones w
    3 ^ ones w < 2 ^ w.length → D ∣ carry w →
      Nat.gcd D (carry (u ++ [true] ++ List.replicate h false ++ v)) =
        Nat.gcd D (2 ^ h - 1) := by
  dsimp only
  intro hpositive hzero
  have hA : 0 < (u ++ List.replicate h false ++ [true] ++ v).length := by
    simp only [List.length_append, List.length_replicate, List.length_singleton]
    omega
  have hp : 0 < ones (u ++ List.replicate h false ++ [true] ++ v) := by
    simp [ones_append, zeroes_ones, ones]
  obtain ⟨hD2, hD3⟩ := denominator_coprime_two_three _ _ hA hp hpositive.le
  exact moving_one_gcd u v h _ hD2 hD3 hzero

/-- After an adjacent swap of an integral word, no denominator prime
cancels from the new carry. This is the h=1 consequence, not a cycle
exclusion theorem. -/
theorem adjacent_zero_has_coprime_neighbor (u v : List Bool) (D : Nat)
    (hD2 : D.Coprime 2) (hD3 : D.Coprime 3)
    (hzero : D ∣ carry (u ++ [false, true] ++ v)) :
    D.Coprime (carry (u ++ [true, false] ++ v)) := by
  simpa [Nat.Coprime, List.append_assoc] using
    moving_one_gcd u v 1 D hD2 hD3 (by simpa [List.append_assoc] using hzero)

end Collatz.HighVariance.CycleCancellation

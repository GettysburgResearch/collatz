import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Finset.Card
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Finite ordinary arithmetic behind periodic phase concentration

The exact edge equations are explicit hypotheses. No infinite orbit, iid law,
harmonic measure, or de Bruijn construction is asserted here. The written note
supplies the positive odd CRT realizations and the finite periodic templates.
The module checks their full carry, signed-shadow telescope, two divisibility
payments, source-height lower bound, and finite phase collision consequence.
-/

namespace Collatz.LiteratureRoundFour.ActualLawRigidity

set_option autoImplicit false

def gapCarry : List Nat → Nat
  | [] => 0
  | g :: w => 3 ^ w.length + 2 ^ g * gapCarry w

def clock (g : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => clock g n + g n

/-- Complete chronological concatenation of odd-gap words. -/
theorem gapCarry_append (u v : List Nat) :
    gapCarry (u ++ v) = 3 ^ v.length * gapCarry u + 2 ^ u.sum * gapCarry v := by
  induction u with
  | nil => simp [gapCarry]
  | cons g u ih =>
      simp [gapCarry, ih, pow_add]
      ring

/-- One cyclic rotation, retaining both full clocks and every carry term. -/
theorem rotated_gap_carry (g : Nat) (w : List Nat) :
    3 * gapCarry (g :: w) + 2 ^ (g :: w).sum =
      3 ^ (g :: w).length + 2 ^ g * gapCarry (w ++ [g]) := by
  simp [gapCarry_append, gapCarry, pow_add, pow_succ]
  ring

/-- With the positive denominator difference supplied, rotated carries are
the numerators of a negative rational periodic shadow. -/
theorem period_shadow_step (g D : Nat) (w : List Nat)
    (hD : D + 2 ^ (g :: w).sum = 3 ^ (g :: w).length) :
    3 * gapCarry (g :: w) = D + 2 ^ g * gapCarry (w ++ [g]) := by
  have h := rotated_gap_carry g w
  omega

/-- Combine an actual ordinary edge with its common-denominator shadow.
Positivity and oddness are needed for the written ordinary realization,
but this exact algebraic identity needs only the two displayed equations. -/
theorem actual_shadow_step (D n q b c g : Nat)
    (hedge : 3 * n + 1 = 2 ^ g * q)
    (hshadow : 3 * b = D + 2 ^ g * c) :
    2 ^ g * (D * q + c) = 3 * (D * n + b) := by
  nlinarith

/-- The same source remains in the complete finite shadow telescope. -/
theorem shadow_telescope (g q b : Nat → Nat) (D T : Nat)
    (hedge : ∀ i < T, 3 * q i + 1 = 2 ^ g i * q (i + 1))
    (hshadow : ∀ i < T, 3 * b i = D + 2 ^ g i * b (i + 1)) :
    2 ^ clock g T * (D * q T + b T) = 3 ^ T * (D * q 0 + b 0) := by
  induction T with
  | zero => simp [clock]
  | succ T ih =>
      have hprev := ih (fun i hi => hedge i (by omega))
        (fun i hi => hshadow i (by omega))
      have hstep := actual_shadow_step D (q T) (q (T + 1)) (b T) (b (T + 1))
        (g T) (hedge T (by omega)) (hshadow T (by omega))
      calc
        2 ^ clock g (T + 1) * (D * q (T + 1) + b (T + 1)) =
            2 ^ clock g T * (2 ^ g T * (D * q (T + 1) + b (T + 1))) := by
          simp [clock, pow_add, Nat.mul_assoc]
        _ = 2 ^ clock g T * (3 * (D * q T + b T)) := by rw [hstep]
        _ = 3 * (2 ^ clock g T * (D * q T + b T)) := by ring
        _ = 3 * (3 ^ T * (D * q 0 + b 0)) := by rw [hprev]
        _ = 3 ^ (T + 1) * (D * q 0 + b 0) := by rw [pow_succ]; ring

/-- Ternary precision is gained at every actual odd step. -/
theorem shadow_ternary_divisibility (A j D n p b c : Nat)
    (h : 2 ^ A * (D * n + b) = 3 ^ j * (D * p + c)) :
    3 ^ j ∣ D * n + b := by
  have hc : Nat.Coprime (3 ^ j) (2 ^ A) :=
    ((by decide : Nat.Coprime 3 2).pow_left j).pow_right A
  exact hc.dvd_of_dvd_mul_left ⟨D * p + c, h⟩

/-- The unchanged positive source pays the entire binary clock. -/
theorem shadow_binary_divisibility (A j D n p b c : Nat)
    (h : 2 ^ A * (D * n + b) = 3 ^ j * (D * p + c)) :
    2 ^ A ∣ D * p + c := by
  have hc : Nat.Coprime (2 ^ A) (3 ^ j) :=
    ((by decide : Nat.Coprime 2 3).pow_left A).pow_right j
  exact hc.dvd_of_dvd_mul_left ⟨D * n + b, h.symm⟩

/-- This is the exact source-height cost, not a uniform mixing assertion. -/
theorem source_height_payment (A j D n p b c : Nat)
    (hpositive : 0 < D * p + c)
    (h : 2 ^ A * (D * n + b) = 3 ^ j * (D * p + c)) :
    2 ^ A ≤ D * p + c :=
  Nat.le_of_dvd hpositive (shadow_binary_divisibility A j D n p b c h)

/-- Equal shadow numerators force equal actual endpoint residues once the
ternary precision has been paid. The denominator is required to be a unit. -/
theorem same_shadow_phase_residue (Q D n n' b : Nat)
    (hD : Nat.Coprime Q D)
    (hn : Q ∣ D * n + b) (hn' : Q ∣ D * n' + b) : n % Q = n' % Q := by
  have hz : Nat.ModEq Q (D * n + b) (D * n' + b) :=
    (Nat.modEq_zero_iff_dvd.mpr hn).trans (Nat.modEq_zero_iff_dvd.mpr hn').symm
  exact Nat.ModEq.cancel_left_of_coprime hD (Nat.ModEq.add_right_cancel' b hz)

/-- The phase coding has at most d residues, on any supplied set of
observation clocks. No uniform phase frequencies are assumed here. -/
theorem phase_residue_card (S : Finset Nat) (d Q : Nat) (hd : 0 < d)
    (q phaseResidue : Nat → Nat)
    (hphase : ∀ i ∈ S, q i % Q = phaseResidue (i % d)) :
    (S.image (fun i => q i % Q)).card ≤ d := by
  have hsub : S.image (fun i => q i % Q) ⊆ (Finset.range d).image phaseResidue := by
    intro a ha
    obtain ⟨i, hi, rfl⟩ := Finset.mem_image.mp ha
    exact Finset.mem_image.mpr
      ⟨i % d, Finset.mem_range.mpr (Nat.mod_lt i hd), (hphase i hi).symm⟩
  exact (Finset.card_le_card hsub).trans
    (Finset.card_image_le.trans (by rw [Finset.card_range]))

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Any original weights on at most d occupied residues have this collision
lower bound. No iid resampling occurs; diagonal terms remain in each square. -/
theorem phase_collision_lower (S : Finset Nat) (d Q : Nat) (hd : 0 < d)
    (q phaseResidue : Nat → Nat) (weight : Nat → K)
    (hphase : ∀ i ∈ S, q i % Q = phaseResidue (i % d)) :
    (∑ i ∈ S, weight i) ^ 2 ≤ (d : K) *
      ∑ a ∈ S.image (fun i => q i % Q),
        (∑ i ∈ S.filter (fun i => q i % Q = a), weight i) ^ 2 := by
  have hcard : ((S.image (fun i => q i % Q)).card : K) ≤ d := by
    exact_mod_cast phase_residue_card S d Q hd q phaseResidue hphase
  have hsum : (∑ a ∈ S.image (fun i => q i % Q),
      ∑ i ∈ S.filter (fun i => q i % Q = a), weight i) = ∑ i ∈ S, weight i := by
    exact Finset.sum_fiberwise_of_maps_to
      (fun i hi => Finset.mem_image.mpr ⟨i, hi, rfl⟩) weight
  calc
    (∑ i ∈ S, weight i) ^ 2 =
        (∑ a ∈ S.image (fun i => q i % Q),
          ∑ i ∈ S.filter (fun i => q i % Q = a), weight i) ^ 2 := by rw [hsum]
    _ ≤ ((S.image (fun i => q i % Q)).card : K) *
        ∑ a ∈ S.image (fun i => q i % Q),
          (∑ i ∈ S.filter (fun i => q i % Q = a), weight i) ^ 2 := by
      simpa using Finset.sum_mul_sq_le_sq_mul_sq (S.image (fun i => q i % Q))
        (fun _ => (1 : K))
        (fun a => ∑ i ∈ S.filter (fun i => q i % Q = a), weight i)
    _ ≤ (d : K) * ∑ a ∈ S.image (fun i => q i % Q),
          (∑ i ∈ S.filter (fun i => q i % Q = a), weight i) ^ 2 :=
      mul_le_mul_of_nonneg_right hcard (Finset.sum_nonneg (fun _ _ => sq_nonneg _))

/-- Each pair of different affine slopes excludes at most one original
source. The written CRT construction counts these finite exclusions. -/
theorem affine_coincidence_unique (a b c d x y : K) (hne : a ≠ c)
    (hx : a * x + b = c * x + d) (hy : a * y + b = c * y + d) : x = y := by
  have hp : (a - c) * (x - y) = 0 := by nlinarith
  exact sub_eq_zero.mp ((mul_eq_zero.mp hp).resolve_left (sub_ne_zero.mpr hne))

end Collatz.LiteratureRoundFour.ActualLawRigidity

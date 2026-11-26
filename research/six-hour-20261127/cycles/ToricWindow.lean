import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Algebra.Polynomial.Degree.TrailingDegree
import Mathlib.Data.Rat.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.Omega

/-! Finite algebra of cyclic clock differences. The analytical gcd bound on
algebraic tori and the asymptotic denominator statements are written proofs. -/

namespace ToricWindow

/-- Total native clock of the next `v` odd gaps. -/
def window (gap : ℕ → ℕ) (i v : ℕ) : ℕ :=
  ∑ j ∈ Finset.range v, gap (i + j)

variable {R : Type*} [CommRing R]

/-- Normalized carry term, with `t` representing the inverse of three. -/
def term (gap : ℕ → ℕ) (t : R) (i : ℕ) : R :=
  (2 : R) ^ window gap 0 i * t ^ i

theorem window_append (gap : ℕ → ℕ) (i j : ℕ) :
    window gap 0 (i + j) = window gap 0 i + window gap i j := by
  simp only [window, Nat.zero_add, Finset.sum_range_add]

theorem term_advance (gap : ℕ → ℕ) (t : R) (i v : ℕ) :
    term gap t (i + v) = (2 : R) ^ window gap i v * t ^ v * term gap t i := by
  simp only [term, window_append, pow_add]
  ring

theorem term_periodic (gap : ℕ → ℕ) (t : R) (p : ℕ)
    (hgap : ∀ i, gap (p + i) = gap i)
    (hclock : (2 : R) ^ window gap 0 p * t ^ p = 1) (i : ℕ) :
    term gap t (p + i) = term gap t i := by
  have hw : window gap p i = window gap 0 i := by simp [window, hgap]
  rw [term_advance, hw]
  simp [term, hclock]

theorem rotated_sum (c : ℕ → R) (p v : ℕ) (hc : ∀ i, c (p + i) = c i) :
    ∑ i ∈ Finset.range p, c (v + i) = ∑ i ∈ Finset.range p, c i := by
  have h := Finset.sum_range_add c v p
  rw [Nat.add_comm v p, Finset.sum_range_add, show
    (∑ i ∈ Finset.range v, c (p + i)) = ∑ i ∈ Finset.range v, c i by simp [hc]] at h
  exact add_left_cancel (by simpa only [add_comm (∑ i ∈ Finset.range p, c i)] using h.symm)

/-- The full cyclic carry times its clock-shift multiplier is supported
exactly on the exceptional window clocks. No inverse of the multiplier is used. -/
theorem sparse_window (gap : ℕ → ℕ) (t : R) (p u v : ℕ)
    (hgap : ∀ i, gap (p + i) = gap i)
    (hclock : (2 : R) ^ window gap 0 p * t ^ p = 1) :
    ((2 : R) ^ u * t ^ v - 1) * (∑ i ∈ Finset.range p, term gap t i) =
      ∑ i ∈ (Finset.range p).filter (fun i => window gap i v ≠ u),
        ((2 : R) ^ u - (2 : R) ^ window gap i v) * t ^ v * term gap t i := by
  classical
  have hrot := rotated_sum (term gap t) p v (term_periodic gap t p hgap hclock)
  rw [Finset.sum_filter]
  calc
    _ = (∑ i ∈ Finset.range p, ((2 : R) ^ u * t ^ v) * term gap t i) -
          ∑ i ∈ Finset.range p, term gap t (v + i) := by
        rw [hrot, ← Finset.mul_sum, sub_mul, one_mul]
    _ = _ := by
      rw [← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro i _
      rw [Nat.add_comm v i, term_advance]
      by_cases h : window gap i v = u
      · simp [h]
      · simp [h]
        ring

/-- Signed odd part of a difference of unequal powers of two. -/
def dyadicCore (u b : ℕ) : ℤ :=
  if b < u then (2 : ℤ) ^ (u - b) - 1 else -((2 : ℤ) ^ (b - u) - 1)

theorem difference_factor (u b : ℕ) :
    (2 : ℤ) ^ min u b * dyadicCore u b = (2 : ℤ) ^ u - 2 ^ b := by
  by_cases h : b < u
  · rw [dyadicCore, ite_eq_left h, min_eq_right h.le, mul_sub, ← pow_add,
        Nat.add_sub_of_le h.le, mul_one]
  · have h' : u ≤ b := Nat.le_of_not_gt h
    rw [dyadicCore, ite_eq_right h, min_eq_left h', mul_neg, mul_sub, ← pow_add,
        Nat.add_sub_of_le h', mul_one]
    ring

theorem core_mod_two (u b : ℕ) (hne : u ≠ b) :
    (dyadicCore u b : ZMod 2) = 1 := by
  have hz : (2 : ZMod 2) = 0 := by decide
  by_cases h : b < u
  · simp [dyadicCore, h, hz, (Nat.sub_pos_of_lt h).ne']
  · have h' : u < b := by omega
    simp [dyadicCore, h, hz, (Nat.sub_pos_of_lt h').ne']

theorem prefix_strict (gap : ℕ → ℕ) (hg : ∀ i, 0 < gap i) :
    StrictMono (window gap 0) := by
  apply strictMono_nat_of_lt_succ
  intro i
  simp [window, Finset.sum_range_succ, hg]

/-- Native clock at the left end of the difference of the two candidate dates. -/
def firstClock (gap : ℕ → ℕ) (u v i : ℕ) : ℕ :=
  min (window gap 0 i + u) (window gap 0 (i + v))

theorem firstClock_strict (gap : ℕ → ℕ) (hg : ∀ i, 0 < gap i) (u v : ℕ) :
    StrictMono (firstClock gap u v) := by
  intro i j hij
  have h := prefix_strict gap hg
  exact min_lt_min (Nat.add_lt_add_right (h hij) u) (h (Nat.add_lt_add_right hij v))

theorem firstClock_factor (gap : ℕ → ℕ) (u v i : ℕ) :
    firstClock gap u v i = window gap 0 i + min u (window gap i v) := by
  rw [firstClock, window_append, min_add_add_left]

theorem row_factor (gap : ℕ → ℕ) (hg : ∀ i, 0 < gap i) (u v i : ℕ) :
    (2 : ℤ) ^ firstClock gap u v 0 *
      (2 ^ (firstClock gap u v i - firstClock gap u v 0) * dyadicCore u (window gap i v)) =
    2 ^ window gap 0 i * (2 ^ u - 2 ^ window gap i v) := by
  have hle := (firstClock_strict gap hg u v).monotone (Nat.zero_le i)
  rw [← mul_assoc, ← pow_add, Nat.add_sub_of_le hle, firstClock_factor, pow_add,
      mul_assoc, difference_factor]

theorem inverse_power (t : R) (ht : (3 : R) * t = 1) (i : ℕ) :
    (3 : R) ^ i * t ^ i = 1 := by
  rw [← mul_pow, ht, one_pow]

/-- Normalized signed integer from every supplied exceptional row in a clock cut. -/
def cutResidual (gap : ℕ → ℕ) (u v stop : ℕ) (exceptional : Finset ℕ) : ℤ :=
  ∑ i ∈ exceptional, (3 : ℤ) ^ (stop - i) *
    2 ^ (firstClock gap u v i - firstClock gap u v 0) *
    dyadicCore u (window gap i v)

theorem cutResidual_mod_two (gap : ℕ → ℕ) (hg : ∀ i, 0 < gap i)
    (u v stop : ℕ) (exceptional : Finset ℕ) (h0 : 0 ∈ exceptional)
    (hfirst : u ≠ window gap 0 v) :
    (cutResidual gap u v stop exceptional : ZMod 2) = 1 := by
  have h2 : (2 : ZMod 2) = 0 := by decide
  have h3 : (3 : ZMod 2) = 1 := by decide
  simp only [cutResidual, Int.cast_sum, Int.cast_mul, Int.cast_pow, Int.cast_ofNat]
  rw [Finset.sum_eq_single_of_mem 0 h0]
  · simp [h3, core_mod_two u _ hfirst]
  · intro i _ hi
    have hlt := firstClock_strict gap hg u v (Nat.pos_of_ne_zero hi)
    simp [h2, (Nat.sub_pos_of_lt hlt).ne']

theorem cutResidual_ne_zero (gap : ℕ → ℕ) (hg : ∀ i, 0 < gap i)
    (u v stop : ℕ) (exceptional : Finset ℕ) (h0 : 0 ∈ exceptional)
    (hfirst : u ≠ window gap 0 v) :
    cutResidual gap u v stop exceptional ≠ 0 := by
  intro he
  have h := cutResidual_mod_two gap hg u v stop exceptional h0 hfirst
  rw [he, Int.cast_zero] at h
  exact zero_ne_one h

/-- Removing the cut's dyadic normalization recovers the integer difference
of all weighted clock terms, before any modulus or choice of inverse. -/
theorem cutResidual_factor (gap : ℕ → ℕ) (hg : ∀ i, 0 < gap i)
    (u v stop : ℕ) (exceptional : Finset ℕ) :
    (2 : ℤ) ^ firstClock gap u v 0 * cutResidual gap u v stop exceptional =
    ∑ i ∈ exceptional, 3 ^ (stop - i) * 2 ^ window gap 0 i *
      (2 ^ u - 2 ^ window gap i v) := by
  rw [cutResidual, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  have h := row_factor gap hg u v i
  calc
    _ = (3 : ℤ) ^ (stop - i) *
        (2 ^ firstClock gap u v 0 *
        (2 ^ (firstClock gap u v i - firstClock gap u v 0) * dyadicCore u (window gap i v))) := by ring
    _ = _ := by rw [h]; ring



theorem clear_ternary_weight (t : R) (ht : (3 : R) * t = 1) (stop v i : ℕ)
    (hi : i ≤ stop) :
    (3 : R) ^ (stop + v) * t ^ v * t ^ i = 3 ^ (stop - i) := by
  have h : stop + v = (stop - i) + i + v := by omega
  calc
    _ = 3 ^ (stop - i) * ((3 : R) ^ i * t ^ i) * ((3 : R) ^ v * t ^ v) := by
      rw [h, pow_add, pow_add]
      ring
    _ = _ := by rw [inverse_power t ht, inverse_power t ht]; simp

/-- Full normalized integer residual identity in any modular clock ring.
No inverse of the comparison window multiplier is required. -/
theorem cleared_sparse_window (gap : ℕ → ℕ) (hg : ∀ i, 0 < gap i)
    (t : R) (ht : (3 : R) * t = 1) (p u v stop : ℕ)
    (hgap : ∀ i, gap (p + i) = gap i)
    (hclock : (2 : R) ^ window gap 0 p * t ^ p = 1)
    (hstop : ∀ i, i < p → window gap i v ≠ u → i ≤ stop) :
    (3 : R) ^ (stop + v) * (((2 : R) ^ u * t ^ v - 1) *
      (∑ i ∈ Finset.range p, term gap t i)) =
    (2 : R) ^ firstClock gap u v 0 *
      (cutResidual gap u v stop ((Finset.range p).filter (fun i => window gap i v ≠ u)) : R) := by
  have hcast := congrArg (fun z : ℤ => (z : R))
    (cutResidual_factor gap hg u v stop ((Finset.range p).filter (fun i => window gap i v ≠ u)))
  simp only [Int.cast_sum, Int.cast_mul, Int.cast_sub, Int.cast_pow, Int.cast_ofNat] at hcast
  rw [hcast, sparse_window gap t p u v hgap hclock, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  obtain ⟨hp, hw⟩ := Finset.mem_filter.mp hi
  have h := clear_ternary_weight t ht stop v i (hstop i (Finset.mem_range.mp hp) hw)
  rw [← h, term]
  ring

section ValuationWidth

open Polynomial

/-- Width after clearing a Laurent monomial. Multiplication by a monomial
moves both ends and leaves this width unchanged. -/
def supportWidth (f : ℚ[X]) : ℕ := f.natDegree - f.natTrailingDegree

theorem supportWidth_mul {f g : ℚ[X]} (hf : f ≠ 0) (hg : g ≠ 0) :
    supportWidth (f * g) = supportWidth f + supportWidth g := by
  have hfd := natTrailingDegree_le_natDegree f
  have hgd := natTrailingDegree_le_natDegree g
  rw [supportWidth, natDegree_mul hf hg, natTrailingDegree_mul hf hg]
  unfold supportWidth
  omega

theorem supportWidth_monomial_shift {f : ℚ[X]} (hf : f ≠ 0) (l : ℕ) :
    supportWidth (f * X ^ l) = supportWidth f := by
  rw [supportWidth_mul hf (pow_ne_zero _ X_ne_zero)]
  simp [supportWidth, natTrailingDegree_X_pow]

/-- The 3-adic one-parameter specialization of a nonzero binomial divisor
has at most the width of every surviving multiple. The integer l is the
absolute valuation of the primitive character and c its rational value. -/
theorem specialized_degree_le_width (g residual : ℚ[X]) (c : ℚ) (l : ℕ)
    (hc : c ≠ 0) (hl : l ≠ 0) (hconstant : g.coeff 0 ≠ 0)
    (hres : residual ≠ 0) (hdiv : g.comp (C c * X ^ l) ∣ residual) :
    g.natDegree * l ≤ supportWidth residual := by
  let q : ℚ[X] := g.comp (C c * X ^ l)
  have hcoeff : q.coeff 0 ≠ 0 := by
    simpa [q, coeff_zero_eq_eval_zero, hl] using hconstant
  have hq : q ≠ 0 := by
    intro h
    simp [h] at hcoeff
  have hwidth : supportWidth q = g.natDegree * l := by
    rw [supportWidth, natTrailingDegree_eq_zero.mpr (.inr hcoeff), Nat.sub_zero]
    simp [q, natDegree_comp, natDegree_C_mul hc]
  obtain ⟨k, hk⟩ := hdiv
  have hk' : k ≠ 0 := by
    intro h
    exact hres (by simp [hk, h])
  change residual = q * k at hk
  rw [hk, supportWidth_mul hq hk', hwidth]
  exact Nat.le_add_right _ _

end ValuationWidth

#print axioms clear_ternary_weight
#print axioms cleared_sparse_window
#print axioms supportWidth_mul
#print axioms supportWidth_monomial_shift
#print axioms specialized_degree_le_width
#print axioms window_append
#print axioms term_advance
#print axioms term_periodic
#print axioms rotated_sum
#print axioms sparse_window
#print axioms difference_factor
#print axioms core_mod_two
#print axioms prefix_strict
#print axioms firstClock_strict
#print axioms firstClock_factor
#print axioms row_factor
#print axioms inverse_power
#print axioms cutResidual_factor
#print axioms cutResidual_mod_two
#print axioms cutResidual_ne_zero

end ToricWindow

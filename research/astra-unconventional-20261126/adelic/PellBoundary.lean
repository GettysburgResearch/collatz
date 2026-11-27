import Mathlib.Algebra.Field.ZMod
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Exact algebra of the Pell-unit edge, quadratic trace gap and a rational Bloch boundary.
The source is an ordinary odd state when its physical clock is used below. -/

namespace Collatz.PellBoundary

set_option autoImplicit false

section FieldAlgebra

variable {K : Type*} [Field K]

/-- The norm-one trace-square relation behind the physical Pell lift. -/
theorem pell_traces {b c : K} (hc : c^2 - b^2 = 1) :
    (c+b)*(c-b) = 1 ∧ (c+b)^2 + (c-b)^2 = 4*b^2+2 := by
  constructor
  · linear_combination hc
  · linear_combination 2*hc

/-- Factorization of the punctured-line equation for an actual adjacent pair of units. -/
theorem punctured_edge {k u w : K} (hu : u ≠ 0) (hw : w ≠ 0)
    (h : w-w⁻¹ = k*(u+u⁻¹)) :
    (1-k*u/w)*(1+k*u*w) = 1+k^2 := by
  field_simp [hu, hw] at h ⊢
  linear_combination k*h

/-- The two rational arguments in Abel's five-term relation reduce to the edge parameters. -/
theorem abel_arguments {x y v s : K} (hv : v ≠ 1) (hs : s ≠ -1)
    (hx : (1+x)*(1-v) = 1+x*y)
    (hy : (1-y)*(1+s) = 1+x*y) (hden : 1+x*y ≠ 0) :
    y*(1+x)/(1+x*y) = s/(1+s) ∧
    (-x)*(1-y)/(1+x*y) = -v/(1-v) := by
  have h1 : 1-v ≠ 0 := sub_ne_zero.mpr (Ne.symm hv)
  have h2 : 1+s ≠ 0 := by intro he; apply hs; linear_combination he
  constructor
  · apply (div_eq_div_iff hden h2).mpr
    linear_combination -hy
  · apply (div_eq_div_iff hden h1).mpr
    linear_combination -hx

/-- The ratio trace of two units with the same quadratic conjugation gives Fricke's conic. -/
theorem fricke {u w : K} (hu : u ≠ 0) (hw : w ≠ 0) :
    let s := u+u⁻¹
    let t := w+w⁻¹
    let r := w/u+u/w
    s^2+t^2-r*s*t+r^2-4 = 0 := by
  dsimp
  field_simp [hu, hw]
  ring

/-- The affine trace relation pushes the conic to an integer quadratic with an odd
leading coefficient for a physical shortcut word. -/
theorem eliminate_trace {d g e s t r : K} (affine : d*t = g*s+e)
    (conic : s^2+t^2-r*s*t+r^2-4 = 0) :
    (d^2+g^2-d*g*r)*s^2 + (2*g-d*r)*e*s + e^2 + d^2*(r^2-4) = 0 := by
  linear_combination d^2*conic - (d*t+g*s+e-d*r*s)*affine

end FieldAlgebra

/-- The numerator giving separation of the quadratic-unit trace from the rational slope
and its reciprocal is odd whenever the word has positive dyadic clock. -/
theorem trace_grid (h m : ℕ) (r : ℤ) :
    (2^(h+1) : ℤ)^2 + (3^m : ℤ)^2 - 2^(h+1)*3^m*r ≠ 0 := by
  intro hz
  have hm := congrArg (Int.castRingHom (ZMod 2)) hz
  simp only [map_zero, map_sub, map_add, map_mul, map_pow, map_ofNat] at hm
  change ((2 : ZMod 2)^(h+1))^2 + ((3 : ZMod 2)^m)^2 - 2^(h+1)*3^m*(r : ZMod 2) = 0 at hm
  rw [show (2 : ZMod 2) = 0 by decide, show (3 : ZMod 2) = 1 by decide] at hm
  simp at hm

/-- Additive valuation of a quotient of natural numbers. -/
def valQuot (p n d : ℕ) : ℤ := (n.factorization p : ℤ) - (d.factorization p : ℤ)

/-- The (3,p) exterior-product coordinate of z ∧ (1-z), z=1/(3x+1). -/
def cycleCoordinate (x p : ℕ) : ℤ :=
  valQuot 3 1 (3*x+1) * valQuot p (3*x) (3*x+1) -
    valQuot p 1 (3*x+1) * valQuot 3 (3*x) (3*x+1)

/-- This coordinate records exactly the odd-prime valuation of the successor on an odd
cycle, where all states are prime to three. -/
theorem ordinary_coordinate (x y a p : ℕ) (hx : 0 < x) (hy : 0 < y)
    (hp : p.Prime) (hp2 : p ≠ 2) (hx3 : ¬ 3 ∣ x) (edge : 2^a*y = 3*x+1) :
    cycleCoordinate x p = y.factorization p := by
  have h30 : (3*x+1).factorization 3 = 0 := Nat.factorization_eq_zero_of_not_dvd (by omega)
  have h31 : (3*x).factorization 3 = 1 := by
    rw [Nat.factorization_mul (by decide) hx.ne']
    simp [Nat.factorization_eq_zero_of_not_dvd hx3, Nat.Prime.factorization_self (by decide : Nat.Prime 3)]
  have h2p : (2^a).factorization p = 0 := by
    apply Nat.factorization_eq_zero_of_not_dvd
    intro hd
    exact hp2 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp (hp.dvd_of_dvd_pow hd))
  have hpy : (3*x+1).factorization p = y.factorization p := by
    rw [← edge, Nat.factorization_mul (pow_ne_zero _ (by decide)) hy.ne']
    change (2^a).factorization p + y.factorization p = y.factorization p
    rw [h2p, zero_add]
  simp [cycleCoordinate, valQuot, h30, h31, hpy]

#print axioms pell_traces
#print axioms punctured_edge
#print axioms abel_arguments
#print axioms fricke
#print axioms eliminate_trace
#print axioms trace_grid
#print axioms ordinary_coordinate

end Collatz.PellBoundary

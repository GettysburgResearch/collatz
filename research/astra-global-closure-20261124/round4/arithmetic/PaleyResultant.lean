import Mathlib.RingTheory.Polynomial.Resultant.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Tactic.Ring

/-! Algebraic kernels of the full-denominator bound.  The modular roots may
live in a ring with zero divisors.  In particular these statements do not
replace a numerical gcd by its radical. -/
namespace Collatz.PaleyResultant

/-- Conjugate quadratic periods have sum `-1` and product `c`. -/
theorem period_quadratic {R : Type*} [CommRing R] (f b c : R)
    (hs : f + b = -1) (hp : f * b = c) : f ^ 2 + f + c = 0 := by
  rw [← hp]
  calc
    f ^ 2 + f + f * b = f * (f + b + 1) := by ring
    _ = 0 := by rw [hs]; simp

/-- Clearing the physical carry scale never requires it to be a unit. -/
theorem scaled_error {R : Type*} [CommRing R] (f e b c : R)
    (hf : f ^ 2 + f + c = 0) (he : e = -(b * f)) :
    e ^ 2 - b * e + c * b ^ 2 = 0 := by
  rw [he]
  calc
    (-(b*f))^2 - b * (-(b*f)) + c*b^2 = b^2 * (f^2 + f + c) := by ring
    _ = 0 := by rw [hf, mul_zero]

/-- A coprime change of generator reads all signed error positions at once. -/
theorem short_exponent {G : Type*} [Group G] (t : G) (N b u a s : ℤ)
    (hN : t ^ N = 1) (hbu : N ∣ b * u - 1) (hs : N ∣ s - u * a) :
    (t ^ b) ^ u = t ∧ (t ^ b) ^ s = t ^ a := by
  have eqpow (m n : ℤ) (h : N ∣ m - n) : t ^ m = t ^ n := by
    obtain ⟨k, hk⟩ := h
    have h' : m = n + N * k := by rw [← hk]; abel
    rw [h', zpow_add, zpow_mul, hN, one_zpow, mul_one]
  constructor
  · rw [← zpow_mul]
    simpa only [zpow_one] using eqpow _ _ hbu
  · rw [← zpow_mul]
    apply eqpow
    obtain ⟨v, hv⟩ := hbu
    obtain ⟨h, hh⟩ := hs
    refine ⟨v * a + b * h, ?_⟩
    calc
      b * s - a = (b * u - 1) * a + b * (s - u * a) := by ring
      _ = N * (v * a + b * h) := by rw [hv, hh]; ring

/-- A simultaneous modular root gives divisibility by the entire modulus. -/
theorem full_resultant_dvd (m : ℕ) (F G : Polynomial ℤ) (z : ZMod m)
    (hdeg : F.natDegree ≠ 0 ∨ G.natDegree ≠ 0)
    (hF : F.eval₂ (Int.castRingHom (ZMod m)) z = 0)
    (hG : G.eval₂ (Int.castRingHom (ZMod m)) z = 0) :
    (m : ℤ) ∣ F.resultant G := by
  apply (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mp
  obtain ⟨p, q, _, _, he⟩ :=
    Polynomial.exists_mul_add_mul_eq_C_resultant F G (le_refl _) (le_refl _) hdeg
  have hx := congrArg (Polynomial.eval₂RingHom (Int.castRingHom (ZMod m)) z) he
  simpa [Polynomial.eval₂RingHom, Polynomial.eval₂_add, Polynomial.eval₂_mul, hF, hG] using hx.symm

/-- Reduced residue algebra forces common divisibility in a putative
ramified square.  The proof works even when `(p)` is not a prime ideal. -/
theorem ramified_square {R : Type*} [CommRing R] [IsDomain R] {p a b : R}
    (hp : p ≠ 0) (hred : ∀ t : R, p ∣ t ^ 2 → p ∣ t)
    (hs : a ^ 2 = -p * b ^ 2) : p ∣ a ∧ p ∣ b := by
  have ha : p ∣ a := hred _ ⟨-(b ^ 2), by rw [hs]; ring⟩
  obtain ⟨v, hv⟩ := ha
  have he : p * (p * v ^ 2) = p * (-(b ^ 2)) := by
    calc
      p * (p * v ^ 2) = a ^ 2 := by rw [hv]; ring
      _ = p * (-(b ^ 2)) := by rw [hs]; ring
  have hc := mul_left_cancel₀ hp he
  refine ⟨⟨v, hv⟩, hred _ ⟨-(v ^ 2), ?_⟩⟩
  calc
    b ^ 2 = -(p * v ^ 2) := by rw [hc, neg_neg]
    _ = p * -(v ^ 2) := by ring

#print axioms period_quadratic
#print axioms scaled_error
#print axioms short_exponent
#print axioms full_resultant_dvd
#print axioms ramified_square
end Collatz.PaleyResultant

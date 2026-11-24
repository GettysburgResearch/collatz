import Mathlib

set_option autoImplicit false
open scoped BigOperators

namespace PointwiseFiber

/-- Cleared carry equation with the exact prescribed target retained. -/
theorem different_carries_different_sources
    (p e : ℕ) (q x y c d : ℤ)
    (hx : (3:ℤ)^p*x+c = (2:ℤ)^e*q)
    (hy : (3:ℤ)^p*y+d = (2:ℤ)^e*q)
    (hcd : c ≠ d) : x ≠ y := by
  intro h
  rw [h] at hx
  apply hcd
  linarith

/-- A bounded real offset keeps every inverse candidate above half its scale. -/
theorem bounded_offset_height
    (G q beta x : ℚ) (hG : 0 ≤ G) (hq : 1 ≤ q)
    (hb0 : 0 ≤ beta) (hb1 : beta ≤ 1/2)
    (hx : x = G*(q-beta)) :
    G*q/2 ≤ x ∧ x ≤ G*q := by
  have hlow : 0 ≤ q/2-beta := by linarith
  constructor
  · rw [hx]
    nlinarith [mul_nonneg hG hlow]
  · rw [hx]
    nlinarith [mul_nonneg hG hb0]

/-- Two fine unit cells per image; normalized harmonic mass is multiplicity/G. -/
theorem pressure_identity (p e : ℕ) (N : ℚ) :
    (N / (2*(2:ℚ)^e)) / (1/(2*(3:ℚ)^p)) =
      N / ((2:ℚ)^e/(3:ℚ)^p) := by
  have h2 : (2:ℚ)^e ≠ 0 := pow_ne_zero _ (by norm_num)
  have h3 : (3:ℚ)^p ≠ 0 := pow_ne_zero _ (by norm_num)
  field_simp [h2, h3] <;> ring

/-- The exact finite low-fiber incidence bound used before Borel–Cantelli.
    The index set need not consist of any random samples. -/
theorem bad_incidence_bound {A : Type*} [DecidableEq A]
    (s : Finset A) (n : A → ℕ) (M : ℕ) :
    (∑ a ∈ s.filter (fun a => n a < M), n a) ≤ s.card*M := by
  classical
  calc
    (∑ a ∈ s.filter (fun a => n a < M), n a) ≤
        ∑ _a ∈ s.filter (fun a => n a < M), M := by
      apply Finset.sum_le_sum
      intro a ha
      exact Nat.le_of_lt (Finset.mem_filter.mp ha).2
    _ = (s.filter (fun a => n a < M)).card*M := by simp
    _ ≤ s.card*M :=
      Nat.mul_le_mul_right M (Finset.card_le_card (Finset.filter_subset _ _))

/-- The two-arm labels are inherited by every actual common-clock inverse. -/
theorem inherit_pair {A : Type*} (T : A → A) (f : A → Bool)
    (hinv : ∀ z, f (T z) = f z)
    (x y q r : A) (e : ℕ)
    (hx : (T^[e]) x = q) (hy : (T^[e]) y = r) :
    (f x, f y) = (f q, f r) := by
  have hiter : ∀ (k : ℕ) (z : A), f ((T^[k]) z) = f z := by
    intro k
    induction k with
    | zero => intro z; rfl
    | succ k ih =>
      intro z
      rw [Function.iterate_succ_apply', hinv, ih]
  have h1 := hiter e x
  have h2 := hiter e y
  rw [hx] at h1
  rw [hy] at h2
  rw [h1, h2]

#print axioms different_carries_different_sources
#print axioms bounded_offset_height
#print axioms pressure_identity
#print axioms bad_incidence_bound
#print axioms inherit_pair

end PointwiseFiber

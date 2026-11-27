import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic.Ring

/-! The finite character-sum step used on a torsion component. -/

namespace Collatz.InfiniteDescent.FourierSupport

variable {K : Type*} [Field K]

def expSum (s : List K) (c : K → K) (n : ℕ) : K :=
  (s.map fun x => c x * x ^ n).sum

@[simp] theorem expSum_cons (a : K) (s : List K) (c : K → K) (n : ℕ) :
    expSum (a :: s) c n = c a * a ^ n + expSum s c n := by simp [expSum]

theorem eliminate (s : List K) (c : K → K) (a : K) (n : ℕ) :
    expSum s c (n+1) - a * expSum s c n =
      expSum s (fun x => (x-a) * c x) n := by
  induction s with
  | nil => simp [expSum]
  | cons x s ih => simp only [expSum_cons, pow_succ]; rw [← ih]; ring

theorem zero_if_coefficients_zero (s : List K) (c : K → K) (n : ℕ)
    (hz : ∀ a ∈ s, c a = 0) : expSum s c n = 0 := by
  induction s with
  | nil => simp [expSum]
  | cons a s ih =>
    rw [expSum_cons, hz a (by simp), ih (fun x hx => hz x (by simp [hx]))]
    simp

/-- A sum of powers with distinct bases cannot vanish throughout a block
of length equal to its number of nonzero coefficients. -/
theorem coefficients_of_zero_block (s : List K) (c : K → K)
    (hd : s.Nodup) (hz : ∀ i < s.length, expSum s c i = 0) :
    ∀ x ∈ s, c x = 0 := by
  induction s generalizing c with
  | nil => simp
  | cons a s ih =>
    have hnodup := List.nodup_cons.mp hd
    have htail : ∀ i < s.length, expSum s (fun x => (x-a) * c x) i = 0 := by
      intro i hi
      have hrec := eliminate (a :: s) c a i
      rw [hz (i+1) (by simpa using hi), hz i (by simp; omega)] at hrec
      simpa using hrec.symm
    have hmul := ih (fun x => (x-a) * c x) hnodup.2 htail
    have hcoeff : ∀ x ∈ s, c x = 0 := by
      intro x hx
      have hne : x ≠ a := fun he => hnodup.1 (he ▸ hx)
      exact (mul_eq_zero.mp (hmul x hx)).resolve_left (sub_ne_zero.mpr hne)
    have ht0 := zero_if_coefficients_zero s c 0 hcoeff
    have ha := hz 0 (by simp)
    simp [ht0] at ha
    intro x hx
    rcases List.mem_cons.mp hx with hx | hx
    · simpa [hx] using ha
    · exact hcoeff x hx

theorem translate (s : List K) (c : K → K) (m n : ℕ) :
    expSum s c (m+n) = expSum s (fun x => c x * x^m) n := by
  induction s with
  | nil => simp [expSum]
  | cons a s ih => simp only [expSum_cons, ih, pow_add]; ring

theorem nonzero_on_every_block (s : List K) (c : K → K) (m : ℕ)
    (hd : s.Nodup) {x : K} (hx : x ∈ s) (hx0 : x ≠ 0) (hc : c x ≠ 0) :
    ∃ i < s.length, expSum s c (m+i) ≠ 0 := by
  by_contra! h
  have ht : ∀ i < s.length, expSum s (fun y => c y * y ^ m) i = 0 := by
    intro i hi
    rw [← translate, h i hi]
  exact (mul_ne_zero hc (pow_ne_zero _ hx0))
    (coefficients_of_zero_block s _ hd ht x hx)

#print axioms coefficients_of_zero_block
#print axioms nonzero_on_every_block

end Collatz.InfiniteDescent.FourierSupport

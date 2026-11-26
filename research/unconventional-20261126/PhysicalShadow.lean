import PeriodicWindows
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith

/-!
The common-word arithmetic used in the fixed-source record argument.
The topological extraction of such a word is a separate written theorem.
No universal convergence hypothesis is asserted here.
-/
namespace PhysicalShadow

open PeriodicWindows

theorem word_clock (w : List Bool) : (word w).clock = w.length := by
  induction w with
  | nil => rfl
  | cons b w ih =>
    cases b <;> simp [word, join, letter, ih, Nat.add_comm]

theorem itinerary_length (n : ℕ) (x : ℤ) : (itinerary n x).length = n := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih => simp [itinerary, ih]

theorem actual_clock (n : ℕ) (x : ℤ) : (word (itinerary n x)).clock = n := by
  rw [word_clock, itinerary_length]

/-- A rational shadow with one fixed denominator following the very same
    physical prefix forces divisibility by the *entire shortcut clock*. -/
theorem common_prefix_divides (n : ℕ) (x D a b : ℤ)
    (hshadow : (2 : ℤ)^n * b =
      3^(word (itinerary n x)).grade * a + D * (word (itinerary n x)).carry) :
    (2 : ℤ)^n ∣ D*x-a := by
  have hz : defect (word (itinerary n x)) D a b = 0 := by
    apply genuine_zero
    simpa only [actual_clock] using hshadow
  simpa only [actual_clock] using no_defect_divides (actual_trace n x) D a b hz

theorem zero_of_all_dyadic_divisors (a : ℤ)
    (h : ∀ n : ℕ, (2 : ℤ)^n ∣ a) : a = 0 := by
  have hp : ∀ n : ℕ, n < 2^n := by
    intro n
    induction n with
    | zero => decide
    | succ n ih => rw [pow_succ]; omega
  have hn := Int.natAbs_dvd_natAbs.mpr (h a.natAbs)
  simp only [Int.natAbs_pow] at hn
  by_contra ha
  have ha' : 0 < a.natAbs := Int.natAbs_pos.mpr ha
  have hle := Nat.le_of_dvd ha' hn
  exact (not_le_of_gt (hp a.natAbs)) hle

/-- The common denominator may have any prime factors. The conclusion is
    equality of the two initial values, not convergence of either orbit. -/
theorem infinite_shadow_unique (x D a : ℤ) (b : ℕ → ℤ)
    (hshadow : ∀ n : ℕ, (2 : ℤ)^n * b n =
      3^(word (itinerary n x)).grade * a + D * (word (itinerary n x)).carry) :
    D*x = a := by
  have hd : D*x-a = 0 := zero_of_all_dyadic_divisors _ (fun n =>
    common_prefix_divides n x D a (b n) (hshadow n))
  omega

theorem negative_shadow_excludes_positive (x D a : ℤ) (b : ℕ → ℤ)
    (hx : 0 < x) (hD : 0 < D) (ha : a ≤ 0)
    (hshadow : ∀ n : ℕ, (2 : ℤ)^n * b n =
      3^(word (itinerary n x)).grade * a + D * (word (itinerary n x)).carry) :
    False := by
  have he := infinite_shadow_unique x D a b hshadow
  have hp := mul_pos hD hx
  omega

/-- A finite exact quantitative version: a different fixed rational shadow
    cannot agree longer than the binary size of the cleared initial gap. -/
theorem finite_shadow_height (n : ℕ) (x D a b : ℤ) (hne : D*x ≠ a)
    (hshadow : (2 : ℤ)^n * b =
      3^(word (itinerary n x)).grade * a + D * (word (itinerary n x)).carry) :
    2^n ≤ (D*x-a).natAbs := by
  have hd := Int.natAbs_dvd_natAbs.mpr (common_prefix_divides n x D a b hshadow)
  simp only [Int.natAbs_pow] at hd
  exact Nat.le_of_dvd (Int.natAbs_pos.mpr (sub_ne_zero.mpr hne)) hd

#print axioms word_clock
#print axioms itinerary_length
#print axioms actual_clock
#print axioms common_prefix_divides
#print axioms zero_of_all_dyadic_divisors
#print axioms infinite_shadow_unique
#print axioms negative_shadow_excludes_positive
#print axioms finite_shadow_height

end PhysicalShadow

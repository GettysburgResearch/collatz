import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.RingTheory.Coprime.Lemmas

namespace Collatz.RotationOccupation

/-- Cleared odd edges. The last target can be the even intermediate just
    after the common part of an unequal final division. -/
def Along (q : ℤ) : List ℕ → ℤ → ℤ → Prop
  | [], x, y => x = y
  | a :: u, x, y => ∃ v : ℤ, 2 ^ a * v = 3 * x + q ∧ Along q u v y

theorem subtractAlong {q : ℤ} (w : List ℕ) {x y u v : ℤ}
    (hx : Along q w x y) (hu : Along q w u v) :
    2 ^ w.sum * (y-v) = 3 ^ w.length * (x-u) := by
  induction w generalizing x u with
  | nil =>
    change x = y at hx
    change u = v at hu
    simp [hx, hu]
  | cons a tail ih =>
    obtain ⟨x', ex, px⟩ := hx
    obtain ⟨u', eu, pu⟩ := hu
    have e : (2 : ℤ)^a*(x'-u') = 3*(x-u) := by
      rw [mul_sub, mul_sub, ex, eu]
      ring
    have h := ih px pu
    simp only [List.sum_cons, List.length_cons, pow_add, pow_succ]
    calc
      2^a * 2^tail.sum * (y-v) = 2^a * (2^tail.sum*(y-v)) := by ring
      _ = 2^a * (3^tail.length*(x'-u')) := by rw [h]
      _ = 3^tail.length * (2^a*(x'-u')) := by ring
      _ = 3^tail.length * 3 * (x-u) := by rw [e]; ring

/-- At the last departure the two exponents may differ. Stopping both tracks
    after their common minimum b gives true integral intermediate targets. -/
theorem partialLast {q x y : ℤ} {b d : ℕ}
    (h : 2^(b+d)*y = 3*x+q) : Along q [b] x (2^d*y) := by
  refine ⟨2^d*y, ?_, rfl⟩
  rw [pow_add] at h
  simpa only [mul_assoc] using h

/-- The full past and remaining future pay different primes at the same date. -/
theorem interiorLattice {q x₀ x₁ x₂ y₀ y₁ y₂ : ℤ} {past future : List ℕ}
    (px : Along q past x₀ x₁) (py : Along q past y₀ y₁)
    (fx : Along q future x₁ x₂) (fy : Along q future y₁ y₂) :
    (3 : ℤ)^past.length * 2^future.sum ∣ x₁-y₁ := by
  have hp := subtractAlong past px py
  have hf := subtractAlong future fx fy
  have co : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by decide⟩
  have a : (3 : ℤ)^past.length ∣ x₁-y₁ :=
    (co.symm.pow (m := past.length) (n := past.sum)).dvd_of_dvd_mul_left
      ⟨x₀-y₀, hp⟩
  have b : (2 : ℤ)^future.sum ∣ x₁-y₁ :=
    (co.pow (m := future.sum) (n := future.length)).dvd_of_dvd_mul_left
      ⟨x₂-y₂, hf.symm⟩
  exact (co.symm.pow (m := past.length) (n := future.sum)).mul_dvd a b

/-- Two different positive lattice points in a low shell cost more,
    in the shell ceiling, than one lattice spacing. -/
theorem shellGap {g x y cap : ℤ} (hg : 0 < g) (hx : 0 < x) (hxy : x < y)
    (hy : y ≤ cap) (hd : g ∣ y-x) : g < cap := by
  obtain ⟨t, ht⟩ := hd
  have htpos : 0 < t := by
    by_contra! hn
    have h := mul_nonpos_of_nonneg_of_nonpos hg.le hn
    omega
  have ht1 : 1 ≤ t := by omega
  have h := mul_le_mul_of_nonneg_left ht1 hg.le
  simp only [mul_one] at h
  omega

theorem fullLengthFloor (past future : List ℕ)
    (h : future.length ≤ future.sum) :
    (2 : ℤ)^(past.length+future.length) ≤ 3^past.length * 2^future.sum := by
  rw [pow_add]
  exact mul_le_mul (pow_le_pow_left₀ (by decide) (by decide) _)
    (pow_le_pow_right₀ (by decide) h) (by positivity) (by positivity)

theorem multiplicityCost (n : ℕ) :
    2 * n ≤ 2 + n * (n-1) := by
  cases n with
  | zero => decide
  | succ m =>
    cases m with
    | zero => decide
    | succ k =>
      simp only [Nat.succ_sub_one]
      nlinarith

#print axioms subtractAlong
#print axioms partialLast
#print axioms interiorLattice
#print axioms shellGap
#print axioms fullLengthFloor
#print axioms multiplicityCost

end Collatz.RotationOccupation

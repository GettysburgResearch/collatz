import Mathlib.RingTheory.Coprime.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-! Exact divisibility under an arbitrary contiguous replacement in a closed shortcut word.
The six coefficients are the affine numerators and dyadic denominators of the two prefixes
and their common suffix. -/

namespace Collatz.SixHour.CycleSurgery

def determinant (a A b B : ℤ) : ℤ := A*B-a*b

def fullCarry (A c b d : ℤ) : ℤ := b*c+A*d

def difference (x a A c a' A' c' : ℤ) : ℤ := (A'*a-A*a')*x+A'*c-A*c'

theorem eliminated_suffix {x a A c a' A' c' b B d : ℤ}
    (original : determinant a A b B * x = fullCarry A c b d) :
    A * (determinant a' A' b B * x - fullCarry A' c' b d)
      = b * difference x a A c a' A' c' := by
  unfold determinant fullCarry difference at *
  linear_combination A' * original

/-- Every multiple that clears the edited carry also clears the short-block difference,
and conversely. This keeps the full modulus at all prime powers. -/
theorem all_multiples {x a A c a' A' c' b B d : ℤ}
    (original : determinant a A b B * x = fullCarry A c b d)
    (unitA : IsCoprime (determinant a' A' b B) A)
    (unitB : IsCoprime (determinant a' A' b B) b) (t : ℤ) :
    determinant a' A' b B ∣ t * fullCarry A' c' b d ↔
    determinant a' A' b B ∣ t * difference x a A c a' A' c' := by
  have he := eliminated_suffix (a' := a') (A' := A') (c' := c') original
  constructor
  · rintro ⟨q, hq⟩
    apply unitB.dvd_of_dvd_mul_left
    use A*(t*x-q)
    linear_combination -t * he - A * hq
  · rintro ⟨q, hq⟩
    apply unitA.dvd_of_dvd_mul_left
    use A*t*x-b*q
    linear_combination -t * he - b * hq

theorem delete_initial_odd (x : ℤ) :
    difference x 3 2 1 1 2 0 = 2 * (2*x+1) := by
  unfold difference
  ring

end Collatz.SixHour.CycleSurgery

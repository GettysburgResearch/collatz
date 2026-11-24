import Std

/-!
An interval of edges with canonical digit one cannot create a positive carry
from zero. This module proves the resulting finite support restriction.
-/

namespace Collatz.RunSupport

/-- A zero carry persists to the end of a run of digit-one edges. -/
theorem zero_persists
    (g b k : Nat → Nat)
    (gap_pos : ∀ i, 1 ≤ g i)
    (carry : ∀ i, g i + k (i + 1) = b i + 3 * k i)
    (start len : Nat)
    (init : k start = 0)
    (ones : ∀ i, start ≤ i → i < start + len → b i = 1) :
    k (start + len) = 0 := by
  induction len with
  | zero => simpa using init
  | succ len ih =>
    have hprev : k (start + len) = 0 := ih (by
      intro i hlow hhigh
      apply ones i hlow
      omega)
    have hdigit : b (start + len) = 1 :=
      ones (start + len) (by omega) (by omega)
    have he := carry (start + len)
    have hg := gap_pos (start + len)
    rw [hprev, hdigit] at he
    change k (start + len + 1) = 0
    omega

/-- The positive vertices in a digit-one component form an initial segment. -/
theorem positive_prefix
    (g b k : Nat → Nat)
    (gap_pos : ∀ i, 1 ≤ g i)
    (carry : ∀ i, g i + k (i + 1) = b i + 3 * k i)
    (i j : Nat) (hij : i ≤ j)
    (ones : ∀ t, i ≤ t → t < j → b t = 1)
    (hj : 0 < k j) : 0 < k i := by
  apply Classical.byContradiction
  intro hn
  have hi : k i = 0 := by omega
  have hlen : i + (j - i) = j := by omega
  have hz := zero_persists g b k gap_pos carry i (j - i) hi (by
    simpa only [hlen] using ones)
  rw [hlen] at hz
  omega

end Collatz.RunSupport

#print axioms Collatz.RunSupport.zero_persists
#print axioms Collatz.RunSupport.positive_prefix

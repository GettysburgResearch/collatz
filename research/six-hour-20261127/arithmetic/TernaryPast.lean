import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.TernaryPast

/-- A genuine past with the two allowed multipliers. Allowing all signed
integer witnesses makes the progression obstruction stronger. -/
def Past : ℕ → ℤ → Prop
  | 0, _ => True
  | n+1, y => ∃ x, Past n x ∧ (3*x+1=2*y ∨ 3*x+1=4*y)

private theorem extend_divisibility {n : ℕ} {m d e : ℤ}
    (cop : IsCoprime (3 : ℤ) m) (rel : 3*e = m*d) (h : (3 : ℤ)^n ∣ e) :
    (3 : ℤ)^(n+1) ∣ d := by
  apply cop.pow_left.dvd_of_dvd_mul_left
  obtain ⟨t, ht⟩ := h
  refine ⟨t, ?_⟩
  rw [← rel, ht, pow_succ]
  ring

/-- Three endpoints in arithmetic progression with n binary predecessors
must already be identical modulo 3^n. -/
theorem progression_spacing (n : ℕ) {x y z : ℤ}
    (hx : Past n x) (hy : Past n y) (hz : Past n z) (ap : x+z=2*y) :
    (3 : ℤ)^n ∣ y-x := by
  induction n generalizing x y z with
  | zero => simp
  | succ n ih =>
    obtain ⟨a, ha, ea⟩ := hx
    obtain ⟨b, hb, eb⟩ := hy
    obtain ⟨c, hc, ec⟩ := hz
    rcases ea with ea | ea <;> rcases eb with eb | eb <;> rcases ec with ec | ec
    all_goals first
      | exfalso; omega
      | have prev : a+c=2*b := by omega
        have div := ih ha hb hc prev
        first
          | exact extend_divisibility (m := 2) ⟨1, -1, by norm_num⟩ (by omega) div
          | exact extend_divisibility (m := 4) ⟨-1, 1, by norm_num⟩ (by omega) div

/-- There is no nonconstant three-term progression in the simultaneous
all-depth survivor set, even when its points belong to different components. -/
theorem no_progression {x y z : ℤ} (hx : ∀ n, Past n x) (hy : ∀ n, Past n y)
    (hz : ∀ n, Past n z) (ap : x+z=2*y) : x=y ∧ y=z := by
  let n := (y-x).natAbs
  have d := progression_spacing n (hx n) (hy n) (hz n) ap
  have bound := Int.natAbs_dvd_natAbs.mpr d
  rw [Int.natAbs_pow] at bound
  change (3:ℕ)^n ∣ n at bound
  have zero : n=0 := by
    by_contra nonzero
    have := Nat.le_of_dvd (Nat.pos_of_ne_zero nonzero) bound
    have small : n<(3:ℕ)^n := Nat.lt_pow_self (by decide)
    omega
  have eqn : y-x=0 := Int.natAbs_eq_zero.mp zero
  omega

/-- The three unordered pair sums of two distinct ternary trits have
different residues. This is the local energy split. -/
theorem pair_sums_split (a b : Fin 3) (hne : a ≠ b) :
    (2*a.val)%3 ≠ (a.val+b.val)%3 ∧
    (2*a.val)%3 ≠ (2*b.val)%3 ∧ (a.val+b.val)%3 ≠ (2*b.val)%3 := by
  revert a b
  decide

#print axioms progression_spacing
#print axioms no_progression
#print axioms pair_sums_split

end Collatz.TernaryPast

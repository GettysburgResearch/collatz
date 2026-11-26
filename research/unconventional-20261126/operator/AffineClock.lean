module

public import Mathlib.Logic.Function.Iterate
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-! Uniqueness of the arrival clock from its affine slope, and the at-most-one
accidental root principle for local ordinary realization. -/
@[expose] public section

namespace OrdinaryOperatorClock

theorem odd_three_pow (p : ℕ) : 3^p % 2 = 1 := by
  induction p with
  | zero => rfl
  | succ p ih =>
    rw [pow_succ]
    omega

theorem unique_two_exponent (p q b f : ℕ)
    (h : 3^p*2^b = 3^q*2^f) : b=f := by
  induction b generalizing f with
  | zero =>
    cases f with
    | zero => rfl
    | succ f =>
      simp only [pow_zero, mul_one, pow_succ 2 f, ← mul_assoc] at h
      have hp := odd_three_pow p
      omega
  | succ b ih =>
    cases f with
    | zero =>
      simp only [pow_zero, mul_one, pow_succ 2 b, ← mul_assoc] at h
      have hq := odd_three_pow q
      omega
    | succ f =>
      simp only [pow_succ 2 b, pow_succ 2 f, ← mul_assoc] at h
      have h' : 3^p*2^b = 3^q*2^f := by omega
      exact congrArg Nat.succ (ih f h')

theorem clocks_of_equal_slope
    (p q f b p' q' f' b' : ℕ)
    (h : ((3:ℚ)^p*2^b)/((3:ℚ)^q*2^f) =
         ((3:ℚ)^p'*2^b')/((3:ℚ)^q'*2^f')) :
    (f : ℤ)-b = (f' : ℤ)-b' := by
  have hc := (div_eq_div_iff (by positivity : (3:ℚ)^q*2^f ≠ 0)
    (by positivity : (3:ℚ)^q'*2^f' ≠ 0)).mp h
  have hn : 3^p*2^b*(3^q'*2^f') = 3^p'*2^b'*(3^q*2^f) := by exact_mod_cast hc
  have ht : 3^(p+q')*2^(b+f') = 3^(p'+q)*2^(b'+f) := by
    calc
      3^(p+q')*2^(b+f') = 3^p*2^b*(3^q'*2^f') := by rw [pow_add,pow_add]; ring
      _ = 3^p'*2^b'*(3^q*2^f) := hn
      _ = 3^(p'+q)*2^(b'+f) := by rw [pow_add,pow_add]; ring
  have hv := unique_two_exponent _ _ _ _ ht
  omega

theorem eq_germ_of_two_roots (a b c d x y : ℚ) (hxy : x ≠ y)
    (hx : a*x+b = c*x+d) (hy : a*y+b = c*y+d) :
    a=c ∧ b=d := by
  have h : (a-c)*(x-y) = 0 := by nlinarith
  have hac : a=c := sub_eq_zero.mp ((mul_eq_zero.mp h).resolve_right (sub_ne_zero.mpr hxy))
  exact ⟨hac, by simpa [hac] using hx⟩

theorem no_second_root_of_distinct_germs (a b c d x y : ℚ)
    (hne : (a,b) ≠ (c,d)) (hx : a*x+b = c*x+d)
    (hy : a*y+b = c*y+d) : x=y := by
  by_contra hxy
  rcases eq_germ_of_two_roots a b c d x y hxy hx hy with ⟨rfl,rfl⟩
  exact hne rfl

end OrdinaryOperatorClock
#print axioms OrdinaryOperatorClock.odd_three_pow
#print axioms OrdinaryOperatorClock.unique_two_exponent
#print axioms OrdinaryOperatorClock.clocks_of_equal_slope
#print axioms OrdinaryOperatorClock.eq_germ_of_two_roots
#print axioms OrdinaryOperatorClock.no_second_root_of_distinct_germs

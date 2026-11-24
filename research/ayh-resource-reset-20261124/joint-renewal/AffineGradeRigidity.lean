import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-! Ordered and crossed two-arm cylinder comparisons retain the absolute
corrected grade. The input equalities are the integer endpoint slope equations. -/

namespace CollatzShell.EntranceGrades

theorem two_point_slope {a b c d x y : ℚ} (ne : x ≠ y)
    (at_x : a*x+b=c*x+d) (at_y : a*y+b=c*y+d) : a=c := by
  have product : (a-c)*(x-y)=0 := by nlinarith
  exact sub_eq_zero.mp ((mul_eq_zero.mp product).resolve_right (sub_ne_zero.mpr ne))

private theorem valMul {A B : Nat} (hA : A≠0) (hB : B≠0) (p : Nat) :
    (A*B).factorization p = A.factorization p+B.factorization p := by
  rw [Nat.factorization_mul hA hB]; rfl

private theorem valPow (c h p : Nat) :
    (c^h).factorization p = h*c.factorization p := by
  simp [Nat.factorization_pow]

private theorem digits_val (A t s : Nat) (pos : A≠0) :
    (A*2^t*3^s).factorization 2=A.factorization 2+t ∧
    (A*2^t*3^s).factorization 3=A.factorization 3+s := by
  have two : (2:Nat).factorization 2=1 := Nat.prime_two.factorization_self
  have three : (3:Nat).factorization 3=1 := Nat.prime_three.factorization_self
  have off₂ : (2:Nat).factorization 3=0 := Nat.factorization_eq_zero_of_not_dvd (by decide)
  have off₃ : (3:Nat).factorization 2=0 := Nat.factorization_eq_zero_of_not_dvd (by decide)
  constructor <;>
    rw [valMul (A:=A*2^t) (B:=3^s) (mul_ne_zero pos (by positivity)) (by positivity),
        valMul (A:=A) (B:=2^t) pos (by positivity), valPow, valPow] <;>
    simp [two,three,off₂,off₃]

/-- The change in each grade is prescribed by the source slope ratio. -/
theorem slope_signature {A B a b p q : Nat} (hA : A≠0) (hB : B≠0)
    (same : A*2^b*3^p=B*2^a*3^q) :
    (b:Int)-a=(B.factorization 2:Int)-A.factorization 2 ∧
    (q:Int)-p=(A.factorization 3:Int)-B.factorization 3 := by
  have vA := digits_val A b p hA
  have vB := digits_val B a q hB
  rw [same] at vA
  omega

private theorem trit_vals {A : Nat} (hA : A≠0) (s : Nat) :
    (A*3^s).factorization 2=A.factorization 2 ∧
    (A*3^s).factorization 3=A.factorization 3+s := by
  simpa using digits_val A 0 s hA

/-- For a head of arbitrary trit deletion depth s, ordered fusions on a
cylinder shift both arm clocks, and both odd counts, by the same integers. -/
theorem ordered_head_shifts {A B s a₁ a₂ b₁ b₂ p₁ p₂ q₁ q₂ : Nat}
    (hA : A≠0) (hB : B≠0)
    (child : (A*3^s)*2^b₁*3^p₁=(B*3^s)*2^a₁*3^q₁)
    (parent : A*2^b₂*3^p₂=B*2^a₂*3^q₂) :
    (b₁:Int)-a₁=(b₂:Int)-a₂ ∧ (q₁:Int)-p₁=(q₂:Int)-p₂ := by
  have h₁ := slope_signature (mul_ne_zero hA (by positivity)) (mul_ne_zero hB (by positivity)) child
  have h₂ := slope_signature hA hB parent
  have vA := trit_vals hA s
  have vB := trit_vals hB s
  omega

/-- Crossed fusions reverse the signed physical gap and reflect the signed
odd-count gap about -s once the matched common tails are restored. -/
theorem crossed_head_shifts {A B s a₁ a₂ b₁ b₂ p₁ p₂ q₁ q₂ : Nat}
    (hA : A≠0) (hB : B≠0)
    (newChild : A*2^b₁*3^p₂=(B*3^s)*2^a₂*3^q₁)
    (newParent : (A*3^s)*2^b₂*3^p₁=B*2^a₁*3^q₂) :
    (b₁:Int)-a₂=(b₂:Int)-a₁ ∧
    ((q₁:Int)-p₂)-((q₂:Int)-p₁)= -2*(s:Int) := by
  have h₁ := slope_signature hA (mul_ne_zero hB (by positivity)) newChild
  have h₂ := slope_signature (mul_ne_zero hA (by positivity)) hB newParent
  have vA := trit_vals hA s
  have vB := trit_vals hB s
  omega

#print axioms two_point_slope
#print axioms slope_signature
#print axioms ordered_head_shifts
#print axioms crossed_head_shifts

end CollatzShell.EntranceGrades

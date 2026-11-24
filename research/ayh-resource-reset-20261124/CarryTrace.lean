import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Abel
import Mathlib.Tactic.NormNum

/-! Natural matrix carry defects vanish on every returning digit path. -/
namespace CarryTrace
open Matrix
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
abbrev Mat (ι : Type*) := Matrix ι ι ℕ

/-- The six carry defects sum to a single nonnegative commutator defect. -/
theorem aggregate (a b e f g u v w x y z : Mat ι)
    (ae : a*e = e*a+u) (af : a*f = e*b+v) (ag : a*g = f*a+w)
    (be : b*e = f*b+x) (bf : b*f = g*a+y) (bg : b*g = g*b+z) :
    (a+b)*(e+f+g) = (e+f+g)*(a+b)+(u+v+w+x+y+z) := by
  simp only [add_mul, mul_add, ae, af, ag, be, bf, bg]
  abel

/-- A weighted trace identity over naturals, with no Perron hypotheses. -/
theorem trace_zero (P Q S : Mat ι) (h : P*Q = Q*P+S) (k : ℕ) :
    (S*(P+Q)^k).trace = 0 := by
  let M := P+Q
  have hm : P*M = M*P+S := by
    dsimp [M]; rw [mul_add, add_mul, h]; abel
  have ht : ((P*M)*M^k).trace = ((M*P)*M^k).trace := by
    calc
      ((P*M)*M^k).trace = (P * M^(k+1)).trace := by rw [mul_assoc, pow_succ']
      _ = ((P*M^k)*M).trace := by rw [mul_assoc, pow_succ]
      _ = (M*(P*M^k)).trace := trace_mul_comm _ _
      _ = ((M*P)*M^k).trace := by rw [mul_assoc]
  rw [hm, add_mul, trace_add] at ht
  exact Nat.add_left_cancel (ht.trans (Nat.add_zero _).symm)

/-- A positive return in a matrix power forces zero slack on the reverse edge. -/
theorem zero_on_return (P Q S : Mat ι) (h : P*Q = Q*P+S)
    (k : ℕ) (i j : ι) (hret : 0 < ((P+Q)^k) j i) : S i j = 0 := by
  have hz := trace_zero P Q S h k
  have hd : (S*(P+Q)^k) i i = 0 :=
    (Finset.sum_eq_zero_iff.mp hz) i (Finset.mem_univ i)
  rw [Matrix.mul_apply] at hd
  have hc := (Finset.sum_eq_zero_iff.mp hd) j (Finset.mem_univ j)
  exact (Nat.mul_eq_zero.mp hc).resolve_right (Nat.ne_of_gt hret)

/-- Any nonnegative summand of the slack has the same returning-path exactness. -/
theorem summand_zero_on_return (P Q S A : Mat ι) (h : P*Q = Q*P+S)
    (hA : ∀ i j, A i j ≤ S i j) (k : ℕ) (i j : ι)
    (hret : 0 < ((P+Q)^k) j i) : A i j = 0 := by
  exact Nat.eq_zero_of_le_zero ((hA i j).trans_eq (zero_on_return P Q S h k i j hret))
end CarryTrace

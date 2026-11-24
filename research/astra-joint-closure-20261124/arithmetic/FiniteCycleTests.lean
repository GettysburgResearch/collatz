import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Finite return identities for the local cycle construction. The word
count, CRT construction, and irrational padding are written proofs. -/
namespace FiniteCycleTests

variable {R : Type*} [CommRing R]

def evenBranch (h x : R) := h*x
def oddBranch (h x : R) := h*(3*x+1)

/-- Swapping two branches changes only the intercept. Here h is 1/2. -/
theorem branch_swap (h x : R) (inverseTwo : 2*h=1) :
    oddBranch h (evenBranch h x) - evenBranch h (oddBranch h x) = h*h := by
  unfold evenBranch oddBranch
  calc
    _ = h - h*h := by ring
    _ = (1-2*h)*h + h*h := by ring
    _ = h*h := by rw [inverseTwo]; ring

/-- Four copies of this intercept difference generate translation by one. -/
theorem translation_generator (h : R) (inverseTwo : 2*h=1) :
    4*(h*h)=1 := by
  calc
    _ = (2*h)*(2*h) := by ring
    _ = 1 := by rw [inverseTwo]; ring

/-- At a prescribed outside factor E, a unit carry forces the whole E
into the denominator of any integral presentation of a fixed point. -/
theorem outside_divides_denominator (E D A a b u v : Int)
    (clock : E ∣ D) (bezout : u*E+v*A=1) (fixedPoint : D*a=A*b) :
    E ∣ b := by
  obtain ⟨s, hs⟩ := clock
  refine ⟨u*b+v*s*a, ?_⟩
  calc
    b = (u*E+v*A)*b := by rw [bezout]; ring
    _ = u*E*b+v*(A*b) := by ring
    _ = E*(u*b+v*s*a) := by rw [← fixedPoint, hs]; ring

/-- Lift past the valuation common to slope defect and carry. The
remaining clock is a unit at the test modulus; the integer numerator
then represents the prescribed residue times its denominator. -/
theorem saturated_residue (K M d A a b r z u v : Int)
    (positive : 0<K) (carry : A=(K*d)*r+K*M*z)
    (fixedPoint : (K*d)*a=A*b) (bezout : u*M+v*d=1) :
    M ∣ a-r*b := by
  have cancel : K*(d*(a-r*b))=K*(M*z*b) := by
    calc
      _ = (K*d)*a - (K*d)*r*b := by ring
      _ = K*(M*z*b) := by rw [fixedPoint, carry]; ring
  have reduced : d*(a-r*b)=M*z*b := mul_left_cancel₀ (ne_of_gt positive) cancel
  refine ⟨u*(a-r*b)+v*z*b, ?_⟩
  calc
    a-r*b = (u*M+v*d)*(a-r*b) := by rw [bezout]; ring
    _ = u*M*(a-r*b)+v*(d*(a-r*b)) := by ring
    _ = M*(u*(a-r*b)+v*z*b) := by rw [reduced]; ring

#print axioms branch_swap
#print axioms translation_generator
#print axioms outside_divides_denominator
#print axioms saturated_residue

end FiniteCycleTests

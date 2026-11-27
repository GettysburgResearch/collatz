module

public import FiberRouting
import all TernaryItinerary

public section
namespace Collatz.Itinerary.InverseHeight

set_option autoImplicit false

/-- Pull a literal shortcut path backwards from both q+3^h*t and q.
All inverse steps at q remain positive integral. The large predecessor is
at least as large relative to its target as the small predecessor. -/
theorem pullback (h n q t : Nat) (pos : 0<q) (hit : run h n=q+3^h*t) :
    ∃ y a, 0<y ∧ run h y=q ∧ n=y+a*t ∧ (q+3^h*t)*y≤q*n := by
  induction h generalizing n t with
  | zero =>
    exact ⟨q,1,pos,rfl,by simpa [run] using hit,by simp [run] at hit; simp [hit,Nat.mul_comm]⟩
  | succ h ih =>
    let b := q+3^(h+1)*t
    have eq : q+3^h*(3*t)=b := by dsimp [b]; rw [Nat.pow_succ]; ac_rfl
    have tail : run h (step n)=q+3^h*(3*t) := by rw [eq]; exact hit
    obtain ⟨y,a,yp,runs,split,ratio⟩ := ih (step n) (3*t) tail
    rw [eq] at ratio
    have twice := Nat.mul_le_mul_left 2 ratio
    by_cases even : n%2=0
    · have actual : n=2*step n := by simp [step,even]; omega
      have next : step (2*y)=y := by simp [step]
      refine ⟨2*y,6*a,by omega,?_,?_,?_⟩
      · change run h (step (2*y))=q
        rwa [next]
      · calc
          n = 2*(y+a*(3*t)) := actual.trans (congrArg (2*·) split)
          _ = 2*y+6*a*t := by grind
      · change b*(2*y)≤q*n
        calc
          b*(2*y) = 2*(b*y) := by ac_rfl
          _ ≤ 2*(q*step n) := twice
          _ = q*n := by
            conv => rhs; rw [actual]
            ac_rfl
    · have edge : 2*step n=3*n+1 := by simp [step,even]; omega
      let D := 2*a*t
      have arith : 2*y+3*D=3*n+1 := by
        calc
          2*y+3*D = 2*(y+a*(3*t)) := by dsimp [D]; grind
          _ = 2*step n := congrArg (2*·) split.symm
          _ = 3*n+1 := edge
      let u := n-D
      have un : n=u+D := by dsimp [u]; omega
      have edge' : 2*y=3*u+1 := by omega
      have uo : u%2=1 := by omega
      have up : 0<u := by omega
      have next : step u=y := by simp [step,uo]; omega
      refine ⟨u,2*a,up,?_,un,?_⟩
      · change run h (step u)=q
        rwa [next]
      · change b*u≤q*n
        have bounded : b*(3*u+1)≤q*(3*n+1) := by
          rw [←edge',←edge]
          simpa only [Nat.mul_left_comm b 2,Nat.mul_left_comm q 2] using twice
        have bb : q≤b := Nat.le_add_right _ _
        rw [Nat.mul_add,Nat.mul_one,Nat.mul_add,Nat.mul_one] at bounded
        have l : b*(3*u)=3*(b*u) := by ac_rfl
        have r : q*(3*n)=3*(q*n) := by ac_rfl
        rw [l,r] at bounded
        omega

/-- An entire ternary class at height h has no smaller ordinary predecessor
at any clock through h, allowing every possible positive ancestor. -/
theorem no_smaller_before (h t j x : Nat) (short : j≤h)
    (hit : run j x=1+3^h*t) : 1+3^h*t≤x := by
  have exponent : h=j+(h-j) := by omega
  have scale : 1+3^h*t=1+3^j*(3^(h-j)*t) := by
    conv => lhs; rw [exponent,Nat.pow_add]
    ac_rfl
  obtain ⟨y,_,yp,_,_,ratio⟩ := pullback j x 1 _ (by decide) (hit.trans scale)
  rw [←scale,Nat.one_mul] at ratio
  exact Nat.le_trans (Nat.le_mul_of_pos_right _ yp) ratio

#print axioms pullback
#print axioms no_smaller_before
end Collatz.Itinerary.InverseHeight

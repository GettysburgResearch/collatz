module

public import TowerFrontierAffine
import all TernaryItinerary

public section
namespace Collatz.Itinerary.PairInverseRays

set_option autoImplicit false

/-- An affine family of positive-integer inverse candidates, evaluated at t. -/
abbrev Ray := Nat × Nat

@[expose] def value (a : Ray) (t : Nat) := a.1+a.2*t

/-- Invert h steps on the entire target progression b+d*t. A branch whose
odd inverse requires restricting t is omitted. With 3^h dividing d every
ordinary branch is present. The parameter t is shared across all arms. -/
@[expose] def rays : Nat → Nat → Nat → List Ray
  | 0, b, d => [(b,d)]
  | h+1, b, d => rays h (2*b) (2*d) ++
      (if b%3=2 ∧ d%3=0 then rays h ((2*b-1)/3) (2*d/3) else [])

private theorem odd_preimage (b d t : Nat) (hb : b%3=2) (hd : d%3=0) :
    step ((2*b-1)/3+(2*d/3)*t)=b+d*t := by
  have base : 3*((2*b-1)/3)+1=2*b := by omega
  have slope : 3*(2*d/3)=2*d := by omega
  have eq : 3*((2*b-1)/3+(2*d/3)*t)+1=2*(b+d*t) := by
    rw [Nat.mul_add,Nat.mul_add,←Nat.mul_assoc 3,slope,Nat.mul_assoc 2 d t]
    omega
  have odd : ((2*b-1)/3+(2*d/3)*t)%2=1 := by omega
  simp [step,odd,eq]

theorem ray_sound {h b d : Nat} {a : Ray} (mem : a∈rays h b d) (t : Nat) :
    run h (value a t)=b+d*t := by
  induction h generalizing a b d with
  | zero =>
    have eq : a=(b,d) := by simpa [rays] using mem
    simp [eq,run,value]
  | succ h ih =>
    rw [rays,List.mem_append] at mem
    rw [run_add h 1]
    change step (run h (value a t))=b+d*t
    rcases mem with even | odd
    · rw [ih even]
      have eq : 2*b+2*d*t=2*(b+d*t) := by grind
      simp [eq,step]
    · split at odd
      next yes => rw [ih odd,odd_preimage _ _ _ yes.1 yes.2]
      next => simp at odd

/-- Every ordinary predecessor at a common clock lies on a listed ray as
soon as the target stride contains that clock's power of three. -/
theorem ray_complete (h b d t x : Nat) (div : 3^h ∣ d)
    (hit : run h x=b+d*t) :
    ∃ a∈rays h b d, x=value a t := by
  induction h generalizing b d with
  | zero =>
    exact ⟨(b,d),by simp [rays],by simpa [run,value] using hit⟩
  | succ h ih =>
    obtain ⟨u,hu⟩ := div
    have mult : d=3*(3^h*u) := by rw [hu,Nat.pow_succ]; ac_rfl
    let y := run h x
    have last : step y=b+d*t := by
      rw [run_add h 1] at hit
      exact hit
    by_cases even : y%2=0
    · have eq : y=2*(b+d*t) := by simp [step,even] at last; omega
      have dy : 3^h∣2*d := ⟨6*u,by rw [mult]; grind⟩
      have path : run h x=2*b+2*d*t := by
        change y=_; rw [eq]; grind
      obtain ⟨a,mem,same⟩ := ih (2*b) (2*d) dy path
      exact ⟨a,List.mem_append_left _ mem,same⟩
    · have e : 3*y+1=2*(b+d*t) := by simp [step,even] at last; omega
      have hd : d%3=0 := by rw [mult]; simp
      have hdt : (d*t)%3=0 := by rw [mult,Nat.mul_assoc]; simp
      have hb : b%3=2 := by omega
      have path : run h x=(2*b-1)/3+(2*d/3)*t := by
        have aa : (2*d/3)*t=2*(3^h*u*t) := by
          have : 2*d/3=2*(3^h*u) := by rw [mult]; omega
          rw [this,Nat.mul_assoc]
        rw [aa]; change y=_
        have dt : d*t=3*(3^h*u*t) := by rw [mult,Nat.mul_assoc]
        rw [dt] at e
        omega
      have dy : 3^h∣2*d/3 := ⟨2*u,by
        have : 2*d/3=2*(3^h*u) := by rw [mult]; omega
        rw [this]; ac_rfl⟩
      obtain ⟨a,mem,same⟩ := ih _ _ dy path
      exact ⟨a,by simp only [rays,hb,hd,and_self,if_true,List.mem_append]; exact Or.inr mem,same⟩

#print axioms ray_sound
#print axioms ray_complete

end Collatz.Itinerary.PairInverseRays

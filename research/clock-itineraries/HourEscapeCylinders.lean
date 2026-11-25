module

public import EscapeRecords
import all EscapeRecords
import all FixedGate

public section
namespace Collatz.Itinerary.HourEscape

open Sparse FixedGate EscapeRecords
set_option autoImplicit false

private theorem pow_unit (s : Nat) : 2^s%3≠0 := by
  induction s with
  | zero => decide
  | succ s ih => rw [Nat.pow_succ]; omega

private theorem choose_digit (a h : Nat) (unit : h%3≠0) :
    ∃ d, (a+h*d)%3=1 := by
  by_cases h₀ : a%3=1
  · exact ⟨0,by simpa⟩
  by_cases h₁ : (a+h)%3=1
  · exact ⟨1,by simpa⟩
  exact ⟨2,by omega⟩

/-- Every finite chronological list of positive gaps occurs on an ordinary
positive odd orbit. The construction retains its exact odd successor at each step. -/
theorem realize_positive_word (es : List Nat) (valid : ∀ e ∈ es, 0<e) :
    ∃ x q, x%2=1 ∧ q%2=1 ∧ Path es x q := by
  induction es with
  | nil => exact ⟨1,1,rfl,rfl,.nil 1⟩
  | cons e es ih =>
    have ep := valid e (by simp)
    obtain ⟨y,q,yo,qo,p⟩ := ih (fun f h => valid f (by simp [h]))
    let h := 2^(e+1+es.sum)
    have unit : h%3≠0 := pow_unit _
    obtain ⟨d,one⟩ := choose_digit (2^e*y) h unit
    let y' := y+2*(2^es.sum*d)
    let q' := q+2*(3^es.length*d)
    have eq : 2^e*y'=2^e*y+h*d := by
      simp only [y',h,Nat.pow_add,Nat.mul_add,Nat.pow_one]
      ac_rfl
    have tern : (2^e*y')%3=1 := by rwa [eq]
    let x := (2^e*y')/3
    have div : 2^e*y'=3*x+1 := by dsimp [x]; omega
    have even : (2^e*y')%2=0 := by
      obtain ⟨v,hv⟩ := Nat.exists_eq_add_of_le (show 1≤e from ep)
      rw [hv,Nat.pow_add]
      change (2*2^v*y')%2=0
      rw [Nat.mul_assoc]; omega
    have xo : x%2=1 := by omega
    have y'o : y'%2=1 := by dsimp [y']; omega
    have q'o : q'%2=1 := by dsimp [q']; omega
    exact ⟨x,q',xo,q'o,.cons ⟨ep,xo,y'o,div⟩ (Shadow.translate p d)⟩

/-- Strict uncorrected clock growth along every nonempty terminal suffix. -/
def CriticalWord (es : List Nat) : Prop :=
  ∀ front tail, es=front++tail → tail≠[] → 2^tail.sum<3^tail.length

private theorem prefix_clock {es : List Nat} {x q : Nat} (p : Path es x q)
    (i : Nat) (bound : i≤es.length) : elapsed i x=(es.take i).sum := by
  induction p generalizing i with
  | nil =>
    obtain rfl : i=0 := by simpa using bound
    rfl
  | @cons x y q e es edge _ ih =>
    cases i with
    | zero => rfl
    | succ i =>
      have b : i≤es.length := by simpa using bound
      simp only [elapsed,gap_next edge,List.take_succ_cons,List.sum_cons,ih i b]

private theorem endpoint {es : List Nat} {x q : Nat} (p : Path es x q) :
    after es.length x=q := by
  induction p with
  | nil => rfl
  | cons edge _ ih => simpa [after,gap_next edge] using ih

/-- The word condition is a strict upper record for the actual ordinary orbit. -/
theorem critical_of_word {es : List Nat} {x q : Nat} (p : Path es x q)
    (word : CriticalWord es) : Critical x es.length := by
  unfold Critical
  intro i lt
  let front := es.take i
  let tail := es.drop i
  have decomp : es=front++tail := (List.take_append_drop i es).symm
  have flen : front.length=i := by simp [front,Nat.min_eq_left (Nat.le_of_lt lt)]
  have tlen : tail.length=es.length-i := by simp [tail]
  have nonempty : tail≠[] := by intro emp; rw [emp] at tlen; simp at tlen; omega
  have wt := word front tail decomp nonempty
  have sclock : elapsed es.length x=es.sum := by simpa using prefix_clock p es.length (by omega)
  have pc : elapsed i x=front.sum := prefix_clock p i (by omega)
  have sz : es.sum=front.sum+tail.sum := by simpa only [List.sum_append] using congrArg List.sum decomp
  have len : es.length=i+tail.length := by omega
  rw [sclock,pc,sz,Nat.pow_add,show 3^es.length=3^i*3^tail.length by rw [len,Nat.pow_add]]
  have scaled := Nat.mul_lt_mul_of_pos_left wt
    (Nat.mul_pos (Nat.two_pow_pos front.sum) (Nat.pow_pos (n:=i) (by decide : 0<3)))
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using scaled

/-- Each finite critical script occurs on an orbit whose very next odd value
after the strict record is any prescribed positive odd ternary unit. The
source and the record can both exceed an arbitrary bound. -/
theorem critical_word_to_target (es : List Nat) (valid : ∀ e ∈ es, 0<e)
    (word : CriticalWord es) (t B : Nat) (to_ : t%2=1) (tu : t%3≠0) :
    ∃ a q e, B<a ∧ B<q ∧ a%2=1 ∧ a%3≠0 ∧ Path es a q ∧
      Critical a es.length ∧ after es.length a=q ∧ Gap e q t ∧
      after (es.length+1) a=t := by
  obtain ⟨x,q,xo,qo,p⟩ := realize_positive_word es valid
  let m := 2*2^es.sum
  have unit : m%3≠0 := by
    change (2*2^es.sum)%3≠0
    rw [Nat.mul_comm,←Nat.pow_succ]
    exact pow_unit _
  obtain ⟨v,one⟩ := choose_digit (x+m*(B+1)) m unit
  let d := B+1+v
  let x₀ := x+2*(2^es.sum*d)
  let q₀ := q+2*(3^es.length*d)
  have x₀o : x₀%2=1 := by dsimp [x₀]; omega
  have q₀o : q₀%2=1 := by dsimp [q₀]; omega
  have x₀u : x₀%3=1 := by
    have norm : x₀=x+m*(B+1)+m*v := by
      dsimp only [x₀,d,m]
      rw [←Nat.mul_assoc,Nat.mul_add (2*2^es.sum) (B+1) v,Nat.add_assoc]
    rwa [norm]
  have bigX : B<x₀ := by
    have h := Nat.mul_le_mul_right d (Nat.two_pow_pos es.sum)
    dsimp [x₀]; dsimp [d] at *; omega
  have bigQ : B<q₀ := by
    have h := Nat.mul_le_mul_right d (Nat.pow_pos (n:=es.length) (by decide : 0<3))
    dsimp [q₀]; dsimp [d] at *; omega
  obtain ⟨e,D,_,_,edge⟩ := Shadow.one_gap_cylinder q₀o to_ tu (es.length+1)
  let a := x₀+2*(2^es.sum*(3*D))
  let z := q₀+2*(3^es.length*(3*D))
  have path : Path es a z := Shadow.translate (Shadow.translate p d) (3*D)
  have gap : Gap e z t := by
    simpa only [z,Nat.pow_succ,Nat.mul_assoc] using edge
  have post : after es.length a=z := endpoint path
  have ev : (2*2^es.sum)*(3*D)=3*((2*2^es.sum)*D) := by ac_rfl
  have odd : a%2=1 := by dsimp [a]; omega
  have u : a%3≠0 := by
    dsimp [a]; rw [←Nat.mul_assoc,ev]; omega
  refine ⟨a,z,e,by dsimp [a]; omega,by dsimp [z]; omega,odd,u,path,
    critical_of_word path word,post,gap,?_⟩
  rw [after_add,post]
  simp [after,gap_next gap]

#print axioms realize_positive_word
#print axioms critical_of_word
#print axioms critical_word_to_target

end Collatz.Itinerary.HourEscape

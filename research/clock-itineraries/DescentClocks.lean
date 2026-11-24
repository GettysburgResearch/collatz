module

public import FixedGate
public import SynchronousShadow

public section
namespace Collatz.Itinerary.DescentClocks

open Sparse
set_option autoImplicit false

/-- Any inverse word that compares its ordinary source to a larger
endpoint above two lies in the subcritical clock range. -/
theorem descent_clock {y b : Nat} (hy : y%2=1) (hq : 2<FixedGate.after b y)
    (smaller : y≤FixedGate.after b y) : 5*FixedGate.elapsed b y≤8*b := by
  let q := FixedGate.after b y
  have route := FixedGate.distortion hy hq
  have powBound := Nat.pow_le_pow_left smaller 5
  have high := Nat.le_trans route
    (Nat.mul_le_mul_left 100000 (Nat.mul_le_mul_left (2^(8*b)) powBound))
  change 59049*(2^(5*FixedGate.elapsed b y)*q^5)≤100000*(2^(8*b)*q^5) at high
  rw [←Nat.mul_assoc,←Nat.mul_assoc] at high
  have pos : 0<q^5 := Nat.pow_pos (by dsimp [q]; omega)
  have cancel := Nat.le_of_mul_le_mul_right high pos
  have strict : 2^(5*FixedGate.elapsed b y)<2^(8*b+1) := by
    rw [Nat.pow_succ]
    have := Nat.two_pow_pos (8*b)
    omega
  have := (Nat.pow_lt_pow_iff_right (by decide : 1<2)).1 strict
  omega

/-- Every word at the upper endpoint has an ordinary positive
realization at the lower endpoint of its ternary congruence class. -/
theorem lower_lift {es : List Nat} {x q : Nat} (p : Path es x q)
    {z d : Nat} (odd : z%2=1) (hq : q=z+2*(3^es.length*d)) :
    ∃ y, 0<y ∧ y%2=1 ∧ Path es y z ∧ x=y+2*(2^es.sum*d) := by
  induction p generalizing z d with
  | nil =>
    refine ⟨z,by omega,odd,.nil z,?_⟩
    simpa using hq
  | @cons x v q e es edge _ ih =>
    have hr : q=z+2*(3^es.length*(3*d)) := by
      simpa only [List.length_cons,Nat.pow_succ,Nat.mul_assoc] using hq
    obtain ⟨u,upos,uodd,tail,hu⟩ := ih odd hr
    let D := 2*(2^(e+es.sum)*d)
    have eqn := edge.eqn
    rw [hu,Nat.mul_add] at eqn
    have norm : 2^e*(2*(2^es.sum*(3*d)))=3*D := by
      simp only [D,Nat.pow_add]
      ac_rfl
    rw [norm] at eqn
    have big : 2≤2^e*u := by
      have k := Nat.pow_le_pow_right (by decide : 0<2) edge.pos
      change 2^1 ≤ 2^e at k
      simpa using Nat.mul_le_mul k upos
    have lt : D<x := by omega
    have splitX : x=(x-D)+D := by omega
    have even : D%2=0 := by dsimp [D]; omega
    have xodd := edge.oddSource
    have yodd : (x-D)%2=1 := by omega
    have small : Gap e (x-D) u := ⟨edge.pos,yodd,uodd,by omega⟩
    exact ⟨x-D,by omega,yodd,.cons small tail,by simpa [D] using splitX⟩

private theorem positive_scale {es : List Nat} {x q : Nat} (p : Path es x q)
    (hne : es≠[]) : 3^es.length*x<2^es.sum*q := by
  cases p with
  | nil => simp at hne
  | @cons x v q e es edge rest =>
    have h₁ := Shadow.affine rest
    have h₂ : 3^es.length*v≤2^es.sum*q := by omega
    have h₃ := Nat.mul_le_mul_left (2^e) h₂
    simp only [List.length_cons,Nat.pow_succ,List.sum_cons,Nat.pow_add]
    simp only [Nat.mul_assoc]
    have norm : 2^e*(3^es.length*v)=3^es.length*(3*x+1) := by
      rw [←edge.eqn]
      ac_rfl
    rw [norm,Nat.mul_add,Nat.mul_one] at h₃
    have := Nat.pow_pos (n:=es.length) (by decide : 0<3)
    omega

/-- A weak descent at a higher lift forces a strict descent of the same
word at every smaller positive odd representative of its cylinder. -/
theorem downward_descent {es : List Nat} {x q z d : Nat} (p : Path es x q)
    (hn : es≠[]) (odd : z%2=1) (hq : q=z+2*(3^es.length*d)) (hd : 0<d) (hx : x≤q) :
    ∃ y, 0<y ∧ y<z ∧ Path es y z := by
  obtain ⟨y,pos,_,p₀,eqn⟩ := lower_lift p odd hq
  refine ⟨y,pos,?_,p₀⟩
  by_cases le : z≤y
  · have bound := Nat.lt_of_le_of_lt (Nat.mul_le_mul_left (3^es.length) le)
      (positive_scale p₀ hn)
    have grow : 3^es.length<2^es.sum := by
      by_cases small : 2^es.sum≤3^es.length
      · have := Nat.mul_le_mul_right z small; omega
      · omega
    have := Nat.mul_lt_mul_of_pos_right grow hd
    omega
  · omega

/-- No positive odd root one modulo the full ternary word modulus
has a weakly smaller ancestor of that exact nonzero depth, at any clock. -/
theorem no_descent_at_one_cylinder {es : List Nat} {x q : Nat} (p : Path es x q)
    (hn : es≠[]) (hq : 1<q) (odd : q%2=1) (hmod : q%3^es.length=1) : q<x := by
  let D := q/3^es.length
  have splitQ : q=1+3^es.length*D := by
    simpa [hmod,D] using (Nat.mod_add_div q (3^es.length)).symm
  have powOdd (n : Nat) : 3^n%2=1 := by
    induction n with
    | zero => decide
    | succ n ih => rw [Nat.pow_succ,Nat.mul_mod,ih]
  have mult : (3^es.length*D)%2=D%2 := by
    rw [Nat.mul_mod,powOdd,Nat.one_mul,Nat.mod_mod]
  have doubled : D=2*(D/2) := by omega
  let d := D/2
  have dq : q=1+2*(3^es.length*d) := by
    calc
      q = 1+3^es.length*D := splitQ
      _ = 1+3^es.length*(2*d) := by rw [←show D=2*d from doubled]
      _ = _ := by ac_rfl
  have hd : 0<d := by
    by_cases h : d=0
    · simp [h] at dq; omega
    · omega
  by_cases le : x≤q
  · obtain ⟨y,pos,lt,_⟩ := downward_descent p hn (by decide : 1%2=1) dq hd le
    omega
  · omega

/-- An explicit one-gap predecessor of one is insulated from downward
comparisons at every depth from one through B. -/
theorem converging_obstruction (B : Nat) :
    let e := 2+2*3^B
    let q := (2^e-1)/3
    1<q ∧ q%2=1 ∧ Gap e q 1 ∧
      ∀ (es : List Nat) (x : Nat), es≠[] → es.length≤B → Path es x q → q<x := by
  dsimp only
  obtain ⟨w,hw⟩ := Shadow.ternary_stride B
  let u := 1+3*w
  have mult : 2^(2+2*3^B)=4*(1+3*3^B*u) := by
    rw [Nat.pow_add,Nat.pow_mul]
    change 4*4^(3^B)=_
    rw [hw]
  let q := (2^(2+2*3^B)-1)/3
  have hq : q=1+4*(3^B*u) := by
    dsimp [q]
    rw [mult]
    rw [show 3*3^B*u=3*(3^B*u) by ac_rfl]
    omega
  have pos := Nat.mul_pos (Nat.pow_pos (n:=B) (by decide : 0<3)) (by dsimp [u]; omega : 0<u)
  have odd : q%2=1 := by omega
  have realGap : Gap (2+2*3^B) q 1 := by
    refine ⟨by omega,odd,by decide,?_⟩
    rw [Nat.mul_one,mult,hq]
    grind
  refine ⟨by change 1<q; omega,odd,realGap,?_⟩
  intro es x hn len p
  have ⟨v,hv⟩ := Nat.pow_dvd_pow 3 len
  have powLarge : 1<3^es.length := by
    cases es with
    | nil => simp at hn
    | cons e tail =>
      simp only [List.length_cons,Nat.pow_succ]
      have := Nat.pow_pos (n:=tail.length) (by decide : 0<3)
      omega
  have eq : q=1+3^es.length*(4*v*u) := by rw [hq,hv]; ac_rfl
  have cls : q%3^es.length=1 := by rw [eq,Nat.add_mul_mod_self_left,Nat.mod_eq_of_lt powLarge]
  exact no_descent_at_one_cylinder p hn (by change 1<q; omega) odd cls

#print axioms descent_clock
#print axioms lower_lift
#print axioms downward_descent
#print axioms no_descent_at_one_cylinder
#print axioms converging_obstruction
end Collatz.Itinerary.DescentClocks

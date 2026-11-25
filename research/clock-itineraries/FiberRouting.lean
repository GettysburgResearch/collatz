module

public import FiberTransport
import all FiberTransport

public section
namespace Collatz.Itinerary.FiberRouting

open FiberTransport
set_option autoImplicit false

private theorem small_power (k r : Nat) (unit : r%3≠0) :
    ∃ e, 0<e ∧ e≤2*3^k ∧ 2^e%3^(k+1)=r%3^(k+1) := by
  let m := 3^(k+1)
  let P := 2*3^k
  have mp : 1<m := Nat.one_lt_pow (by omega) (by decide)
  have pp : 0<P := Nat.mul_pos (by decide) (Nat.pow_pos (by decide))
  obtain ⟨d,v,_,eq⟩ := large_dyadic_lift k 1 r 0 (by decide) unit
  have root : 2^d%m=r%m := by
    simp only [Nat.mul_one] at eq
    rw [eq]
    exact Nat.add_mul_mod_self_left _ _ _
  obtain ⟨u,factor,_⟩ := power_lift k
  have period : 2^P%m=1 := by
    change 2^(2*3^k)%3^(k+1)=1
    rw [factor,Nat.add_mul_mod_self_left,Nat.mod_eq_of_lt mp]
  have periods : ((2^P)^(d/P))%m=1 := by
    rw [Nat.pow_mod,period,Nat.one_pow,Nat.mod_eq_of_lt mp]
  have product : 2^d=2^(d%P)*(2^P)^(d/P) := by
    rw [←Nat.pow_mul,←Nat.pow_add,Nat.mod_add_div]
  have smaller : 2^(d%P)%m=r%m := by
    rw [product,Nat.mul_mod,periods,Nat.mul_one,Nat.mod_mod] at root
    exact root
  by_cases h : d%P=0
  · rw [h,Nat.pow_zero,Nat.mod_eq_of_lt mp] at smaller
    exact ⟨P,pp,Nat.le_refl _,period.trans smaller⟩
  · exact ⟨d%P,by omega,Nat.le_of_lt (Nat.mod_lt d pp),smaller⟩

private theorem gaps_from_equation {a f x b : Nat} (ha : 0<a) (hf : 0<f)
    (odd : b%2=1) (eq : 2^(a+f)*b=2^a+3+9*x) :
    ∃ y, Gap a x y ∧ Gap f y b := by
  let Z := 2^f*b
  have prod : 2^a*Z=2^a+3+9*x := by
    simpa only [Z,Nat.pow_add,Nat.mul_assoc] using eq
  have au : 2^a%3≠0 := by simpa using unit_pow_two a 1 (by decide)
  have rem : Z%3=1 := by
    have same := congrArg (·%3) prod
    change 2^a*Z%3=(2^a+3+9*x)%3 at same
    have rhs : (2^a+3+9*x)%3=2^a%3 := by omega
    rw [rhs,Nat.mul_mod] at same
    have A : 2^a%3=1 ∨ 2^a%3=2 := by omega
    have V : Z%3=0 ∨ Z%3=1 ∨ Z%3=2 := by omega
    rcases A with a1 | a1 <;> rcases V with v1 | v1 | v1 <;> simp_all
  let y := Z/3
  have second : Z=3*y+1 := by dsimp [y]; omega
  have first : 2^a*y=3*x+1 := by
    rw [second,Nat.mul_add,Nat.mul_one] at prod
    have reorder : 2^a*(3*y)=3*(2^a*y) := by ac_rfl
    rw [reorder] at prod
    omega
  have ev (e n : Nat) (he : 0<e) : (2^e*n)%2=0 := by
    cases e with
    | zero => omega
    | succ e => rw [Nat.pow_succ,Nat.mul_right_comm]; omega
  have yodd : y%2=1 := by
    have h : Z%2=0 := ev f b hf
    omega
  have xodd : x%2=1 := by have h := ev a y ha; omega
  exact ⟨y,⟨ha,xodd,yodd,first⟩,⟨hf,yodd,odd,second⟩⟩

/-- One threshold works for every odd unit target and every later clock.
The two odd steps begin on a prescribed ternary ray above a prescribed
parameter bound. -/
theorem exact_ray_at (z G B S b : Nat) (odd : b%2=1) (ub : b%3≠0)
    (ps : 2*3^(G+2)<S)
    (high : 2^(2*3^(G+2))+(3+9*z)+9*3^(G+1)*B<2^S*b) :
    ∃ v, B<v ∧ ∃ a f y, a+f=S ∧ a≤2*3^(G+2) ∧
      Gap a (z+3^(G+1)*v) y ∧ Gap f y b ∧
      2^S*b=2^a+3+9*(z+3^(G+1)*v) := by
  let m := 3^(G+1)
  let P := 2*3^(G+2)
  let shift := 3+9*z
  let cap := 2^P+shift+9*m*B
  change P<S at ps
  change cap<2^S*b at high
  let D := 2^S*b-shift
  have within (x y w : Nat) : y≤x+y+w := by omega
  have boundShift := within (2^P) shift (9*m*B)
  have dp : shift≤2^S*b := Nat.le_trans boundShift (Nat.le_of_lt high)
  have expand : 2^S*b=D+shift := by dsimp [D]; omega
  have du : D%3≠0 := by
    have unit := unit_pow_two S b ub
    dsimp [shift] at expand
    omega
  obtain ⟨a,apos,amax,res⟩ := small_power (G+2) D du
  change a≤P at amax
  have modEq : 2^a%(9*m)=D%(9*m) := by
    have modulus : 3^(G+2+1)=9*m := by dsimp [m]; rw [Nat.pow_succ,Nat.pow_succ 3 (G+1)]; omega
    rwa [modulus] at res
  have small := Nat.pow_le_pow_right (by decide : 0<2) amax
  have before : 2^P+shift+9*m*B<D+shift := by change cap<D+shift; rwa [←expand]
  have diff : 2^a+9*m*B<D := by omega
  let v := (D-2^a)/(9*m)
  have divs : 9*m ∣ D-2^a :=
    Nat.dvd_of_mod_eq_zero (Nat.sub_mod_eq_zero_of_mod_eq modEq.symm)
  have decomp : D=2^a+9*m*v := by
    have h := Nat.mul_div_cancel' divs
    change 9*m*v=D-2^a at h
    omega
  have vbig : B<v := by
    apply Classical.byContradiction
    intro notLarge
    have bound := Nat.mul_le_mul_left (9*m) (show v≤B by omega)
    omega
  let f := S-a
  have earlier := Nat.lt_of_le_of_lt amax ps
  have sf : a+f=S := by dsimp [f]; omega
  have fp : 0<f := by dsimp [f]; omega
  have eq : 2^(a+f)*b=2^a+3+9*(z+m*v) := by
    rw [sf,expand,decomp]
    dsimp [shift]
    grind
  obtain ⟨y,h1,h2⟩ := gaps_from_equation apos fp odd eq
  exact ⟨v,vbig,a,f,y,sf,amax,h1,h2,sf ▸ eq⟩

theorem exact_ray (z G B : Nat) :
    ∃ N, ∀ S, N≤S → ∀ b, b%2=1 → b%3≠0 →
      ∃ v, B<v ∧ ∃ a f y, a+f=S ∧ a≤2*3^(G+2) ∧
        Gap a (z+3^(G+1)*v) y ∧ Gap f y b ∧
        2^S*b=2^a+3+9*(z+3^(G+1)*v) := by
  let P := 2*3^(G+2)
  let c := (3+9*z)+9*3^(G+1)*B
  refine ⟨P+c+1,?_⟩
  intro S large b odd unit
  have gap (p t : Nat) : 2^p+t≤2^(p+t) := by
    induction t with
    | zero => simp
    | succ t ih =>
      rw [show p+(t+1)=(p+t)+1 by omega,Nat.pow_succ]
      have hp := Nat.two_pow_pos (p+t)
      omega
  have one := gap P (c+1)
  have two := Nat.pow_le_pow_right (by decide : 0<2) (show P+(c+1)≤S by omega)
  have three := Nat.le_mul_of_pos_right (2^S) (show 0<b by omega)
  apply exact_ray_at z G B S b odd unit (show P<S by omega)
  change 2^P+(3+9*z)+9*3^(G+1)*B<2^S*b
  have bound : 2^P+c+1≤2^S*b := by omega
  have strict : 2^P+c<2^S*b := Nat.lt_of_succ_le bound
  simpa only [c,Nat.add_assoc] using strict

/-- After the requested prefix, two exact odd gaps route a copy to any odd
unit at every sufficiently large common deadline. Each inverse clock row
at grade at most K is transported in both directions. -/
theorem exact_copies (q H K B : Nat) (hq : 0<q) :
    ∃ N, ∀ S, N≤S → ∀ b, b%2=1 → b%3≠0 →
      ∃ u, B<u ∧
        let q' := q+2^(H+1)*3^K*u
        parityPrefix (H+1) q'=parityPrefix (H+1) q ∧
        run (H+1+S) q'=b ∧
        (∃ a f y, a+f=S ∧ Gap a (run (H+1) q') y ∧ Gap f y b) ∧
        ∀ (es : List Nat), es.length≤K → ∀ x',
          Row es x' q' ↔ ∃ x, Row es x q ∧
            x'=x+2*2^es.sum*(2^H*3^(K-es.length)*u) := by
  let h := H+1
  let z := run h q
  let g := (TowerFrontier.track h q K).2
  obtain ⟨N,route⟩ := exact_ray z g B
  refine ⟨N,?_⟩
  intro S late b odd unit
  obtain ⟨v,large,a,f,y,sf,_,first,second,_⟩ := route S late b odd unit
  let u := 3*v
  let q' := q+2^h*3^K*u
  have atPrefix : run h q'=z+3^(g+1)*v := by
    rw [show run h q'=z+3^g*u by
      simpa only [q',z,g,track_value] using TowerFrontier.affine h q K u]
    dsimp only [u]
    rw [Nat.pow_succ]; ac_rfl
  refine ⟨u,by dsimp [u]; omega,?_,?_,?_,?_⟩
  · simpa only [Nat.mul_assoc,h] using same_prefix h q (3^K*u)
  · change run (h+S) q'=b
    rw [run_add,atPrefix,←sf,run_add,first.follow,second.follow]
  · exact ⟨a,f,y,sf,atPrefix.symm ▸ first,second⟩
  · intro es short x'
    have split : K=es.length+(K-es.length) := by omega
    have base : q'=q+2*3^es.length*(2^H*3^(K-es.length)*u) := by
      dsimp [q',h]
      conv => lhs; rw [split,Nat.pow_add 3,Nat.pow_succ 2 H]
      ac_rfl
    change Row es x' q' ↔ _
    rw [base]
    exact whole_row es q _ x' hq

#print axioms exact_ray_at
#print axioms exact_ray
#print axioms exact_copies
end Collatz.Itinerary.FiberRouting

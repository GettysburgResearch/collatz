import PhysicalWindow
import Mathlib.Data.Nat.Factorization.Basic

/-! Physical peak equality at two independently chosen clocks. -/
namespace Collatz.ClockSeparation
open Collatz.SourceDeletion Collatz.ShadowBarrier Collatz.PhysicalWindow

private theorem peak_error (h j : Nat) :
    ∃ e : Int, (2:Int)^h * run h (3^j-1) = 3^(j+odds h (3^j-1))+e ∧
      -(3:Int)^h≤e ∧ e≤(3:Int)^h := by
  let x:=3^j-1
  let p:=odds h x
  have ppos : 1≤(3:Nat)^j := Nat.pow_pos (by decide)
  have xc : (x:Int)=(3:Int)^j-1 := by
    dsimp [x]
    rw [Nat.cast_sub ppos]
    push_cast
    rfl
  have aff := congrArg (fun n : Nat => (n:Int)) (affine h x)
  push_cast at aff
  have bound := offset_bound h x
  have off : (offset h x:Int)≤(3:Int)^h := by exact_mod_cast (Nat.le_trans (Nat.le_add_right _ _) bound)
  have pc : (3:Int)^p≤(3:Int)^h := by exact_mod_cast Nat.pow_le_pow_right (by decide : 0<(3:Nat)) (odd_le h x)
  have po : 0≤(3:Int)^p := by positivity
  have co : 0≤(offset h x:Int) := by positivity
  refine ⟨(offset h x:Int)-3^p,?_,by omega,by omega⟩
  change (2:Int)^h*run h x=3^(j+p)+((offset h x:Int)-3^p)
  rw [aff,xc,pow_add]
  dsimp [p]
  ring

private theorem scale_error (h H : Nat) (small : h≤H) (e : Int)
    (left : -(3:Int)^h≤e) (right : e≤(3:Int)^h) :
    -(3:Int)^H ≤ (2:Int)^(H-h)*e ∧ (2:Int)^(H-h)*e ≤ (3:Int)^H := by
  have bound : (2:Int)^(H-h)*(3:Int)^h ≤ (3:Int)^H := calc
    _ ≤ (3:Int)^(H-h)*(3:Int)^h := by gcongr; norm_num
    _ = _ := by rw [←pow_add,Nat.sub_add_cancel small]
  have low := mul_le_mul_of_nonneg_left left (by positivity : 0≤(2:Int)^(H-h))
  have high := mul_le_mul_of_nonneg_left right (by positivity : 0≤(2:Int)^(H-h))
  rw [mul_neg] at low
  omega

private theorem factor_clock (a b c d : Nat)
    (same : (2:Nat)^a*3^b=2^c*3^d) : a=c ∧ b=d := by
  have va:=congrArg (fun n : Nat => n.factorization 2) same
  have vb:=congrArg (fun n : Nat => n.factorization 3) same
  simp [Nat.factorization_mul, Nat.factorization_pow, Nat.Prime.factorization,
    Nat.prime_two, Nat.prime_three] at va vb
  exact ⟨va,vb⟩

private theorem small_multiple (g d : Int) (positive : 0<g) (dg : g∣d)
    (low : -g<d) (high : d<g) : d=0 := by
  obtain ⟨u,rfl⟩:=dg
  by_cases uz : u=0
  · simp [uz]
  by_cases up : 1≤u
  · have q:=mul_le_mul_of_nonneg_left up (le_of_lt positive)
    rw [mul_one] at q
    omega
  · have un : u≤-1 := by omega
    have q:=mul_le_mul_of_nonneg_left un (le_of_lt positive)
    rw [mul_neg_one] at q
    omega

/-- A shared physical site high relative to the budget forces equality of
both clocks and both augmented ternary grades. -/
theorem high_meeting (h l H j t y : Nat) (hh : h≤H) (ll : l≤H)
    (high : 3*3^H < y) (native : run h (3^j-1)=y) (other : run l (3^t-1)=y) :
    h=l ∧ j+odds h (3^j-1)=t+odds l (3^t-1) := by
  let a:=j+odds h (3^j-1)
  let b:=t+odds l (3^t-1)
  obtain ⟨e,he,el,eu⟩:=peak_error h j
  obtain ⟨f,hf,fl,fu⟩:=peak_error l t
  rw [native] at he
  rw [other] at hf
  change (2:Int)^h*y=3^a+e at he
  change (2:Int)^l*y=3^b+f at hf
  have ly (k : Nat) : (y:Int)≤(2:Int)^k*y := by
    have o : (1:Int)≤(2:Int)^k := by exact_mod_cast (Nat.two_pow_pos k)
    simpa using mul_le_mul_of_nonneg_right o (by positivity : (0:Int)≤y)
  have eH : (3:Int)^h ≤ (3:Int)^H := by gcongr; norm_num
  have fH : (3:Int)^l ≤ (3:Int)^H := by gcongr; norm_num
  have hy : (3:Int)*3^H<y := by exact_mod_cast high
  have mina : 2*(3:Int)^H < (3:Int)^a := by linarith only [he,ly h,eu,eH,hy]
  have minb : 2*(3:Int)^H < (3:Int)^b := by linarith only [hf,ly l,fu,fH,hy]
  let g:=(3:Int)^min a b
  have gp : 2*(3:Int)^H<g := by
    rcases le_total a b with ab|ba
    · simpa only [g,min_eq_left ab] using mina
    · simpa only [g,min_eq_right ba] using minb
  let A:=(2:Int)^(H-h)*3^a
  let B:=(2:Int)^(H-l)*3^b
  have gd : g∣A-B := Int.dvd_sub
    (dvd_mul_of_dvd_right (pow_dvd_pow 3 (min_le_left a b)) _)
    (dvd_mul_of_dvd_right (pow_dvd_pow 3 (min_le_right a b)) _)
  have eqn : A-B=(2:Int)^(H-l)*f-2^(H-h)*e := by
    have sh:=congrArg (fun w : Int => 2^(H-h)*w) he
    have sl:=congrArg (fun w : Int => 2^(H-l)*w) hf
    rw [←mul_assoc,←pow_add,Nat.sub_add_cancel hh,mul_add] at sh
    rw [←mul_assoc,←pow_add,Nat.sub_add_cancel ll,mul_add] at sl
    dsimp [A,B]
    linarith only [sh,sl]
  obtain ⟨e1,e2⟩:=scale_error h H hh e el eu
  obtain ⟨f1,f2⟩:=scale_error l H ll f fl fu
  have gz : 0<g := by dsimp [g];positivity
  have zero:=small_multiple g (A-B) gz gd (by omega) (by omega)
  have nat_eq : (2:Nat)^(H-h)*3^a=2^(H-l)*3^b := by
    have eab : A=B := by omega
    dsimp [A,B] at eab
    exact_mod_cast eab
  obtain ⟨time,grade⟩:=factor_clock _ _ _ _ nat_eq
  exact ⟨by omega,grade⟩

#print axioms high_meeting
end Collatz.ClockSeparation

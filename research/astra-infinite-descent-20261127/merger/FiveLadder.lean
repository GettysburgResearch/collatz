import FiveRouting
import Threshold

/-! A joint inverse ladder for y and 5y. All physical prefixes before
return lie strictly above the respective targets. An integer change of
origin bounds the cumulative affine error independently of word length. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FiveLadder
open TwoGapRouting FiveRouting FirstArrival

def Flight (D g x y : ℕ) : Prop :=
  Dual D g x y ∧ ∀i<D, y<run i x ∧ 5*y<run i (5*x)

theorem Flight.first {D g x y : ℕ} (f : Flight D g x y) :
    First D x y ∧ First D (5*x) (5*y) :=
  ⟨⟨f.1.1,fun i h => (f.2 i h).1.ne'⟩,⟨f.1.2.2.1,fun i h => (f.2 i h).2.ne'⟩⟩

private theorem halving_floor (d n : ℕ) : n≤2^d*run d n := by
  have h:=MergerThreshold.forward_lower d n
  have k:=Nat.le_mul_of_pos_left n (by positivity : 0<(3:ℕ)^(odds d n))
  omega

private theorem above (i h x y : ℕ) (short : i≤h) (large : 2^h*y<x) :
    y<run i x := by
  by_contra! bad
  have l:=halving_floor i x
  have k:=Nat.mul_le_mul (Nat.pow_le_pow_right (by decide : 0<2) short) bad
  omega

theorem flight_halves (h y : ℕ) (yp : 0<y) : Flight h 0 (2^h*y) y := by
  refine ⟨halves h y,?_⟩
  intro i short
  have p:=Nat.pow_lt_pow_right (by decide : 1<2) short
  have a:=Nat.mul_lt_mul_of_pos_right p yp
  have b:=Nat.mul_lt_mul_of_pos_right p (by positivity : 0<5*y)
  exact ⟨above i i _ _ (le_rfl) a,above i i _ _ (le_rfl) (by nlinarith only [b])⟩

/-- A high initial dual certificate can precede any joint first-arrival
flight. Its two starts remain above their respective ultimate targets
through every clock in the fixed prefix. -/
theorem preattach {h g x w e a y : ℕ} (head : Dual h g x w) (tail : Flight e a w y)
    (large : 2^h*y<x) : Flight (h+e) (g+a) x y := by
  refine ⟨FiveRouting.join head tail.1,?_⟩
  intro i bound
  by_cases short : i<h
  · exact ⟨above i h _ _ short.le large,above i h _ _ short.le (by nlinarith only [large])⟩
  · let j:=i-h
    have z : h+j=i := by dsimp [j]; omega
    have a:=(append h j x).1
    have b:=(append h j (5*x)).1
    rw [z,head.1] at a
    rw [z,head.2.2.1] at b
    rw [a,b]
    exact tail.2 j (by omega)

theorem Flight.join {h g x w e a y : ℕ} (head : Flight h g x w) (tail : Flight e a w y) :
    Flight (h+e) (g+a) x y := by
  have order : y≤w := by
    cases e with
    | zero => have hit:=tail.1.1; change w=y at hit; omega
    | succ e => exact (tail.2 0 (by omega)).1.le
  refine ⟨FiveRouting.join head.1 tail.1,?_⟩
  intro i bound
  by_cases short : i<h
  · have p:=head.2 i short
    exact ⟨lt_of_le_of_lt order p.1,lt_of_le_of_lt (Nat.mul_le_mul_left 5 order) p.2⟩
  · let j:=i-h
    have clock : h+j=i := by dsimp [j]; omega
    have a:=(append h j x).1
    have b:=(append h j (5*x)).1
    rw [clock,head.1.1] at a
    rw [clock,head.1.2.2.1] at b
    rw [a,b]
    exact tail.2 j (by omega)

def degree (b : Bool) : ℕ := if b then 3 else 2
private def carry (b : Bool) : ℕ := if b then 37 else 7
private def wordTime (b : Bool) : ℕ := if b then 8 else 6

theorem unit_pow_mul {y : ℕ} (k : ℕ) (yu : y%3≠0) : (2^k*y)%3≠0 := by
  intro bad
  rcases Nat.prime_three.dvd_mul.mp (Nat.dvd_of_mod_eq_zero bad) with left|right
  · exact (by decide : ¬3 ∣ (2:ℕ)) (Nat.prime_three.dvd_of_dvd_pow left)
  · exact yu (Nat.mod_eq_zero_of_dvd right)

private theorem local_flight (b : Bool) (e x y : ℕ) (eh : 20≤e) (yp : 0<y)
    (eq : 3^(degree b)*x+carry b=2^e*y) : Flight e (degree b) x y := by
  let h:=wordTime b
  have hp : h≤8 := by cases b <;> decide +kernel
  have hsize : 2^h≤256 := by
    calc (2:ℕ)^h≤2^8:=Nat.pow_le_pow_right (by decide) hp
         _=256:=by decide
  have big : 1048576≤2^e := by
    calc 1048576=(2:ℕ)^20:=by decide
         _≤2^e:=Nat.pow_le_pow_right (by decide) eh
  have cap : 3^(degree b)≤27 ∧ carry b≤37 := by cases b <;> decide +kernel
  have xy : 2^h*y<x := by
    by_contra! bad
    have v:=Nat.mul_le_mul cap.1 bad
    have k:=Nat.mul_le_mul_right y hsize
    have t:=Nat.mul_le_mul_right y big
    nlinarith only [v,k,t,eq,cap.2,yp]
  let r:=e-h
  have total : h+r=e := by dsimp [r]; omega
  have num : 3^(degree b)*x+carry b=2^h*(2^r*y) := by rw [eq,←total,pow_add]; ring
  have pre : Dual h (degree b) x (2^r*y) := by
    cases b with
    | false => exact macroA 6 x _ (by decide) num
    | true => exact macroB 8 x _ (by decide) num
  simpa only [total,Nat.add_zero] using preattach pre (flight_halves r y yp) xy

def weight (L n : ℕ) : ℕ := 2^L*n-64

private theorem one (b : Bool) (L y : ℕ) (lp : 20≤L) (yu : y%3≠0) :
    ∃x e : ℕ, x%3≠0 ∧ e≤L+54 ∧ Flight e (degree b) x y ∧
      3^(degree b)*x≤2^e*y ∧ 2^e*weight L y≤3^(degree b)*weight L x := by
  let a:=3^(degree b)
  let c:=carry b
  have small : a≤27 ∧ c≤37 ∧ (c+a)%3≠0 ∧ 2*3^(degree b)≤54 := by cases b <;> decide +kernel
  have yp : 0<y := by omega
  have huge : 1048576≤2^L := by
    calc 1048576=(2:ℕ)^20:=by decide
         _≤2^L:=Nat.pow_le_pow_right (by decide) lp
  obtain ⟨p,pp,pb,addr⟩:=scaled_address (degree b) (2^L*y) (c+a) (unit_pow_mul L yu) small.2.2.1
  let e:=L+p
  have eqn : 2^L*y*2^p=2^e*y := by dsimp [e]; rw [pow_add]; ring
  rw [eqn] at addr
  have lePow : 2^L≤2^e := Nat.pow_le_pow_right (by decide) (by dsimp [e]; omega)
  have full:=Nat.le_mul_of_pos_right (2^e) yp
  obtain ⟨v,div⟩:=(Nat.modEq_iff_dvd' (by omega : c+a≤2^e*y)).mp addr.symm
  let x:=1+3*v
  have mult : 3^(degree b+1)*v=a*(3*v) := by dsimp [a]; ring
  have form : a*x+c=2^e*y := by dsimp [x]; rw [Nat.mul_add,Nat.mul_one]; omega
  have xu : x%3≠0 := by dsimp [x]; omega
  refine ⟨x,e,xu,by dsimp [e]; omega,local_flight b e x y (by dsimp [e]; omega) yp form,by change a*x≤2^e*y; omega,?_⟩
  have px:=Nat.le_mul_of_pos_right (2^L) (show 0<x by omega)
  have py:=Nat.le_mul_of_pos_right (2^L) yp
  have wx : weight L x+64=2^L*x := by dsimp [weight]; omega
  have wy : weight L y+64=2^L*y := by dsimp [weight]; omega
  have gsmall:=Nat.mul_le_mul_left 64 small.1
  have csmall:=Nat.mul_le_mul_left (2^L) small.2.1
  have scaled:=congrArg (fun z:ℕ => 2^L*z) form
  have wx':=congrArg (fun z:ℕ => a*z) wx
  have wy':=congrArg (fun z:ℕ => 2^e*z) wy
  change 2^e*weight L y≤a*weight L x
  nlinarith only [scaled,wx',wy',gsmall,csmall,lePow,huge]

private def grade (w : List Bool) := (w.map degree).sum

private theorem build (w : List Bool) (L y : ℕ) (lp : 20≤L) (yu : y%3≠0) :
    ∃x S : ℕ, x%3≠0 ∧ S≤(L+54)*w.length ∧ Flight S (grade w) x y ∧
      3^(grade w)*x≤2^S*y ∧ 2^S*weight L y≤3^(grade w)*weight L x := by
  induction w generalizing y with
  | nil => exact ⟨y,0,yu,by simp,⟨⟨rfl,rfl,rfl,rfl⟩,by omega⟩,by simp [grade],by simp [grade]⟩
  | cons b w ih =>
    obtain ⟨z,e,zu,eb,first,hi,lo⟩:=one b L y lp yu
    obtain ⟨x,S,xu,Sb,rest,hi',lo'⟩:=ih z zu
    have g : grade (b::w)=grade w+degree b := by simp [grade,Nat.add_comm]
    rw [g]
    refine ⟨x,S+e,xu,by simp only [List.length_cons,Nat.mul_succ]; omega,rest.join first,?_,?_⟩
    · rw [pow_add,pow_add]
      have a:=Nat.mul_le_mul_left (3^(degree b)) hi'
      have c:=Nat.mul_le_mul_left (2^S) hi
      nlinarith only [a,c]
    · rw [pow_add,pow_add]
      have a:=Nat.mul_le_mul_left (2^S) lo
      have c:=Nat.mul_le_mul_left (3^(degree b)) lo'
      nlinarith only [a,c]

/-- Each repeated group of Q macros uses 2Q+1 actual odd departures on
both arms. This lets the depth mark control every residue modulo Q. -/
theorem seed (L Q j y : ℕ) (lp : 20≤L) (qp : 0<Q) (yu : y%3≠0) :
    ∃x S : ℕ, x%3≠0 ∧ S≤(L+54)*(Q*j) ∧ Flight S ((2*Q+1)*j) x y ∧
      3^((2*Q+1)*j)*x≤2^S*y ∧ 2^S*weight L y≤3^((2*Q+1)*j)*weight L x := by
  let w:=List.replicate ((Q-1)*j) false ++ List.replicate j true
  have qq : Q-1+1=Q := by omega
  have eq : (Q-1)*j+j=Q*j := by
    calc (Q-1)*j+j=(Q-1+1)*j := by ring
         _=Q*j:=by rw [qq]
  have len : w.length=Q*j := by simpa [w] using eq
  have g : grade w=(2*Q+1)*j := by simp [w,grade,degree]; nlinarith only [eq]
  simpa only [len,g] using build w L y lp yu

#print axioms flight_halves
#print axioms preattach
#print axioms seed
end Collatz.FiveLadder

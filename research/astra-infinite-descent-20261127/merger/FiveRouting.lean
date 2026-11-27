import AffineProfiles
import FirstArrival

/-! Ordinary ratio-five returns. The length-six and length-eight macro
words come from the five-certificate ladder in PR166 and PR146. The
two-macro congruence controls both targets at the same supplied clock. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FiveRouting
open TwoGapRouting AffineProfiles FirstArrival

def Dual (h g x y : ℕ) : Prop :=
  run h x=y ∧ odds h x=g ∧ run h (5*x)=5*y ∧ odds h (5*x)=g

theorem join {h g x y k a z : ℕ} (left : Dual h g x y) (right : Dual k a y z) :
    Dual (h+k) (g+a) x z := by
  obtain ⟨xr,xg,fr,fg⟩:=left
  obtain ⟨yr,yg,vr,vg⟩:=right
  simp only [Dual,(append h k x).1,(append h k x).2,(append h k (5*x)).1,
    (append h k (5*x)).2,xr,xg,fr,fg,yr,yg,vr,vg,and_self]

theorem halves (h y : ℕ) : Dual h 0 (2^h*y) y := by
  have zero (d : ℕ) : run d 0=0 ∧ odds d 0=0 := by
    induction d with
    | zero => simp [run,odds]
    | succ d ih => simpa [run,odds,step] using ih
  have p (n : ℕ) : run h (2^h*n)=n ∧ odds h (2^h*n)=0 := by
    simpa [zero h] using lift h 0 n
  have eq : 5*(2^h*y)=2^h*(5*y) := by ring
  exact ⟨(p y).1,(p y).2,eq ▸ (p (5*y)).1,eq ▸ (p (5*y)).2⟩

private theorem base_lift {h g R z : ℕ} (A : Dual h g R z) (t : ℕ) :
    Dual h g (R+2^h*t) (z+3^g*t) := by
  obtain ⟨r,o,f,p⟩:=A
  have l:=lift h R t
  have u:=lift h (5*R) (5*t)
  rw [r,o] at l
  rw [f,p] at u
  have fs : 5*(R+2^h*t)=5*R+2^h*(5*t) := by ring
  refine ⟨l.1,l.2,?_,by rw [fs]; exact u.2⟩
  rw [fs,u.1]; ring

private theorem six : Dual 6 2 49 7 := by unfold Dual; decide +kernel
private theorem eight : Dual 8 3 65 7 := by unfold Dual; decide +kernel

theorem macroA (e x y : ℕ) (eh : 6≤e) (eq : 9*x+7=2^e*y) : Dual e 2 x y := by
  let h:=e-6
  let z:=2^h*y
  have clock : 6+h=e := by dsimp [h]; omega
  have num : 9*x+7=64*z := by rw [eq,←clock,pow_add]; dsimp [z]; ring
  have form : x=49+64*(x/64) := by omega
  have p:=base_lift six (x/64)
  have start : 49+2^6*(x/64)=x := by norm_num; omega
  have dest : 7+3^2*(x/64)=z := by norm_num; omega
  rw [start,dest] at p
  simpa only [clock,Nat.add_zero] using join p (halves h y)

theorem macroB (e x y : ℕ) (eh : 8≤e) (eq : 27*x+37=2^e*y) : Dual e 3 x y := by
  let h:=e-8
  let z:=2^h*y
  have clock : 8+h=e := by dsimp [h]; omega
  have num : 27*x+37=256*z := by rw [eq,←clock,pow_add]; dsimp [z]; ring
  have form : x=65+256*(x/256) := by omega
  have p:=base_lift eight (x/256)
  have start : 65+2^8*(x/256)=x := by norm_num; omega
  have dest : 7+3^3*(x/256)=z := by norm_num; omega
  rw [start,dest] at p
  simpa only [clock,Nat.add_zero] using join p (halves h y)

private theorem unit_three {k : ℕ} (ku : k%3≠0) : Nat.Coprime 3 k :=
  Nat.prime_three.coprime_iff_not_dvd.mpr (by simpa [Nat.dvd_iff_mod_eq_zero] using ku)

/-- Multiplying the binary exponent by a supplied ternary unit preserves
the complete primitive-root exponent bank. -/
theorem scaled_address (s k b : ℕ) (ku : k%3≠0) (bu : b%3≠0) :
    ∃e : ℕ, 0<e ∧ e≤2*3^s ∧ k*2^e ≡ b [MOD 3^(s+1)] := by
  let z:=Nat.chineseRemainder ((unit_three ku).symm.pow_right (s+1)) 0 b
  obtain ⟨t,eq⟩:=Nat.modEq_zero_iff_dvd.mp z.property.1
  have res:=z.property.2
  rw [eq] at res
  have low:=res.of_dvd (show 3 ∣ 3^(s+1) by rw [pow_succ]; exact dvd_mul_left _ _)
  have tu : t%3≠0 := by
    intro bad
    change (k*t)%3=b%3 at low
    rw [Nat.mul_mod,bad,Nat.mul_zero] at low
    omega
  obtain ⟨e,ep,eb,addr⟩:=address s t tu
  exact ⟨e,ep,eb,(addr.mul_left k).trans res⟩

theorem two_replay (e f x y : ℕ) (eh : 6≤e) (fh : 6≤f)
    (eq : 81*x+63+7*2^e=2^(e+f)*y) : Dual (e+f) 4 x y := by
  let t:=2^f*y
  have h : 9*(9*x+7)+2^e*7=2^e*t := by
    dsimp [t]; rw [pow_add] at eq; nlinarith only [eq]
  have congr : 2^e*t ≡ 2^e*7 [MOD 9] := by rw [←h]; simp [Nat.ModEq]
  have coprime : Nat.Coprime 9 (2^e) := (by decide : Nat.Coprime 9 2).pow_right e
  have tm:=Nat.ModEq.cancel_left_of_coprime coprime congr
  change t%9=7%9 at tm
  let u:=t/9
  have ut : 9*u+7=t := by dsimp [u]; omega
  have xu : 9*x+7=2^e*u := by rw [←ut] at h; nlinarith only [h]
  exact join (macroA e x u eh xu) (macroA f u y fh ut)

/-- Two native ratio-five macros hit y and 5y at the same prescribed
clock and grade on both arms, while imposing arbitrary input trits. -/
theorem route (s D y c : ℕ) (clock : 54*3^s+11≤D) (unit : y%3≠0) :
    ∃x e : ℕ, 0<x ∧ 6≤e ∧ e+6≤D ∧ e≤54*3^s+5 ∧
      x ≡ c [MOD 3^s] ∧ 81*x+63+7*2^e=2^D*y ∧ Dual D 4 x y := by
  let m:=3^s
  let r:=c%m
  let A:=2^D*y-(63+81*r)
  let half:=2^(D-1)
  have mp : 0<m := by dsimp [m]; positivity
  have rm : r<m := Nat.mod_lt _ mp
  have yp : 0<y := by omega
  change 54*m+11≤D at clock
  have tw : 2^D=2*half := by
    rw [show D=(D-1)+1 by omega,pow_succ]; dsimp [half]; ring
  have large : 2*(D-1)≤half := by
    have h : D-2<2^(D-2) := Nat.lt_two_pow_self
    dsimp [half]; rw [show D-1=(D-2)+1 by omega,pow_succ]; omega
  have size : 2*half≤2^D*y := by rw [←tw]; exact Nat.le_mul_of_pos_right _ yp
  have num : A+(63+81*r)=2^D*y := by dsimp [A]; omega
  have pu : 2^D%3≠0 := by
    intro bad
    exact (by decide : ¬3 ∣ (2:ℕ)) (Nat.prime_three.dvd_of_dvd_pow (Nat.dvd_of_mod_eq_zero bad))
  have prodUnit : (2^D*y)%3≠0 := by
    rw [Nat.mul_mod]
    rcases (show 2^D%3=1 ∨ 2^D%3=2 by omega) with a|a <;>
      rcases (show y%3=1 ∨ y%3=2 by omega) with b|b <;> rw [a,b] <;> decide
  have au : A%3≠0 := by omega
  obtain ⟨p,pp,pb,addr⟩:=scaled_address (s+3) 224 A (by decide) au
  let e:=p+5
  have eb : e≤54*m+5 := by dsimp [e]; dsimp [m]; rw [pow_add] at pb; norm_num at pb; omega
  have ef : e+6≤D := by omega
  have exponent : 7*2^e=224*2^p := by dsimp [e]; rw [pow_add]; ring
  have eh : 8*2^e≤half := by
    have h:=Nat.pow_le_pow_right (by decide : 0<(2:ℕ)) (by omega : e+3≤D-1)
    dsimp [half]; rw [pow_add] at h; norm_num at h; omega
  rw [←exponent] at addr
  obtain ⟨v,vf⟩:=(Nat.modEq_iff_dvd' (by omega : 7*2^e≤A)).mp addr
  let x:=r+m*v
  have factor : 3^(s+3+1)*v=81*(m*v) := by dsimp [m]; ring
  have eq : 81*x+63+7*2^e=2^D*y := by dsimp [x]; omega
  have xp : 0<x := by omega
  have xc : x ≡ c [MOD 3^s] := by dsimp [x,r,m]; simp [Nat.ModEq]
  have ee : e+(D-e)=D := by omega
  refine ⟨x,e,xp,by dsimp [e]; omega,ef,eb,xc,eq,?_⟩
  exact ee ▸ two_replay e (D-e) x y (by dsimp [e]; omega) (by omega) (by rwa [ee])

#print axioms macroA
#print axioms macroB
#print axioms scaled_address
#print axioms route
end Collatz.FiveRouting

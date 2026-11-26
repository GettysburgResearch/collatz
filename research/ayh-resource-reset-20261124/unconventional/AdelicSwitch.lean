import Mathlib.Tactic.Linarith
import WordRank

/-! A source-dependent preparation of an inverse word, followed by a free
ternary digit lift and a long block of odd inverses, on the ordinary
three-odd upper Mersenne parent family. -/
namespace AdelicSwitch
open CollatzReverseBasin WordRank

private theorem inverse_row (y : Nat) (unit : y%3≠0) :
    ∃ a b : Nat, a≤3 ∧ 0<b ∧ b%2=1 ∧ b%3≠0 ∧ 3*b+1=2^(a+1)*y := by
  let u:=y/9
  have row : y=9*u+y%9 := by dsimp [u]; omega
  have cases' : y%9=1 ∨ y%9=2 ∨ y%9=4 ∨ y%9=5 ∨ y%9=7 ∨ y%9=8 := by omega
  rcases cases' with e|e|e|e|e|e
  · exact ⟨1,12*u+1,by decide,by omega,by omega,by omega,by rw [e] at row; omega⟩
  · exact ⟨0,6*u+1,by decide,by omega,by omega,by omega,by rw [e] at row; omega⟩
  · exact ⟨1,12*u+5,by decide,by omega,by omega,by omega,by rw [e] at row; omega⟩
  · exact ⟨2,24*u+13,by decide,by omega,by omega,by omega,by rw [e] at row; omega⟩
  · exact ⟨3,48*u+37,by decide,by omega,by omega,by omega,by rw [e] at row; omega⟩
  · exact ⟨0,6*u+5,by decide,by omega,by omega,by omega,by rw [e] at row; omega⟩

/-- Every positive ternary unit has an ordinary inverse word of exactly d
odd steps, using at most four clocks per odd step and ending on a unit. -/
theorem prepare (d y : Nat) (pos : 0<y) (unit : y%3≠0) :
    ∃ h b : Nat, h≤4*d ∧ 0<b ∧ b%3≠0 ∧ run h b=y ∧ odds h b=d := by
  induction d with
  | zero => exact ⟨0,y,by omega,pos,unit,rfl,rfl⟩
  | succ d ih =>
    obtain ⟨h,c,bound,_,uc,rc,oc⟩:=ih
    obtain ⟨a,b,ab,pb,odd,ub,eq⟩:=inverse_row c uc
    have sc : shortcut b=2^a*c := by
      rw [pow_succ] at eq
      have id : 3*b+1=2*(2^a*c) := by rw [eq]; ring
      simp [shortcut,odd,id]
    obtain ⟨endp,count⟩:=halves a c
    have st : run (a+1) b=c := by change run a (shortcut b)=c; rwa [sc]
    have ct : odds (a+1) b=1 := by change b%2+odds a (shortcut b)=1; rw [odd,sc,count]
    exact ⟨(a+1)+h,b,by omega,pb,ub,by rw [runAdd,st,rc],by rw [oddsAdd,ct,st,oc]; omega⟩

private def P (m : Nat) := (2:Nat)^(11+162*m)

private theorem p_unit (m : Nat) : P m%3=2 := by
  unfold P
  rw [pow_add,pow_mul,Nat.mul_mod,Nat.pow_mod (2^162) m 3,show (2:Nat)^162%3=1 by decide,one_pow]
  decide

private theorem two_unit (h : Nat) : (2:Nat)^h%3=1 ∨ (2:Nat)^h%3=2 := by
  induction h with
  | zero => decide
  | succ h ih => rw [pow_succ,Nat.mul_mod]; rcases ih with e|e <;> rw [e] <;> decide

/-- P(m+3^(k+p)) adds one new nonzero ternary digit after dividing by
3^(k+5+p), uniformly in m. -/
private theorem step_power (k p m : Nat) : ∃ c : Nat,
    P (m+3^(k+p))=P m+3^(k+5)*3^p*c ∧ c%3=2 := by
  obtain ⟨v,hv⟩:=TernaryPowerLift.period (4+(k+p))
  have ex : 2*3^(4+(k+p))=162*3^(k+p) := by rw [pow_add]; ring
  have tr : 3^(4+(k+p)+1)=3^(k+5)*3^p := by rw [←pow_add]; congr 1; omega
  rw [ex,tr] at hv
  refine ⟨P m*(3*v+1),?_,?_⟩
  · unfold P
    rw [show 11+162*(m+3^(k+p))=(11+162*m)+162*3^(k+p) by ring,pow_add,hv]; ring
  · rw [Nat.mul_mod,p_unit,show (3*v+1)%3=1 by omega]

private theorem edge_multiple (k m t : Nat) : ∃ c : Nat,
    P (m+3^k*t)=P m+3^(k+5)*c ∧ c%3=(2*t)%3 := by
  induction t with
  | zero => exact ⟨0,by simp,by simp⟩
  | succ t ih =>
    obtain ⟨c,step,uc⟩:=ih
    obtain ⟨e,es,ue⟩:=step_power k 0 (m+3^k*t)
    simp only [Nat.add_zero,pow_zero,Nat.mul_one] at es
    refine ⟨c+e,?_,?_⟩
    · rw [Nat.mul_succ,←Nat.add_assoc,es,step]; ring
    · rw [Nat.add_mod,uc,ue]; omega

/-- The exact change of ternary precision on the original parameter row.
In particular the residue map is bijective after deleting five fixed
ternary digits from the power. -/
theorem power_precision (k m t : Nat) :
    3^(k+5) ∣ 2^(11+162*(m+t))-2^(11+162*m) ↔ 3^k ∣ t := by
  change 3^(k+5) ∣ P (m+t)-P m ↔ 3^k ∣ t
  induction k with
  | zero =>
    obtain ⟨c,eq,_⟩:=edge_multiple 0 m t
    simp only [pow_zero,Nat.one_mul] at eq
    rw [eq,Nat.add_sub_cancel_left]; simp
  | succ k ih =>
    by_cases div : 3^k ∣ t
    · obtain ⟨u,hu⟩:=div
      obtain ⟨c,eq,uc⟩:=edge_multiple k m u
      rw [hu,eq,Nat.add_sub_cancel_left,show k+1+5=k+5+1 by omega,
          pow_succ (3:Nat) (k+5),pow_succ (3:Nat) k]
      rw [Nat.mul_dvd_mul_iff_left (by positivity : 0<(3:Nat)^(k+5)),
          Nat.mul_dvd_mul_iff_left (by positivity : 0<(3:Nat)^k)]
      omega
    · have nleft : ¬3^(k+1+5) ∣ P (m+t)-P m := fun d =>
        div (ih.mp ((pow_dvd_pow 3 (show k+5≤k+1+5 by omega)).trans d))
      have nright : ¬3^(k+1) ∣ t := fun d => div ((pow_dvd_pow 3 (show k≤k+1 by omega)).trans d)
      simp [nleft,nright]

private structure Point (k a h b p m q t : Nat) : Prop where
  power : P m=P a+3^(k+5)*q
  aligned : b+2^h*q+1=3^p*t

private theorem shift (k a h b p m q t : Nat) (pt : Point k a h b p m q t) :
    ∃ q' t' : Nat, Point k a h b p (m+3^(k+p)) q' t' ∧
    t'%3=(t+(2^h*2)%3)%3 := by
  obtain ⟨c,step,uc⟩:=step_power k p m
  refine ⟨q+3^p*c,t+2^h*c,⟨?_,?_⟩,?_⟩
  · rw [step,pt.power]; ring
  · calc
      b+2^h*(q+3^p*c)+1 = (b+2^h*q+1)+3^p*(2^h*c) := by ring
      _ = _ := by rw [pt.aligned]; ring
  · have id : (2^h*c)%3=(2^h*2)%3 := by rw [Nat.mul_mod (2^h) c,uc,←Nat.mul_mod (2^h) 2]
    rw [Nat.add_mod t (2^h*c),id,←Nat.add_mod_mod,Nat.add_mod t ((2^h*2)%3)]

private theorem cover_three (x y z d : Nat) (hy : y%3=(x+d)%3) (hz : z%3=(y+d)%3)
    (hd : d=1 ∨ d=2) : x%3=0 ∨ y%3=0 ∨ z%3=0 := by
  rcases hd with rfl|rfl <;> omega

/-- In every prescribed parameter class a modulo 3^k one can reach and
retain an arbitrary additional length p of divisibility. -/
private theorem steer (k a h b p : Nat) : ∃ v q t : Nat, v<3^p ∧
    Point k a h b p (a+3^k*v) q t := by
  induction p with
  | zero => exact ⟨0,0,b+1,by decide,by constructor <;> simp⟩
  | succ p ih =>
    obtain ⟨v,q,t,small,pt⟩:=ih
    let m:=a+3^k*v
    let d:=(2^h*2)%3
    have du : d=1 ∨ d=2 := by
      dsimp [d]; rw [Nat.mul_mod]; rcases two_unit h with e|e <;> rw [e] <;> decide
    obtain ⟨q1,t1,pt1,ht1⟩:=shift k a h b p m q t pt
    obtain ⟨q2,t2,pt2,ht2⟩:=shift k a h b p (m+3^(k+p)) q1 t1 pt1
    have check (w s r : Nat) (lo : w<3^(p+1)) (ok : Point k a h b p (a+3^k*w) s r)
        (dig : r%3=0) : ∃ w s r : Nat, w<3^(p+1) ∧ Point k a h b (p+1) (a+3^k*w) s r := by
      refine ⟨w,s,r/3,lo,⟨ok.power,?_⟩⟩
      rw [ok.aligned,pow_succ, Nat.mul_assoc]
      congr 1; omega
    rcases cover_three t t1 t2 d ht1 ht2 du with good|good|good
    · exact check v q t (by rw [pow_succ]; omega) pt good
    · apply check (v+3^p) q1 t1 (by rw [pow_succ]; omega) _ good
      have id : a+3^k*(v+3^p)=m+3^(k+p) := by dsimp [m]; rw [pow_add]; ring
      rwa [id]
    · apply check (v+2*3^p) q2 t2 (by rw [pow_succ]; omega) _ good
      have id : a+3^k*(v+2*3^p)=m+3^(k+p)+3^(k+p) := by dsimp [m]; rw [pow_add]; ring
      rwa [id]

private theorem whole (k a h b p m q t : Nat) (pt : Point k a h b p m q t) (i : Nat) :
    ∃ s r : Nat, Point k a h b p (m+3^(k+p)*i) s r := by
  induction i with
  | zero => exact ⟨q,t,by simpa using pt⟩
  | succ i ih =>
    obtain ⟨s,r,pr⟩:=ih
    obtain ⟨s',r',nxt,_⟩:=shift k a h b p (m+3^(k+p)*i) s r pr
    exact ⟨s',r',by simpa only [Nat.mul_succ,Nat.add_assoc] using nxt⟩

private theorem odd_prefix (p x t : Nat) (start : x+1=2^p*t) :
    run p x+1=3^p*t ∧ odds p x=p := by
  induction p generalizing x t with
  | zero => simpa [run,odds] using start
  | succ p ih =>
    have eq : x+1=2*(2^p*t) := by rw [start]; ring
    have odd : x%2=1 := by omega
    have sc : shortcut x+1=2^p*(3*t) := by
      rw [show 2^p*(3*t)=3*(2^p*t) by ring]; unfold shortcut; split <;> omega
    obtain ⟨ep,num⟩:=ih (shortcut x) (3*t) sc
    change run p (shortcut x)+1=_ ∧ x%2+odds p (shortcut x)=_
    rw [ep,num,odd]; constructor <;> ring

private theorem source_prefix (n : Nat) : run 4 (48*n+17)=27*n+10 ∧ odds 4 (48*n+17)=2 := by
  have e1 : shortcut (48*n+17)=72*n+26 := by unfold shortcut; split <;> omega
  have e2 : shortcut (72*n+26)=36*n+13 := by unfold shortcut; split <;> omega
  have e3 : shortcut (36*n+13)=54*n+20 := by unfold shortcut; split <;> omega
  have e4 : shortcut (54*n+20)=27*n+10 := by unfold shortcut; split <;> omega
  simp only [run,odds,e1,e2,e3,e4]; constructor <;> first | trivial | omega

private theorem linear_lower (h x : Nat) : 3^(odds h x)*x≤2^h*run h x := by
  induction h generalizing x with
  | zero => simp [odds,run]
  | succ h ih =>
    let y:=shortcut x
    have st : 3^(x%2)*x≤2*y := by
      dsimp [y,shortcut]; split
      · rename_i even; rw [even]; simp; omega
      · rename_i odd; rw [show x%2=1 by omega]; simp; omega
    have lift:=Nat.mul_le_mul_left (3^(odds h y)) st
    have tail:=Nat.mul_le_mul_left 2 (ih y)
    change 3^(x%2+odds h y)*x≤2^(h+1)*run h y
    rw [pow_add,pow_succ]; nlinarith only [lift,tail]

/-- The odd suffix length is a multiple of eighteen, with a linear bound
in the prescribed savings exponent and initial ternary precision. -/
def tailDepth (k f : Nat) := 18*((f+4*(k+5)+4)/9+1)

private theorem tail_bounds (k f : Nat) :
    2*(f+4*(k+5)+4)<tailDepth k f ∧ tailDepth k f≤2*(f+4*(k+5)+4)+18 := by
  unfold tailDepth; omega

private theorem cheap (k h f : Nat) (bound : h≤4*(k+5)) :
    (2:Nat)^f*2^(4+tailDepth k f+h)<3^(2+tailDepth k f+(k+5)) := by
  let p:=tailDepth k f
  let r:=p/2
  have pr : p=2*r := by dsimp [r,p,tailDepth]; omega
  have lb := (tail_bounds k f).1
  change 2*(f+4*(k+5)+4)<p at lb
  have lt' : f+(4+p+h)<3*r := by omega
  have first := Nat.pow_lt_pow_right (by decide : 1<(2:Nat)) lt'
  have mult : (2:Nat)^(3*r)≤3^p := by
    rw [pr,pow_mul,pow_mul]; exact Nat.pow_le_pow_left (by decide : 2^3≤(3:Nat)^2) r
  have last : (3:Nat)^p≤3^(2+p+(k+5)) := Nat.pow_le_pow_right (by decide) (by omega)
  rw [←pow_add]
  exact lt_of_lt_of_le first (mult.trans last)

private theorem tail_unit (k f : Nat) : (2:Nat)^tailDepth k f%27=1 := by
  unfold tailDepth; rw [pow_mul,Nat.pow_mod (2^18) _ 27,show (2:Nat)^18%27=1 by decide,one_pow]; decide

/-- A prepared tail lands on a genuine 17-mod-48 ordinary source. -/
private theorem realize (k a h b f m q s : Nat)
    (base : run h b+1=P a) (grade : odds h b=k+5)
    (pt : Point k a h (b+16*3^tailDepth k f) (tailDepth k f+3) m q s) :
    ∃ w : Nat, 0<w ∧ w%48=17 ∧
      run (4+tailDepth k f+h) w+1=P m ∧ odds (4+tailDepth k f+h) w=2+tailDepth k f+(k+5) := by
  let p:=tailDepth k f
  let x:=2^h*q+b
  have tail : x+1+16*3^p=3^p*(27*s) := by
    have e := pt.aligned
    change b+16*3^p+2^h*q+1=3^(p+3)*s at e
    rw [pow_add] at e
    dsimp [x]; linarith only [e]
  have spos : 0<s := by
    by_contra! hz
    have z : s=0 := by omega
    rw [z] at tail; simp at tail
  let n:=s-1
  let t:=27*n+11
  have st : s=n+1 := by dsimp [n]; omega
  have xe : x+1=3^p*t := by rw [st] at tail; dsimp [t]; linarith only [tail]
  let u:=2^p/27
  have eu : 2^p=27*u+1 := by have := tail_unit k f; change 2^p%27=1 at this; dsimp [u]; omega
  let v:=n+u*t
  have we : (27*v+10)+1=2^p*t := by rw [eu]; dsimp [v,t]; ring
  obtain ⟨oe,og⟩:=odd_prefix p (27*v+10) t we
  have ot : run p (27*v+10)=x := by omega
  obtain ⟨ae,ag⟩:=liftPrefix h q b
  change run h x=_ at ae
  change odds h x=_ at ag
  rw [grade] at ae ag
  have he : run h x+1=P m := by rw [ae,pt.power]; omega
  obtain ⟨qe,qg⟩:=source_prefix v
  refine ⟨48*v+17,by omega,by omega,?_,?_⟩
  · rw [runAdd (4+p) h,runAdd 4 p,qe,ot,he]
  · rw [oddsAdd (4+p) h,runAdd 4 p,oddsAdd 4 p,qe,qg,og,ot,ag]

/-- Every prescribed ternary cylinder contains a complete progression of
ordinary parameters carrying a 17-mod-48 lower merger with any chosen
power-of-two height saving. Its first representative lies in the first
period of the supplied cylinder. All clocks and the subprogression's
modulus admit bounds independent of the height of a. -/
theorem cylinder (k a f : Nat) : ∃ h v : Nat,
    h≤4*(k+5) ∧ v<3^(tailDepth k f+3) ∧
    ∀ i : Nat, ∃ w : Nat, 0<w ∧ w%48=17 ∧
      let m:=a+3^k*v+3^(k+(tailDepth k f+3))*i
      run (4+tailDepth k f+h) w+1=2^(11+162*m) ∧
      odds (4+tailDepth k f+h) w=2+tailDepth k f+(k+5) ∧
      2^f*w<2^(11+162*m)-1 := by
  let y:=P a-1
  have pa : 1<P a := by unfold P; exact Nat.one_lt_two_pow (by omega)
  have first : y+1=P a := by dsimp [y]; omega
  have yu : y%3≠0 := by have := p_unit a; omega
  obtain ⟨h,b,hb,_,_,rb,gb⟩:=prepare (k+5) y (by omega) yu
  let p:=tailDepth k f
  obtain ⟨v,q,t,vs,pt⟩:=steer k a h (b+16*3^p) (p+3)
  refine ⟨h,v,hb,vs,fun i => ?_⟩
  let m:=a+3^k*v+3^(k+(p+3))*i
  obtain ⟨q',s,pti⟩:=whole k a h (b+16*3^p) (p+3) (a+3^k*v) q t pt i
  obtain ⟨w,wp,wr,ep,og⟩:=realize k a h b f m q' s (by rw [rb,first]) gb pti
  refine ⟨w,wp,wr,ep,og,?_⟩
  let H:=4+p+h
  have low:=linear_lower H w
  change odds H w=2+p+(k+5) at og
  rw [og] at low
  have ch:=cheap k h f hb
  change 2^f*2^H<3^(2+p+(k+5)) at ch
  have strict:=Nat.mul_lt_mul_of_pos_right ch wp
  have joined : 2^H*(2^f*w)<2^H*run H w := by nlinarith only [strict,low]
  have drop:=Nat.lt_of_mul_lt_mul_left joined
  change run H w+1=P m at ep
  change 2^f*w<P m-1
  omega

#print axioms power_precision
#print axioms prepare
#print axioms cylinder
end AdelicSwitch

module

public import PassageDescentIndependent
public import FiberTransport
import all FiberTransport
import all TernaryItinerary
import all ReturnDescent
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.PassageDescent

open ReturnDescent TowerFrontier
set_option autoImplicit false
set_option maxHeartbeats 3000000

/-- A source below a binary translate stays below the corresponding ternary
    translate. This keeps the transferred comparison source nonnegative. -/
private theorem envelope (h x e w : Nat) (small : x<2^h*3^e*w) :
    (track h x e).1<3^(track h x e).2*w := by
  induction h generalizing x e with
  | zero => simpa [track] using small
  | succ h ih =>
    have cap : x<2*(2^h*3^e*w) := by
      rw [Nat.pow_succ] at small
      grind
    simp only [track]
    split
    · exact ih _ _ (by omega)
    · apply ih
      rw [Nat.pow_succ]
      have eq : 2^h*(3^e*3)*w=3*(2^h*3^e*w) := by ac_rfl
      omega

private theorem leading (h x e : Nat) :
    3^(track h x e).2*x≤2^h*(track h x e).1*3^e := by
  induction h generalizing x e with
  | zero => simp [track,Nat.mul_comm]
  | succ h ih =>
    simp only [track]
    split <;> rename_i even
    · let y := x/2
      have b := ih y e
      have eq : x=2*y := by dsimp only [y]; omega
      have move := congrArg (fun n => 3^(track h y e).2*n) eq
      rw [Nat.pow_succ]
      change 3^(track h y e).2*x≤2^h*2*(track h y e).1*3^e
      grind
    · let y := (3*x+1)/2
      have b := ih y (e+1)
      rw [Nat.pow_succ 3 e] at b
      have eq : 3*x+1=2*y := by dsimp only [y]; omega
      have move := congrArg (fun n => 3^(track h y (e+1)).2*n) eq
      rw [Nat.pow_succ]
      change 3^(track h y (e+1)).2*x≤2^h*2*(track h y (e+1)).1*3^e
      grind

private def guard (b : Nat) : Nat → Nat → Nat → Bool
  | 0,x,_ => x==1
  | f+1,x,d => x==1 || ((x != 589 || decide (d<4) || (b==929 && d==7)) && guard b f (step x) (d+1))

private theorem one_small (h x : Nat) (hx : x=1 ∨ x=2) : run h x≤2 := by
  induction h generalizing x with
  | zero => simpa only [run] using (show x≤2 by omega)
  | succ h ih => rw [run]; apply ih; rcases hx with rfl|rfl <;> decide

private theorem guard_sound {b f x d t : Nat} (ok : guard b f x d=true)
    (hit : run t x=589) : d+t<4 ∨ (b=929 ∧ d+t=7) := by
  induction f generalizing x d t with
  | zero =>
    have eq : x=1 := by simpa [guard] using ok
    have bound := one_small t x (Or.inl eq)
    omega
  | succ f ih =>
    by_cases eq : x=1
    · have bound := one_small t x (Or.inl eq)
      omega
    · obtain ⟨now,next⟩ := Bool.and_eq_true_iff.mp
        (show ((x != 589 || decide (d<4) || (b==929 && d==7)) && guard b f (step x) (d+1))=true by
          simpa [guard,eq] using ok)
      cases t with
      | zero =>
        change x=589 at hit
        simp [hit] at now
        simpa using now
      | succ t =>
        rcases ih next hit with early|⟨eb,et⟩
        · exact Or.inl (by omega)
        · exact Or.inr ⟨eb,by omega⟩

private theorem twenty : ∀ i : Fin 20, guard (48*i.val+17) 200 (48*i.val+17) 0=true := by
  decide +kernel

private theorem anchor_hit {b h : Nat} (cls : b%48=17) (size : b≤930) (clock : 4≤h) (hit : run h b=589) :
    b=929 ∧ h=7 := by
  have repr := Nat.mod_add_div b 48
  rw [cls] at repr
  have c := twenty ⟨b/48,by omega⟩
  change guard (48*(b/48)+17) 200 (48*(b/48)+17) 0=true at c
  rw [show 48*(b/48)+17=b by omega] at c
  rcases guard_sound c hit with early|found
  · omega
  · simpa using found

private theorem minimum_lower_clock {m h y : Nat} (enough : 4≤m) (cls : y%48=17)
    (hit : run h y=M m) : 4≤h := by
  have repr := Nat.mod_add_div y 48
  rw [cls] at repr
  have p : 2^m=16*2^(m-4) := by
    rw [show (16:Nat)=2^4 by decide,←Nat.pow_add]; congr 1; omega
  have pos := Nat.two_pow_pos (m-4)
  let q := y/48
  have s1 : step y=26+72*q := by dsimp only [q]; unfold step; split <;> omega
  have s2 : step (26+72*q)=13+36*q := by unfold step; split <;> omega
  have s3 : step (13+36*q)=20+54*q := by unfold step; split <;> omega
  by_cases ok : 4≤h
  · exact ok
  rcases (show h=0 ∨ h=1 ∨ h=2 ∨ h=3 by omega) with e|e|e|e <;>
    subst h <;> simp only [M,p,run,s1,s2,s3] at hit <;> omega

/-- On every sufficiently high lift of 590 at precision K+1, each smaller
    canonical direct ancestor spends more than K odd departures. Its clock
    and upper orbit are unrestricted. -/
theorem ternary_ancestor_price {m h y p K : Nat} (enough : 4≤m)
    (near : ∃ a, 2^m=590+3^(K+1)*a) (high : 590+75521*3^K≤2^m)
    (cls : y%48=17) (small : y<hardParent m) (route : track h y 0=(M m,p)) : K<p := by
  by_cases ok : K<p
  · exact ok
  obtain ⟨a,ha⟩ := near
  let v := 3^(K-p)*a
  let w := 3*v
  let P := 3^p
  have exactN : 2^m=590+P*w := by
    rw [ha]
    dsimp only [P,w,v]
    rw [show K+1=p+(K-p)+1 by omega,Nat.pow_succ,Nat.pow_add 3 p]
    ac_rfl
  have pg : 3^p≤3^K := Nat.pow_le_pow_right (by decide) (by omega)
  have hg := Nat.mul_le_mul_left 75521 pg
  have pp : 0<P := Nat.pow_pos (by decide)
  have wc : 75521≤w := by
    have bound : P*75521≤P*w := by
      rw [Nat.mul_comm P 75521]
      change 75521*3^p≤P*w
      omega
    exact Nat.le_of_mul_le_mul_left bound pp
  have physical : run h y=M m := by rw [←track_run h y 0,route]
  have four := minimum_lower_clock enough cls physical
  have initial : 2^h*w≤y := by
    by_cases v : 2^h*w≤y
    · exact v
    have weak := envelope h y 0 w (by simpa using (show y<2^h*w by omega))
    rw [route] at weak
    change M m<P*w at weak
    unfold M at weak
    omega
  let b := y-2^h*w
  have shape : y=b+2^h*w := by dsimp only [b]; omega
  have transfer := track_lift h b w
  rw [←shape,route] at transfer
  have bg : (track h b 0).2=p := (congrArg Prod.snd transfer).symm
  have bf := congrArg Prod.fst transfer
  change M m=(track h b 0).1+3^(track h b 0).2*w at bf
  rw [bg] at bf
  change M m=(track h b 0).1+P*w at bf
  unfold M at bf
  have bh : run h b=589 := by rw [←track_run h b 0]; omega
  have div : 2^h*w=48*(2^(h-4)*v) := by
    have bin : 2^h=16*2^(h-4) := by
      rw [show (16:Nat)=2^4 by decide,←Nat.pow_add]; congr 1; omega
    rw [bin]
    change (16*2^(h-4))*(3*v)=(16*3)*(2^(h-4)*v)
    ac_rfl
  have cb : b%48=17 := by rw [shape,div,Nat.add_mul_mod_self_left] at cls; exact cls
  have price : 81*y+271<128*2^m := by
    unfold hardParent at small
    rw [Nat.pow_add] at small
    omega
  have slope : 81*2^h≤128*P := by
    by_cases v : 81*2^h≤128*P
    · exact v
    have slack := Nat.mul_le_mul_right w (show 128*P+1≤81*2^h by omega)
    grind
  have lb := leading h b 0
  rw [bg,track_run,bh,Nat.pow_zero,Nat.mul_one] at lb
  change P*b≤2^h*589 at lb
  have bound : b≤930 := by
    by_cases le : b≤930
    · exact le
    have large := Nat.mul_le_mul_left P (show 931≤b by omega)
    have sc := Nat.mul_le_mul_right 589 slope
    grind
  obtain ⟨bb,hh⟩ := anchor_hit cb bound four bh
  have grade : p=4 := by rw [←bg,bb,hh]; decide +kernel
  rw [bb,hh] at shape
  have coef : P=81 := by dsimp only [P]; rw [grade]
  rw [coef] at exactN
  omega

#print axioms ternary_ancestor_price

private theorem periodic {M T : Nat} (large : 1<M) (one : 2^T%M=1) (a : Nat) :
    2^a%M=2^(a%T)%M := by
  have exp := Nat.mod_add_div a T
  have tail : (2^T)^(a/T)%M=1 := by rw [Nat.pow_mod,one,Nat.one_pow,Nat.mod_eq_of_lt large]
  calc
    2^a%M=2^(a%T+T*(a/T))%M := congrArg (fun v => 2^v%M) exp.symm
    _ = _ := by rw [Nat.pow_add,Nat.pow_mul,Nat.mul_mod,tail,Nat.mul_one,Nat.mod_mod]

private theorem hard_phase : ∀ i : Fin 162, 2^i.val%243=590%243 → i.val=11 := by decide +kernel
private theorem inner_phase : ∀ i : Fin 18, 2^i.val%27=2 → i.val=1 := by decide +kernel

private theorem keep {B d x : Nat} (eq : B=1+d*x) (n : Nat) :
    ∃ v, B^n=1+d*v := by
  induction n with
  | zero => exact ⟨0,by simp⟩
  | succ n ih =>
    obtain ⟨v,hv⟩ := ih
    exact ⟨v+x+d*v*x,by rw [Nat.pow_succ,hv,eq]; grind⟩

/-- The ordinary delayed exponents themselves enter arbitrarily high 590
    cylinders. Both exponent selections are carried out at positive integers. -/
theorem delayed_approaches_anchor (K L : Nat) :
    ∃ k, L≤k ∧ 4≤delayedExponent k ∧
      (∃ v, 2^(delayedExponent k)=590+3^(K+1)*v) ∧
      590+75521*3^K≤2^(delayedExponent k) := by
  let size := 590+75521*3^K+L
  obtain ⟨e,w,hs,h0⟩ := FiberTransport.large_dyadic_lift (K+4) 1 590 size (by decide) (by decide)
  simp only [Nat.mul_one] at h0
  have lift : 3^(K+4+1)=243*3^K := by
    rw [show K+4+1=5+K by omega,Nat.pow_add]
  rw [lift] at h0
  have ebase : 2^e%243=590%243 := by rw [h0,Nat.mul_assoc,Nat.add_mul_mod_self_left]
  have er : e%162=11 := hard_phase ⟨e%162,Nat.mod_lt _ (by decide)⟩
    ((periodic (by decide) (by decide +kernel : 2^162%243=1) e).symm.trans ebase)
  let j := e/162
  have ex := Nat.mod_add_div e 162
  rw [er] at ex
  change 11+162*j=e at ex
  let q := 2+27*j
  have unit : q%3≠0 := by dsimp only [q]; omega
  obtain ⟨d,v,hd,h1⟩ := FiberTransport.large_dyadic_lift (K+4) 1 q (18*L+1) (by decide) unit
  simp only [Nat.mul_one] at h1
  rw [lift] at h1
  have dbase : 2^d%27=2 := by
    rw [h1,show 243*3^K*v=27*(9*3^K*v) by grind]
    dsimp only [q]
    omega
  have dr : d%18=1 := inner_phase ⟨d%18,Nat.mod_lt _ (by decide)⟩
    ((periodic (by decide) (by decide : 2^18%27=1) d).symm.trans dbase)
  let k := d/18
  have dx := Nat.mod_add_div d 18
  rw [dr] at dx
  change 1+18*k=d at dx
  have inner : 2*2^(18*k)=q+243*3^K*v := by rw [←h1,←dx,Nat.pow_add]
  let m := delayedExponent k
  let T := 2*3^K
  have qval : 6*q=e+1 := by dsimp only [q]; omega
  have extension : m=e+T*(729*v) := by
    dsimp only [m,delayedExponent,T]
    have hm := congrArg (fun n => 6*n) inner
    grind
  obtain ⟨f,period,_⟩ := FiberTransport.power_lift K
  obtain ⟨g,hg⟩ := keep period (729*v)
  rw [←Nat.pow_mul] at hg
  change 2^(T*(729*v))=1+3^(K+1)*g at hg
  have ed : 2^e=590+3^(K+1)*(81*w) := by
    rw [h0,Nat.pow_succ]; grind
  have full : 2^m=590+3^(K+1)*(81*w+2^e*g) := by
    rw [extension,Nat.pow_add,hg,Nat.mul_add,Nat.mul_one]
    grind
  have bound := Nat.lt_two_pow_self (n:=m)
  have em : e≤m := by omega
  dsimp only [size] at hs
  refine ⟨k,by omega,?_,⟨_,full⟩,?_⟩
  · change 4≤m
    omega
  · change 590+75521*3^K≤2^m
    omega

/-- No finite lower odd-step budget covers all preassigned delayed parents
    by smaller canonical direct ancestry of their native Mersennes. -/
theorem delayed_ancestor_price_unbounded (K L : Nat) :
    ∃ k, L≤k ∧ ∀ h y p, y%48=17 → y<hardParent (delayedExponent k) →
      track h y 0=(M (delayedExponent k),p) → K<p := by
  obtain ⟨k,high,enough,near,price⟩ := delayed_approaches_anchor K L
  exact ⟨k,high,fun _ _ _ cls less path => ternary_ancestor_price enough near price cls less path⟩

#print axioms delayed_ancestor_price_unbounded

private theorem grade_bound (h y e : Nat) : (track h y e).2≤h+e := by
  induction h generalizing y e with
  | zero => simp [track]
  | succ h ih =>
    simp only [track]
    split
    · have := ih (y/2) e
      omega
    · have := ih ((3*y+1)/2) (e+1)
      omega

private theorem add_odd (h y e : Nat) :
    track h y (e+1)=((track h y e).1,(track h y e).2+1) := by
  induction h generalizing y e with
  | zero => rfl
  | succ h ih => simp only [track]; split <;> apply ih

private theorem four_growth (h x : Nat) : 2^h*run h x≤4^(track h x 0).2*x := by
  induction h generalizing x with
  | zero => simp [run,track]
  | succ h ih =>
    by_cases ev : x%2=0
    · let y := x/2
      have eq : 2*y=x := by dsimp only [y]; omega
      have mul := congrArg (fun v => 4^(track h y 0).2*v) eq
      have k := Nat.mul_le_mul_left 2 (ih y)
      simp only [run,step,track,ev,↓reduceIte,Nat.pow_succ]
      change 2^h*2*run h y≤4^(track h y 0).2*x
      grind
    · let y := (3*x+1)/2
      have sb : y≤2*x := by dsimp only [y]; omega
      have mul := Nat.mul_le_mul_left (4^(track h y 0).2) sb
      have k := Nat.mul_le_mul_left 2 (ih y)
      simp only [run,step,track,ev,↓reduceIte,Nat.pow_succ]
      change 2^h*2*run h y≤4^(track h y 1).2*x
      rw [add_odd h y 0,Nat.pow_succ]
      grind

private theorem lag_grade_bound {m h y r : Nat} (enough : 2≤m) (small : y<hardParent m)
    (upper : track (h+2) (3*y) 0=(2^(m-2),r)) : h≤2*r+2 := by
  have b := four_growth (h+2) (3*y)
  rw [←track_run (h+2) (3*y) 0,upper] at b
  change 2^(h+2)*2^(m-2)≤4^r*(3*y) at b
  have left : 2^(h+2)*2^(m-2)=2^h*2^m := by
    rw [←Nat.pow_add,←Nat.pow_add]; congr 1; omega
  rw [left] at b
  have price : y<2*2^m := by
    unfold hardParent at small
    rw [Nat.pow_add] at small
    omega
  have mult := Nat.mul_lt_mul_of_pos_left price (show 0<4^r by exact Nat.pow_pos (by decide))
  have pow : 2^(2*r+3)=4^r*8 := by rw [Nat.pow_add,Nat.pow_mul]
  by_cases ok : h≤2*r+2
  · exact ok
  have tooHigh : 2^(2*r+3)≤2^h := Nat.pow_le_pow_right (by decide) (by omega)
  rw [pow] at tooHigh
  have cmp := Nat.mul_le_mul_right (2^m) tooHigh
  grind

/-- A single supplied delayed parent can force both grades past any
    prescribed budgets on every smaller canonical equal-lag comparison. -/
theorem delayed_pair_grades_unbounded (lowerBudget upperBudget L : Nat) :
    ∃ k, L≤k ∧ ∀ h y p r, y%48=17 → y<hardParent (delayedExponent k) →
      track h y 0=(M (delayedExponent k),p) →
      track (h+2) (3*y) 0=(2^(delayedExponent k-2),r) →
      lowerBudget<p ∧ upperBudget<r := by
  let K := max lowerBudget (2*upperBudget+2)
  obtain ⟨k,high,enough,near,price⟩ := delayed_approaches_anchor K L
  refine ⟨k,high,?_⟩
  intro h y p r cls small lower upper
  have expensive := ternary_ancestor_price enough near price cls small lower
  have bound := grade_bound h y 0
  rw [lower] at bound
  change p≤h+0 at bound
  have width := lag_grade_bound (by omega : 2≤delayedExponent k) small upper
  dsimp only [K] at expensive
  omega

#print axioms delayed_pair_grades_unbounded

end Collatz.Itinerary.PassageDescent

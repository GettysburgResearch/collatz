module

public import PassageDescentRankTable
public import PassageDescentDelayed
import all TernaryItinerary
import all ReturnDescent
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.PassageDescent

open ReturnDescent TowerFrontier
set_option autoImplicit false
set_option maxHeartbeats 4000000
set_option exponentiation.threshold 10000

private theorem inc_grade (h n e : Nat) :
    track h n (e+1)=((track h n e).1,(track h n e).2+1) := by
  induction h generalizing n e with
  | zero => rfl
  | succ h ih => simp only [track]; split <;> apply ih

private theorem word_bound (h x : Nat) :
    2^h*(track h x 0).1≤3^(track h x 0).2*(x+2^h) := by
  induction h generalizing x with
  | zero => simp [track]
  | succ h ih =>
    simp only [track]
    split
    · have b := Nat.mul_le_mul_left 2 (ih (x/2))
      have half : 2*(x/2)≤x := by omega
      have pp := Nat.mul_le_mul_left (3^(track h (x/2) 0).2) half
      rw [Nat.pow_succ 2 h]
      grind
    · let n := (3*x+1)/2
      have g : track h n 1=((track h n 0).1,(track h n 0).2+1) := inc_grade h n 0
      change 2^(h+1)*(track h n 1).1≤3^(track h n 1).2*(x+2^(h+1))
      rw [g,Nat.pow_succ 2 h,Nat.pow_succ]
      have b := Nat.mul_le_mul_left 2 (ih n)
      have half : 2*n≤3*x+1 := by dsimp [n]; omega
      have pp := Nat.mul_le_mul_left (3^(track h n 0).2) half
      have one : 1≤2^h := Nat.two_pow_pos _
      have pos := Nat.mul_le_mul_left (3^(track h n 0).2) one
      grind

theorem upper_cut_clock_bound {m y h r : Nat} (large : 173≤m) (source : y<hardParent m)
    (rank : r≤10) (upper : track (h+2) (3*y) 0=(2^(m-2),r)) : h≤18 := by
  have b := word_bound (h+2) (3*y)
  rw [upper] at b
  change 2^(h+2)*2^(m-2)≤3^r*(3*y+2^(h+2)) at b
  have e : 2^(h+2)*2^(m-2)=2^h*2^m := by rw [←Nat.pow_add,←Nat.pow_add]; congr 1; omega
  rw [e,Nat.pow_add] at b
  have p := Nat.pow_le_pow_right (by decide : 0<3) rank
  have q := Nat.mul_le_mul_right (3*y+2^h*4) p
  have zcap : y≤2*2^m := by unfold hardParent at source; rw [Nat.pow_add] at source; omega
  have small : 2^h*2^m≤354294*2^m+236196*2^h := by grind
  by_cases hn : h≤18
  · exact hn
  have grow : 2^19≤2^h := Nat.pow_le_pow_right (by decide) (by omega)
  have lb : 4*354294≤3*2^h := by omega
  have lbm := Nat.mul_le_mul_right (2^m) lb
  have mb : 2^22≤2^m := Nat.pow_le_pow_right (by decide) (by omega)
  have mbh := Nat.mul_le_mul_left (2^h) (show 4*236196+1≤2^m by omega)
  grind

private theorem run_upper (h n : Nat) : run h n≤2^h*n := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih =>
    have b : step n≤2*n := by unfold step; split <;> omega
    have bs := Nat.mul_le_mul_left (2^h) b
    rw [run,Nat.pow_succ,Nat.mul_assoc]
    exact Nat.le_trans (ih _) bs

private theorem low_source {y : Nat} (cls : y%48=17) (h : Nat) :
    ∃ i t, i<2^(h-2) ∧ y=(48*i+17)+3*2^(h+2)*t := by
  have src := Nat.mod_add_div y 48
  rw [cls] at src
  cases h with
  | zero => exact ⟨0,4*(y/48),by decide,by omega⟩
  | succ h =>
    cases h with
    | zero => exact ⟨0,2*(y/48),by decide,by omega⟩
    | succ n =>
      let N := 2^n
      let q := y/48
      refine ⟨q%N,q/N,?_,?_⟩
      · rw [show n+1+1-2=n by omega]
        exact Nat.mod_lt q (Nat.two_pow_pos n)
      · have md := Nat.mod_add_div q N
        have pow : 2^(n+1+1+2)=N*16 := by dsimp only [N]; exact Nat.pow_add 2 n 4
        rw [pow]
        dsimp only [q] at md
        grind

private theorem term_class (j : Nat) :
    2^(11+162*j-2)%243=512%243 := by
  rw [show 11+162*j-2=9+162*j by omega,Nat.pow_add,Nat.pow_mul,Nat.mul_mod]
  have base : 2^162%243=1 := by decide +kernel
  have term : (2^162)^j%243=1 := by rw [Nat.pow_mod,base,Nat.one_pow]
  rw [term]

/-- The two exact native cuts cannot have a strictly smaller canonical
    synchronous predecessor with at most ten upper odd departures. -/
theorem eleven_required {j h y r : Nat} (positive : 0<j)
    (cls : y%48=17) (small : y<hardParent (11+162*j))
    (lower : run h y=M (11+162*j))
    (upper : track (h+2) (3*y) 0=(2^(11+162*j-2),r)) : 11≤r := by
  let m := 11+162*j
  change y<hardParent m at small
  change run h y=M m at lower
  change track (h+2) (3*y) 0=(2^(m-2),r) at upper
  by_cases ok : 11≤r
  · exact ok
  have rank : r≤10 := by omega
  have large : 173≤m := by dsimp only [m]; omega
  have hh := upper_cut_clock_bound large small rank upper
  obtain ⟨i,t,hi,repr⟩ := low_source cls h
  let b := 48*i+17
  let l := track h b 0
  let u := track (h+2) (3*b) 0
  change y=b+3*2^(h+2)*t at repr
  have yl : y=b+2^h*(12*t) := by rw [repr,Nat.pow_add]; grind
  have yu : 3*y=3*b+2^(h+2)*(9*t) := by rw [repr]; grind
  have L := track_lift h b (12*t)
  have U := track_lift (h+2) (3*b) (9*t)
  rw [←yl] at L
  rw [←yu,upper] at U
  have lr : l.1+3^l.2*(12*t)=M m := by rw [←lower,←track_run h y 0,L]
  have ur : u.1+3^u.2*(9*t)=2^(m-2) := (congrArg Prod.fst U).symm
  have gr : u.2=r := (congrArg Prod.snd U).symm
  have p4 : 2^m=4*2^(m-2) := by
    rw [show (4:Nat)=2^2 by decide,←Nat.pow_add]; congr 1; omega
  have branch : l.1+1+12*3^l.2*t=4*u.1+36*3^u.2*t := by
    unfold M at lr
    have nonzero := Nat.two_pow_pos m
    grind
  have prec : 2^(h-2)≤2^16 := Nat.pow_le_pow_right (by decide) (by omega)
  have bs : b≤2^22 := by dsimp only [b]; omega
  have cap (v a : Nat) (ha : a≤20) (hv : v≤2^24) : (track a v 0).1≤2^44 := by
    rw [track_run]
    have product : 2^a*v≤2^20*2^24 :=
      Nat.mul_le_mul (Nat.pow_le_pow_right (by decide : 0<2) ha) hv
    exact Nat.le_trans (run_upper a v) product
  have lc : l.1≤2^44 := cap _ _ (by omega) (by omega)
  have uc : u.1≤2^44 := cap _ _ (by omega) (by omega)
  have brutal : 2^170≤2^(m-2) := Nat.pow_le_pow_right (by decide) (by omega)
  have rate := Nat.mul_le_mul_right (9*t) (Nat.pow_le_pow_right (by decide : 0<3)
    (show u.2≤10 by omega))
  have big : 2^80<t := by omega
  have lr0 : l.1+1=4*u.1 := by
    have z := congrArg (fun x => x%t) branch
    simpa only [Nat.add_mul_mod_self_right,Nat.mod_eq_of_lt (show l.1+1<t by omega),
      Nat.mod_eq_of_lt (show 4*u.1<t by omega)] using z
  have equal : 12*3^l.2=36*3^u.2 := by
    rw [lr0] at branch
    exact Nat.eq_of_mul_eq_mul_right (by omega : 0<t) (Nat.add_left_cancel branch)
  have slope : 81*(3*2^(h+2))≤128*(36*3^u.2) := by
    by_cases v : 81*(3*2^(h+2))≤128*(36*3^u.2)
    · exact v
    have d := Nat.mul_le_mul_right t (show 128*(36*3^u.2)+1≤81*(3*2^(h+2)) by omega)
    have gap : 81*y+271<128*2^m := by
      unfold hardParent at small
      rw [Nat.pow_add] at small
      omega
    grind
  let D := Nat.gcd (9*3^u.2) 243
  have modU : u.1%D=512%D := by
    have reach : 2^(m-2)%D=u.1%D := by
      obtain ⟨v,hv⟩ := Nat.gcd_dvd_left (9*3^u.2) 243
      change 9*3^u.2=D*v at hv
      rw [←ur,show 3^u.2*(9*t)=(9*3^u.2)*t by ac_rfl,hv,Nat.mul_assoc,Nat.add_mul_mod_self_left]
    have dv : D∣243 := Nat.gcd_dvd_right _ _
    have modQ : 2^(m-2)%243=512%243 := term_class j
    rw [←reach,←Nat.mod_mod_of_dvd (2^(m-2)) dv,modQ,Nat.mod_mod_of_dvd _ dv]
  obtain ⟨h7,u3,base⟩ := rank_table hh hi ⟨show u.2≤10 by omega,lr0,equal,slope,modU⟩
  change u.2=3 at u3
  change 81*b+271=512*u.1 at base
  rw [h7] at repr
  rw [u3] at ur
  have exactPrice : 81*y+271=128*2^m := by omega
  unfold hardParent at small
  rw [Nat.pow_add] at small
  omega

#print axioms eleven_required

end Collatz.Itinerary.PassageDescent

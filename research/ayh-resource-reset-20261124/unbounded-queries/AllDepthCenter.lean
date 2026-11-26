import Mathlib.Tactic.Linarith
import CenterPhaseObstruction
import SignedCycleDilation

/-! An all-clock ordinary obstruction to extrapolating the long lower word
past the first source's binary precision. -/
namespace AllDepthCenter
open CollatzReverseBasin WordRank SignedCycleDilation

/-- Inverting a finite shortcut word at the reference -1 costs at most one
factor two for each even input, independently of its odd count. -/
theorem inverse_band (h x : Nat) :
    let p := odds h x
    3^p*(x+1) ≤ 2^h*(run h x+1) ∧
      2^h*(run h x+1) ≤ 3^p*(x+2^(h-p)) := by
  induction h generalizing x with
  | zero => simp [odds,run]
  | succ h ih =>
    let y := shortcut x
    let q := odds h y
    have qle : ∀ n m : Nat, odds n m ≤ n := by
      intro n
      induction n with
      | zero => intro m; rfl
      | succ n hi =>
        intro m
        change m%2+odds n (shortcut m)≤n+1
        have := hi (shortcut m)
        omega
    have small : q≤h := qle h y
    obtain ⟨lo,hi⟩ := ih y
    change 3^q*(y+1) ≤ 2^h*(run h y+1) at lo
    change 2^h*(run h y+1) ≤ 3^q*(y+2^(h-q)) at hi
    change 3^(x%2+q)*(x+1) ≤ 2^(h+1)*(run h y+1) ∧
      2^(h+1)*(run h y+1) ≤ 3^(x%2+q)*(x+2^(h+1-(x%2+q)))
    rw [pow_succ]
    by_cases e : x%2=0
    · have eq : 2*y=x := by dsimp [y,shortcut]; simp only [e,ite_true]; omega
      rw [e,zero_add,show h+1-q=h-q+1 by omega,pow_succ]
      rw [←eq]
      constructor
      · calc
          _ ≤ 2*(3^q*(y+1)) := by ring_nf; omega
          _ ≤ 2*(2^h*(run h y+1)) := Nat.mul_le_mul_left 2 lo
          _ = _ := by ring
      · calc
          _ = 2*(2^h*(run h y+1)) := by ring
          _ ≤ 2*(3^q*(y+2^(h-q))) := Nat.mul_le_mul_left 2 hi
          _ = _ := by ring
    · have o : x%2=1 := by omega
      have eq : 2*y=3*x+1 := by dsimp [y,shortcut]; simp only [e,ite_false]; omega
      rw [o,pow_add,pow_one,show h+1-(1+q)=h-q by omega]
      have pos : 0< (2:Nat)^(h-q) := by positivity
      constructor <;> nlinarith [congrArg (fun v : Nat => 3^q*v) eq,
        Nat.mul_le_mul_left (3^q) (show 1≤2^(h-q) by omega)]

private def trap (v : Nat) : Bool := decide (v=177146 ∨ v=531439 ∨ v=531440)
private def test : Nat → Nat → Nat → Nat → Nat → Bool
  | 0, _, _, _, x => decide (x=1)
  | f+1, w, i, p, x =>
      decide (x=1) || (decide (x≤638468) &&
        (!trap x || decide (w=3233 ∧ i=18 ∧ p=15 ∧ x=177146)) &&
        test f w (i+1) (p+x%2) (shortcut x))

private theorem after_one (h : Nat) (x : Nat) (small : x=1 ∨ x=2) :
    run h x=1 ∨ run h x=2 := by
  induction h generalizing x with
  | zero => exact small
  | succ h ih => apply ih; rcases small with rfl|rfl <;> decide

private theorem test_sound (f w k p x : Nat) (pass : test f w k p x=true) (i : Nat) :
    run i x≤638468 ∧ (trap (run i x)=true →
      w=3233 ∧ k+i=18 ∧ p+odds i x=15 ∧ run i x=177146) := by
  by_cases ended : x=1
  · have t := after_one i x (Or.inl ended)
    rcases t with t|t <;> simp [t,trap]
  cases f with
  | zero => exact False.elim (ended (of_decide_eq_true pass))
  | succ f =>
    simp only [test,Bool.or_eq_true,Bool.and_eq_true,decide_eq_true_eq] at pass
    obtain ⟨⟨mx,pair⟩,next⟩ := pass.resolve_left ended
    cases i with
    | zero =>
      refine ⟨mx,fun h => ?_⟩
      change trap x=true at h
      simpa [h,odds,run] using pair
    | succ i =>
      obtain ⟨mx',rec⟩ := test_sound f w (k+1) (p+x%2) (shortcut x) next i
      refine ⟨mx',fun tr => ?_⟩
      obtain ⟨one,two,three,four⟩ := rec tr
      exact ⟨one,by omega,by change p+(x%2+odds i (shortcut x))=15; omega,four⟩
termination_by f

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
private theorem table : (List.range 68).all
    (fun n => test 107 (48*n+17) 0 0 (48*n+17)) = true := by decide +kernel

private theorem large_gap (n : Nat) : 638468+2^(n+2)<3^(n+13) := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [show n+1+2=(n+2)+1 by omega, show n+1+13=(n+13)+1 by omega,
      pow_succ (2:Nat),pow_succ (3:Nat)]
    omega

/-- Exact ordinary audit at every clock, including all later 1,2 laps. -/
theorem cutoff_trap (w i r : Nat) (res : w%48=17) (size : w<3236) (rr : 11≤r)
    (lo : 3^r ≤ run i w+2^(r-11)) (hi : run i w+1≤3^r) :
    w=3233 ∧ i=18 ∧ odds i w=15 ∧ r=11 := by
  have row := List.all_eq_true.mp table (w/48) (List.mem_range.mpr (by omega))
  change test 107 (48*(w/48)+17) 0 0 (48*(w/48)+17)=true at row
  rw [show 48*(w/48)+17=w by omega] at row
  obtain ⟨mx,tr⟩ := test_sound 107 w 0 0 w row i
  have bound : r≤12 := by
    by_contra! big
    obtain ⟨n,hn⟩ : ∃ n, r=n+13 := ⟨r-13,by omega⟩
    have gap := large_gap n
    rw [hn,show n+13-11=n+2 by omega] at lo
    omega
  rcases (show r=11 ∨ r=12 by omega) with rfl|rfl
  · norm_num at lo hi
    have v : run i w=177146 := by omega
    simpa [v] using tr (by simp [v,trap])
  · norm_num at lo hi
    have h : trap (run i w)=true := by
      unfold trap; apply decide_eq_true
      omega
    have val := (tr h).2.2.2
    omega

#print axioms inverse_band
#print axioms cutoff_trap

private theorem signed_run (h w : Nat) : orbit h (w:Int)=(run h w:Int) := by
  rw [nat_orbit]
  congr 1
  induction h generalizing w with
  | zero => rfl
  | succ h ih => exact ih (shortcut w)

private theorem signed_count (h w : Nat) : count h (w:Int)=odds h w := by
  induction h generalizing w with
  | zero => rfl
  | succ h ih =>
    have st : step (w:Int)=(shortcut w:Int) := signed_run 1 w
    change (if (w:Int)%2=0 then 0 else 1)+count h (step w) = w%2+odds h (shortcut w)
    rw [st,ih]
    split <;> omega

private theorem pos_of_orbit (i : Nat) (x : Int) (pos : 0<orbit i x) : 0<x := by
  induction i generalizing x with
  | zero => exact pos
  | succ i ih =>
    have hp := ih (step x) pos
    unfold step at hp
    split at hp <;> omega

private theorem shift_back (h w : Nat) (c x : Int) (eq : x=(w:Int)-2^h*c) :
    orbit h x=(run h w:Int)-3^(odds h w)*c := by
  rw [eq,show (w:Int)-2^h*c=2^h*(-c)+w by ring,lift,signed_run,signed_count]
  ring

private theorem odds_le (n m : Nat) : odds n m ≤ n := by
  induction n generalizing m with
  | zero => rfl
  | succ n ih =>
    change m%2+odds n (shortcut m)≤n+1
    have := ih (shortcut m)
    omega

/-- A source having the specified lower merger and strict slope pays
at least a new ternary digit beyond every congruence 2^n=1 mod 3^(d+1).
There is no bound on the extra odd count u, comparison clock, or m. -/
theorem no_congruent_merger (n d E u w v : Nat) (res : w%48=17)
    (prec : u≤11+n) (tern : 2^n=1+3^d*(3*v))
    (shrink : 81*2^(d+E)<128*3^d)
    (p : odds (d+E+u) w=d+u)
    (hit : run (d+E+u) w+1=2^(11+n-u)*3^u) : False := by
  let a := 11+d+E
  let h := d+E+u
  let x : Int := (w:Int)-2^a*(3*v)
  have de : (0:Nat)<3^d := by positivity
  have denom : (0:Int)<3^d := by positivity
  have full := (inverse_band h w).1
  change 3^(odds (d+E+u) w)*(w+1)≤2^(d+E+u)*(run (d+E+u) w+1) at full
  rw [p,hit,pow_add,
    show 2^(d+E+u)*(2^(11+n-u)*3^u)=2^(a+n)*3^u by
      rw [←Nat.mul_assoc,←pow_add,show d+E+u+(11+n-u)=a+n by dsimp [a]; omega]] at full
  have size : 3^d*(w+1)≤2^a*2^n := by
    rw [←pow_add]
    apply Nat.le_of_mul_le_mul_right (c:=3^u) _ (by positivity)
    simpa only [Nat.mul_assoc,Nat.mul_comm (3^u) (w+1)] using full
  have ws : x<3236 := by
    have sn : (81:Nat)*2^a<262144*3^d := by
      have eq : 2^a=2048*2^(d+E) := by
        change 2^(11+d+E)=_; rw [Nat.add_assoc,pow_add]; rfl
      rw [eq]; omega
    rw [tern] at size
    have si : (3:Int)^d*(w+1)≤2^a*(1+3^d*(3*v)) := by exact_mod_cast size
    have ss : (81:Int)*2^a<262144*3^d := by exact_mod_cast sn
    have strip : (3:Int)^d*(x+1)≤2^a := by dsimp [x]; linarith only [si]
    by_contra! ge
    have big := mul_le_mul_of_nonneg_left (show 3237≤x+1 by omega) denom.le
    linarith only [big,strip,ss,denom]
  have residue : x%48=17 := by
    have eq : (2:Int)^a=16*2^(7+d+E) := by
      rw [show a=4+(7+d+E) by dsimp [a]; omega,pow_add]; rfl
    have rem : (w:Int)%48=17 := by exact_mod_cast res
    dsimp [x]; rw [eq,show (16:Int)*2^(7+d+E)*(3*v)=48*(2^(7+d+E)*v) by ring]
    omega
  by_cases short : u≤11
  · have diff : a=h+(11-u) := by dsimp [a,h]; omega
    have eq : x=(w:Int)-2^h*((2:Int)^(11-u)*(3*v)) := by
      dsimp [x]; rw [diff,pow_add]; ring
    have tr := shift_back h w _ x eq
    change odds h w=d+u at p
    change run h w+1=2^(11+n-u)*3^u at hit
    rw [p] at tr
    have ti : (2:Int)^n=1+3^d*(3*v) := by exact_mod_cast tern
    have hi : (run h w:Int)+1=2^(11+n-u)*3^u := by exact_mod_cast hit
    rw [show 11+n-u=(11-u)+n by omega,pow_add,ti] at hi
    rw [pow_add] at tr
    have target : orbit h x+1=2^(11-u)*3^u := by linarith only [tr,hi]
    have pl : 2 < CenterPhaseObstruction.phase u := by
      have c : ∀ i : Fin 12, 2<CenterPhaseObstruction.phase i.val := by decide +kernel
      exact c ⟨u,by omega⟩
    have pp : 0 < (2:Nat)^(11-u)*3^u := by positivity
    have ppi : (CenterPhaseObstruction.phase u:Int)+1=2^(11-u)*3^u := by
      exact_mod_cast (show CenterPhaseObstruction.phase u+1=2^(11-u)*3^u by
        unfold CenterPhaseObstruction.phase; omega)
    have pos := pos_of_orbit h x (by omega)
    lift x to Nat using pos.le with x ex
    rw [signed_run] at target
    have meet : run h x=CenterPhaseObstruction.phase u := by omega
    have sm : x<3236 := by omega
    have re : x%48=17 := by omega
    by_cases lt : x<3233
    · exact CenterPhaseObstruction.smaller_never_hits x h u re lt short meet
    have old : x=3233 := by omega
    subst x
    have ck := CenterPhaseObstruction.parent_phase_clock h u short meet
    have eqDE : d+E=7 := by dsimp [h] at ck; omega
    rw [eqDE] at shrink
    have big : 5≤d := by
      by_contra! small
      have ub := Nat.pow_le_pow_right (by decide : 0<3) (show d≤4 by omega)
      omega
    have ge := Nat.pow_le_pow_right (by decide : 0<3) big
    have na : a=18 := by dsimp [a]; omega
    have sn : 3^d*(3233+1) ≤ (2:Nat)^a := by
      rw [tern] at size
      have back : (w:Int)=(3233:Int)+2^a*(3*v) := by omega
      have si : (3:Int)^d*(w+1)≤2^a*(1+3^d*(3*v)) := by exact_mod_cast size
      rw [back] at si
      exact_mod_cast (show (3:Int)^d*(3233+1)≤2^a by linarith only [si])
    rw [na] at sn
    omega
  · let t:=u-11
    have len : h=a+t := by dsimp [h,a,t]; omega
    let b:=odds a w
    let q:=odds t (run a w)
    have sum : b+q=d+u := by
      change odds h w=d+u at p
      rwa [len,oddsAdd] at p
    have qlt : q≤t := odds_le _ _
    let r:=b-d
    have br : b=d+r := by dsimp [t] at qlt; dsimp [r]; omega
    have qr : q+r=u := by omega
    have rr : 11≤r := by dsimp [t] at qlt; omega
    have et : t-q=r-11 := by dsimp [t]; omega
    have cnt : odds a w=d+r := br
    have endp : run t (run a w)+1=2^(11+n-u)*3^u := by
      change run h w+1=_ at hit
      rwa [len,runAdd] at hit
    obtain ⟨lo,hi⟩ := inverse_band t (run a w)
    change 3^q*(run a w+1)≤2^t*(run t (run a w)+1) at lo
    change 2^t*(run t (run a w)+1)≤3^q*(run a w+2^(t-q)) at hi
    have splitPow : 2^t*(run t (run a w)+1)=3^q*(2^n*3^r) := by
      rw [endp,←qr,pow_add (3:Nat),
        show 2^t*(2^(11+n-(q+r))*(3^q*3^r))=
          (2^t*2^(11+n-(q+r)))*(3^q*3^r) by ring,←pow_add,
        show t+(11+n-(q+r))=n by dsimp [t]; omega]; ring
    rw [splitPow] at lo hi
    have lower := Nat.le_of_mul_le_mul_left lo (by positivity : 0<3^q)
    have upper := Nat.le_of_mul_le_mul_left hi (by positivity : 0<3^q)
    rw [et,tern] at upper
    rw [tern] at lower
    have li : (run a w:Int)+1≤(1+3^d*(3*v))*3^r := by exact_mod_cast lower
    have ui : ((1:Int)+3^d*(3*v))*3^r≤run a w+2^(r-11) := by exact_mod_cast upper
    have tr := shift_back a w (3*v) x rfl
    rw [cnt,pow_add] at tr
    have low : (3:Int)^r ≤ orbit a x+2^(r-11) := by linarith only [ui,tr]
    have high : orbit a x+1≤(3:Int)^r := by linarith only [li,tr]
    have pospow : (2:Int)^(r-11)<3^r := by
      have a1 := pow_le_pow_right₀ (by decide : (1:Int)≤2) (show r-11<r by omega).le
      have a2 := pow_lt_pow_left₀ (by decide : (2:Int)<3) (by decide : (0:Int)≤2) (show r≠0 by omega)
      omega
    have pos := pos_of_orbit a x (by omega)
    lift x to Nat using pos.le with x ex
    rw [signed_run] at low high
    have re : x%48=17 := by omega
    obtain ⟨base,clock,bits,rval⟩ := cutoff_trap x a r re (by omega) rr
      (by exact_mod_cast low) (by exact_mod_cast high)
    have orig : w=2^a*(3*v)+x := by exact_mod_cast (show (w:Int)=2^a*(3*v)+x by omega)
    have same := (liftPrefix a (3*v) x).2
    rw [←orig,cnt,bits,rval] at same
    have four : d=4 := by omega
    have total : d+E=7 := by dsimp [a] at clock; omega
    rw [total,four] at shrink
    contradiction

#print axioms no_congruent_merger

private theorem power_multiple (a c b t : Nat) (base : a=1+c*b) :
    ∃ y : Nat, a^t=1+c*y := by
  induction t with
  | zero => exact ⟨0,by simp⟩
  | succ t ih =>
    obtain ⟨y,hy⟩ := ih
    exact ⟨y+b+c*y*b,by rw [pow_succ,hy,base]; ring⟩

/-- Denominator growth on the original ordinary parameters for every
normalized lower meeting, including words exceeding the small-source
binary precision. The upper arm and center numerator need no hypotheses. -/
theorem denominator_growth (k t d E u w : Nat) (res : w%48=17)
    (prec : u≤11+162*(3^k*t)) (shrink : 81*2^(d+E)<128*3^d)
    (p : odds (d+E+u) w=d+u)
    (hit : run (d+E+u) w+1=2^(11+162*(3^k*t)-u)*3^u) : k+5≤d := by
  by_contra! small
  obtain ⟨v,hv⟩ := TernaryPowerLift.period (k+4)
  rw [show 2*3^(k+4)=162*3^k by rw [pow_add]; ring] at hv
  obtain ⟨y,hy⟩ := power_multiple _ _ _ t hv
  rw [←pow_mul, Nat.mul_assoc] at hy
  have pp : 3^(k+4+1)=3^d*(3*3^(k+4-d)) := by
    rw [←pow_succ',←pow_add]
    congr 1; omega
  rw [pp] at hy
  exact no_congruent_merger (162*(3^k*t)) d E u w (3^(k+4-d)*y) res prec
    (by rw [hy]; ring) shrink p hit

#print axioms denominator_growth
end AllDepthCenter

import SmoothCore
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Linarith

namespace Collatz.AnchorDescent
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.SmoothCore

private theorem run_add (i j x : Nat) : run (i+j) x = run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem one_pairs (d t : Nat) : run (2*d) (1+4^d*t)=1+3^d*t := by
  induction d generalizing t with
  | zero => simp [run]
  | succ d ih =>
    let u := 4^d*t
    have e : 1+4^(d+1)*t=1+4*u := by dsimp [u]; ring
    have p : step (1+4*u)=2+6*u := by unfold step; split <;> omega
    have q : step (2+6*u)=1+3*u := by unfold step; split <;> omega
    rw [e, show 2*(d+1)=(2*d+1)+1 by omega]
    simp only [run,p,q]
    rw [show 1+3*u=1+4^d*(3*t) by dsimp [u]; ring, ih]
    ring

/-- The two literal endpoints of the positive-cycle transfer. -/
theorem positive_meeting {a h : Nat} (hit : run h a=1) (d t : Nat) :
    run (h+2*d) (a+2^h*4^d*t) = run h (a+2^h*3^d*t) := by
  rw [run_add, Nat.mul_assoc, Nat.mul_assoc, lift, lift, hit]
  rw [show 3^(odds h a)*(4^d*t) = 4^d*(3^(odds h a)*t) by ring, one_pairs]
  ring

/-- Source-preserving change of ternary exponent, with a strictly smaller base.
    No bound on either exponent or on the clock of the smaller-base anchor. -/
theorem grade_gain {r d b h t w : Nat} (hd : 0<d) (hb : 0<b)
    (hit : run h (3^(r+d)*b)=1) (src : w=3^d*b+2^h*4^d*t) :
    0<b+2^h*t ∧ b+2^h*t<w ∧
    run (h+2*d) (3^r*w) = run h (3^(r+d)*(b+2^h*t)) := by
  have gain : 1< (3:Nat)^d := Nat.one_lt_pow (by omega) (by decide)
  have base := Nat.mul_lt_mul_of_pos_right gain hb
  have factor := Nat.one_le_pow d 4 (by decide)
  have shift := Nat.mul_le_mul_left (2^h*t) factor
  have shift' : 2^h*t ≤ 2^h*4^d*t := by simpa only [Nat.mul_one, Nat.mul_right_comm] using shift
  refine ⟨by omega,by omega,?_⟩
  have eq := positive_meeting hit d (3^r*t)
  convert eq using 2 <;> simp only [src,pow_add] <;> ring

theorem exclude_first_tower {w r d b h t : Nat} (tower : FirstTower w r)
    (hd : 0<d) (hb : 0<b) (hit : run h (3^(r+d)*b)=1)
    (src : w=3^d*b+2^h*4^d*t) : False := by
  obtain ⟨pos,lt,meet⟩ := grade_gain hd hb hit src
  apply tower.bad
  apply (good_run (h+2*d) _).mp
  rw [meet]
  exact (good_run h _).mpr (tower.smaller _ pos lt _)

private theorem anchor_numerator (k : Nat) :
    ∃ b : Nat, 0<b ∧ 2^(2*3^k)=1+3^(k+1)*b := by
  induction k with
  | zero => exact ⟨1,by decide,by decide⟩
  | succ k ih =>
    obtain ⟨b,hb,eq⟩ := ih
    let q := 3^k*b
    refine ⟨b*(1+3*q+3*q^2),Nat.mul_pos hb (by omega),?_⟩
    rw [show 2*3^(k+1)=(2*3^k)*3 by ring,pow_mul,eq]
    dsimp [q]; ring

private theorem halve_pow (n : Nat) : run n (2^n)=1 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have eq : step (2^(n+1))=2^n := by rw [pow_succ]; unfold step; split <;> omega
    rw [run,eq,ih]

private theorem one_odd_power {a h : Nat} (hh : 0<h) (eq : 2^h=1+3*a) :
    run h a=1 := by
  obtain ⟨z,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hh)
  rw [pow_succ] at eq
  have st : step a=2^z := by unfold step; split <;> omega
  rw [run,st,halve_pow]

/-- Every initial exponent and every positive requested exponent gain admit
    one fixed ordinary anchor and a whole explicit progression of bases. -/
theorem all_exponents (r d : Nat) (hd : 0<d) :
    let h := 2*3^(r+d)
    ∃ b : Nat, 0<b ∧ run h (3^(r+d)*b)=1 ∧
      ∀ t : Nat, let w := 3^d*b+2^h*4^d*t
        0<b+2^h*t ∧ b+2^h*t<w ∧
        run (h+2*d) (3^r*w) = run h (3^(r+d)*(b+2^h*t)) := by
  dsimp only
  obtain ⟨b,hb,eq⟩ := anchor_numerator (r+d)
  have positive : 0<2*3^(r+d) := Nat.mul_pos (by decide) (Nat.pow_pos (by decide))
  have shape : 2^(2*3^(r+d))=1+3*(3^(r+d)*b) := by rw [eq]; ring
  have hit := one_odd_power positive shape
  exact ⟨b,hb,hit,fun t => grade_gain hd hb hit rfl⟩

private theorem start_le (h n : Nat) : n≤2^h*run h n := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih =>
    have st : n≤2*step n := by unfold step; split <;> omega
    calc
      n ≤ 2*step n := st
      _ ≤ 2*(2^h*run h (step n)) := Nat.mul_le_mul_left _ (ih _)
      _ = 2^(h+1)*run (h+1) n := by simp [run,pow_succ]; ring

private theorem square_pow (d : Nat) : 4^d=(2^d:Nat)*2^d := by
  rw [show (4:Nat)=2*2 by decide,mul_pow]

private theorem three_coprime_gap (d : Nat) (hd : 0<d) : Nat.Coprime 3 (4^d-3^d) := by
  have four : (4:Nat)^d%3=1 := by rw [Nat.pow_mod]; simp
  have three : (3:Nat)^d%3=0 := by cases d with
    | zero => omega
    | succ k => rw [pow_succ]; omega
  have le : (3:Nat)^d≤4^d := Nat.pow_le_pow_left (by decide) d
  have res : (4^d-3^d)%3=1 := by omega
  change Nat.gcd 3 (4^d-3^d) = 1
  rw [Nat.gcd_rec,res]; decide

private theorem common_power {w r a h d t s b : Nat} (hd : 0<d)
    (src : 3^r*w=a+2^h*4^d*t) (dst : 3^s*b=a+2^h*3^d*t) :
    3^(min r s) ∣ a ∧ 3^(min r s) ∣ t := by
  let k := min r s
  have xdiv : 3^k ∣ 3^r*w := dvd_mul_of_dvd_left (Nat.pow_dvd_pow 3 (min_le_left _ _)) w
  have ydiv : 3^k ∣ 3^s*b := dvd_mul_of_dvd_left (Nat.pow_dvd_pow 3 (min_le_right _ _)) b
  rw [src] at xdiv
  rw [dst] at ydiv
  have le : (3:Nat)^d≤4^d := Nat.pow_le_pow_left (by decide) d
  have gap := Nat.sub_add_cancel le
  have decomp : a+2^h*4^d*t = (a+2^h*3^d*t) + (2^h*(4^d-3^d))*t := by
    calc
      _ = a+2^h*((4^d-3^d)+3^d)*t := by rw [gap]
      _ = _ := by ring
  rw [decomp] at xdiv
  have cancel := Nat.dvd_add_right ydiv |>.mp xdiv
  have cop := ((show Nat.Coprime 3 2 by decide).pow_right h).mul_right (three_coprime_gap d hd)
  have td : 3^k ∣ t := (cop.pow_left k).dvd_of_dvd_mul_left cancel
  have ad : 3^k ∣ a := (Nat.dvd_add_left (dvd_mul_of_dvd_right td _)).mp ydiv
  exact ⟨ad,td⟩

private theorem slope_lower (h n : Nat) : 3^(odds h n)*n ≤ 2^h*run h n := by
  induction h generalizing n with
  | zero => simp [run,odds]
  | succ h ih =>
    have st : 3^(n%2)*n ≤ 2*step n := by
      by_cases hz : n%2=0
      · simp [step,hz]; omega
      · have ho : n%2=1 := by omega
        simp [step,ho]; omega
    calc
      _ = 3^(odds h (step n))*(3^(n%2)*n) := by simp [odds,pow_add]; ring
      _ ≤ 3^(odds h (step n))*(2*step n) := Nat.mul_le_mul_left _ st
      _ = 2*(3^(odds h (step n))*step n) := by ring
      _ ≤ 2*(2^h*run h (step n)) := Nat.mul_le_mul_left _ (ih _)
      _ = _ := by simp [run,pow_succ]; ring

/-- Every point in the same binary cylinder as a source hitting one contracts
    by at least the factor a at the anchor's hitting clock. -/
theorem anchor_contraction {a h : Nat} (hit : run h a=1) (u : Nat) :
    a*run h (a+2^h*u) ≤ a+2^h*u := by
  have slope := slope_lower h a
  rw [hit,Nat.mul_one] at slope
  rw [lift,hit]
  have scale := Nat.mul_le_mul_right u slope
  nlinarith only [scale]

/-- Every positive-cycle anchor which lands on any smaller ternary base
    already produces a literal ordinary endpoint below the original base. -/
theorem positive_anchor_native {w r a h d t s b : Nat} (ha : 0<a)
    (hd : 0<d) (ht : 0<t) (hit : run h a=1)
    (src : 3^r*w=a+2^h*4^d*t) (dst : 3^s*b=a+2^h*3^d*t)
    (lt : b<w) : run (h+2*d) (3^r*w)<w := by
  have common := positive_meeting hit d t
  have bound := anchor_contraction hit (3^d*t)
  rw [←Nat.mul_assoc] at bound
  rw [src,common]
  have power := Nat.le_of_dvd ha (common_power hd src dst).1
  have strict : 3^d< (4:Nat)^d := Nat.pow_lt_pow_left (by decide) (by omega)
  have gap := Nat.mul_lt_mul_of_pos_right
    (Nat.mul_lt_mul_of_pos_left strict (show 0<2^h from Nat.pow_pos (by decide))) ht
  apply Nat.lt_of_mul_lt_mul_left (a:=a)
  refine bound.trans_lt ?_
  by_cases order : r≤s
  · rw [min_eq_left order] at power
    have compare := Nat.mul_le_mul_right w power
    omega
  · rw [min_eq_right (by omega : s≤r)] at power
    have compare := Nat.mul_le_mul_right b power
    have blt := Nat.mul_lt_mul_of_pos_left lt ha
    omega

/-- On the constructive grade-gain row the earlier anchor clock itself
    already reaches an ordinary integer below the original base. -/
theorem grade_gain_native {r d b h t w : Nat} (hd : 0<d) (hb : 0<b)
    (hit : run h (3^(r+d)*b)=1) (src : w=3^d*b+2^h*4^d*t) :
    run h (3^r*w)<w := by
  have eq : 3^r*w=3^(r+d)*b+2^h*(4^d*3^r*t) := by rw [src,pow_add]; ring
  have bound := anchor_contraction hit (4^d*3^r*t)
  rw [←eq] at bound
  have grow := Nat.mul_le_mul_left (3^(r+d)) (show 1≤b by omega)
  have powgt : (3:Nat)^r<3^(r+d) := Nat.pow_lt_pow_right (by decide) (by omega)
  have wpos : 0<w := by have := Nat.mul_pos (Nat.pow_pos (show 0<3 by decide) : 0<3^d) hb; omega
  apply Nat.lt_of_mul_lt_mul_left (a:=3^(r+d)*b)
  exact bound.trans_lt (Nat.mul_lt_mul_of_pos_right (by omega) wpos)

/-- Every positive-cycle anchor transfer landing immediately on a smaller
    ternary base must start with exponent factor strictly below its base.
    The anchor, its hitting clock and the number of cycles are unrestricted. -/
theorem positive_anchor_scale {w r a h d t s b : Nat}
    (ha : 0<a) (hd : 0<d) (ht : 0<t) (hit : run h a=1)
    (src : 3^r*w=a+2^h*4^d*t) (dst : 3^s*b=a+2^h*3^d*t)
    (hw : 0<w) (smallBase : b≤w) : 3^r<w := by
  let k := min r s
  obtain ⟨ad,td⟩ := common_power hd src dst
  have le : (3:Nat)^d≤4^d := Nat.pow_le_pow_left (by decide) d
  have atMost : 3^k ≤ 2^h := (Nat.le_of_dvd ha ad).trans (by simpa [hit] using start_le h a)
  have tMin := Nat.le_of_dvd ht td
  have sq := Nat.mul_le_mul atMost tMin
  have sqBound : (2^d*3^k)*(2^d*3^k) < 3^r*w := by
    calc
      _ = 4^d*(3^k*3^k) := by rw [square_pow]; ring
      _ ≤ 4^d*(2^h*t) := Nat.mul_le_mul_left _ sq
      _ < 3^r*w := by rw [src,show 4^d*(2^h*t)=2^h*4^d*t by ring]; omega
  have wt : 3^r ≤ 2^d*3^k := by
    by_cases small : r≤s
    · have eq : k=r := min_eq_left small
      rw [eq]
      simpa only [Nat.one_mul] using Nat.mul_le_mul_right (3^r) (Nat.one_le_pow d 2 (by decide))
    · have eq : k=s := min_eq_right (by omega)
      rw [eq]
      have comp : 3^d*(3^r*w) ≤ 4^d*(3^s*b) := by
        rw [src,dst]
        have := Nat.mul_le_mul_right a le
        nlinarith only [this]
      have sb := Nat.mul_le_mul_left (4^d*3^s) smallBase
      have baseProd : (3^d*3^r)*w ≤ (4^d*3^s)*w := by
        calc
          _ = 3^d*(3^r*w) := by ring
          _ ≤ 4^d*(3^s*b) := comp
          _ = (4^d*3^s)*b := by ring
          _ ≤ _ := sb
      have cut := Nat.le_of_mul_le_mul_right baseProd hw
      have tw := Nat.pow_le_pow_left (show 2≤3 by decide) d
      apply Nat.le_of_mul_le_mul_left (c:=2^d)
      · calc
          2^d*3^r ≤ 3^d*3^r := Nat.mul_le_mul_right _ tw
          _ ≤ 4^d*3^s := cut
          _ = 2^d*(2^d*3^s) := by rw [square_pow]; ring
      · exact Nat.pow_pos (by decide)
  exact Nat.lt_of_mul_lt_mul_left ((Nat.mul_self_le_mul_self wt).trans_lt sqBound)

/-- Magnitude dynamics on negative integer anchors. -/
def negStep (m : Nat) : Nat := if m%2=0 then m/2 else (3*m-1)/2

def negRun : Nat → Nat → Nat
  | 0, m => m
  | h+1, m => negRun h (negStep m)

def negOdds : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, m => m%2 + negOdds h (negStep m)

private theorem negative_size (h m : Nat) : m ≤ 2^h*negRun h m := by
  induction h generalizing m with
  | zero => simp [negRun]
  | succ h ih =>
    have st : m≤2*negStep m := by unfold negStep; split <;> omega
    calc
      _ ≤ 2*negStep m := st
      _ ≤ 2*(2^h*negRun h (negStep m)) := Nat.mul_le_mul_left _ (ih _)
      _ = _ := by simp [negRun,pow_succ]; ring

private theorem negative_slope (e m : Nat) : 2^e*negRun e m ≤ 3^(negOdds e m)*m := by
  induction e generalizing m with
  | zero => simp [negRun,negOdds]
  | succ e ih =>
    have st : 2*negStep m ≤ 3^(m%2)*m := by
      by_cases hz : m%2=0
      · simp [negStep,hz]; omega
      · have ho : m%2=1 := by omega
        simp [negStep,ho]; omega
    calc
      _ = 2*(2^e*negRun e (negStep m)) := by simp [negRun,pow_succ]; ring
      _ ≤ 2*(3^(negOdds e (negStep m))*negStep m) := Nat.mul_le_mul_left _ (ih _)
      _ = 3^(negOdds e (negStep m))*(2*negStep m) := by ring
      _ ≤ 3^(negOdds e (negStep m))*(3^(m%2)*m) := Nat.mul_le_mul_left _ st
      _ = _ := by simp [negOdds,pow_add]; ring

private theorem negative_cycle_expands {e C : Nat} (he : 0<e) (hc : 0<C)
    (lap : negRun e C=C) : 2^e < 3^(negOdds e C) := by
  have s := negative_slope e C
  rw [lap] at s
  have weak := Nat.le_of_mul_le_mul_right s hc
  have even : (2:Nat)^e%2=0 := by
    cases e with
    | zero => omega
    | succ n => rw [pow_succ]; omega
  have odd : (3:Nat)^(negOdds e C)%2=1 := by rw [Nat.pow_mod]; simp
  omega

private theorem shadow (h x m t : Nat) (source : x+m=2^h*t) :
    run h x + negRun h m = 3^(negOdds h m)*t := by
  induction h generalizing x m t with
  | zero => simpa [run,negRun,negOdds] using source
  | succ h ih =>
    rw [show 2^(h+1)*t=2*(2^h*t) by ring] at source
    have paired : step x+negStep m=2^h*(3^(m%2)*t) := by
      by_cases ev : m%2=0
      · have xe : x%2=0 := by omega
        simp [step,negStep,ev,xe]; omega
      · have mo : m%2=1 := by omega
        have xo : x%2=1 := by omega
        simp [step,negStep,mo,xo]
        rw [show 2^h*(3*t)=3*(2^h*t) by ring]; omega
    have next := ih (step x) (negStep m) _ paired
    simp only [run,negRun,negOdds,pow_add]
    rw [next]; ring

/-- A negative periodic shadow gives a physical meeting on positive inputs,
    at two possibly different clocks on the same positive shortcut map. -/
theorem negative_meeting {x y m C h e t : Nat} (hit : negRun h m=C)
    (lap : negRun e C=C) (src : x+m=2^h*2^e*t)
    (dst : y+m=2^h*3^(negOdds e C)*t) :
    run (h+e) x = run h y := by
  rw [Nat.mul_assoc] at src dst
  have lo := shadow h x m _ src
  have hi := shadow h y m _ dst
  rw [hit] at lo hi
  rw [show 3^(negOdds h m)*(2^e*t) = 2^e*(3^(negOdds h m)*t) by ring] at lo
  have endLo := shadow e _ C _ lo
  rw [lap] at endLo
  rw [run_add]
  rw [show 3^(negOdds h m)*(3^(negOdds e C)*t) =
    3^(negOdds e C)*(3^(negOdds h m)*t) by ring] at hi
  omega

/-- Even an unbounded negative preperiod and an arbitrary expanding signed
    cycle cannot land immediately on a nonincreasing ternary base outside this strip.
    C is the actual magnitude of the chosen periodic phase. -/
theorem negative_anchor_scale {w r m C h e t s b : Nat}
    (hm : 0<m) (hc : 0<C) (he : 0<e) (ht : 0<t)
    (hit : negRun h m=C) (lap : negRun e C=C)
    (src : 3^r*w+m=2^h*2^e*t)
    (dst : 3^s*b+m=2^h*3^(negOdds e C)*t) (hw : 0<w) (smallBase : b≤w) : 3^r≤C*w := by
  let p := negOdds e C
  have up : 2^e<3^p := negative_cycle_expands he hc lap
  change 3^s*b+m=2^h*3^p*t at dst
  have stepp := Nat.mul_lt_mul_of_pos_right (Nat.mul_lt_mul_of_pos_left up (show 0<2^h from Nat.pow_pos (by decide))) ht
  have rs : r<s := by
    by_contra no
    have ord := Nat.pow_le_pow_right (by decide : 0<3) (show s≤r by omega)
    have pair := Nat.mul_le_mul ord smallBase
    omega
  have xdiv : 3^r ∣ 3^r*w := dvd_mul_right _ _
  have ydiv : 3^r ∣ 3^s*b := dvd_mul_of_dvd_left (Nat.pow_dvd_pow 3 rs.le) _
  have g := Nat.sub_add_cancel up.le
  have diff : 3^s*b=3^r*w+(2^h*(3^p-2^e))*t := by
    have add : 2^h*3^p*t=2^h*2^e*t+(2^h*(3^p-2^e))*t := by
      calc
        _ = 2^h*((3^p-2^e)+2^e)*t := by rw [g]
        _ = _ := by ring
    omega
  rw [diff] at ydiv
  have gd := (Nat.dvd_add_right xdiv).mp ydiv
  have pp : 0<p := by
    by_contra nz
    have : p=0 := by omega
    rw [this,pow_zero] at up
    have := Nat.one_le_pow e 2 (by decide); omega
  have tern : (3:Nat)^p%3=0 := by
    obtain ⟨z,hz⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt pp)
    rw [hz,pow_succ]; omega
  have allUnit : ∀ n : Nat, (2:Nat)^n%3=1 ∨ 2^n%3=2 := by
    intro n
    induction n with
    | zero => decide
    | succ n ih =>
      rw [pow_succ,Nat.mul_mod]
      rcases ih with l|l <;> rw [l] <;> decide
  have unit := allUnit e
  have cp : Nat.Coprime 3 (3^p-2^e) := by
    change Nat.gcd 3 (3^p-2^e)=1
    rw [Nat.gcd_rec]
    have : (3^p-2^e)%3=1 ∨ (3^p-2^e)%3=2 := by omega
    rcases this with l|l <;> rw [l] <;> decide
  have cop := ((show Nat.Coprime 3 2 by decide).pow_right h).mul_right cp
  have td : 3^r ∣ t := (cop.pow_left r).dvd_of_dvd_mul_left gd
  have md : 3^r ∣ m := (Nat.dvd_add_right xdiv).mp
    (src ▸ dvd_mul_of_dvd_right td _)
  have lower := Nat.le_of_dvd hm md
  have upper := negative_size h m
  rw [hit] at upper
  by_cases sm : 3^r ≤ C
  · exact sm.trans (by simpa using Nat.mul_le_mul_left C (show 1≤w from hw))
  have large := Nat.le_of_dvd ht td
  have two : 2≤(2:Nat)^e := Nat.one_lt_pow (by omega) (by decide)
  have big := Nat.mul_le_mul (Nat.mul_le_mul_left (2^h) two) large
  have little := Nat.mul_le_mul_left (2^h) (show C≤3^r by omega)
  have base : 2^h≤w := by
    apply Nat.le_of_mul_le_mul_right (c:=3^r) _ (Nat.pow_pos (by decide))
    nlinarith only [big,src,upper,little]
  exact lower.trans (upper.trans ((Nat.mul_le_mul_right C base).trans_eq (by ring)))

/-- This ordinary source descends below its base despite lying above the
    entire strip for every negative periodic phase up through magnitude 136. -/
theorem anchor_control : 136*5<3^6 ∧ run 29 (3^6*5)=4 ∧
    ∀ i : Fin 29, 5≤run i.val (3^6*5) := by decide

#print axioms positive_meeting
#print axioms grade_gain
#print axioms all_exponents
#print axioms exclude_first_tower
#print axioms anchor_contraction
#print axioms grade_gain_native
#print axioms positive_anchor_native
#print axioms positive_anchor_scale
#print axioms negative_meeting
#print axioms negative_anchor_scale
#print axioms anchor_control
end Collatz.AnchorDescent

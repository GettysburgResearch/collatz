import SourceDeletion
import Mathlib.Data.Nat.GCD.Basic

/-! Literal shortcut paths. The word order is chronological.
Distinct words may have the same affine constant and different odd counts. -/
namespace Collatz.TowerClock

open Collatz.SourceDeletion

def weight : List Bool → Nat
  | [] => 0
  | a :: v => a.toNat + weight v

def carry : List Bool → Nat
  | [] => 0
  | a :: v => a.toNat * 3^(weight v) + 2 * carry v

def trace : Nat → Nat → List Bool
  | 0, _ => []
  | t+1, n => (n%2 == 1) :: trace t (step n)

@[simp] theorem trace_length (t n : Nat) : (trace t n).length = t := by
  induction t generalizing n <;> simp_all [trace]

theorem weight_le (v : List Bool) : weight v ≤ v.length := by
  induction v with
  | nil => simp [weight]
  | cons a v ih => cases a <;> simp [weight] <;> omega

private theorem three_pow_odd (k : Nat) : 3^k%2=1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ,Nat.mul_mod,ih]

theorem carry_bound (v : List Bool) : carry v + 2^v.length ≤ 3^v.length := by
  induction v with
  | nil => decide
  | cons a v ih =>
    have hw := Nat.pow_le_pow_right (by decide : 0 < 3) (weight_le v)
    cases a <;> simp only [carry,List.length_cons,pow_succ,Bool.toNat_false,
      Bool.toNat_true,zero_mul,one_mul,zero_add] <;> omega

private theorem step_num (n : Nat) : 2*step n=3^(n%2)*n+n%2 := by
  by_cases e : n%2=0
  · simp [step,e]; omega
  · have o : n%2=1 := by omega
    simp [step,o]; omega

/-- Integrality of the proposed endpoint forces every parity decision. -/
theorem word_iff (v : List Bool) (n y : Nat) :
    2^v.length*y = 3^(weight v)*n + carry v ↔
    trace v.length n = v ∧ run v.length n = y := by
  induction v generalizing n y with
  | nil => simp [weight,carry,trace,run,eq_comm]
  | cons a v ih =>
    let P := 3^(weight v)
    let c := a.toNat
    change 2^(v.length+1)*y = 3^(c+weight v)*n+(c*P+2*carry v) ↔ _
    rw [show 2^(v.length+1)*y=2*(2^v.length*y) by ring, pow_add]
    change 2*(2^v.length*y) = 3^c*P*n + (c*P+2*carry v) ↔ _
    rw [show 3^c*P*n+(c*P+2*carry v)=P*(3^c*n+c)+2*carry v by ring]
    have po : P%2=1 := three_pow_odd _
    have qo : 3^c%2=1 := three_pow_odd _
    have cv : c=0 ∨ c=1 := by cases a <;> simp [c]
    have bit : n%2=c ↔ (n%2 == 1)=a := by
      cases a <;> simp [c]
    constructor
    · intro e
      have par : n%2=c := by
        have m := congrArg (·%2) e
        simp [Nat.add_mod,Nat.mul_mod P, Nat.mul_mod (3^c),po,qo] at m
        omega
      rw [← par, ← step_num] at e
      rw [show P*(2*step n)=2*(P*step n) by ring] at e
      have tail : 2^v.length*y=P*step n+carry v := by omega
      obtain ⟨tr,eq⟩ := (ih (step n) y).mp tail
      simp [trace,run,bit.mp par,tr,eq]
    · rintro ⟨tr,eq⟩
      change ((n%2 == 1)::trace v.length (step n))=a::v at tr
      obtain ⟨hd,tl⟩ := List.cons.inj tr
      have tail := (ih (step n) y).mpr ⟨tl,eq⟩
      rw [← bit.mpr hd, ← step_num,tail]
      change 2*(P*step n+carry v)=P*(2*step n)+2*carry v
      ring

theorem physical_affine (t n : Nat) :
    2^t * run t n = 3^(weight (trace t n))*n + carry (trace t n) := by
  simpa using (word_iff (trace t n) n (run t n)).mpr (by simp)

/-- A positive construction. Any heavier word in the same constant fiber
is automatically legal at the corresponding lower power of three. -/
theorem lower_power_meeting {t x z d : Nat} {v : List Bool}
    (len : v.length=t) (same : carry v = carry (trace t x))
    (weightEq : weight v = weight (trace t x)+d) (source : x=3^d*z) :
    trace t z=v ∧ run t z=run t x := by
  have a := physical_affine t x
  have b : 3^(weight v)*z=3^(weight (trace t x))*x := by
    rw [weightEq,pow_add,show 3^(weight (trace t x))*3^d*z=3^(weight (trace t x))*(3^d*z) by ring,←source]
  have := (word_iff v z (run t x)).mp (by rw [len,same,b]; exact a)
  simpa [len] using this

private def slope (H t n : Nat) := 2^(H-t)*3^(weight (trace t n))
private def offset (H t n : Nat) := 2^(H-t)*carry (trace t n)

private theorem bounded (H t n : Nat) (ht : t≤H) :
    0 < slope H t n ∧ slope H t n ≤ 3^H ∧ offset H t n < 3^H := by
  have small : 2^(H-t)*3^t ≤ 3^H := by
    calc
      _ ≤ 3^(H-t)*3^t := Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide) _)
      _ = _ := by rw [←pow_add,Nat.sub_add_cancel ht]
  have w : weight (trace t n) ≤ t := by simpa using weight_le (trace t n)
  have b : carry (trace t n) + 2^t ≤ 3^t := by simpa using carry_bound (trace t n)
  have pos : 0 < 2^t := Nat.pow_pos (by decide)
  refine ⟨Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide)),?_,?_⟩
  · exact (Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide : 0<3) w)).trans small
  · exact (Nat.mul_lt_mul_of_pos_left (show carry (trace t n)<3^t by omega)
      (Nat.pow_pos (by decide : 0<2))).trans_le small

private theorem normalized (H t n : Nat) (ht : t≤H) :
    2^H*run t n=slope H t n*n+offset H t n := by
  calc
    _ = 2^(H-t)*(2^t*run t n) := by rw [←Nat.mul_assoc,←pow_add,Nat.sub_add_cancel ht]
    _ = _ := by rw [physical_affine]; unfold slope offset; ring

private theorem same_twos {i j a b : Nat} (oa : a%2=1) (ob : b%2=1)
    (e : 2^i*a=2^j*b) : i=j ∧ a=b := by
  induction i generalizing j with
  | zero =>
    cases j with
    | zero => simpa using e
    | succ j => rw [pow_succ] at e; simp only [pow_zero,one_mul] at e
                rw [show 2^j*2*b=2*(2^j*b) by ring] at e; omega
  | succ i ih =>
    cases j with
    | zero => rw [pow_succ] at e; simp only [pow_zero,one_mul] at e
              rw [show 2^i*2*a=2*(2^i*a) by ring] at e; omega
    | succ j =>
      rw [show 2^(i+1)*a=2*(2^i*a) by ring, show 2^(j+1)*b=2*(2^j*b) by ring] at e
      obtain ⟨ij,ab⟩ := ih (show 2^i*a=2^j*b by omega)
      exact ⟨by omega,ab⟩

/-- Every short literal meeting with the entire lower-base cone is a
synchronous meeting on the same base. The source b may be even and the
shared forward endpoint may have either parity. -/
theorem short_meeting_rigid {H f h r j w b : Nat}
    (hf : f≤H) (hh : h≤H) (tall : 2*H≤r)
    (c2 : w.Coprime 2) (c3 : w.Coprime 3) (hb : 0<b) (bw : b≤w)
    (meet : run f (3^r*w) = run h (3^j*b)) :
    b=w ∧ f=h ∧ carry (trace f (3^r*w))=carry (trace h (3^j*b)) ∧
    weight (trace f (3^r*w))+r = weight (trace h (3^j*b))+j := by
  let x := 3^r*w
  let z := 3^j*b
  have p := normalized H f x hf
  have q := normalized H h z hh
  change run f x=run h z at meet
  rw [meet] at p
  have eq := p.symm.trans q
  obtain ⟨spx,_,ox⟩ := bounded H f x hf
  obtain ⟨_,sbz,oz⟩ := bounded H h z hh
  have size : x < 3^H*(z+1) := by
    have lhs := Nat.mul_le_mul_right x (show 1 ≤ slope H f x by omega)
    have rhs := Nat.mul_le_mul_right z sbz
    simp only [one_mul] at lhs
    rw [Nat.mul_add,Nat.mul_one]
    omega
  have hj : H≤j := by
    by_contra no
    have ex : H+j+1≤r := by omega
    have lo := Nat.mul_le_mul_right w (Nat.pow_le_pow_right (by decide : 0<3) ex)
    have dw := Nat.mul_le_mul_left (3^j) bw
    have pos : 0<3^j*w := Nat.mul_pos (Nat.pow_pos (by decide)) (by omega)
    have up := Nat.mul_le_mul_left (3^H) (show 3^j*b+1≤3*(3^j*w) by omega)
    change 3^r*w < 3^H*(3^j*b+1) at size
    rw [show 3^(H+j+1)*w=3^H*(3*(3^j*w)) by rw [pow_succ,pow_add]; ring] at lo
    omega
  have d₁ : 3^H ∣ slope H f x*x := by
    refine dvd_mul_of_dvd_right ?_ _
    exact dvd_mul_of_dvd_left (pow_dvd_pow 3 (by omega : H≤r)) _
  have d₂ : 3^H ∣ slope H h z*z := by
    refine dvd_mul_of_dvd_right ?_ _
    exact dvd_mul_of_dvd_left (pow_dvd_pow 3 hj) _
  have em := congrArg (·%3^H) eq
  rw [Nat.add_mod,Nat.add_mod (slope H h z*z), Nat.mod_eq_zero_of_dvd d₁,
    Nat.mod_eq_zero_of_dvd d₂, Nat.mod_eq_of_lt ox,Nat.mod_eq_of_lt oz] at em
  have ce : offset H f x=offset H h z := by simpa [Nat.mod_eq_of_lt ox,Nat.mod_eq_of_lt oz] using em
  have ne : slope H f x*x=slope H h z*z := by omega
  have reduced : (2^(H-f)*3^(weight (trace f x)+r))*w =
      (2^(H-h)*3^(weight (trace h z)+j))*b := by
    change (2^(H-f)*3^(weight (trace f x)))*(3^r*w) =
      (2^(H-h)*3^(weight (trace h z)))*(3^j*b) at ne
    rw [pow_add,pow_add]
    simpa only [Nat.mul_assoc] using ne
  have div : w ∣ b := by
    apply ((c2.pow_right (H-h)).mul_right (c3.pow_right (weight (trace h z)+j))).dvd_of_dvd_mul_left
    rw [←reduced]
    exact Nat.dvd_mul_left _ _
  have wb : b=w := Nat.le_antisymm bw (Nat.le_of_dvd hb div)
  have rn := reduced
  rw [wb] at rn
  have rc := Nat.mul_right_cancel (by omega : 0<w) rn
  obtain ⟨clock,ew⟩ := same_twos (three_pow_odd _) (three_pow_odd _) rc
  have fh : f=h := by omega
  have carryEq : carry (trace f x)=carry (trace h z) := by
    change 2^(H-f)*carry (trace f x)=2^(H-h)*carry (trace h z) at ce
    rw [clock] at ce
    exact Nat.mul_left_cancel (Nat.pow_pos (by decide)) ce
  exact ⟨wb,fh,carryEq,Nat.pow_right_injective (by decide : 2≤3) ew⟩

/-- Bounded, unconditional characterization; every witness on the right
constructs a literal lower-power source, even without the height hypothesis
if the extra odd count is at most r. -/
theorem short_cone_iff {H r w : Nat} (hw : 0<w) (tall : 2*H≤r)
    (c2 : w.Coprime 2) (c3 : w.Coprime 3) :
    (∃ f h j b, f≤H ∧ h≤H ∧ 0<b ∧ (b<w ∨ (b=w ∧ j<r)) ∧
        run f (3^r*w)=run h (3^j*b)) ↔
    (∃ f v, f≤H ∧ v.length=f ∧ carry v=carry (trace f (3^r*w)) ∧
        weight (trace f (3^r*w)) < weight v) := by
  constructor
  · rintro ⟨f,h,j,b,hf,hh,hb,lt,meet⟩
    have bw : b≤w := by rcases lt with l|⟨e,_⟩ <;> omega
    obtain ⟨e,clock,B,odds⟩ := short_meeting_rigid hf hh tall c2 c3 hb bw meet
    exact ⟨f, trace h (3^j*b),hf,by simpa using clock.symm,B.symm,by
      rcases lt with l|⟨_,lower⟩ <;> omega⟩
  · rintro ⟨f,v,hf,len,B,more⟩
    let a := weight (trace f (3^r*w))
    let d := weight v-a
    have cap : weight v≤f := len ▸ weight_le v
    have wd : weight v=a+d := by dsimp [d,a]; omega
    have split : r=d+(r-d) := by dsimp [d]; omega
    have source : 3^r*w=3^d*(3^(r-d)*w) := by
      calc
        _ = 3^(d+(r-d))*w := congrArg (fun z : Nat => 3^z*w) split
        _ = _ := by rw [pow_add]; ring
    have path := lower_power_meeting len B wd source
    exact ⟨f,f,r-d,w,hf,hf,hw,Or.inr ⟨rfl,by dsimp [d,a]; omega⟩,path.2.symm⟩

theorem all_odd_weight {t n : Nat} (den : 2^t ∣ n+1) :
    weight (trace t n)=t := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih =>
    obtain ⟨m,hm⟩ := den
    rw [show 2^(t+1)*m=2*(2^t*m) by ring] at hm
    have odd : n%2=1 := by omega
    have ns : step n+1=2^t*(3*m) := by
      rw [show 2^t*(3*m)=3*(2^t*m) by ring]
      simp [step,odd]; omega
    simp [trace,odd,weight,ih ⟨_,ns⟩,Nat.add_comm]

/-- A whole ordinary all-odd cylinder, through physical clock H inclusive. -/
theorem all_odd_no_short_cone {H r w : Nat} (hw : 0<w) (tall : 2*H≤r)
    (c2 : w.Coprime 2) (c3 : w.Coprime 3) (den : 2^H ∣ 3^r*w+1) :
    ¬ ∃ f h j b, f≤H ∧ h≤H ∧ 0<b ∧ (b<w ∨ (b=w ∧ j<r)) ∧
        run f (3^r*w)=run h (3^j*b) := by
  intro meet
  obtain ⟨f,v,hf,len,_,more⟩ := (short_cone_iff hw tall c2 c3).mp meet
  have legal := all_odd_weight (dvd_trans (pow_dvd_pow 2 hf) den)
  have bound := weight_le v
  omega

private theorem trace_add (i j n : Nat) :
    trace (i+j) n = trace i n ++ trace j (run i n) := by
  induction i generalizing n with
  | zero => simp [trace,run]
  | succ i ih => simp [Nat.succ_add,trace,run,ih]

private theorem weight_append (u v : List Bool) : weight (u++v)=weight u+weight v := by
  induction u with
  | nil => simp [weight]
  | cons b u ih => simp [weight,ih,Nat.add_assoc]

/-- On 15 versus its only lower power 5, an actual meeting occurs, but a
same-constant heavier word with one extra odd step is impossible at any clock. -/
theorem fifteen_no_affine_return :
    run 8 15=5 ∧ ∀ t v, v.length=t → carry v=carry (trace t 15) →
    weight v ≠ weight (trace t 15)+1 := by
  refine ⟨by decide,?_⟩
  intro t v len B heavier
  have path := lower_power_meeting len B heavier (show 15=3^1*5 by decide)
  have more : weight (trace t 5)=weight (trace t 15)+1 := path.1 ▸ heavier
  by_cases early : t<11
  · have table : ∀ k : Fin 11, weight (trace k.val 5) ≤ weight (trace k.val 15) := by decide
    have ht : weight (trace t 5) ≤ weight (trace t 15) := table ⟨t,early⟩
    omega
  · obtain ⟨j,hj⟩ := Nat.exists_eq_add_of_le (show 11≤t by omega)
    rw [hj,trace_add,trace_add,weight_append,weight_append] at more
    change 5+weight (trace j 2)=5+weight (trace j 2)+1 at more
    omega

private theorem run_sum (m e x : Nat) : run (m+e) x=run e (run m x) := by
  induction m generalizing x with
  | zero => simp [run]
  | succ m ih => simp [Nat.succ_add,run,ih]

private theorem odd_run {m x a : Nat} (den : x+1=2^m*a) :
    run m x+1=3^m*a := by
  induction m generalizing x a with
  | zero => simpa [run] using den
  | succ m ih =>
    rw [show 2^(m+1)*a=2*(2^m*a) by ring] at den
    have odd : x%2=1 := by omega
    have s : step x+1=2^m*(3*a) := by
      rw [show 2^m*(3*a)=3*(2^m*a) by ring]
      simp [step,odd]; omega
    rw [run,ih s]; ring

private theorem halve (e b : Nat) : run e (2^e*b)=b := by
  induction e with
  | zero => simp [run]
  | succ e ih =>
    rw [show 2^(e+1)*b=2*(2^e*b) by ring,run]
    simpa [step] using ih

private theorem odd_endpoint {H f x a : Nat} (hf : f≤H) (start : x+1=2^(H+1)*a) :
    run f x % 2=1 := by
  have E : H+1=f+(H-f+1) := by omega
  have S : x+1=2^f*(2^(H-f+1)*a) := by rw [start,E,pow_add]; ring
  have ep := odd_run S
  rw [show 3^f*(2^(H-f+1)*a)=2*(3^f*2^(H-f)*a) by ring] at ep
  omega

private theorem remove_twos {i h n y : Nat} (odd : y%2=1) (p : run h (2^i*n)=y) :
    ∃ k, k≤h ∧ run k n=y := by
  induction i generalizing h with
  | zero => exact ⟨h,by omega,by simpa using p⟩
  | succ i ih =>
    rw [show 2^(i+1)*n=2*(2^i*n) by ring] at p
    cases h with
    | zero => change 2*(2^i*n)=y at p; omega
    | succ h =>
      have eq : step (2*(2^i*n))=2^i*n := by simp [step]
      rw [run,eq] at p
      obtain ⟨k,hk,e⟩ := ih p
      exact ⟨k,by omega,e⟩

/-- If every target endpoint through H is odd, a free power of two on any
reservoir source can be completely removed within the original source clock. -/
theorem all_odd_no_short_smooth {H r w a : Nat} (hw : 0<w) (tall : 2*H≤r)
    (c2 : w.Coprime 2) (c3 : w.Coprime 3) (start : 3^r*w+1=2^(H+1)*a) :
    ¬ ∃ f h i j b, f≤H ∧ h≤H ∧ 0<b ∧ (b<w ∨ (b=w ∧ j<r)) ∧
        run f (3^r*w)=run h (2^i*(3^j*b)) := by
  rintro ⟨f,h,i,j,b,hf,hh,hb,lower,meet⟩
  obtain ⟨k,hk,p⟩ := remove_twos (odd_endpoint hf start) meet.symm
  have den : 2^H ∣ 3^r*w+1 := by rw [start,pow_succ]; exact ⟨2*a,by ring⟩
  exact all_odd_no_short_cone hw tall c2 c3 den ⟨f,k,j,b,hf,hk.trans hh,hb,lower,p.symm⟩

/-- Two literal runs. The slope budget allows for the additive term in the
affine formula and produces strict descent past the whole base w. -/
theorem two_run_drop {r m e w a b : Nat} (hw : 0<w)
    (start : 3^r*w+1=2^m*a) (exitRow : 3^m*a=2^e*b+1)
    (budget : 2*3^(m+r) ≤ 2^(m+e)) :
    run (m+e) (3^r*w)=b ∧ b<w := by
  have endpoint := odd_run start
  have ep : run m (3^r*w)=2^e*b := by omega
  refine ⟨by rw [run_sum,ep,halve],?_⟩
  by_contra notLess
  have wb : w≤b := by omega
  have left := Nat.mul_le_mul_right w budget
  have upper := Nat.mul_le_mul_left (2^(m+e)) wb
  have eq : 2^(m+e)*b+2^m=3^(m+r)*w+3^m := by
    calc
      _ = 2^m*(2^e*b+1) := by rw [pow_add]; ring
      _ = 3^m*(2^m*a) := by rw [←exitRow]; ring
      _ = _ := by rw [←start,pow_add]; ring
  have pw : 0<3^r*w := Nat.mul_pos (Nat.pow_pos (by decide)) hw
  have delta := Nat.mul_le_mul_left (3^m) (show 1≤3^r*w by omega)
  rw [Nat.mul_one,←Nat.mul_assoc,←pow_add] at delta
  rw [Nat.mul_assoc] at left
  have pos : 0<2^m := Nat.pow_pos (by decide)
  omega

/-- On the same input, every pair of physical clocks up to H misses the
cone, while a cross-base return occurs at exactly the displayed clock. -/
theorem delayed_linear_return {H w a b : Nat} (hw : 0<w)
    (c2 : w.Coprime 2) (c3 : w.Coprime 3)
    (start : 3^(2*H)*w+1=2^(H+1)*a)
    (exitRow : 3^(H+1)*a=2^(5*H+2)*b+1) :
    (¬ ∃ f h i j d, f≤H ∧ h≤H ∧ 0<d ∧ (d<w ∨ (d=w ∧ j<2*H)) ∧
      run f (3^(2*H)*w)=run h (2^i*(3^j*d))) ∧
    0<b ∧ run (6*H+3) (3^(2*H)*w)=b ∧ b<w := by
  have positive : 0<b := by
    by_contra no
    have zero : b=0 := by omega
    rw [zero,Nat.mul_zero,Nat.zero_add,show 3^(H+1)*a=3*(3^H*a) by ring] at exitRow
    omega
  refine ⟨all_odd_no_short_smooth hw (by omega) c2 c3 start,positive,?_⟩
  have cap : 2*3^((H+1)+2*H) ≤ 2^((H+1)+(5*H+2)) := by
    have p : 27^H≤64^H := Nat.pow_le_pow_left (by decide) _
    rw [show H+1+2*H=3*H+1 by omega,show H+1+(5*H+2)=6*H+3 by omega,
      pow_succ,pow_add,pow_mul,pow_mul]
    change 2*(27^H*3)≤64^H*8
    omega
  simpa only [show H+1+(5*H+2)=6*H+3 by omega] using two_run_drop hw start exitRow cap

#print axioms word_iff
#print axioms carry_bound
#print axioms lower_power_meeting
#print axioms short_meeting_rigid
#print axioms short_cone_iff
#print axioms all_odd_weight
#print axioms all_odd_no_short_cone
#print axioms all_odd_no_short_smooth
#print axioms fifteen_no_affine_return
#print axioms two_run_drop
#print axioms delayed_linear_return

end Collatz.TowerClock

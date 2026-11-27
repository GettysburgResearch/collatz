module

public import ReturnDescentFixed
import all ReturnDescent
import all ReturnDescentRows
import all TowerFrontierAffine
import all TernaryItinerary

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier ReturnDescent
set_option autoImplicit false
set_option maxRecDepth 20000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 1000000

private theorem keep_factor {u A w : Nat} (base : u=1+A*w) (k : Nat) :
    ∃ v, u^k=1+A*v := by
  induction k with
  | zero => exact ⟨0,by simp⟩
  | succ k ih =>
    obtain ⟨v,hv⟩ := ih
    exact ⟨v+w+A*v*w,by rw [Nat.pow_succ,hv,base]; grind⟩

private theorem square_factor {u c w : Nat} (base : u=1+2*c*w) (k : Nat) :
    ∃ v, u^(2^k)=1+2^(k+1)*c*v := by
  induction k with
  | zero => exact ⟨w,by simpa using base⟩
  | succ k ih =>
    obtain ⟨v,hv⟩ := ih
    refine ⟨v+2^k*c*v*v,?_⟩
    rw [Nat.pow_succ 2 k, Nat.pow_mul, hv, Nat.pow_succ 2 k, Nat.pow_succ 2 (k+1),
      Nat.pow_succ 2 k]
    grind

private theorem odd_power {b : Nat} (odd : b%2=1) (k : Nat) :
    ∃ s, b^(2^(k+1))=1+2^(k+3)*s := by
  have hs : ∃ t, b^2=1+2*4*t := by
    let q := b/4
    have cases : b=4*q+1 ∨ b=4*q+3 := by dsimp [q]; omega
    rcases cases with h|h
    · exact ⟨2*q*q+q,by rw [h]; grind⟩
    · exact ⟨2*q*q+3*q+1,by rw [h]; grind⟩
  obtain ⟨w,hw⟩ := hs
  obtain ⟨a,ha⟩ := square_factor hw k
  have e : 2*2^k=2^(k+1) := by rw [Nat.pow_succ,Nat.mul_comm]
  rw [←Nat.pow_mul b 2 (2^k),e] at ha
  have coeff : 2^(k+1)*4=2^(k+3) := by rw [show (4:Nat)=2^2 by decide,←Nat.pow_add]
  rw [coeff] at ha
  exact ⟨a,ha⟩

private theorem power_multiple {b n k : Nat} (odd : b%2=1) (degree : 2^(k+1) ∣ n) :
    ∃ s, b^n=1+2^(k+3)*s := by
  obtain ⟨v,hv⟩ := degree
  obtain ⟨a,ha⟩ := odd_power odd k
  rw [hv,Nat.pow_mul]
  exact keep_factor ha v

/-- The binary input class of the 499-clock chart holds for all odd bases
    whenever the specified degree is divisible by 2^494. -/
theorem power_parameter {b n : Nat} (odd : b%2=1) (degree : 2^494 ∣ n) :
    ∃ s, b^n=1+2^496*s := power_multiple (k:=493) odd degree

private theorem grade_shift (h n a b : Nat) :
    track h n (a+b)=((track h n a).1,(track h n a).2+b) := by
  induction h generalizing n a with
  | zero => rfl
  | succ h ih =>
    simp only [track]
    split
    · exact ih _ _
    · rw [show a+b+1=(a+1)+b by omega]
      exact ih _ _

private theorem graded_lift (h n e t : Nat) :
    track h (n+2^h*3^e*t) e =
      ((track h n e).1+3^(track h n e).2*t,(track h n e).2) := by
  have shift (x : Nat) : track h x e=((track h x 0).1,(track h x 0).2+e) := by
    simpa only [Nat.zero_add] using grade_shift h x 0 e
  rw [shift,shift,Nat.mul_assoc,track_lift]
  simp only [Nat.pow_add,Nat.mul_assoc]

/-- A concrete compensated chart is valid at each ordinary exponent in
    its full binary progression. -/
private theorem peakChart {s h g : Nat} (hg : g≤173) (hh : 3≤h)
    (check : track h (3^173-1) g=track h (3^(173-g)-1) 0) :
    let m := 11+162*(1+2^(h-3)*s)
    track h (3^m-1) g=track h (3^(m-g)-1) 0 := by
  intro m
  obtain ⟨w,hw⟩ := square_factor
    (show 3^162=1+2*4*((3^162-1)/8) by decide +kernel) (h-3)
  have coeff : 2^(h-3+1)*4=2^h := by
    rw [show (4:Nat)=2^2 by decide,←Nat.pow_add]
    congr 1
    omega
  rw [coeff] at hw
  obtain ⟨v,hv⟩ := keep_factor hw s
  rw [←Nat.pow_mul,←Nat.pow_mul] at hv
  have e : m=173+162*(2^(h-3)*s) := by dsimp only [m]; omega
  have f : m-g=(173-g)+162*(2^(h-3)*s) := by omega
  let t := 3^(173-g)*v
  have up : 3^m-1=(3^173-1)+2^h*3^g*t := by
    have eq : 3^g*3^(173-g)=3^173 := by rw [←Nat.pow_add]; congr 1; omega
    have pos : 0<3^173 := Nat.pow_pos (by decide)
    rw [e,Nat.pow_add,hv,Nat.mul_add,Nat.mul_one]
    have mul : 2^h*3^g*t=3^173*(2^h*v) := by
      dsimp only [t]
      rw [←eq]
      ac_rfl
    omega
  have dn : 3^(m-g)-1=(3^(173-g)-1)+2^h*3^0*t := by
    have pos : 0<3^(173-g) := Nat.pow_pos (by decide)
    rw [f,Nat.pow_add,hv,Nat.mul_add,Nat.mul_one,Nat.pow_zero,Nat.mul_one]
    have mul : 2^h*t=3^(173-g)*(2^h*v) := by dsimp only [t]; ac_rfl
    omega
  rw [up,dn]
  rw [graded_lift,graded_lift,check]

/-- These offsets all give equality at clock 499 after the two complete
    Mersenne ascents, with the exact augmentation of the two odd counts. -/
theorem anchor_499 {j g : Nat} (binary : ∃ s, j=1+2^496*s)
    (gap : g=9 ∨ g=10 ∨ g=17 ∨ g=18 ∨ g=19 ∨ g=20) :
    let m := 11+162*j
    track 499 (3^m-1) g=track 499 (3^(m-g)-1) 0 := by
  obtain ⟨s,rfl⟩ := binary
  rcases gap with h|h|h|h|h|h <;> subst g <;>
    apply peakChart (s:=s) (by decide) (by decide) <;> decide +kernel

theorem anchor_763 {j : Nat} (binary : ∃ s, j=1+2^760*s) :
    let m := 11+162*j
    track 763 (3^m-1) 27=track 763 (3^(m-27)-1) 0 := by
  obtain ⟨s,rfl⟩ := binary
  apply peakChart (s:=s) (by decide) (by decide)
  decide +kernel

theorem meeting_of_chart {h m g : Nat}
    (chart : track h (3^m-1) g=track h (3^(m-g)-1) 0) :
    Meets (M m) (M (m-g)) := by
  refine ⟨m+h,m-g+h,?_⟩
  rw [run_add,peak,run_add,peak,←track_run h _ g,chart,track_run]

/-- The stronger binary precision pays the earlier three-odd row directly. -/
theorem three_odd_return {j : Nat} (binary : ∃ s, j=1+2^760*s) :
    CanonicalReturn (11+162*j) := by
  let m := 11+162*j
  obtain ⟨s,hj⟩ := binary
  have jpos : 0<j := by omega
  have low : 173≤m := by dsimp only [m]; omega
  have idx : ((m-27-1)/2)%81=72 := by dsimp only [m]; omega
  have price : clockCharge (m-27)=12 := by
    unfold clockCharge
    rw [idx]
    decide +kernel
  apply return_of_earlier (t:=m-27) rfl (by omega) (by rw [price]; omega)
  exact meeting_of_chart (anchor_763 ⟨s,hj⟩)

end Collatz.Itinerary.PassageDescent

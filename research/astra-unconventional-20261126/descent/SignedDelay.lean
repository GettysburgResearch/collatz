import Portal
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace Collatz.SignedPeakDelay

/-- Numerator dynamics at the fixed odd denominator d. -/
def step (d a : Int) : Int := if a%2=0 then a/2 else (3*a+d)/2

def run (d : Int) : Nat → Int → Int
  | 0, a => a
  | h+1, a => step d (run d h a)

private def Safe (d a : Int) : Prop :=
  0<a ∨ (a<0 ∧ -d<4*a) ∨ (a<0 ∧ -d<2*a ∧ a%3≠0)

private theorem safe_step {d a : Int} (pos : 0<d) (nine : d%9=0) (odd : d%2=1)
    (good : Safe d a) : Safe d (step d a) := by
  unfold Safe at good ⊢
  unfold step
  split <;> omega

private theorem first_safe {d : Int} (_large : 9≤d) (nine : d%9=0) (odd : d%2=1) :
    Safe d (step d (1-d)) := by
  unfold Safe step
  split <;> omega

/-- Every earlier signed peak 1/d−1, for d an odd multiple of nine,
avoids all three states of the signed reference orbit −2/3, −1/3, 0.
The statement includes clock zero. -/
theorem signed_peaks_apart {d : Int} (large : 9≤d) (nine : d%9=0) (odd : d%2=1)
    (h : Nat) : 3*run d h (1-d)≠-2*d ∧ 3*run d h (1-d)≠-d ∧ run d h (1-d)≠0 := by
  cases h with
  | zero => simp only [run]; omega
  | succ h =>
    have g : Safe d (run d (h+1) (1-d)) := by
      induction h with
      | zero => exact first_safe large nine odd
      | succ h ih => exact safe_step (by omega) nine odd ih
    unfold Safe at g
    omega

private theorem fixed_states {d : Int} (nine : d%9=0) (odd : d%2=1) (h : Nat) :
    3*run d h (-(2*(d/3))) = -2*d ∨ 3*run d h (-(2*(d/3))) = -d ∨
    run d h (-(2*(d/3)))=0 := by
  induction h with
  | zero => simp only [run]; omega
  | succ h ih =>
    simp only [run,step]
    split <;> omega

private theorem one_lift (d a z : Int) :
    ∃ e : Int, step d (a+2*z)=step d a+z*e := by
  unfold step
  rw [show (a+2*z)%2=a%2 by omega]
  split
  · exact ⟨1,by omega⟩
  · exact ⟨3,by omega⟩

private theorem prefix_lift (d a : Int) (h : Nat) (M z : Int) :
    ∃ t : Int, run d h (a+2^h*M*z)=run d h a+M*t := by
  induction h generalizing M z with
  | zero => exact ⟨z,by simp [run]⟩
  | succ h ih =>
    have e : a+2^(h+1)*M*z=a+2^h*(2*M)*z := by rw [pow_succ]; ring
    obtain ⟨t,ht⟩ := ih (2*M) z
    rw [e,run,run,ht,show (2*M)*t=2*(M*t) by ring]
    obtain ⟨c,hc⟩ := one_lift d (run d h a) (M*t)
    exact ⟨t*c,by rw [hc]; ring⟩

private theorem clock_lift (d a M z : Int) (h H : Nat) (bound : h≤H) :
    ∃ t : Int, run d h (a+2^H*M*z)=run d h a+M*t := by
  obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le bound
  rw [pow_add,show a+(2:Int)^h*2^j*M*z=a+2^h*M*(2^j*z) by ring]
  exact prefix_lift d a h M _

private theorem bounded (d a : Int) (pos : 0≤d) (init : -d≤a ∧ a≤d) (h : Nat) :
    -(2^h*d) ≤ run d h a ∧ run d h a ≤ 2^h*d := by
  induction h with
  | zero => simpa [run] using init
  | succ h ih =>
    have dc : d≤(2:Int)^h*d := (le_mul_of_one_le_left pos (one_le_pow₀ (by decide : (1:Int)≤2)))
    simp only [run,step,pow_succ]
    rw [show (2:Int)^h*2*d=2*(2^h*d) by ring]
    split <;> omega

/-- If two actual numerators lift the disjoint signed reference states
at modulus 2^H M and both signed runs fit inside a half interval modulo M,
no choice of independent clocks through H gives an ordinary equality. -/
theorem delayed_lifts {d M : Int} (large : 9≤d) (nine : d%9=0) (odd : d%2=1)
    (H i l : Nat) (hi : i≤H) (hl : l≤H) (wide : 2*(2^H*d)<M) (u v : Int) :
    run d i (-(2*(d/3))+2^H*M*u) ≠ run d l (1-d+2^H*M*v) := by
  obtain ⟨uu,hu⟩ := clock_lift d (-(2*(d/3))) M u i H hi
  obtain ⟨vv,hv⟩ := clock_lift d (1-d) M v l H hl
  have b1 := bounded d (-(2*(d/3))) (by omega) (by omega) i
  have b2 := bounded d (1-d) (by omega) (by omega) l
  have bi := mul_le_mul_of_nonneg_right (pow_le_pow_right₀ (by decide : (1:Int)≤2) hi) (by omega : (0:Int)≤d)
  have bl := mul_le_mul_of_nonneg_right (pow_le_pow_right₀ (by decide : (1:Int)≤2) hl) (by omega : (0:Int)≤d)
  intro same
  rw [hu,hv] at same
  have mp : 0<M := by omega
  have eq : uu=vv := by
    by_contra ne
    rcases lt_or_gt_of_ne ne with small|big
    · have gap := mul_le_mul_of_nonneg_left (show uu+1≤vv by omega) (le_of_lt mp)
      rw [mul_add,mul_one] at gap
      omega
    · have gap := mul_le_mul_of_nonneg_left (show vv+1≤uu by omega) (le_of_lt mp)
      rw [mul_add,mul_one] at gap
      omega
  rw [eq] at same
  have := fixed_states nine odd i
  have := signed_peaks_apart large nine odd l
  omega

private theorem scale_step (d : Int) (odd : d%2=1) (x : Nat) :
    step d (d*(x:Int))=d*(TernaryPortal.step x : Int) := by
  have par : (d*(x:Int))%2=(x:Int)%2 := by rw [Int.mul_emod,odd]; simp
  unfold step TernaryPortal.step
  rw [par]
  by_cases even : x%2=0
  · rw [ite_eq_left even,ite_eq_left (show (x:Int)%2=0 by omega)]
    have eq : (x:Int)=2*((x/2:Nat):Int) := by omega
    have d2 : d*(x:Int)=2*(d*((x/2:Nat):Int)) := by linear_combination d*eq
    rw [d2]
    omega
  · rw [ite_eq_right even,ite_eq_right (show (x:Int)%2≠0 by omega)]
    have eq : 3*(x:Int)+1=2*(((3*x+1)/2:Nat):Int) := by omega
    have d2 : 3*(d*(x:Int))+d=2*(d*(((3*x+1)/2:Nat):Int)) := by linear_combination d*eq
    rw [d2]
    omega

private theorem scale_run (d : Int) (odd : d%2=1) (h x : Nat) :
    run d h (d*(x:Int))=d*(TernaryPortal.run h x : Int) := by
  induction h with
  | zero => rfl
  | succ h ih =>
    rw [run,ih,scale_step d odd]
    rw [TernaryPortal.run_add]
    rfl

/-- The congruence and width conditions directly exclude an equality of
the two ordinary positive-input shortcut trajectories. -/
theorem ordinary_delayed_lifts {d M : Int} (large : 9≤d) (nine : d%9=0) (odd : d%2=1)
    (H i l x y : Nat) (hi : i≤H) (hl : l≤H) (wide : 2*(2^H*d)<M) (u v : Int)
    (linkx : d*(x:Int)= -(2*(d/3))+2^H*M*u)
    (linky : d*(y:Int)= 1-d+2^H*M*v) : TernaryPortal.run i x ≠ TernaryPortal.run l y := by
  have no := delayed_lifts large nine odd H i l hi hl wide u v
  rw [←linkx,←linky,scale_run d odd,scale_run d odd] at no
  intro equal
  exact no (by rw [equal])

private theorem lower_word (h x : Nat) : x ≤ 2^h*TernaryPortal.run h x := by
  induction h generalizing x with
  | zero => simp [TernaryPortal.run]
  | succ h ih =>
    have first : x≤2*TernaryPortal.step x := by unfold TernaryPortal.step; split <;> omega
    have next := Nat.mul_le_mul_left 2 (ih (TernaryPortal.step x))
    calc
      x ≤ 2*TernaryPortal.step x := first
      _ ≤ 2*(2^h*TernaryPortal.run h (TernaryPortal.step x)) := next
      _ = _ := by rw [TernaryPortal.run,pow_succ]; ring

private theorem upper_word (h x : Nat) : 2^h*(TernaryPortal.run h x+1)≤3^h*(x+1) := by
  induction h generalizing x with
  | zero => simp [TernaryPortal.run]
  | succ h ih =>
    have first : 2*(TernaryPortal.step x+1)≤3*(x+1) := by unfold TernaryPortal.step; split <;> omega
    calc
      _ = 2*(2^h*(TernaryPortal.run h (TernaryPortal.step x)+1)) := by rw [TernaryPortal.run,pow_succ]; ring
      _ ≤ 2*(3^h*(TernaryPortal.step x+1)) := Nat.mul_le_mul_left 2 (ih _)
      _ = 3^h*(2*(TernaryPortal.step x+1)) := by ring
      _ ≤ 3^h*(3*(x+1)) := Nat.mul_le_mul_left _ first
      _ = _ := by rw [pow_succ]; ring

private theorem upper_envelope {H l : Nat} (hl : l≤H) (x : Nat) :
    2^H*(TernaryPortal.run l x+1)≤3^H*(x+1) := by
  obtain ⟨z,rfl⟩ := Nat.exists_eq_add_of_le hl
  have b := Nat.mul_le_mul (upper_word l x) (Nat.pow_le_pow_left (by decide : 2≤3) z)
  rw [pow_add,pow_add]
  convert b using 1 <;> ring

/-- Any independently timed meeting of two ordinary peaks requires
strictly more clocks than their exponent gap. -/
theorem peak_gap {H i l t s : Nat} (pos : 0<H) (hi : i≤H) (hl : l≤H)
    (meet : TernaryPortal.run i (3^(t+s)-1)=TernaryPortal.run l (3^t-1)) : s<H := by
  have b1 := lower_word i (3^(t+s)-1)
  rw [meet] at b1
  have b2 := upper_envelope hl (3^t-1)
  have ip := Nat.mul_le_mul_right (TernaryPortal.run l (3^t-1)) (Nat.pow_le_pow_right (by decide : 0<2) hi)
  have h1 := b1.trans ip
  rw [Nat.sub_add_cancel (Nat.pow_pos (by decide : 0<3) (n:=t))] at b2
  rw [Nat.mul_add,Nat.mul_one] at b2
  have two : (2:Nat)≤2^H := Nat.pow_le_pow_right (by decide : 0<2) (show 1≤H by omega)
  have positive := Nat.pow_pos (by decide : 0<3) (n:=t+s)
  by_contra nh
  have p := Nat.mul_le_mul_right (3^t) (Nat.pow_le_pow_right (by decide : 0<3) (show H≤s by omega))
  have pp : (3:Nat)^H*3^t≤3^(t+s) := by
    calc
      _ ≤ 3^s*3^t := p
      _ = _ := by rw [pow_add]; ac_rfl
  omega

/-- The paired signed lifts specialize to the two actual peaks, for every
choice of the earlier exponent and both physical clocks in range. -/
theorem postpeak_no_meeting {H i l t s : Nat} {M : Int} (hs : 0<s)
    (hi : i≤H) (hl : l≤H) (link : (3:Int)^(t+s+1)=1+2^H*M)
    (wide : 2*((2:Int)^H*3^(s+1))<M) :
    TernaryPortal.run i (3^(t+s)-1) ≠ TernaryPortal.run l (3^t-1) := by
  let u := (3:Int)^s
  let d := (3:Int)^(s+1)
  have du : d=3*u := by dsimp [d,u]; rw [pow_succ,mul_comm]
  have bigu : 3≤u := pow_le_pow_right₀ (by decide : (1:Int)≤3) (show 1≤s by omega)
  have du3 : u%3=0 := by
    obtain ⟨z,hz⟩ := Nat.exists_eq_add_of_le (show 1≤s by omega)
    dsimp [u]
    rw [hz,pow_add,pow_one]
    omega
  have odd : d%2=1 := by
    have hh := (show (3:Int) ≡ 1 [ZMOD 2] by decide).pow (s+1)
    change (3:Int)^(s+1)%2=(1:Int)%2
    exact (show (3:Int)^(s+1) ≡ 1 [ZMOD 2] by simpa using hh)
  have dv : d/3=u := by omega
  have dp : d*(3:Int)^t=(3:Int)^(t+s+1) := by
    dsimp [d]
    rw [←pow_add]
    congr 1
    omega
  apply ordinary_delayed_lifts (d:=d) (M:=M) (by omega) (by omega) odd H i l _ _ hi hl wide u 1
  · rw [Nat.cast_sub (Nat.pow_pos (by decide : 0<3) (n:=t+s))]
    push_cast
    rw [dv,du]
    rw [pow_succ] at link
    linear_combination u*link
  · rw [Nat.cast_sub (Nat.pow_pos (by decide : 0<3) (n:=t))]
    push_cast
    rw [←dp] at link
    linear_combination link

/-- The earlier exponent and both clocks may be selected after the original
positive peak. A binary lift and one width inequality exclude them all. -/
theorem all_earlier {H m : Nat} {M : Int} (hp : 0<H)
    (link : (3:Int)^(m+1)=1+2^H*M) (wide : 2*((2:Int)^H*3^H)<M)
    (t i l : Nat) (ht : t<m) (hi : i≤H) (hl : l≤H) :
    TernaryPortal.run i (3^m-1) ≠ TernaryPortal.run l (3^t-1) := by
  let s := m-t
  have pos : 0<s := by dsimp [s]; omega
  have split : m=t+s := by dsimp [s]; omega
  intro same
  rw [split] at same link
  have gap := peak_gap hp hi hl same
  have pw := pow_le_pow_right₀ (by decide : (1:Int)≤3) (show s+1≤H by omega)
  have non := mul_le_mul_of_nonneg_left pw (by positivity : (0:Int)≤2^H)
  exact postpeak_no_meeting pos hi hl link (by omega) same

private theorem special_width (b : Nat) :
    ∃ M : Int, (3:Int)^(12*2^b)=1+2^(b+4)*M ∧ 2*((2:Int)^(b+4)*3^(b+4))<M := by
  induction b with
  | zero => exact ⟨33215,by decide,by decide⟩
  | succ b ih =>
    obtain ⟨M,link,wide⟩ := ih
    let A : Int := 2^(b+3)
    have Apos : 1≤A := one_le_pow₀ (by decide : (1:Int)≤2)
    have P : (2:Int)^(b+4)=2*A := by dsimp [A]; rw [pow_succ]; ring
    have q : 2≤(2:Int)^(b+4) := pow_le_pow_right₀ (by decide : (1:Int)≤2) (show 1≤b+4 by omega)
    have r : 3≤(3:Int)^(b+4) := pow_le_pow_right₀ (by decide : (1:Int)≤3) (show 1≤b+4 by omega)
    have Mpos : 6≤M := by nlinarith [mul_nonneg (show 0≤(2:Int)^(b+4)-2 by omega) (show 0≤(3:Int)^(b+4)-3 by omega)]
    have sq : 6*M≤M+A*M*M := by
      nlinarith [mul_nonneg (show 0≤M-6 by omega) (show 0≤M by omega),
        mul_nonneg (show 0≤A-1 by omega) (sq_nonneg M)]
    refine ⟨M+A*M*M,?_,?_⟩
    · rw [show 12*2^(b+1)=(12*2^b)*2 by rw [pow_succ]; ring,pow_mul,link]
      rw [show (2:Int)^(b+1+4)=2^(b+4)*2 from pow_succ _ _,P]
      ring
    · rw [show (2:Int)^(b+1+4)=2^(b+4)*2 from pow_succ _ _,
          show (3:Int)^(b+1+4)=3^(b+4)*3 from pow_succ _ _]
      linarith

/-- Every earlier peak is simultaneously absent through the explicit
logarithmic clock at every ordinary exponent 12*2^b−1. -/
theorem explicit_delayed (b t i l : Nat) (ht : t<12*2^b-1) (hi : i≤b+4) (hl : l≤b+4) :
    TernaryPortal.run i (3^(12*2^b-1)-1) ≠ TernaryPortal.run l (3^t-1) := by
  obtain ⟨M,link,wide⟩ := special_width b
  have pos := Nat.two_pow_pos b
  rw [show 12*2^b=(12*2^b-1)+1 by omega] at link
  exact all_earlier (by omega) link wide t i l ht hi hl

#print axioms signed_peaks_apart
#print axioms delayed_lifts
#print axioms ordinary_delayed_lifts
#print axioms peak_gap
#print axioms postpeak_no_meeting
#print axioms all_earlier
#print axioms explicit_delayed
end Collatz.SignedPeakDelay

import ValuationReturns
import SignedDelay

/-! Exact first possible independent-clock deadline for the two whole
canonical classes. The prior signed-peak width lemma handles the lower
bound. Its original pointwise exponent family is extended to all positive
cofactors by the ordinary binomial power identity. -/
namespace Collatz.ValuationSharp
open Itinerary Itinerary.ReturnDescent.ValuationReturns

set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 60000
set_option exponentiation.threshold 60000

-- The width induction is reproduced from the pinned private PR192 lemma.
private theorem base_width (b : Nat) :
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

private theorem matching_run (h x : ℕ) : TernaryPortal.run h x=Itinerary.run h x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact ih (TernaryPortal.step x)

/-- All positive cofactors keep the original initial signed-center obstruction. -/
theorem initial_delay (q r : ℕ) (rp : 0<r) :
    let m:=12*2^q*r-1
    ∀t i l : ℕ, t<m → i≤q+4 → l≤q+4 →
      run i (3^m-1)≠run l (3^t-1) := by
  obtain ⟨M,start,wide⟩:=base_width q
  let B:=12*2^q
  let D:ℤ:=2^(q+4)
  have Dp : 0<D := by positivity
  have Mp : 0<M := (show 0<2*((2:ℤ)^(q+4)*3^(q+4)) by positivity).trans wide
  have powers (n : ℕ) : ∃z : ℤ, (3:ℤ)^(B*(n+1))=1+D*z ∧ M≤z := by
    induction n with
    | zero => exact ⟨M,by simpa only [Nat.zero_add,Nat.mul_one] using start,le_rfl⟩
    | succ n ih =>
      obtain ⟨z,old,le⟩:=ih
      have positive : 0≤D*z*M := mul_nonneg (mul_nonneg Dp.le (Mp.le.trans le)) Mp.le
      refine ⟨z+M+D*z*M,?_,by linarith⟩
      rw [Nat.mul_succ B (n+1),pow_add,old,show (3:ℤ)^B=1+D*M from start]; ring
  obtain ⟨v,rv⟩:=Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt rp)
  obtain ⟨z,eq,le⟩:=powers v
  have positive : 0<B*r := Nat.mul_pos (by dsimp [B]; positivity) rp
  have link : (3:ℤ)^(B*r-1+1)=1+(2:ℤ)^(q+4)*z := by
    rw [Nat.sub_add_cancel positive,rv]; exact eq
  intro m t i l tm hi hl
  have no:=SignedPeakDelay.all_earlier (by omega : 0<q+4) link (wide.trans_le le) t i l tm hi hl
  simpa only [matching_run] using no

/-- Physical endpoint upper bound, price gain and exclusion of every
independent pair of clocks through the preceding deadline. -/
def SharpPaidPeak (m d J savings : ℕ) : Prop := PaidPeak m d (J+1) savings ∧
  ∀t i l : ℕ, t<m → i≤J → l≤J → run i (3^m-1)≠run l (3^t-1)

theorem first_857 (n : ℕ) : SharpPaidPeak (12*2^852*(19+54*n)-1) 420 856 401 :=
  ⟨valuation_856 n,initial_delay 852 _ (by omega)⟩

theorem first_1737 (n : ℕ) : SharpPaidPeak (12*2^1732*(49+54*n)-1) 886 1736 876 :=
  ⟨valuation_1736 n,initial_delay 1732 _ (by omega)⟩

#print axioms initial_delay
#print axioms first_857
#print axioms first_1737
end Collatz.ValuationSharp

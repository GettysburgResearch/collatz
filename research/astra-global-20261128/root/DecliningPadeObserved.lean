import PadeWindow
import DecliningPadeHeight

/-! Actual ordinary finite tails for declining even-clock spacings. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.DecliningPadeObserved
open CoreBranching PinClock PinCriterion
open Collatz.PadeArithmetic Collatz.PadeIntegral Collatz.FinitePade
open Collatz.PadeNative Collatz.PadeObserved Collatz.PadeWindow
open Collatz.PadeValuations Collatz.DecliningPadeIntegral
open Collatz.DecliningPadeValuations Collatz.DecliningPadeHeight
open scoped BigOperators

def downSchedule (b h j : ℕ) : ℕ := j*(b+1)-h*tri j

theorem curvature_le (b h j : ℕ) (hb : h*j≤b) : h*tri j≤b*j := by
  have ht := tri_le_mul j j (by omega)
  have h0 := Nat.mul_le_mul_left h ht
  have h1 := Nat.mul_le_mul_right j hb
  nlinarith

theorem down_schedule_sub (b h j : ℕ) :
    downSchedule b h j-j=b*j-h*tri j := by
  unfold downSchedule
  have he : j*(b+1)=b*j+j := by ring
  rw [he]
  omega

theorem down_schedule_cast (b h j : ℕ) (hb : h*j≤b) :
    (downSchedule b h j:ℤ)=downClock h b j := by
  have hc := curvature_le b h j hb
  have hle : h*tri j≤j*(b+1) := by nlinarith
  simp only [downSchedule,Nat.cast_sub hle,Nat.cast_mul,Nat.cast_add,Nat.cast_one,
    downClock]

theorem amplitude_of_down_schedule (b h j n : ℕ) (hb : h*j≤b)
    (hc : clock j n=downSchedule b h j) :
    amplitude j n=term (qDown h) (zBase b) j := by
  have hle := curvature_le b h j hb
  have hle' : h*tri j≤j*(b+1) := by nlinarith
  unfold amplitude
  rw [hc,down_schedule_sub,downSchedule,pow_sub₀ (2:ℚ) (by decide) hle',
    pow_sub₀ (3:ℚ) (by decide) hle]
  simp only [term,qDown,zBase,div_pow,←pow_mul]
  rw [Nat.mul_comm j (b+1)]
  field_simp

theorem down_nativeSum (b h e n : ℕ) (hb : h*e≤b)
    (hc : ∀ j<e,clock j n=downSchedule b h j) :
    nativeSum e n=partialSum (qDown h) (zBase b) e := by
  unfold nativeSum partialSum
  apply Finset.sum_congr rfl
  intro j hj
  have hj' : j<e := Finset.mem_range.mp hj
  exact amplitude_of_down_schedule b h j n
    ((Nat.mul_le_mul_left h (by omega)).trans hb) (hc j hj')

/-- The lower valuation required by the finite declining kernel comes from the run itself. -/
theorem down_native_tail (b h e n : ℕ) (hb : h*e≤b)
    (hc : ∀ j≤e,clock j n=downSchedule b h j) :
    AtLeast (downClock h b e)
      (-((n:ℚ)+1)-partialSum (qDown h) (zBase b) e) := by
  have hcal := native_calibration e n
  rw [down_nativeSum b h e n hb (fun j hj => hc j (by omega))] at hcal
  have he : -((n:ℚ)+1)-partialSum (qDown h) (zBase b) e =
      -amplitude e n*((run (clock e n) n:ℚ)+1) := by nlinarith
  rw [he]
  have ha := amplitude_exact e n
  have hv : 0≤padicValRat 2 ((run (clock e n) n:ℚ)+1) := by
    simpa only [Nat.cast_add,Nat.cast_one] using
      (zero_le_padicValRat_of_nat (p:=2) (run (clock e n) n+1))
  right
  rw [padicValRat.mul (neg_ne_zero.mpr ha.1) (by positivity),padicValRat.neg,
    ha.2,hc e le_rfl,down_schedule_cast b h e hb]
  rw [hc e le_rfl] at hv
  omega

/-- The declining interpolation estimate, with all physical tails discharged. -/
theorem actual_declining_height (b h s n : ℕ) (hh : 0<h) (hs : 0<s)
    (hb : 200*h*s≤b)
    (hc : ∀ j≤5*s+2,clock j n=downSchedule b h j) :
    (2:ℤ)^(b*s)≤((n:ℤ)+2)^8 := by
  have hlast : h*(5*s+2)≤b := by nlinarith
  have ht : ∀ k≤2*s,AtLeast (downClock h b (2*s+s+k+2))
      (((-((n:ℤ)+1):ℤ):ℚ)-partialSum (qDown h) (zBase b) (2*s+s+k+2)) := by
    intro k hk
    have he := down_native_tail b h (2*s+s+k+2) n
      ((Nat.mul_le_mul_left h (by omega)).trans hlast)
      (fun j hj => hc j (by omega))
    simpa only [Int.cast_neg,Int.cast_add,Int.cast_natCast,Int.cast_one] using he
  have he := down_finite_height h b s hh hs hb (-((n:ℤ)+1)) ht
  simpa only [abs_neg,abs_of_nonneg (by positivity : 0≤(n:ℤ)+1),add_assoc,
    show (1:ℤ)+1=2 by rfl] using he

theorem actual_declining_exponent (b h s n B : ℕ) (hh : 0<h) (hs : 0<s)
    (hb : 200*h*s≤b)
    (hc : ∀ j≤5*s+2,clock j n=downSchedule b h j)
    (hB : (n:ℤ)+2≤(2:ℤ)^B) : b*s≤8*B := by
  have hp := actual_declining_height b h s n hh hs hb hc
  have hpow := pow_le_pow_left₀ (by positivity : 0≤(n:ℤ)+2) hB 8
  have hi := hp.trans hpow
  rw [←pow_mul] at hi
  have he := (pow_le_pow_iff_right₀ (by decide : (1:ℤ)<2)).mp hi
  omega

end Collatz.DecliningPadeObserved

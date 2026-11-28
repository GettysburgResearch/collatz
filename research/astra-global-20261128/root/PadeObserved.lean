import PadeNative
import PadeHeight

/-! The finite Padé barrier with every tail premise discharged on actual Collatz runs. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeObserved
open CoreBranching PinClock PinCriterion
open Collatz.PadeArithmetic Collatz.PadeIntegral Collatz.FinitePade
open Collatz.PadeNative Collatz.PadeValuations Collatz.PadeHeight

private theorem odd_nat_val (a : ℕ) (ha : a%2=1) :
    padicValRat 2 (a:ℚ)=0 := by
  have hd : ¬2∣a := by
    intro h
    have hm := Nat.mod_eq_zero_of_dvd h
    omega
  rw [padicValRat.of_nat,padicValNat.eq_zero_of_not_dvd hd]
  rfl

theorem amplitude_exact (e n : ℕ) : Exact (clock e n) (amplitude e n) := by
  have h2 : padicValRat 2 (2:ℚ)=1 := padicValRat.self (by decide)
  have h3 : padicValRat 2 (3:ℚ)=0 := odd_nat_val 3 (by decide)
  unfold amplitude
  refine ⟨by positivity,?_⟩
  rw [padicValRat.div (by positivity) (by positivity),padicValRat.pow,
    padicValRat.pow,h2,h3]
  ring

/-- The parity at the actual terminal clock makes the remaining factor a dyadic unit. -/
theorem native_remainder_exact (b h e n : ℕ)
    (hc : ∀ j≤e,clock j n=schedule b h j) :
    Exact (clockExponent h b e)
      (-((n:ℚ)+1)-partialSum (qBase h) (zBase b) e) := by
  rw [native_remainder b h e n (fun j hj => hc j (by omega))]
  have he := even_at_clock e n
  have ho : (run (clock e n) n+1)%2=1 := by omega
  have hv : padicValRat 2 ((run (clock e n) n:ℚ)+1)=0 := by
    simpa only [Nat.cast_add,Nat.cast_one] using odd_nat_val _ ho
  have ha := amplitude_exact e n
  refine ⟨mul_ne_zero (neg_ne_zero.mpr ha.1) (by positivity),?_⟩
  rw [padicValRat.mul (neg_ne_zero.mpr ha.1) (by positivity),padicValRat.neg,ha.2,hv,add_zero,
    hc e le_rfl]
  rfl

/-- An actual positive-curvature clock cannot persist past this starting-height barrier.
No approximation, analytic limit, or assumed tail premise remains in this theorem. -/
theorem actual_clock_height_barrier (b h s n : ℕ) (hh : 0<h)
    (hc : ∀ j≤5*s+2,clock j n=schedule b h j) :
    (2:ℤ)^(3*h*s*s+4*b*s)≤((n:ℤ)+2)^17 := by
  have ht : ∀ k≤2*s,AtLeast (clockExponent h b (2*s+s+k+2))
      (((-((n:ℤ)+1):ℤ):ℚ)-partialSum (qBase h) (zBase b) (2*s+s+k+2)) := by
    intro k hk
    have he := native_remainder_exact b h (2*s+s+k+2) n
      (fun j hj => hc j (by omega))
    right
    simpa only [Int.cast_neg,Int.cast_add,Int.cast_natCast,Int.cast_one,he.2] using le_refl
      (clockExponent h b (2*s+s+k+2):ℤ)
  have hb := finite_height_barrier h b s hh (-((n:ℤ)+1)) ht
  simpa only [abs_neg,abs_of_nonneg (by positivity : 0≤(n:ℤ)+1),add_assoc,
    show (1:ℤ)+1=2 by rfl] using hb

/-- A convenient exact integer bit budget; the input bound uses no real logarithm. -/
theorem actual_clock_exponent_bound (b h s n B : ℕ) (hh : 0<h)
    (hc : ∀ j≤5*s+2,clock j n=schedule b h j)
    (hB : (n:ℤ)+2≤(2:ℤ)^B) :
    3*h*s*s+4*b*s≤17*B := by
  have hp := actual_clock_height_barrier b h s n hh hc
  have hpow := pow_le_pow_left₀ (by positivity : 0≤(n:ℤ)+2) hB 17
  have h := hp.trans hpow
  rw [←pow_mul] at h
  have he := (pow_le_pow_iff_right₀ (by decide : (1:ℤ)<2)).mp h
  omega

end Collatz.PadeObserved

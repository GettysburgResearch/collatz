import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
Integer algebra behind the Phi_12-degenerate twelve-block cycle family.
This proves an all-parameter divisibility exclusion for the displayed
factorization. The correspondence with the explicit parity words, and their
primitivity, is a separate written proof; no general cycle exclusion is assumed.
-/
namespace CollatzCyclotomicBlock

set_option maxHeartbeats 1500000

def residualD (s t : ℤ) : ℤ := (s^6-t^6)*(s^2+t^2)
def commonG (s t : ℤ) : ℤ := t^4-s^2*t^2+s^4
def residualB (s t : ℤ) : ℤ :=
  t^7+t^6*s+3*t^5*s^2+3*t^4*s^3+3*t^3*s^4+
    6*t^2*s^5+2*t*s^6+4*s^7
def bezoutU (s t : ℤ) : ℤ :=
  -392*t^6-600*t^5*s-971*t^4*s^2-1365*t^3*s^3-
    931*t^2*s^4-1926*t*s^5-1353*s^6
def bezoutV (s t : ℤ) : ℤ :=
  392*t^7+208*t^6*s-21*t^5*s^2+186*t^4*s^3-
    21*t^3*s^4-159*t^2*s^5-413*t*s^6-137*s^7

theorem complete_denominator_factorization (s t : ℤ) :
    s^12-t^12 = commonG s t * residualD s t := by
  unfold commonG residualD
  ring

theorem integer_bezout_805 (s t : ℤ) :
    -(bezoutU s t) * residualD s t + bezoutV s t * residualB s t =
      805*s^14 := by
  unfold bezoutU residualD bezoutV residualB
  ring

theorem residual_coprime (s t : ℤ) (h : IsCoprime s t) :
    IsCoprime (residualD s t) s := by
  have h6 : IsCoprime (s^6-t^6) s := by
    have hc : IsCoprime (s*s^5-t^6) s :=
      IsCoprime.mul_sub_left_left_iff.mpr (h.symm.pow_left : IsCoprime (t^6) s)
    convert hc using 1
    ring
  have h2 : IsCoprime (s^2+t^2) s := by
    have hc : IsCoprime (s*s+t^2) s :=
      IsCoprime.mul_add_left_left_iff.mpr (h.symm.pow_left : IsCoprime (t^2) s)
    simpa only [pow_two] using hc
  exact h6.mul_left h2

theorem reduced_divisibility (s t u : ℤ) (hst : IsCoprime s t)
    (h : residualD s t ∣ (t-u)*residualB s t) :
    residualD s t ∣ 805*(t-u) := by
  have hleft : residualD s t ∣ (t-u)*(-(bezoutU s t)*residualD s t) := by
    refine ⟨(t-u)*(-(bezoutU s t)), ?_⟩
    ring
  have hright : residualD s t ∣ (t-u)*(bezoutV s t*residualB s t) := by
    convert dvd_mul_of_dvd_right h (bezoutV s t) using 1
    ring
  have hb : residualD s t ∣ (805*(t-u))*s^14 := by
    have hsum := dvd_add hleft hright
    have heq : (t-u)*(-(bezoutU s t)*residualD s t) +
        (t-u)*(bezoutV s t*residualB s t) = (805*(t-u))*s^14 := by
      calc
        _ = (t-u)*(-(bezoutU s t)*residualD s t +
          bezoutV s t*residualB s t) := by ring
        _ = _ := by rw [integer_bezout_805]; ring
    rwa [heq] at hsum
  exact (residual_coprime s t hst).pow_right.dvd_of_dvd_mul_right hb

theorem residual_lower_bound (s t : ℤ) (ht : 0 ≤ t) (hst : t < s) :
    12*t^7 ≤ residualD s t := by
  have hstep : t+1 ≤ s := by omega
  have hpow : (t+1)^6 ≤ s^6 := pow_le_pow_left₀ (by omega) hstep 6
  have hrem : 0 ≤ 15*t^4+20*t^3+15*t^2+6*t+1 := by positivity
  have hd : 6*t^5 ≤ s^6-t^6 := by nlinarith
  have hs2 : t^2 ≤ s^2 := pow_le_pow_left₀ ht (le_of_lt hst) 2
  have hm := mul_le_mul hd (show 2*t^2 ≤ s^2+t^2 by linarith)
    (by positivity : 0 ≤ 2*t^2) (le_trans (by positivity : 0 ≤ 6*t^5) hd)
  unfold residualD
  nlinarith [hm]

theorem residual_exceeds_805 (s t : ℤ) (ht : 3 ≤ t) (hst : t < s) :
    805*t < residualD s t := by
  have ht0 : 0 < t := by omega
  have ht6 : (3 : ℤ)^6 ≤ t^6 := pow_le_pow_left₀ (by norm_num) ht 6
  have hbound := residual_lower_bound s t (by omega) hst
  have hmul := mul_le_mul_of_nonneg_right ht6 (le_of_lt ht0)
  norm_num at hmul
  nlinarith [show t^6*t=t^7 by ring]

theorem residual_nondivisibility (s t u : ℤ) (hst : IsCoprime s t)
    (ht : 3 ≤ t) (horder : t < s) (hu : 0 < u) (hut : u < t) :
    ¬ residualD s t ∣ (t-u)*residualB s t := by
  intro h
  have hd := reduced_divisibility s t u hst h
  have hpos : 0 < 805*(t-u) := by omega
  have hle := Int.le_of_dvd hpos hd
  have hlarge := residual_exceeds_805 s t ht horder
  omega

theorem common_factor_pos (s t : ℤ) (hs : 0 < s) (ht : 0 < t) :
    0 < commonG s t := by
  have hp : 0 < s^2*t^2 := by positivity
  have hsq := sq_nonneg (s^2-t^2)
  unfold commonG
  nlinarith

theorem complete_nondivisibility (s t u : ℤ) (hst : IsCoprime s t)
    (ht : 3 ≤ t) (horder : t < s) (hu : 0 < u) (hut : u < t) :
    ¬ (s^12-t^12) ∣ (t-u)*commonG s t*residualB s t := by
  intro h
  have hg : commonG s t ≠ 0 := ne_of_gt (common_factor_pos s t (by omega) (by omega))
  apply residual_nondivisibility s t u hst ht horder hu hut
  obtain ⟨c, hc⟩ := h
  refine ⟨c, ?_⟩
  apply mul_left_cancel₀ hg
  calc
    commonG s t*((t-u)*residualB s t) = (t-u)*commonG s t*residualB s t := by ring
    _ = (s^12-t^12)*c := hc
    _ = commonG s t*(residualD s t*c) := by
      rw [complete_denominator_factorization]
      ring

theorem twelve_block_power_nondivisibility (a b : ℕ) (hb : 0 < b)
    (hab : (3 : ℤ)^b < 2^a) :
    ¬ ((2 : ℤ)^(12*a)-3^(12*b)) ∣
      (3^b-2^b)*commonG (2^a) (3^b)*residualB (2^a) (3^b) := by
  have hbase : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have hcop : IsCoprime ((2 : ℤ)^a) (3^b) := hbase.pow
  have ht : (3 : ℤ) ≤ 3^b := le_self_pow₀ (by norm_num) (Nat.ne_of_gt hb)
  have hu : (0 : ℤ) < 2^b := by positivity
  have hut : (2 : ℤ)^b < 3^b := pow_lt_pow_left₀ (by norm_num) (by norm_num) (Nat.ne_of_gt hb)
  have hn := complete_nondivisibility (2^a) (3^b) (2^b) hcop ht hab hu hut
  simpa only [← pow_mul, Nat.mul_comm a 12, Nat.mul_comm b 12] using hn

#print axioms complete_denominator_factorization
#print axioms integer_bezout_805
#print axioms residual_coprime
#print axioms reduced_divisibility
#print axioms residual_lower_bound
#print axioms residual_exceeds_805
#print axioms residual_nondivisibility
#print axioms common_factor_pos
#print axioms complete_nondivisibility
#print axioms twelve_block_power_nondivisibility

end CollatzCyclotomicBlock

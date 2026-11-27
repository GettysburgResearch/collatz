import Mathlib.Data.Int.GCD
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Integral elliptic markers for a positive rational fixed point of an affine lap. -/
namespace Collatz.SixHour.Markers

/-- A positive-denominator det-one marker has the primitive first column. -/
theorem primitive_column (r q u v w t : ℤ) (hq : 0 < q) (hw : 0 < w)
    (hcop : q.gcd r = 1) (hslope : q*u = r*w) (hdet : u*(t-u)-v*w=1) :
    u=r ∧ w=q := by
  have hdiv : q ∣ r*w := ⟨u, hslope.symm⟩
  obtain ⟨k, hwk⟩ := Int.dvd_of_dvd_mul_right_of_gcd_one hdiv hcop
  have hsame : q*u=q*(r*k) := by rw [hslope, hwk]; ring
  have huk := (mul_right_inj' (ne_of_gt hq)).mp hsame
  have hprod : k*(r*(t-u)-v*q)=1 := by
    calc
      _ = (r*k)*(t-u)-v*(q*k) := by ring
      _ = 1 := by rw [← huk, ← hwk]; exact hdet
  have hk_pos : 0 < k := by
    by_contra! hn
    have := mul_nonpos_of_nonneg_of_nonpos (le_of_lt hq) hn
    omega
  have hfactor_pos : 0 < r*(t-u)-v*q := by
    by_contra! hn
    have := mul_nonpos_of_nonneg_of_nonpos (le_of_lt hk_pos) hn
    omega
  have hf : 1 ≤ r*(t-u)-v*q := by omega
  have hl := mul_le_mul_of_nonneg_left hf (le_of_lt hk_pos)
  have hk : k=1 := by rw [hprod, mul_one] at hl; omega
  simp_all

/-- Exact integral existence, retaining the full reduced denominator. -/
theorem integral_marker_iff (r q t : ℤ) (hq : 0 < q) (hcop : q.gcd r=1) :
    (∃ u v w : ℤ, 0<w ∧ q*u=r*w ∧ u*(t-u)-v*w=1) ↔ q ∣ r^2-t*r+1 := by
  constructor
  · rintro ⟨u,v,w,hw,hs,hd⟩
    obtain ⟨rfl,rfl⟩ := primitive_column r q u v w t hq hw hcop hs hd
    exact ⟨-v, by linarith only [hd]⟩
  · rintro ⟨v,hv⟩
    exact ⟨r,-v,q,hq,by ring,by linarith only [hv]⟩

/-- At an even departure two same-type markers can share only primes of three. -/
theorem two_even_cuts (q r s : ℤ) (hstep : 2*s=r)
    (hr : q ∣ r^2+1) (hs : q ∣ s^2+1) : q ∣ 3 := by
  obtain ⟨a,ha⟩ := hr
  obtain ⟨b,hb⟩ := hs
  exact ⟨4*b-a, by rw [← hstep] at ha; linarith only [ha,hb]⟩

/-- The incompatible trace-zero/trace-one markers already detect the whole denominator at one cut. -/
theorem two_traces (q r : ℤ) (hzero : q ∣ r^2+1) (hone : q ∣ r^2-r+1) : q ∣ 1 := by
  obtain ⟨a,ha⟩ := hzero
  obtain ⟨b,hb⟩ := hone
  have hc : r=q*(a-b) := by linarith only [ha,hb]
  refine ⟨a-r*(a-b), ?_⟩
  calc
    1=r^2+1-r*r := by ring
    _=q*a-r*(q*(a-b)) := by rw [ha, ← hc]
    _=q*(a-r*(a-b)) := by ring

theorem trace_alignment (g d B u w t : ℤ) :
    g*u+B*w+d*(t-u)=d*t ↔ (d-g)*u=B*w := by constructor <;> intro h <;> linarith only [h]

end Collatz.SixHour.Markers

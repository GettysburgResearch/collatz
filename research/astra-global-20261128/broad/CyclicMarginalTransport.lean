import CyclicTent
import Mathlib.Data.Nat.ModEq

/-! Positive directed routing on the log circle and its rational top-trit band. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.CyclicMarginalTransport
open Collatz.CyclicTent
open scoped BigOperators

def average (n : ℕ) (mass test : ℕ→ℚ) : ℚ := ∑ i∈Finset.range n,mass i*test i

def periodic (m : ℕ) (f : ℕ→ℚ) : Prop := ∀ d,f (d+m)=f d

def scaledTent (m L shift d : ℕ) : ℚ := (m:ℚ)*tent m L (shift+d)

def band (m L shift d : ℕ) : ℚ := scaledTent (3*m) L shift d-scaledTent m L shift d

theorem scaled_period (m L shift : ℕ) (hm : 0<m) : periodic m (scaledTent m L shift) := by
  intro d
  unfold scaledTent
  rw [show shift+(d+m)=shift+d+m by omega,tent_period _ _ _ hm]

theorem scaled_step (m L shift d : ℕ) (hm : 0<m) :
    |scaledTent m L shift (d+1)-scaledTent m L shift d|≤m := by
  unfold scaledTent
  rw [show shift+(d+1)=shift+d+1 by omega,←mul_sub,abs_mul,abs_of_nonneg (Nat.cast_nonneg m)]
  simpa only [mul_one] using mul_le_mul_of_nonneg_left (tent_step m L (shift+d) hm) (Nat.cast_nonneg m : (0:ℚ)≤m)

theorem band_period (m L shift : ℕ) (hm : 0<m) : periodic (3*m) (band m L shift) := by
  intro d
  unfold band
  rw [scaled_period _ _ _ (by omega) d]
  rw [show d+3*m=d+m+m+m by omega,scaled_period _ _ _ hm,scaled_period _ _ _ hm,scaled_period _ _ _ hm]

theorem band_zero_triple (m L shift d : ℕ) (hm : 0<m) :
    band m L shift d + band m L shift (d+m) + band m L shift (d+2*m)=0 := by
  unfold band
  rw [show d+2*m=d+m+m by omega,scaled_period m L shift hm (d+m),scaled_period m L shift hm d]
  unfold scaledTent
  rw [show shift+(d+m)=shift+d+m by omega,show shift+(d+m+m)=shift+d+2*m by omega]
  rw [tent_triple m L (shift+d) hm]
  push_cast
  ring

theorem band_step (m L shift d : ℕ) (hm : 0<m) :
    |band m L shift (d+1)-band m L shift d|≤4*(m:ℚ) := by
  have hi := abs_le.mp (scaled_step (3*m) L shift d (by omega))
  have lo := abs_le.mp (scaled_step m L shift d hm)
  push_cast at hi
  unfold band
  rw [abs_le]
  constructor <;> linarith [hi.1,hi.2,lo.1,lo.2]

theorem band_move (m L shift d gap : ℕ) (hm : 0<m) :
    band m L shift (d+gap) ≤ band m L shift d + 4*(m:ℚ)*gap := by
  induction gap with
  | zero => simp
  | succ gap ih =>
    have h := (abs_le.mp (band_step m L shift (d+gap) hm)).2
    rw [Nat.add_succ]
    push_cast
    linarith

/-- Finite path packets. Its actual source is a uniform top trit over the stated
lower marginal. Its log endpoints are the source plus the positive gap. -/
structure Flow (m : ℕ) where
  count : ℕ
  start : ℕ→ℕ
  gap : ℕ→ℕ
  mass : ℕ→ℚ
  parentMass : ℕ→ℚ
  nonneg : ∀ i<count, 0≤mass i
  positiveGap : ∀ i<count, 0<gap i
  uniformTop : ∀ (f : ℕ→ℚ), periodic (3*m) f →
    average count mass (fun i => f (start i)) =
      average m parentMass (fun d => (f d+f (d+m)+f (d+2*m))/3)

def Flow.cost {m : ℕ} (flow : Flow m) : ℚ :=
  average flow.count flow.mass (fun i => (flow.gap i:ℚ))

def Flow.demands {m : ℕ} (flow : Flow m) (target : ℕ→ℚ) : Prop :=
  ∀ (f : ℕ→ℚ), periodic (3*m) f →
    average (3*m) target f = average flow.count flow.mass (fun i => f (flow.start i+flow.gap i))

theorem flow_band_bound {m : ℕ} (hm : 0<m) (L shift : ℕ) (flow : Flow m)
    (target : ℕ→ℚ) (hroutes : flow.demands target) :
    average (3*m) target (band m L shift) ≤ 4*(m:ℚ)*flow.cost := by
  have hp := band_period m L shift hm
  have hs := flow.uniformTop (band m L shift) hp
  have hzero : average flow.count flow.mass (fun i => band m L shift (flow.start i))=0 := by
    rw [hs]
    simp only [average,band_zero_triple _ _ _ _ hm,zero_div,mul_zero,Finset.sum_const_zero]
  rw [hroutes _ hp]
  calc
    _ ≤ average flow.count flow.mass (fun i => band m L shift (flow.start i)+4*(m:ℚ)*(flow.gap i:ℚ)) := by
      apply Finset.sum_le_sum
      intro i hi
      exact mul_le_mul_of_nonneg_left (band_move m L shift _ _ hm) (flow.nonneg i (Finset.mem_range.mp hi))
    _ = average flow.count flow.mass (fun i => band m L shift (flow.start i))+4*(m:ℚ)*flow.cost := by
      unfold Flow.cost average
      simp only [mul_add,Finset.sum_add_distrib,Finset.mul_sum]
      congr 1
      apply Finset.sum_congr rfl
      intro i _
      ring
    _ = _ := by rw [hzero,zero_add]

/-- For the native inverse edge `2^e s=1+3 v`, shipping its log source `d`
through `e` positive steps gives precisely the target log cell. -/
theorem native_doubling_endpoint (M d e s v : ℕ) (hlog : 2^d ≡ s [MOD M])
    (hedge : 2^e*s ≡ 1+3*v [MOD M]) : 2^(d+e) ≡ 1+3*v [MOD M] := by
  rw [pow_add,Nat.mul_comm (2^d)]
  exact (hlog.mul_left (2^e)).trans hedge

end Collatz.CyclicMarginalTransport

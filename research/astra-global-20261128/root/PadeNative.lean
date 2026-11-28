import PinCriterion
import PadeIntegral

/-! The finite interpolation remainders on the actual ordinary even-event clock. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeNative
open CoreBranching PinClock PinCriterion
open Collatz.PadeArithmetic Collatz.FinitePade Collatz.PadeIntegral
open scoped BigOperators

def amplitude (e n : ℕ) : ℚ := (2:ℚ)^(clock e n)/3^(clock e n-e)

def nativeSum (e n : ℕ) : ℚ := ∑ j ∈ Finset.range e, amplitude j n

def blockScale (n : ℕ) : ℚ := (2:ℚ)^(twos (n+1)+1)/3^(twos (n+1))

theorem clock_ge (e n : ℕ) : e≤clock e n := by
  induction e generalizing n with
  | zero => omega
  | succ e ih =>
    have h := ih (afterEven n)
    rw [clock]
    omega

theorem first_even (n : ℕ) : run (twos (n+1)) n%2=0 := by
  have h0 := (first_block (twos (n+1)) n rfl).1
  have h1 := (first_block (twos (n+1)) n rfl).2
  rw [evenCount_add,h0] at h1
  by_contra hn
  simp [evenCount,hn] at h1

theorem run_first_block (n : ℕ) : run (twos (n+1)+1) n=afterEven n := by
  rw [run_add]
  simp only [run,afterEven]

theorem run_clock_succ (e n : ℕ) :
    run (clock (e+1) n) n=run (clock e (afterEven n)) (afterEven n) := by
  rw [clock,run_add,run_first_block]

theorem even_at_clock (e n : ℕ) : run (clock e n) n%2=0 := by
  induction e generalizing n with
  | zero => exact first_even n
  | succ e ih => rw [run_clock_succ]; exact ih (afterEven n)

theorem first_odd_shift (g n : ℕ) (hg : twos (n+1)=g) :
    2^g*(run g n+1)=3^g*(n+1) := by
  induction g generalizing n with
  | zero => simp [run]
  | succ g ih =>
    have ho : n%2≠0 := by
      intro he
      have hv := even_twos he
      omega
    have hv := odd_twos ho
    have hnext : twos (step n+1)=g := by omega
    have hstep : 2*(step n+1)=3*(n+1) := by
      unfold step
      rw [ite_eq_right ho]
      omega
    have ht := ih (step n) hnext
    calc
      _ = 2*(2^g*(run g (step n)+1)) := by simp only [run,pow_succ]; ring
      _ = 3^g*(2*(step n+1)) := by rw [ht]; ring
      _ = _ := by rw [hstep,pow_succ]; ring

theorem first_even_block (n : ℕ) :
    3^(twos (n+1))*(n+1)+2^(twos (n+1)) =
      2^(twos (n+1)+1)*(afterEven n+1) := by
  have hs := first_odd_shift (twos (n+1)) n rfl
  have he := first_even n
  have hnext : 2*(afterEven n+1)=run (twos (n+1)) n+2 := by
    simp only [afterEven,step,he,ite_true]
    omega
  have hm := congrArg (fun v : ℕ => 2^(twos (n+1))*v) hnext
  rw [pow_succ]
  nlinarith

theorem first_edge (n : ℕ) :
    (n:ℚ)+1+amplitude 0 n=blockScale n*((afterEven n:ℚ)+1) := by
  have h : (3:ℚ)^(twos (n+1))*((n:ℚ)+1)+2^(twos (n+1)) =
      2^(twos (n+1)+1)*((afterEven n:ℚ)+1) := by
    exact_mod_cast first_even_block n
  unfold amplitude blockScale
  simp only [clock,Nat.sub_zero]
  field_simp
  nlinarith

theorem amplitude_succ (e n : ℕ) :
    amplitude (e+1) n=blockScale n*amplitude e (afterEven n) := by
  have hc := clock_ge e (afterEven n)
  have he : twos (n+1)+1+clock e (afterEven n)-(e+1)=
      twos (n+1)+(clock e (afterEven n)-e) := by omega
  unfold amplitude blockScale
  rw [clock,he,pow_add,pow_add]
  ring

theorem nativeSum_succ (e n : ℕ) :
    nativeSum (e+1) n=amplitude 0 n+blockScale n*nativeSum e (afterEven n) := by
  simp only [nativeSum,Finset.sum_range_succ',amplitude_succ,←Finset.mul_sum]
  ring

/-- Exact native telescoping, before the next even input is performed. -/
theorem native_calibration (e n : ℕ) :
    (n:ℚ)+1+nativeSum e n =
      amplitude e n*((run (clock e n) n:ℚ)+1) := by
  induction e generalizing n with
  | zero =>
    have h : (2:ℚ)^(twos (n+1))*((run (twos (n+1)) n:ℚ)+1) =
        3^(twos (n+1))*((n:ℚ)+1) := by
      exact_mod_cast first_odd_shift (twos (n+1)) n rfl
    simp only [nativeSum,Finset.range_zero,Finset.sum_empty,add_zero,amplitude,
      clock,Nat.sub_zero]
    field_simp
    nlinarith
  | succ e ih =>
    calc
      _ = ((n:ℚ)+1+amplitude 0 n)+blockScale n*nativeSum e (afterEven n) := by
        rw [nativeSum_succ]
        ring
      _ = blockScale n*((afterEven n:ℚ)+1+nativeSum e (afterEven n)) := by
        rw [first_edge]
        ring
      _ = blockScale n*(amplitude e (afterEven n)*
          ((run (clock e (afterEven n)) (afterEven n):ℚ)+1)) := by rw [ih]
      _ = _ := by rw [amplitude_succ,run_clock_succ]; ring

def schedule (b h j : ℕ) : ℕ := j*(b+1)+h*tri j

theorem schedule_ge (b h j : ℕ) : j≤schedule b h j := by
  unfold schedule
  nlinarith

theorem schedule_sub (b h j : ℕ) : schedule b h j-j=b*j+h*tri j := by
  unfold schedule
  rw [show j*(b+1)+h*tri j=b*j+h*tri j+j by ring,Nat.add_sub_cancel]

theorem amplitude_of_schedule (b h j n : ℕ) (hc : clock j n=schedule b h j) :
    amplitude j n=term (qBase h) (zBase b) j := by
  unfold amplitude
  rw [hc,schedule_sub]
  simp only [term,qBase,zBase,div_pow,←pow_mul,schedule,pow_add]
  rw [Nat.mul_comm j (b+1)]
  field_simp
  ring

theorem nativeSum_of_schedule (b h e n : ℕ)
    (hc : ∀ j<e, clock j n=schedule b h j) :
    nativeSum e n=partialSum (qBase h) (zBase b) e := by
  unfold nativeSum partialSum
  apply Finset.sum_congr rfl
  intro j hj
  exact amplitude_of_schedule b h j n (hc j (Finset.mem_range.mp hj))

/-- A finite prefix of actual even clocks supplies each Padé remainder exactly. -/
theorem native_remainder (b h e n : ℕ)
    (hc : ∀ j<e, clock j n=schedule b h j) :
    -((n:ℚ)+1)-partialSum (qBase h) (zBase b) e =
      -amplitude e n*((run (clock e n) n:ℚ)+1) := by
  have hcal := native_calibration e n
  rw [nativeSum_of_schedule b h e n hc] at hcal
  nlinarith

end Collatz.PadeNative

import CoreBranching
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Exact arithmetic behind a repeated shifted cofactor.

The endpoint hypothesis says that `2*n+1` and `2*run r n+1` have the same
factor after removing powers of three.  No existence of a collision, bound
for logarithmic forms, or assertion of universal convergence is assumed
implicitly.  The final bound retains its finite, explicit power gap.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.CofactorDescent
open CoreBranching

def height (n : ℕ) : ℕ := 2*n+1

def odds : ℕ → ℕ → ℕ
  | 0, _ => 0
  | r+1, n => n%2 + odds r (step n)

def numerator (n : ℕ) : ℚ := (3:ℚ)^(n%2) * (height n : ℚ)

def weight (n : ℕ) : ℚ := numerator n / (numerator n + 1)

def survival : ℕ → ℕ → ℚ
  | 0, _ => 1
  | r+1, n => weight n * survival r (step n)

theorem shifted_step (n : ℕ) :
    2*height (step n) = 3^(n%2)*height n+1 := by
  have hm : n%2<2 := Nat.mod_lt n (by decide)
  interval_cases h : n%2
  · simp only [step,h,ite_true,pow_zero,one_mul,height]
    omega
  · simp only [step,h,pow_one,height]
    split <;> omega

theorem numerator_pos (n : ℕ) : 0<numerator n := by
  unfold numerator height
  positivity

theorem numerator_ge_height (n : ℕ) : (height n : ℚ) ≤ numerator n := by
  have hm : n%2<2 := Nat.mod_lt n (by decide)
  interval_cases h : n%2 <;> simp only [numerator,h,pow_zero,pow_one,one_mul]
  · exact le_rfl
  · have hp : (0:ℚ)≤height n := Nat.cast_nonneg _
    linarith

theorem weight_bounds (n : ℕ) : 0<weight n ∧ weight n<1 := by
  have hp := numerator_pos n
  unfold weight
  constructor
  · positivity
  · exact (div_lt_one (by positivity)).mpr (by linarith)

theorem survival_bounds (r n : ℕ) : 0<survival r n ∧ survival r n≤1 := by
  induction r generalizing n with
  | zero => norm_num [survival]
  | succ r ih =>
    obtain ⟨ha,hb⟩ := weight_bounds n
    obtain ⟨hc,hd⟩ := ih (step n)
    simp only [survival]
    constructor
    · exact mul_pos ha hc
    · nlinarith

theorem survival_lt_one (r n : ℕ) (hr : 0<r) : survival r n<1 := by
  cases r with
  | zero => omega
  | succ r =>
    have hw := weight_bounds n
    have hs := survival_bounds r (step n)
    simp only [survival]
    nlinarith

theorem weight_calibration (n : ℕ) :
    weight n * (2*(height (step n):ℚ)) = numerator n := by
  have he : 2*(height (step n):ℚ)=numerator n+1 := by
    unfold numerator
    exact_mod_cast shifted_step n
  rw [he]
  unfold weight
  exact div_mul_cancel₀ _ (ne_of_gt (by linarith [numerator_pos n]))

theorem survival_calibration (r n : ℕ) :
    survival r n * (2:ℚ)^r * (height (run r n):ℚ) =
      (3:ℚ)^(odds r n) * (height n:ℚ) := by
  induction r generalizing n with
  | zero => simp [survival,run,odds]
  | succ r ih =>
    have hh := ih (step n)
    have hw := weight_calibration n
    calc
      _ = (2*weight n) *
          (survival r (step n) * (2:ℚ)^r * (height (run r (step n)):ℚ)) := by
            simp only [survival,run,pow_succ]
            ring
      _ = (2*weight n) * ((3:ℚ)^(odds r (step n)) * (height (step n):ℚ)) := by rw [hh]
      _ = (3:ℚ)^(odds r (step n)) * numerator n := by
            calc
              _ = (3:ℚ)^(odds r (step n)) * (weight n*(2*(height (step n):ℚ))) := by ring
              _ = _ := by rw [hw]
      _ = _ := by simp only [odds,pow_add,numerator]; ring

theorem edge_deficit (m n : ℕ) (hm : m≤n) :
    (2*(m:ℚ)+2)*(1-weight n) ≤ 1 := by
  have hp := numerator_pos n
  have hn := numerator_ge_height n
  have hc : (m:ℚ)≤n := by exact_mod_cast hm
  have hh : (height n:ℚ)=2*(n:ℚ)+1 := by simp [height]
  have hw : 1-weight n = 1/(numerator n+1) := by
    unfold weight
    field_simp
    ring
  rw [hw, mul_one_div]
  apply (div_le_one (by positivity)).mpr
  linarith

/-- The union bound on the actual correction losses, with no analytic estimates. -/
theorem path_deficit (r m n : ℕ)
    (floor : ∀ j<r, m≤run j n) :
    (2*(m:ℚ)+2)*(1-survival r n) ≤ (r:ℚ) := by
  induction r generalizing n with
  | zero => norm_num [survival]
  | succ r ih =>
    have hfirst : m≤n := by simpa only [run] using floor 0 (by omega)
    have htail : ∀ j<r, m≤run j (step n) := by
      intro j hj
      exact floor (j+1) (by omega)
    have he := edge_deficit m n hfirst
    have ht := ih (step n) htail
    have hw := weight_bounds n
    have hs := survival_bounds r (step n)
    have hM : 0≤2*(m:ℚ)+2 := by positivity
    have herr : 0≤(2*(m:ℚ)+2)*(1-weight n)*(1-survival r (step n)) :=
      mul_nonneg (mul_nonneg hM (by linarith)) (by linarith)
    simp only [survival, Nat.cast_add, Nat.cast_one]
    nlinarith

theorem collision_calibration (r n q a b : ℕ) (hq : 0<q)
    (hstart : height n=q*3^a) (hend : height (run r n)=q*3^b) :
    survival r n * ((2:ℚ)^r*(3:ℚ)^b) = (3:ℚ)^(a+odds r n) := by
  have hh := survival_calibration r n
  have hs : (height n:ℚ)=(q:ℚ)*(3:ℚ)^a := by exact_mod_cast hstart
  have he : (height (run r n):ℚ)=(q:ℚ)*(3:ℚ)^b := by exact_mod_cast hend
  rw [hs,he] at hh
  have hq' : (q:ℚ)≠0 := by exact_mod_cast (Nat.ne_of_gt hq)
  apply mul_right_cancel₀ hq'
  calc
    _ = survival r n * (2:ℚ)^r * ((q:ℚ)*(3:ℚ)^b) := by ring
    _ = (3:ℚ)^(odds r n) * ((q:ℚ)*(3:ℚ)^a) := hh
    _ = _ := by rw [pow_add]; ring

/-- A repeated cofactor has a strictly positive power gap on every nonempty path. -/
theorem collision_power_gap (r n q a b : ℕ) (hr : 0<r) (hq : 0<q)
    (hstart : height n=q*3^a) (hend : height (run r n)=q*3^b) :
    (3:ℚ)^(a+odds r n) < (2:ℚ)^r*(3:ℚ)^b := by
  have hc := collision_calibration r n q a b hq hstart hend
  have hs := survival_lt_one r n hr
  have hp : (0:ℚ)<(2:ℚ)^r*(3:ℚ)^b := by positivity
  nlinarith

/-- Explicit bound on the input floor in terms of the exact endpoint power gap. -/
theorem collision_floor (r m n q a b : ℕ) (hq : 0<q)
    (floor : ∀ j<r, m≤run j n)
    (hstart : height n=q*3^a) (hend : height (run r n)=q*3^b) :
    (2*(m:ℚ)+2) * ((2:ℚ)^r*(3:ℚ)^b-(3:ℚ)^(a+odds r n)) ≤
      (r:ℚ)*((2:ℚ)^r*(3:ℚ)^b) := by
  have hd := path_deficit r m n floor
  have hc := collision_calibration r n q a b hq hstart hend
  have hp : (0:ℚ)≤(2:ℚ)^r*(3:ℚ)^b := by positivity
  have hm := mul_le_mul_of_nonneg_right hd hp
  calc
    _ = ((2*(m:ℚ)+2)*(1-survival r n))*((2:ℚ)^r*(3:ℚ)^b) := by
      rw [← hc]
      ring
    _ ≤ _ := hm

/-- A stated relative separation of the powers forces an ordinary low state. -/
theorem low_state_of_relative_gap (r m n q a b : ℕ) (hq : 0<q)
    (η : ℚ) (_hη : 0<η)
    (hstart : height n=q*3^a) (hend : height (run r n)=q*3^b)
    (gap : (3:ℚ)^(a+odds r n) ≤ (1-η)*((2:ℚ)^r*(3:ℚ)^b))
    (short : (r:ℚ)<(2*(m:ℚ)+2)*η) :
    ∃ j<r, run j n<m := by
  by_contra! high
  have hf := collision_floor r m n q a b hq high hstart hend
  have hp : (0:ℚ)<(2:ℚ)^r*(3:ℚ)^b := by positivity
  have hM : (0:ℚ)≤2*(m:ℚ)+2 := by positivity
  have hg := mul_le_mul_of_nonneg_left gap hM
  have hshort := mul_lt_mul_of_pos_right short hp
  nlinarith

end Collatz.CofactorDescent

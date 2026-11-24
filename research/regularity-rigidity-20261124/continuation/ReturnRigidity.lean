import Mathlib

set_option autoImplicit false

namespace ReturnRigidity

/-- Exact finite shortcut affine expression over rational coordinates. -/
def step (b : Bool) (x : ℚ) : ℚ :=
  if b then (3*x+1)/2 else x/2

def run : List Bool → ℚ → ℚ
  | [], x => x
  | b::w, x => run w (step b x)

def slope : List Bool → ℚ
  | [] => 1
  | b::w => slope w * (if b then 3/2 else 1/2)

def offset : List Bool → ℚ
  | [] => 0
  | b::w => offset w + slope w * (if b then 1/2 else 0)

theorem run_affine (w : List Bool) (x : ℚ) :
    run w x = slope w*x + offset w := by
  induction w generalizing x with
  | nil => simp [run, slope, offset]
  | cons b w ih =>
    rw [run, ih]
    cases b <;> simp [step, slope, offset] <;> ring

theorem run_append (u v : List Bool) (x : ℚ) :
    run (u++v) x = run v (run u x) := by
  induction u generalizing x with
  | nil => simp [run]
  | cons b u ih => simp [run, ih]

theorem common_prefix_tail {Q D : Type*} (step : Q → D → Q)
    (q r : Q) (u v w : List D)
    (h : u.foldl step q = v.foldl step r) :
    (u++w).foldl step q = (v++w).foldl step r := by
  rw [List.foldl_append, List.foldl_append, h]

/-- Exact quadratic drift for two symmetric increments. -/
theorem symmetric_quadratic (x d : ℝ) :
    ((x+d)^2+(x-d)^2)/2-x^2 = d^2 := by ring

/-- A pair of probability masses sharing a common subdistribution. -/
theorem shared_mass {a b c : ℝ} (ha : c ≤ a) (hb : c ≤ b) :
    c ≤ min a b := le_min ha hb

/-- Binary error after decorrelation is bounded below by constant prediction. -/
theorem constant_prediction_bound (p q : ℝ)
    (hp0 : 0 ≤ p) (hp1 : p ≤ 1)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1) :
    min p (1-p) ≤ p+q-2*p*q := by
  by_cases h : p ≤ 1-p
  · rw [min_eq_left h]
    have h2 : 0 ≤ 1-2*p := by linarith
    nlinarith [mul_nonneg q h2]
  · have h' : 1-p ≤ p := le_of_lt (lt_of_not_ge h)
    rw [min_eq_right h']
    have h2 : 0 ≤ 2*p-1 := by linarith
    nlinarith [mul_nonneg (sub_nonneg.mpr hq1) h2]

/-- The binary mismatch expression, with no independence assumption. -/
theorem error_covariance (p q joint : ℝ) :
    p+q-2*joint = p+q-2*p*q-2*(joint-p*q) := by ring

#print axioms run_affine
#print axioms run_append
#print axioms common_prefix_tail
#print axioms symmetric_quadratic
#print axioms shared_mass
#print axioms constant_prediction_bound
#print axioms error_covariance

end ReturnRigidity

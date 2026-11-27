import Mathlib.Tactic

/-! Physical binary lifts, contraction at a pair of cycle anchors, and the
one-dimensional real estimate for an ordinary two-arm profile. -/

set_option autoImplicit false
namespace Collatz.PairedProfiles

def bit (x : ℕ) : ℕ := x % 2

def step (x : ℕ) : ℕ := (3 ^ bit x * x + bit x) / 2

def trace : ℕ → ℕ → ℕ × ℕ
  | 0, x => (x, 0)
  | h+1, x => let z := trace h x; (step z.1, z.2 + bit z.1)

theorem bit_add_twice (a d : ℕ) : bit (a + 2*d) = bit a := by
  simp [bit, Nat.add_mod]

theorem step_add_twice (a d : ℕ) :
    step (a + 2*d) = step a + 3^(bit a)*d := by
  simp only [step, bit_add_twice]
  have he : 3^bit a * (a + 2*d) + bit a =
      (3^bit a*a + bit a) + (3^bit a*d)*2 := by ring
  rw [he, Nat.add_mul_div_right]
  decide

theorem lift (h r t : ℕ) :
    trace h (r + 2^h*t) =
      ((trace h r).1 + 3^(trace h r).2*t, (trace h r).2) := by
  induction h generalizing t with
  | zero => simp [trace]
  | succ h ih =>
    rw [show r + 2^(h+1)*t = r + 2^h*(2*t) by ring, trace, ih]
    change (step ((trace h r).1 + 3^(trace h r).2*(2*t)),
        (trace h r).2 + bit ((trace h r).1 + 3^(trace h r).2*(2*t))) = _
    rw [show 3^(trace h r).2*(2*t) = 2*(3^(trace h r).2*t) by ring,
        step_add_twice, bit_add_twice]
    simp only [trace, pow_add]
    congr 2
    ring

theorem trace_add (h k r : ℕ) :
    trace (h+k) r = ((trace k (trace h r).1).1, (trace h r).2+(trace k (trace h r).1).2) := by
  induction k with
  | zero => simp [trace]
  | succ k ih => simp [trace, ih, Nat.add_assoc]

theorem cycle_pair (y : ℕ) (hy : y=1 ∨ y=2) : trace 2 y = (y,1) := by
  rcases hy with rfl | rfl <;> decide

theorem anchor_arm (r h t : ℕ) (hr : (trace h r).1=1 ∨ (trace h r).1=2) :
    (trace (h+2) (r+2^(h+2)*t)).1 = (trace h (r+3*2^h*t)).1 := by
  rw [lift, show r+3*2^h*t = r+2^h*(3*t) by ring, lift, trace_add, cycle_pair _ hr]
  simp only [pow_succ]
  ring

theorem paired_anchor (r h t : ℕ)
    (hl : (trace h r).1=1 ∨ (trace h r).1=2)
    (hu : (trace h (3*r)).1=1 ∨ (trace h (3*r)).1=2) :
    (trace (h+2) (r+2^(h+2)*t)).1 = (trace h (r+3*2^h*t)).1 ∧
    (trace (h+2) (3*(r+2^(h+2)*t))).1 = (trace h (3*(r+3*2^h*t))).1 := by
  refine ⟨anchor_arm r h t hl, ?_⟩
  rw [show 3*(r+2^(h+2)*t) = 3*r+2^(h+2)*(3*t) by ring,
      show 3*(r+3*2^h*t) = 3*r+3*2^h*(3*t) by ring]
  exact anchor_arm (3*r) h (3*t) hu

theorem anchor_smaller (r h t : ℕ) (ht : 0<t) :
    r+3*2^h*t < r+2^(h+2)*t := by
  have hp : 0 < 2^h*t := by positivity
  rw [show r+2^(h+2)*t = r+4*(2^h*t) by ring,
      show r+3*2^h*t = r+3*(2^h*t) by ring]
  omega

theorem translate_profile (h r s t : ℕ)
    (hl : trace h r = trace h s) (hu : trace h (3*r) = trace h (3*s)) :
    trace h (r+2^h*t) = trace h (s+2^h*t) ∧
    trace h (3*(r+2^h*t)) = trace h (3*(s+2^h*t)) := by
  constructor
  · simp only [lift, hl]
  · rw [show 3*(r+2^h*t) = 3*r+2^h*(3*t) by ring,
        show 3*(s+2^h*t) = 3*s+2^h*(3*t) by ring, lift, lift, hu]

/-- The smaller-slope endpoint is within one carry budget of the larger
endpoint times their slope ratio, after cancelling the shared seed. -/
theorem profile_strip (a b R d z : ℝ) (hd : 0 ≤ d) (hD : d ≤ 1)
    (ha : 0 ≤ a) (haR : a ≤ R) (hb : 0 ≤ b) (hbR : b ≤ R) :
    -R ≤ (d*z+a)-d*(z+b) ∧ (d*z+a)-d*(z+b) ≤ R := by
  have hdb : 0 ≤ d*b := mul_nonneg hd hb
  have hub : d*b ≤ b := by nlinarith [mul_nonneg (sub_nonneg.mpr hD) hb]
  constructor <;> nlinarith

theorem location (X Y b c G R : ℝ) (hG : 0 ≤ G)
    (hb : 0 ≤ b) (hc : c ≤ R) (hxy : X + G*b = Y + G*c) :
    X-Y ≤ G*R := by
  nlinarith [mul_nonneg hG hb, mul_nonneg hG (sub_nonneg.mpr hc)]

#print axioms lift
#print axioms trace_add
#print axioms anchor_arm
#print axioms paired_anchor
#print axioms anchor_smaller
#print axioms translate_profile
#print axioms profile_strip
#print axioms location
end Collatz.PairedProfiles

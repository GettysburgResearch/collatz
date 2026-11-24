import Mathlib

set_option autoImplicit false

namespace RegularityRigidity

def T (x : ℤ) : ℤ := if x % 2 = 0 then x / 2 else (3*x+1)/2

/-- Whole two-adic cylinder lift for one step. -/
theorem step_lift (x t : ℤ) :
    T (x+2*t) = T x + (if x % 2 = 0 then 1 else 3)*t := by
  by_cases h : x % 2 = 0
  · have h' : (x+2*t) % 2 = 0 := by omega
    simp only [T, h, h', if_true, one_mul]
    omega
  · have h' : (x+2*t) % 2 ≠ 0 := by omega
    simp only [T, h, h', if_false]
    omega

/-- An exact affine profile yields an inverse on the given endpoint. -/
theorem affine_inverse {a c q x : ℤ} {h e : ℕ}
    (hle : h ≤ e)
    (hx : a*x+c = (2:ℤ)^e*q) :
    a*x+c = (2:ℤ)^h*((2:ℤ)^(e-h)*q) := by
  rw [hx, ← mul_assoc, ← pow_add, Nat.add_sub_of_le hle]

/-- The weighted stopping-time phase increment, before reduction mod d. -/
theorem weighted_phase_increment
    (w u e j W W' ell ell' : ℤ)
    (hw : W' = W+w*e+u)
    (ha : ell' = ell+e-j) :
    W'-w*ell' = W-w*ell+u+w*j := by
  rw [hw, ha]
  ring

/-- A path's multiplicative growth and its lower weight telescope. -/
theorem path_probability_step {p p' x x' G s : ℝ}
    (hG : 0 < G) (hx : 0 ≤ x') (hs : 0 ≤ s)
    (hp : p' ≤ p / G) (hpp : 0 ≤ p)
    (hxx : x' ≤ G*x) (hbound : p*x ≤ s) :
    p'*x' ≤ s := by
  calc
    p'*x' ≤ (p/G)*x' := mul_le_mul_of_nonneg_right hp hx
    _ ≤ (p/G)*(G*x) := mul_le_mul_of_nonneg_left hxx (div_nonneg hpp hG.le)
    _ = p*x := by field_simp [ne_of_gt hG]
    _ ≤ s := hbound

/-- One monochromatic actual block forces an error if the prediction is not monochromatic. -/
theorem block_error {f g : ℕ → Bool} {x M : ℕ} {c : Bool}
    (hf : ∀ i < M, f (x+i) = c)
    (hg : ¬ (∀ i < M, g (x+i) = c)) :
    ∃ i < M, f (x+i) ≠ g (x+i) := by
  by_contra hn
  apply hg
  intro i hi
  have he : f (x+i) = g (x+i) := by
    by_contra hne
    exact hn ⟨i, hi, hne⟩
  rw [← he]
  exact hf i hi

def feed {Q D : Type*} (step : Q → D → Q) (q : Q) : List D → Q
  | [] => q
  | a::w => feed step (step q a) w

theorem feed_append {Q D : Type*} (step : Q → D → Q)
    (q : Q) (u v : List D) :
    feed step q (u++v) = feed step (feed step q u) v := by
  induction u generalizing q with
  | nil => simp [feed]
  | cons a u ih => simp [feed, ih]

/-- Prefixes reaching the same state have identical output on every common suffix. -/
theorem prefix_transfer {Q D A : Type*} (step : Q → D → Q) (out : Q → A)
    (q : Q) (u v w : List D) (h : feed step q u = feed step q v) :
    out (feed step q (u++w)) = out (feed step q (v++w)) := by
  rw [feed_append, feed_append, h]

#print axioms step_lift
#print axioms affine_inverse
#print axioms weighted_phase_increment
#print axioms path_probability_step
#print axioms block_error
#print axioms feed_append
#print axioms prefix_transfer

end RegularityRigidity

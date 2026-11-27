import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Positive real and ordinary-integer consequences of genuine odd affine words. -/
set_option autoImplicit false

namespace Collatz.Diagonal.RecordAffine

/-- Input letters are actual positive divisors `2^e`, in chronological order. -/
def gain : List ℚ → ℚ
  | [] => 1
  | d :: ds => (3/d) * gain ds

def forward : List ℚ → ℚ → ℚ
  | [], x => x
  | d :: ds, x => forward ds ((3*x+1)/d)

theorem gain_pos {ds : List ℚ} (hp : ∀ d ∈ ds, 0 < d) : 0 < gain ds := by
  induction ds with
  | nil => norm_num [gain]
  | cons d ds ih =>
    have hd := hp d (by simp)
    have hds : ∀ q ∈ ds, 0 < q := fun q hq => hp q (by simp [hq])
    exact mul_pos (div_pos (by norm_num) hd) (ih hds)

theorem forward_ge_linear (ds : List ℚ) (hp : ∀ d ∈ ds, 0 < d) (x : ℚ) :
    gain ds * x ≤ forward ds x := by
  induction ds generalizing x with
  | nil => simp [gain, forward]
  | cons d ds ih =>
    have hd := hp d (by simp)
    have hds : ∀ q ∈ ds, 0 < q := fun q hq => hp q (by simp [hq])
    have hg := gain_pos hds
    have h := ih hds ((3*x+1)/d)
    have hs : (3 / d * gain ds) * x ≤ gain ds * ((3*x+1)/d) := by
      field_simp [hd.ne']
      nlinarith
    exact hs.trans h

/-- The first physical +1 costs at least one third before applying the gain. -/
theorem forward_ge_gain_add_third (d : ℚ) (ds : List ℚ)
    (hp : ∀ q ∈ d :: ds, 0 < q) (x : ℚ) :
    gain (d::ds) * (x + 1/3) ≤ forward (d::ds) x := by
  have hd := hp d (by simp)
  have hds : ∀ q ∈ ds, 0 < q := fun q hq => hp q (by simp [hq])
  have h := forward_ge_linear ds hds ((3*x+1)/d)
  have he : gain (d::ds) * (x+1/3) = gain ds * ((3*x+1)/d) := by
    simp only [gain]
    field_simp [hd.ne']
  exact he ▸ h

theorem record_drop (d : ℚ) (ds : List ℚ)
    (hp : ∀ q ∈ d :: ds, 0 < q) (hg : 1 < gain (d::ds))
    (x : ℚ) (hx : 0 ≤ x) : x + 1/3 < forward (d::ds) x := by
  have hp' : 0 < x + 1/3 := by linarith
  have h1 := mul_lt_mul_of_pos_right hg hp'
  have h2 := forward_ge_gain_add_third d ds hp x
  linarith

theorem chain_budget (r : ℕ → ℚ) (n : ℕ)
    (h : ∀ i < n, r (i+1) + 1/3 ≤ r i) :
    r n + (n:ℚ)/3 ≤ r 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    have ht := ih (fun i hi => h i (Nat.lt_succ_of_lt hi))
    have hs := h n (Nat.lt_succ_self n)
    push_cast
    linarith

end Collatz.Diagonal.RecordAffine

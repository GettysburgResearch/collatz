import RotationDuals

/-! A checked endpoint certificate forces a violated row at every interpolated
slope. The offending row is allowed to depend on the slope and cube point. -/
set_option autoImplicit false
namespace Collatz.InfiniteDescent.CubeDual

def weightValue (f : Row → ℝ) : List Row → ℝ
  | [] => 0
  | r::rs => (r.weight : ℝ)*f r + weightValue f rs

theorem weightValue_endpoint (edge : Bool) (rs : List Row) (x : ℕ → ℝ) (n : ℕ) :
    weightValue (fun r => value (rowCoeff edge r) x n) rs =
      value (combine edge rs) x n := by
  induction rs with
  | nil =>
    simp only [weightValue]
    induction n with
    | zero => simp [value,combine]
    | succ n ih => simpa [value,combine] using ih
  | cons r rs ih =>
    change _=(value (fun j => (r.weight:ℤ)*rowCoeff edge r j + combine edge rs j) x n)
    simp only [weightValue,ih,value_smul_add,Int.cast_natCast]

theorem weightValue_blend (s : ℝ) (f g : Row → ℝ) (rs : List Row) :
    weightValue (fun r => (1-s)*f r+s*g r) rs =
      (1-s)*weightValue f rs+s*weightValue g rs := by
  induction rs with
  | nil => simp [weightValue]
  | cons r rs ih => simp only [weightValue,ih]; ring

theorem weightValue_lower (t : ℝ) (f : Row → ℝ) (rs : List Row)
    (h : ∀ r ∈ rs, t ≤ f r) : (total rs : ℝ)*t ≤ weightValue f rs := by
  induction rs with
  | nil => simp [total,weightValue]
  | cons r rs ih =>
    simp only [total,weightValue,Nat.cast_add,add_mul]
    exact add_le_add
      (mul_le_mul_of_nonneg_left (h r List.mem_cons_self) (Nat.cast_nonneg r.weight))
      (ih (fun a ha => h a (List.mem_cons_of_mem _ ha)))

theorem endpoint_cap_lt (c : Certificate) (edge : Bool)
    (hm : 0<c.reciprocalMargin) (hc : endpointPass c edge = true) :
    (cap (combine edge c.rows) c.dimension : ℝ) <
      (total c.rows : ℝ)*(-10000/(c.reciprocalMargin : ℝ)) := by
  have dint : c.reciprocalMargin*cap (combine edge c.rows) c.dimension+
      10000*(total c.rows : ℤ)<0 := of_decide_eq_true hc
  have dreal : (c.reciprocalMargin:ℝ)*(cap (combine edge c.rows) c.dimension:ℝ)+
      10000*(total c.rows : ℝ)<0 := by exact_mod_cast dint
  have pos : (0:ℝ)<c.reciprocalMargin := by exact_mod_cast hm
  rw [← mul_div_assoc,lt_div_iff₀ pos]
  linarith only [dreal]

theorem interpolated_row_lt (c : Certificate) (hc : passes c = true)
    (hm : 0<c.reciprocalMargin) (x : ℕ → ℝ) (hx : ∀ i, 0≤x i ∧ x i≤1)
    (s : ℝ) (hs : 0≤s ∧ s≤1) :
    ∃ r ∈ c.rows, (1-s)*value (rowCoeff false r) x c.dimension+
      s*value (rowCoeff true r) x c.dimension < -10000/(c.reciprocalMargin:ℝ) := by
  have both : endpointPass c false = true ∧ endpointPass c true = true :=
    Bool.and_eq_true_iff.mp hc
  let t : ℝ := -10000/(c.reciprocalMargin:ℝ)
  let f := fun edge r => value (rowCoeff edge r) x c.dimension
  have strict (edge : Bool) (he : endpointPass c edge = true) :
      weightValue (f edge) c.rows < (total c.rows : ℝ)*t := by
    rw [weightValue_endpoint]
    exact lt_of_le_of_lt (value_le_cap _ _ hx _) (endpoint_cap_lt c edge hm he)
  have ea := strict false both.1
  have eb := strict true both.2
  by_contra! hall
  have lower := weightValue_lower t (fun r => (1-s)*f false r+s*f true r) c.rows hall
  rw [weightValue_blend] at lower
  by_cases se : s=1
  · subst s; simp at lower; exact (not_lt_of_ge lower) eb
  · have sl : 0<1-s := by linarith [lt_of_le_of_ne hs.2 se]
    have la := mul_lt_mul_of_pos_left ea sl
    have lb := mul_le_mul_of_nonneg_left eb.le hs.1
    linarith only [lower,la,lb]

end Collatz.InfiniteDescent.CubeDual

namespace Collatz.InfiniteDescent.RotationDuals
open CubeDual

theorem certified_interior (c : Certificate) (hc : c ∈ allCases)
    (x : ℕ → ℝ) (hx : ∀ i, 0≤x i ∧ x i≤1) (s : ℝ) (hs : 0≤s ∧ s≤1) :
    ∃ r ∈ c.rows, (1-s)*value (rowCoeff false r) x c.dimension+
      s*value (rowCoeff true r) x c.dimension < -10000/(c.reciprocalMargin:ℝ) := by
  apply interpolated_row_lt c (allCases_pass c hc) _ x hx s hs
  have pos : allCases.all (fun a => decide (0<a.reciprocalMargin)) = true := by decide +kernel
  exact of_decide_eq_true ((List.all_eq_true.mp pos) c hc)

end Collatz.InfiniteDescent.RotationDuals

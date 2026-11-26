import NonunitExit
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Int.GCD

/-! Integer kernels for transporting an entire legal list of odd inverse
exponents between ordinary and signed roots.  The gain and density bounds
in FRESH_ASCENT_BARRIER.md are written results. -/
namespace Collatz.FreshAscentShadow

set_option autoImplicit false

/-- Read the list outwards from the root.  Each row is the exact signed
integer equation for division by three at a positive dyadic exponent. -/
def OddInversePath : List ℕ → ℤ → ℤ → Prop
  | [], x, y => x = y
  | e :: es, x, y => 0 < e ∧ ∃ v : ℤ, 3*v = 2^e*x-1 ∧ OddInversePath es v y

/-- The same exponent list gives at most one integer endpoint. -/
theorem endpoint_unique (es : List ℕ) (x u v : ℤ)
    (hu : OddInversePath es x u) (hv : OddInversePath es x v) : u = v := by
  induction es generalizing x u v with
  | nil => exact hu.symm.trans hv
  | cons e es ih =>
    obtain ⟨_, y, hy, hup⟩ := hu
    obtain ⟨_, z, hz, hvp⟩ := hv
    have h : y = z := by omega
    subst z
    exact ih y u v hup hvp

/-- A shift by the full ternary class preserves each legal edge. -/
theorem shift_path (es : List ℕ) (x y t : ℤ) (h : OddInversePath es x y) :
    OddInversePath es (x+3^es.length*t) (y+2^es.sum*t) := by
  induction es generalizing x y t with
  | nil =>
    change x = y at h
    simp [OddInversePath,h]
  | cons e es ih =>
    obtain ⟨he, v, hv, hp⟩ := h
    refine ⟨he, v+3^es.length*(2^e*t), ?_, ?_⟩
    · have heq : (3:ℤ)^(e :: es).length = 3^es.length*3 := by
        simp [pow_succ]
      rw [heq]
      calc
        _ = 3*v+3*(3^es.length*(2^e*t)) := by ring
        _ = _ := by rw [hv]; ring
    · have ht := ih v y (2^e*t) hp
      have hr : y+2^(e :: es).sum*t = y+2^es.sum*(2^e*t) := by
        simp only [List.sum_cons,pow_add]
        ring
      rw [hr]
      exact ht

/-- Transfer from a positive ascent terminal directly to the signed fixed
point.  This moves all intermediate integers via the same exponent list. -/
theorem at_signed_fixed_point (es : List ℕ) (q u t : ℤ)
    (hclass : q+1=3^es.length*t) (h : OddInversePath es q u) :
    OddInversePath es (-1) (u-2^es.sum*t) := by
  have hs := shift_path es q u (-t) h
  have hq : q+3^es.length*(-t) = -1 := by
    rw [mul_neg,← hclass]; ring
  rw [hq] at hs
  simpa only [mul_neg, sub_eq_add_neg] using hs

/-- Once a signed inverse leaves minus one its magnitude never returns to
one. This one-edge form also allows arbitrarily large legal exponents. -/
theorem signed_parent_gt_one (e : ℕ) (x y : ℤ) (he : 0<e) (hx : 1<x)
    (row : 3*y=2^e*x+1) : 1<y := by
  have hp : (2:ℤ)^1 ≤ 2^e :=
    pow_le_pow_right₀ (by decide : (1:ℤ)≤2) he
  have hpx : (2:ℤ)*x ≤ 2^e*x :=
    mul_le_mul_of_nonneg_right (by simpa using hp) (by omega)
  omega

/-- If the very first inverse exponent differs from the fixed-point edge,
the first signed magnitude is strictly greater than one. -/
theorem first_fresh_parent (e : ℕ) (y : ℤ) (he : 0<e) (fresh : e≠1)
    (row : 3*y=2^e+1) : 1<y := by
  have hpe : (2:ℤ)^2 ≤ 2^e :=
    pow_le_pow_right₀ (by decide : (1:ℤ)≤2) (by omega)
  norm_num at hpe
  omega

#print axioms endpoint_unique
#print axioms shift_path
#print axioms at_signed_fixed_point
#print axioms signed_parent_gt_one
#print axioms first_fresh_parent
end Collatz.FreshAscentShadow

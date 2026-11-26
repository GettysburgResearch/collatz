import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Exact real second directional derivatives of the three-arm potential,
and the negative covariance contraction used on deep blocks. -/
namespace CollatzSlopeOccupation

noncomputable section

/-- The sorted-gap potential on the positive-spread region. -/
def barrier (γ u v : ℝ) : ℝ := u*v*(u+v)^γ

private def linear (a b t : ℝ) : ℝ := a+b*t
private def poly (a b c t : ℝ) : ℝ := a+b*t+c*t^2
private def prodLine (a b c w d γ t : ℝ) : ℝ := poly a b c t*(linear w d t)^γ
private def prodSlope (a b c w d γ t : ℝ) : ℝ :=
  linear b (2*c) t*(linear w d t)^γ
    + poly a b c t * (d*γ) * (linear w d t)^(γ-1)

private lemma lin_deriv (a b t : ℝ) : HasDerivAt (linear a b) b t := by
  exact (((hasDerivAt_id t).const_mul b).const_add a).congr_deriv (mul_one _)

private lemma poly_deriv (a b c t : ℝ) :
    HasDerivAt (poly a b c) (linear b (2*c) t) t := by
  have h := (lin_deriv a b t).add (((hasDerivAt_id t).pow 2).const_mul c)
  apply h.congr_deriv
  simp [linear]
  ring

private lemma first_prod (a b c w d γ t : ℝ) (hw : linear w d t ≠ 0) :
    HasDerivAt (prodLine a b c w d γ) (prodSlope a b c w d γ t) t := by
  have h := (poly_deriv a b c t).mul ((lin_deriv w d t).rpow_const (p := γ) (Or.inl hw))
  apply h.congr_deriv
  unfold prodSlope
  ring

private lemma slope_zero (a b c w d γ : ℝ) (hw : 0<w) :
    HasDerivAt (prodSlope a b c w d γ)
      (2*c*w^γ + 2*b*d*γ*w^(γ-1) + a*d^2*γ*(γ-1)*w^(γ-2)) 0 := by
  have h0 : linear w d 0 ≠ 0 := by simpa [linear] using hw.ne'
  have h₁ := (lin_deriv b (2*c) 0).mul
    ((lin_deriv w d 0).rpow_const (p := γ) (Or.inl h0))
  have h₂ := ((poly_deriv a b c 0).mul_const (d*γ)).mul
    ((lin_deriv w d 0).rpow_const (p := γ-1) (Or.inl h0))
  have h := h₁.add h₂
  apply h.congr_deriv
  simp [linear, poly, show γ-1-1=γ-2 by ring]
  ring

private lemma prod_second (a b c w d γ : ℝ) (hw : 0<w) :
    deriv (deriv (prodLine a b c w d γ)) 0 =
      2*c*w^γ + 2*b*d*γ*w^(γ-1) + a*d^2*γ*(γ-1)*w^(γ-2) := by
  have hpos : 0 < linear w d 0 := by simpa [linear] using hw
  have heq : deriv (prodLine a b c w d γ) =ᶠ[nhds 0] prodSlope a b c w d γ := by
    filter_upwards [((lin_deriv w d 0).continuousAt.eventually (Ioi_mem_nhds hpos))] with x hx
    exact (first_prod a b c w d γ x hx.ne').deriv
  rw [heq.deriv_eq]
  exact (slope_zero a b c w d γ hw).deriv

/-- The true second derivative at zero along any affine line in gap space. -/
theorem barrier_line_second (γ u v a b : ℝ) (hw : 0<u+v) :
    deriv (deriv (fun t : ℝ => barrier γ (u+a*t) (v+b*t))) 0 =
      2*(a*b)*(u+v)^γ
      + 2*(a*v+b*u)*(a+b)*γ*(u+v)^(γ-1)
      + (u*v)*(a+b)^2*γ*(γ-1)*(u+v)^(γ-2) := by
  have h : (fun t : ℝ => barrier γ (u+a*t) (v+b*t)) =
      prodLine (u*v) (a*v+b*u) (a*b) (u+v) (a+b) γ := by
    funext t
    unfold barrier prodLine poly linear
    congr 1
    · ring
    · congr 1
      ring
  rw [h]
  exact prod_second _ _ _ _ _ _ hw

/-- One eighth of the sum of second derivatives in the three distinct
nonzero directions, the half-Hessian contraction for covariance with
diagonal 1/2 and off-diagonal -1/4. -/
def curvature (γ u v : ℝ) : ℝ :=
  (deriv (deriv (fun t : ℝ => barrier γ (u+1*t) (v+0*t))) 0
    + deriv (deriv (fun t : ℝ => barrier γ (u+0*t) (v+1*t))) 0
    + deriv (deriv (fun t : ℝ => barrier γ (u+1*t) (v+(-1)*t))) 0)/8

theorem curvature_eq (γ u v : ℝ) (hw : 0<u+v) :
    curvature γ u v = (γ-1)/4 * ((u+v)^γ+γ*u*v*(u+v)^(γ-2)) := by
  unfold curvature
  rw [barrier_line_second _ _ _ _ _ hw, barrier_line_second _ _ _ _ _ hw,
    barrier_line_second _ _ _ _ _ hw]
  have hpow : (u+v)^(γ-1)*(u+v) = (u+v)^γ := by
    conv_rhs => rw [show γ=(γ-1)+1 by ring, Real.rpow_add hw, Real.rpow_one]
  linear_combination (norm := ring_nf) (γ/4)*hpow

/-- Uniformly negative drift coefficient at every nonnegative strictly
positive-spread profile for the open subcritical exponent range. -/
theorem curvature_le_negative (γ u v : ℝ) (hg : 0<γ) (hg' : γ<1)
    (hu : 0≤u) (hv : 0≤v) (hw : 0<u+v) :
    curvature γ u v ≤ -((1-γ)/4)*(u+v)^γ := by
  rw [curvature_eq _ _ _ hw]
  have hn : 0≤γ*u*v*(u+v)^(γ-2) :=
    mul_nonneg (mul_nonneg (mul_nonneg hg.le hu) hv) (Real.rpow_nonneg hw.le _)
  nlinarith [mul_nonpos_of_nonpos_of_nonneg (by linarith : γ-1≤0) hn]

end
end CollatzSlopeOccupation

import Mathlib.Tactic.Ring

/- Finite signed affine and divisibility implications only. The all-sublap
   crossing theorem and asymptotic gcd estimates are written mathematics. -/
namespace CollatzResearch.SublapDefects

/-- Two consecutive actual odd steps with signed endpoint defects. The four
    scale factors may be supplied as integer powers of two by the caller. -/
theorem signedDefectStep (x y x' y' h h' A B U V : ℤ)
    (hx : A*x' = 3*x+1) (hy : B*y' = 3*y+1)
    (h₀ : y = U*x+h) (h₁ : y' = V*x'+h') (hscale : B*V = U*A) :
    B*h' = 3*h+1-U := by
  calc
    B*h' = B*(V*x'+h')-(B*V)*x' := by ring
    _ = (3*y+1)-U*(A*x') := by rw [←h₁,hy,hscale]; ring
    _ = 3*h+1-U := by rw [hx,h₀]; ring

private theorem cancelTwo (k z : ℤ) (h : (2*k+1) ∣ 2*z) : (2*k+1) ∣ z := by
  obtain ⟨w,hw⟩ := h
  refine ⟨z-k*w,?_⟩
  calc
    z = (2*k+1)*z-k*(2*z) := by ring
    _ = (2*k+1)*(z-k*w) := by rw [hw]; ring

/-- An odd common divisor of the determinant and a genuine affine carry
    divides its signed defect at a nonnegative padding length. -/
theorem carryLossDividesDefect (k D C x h : ℤ) (m : ℕ)
    (hc : C=D*x+(2:ℤ)^m*h) (hd : (2*k+1) ∣ D) (hl : (2*k+1) ∣ C) :
    (2*k+1) ∣ h := by
  obtain ⟨a,ha⟩ := hd
  obtain ⟨b,hb⟩ := hl
  have hp : (2*k+1) ∣ (2:ℤ)^m*h := by
    refine ⟨b-a*x,?_⟩
    calc
      (2:ℤ)^m*h = C-D*x := by rw [hc]; ring
      _ = (2*k+1)*(b-a*x) := by rw [ha,hb]; ring
  clear hc ha hb
  induction m with
  | zero => simpa only [pow_zero,one_mul] using hp
  | succ m ih =>
    apply ih
    apply cancelTwo
    have heq : (2:ℤ)*(2^m*h)=2^(m+1)*h := by rw [pow_succ]; ring
    rwa [heq]

/-- An odd common divisor of the determinant and both actual carries divides
    the dyadic scale displacement minus one. -/
theorem commonCarryLoss (k D C C' x x' h h' B U : ℤ) (m m' : ℕ)
    (hc : C=D*x+(2:ℤ)^m*h) (hc' : C'=D*x'+(2:ℤ)^m'*h')
    (hd : (2*k+1) ∣ D) (hl : (2*k+1) ∣ C) (hl' : (2*k+1) ∣ C')
    (hstep : B*h' = 3*h+1-U) : (2*k+1) ∣ U-1 := by
  obtain ⟨r,hr⟩ := carryLossDividesDefect k D C x h m hc hd hl
  obtain ⟨s,hs⟩ := carryLossDividesDefect k D C' x' h' m' hc' hd hl'
  refine ⟨3*r-B*s,?_⟩
  calc
    U-1 = 3*h-(3*h+1-U) := by ring
    _ = (2*k+1)*(3*r-B*s) := by rw [←hstep,hr,hs]; ring

end CollatzResearch.SublapDefects

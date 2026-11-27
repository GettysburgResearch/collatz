import WindowMesh
import PhaseNet

/-! Unconditional ordinary relative-window visitors with a uniform clock budget. -/
set_option autoImplicit false
set_option warningAsError true

namespace FastWindow
open CoreBranching PeakRigidity InverseSpreading

/-- For each positive relative width the onset and visit-clock multiplier
are uniform in the ordinary target. All sources are supplied by integer paths. -/
theorem visitors (δ : ℝ) (positive : 0<δ) :
    ∃ P Q : ℝ, ∃ G : ℕ, 0<P ∧ 0<Q ∧ ∀ b : ℕ, unitOdd b → ∀ Z : ℝ, P*b≤Z →
      ∃ w m j : ℕ, 0<w ∧ w%3≠0 ∧ Z≤w ∧ (w:ℝ)<(1+δ)*Z ∧
        run m w=b ∧ grade m w=j ∧ j≤G ∧ (2:ℝ)^m*b≤Q*w := by
  let ε := min (1:ℝ) (δ/4)
  have ep : 0<ε := lt_min (by norm_num) (by positivity)
  have esmall : ε≤1 := min_le_left _ _
  have portion : ε≤δ/4 := min_le_right _ _
  have square : (1+ε)^2≤1+δ := by nlinarith [mul_nonneg ep.le (sub_nonneg.mpr esmall)]
  obtain ⟨D,mesh⟩ := PhaseNet.pow_ratio_net ε ep
  obtain ⟨N,nLarge⟩ := exists_nat_gt (8*(1+ε)/(5*ε))
  let L := N+1
  have power : (N:ℝ)≤(2:ℝ)^L := by
    have h : N≤2^L := by dsimp [L]; have h' : N+1<2^(N+1) := Nat.lt_two_pow_self; omega
    exact_mod_cast h
  have cal : 8*(1+ε)≤5*ε*(2:ℝ)^L := by
    have val := (div_lt_iff₀ (by positivity : 0<5*ε)).mp nLarge
    nlinarith [mul_le_mul_of_nonneg_left power (show 0≤5*ε by positivity)]
  refine ⟨2^(L+3+6*D),(1+ε)*3^D,D,by positivity,by positivity,?_⟩
  intro b ub Z onset
  have bp : 0<b := by have := ub.1; omega
  have Zpos : 0<Z := lt_of_lt_of_le (by positivity) onset
  obtain ⟨w,m,j,wp,wu,wl,wh,hit,gr,jb,clock⟩ :=
    visit_from_mesh ep (by dsimp [L]; omega) cal ub onset (fun u hu => by
      obtain ⟨d,k,hd,lo,hi⟩ := mesh u hu
      exact ⟨d,k,hd,lo.le,hi⟩)
  refine ⟨w,m,j,wp,wu,wl,wh.trans_le (mul_le_mul_of_nonneg_right square Zpos.le),hit,gr,jb,?_⟩
  have g : (3:ℝ)^j≤3^D := pow_le_pow_right₀ (by norm_num) jb
  exact clock.trans (mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left g (by positivity)) (by positivity))

#print axioms visitors
end FastWindow

import WindowMesh
import PhaseResidues

/-! Actual relative-window visitors with prescribed clock and grade residues. -/
set_option autoImplicit false
set_option warningAsError true

namespace FastWindow
open CoreBranching PeakRigidity InverseSpreading

/-- The ordinary visit, grade, supplied residues and near-fast time bound all
hold for the same source. The onset is uniform in the target and residues. -/
theorem visitors_residues (δ : ℝ) (positive : 0<δ)
    (M Q : ℕ) (Mp : 0<M) (Qp : 0<Q) :
    ∃ P V : ℝ, ∃ J : ℕ, 0<P ∧ 0<V ∧ ∀b : ℕ, unitOdd b →
      ∀ Z : ℝ, P*b≤Z → ∀t r : ℕ, ∃w m j : ℕ, 0<w ∧ w%3≠0 ∧ Z≤w ∧
      (w:ℝ)<(1+δ)*Z ∧ run m w=b ∧ grade m w=j ∧
      j≤J ∧ (2:ℝ)^m*b≤V*w ∧ m ≡ t [MOD M] ∧ j ≡ r [MOD Q] := by
  let ε := min (1:ℝ) (δ/4)
  have ep : 0<ε := lt_min (by norm_num) (by positivity)
  have esmall : ε≤1 := min_le_left _ _
  have portion : ε≤δ/4 := min_le_right _ _
  have square : (1+ε)^2≤1+δ := by nlinarith [mul_nonneg ep.le (sub_nonneg.mpr esmall)]
  obtain ⟨D,mesh⟩ := PhaseNet.pow_ratio_net_residues Q M Qp Mp ε ep
  obtain ⟨N,nLarge⟩ := exists_nat_gt (8*(1+ε)/(5*ε))
  let L := N+1
  have power : (N:ℝ)≤(2:ℝ)^L := by
    have h : N≤2^L := by dsimp [L]; have h' : N+1<2^(N+1) := Nat.lt_two_pow_self; omega
    exact_mod_cast h
  have cal : 8*(1+ε)≤5*ε*(2:ℝ)^L := by
    have val := (div_lt_iff₀ (by positivity : 0<5*ε)).mp nLarge
    nlinarith [mul_le_mul_of_nonneg_left power (show 0≤5*ε by positivity)]
  refine ⟨2^(L+3+6*D),(1+ε)*3^D,D,by positivity,by positivity,?_⟩
  intro b ub Z onset t r
  have bp : 0<b := by have := ub.1; omega
  have Zpos : 0<Z := lt_of_lt_of_le (by positivity) onset
  obtain ⟨w,m,j,wp,wu,wl,wh,hit,gr,jb,clock,tm,jr⟩ :=
    visit_from_mesh_with (fun d k => k ≡ t [MOD M] ∧ d ≡ r [MOD Q])
      ep (by dsimp [L]; omega) cal ub onset (fun u hu => by
        obtain ⟨d,k,hd,dr,kt,lo,hi⟩ := mesh (r%Q) (t%M)
          (Nat.mod_lt r Qp) (Nat.mod_lt t Mp) u hu
        exact ⟨d,k,hd,lo.le,hi,kt.trans (Nat.mod_modEq t M),dr.trans (Nat.mod_modEq r Q)⟩)
  refine ⟨w,m,j,wp,wu,wl,wh.trans_le (mul_le_mul_of_nonneg_right square Zpos.le),
    hit,gr,jb,?_,tm,jr⟩
  have g : (3:ℝ)^j≤3^D := pow_le_pow_right₀ (by norm_num) jb
  exact clock.trans (mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left g (by positivity)) (by positivity))

#print axioms visitors_residues
end FastWindow


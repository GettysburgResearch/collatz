import PhaseResidues

/-! The same relative phase cover when each inverse macro contributes a
fixed positive odd count. Its grade is congruent to one modulo the supplied
modulus, so every requested actual grade class remains available. -/
set_option autoImplicit false
set_option warningAsError true

namespace PhaseNet

theorem pow_ratio_net_multiples (k Q M : ℕ) (kp : 0<k) (Qp : 0<Q) (Mp : 0<M)
    (mark : k ≡ 1 [MOD Q]) (ε : ℝ) (ep : 0<ε) :
    ∃ J : ℕ, ∀r t : ℕ, ∀u : ℝ, 1≤u → ∃j m : ℕ,
      j≤J ∧ k*j ≡ r [MOD Q] ∧ m ≡ t [MOD M] ∧
      u<(2:ℝ)^m/3^(k*j) ∧ (2:ℝ)^m/3^(k*j)<(1+ε)*u := by
  obtain ⟨D,net⟩ := pow_ratio_net_residues (k*Q) M (by positivity) Mp ε ep
  refine ⟨D,?_⟩
  intro r t u hu
  have small : k*(r%Q)<k*Q := Nat.mul_lt_mul_of_pos_left (Nat.mod_lt r Qp) kp
  obtain ⟨d,m,dd,dr,mt,lo,hi⟩ := net (k*(r%Q)) (t%M) small (Nat.mod_lt t Mp) u hu
  have dz : d ≡ 0 [MOD k] :=
    (dr.of_dvd (dvd_mul_right k Q)).trans (by simp [Nat.ModEq])
  obtain ⟨j,eq⟩ := Nat.modEq_zero_iff_dvd.mp dz
  have jd : j≤d := by rw [eq]; exact Nat.le_mul_of_pos_left j kp
  have grade : d ≡ r [MOD Q] := by
    have low := dr.of_dvd (dvd_mul_left Q k)
    have rem : k*(r%Q) ≡ r [MOD Q] := by
      exact (mark.mul_right (r%Q)).trans (by simpa using (Nat.mod_modEq r Q))
    exact low.trans rem
  refine ⟨j,m,jd.trans dd,?_,mt.trans (Nat.mod_modEq t M),?_,?_⟩
  · simpa only [eq] using grade
  · simpa only [eq] using lo
  · simpa only [eq] using hi

#print axioms pow_ratio_net_multiples
end PhaseNet

module

public import Mathlib.LinearAlgebra.Matrix.Adjugate
public import Mathlib.Data.ZMod.Basic
public import Mathlib.RingTheory.Norm.Defs
public import Mathlib.RingTheory.AdjoinRoot

/-!
Full-modulus determinant certificates.  The modulus is arbitrary, so the
argument retains prime powers and does not assume a field of residues.
No cycle existence or global Collatz assertion is an assumption here.
-/

public section

namespace Collatz.NormCertificate

set_option autoImplicit false

open Matrix

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- A left null vector with one coordinate equal to one kills the determinant,
even over a commutative ring with zero divisors. -/
theorem det_eq_zero_of_normalized_left_kernel
    {R : Type*} [CommRing R] (M : Matrix ι ι R) (v : ι → R)
    (j : ι) (hv : v j = 1) (hM : v ᵥ* M = 0) : M.det = 0 := by
  have he : v ᵥ* (M * M.adjugate) = 0 := by
    rw [← vecMul_vecMul, hM, zero_vecMul]
  rw [mul_adjugate, vecMul_smul, vecMul_one] at he
  have hj := congrFun he j
  simpa [hv] using hj

/-- The entire integer modulus divides the determinant.  In particular this
applies with the complete numerical gcd as modulus. -/
theorem modulus_dvd_det
    (m : ℕ) (M : Matrix ι ι ℤ) (v : ι → ZMod m) (j : ι)
    (hv : v j = 1)
    (hM : v ᵥ* M.map (Int.castRingHom (ZMod m)) = 0) :
    (m : ℤ) ∣ M.det := by
  apply (ZMod.intCast_zmod_eq_zero_iff_dvd M.det m).mp
  rw [Int.cast_det]
  exact det_eq_zero_of_normalized_left_kernel _ v j hv hM

/-- An evaluated multiplication table supplies the normalized kernel.  Its
column identities are checked over the full composite modulus. -/
theorem modulus_dvd_multiplication_det
    (m : ℕ) (M : Matrix ι ι ℤ) (v : ι → ZMod m)
    (h : ZMod m) (j : ι) (hv : v j = 1) (hh : h = 0)
    (hcol : ∀ k, ∑ i, v i * (M i k : ZMod m) = h * v k) :
    (m : ℤ) ∣ M.det := by
  apply modulus_dvd_det m M v j hv
  ext k
  simpa [Matrix.vecMul, dotProduct, hh] using hcol k

/-- In any finite free integer algebra with a basis containing one, an
evaluation into the full residue ring sends a vanishing element's norm to zero.
This is the complete norm certificate used by the residue-defect construction. -/
theorem modulus_dvd_norm_of_evaluation
    {S : Type*} [CommRing S]
    (b : Module.Basis ι ℤ S) (j : ι) (hj : b j = 1)
    (m : ℕ) (φ : S →+* ZMod m) (z : S) (hz : φ z = 0) :
    (m : ℤ) ∣ Algebra.norm ℤ z := by
  rw [Algebra.norm_eq_matrix_det b]
  apply modulus_dvd_multiplication_det m _ (fun i => φ (b i)) (φ z) j
  · simp [hj]
  · exact hz
  · intro k
    have hr := congrArg φ (b.sum_repr (z * b k))
    simpa [Algebra.leftMulMatrix_eq_repr_mul, map_sum, map_zsmul,
      zsmul_eq_mul, mul_comm] using hr

/-- A common root modulo an arbitrary integer modulus certifies divisibility
of the whole algebraic norm in the monic quotient, with no field assumption. -/
theorem monic_quotient_norm_certificate
    (f F : Polynomial ℤ) (hf : f.Monic) (hd : 0 < f.natDegree)
    (m : ℕ) (x : ZMod m)
    (hx : f.eval₂ (Int.castRingHom (ZMod m)) x = 0)
    (hF : F.eval₂ (Int.castRingHom (ZMod m)) x = 0) :
    (m : ℤ) ∣ Algebra.norm ℤ (AdjoinRoot.mk f F) := by
  let pb := AdjoinRoot.powerBasis' hf
  let j : Fin pb.dim := ⟨0, hd⟩
  have hj : pb.basis j = 1 := by
    rw [pb.basis_eq_pow]
    exact pow_zero _
  let φ : AdjoinRoot f →+* ZMod m :=
    AdjoinRoot.lift (Int.castRingHom (ZMod m)) x hx
  apply modulus_dvd_norm_of_evaluation pb.basis j hj m φ (AdjoinRoot.mk f F)
  simpa [φ, AdjoinRoot.lift_mk] using hF

/-- A binomial annihilator transfers to a small integer congruence without
passing to a prime divisor or losing the prime-power part of the modulus. -/
theorem dyadic_relation_of_binomial
    {R : Type*} [CommRing R] (x : R) (p v : ℕ)
    (hp : x ^ p = 2) (hv : x ^ v = -1) :
    (2 : R) ^ v = (-1 : R) ^ p := by
  calc
    (2 : R) ^ v = (x ^ p) ^ v := by rw [hp]
    _ = (x ^ v) ^ p := by rw [← pow_mul, ← pow_mul, Nat.mul_comm]
    _ = (-1 : R) ^ p := by rw [hv]

theorem modulus_dvd_dyadic_relation
    (m p v : ℕ) (x : ZMod m) (hp : x ^ p = 2) (hv : x ^ v = -1) :
    (m : ℤ) ∣ (2 : ℤ) ^ v - (-1 : ℤ) ^ p := by
  apply (ZMod.intCast_zmod_eq_zero_iff_dvd _ m).mp
  push_cast
  exact sub_eq_zero.mpr (dyadic_relation_of_binomial x p v hp hv)

#print axioms det_eq_zero_of_normalized_left_kernel
#print axioms modulus_dvd_det
#print axioms modulus_dvd_multiplication_det
#print axioms modulus_dvd_norm_of_evaluation
#print axioms monic_quotient_norm_certificate
#print axioms dyadic_relation_of_binomial
#print axioms modulus_dvd_dyadic_relation

end Collatz.NormCertificate

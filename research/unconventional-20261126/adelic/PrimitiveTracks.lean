import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Rat.Lemmas
import Mathlib.Algebra.Ring.Periodic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Finite algebra for the two-track periodic rational construction. The first
    lemma combines two periodic affine forcings at their product period.  The
    denominator lemma retains both independent factors after the common factor
    is cancelled. Primality, native least period, and the real estimates are
    proved in the accompanying mathematical text. -/
namespace PrimitiveTracks

theorem periodic_sum {r t : ℕ} {u v : ℕ → ℚ} (c : ℚ)
    (hu : Function.Periodic u r) (hv : Function.Periodic v t) :
    Function.Periodic (fun j => c + u j + v j) (r * t) := by
  intro j
  have hur : Function.Periodic u (r * t) := by simpa [Nat.mul_comm] using hu.nat_mul t
  change c + u (j + r * t) + v (j + r * t) = c + u j + v j
  have hvr : Function.Periodic v (r * t) := by simpa using hv.nat_mul r
  rw [hur j, hvr j]

theorem affine_superposition {s c C : ℚ} {u v e f : ℕ → ℚ}
    (hc : c = s * c + C)
    (he : ∀ j, u (j + 1) = s * u j + e j)
    (hf : ∀ j, v (j + 1) = s * v j + f j) (j : ℕ) :
    c + u (j + 1) + v (j + 1) = s * (c + u j + v j) + (C + e j + f j) := by
  rw [he j, hf j]
  calc
    _ = (s * c + C) + (s * u j + e j) + (s * v j + f j) := by rw [← hc]
    _ = _ := by ring

theorem exact_denominator {D Z U V a b c : ℕ}
    (hU : 0 < U) (hV : 0 < V) (huv : U.Coprime V)
    (ha : a.Coprime U) (hb : b.Coprime V)
    (hcancel : D * Z = c * U * V + a * V + b * U) :
    ((Z : ℚ) / (U * V : ℕ)).den = U * V := by
  have hu : (D * Z).Coprime U := by
    rw [hcancel, show c * U * V + a * V + b * U = a * V + (c * V + b) * U by ring,
      Nat.coprime_add_mul_right_left]
    exact ha.mul_left huv.symm
  have hv : (D * Z).Coprime V := by
    rw [hcancel, show c * U * V + a * V + b * U = b * U + (c * U + a) * V by ring,
      Nat.coprime_add_mul_right_left]
    exact hb.mul_left huv
  have hZ : Z.Coprime (U * V) := (hu.mul_right hv).of_dvd_left (dvd_mul_left Z D)
  have hp : 0 < U * V := Nat.mul_pos hU hV
  have hx := Rat.den_div_eq_of_coprime (a := (Z : ℤ)) (b := (U * V : ℕ))
    (by exact_mod_cast hp) (by simpa only [Int.natAbs_natCast] using hZ)
  apply Int.ofNat_inj.mp
  simpa only [Int.cast_natCast] using hx

#print axioms periodic_sum
#print axioms affine_superposition
#print axioms exact_denominator
end PrimitiveTracks

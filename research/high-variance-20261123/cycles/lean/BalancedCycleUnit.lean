import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Tactic

/-!
The full balanced carry is a unit at any unit root satisfying the two
actual cycle power relations. The root is later constructed in ZMod D.
No cycle exclusion premise is assumed.
-/

open scoped BigOperators

namespace CollatzBalancedCycle

def carry (A p : ℕ) : ℕ :=
  ∑ i ∈ Finset.range p, 2 ^ (A * i / p) * 3 ^ (p - 1 - i)

/-- The complete balanced exponent, including both subtractions. -/
theorem balanced_exponent (A p i : ℕ) (hA : 1 ≤ A) (hi : i < p) :
    p * (A * i / p) + A * (p - 1 - i) =
      (A - 1) * (p - 1) + (p - 1 - (A * i) % p) := by
  have hp : 0 < p := by omega
  have hr := Nat.mod_lt (A * i) hp
  have hd := Nat.mod_add_div (A * i) p
  have hi' : (p - 1 - i) + i = p - 1 := by omega
  have hr' : (p - 1 - (A * i) % p) + (A * i) % p = p - 1 := by omega
  have hA' : (A - 1) + 1 = A := by omega
  nlinarith

/-- Multiplication by a coprime integer permutes the full residue interval. -/
theorem sum_mul_mod {M : Type*} [AddCommMonoid M]
    (A p : ℕ) (hp : 0 < p) (hc : A.Coprime p) (f : ℕ → M) :
    (∑ i ∈ Finset.range p, f ((A * i) % p)) =
      ∑ i ∈ Finset.range p, f i := by
  let e : Fin p → Fin p := fun i => ⟨(A * i.val) % p, Nat.mod_lt _ hp⟩
  have hinj : Function.Injective e := by
    intro i j hij
    have heq : (A * i.val) % p = (A * j.val) % p :=
      congrArg Fin.val hij
    have hmod : Nat.ModEq p i.val j.val :=
      Nat.ModEq.cancel_left_of_coprime hc.symm.gcd_eq_one heq
    apply Fin.ext
    simpa only [Nat.ModEq, Nat.mod_eq_of_lt i.isLt,
      Nat.mod_eq_of_lt j.isLt] using hmod
  have hbij : Function.Bijective e :=
    ⟨hinj, Finite.injective_iff_surjective.mp hinj⟩
  have hh := hbij.sum_comp (fun i : Fin p => f i.val)
  calc
    (∑ i ∈ Finset.range p, f ((A * i) % p)) =
        ∑ i : Fin p, f ((A * i.val) % p) :=
      (Fin.sum_univ_eq_sum_range (fun i => f ((A * i) % p)) p).symm
    _ = ∑ i : Fin p, f i.val := by simpa only [e] using hh
    _ = ∑ i ∈ Finset.range p, f i := Fin.sum_univ_eq_sum_range f p

/-- An exact ring factorization of the literal balanced Collatz carry. -/
theorem carry_factor {R : Type*} [CommRing R]
    (A p : ℕ) (hA : 1 ≤ A) (hp : 0 < p) (hc : A.Coprime p)
    (u : R) (h2 : u ^ p = 2) (h3 : u ^ A = 3) :
    (carry A p : R) =
      u ^ ((A - 1) * (p - 1)) * ∑ j ∈ Finset.range p, u ^ j := by
  have ht : ∀ i ∈ Finset.range p,
      (2 : R) ^ (A * i / p) * 3 ^ (p - 1 - i) =
        u ^ ((A - 1) * (p - 1) + (p - 1 - (A * i) % p)) := by
    intro i hi
    rw [← h2, ← h3, ← pow_mul, ← pow_mul, ← pow_add]
    rw [balanced_exponent A p i hA (Finset.mem_range.mp hi)]
  calc
    (carry A p : R) =
        ∑ i ∈ Finset.range p,
          u ^ ((A - 1) * (p - 1) + (p - 1 - (A * i) % p)) := by
      simp only [carry, Nat.cast_sum, Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat]
      exact Finset.sum_congr rfl ht
    _ = u ^ ((A - 1) * (p - 1)) *
        ∑ i ∈ Finset.range p, u ^ (p - 1 - (A * i) % p) := by
      simp_rw [pow_add]
      rw [Finset.mul_sum]
    _ = u ^ ((A - 1) * (p - 1)) *
        ∑ j ∈ Finset.range p, u ^ (p - 1 - j) := by
      rw [sum_mul_mod A p hp hc (fun j => u ^ (p - 1 - j))]
    _ = u ^ ((A - 1) * (p - 1)) *
        ∑ j ∈ Finset.range p, u ^ j := by
      rw [Finset.sum_range_reflect]

/-- The exact geometric sum is a unit, without any domain hypothesis. -/
theorem geom_sum_isUnit {R : Type*} [CommRing R]
    (u : R) (p : ℕ) (h2 : u ^ p = 2) :
    IsUnit (∑ j ∈ Finset.range p, u ^ j) := by
  apply IsUnit.of_mul_eq_one (u - 1)
  rw [geom_sum_mul, h2]
  norm_num

/-- The actual balanced carry is a unit whenever the unit cycle root exists. -/
theorem carry_isUnit_of_root {R : Type*} [CommRing R]
    (A p : ℕ) (hA : 1 ≤ A) (hp : 0 < p) (hc : A.Coprime p)
    (u : R) (hu : IsUnit u) (h2 : u ^ p = 2) (h3 : u ^ A = 3) :
    IsUnit (carry A p : R) := by
  rw [carry_factor A p hA hp hc u h2 h3]
  exact (hu.pow _).mul (geom_sum_isUnit u p h2)

/-- Bézout extraction in a commutative group, retaining both power relations. -/
theorem exists_coprime_root {G : Type*} [CommGroup G]
    (a b : G) (A p : ℕ) (hc : A.Coprime p) (h : a ^ A = b ^ p) :
    ∃ u : G, u ^ p = a ∧ u ^ A = b := by
  let r : ℤ := Nat.gcdB A p
  let s : ℤ := Nat.gcdA A p
  have hb : (A : ℤ) * s + (p : ℤ) * r = 1 := by
    simpa only [r, s, hc.gcd_eq_one, Nat.cast_one] using
      (Nat.gcd_eq_gcd_ab A p).symm
  refine ⟨a ^ r * b ^ s, ?_, ?_⟩
  · calc
      (a ^ r * b ^ s) ^ p = a ^ (r * p) * b ^ (s * p) := by
        rw [mul_pow]
        congr 1
        · simpa only [zpow_natCast] using (zpow_mul a r (p : ℤ)).symm
        · simpa only [zpow_natCast] using (zpow_mul b s (p : ℤ)).symm
      _ = a ^ (r * p) * (b ^ p) ^ s := by
        congr 1
        rw [mul_comm s (p : ℤ), zpow_mul, zpow_natCast]
      _ = a ^ (r * p) * (a ^ A) ^ s := by rw [← h]
      _ = a ^ (r * p + A * s) := by
        rw [← zpow_natCast a A, ← zpow_mul, ← zpow_add]
      _ = a := by rw [show r * (p : ℤ) + A * s = 1 by nlinarith [hb], zpow_one]
  · calc
      (a ^ r * b ^ s) ^ A = a ^ (r * A) * b ^ (s * A) := by
        rw [mul_pow]
        congr 1
        · simpa only [zpow_natCast] using (zpow_mul a r (A : ℤ)).symm
        · simpa only [zpow_natCast] using (zpow_mul b s (A : ℤ)).symm
      _ = (a ^ A) ^ r * b ^ (s * A) := by
        congr 1
        rw [mul_comm r (A : ℤ), zpow_mul, zpow_natCast]
      _ = (b ^ p) ^ r * b ^ (s * A) := by rw [h]
      _ = b ^ (p * r + s * A) := by
        rw [← zpow_natCast b p, ← zpow_mul, ← zpow_add]
      _ = b := by rw [show (p : ℤ) * r + s * A = 1 by nlinarith [hb], zpow_one]

/-- The literal balanced carry is coprime to the entire actual cycle denominator. -/
theorem balanced_carry_coprime (A p : ℕ) (hA : 1 ≤ A) (hp : 0 < p)
    (hc : A.Coprime p) (hcone : 3 ^ p < 2 ^ A) :
    (carry A p).Coprime (2 ^ A - 3 ^ p) := by
  let D := 2 ^ A - 3 ^ p
  have hle : 3 ^ p ≤ 2 ^ A := Nat.le_of_lt hcone
  have h23 : (2 ^ A).Coprime (3 ^ p) :=
    Nat.Coprime.pow A p (by decide : Nat.Coprime 2 3)
  have h2D : Nat.Coprime 2 D :=
    (Nat.coprime_pow_left_iff (by omega : 0 < A) 2 D).mp
      ((Nat.coprime_self_sub_right hle).mpr h23)
  have h3D : Nat.Coprime 3 D :=
    (Nat.coprime_pow_left_iff hp 3 D).mp
      ((Nat.coprime_sub_self_right hle).mpr h23.symm)
  let a : (ZMod D)ˣ := ZMod.unitOfCoprime 2 h2D
  let b : (ZMod D)ˣ := ZMod.unitOfCoprime 3 h3D
  have hab : a ^ A = b ^ p := by
    apply Units.ext
    have hz : ((2 ^ A - 3 ^ p : ℕ) : ZMod D) = 0 := ZMod.natCast_self D
    rw [Nat.cast_sub hle] at hz
    have hrel := sub_eq_zero.mp hz
    simpa only [a, b, Units.val_pow_eq_pow_val, ZMod.coe_unitOfCoprime,
      Nat.cast_pow, Nat.cast_ofNat] using hrel
  obtain ⟨u, hu2, hu3⟩ := exists_coprime_root a b A p hc hab
  have hu2' : (u : ZMod D) ^ p = 2 := by
    simpa only [Units.val_pow_eq_pow_val, a, ZMod.coe_unitOfCoprime,
      Nat.cast_ofNat] using congrArg (fun v : (ZMod D)ˣ => (v : ZMod D)) hu2
  have hu3' : (u : ZMod D) ^ A = 3 := by
    simpa only [Units.val_pow_eq_pow_val, b, ZMod.coe_unitOfCoprime,
      Nat.cast_ofNat] using congrArg (fun v : (ZMod D)ˣ => (v : ZMod D)) hu3
  exact (ZMod.isUnit_iff_coprime (carry A p) D).mp
    (carry_isUnit_of_root A p hA hp hc (u : ZMod D) u.isUnit hu2' hu3')

/-- A nontrivial full denominator cannot divide this actual balanced carry. -/
theorem balanced_denominator_not_dvd (A p : ℕ) (hA : 1 ≤ A) (hp : 0 < p)
    (hc : A.Coprime p) (hcone : 3 ^ p < 2 ^ A)
    (hD : 1 < 2 ^ A - 3 ^ p) :
    ¬ (2 ^ A - 3 ^ p) ∣ carry A p := by
  intro hd
  have hcop := balanced_carry_coprime A p hA hp hc hcone
  have hdiv : (2 ^ A - 3 ^ p) ∣ 1 := by
    rw [← hcop.gcd_eq_one]
    exact Nat.dvd_gcd hd (dvd_refl _)
  have hle := Nat.le_of_dvd (by decide : 0 < 1) hdiv
  omega

end CollatzBalancedCycle

import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Linarith

/-! Exact finite arithmetic behind a pair of opposite adjacent swaps. -/
namespace CollatzResearch.SwapArithmetic

private theorem powers_of_divisibility {t b G : ℕ} (hbt : b ≤ t)
    (ht : t.Coprime G) (hb : b.Coprime G) (k : ℕ)
    (h : G ∣ t ^ k - b ^ k) :
    (ZMod.unitOfCoprime t ht) ^ k = (ZMod.unitOfCoprime b hb) ^ k := by
  apply Units.ext
  have hcast := (ZMod.natCast_eq_natCast_iff (t ^ k) (b ^ k) G).2
    ((Nat.modEq_iff_dvd' (Nat.pow_le_pow_left hbt k)).2 h).symm
  simpa using hcast

/-- Two modular power equalities imply equality at the gcd exponent. -/
theorem cancelled_dvd_root {t b G M l : ℕ} (hbt : b ≤ t)
    (ht : t.Coprime G) (hb : b.Coprime G)
    (hM : G ∣ t ^ M - b ^ M) (hl : G ∣ t ^ l - b ^ l) :
    G ∣ t ^ M.gcd l - b ^ M.gcd l := by
  let x := ZMod.unitOfCoprime t ht
  let y := ZMod.unitOfCoprime b hb
  have hpM : (x / y) ^ M = 1 := by
    rw [div_pow, div_eq_one]
    exact powers_of_divisibility hbt ht hb M hM
  have hpl : (x / y) ^ l = 1 := by
    rw [div_pow, div_eq_one]
    exact powers_of_divisibility hbt ht hb l hl
  have hpg : (x / y) ^ M.gcd l = 1 :=
    orderOf_dvd_iff_pow_eq_one.mp
      (Nat.dvd_gcd (orderOf_dvd_iff_pow_eq_one.mpr hpM)
        (orderOf_dvd_iff_pow_eq_one.mpr hpl))
  rw [div_pow, div_eq_one] at hpg
  have hcast := congrArg (fun z : (ZMod G)ˣ => (z : ZMod G)) hpg
  have hmod : (t ^ M.gcd l : ℕ) ≡ b ^ M.gcd l [MOD G] := by
    apply (ZMod.natCast_eq_natCast_iff _ _ _).mp
    simpa [x, y] using hcast
  exact (Nat.modEq_iff_dvd' (Nat.pow_le_pow_left hbt _)).mp hmod.symm

/-- The entire geometric quotient survives cancellation by G. -/
theorem opposite_factor {t b G M l : ℕ} (hbt : b ≤ t)
    (ht : t.Coprime G) (hb : b.Coprime G)
    (hM : G ∣ t ^ M - b ^ M) (hl : G ∣ t ^ l - b ^ l) :
    (t ^ M - b ^ M) / (t ^ M.gcd l - b ^ M.gcd l) ∣
      (t ^ M - b ^ M) / G := by
  exact Nat.div_dvd_div_left
    (Nat.pow_sub_pow_dvd_pow_sub_pow t b (Nat.gcd_dvd_left M l))
    (cancelled_dvd_root hbt ht hb hM hl)

/-- A proper positive root exponent leaves a quotient strictly larger than its leading term. -/
theorem leading_lt_quotient {t b M r : ℕ} (hb : 0 < b) (hbt : b < t)
    (hr : 0 < r) (hrM : r < M) (hd : r ∣ M) :
    t ^ (M - r) < (t ^ M - b ^ M) / (t ^ r - b ^ r) := by
  have hot : b ^ r < t ^ r := Nat.pow_lt_pow_left hbt (by omega)
  have hrem : b ^ (M - r) < t ^ (M - r) := Nat.pow_lt_pow_left hbt (by omega)
  have hbr : 0 < b ^ r := Nat.pow_pos hb
  have hless := Nat.mul_lt_mul_of_pos_right hrem hbr
  have hterm : t ^ (M - r) * (t ^ r - b ^ r) < t ^ M - b ^ M := by
    have htM : t ^ M = t ^ (M-r) * t ^ r := by
      rw [← pow_add, Nat.sub_add_cancel hrM.le]
    have hbM : b ^ M = b ^ (M-r) * b ^ r := by
      rw [← pow_add, Nat.sub_add_cancel hrM.le]
    have hle := Nat.pow_le_pow_left hbt.le M
    have h := Nat.sub_add_cancel hot.le
    have h' := Nat.sub_add_cancel hle
    rw [htM, hbM] at h'
    rw [htM, hbM]
    nlinarith
  have hdvd := Nat.pow_sub_pow_dvd_pow_sub_pow t b hd
  rw [← Nat.div_mul_cancel hdvd] at hterm
  exact Nat.lt_of_mul_lt_mul_right hterm

/-- The reduced denominator from the opposite-direction data exceeds t to the complementary power. -/
theorem opposite_growth {t b G M l : ℕ} (hbpos : 0 < b) (hbt : b < t)
    (ht : t.Coprime G) (hb : b.Coprime G) (hlpos : 0 < l) (hlM : l < M)
    (hM : G ∣ t ^ M - b ^ M) (hl : G ∣ t ^ l - b ^ l) :
    t ^ (M - M.gcd l) < (t ^ M - b ^ M) / G := by
  have hgpos : 0 < M.gcd l := Nat.gcd_pos_of_pos_right M hlpos
  have hgl : M.gcd l ≤ l := Nat.le_of_dvd hlpos (Nat.gcd_dvd_right M l)
  have hlead := leading_lt_quotient hbpos hbt hgpos (lt_of_le_of_lt hgl hlM)
    (Nat.gcd_dvd_left M l)
  have hraw : 0 < t ^ M - b ^ M :=
    Nat.sub_pos_of_lt (Nat.pow_lt_pow_left hbt (by omega))
  have hden : 0 < (t ^ M - b ^ M) / G := Nat.div_pos (Nat.le_of_dvd hraw hM)
    (Nat.pos_of_dvd_of_pos hM hraw)
  exact lt_of_lt_of_le hlead (Nat.le_of_dvd hden (opposite_factor hbt.le ht hb hM hl))

#print axioms cancelled_dvd_root
#print axioms opposite_factor
#print axioms leading_lt_quotient
#print axioms opposite_growth

end CollatzResearch.SwapArithmetic

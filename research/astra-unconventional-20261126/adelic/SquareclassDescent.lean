import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! A squareclass dependence at every accelerated growth triple forces an actual hit of 1. -/

namespace Collatz.SquareclassDescent

set_option autoImplicit false

/-- The exponent and physical odd map agree with the project's `ActualScalar` convention. -/
def clock (x : ℕ) : ℕ := (3 * x + 1).factorization 2
def next (x : ℕ) : ℕ := (3 * x + 1) / 2 ^ clock x

theorem physical (x : ℕ) : 2 ^ clock x * next x = 3 * x + 1 :=
  Nat.ordProj_mul_ordCompl_eq_self _ _

theorem next_odd (x : ℕ) : Odd (next x) :=
  Nat.odd_iff.mpr (Nat.two_dvd_ne_zero.mp (Nat.not_dvd_ordCompl Nat.prime_two (by omega)))

theorem clock_pos {x : ℕ} (h : Odd x) : 1 ≤ clock x := by
  have hx := Nat.odd_iff.mp h
  exact (Nat.prime_two.dvd_iff_one_le_factorization (by omega)).mp (by omega)

/-- Nonempty products in the three physical positive integer squareclasses. -/
def Dependent (x y z : ℕ) : Prop :=
  IsSquare x ∨ IsSquare y ∨ IsSquare z ∨ IsSquare (x * y) ∨
  IsSquare (x * z) ∨ IsSquare (y * z) ∨ IsSquare (x * y * z)

private theorem not_square_mod4 {x : ℕ} (h : x % 4 = 3) : ¬IsSquare x := by
  rintro ⟨k, rfl⟩
  have hc : ∀ i : Fin 4, (i.val * i.val) % 4 ≠ 3 := by decide
  exact hc ⟨k % 4, Nat.mod_lt _ (by decide)⟩ ((Nat.mul_mod k k 4).symm.trans h)

private theorem not_square_mod3 {x : ℕ} (h : x % 3 = 2) : ¬IsSquare x := by
  rintro ⟨k, rfl⟩
  have hc : ∀ i : Fin 3, (i.val * i.val) % 3 ≠ 2 := by decide
  exact hc ⟨k % 3, Nat.mod_lt _ (by decide)⟩ ((Nat.mul_mod k k 3).symm.trans h)

private theorem odd_square_mod8 {x : ℕ} (ho : Odd x) (h : IsSquare x) : x % 8 = 1 := by
  rcases h with ⟨k, rfl⟩
  have hc : ∀ i : Fin 8, i.val * i.val % 8 = 0 ∨ i.val * i.val % 8 = 1 ∨
      i.val * i.val % 8 = 4 := by decide
  have he := hc ⟨k % 8, Nat.mod_lt _ (by decide)⟩
  change _ ∨ _ ∨ _ at he
  simp only [← Nat.mul_mod] at he
  have hp := Nat.odd_iff.mp ho
  omega

private theorem edge_coprime {x y a : ℕ} (he : 2 ^ a * y = 3 * x + 1) : x.Coprime y := by
  have h : x.Coprime (3 * x + 1) := (Nat.coprime_mul_right_add_right x 1 3).2 (by simp)
  rw [← he] at h
  exact h.of_dvd_right (dvd_mul_left _ _)

private theorem even_left_at {a b p : ℕ} (ha : a ≠ 0) (hb : b ≠ 0) (hp : p.Prime)
    (h : IsSquare (a * b)) (hcommon : ¬(p ∣ a ∧ p ∣ b)) : Even (a.factorization p) := by
  by_cases hpa : p ∣ a
  · have hpb : ¬p ∣ b := fun hd => hcommon ⟨hpa, hd⟩
    have he := Nat.isSquare_iff_even_factorization.mp h p hp
    simpa [Nat.factorization_mul ha hb, Nat.factorization_eq_zero_of_not_dvd hpb] using he
  · simp [Nat.factorization_eq_zero_of_not_dvd hpa]

private theorem square_left {a b : ℕ} (ha : a ≠ 0) (hb : b ≠ 0) (hc : a.Coprime b)
    (hs : IsSquare (a * b)) : IsSquare a := by
  apply Nat.isSquare_iff_even_factorization.mpr
  intro p hp
  apply even_left_at ha hb hp hs
  rintro ⟨h1, h2⟩
  exact hp.not_dvd_one (hc ▸ Nat.dvd_gcd h1 h2)

/-- The coefficient 5 arises from the first two odd departures, even when the second clock is large. -/
theorem growth_carry {x y z b : ℕ} (hxy : 2 * y = 3 * x + 1)
    (hyz : 2 ^ b * z = 3 * y + 1) : 2 * (2 ^ b * z) = 9 * x + 5 := by omega

private theorem not_square_outer {x y z b : ℕ} (hx : x % 4 = 3) (hz : z ≠ 0)
    (hxy : 2 * y = 3 * x + 1) (hyz : 2 ^ b * z = 3 * y + 1) : ¬IsSquare (x * z) := by
  intro hsq
  have hrest (p : ℕ) (hp : p.Prime) (hne : p ≠ 5) : Even (x.factorization p) := by
    apply even_left_at (by omega) hz hp hsq
    rintro ⟨hdx, hdz⟩
    have hd : p ∣ 9 * x + 5 := by
      rw [← growth_carry hxy hyz]
      exact dvd_mul_of_dvd_right (dvd_mul_of_dvd_right hdz _) _
    have hd5 : p ∣ 5 := (Nat.dvd_add_iff_right (dvd_mul_of_dvd_right hdx 9)).mpr hd
    exact hne ((Nat.prime_dvd_prime_iff_eq hp (by decide : Nat.Prime 5)).mp hd5)
  by_cases h5 : Even (x.factorization 5)
  · apply not_square_mod4 hx
    exact Nat.isSquare_iff_even_factorization.mpr (fun p hp => by
      by_cases he : p = 5
      · simpa [he] using h5
      · exact hrest p hp he)
  · have h5x : IsSquare (5 * x) := by
      apply Nat.isSquare_iff_even_factorization.mpr
      intro p hp
      rw [Nat.factorization_mul (by decide) (by omega)]
      by_cases he : p = 5
      · subst p
        simp only [Finsupp.add_apply, Nat.Prime.factorization_self (by decide : Nat.Prime 5)]
        rw [Nat.even_iff] at h5 ⊢
        omega
      · have hnd : ¬p ∣ 5 := fun hd => he ((Nat.prime_dvd_prime_iff_eq hp (by decide)).mp hd)
        simpa [Nat.factorization_eq_zero_of_not_dvd hnd] using hrest p hp he
    exact not_square_mod4 (show 5 * x % 4 = 3 by omega) h5x

/-- At a growth transition a dependence in the three consecutive physical squareclasses forces
an actual integer square at the third odd node. -/
theorem square_after_growth {x y z b : ℕ} (hyo : Odd y) (hzo : Odd z)
    (hxy : 2 * y = 3 * x + 1) (hyz : 2 ^ b * z = 3 * y + 1)
    (hdep : Dependent x y z) : IsSquare z := by
  have hoy := Nat.odd_iff.mp hyo
  have hoz := Nat.odd_iff.mp hzo
  have hx : x % 4 = 3 := by omega
  have hy : ¬IsSquare y := not_square_mod3 (by omega)
  have cxy : x.Coprime y := edge_coprime (a := 1) (by simpa using hxy)
  have cyz := edge_coprime hyz
  rcases hdep with h | h | h | h | h | h | h
  · exact False.elim (not_square_mod4 hx h)
  · exact False.elim (hy h)
  · exact h
  · exact False.elim (not_square_mod4 hx (square_left (by omega) (by omega) cxy h))
  · exact False.elim (not_square_outer hx (by omega) hxy hyz h)
  · exact False.elim (hy (square_left (by omega) (by omega) cyz h))
  · have hs : IsSquare (y * (x * z)) := by simpa only [mul_left_comm, mul_assoc] using h
    exact False.elim (hy (square_left (by omega) (Nat.mul_ne_zero (by omega) (by omega))
      (cxy.symm.mul_right cyz) hs))

/-- Either the first step decreases, or the next three odd steps together decrease. -/
theorem local_descent {x : ℕ} (ho : Odd x) (hx : 5 ≤ x)
    (hd : clock x = 1 → Dependent x (next x) (next (next x))) :
    next x < x ∨ next (next (next x)) < x := by
  let y := next x
  let z := next y
  let w := next z
  have h1 := physical x
  have h2 := physical y
  have h3 := physical z
  change 2 ^ clock x * y = _ at h1
  change 2 ^ clock y * z = _ at h2
  change 2 ^ clock z * w = _ at h3
  have hp := clock_pos ho
  by_cases hg : clock x = 1
  · right
    have he : 2 * y = 3 * x + 1 := by simpa [hg] using h1
    have hs : IsSquare z := square_after_growth (next_odd _) (next_odd _) he h2 (hd hg)
    have hn : clock y ≠ 1 := by
      intro h
      rw [h, pow_one] at h2
      exact not_square_mod3 (by omega) hs
    have hpy : 1 ≤ clock y := clock_pos (next_odd x)
    have hge : 4 ≤ 2 ^ clock y := (Nat.pow_le_pow_right (by decide : 0 < 2) (show 2 ≤ clock y by omega))
    have hge2 : 4 * z ≤ 3 * y + 1 := h2 ▸ Nat.mul_le_mul_right z hge
    have hz8 := odd_square_mod8 (next_odd y) hs
    have hgz : 2 ≤ clock z := (Nat.prime_two.pow_dvd_iff_le_factorization (by omega)).mp
      (show 2 ^ 2 ∣ 3 * z + 1 by omega)
    have hge3 : 4 * w ≤ 3 * z + 1 := h3 ▸ Nat.mul_le_mul_right w (Nat.pow_le_pow_right (by decide : 0 < 2) hgz)
    change w < x
    omega
  · left
    have hge : 4 ≤ 2 ^ clock x := Nat.pow_le_pow_right (by decide : 0 < 2) (by omega : 2 ≤ clock x)
    have hbound : 4 * y ≤ 3 * x + 1 := h1 ▸ Nat.mul_le_mul_right y hge
    change y < x
    omega

/-- A local, checked consumer on the actual odd map. Local dependence can vary from step to step. -/
theorem reaches_one_of_dependent_growth {x : ℕ} (ho : Odd x)
    (hd : ∀ i : ℕ, let v := next^[i] x; clock v = 1 → Dependent v (next v) (next (next v))) :
    ∃ j : ℕ, next^[j] x = 1 := by
  induction x using Nat.strong_induction_on with
  | h x ih =>
    by_cases hx : 5 ≤ x
    · have strict := local_descent ho hx (hd 0)
      have step (k : ℕ) (hk : Odd (next^[k] x)) (hl : next^[k] x < x) :
          ∃ j : ℕ, next^[j] x = 1 := by
        have htail (i : ℕ) := hd (i + k)
        simp only [Function.iterate_add_apply] at htail
        obtain ⟨j, hj⟩ := ih _ hl hk htail
        exact ⟨j + k, by simpa only [Function.iterate_add_apply] using hj⟩
      rcases strict with h | h
      · exact step 1 (next_odd x) h
      · exact step 3 (next_odd _) h
    · have hmod := Nat.odd_iff.mp ho
      have hs : x = 1 ∨ x = 3 := by omega
      rcases hs with rfl | rfl
      · exact ⟨0, rfl⟩
      · have hc3 : clock 3 = 1 := by
          change (2 * 5).factorization 2 = 1
          rw [Nat.factorization_mul (by decide) (by decide)]
          simp [Nat.Prime.factorization_self Nat.prime_two,
            Nat.factorization_eq_zero_of_not_dvd (by decide : ¬2 ∣ 5)]
        have hc5 : clock 5 = 4 := by
          change (2 ^ 4).factorization 2 = 4
          rw [Nat.prime_two.factorization_pow]
          norm_num
        have h3 : next 3 = 5 := by norm_num [next, hc3]
        have h5 : next 5 = 1 := by norm_num [next, hc5]
        exact ⟨2, show next (next 3) = 1 by rw [h3, h5]⟩

/-- The quadratic characters of conductor 4 and 8, on the odd inputs used below. -/
def minusOneCharacter (x : ℕ) : ℤ := if x % 4 = 1 then 1 else -1
def twoCharacter (x : ℕ) : ℤ := if x % 8 = 1 ∨ x % 8 = 7 then 1 else -1

def dyadicScore (x : ℕ) : ℤ :=
  7 + 3 * minusOneCharacter x - twoCharacter x - minusOneCharacter x * twoCharacter x

/-- The three named dyadic characters give the exact lower clock truncated at three,
scaled by four. This bound uses the actual 2-adic valuation of the numerator. -/
theorem dyadic_clock (x : ℕ) (ho : Odd x) : dyadicScore x ≤ 4 * (clock x : ℤ) := by
  have hm := Nat.odd_iff.mp ho
  have hp := clock_pos ho
  have h : x % 8 = 1 ∨ x % 8 = 3 ∨ x % 8 = 5 ∨ x % 8 = 7 := by omega
  rcases h with h | h | h | h
  · have h4 : x % 4 = 1 := by omega
    have hg : 2 ≤ clock x := (Nat.prime_two.pow_dvd_iff_le_factorization (by omega)).mp
      (show 2 ^ 2 ∣ 3 * x + 1 by omega)
    simp [dyadicScore, minusOneCharacter, twoCharacter, h4, h]
    omega
  · have h4 : x % 4 ≠ 1 := by omega
    simp [dyadicScore, minusOneCharacter, twoCharacter, h4, h]
    omega
  · have h4 : x % 4 = 1 := by omega
    have hg : 3 ≤ clock x := (Nat.prime_two.pow_dvd_iff_le_factorization (by omega)).mp
      (show 2 ^ 3 ∣ 3 * x + 1 by omega)
    simp [dyadicScore, minusOneCharacter, twoCharacter, h4, h]
    omega
  · have h4 : x % 4 ≠ 1 := by omega
    simp [dyadicScore, minusOneCharacter, twoCharacter, h4, h]
    omega

/-- Cumulative character score on a fixed physical accelerated orbit. -/
theorem dyadic_prefix (x N : ℕ) (ho : Odd x) :
    (∑ i ∈ Finset.range N, dyadicScore (next^[i] x)) ≤
      4 * ∑ i ∈ Finset.range N, (clock (next^[i] x) : ℤ) := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i _
  apply dyadic_clock
  cases i with
  | zero => exact ho
  | succ i => rw [Function.iterate_succ_apply']; exact next_odd _

#print axioms physical
#print axioms next_odd
#print axioms clock_pos
#print axioms growth_carry
#print axioms square_after_growth
#print axioms local_descent
#print axioms reaches_one_of_dependent_growth
#print axioms dyadic_clock
#print axioms dyadic_prefix

end Collatz.SquareclassDescent

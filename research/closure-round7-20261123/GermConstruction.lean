import Mathlib.Tactic
import Mathlib.Data.Rat.Lemmas

/-!
# Integer clearing for the actual Taylor transport

The coefficient equations of `(2+t) B = 3^e A - e` are triangular.
This file proves that ordinary binary integrality removes the apparent
powers of two from division by `2+t`, while each odd step removes one
power of three from a common denominator, until that exponent is zero.

The rational coefficients and binary-integral actual tail are explicit
inputs. No rational Taylor germ is constructed for an arbitrary orbit.
-/

namespace Collatz.ClosureRoundSeven.GermConstruction

set_option autoImplicit false

def BinaryIntegral (q : ℚ) : Prop := q.den.Coprime 2

def Integral (q : ℚ) : Prop := ∃ z : ℤ, q = z

def Cleared (s r : ℕ) (a : ℕ → ℚ) : Prop :=
  ∀ j ≤ r, Integral ((3 : ℚ) ^ s * a j)

private theorem integral_sub {a b : ℚ} (ha : Integral a) (hb : Integral b) :
    Integral (a - b) := by
  obtain ⟨u, rfl⟩ := ha
  obtain ⟨v, rfl⟩ := hb
  exact ⟨u - v, by norm_cast⟩

private theorem integral_mul {a b : ℚ} (ha : Integral a) (hb : Integral b) :
    Integral (a * b) := by
  obtain ⟨u, rfl⟩ := ha
  obtain ⟨v, rfl⟩ := hb
  exact ⟨u * v, by norm_cast⟩

private theorem integral_three_pow (s : ℕ) : Integral ((3 : ℚ) ^ s) :=
  ⟨(3 : ℤ) ^ s, by norm_cast⟩

/-- Multiplication by an ordinary integer cannot introduce a binary denominator. -/
theorem binaryIntegral_int_mul (z : ℤ) {q : ℚ} (hq : BinaryIntegral q) :
    BinaryIntegral ((z : ℚ) * q) := by
  unfold BinaryIntegral at *
  have hd := Rat.mul_den_dvd (z : ℚ) q
  simp only [Rat.den_intCast, one_mul] at hd
  exact hq.of_dvd_left hd

/-- A binary-integral rational whose double is an integer is itself an integer. -/
theorem integral_of_double {q : ℚ} (hq : BinaryIntegral q)
    (hdouble : Integral (2 * q)) : Integral q := by
  obtain ⟨z, hz⟩ := hdouble
  have hqeq : q = (z : ℚ) / 2 := by linarith
  have hd : (q.den : ℤ) ∣ (2 : ℤ) := by
    rw [hqeq, show (2 : ℚ) = ((2 : ℤ) : ℚ) by norm_num,
      Rat.intCast_div_eq_divInt]
    exact Rat.den_dvd z 2
  have hdn : q.den ∣ 2 := by exact_mod_cast hd
  have hone : q.den = 1 := by
    exact Nat.eq_one_of_dvd_coprimes hq (dvd_refl _) hdn
  exact ⟨q.num, (Rat.coe_int_num_of_den_eq_one hone).symm⟩

private theorem binaryIntegral_three_pow_mul (s : ℕ) {q : ℚ}
    (hq : BinaryIntegral q) : BinaryIntegral ((3 : ℚ) ^ s * q) := by
  simpa using binaryIntegral_int_mul ((3 : ℤ) ^ s) hq

/-- Triangular division by `2+t` preserves ordinary integrality when the
actual output coefficients are binary integral. -/
theorem triangular_integrality (r : ℕ) (a b : ℕ → ℚ)
    (ha : ∀ j ≤ r, Integral (a j))
    (hb : ∀ j ≤ r, BinaryIntegral (b j))
    (hzero : 2 * b 0 = a 0)
    (hnext : ∀ j, j + 1 ≤ r → 2 * b (j + 1) = a (j + 1) - b j) :
    ∀ j ≤ r, Integral (b j) := by
  intro j hj
  induction j with
  | zero => exact integral_of_double (hb 0 hj) (hzero ▸ ha 0 hj)
  | succ j ih =>
    apply integral_of_double (hb (j + 1) hj)
    rw [hnext j hj]
    exact integral_sub (ha (j + 1) hj) (ih (by omega))

/-- An even shortcut step retains a common ternary denominator for the
complete finite Taylor jet, not just its constant coefficient. -/
theorem even_step_cleared (s r : ℕ) (a b : ℕ → ℚ)
    (ha : Cleared s r a)
    (hb : ∀ j ≤ r, BinaryIntegral (b j))
    (hzero : 2 * b 0 = a 0)
    (hnext : ∀ j, j + 1 ≤ r → 2 * b (j + 1) = a (j + 1) - b j) :
    Cleared s r b := by
  apply triangular_integrality r (fun j => (3 : ℚ) ^ s * a j)
    (fun j => (3 : ℚ) ^ s * b j) ha
  · intro j hj
    exact binaryIntegral_three_pow_mul s (hb j hj)
  · calc
      2 * ((3 : ℚ) ^ s * b 0) = (3 : ℚ) ^ s * (2 * b 0) := by ring
      _ = (3 : ℚ) ^ s * a 0 := by rw [hzero]
  · intro j hj
    calc
      2 * ((3 : ℚ) ^ s * b (j + 1)) =
          (3 : ℚ) ^ s * (2 * b (j + 1)) := by ring
      _ = (3 : ℚ) ^ s * a (j + 1) - (3 : ℚ) ^ s * b j := by
        rw [hnext j hj]; ring

/-- An odd shortcut removes one power of three from the denominator
of every coefficient in the finite jet simultaneously. -/
theorem odd_step_cleared (s r : ℕ) (a b : ℕ → ℚ)
    (ha : Cleared (s + 1) r a)
    (hb : ∀ j ≤ r, BinaryIntegral (b j))
    (hzero : 2 * b 0 = 3 * a 0 - 1)
    (hnext : ∀ j, j + 1 ≤ r → 2 * b (j + 1) = 3 * a (j + 1) - b j) :
    Cleared s r b := by
  intro j hj
  induction j with
  | zero =>
    apply integral_of_double (binaryIntegral_three_pow_mul s (hb 0 hj))
    have h : 2 * ((3 : ℚ) ^ s * b 0) =
        (3 : ℚ) ^ (s + 1) * a 0 - (3 : ℚ) ^ s := by
      rw [pow_succ]
      calc
        2 * ((3 : ℚ) ^ s * b 0) = (3 : ℚ) ^ s * (2 * b 0) := by ring
        _ = (3 : ℚ) ^ s * 3 * a 0 - (3 : ℚ) ^ s := by rw [hzero]; ring
    rw [h]
    exact integral_sub (ha 0 hj) (integral_three_pow s)
  | succ j ih =>
    apply integral_of_double (binaryIntegral_three_pow_mul s (hb (j + 1) hj))
    have h : 2 * ((3 : ℚ) ^ s * b (j + 1)) =
        (3 : ℚ) ^ (s + 1) * a (j + 1) - (3 : ℚ) ^ s * b j := by
      rw [pow_succ]
      calc
        2 * ((3 : ℚ) ^ s * b (j + 1)) =
            (3 : ℚ) ^ s * (2 * b (j + 1)) := by ring
        _ = (3 : ℚ) ^ s * 3 * a (j + 1) - (3 : ℚ) ^ s * b j := by
          rw [hnext j hj]; ring
    rw [h]
    exact integral_sub (ha (j + 1) hj) (ih (by omega))

/-- Once the whole finite jet is integral, an odd shortcut preserves it. -/
theorem odd_step_integral (r : ℕ) (a b : ℕ → ℚ)
    (ha : Cleared 0 r a)
    (hb : ∀ j ≤ r, BinaryIntegral (b j))
    (hzero : 2 * b 0 = 3 * a 0 - 1)
    (hnext : ∀ j, j + 1 ≤ r → 2 * b (j + 1) = 3 * a (j + 1) - b j) :
    Cleared 0 r b := by
  have ha' : Cleared 1 r a := by
    intro j hj
    simpa using integral_mul (show Integral (3 : ℚ) from ⟨3, rfl⟩)
      (ha j hj)
  exact odd_step_cleared 0 r a b ha' hb hzero hnext

private theorem mem_of_scale (S : Subring ℚ) {scale q : ℚ}
    (hne : scale ≠ 0) (hi : scale⁻¹ ∈ S) (h : scale * q ∈ S) : q ∈ S := by
  have hm := S.mul_mem hi h
  simpa only [← mul_assoc, inv_mul_cancel₀ hne, one_mul] using hm

/-- Away from two and three, finite Taylor integrality is exactly
invariant under an actual shortcut step. The natural exponent includes
the two actual cases `e=0` and `e=1`. -/
theorem jet_subring_iff (S : Subring ℚ) (r e : ℕ) (a b : ℕ → ℚ)
    (h2 : (2 : ℚ)⁻¹ ∈ S) (h3 : (3 : ℚ)⁻¹ ∈ S)
    (hzero : 2 * b 0 = (3 : ℚ) ^ e * a 0 - e)
    (hnext : ∀ j, j + 1 ≤ r →
      2 * b (j + 1) = (3 : ℚ) ^ e * a (j + 1) - b j) :
    (∀ j ≤ r, a j ∈ S) ↔ (∀ j ≤ r, b j ∈ S) := by
  have hscale : (3 : ℚ) ^ e ∈ S := S.pow_mem (natCast_mem S 3) e
  have hinv : ((3 : ℚ) ^ e)⁻¹ ∈ S := by
    simpa only [inv_pow] using S.pow_mem h3 e
  have hne : (3 : ℚ) ^ e ≠ 0 := pow_ne_zero _ (by norm_num)
  constructor
  · intro ha j hj
    induction j with
    | zero =>
      apply mem_of_scale S (by norm_num : (2 : ℚ) ≠ 0) h2
      rw [hzero]
      exact S.sub_mem (S.mul_mem hscale (ha 0 hj)) (natCast_mem S e)
    | succ j ih =>
      apply mem_of_scale S (by norm_num : (2 : ℚ) ≠ 0) h2
      rw [hnext j hj]
      exact S.sub_mem (S.mul_mem hscale (ha (j + 1) hj)) (ih (by omega))
  · intro hb j hj
    apply mem_of_scale S hne hinv
    cases j with
    | zero =>
      have h : (3 : ℚ) ^ e * a 0 = 2 * b 0 + e := by linarith [hzero]
      rw [h]
      exact S.add_mem (S.mul_mem (natCast_mem S 2) (hb 0 hj)) (natCast_mem S e)
    | succ j =>
      have h : (3 : ℚ) ^ e * a (j + 1) = 2 * b (j + 1) + b j := by
        linarith [hnext j hj]
      rw [h]
      exact S.add_mem (S.mul_mem (natCast_mem S 2) (hb (j + 1) hj)) (hb j (by omega))

end Collatz.ClosureRoundSeven.GermConstruction

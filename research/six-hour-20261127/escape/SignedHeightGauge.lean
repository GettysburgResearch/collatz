import Mathlib.Data.Int.ModEq
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite determinant and denominator-separation steps in the two-height test. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeSignedHeightGauge

theorem determinant_congruence (Q r d a b q p : ℤ)
    (same : Q ∣ d*(b*r-a)) (opposite : Q ∣ p+r*q) :
    Q ∣ d*(b*p+a*q) := by
  obtain ⟨i,hi⟩ := same
  obtain ⟨j,hj⟩ := opposite
  use d*b*j-q*i
  calc
    d*(b*p+a*q) = d*b*(p+r*q)-q*(d*(b*r-a)) := by ring
    _ = Q*(d*b*j-q*i) := by rw [hi,hj]; ring

theorem aspect_lower (Q d a b p q c H : ℚ)
    (hp : p≤c*H) (hq : q≤H) (hd : 0≤d) (ha : 0≤a) (hb : 0≤b)
    (det : Q≤d*(b*p+a*q)) : Q≤d*(a+c*b)*H := by
  have h := add_le_add (mul_le_mul_of_nonneg_left hp hb)
                       (mul_le_mul_of_nonneg_left hq ha)
  have hd' := mul_le_mul_of_nonneg_left h hd
  calc
    Q ≤ d*(b*p+a*q) := det
    _ ≤ d*(b*(c*H)+a*H) := hd'
    _ = d*(a+c*b)*H := by ring

theorem aspect_error (Q G H E : ℚ) (hQ : 0<Q) (hG : 0<G)
    (he : 0≤E) (low : Q≤G*H) (high : G*H≤Q+G*E) :
    0≤G-Q/H ∧ G-Q/H≤G^2*E/Q := by
  have hH : 0<H := by nlinarith
  have lhs : Q/H ≤ G := (div_le_iff₀ hH).mpr (by simpa [mul_comm] using low)
  refine ⟨by linarith,?_⟩
  apply (le_div_iff₀ hQ).mpr
  have e1 : (G*H-Q)*Q ≤ (G*E)*Q :=
    mul_le_mul_of_nonneg_right (by linarith) hQ.le
  have e2 : G*E*Q ≤ G*E*(G*H) :=
    mul_le_mul_of_nonneg_left low (mul_nonneg hG.le he)
  have e := e1.trans e2
  have ht : (Q/H)*H=Q := div_mul_cancel₀ Q hH.ne'
  apply le_of_mul_le_mul_right (a:=H) (by
    calc
      (G-Q/H)*Q*H = (G*H-Q)*Q := by
        calc
          (G-Q/H)*Q*H = G*H*Q-(Q/H*H)*Q := by ring
          _ = (G*H-Q)*Q := by rw [ht]; ring
      _ ≤ G*E*(G*H) := e
      _ = G^2*E*H := by ring) hH

theorem select_denominator (X : ℚ) (d b : ℕ) (hd : 0<d) (hb : 0<b)
    (close : |X-((d*b:ℕ):ℚ)|<1/3) :
    |X-1|<1/3 ↔ d=1 ∧ b=1 := by
  constructor
  · intro sel
    have u := (abs_lt.mp close).1
    have v := (abs_lt.mp sel).2
    have h : ((d*b:ℕ):ℚ)<2 := by linarith
    have nh : d*b<2 := by exact_mod_cast h
    have h1 := Nat.mul_le_mul_left d (show 1≤b by omega)
    have h2 := Nat.mul_le_mul_right b (show 1≤d by omega)
    simp only [Nat.mul_one,Nat.one_mul] at h1 h2
    omega
  · rintro ⟨rfl,rfl⟩
    norm_num at close ⊢
    exact close

#print axioms determinant_congruence
#print axioms aspect_lower
#print axioms aspect_error
#print axioms select_denominator
end EscapeSignedHeightGauge


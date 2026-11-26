import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.Ring.GeomSum

/-! Divisibility propagation on arbitrary finite complete Syracuse block
    schedules, and the positive Mersenne geometric expansion used in E1. -/

namespace ResetDepthRatio

/-- Each list entry is a complete-block excess depth, paired with its shifted
    landing. The equation is the exact shifted relation for an odd ascent. -/
inductive Trace : ℕ → List ℕ → List ℕ → Prop
  | nil (s : ℕ) : Trace s [] []
  | cons {s y t b : ℕ} {depths outputs : List ℕ}
      (edge : 2^(t+b)*y = 3^t*s + 2^t*(2^b-1))
      (rest : Trace y depths outputs) : Trace s (b :: depths) (y :: outputs)

theorem edge_divisor {s y t b g : ℕ} (oddFactor : Nat.Coprime g 2) (initial : g ∣ s)
    (edge : 2^(t+b)*y = 3^t*s + 2^t*(2^b-1)) :
    g ∣ y ↔ g ∣ 2^b-1 := by
  have remove (q n : ℕ) : g ∣ 2^q*n ↔ g ∣ n := by
    constructor
    · exact (oddFactor.pow_right q).dvd_of_dvd_mul_left
    · exact fun hn => dvd_mul_of_dvd_right hn _
  rw [← remove (t+b) y, edge, Nat.dvd_add_right (dvd_mul_of_dvd_right initial _),
    remove t (2^b-1)]

theorem all_outputs {s g : ℕ} {depths outputs : List ℕ} (path : Trace s depths outputs)
    (oddFactor : Nat.Coprime g 2) (initial : g ∣ s) :
    (∀ y ∈ outputs, g ∣ y) ↔ (∀ b ∈ depths, g ∣ 2^b-1) := by
  induction path with
  | nil s => simp
  | cons edge rest ih =>
    simp only [List.forall_mem_cons]
    have step := edge_divisor oddFactor initial edge
    constructor
    · intro h
      exact ⟨step.mp h.1, (ih h.1).mp h.2⟩
    · intro h
      have hy := step.mpr h.1
      exact ⟨hy, (ih hy).mpr h.2⟩

theorem gcd_depths (depths : List ℕ) (g : ℕ) :
    (∀ b ∈ depths, g ∣ 2^b-1) ↔ g ∣ 2^(depths.foldr Nat.gcd 0)-1 := by
  induction depths with
  | nil => simp
  | cons b depths ih =>
    simp only [List.forall_mem_cons, List.foldr_cons, ih,
      ← Nat.pow_sub_one_gcd_pow_sub_one, Nat.dvd_gcd_iff]

/-- Test every common odd divisor using only the entrance and the gcd of the
    reset excesses. The input divisor is unrestricted away from two. -/
theorem common_divisor {s g : ℕ} {depths outputs : List ℕ} (path : Trace s depths outputs)
    (oddFactor : Nat.Coprime g 2) :
    (g ∣ s ∧ ∀ y ∈ outputs, g ∣ y) ↔
      g ∣ Nat.gcd s (2^(depths.foldr Nat.gcd 0)-1) := by
  rw [Nat.dvd_gcd_iff]
  constructor
  · rintro ⟨hs, h⟩
    exact ⟨hs, (gcd_depths depths g).mp ((all_outputs path oddFactor hs).mp h)⟩
  · rintro ⟨hs, h⟩
    exact ⟨hs, (all_outputs path oddFactor hs).mpr ((gcd_depths depths g).mpr h)⟩

theorem split_correction (e m g q : ℕ) (factor : 2^e-1 = g*q) :
    2^(e*m)-1 = g * (q * ∑ i ∈ Finset.range m, (2^e)^i) := by
  rw [pow_mul, ← geom_sum_mul_of_one_le (show 1 ≤ (2 : ℕ)^e from Nat.pow_pos (by decide : 0 < 2)) m,
     factor]
  ac_rfl

#print axioms edge_divisor
#print axioms all_outputs
#print axioms gcd_depths
#print axioms common_divisor
#print axioms split_correction

end ResetDepthRatio

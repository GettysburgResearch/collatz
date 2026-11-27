import Mathlib.RingTheory.Coprime.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-! Exact signed differences on every matched run of two ordinary binary-gap
    phases, with endpoints on the appropriate two distinct native branches. -/

namespace Collatz.Diagonal.RunCofactors

theorem equal_letter {x y x' y' P D : ℤ}
    (hx : P*x' = 3*x+D) (hy : P*y' = 3*y+D) :
    P*(x'-y') = 3*(x-y) := by linear_combination hx-hy

theorem mixed_incoming {x y u v : ℤ} (hu : 2*x = 3*u+1)
    (hv : 4*y = 3*v+1) : ¬3 ∣ x-y := by omega

theorem mixed_outgoing {x y u v : ℤ}
    (hu : 2*u = 3*x+1) (hv : 4*v = 3*y+1) (hodd : u%2=1) :
    ∃ w : ℤ, x-y=2*w ∧ ¬2 ∣ w := by
  refine ⟨(x-y)/2, ?_, ?_⟩ <;> omega

theorem matched_prefix {D : ℕ → ℤ} {a E : ℕ → ℕ} (n : ℕ)
    (h0 : E 0 = 0) (hE : ∀ j < n, E (j+1) = E j + a j)
    (hD : ∀ j < n, (2:ℤ)^(a j)*D (j+1) = 3*D j) :
    ∀ j ≤ n, (2:ℤ)^(E j)*D j = 3^j*D 0 := by
  intro j hj
  induction j with
  | zero => simp [h0]
  | succ j ih =>
    have hlt : j < n := by omega
    rw [hE j hlt, pow_add, mul_assoc, hD j hlt, pow_succ]
    linear_combination 3 * ih (by omega)

theorem one_signed_core {D : ℕ → ℤ} {a E : ℕ → ℕ} (n : ℕ)
    (h0 : E 0 = 0) (hE : ∀ j < n, E (j+1) = E j + a j)
    (hD : ∀ j < n, (2:ℤ)^(a j)*D (j+1) = 3*D j)
    (left : ¬3 ∣ D 0) (right : ∃ w : ℤ, D n=2*w ∧ ¬2 ∣ w) :
    ∃ c : ℤ, (¬2 ∣ c) ∧ (¬3 ∣ c) ∧
      ∀ j ≤ n, D j = 2 ^ (E n - E j + 1) * 3^j * c := by
  obtain ⟨w, hw, ho⟩ := right
  have prefixes := matched_prefix n h0 hE hD
  have whole := prefixes n (by omega)
  rw [hw] at whole
  have hc23 : IsCoprime (3:ℤ) 2 := ⟨1,-1, by decide⟩
  have h3 (k : ℕ) : IsCoprime ((3:ℤ)^k) 2 := by
    induction k with
    | zero => exact ⟨1,0, by ring⟩
    | succ k ih => rw [pow_succ]; exact ih.mul_left hc23
  have h2 (k : ℕ) : IsCoprime ((3:ℤ)^n) (2^k) := by
    induction k with
    | zero => exact ⟨0,1, by ring⟩
    | succ k ih => rw [pow_succ]; exact ih.mul_right (h3 n)
  have hc := h2 (E n+1)
  have dvd : (3:ℤ)^n ∣ w := by
    apply hc.dvd_of_dvd_mul_left
    exact ⟨D 0, by rw [pow_succ, mul_assoc]; exact whole⟩
  obtain ⟨c,hc'⟩ := dvd
  have leftEq : D 0 = 2^(E n+1)*c := by
    apply mul_left_cancel₀ (show (3:ℤ)^n ≠ 0 by positivity)
    rw [← whole, hc', pow_succ]
    ring
  refine ⟨c, ?_, ?_, ?_⟩
  · exact fun h => ho (hc' ▸ dvd_mul_of_dvd_right h _)
  · exact fun h => left (leftEq ▸ dvd_mul_of_dvd_right h _)
  · intro j hj
    have mono : ∀ k ≤ n, ∀ i ≤ k, E i ≤ E k := by
      intro k hk
      induction k with
      | zero =>
        intro i hi
        have he : i = 0 := by omega
        simp [he]
      | succ k ih =>
        intro i hi
        by_cases he : i = k+1
        · rw [he]
        · exact le_trans (ih (by omega) i (by omega))
            (by rw [hE k (by omega)]; omega)
    have le := mono n (by omega) j hj
    apply mul_left_cancel₀ (show (2:ℤ)^(E j) ≠ 0 by positivity)
    rw [prefixes j hj, leftEq]
    calc
      (3:ℤ)^j * (2^(E n+1)*c)
          = (2^(E j) * 2^(E n-E j+1)) * (3^j*c) := by
              rw [← pow_add, show E j + (E n-E j+1)=E n+1 by omega]
              ring
      _ = _ := by ring

end Collatz.Diagonal.RunCofactors

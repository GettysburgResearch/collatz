import Mathlib.Order.Iterate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! The integer order steps in the extremal octave construction. -/
set_option autoImplicit false
set_option warningAsError true

namespace SixHour.CompletionOrder

/-- Increasing integer coordinates permit an equality at a plateau. -/
theorem node_mono {m n c d : ℤ} (hm : m < n) (hc : c ≤ 4) (hd : 1 ≤ d) :
    3*m + c ≤ 3*n + d := by omega

private theorem iter_translate (f : ℤ → ℤ) {N : ℤ}
    (hf : ∀ x k : ℤ, f (x+k*N) = f x+k*N)
    (n : ℕ) (x k : ℤ) : f^[n] (x+k*N) = f^[n] x+k*N := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [Function.iterate_succ_apply', ih, hf]

private theorem repeat_lap (f : ℤ → ℤ) {N a h : ℤ} {p : ℕ}
    (hf : ∀ x k : ℤ, f (x+k*N) = f x+k*N)
    (ha : f^[p] a = a+h*N) (j : ℕ) :
    f^[j*p] a = a+((j : ℤ)*h)*N := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [Nat.succ_mul, Nat.add_comm, Function.iterate_add_apply, ih,
      iter_translate f hf, ha]
    push_cast
    ring

/-- Two distinct node representatives in one octave on periodic orbits of
the same monotone lift have exactly the same rational slope. -/
theorem periodic_slopes {f : ℤ → ℤ} {N a b h k : ℤ} {p q : ℕ}
    (hN : 0 < N) (hab : a < b) (hba : b < a+N)
    (hm : Monotone f) (hf : ∀ x j : ℤ, f (x+j*N) = f x+j*N)
    (ha : f^[p] a = a+h*N) (hb : f^[q] b = b+k*N) :
    (q : ℤ)*h = (p : ℤ)*k := by
  have la := repeat_lap f hf ha q
  have lb := repeat_lap f hf hb p
  rw [Nat.mul_comm p q] at lb
  have l := (hm.iterate (q*p)) hab.le
  have u := (hm.iterate (q*p)) hba.le
  have tr : f^[q*p] (a+N) = f^[q*p] a+N := by
    simpa using iter_translate f hf (q*p) a 1
  rw [la, lb] at l
  rw [lb, tr, la] at u
  by_contra ne
  rcases lt_or_gt_of_ne ne with hh | hh
  · have e : (q : ℤ)*h+1 ≤ (p : ℤ)*k := by omega
    have v := mul_le_mul_of_nonneg_right e hN.le
    nlinarith
  · have e : (p : ℤ)*k+1 ≤ (q : ℤ)*h := by omega
    have v := mul_le_mul_of_nonneg_right e hN.le
    nlinarith

/-- A correction for a high-drift finite path incurs linear oscillation. -/
theorem correction_cost (u : ℕ → ℚ) {t : ℕ} {margin : ℚ}
    (hs : ∀ i < t, u (i+1) + margin ≤ u i) : (t : ℚ)*margin ≤ u 0-u t := by
  have propagate (j : ℕ) (hj : j ≤ t) : (j : ℚ)*margin ≤ u 0-u j := by
    induction j with
    | zero => simp
    | succ j ih =>
      have a := ih (by omega)
      have b := hs j (by omega)
      push_cast
      linarith
  exact propagate t le_rfl

#print axioms node_mono
#print axioms periodic_slopes
#print axioms correction_cost

end SixHour.CompletionOrder

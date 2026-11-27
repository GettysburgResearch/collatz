import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Ring

/-! Exact finite arithmetic for the fair-gate first-clear clock. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeFairFirstClear

def tailCount (K h : ℕ) : ℕ := 2^h * Nat.choose (2*K-h) K

/-- Successive unnormalized clock tails, without division. -/
theorem tail_recurrence (K h : ℕ) (needed : 0<K) (within : h≤K) :
    tailCount K (h+1)*(2*K-h) = 2*(K-h)*tailCount K h := by
  let m := 2*K-(h+1)
  have hm : m+1=2*K-h := by dsimp [m]; omega
  have hc := Nat.choose_mul_succ_eq m K
  have hd : m+1-K=K-h := by omega
  rw [hd, hm] at hc
  change 2^(h+1)*m.choose K*(2*K-h) = 2*(K-h)*(2^h*(2*K-h).choose K)
  calc
    _ = 2^(h+1)*(m.choose K*(2*K-h)) := by ring
    _ = 2^(h+1)*((2*K-h).choose K*(K-h)) := by rw [hc]
    _ = _ := by rw [pow_succ]; ring

/-- The tail difference has fraction h / (2K-h), also at the last clock. -/
theorem tail_atom (K h : ℕ) (needed : 0<K) (within : h≤K) :
    tailCount K h*(2*K-h) =
      tailCount K (h+1)*(2*K-h) + h*tailCount K h := by
  rw [tail_recurrence K h needed within]
  have n : 2*K-h=2*(K-h)+h := by omega
  conv_lhs => rw [n]
  ring

/-- Once grade K has arrived, every remaining prefix to time 2K
continues to meet the original fair gate. -/
theorem automatic_tail (K t h j g : ℕ) (clock : t+h=2*K)
    (wait : j≤h) : t+j≤2*(K+g) := by omega

#print axioms tail_recurrence
#print axioms tail_atom
#print axioms automatic_tail
end EscapeFairFirstClear

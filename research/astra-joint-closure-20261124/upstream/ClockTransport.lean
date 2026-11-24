import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite transport from PR202, compiled in the joint-closure audit.
Original theorem statements and proof bodies retained; narrow imports and unused binder name adjusted.
The analytic synchronization and routing inputs are not asserted as Lean axioms.
-/

namespace SynchronizedBasinBlocks

def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3*x+1)/2

def walk (T : ℕ → ℕ) : ℕ → ℕ → ℕ
  | 0, x => x
  | n+1, x => walk T n (T x)

theorem walk_add (T : ℕ → ℕ) (h k x : ℕ) :
    walk T (h+k) x = walk T k (walk T h x) := by
  induction h generalizing x with
  | zero => simp [walk]
  | succ h ih =>
    rw [Nat.succ_add]
    exact ih (T x)

theorem common_clock (T : ℕ → ℕ) (h b r p z t q M : ℕ)
    (hsync : ∀ i < M, walk T h (r+2^h*t+i) = z+3^p*t)
    (hroute : walk T (2*b) (z+3^p*t) = q) :
    ∀ i < M, walk T (h+2*b) (r+2^h*t+i) = q := by
  intro i hi
  rw [walk_add, hsync i hi, hroute]

theorem attach_target (T : ℕ → ℕ) (h b j x q a M : ℕ)
    (hcommon : ∀ i < M, walk T (h+2*b) (x+i) = q)
    (ha : walk T j q = a) :
    ∀ i < M, walk T (h+2*b+j) (x+i) = a := by
  intro i hi
  rw [walk_add, hcommon i hi, ha]

theorem fixed_clock_injective (T : ℕ → ℕ) (H : ℕ)
    (Q : Set ℕ) (start : ℕ → ℕ)
    (h : ∀ q ∈ Q, walk T H (start q) = q) :
    Set.InjOn start Q := by
  intro q hq q' hq' he
  calc
    q = walk T H (start q) := (h q hq).symm
    _ = walk T H (start q') := by rw [he]
    _ = q' := h q' hq'

theorem inverse_step_affine (e : ℕ) (y z : ℤ)
    (h : 3*z+1 = 2^e*y) : 3*(4*z+1)+1 = 2^(e+2)*y := by
  rw [pow_add]
  norm_num
  linarith only [h]

theorem carry_height_identity (A B C D q y x r z : ℤ)
    (hroute : A*q = B*y+C) (hlift : D*(x-r) = y-z) :
    B*D*(x-r) = A*q-C-B*z := by
  calc
    B*D*(x-r) = B*(D*(x-r)) := by ring
    _ = B*(y-z) := by rw [hlift]
    _ = A*q-C-B*z := by linarith only [hroute]

-- Division-free version of the exact error identity:
-- D*(x-r)=E*(y-z), A*q=B*y+C, where E=2^h, D=3^p.
theorem scaled_carry_identity (A B C D E q y x r z : ℤ)
    (hroute : A*q = B*y+C)
    (hlift : D*(x-r) = E*(y-z)) :
    B*D*(x-r) = E*(A*q-C-B*z) := by
  calc
    B*D*(x-r) = B*(D*(x-r)) := by ring
    _ = B*(E*(y-z)) := by rw [hlift]
    _ = E*(B*y-B*z) := by ring
    _ = E*(A*q-C-B*z) := by
      have h : B*y = A*q-C := by linarith only [hroute]
      rw [h]

theorem router_height_cost (A B m q y : ℕ)
    (_hB : 0 < B) (hy : m ≤ y) (hroute : B*y ≤ A*q) :
    B*m ≤ A*q :=
  le_trans (Nat.mul_le_mul_left B hy) hroute

#print axioms walk_add
#print axioms common_clock
#print axioms attach_target
#print axioms fixed_clock_injective
#print axioms inverse_step_affine
#print axioms carry_height_identity
#print axioms scaled_carry_identity
#print axioms router_height_cost

end SynchronizedBasinBlocks

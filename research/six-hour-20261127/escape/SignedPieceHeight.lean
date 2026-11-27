import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.Order.Monoid.Unbundled.Pow
import Mathlib.Algebra.Group.Nat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Integer height certificates for a positive Syracuse segment sharing its
division word with a signed rational starting value. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeSignedPieceHeight

/-- The terminal numerator difference after clearing the odd denominator.
The ordinary starting difference is q*x+p for the signed anchor -p/q. -/
theorem cleared_gap (a t k q x p : ℕ) (hp : 0<p)
    (eqn : 2^a*k=3^t*(q*x+p)) : 2^a ≤ q*x+p := by
  have d : 2^a ∣ 3^t*(q*x+p) := ⟨k,eqn.symm⟩
  have cop := Nat.Coprime.pow a t (by decide : Nat.Coprime 2 3)
  exact Nat.le_of_dvd (by omega) (cop.dvd_of_dvd_mul_left d)

/-- A finite witness bounds the word's division cost against the physical
starting height, the anchor height and the prior count of one exponents. -/
theorem segment_bound (a t k q x p H m R : ℕ) (hp : 0<p)
    (hq : q≤H) (hm : p≤H) (eqn : 2^a*k=3^t*(q*x+p))
    (travel : 2^R*(x+1) ≤ 3^R*(m+1)) :
    2^(a+R) ≤ H*3^R*(m+1) := by
  have lower := cleared_gap a t k q x p hp eqn
  have cap : q*x+p ≤ H*(x+1) := by
    rw [mul_add,mul_one]
    exact Nat.add_le_add (Nat.mul_le_mul_right x hq) hm
  calc
    2^(a+R) = 2^R*2^a := by rw [pow_add,Nat.mul_comm]
    _ ≤ 2^R*(H*(x+1)) := Nat.mul_le_mul_left _ (lower.trans cap)
    _ = H*(2^R*(x+1)) := by ring
    _ ≤ H*(3^R*(m+1)) := Nat.mul_le_mul_left _ travel
    _ = H*3^R*(m+1) := by ring

/-- The actual shifted-height multiplier for an exact Syracuse exponent. -/
theorem shifted_edge (x y e : ℕ) (pos : 0<e) (edge : 2^e*y=3*x+1) :
    (if e=1 then 2 else 1)*(y+1) ≤ (if e=1 then 3 else 1)*(x+1) := by
  by_cases one : e=1
  · subst e
    simp at edge ⊢
    omega
  · have h : 2≤e := by omega
    have four := Nat.pow_le_pow_right (n:=2) (by decide) h
    have bound := Nat.mul_le_mul_right y four
    simp [one]
    norm_num at bound
    omega

/-- The same shifted-height estimate in a binary shortcut word. -/
theorem binary_shifted_edge (x y : ℕ) (oddStep : Bool)
    (edge : 2*y=if oddStep then 3*x+1 else x) :
    (if oddStep then 2 else 1)*(y+1) ≤
    (if oddStep then 3 else 1)*(x+1) := by
  cases oddStep <;> simp at edge ⊢ <;> omega

/-- Any accepted length-n prefix reaching 1 must spend at least n/4
odd steps before its first arrival. The subsequent exponent is two. -/
theorem one_hit_floor (n h A : ℕ) (inside : h≤n)
    (clock : h+2*(n-h)≤A) (gate : 4*A≤7*n) : n≤4*h := by omega

/-- Binary counterpart. g counts all odd departures, and u those before
arrival at the shortcut cycle 1,2. The final alternating tail costs at
most its length plus one after doubling. -/
theorem binary_one_floor (N h g u : ℕ) (inside : h≤N) (prefixCap : u≤h)
    (clock : 2*g≤2*u+(N-h)+1) (gate : 5*N≤8*g) :
    N≤4*h+4 ∧ N≤4*u+4 := by omega

#print axioms cleared_gap
#print axioms segment_bound
#print axioms shifted_edge
#print axioms binary_shifted_edge
#print axioms one_hit_floor
#print axioms binary_one_floor
end EscapeSignedPieceHeight

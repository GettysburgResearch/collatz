import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic

/-! Affine parity-word numerators, their dyadic separation at fixed weight,
and real shadow updates for an oriented pair. Words are chronological. -/

namespace CollatzShell.HighGradeShadow

def weight : List Bool → ℕ
  | [] => 0
  | b :: w => b.toNat + weight w

def numer : List Bool → ℕ
  | [] => 0
  | b :: w => b.toNat * 3 ^ weight w + 2 * numer w

theorem parity_numer (b : Bool) (w : List Bool) : numer (b :: w) % 2 = b.toNat := by
  cases b <;> simp [numer, Nat.add_mod, Nat.pow_mod]

/-- The affine intercept of a fixed-weight word records its dyadic residue faithfully. -/
theorem fixed_weight_residue_injective {u v : List Bool} (len : u.length = v.length)
    (count : weight u = weight v) (res : numer u ≡ numer v [MOD 2^u.length]) : u = v := by
  induction u generalizing v with
  | nil => simpa using len.symm
  | cons b u ih =>
    cases v with
    | nil => simp at len
    | cons c v =>
      have length' : u.length = v.length := by simpa using len
      have ev : numer (b::u) ≡ numer (c::v) [MOD 2] := by
        apply res.of_dvd
        simp [pow_succ]
      have bit : b = c := by
        change numer (b :: u) % 2 = numer (c :: v) % 2 at ev
        rw [parity_numer, parity_numer] at ev
        cases b <;> cases c <;> simp_all
      subst c
      have count' : weight u = weight v := by simpa [weight] using count
      simp only [numer, count', List.length_cons, pow_succ] at res
      have rr := Nat.ModEq.add_left_cancel' (b.toNat * 3^weight v) res
      rw [Nat.mul_comm (2^u.length) 2] at rr
      have sub : numer u ≡ numer v [MOD 2^u.length] := Nat.ModEq.mul_left_cancel' (by decide : (2 : ℕ) ≠ 0) rr
      exact congrArg (List.cons b) (ih length' count' sub)

/-- The exact shadow update allows the upper bit to depend on all lower bits. -/
theorem oriented_shadow_update {X Y W c c' a b a' b' : ℚ}
    (rel : Y = c * (X-W)) (cc : c * a' = c' * a) (nz : c' ≠ 0) :
    (a*X+b)/2 - (a'*Y+b')/(2*c') = (a*W+b)/2 - b'/(2*c') := by
  field_simp [nz]
  rw [rel]
  linear_combination -(X-W)*cc

end CollatzShell.HighGradeShadow

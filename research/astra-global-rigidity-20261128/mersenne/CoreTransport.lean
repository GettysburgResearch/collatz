import Mathlib.Data.Nat.Basic
import Lean.Elab.Tactic.Omega

/-!
Integer algebra for reduced adjacent cores. The analytic estimates are
explicit numerical hypotheses. The product identity is unconditional on
every sequence of physical core factorizations satisfying its one-step law.
-/
namespace Collatz.CoreTransport

/-- Keep the two separate one-step upper bounds and the shared factor. -/
theorem uncancelled_bound (N v W G U V K : Nat) (hU : 0 < U)
    (hN : N ≤ v*W) (hW : W ≤ K*U*V) (hv : v ≤ K*(G*V))
    (hG : G*U ≤ W) : N ≤ K^3*U*V^3 := by
  have hcancel : U*G ≤ U*(K*V) := by
    calc
      _ = G*U := Nat.mul_comm _ _
      _ ≤ K*U*V := le_trans hG hW
      _ = _ := by ac_rfl
  have hret : G ≤ K*V := by
    by_contra h
    have hn : K*V < G := by omega
    exact (not_lt_of_ge hcancel) (Nat.mul_lt_mul_of_pos_left hn hU)
  have hhalving : v ≤ K*((K*V)*V) :=
    le_trans hv (Nat.mul_le_mul_left K (Nat.mul_le_mul_right V hret))
  calc
    _ ≤ v*W := hN
    _ ≤ (K*((K*V)*V))*(K*U*V) := Nat.mul_le_mul hhalving hW
    _ = _ := by simp only [Nat.pow_succ, Nat.pow_zero, Nat.one_mul]; ac_rfl

def prefixProduct (f : Nat → Nat) : Nat → Nat
  | 0 => 1
  | n+1 => prefixProduct f n * f n

theorem core_telescope (a U V : Nat → Nat)
    (h : ∀ i, a i * U i = a (i+1) * V i) (k : Nat) :
    a 0 * prefixProduct U k = a k * prefixProduct V k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    simp only [prefixProduct]
    calc
      _ = (a 0 * prefixProduct U k) * U k := by ac_rfl
      _ = (a k * prefixProduct V k) * U k := by rw [ih]
      _ = (a k * U k) * prefixProduct V k := by ac_rfl
      _ = (a (k+1) * V k) * prefixProduct V k := by rw [h k]
      _ = _ := by ac_rfl

private theorem factors_product (U V : Nat → Nat) (k : Nat) :
    prefixProduct (fun i => U i * V i^3) k =
    prefixProduct U k * (prefixProduct V k)^3 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    simp only [prefixProduct, ih, Nat.mul_pow]
    ac_rfl

/-- The third power in the one-step denominator leaves a fourth power of
    the inserted factors after summing a whole finite physical segment. -/
theorem inserted_product (a U V : Nat → Nat)
    (h : ∀ i, a i * U i = a (i+1) * V i) (k : Nat) :
    prefixProduct (fun i => U i * V i^3) k * (a k)^3 =
    (prefixProduct U k)^4 * (a 0)^3 := by
  rw [factors_product]
  calc
    _ = prefixProduct U k * (a k * prefixProduct V k)^3 := by
      rw [Nat.mul_pow]
      ac_rfl
    _ = prefixProduct U k * (a 0 * prefixProduct U k)^3 := by
      rw [core_telescope a U V h k]
    _ = _ := by rw [Nat.mul_pow, Nat.pow_succ (prefixProduct U k) 3]; ac_rfl

end Collatz.CoreTransport

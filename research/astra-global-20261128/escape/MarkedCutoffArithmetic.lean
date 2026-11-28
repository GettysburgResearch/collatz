import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Nat.ModEq

/-! Actual odd-map branch arithmetic used in the moving cutoff. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.MarkedCutoffFlux
open Nat
def gap (x : ℕ) : ℕ := (3 * x + 1).factorization 2
def landing (x : ℕ) : ℕ := ordCompl[2] (3 * x + 1)

theorem native_edge (x : ℕ) : 2 ^ gap x * landing x = 3 * x + 1 := by
  exact Nat.ordProj_mul_ordCompl_eq_self (3 * x + 1) 2

/-- On one clock no two distinct sources in one ternary class can enter
the same interval of targets from 1 to the next ternary period. -/
theorem residue_injective (n e x y : ℕ)
    (cx : gap x = e) (cy : gap y = e)
    (px : 0 < landing x) (py : 0 < landing y)
    (bx : landing x ≤ 3 * 3 ^ n) (byy : landing y ≤ 3 * 3 ^ n)
    (h : Nat.ModEq (3 ^ n) x y) : x = y := by
  have ex := native_edge x
  have ey := native_edge y
  rw [cx] at ex
  rw [cy] at ey
  have congr : Nat.ModEq (3 * 3 ^ n) (2 ^ e * landing x) (2 ^ e * landing y) := by
    rw [ex, ey]
    exact (h.mul_left' 3).add_right 1
  have cop : Nat.Coprime (3 * 3 ^ n) (2 ^ e) := by
    simpa [pow_succ, Nat.mul_comm] using
      (Nat.Coprime.pow_left (n + 1) (Nat.Coprime.pow_right e (by decide : Nat.Coprime 3 2)))
  have eqm := Nat.ModEq.cancel_left_of_coprime cop congr
  have same : landing x = landing y := by
    apply eqm.eq_of_abs_lt
    rw [abs_lt]
    omega
  rw [same] at ex
  omega

end Collatz.MarkedCutoffFlux

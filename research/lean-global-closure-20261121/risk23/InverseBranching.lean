import Std

/-!
Two strictly increasing, positive odd unit predecessors at every odd unit root.
This is the arithmetic input to the written inverse-tree Hardy-space argument.
It does not formalize that analytic argument or prove Collatz convergence.
Only Lean core/Std is used; there is no native_decide or custom axiom.
-/

namespace Collatz.InverseBranching

/-- A unit child above its root, with a bounded exact odd-step exponent. -/
def GoodChild (n e x : Nat) : Prop :=
  3 ≤ e ∧ e ≤ 8 ∧ n < x ∧ x % 2 = 1 ∧ x % 3 ≠ 0 ∧
    3 * x + 1 = 2 ^ e * n

theorem two_children (n : Nat) (hn : 0 < n)
    (hodd : n % 2 = 1) (hunit : n % 3 ≠ 0) :
    ∃ e f x y : Nat, GoodChild n e x ∧ GoodChild n f y ∧ e < f ∧ x < y := by
  have hres : n % 18 = 1 ∨ n % 18 = 5 ∨ n % 18 = 7 ∨
      n % 18 = 11 ∨ n % 18 = 13 ∨ n % 18 = 17 := by omega
  rcases hres with h | h | h | h | h | h
  · refine ⟨4, 8, 96 * (n / 18) + 5, 1536 * (n / 18) + 85, ?_⟩
    simp only [GoodChild]
    omega
  · refine ⟨3, 5, 48 * (n / 18) + 13, 192 * (n / 18) + 53, ?_⟩
    simp only [GoodChild]
    omega
  · refine ⟨4, 6, 96 * (n / 18) + 37, 384 * (n / 18) + 149, ?_⟩
    simp only [GoodChild]
    omega
  · refine ⟨3, 7, 48 * (n / 18) + 29, 768 * (n / 18) + 469, ?_⟩
    simp only [GoodChild]
    omega
  · refine ⟨6, 8, 384 * (n / 18) + 277, 1536 * (n / 18) + 1109, ?_⟩
    simp only [GoodChild]
    omega
  · refine ⟨5, 7, 192 * (n / 18) + 181, 768 * (n / 18) + 725, ?_⟩
    simp only [GoodChild]
    omega

#print axioms two_children

end Collatz.InverseBranching

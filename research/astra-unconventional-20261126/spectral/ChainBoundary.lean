import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Tactic.Abel

/-! Finite telescoping kernel for the written spectral singular sequences.
No assertion about infinite spectra or norm convergence is made here. -/

namespace ChainBoundary

variable {K V : Type*} [CommRing K] [AddCommGroup V] [Module K V]

def chain (c : K) (v : ℕ → V) : ℕ → V
  | 0 => 0
  | n+1 => c • chain c v n + v n

theorem boundary (A : V →ₗ[K] V) (c : K) (v : ℕ → V)
    (n : ℕ) (hv : ∀ j < n, A (v j) = v (j+1)) :
    A (chain c v n) + c^n • v 0 = c • chain c v n + v n := by
  induction n with
  | zero => simp [chain]
  | succ n ih =>
    have hi := ih (fun j hj => hv j (Nat.lt_trans hj (Nat.lt_succ_self n)))
    have hn := hv n (Nat.lt_succ_self n)
    simp only [chain, map_add, map_smul, hn, pow_succ]
    have hs := congrArg (fun x : V => c • x) hi
    simp only [smul_add, smul_smul] at hs
    simp only [smul_add, smul_smul]
    have hs' := congrArg (fun x : V => x + v (n+1)) hs
    rw [mul_comm c (c^n)] at hs'
    convert hs' using 1
    abel

theorem boundary_sub (A : V →ₗ[K] V) (c : K) (v : ℕ → V)
    (n : ℕ) (hv : ∀ j < n, A (v j) = v (j+1)) :
    A (chain c v n) - c • chain c v n = v n - c^n • v 0 := by
  have h := boundary A c v n hv
  apply sub_eq_sub_iff_add_eq_add.mpr
  simpa only [add_comm] using h

end ChainBoundary

#print axioms ChainBoundary.boundary
#print axioms ChainBoundary.boundary_sub

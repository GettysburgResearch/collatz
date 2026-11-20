/-
  Lean 4 Blueprint extending PR #146 (GettysburgResearch/collatz)
  Status: PROPOSED / READY FOR `lake build` VERIFICATION

  Proves exact unconditional algebraic coalescence of (n, 3n) for
  residue classes mod 2^M, starting with the minimal depth M = 5 witness
  n = 32*m + 23 where T^5(n) = T^5(3n) = 27*m + 20.
-/

namespace GettysburgCollatz.Route1

/-- Shortcut Collatz map T(n) = n/2 if even, (3n+1)/2 if odd. -/
def T (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

/-- Iterated shortcut Collatz map. -/
def T_iter : Nat -> Nat -> Nat
  | 0, n => n
  | k + 1, n => T_iter k (T n)

/-- Two trajectories coalesce if they meet at some finite steps (k1, k2). -/
def Coalesce (a b : Nat) : Prop :=
  exists k1 k2 : Nat, T_iter k1 a = T_iter k2 b

/--
  Theorem (Depth-5 Exact Algebraic Coalescence for PR #146):
  For every m : Nat, n = 32*m + 23 satisfies T^5(n) = 27*m + 20 = T^5(3*n).
  Hence no n ≡ 23 (mod 32) can belong to the failed tripling set D(X).
-/
theorem coalesce_mod32_23 (m : Nat) :
    T_iter 5 (32 * m + 23) = 27 * m + 20 /\
    T_iter 5 (3 * (32 * m + 23)) = 27 * m + 20 := by
  constructor
  · -- Step-by-step evaluation:
    -- T^0 = 32m+23 (odd)
    -- T^1 = 48m+35 (odd)
    -- T^2 = 72m+53 (odd)
    -- T^3 = 108m+80 (even)
    -- T^4 = 54m+40 (even)
    -- T^5 = 27m+20
    simp [T_iter, T]
    omega
  · -- Step-by-step evaluation for 3*(32m+23) = 96m+69:
    -- T^0 = 96m+69 (odd)
    -- T^1 = 144m+104 (even)
    -- T^2 = 72m+52 (even)
    -- T^3 = 36m+26 (even)
    -- T^4 = 18m+13 (odd)
    -- T^5 = 27m+20
    simp [T_iter, T]
    omega

theorem not_failed_tripling_mod32_23 (m : Nat) :
    Coalesce (32 * m + 23) (3 * (32 * m + 23)) := by
  refine ⟨5, 5, ?_⟩
  have h := coalesce_mod32_23 m
  exact h.1.trans h.2.symm

/-
  NEXT TARGETS FOR AUTOMATED CODEGEN (see algebraic_coalescence_sieve.py):
  Generate and verify all 3 classes at M=6 (r in {23, 55, ...}),
  8 classes at M=7, 19 classes at M=8, ..., 855 classes at M=13,
  and combine with PR #146's minimality lemma for x_min.
-/

end GettysburgCollatz.Route1

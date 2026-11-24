import Std

/-! Finite arithmetic core for stationary-carry-rigidity-20261124.
    Source candidate, not compiled in the authoring environment.
    All scalar/physical hypotheses are explicit; no convergence axiom. -/

namespace Collatz.StationaryCarryRigidity

def prefixSum (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => prefixSum f n + f n

theorem prefixSum_congr (f f' : Nat → Nat) :
    ∀ m : Nat, (∀ i, i < m → f i = f' i) →
      prefixSum f m = prefixSum f' m := by
  intro m
  induction m with
  | zero => intro h; rfl
  | succ m ih =>
    intro h
    simp only [prefixSum]
    rw [ih (fun i hi => h i (Nat.lt_succ_of_lt hi)),
        h m (Nat.lt_succ_self m)]

theorem prefixSum_ge_length (b : Nat → Nat) (hb : ∀ i, 1 ≤ b i)
    (m : Nat) : m ≤ prefixSum b m := by
  induction m with
  | zero => simp [prefixSum]
  | succ m ih =>
    simp only [prefixSum]
    have h := hb m
    omega

/-- Full phase/carry telescope in naturals: no truncated subtraction. -/
theorem carry_telescope (g b k : Nat → Nat)
    (h : ∀ i, g i + k (i+1) = b i + 3*k i) (m : Nat) :
    prefixSum g m + k m =
      prefixSum b m + 2*prefixSum k m + k 0 := by
  induction m with
  | zero => simp [prefixSum]
  | succ m ih =>
    simp only [prefixSum]
    have hs := h m
    omega

/-- A supplied exact integer height budget implies a carry-sum budget.
    H+R is the explicit endpoint-height allowance (including rounding). -/
theorem carry_budget (g b k : Nat → Nat)
    (h : ∀ i, g i + k (i+1) = b i + 3*k i)
    (hb : ∀ i, 1 ≤ b i) (m H R : Nat)
    (hheight : 3*k m + prefixSum g m ≤ H+R) :
    6*prefixSum k m + 3*m ≤ 2*prefixSum g m + H+R := by
  have ht := carry_telescope g b k h m
  have hB := prefixSum_ge_length b hb m
  omega

/-- At fixed clock and phase, the final carry and complete gap word
    are determined by the first m carries. -/
theorem carry_word_determined (g g' b k k' : Nat → Nat) (m : Nat)
    (hm : 0 < m)
    (h : ∀ i, g i + k (i+1) = b i + 3*k i)
    (h' : ∀ i, g' i + k' (i+1) = b i + 3*k' i)
    (hk : ∀ i, i < m → k i = k' i)
    (hA : prefixSum g m = prefixSum g' m) :
    k m = k' m ∧ ∀ i, i < m → g i = g' i := by
  have hsum := prefixSum_congr k k' m hk
  have hz := hk 0 hm
  have ht := carry_telescope g b k h m
  have ht' := carry_telescope g' b k' h' m
  have hend : k m = k' m := by omega
  refine ⟨hend, ?_⟩
  intro i hi
  have hki := hk i hi
  have hkNext : k (i+1) = k' (i+1) := by
    by_cases hn : i+1 < m
    · exact hk (i+1) hn
    · have he : i+1 = m := by omega
      rw [he]
      exact hend
  have e1 := h i
  have e2 := h' i
  omega

/-- Exact forbidden transition used by the KL argument. -/
theorem no_carry_birth {g kNext : Nat} (hg : 1 ≤ g)
    (h : g+kNext = 1) : kNext = 0 := by
  omega

end Collatz.StationaryCarryRigidity

#print axioms Collatz.StationaryCarryRigidity.carry_telescope
#print axioms Collatz.StationaryCarryRigidity.carry_budget
#print axioms Collatz.StationaryCarryRigidity.carry_word_determined
#print axioms Collatz.StationaryCarryRigidity.no_carry_birth

#print axioms Collatz.StationaryCarryRigidity.prefixSum_congr
#print axioms Collatz.StationaryCarryRigidity.prefixSum_ge_length

import Init.Omega

/-! A general finite-orbit whitelist. The native shortcut `orbit` and its
composition law instantiate the orbit parameters. -/

namespace Collatz.FiniteWhitelist

variable (orbit : Nat → Nat → Nat)
variable (compose : ∀ i j x, orbit (i+j) x = orbit j (orbit i x))

include compose

theorem repeat_periodic {i j k n : Nat} (hij : i < j) (hjk : j ≤ k)
    (hit : orbit i n = orbit j n) :
    ∃ p, 0 < p ∧ orbit p (orbit k n) = orbit k n := by
  refine ⟨j-i, by omega, ?_⟩
  calc
    orbit (j-i) (orbit k n) = orbit (k+(j-i)) n := (compose _ _ _).symm
    _ = orbit (j+(k-i)) n := congrArg (fun l => orbit l n) (by omega)
    _ = orbit (k-i) (orbit j n) := compose _ _ _
    _ = orbit (k-i) (orbit i n) := congrArg (orbit (k-i)) hit.symm
    _ = orbit (i+(k-i)) n := (compose _ _ _).symm
    _ = orbit k n := congrArg (fun l => orbit l n) (by omega)

theorem large_prefix_whitelist (H k n : Nat) (W : Nat → Prop)
    (large : Prop) (isLarge : large)
    (highSimple : (∀ i j : Nat, i < j → j ≤ k → orbit i n ≠ orbit j n) →
      (∀ i ≤ k, H < orbit i n) → ¬large)
    (lowFuture : ∀ v ≤ H, ∀ h, W (orbit h v)) :
    (∃ p, 0 < p ∧ orbit p (orbit k n) = orbit k n) ∨ W (orbit k n) := by
  by_cases repeated : ∃ i j, i < j ∧ j ≤ k ∧ orbit i n = orbit j n
  · obtain ⟨i,j,hij,hjk,hit⟩ := repeated
    exact Or.inl (repeat_periodic orbit compose hij hjk hit)
  · by_cases low : ∃ i ≤ k, orbit i n ≤ H
    · obtain ⟨i,hi,hv⟩ := low
      have hit : orbit (k-i) (orbit i n) = orbit k n := by
        calc
          _ = orbit (i+(k-i)) n := (compose _ _ _).symm
          _ = orbit k n := congrArg (fun l => orbit l n) (by omega)
      exact Or.inr (hit ▸ lowFuture _ hv (k-i))
    · apply False.elim
      apply highSimple _ _ isLarge
      · intro i j hij hjk hit
        exact repeated ⟨i,j,hij,hjk,hit⟩
      · intro i hi
        exact Nat.lt_of_not_ge (fun hv => low ⟨i,hi,hv⟩)

#print axioms large_prefix_whitelist

end Collatz.FiniteWhitelist

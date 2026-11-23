import Std

/-!
The source-separation core of SIBLING_CONE_TRANSPORT.md.

Every alternate root v(j) merges with the retained orbit after one step,
but differs from the retained orbit at clock j. If x(j) reaches v(j)
after exactly j steps, the x(j) are pairwise distinct. This is a theorem
for any deterministic map, so its application needs no parity model.

The analytic product bound, logarithmic estimate, and Collatz convergence
are not formalized here. No custom axiom or native_decide is used.
-/

namespace Collatz.SiblingTransport

variable {α : Type}

def forward (u : α → α) : Nat → α → α
  | 0, x => x
  | k + 1, x => u (forward u k x)

theorem forward_add (u : α → α) (m n : Nat) (x : α) :
    forward u (m + n) x = forward u m (forward u n x) := by
  induction m with
  | zero => simp [forward]
  | succ m ih => simp [Nat.succ_add, forward, ih]

theorem forward_step (u : α → α) (k : Nat) (x : α) :
    forward u k (u x) = u (forward u k x) := by
  induction k with
  | zero => rfl
  | succ k ih => simp [forward, ih]

theorem unequal_sources_of_lt
    (u : α → α) (p : α) (v x : Nat → α)
    (hmerge : ∀ j, u (v j) = forward u (j + 1) p)
    (hoff : ∀ j, v j ≠ forward u j p)
    (hreach : ∀ j, forward u j (x j) = v j)
    (j k : Nat) (hjk : j < k) : x j ≠ x k := by
  intro heq
  let d := k - j - 1
  have hk : k = (d + 1) + j := by dsimp [d]; omega
  have hclock : d + (j + 1) = k := by omega
  have hforward : forward u k (x j) = forward u k p := by
    calc
      forward u k (x j)
          = forward u (d + 1) (forward u j (x j)) := by
              rw [hk, forward_add]
      _ = forward u (d + 1) (v j) := by rw [hreach j]
      _ = forward u d (u (v j)) := by
              simp only [forward, forward_step]
      _ = forward u d (forward u (j + 1) p) := by rw [hmerge j]
      _ = forward u (d + (j + 1)) p := (forward_add u d (j + 1) p).symm
      _ = forward u k p := by rw [hclock]
  apply hoff k
  calc
    v k = forward u k (x k) := (hreach k).symm
    _ = forward u k (x j) := by rw [heq]
    _ = forward u k p := hforward

theorem sources_injective
    (u : α → α) (p : α) (v x : Nat → α)
    (hmerge : ∀ j, u (v j) = forward u (j + 1) p)
    (hoff : ∀ j, v j ≠ forward u j p)
    (hreach : ∀ j, forward u j (x j) = v j) :
    Function.Injective x := by
  intro j k heq
  by_cases hjk : j = k
  · exact hjk
  · have horder : j < k ∨ k < j := by omega
    cases horder with
    | inl h => exact False.elim (unequal_sources_of_lt u p v x hmerge hoff hreach j k h heq)
    | inr h => exact False.elim (unequal_sources_of_lt u p v x hmerge hoff hreach k j h heq.symm)

#print axioms sources_injective

end Collatz.SiblingTransport

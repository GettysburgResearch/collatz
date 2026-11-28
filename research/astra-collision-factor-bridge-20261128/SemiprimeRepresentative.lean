import Mathlib.Data.Nat.Prime.Defs

/-!
# The finite ordinary semiprime-representative interface

The existence of a representative for every positive source remains the
source-qualified written theorem. This file proves its precise logical
consumer and checks the seven published ordinary merger witnesses by
kernel computation. It does not assume convergence as an axiom.
-/

namespace Collatz.SemiprimeRepresentative

set_option maxRecDepth 100000
set_option maxHeartbeats 1000000

def step (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit : ℕ → ℕ → ℕ
  | 0, n => n
  | k + 1, n => orbit k (step n)

def Converges (n : ℕ) : Prop := ∃ k, orbit k n = 1

def Meets (n s : ℕ) : Prop := ∃ a b, orbit a n = orbit b s

def bits (n : ℕ) : ℕ := n.log2 + 1

def InFamily (n : ℕ) : Prop :=
  ∃ p q : ℕ, p.Prime ∧ q.Prime ∧ p < q ∧ n = p * q ∧
    4 ≤ bits n ∧ bits n < p ∧ 4 * p ≤ (bits n) ^ 2

private theorem orbit_add (a b n : ℕ) :
    orbit (a + b) n = orbit a (orbit b n) := by
  induction b generalizing n with
  | zero => rfl
  | succ b ih =>
      change orbit (a + b) (step n) = orbit a (orbit b (step n))
      exact ih (step n)

/-- Reaching one is preserved by the actual shortcut step, including the
case where the supplied visit occurs at date zero. -/
theorem convergence_step {n : ℕ} (h : Converges n) : Converges (step n) := by
  rcases h with ⟨k, hk⟩
  cases k with
  | zero =>
      have hn : n = 1 := hk
      subst n
      exact ⟨1, by decide⟩
  | succ k => exact ⟨k, hk⟩

theorem convergence_iterate (k n : ℕ) (h : Converges n) :
    Converges (orbit k n) := by
  induction k generalizing n with
  | zero => exact h
  | succ k ih => exact ih (step n) (convergence_step h)

/-- The two arms can have different clocks. If the representative reaches
one, their common future does too, and then so does the original source. -/
theorem merger_transfers_convergence {n s : ℕ}
    (hm : Meets n s) (hs : Converges s) : Converges n := by
  rcases hm with ⟨a, b, hab⟩
  rcases convergence_iterate b s hs with ⟨k, hk⟩
  refine ⟨k + a, ?_⟩
  rw [orbit_add, hab, hk]

theorem family_positive {n : ℕ} (hn : InFamily n) : 0 < n := by
  rcases hn with ⟨p, q, hp, hq, _, rfl, _, _, _⟩
  exact Nat.mul_pos hp.pos hq.pos

/-- This is the exact formal consumer of the written representative
existence theorem. That theorem is an argument, not a postulated axiom. -/
theorem universal_iff_family
    (representatives : ∀ n : ℕ, 0 < n → ∃ s, InFamily s ∧ Meets n s) :
    (∀ n : ℕ, 0 < n → Converges n) ↔
      (∀ s : ℕ, InFamily s → Converges s) := by
  constructor
  · intro all n hn
    exact all n (family_positive hn)
  · intro all n hn
    rcases representatives n hn with ⟨s, hs, hm⟩
    exact merger_transfers_convergence hm (all s hs)

/-- Every representative appearing in the seven JSON certificates is an
actual squarefree semiprime in the exact integer family. -/
theorem sample_family_members :
    InFamily 143 ∧ InFamily 437 ∧ InFamily 517 ∧ InFamily 713 ∧ InFamily 871 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · exact ⟨11, 13, by decide⟩
  · exact ⟨19, 23, by decide⟩
  · exact ⟨11, 47, by decide⟩
  · exact ⟨23, 31, by decide⟩
  · exact ⟨13, 67, by decide⟩

/-- Ordinary integer replays, independent of the Python step function.
Only kernel decision is used; there is no native-evaluation axiom. -/
theorem sample_actual_mergers :
    Meets 1 143 ∧ Meets 3 143 ∧ Meets 6 143 ∧ Meets 27 437 ∧
      Meets 85 713 ∧ Meets 97 517 ∧ Meets 871 871 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · exact ⟨0, 66, by decide⟩
  · exact ⟨1, 62, by decide⟩
  · exact ⟨2, 62, by decide⟩
  · exact ⟨1, 5, by decide⟩
  · exact ⟨0, 11, by decide⟩
  · exact ⟨0, 4, by decide⟩
  · exact ⟨0, 0, by decide⟩

end Collatz.SemiprimeRepresentative

import BallisticColor
import ForwardPliss

/-! The forward Pliss count instantiated on two actual ordinary Collatz
orbits with different basin-of-one colors. -/
namespace CollatzShell.TernaryHead

open OffsetDescent CollatzForwardPliss
open scoped Classical

/-- A marked clock is required to satisfy the signed odd-count inequality on
every future block. This is an anticipative predicate, not a stopping rule. -/
def ExcessMark (n u s : ℕ) : Prop :=
  ∀ b, b + 16*oddCount b (orbit s u) ≤ 16*oddCount b (orbit s n)

/-- An explicit finite count of all-future marks on a color-discordant pair.
In particular their lower asymptotic time density is at least 1/15. -/
theorem discordant_mark_count {n u L q : ℕ} (hn : 0<n) (bad : ¬ Basin n)
    (size : n≤2^L) (hit : orbit q u=1) (N : ℕ) :
    (N : ℤ) - 2*(5*(L:ℤ)+4*q+4) ≤
      15 * (((Finset.range N).filter (ExcessMark n u)).card : ℤ) := by
  obtain ⟨zero, lower, upper, windows⟩ := ballisticWalk_laws hn bad size hit
  have main := forward_record_count (ballisticWalk n u)
    (2*(5*(L:ℤ)+4*q+4)) 15 (by decide) lower upper N
  have predicates : FutureRecord (ballisticWalk n u) = ExcessMark n u := by
    funext s
    apply propext
    constructor
    · intro hs b
      exact (windows s b).mp (hs (s+b) (by omega))
    · intro hs t ht
      have hw := (windows s (t-s)).mpr (hs (t-s))
      simpa [Nat.add_sub_of_le ht] using hw
  rw [predicates, zero] at main
  simpa using main

/-- Every actual discordant pair has one fixed allowance that works at all
time horizons. No upper bound on its convergence witness is introduced. -/
theorem discordant_uniform_mark_allowance {n u : ℕ} (hn : 0<n)
    (bad : ¬ Basin n) (good : Basin u) :
    ∃ C : ℕ, ∀ N : ℕ, (N : ℤ) - C ≤
      15 * (((Finset.range N).filter (ExcessMark n u)).card : ℤ) := by
  obtain ⟨q, hit⟩ := good
  refine ⟨2*(5*n+4*q+4), ?_⟩
  intro N
  have main := discordant_mark_count hn bad (Nat.le_of_lt n.lt_two_pow_self) hit N
  simpa only [Nat.cast_mul, Nat.cast_add, Nat.cast_ofNat] using main

#print axioms discordant_mark_count
#print axioms discordant_uniform_mark_allowance

end CollatzShell.TernaryHead

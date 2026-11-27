import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Finite arithmetic behind gluing exact-clock inverse rows at ordinary targets. -/

namespace Collatz.RoundTen.ClockBlocks

/-- Number of shortcut steps from a positive odd input to its next odd state. -/
def gap (x : ℕ) := (3 * x + 1).factorization 2

def nextOdd (x : ℕ) := (3 * x + 1) / 2 ^ gap x

/-- Endpoint and elapsed shortcut clock after the specified number of odd gaps. -/
def walk : ℕ → ℕ → ℕ × ℕ
  | 0, x => (x, 0)
  | n + 1, x =>
    let tail := walk n (nextOdd x)
    (tail.1, gap x + tail.2)

theorem walk_add (n m x : ℕ) :
    walk (n + m) x =
      ((walk m (walk n x).1).1, (walk n x).2 + (walk m (walk n x).1).2) := by
  induction n generalizing x with
  | zero => simp [walk]
  | succ n ih => simp [Nat.succ_add, walk, ih, Nat.add_assoc]

/-- A source, intermediate endpoint, and block clock remain on the same orbit. -/
theorem concatenate {n m x a q u v : ℕ}
    (first : walk n x = (a, u)) (last : walk m a = (q, v)) :
    walk (n + m) x = (q, u + v) := by
  simp [walk_add, first, last]

/-- Different (cut vertex, cut clock) keys have disjoint source sets.  The two
blocks may include repeated vertices; the number of gaps before the cut is fixed. -/
theorem bank_cardinality {n : ℕ} (keys : Finset (ℕ × ℕ))
    (bank : ℕ × ℕ → Finset ℕ)
    (first : ∀ k ∈ keys, ∀ x ∈ bank k, walk n x = k) :
    (keys.biUnion bank).card = ∑ k ∈ keys, (bank k).card := by
  apply Finset.card_biUnion
  intro k hk l hl hkl
  apply Finset.disjoint_left.mpr
  intro x hx hy
  exact hkl ((first k hk x hx).symm.trans (first l hl x hy))

/-- A weighted subdivision can therefore sum the literal bank populations
without charging a complete source twice.  Only the selected finite ambient
set and the two block replay equations are needed. -/
theorem sum_le_row {n m q total : ℕ} (space : Finset ℕ)
    (keys : Finset (ℕ × ℕ)) (bank : ℕ × ℕ → Finset ℕ)
    (lastCost : ℕ × ℕ → ℕ)
    (first : ∀ k ∈ keys, ∀ x ∈ bank k, walk n x = k)
    (last : ∀ k ∈ keys, walk m k.1 = (q, lastCost k))
    (clock : ∀ k ∈ keys, k.2 + lastCost k = total)
    (bound : ∀ k ∈ keys, bank k ⊆ space) :
    (∑ k ∈ keys, (bank k).card) ≤
      (space.filter (fun x => walk (n + m) x = (q, total))).card := by
  rw [← bank_cardinality keys bank first]
  apply Finset.card_le_card
  intro x hx
  obtain ⟨k, hk, hmem⟩ := Finset.mem_biUnion.mp hx
  apply Finset.mem_filter.mpr
  refine ⟨bound k hk hmem, ?_⟩
  simpa [clock k hk] using concatenate (first k hk x hmem) (last k hk)

/-- One real-affine block of slope at most one half preserves the doubled
offset budget of the earlier blocks. -/
theorem bounded_offset {B offset earlier slope : ℚ}
    (hoff : offset ≤ B) (hprev : earlier ≤ 2 * B)
    (he : 0 ≤ earlier) (hs : slope ≤ 1 / 2) :
    offset + slope * earlier ≤ 2 * B := by
  nlinarith [mul_nonneg (sub_nonneg.mpr hs) he]

/-- Rearrange the additive height identity, over any field. In the application
L2 and L3 are log 2 and log 3, and X, G, and D are the logs of the source,
terminal and distortion. -/
theorem clock_balance {K : Type*} [Field K] (L2 L3 X G D n s : K)
    (nonzero : 2*L2 - L3 ≠ 0)
    (height : X = s*L2 - n*L3 + G - D) :
    (2 / (2*L2-L3)) * X - s =
      (L3 / (2*L2-L3)) * (s - 2*n) +
      (2 / (2*L2-L3)) * (G - D) := by
  rw [height]
  field_simp [nonzero]
  ring

#print axioms clock_balance
#print axioms walk_add
#print axioms concatenate
#print axioms bank_cardinality
#print axioms sum_le_row
#print axioms bounded_offset

end Collatz.RoundTen.ClockBlocks

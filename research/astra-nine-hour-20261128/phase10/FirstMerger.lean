import Mathlib.Logic.Function.Iterate
import Mathlib.Data.Nat.Basic
import Mathlib.NumberTheory.Padics.PadicVal.Basic

/-! Deterministic first-merger uniqueness at nonperiodic targets.
This is the graph-theoretic input behind the summable distinct-parent
collision injection on actual positive Collatz paths. -/
namespace Collatz.FirstMerger

variable {α : Type*}

def Nonperiodic (f : α → α) (y : α) : Prop :=
  ∀ n : ℕ, 0 < n → (f^[n]) y ≠ y

/-- A nonperiodic target is visited at at most one time from any source. -/
theorem hit_time_unique (f : α → α) {x y : α} (hy : Nonperiodic f y)
    {m n : ℕ} (hm : (f^[m]) x = y) (hn : (f^[n]) x = y) : m = n := by
  have ordered : ∀ a b : ℕ, (f^[a]) x = y → (f^[b]) x = y → a ≤ b → a = b := by
    intro a b ha hb hab
    by_contra hne
    have hpos : 0 < b-a := by omega
    apply hy (b-a) hpos
    calc
      (f^[b-a]) y = (f^[b-a]) ((f^[a]) x) := by rw [ha]
      _ = (f^[(b-a)+a]) x := (Function.iterate_add_apply f (b-a) a x).symm
      _ = y := by rw [Nat.sub_add_cancel hab, hb]
  rcases le_total m n with h | h
  · exact ordered m n hm hn h
  · exact (ordered n m hn hm h).symm

/-- Distinct incoming branches of a nonperiodic vertex have disjoint
ordinary predecessor cones. No probability assumption enters this lemma. -/
theorem parent_cones_disjoint (f : α → α) {u v y x : α}
    (hy : Nonperiodic f y) (hu : f u = y) (hv : f v = y) (hne : u ≠ v)
    (m n : ℕ) (hm : (f^[m]) x = u) (hn : (f^[n]) x = v) : False := by
  have hmu : (f^[m+1]) x = y := by rw [Function.iterate_succ_apply', hm, hu]
  have hnv : (f^[n+1]) x = y := by rw [Function.iterate_succ_apply', hn, hv]
  have hmn : m = n := by have := hit_time_unique f hy hmu hnv; omega
  apply hne
  rw [← hm, ← hn, hmn]

private theorem ordered_mergers (f : α → α) {a b y z : α}
    (hz : Nonperiodic f z) {m n p q : ℕ}
    (ha : (f^[m+1]) a = y) (hb : (f^[n+1]) b = y)
    (ha' : (f^[p+1]) a = z) (hb' : (f^[q+1]) b = z)
    (hne : (f^[p]) a ≠ (f^[q]) b) (hmp : m ≤ p) : y = z := by
  by_cases heq : m = p
  · rw [heq] at ha
    exact ha.symm.trans ha'
  · have hlt : m+1 ≤ p := by omega
    let d := p-(m+1)
    have hd : d+(m+1) = p := Nat.sub_add_cancel hlt
    have hparent : (f^[p]) a = (f^[d]) y := by
      rw [← hd, Function.iterate_add_apply, ha]
    have hother : (f^[d+(n+1)]) b = (f^[p]) a := by
      rw [Function.iterate_add_apply, hb, hparent]
    have hhit : (f^[(d+(n+1))+1]) b = z := by
      rw [Function.iterate_succ_apply', hother]
      exact (Function.iterate_succ_apply' f p a).symm.trans ha'
    have hq : q = d+(n+1) := by
      have := hit_time_unique f hz hb' hhit
      omega
    exact False.elim (hne (by rw [hq, hother]))

/-- Two ordered source paths cannot first merge through distinct parents
at two different nonperiodic targets. This makes the corresponding
source-pair events disjoint even when their individual clocks differ. -/
theorem merger_target_unique (f : α → α) {a b y z : α}
    (hy : Nonperiodic f y) (hz : Nonperiodic f z) {m n p q : ℕ}
    (ha : (f^[m+1]) a = y) (hb : (f^[n+1]) b = y)
    (ha' : (f^[p+1]) a = z) (hb' : (f^[q+1]) b = z)
    (hne : (f^[m]) a ≠ (f^[n]) b)
    (hne' : (f^[p]) a ≠ (f^[q]) b) : y = z := by
  rcases le_total m p with h | h
  · exact ordered_mergers f hz ha hb ha' hb' hne' h
  · exact (ordered_mergers f hy ha' hb' ha hb hne h).symm

/-- Once the common target is nonperiodic, both incoming vertices are
also fixed uniquely by the ordered pair of original sources. -/
theorem merger_parents_unique (f : α → α) {a b y : α}
    (hy : Nonperiodic f y) {m n p q : ℕ}
    (ha : (f^[m+1]) a = y) (hb : (f^[n+1]) b = y)
    (ha' : (f^[p+1]) a = y) (hb' : (f^[q+1]) b = y) :
    (f^[m]) a = (f^[p]) a ∧ (f^[n]) b = (f^[q]) b := by
  have hmp : m = p := by have := hit_time_unique f hy ha ha'; omega
  have hnq : n = q := by have := hit_time_unique f hy hb hb'; omega
  exact ⟨congrArg (fun k => (f^[k]) a) hmp, congrArg (fun k => (f^[k]) b) hnq⟩

/-- The actual accelerated odd Collatz formula; applications start at
positive odd integers. -/
def oddStep (x : ℕ) : ℕ := (3*x+1) / 2^(padicValNat 2 (3*x+1))

/-- The unique-merger statement specialized to the actual valuation-defined
odd map, with both source clocks retained separately. -/
theorem ordinary_merger_target_unique {a b y z : ℕ}
    (hy : Nonperiodic oddStep y) (hz : Nonperiodic oddStep z) {m n p q : ℕ}
    (ha : (oddStep^[m+1]) a = y) (hb : (oddStep^[n+1]) b = y)
    (ha' : (oddStep^[p+1]) a = z) (hb' : (oddStep^[q+1]) b = z)
    (hne : (oddStep^[m]) a ≠ (oddStep^[n]) b)
    (hne' : (oddStep^[p]) a ≠ (oddStep^[q]) b) : y = z :=
  merger_target_unique oddStep hy hz ha hb ha' hb' hne hne'

end Collatz.FirstMerger

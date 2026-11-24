import SelfEmbedding
import PolynomialPump

namespace PositivePolynomialBarrier
open PolynomialPump AYHSelfEmbedding

abbrev PositiveState := { s : State // ∀ i, 0 < s i }
def weakLe (s t : PositiveState) : Prop := ∀ i, s.val i ≤ t.val i
def strictLt (s t : PositiveState) : Prop := weakLe s t ∧ s.val 0 < t.val 0

/-- The usual distinguished-coordinate order on the positive orthant. -/
def interpretation (ops : ℕ → PositiveState → PositiveState)
    (wm : ∀ k {u v}, weakLe u v → weakLe (ops k u) (ops k v))
    (sm : ∀ k {u v}, strictLt u v → strictLt (ops k u) (ops k v)) :
    Algebra PositiveState where
  le := weakLe
  lt := strictLt
  refl _ _ := le_rfl
  trans h k i := le_trans (h i) (k i)
  le_lt h k := ⟨fun i => (h i).trans (k.1 i), (h 0).trans_lt k.2⟩
  lt_le h k := ⟨fun i => (h.1 i).trans (k i), h.2.trans_le (k 0)⟩
  irrefl _ h := (Nat.lt_irrefl _) h.2
  op := ops
  mono := wm
  strictMono := sm

/-- Only symbol 0 (binary zero) must have polynomial coordinates. The six
other symbols can be arbitrary context-monotone functions on positive triples. -/
theorem no_strict_rule (ops : ℕ → PositiveState → PositiveState)
    (wm : ∀ k {u v}, weakLe u v → weakLe (ops k u) (ops k v))
    (sm : ∀ k {u v}, strictLt u v → strictLt (ops k u) (ops k v))
    (f : Fin 3 → Expr) (hpoly : ∀ s i, (ops 0 s).val i = eval (f i) s.val)
    (hw : ∀ i, i < 11 → Weak (interpretation ops wm sm) i) (i : ℕ) (hi : i < 11) :
    ¬ Strict (interpretation ops wm sm) i := by
  have hused : uses (f 0) 0 := by
    apply used_of_strict
    intro s t hs hst hlt
    let sp : PositiveState := ⟨s,hs⟩
    let tp : PositiveState := ⟨t,fun j => (hs j).trans_le (hst j)⟩
    have h := (sm 0 (u:=sp) (v:=tp) ⟨hst,hlt⟩).2
    simpa only [hpoly] using h
  let start : PositiveState := ⟨fun _ => 1,fun _ => Nat.zero_lt_one⟩
  apply no_strict_rule_of_zero_stutter (interpretation ops wm sm) start hw _ i hi
  intro s j
  have hop (t : PositiveState) : (ops 0 t).val = step f t.val :=
    funext (hpoly t)
  change (ops 0 (ops 0 s)).val j ≤ (ops 0 (ops 0 (ops 0 (ops 0 s)))).val j
  simp only [hop]
  exact pump f hused s.val s.property j

#print axioms no_strict_rule
end PositivePolynomialBarrier

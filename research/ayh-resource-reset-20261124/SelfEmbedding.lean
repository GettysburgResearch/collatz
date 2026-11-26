import Std.Tactic

/-!
A checked all-rule self-embedding obstruction for the mixed-base Collatz SRS.
This proves a limitation of extensive ordered interpretations, not termination
or nontermination of the SRS. The certificate has 29 literal rewrite steps.
-/
namespace AYHSelfEmbedding

abbrev Word := List Nat

def rule : Nat → Word × Word
  | 0 => ([0,3], [3])
  | 1 => ([1,3], [6,3])
  | 2 => ([0,4], [4,0])
  | 3 => ([0,5], [4,1])
  | 4 => ([0,6], [5,0])
  | 5 => ([1,4], [5,1])
  | 6 => ([1,5], [6,0])
  | 7 => ([1,6], [6,1])
  | 8 => ([2,4], [2,1])
  | 9 => ([2,5], [2,0,0])
  | 10 => ([2,6], [2,0,1])
  | _ => ([], [])

/-- An ordered algebra with weak and strict comparisons.
All order and monotonicity assumptions are explicit, including context strictness. -/
structure Algebra (α : Type) where
  le : α → α → Prop
  lt : α → α → Prop
  refl : ∀ x, le x x
  trans : ∀ {x y z}, le x y → le y z → le x z
  le_lt : ∀ {x y z}, le x y → lt y z → lt x z
  lt_le : ∀ {x y z}, lt x y → le y z → lt x z
  irrefl : ∀ x, ¬ lt x x
  op : Nat → α → α
  mono : ∀ s {x y}, le x y → le (op s x) (op s y)
  strictMono : ∀ s {x y}, lt x y → lt (op s x) (op s y)

def eval {α} (A : Algebra α) : Word → α → α
  | [], x => x
  | s :: w, x => A.op s (eval A w x)

private theorem eval_append {α} (A : Algebra α) (u v : Word) (x : α) :
    eval A (u ++ v) x = eval A u (eval A v x) := by
  induction u with
  | nil => rfl
  | cons s u ih => simp only [List.cons_append, eval, ih]

private theorem eval_mono {α} (A : Algebra α) (w : Word) {x y : α}
    (h : A.le x y) : A.le (eval A w x) (eval A w y) := by
  induction w with
  | nil => exact h
  | cons s w ih => exact A.mono s ih

private theorem eval_strict {α} (A : Algebra α) (w : Word) {x y : α}
    (h : A.lt x y) : A.lt (eval A w x) (eval A w y) := by
  induction w with
  | nil => exact h
  | cons s w ih => exact A.strictMono s ih

private theorem sublist_le {α} (A : Algebra α) {u v : Word}
    (he : ∀ s x, A.le x (A.op s x))
    (h : u.Sublist v) (x : α) : A.le (eval A u x) (eval A v x) := by
  induction h with
  | slnil => exact A.refl x
  | cons s h ih => exact A.trans ih (he s _)
  | cons_cons s h ih => exact A.mono s ih

def Weak {α} (A : Algebra α) (i : Nat) :=
  ∀ x, A.le (eval A (rule i).2 x) (eval A (rule i).1 x)

def Strict {α} (A : Algebra α) (i : Nat) :=
  ∀ x, A.lt (eval A (rule i).2 x) (eval A (rule i).1 x)

private theorem contextual_weak {α} (A : Algebra α) (pre post : Word)
    {i : Nat} (h : Weak A i) (x : α) :
    A.le (eval A (pre ++ (rule i).2 ++ post) x)
         (eval A (pre ++ (rule i).1 ++ post) x) := by
  simp only [eval_append]
  exact eval_mono A pre (h _)

private theorem contextual_strict {α} (A : Algebra α) (pre post : Word)
    {i : Nat} (h : Strict A i) (x : α) :
    A.lt (eval A (pre ++ (rule i).2 ++ post) x)
         (eval A (pre ++ (rule i).1 ++ post) x) := by
  simp only [eval_append]
  exact eval_strict A pre (h _)

inductive Trace : Word → Word → List Nat → Prop where
  | nil (w : Word) : Trace w w []
  | step (pre post : Word) (i : Nat) (hi : i < 11)
      {v : Word} {is : List Nat}
      (tail : Trace (pre ++ (rule i).2 ++ post) v is) :
      Trace (pre ++ (rule i).1 ++ post) v (i :: is)

private theorem trace_weak {α} (A : Algebra α)
    (hw : ∀ i, i < 11 → Weak A i) {u v : Word} {is : List Nat}
    (tr : Trace u v is) (x : α) : A.le (eval A v x) (eval A u x) := by
  induction tr with
  | nil w => exact A.refl _
  | step pre post i hi tail ih =>
    exact A.trans ih (contextual_weak A pre post (hw i hi) x)

private theorem trace_strict {α} (A : Algebra α)
    (hw : ∀ i, i < 11 → Weak A i) {j : Nat} (hs : Strict A j)
    {u v : Word} {is : List Nat} (tr : Trace u v is) (hj : j ∈ is)
    (x : α) : A.lt (eval A v x) (eval A u x) := by
  induction tr with
  | nil w => simp at hj
  | step pre post i hi tail ih =>
    simp only [List.mem_cons] at hj
    rcases hj with h | h
    · subst j
      exact A.le_lt (trace_weak A hw tail x) (contextual_strict A pre post hs x)
    · exact A.lt_le (ih h) (contextual_weak A pre post (hw i hi) x)

def source : Word := [2,1,0,1,1,3]
def target : Word := [2,4,0,1,0,1,1,3]

def used : List Nat := [1, 7, 4, 6, 10, 1, 4, 3, 5, 3, 8, 0, 1, 7, 7, 7, 10, 1, 7, 7, 7, 4, 9, 1, 7, 7, 4, 3, 2]

theorem certificate : Trace source target used := by
  unfold source target used
  apply Trace.step [2,1,0,1] [] 1 (by decide)
  apply Trace.step [2,1,0] [3] 7 (by decide)
  apply Trace.step [2,1] [1,3] 4 (by decide)
  apply Trace.step [2] [0,1,3] 6 (by decide)
  apply Trace.step [] [0,0,1,3] 10 (by decide)
  apply Trace.step [2,0,1,0,0] [] 1 (by decide)
  apply Trace.step [2,0,1,0] [3] 4 (by decide)
  apply Trace.step [2,0,1] [0,3] 3 (by decide)
  apply Trace.step [2,0] [1,0,3] 5 (by decide)
  apply Trace.step [2] [1,1,0,3] 3 (by decide)
  apply Trace.step [] [1,1,1,0,3] 8 (by decide)
  apply Trace.step [2,1,1,1,1] [] 0 (by decide)
  apply Trace.step [2,1,1,1] [] 1 (by decide)
  apply Trace.step [2,1,1] [3] 7 (by decide)
  apply Trace.step [2,1] [1,3] 7 (by decide)
  apply Trace.step [2] [1,1,3] 7 (by decide)
  apply Trace.step [] [1,1,1,3] 10 (by decide)
  apply Trace.step [2,0,1,1,1] [] 1 (by decide)
  apply Trace.step [2,0,1,1] [3] 7 (by decide)
  apply Trace.step [2,0,1] [1,3] 7 (by decide)
  apply Trace.step [2,0] [1,1,3] 7 (by decide)
  apply Trace.step [2] [1,1,1,3] 4 (by decide)
  apply Trace.step [] [0,1,1,1,3] 9 (by decide)
  apply Trace.step [2,0,0,0,1,1] [] 1 (by decide)
  apply Trace.step [2,0,0,0,1] [3] 7 (by decide)
  apply Trace.step [2,0,0,0] [1,3] 7 (by decide)
  apply Trace.step [2,0,0] [1,1,3] 4 (by decide)
  apply Trace.step [2,0] [0,1,1,3] 3 (by decide)
  apply Trace.step [2] [1,0,1,1,3] 2 (by decide)
  exact Trace.nil _

theorem every_rule_used (i : Nat) (hi : i < 11) : i ∈ used := by
  simp only [used, List.mem_cons, List.not_mem_nil, or_false]
  omega

theorem source_embeds : source.Sublist target := by decide

/-- No one of the eleven rules can be uniformly strict in any extensive
context-compatible ordered algebra that weakly orients all eleven rules. -/
theorem no_strict_rule {α : Type} (A : Algebra α) (x : α)
    (he : ∀ s y, A.le y (A.op s y))
    (hw : ∀ i, i < 11 → Weak A i) (i : Nat) (hi : i < 11) :
    ¬ Strict A i := by
  intro hs
  have hlt := trace_strict A hw hs certificate (every_rule_used i hi) x
  have hle := sublist_le A he source_embeds x
  exact A.irrefl _ (A.lt_le hlt hle)

#print axioms certificate
#print axioms every_rule_used
#print axioms source_embeds
#print axioms no_strict_rule



/-- A reusable finite obstruction: strict rule use conflicts with a reverse
comparison between the two ends of a weakly oriented trace. -/
theorem no_strict_of_trace {α : Type} (A : Algebra α) (x : α)
    (hw : ∀ i, i < 11 → Weak A i) {u v : Word} {ids : List Nat}
    (tr : Trace u v ids) (hback : A.le (eval A u x) (eval A v x))
    (i : Nat) (hi : i ∈ ids) : ¬ Strict A i := by
  intro hs
  exact A.irrefl _ (A.lt_le (trace_strict A hw hs tr hi x) hback)

def source41 : Word := [2,0,1,0,0,1,3]
def target41 : Word := [2,0,1,0,0,0,0,1,3]

def used41 : List Nat := [1, 4, 3, 5, 3, 8, 0, 1, 7, 7, 7, 10, 1, 7, 7, 7, 4, 9, 1, 7, 7, 4, 3, 2, 8, 1, 7, 4, 6, 4, 6, 10]

theorem certificate41 : Trace source41 target41 used41 := by
  unfold source41 target41 used41
  apply Trace.step [2,0,1,0,0] [] 1 (by decide)
  apply Trace.step [2,0,1,0] [3] 4 (by decide)
  apply Trace.step [2,0,1] [0,3] 3 (by decide)
  apply Trace.step [2,0] [1,0,3] 5 (by decide)
  apply Trace.step [2] [1,1,0,3] 3 (by decide)
  apply Trace.step [] [1,1,1,0,3] 8 (by decide)
  apply Trace.step [2,1,1,1,1] [] 0 (by decide)
  apply Trace.step [2,1,1,1] [] 1 (by decide)
  apply Trace.step [2,1,1] [3] 7 (by decide)
  apply Trace.step [2,1] [1,3] 7 (by decide)
  apply Trace.step [2] [1,1,3] 7 (by decide)
  apply Trace.step [] [1,1,1,3] 10 (by decide)
  apply Trace.step [2,0,1,1,1] [] 1 (by decide)
  apply Trace.step [2,0,1,1] [3] 7 (by decide)
  apply Trace.step [2,0,1] [1,3] 7 (by decide)
  apply Trace.step [2,0] [1,1,3] 7 (by decide)
  apply Trace.step [2] [1,1,1,3] 4 (by decide)
  apply Trace.step [] [0,1,1,1,3] 9 (by decide)
  apply Trace.step [2,0,0,0,1,1] [] 1 (by decide)
  apply Trace.step [2,0,0,0,1] [3] 7 (by decide)
  apply Trace.step [2,0,0,0] [1,3] 7 (by decide)
  apply Trace.step [2,0,0] [1,1,3] 4 (by decide)
  apply Trace.step [2,0] [0,1,1,3] 3 (by decide)
  apply Trace.step [2] [1,0,1,1,3] 2 (by decide)
  apply Trace.step [] [0,1,0,1,1,3] 8 (by decide)
  apply Trace.step [2,1,0,1,0,1] [] 1 (by decide)
  apply Trace.step [2,1,0,1,0] [3] 7 (by decide)
  apply Trace.step [2,1,0,1] [1,3] 4 (by decide)
  apply Trace.step [2,1,0] [0,1,3] 6 (by decide)
  apply Trace.step [2,1] [0,0,1,3] 4 (by decide)
  apply Trace.step [2] [0,0,0,1,3] 6 (by decide)
  apply Trace.step [] [0,0,0,0,1,3] 10 (by decide)
  exact Trace.nil _

theorem every_rule_used41 (i : Nat) (hi : i < 11) : i ∈ used41 := by
  simp only [used41, List.mem_cons, List.not_mem_nil, or_false]
  omega

/-- Only the binary-zero operator needs the two-to-four iterate comparison.
All other symbols can reset auxiliary resources and need not be extensive. -/
theorem no_strict_rule_of_zero_stutter {α : Type} (A : Algebra α) (x : α)
    (hw : ∀ i, i < 11 → Weak A i)
    (ha : ∀ y, A.le (A.op 0 (A.op 0 y))
      (A.op 0 (A.op 0 (A.op 0 (A.op 0 y)))) )
    (i : Nat) (hi : i < 11) : ¬ Strict A i := by
  apply no_strict_of_trace A x hw certificate41 _ i (every_rule_used41 i hi)
  change A.le (eval A ([2,0,1] ++ [0,0] ++ [1,3]) x)
    (eval A ([2,0,1] ++ [0,0,0,0] ++ [1,3]) x)
  simp only [eval_append]
  exact eval_mono A [2,0,1] (ha _)

#print axioms no_strict_of_trace
#print axioms certificate41
#print axioms every_rule_used41
#print axioms no_strict_rule_of_zero_stutter

end AYHSelfEmbedding

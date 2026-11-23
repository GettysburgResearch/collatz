/-
Backward affine carries through an arbitrary supplied source context.

The entire carry run is arithmetic data, with no bounded word alphabet or
bounded state space assumed.  Every successful run produces an actual prefix
and preserves the original complete tail.  A rank-decreasing completed run,
or an earlier captured interval, supplies the original induction query.
No theorem asserts that every source admits such a successful run.
-/
import Collatz.JointMinimalCounterexample

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzBoundedGapCofinal
open CollatzLowGapLoops

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzContextSurgery

/-- A backward carry lifts the old endpoint `m` to `2^d*m+B`.
After consuming original gap `a` with replacement gap `b`, its predecessor
becomes `2^nextD*n+nextB`.  The second equality is the exact ternary guard. -/
def CarryStep (a b d B nextD nextB : Nat) : Prop :=
  0<b ∧ a+nextD=d+b ∧ 3*nextB+1=2^nextD+2^b*B

theorem carry_step_identity (a b d B nextD nextB n m : Nat)
    (carry : CarryStep a b d B nextD nextB)
    (edge : 3*n+1=2^a*m) :
    3*(2^nextD*n+nextB)+1=2^b*(2^d*m+B) := by
  obtain ⟨_,powers,constant⟩ := carry
  have multiplied := congrArg (2^nextD*·) edge
  have factors : 2^nextD*2^a=2^b*2^d := by
    rw [←Nat.pow_add,←Nat.pow_add]
    congr 1
    omega
  grind

/-- Unbounded backward traversal.  The rightmost pair is processed first;
the four natural carry parameters retain both endpoint and source affine
maps.  No carry may be silently replaced at a word boundary. -/
inductive CarryWord : List Nat → List Nat → Nat → Nat → Nat → Nat → Prop
  | nil (d B : Nat) : CarryWord [] [] d B d B
  | cons {old new : List Nat} {a b d B middleD middleB sourceD sourceB : Nat}
      (tail : CarryWord old new d B middleD middleB)
      (step : CarryStep a b middleD middleB sourceD sourceB) :
      CarryWord (a::old) (b::new) d B sourceD sourceB

theorem carry_word_length {old new : List Nat} {d B sourceD sourceB : Nat}
    (carry : CarryWord old new d B sourceD sourceB) : old.length=new.length := by
  induction carry with
  | nil => rfl
  | cons _ _ ih => simp [ih]

theorem carry_word_clock {old new : List Nat} {d B sourceD sourceB : Nat}
    (carry : CarryWord old new d B sourceD sourceB) :
    total old+sourceD=d+total new := by
  induction carry with
  | nil => simp [total]
  | cons tail step ih =>
    obtain ⟨_,powers,_⟩ := step
    simp only [total]
    omega

/-- Compose arbitrary adjacent carry runs at their exact shared arithmetic
state.  In particular, a seed may be transported through an unbounded prefix. -/
theorem carry_word_append {oldFront newFront oldTail newTail : List Nat}
    {d B middleD middleB sourceD sourceB : Nat}
    (front : CarryWord oldFront newFront middleD middleB sourceD sourceB)
    (tail : CarryWord oldTail newTail d B middleD middleB) :
    CarryWord (oldFront++oldTail) (newFront++newTail) d B sourceD sourceB := by
  induction front with
  | nil => exact tail
  | cons previous step ih => exact CarryWord.cons (ih tail) step

theorem carry_word_prefix {old new : List Nat} {d B sourceD sourceB q endpoint : Nat}
    (carry : CarryWord old new d B sourceD sourceB)
    (path : Prefix q old endpoint) :
    Prefix (2^sourceD*q+sourceB) new (2^d*endpoint+B) := by
  induction carry generalizing q with
  | nil d B =>
    have same : q=endpoint := by simpa [Prefix,correction,total] using path.2
    subst q
    simp [Prefix,PositiveGaps,correction,total]
  | @cons old new a b d B middleD middleB sourceD sourceB tail step ih =>
    obtain ⟨_,m,edge,rest⟩ := (prefix_cons_iff q a endpoint old).mp path
    exact (prefix_cons_iff _ b _ new).mpr
      ⟨step.1,2^middleD*m+middleB,
        carry_step_identity a b middleD middleB sourceD sourceB q m step edge,
        ih rest⟩

/-- A completed carry starts from the unchanged splice endpoint.  The same
complete tail is appended after the newly proved actual prefix. -/
theorem carry_word_certificate {old new tail : List Nat} {sourceD sourceB q : Nat}
    (carry : CarryWord old new 0 0 sourceD sourceB)
    (cert : Certificate q (old++tail)) :
    Certificate (2^sourceD*q+sourceB) (new++tail) := by
  obtain ⟨endpoint,path,complete⟩ := split_certificate q old tail cert
  have lifted := carry_word_prefix carry path
  simp only [Nat.pow_zero,Nat.one_mul,Nat.add_zero] at lifted
  exact append_certificate lifted complete

/-- The replacement source never shrinks: its affine slope is a positive
integer power of two and its carried offset is nonnegative. -/
theorem carry_source_grows (q d B : Nat) : q≤2^d*q+B := by
  have power : 0<2^d := Nat.pow_pos (by decide)
  have base : q≤2^d*q := Nat.le_mul_of_pos_left q power
  omega

/-- Every successful lower-grade carry solves the full original interval.
There is no requirement to replay a target parity prefix or to bound the
number of carry states.  Completeness of such carries is not assumed. -/
theorem carry_interval_rule (source target e q sourceD sourceB : Nat)
    (old new tail : List Nat) (parent : source=2^e*q)
    (cert : Certificate q (old++tail)) (active : Interval source target)
    (carry : CarryWord old new 0 0 sourceD sourceB)
    (drop : Less (grades e (new++tail)) (grades e (old++tail)))
    (ih : CollatzGapComparison.Hyp Interval (grades e (old++tail))) : Basin target := by
  have child := carry_word_certificate carry cert
  have growth := Nat.mul_le_mul_left (2^e) (carry_source_grows q sourceD sourceB)
  have childActive : Interval (2^e*(2^sourceD*q+sourceB)) target := by
    constructor
    · exact active.1
    · have ceiling := active.2
      rw [parent] at ceiling
      omega
  exact ih _ target e (new++tail) childActive ⟨_,rfl,child⟩ drop

/-- A partially transformed suffix can finish immediately when its known
source captures the original target.  The unused original prefix is deleted,
not rebuilt.  This admits a successful exit before a dead inverse guard. -/
theorem suffix_exit_rule (target e f q endpoint d B : Nat)
    (discard old new tail : List Nat)
    (cert : Certificate q (discard++old++tail))
    (atSuffix : Prefix q discard endpoint)
    (carry : CarryWord old new 0 0 d B)
    (positive : 0<target) (captures : target≤2*(2^f*(2^d*endpoint+B))+1)
    (drop : Less (grades f (new++tail)) (grades e (discard++old++tail)))
    (ih : CollatzGapComparison.Hyp Interval (grades e (discard++old++tail))) :
    Basin target := by
  obtain ⟨u,split,complete⟩ := split_certificate q discard (old++tail)
    (by simpa [List.append_assoc] using cert)
  have same : u=endpoint := by
    have left := split.2
    have right := atSuffix.2
    have equal : 2^total discard*u=2^total discard*endpoint := by omega
    exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) equal
  subst u
  have child := carry_word_certificate carry complete
  exact ih _ target f (new++tail) ⟨positive,captures⟩ ⟨_,rfl,child⟩ drop

/-- A ternary-multiple lifted endpoint cannot be extended by any positive
gap, regardless of how large that gap is.  Increasing a gap after reaching
this dead endpoint cannot repair the carry. -/
theorem dead_endpoint (endpoint b predecessor : Nat)
    (dead : endpoint%3=0) : ¬(3*predecessor+1=2^b*endpoint) := by
  intro edge
  have reduced := congrArg (fun n : Nat => n%3) edge
  simp [Nat.add_mod,Nat.mul_mod,dead] at reduced

/-- Before a dead endpoint is reached, changing a chosen inverse gap by two
changes its predecessor to the genuine sibling `4*p+1`.  The next ternary
guard therefore moves by one, rather than remaining unchanged. -/
theorem raise_gap_two (endpoint b predecessor : Nat)
    (edge : 3*predecessor+1=2^b*endpoint) :
    3*(4*predecessor+1)+1=2^(b+2)*endpoint := by
  have multiplied := congrArg (4*·) edge
  rw [Nat.pow_add]
  grind

theorem raised_predecessor_residue (predecessor : Nat) :
    (4*predecessor+1)%3=(predecessor+1)%3 := by omega

/-- A concrete seed for the arbitrary-context carry machine.  It is useful
as a seed, not an exhaustive source-word cover. -/
theorem four_one_seed : CarryWord [4,1] [3,3] 0 0 1 3 := by
  apply CarryWord.cons (middleD:=2) (middleB:=1)
  · apply CarryWord.cons
    · exact CarryWord.nil 0 0
    · unfold CarryStep; decide
  · unfold CarryStep; decide

/-- The seed cannot be applied underneath even one unchanged gap.  This is
an all-context obstruction, not an experimental failure of one word length.
The preceding word must itself change, or the construction must exit early. -/
theorem unchanged_context_blocks_seed (word : List Nat) (q p endpoint : Nat)
    (nonempty : word≠[]) (old : Prefix q word endpoint) :
    ¬Prefix p word (2*endpoint+3) := by
  induction word generalizing q p with
  | nil => exact False.elim (nonempty rfl)
  | cons a word ih =>
    intro new
    obtain ⟨_,m,first,rest⟩ := (prefix_cons_iff q a endpoint word).mp old
    obtain ⟨_,n,second,changed⟩ := (prefix_cons_iff p a (2*endpoint+3) word).mp new
    by_cases empty : word=[]
    · subst word
      have oldEnd : m=endpoint := by simpa [Prefix,correction,total] using rest.2
      have newEnd : n=2*endpoint+3 := by simpa [Prefix,correction,total] using changed.2
      rw [oldEnd] at first
      rw [newEnd] at second
      have identity : 3*p+1=2*(3*q+1)+3*2^a := by grind
      omega
    · exact ih m n empty rest changed

private theorem seventy_seven_closed (p q a : Nat)
    (family : q=77 ∨ q=51 ∨ q=205 ∨ q=273)
    (positive : 0<a) (small : a≤3) (edge : 3*p+1=2^a*q) :
    p=77 ∨ p=51 ∨ p=205 ∨ p=273 := by
  have cases : a=1 ∨ a=2 ∨ a=3 := by omega
  rcases cases with one | two | three <;> subst a <;>
    rcases family with first | second | third | fourth <;> subst q <;>
    simp at edge <;> omega

/-- This finite set is the entire inverse tree of 77 using gaps at most
three.  Induction covers arbitrary word length, not a bounded orbit search. -/
theorem seventy_seven_predecessors (q : Nat) (word : List Nat)
    (path : Prefix q word 77) (bounded : ∀ a∈word, a≤3) :
    q=77 ∨ q=51 ∨ q=205 ∨ q=273 := by
  induction word generalizing q with
  | nil =>
    have same : q=77 := by simpa [Prefix,correction,total] using path.2
    exact Or.inl same
  | cons a word ih =>
    obtain ⟨positive,m,edge,rest⟩ := (prefix_cons_iff q a 77 word).mp path
    have family := ih m rest (by
      intro b member
      exact bounded b (by simp [member]))
    exact seventy_seven_closed q m a family positive (bounded a (by simp)) edge

/-- The tempting universal strategy "erase the internal four, then use
only gaps at most three until the source grows" already fails on this
actual source context.  The failed strategy is narrower than the complete
rank/target-dependent carry program. -/
theorem all_length_seed_growth_failure :
    Prefix 461 [3,3,2,2,4,1] 11 ∧
    ∀ p word, Prefix p word 77 → (∀ a∈word, a≤3) → ¬461≤p := by
  constructor
  · unfold Prefix PositiveGaps correction total
    decide
  · intro p word path bounded large
    have family := seventy_seven_predecessors p word path bounded
    omega

end CollatzContextSurgery

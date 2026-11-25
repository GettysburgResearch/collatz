module

public import HourEscapeCylinders
import all FixedGate

public section
namespace Collatz.Itinerary.HourEscape

open Sparse FixedGate ClockRecurrence
set_option autoImplicit false

/-- The exact outgoing gap at an odd orbit index. -/
def gapAt (a i : Nat) := (next (after i a)).1

def window (f : Nat → Nat) : Nat → Nat → List Nat
  | 0, _ => []
  | b+1, i => f i :: window f b (i+1)

private theorem actual_path {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (i b : Nat) : Path (window (gapAt a) b i) (after i a) (after (i+b) a) := by
  induction b generalizing i with
  | zero => simp [window,Path.nil]
  | succ b ih =>
    obtain ⟨_,_,_,oi,_⟩ := route_exists i a odd color
    have g := next_gap oi
    have successor : after (i+1) a=(next (after i a)).2 := by rw [after_add]; rfl
    rw [←successor] at g
    have rest := ih (i+1)
    rw [show i+1+b=i+(b+1) by omega] at rest
    exact .cons g rest

private theorem big_window {a : Nat} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (i b : Nat) : b≤(window (gapAt a) b i).sum := by
  induction b generalizing i with
  | zero => simp
  | succ b ih =>
    obtain ⟨_,_,_,oi,_⟩ := route_exists i a odd color
    have positive : 0<gapAt a i := (next_gap oi).pos
    simp only [window,List.sum_cons]
    have := ih (i+1)
    omega

private theorem same_window {f : Nat → Nat} {i j : Nat}
    (same : ∀ n, f (i+n)=f (j+n)) (b : Nat) : window f b i=window f b j := by
  induction b generalizing i j with
  | zero => rfl
  | succ b ih =>
    have eq := same 0
    simp only [Nat.add_zero] at eq
    simp only [window,eq,List.cons.injEq,true_and]
    exact ih (fun n => by simpa only [Nat.add_assoc] using same (1+n))

/-- Identical infinite forward gap tails on one ordinary orbit force the two
starting heights to agree. This step uses divisibility at one fixed pair. -/
theorem equal_of_same_gap_tail {a i j : Nat} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (same : ∀ n, gapAt a (i+n)=gapAt a (j+n)) :
    after i a=after j a := by
  let b := after i a+after j a+1
  let es := window (gapAt a) b i
  have pi : Path es (after i a) (after (i+b) a) := actual_path odd color i b
  have pj := actual_path odd color j b
  rw [←same_window same b] at pj
  change Path es (after j a) (after (j+b) a) at pj
  obtain ⟨_,_,_,oi,_⟩ := route_exists (i+b) a odd color
  obtain ⟨_,_,_,oj,_⟩ := route_exists (j+b) a odd color
  have clock : b≤es.sum := big_window odd color i b
  have high := Nat.lt_two_pow_self (n:=es.sum)
  have sourceI := route_exists i a odd color
  have sourceJ := route_exists j a odd color
  obtain ⟨_,_,_,ori,_⟩ := sourceI
  obtain ⟨_,_,_,orj,_⟩ := sourceJ
  by_cases cmp : after i a≤after j a
  · exact (Shadow.frozen_prefix pj pi cmp oj oi (by dsimp [b] at clock; omega)
      (by omega)).1.symm
  · exact (Shadow.frozen_prefix pi pj (by omega) oi oj (by dsimp [b] at clock; omega)
      (by omega)).1

private def language (G : Nat) : Nat → List (List Nat)
  | 0 => [[]]
  | b+1 => (List.range G).flatMap fun e => (language G b).map (e::·)

private theorem window_mem {G I : Nat} {f : Nat → Nat} (bound : ∀ n, I≤n → f n<G)
    (b i : Nat) (late : I≤i) : window f b i∈language G b := by
  induction b generalizing i with
  | zero => simp [language,window]
  | succ b ih =>
    apply List.mem_flatMap.mpr
    exact ⟨f i,List.mem_range.mpr (bound i late),
      List.mem_map.mpr ⟨window f b (i+1),ih _ (by omega),rfl⟩⟩

private theorem collision {G I : Nat} {f : Nat → Nat} (bound : ∀ n, I≤n → f n<G)
    (b : Nat) : ∃ i j, I≤i ∧ i<j ∧ window f b i=window f b j := by
  let words := language G b
  let w := fun n => window f b (I+n)
  apply Classical.byContradiction
  intro no
  have distinct : ((List.range (words.length+1)).map w).Nodup := by
    apply List.Pairwise.map _ _ List.nodup_range
    intro i j ne eqn
    by_cases lt : i<j
    · exact no ⟨I+i,I+j,by omega,by omega,eqn⟩
    · exact no ⟨I+j,I+i,by omega,by omega,eqn.symm⟩
  have inside : (List.range (words.length+1)).map w⊆words := by
    intro x mem
    obtain ⟨i,_,rfl⟩ := List.mem_map.mp mem
    exact window_mem bound _ _ (by omega)
  have := distinct.length_le_of_subset inside
  simp at this
  omega

private theorem extend_window (f : Nat → Nat) (b i : Nat) :
    window f (b+1) i=window f b i++[f (i+b)] := by
  induction b generalizing i with
  | zero => simp [window]
  | succ b ih =>
    change f i :: window f (b+1) (i+1)=
      (f i :: window f b (i+1))++[f (i+(b+1))]
    rw [List.cons_append,ih,show i+1+b=i+(b+1) by omega]

/-- An escaping ray with eventually bounded gaps has arbitrarily late
occurrences of the same length-b gap word with two different successors.
The two occurrences belong to the same fixed ordinary integer orbit. -/
theorem right_special_windows {a : Nat} {c : Bool} (odd : a%2=1)
    (color : a%3=digit c) (escape : ¬Repeats a) {G I : Nat}
    (bound : ∀ n, I≤n → gapAt a n<G) (b R : Nat) :
    ∃ i j, R≤i ∧ i<j ∧ window (gapAt a) b i=window (gapAt a) b j ∧
        gapAt a (i+b)≠gapAt a (j+b) := by
  let f := gapAt a
  apply Classical.byContradiction
  intro no
  have nextEq {i j : Nat} (hi : R≤i) (lt : i<j)
      (eqn : window f b i=window f b j) : f (i+b)=f (j+b) := by
    apply Classical.byContradiction
    intro ne
    exact no ⟨i,j,hi,lt,eqn,ne⟩
  obtain ⟨i,j,hi,lt,eqn⟩ := collision (I:=max I R)
    (fun n hn => bound n (Nat.le_trans (Nat.le_max_left ..) hn)) b
  have late : R≤i := Nat.le_trans (Nat.le_max_right ..) hi
  have matching (r : Nat) : window f b (i+r)=window f b (j+r) := by
    induction r with
    | zero => simpa using eqn
    | succ r ih =>
      have last := nextEq (i:=i+r) (j:=j+r) (by omega) (by omega) ih
      have whole : window f (b+1) (i+r)=window f (b+1) (j+r) := by
        rw [extend_window,extend_window,ih,last]
      exact congrArg List.tail whole
  have forever (r : Nat) : f (i+b+r)=f (j+b+r) := by
    have last := nextEq (i:=i+r) (j:=j+r) (by omega) (by omega) (matching r)
    simpa only [Nat.add_assoc,Nat.add_comm r b] using last
  have equal := equal_of_same_gap_tail (i:=i+b) (j:=j+b) odd color forever
  exact escape ⟨i+b,j-i,by omega,by rw [show i+b+(j-i)=j+b by omega,equal]⟩

#print axioms equal_of_same_gap_tail
#print axioms right_special_windows

end Collatz.Itinerary.HourEscape

import ShellCover

/-!
An explicit height-and-clock bound for the literal-tail alphabet-four
predecessor selector. The six-row arithmetic selector is from PR177,
a0a0d76f91b4e3846c1b1f0706cad56cb6098317,
research/lean-exact-witness-global-20261121/lean/Collatz/BoundedGapCofinal.lean.
The new proof uses pairwise distinctness and the first height crossing.
It does not prove a cap-three replacement or a universal interval cover.
-/

namespace CollatzShell.QuantitativeInverseSelector

set_option autoImplicit false
set_option maxHeartbeats 1200000

def selectedGap (q : Nat) : Nat :=
  match q % 18 with
  | 1 => 4 | 5 => 3 | 7 => 4 | 11 => 3 | 13 => 2 | _ => 1

def selectedPredecessor (q : Nat) : Nat :=
  match q % 18 with
  | 1 => 96*(q/18)+5
  | 5 => 48*(q/18)+13
  | 7 => 96*(q/18)+37
  | 11 => 48*(q/18)+29
  | 13 => 24*(q/18)+17
  | _ => 12*(q/18)+11

/-- Exact inherited selector, including nonterminality of the source-one row. -/
theorem selected_spec (q : Nat) (odd : q%2=1) (unit : q%3≠0) :
    0<selectedGap q ∧ selectedGap q≤4 ∧
    1<selectedPredecessor q ∧ selectedPredecessor q%2=1 ∧
    selectedPredecessor q%3≠0 ∧
    3*selectedPredecessor q+1=2^(selectedGap q)*q := by
  have residues : q%18=1 ∨ q%18=5 ∨ q%18=7 ∨ q%18=11 ∨
      q%18=13 ∨ q%18=17 := by omega
  rcases residues with h|h|h|h|h|h <;>
    simp only [selectedGap, selectedPredecessor, h] <;> norm_num <;> omega

/-- A positive odd gap is an exact ordinary path, at its stated shortcut clock. -/
theorem odd_gap_path (p q a : Nat) (odd : p%2=1) (positive : 0<a)
    (edge : 3*p+1=2^a*q) : orbit a p=q := by
  cases a with
  | zero => omega
  | succ a =>
    have first : step p=2^a*q := by
      rw [step,ite_eq_right (by omega)]
      rw [edge,pow_succ]
      have reorder : 2^a*2*q=2*(2^a*q) := by ring
      rw [reorder]
      omega
    simpa [orbit,first] using orbit_pad a q

private theorem power_prefix (b t q : Nat) (bound : t≤b) :
    orbit t (2^b*q)=2^(b-t)*q := by
  have form : 2^b*q=2^t*(2^(b-t)*q) := by
    rw [← mul_assoc,← pow_add]
    congr 2
    omega
  rw [form,orbit_pad]

/-- No hidden visit to one occurs before a selected nonterminal odd edge ends. -/
theorem odd_gap_nonterminal (p q a : Nat) (parent : 1<p) (target : 0<q)
    (odd : p%2=1) (positive : 0<a) (edge : 3*p+1=2^a*q) :
    ∀ t, t<a → orbit t p≠1 := by
  cases a with
  | zero => omega
  | succ a =>
    have first : step p=2^a*q := by
      rw [step,ite_eq_right (by omega),edge,pow_succ]
      have reorder : 2^a*2*q=2*(2^a*q) := by ring
      rw [reorder]
      omega
    intro t small
    cases t with
    | zero => simpa [orbit] using (by omega : p≠1)
    | succ t =>
      have tb : t≤a := by omega
      have ab : 1≤a-t := by omega
      have pbound : 2≤2^(a-t) := by
        simpa using Nat.pow_le_pow_right (by decide : 1≤(2:Nat)) ab
      have lower : 2≤2^(a-t)*q := by nlinarith
      simpa [orbit,first,power_prefix a t q tb] using (by omega : 2^(a-t)*q≠1)

noncomputable def firstTime (n : Nat) : Nat := by
  classical
  exact if h : Basin n then Nat.find h else 0

private theorem firstTime_hit (n : Nat) (h : Basin n) : orbit (firstTime n) n=1 := by
  simpa [firstTime,h] using Nat.find_spec h

private theorem firstTime_min (n t : Nat) (h : Basin n) (hit : orbit t n=1) :
    firstTime n≤t := by
  simpa [firstTime,h] using Nat.find_min' h hit

/-- A nonterminal inverse edge strictly raises the ordinary first-hit clock. -/
theorem firstTime_increases (p q a : Nat) (parent : 1<p) (target : 0<q)
    (odd : p%2=1) (positive : 0<a) (edge : 3*p+1=2^a*q)
    (known : Basin q) : Basin p ∧ firstTime q<firstTime p := by
  have path := odd_gap_path p q a odd positive edge
  have hp : Basin p := by
    obtain ⟨t,hit⟩ := known
    exact ⟨a+t,by rw [orbit_add,path,hit]⟩
  have phit := firstTime_hit p hp
  have atMost : a≤firstTime p := by
    by_contra h
    exact odd_gap_nonterminal p q a parent target odd positive edge
      (firstTime p) (by omega) phit
  have qhit : orbit (firstTime p-a) q=1 := by
    have split : firstTime p=a+(firstTime p-a) := by omega
    rw [split,orbit_add,path] at phit
    exact phit
  have lower := firstTime_min q (firstTime p-a) known qhit
  exact ⟨hp,by omega⟩

def walk (q : Nat) : Nat → Nat
  | 0 => q
  | k+1 => selectedPredecessor (walk q k)

def prefixWord (q : Nat) : Nat → List Nat
  | 0 => []
  | k+1 => selectedGap (walk q k)::prefixWord q k

/-- Actual odd-gap paths. The tail parameter is part of the proposition. -/
inductive GapPath : Nat → List Nat → Nat → Prop
  | nil (q : Nat) (odd : q%2=1) : GapPath q [] q
  | cons (p q r a : Nat) (tail : List Nat) (odd : p%2=1) (gap : 0<a)
      (edge : 3*p+1=2^a*q) (rest : GapPath q tail r) :
      GapPath p (a::tail) r

theorem GapPath.append {p q r : Nat} {front tail : List Nat}
    (left : GapPath p front q) (right : GapPath q tail r) :
    GapPath p (front++tail) r := by
  induction left with
  | nil _ _ => simpa using right
  | cons p q s a front odd gap edge rest ih =>
    exact GapPath.cons p q r a (front++tail) odd gap edge (ih right)

theorem GapPath.run {p q : Nat} {word : List Nat} (path : GapPath p word q) :
    orbit word.sum p=q := by
  induction path with
  | nil p _ => rfl
  | cons p q r a word odd gap edge _ ih =>
    simpa [List.sum_cons,orbit_add,odd_gap_path p q a odd gap edge] using ih

theorem GapPath.start_odd {p q : Nat} {word : List Nat} (path : GapPath p word q) :
    p%2=1 := by
  cases path with
  | nil _ odd => exact odd
  | cons _ _ _ _ _ odd _ _ _ => exact odd

/-- Every finite selected prefix is an actual positive odd word to the same root. -/
theorem walk_path (q k : Nat) (odd : q%2=1) (unit : q%3≠0) :
    (walk q k)%2=1 ∧ (walk q k)%3≠0 ∧
    GapPath (walk q k) (prefixWord q k) q ∧
    (prefixWord q k).length=k ∧
    (∀ a∈prefixWord q k, 0<a ∧ a≤4) ∧ (prefixWord q k).sum≤4*k := by
  induction k with
  | zero => exact ⟨odd,unit,GapPath.nil q odd,rfl,by simp [prefixWord],by simp [prefixWord]⟩
  | succ k ih =>
    obtain ⟨oldOdd,oldUnit,path,len,bounds,clock⟩ := ih
    obtain ⟨gap,cap,_,newOdd,newUnit,edge⟩ := selected_spec (walk q k) oldOdd oldUnit
    refine ⟨newOdd,newUnit,?_,?_,?_,?_⟩
    · exact GapPath.cons _ _ q _ _ newOdd gap edge path
    · simp [prefixWord,len]
    · intro a ha
      simp only [prefixWord,List.mem_cons] at ha
      rcases ha with rfl|ha
      · exact ⟨gap,cap⟩
      · exact bounds a ha
    · simp only [prefixWord,List.sum_cons]
      omega

private theorem walk_basin (q k : Nat) (odd : q%2=1) (unit : q%3≠0)
    (known : Basin q) : Basin (walk q k) := by
  obtain ⟨_,_,path,_,_,_⟩ := walk_path q k odd unit
  obtain ⟨t,hit⟩ := known
  exact ⟨(prefixWord q k).sum+t,by rw [orbit_add,path.run,hit]⟩

/-- Selected inverse vertices cannot repeat on a supplied basin component. -/
theorem walk_injective (q : Nat) (odd : q%2=1) (unit : q%3≠0)
    (known : Basin q) : Function.Injective (walk q) := by
  have mono : StrictMono (fun k => firstTime (walk q k)) := by
    apply strictMono_nat_of_lt_succ
    intro k
    obtain ⟨oldOdd,oldUnit,_,_,_,_⟩ := walk_path q k odd unit
    obtain ⟨gap,_,parent,newOdd,_,edge⟩ := selected_spec (walk q k) oldOdd oldUnit
    exact (firstTime_increases _ _ _ parent (by omega) newOdd gap edge
      (walk_basin q k odd unit known)).2
  intro i j eq
  exact mono.injective (congrArg firstTime eq)

def unitWindow (N : Nat) : Finset Nat :=
  (Finset.Icc 1 N).filter (fun n => n%2=1 ∧ n%3≠0)

/-- Pigeonhole gives an explicit inverse-depth budget, without an unknown
uniform bound on the hitting times of known basin members below N. -/
theorem crosses_within_window_card (q N : Nat) (odd : q%2=1) (unit : q%3≠0)
    (known : Basin q) : ∃ k, k≤(unitWindow N).card ∧ N<walk q k := by
  classical
  by_contra h
  have small : ∀ k, k≤(unitWindow N).card → walk q k≤N := by
    intro k bound
    by_contra big
    exact h ⟨k,bound,by omega⟩
  let index := Finset.range ((unitWindow N).card+1)
  have contained : index.image (walk q) ⊆ unitWindow N := by
    intro x mem
    obtain ⟨k,ki,rfl⟩ := Finset.mem_image.mp mem
    have kb : k≤(unitWindow N).card := by
      have h : k<(unitWindow N).card+1 := by simpa [index] using ki
      omega
    obtain ⟨ko,ku,_,_,_,_⟩ := walk_path q k odd unit
    have bound := small k kb
    simp only [unitWindow,Finset.mem_filter,Finset.mem_Icc]
    exact ⟨⟨by omega,bound⟩,ko,ku⟩
  have count := Finset.card_le_card contained
  rw [Finset.card_image_of_injective _ (walk_injective q odd unit known)] at count
  simp [index] at count

/-- All-bound first-crossing selector with exact height, depth, ordinary clock,
and literal inherited-tail guarantees. Only the supplied root certificate is used. -/
theorem bounded_window_literal_tail (q N : Nat) (tail : List Nat)
    (cert : GapPath q tail 1) (unit : q%3≠0) (initial : q≤N) :
    ∃ p word,
      N<p ∧ 3*p<16*N ∧ p%3≠0 ∧
      word.length≤(unitWindow N).card ∧ word.sum≤4*(unitWindow N).card ∧
      (∀ a∈word, 0<a ∧ a≤4) ∧ GapPath p (word++tail) 1 := by
  classical
  have odd := cert.start_odd
  have known : Basin q := ⟨tail.sum,cert.run⟩
  have existsCross : ∃ k, N<walk q k := by
    obtain ⟨k,_,h⟩ := crosses_within_window_card q N odd unit known
    exact ⟨k,h⟩
  let k := Nat.find existsCross
  have crossed : N<walk q k := Nat.find_spec existsCross
  have positive : 0<k := by
    by_contra h
    have zero : k=0 := by omega
    simp [zero,walk] at crossed
    omega
  obtain ⟨j,jbound,jcross⟩ := crosses_within_window_card q N odd unit known
  have kb : k≤(unitWindow N).card :=
    (Nat.find_min' existsCross jcross).trans jbound
  have previous : walk q (k-1)≤N := by
    have h := Nat.find_min existsCross (by omega : k-1<k)
    omega
  obtain ⟨po,pu,_,_,_,_⟩ := walk_path q (k-1) odd unit
  obtain ⟨_,gapCap,_,_,_,edge⟩ := selected_spec (walk q (k-1)) po pu
  have fourCap : 2^(selectedGap (walk q (k-1)))≤16 := by
    have h := Nat.pow_le_pow_right (by decide : 1≤(2:Nat)) gapCap
    simpa using h
  have lift : walk q k=selectedPredecessor (walk q (k-1)) := by
    have split : k=(k-1)+1 := by omega
    conv_lhs => rw [split]
    rfl
  have size : 3*walk q k<16*N := by
    rw [lift]
    have a := Nat.mul_le_mul fourCap previous
    omega
  obtain ⟨_,punit,path,len,bounds,clock⟩ := walk_path q k odd unit
  exact ⟨walk q k,prefixWord q k,crossed,size,punit,by omega,
    by omega,bounds,path.append cert⟩

end CollatzShell.QuantitativeInverseSelector

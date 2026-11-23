/-
Every complete alphabet-four certificate has one fixed absorbing tail, apart
from a finite terminal core. The factorization retains the supplied literal
word, including arbitrary terminal gap-two padding.
-/
import Collatz.LowIntervalRefinement

open CollatzReverseBasin CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzBoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 4000000
set_option maxRecDepth 100000

namespace CollatzBoundedFourNormalForm

/-- The unique nonterminal absorbing tail of the bounded-four inverse tree. -/
def elevenTail : List Nat := [1,2,3,4]

inductive Core
  | one | three | five | thirteen | seventeen | fortyFive | sixtyNine
  deriving DecidableEq

def coreValue : Core → Nat
  | .one => 1
  | .three => 3
  | .five => 5
  | .thirteen => 13
  | .seventeen => 17
  | .fortyFive => 45
  | .sixtyNine => 69

def coreWord : Core → List Nat
  | .one => []
  | .three => [1,4]
  | .five => [4]
  | .thirteen => [3,4]
  | .seventeen => [2,3,4]
  | .fortyFive => [3,2,3,4]
  | .sixtyNine => [4,3,4]

private theorem core_predecessor (c : Core) (n a : Nat)
    (positive : 0<a) (bounded : a≤4) (edge : 3*n+1=2^a*coreValue c) :
    (c=.one ∧ a=2 ∧ n=1) ∨
    (∃ d, n=coreValue d ∧ a::coreWord c=coreWord d) ∨
    (n=11 ∧ a::coreWord c=elevenTail) := by
  have acases : a=1 ∨ a=2 ∨ a=3 ∨ a=4 := by omega
  cases c with
  | one =>
    rcases acases with ha | ha | ha | ha <;> subst a
    · simp [coreValue] at edge; omega
    · left; exact ⟨rfl,rfl,by simp [coreValue] at edge; omega⟩
    · simp [coreValue] at edge; omega
    · right; left; exact ⟨.five,by simp [coreValue] at edge ⊢; omega,rfl⟩
  | three =>
    rcases acases with ha | ha | ha | ha <;> subst a <;>
      simp [coreValue] at edge <;> omega
  | five =>
    rcases acases with ha | ha | ha | ha <;> subst a
    · right; left; exact ⟨.three,by simp [coreValue] at edge ⊢; omega,rfl⟩
    · simp [coreValue] at edge; omega
    · right; left; exact ⟨.thirteen,by simp [coreValue] at edge ⊢; omega,rfl⟩
    · simp [coreValue] at edge; omega
  | thirteen =>
    rcases acases with ha | ha | ha | ha <;> subst a
    · simp [coreValue] at edge; omega
    · right; left; exact ⟨.seventeen,by simp [coreValue] at edge ⊢; omega,rfl⟩
    · simp [coreValue] at edge; omega
    · right; left; exact ⟨.sixtyNine,by simp [coreValue] at edge ⊢; omega,rfl⟩
  | seventeen =>
    rcases acases with ha | ha | ha | ha <;> subst a
    · right; right; exact ⟨by simp [coreValue] at edge; omega,rfl⟩
    · simp [coreValue] at edge; omega
    · right; left; exact ⟨.fortyFive,by simp [coreValue] at edge ⊢; omega,rfl⟩
    · simp [coreValue] at edge; omega
  | fortyFive =>
    rcases acases with ha | ha | ha | ha <;> subst a <;>
      simp [coreValue] at edge <;> omega
  | sixtyNine =>
    rcases acases with ha | ha | ha | ha <;> subst a <;>
      simp [coreValue] at edge <;> omega

/-- Exact normal form of the entire supplied certificate. No length or source
bound is imposed. The unbounded case is an actual odd prefix ending at 11. -/
theorem certificate_normal_form (n : Nat) (word : List Nat)
    (cert : Certificate n word) (bounded : ∀ a∈word, a≤4) :
    (∃ c k, n=coreValue c ∧ word=coreWord c++List.replicate k 2) ∨
    (∃ front k, Prefix n front 11 ∧
      word=front++elevenTail++List.replicate k 2) := by
  induction word generalizing n with
  | nil =>
    have one : n=1 := by simpa [Certificate,correction,total] using cert.2
    exact Or.inl ⟨.one,0,one,rfl⟩
  | cons a word ih =>
    obtain ⟨positive,q,edge,tail⟩ := (certificate_cons_iff n a word).mp cert
    have ab := bounded a (by simp)
    have tailBound : ∀ b∈word, b≤4 := fun b hb => bounded b (by simp [hb])
    rcases ih q tail tailBound with ⟨c,k,value,form⟩ | ⟨front,k,path,form⟩
    · rw [value] at edge
      rcases core_predecessor c n a positive ab edge with
        ⟨one,two,nOne⟩ | ⟨d,newValue,newWord⟩ | ⟨eleven,newWord⟩
      · subst c; subst a
        left
        refine ⟨.one,k+1,nOne,?_⟩
        simpa [coreWord,List.replicate_succ] using congrArg (2::·) form
      · left
        refine ⟨d,k,newValue,?_⟩
        rw [form,←List.cons_append,newWord]
      · right
        refine ⟨[],k,?_,?_⟩
        · exact ⟨by intro b hb; simp at hb,by simpa [correction,total] using eleven⟩
        · rw [form,←List.cons_append,newWord]
          rfl
    · right
      refine ⟨a::front,k,(prefix_cons_iff n a 11 front).mpr
        ⟨positive,q,edge,path⟩,?_⟩
      simpa [List.cons_append] using congrArg (a::·) form

theorem core_value_bound (c : Core) : coreValue c≤69 := by cases c <;> decide

/-- Every bounded-four source above the terminal core passes through the same
ordinary state 11, with the exact supplied terminal tail and padding. -/
theorem above_core_passes_eleven (n : Nat) (word : List Nat)
    (cert : Certificate n word) (bounded : ∀ a∈word, a≤4) (large : 69<n) :
    ∃ front k, Prefix n front 11 ∧ word=front++elevenTail++List.replicate k 2 := by
  rcases certificate_normal_form n word cert bounded with ⟨c,k,value,_⟩ | result
  · have small := core_value_bound c
    omega
  · exact result

/-- The fixed absorbing tail is an ordinary certificate, not a symbolic
endpoint whose convergence would have to be supplied separately. -/
theorem eleven_certificate : Certificate 11 elevenTail := by
  simp [elevenTail,Certificate,PositiveGaps,correction,total]

theorem canonical_certificate (n : Nat) (front : List Nat)
    (path : Prefix n front 11) : Certificate n (front++elevenTail) :=
  append_certificate path eleven_certificate

/-- The normalized prefix language is cofinal in the positive integers.
Every generated prefix is nonempty and preserves the same fixed tail. -/
theorem cofinal_eleven_prefixes (N : Nat) :
    ∃ q front, N<q ∧ front≠[] ∧ (∀ a∈front, a≤4) ∧ Prefix q front 11 := by
  obtain ⟨q,front,large,_,bounded,cert⟩ :=
    cofinal_predecessors 11 (max N 69) elevenTail eleven_certificate (by decide)
  obtain ⟨u,path,last⟩ :=
    CollatzLowGapLoops.split_certificate q front elevenTail cert
  have endpoint : u=11 := by
    have identity := last.2
    simp [elevenTail,correction,total] at identity
    omega
  subst u
  have largeN : N<q := by have h := Nat.le_max_left N 69; omega
  have largeCore : 69<q := by have h := Nat.le_max_right N 69; omega
  have nonempty : front≠[] := by
    intro empty
    have same : q=11 := by simpa [empty,correction,total] using path.2
    omega
  exact ⟨q,front,largeN,nonempty,bounded,path⟩

/-- The whole fixed tail, including an arbitrary common terminal padding,
cancels from the original complete-source grade. -/
theorem canonical_rank_cancel (e f k : Nat) (parent child : List Nat) :
    Less (grades f (child++elevenTail++List.replicate k 2))
      (grades e (parent++elevenTail++List.replicate k 2)) ↔
    Less (grades f child) (grades e parent) := by
  have cancel := less_append_right_iff (grades f child) (grades e parent)
    ((elevenTail++List.replicate k 2).map (2*·))
  simpa [grades,List.map_append,List.append_assoc] using cancel

/-- Removing a nonempty terminal cycle lowers the original supplied grade,
even though the represented source value is unchanged. -/
theorem terminal_padding_rank (e k : Nat) (word : List Nat) :
    Less (grades e word) (grades e (word++List.replicate (k+1) 2)) := by
  have nonempty : (List.replicate (k+1) 2).map (2*·) ≠ [] := by simp
  have drop : Less [] ((List.replicate (k+1) 2).map (2*·)) :=
    replace_many _ [] nonempty (by intro b hb; simp at hb)
  have carried := (less_append_left_iff (grades e word) []
    ((List.replicate (k+1) 2).map (2*·))).mpr drop
  simpa [grades,List.map_append,List.append_assoc] using carried

/-- An arbitrary positive terminal padding is eliminated outright by the
existing interval induction hypothesis. The target remains unchanged. -/
theorem terminal_padding_interval_rule (source target e q k : Nat)
    (front : List Nat) (parent : source=2^e*q) (path : Prefix q front 11)
    (active : Interval source target)
    (ih : CollatzGapComparison.Hyp Interval
      (grades e (front++elevenTail++List.replicate (k+1) 2))) : Basin target := by
  exact ih source target e (front++elevenTail) active
    ⟨q,parent,canonical_certificate q front path⟩
    (terminal_padding_rank e k (front++elevenTail))

private def reachesWithin (n : Nat) : Nat → Bool
  | 0 => n==1
  | k+1 => if n==1 then true else reachesWithin (shortcut n) k

private theorem reachesWithin_sound (n k : Nat) (hit : reachesWithin n k=true) :
    Basin n := by
  induction k generalizing n with
  | zero =>
    have one : n=1 := by simpa [reachesWithin] using hit
    subst n
    exact ⟨0,rfl⟩
  | succ k ih =>
    by_cases one : n=1
    · subst n; exact ⟨0,rfl⟩
    · have next : reachesWithin (shortcut n) k=true := by
        simpa [reachesWithin,one] using hit
      exact (CollatzClosure.basin_step n).mp (ih _ next)

/-- This finite range is forced by the seven terminal motifs and e<=3:
2*(2^3*69)+1=1105. The kernel checks the complete finite base in 113 clocks. -/
theorem terminal_core_range (n : Nat) (positive : 0<n) (small : n≤1105) :
    Basin n := by
  have finite : ∀ n : Fin 1106, n.val≠0 → reachesWithin n.val 113=true := by decide
  let v : Fin 1106 := ⟨n,by omega⟩
  have hit := finite v (by dsimp [v]; omega)
  exact reachesWithin_sound n 113 (by simpa [v] using hit)

/-- Every finite terminal motif is closed explicitly at every low initial
valuation, without invoking any unproved interval coverage premise. -/
theorem terminal_core_interval_rule (source target e : Nat) (c : Core)
    (parent : source=2^e*coreValue c) (small : e≤3)
    (active : Interval source target) : Basin target := by
  have powerBound : 2^e≤8 := Nat.pow_le_pow_right (by decide : 1≤2) small
  have sourceBound : source≤552 := by
    rw [parent]
    exact Nat.mul_le_mul powerBound (core_value_bound c)
  exact terminal_core_range target active.1 (by have upper := active.2; omega)

/-- The remaining low-interval obligation now has a single fixed endpoint
and a single fixed complete tail. There is no arbitrary supplied suffix and
no terminal gap-two padding. -/
def ElevenIntervalStep : Prop :=
  ∀ source target e q front, source=2^e*q → Prefix q front 11 → front≠[] →
    1≤e → e≤3 → (∀ a∈front, a≤4) → target%2=1 →
    source+1<target → target≤2*source+1 →
    CollatzGapComparison.Hyp Interval (grades e (front++elevenTail)) → Basin target

/-- Exact fixed-tail normalization of the entire residual interval problem.
All exceptional motifs and all nonempty terminal padding are already closed. -/
theorem low_interval_of_eleven (cover : ElevenIntervalStep) : LowIntervalStep := by
  intro source target e gaps cert epos esmall bounded targetOdd lower upper ih
  obtain ⟨q,parent,oddCert⟩ := cert
  have active : Interval source target := ⟨by omega,upper⟩
  rcases certificate_normal_form q gaps oddCert bounded with
    ⟨c,k,value,_⟩ | ⟨front,k,path,form⟩
  · exact terminal_core_interval_rule source target e c (by simpa [value] using parent)
      esmall active
  · cases k with
    | succ k =>
      subst gaps
      exact terminal_padding_interval_rule source target e q k front parent path active ih
    | zero =>
      simp only [List.replicate_zero,List.append_nil] at form
      subst gaps
      by_cases empty : front=[]
      · have eleven : q=11 := by simpa [empty,Prefix,total,correction] using path.2
        have powerBound : 2^e≤8 := Nat.pow_le_pow_right (by decide : 1≤2) esmall
        have sourceBound : source≤88 := by rw [parent,eleven]; omega
        exact terminal_core_range target active.1 (by omega)
      · apply cover source target e q front parent path empty epos esmall
          (fun a ha => bounded a (by simp [ha])) targetOdd lower upper ih

/-- The normalization is an equivalence: it does not strengthen the missing
coverage premise or change its original induction hypothesis. -/
theorem eleven_interval_of_low (cover : LowIntervalStep) : ElevenIntervalStep := by
  intro source target e q front parent path _ epos esmall bounded targetOdd lower upper ih
  have allBounded : ∀ a∈front++elevenTail, a≤4 := by
    intro a ha
    rcases List.mem_append.mp ha with old | fixed
    · exact bounded a old
    · simp only [elevenTail,List.mem_cons,List.not_mem_nil,or_false] at fixed
      omega
  exact cover source target e (front++elevenTail)
    ⟨q,parent,canonical_certificate q front path⟩ epos esmall allBounded
    targetOdd lower upper ih

theorem low_interval_iff_eleven : LowIntervalStep ↔ ElevenIntervalStep :=
  ⟨eleven_interval_of_low,low_interval_of_eleven⟩

/-- The sole premise is the named, still unproved nonempty-prefix-to-11
coverage statement. Every other interval case and terminal motif is closed. -/
theorem collatz_of_eleven_prefix (cover : ElevenIntervalStep) :
    ∀ n, 0<n → Basin n :=
  collatz_of_low_interval (low_interval_of_eleven cover)

end CollatzBoundedFourNormalForm

/-
Cofinal known predecessors over the fixed source alphabet {1,2,3,4}.
The construction preserves the complete supplied tail and gives an unguarded
high-gap rewrite in the interval comparison domain. Interval coverage with
all source gaps at most four remains a separate, unproved global assertion.
-/
import Collatz.GapComparison

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzSourceWitness

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzBoundedGapCofinal

private theorem unit_residue (r : Nat) (small : r<18)
    (odd : r%2=1) (unit : r%3≠0) :
    r=1 ∨ r=5 ∨ r=7 ∨ r=11 ∨ r=13 ∨ r=17 := by omega

/-- Every odd ternary unit has a nonterminal unit predecessor using gap at
most four. At q=1 the selected edge is 5 -> 1, not the terminal self-loop. -/
theorem unit_predecessor (q : Nat) (odd : q % 2 = 1) (unit : q % 3 ≠ 0) :
    ∃ a p, 0 < a ∧ a ≤ 4 ∧ 1 < p ∧ p % 2 = 1 ∧ p % 3 ≠ 0 ∧
      3*p+1 = 2^a*q := by
  have residues := unit_residue (q%18) (Nat.mod_lt q (by decide))
    (by rwa [Nat.mod_mod_of_dvd q (by decide : 2∣18)])
    (by rwa [Nat.mod_mod_of_dvd q (by decide : 3∣18)])
  clear odd unit
  rcases residues with h | h | h | h | h | h
  · refine ⟨4,96*(q/18)+5,by decide,by decide,by omega,by omega,by omega,?_⟩
    change 3*(96*(q/18)+5)+1=16*q
    omega
  · refine ⟨3,48*(q/18)+13,by decide,by decide,by omega,by omega,by omega,?_⟩
    change 3*(48*(q/18)+13)+1=8*q
    omega
  · refine ⟨4,96*(q/18)+37,by decide,by decide,by omega,by omega,by omega,?_⟩
    change 3*(96*(q/18)+37)+1=16*q
    omega
  · refine ⟨3,48*(q/18)+29,by decide,by decide,by omega,by omega,by omega,?_⟩
    change 3*(48*(q/18)+29)+1=8*q
    omega
  · refine ⟨2,24*(q/18)+17,by decide,by decide,by omega,by omega,by omega,?_⟩
    change 3*(24*(q/18)+17)+1=4*q
    omega
  · refine ⟨1,12*(q/18)+11,by decide,by decide,by omega,by omega,by omega,?_⟩
    change 3*(12*(q/18)+11)+1=2*q
    omega

/-- A nonterminal bounded-gap predecessor consumes a positive ordinary clock
from every supplied hitting certificate, with no choice of minimal clock. -/
theorem predecessor_clock (p q a clock : Nat) (parent : 1 < p)
    (_positive : 0 < q) (gap : 0 < a) (bound : a ≤ 4)
    (edge : 3*p+1=2^a*q) (hit : Hits p clock) :
    ∃ tail, tail < clock ∧ Hits q tail := by
  have twice : shortcut (2*q)=q := by simp [shortcut]
  have four : shortcut (4*q)=2*q := by
    rw [show 4*q=2*(2*q) by omega]
    simp [shortcut]
  have eight : shortcut (8*q)=4*q := by
    rw [show 8*q=2*(4*q) by omega]
    simp [shortcut]
  have cases : a=1 ∨ a=2 ∨ a=3 ∨ a=4 := by omega
  rcases cases with eq | eq | eq | eq <;> subst a
  · have first : shortcut p=q := by unfold shortcut; simp only [Nat.pow_one] at edge; split <;> omega
    have path : Trace p q [p] := by simp [Trace,first]
    obtain ⟨t,len,ht⟩ := trace_peel path (by intro x hx; simp at hx; omega) hit
    simp only [List.length_cons,List.length_nil] at len
    exact ⟨t,by omega,ht⟩
  · have first : shortcut p=2*q := by change 3*p+1=4*q at edge; unfold shortcut; split <;> omega
    have path : Trace p q [p,2*q] := by simp [Trace,first,twice]
    obtain ⟨t,len,ht⟩ := trace_peel path (by
      intro x hx; simp only [List.mem_cons,List.not_mem_nil,or_false] at hx; omega) hit
    simp only [List.length_cons,List.length_nil] at len
    exact ⟨t,by omega,ht⟩
  · have first : shortcut p=4*q := by change 3*p+1=8*q at edge; unfold shortcut; split <;> omega
    have path : Trace p q [p,4*q,2*q] := by simp [Trace,first,four,twice]
    obtain ⟨t,len,ht⟩ := trace_peel path (by
      intro x hx; simp only [List.mem_cons,List.not_mem_nil,or_false] at hx; omega) hit
    simp only [List.length_cons,List.length_nil] at len
    exact ⟨t,by omega,ht⟩
  · have first : shortcut p=8*q := by change 3*p+1=16*q at edge; unfold shortcut; split <;> omega
    have path : Trace p q [p,8*q,4*q,2*q] := by simp [Trace,first,eight,four,twice]
    obtain ⟨t,len,ht⟩ := trace_peel path (by
      intro x hx; simp only [List.mem_cons,List.not_mem_nil,or_false] at hx; omega) hit
    simp only [List.length_cons,List.length_nil] at len
    exact ⟨t,by omega,ht⟩

/-- Any finite interval has a common bound on the hitting clocks of its known
basin members. No convergence of the other integers is assumed. -/
theorem bounded_basin_clocks (N : Nat) :
    ∃ K, ∀ n, n ≤ N → Basin n → ∃ k, k ≤ K ∧ Hits n k := by
  classical
  induction N with
  | zero =>
    by_cases h : Basin 0
    · obtain ⟨k,hk⟩ := h
      refine ⟨k,?_⟩
      intro n hn _
      have eq : n=0 := by omega
      subst n
      exact ⟨k,by omega,hk⟩
    · refine ⟨0,?_⟩
      intro n hn hb
      have eq : n=0 := by omega
      subst n
      exact False.elim (h hb)
  | succ N ih =>
    obtain ⟨K,hK⟩ := ih
    by_cases h : Basin (N+1)
    · obtain ⟨j,hj⟩ := h
      refine ⟨K+j,?_⟩
      intro n hn hb
      by_cases old : n ≤ N
      · obtain ⟨k,hk,hit⟩ := hK n old hb
        exact ⟨k,by omega,hit⟩
      · have eq : n=N+1 := by omega
        subst n
        exact ⟨j,by omega,hj⟩
    · refine ⟨K,?_⟩
      intro n hn hb
      by_cases old : n ≤ N
      · exact hK n old hb
      · have eq : n=N+1 := by omega
        subst n
        exact False.elim (h hb)

/-- Arbitrarily long legal predecessor words over {1,2,3,4}, carrying the exact
original tail. Their length is a lower bound on every ordinary hitting clock. -/
theorem long_predecessor (q : Nat) (tail : List Nat) (cert : Certificate q tail)
    (unit : q%3≠0) (depth : Nat) :
    ∃ p word, p%3≠0 ∧ word.length=depth ∧ (∀ a ∈ word, a≤4) ∧
      Certificate p (word++tail) ∧ (∀ clock, Hits p clock → depth≤clock) := by
  induction depth with
  | zero => exact ⟨q,[],unit,rfl,by simp,by simpa using cert,by intro clock _; omega⟩
  | succ depth ih =>
    obtain ⟨p,word,pu,len,bound,pc,lower⟩ := ih
    have po : p%2=1 := witness_odd (certificate_witness pc)
    obtain ⟨a,n,apos,ab,nb,no,nu,edge⟩ := unit_predecessor p po pu
    have nc : Certificate n (a::(word++tail)) :=
      (certificate_cons_iff n a (word++tail)).mpr ⟨apos,p,edge,pc⟩
    refine ⟨n,a::word,nu,by simp [len],?_,by simpa using nc,?_⟩
    · intro b hb
      rcases List.mem_cons.mp hb with eq | mem
      · omega
      · exact bound b mem
    · intro clock hit
      obtain ⟨t,lt,ht⟩ := predecessor_clock n p a clock nb (by omega) apos ab edge hit
      have le := lower t ht
      omega

/-- A certified unit has arbitrarily large certified predecessors with only
gaps at most four before its literal supplied tail. No new residue guard. -/
theorem cofinal_predecessors (q N : Nat) (tail : List Nat)
    (cert : Certificate q tail) (unit : q%3≠0) :
    ∃ p word, N<p ∧ p%3≠0 ∧ (∀ a ∈ word, a≤4) ∧ Certificate p (word++tail) := by
  obtain ⟨K,hK⟩ := bounded_basin_clocks N
  obtain ⟨p,word,pu,_,bound,pc,lower⟩ := long_predecessor q tail cert unit (K+1)
  refine ⟨p,word,?_,pu,bound,pc⟩
  by_cases large : N<p
  · exact large
  have hp : p≤N := by omega
  obtain ⟨k,hk,hit⟩ := hK p hp (witness_basin (certificate_witness pc))
  have le := lower k hit
  omega

/-- Four is the sharp alphabet bound: every complete source certificate with
all gaps at most three represents one, regardless of its length. -/
theorem gaps_at_most_three (n : Nat) (word : List Nat)
    (cert : Certificate n word) (bound : ∀ a ∈ word, a≤3) : n=1 := by
  induction word generalizing n with
  | nil => simpa [Certificate,correction,total] using cert.2
  | cons a word ih =>
    obtain ⟨apos,q,edge,tail⟩ := (certificate_cons_iff n a word).mp cert
    have qb : ∀ b ∈ word, b≤3 := fun b hb => bound b (by simp [hb])
    have one := ih q tail qb
    have ab := bound a (by simp)
    have cases : a=1 ∨ a=2 ∨ a=3 := by omega
    rw [one] at edge
    rcases cases with eq | eq | eq <;> subst a <;> simp at edge <;> omega

/-- Exact fixed-alphabet threshold for cofinal known odd sources. -/
theorem cofinal_alphabet_iff (H : Nat) :
    (∀ N, ∃ p word, N<p ∧ Certificate p word ∧ (∀ a ∈ word, a≤H)) ↔ 4≤H := by
  constructor
  · intro h
    obtain ⟨p,word,large,cert,bound⟩ := h 1
    by_cases high : 4≤H
    · exact high
    have one := gaps_at_most_three p word cert (by
      intro a ha
      have le := bound a ha
      omega)
    omega
  · intro high N
    have one : Certificate 1 [] := by simp [Certificate,PositiveGaps,correction,total]
    obtain ⟨p,word,large,_,bound,cert⟩ := cofinal_predecessors 1 N [] one (by decide)
    refine ⟨p,word,large,by simpa using cert,?_⟩
    intro a ha
    exact Nat.le_trans (bound a ha) high

theorem certificate_suffix (n : Nat) (front tail : List Nat)
    (cert : Certificate n (front++tail)) : ∃ q, Certificate q tail := by
  induction front generalizing n with
  | nil => exact ⟨n,cert⟩
  | cons a front ih =>
    obtain ⟨_,q,_,rest⟩ := (certificate_cons_iff n a (front++tail)).mp cert
    exact ih q rest

/-- An arbitrary high gap ANYWHERE in the supplied source pays for a new
four-letter prefix above any requested bound. The full tail after that gap
is unchanged. No arithmetic entrance guard or insertion-length cap remains. -/
theorem high_gap_replacement (n a N : Nat) (front tail : List Nat)
    (cert : Certificate n (front++a::tail)) (high : 5≤a) :
    ∃ p word, N<p ∧ Certificate p (word++tail) ∧ (∀ b ∈ word, b≤4) ∧
      Less (grades 0 (word++tail)) (grades 0 (front++a::tail)) := by
  obtain ⟨u,rest⟩ := certificate_suffix n front (a::tail) cert
  obtain ⟨_,q,edge,tailCert⟩ := (certificate_cons_iff u a tail).mp rest
  have unit : q%3≠0 := by
    intro zero
    have h := congrArg (fun x : Nat => x%3) edge
    simp [Nat.add_mod,Nat.mul_mod,zero] at h
  obtain ⟨p,word,large,_,bound,child⟩ := cofinal_predecessors q N tail tailCert unit
  refine ⟨p,word,large,child,bound,?_⟩
  have member : 2*a ∈ (front++[a]).map (2*·) := by
    apply List.mem_map.mpr
    exact ⟨a,by simp,rfl⟩
  have nonempty : (front++[a]).map (2*·) ≠ [] := by
    intro eq
    rw [eq] at member
    simp at member
  have drop : Less (word.map (2*·)) ((front++[a]).map (2*·)) := by
    apply replace_many _ _ nonempty
    intro b hb
    obtain ⟨c,hc,eq⟩ := List.mem_map.mp hb
    have le := bound c hc
    exact ⟨2*a,member,by omega⟩
  have all := (less_append_right_iff (word.map (2*·)) ((front++[a]).map (2*·))
    (tail.map (2*·))).mpr drop
  simpa [grades,List.map_append,List.append_assoc] using all

/-- This larger active domain contains the desired psi and reverse-tripling
pairs. Enlarging the domain also enlarges its still-unproved low-gap cases. -/
def Interval (source target : Nat) : Prop := 0<target ∧ target≤2*source+1

theorem high_gap_interval_rule (source target a : Nat) (front tail : List Nat)
    (positive : 0<target) (cert : Certificate source (front++a::tail))
    (high : 5≤a)
    (ih : CollatzGapComparison.Hyp Interval (grades 0 (front++a::tail))) :
    Basin target := by
  obtain ⟨p,word,large,child,_,drop⟩ :=
    high_gap_replacement source a target front tail cert high
  exact ih p target 0 (word++tail) ⟨positive,by omega⟩ ⟨p,by simp,child⟩ drop

private theorem remove_even_grade (e : Nat) (gaps : List Nat) (positive : 0<e) :
    Less (grades 0 gaps) (grades e gaps) := by
  have drop := replace_one_with_tail (2*e+1) [] (gaps.map (2*·)) (by simp)
  simpa [grades,show e≠0 by omega] using drop

/-- An initial run of at least four halvings also pays for any number of
four-letter predecessor gaps. If the current odd source is a ternary
nonunit, consume its first odd edge to obtain a certified unit tail. -/
theorem large_even_replacement (source e N : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source e gaps) (high : 4≤e) :
    ∃ p word, N<p ∧ Certificate p word ∧
      Less (grades 0 word) (grades e gaps) := by
  obtain ⟨q,_,qc⟩ := cert
  cases gaps with
  | nil =>
    have one : q=1 := by simpa [Certificate,correction,total] using qc.2
    obtain ⟨p,word,large,_,bound,child⟩ :=
      cofinal_predecessors q N [] qc (by simp [one])
    refine ⟨p,word,large,by simpa using child,?_⟩
    have drop := even_to_odd_replacement e word [] (by omega) (by
      intro a ha
      exact Nat.le_trans (bound a ha) high)
    simpa using drop
  | cons a tail =>
    obtain ⟨_,u,edge,uc⟩ := (certificate_cons_iff q a tail).mp qc
    have unit : u%3≠0 := by
      intro zero
      have h := congrArg (fun x : Nat => x%3) edge
      simp [Nat.add_mod,Nat.mul_mod,zero] at h
    obtain ⟨p,word,large,_,bound,child⟩ := cofinal_predecessors u N tail uc unit
    have first := even_to_odd_replacement e word tail (by omega) (by
      intro b hb
      exact Nat.le_trans (bound b hb) high)
    have erase := replace_one_with_tail (2*a) [] (tail.map (2*·)) (by simp)
    have second : Less (grades e tail) (grades e (a::tail)) := by
      have h := (less_append_left_iff (if e=0 then [] else [2*e+1])
        (tail.map (2*·)) ((2*a)::tail.map (2*·))).mpr (by simpa using erase)
      simpa [grades] using h
    exact ⟨p,word++tail,large,child,less_trans first second⟩

/-- High odd gaps are removable even when the supplied source begins with
an arbitrary initial halving run. -/
theorem high_gap_powered_interval_rule (source target e a : Nat)
    (front tail : List Nat) (positive : 0<target)
    (cert : PoweredCertificate source e (front++a::tail)) (high : 5≤a)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++a::tail))) :
    Basin target := by
  obtain ⟨q,_,qc⟩ := cert
  obtain ⟨p,word,large,child,_,drop⟩ :=
    high_gap_replacement q a target front tail qc high
  have decrease : Less (grades 0 (word++tail)) (grades e (front++a::tail)) := by
    by_cases zero : e=0
    · simpa [zero] using drop
    · exact less_trans drop (remove_even_grade e (front++a::tail) (by omega))
  exact ih p target 0 (word++tail) ⟨positive,by omega⟩ ⟨p,by simp,child⟩ decrease

theorem large_even_interval_rule (source target e : Nat) (gaps : List Nat)
    (positive : 0<target) (cert : PoweredCertificate source e gaps) (high : 4≤e)
    (ih : CollatzGapComparison.Hyp Interval (grades e gaps)) : Basin target := by
  obtain ⟨p,word,large,child,drop⟩ := large_even_replacement source e target gaps cert high
  exact ih p target 0 word ⟨positive,by omega⟩ ⟨p,by simp,child⟩ drop

/-- The precise residual universal obligation after the unguarded cofinal
rewrites. Word length and source/target values remain unrestricted. This
definition is not a theorem asserting that the residual cases close. -/
def LowIntervalStep : Prop :=
  ∀ source target e gaps, PoweredCertificate source e gaps →
    1≤e → e≤3 → (∀ a∈gaps, a≤4) → target%2=1 →
    source+1<target → target≤2*source+1 →
    CollatzGapComparison.Hyp Interval (grades e gaps) → Basin target

/-- All other interval cases are covered: nonterminal odd sources, even
targets, targets at most source+1, every high odd gap, and every initial
halving run of length at least four. -/
theorem interval_complete_of_low (low : LowIntervalStep) :
    CollatzGapComparison.Complete Interval := by
  intro source target e gaps active cert ih
  obtain ⟨positive,upper⟩ := active
  by_cases one : source=1
  · have cases : target=1 ∨ target=2 ∨ target=3 := by omega
    rcases cases with eq | eq | eq <;> subst target
    · exact ⟨0,rfl⟩
    · exact ⟨1,rfl⟩
    · exact ⟨5,rfl⟩
  by_cases highGap : ∃ a∈gaps, 5≤a
  · obtain ⟨a,mem,high⟩ := highGap
    obtain ⟨front,tail,eq⟩ := List.mem_iff_append.mp mem
    subst gaps
    exact high_gap_powered_interval_rule source target e a front tail positive cert high ih
  have bounded : ∀ a∈gaps, a≤4 := by
    intro a ha
    have no : ¬5≤a := fun h => highGap ⟨a,ha,h⟩
    omega
  by_cases highEven : 4≤e
  · exact large_even_interval_rule source target e gaps positive cert highEven ih
  obtain ⟨q,eq,qc⟩ := cert
  have qo : q%2=1 := witness_odd (certificate_witness qc)
  have powered : PoweredCertificate source e gaps := ⟨q,eq,qc⟩
  by_cases zero : e=0
  · have value : source=q := by simpa [zero] using eq
    have odd : source%2=1 := by simpa [value] using qo
    have step : 2*shortcut source=3*source+1 := by
      unfold shortcut
      split <;> omega
    exact CollatzGapComparison.ordinary_source powered one ⟨positive,by omega⟩ ih
  obtain ⟨f,ef⟩ := Nat.exists_eq_succ_of_ne_zero zero
  have form : source=2*(2^f*q) := by rw [eq,ef,Nat.pow_succ]; grind
  have step : 2*shortcut source=source := by rw [form]; simp [shortcut]
  by_cases near : target≤source+1
  · exact CollatzGapComparison.ordinary_source powered one ⟨positive,by omega⟩ ih
  by_cases even : target%2=0
  · have child : Basin (target/2) :=
      CollatzGapComparison.ordinary_source powered one
        (show Interval (shortcut source) (target/2) from ⟨by omega,by omega⟩) ih
    have value : target=2*(target/2) := by omega
    rw [value]
    exact (basin_twice (target/2)).mpr child
  exact low source target e gaps powered (by omega) (by omega) bounded (by omega)
    (by omega) upper ih

/-- Conditional global closure, with its only remaining premise explicitly
restricted to the three low initial valuations and alphabet four. -/
theorem collatz_of_low_interval (low : LowIntervalStep) :
    ∀ n, 0<n → Basin n := by
  apply CollatzGapComparison.collatz_of_complete_psi (interval_complete_of_low low)
  intro source positive
  exact ⟨by omega,by omega⟩

end CollatzBoundedGapCofinal

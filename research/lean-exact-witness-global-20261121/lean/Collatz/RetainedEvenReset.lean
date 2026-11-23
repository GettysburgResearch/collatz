/-
Retaining a shorter initial even run removes a broad low-alphabet boundary.
The four prefix identities below are the complete inverse-two-run split for
ternary units, apart from q=1 and the dead cells q=7 mod9 and q=19 mod27.
Every source suffix and every target in the original interval are preserved.
-/
import Collatz.GapComparison

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzRetainedEvenReset

/-- A finite exact cover with an unbounded integer parameter: each surviving
unit tail has an ordinary predecessor at least twice as large, using gaps at
most three. The excluded cells are where the forced two-run dies too early. -/
theorem doubling_prefix (q : Nat) (positive : 0<q) (unit : q%3≠0)
    (nonterminal : q≠1) (not_first_dead : q%9≠7) (not_second_dead : q%27≠19) :
    ∃ p word, Prefix p word q ∧ (∀ a ∈ word, a≤3) ∧ 2*q≤p := by
  have cells : q%3=2 ∨ q%9=4 ∨ q%27=10 ∨ q%27=1 := by omega
  rcases cells with cell | cell | cell | cell
  · let p := (8*q-1)/3
    have equation : 3*p+1=8*q := by dsimp [p]; omega
    refine ⟨p,[3],⟨by simp [PositiveGaps],?_⟩,?_,by omega⟩
    · simpa [correction,total] using equation
    · intro a ha
      have eq : a=3 := by simpa using ha
      omega
  · let p := (32*q-11)/9
    have equation : 9*p+11=32*q := by dsimp [p]; omega
    refine ⟨p,[3,2],⟨by simp [PositiveGaps],?_⟩,?_,by omega⟩
    · simpa [correction,total] using equation
    · intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega
  · let p := (128*q-65)/27
    have equation : 27*p+65=128*q := by dsimp [p]; omega
    refine ⟨p,[3,2,2],⟨by simp [PositiveGaps],?_⟩,?_,by omega⟩
    · simpa [correction,total] using equation
    · intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega
  · let p := (64*q-37)/27
    have large : 28≤q := by omega
    have equation : 27*p+37=64*q := by dsimp [p]; omega
    refine ⟨p,[2,2,2],⟨by simp [PositiveGaps],?_⟩,?_,by omega⟩
    · simpa [correction,total] using equation
    · intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega

/-- The removed grade seven pays both for the retained even-run grade five
and for every new odd-source grade, which is at most six. -/
theorem retained_even_rank (word tail : List Nat) (bounded : ∀ a ∈ word, a≤3) :
    Less (grades 2 (word++tail)) (grades 3 tail) := by
  have below : ∀ b ∈ 5::word.map (2*·), b<7 := by
    intro b hb
    rcases List.mem_cons.mp hb with eq | mem
    · omega
    · obtain ⟨a,ha,eq⟩ := List.mem_map.mp mem
      have bound := bounded a ha
      omega
  have drop := replace_one_with_tail 7 (5::word.map (2*·)) (tail.map (2*·)) below
  simpa [grades,List.map_append] using drop

/-- Complete supplied-witness reset from 8q to 4p≥8q. Since the source grows,
every target t≤2S+1 remains in the same interval without any target rewrite.
The terminal q=1 and the two early dead cells remain explicitly excluded. -/
theorem whole_witness_interval_reset (S t : Nat) (tail : List Nat)
    (cert : PoweredCertificate S 3 tail) (target_positive : 0<t) (target_bound : t≤2*S+1)
    (unit : (S/8)%3≠0) (nonterminal : S/8≠1)
    (not_first_dead : (S/8)%9≠7) (not_second_dead : (S/8)%27≠19) :
    ∃ S' word, S≤S' ∧ PoweredCertificate S' 2 (word++tail) ∧
      Less (grades 2 (word++tail)) (grades 3 tail) ∧
      0<t ∧ t≤2*S'+1 := by
  obtain ⟨q,parent,tailCert⟩ := cert
  have parent' : S=8*q := by simpa using parent
  have quotient : S/8=q := by omega
  rw [quotient] at unit nonterminal not_first_dead not_second_dead
  have odd := witness_odd (certificate_witness tailCert)
  have positive : 0<q := by omega
  obtain ⟨p,word,path,bounded,large⟩ :=
    doubling_prefix q positive unit nonterminal not_first_dead not_second_dead
  have childCert := append_certificate path tailCert
  have enlarged : S≤4*p := by omega
  refine ⟨4*p,word,enlarged,⟨p,rfl,childCert⟩,retained_even_rank word tail bounded,
    target_positive,?_⟩
  omega

end CollatzRetainedEvenReset

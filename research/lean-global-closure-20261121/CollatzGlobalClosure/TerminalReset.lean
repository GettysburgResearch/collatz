/-
Every power-of-two source is a closed case of the common source-certificate
induction. Large exponents transfer to the explicit certificate of three;
the four small parent exponents close by literal ordinary trajectories.
This is an induction step, not a stand-alone proof of all Mersenne convergence.
-/
import CollatzGlobalClosure.AsynchronousReset

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzUnboundedGapReset CollatzAsynchronousReset

set_option autoImplicit false
set_option maxHeartbeats 4000000

namespace CollatzTerminalReset

/-- Spend a positive number of the parent's actual initial target odd steps,
using an explicit complete certificate of the corresponding power of three.
All terminal padding supplied by the caller is retained literally. -/
theorem power_transfer {e j : Nat} {word tail : List Nat}
    (hj : 0<j) (hle : j≤e) (seed : Certificate (3^j) word)
    (bound : ∀ a ∈ word, a≤e) (terminal : Certificate 1 tail) :
    PoweredCertificate (2^(e-j)*3^j) (e-j) (word++tail) ∧
      Less (grades (e-j) (word++tail)) (grades e tail) ∧
      (Basin (2*(2^(e-j)*3^j)-1) ↔ Basin (2*2^e-1)) := by
  have he : 0<e := by omega
  have seedPath : WordPath (3^j) 1 word :=
    word_path_of_identity seed.1 (by simpa using seed.2)
  have childCert := word_path_prepend_certificate seedPath terminal
  let front := (if e-j=0 then [] else [2*(e-j)+1])++word.map (2*·)
  have smaller : ∀ a ∈ front, a<2*e+1 := by
    intro a ha
    rcases List.mem_append.mp ha with initial | odd
    · by_cases zero : e-j=0
      · simp [zero] at initial
      · have eq : a=2*(e-j)+1 := by simpa [zero] using initial
        omega
    · obtain ⟨b,hb,eq⟩ := List.mem_map.mp odd
      have limit := bound b hb
      omega
  have drop := replace_one_with_tail (2*e+1) front (tail.map (2*·)) smaller
  have rank : Less (grades (e-j) (word++tail)) (grades e tail) := by
    simpa [grades,front,List.map_append,List.append_assoc,show e≠0 by omega] using drop
  have merge := parent_target_component (e:=e) (j:=j) (q:=1) (by omega) (by decide)
  have exponent : e+1-j=(e-j)+1 := by omega
  have value : 3^j*2^(e+1-j)*1=2*(2^(e-j)*3^j) := by
    rw [exponent,Nat.pow_succ]
    grind
  rw [Nat.mul_one,value] at merge
  exact ⟨⟨3^j,rfl,childCert⟩,rank,merge.symm⟩

theorem three_seed : Certificate 3 [1,4] := by
  constructor
  · intro a ha; simp at ha; omega
  · decide

/-- All parent exponents at least four, including every even exponent, have
one lower-ranked powered child. No search for a Mersenne target is used. -/
theorem all_large_powers (e : Nat) (tail : List Nat) (high : 4≤e)
    (terminal : Certificate 1 tail) :
    PoweredCertificate (2^(e-1)*3) (e-1) ([1,4]++tail) ∧
      Less (grades (e-1) ([1,4]++tail)) (grades e tail) ∧
      (Basin (2*(2^(e-1)*3)-1) ↔ Basin (2*2^e-1)) := by
  have h := power_transfer (e:=e) (j:=1) (by decide) (by omega)
    (show Certificate (3^1) [1,4] from three_seed)
    (by intro a ha; simp at ha; omega) terminal
  simpa using h

/-- The complete terminal-source case of a well-founded psi dispatcher.
Its hypothesis is exactly the induction hypothesis on smaller full source
certificates; it does not assert that every other case has been covered. -/
theorem terminal_case (e : Nat) (tail : List Nat) (terminal : Certificate 1 tail)
    (ih : ∀ source evenRun word, PoweredCertificate source evenRun word →
      Less (grades evenRun word) (grades e tail) → Basin (2*source-1)) :
    Basin (2*2^e-1) := by
  by_cases high : 4≤e
  · obtain ⟨child,drop,merge⟩ := all_large_powers e tail high terminal
    exact merge.mp (ih _ _ _ child drop)
  · have cases : e=0 ∨ e=1 ∨ e=2 ∨ e=3 := by omega
    rcases cases with eq | eq | eq | eq <;> subst e
    · exact ⟨0,rfl⟩
    · exact ⟨5,rfl⟩
    · exact ⟨11,rfl⟩
    · exact ⟨12,rfl⟩

#print axioms power_transfer
#print axioms three_seed
#print axioms all_large_powers
#print axioms terminal_case

end CollatzTerminalReset

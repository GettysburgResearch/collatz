/-
Total first-gap handoffs between reverse tripling and the comparison
Hplus(n): Basin n -> Basin (2*n+1).

Every supplied R3 first gap at least three is handled, with no extra congruence
guard: the child replaces that gap by a-2 and retains the complete tail.
Hplus still needs its own complete dispatcher; it is not assumed proved here.
-/
import Collatz.GapComparison

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset

namespace CollatzGapHandoffs

/-- The source-one Hplus query has an explicit ordinary terminal proof. -/
theorem hplus_one : Basin (2*1+1) := ⟨5,rfl⟩

/-- A total high-gap R3 handoff. The exact input certificate forces every
integrality guard, and the first gap alone strictly decreases. -/
theorem reverse_high_handoff (n a : Nat) (tail : List Nat)
    (cert : Certificate (3*n) (a::tail)) (high : 3 ≤ a) :
    ∃ p, 3*n = 4*p+1 ∧ Certificate p ((a-2)::tail) ∧
      Less (grades 0 ((a-2)::tail)) (grades 0 (a::tail)) ∧
      (Basin n ↔ Basin (2*p+1)) := by
  obtain ⟨_,u,first,tailCert⟩ := (certificate_cons_iff (3*n) a tail).mp cert
  have eight : 2^a = 8*2^(a-3) := by
    calc
      2^a = 2^(3+(a-3)) := by congr 1; omega
      _ = 2^3*2^(a-3) := Nat.pow_add 2 3 (a-3)
      _ = _ := rfl
  have sourceEq : 9*n+1 = 8*(2^(a-3)*u) := by rw [eight] at first; grind
  have residue : n % 8 = 7 := by omega
  let p := 6*(n/8)+5
  have parent : 3*n = 4*p+1 := by dsimp [p]; omega
  have four : 2^a = 4*2^(a-2) := by
    calc
      2^a = 2^(2+(a-2)) := by congr 1; omega
      _ = 2^2*2^(a-2) := Nat.pow_add 2 2 (a-2)
      _ = _ := rfl
  have childEq : 3*p+1 = 2^(a-2)*u := by
    rw [parent,four] at first
    grind
  have child : Certificate p ((a-2)::tail) :=
    (certificate_cons_iff p (a-2) tail).mpr ⟨by omega,u,childEq,tailCert⟩
  have drop := odd_to_odd_replacement a [a-2] tail (by
    intro b hb
    have eq : b = a-2 := by simpa using hb
    omega)
  have step : shortcut n = 2*p+1 := by unfold shortcut; split <;> omega
  refine ⟨p,parent,child,by simpa using drop,?_⟩
  have move := (basin_step n).symm
  rwa [step] at move

/-- Hplus consumes a first gap of one and remains Hplus on the exact supplied
source suffix. No new convergence witness is selected. -/
theorem hplus_gap_one (n : Nat) (tail : List Nat)
    (cert : Certificate n (1::tail)) :
    ∃ u, Certificate u tail ∧
      Less (grades 0 tail) (grades 0 (1::tail)) ∧
      (Basin (2*n+1) ↔ Basin (2*u+1)) := by
  obtain ⟨_,u,first,tailCert⟩ := (certificate_cons_iff n 1 tail).mp cert
  have drop := odd_to_odd_replacement 1 [] tail (by intro b hb; simp at hb)
  have step : shortcut (2*n+1) = 2*u+1 := by unfold shortcut; split <;> omega
  refine ⟨u,tailCert,by simpa using drop,?_⟩
  have move := (basin_step (2*n+1)).symm
  rwa [step] at move

/-- Hplus closes outright at a first source gap of two: its target has an
ordinary merger with the certified source suffix. -/
theorem hplus_gap_two (n : Nat) (tail : List Nat)
    (cert : Certificate n (2::tail)) : Basin (2*n+1) := by
  obtain ⟨_,u,first,tailCert⟩ := (certificate_cons_iff n 2 tail).mp cert
  have odd : u % 2 = 1 := witness_odd (certificate_witness tailCert)
  have base : Basin u := witness_basin (certificate_witness tailCert)
  have targetStep : shortcut (2*n+1) = 4*u+1 := by unfold shortcut; split <;> omega
  have middle : Basin (4*u+1) :=
    (basin_exch (4*u+1) (3*u+1) u rfl rfl).mpr ((basin_odd u odd).mpr base)
  have move := basin_step (2*n+1)
  rw [targetStep] at move
  exact move.mp middle

open CollatzGapComparison

/-- The total high-gap handoff is a concrete rule in the shared source/target
comparison kernel, provided its Hplus child belongs to the active domain. -/
theorem apply_reverse_high {active : Active} (n a : Nat) (tail : List Nat)
    (cert : Certificate (3*n) (a::tail)) (high : 3 ≤ a)
    (activated : ∀ p, 3*n = 4*p+1 → active p (2*p+1))
    (ih : Hyp active (grades 0 (a::tail))) : Basin n := by
  obtain ⟨p,parent,child,drop,merge⟩ := reverse_high_handoff n a tail cert high
  have powered : PoweredCertificate p 0 ((a-2)::tail) := ⟨p,by simp,child⟩
  exact CollatzGapComparison.one_query (activated p parent) powered drop merge.mpr ih

theorem apply_hplus_gap_one {active : Active} (n : Nat) (tail : List Nat)
    (cert : Certificate n (1::tail))
    (activated : ∀ u, Certificate u tail → active u (2*u+1))
    (ih : Hyp active (grades 0 (1::tail))) : Basin (2*n+1) := by
  obtain ⟨u,child,drop,merge⟩ := hplus_gap_one n tail cert
  have powered : PoweredCertificate u 0 tail := ⟨u,by simp,child⟩
  exact CollatzGapComparison.one_query (activated u child) powered drop merge.mpr ih

end CollatzGapHandoffs

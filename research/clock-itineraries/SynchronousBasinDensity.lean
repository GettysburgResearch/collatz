module

public import SynchronousBasinCount
import all SynchronousBasinCount
import all TernaryItinerary

public section
namespace Collatz.Itinerary.SynchronousBasinDensity

open SynchronousBasinCount SynchronousBasin
set_option autoImplicit false

/-- Full Collatz, matching the convention in Mazur's predecessor theorem. -/
def fullStep (n : Nat) := if n%2=0 then n/2 else 3*n+1
def fullRun : Nat → Nat → Nat
  | 0, x => x
  | h+1, x => fullRun h (fullStep x)

/-- Skipping the even intermediate 3n+1 preserves every visit to an odd target. -/
theorem odd_target_transfer (h n b : Nat) (odd : b%2=1) (hit : fullRun h n=b) :
    ∃ j, run j n=b := by
  induction h using Nat.strongRecOn generalizing n with
  | ind h ih =>
    cases h with
    | zero => exact ⟨0,hit⟩
    | succ h =>
      by_cases even : n%2=0
      · have same : fullStep n=step n := by simp [fullStep,step,even]
        change fullRun h (fullStep n)=b at hit
        rw [same] at hit
        obtain ⟨j,path⟩ := ih h (by omega) _ hit
        exact ⟨j+1,path⟩
      · have f : fullStep n=3*n+1 := by simp [fullStep,even]
        have parity : (3*n+1)%2=0 := by omega
        cases h with
        | zero =>
          change fullStep n=b at hit
          rw [f] at hit; omega
        | succ h =>
          change fullRun h (fullStep (fullStep n))=b at hit
          have twice : fullStep (fullStep n)=step n := by simp [fullStep,step,even,parity]
          rw [twice] at hit
          obtain ⟨j,path⟩ := ih h (by omega) _ hit
          exact ⟨j+1,path⟩

/-- Integer reciprocal form of positive lower density for full-map
predecessors of each fixed odd ternary unit, with a target-dependent cutoff. -/
def PositivePredecessorDensity : Prop :=
  ∀ b, b%2=1 → b%3≠0 → ∃ K A, ∀ X, A≤X → ∃ xs : List Nat,
    xs.Nodup ∧ X≤K*xs.length ∧
    ∀ n∈xs, 0<n ∧ n≤X ∧ ∃ h, fullRun h n=b

/-- With positive predecessor density supplied, vanishing missed fractions
along selected scales of synchronized triples suffice, even with moving gates. -/
theorem universal_iff_vanishing_misses (density : PositivePredecessorDensity) :
    Universal ↔ ∀ D N, ∃ X O g, N≤X ∧ D*(misses X O g).length<X := by
  constructor
  · intro all D N
    obtain ⟨O,none⟩ := zero_misses all (N+1)
    exact ⟨N+1,O,1,by omega,by rw [none]; simp⟩
  · intro pass
    apply Classical.byContradiction
    intro failure
    obtain ⟨q,c,odd,col,bad⟩ := odd_bad_unit failure
    have uq : q%3≠0 := by cases c <;> simp_all [digit]
    obtain ⟨K,A,goodBanks⟩ := density 1 (by decide) (by decide)
    obtain ⟨L,B,badBanks⟩ := density q odd uq
    obtain ⟨X,O,g,large,small⟩ := pass (K+L) (A+B)
    obtain ⟨F,enc⟩ := triple_encoding
    have oppose (b C : Nat) (ob : b%2=1) (ub : b%3≠0) (cap : C≤K+L)
        (diff : ¬(ReachesOne b ↔ ReachesOne g))
        (bank : ∃ xs : List Nat, xs.Nodup ∧ X≤C*xs.length ∧
          ∀ n∈xs, 0<n ∧ n≤X ∧ ∃ h, fullRun h n=b) : False := by
      obtain ⟨xs,nd,count,sites⟩ := bank
      have paths (n : Nat) (mem : n∈xs) : 0<n ∧ n≤X ∧ ∃ h, run h n=b := by
        obtain ⟨pn,bounded,h,reach⟩ := sites n mem
        exact ⟨pn,bounded,odd_target_transfer h n b ob reach⟩
      have le := Nat.mul_le_mul cap (enough (O:=O) enc ub diff nd paths)
      exact Nat.not_lt_of_ge (Nat.le_trans count le) small
    by_cases reached : ReachesOne g
    · exact oppose q L odd uq (by omega) (fun eq => bad (eq.mpr reached)) (badBanks X (by omega))
    · exact oppose 1 K (by decide) (by decide) (by omega)
        (fun eq => reached (eq.mp ⟨0,rfl⟩)) (goodBanks X (by omega))

#print axioms odd_target_transfer
#print axioms universal_iff_vanishing_misses
end Collatz.Itinerary.SynchronousBasinDensity

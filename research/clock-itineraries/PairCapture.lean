module

public import TowerCapture
public import PairCover
import all TowerCapture
import all PairCover
import all WindowCapture
import all TernaryItinerary

public section
namespace Collatz.Itinerary.PairCapture

open PairCover TowerCapture WindowCapture
set_option autoImplicit false
set_option maxRecDepth 8192
set_option maxHeartbeats 220000
attribute [local irreducible] run

@[expose] def arm (u r : Nat) := if r=0 then 23+32*u else 3*(23+32*u)

private theorem right_inverse (b : Nat) (odd : b%2=1) (unit : b%3≠0) :
    ∃ u, True ∧ u≤9710*b ∧ ∀ r≤1, run 23 (arm u r)=b := by
  obtain ⟨u,h₀,h₁⟩ := all_at_23 b odd unit
  have mid : run 18 (20+27*u)=b := calc
    _ = run 18 (run 5 (23+32*u)) := congrArg (run 18) (pair_five u).1.symm
    _ = run 23 (23+32*u) := (run_add 5 18 _).symm
    _ = b := h₀
  have height := input_bound 18 (20+27*u)
  rw [mid] at height
  change 20+27*u≤262144*b at height
  refine ⟨u,True.intro,by omega,?_⟩
  intro r _
  by_cases zero : r=0
  · simpa only [arm,if_pos zero] using h₀
  · simpa only [arm,if_neg zero] using h₁

/-- Parameters whose two certified starts both miss the chosen gate by O. -/
@[expose] def pairMisses (k O g : Nat) : List Nat :=
  (List.range (9710*window k+1)).filter (fun u =>
    !(hitBy O (arm u 0) g || hitBy O (arm u 1) g))

private theorem covered {k O g u : Nat} (within : u≤9710*window k)
    (outside : u∉pairMisses k O g) : ∃ r≤1, ∃ t≤O, run t (arm u r)=g := by
  have range : u∈List.range (9710*window k+1) := List.mem_range.mpr (by omega)
  by_cases a : hitBy O (arm u 0) g=true
  · exact ⟨0,by decide,(hitBy_iff _ _ _).mp a⟩
  by_cases b : hitBy O (arm u 1) g=true
  · exact ⟨1,by decide,(hitBy_iff _ _ _).mp b⟩
  exact False.elim (outside (List.mem_filter.mpr ⟨range,by simp [a,b]⟩))

/-- A fully numerical version of the common-clock parameter test. -/
theorem universal_iff_pair_counts : Universal ↔ ∀ N, ∃ k O g, N≤k ∧
    (pairMisses k O g).length<quota k (k/2) := by
  constructor
  · intro all N
    let xs := List.range (9710*window N+1)
    have pos (u : Nat) : 0<arm u 0 := by simp [arm]; omega
    obtain ⟨O,done⟩ := all_hit all (xs.map (fun u => arm u 0)) (by
      intro n mem; obtain ⟨u,_,rfl⟩ := List.mem_map.mp mem; exact pos u)
    have none : pairMisses N O 1=[] := by
      apply List.eq_nil_iff_forall_not_mem.mpr
      intro u mem
      unfold pairMisses at mem
      have ⟨range,failed⟩ := List.mem_filter.mp mem
      have reached := done _ (List.mem_map.mpr ⟨u,range,rfl⟩)
      have hit := (hitBy_iff _ _ _).mpr reached
      change (!(hitBy O (arm u 0) 1 || hitBy O (arm u 1) 1))=true at failed
      simp [hit] at failed
    refine ⟨N,O,1,Nat.le_refl _,?_⟩
    have h := half_quota N
    have p := Nat.two_pow_pos N
    rw [none]; change 0<_; omega
  · intro passed
    apply Classical.byContradiction
    intro bad
    obtain ⟨q,c,odd,col,non⟩ := odd_bad_unit bad
    obtain ⟨k,O,g,big,few⟩ := passed q
    have cap := Nat.lt_mul_div_succ (2^(4*k+2*(k/2))*(k+1)) (Nat.pow_pos (by decide : 0<3) (n:=k))
    have room : 2^(4*k+2*(k/2))*(k+1)≤3^k*window k := Nat.le_of_lt cap
    have share (b : Nat) (small : b≤k+1) {d : Bool} (bo : b%2=1) (bc : b%3=digit d) :
        ReachesOne b ↔ ReachesOne g := by
      exact transfers_count (T:=23) (R:=1) (C:=9710) arm (fun _ => True) right_inverse bo bc
        (Nat.le_trans (Nat.mul_le_mul_left _ small) room) (pairMisses k O g) few
        (fun _ _ le out => covered le out)
    have gate := (share 1 (by omega) (d:=false) (by decide) (by decide)).mp ⟨0,by simp only [run]⟩
    exact non ((share q (by omega) odd col).mpr gate)

#print axioms universal_iff_pair_counts
end Collatz.Itinerary.PairCapture

module

public import NegativeCarry

@[expose] public section

/-!
# The negative seventeen cycle inside the residual head-three family

This module proves an obstruction to original-target descent during an
arbitrarily long supplied binary window. It does not assert that the
corresponding complete sources have an alphabet-four certificate.
-/

namespace CollatzShell.HeadThreeNegativeCycle

open WitnessGlobal WitnessSynthesis
open NegativeCarry

set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

theorem negative_cycle :
    negativeOrbit 11 136 = 136 ∧ evenCount 11 136 = 4 := by
  decide

theorem negative_cycle_uniform (k : Nat) :
    negativeOrbit k 136 ≤ 136 ∧ 2^k ≤ 8 * 3^(k-evenCount k 136) := by
  induction k using Nat.strong_induction_on with
  | h k ih =>
    by_cases small : k < 11
    · interval_cases k <;> decide
    · obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le (show 11 ≤ k by omega)
      have earlier : j < 11+j := by omega
      obtain ⟨bounded, multiplier⟩ := ih j earlier
      have events := evenCount_le j 136
      have count : 11+j-(4+evenCount j 136) = (j-evenCount j 136)+7 := by omega
      rw [negativeOrbit_add,evenCount_add,negative_cycle.1,negative_cycle.2,count]
      refine ⟨bounded, ?_⟩
      rw [pow_add,pow_add]
      norm_num
      have scaled := Nat.mul_le_mul_left 2048 multiplier
      omega

private def entryA : Nat → Nat
  | 0 => 16384 | 1 => 24576 | 2 => 36864 | 3 => 55296
  | 4 => 27648 | 5 => 41472 | 6 => 62208 | 7 => 93312
  | 8 => 139968 | 9 => 209952 | 10 => 104976
  | 11 => 157464 | 12 => 236196 | _ => 354294

private def entryB : Nat → Nat
  | 0 => 3431 | 1 => 5147 | 2 => 7721 | 3 => 11582
  | 4 => 5791 | 5 => 8687 | 6 => 13031 | 7 => 19547
  | 8 => 29321 | 9 => 43982 | 10 => 21991
  | 11 => 32987 | 12 => 49481 | _ => 74222

private theorem entry_step (b i : Nat) (clock : i<13) :
    step (entryA i*b+entryB i) = entryA (i+1)*b+entryB (i+1) := by
  interval_cases i <;> norm_num [entryA,entryB,step,Nat.add_mod,Nat.mul_mod] <;> omega

private theorem entry_prefix (b t : Nat) (clock : t≤13) :
    orbit t (16384*b+3431) = entryA t*b+entryB t := by
  induction t with
  | zero => rfl
  | succ t ih =>
    have earlier : t≤13 := by omega
    rw [show t+1=t+1 by rfl,orbit_add,ih earlier]
    simpa only [orbit] using entry_step b t (by omega)

theorem head_three_entry (b : Nat) :
    orbit 13 (16384*b+3431) = 354294*b+74222 := by
  exact entry_prefix b 13 (by decide)

theorem head_three_entry_no_descent (b t : Nat) (positive : 0<t) (bound : t≤13) :
    16384*b+3431 < orbit t (16384*b+3431) := by
  rw [entry_prefix b t bound]
  interval_cases t <;> norm_num [entryA,entryB] <;> omega

theorem source_entry (b : Nat) :
    GapTrace (2048*b+429) (486*b+103) [3,2,2,1,2] := by
  refine ⟨by decide, 768*b+161, ?_,
    by decide, 576*b+121, ?_,
    by decide, 432*b+91, ?_,
    by decide, 648*b+137, ?_,
    by decide, 486*b+103, ?_, ?_⟩ <;>
    norm_num [GapTrace] <;> omega

theorem source_twos (k d : Nat) :
    GapTrace (1+2*4^k*d) (1+2*3^k*d) (List.replicate k 2) := by
  induction k generalizing d with
  | zero => simp [GapTrace]
  | succ k ih =>
    simp only [List.replicate_succ,GapTrace]
    refine ⟨by decide, 1+2*4^k*(3*d), ?_, ?_⟩
    · rw [pow_succ]
      ring
    · have endpoint : 1+2*3^(k+1)*d=1+2*3^k*(3*d) := by
        rw [pow_succ]
        ring
      rw [endpoint]
      exact ih (3*d)

theorem source_long_prefix (k b d : Nat)
    (pin : 486*b+102 = 2^(2*k+1)*d) :
    GapTrace (2048*b+429) (1+2*3^k*d)
      ([3,2,2,1,2] ++ List.replicate k 2) := by
  have power : 2^(2*k+1)=2*4^k := by
    rw [pow_add,pow_mul]
    norm_num
    ring
  rw [power] at pin
  have source : 486*b+103 = 1+2*4^k*d := by omega
  apply (trace_append_iff _ _ _ _).mpr
  exact ⟨486*b+103,source_entry b,by rw [source]; exact source_twos k d⟩

theorem lifted_negative_window (H b d k : Nat)
    (pin : 486*b+102 = 2^H*d) (clock : k≤H) :
    16384*b+3431 < orbit (13+k) (16384*b+3431) := by
  have split : 2^H = 2^k*2^(H-k) := by
    rw [←pow_add, Nat.add_sub_of_le clock]
  have initial : (354294*b+74222)+136 = 2^k*(729*2^(H-k)*d) := by
    rw [split] at pin
    nlinarith [pin]
  have lift := complement_lift k (354294*b+74222) 136
    (729*2^(H-k)*d) (by decide) initial
  obtain ⟨bounded, multiplier⟩ := negative_cycle_uniform k
  have scaled := Nat.mul_le_mul_right (729*2^(H-k)*d) multiplier
  rw [orbit_add,head_three_entry]
  nlinarith [scaled,initial,bounded]

theorem original_target_no_descent (H b d t : Nat)
    (pin : 486*b+102 = 2^H*d) (positive : 0<t) (clock : t≤13+H) :
    16384*b+3431 < orbit t (16384*b+3431) := by
  by_cases early : t≤13
  · exact head_three_entry_no_descent b t positive early
  · have late : t=13+(t-13) := by omega
    rw [late]
    exact lifted_negative_window H b d (t-13) pin (by omega)


def hardWord : List Nat := [3,2,2,1,2,2,2,2,2,2,1,3,2,3,1,4,2,2,2,2,2,2,4,2,1,2,2,1,2,2,4,3,2,1,2,3,1,2,1,4,1,3,1,2,3,4]

/-- One actual complete alphabet-four source whose window contains the full
negative cycle. This does not assert unbounded complete-source realization. -/
theorem complete_cap_four_example :
    GapTrace 58849709 1 hardWord ∧
      (∀ a ∈ hardWord, a≤4) ∧
      (∀ t, 0<t → t≤24 → 470797671 < orbit t 470797671) := by
  refine ⟨?_, ?_, ?_⟩
  · exact ⟨by decide, 22068641, by decide, ⟨by decide, 16551481, by decide, ⟨by decide, 12413611, by decide, ⟨by decide, 18620417, by decide, ⟨by decide, 13965313, by decide, ⟨by decide, 10473985, by decide, ⟨by decide, 7855489, by decide, ⟨by decide, 5891617, by decide, ⟨by decide, 4418713, by decide, ⟨by decide, 3314035, by decide, ⟨by decide, 4971053, by decide, ⟨by decide, 1864145, by decide, ⟨by decide, 1398109, by decide, ⟨by decide, 524291, by decide, ⟨by decide, 786437, by decide, ⟨by decide, 147457, by decide, ⟨by decide, 110593, by decide, ⟨by decide, 82945, by decide, ⟨by decide, 62209, by decide, ⟨by decide, 46657, by decide, ⟨by decide, 34993, by decide, ⟨by decide, 26245, by decide, ⟨by decide, 4921, by decide, ⟨by decide, 3691, by decide, ⟨by decide, 5537, by decide, ⟨by decide, 4153, by decide, ⟨by decide, 3115, by decide, ⟨by decide, 4673, by decide, ⟨by decide, 3505, by decide, ⟨by decide, 2629, by decide, ⟨by decide, 493, by decide, ⟨by decide, 185, by decide, ⟨by decide, 139, by decide, ⟨by decide, 209, by decide, ⟨by decide, 157, by decide, ⟨by decide, 59, by decide, ⟨by decide, 89, by decide, ⟨by decide, 67, by decide, ⟨by decide, 101, by decide, ⟨by decide, 19, by decide, ⟨by decide, 29, by decide, ⟨by decide, 11, by decide, ⟨by decide, 17, by decide, ⟨by decide, 13, by decide, ⟨by decide, 5, by decide, ⟨by decide, 1, by decide, rfl⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩
  · norm_num [hardWord]
  · intro t positive clock
    exact original_target_no_descent 11 28735 6819 t (by decide) positive clock

end CollatzShell.HeadThreeNegativeCycle

#print axioms CollatzShell.HeadThreeNegativeCycle.negative_cycle
#print axioms CollatzShell.HeadThreeNegativeCycle.negative_cycle_uniform
#print axioms CollatzShell.HeadThreeNegativeCycle.head_three_entry
#print axioms CollatzShell.HeadThreeNegativeCycle.head_three_entry_no_descent
#print axioms CollatzShell.HeadThreeNegativeCycle.source_entry
#print axioms CollatzShell.HeadThreeNegativeCycle.source_twos
#print axioms CollatzShell.HeadThreeNegativeCycle.source_long_prefix
#print axioms CollatzShell.HeadThreeNegativeCycle.lifted_negative_window
#print axioms CollatzShell.HeadThreeNegativeCycle.original_target_no_descent
#print axioms CollatzShell.HeadThreeNegativeCycle.complete_cap_four_example

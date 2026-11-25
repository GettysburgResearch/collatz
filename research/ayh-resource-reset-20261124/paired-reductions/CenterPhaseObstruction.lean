import WordRank

/-! All-clock exclusion of the lower phase required by the signed
minus-one/zero two-center construction at the e=6 source j=11. -/
namespace CenterPhaseObstruction
open CollatzReverseBasin WordRank

def phase (u : Nat) : Nat := 2^(11-u)*3^u-1

private def permit (parent : Bool) (k x : Nat) : Bool :=
  (List.range 12).all (fun u => decide (x ≠ phase u ∨ (parent=true ∧ k=7+u)))

private def check : Nat → Bool → Nat → Nat → Bool
  | 0,_,_,x => decide (x=1)
  | f+1,parent,k,x => decide (x=1) || (permit parent k x && check f parent (k+1) (shortcut x))

private theorem phase_large (u : Nat) (bound : u≤11) : 2 < phase u := by
  have test : ∀ i : Fin 12, 2 < phase i.val := by decide +kernel
  exact test ⟨u,by omega⟩

private theorem from_one (i x : Nat) (small : x=1 ∨ x=2) : run i x=1 ∨ run i x=2 := by
  induction i generalizing x with
  | zero => exact small
  | succ i ih => apply ih; rcases small with rfl|rfl <;> decide

private theorem sound (f : Nat) (parent : Bool) (k x : Nat) (ok : check f parent k x=true)
    (i u : Nat) (bound : u≤11) (hit : run i x=phase u) : parent=true ∧ k+i=7+u := by
  induction f generalizing i k x with
  | zero =>
    have eq : x=1 := of_decide_eq_true ok
    have stops := from_one i x (Or.inl eq)
    have big := phase_large u bound
    omega
  | succ f ih =>
    simp only [check,Bool.or_eq_true,Bool.and_eq_true,decide_eq_true_eq] at ok
    rcases ok with eq|⟨row,next⟩
    · have stops := from_one i x (Or.inl eq)
      have big := phase_large u bound
      omega
    cases i with
    | zero =>
      have allowed := List.all_eq_true.mp row u (List.mem_range.mpr (by omega))
      have cases := of_decide_eq_true allowed
      change x=phase u at hit
      rcases cases with wrong | exactRow
      · exact False.elim (wrong hit)
      · exact exactRow
    | succ i =>
      obtain ⟨p,id⟩ := ih (k+1) (shortcut x) next i hit
      exact ⟨p,by omega⟩

set_option maxRecDepth 10000 in
set_option maxHeartbeats 0 in
private theorem family_table :
    (List.range 67).all (fun i => check 99 false 0 (48*i+17)) = true := by decide +kernel

private theorem parent_table : check 107 true 0 3233=true := by decide +kernel

/-- All 67 smaller candidates miss all 12 target phases, at every clock. -/
theorem smaller_never_hits (w i u : Nat) (residue : w%48=17) (small : w<3233)
    (bound : u≤11) : run i w ≠ phase u := by
  intro hit
  have row := List.all_eq_true.mp family_table (w/48) (List.mem_range.mpr (by omega))
  change check 99 false 0 (48*(w/48)+17)=true at row
  rw [show 48*(w/48)+17=w by omega] at row
  have no := (sound 99 false 0 w row i u bound hit).1
  contradiction

/-- The source itself visits a target phase only at its original clock. -/
theorem parent_phase_clock (i u : Nat) (bound : u≤11) (hit : run i 3233=phase u) :
    i=7+u := by simpa using (sound 107 true 0 3233 parent_table i u bound hit).2

/-- The reference at m=0 cannot be recovered as a limiting comparison
of strict slope decrease, even if its integral comparison source equals
3233. The displayed inequalities are the size, negative center, and
slope guards after the arithmetic transfer. -/
theorem limiting_query_impossible (w i u d E B : Nat)
    (bound : u≤11) (residue : w%48=17) (size : w<3236)
    (negative : 3^d≤B)
    (source : 3^d*w+B=2^(11+d+E))
    (shrink : 81*2^(d+E)<128*3^d)
    (clock : i=d+E+u) (hit : run i w=phase u) : False := by
  by_cases smaller : w<3233
  · exact smaller_never_hits w i u residue smaller bound hit
  have w_eq : w=3233 := by omega
  subst w
  have exactClock := parent_phase_clock i u bound hit
  have total : d+E=7 := by omega
  rw [total] at shrink
  rw [show 11+d+E=18 by omega] at source
  have bigger : 81<3^d := by omega
  have dLarge : 5≤d := by
    by_contra! low
    have q := Nat.pow_le_pow_right (by decide : 0<3) (show d≤4 by omega)
    omega
  have lower := Nat.pow_le_pow_right (by decide : 0<3) dLarge
  omega

#print axioms smaller_never_hits
#print axioms parent_phase_clock
#print axioms limiting_query_impossible
end CenterPhaseObstruction

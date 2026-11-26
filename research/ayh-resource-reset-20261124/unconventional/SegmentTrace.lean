import WordRank

/-! Verify long ordinary trajectories from independently checked small
residue profiles. Large lifts require one integer update per block. -/
namespace SegmentTrace
open WordRank

structure Block where
  clocks : Nat
  residue : Nat
  image : Nat
  oddCount : Nat

def Valid (s : Block) : Prop :=
  run s.clocks s.residue=s.image ∧ odds s.clocks s.residue=s.oddCount

instance (s : Block) : Decidable (Valid s) := inferInstanceAs
  (Decidable (run s.clocks s.residue=s.image ∧ odds s.clocks s.residue=s.oddCount))

def clockSum : List Block → Nat
  | [] => 0
  | s::rest => s.clocks+clockSum rest

def replay : List Block → Nat → Option (Nat × Nat)
  | [],x => some (x,0)
  | s::rest,x =>
    if x%2^s.clocks=s.residue then
      let y:=3^s.oddCount*(x/2^s.clocks)+s.image
      (replay rest y).map (fun endp => (endp.1,s.oddCount+endp.2))
    else none

theorem correct (blocks : List Block) (x y p : Nat)
    (certified : ∀ s ∈ blocks, Valid s) (ok : replay blocks x=some (y,p)) :
    run (clockSum blocks) x=y ∧ odds (clockSum blocks) x=p := by
  induction blocks generalizing x y p with
  | nil => simpa [replay,clockSum,run,odds] using ok
  | cons s rest ih =>
    have sc:=certified s (by simp)
    obtain ⟨sv,so⟩:=sc
    unfold replay at ok
    split at ok
    next phase =>
      have split : 2^s.clocks*(x/2^s.clocks)+s.residue=x := by
        rw [←phase,Nat.add_comm,Nat.mod_add_div]
      obtain ⟨im,gr⟩:=liftPrefix s.clocks (x/2^s.clocks) s.residue
      rw [split,sv,so] at im
      rw [split,so] at gr
      cases hit : replay rest (3^s.oddCount*(x/2^s.clocks)+s.image) with
      | none => simp [hit] at ok
      | some a =>
        obtain ⟨z,q⟩:=a
        have eq : z=y ∧ s.oddCount+q=p := by simpa [hit] using ok
        obtain ⟨ev,eg⟩:=ih (3^s.oddCount*(x/2^s.clocks)+s.image) z q
          (fun t ht => certified t (List.mem_cons_of_mem s ht)) hit
        simp only [clockSum,runAdd,oddsAdd,im,gr,ev,eg,eq.1,eq.2,and_self]
    next => contradiction

#print axioms correct
end SegmentTrace

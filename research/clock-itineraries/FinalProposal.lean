module

public import ClosureProposal
import all FixedGate
import all TernaryItinerary
import all SynchronousShadow

public section
namespace Collatz.Itinerary.Proposal

open CycleRows CycleAmplification FixedGate
set_option autoImplicit false

/-- Even a single positive result of the finite, executable test certifies
a nontrivial cycle. Such a cycle would make every sufficiently late test positive. -/
theorem cycle_iff_eventually_positive :
    NontrivialCycle ↔ ∃ B, ∀ b, B≤b → witnessTest b=true := by
  constructor
  · intro cycle
    obtain ⟨q,B,above,eventual⟩ := cycle_amplifies_eventually cycle
    refine ⟨B,fun b hb => ?_⟩
    obtain ⟨x,rs,hl,r,large⟩ := eventual b hb
    exact (witnessTest_iff b).mpr ⟨q,x,rs,above,hl,r,large⟩
  · rintro ⟨B,tests⟩
    exact witness_implies_cycle ((witnessTest_iff B).mp (tests B (by omega)))

theorem cycle_iff_one_positive : NontrivialCycle ↔ ∃ b, witnessTest b=true := by
  constructor
  · intro cycle
    obtain ⟨B,h⟩ := cycle_iff_eventually_positive.mp cycle
    exact ⟨B,h B (by omega)⟩
  · rintro ⟨b,h⟩
    exact witness_implies_cycle ((witnessTest_iff b).mp h)

/-- Both right-hand conditions only use executable arithmetic on finite
prefixes. Their outer universal quantifiers remain mathematical obligations. -/
theorem final_proposal : Universal ↔
    (∀ (a : Nat) (c : Bool), a%2=1 → a%3=digit c → Crosses a) ∧
    (∀ N, ∃ b, N≤b ∧ witnessTest b=false) := by
  rw [universal_iff_clocks_and_rows]
  constructor
  · rintro ⟨crosses,none⟩
    refine ⟨crosses,fun N => ⟨N,by omega,?_⟩⟩
    cases h : witnessTest N with
    | false => rfl
    | true => exact False.elim (none N ((witnessTest_iff N).mp h))
  · rintro ⟨crosses,zeros⟩
    refine ⟨crosses,?_⟩
    intro b w
    obtain ⟨B,all⟩ := cycle_iff_eventually_positive.mp (witness_implies_cycle w)
    obtain ⟨j,hj,zero⟩ := zeros B
    have one := all j hj
    simp [zero] at one

private theorem block {x y k r : Nat} (h : run k x=y) : run (k+r) x=run r y := by
  rw [run_add,h]

set_option maxRecDepth 2000 in
private theorem gate_hit : run 553 (2^63-1)=1 := by
  calc
    run 553 (2^63-1) = run 529 155267279694122742448127 := block (x:=(2^63-1)) (y:=155267279694122742448127) (k:=24) (r:=529) (by decide)
    _ = run 505 2613786806742958403202613247 := block (x:=155267279694122742448127) (y:=2613786806742958403202613247) (k:=24) (r:=505) (by decide)
    _ = run 481 20119241134526440339792084508 := block (x:=2613786806742958403202613247) (y:=20119241134526440339792084508) (k:=24) (r:=481) (by decide)
    _ = run 457 212434721544859130792209418 := block (x:=20119241134526440339792084508) (y:=212434721544859130792209418) (k:=24) (r:=457) (by decide)
    _ = run 433 6729157021792023261031069 := block (x:=212434721544859130792209418) (y:=6729157021792023261031069) (k:=24) (r:=433) (by decide)
    _ = run 409 213155146647582926384546 := block (x:=6729157021792023261031069) (y:=213155146647582926384546) (k:=24) (r:=409) (by decide)
    _ = run 385 20255932382858655091658 := block (x:=213155146647582926384546) (y:=20255932382858655091658) (k:=24) (r:=385) (by decide)
    _ = run 361 641634044735359342133 := block (x:=20255932382858655091658) (y:=641634044735359342133) (k:=24) (r:=361) (by decide)
    _ = run 337 83640435685886794 := block (x:=641634044735359342133) (y:=83640435685886794) (k:=24) (r:=337) (by decide)
    _ = run 313 2649423884233441 := block (x:=83640435685886794) (y:=2649423884233441) (k:=24) (r:=313) (by decide)
    _ = run 289 6797850773056352 := block (x:=2649423884233441) (y:=6797850773056352) (k:=24) (r:=289) (by decide)
    _ = run 265 215331114094489 := block (x:=6797850773056352) (y:=215331114094489) (k:=24) (r:=265) (by decide)
    _ = run 241 20462712515396 := block (x:=215331114094489) (y:=20462712515396) (k:=24) (r:=241) (by decide)
    _ = run 217 72020453890 := block (x:=20462712515396) (y:=72020453890) (k:=24) (r:=217) (by decide)
    _ = run 193 84494269 := block (x:=72020453890) (y:=84494269) (k:=24) (r:=193) (by decide)
    _ = run 169 216794098 := block (x:=84494269) (y:=216794098) (k:=24) (r:=169) (by decide)
    _ = run 145 185415655 := block (x:=216794098) (y:=185415655) (k:=24) (r:=145) (by decide)
    _ = run 121 652588 := block (x:=185415655) (y:=652588) (k:=24) (r:=121) (by decide)
    _ = run 97 20675 := block (x:=652588) (y:=20675) (k:=24) (r:=97) (by decide)
    _ = run 73 656 := block (x:=20675) (y:=656) (k:=24) (r:=73) (by decide)
    _ = run 49 593 := block (x:=656) (y:=593) (k:=24) (r:=49) (by decide)
    _ = run 25 4616 := block (x:=593) (y:=4616) (k:=24) (r:=25) (by decide)
    _ = run 1 2 := block (x:=4616) (y:=2) (k:=24) (r:=1) (by decide)
    _ = 1 := by decide

/-- The 512-source row in the original replay passes through an ordinary
gate with a kernel-checked 553-step itinerary to one. -/
theorem published_gate : run 553 (2^63-1)=1 ∧ FullRow (2^63-1) 70 10 := by
  refine ⟨gate_hit,?_⟩
  let a := 2^63-1
  have first : Gap 1 a (Shadow.site 59 4) := ⟨by decide,by decide,by decide,by decide⟩
  have suffix := Shadow.prepend (Shadow.stair 59 4 (by decide)) first
    (show a%3=digit false by decide)
  refine ⟨_,_,80,60,by decide,by simp,suffix,by decide,?_⟩
  intro w hw
  apply free_marks (c:=false) (by decide) (by decide) w <;> omega

#print axioms cycle_iff_eventually_positive
#print axioms cycle_iff_one_positive
#print axioms final_proposal
#print axioms published_gate
end Collatz.Itinerary.Proposal

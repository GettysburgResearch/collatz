module

public import ReturnDescent
meta import Lean.Elab.Tactic
import all TowerFrontierAffine
import all TernaryItinerary

public section

namespace Collatz.Itinerary.ReturnDescent
open TowerFrontier
set_option autoImplicit false
set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

/-- Evaluate two physical subwords, using only the necessary low bits for the
    first and restoring its exact affine high contribution at their boundary. -/
private def splitEval : Nat → Nat → Nat → Nat × Nat
  | 0,h,n => stride h n 0
  | f+1,h,n =>
    let l := h/2
    let D := 2^l
    let q := n/D
    let L := splitEval f l (n%D)
    let mid := if q=0 then L.1 else L.1+3^L.2*q
    let R := splitEval f (h-l) mid
    (R.1,L.2+R.2)

private theorem track_shift (h n g : Nat) : track h n g=((track h n 0).1,g+(track h n 0).2) := by
  have add (h n e t : Nat) : track h n (e+t)=((track h n e).1,(track h n e).2+t) := by
    induction h generalizing n e t with
    | zero => rfl
    | succ h ih =>
      rw [track,track]
      split
      · apply ih
      · rw [show e+t+1=(e+1)+t by omega,ih]
  simpa only [Nat.zero_add,Nat.add_comm g] using add h n 0 g

private theorem track_append' (i j n e : Nat) :
    track (i+j) n e=track j (track i n e).1 (track i n e).2 := by
  induction i generalizing n e with
  | zero => simp [track]
  | succ i ih => rw [Nat.succ_add,track,track]; split <;> apply ih

private theorem splitEval_spec (f h n : Nat) : splitEval f h n=track h n 0 := by
  induction f generalizing h n with
  | zero => exact stride_eq ..
  | succ f ih =>
    let l := h/2
    let D := 2^l
    let L := track l (n%D) 0
    let mid := L.1+3^L.2*(n/D)
    have shift := track_lift l (n%D) (n/D)
    change track l (n%D + D*(n/D)) 0=(mid,L.2) at shift
    rw [Nat.mod_add_div] at shift
    have splitH := track_append' l (h-l) n 0
    rw [show l+(h-l)=h by dsimp only [l]; omega,shift] at splitH
    rw [splitH,track_shift (h-l) mid L.2]
    dsimp only [splitEval]
    simp only [ih]
    change (let R := track (h-l) (if n/D=0 then L.1 else mid) 0; (R.1,L.2+R.2))=_
    by_cases z : n/D=0
    · have mid_eq : mid=L.1 := by dsimp only [mid]; rw [z,Nat.mul_zero,Nat.add_zero]
      simp only [z,↓reduceIte,mid_eq]
    · simp only [z,↓reduceIte]

private def cp0 : Nat := 3^3145727-1

private theorem checked_edge {f h n y : Nat} (proof : (splitEval f h n).1=y) : run h n=y := by
  rwa [splitEval_spec,track_run] at proof

private theorem glue {a b n v w : Nat} (p : run a n=v) (q : run b v=w) : run (a+b) n=w := by
  rw [run_add,p,q]

/- Native elaboration proposes each ordinary intermediate as a numeral. Every
   transition below is independently checked by kernel reduction with its exact
   source and endpoint, so the generated values carry no mathematical trust. -/
private def cp1 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp0).1))
private theorem edge0 : run 500000 cp0=cp1 := checked_edge (f:=10) (by decide +kernel)

private def cp2 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp1).1))
private theorem edge1 : run 500000 cp1=cp2 := checked_edge (f:=10) (by decide +kernel)

private def cp3 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp2).1))
private theorem edge2 : run 500000 cp2=cp3 := checked_edge (f:=10) (by decide +kernel)

private def cp4 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp3).1))
private theorem edge3 : run 500000 cp3=cp4 := checked_edge (f:=10) (by decide +kernel)

private def cp5 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp4).1))
private theorem edge4 : run 500000 cp4=cp5 := checked_edge (f:=10) (by decide +kernel)

private def cp6 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp5).1))
private theorem edge5 : run 500000 cp5=cp6 := checked_edge (f:=10) (by decide +kernel)

private def cp7 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp6).1))
private theorem edge6 : run 500000 cp6=cp7 := checked_edge (f:=10) (by decide +kernel)

private def cp8 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp7).1))
private theorem edge7 : run 500000 cp7=cp8 := checked_edge (f:=10) (by decide +kernel)

private def cp9 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp8).1))
private theorem edge8 : run 500000 cp8=cp9 := checked_edge (f:=10) (by decide +kernel)

private def cp10 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp9).1))
private theorem edge9 : run 500000 cp9=cp10 := checked_edge (f:=10) (by decide +kernel)

private def cp11 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp10).1))
private theorem edge10 : run 500000 cp10=cp11 := checked_edge (f:=10) (by decide +kernel)

private def cp12 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp11).1))
private theorem edge11 : run 500000 cp11=cp12 := checked_edge (f:=10) (by decide +kernel)

private def cp13 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp12).1))
private theorem edge12 : run 500000 cp12=cp13 := checked_edge (f:=10) (by decide +kernel)

private def cp14 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp13).1))
private theorem edge13 : run 500000 cp13=cp14 := checked_edge (f:=10) (by decide +kernel)

private def cp15 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp14).1))
private theorem edge14 : run 500000 cp14=cp15 := checked_edge (f:=10) (by decide +kernel)

private def cp16 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp15).1))
private theorem edge15 : run 500000 cp15=cp16 := checked_edge (f:=10) (by decide +kernel)

private def cp17 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp16).1))
private theorem edge16 : run 500000 cp16=cp17 := checked_edge (f:=10) (by decide +kernel)

private def cp18 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp17).1))
private theorem edge17 : run 500000 cp17=cp18 := checked_edge (f:=10) (by decide +kernel)

private def cp19 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp18).1))
private theorem edge18 : run 500000 cp18=cp19 := checked_edge (f:=10) (by decide +kernel)

private def cp20 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp19).1))
private theorem edge19 : run 500000 cp19=cp20 := checked_edge (f:=10) (by decide +kernel)

private def cp21 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp20).1))
private theorem edge20 : run 500000 cp20=cp21 := checked_edge (f:=10) (by decide +kernel)

private def cp22 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp21).1))
private theorem edge21 : run 500000 cp21=cp22 := checked_edge (f:=10) (by decide +kernel)

private def cp23 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp22).1))
private theorem edge22 : run 500000 cp22=cp23 := checked_edge (f:=10) (by decide +kernel)

private def cp24 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp23).1))
private theorem edge23 : run 500000 cp23=cp24 := checked_edge (f:=10) (by decide +kernel)

private def cp25 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp24).1))
private theorem edge24 : run 500000 cp24=cp25 := checked_edge (f:=10) (by decide +kernel)

private def cp26 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp25).1))
private theorem edge25 : run 500000 cp25=cp26 := checked_edge (f:=10) (by decide +kernel)

private def cp27 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp26).1))
private theorem edge26 : run 500000 cp26=cp27 := checked_edge (f:=10) (by decide +kernel)

private def cp28 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp27).1))
private theorem edge27 : run 500000 cp27=cp28 := checked_edge (f:=10) (by decide +kernel)

private def cp29 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp28).1))
private theorem edge28 : run 500000 cp28=cp29 := checked_edge (f:=10) (by decide +kernel)

private def cp30 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp29).1))
private theorem edge29 : run 500000 cp29=cp30 := checked_edge (f:=10) (by decide +kernel)

private def cp31 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp30).1))
private theorem edge30 : run 500000 cp30=cp31 := checked_edge (f:=10) (by decide +kernel)

private def cp32 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp31).1))
private theorem edge31 : run 500000 cp31=cp32 := checked_edge (f:=10) (by decide +kernel)

private def cp33 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp32).1))
private theorem edge32 : run 500000 cp32=cp33 := checked_edge (f:=10) (by decide +kernel)

private def cp34 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp33).1))
private theorem edge33 : run 500000 cp33=cp34 := checked_edge (f:=10) (by decide +kernel)

private def cp35 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp34).1))
private theorem edge34 : run 500000 cp34=cp35 := checked_edge (f:=10) (by decide +kernel)

private def cp36 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp35).1))
private theorem edge35 : run 500000 cp35=cp36 := checked_edge (f:=10) (by decide +kernel)

private def cp37 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp36).1))
private theorem edge36 : run 500000 cp36=cp37 := checked_edge (f:=10) (by decide +kernel)

private def cp38 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp37).1))
private theorem edge37 : run 500000 cp37=cp38 := checked_edge (f:=10) (by decide +kernel)

private def cp39 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp38).1))
private theorem edge38 : run 500000 cp38=cp39 := checked_edge (f:=10) (by decide +kernel)

private def cp40 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp39).1))
private theorem edge39 : run 500000 cp39=cp40 := checked_edge (f:=10) (by decide +kernel)

private def cp41 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp40).1))
private theorem edge40 : run 500000 cp40=cp41 := checked_edge (f:=10) (by decide +kernel)

private def cp42 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp41).1))
private theorem edge41 : run 500000 cp41=cp42 := checked_edge (f:=10) (by decide +kernel)

private def cp43 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp42).1))
private theorem edge42 : run 500000 cp42=cp43 := checked_edge (f:=10) (by decide +kernel)

private def cp44 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp43).1))
private theorem edge43 : run 500000 cp43=cp44 := checked_edge (f:=10) (by decide +kernel)

private def cp45 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp44).1))
private theorem edge44 : run 500000 cp44=cp45 := checked_edge (f:=10) (by decide +kernel)

private def cp46 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp45).1))
private theorem edge45 : run 500000 cp45=cp46 := checked_edge (f:=10) (by decide +kernel)

private def cp47 : Nat := by
  run_tac
    Lean.Elab.Tactic.closeMainGoal `checkpoint (Lean.mkNatLit ((splitEval 10 500000 cp46).1))
private theorem edge46 : run 500000 cp46=cp47 := checked_edge (f:=10) (by decide +kernel)

private theorem edge47 : run 552486 cp47=1 := checked_edge (f:=10) (by decide +kernel)

private theorem longPeak : run 24052486 (3^3145727-1)=1 :=
  (@glue 12000000 12052486 cp0 cp24 1
    (@glue 6000000 6000000 cp0 cp12 cp24
      (@glue 3000000 3000000 cp0 cp6 cp12
        (@glue 1500000 1500000 cp0 cp3 cp6
          (@glue 500000 1000000 cp0 cp1 cp3
            edge0
            (@glue 500000 500000 cp1 cp2 cp3
              edge1
              edge2))
          (@glue 500000 1000000 cp3 cp4 cp6
            edge3
            (@glue 500000 500000 cp4 cp5 cp6
              edge4
              edge5)))
        (@glue 1500000 1500000 cp6 cp9 cp12
          (@glue 500000 1000000 cp6 cp7 cp9
            edge6
            (@glue 500000 500000 cp7 cp8 cp9
              edge7
              edge8))
          (@glue 500000 1000000 cp9 cp10 cp12
            edge9
            (@glue 500000 500000 cp10 cp11 cp12
              edge10
              edge11))))
      (@glue 3000000 3000000 cp12 cp18 cp24
        (@glue 1500000 1500000 cp12 cp15 cp18
          (@glue 500000 1000000 cp12 cp13 cp15
            edge12
            (@glue 500000 500000 cp13 cp14 cp15
              edge13
              edge14))
          (@glue 500000 1000000 cp15 cp16 cp18
            edge15
            (@glue 500000 500000 cp16 cp17 cp18
              edge16
              edge17)))
        (@glue 1500000 1500000 cp18 cp21 cp24
          (@glue 500000 1000000 cp18 cp19 cp21
            edge18
            (@glue 500000 500000 cp19 cp20 cp21
              edge19
              edge20))
          (@glue 500000 1000000 cp21 cp22 cp24
            edge21
            (@glue 500000 500000 cp22 cp23 cp24
              edge22
              edge23)))))
    (@glue 6000000 6052486 cp24 cp36 1
      (@glue 3000000 3000000 cp24 cp30 cp36
        (@glue 1500000 1500000 cp24 cp27 cp30
          (@glue 500000 1000000 cp24 cp25 cp27
            edge24
            (@glue 500000 500000 cp25 cp26 cp27
              edge25
              edge26))
          (@glue 500000 1000000 cp27 cp28 cp30
            edge27
            (@glue 500000 500000 cp28 cp29 cp30
              edge28
              edge29)))
        (@glue 1500000 1500000 cp30 cp33 cp36
          (@glue 500000 1000000 cp30 cp31 cp33
            edge30
            (@glue 500000 500000 cp31 cp32 cp33
              edge31
              edge32))
          (@glue 500000 1000000 cp33 cp34 cp36
            edge33
            (@glue 500000 500000 cp34 cp35 cp36
              edge34
              edge35))))
      (@glue 3000000 3052486 cp36 cp42 1
        (@glue 1500000 1500000 cp36 cp39 cp42
          (@glue 500000 1000000 cp36 cp37 cp39
            edge36
            (@glue 500000 500000 cp37 cp38 cp39
              edge37
              edge38))
          (@glue 500000 1000000 cp39 cp40 cp42
            edge39
            (@glue 500000 500000 cp40 cp41 cp42
              edge40
              edge41)))
        (@glue 1500000 1552486 cp42 cp45 1
          (@glue 500000 1000000 cp42 cp43 cp45
            edge42
            (@glue 500000 500000 cp43 cp44 cp45
              edge43
              edge44))
          (@glue 500000 1052486 cp45 cp46 1
            edge45
            (@glue 500000 552486 cp46 cp47 1
              edge46
              edge47))))))

/-- Unconditional ordinary iteration of the first preassigned delayed hard parent. -/
theorem first_delayed_converges : run 27198220 (hardParent 3145727)=1 := by
  have source := (hard_source 19418).2.2.1
  change run 7 (hardParent 3145727)=M 3145727 at source
  have path := longPeak
  rw [show 27198220=7+(3145727+24052486) by decide,run_add,source,
    run_add,peak,path]

#print axioms first_delayed_converges
end Collatz.Itinerary.ReturnDescent

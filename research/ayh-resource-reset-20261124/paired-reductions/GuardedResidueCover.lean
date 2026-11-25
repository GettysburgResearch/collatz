import SignedCycleDilation
import DirectedEleven

namespace GuardedResidueCover
open CollatzReverseBasin CollatzTwoOdd DirectedEleven

structure Entry where
  source : Row
  middle : Row
  left : String
  right : String
  direct : Bool

def row (i : Fin 16) : Entry :=
  match i.val with
  | 0 => ⟨(1536,401),(432,113),"OEOEE","OOEEIDDDIDDII",false⟩
  | 1 => ⟨(768,545),(2304,1635),"OEOEOOEEIDDDDDII","",true⟩
  | 2 => ⟨(12288,641),(36864,1923),"OEOEOEOOOOEEIDIIDDIDDDII","",true⟩
  | 3 => ⟨(1536,1121),(4608,3363),"OEOEOOOEEIDIDDDDII","",true⟩
  | 4 => ⟨(12288,1169),(36864,3507),"OEOEEOEOOOEEIDIDDDDIDDII","",true⟩
  | 5 => ⟨(6144,1217),(1296,257),"OEOEOEE","OOEEIDDDIIDDDII",false⟩
  | 6 => ⟨(3072,1409),(9216,4227),"OEOEOEOOEEIDDDIDDDII","",true⟩
  | 7 => ⟨(3072,1505),(9216,4515),"OEOEOOOOEEIDIIDDDDII","",true⟩
  | 8 => ⟨(6144,2177),(18432,6531),"OEOEOEOOOEEIDIDDIDDDII","",true⟩
  | 9 => ⟨(6144,3809),(18432,11427),"OEOEOOOOOEEIDIIIDDDDII","",true⟩
  | 10 => ⟨(6144,5777),(18432,17331),"OEOEEOEOOEEIDDDDDIDDII","",true⟩
  | 11 => ⟨(12288,5969),(3888,1889),"OEOEEOOOOEEIDI","OOEEIDDDIIDIDDII",false⟩
  | 12 => ⟨(12288,8657),(1728,1217),"OEOEEOOEEIDI","OOEEEODDIDDIDIDDII",false⟩
  | 13 => ⟨(12288,8705),(36864,26115),"OEOEOEOEOOEEIDDDIDIDDDII","",true⟩
  | 14 => ⟨(12288,11489),(36864,34467),"OEOEOOOOOOEEIDIIIIDDDDII","",true⟩
  | _ => ⟨(12288,11537),(1296,1217),"OEOEEOEE","OOEEIDDDIDDIDDII",false⟩

def covered (z : Nat) : Prop := ∃ i : Fin 16,
  z%(row i).source.1=(row i).source.2

private def triple (r : Row) : Row := (3*r.1,3*r.2)
private theorem triple_value (r : Row) (t : Nat) :
    DirectedEleven.value (triple r) t=3*DirectedEleven.value r t := by
  dsimp [triple,DirectedEleven.value]; ring

private def valid (e : Entry) : Prop :=
  run e.left.toList e.source=some e.middle ∧ queries e.left.toList e.source=[] ∧
  if e.direct then e.middle=triple e.source else
  run e.right.toList (triple e.middle)=some (triple e.source) ∧
  queries e.right.toList (triple e.middle)=[] ∧
  e.middle.1%48=0 ∧ e.middle.2%48=17 ∧
  e.middle.1≤e.source.1 ∧ e.middle.2<e.source.2

private theorem cert : ∀ i : Fin 16, valid (row i) := by
  unfold valid; decide

/-- The number of covered residues in the 256 candidates of this period. -/
theorem census :
    ((List.range 256).filter (fun t => (List.finRange 16).any
      (fun i => (48*t+17)%(row i).source.1==(row i).source.2))).length=55 := by decide

private theorem forward (w : List Char) (r s : Row) (t : Nat)
    (h : run w r=some s) (purePath : queries w r=[])
    (bad : ¬Basin (DirectedEleven.value r t)) : ¬Basin (DirectedEleven.value s t) := by
  apply runSound (fun x => ¬ Basin x) _ _ _ _ _ h t _ bad
  · intro n; apply not_congr
    have e := SignedCycleDilation.basin_value 1 (2*n)
    have v : CollatzTwoOdd.value 1 (2*n)=n := by simp [CollatzTwoOdd.value,shortcut]
    rw [v] at e; exact e.symm
  · intro n; apply not_congr
    have e := SignedCycleDilation.basin_value 1 (2*n+1)
    have v : CollatzTwoOdd.value 1 (2*n+1)=3*n+2 := by
      simp only [CollatzTwoOdd.value,shortcut]; split <;> omega
    rw [v] at e; exact e.symm
  · intros u hu; rw [purePath] at hu; contradiction

/-- Every covered residue is excluded at every actual first-hit upper rank. -/
theorem least_excluded (z : Nat) (hd : ReverseDefect z)
    (least : ∀ v, ReverseDefect v → z≤v) (cov : covered z) : False := by
  obtain ⟨i,hi⟩ := cov
  let e:=row i
  let t:=z/e.source.1
  have zz : DirectedEleven.value e.source t=z := by
    change e.source.1*(z/e.source.1)+e.source.2=z
    rw [←hi]; exact Nat.div_add_mod _ _
  obtain ⟨h1,p1,rest⟩ := (show valid e from cert i)
  have b1 := forward _ _ _ t h1 p1 (zz.symm ▸ hd.2.2)
  cases he : e.direct with
  | true =>
    simp only [he,ite_true] at rest
    rw [rest,triple_value,zz] at b1
    exact b1 hd.2.1
  | false =>
    simp only [he,Bool.false_eq_true,ite_false] at rest
    obtain ⟨h2,p2,ra,rb,ma,mb⟩ := rest
    have residue : DirectedEleven.value e.middle t%48=17 := by
      simp [DirectedEleven.value,Nat.add_mod,Nat.mul_mod,ra,rb]
    have smaller : DirectedEleven.value e.middle t<z := by
      rw [←zz]; exact Nat.add_lt_add_of_le_of_lt (Nat.mul_le_mul_right t ma) mb
    have b2 : ¬Basin (3*DirectedEleven.value e.middle t) := fun h =>
      (Nat.not_le_of_gt smaller) (least _ ⟨residue,h,b1⟩)
    have result := forward _ _ _ t h2 p2 ((triple_value _ _).symm ▸ b2)
    rw [triple_value,zz] at result
    exact result hd.2.1

#print axioms census
#print axioms least_excluded
end GuardedResidueCover

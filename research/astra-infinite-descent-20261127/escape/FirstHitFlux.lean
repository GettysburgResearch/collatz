import MantissaFlow
import FiniteExtinction

/-! A finite, target-uniform comparison for first-entrance clock and grade
atoms of the ordinary shortcut map. The right side is an explicit count of
cells failing the specified finite merger and target-avoidance tests. -/
set_option autoImplicit false
set_option warningAsError true
namespace FirstHitFlux
open CoreBranching PeakRigidity MantissaFlow FiniteExtinction

def First (S : Finset ℕ) (z m : ℕ) : Prop := run m z∈S ∧ ∀j : Fin m, run j.val z∉S
instance (S : Finset ℕ) (z m : ℕ) : Decidable (First S z m) := by unfold First; infer_instance

def Gap (n k : ℕ) : ℕ := if k<8*n then 1 else 2

def Merge (s L x y : ℕ) : Prop :=
  run (L+s) x=run L y ∧ grade (L+s) x=grade L y+1
instance (s L x y : ℕ) : Decidable (Merge s L x y) := by unfold Merge; infer_instance

def Protected (S : Finset ℕ) (L x : ℕ) : Prop := ∀j : Fin (L+1), run j.val x∉S
instance (S : Finset ℕ) (L x : ℕ) : Decidable (Protected S L x) := by unfold Protected; infer_instance

def Good (n L : ℕ) (S : Finset ℕ) (k : ℕ) : Prop :=
  Merge (Gap n k) L (k/3) (dst n k) ∧
  Protected S (L+Gap n k) (k/3) ∧ Protected S L (dst n k)
instance (n L : ℕ) (S : Finset ℕ) (k : ℕ) : Decidable (Good n L S k) := by
  unfold Good; infer_instance

/-- At an actual protected merger, every true first visit on the left is a
true earlier visit on the right, at both cost coordinates. -/
theorem first_transfer (S : Finset ℕ) {s L x y m : ℕ} (meet : Merge s L x y)
    (left : Protected S (L+s) x) (right : Protected S L y) (first : First S x m) :
    ∃j, First S y j ∧ m=j+s ∧ grade m x=grade j y+1 := by
  obtain ⟨rm,gm⟩:=meet
  have late : L+s<m := by
    by_contra! early
    exact left ⟨m,by omega⟩ first.1
  let e:=m-(L+s)
  have total : L+s+e=m := by dsimp [e]; omega
  have state : run (L+e) y=run m x := by rw [←total,run_add L e y,run_add (L+s) e x,rm]
  have gr := grade_add (L+s) e x
  rw [total,gm,rm] at gr
  have gr' := grade_add L e y
  refine ⟨L+e,⟨state ▸ first.1,?_⟩,by omega,by omega⟩
  intro j comes
  by_cases early : j.val≤L
  · exact right ⟨j.val,by omega⟩ comes
  · let v:=j.val-L
    have locate : L+v=j.val := by dsimp [v]; omega
    have jb:=j.isLt
    have before : L+s+v<m := by omega
    have through : run (L+s+v) x=run j.val y := by
      rw [←locate,run_add (L+s) v x,run_add L v y,rm]
    exact first.2 ⟨L+s+v,before⟩ (through ▸ comes)

private theorem first_unique {S : Finset ℕ} {x a b : ℕ} (left : First S x a)
    (right : First S x b) : a=b := by
  rcases lt_trichotomy a b with ab|ab|ab
  · exact (right.2 ⟨a,ab⟩ left.1).elim
  · exact ab
  · exact (left.2 ⟨b,ab⟩ right.1).elim

/-- First-hit score through a finite physical deadline, allowing either the
clock or the grade to be erased. -/
def Row (S : Finset ℕ) (H a b t x : ℕ) : Prop :=
  ∃j : Fin (H+1), First S x j.val ∧ a*j.val+b*grade j.val x=t
instance (S : Finset ℕ) (H a b t x : ℕ) : Decidable (Row S H a b t x) := by
  unfold Row; infer_instance

private def Lower (S : Finset ℕ) (H a b t x : ℕ) : Prop :=
  ∃j : Fin (H+1), First S x j.val ∧ a*j.val+b*grade j.val x<t
private instance (S : Finset ℕ) (H a b t x : ℕ) : Decidable (Lower S H a b t x) := by
  unfold Lower; infer_instance

/-- Integer flux bound using exactly the failed ordinary comparison cells.
Every target, deadline and integer score is supplied without analytic input. -/
theorem first_atom (n L : ℕ) (np : 0<n) (S : Finset ℕ) (H a b t : ℕ) (positive : 0<a+b) :
    3*((Finset.range (2*n)).filter (fun i=>Row S H a b t (2*n+i))).card ≤
      2*((Finset.range (6*n)).filter (fun i=>¬Good n L S (6*n+i))).card := by
  apply atom_card n np (Row S H a b t) (Lower S H a b t) (fun k=>¬Good n L S k)
  · rintro x ⟨j,jf,js⟩ ⟨k,kf,ks⟩
    have eq := first_unique jf kf
    rw [eq] at js
    omega
  · intro k _ _ okay src
    have ok := of_not_not okay
    obtain ⟨meet,protectedLeft,protectedRight⟩:=ok
    obtain ⟨j,jf,level⟩ : ∃j : Fin (H+1), First S (k/3) j.val ∧
        a*j.val+b*grade j.val (k/3)≤t := by
      rcases src with ⟨j,jf,js⟩|⟨j,jf,js⟩
      · exact ⟨j,jf,js.le⟩
      · exact ⟨j,jf,js.le⟩
    obtain ⟨u,uf,tm,gr⟩:=first_transfer S meet protectedLeft protectedRight jf
    have lb:=j.isLt
    have gs : 0<Gap n k := by unfold Gap; split <;> decide
    have inc : 0<a*Gap n k+b := by
      rcases Nat.eq_zero_or_pos a with hz|hp
      · simp_all
      · exact Nat.add_pos_left (Nat.mul_pos hp gs) b
    have score : a*j.val+b*grade j.val (k/3)=a*u+b*grade u (dst n k)+(a*Gap n k+b) := by
      rw [gr,tm]; ring
    refine ⟨⟨u,by omega⟩,uf,?_⟩
    change a*u+b*grade u (dst n k)<t
    omega

#print axioms first_transfer
#print axioms first_atom
end FirstHitFlux

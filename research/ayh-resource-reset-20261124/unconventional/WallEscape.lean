import WallDensity

namespace WallEscape
open WallDichotomy WallRational WallGeneral WallRefinement

/-- Escape on integer numerators of the ordinary 3x+d shortcut. -/
def Escapes (d a : Int) : Prop := ∀ M : Nat, ∃ J, ∀ i≥J, (M:Int)<runD d i a

private theorem no_return (d a : Int) (acyclic : ¬Repeats d a) {i j : Nat} (lt : i<j) :
    runD d i a≠runD d j a := by
  intro hit
  apply acyclic
  refine ⟨i,j-i,by omega,?_⟩
  rw [←runD_add,show i+(j-i)=j by omega]
  exact hit.symm

private theorem lower (d a : Int) (dp : 0<d) (lo : -d<a) (h : Nat) :
    -d<runD d h a := by
  induction h generalizing a with
  | zero => exact lo
  | succ h ih =>
    apply ih
    unfold step;split <;> omega

private theorem increasing_tail (f : Nat → Nat) (distinct : ∀ i j, i<j → f i≠f j)
    (m : Nat) : ∃ J, ∀ i≥J, m<f i := by
  classical
  have last (v : Nat) : ∃ J, ∀ i≥J, f i≠v := by
    by_cases found : ∃ i,f i=v
    · obtain ⟨k,hit⟩ := found
      refine ⟨k+1,?_⟩
      intro i le eq
      exact distinct k i (by omega) (hit.trans eq.symm)
    · exact ⟨0,fun i _ eq => found ⟨i,eq⟩⟩
  induction m with
  | zero =>
    obtain ⟨j,no⟩ := last 0
    exact ⟨j,fun i le => Nat.pos_of_ne_zero (no i le)⟩
  | succ m ih =>
    obtain ⟨j,large⟩ := ih
    obtain ⟨k,no⟩ := last (m+1)
    refine ⟨j+k,?_⟩
    intro i h
    have e := no i (by omega)
    have g := large i (by omega)
    omega

theorem positive_escape (d : Nat) (a : Int) (dp : 0<d) (lo : -(d:Int)<a)
    (acyclic : ¬Repeats d a) : Escapes d a := by
  let f := fun i => (runD d i a+d).toNat
  have rep (i : Nat) : (f i:Int)=runD d i a+d := by
    apply Int.toNat_of_nonneg
    have v := lower d a (by omega) lo i
    omega
  have inj : ∀ i j, i<j → f i≠f j := by
    intro i j le same
    apply no_return d a acyclic le
    have e := congrArg Int.ofNat same
    change (f i:Int)=(f j:Int) at e
    rw [rep,rep] at e
    omega
  intro M
  obtain ⟨J,high⟩ := increasing_tail f inj (M+d)
  refine ⟨J,?_⟩
  intro i hi
  have e := high i hi
  have z := rep i
  omega

/-- Arbitrarily long arbitrarily late powers of any nonconstant, nonalternating
word on one specified ordinary wall force one of two explicit generalized
integer trajectories to escape to positive infinity. -/
theorem forces_escape (C : Coloring) {n : Nat} (cut : Mixed C n)
    (L p d : Nat) (pos : 0<L) (pp : 0<p) (small : p<d) (den : d+1=2^L)
    (oneThird : 3*p≠d) (twoThirds : 3*p≠2*d)
    (powers : ∀ B, 0<B → ∀ J, ∃ j≥J, WallWords.Copies C n j L p B) :
    Escapes d (-(p:Int)) ∨ Escapes d ((d:Int)-p) := by
  classical
  by_cases left : Repeats d (-(p:Int))
  · by_cases right : Repeats d ((d:Int)-p)
    · rcases alternating_or_eventual_cap L p d pos pp small den left right with frac|frac|cap
      · exact False.elim (oneThird frac)
      · exact False.elim (twoThirds frac)
      · obtain ⟨B,bp,all⟩ := cap
        obtain ⟨J,none⟩ := all C n cut
        obtain ⟨j,big,yes⟩ := powers B bp J
        exact False.elim (none j big yes)
    · exact Or.inr (positive_escape d ((d:Int)-p) (by omega) (by omega) right)
  · exact Or.inl (positive_escape d (-(p:Int)) (by omega) (by omega) left)

end WallEscape

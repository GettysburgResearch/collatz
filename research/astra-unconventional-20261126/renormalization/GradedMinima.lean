import RankTwoControl

/-! Arbitrary positive sources at a requested compensated grade of one supplied
reference. At a known hit the minimum is a specific power of two. -/
namespace Collatz.GradedMinima
open Collatz.SourceDeletion Collatz.RankTwoControl Collatz.PhysicalWindow

def Linked (u N y j : Nat) : Prop :=
  ∃ h, run h u=run h y ∧ N+odds h u=j+odds h y

/-- An actual reference hit makes the phase and grade of every permitted
visitor hit explicit. The clock in the conclusion can exceed the first hit. -/
theorem charge_of_link {u N y j H : Nat} (hit : run H y=1) (link : Linked u N y j) :
    ∃ J, run J u=1 ∧ 2*(N+odds J u)+H=2*(j+odds H y)+J := by
  obtain ⟨h,same,pay⟩ := link
  let J := H+2*h
  obtain ⟨refV,refP⟩ := Collatz.RankTwoControl.append H (2*h) y
  rw [hit,(cycle_pairs h).1] at refV
  rw [hit,(cycle_pairs h).2] at refP
  obtain ⟨visV,visP⟩ := Collatz.RankTwoControl.append h (J-h) u
  obtain ⟨lateV,lateP⟩ := Collatz.RankTwoControl.append h (J-h) y
  have le : h≤J := by dsimp [J]; omega
  rw [Nat.add_sub_of_le le,same] at visV visP
  rw [Nat.add_sub_of_le le] at lateV lateP
  exact ⟨J,visV.trans (lateV.symm.trans refV),by dsimp [J] at *; omega⟩

/-- A matching charge at two independently supplied positive hits is also
sufficient for a compensated equal-clock merger. -/
theorem link_of_charge {u N y j H J : Nat} (hu : run J u=1) (hy : run H y=1)
    (eqn : 2*(N+odds J u)+H=2*(j+odds H y)+J) : Linked u N y j := by
  let a := j+odds H y
  let b := N+odds J u
  obtain ⟨uV,uP⟩ := Collatz.RankTwoControl.append J (2*a) u
  obtain ⟨yV,yP⟩ := Collatz.RankTwoControl.append H (2*b) y
  rw [hu,(cycle_pairs a).1] at uV
  rw [hu,(cycle_pairs a).2] at uP
  rw [hy,(cycle_pairs b).1] at yV
  rw [hy,(cycle_pairs b).2] at yP
  have date : J+2*a=H+2*b := by dsimp [a,b]; omega
  rw [←date] at yV yP
  exact ⟨J+2*a,uV.trans yV.symm,by dsimp [a,b] at *; omega⟩

private theorem pure (d : Nat) : run d (2^d)=1 ∧ odds d (2^d)=0 := by
  induction d with
  | zero => decide
  | succ d ih =>
    have s : step (2^d*2)=2^d := by unfold step; split <;> omega
    rw [pow_succ,run,odds,s,ih.1,ih.2]; omega

private theorem four (p : Nat) : (4:Nat)^p=2^(2*p) := by rw [pow_mul]; norm_num

/-- This cap applies also when the formal optimum would have a negative
power of two. No truncating natural subtraction occurs in the inequality. -/
theorem linked_lower {u N y j H : Nat} (pos : 0<u) (hy : run H y=1)
    (link : Linked u N y j) : 2^(2*N+H)≤2^(2*(j+odds H y))*u := by
  obtain ⟨J,hu,pay⟩ := charge_of_link hy link
  have g := growth J u pos
  rw [hu,Nat.mul_one,four] at g
  have id : (2:Nat)^(2*N+H)*2^(2*odds J u) = 2^(2*(j+odds H y))*2^J := by
    rw [←pow_add,←pow_add]
    congr 1
    omega
  have cmp : 2^(2*odds J u)*2^(2*N+H) ≤ 2^(2*odds J u)*(2^(2*(j+odds H y))*u) := calc
    _ = 2^(2*(j+odds H y))*2^J := by rw [Nat.mul_comm,id]
    _ ≤ 2^(2*(j+odds H y))*(2^(2*odds J u)*u) := Nat.mul_le_mul_left _ g
    _ = _ := by ring
  exact Nat.le_of_mul_le_mul_left cmp (Nat.two_pow_pos _)

/-- At every grade with nonnegative dyadic exponent the least permitted
positive source is exactly the stated power of two. -/
theorem upper_minimum {y j N H e : Nat} (hy : run H y=1)
    (balance : e+2*(j+odds H y)=2*N+H) :
    Linked (2^e) N y j ∧ ∀ u, 0<u → Linked u N y j → 2^e≤u := by
  refine ⟨link_of_charge (pure e).1 hy (by rw [(pure e).2]; omega),?_⟩
  intro u pos link
  have lower := linked_lower pos hy link
  rw [←balance,pow_add,Nat.mul_comm] at lower
  exact Nat.le_of_mul_le_mul_left lower (Nat.two_pow_pos _)

/-- A bounded normalized growth of the supplied lower *through the actual
meeting clock* prices both arms of a simultaneous reset. The upper input is
the original finite hit, not a density estimate about another component. -/
theorem paired_cost {u y g H h C : Nat} (pu : 0<u)
    (upper : run H (3*y)=1) (upLink : Linked (3*u) g (3*y) 0)
    (lower : run h u=run h y) (paid : g+odds h u=odds h y)
    (bound : 2^h*run h y≤C*3^(odds h y)*y) :
    4^g*2^H≤4^(odds H (3*y))*(3*(C*3^g*y)) := by
  have low := affine h u
  rw [lower] at low
  have cmp : 3^(odds h u)*u≤3^(odds h u)*(C*3^g*y) := calc
    _ ≤ 2^h*run h y := by omega
    _ ≤ C*3^(odds h y)*y := bound
    _ = _ := by rw [←paid,pow_add]; ring
  have cap := Nat.le_of_mul_le_mul_left cmp (Nat.pow_pos (by decide : 0<(3:Nat)))
  have high := linked_lower (u:=3*u) (by omega) upper upLink
  simp only [Nat.zero_add,pow_add,←four] at high
  exact high.trans (Nat.mul_le_mul_left _ (Nat.mul_le_mul_left 3 cap))

#print axioms charge_of_link
#print axioms link_of_charge
#print axioms linked_lower
#print axioms upper_minimum
#print axioms paired_cost
end Collatz.GradedMinima

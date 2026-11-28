import ExponentCylinders
import ReturnDescentFixed

/-! Physical canonical-parent blocks and a decidable supplied-exponent
reduction. The density bound on the retained arithmetic rows is written. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.HardParentBlocks
open Itinerary Itinerary.ReturnDescent Itinerary.TowerFrontier

private theorem matching_run (n x : ℕ) : TwoGapRouting.run n x=Itinerary.run n x := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih => exact ih (TwoGapRouting.step x)

def exponent (j : ℕ) : ℕ := 11+162*j

private theorem parent_exact (j : ℕ) :
    81*hardParent (exponent j)+271=2^(exponent j+7) := by
  have shape : 2^(exponent j+7)=2^18*(2^162)^j := by
    rw [show exponent j+7=18+162*j by unfold exponent; omega,Nat.pow_add,Nat.pow_mul]
  have residue : 2^(exponent j+7)%81=28 := by
    rw [shape,Nat.mul_mod,Nat.pow_mod (2^162) j,show (2:ℕ)^162%81=1 by decide]
    simp
  have large : 271≤2^(exponent j+7) := by
    exact (by decide : 271≤2^18).trans (Nat.pow_le_pow_right (by decide : 0<2) (by unfold exponent; omega))
  unfold hardParent
  omega

private theorem smaller (j i : ℕ) (ip : 0<i) :
    2^(162*i)*hardParent (exponent j)<hardParent (exponent (j+i)) := by
  have shift : 2^(exponent (j+i)+7)=2^(162*i)*2^(exponent j+7) := by
    rw [←Nat.pow_add]; congr 1; unfold exponent; ring
  rw [←parent_exact,←parent_exact] at shift
  have two : 2≤2^(162*i) := by
    simpa only [Nat.pow_one] using Nat.pow_le_pow_right (by decide : 0<2) (show 1≤162*i by omega)
  nlinarith

private theorem itinerary (j H : ℕ) : run (7+exponent j+H) (hardParent (exponent j))=
    run H (3^(exponent j)-1) := by
  obtain ⟨_,_,hit,_⟩:=hard_source j
  rw [run_add,run_add,show run 7 (hardParent (exponent j))=M (exponent j) from hit,peak]

/-- Every assigned progression of lower row indices contains a whole
subprogression with every indicated later hard parent tied to the lower
one. The actual triple certificates and exponential height improvements
are retained at the explicit canonical sources. -/
theorem canonical_chains (a b K : ℕ) (bp : 0<b) :
    ∃r P H : ℕ, 0<P ∧ ∀u i : ℕ, i≤K →
      let j:=a+b*(r+P*u)
      let m:=exponent j
      let M':=exponent (j+i)
      run (7+M'+H) (hardParent M')=run (7+m+H) (hardParent m) ∧
      hardParent M'%48=17 ∧ track (M'+7) (3*hardParent M') 0=(1,3) ∧
      (0<i → 2^(162*i)*hardParent m<hardParent M') := by
  let offsets:=(List.range (K+1)).map (fun n => 162*n)
  obtain ⟨r,P,H,pp,visits⟩:=ExponentCylinders.peak_progression (exponent a) (162*b) (by omega) offsets
  refine ⟨r,P,H,pp,?_⟩
  intro u i le
  let j:=a+b*(r+P*u)
  have hi : 162*i∈offsets := List.mem_map.mpr ⟨i,List.mem_range.mpr (by omega),rfl⟩
  have meet := (visits u _ hi).1
  have ej : exponent a+162*b*(r+P*u)=exponent j := by dsimp [j,exponent]; ring
  have ei : exponent j+162*i=exponent (j+i) := by dsimp [exponent]; ring
  rw [ej,ei,matching_run,matching_run] at meet
  have data:=hard_source (j+i)
  exact ⟨(itinerary (j+i) H).trans (meet.trans (itinerary j H).symm),data.2.1,data.2.2.2,smaller j i⟩

/-- Physical equalities at the supplied two adjacent Mersenne peaks. -/
def Retained (deadline : ℕ → ℕ) (m : ℕ) : Prop :=
  m=1 ∨ run (deadline m) (3^m-1)≠run (deadline m) (3^(m-1)-1) ∨
  m+TwoGapRouting.odds (deadline m) (3^m-1)≠
    (m-1)+TwoGapRouting.odds (deadline m) (3^(m-1)-1)

instance (deadline : ℕ → ℕ) (m : ℕ) : Decidable (Retained deadline m) :=
  inferInstanceAs (Decidable (_ ∨ _ ∨ _))

/-- The retained test has exactly the Mersenne convergence consequence
for every schedule of pointwise finite deadlines. -/
theorem mersenne_iff_retained (deadline : ℕ → ℕ) :
    (∀m : ℕ, 0<m → ReachesOne (M m)) ↔
    (∀m : ℕ, 0<m → Retained deadline m → ReachesOne (M m)) := by
  constructor
  · exact fun all m mp _ => all m mp
  intro kept m
  induction m with
  | zero => omega
  | succ m ih =>
    intro mp
    by_cases retained : Retained deadline (m+1)
    · exact kept _ mp retained
    have positive : 0<m := by
      by_contra h
      have eq : m=0 := by omega
      exact retained (Or.inl (by omega))
    have equal : run (deadline (m+1)) (3^(m+1)-1)=run (deadline (m+1)) (3^m-1) := by
      by_contra ne
      exact retained (Or.inr (Or.inl (by simpa only [Nat.add_sub_cancel] using ne)))
    apply reaches_of_meets (ih positive)
    exact ⟨(m+1)+deadline (m+1),m+deadline (m+1),by rw [run_add (m+1),run_add m (deadline (m+1)),peak,peak,equal]⟩

#print axioms canonical_chains
#print axioms mersenne_iff_retained
end Collatz.HardParentBlocks

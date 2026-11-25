module

public import BasinTransport
public import MinimumDescent
public import TowerFrontierMergers
import all TernaryItinerary
import all MinimumDescent

public section
namespace Collatz.Itinerary.TowerRecurrence

set_option autoImplicit false

private theorem scaling (e x : Nat) : ReachesOne (2^e*x) ↔ ReachesOne x := by
  have h := MinimumDescent.good_run e (2^e*x)
  rwa [halve,iff_comm] at h

private theorem equal_labels {a b h j : Nat} (eq : run h a=run j b) :
    ReachesOne a ↔ ReachesOne b := by
  have first := MinimumDescent.good_run h a
  rw [eq] at first
  exact first.symm.trans (MinimumDescent.good_run j b)

/-- The shifted-ray tripling descent of PR 146, for the basin label itself. -/
theorem universal_of_odd_tripling
    (trip : ∀ n, n%2=1 → (ReachesOne n ↔ ReachesOne (3*n))) : Universal := by
  have powers (k n : Nat) (odd : n%2=1) : ReachesOne n ↔ ReachesOne (3^k*n) := by
    induction k with
    | zero => simp
    | succ k ih =>
      have o : (3^k*n)%2=1 := by simp [Nat.mul_mod,Nat.pow_mod,odd]
      simpa only [Nat.pow_succ,Nat.mul_right_comm,Nat.mul_comm 3] using
        ih.trans (trip _ o)
  have exchange (k m : Nat) (pos : 0<m) : ReachesOne (2^k*m-1) ↔ ReachesOne (3^k*m-1) := by
    apply equal_labels (h:=k) (j:=0)
    simpa using BasinTransport.affine_rays k 0 0 m pos
  have double_shift (m : Nat) (pos : 0<m) : ReachesOne (4*m-1) ↔ ReachesOne (8*m-1) := by
    have ray := exchange 2 m pos
    change ReachesOne (4*m-1) ↔ ReachesOne (9*m-1) at ray
    have link : ReachesOne (3*(8*m-1)) ↔ ReachesOne (9*m-1) := by
      have actual : run 1 (3*(8*m-1))=4*(9*m-1) := by
        change step (3*(8*m-1))=4*(9*m-1)
        unfold step; split <;> omega
      have down := MinimumDescent.good_run 1 (3*(8*m-1))
      rw [actual] at down
      exact down.symm.trans (scaling 2 (9*m-1))
    exact ray.trans ((trip (8*m-1) (by omega)).trans link).symm
  have extra (i h : Nat) (pos : 0<h) :
      ReachesOne (4*h-1) ↔ ReachesOne (4*(2^i*h)-1) := by
    induction i with
    | zero => simp
    | succ i ih =>
      have more := double_shift (2^i*h) (Nat.mul_pos (Nat.pow_pos (by decide)) pos)
      rw [show 4*(2^(i+1)*h)=8*(2^i*h) by rw [Nat.pow_succ]; grind]
      exact ih.trans more
  have cell (y : Nat) (tag : y%16=3 ∨ y%16=5) : ReachesOne (y-1) ↔ ReachesOne y := by
    rcases tag with h | h
    · apply equal_labels (h:=4) (j:=4)
      simp only [run]; unfold step; repeat' first | omega | split
    · apply equal_labels (h:=3) (j:=3)
      simp only [run]; unfold step; repeat' first | omega | split
  have table : ∀ z : Fin 16, z.val%2=1 → ∃ i : Fin 4,
      (3^i.val*z.val)%16=3 ∨ (3^i.val*z.val)%16=5 := by decide
  have descend (h : Nat) (pos : 0<h) : ReachesOne (4*h-1) ↔ ReachesOne h := by
    obtain ⟨v,u,eq,odd⟩ := split_twos h pos
    let z := 3^(v+2)*u
    have oz : z%2=1 := by simp [z,Nat.mul_mod,Nat.pow_mod,odd]
    obtain ⟨i,hit⟩ := table ⟨z%16,by omega⟩ (by change z%16%2=1; omega)
    let t := i.val+(v+2)
    have pair : 3^t*u=3^i.val*z := by simp [t,z,Nat.pow_add,Nat.mul_assoc]
    have md : (3^t*u)%16=(3^i.val*(z%16))%16 := by rw [pair,Nat.mul_mod]; simp [Nat.mul_mod]
    have tag : (3^t*u)%16=3 ∨ (3^t*u)%16=5 := by rw [md]; exact hit
    have align : 4*(2^i.val*h)=2^t*u := by rw [eq]; simp only [t,Nat.pow_add]; grind
    calc
      ReachesOne (4*h-1) ↔ ReachesOne (4*(2^i.val*h)-1) := extra i.val h pos
      _ ↔ ReachesOne (3^t*u-1) := by rw [align]; exact exchange t u (by omega)
      _ ↔ ReachesOne (3^t*u) := cell _ tag
      _ ↔ ReachesOne u := (powers t u odd).symm
      _ ↔ ReachesOne h := by rw [eq]; exact (scaling v u).symm
  intro n
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro pos
    by_cases one : n=1
    · subst n; exact ⟨0,rfl⟩
    by_cases even : n%2=0
    · have eq : n=2*(n/2) := by omega
      have done : ReachesOne (2*(n/2)) := (scaling 1 (n/2)).mpr
        (ih (n/2) (by omega) (by omega))
      rwa [←eq] at done
    by_cases rem : n%4=1
    · have hit : run 2 n=(3*n+1)/4 := by simp only [run]; unfold step; split <;> split <;> omega
      apply (MinimumDescent.good_run 2 n).mp
      rw [hit]; exact ih _ (by omega) (by omega)
    · let h := (n+1)/4
      have eq : n=4*h-1 := by dsimp [h]; omega
      have small : h<n := by dsimp [h]; omega
      have posH : 0<h := by dsimp [h]; omega
      exact eq ▸ (descend h posH).mpr (ih h small posH)

def Change (w r : Nat) : Prop :=
  ¬(ReachesOne (3^r*w) ↔ ReachesOne (3^(r+1)*w))

/-- A failure of tripling at rank zero cannot recur within every block of
512 candidate edges. This equivalence uses the checked numerical mergers. -/
theorem universal_iff_recurring_changes : Universal ↔
    ∀ w, w%2=1 → Change w 0 → ∀ s, ∃ i, i<512 ∧ Change w (s+i) := by
  constructor
  · intro all w odd ch
    apply False.elim
    apply ch
    exact ⟨fun _ => all _ (by simp; omega),fun _ => all _ (by simp; omega)⟩
  · intro returns
    apply universal_of_odd_tripling
    intro w odd
    apply Classical.byContradiction
    intro ne
    have ch : Change w 0 := by simpa [Change] using ne
    obtain ⟨d,_,y,_,common⟩ := TowerFrontier.recurring_common_endpoint w 0 odd
    obtain ⟨i,hi,different⟩ := returns w odd ch d
    apply different
    apply equal_labels (h:=1381) (j:=1381)
    simpa only [Nat.zero_add,Nat.add_assoc] using
      (common i (by omega)).trans (common (i+1) (by omega)).symm

#print axioms universal_of_odd_tripling
#print axioms universal_iff_recurring_changes

/-- The arbitrary-width version takes the ordinary common-block statement
explicitly. A syndetic change means that every interval of some fixed length
contains a change. Its length may depend on the original odd source. -/
theorem universal_iff_syndetic_changes
    (blocks : ∀ w, w%2=1 → ∀ L : Nat, ∃ s h y,
      ∀ i≤L, run h (3^(s+i)*w)=y) :
    Universal ↔ ∀ w, w%2=1 → Change w 0 →
      ∃ L, ∀ s, ∃ i, i<L ∧ Change w (s+i) := by
  constructor
  · intro all w odd changed
    exact ⟨512,universal_iff_recurring_changes.mp all w odd changed⟩
  · intro recurring
    apply universal_of_odd_tripling
    intro w odd
    apply Classical.byContradiction
    intro ne
    have initial : Change w 0 := by simpa [Change] using ne
    obtain ⟨L,frequent⟩ := recurring w odd initial
    obtain ⟨s,h,y,common⟩ := blocks w odd L
    obtain ⟨i,small,different⟩ := frequent s
    apply different
    apply equal_labels (h:=h) (j:=h)
    simpa only [Nat.add_assoc] using
      (common i (by omega)).trans (common (i+1) small).symm

#print axioms universal_iff_syndetic_changes
end Collatz.Itinerary.TowerRecurrence

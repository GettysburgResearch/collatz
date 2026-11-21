import DyadicMixing

/-! Finite, unanchored comparisons on five copies of the first dyadic octave. -/

namespace CollatzShell.PeriodicWindow

open Finset

def meetsBy (t x y : Nat) : Bool :=
  decide (∃ i j : Fin (t+1), orbit i.val x = orbit j.val y)

def unmatched (p t : Nat) : Finset Nat :=
  (Ico p (6*p)).filter (fun x => meetsBy t x (p+x%p) = false)

private theorem lift_clock {x y t T : Nat} (ht : t≤T) (h : meetsBy t x y=true) :
    meetsBy T x y=true := by
  unfold meetsBy at *
  rw [decide_eq_true_eq] at *
  obtain ⟨i,j,eq⟩ := h
  exact ⟨⟨i.val,by omega⟩,⟨j.val,by omega⟩,eq⟩

private theorem finite_clock {P : Nat → Nat → Bool} (S : Finset Nat)
    (up : ∀ x t T, t≤T → P x t=true → P x T=true)
    (each : ∀ x ∈ S, ∃ t, P x t=true) : ∃ t, ∀ x ∈ S, P x t=true := by
  induction S using Finset.induction_on with
  | empty => exact ⟨0,by simp⟩
  | insert x s _ ih =>
    obtain ⟨a,ha⟩ := each x (mem_insert_self _ _)
    obtain ⟨b,hb⟩ := ih (fun y hy => each y (mem_insert_of_mem hy))
    refine ⟨max a b,?_⟩
    intro y hy
    rcases mem_insert.mp hy with rfl | h
    · exact up _ _ _ (le_max_left _ _) ha
    · exact up _ _ _ (le_max_right _ _) (hb _ h)

private theorem empty_unmatched (all : Universal) {p : Nat} (hp : 0<p) : ∃ t, unmatched p t=∅ := by
  let P (x t : Nat) := meetsBy t x (p+x%p)
  have each (x : Nat) (hx : x ∈ Ico p (6*p)) : ∃ t, P x t=true := by
    have xp := (mem_Ico.mp hx).1
    obtain ⟨a,ha⟩ := all x (by omega)
    obtain ⟨b,hb⟩ := all (p+x%p) (by omega)
    refine ⟨max a b,?_⟩
    apply decide_eq_true
    exact ⟨⟨a,by omega⟩,⟨b,by omega⟩,ha.trans hb.symm⟩
  obtain ⟨t,ht⟩ := finite_clock (P:=P) _ (fun _ _ _ le h => lift_clock le h) each
  refine ⟨t,eq_empty_iff_forall_notMem.mpr ?_⟩
  intro x hx
  obtain ⟨mem,no⟩ := mem_filter.mp hx
  exact Bool.noConfusion ((ht x mem).symm.trans no)

private theorem basin_laws : Laws Basin := by
  constructor
  · intro n; apply propext; exact basin_at_hit ⟨1,step_double n⟩
  · intro n; apply propext; apply basin_at_hit; refine ⟨1,?_⟩
    change step (2*n+1)=3*n+2; unfold step; split <;> omega

private theorem labels_meet {t x y : Nat} (h : meetsBy t x y=true) : Basin x=Basin y := by
  unfold meetsBy at h
  obtain ⟨i,j,eq⟩ := decide_eq_true_eq.mp h
  exact propext ((basin_at_hit (x:=x) ⟨i.val,rfl⟩).trans
    (by rw [eq]; exact (basin_at_hit (x:=y) ⟨j.val,rfl⟩).symm))

private theorem unit_survives_cut {p s q : Nat} (hu : q%3≠0) (S : Finset Nat) (small : S.card<2^s)
    (size : 64^s*((firstMesh 2 (by decide)).cost*q+6) ≤ 3^s*p) :
    ∃ x, p≤x ∧ x≤2*p ∧ x∉S ∧ (Basin x ↔ Basin q) := by
  obtain ⟨t,f,inj,hf⟩ := shell_fan (h:=1) (firstMesh 2 (by decide)) s q p hu size
  obtain ⟨w,clear⟩ := avoids_small f inj S small
  obtain ⟨lo,hi,_,hit⟩ := hf w
  exact ⟨f w,lo,by simpa using hi,clear,basin_at_hit ⟨t,hit⟩⟩

/-- One successful finite comparison test recovers an arbitrary supplied ternary unit. -/
theorem recover_from_comparisons (s q t : Nat) (hu : q%3≠0)
    (size : (firstMesh 2 (by decide)).cost*q+6 ≤ 3^s)
    (ok : (24*s+1)*(unmatched (64^s) t).card+1 < 2^s) : Basin q := by
  classical
  let p := 64^s
  have pe : 2^(6*s)=p := by dsimp [p]; rw [pow_mul]; norm_num
  let g (x : Nat) := Basin (p+x%p)
  have per : Period g (2^(6*s)) := by intro x; simp only [g,pe,Nat.add_mod_right]
  let E := unmatched p t
  have fit (x : Nat) (lo : 2^(6*s)≤x) (hi : x<6*2^(6*s)) (clear : x∉E) : Basin x=g x := by
    apply labels_meet (t:=t)
    have mem : x ∈ Ico p (6*p) := mem_Ico.mpr ⟨pe ▸ lo,pe ▸ hi⟩
    by_cases h : meetsBy t x (p+x%p)=false
    · exact False.elim (clear (mem_filter.mpr ⟨mem,h⟩))
    · exact Bool.eq_true_of_not_eq_false h
  obtain ⟨c,S,card,flat⟩ := octave_rigidity (6*s) basin_laws per E fit
  have small : S.card<2^s := card.trans_lt (by simpa only [E,p,show 4*(6*s)=24*s by omega] using ok)
  have sizeq : 64^s*((firstMesh 2 (by decide)).cost*q+6) ≤ 3^s*p :=
    (Nat.mul_le_mul_left p size).trans_eq (Nat.mul_comm _ _)
  have size1 : 64^s*((firstMesh 2 (by decide)).cost*1+6) ≤ 3^s*p := by
    apply le_trans _ sizeq
    exact Nat.mul_le_mul_left _ (Nat.add_le_add_right (Nat.mul_le_mul_left _ (by omega : 1≤q)) _)
  obtain ⟨x,xl,xu,xc,hx⟩ := unit_survives_cut hu S small sizeq
  obtain ⟨y,yl,yu,yc,hy⟩ := unit_survives_cut (q:=1) (by decide) S small size1
  rw [pe] at flat
  have same : Basin x=Basin y := (flat _ xl xu xc).trans (flat _ yl yu yc).symm
  exact hx.mp (same.mpr (hy.mpr ⟨0,rfl⟩))

/-- Full positive-integer Collatz from unbounded stages of finite, unanchored mergers. -/
theorem collatz_iff_octave_comparisons : Universal ↔
    ∀ K : Nat, ∃ s≥K, ∃ t, (24*s+1)*(unmatched (64^s) t).card+1 < 2^s := by
  constructor
  · intro all K
    let s := K+1
    obtain ⟨t,ht⟩ := empty_unmatched all (p:=64^s) (by positivity)
    refine ⟨s,by dsimp [s]; omega,t,?_⟩
    simp only [ht,card_empty,Nat.mul_zero,Nat.zero_add]
    exact Nat.one_lt_pow (by dsimp [s]; omega) (by decide)
  · intro stages
    apply universal_of_units
    intro q hu
    obtain ⟨s,large,t,ok⟩ := stages ((firstMesh 2 (by decide)).cost*q+6)
    exact recover_from_comparisons s q t hu (large.trans (Nat.lt_pow_self (by decide : 1<3)).le) ok

#print axioms collatz_iff_octave_comparisons
#print axioms dyadic_stability
#print axioms annulus_rigidity

end CollatzShell.PeriodicWindow

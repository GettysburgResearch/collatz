import BlockClock
import FastPairs

/-! Uniform first-visit placement of arbitrary finite ordinary patterns
in a prescribed mixed binary/ternary source cylinder. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FastBlocks
open FastPairs

private def span : List ℕ → ℕ
  | [] => 0
  | i::F => max i (span F)

private theorem le_span {F : List ℕ} {i : ℕ} (hi : i∈F) : i≤span F := by
  induction F with
  | nil => simp at hi
  | cons j F ih =>
    rcases List.mem_cons.mp hi with eq|rest
    · exact eq ▸ le_max_left _ _
    · exact (ih rest).trans (le_max_right _ _)

/-- Every member lies inside the requested real interval and has the stated
ordinary first visit, time residue and odd grade. -/
def Placement (F : List ℕ) (v r s M Q : ℕ) (δ : ℝ) : Prop :=
  ∃C K : ℝ, ∃G : ℕ, 0<C ∧ 0<K ∧ ∀ y : ℕ, y%3≠0 → ∀X : ℝ, C*y≤X →
    ∀c t a₀ : ℕ, ∃x D a : ℕ, 0<x ∧ x ≡ r [MOD 2^v] ∧ x ≡ c [MOD 3^s] ∧
      (∀i∈0::F, X≤(x:ℝ)+i ∧ (x:ℝ)+i≤(1+δ)*X ∧
        FirstArrival.First D (x+i) y ∧ TwoGapRouting.odds D (x+i)=a) ∧
      a≤G ∧ (2:ℝ)^D*y≤K*X ∧ D ≡ t [MOD M] ∧ a ≡ a₀ [MOD Q]

/-- The same threshold and time multiplier work simultaneously for all
requested residues on the physical time and the odd count. -/
theorem of_marked_visitors (F : List ℕ) (v r s M Q : ℕ) (mp : 0<M) (qp : 0<Q)
    (δ : ℝ) (positive : 0<δ) (visitors : ∀η : ℝ, 0<η → MarkedVisitors η M Q) :
    Placement F v r s M Q δ := by
  let members (i : ℕ) := i∈0::F
  let source (c x : ℕ) := x ≡ r [MOD 2^v] ∧ x ≡ c [MOD 3^s]
  obtain ⟨H,g,core⟩:=BlockClock.cover F v r s
  have bank : Rows members source H g := by
    intro w wu c
    obtain ⟨x,xp,xb,xc,arms⟩:=core H (le_refl H) w wu c
    exact ⟨x,xp,⟨xb,xc⟩,arms⟩
  obtain ⟨C,K,G,cp,kp,all⟩:=rows_of_marked_visitors (d:=span F)
    (show members 0 from List.mem_cons_self) bank mp qp δ positive visitors
  refine ⟨C,K,G,cp,kp,?_⟩
  intro y yu X high c t a₀
  obtain ⟨x,D,a,xp,xc,lo,hi,arms,gb,speed,dm,am⟩:=all y yu X high c t a₀
  refine ⟨x,D,a,xp,xc.1,xc.2,?_,gb,speed,dm,am⟩
  intro i inside
  have bound : i≤span F := by
    rcases List.mem_cons.mp inside with eq|rest
    · omega
    · exact le_span rest
  have realBound : (i:ℝ)≤span F := by exact_mod_cast bound
  exact ⟨by linarith [show 0≤(i:ℝ) by positivity],by linarith,arms i inside⟩

theorem fast_blocks (F : List ℕ) (v r s : ℕ) (δ : ℝ) (positive : 0<δ) :
    Placement F v r s 1 1 δ :=
  of_marked_visitors F v r s 1 1 (by decide) (by decide) δ positive
    (fun η ep => trivial_marks (FastWindow.visitors η ep))

#print axioms of_marked_visitors
#print axioms fast_blocks
end Collatz.FastBlocks

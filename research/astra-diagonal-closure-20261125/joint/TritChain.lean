import SourceDeletion
import Mathlib.Data.Finset.Card

/-! A finite trit-chain obstruction to a small deficiency at every query. -/

namespace Collatz.TritChain

open Collatz.SourceDeletion

/-- An absorbing binary residue for each of the 81 trit suffixes. -/
def witness (u : Fin 81) : Nat :=
  ([3315,79,158,493,316,651,986,105,632,199,1243,879,1657,771,210,929,
    1264,735,398,1757,1823,123,1167,537,4489,439,1542,735,105,499,1799,
    1681,421,175,1470,1879,796,363,1855,9,1215,39,246,975,2334,1015,
    1015,385,8978,95,878,583,3967,219,367,249,210,63,939,63,585,211,
    487,507,5601,15,350,823,1007,31,31,105,671,7,411,47,615,195,18,
    97,2430] : List Nat)[u.val]?.getD 0

set_option maxRecDepth 200000 in
set_option maxHeartbeats 10000000 in
private theorem witness_spec : ∀ u : Fin 81,
    witness u < 2^14 ∧
    run 14 (witness u) = run 14 (81*witness u+u.val) ∧
    odds 14 (witness u) = odds 14 (81*witness u+u.val) + 4 := by decide

private theorem odds_lift (h x k : Nat) : odds h (x+2^h*k) = odds h x := by
  induction h generalizing x k with
  | zero => rfl
  | succ h ih =>
    have e : 2^(h+1)*k = 2*(2^h*k) := by ring
    by_cases he : x%2=0
    · have s : step (x+2^(h+1)*k) = step x + 2^h*k := by
        rw [e]; unfold step; split <;> omega
      simp only [odds]
      rw [s, ih, e]
      omega
    · have s : step (x+2^(h+1)*k) = step x + 2^h*(3*k) := by
        rw [e, show 2^h*(3*k)=3*(2^h*k) by ring]; unfold step; split <;> omega
      simp only [odds]
      rw [s, ih, e]
      omega

private theorem after_run (h j x : Nat) : run (h+j) x=run j (run h x) := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem after_odds (h j x : Nat) : odds (h+j) x=odds j (run h x)+odds h x := by
  induction h generalizing x with
  | zero => simp [run,odds]
  | succ h ih => rw [Nat.succ_add]; simp only [odds,run,ih]; omega

/-- Every actual ordinary member of the given binary class meets its
four-trit extension at the same clock, with the required grade correction. -/
theorem fourTritCylinder (u : Fin 81) (x h : Nat) (hr : x % 2^14 = witness u)
    (hh : 14 ≤ h) :
    run h x = run h (81*x+u.val) ∧ odds h x = odds h (81*x+u.val) + 4 := by
  obtain ⟨_, hv, hg⟩ := witness_spec u
  let k := x / 2^14
  have hx : x = witness u + 2^14*k := by
    dsimp [k]
    rw [←hr]
    exact (Nat.mod_add_div _ _).symm
  have hy : 81*x+u.val = 81*witness u+u.val+2^14*(81*k) := by
    rw [hx]; ring
  have hv' : run 14 x = run 14 (81*x+u.val) := by
    rw [hy, hx, lift, lift, hv, hg, pow_add]
    ring
  have hg' : odds 14 x = odds 14 (81*x+u.val) + 4 := by
    rw [hy, hx, odds_lift, odds_lift, hg]
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hh
  rw [after_run, after_run 14 j (81*x+u.val), after_odds, after_odds 14 j (81*x+u.val), hv', hg']
  omega

#print axioms fourTritCylinder

variable {V A : Type*} [DecidableEq V] [DecidableEq A]

/-- Number of sites at which two columns give different labels. -/
def mismatch (s : Finset V) (f g : V → A) : Nat :=
  (s.filter (fun x => f x ≠ g x)).card

private theorem triangle (s : Finset V) (f g h : V → A) :
    mismatch s f h ≤ mismatch s f g + mismatch s g h := by
  unfold mismatch
  refine (Finset.card_le_card ?_).trans (Finset.card_union_le _ _)
  intro x hx
  obtain ⟨hxs, hne⟩ := Finset.mem_filter.mp hx
  by_cases he : f x = g x
  · exact Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hxs, fun e => hne (he.trans e)⟩)
  · exact Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hxs, he⟩)

omit [DecidableEq V] in
private theorem symmCount (s : Finset V) (f g : V → A) :
    mismatch s f g = mismatch s g f := by
  unfold mismatch
  congr 1
  ext x
  simp only [Finset.mem_filter, ne_comm]

/-- Adjacent well-connected columns with dominant classes have the same dominant label. -/
private theorem sameLabel (s : Finset V) (f g : V → A) (a b : A) (D : Nat)
    (hf : mismatch s f (fun _ => a) < D) (hg : mismatch s g (fun _ => b) < D)
    (hfg : mismatch s f g + 2 * D ≤ s.card) : a = b := by
  by_contra hab
  have hconst : mismatch s (fun _ => a) (fun _ => b) = s.card := by
    simp [mismatch, hab]
  have h₁ := triangle s (fun _ => a) f (fun _ => b)
  have h₂ := triangle s f g (fun _ => b)
  rw [hconst, symmCount s (fun _ => a) f] at h₁
  omega

/-- If the endpoints of a chain disagree on at least 2D rows, and adjacent
columns agree on at least 2D rows, some column omits at least D rows from
every one of its label classes. All comparisons use the same finite row set. -/
theorem forcedColumn (s : Finset V) (f : Nat → V → A) (L D : Nat)
    (hadj : ∀ i < L, mismatch s (f i) (f (i+1)) + 2 * D ≤ s.card)
    (hend : 2 * D ≤ mismatch s (f 0) (f L)) :
    ∃ i ≤ L, ∀ a : A, D ≤ mismatch s (f i) (fun _ => a) := by
  classical
  by_contra hf
  push Not at hf
  obtain ⟨a, ha⟩ := hf 0 (Nat.zero_le _)
  have main : ∀ i ≤ L, mismatch s (f i) (fun _ => a) < D := by
    intro i
    induction i with
    | zero => exact fun _ => ha
    | succ i ih =>
      intro hil
      obtain ⟨b, hb⟩ := hf (i+1) hil
      have ab := sameLabel s (f i) (f (i+1)) a b D (ih (by omega)) hb (hadj i (by omega))
      simpa [ab] using hb
  have h := triangle s (f 0) (fun _ => a) (f L)
  rw [symmCount s (fun _ => a) (f L)] at h
  have hL := main L le_rfl
  omega

#print axioms forcedColumn

end Collatz.TritChain

import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-! Products of translated open endpoints. Roots are stored with minus
sign so that a state n contributes the factor X+n. -/
namespace Collatz.ShiftBalance
open Polynomial

noncomputable def rootPoly (v : Multiset ℤ) : ℤ[X] :=
  (v.map fun z => X-C z).prod

/-- Equal-size endpoint multisets of size r are recovered by r distinct
translated product evaluations. The degree drops because both polynomials
are monic. -/
theorem recover_endpoints (a b : Multiset ℤ) (hc : a.card = b.card)
    (s : Finset ℤ) (hs : a.card ≤ s.card)
    (he : ∀ t ∈ s, (rootPoly a).eval t = (rootPoly b).eval t) : a=b := by
  classical
  have hp : (rootPoly a).Monic := monic_multisetProd_X_sub_C _
  have hq : (rootPoly b).Monic := monic_multisetProd_X_sub_C _
  have ha : (rootPoly a).natDegree = a.card := natDegree_multiset_prod_X_sub_C_eq_card _
  have hb : (rootPoly b).natDegree = b.card := natDegree_multiset_prod_X_sub_C_eq_card _
  have eqp : rootPoly a = rootPoly b := by
    by_contra hne
    have hn : rootPoly a-rootPoly b ≠ 0 := sub_ne_zero.mpr hne
    have hd : (rootPoly a).degree = (rootPoly b).degree := by
      rw [degree_eq_natDegree hp.ne_zero,degree_eq_natDegree hq.ne_zero,ha,hb,hc]
    have hd' := degree_sub_lt_left hd hp.ne_zero (hp.trans hq.symm)
    rw [degree_eq_natDegree hn,degree_eq_natDegree hp.ne_zero] at hd'
    have hd'' : (rootPoly a-rootPoly b).natDegree < a.card := by exact_mod_cast ha ▸ hd'
    apply hn
    apply eq_zero_of_natDegree_lt_card_of_eval_eq_zero' _ s _ (hd''.trans_le hs)
    intro t ht
    simp [he t ht]
  have := congrArg Polynomial.roots eqp
  exact (roots_multiset_prod_X_sub_C a).symm.trans (this.trans (roots_multiset_prod_X_sub_C b))

/-- Actual accelerated odd step recorded by its complete power of two. -/
def OddEdge (x y : ℕ) : Prop :=
  x%2=1 ∧ y%2=1 ∧ ∃ k : ℕ, 0<k ∧ 2^k*y=3*x+1

/-- Validates a literal finite odd path with the exponents supplied. -/
def checkPath (x : ℕ) : List (ℕ × ℕ) → Bool
  | [] => true
  | (k,y)::rest => decide (x%2=1 ∧ y%2=1 ∧ 0<k ∧ 2^k*y=3*x+1 ∧ 7≤x ∧ 7≤y)
      && checkPath y rest

def lastState (x : ℕ) : List (ℕ × ℕ) → ℕ
  | [] => x
  | (_,y)::rest => lastState y rest

theorem decreases (W : ℕ → ℝ) (hW : ∀ x y, 7≤x → 7≤y → OddEdge x y → W y < W x)
    (x : ℕ) (p : List (ℕ × ℕ)) (hn : p≠[]) (hc : checkPath x p = true) :
    W (lastState x p) < W x := by
  induction p generalizing x with
  | nil => contradiction
  | cons z rest ih =>
    obtain ⟨k,y⟩ := z
    simp only [checkPath,Bool.and_eq_true,decide_eq_true_eq] at hc
    obtain ⟨⟨h1,h2,hk,he,hx,hy⟩,ht⟩ := hc
    have hd := hW x y hx hy ⟨h1,h2,k,hk,he⟩
    change W (lastState y rest) < W x
    by_cases h : rest=[]
    · simpa [h,lastState] using hd
    · exact (ih y h ht).trans hd

def pathA : List (ℕ × ℕ) := [(1,11)]
def pathB : List (ℕ × ℕ) := [(2,49),(2,37),(4,7),(1,11),(1,17),(2,13)]
def pathC : List (ℕ × ℕ) := [(1,83),(1,125),(3,47),(1,71),(1,107),(1,161),
    (2,121),(2,91),(1,137),(2,103),(1,155),(1,233),(2,175)]

/-- A strictly descending potential cannot be obtained even when two
independent, unrestricted completely additive functions are evaluated at
the current integer and its successor integer n+1. -/
theorem no_two_shift_strict (F G : ℕ → ℝ)
    (hf : ∀ a b : ℕ, F (a*b) = F a+F b)
    (hg : ∀ a b : ℕ, G (a*b) = G a+G b) :
    ¬∀ x y, 7≤x → 7≤y → OddEdge x y → F y+G (y+1) < F x+G (x+1) := by
  intro h
  let w := fun x : ℕ => F x+G (x+1)
  have hA : w 11 < w 7 := decreases w h 7 pathA (by decide) (by decide)
  have hB : w 13 < w 65 := decreases w h 65 pathB (by decide) (by decide)
  have hC : w 175 < w 55 := decreases w h 55 pathC (by decide) (by decide)
  have h0 : F 7+F 65+F 55 = F 11+F 13+F 175 := by
    rw [←hf,←hf,←hf,←hf]
  have h1 : G (7+1)+G (65+1)+G (55+1) = G (11+1)+G (13+1)+G (175+1) := by
    rw [←hg,←hg,←hg,←hg]
  dsimp only [w] at hA hB hC
  linarith

#print axioms recover_endpoints
#print axioms no_two_shift_strict
end Collatz.ShiftBalance

import Mathlib.Data.Int.Basic
import Mathlib.Tactic.NormNum

/-!
Finite integer interfaces of the written strict-rank-convexity argument.
These lemmas verify the ordinary unit-drift seams and the parity rigidity
of arithmetic triples and quadruples. They do not formalize the global
rank construction, the logarithmic-form input, or its asymptotic cutoff.
-/

namespace RankConvexityInterfaces

def lowbit (x : Nat) : Int := if x % 2 = 0 then 2 else 1

theorem regular_signs (q h h' drift : Int)
    (hq : q = 2 ∨ q = 4) (hd : -2 ≤ drift ∧ drift ≤ 2)
    (step : q * h' = 3 * h + drift) :
    (0 < h → 0 < h') ∧ (h < 0 → h' < 0) := by
  rcases hq with rfl | rfl <;> constructor <;> intro hh <;> omega

theorem lower_seam_negative_exit (h h' drift : Int)
    (hd : 1 ≤ drift ∧ drift ≤ 4) (step : 4 * h' = 3 * h + drift)
    (hn : h < 0) (hout : 0 ≤ h') :
    h = -1 ∧ drift = 3 ∧ h' = 0 := by omega

theorem lower_seam_positive_persists (h h' drift : Int)
    (hd : 1 ≤ drift ∧ drift ≤ 4) (step : 4 * h' = 3 * h + drift)
    (hp : 0 < h) : 0 < h' := by omega

theorem upper_seam_positive_exit (h h' drift : Int)
    (hd : -5 ≤ drift ∧ drift ≤ -2) (step : 4 * h' = 3 * h + drift)
    (hp : 0 < h) (hout : h' ≤ 0) :
    h = 1 ∧ drift = -3 ∧ h' = 0 := by
  have hh : h = 1 := by omega
  have hn : h' = 0 := by omega
  exact ⟨hh, by omega, hn⟩

theorem upper_seam_negative_persists (h h' drift : Int)
    (hd : -5 ≤ drift ∧ drift ≤ -2) (step : 4 * h' = 3 * h + drift)
    (hn : h < 0) : h' < 0 := by omega

theorem quadruple_spacing_even (a g : Nat)
    (h0 : a % 4 ≠ 0) (h1 : (a + g) % 4 ≠ 0)
    (h2 : (a + 2 * g) % 4 ≠ 0) (h3 : (a + 3 * g) % 4 ≠ 0) :
    g % 2 = 0 := by
  by_contra hg
  have hga : g % 4 = 1 ∨ g % 4 = 3 := by omega
  have haa : a % 4 = 1 ∨ a % 4 = 2 ∨ a % 4 = 3 := by omega
  rcases hga with hga | hga <;> rcases haa with haa | haa | haa <;> omega

theorem even_spacing_lowbits (a g : Nat) (hg : g % 2 = 0) :
    lowbit (a + g) = lowbit a ∧
    lowbit (a + 2 * g) = lowbit a ∧
    lowbit (a + 3 * g) = lowbit a := by
  have h1 : (a + g) % 2 = a % 2 := by omega
  have h2 : (a + 2 * g) % 2 = a % 2 := by omega
  have h3 : (a + 3 * g) % 2 = a % 2 := by omega
  simp only [lowbit, h1, h2, h3, and_self]

theorem quadruple_lowbit_rigidity (a g : Nat)
    (h0 : a % 4 ≠ 0) (h1 : (a + g) % 4 ≠ 0)
    (h2 : (a + 2 * g) % 4 ≠ 0) (h3 : (a + 3 * g) % 4 ≠ 0) :
    g % 2 = 0 ∧ lowbit (a + g) = lowbit a ∧
    lowbit (a + 2 * g) = lowbit a ∧ lowbit (a + 3 * g) = lowbit a := by
  have hg := quadruple_spacing_even a g h0 h1 h2 h3
  exact ⟨hg, even_spacing_lowbits a g hg⟩

theorem odd_triple_lowbits (a g : Nat)
    (h0 : a % 4 ≠ 0) (h1 : (a + g) % 4 ≠ 0)
    (h2 : (a + 2 * g) % 4 ≠ 0) (hg : g % 2 = 1) :
    lowbit a = 1 ∧ lowbit (a + g) = 2 ∧ lowbit (a + 2 * g) = 1 := by
  have ha : a % 2 ≠ 0 := by omega
  have hb : (a + g) % 2 = 0 := by omega
  have hc : (a + 2 * g) % 2 ≠ 0 := by omega
  simp only [lowbit, ha, hb, hc, ite_false, ite_true, and_self]

theorem nonnegative_triple_spacing_even (a g : Nat) (q next : Int)
    (h0 : a % 4 ≠ 0) (h1 : (a + g) % 4 ≠ 0)
    (h2 : (a + 2 * g) % 4 ≠ 0) (hq : q = 2 ∨ q = 4)
    (hn : 0 ≤ next)
    (step : q * next = lowbit (a + 2 * g) - 2 * lowbit (a + g) + lowbit a) :
    g % 2 = 0 := by
  by_contra he
  have hg : g % 2 = 1 := by omega
  obtain ⟨ha, hb, hc⟩ := odd_triple_lowbits a g h0 h1 h2 hg
  rw [ha, hb, hc] at step
  rcases hq with rfl | rfl <;> omega

theorem same_lowbit_progression_step (a b c u v w q ell : Int)
    (hap : c - b = b - a)
    (ha : q * u = 3 * a + ell)
    (hb : q * v = 3 * b + ell)
    (hc : q * w = 3 * c + ell)
    (hq : q = 2 ∨ q = 4) :
    w - v = v - u ∧ q * (v - u) = 3 * (b - a) := by
  rcases hq with rfl | rfl <;> constructor <;> omega

end RankConvexityInterfaces

#print axioms RankConvexityInterfaces.regular_signs
#print axioms RankConvexityInterfaces.lower_seam_negative_exit
#print axioms RankConvexityInterfaces.lower_seam_positive_persists
#print axioms RankConvexityInterfaces.upper_seam_positive_exit
#print axioms RankConvexityInterfaces.upper_seam_negative_persists
#print axioms RankConvexityInterfaces.quadruple_spacing_even
#print axioms RankConvexityInterfaces.even_spacing_lowbits
#print axioms RankConvexityInterfaces.quadruple_lowbit_rigidity
#print axioms RankConvexityInterfaces.odd_triple_lowbits
#print axioms RankConvexityInterfaces.nonnegative_triple_spacing_even
#print axioms RankConvexityInterfaces.same_lowbit_progression_step

import Mathlib.Data.Int.Basic
import Mathlib.Order.Monotone.Basic
import Mathlib.Tactic.NormNum

/-! A synchronized native template cannot support a longer integer cycle.
At each template position all phases use the same even step, the same odd
step, or either of the equal-grade words 10 and 01. Integer spacing makes
each of these alternatives strictly order-preserving across the phases.
This is a restricted cycle-exclusion theorem, not a universal cycle proof. -/
namespace AlignedCycles

inductive Tile where
  | even
  | odd
  | switch

def Relation : Tile → ℤ → ℤ → Prop
  | .even, x, y => 2*y=x
  | .odd, x, y => 2*y=3*x+1
  | .switch, x, y => ∃ a : ℤ, (a=1 ∨ a=2) ∧ 4*y=3*x+a

theorem tile_strict {t : Tile} {a b c d : ℤ}
    (ha : Relation t a c) (hb : Relation t b d) (h : a<b) : c<d := by
  cases t with
  | even => simp only [Relation] at ha hb; omega
  | odd => simp only [Relation] at ha hb; omega
  | switch =>
      obtain ⟨u, hu, heu⟩ := ha
      obtain ⟨v, hv, hev⟩ := hb
      rcases hu with hu | hu <;> rcases hv with hv | hv <;> omega

inductive Trace : List Tile → ℤ → ℤ → Prop where
  | nil (x : ℤ) : Trace [] x x
  | cons {t : Tile} {ts : List Tile} {x y z : ℤ}
      (edge : Relation t x y) (tail : Trace ts y z) : Trace (t::ts) x z

theorem trace_strict {ts : List Tile} {a c : ℤ} (ha : Trace ts a c)
    {b d : ℤ} (hb : Trace ts b d) (h : a<b) : c<d := by
  induction ha generalizing b d with
  | nil => cases hb; exact h
  | cons edge tail ih =>
      cases hb with
      | cons edge' tail' => exact ih tail' (tile_strict edge edge' h)

theorem first_equal_of_order_preserving_cycle (x : ℕ → ℤ) (p : ℕ)
    (hp : 0<p) (hperiod : x p=x 0)
    (horder : ∀ i j, x i<x j → x (i+1)<x (j+1)) : x 1=x 0 := by
  by_contra hne
  rcases lt_or_gt_of_ne hne with hdown | hup
  · have hsteps : ∀ i, x (i+1)<x i := by
      intro i
      induction i with
      | zero => exact hdown
      | succ i ih => exact horder (i+1) i ih
    have hh := (strictAnti_nat_of_succ_lt hsteps) hp
    rw [hperiod] at hh
    exact (lt_irrefl _ hh)
  · have hsteps : ∀ i, x i<x (i+1) := by
      intro i
      induction i with
      | zero => exact hup
      | succ i ih => exact horder i (i+1) ih
    have hh := (strictMono_nat_of_lt_succ hsteps) hp
    rw [hperiod] at hh
    exact (lt_irrefl _ hh)

theorem template_cycle_constant (ts : List Tile) (x : ℕ → ℤ) (p : ℕ)
    (hp : 0<p) (hperiod : ∀ i, x (i+p)=x i)
    (htrace : ∀ i, Trace ts (x i) (x (i+1))) : ∀ i, x i=x 0 := by
  have hnext : ∀ i, x (i+1)=x i := by
    intro i
    apply first_equal_of_order_preserving_cycle (fun j => x (i+j)) p hp
    · simpa using hperiod i
    · intro j k hjk
      simpa only [Nat.add_assoc] using
        trace_strict (htrace (i+j)) (htrace (i+k)) hjk
  intro i
  induction i with
  | zero => rfl
  | succ i ih => exact (hnext i).trans ih

#print axioms tile_strict
#print axioms trace_strict
#print axioms first_equal_of_order_preserving_cycle
#print axioms template_cycle_constant

end AlignedCycles

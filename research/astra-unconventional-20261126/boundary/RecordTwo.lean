import Mathlib.Tactic.Ring
import Mathlib.Data.Int.Basic

/-! Ordinary algebra for the restriction to first ladder blocks (1) and (2,1).
    All clocks in the endpoint equations are explicit. -/

namespace Collatz.RecordTwo

def oddState (t : ℤ) : ℤ := 6*t-1

def A (t y : ℤ) : Prop := ∃ u : ℤ, t=2*u ∧ y=3*u
def B (t y : ℤ) : Prop := ∃ u : ℤ, t=8*u+7 ∧ y=9*u+8

theorem one_exact (t y : ℤ) :
    2*oddState y=3*oddState t+1 ↔ A t y := by
  unfold oddState A
  constructor
  · intro h
    exact ⟨t / 2, by omega, by omega⟩
  · rintro ⟨u, rfl, rfl⟩
    ring

theorem two_one_exact (t y : ℤ) :
    (∃ h : ℤ, 4*h=3*oddState t+1 ∧ h%2=1 ∧ 2*oddState y=3*h+1) ↔ B t y := by
  unfold oddState B
  constructor
  · rintro ⟨h, h₁, _, h₂⟩
    exact ⟨t / 8, by omega, by omega⟩
  · rintro ⟨u, rfl, rfl⟩
    exact ⟨36*u+31, by ring, by omega, by ring⟩

theorem directed_disjoint {t y z : ℤ} (ha : A t y) (hb : B t z) : False := by
  rcases ha with ⟨u, hu, _⟩
  rcases hb with ⟨v, hv, _⟩
  omega

theorem inverse_disjoint {t y z : ℤ} (ha : A t z) (hb : B y z) : False := by
  rcases ha with ⟨u, _, hu⟩
  rcases hb with ⟨v, _, hv⟩
  omega

theorem expansion {t y : ℤ} (ht : 0<t) (h : A t y ∨ B t y) : t<y := by
  rcases h with ⟨u, rfl, rfl⟩ | ⟨u, rfl, rfl⟩ <;> omega

inductive Iter (R : ℤ → ℤ → Prop) : ℕ → ℤ → ℤ → Prop
  | nil (t : ℤ) : Iter R 0 t t
  | cons {k : ℕ} {x y z : ℤ} : R x y → Iter R k y z → Iter R (k+1) x z

theorem iter_a {k : ℕ} {x z : ℤ} (h : Iter A k x z) :
    (2:ℤ)^k*z=3^k*x := by
  induction h with
  | nil => simp
  | @cons k x y z edge _ ih =>
    rcases edge with ⟨u, rfl, rfl⟩
    calc
      (2:ℤ)^(k+1)*z = 2*(2^k*z) := by ring
      _ = 3^(k+1)*(2*u) := by rw [ih]; ring

theorem iter_b {k : ℕ} {x z : ℤ} (h : Iter B k x z) :
    (8:ℤ)^k*(z+1)=9^k*(x+1) := by
  induction h with
  | nil => simp
  | @cons k x y z edge _ ih =>
    rcases edge with ⟨u, rfl, rfl⟩
    calc
      (8:ℤ)^(k+1)*(z+1) = 8*(8^k*(z+1)) := by ring
      _ = 9^(k+1)*((8*u+7)+1) := by rw [ih]; ring

#print axioms one_exact
#print axioms two_one_exact
#print axioms directed_disjoint
#print axioms inverse_disjoint
#print axioms expansion
#print axioms iter_a
#print axioms iter_b

end Collatz.RecordTwo

module

public import TowerFrontierAffine
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.HourTower

set_option autoImplicit false
set_option exponentiation.threshold 4096
set_option maxRecDepth 8192

/-- On this progression of actual supplied bases, the corresponding strictly
    smaller base has the displayed fixed physical merger. -/
@[expose] def Capture (r d g s h t₀ : Nat) : Prop :=
  ∀ u : Nat, let t := t₀+2^h*u
    0<t → 1+2^d*t < 1+3^g*t ∧
      run h (3^r*(1+3^g*t)) = run (h+d) (3^s*(1+2^d*t))

private def check (r d g s h t₀ : Nat) : Bool :=
  2^d<3^g &&
    TowerFrontier.stride h (3^r*(1+3^g*t₀)) (r+g) ==
    TowerFrontier.stride (h+d) (3^s*(1+2^d*t₀)) s

private theorem certified {r d g s h t₀ : Nat} (c : check r d g s h t₀=true) :
    Capture r d g s h t₀ := by
  have ok : 2^d<3^g ∧ TowerFrontier.track h (3^r*(1+3^g*t₀)) (r+g) =
      TowerFrontier.track (h+d) (3^s*(1+2^d*t₀)) s := by
    simpa [check,TowerFrontier.stride_eq] using c
  intro u t tp
  refine ⟨Nat.add_lt_add_left (Nat.mul_lt_mul_of_pos_right ok.1 tp) _,?_⟩
  have left : 3^r*(1+3^g*t)=3^r*(1+3^g*t₀)+2^h*3^(r+g)*u := by
    dsimp [t]; simp only [Nat.pow_add,Nat.mul_add,Nat.mul_one]; ac_rfl
  have right : 3^s*(1+2^d*t)=3^s*(1+2^d*t₀)+2^(h+d)*3^s*u := by
    dsimp [t]; simp only [Nat.pow_add,Nat.mul_add,Nat.mul_one]; ac_rfl
  change run h (3^r*(1+3^g*t)) = run (h+d) (3^s*(1+2^d*t))
  rw [left,right,TowerFrontier.affine,TowerFrontier.affine,ok.2]

/-- Origin-aligned lower-base captures at five prescribed positive ranks. -/
theorem supplied_captures :
    Capture 1 6 4 6 4 4 ∧ Capture 2 19 12 9 1 0 ∧
    Capture 3 103 65 21 2 0 ∧ Capture 4 1138 718 174 1 0 ∧
    Capture 5 1054 665 138 1 0 := by
  exact ⟨certified (by decide +kernel),certified (by decide +kernel),
    certified (by decide +kernel),certified (by decide +kernel),certified (by decide +kernel)⟩

#print axioms supplied_captures

end Collatz.Itinerary.HourTower

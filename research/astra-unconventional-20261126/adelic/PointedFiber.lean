import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity

/-! Every positive odd ternary-unit target has two genuine odd sources at exactly two
odd steps and every shortcut total at least 19, one in each unit class. This is the
branching kernel in the elementary exponential lower bound of POINTED_SPECTRUM.md. -/

namespace CollatzRound14.Adelic

/-- Two reverse edges of the ordinary positive odd map at a supplied total. -/
structure TwoEdge (y x : ℤ) (H : ℕ) : Prop where
  terminalOdd : Odd y
  witness : ∃ a b : ℕ, ∃ w : ℤ,
      0 < a ∧ 0 < b ∧ a + b = H ∧ 0 < w ∧ Odd w ∧ 0 < x ∧ Odd x ∧
      2^a * y = 3*w+1 ∧ 2^b * w = 3*x+1

private theorem twoCancel (n : ℕ) (a : ℤ) : (3:ℤ) ∣ 2^n*a → (3:ℤ) ∣ a := by
  induction n with
  | zero => simp
  | succ n ih =>
    rintro ⟨u, hu⟩
    apply ih
    refine ⟨2^n*a-u, ?_⟩
    rw [pow_succ] at hu
    linear_combination -hu

set_option maxRecDepth 2000 in
private theorem residueTable : ∀ r : Fin 27, r.val % 3 ≠ 0 →
    ∀ c : Fin 3, c.val ≠ 0 → ∃ b : Fin 18,
        (2^(b.val+1)+3+9*c.val) % 27 = r.val := by decide

private theorem positiveOddPreimage {e : ℕ} (ep : 0<e) {y x : ℤ} (yp : 0<y)
    (eq : 2^e*y=3*x+1) : 0<x ∧ Odd x := by
  obtain ⟨k, hk⟩ : ∃ k, e=k+1 := ⟨e-1, by omega⟩
  rw [hk, pow_succ] at eq
  have positive : 0 < (2:ℤ)^k*y := mul_pos (by positivity) yp
  have scaled : 2*(2^k*y) = 3*x+1 := by linear_combination eq
  exact ⟨by omega, x/2, by omega⟩

/-- Choose the actual positive odd source in either specified unit class at the
same odd depth two and the same arbitrarily supplied total H. -/
theorem twoEdgeInChart {y H c : ℕ} (yp : 0<y) (yo : Odd (y:ℤ)) (yu : y%3≠0) (hH : 19≤H)
    (hc : c=1 ∨ c=2) :
    ∃ x : ℤ, TwoEdge y x H ∧ x % 3 = (c:ℤ) := by
  have unit : (2^H*y)%3≠0 := by
    intro bad
    have d : (3:ℕ)∣2^H*y := Nat.dvd_of_mod_eq_zero bad
    have di : (3:ℤ)∣2^H*(y:ℤ) := by exact_mod_cast d
    have dy := twoCancel H y di
    have dyn : (3:ℕ)∣y := by exact_mod_cast dy
    exact yu (Nat.mod_eq_zero_of_dvd dyn)
  let r : Fin 27 := ⟨(2^H*y)%27, Nat.mod_lt _ (by decide)⟩
  have rgood : r.val % 3 ≠ 0 := by
    dsimp [r]
    rwa [Nat.mod_mod_of_dvd _ (by decide : 3∣27)]
  obtain ⟨b₀, hb₀⟩ := residueTable r rgood ⟨c, by omega⟩ (by simp; omega)
  let b := b₀.val+1
  let a := H-b
  have bp : 0<b := by dsimp [b]; omega
  have ap : 0<a := by dsimp [a,b]; have := b₀.isLt; omega
  have hab : a+b=H := by dsimp [a,b]; have := b₀.isLt; omega
  have cong : 2^b+3+9*c ≡ 2^H*y [MOD 27] := hb₀
  obtain ⟨v, hv⟩ := cong.dvd
  let x : ℤ := 3*v+c
  have whole : (2:ℤ)^H*y = 9*x+3+2^b := by
    dsimp [x]
    push_cast at hv
    linear_combination hv
  have combined : (2:ℤ)^b*(2^a*y-1) = 3*(3*x+1) := by
    rw [←hab, pow_add] at whole
    linear_combination whole
  obtain ⟨w, hw⟩ := twoCancel b _ ⟨3*x+1, combined⟩
  have edge1 : (2:ℤ)^a*y=3*w+1 := by omega
  have edge2 : (2:ℤ)^b*w=3*x+1 := by
    rw [hw] at combined
    have h3 : 3*((2:ℤ)^b*w)=3*(3*x+1) := by
      calc
        3*((2:ℤ)^b*w) = 2^b*(3*w) := by ac_rfl
        _ = _ := combined
    omega
  obtain ⟨wp, wo⟩ := positiveOddPreimage ap (by exact_mod_cast yp) edge1
  obtain ⟨xp, xo⟩ := positiveOddPreimage bp wp edge2
  refine ⟨x, ⟨yo,a,b,w,ap,bp,hab,wp,wo,xp,xo,edge1,edge2⟩, ?_⟩
  rcases hc with rfl|rfl <;> dsimp [x] <;> omega

/-- The two physical sources are distinct at every supplied common clock. -/
theorem twoUnitChildren {y H : ℕ} (yp : 0<y) (yo : Odd (y:ℤ)) (yu : y%3≠0) (hH : 19≤H) :
    ∃ x₁ x₂ : ℤ, TwoEdge y x₁ H ∧ TwoEdge y x₂ H ∧
      x₁%3=1 ∧ x₂%3=2 ∧ x₁≠x₂ := by
  obtain ⟨x₁,h₁,r₁⟩ := twoEdgeInChart yp yo yu hH (c:=1) (Or.inl rfl)
  obtain ⟨x₂,h₂,r₂⟩ := twoEdgeInChart yp yo yu hH (c:=2) (Or.inr rfl)
  exact ⟨x₁,x₂,h₁,h₂,r₁,r₂,by omega⟩

#print axioms twoEdgeInChart
#print axioms twoUnitChildren
end CollatzRound14.Adelic

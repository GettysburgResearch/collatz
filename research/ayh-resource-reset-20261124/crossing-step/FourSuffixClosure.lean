import HeadRayRouting
import SingleReturn

/-! The global consumer of the four multiplier comparisons, using the exact
PR193 finite certificate. The existence of the required concordant head edges
in an actual arc is the written routing hypothesis. -/
namespace FourSuffixClosure

open SingleReturn

/-- For the PR193 residual, three ordinary steps on the tripled source
give the antecedent of its directed return. -/
theorem tripled_return (u : ℕ) :
    T (T (T (3*(8*u+7)))) = 9*u+8 := by
  have h₁ : T (3*(8*u+7)) = 36*u+32 := by unfold T; split <;> omega
  have h₂ : T (36*u+32) = 18*u+16 := by unfold T; split <;> omega
  have h₃ : T (18*u+16) = 9*u+8 := by unfold T; split <;> omega
  rw [h₁,h₂,h₃]

/-- Every positive input carries the label of one if the actual invariant
label passes the four multiplier comparisons extracted by the routing. -/
theorem constant_label {α : Type*} (f : ℕ → α)
    (inv : ∀ n, f (T n) = f n)
    (h81 : ∀ n, 0<n → f (81*n) = f n)
    (hunit : ∀ u : ℕ, u%3 ≠ 0 → ∀ j<4, f (3^j*u)=f u) :
    ∀ n, 0<n → f n=f 1 := by
  have hfull : ∀ n, f (81*n) = f n := by
    intro n
    cases n with
    | zero => rfl
    | succ n => exact h81 _ (Nat.zero_lt_succ n)
  apply singleReturnCover (fun n => f n=f 1) rfl
  · intro n
    rw [inv n]
  · intro u h
    have htrip := HeadRayRouting.tripling_from_four f hfull hunit
      (8*u+7) (by omega)
    calc
      f (8*u+7) = f (3*(8*u+7)) := htrip.symm
      _ = f (T (3*(8*u+7))) := (inv _).symm
      _ = f (T (T (3*(8*u+7)))) := (inv _).symm
      _ = f (T (T (T (3*(8*u+7))))) := (inv _).symm
      _ = f (9*u+8) := by rw [tripled_return]
      _ = f 1 := h

private theorem basin_step (n : ℕ) : reachesOne (T n) ↔ reachesOne n := by
  constructor
  · rintro ⟨k,hk⟩
    exact ⟨k+1,hk⟩
  · rintro ⟨k,hk⟩
    cases k with
    | zero =>
        have hn : n=1 := hk
        subst n
        exact ⟨1,by decide⟩
    | succ k => exact ⟨k,hk⟩

/-- A statement for the positive ordinary basin itself. Each hypothesis
concerns one of the concrete multiplier tests, independently of convergence. -/
theorem basin_iff_four :
    (∀ n, 0<n → reachesOne n) ↔
    (∀ n, 0<n → (reachesOne (81*n) ↔ reachesOne n)) ∧
    (∀ u : ℕ, u%3 ≠ 0 → ∀ j<4, (reachesOne (3^j*u) ↔ reachesOne u)) := by
  constructor
  · intro all
    constructor
    · intro n hn
      exact ⟨fun _ => all n hn, fun _ => all (81*n) (by omega)⟩
    · intro u hu j _
      have hp : 0<u := by omega
      exact ⟨fun _ => all u hp, fun _ => all (3^j*u) (by positivity)⟩
  · rintro ⟨h81,hunit⟩ n hn
    have h := constant_label reachesOne (fun v => propext (basin_step v))
      (fun v hv => propext (h81 v hv))
      (fun v hv j hj => propext (hunit v hv j hj)) n hn
    exact h.mpr ⟨0,rfl⟩

#print axioms tripled_return
#print axioms constant_label
#print axioms basin_iff_four

end FourSuffixClosure

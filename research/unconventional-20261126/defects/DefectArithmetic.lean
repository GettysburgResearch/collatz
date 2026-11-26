module

public import Mathlib.Data.Nat.Prime.Basic
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Ring

@[expose] public section
namespace CenteredDefect

/-- This identity uses the actual transition and the reference transition at the
same phase, even when their dyadic exponents differ. -/
theorem centeredStep (q q' c c' : ℚ) (a m : ℕ)
    (actual : 2^a*q'=3*q+1) (reference : 2^m*c'=3*c+1) :
    2^a*(q'-c')-3*(q-c)=(2^m-2^a)*c' := by
  nlinarith only [actual, reference]

/-- The earliest mismatch beats all later nominal and actual correction exponents,
including when its own actual exponent is smaller than the reference exponent. -/
theorem firstMismatchMarker (A a m B b n : ℕ) (diff : a≠m)
    (later : A+a≤B) (hb : 0<b) (hn : 0<n) :
    A+min a m<A+max a m ∧ A+min a m<B+min b n := by
  omega

private theorem sumDivisible {l : List ℤ} (d : ℤ)
    (all : ∀ x ∈ l, d∣x) : d∣l.sum := by
  induction l with
  | nil => simp
  | cons x xs ih =>
    rw [List.sum_cons]
    obtain ⟨u,hu⟩ := all x (by simp)
    obtain ⟨v,hv⟩ := ih (by intro y hy; exact all y (by simp [hy]))
    exact ⟨u+v,by rw [hu, hv]; ring⟩

/-- An odd marked coefficient at the unique least dyadic exponent cannot
participate in a vanishing subsum of other corrections. -/
theorem uniqueLeastTerm (v : ℕ) (m : ℤ) (oddm : Odd m) (others : List ℤ)
    (later : ∀ x∈others, (2:ℤ)^(v+1)∣x) :
    (2:ℤ)^v*m+others.sum ≠ 0 := by
  intro hz
  obtain ⟨s,hs⟩ := sumDivisible ((2:ℤ)^(v+1)) later
  rw [hs, pow_succ] at hz
  have eqn : (2:ℤ)^v*m=(2:ℤ)^v*(-2*s) := by nlinarith only [hz]
  have hm := mul_left_cancel₀ (pow_ne_zero v (by decide : (2:ℤ)≠0)) eqn
  obtain ⟨t,ht⟩ := oddm
  omega

/-- With common center denominator cleared, a true matching transition on the
signed integer displacement has this form. -/
inductive MatchedPrefix : ℕ → ℕ → ℤ → ℤ → Prop where
  | nil (x : ℤ) : MatchedPrefix 0 0 x x
  | cons {a n A : ℕ} {x y z : ℤ} (ha : 0<a) (first : 2^a*y=3*x)
      (rest : MatchedPrefix n A y z) : MatchedPrefix (n+1) (a+A) x z

theorem prefixAffine {n A : ℕ} {x z : ℤ} (p : MatchedPrefix n A x z) :
    (2:ℤ)^A*z=(3:ℤ)^n*x ∧ n≤A := by
  induction p with
  | nil x => simp
  | @cons a n A x y z ha first rest ih =>
    constructor
    · calc
        (2:ℤ)^(a+A)*z = 2^a*(2^A*z) := by rw [pow_add]; ring
        _ = 2^a*(3^n*y) := by rw [ih.1]
        _ = 3^(n+1)*x := by
          rw [pow_succ]
          nlinarith only [congrArg (fun u : ℤ => 3^n*u) first]
    · omega

/-- The nonzero displacement at the end caps the number of matched odd steps
before it. A nonzero displacement at the start caps total divisions afterwards. -/
theorem prefixDivisibility {n A : ℕ} {x z : ℤ} (p : MatchedPrefix n A x z) :
    3^n ∣ z.natAbs ∧ 2^A ∣ x.natAbs := by
  have eqn := congrArg Int.natAbs (prefixAffine p).1
  simp [Int.natAbs_mul, Int.natAbs_pow] at eqn
  have h32 := ((by decide : Nat.Coprime 3 2).pow_left n).pow_right A
  have d3 : 3^n ∣ 2^A*z.natAbs := eqn.symm ▸ dvd_mul_right _ _
  have d2 : 2^A ∣ 3^n*x.natAbs := eqn ▸ dvd_mul_right _ _
  exact ⟨h32.dvd_of_dvd_mul_left d3, h32.symm.dvd_of_dvd_mul_left d2⟩

#print axioms sumDivisible
#print axioms prefixAffine
#print axioms centeredStep
#print axioms firstMismatchMarker
#print axioms uniqueLeastTerm
#print axioms prefixDivisibility

end CenteredDefect

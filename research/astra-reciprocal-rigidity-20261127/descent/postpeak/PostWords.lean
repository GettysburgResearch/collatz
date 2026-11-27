import RampShadow
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.GCongr

namespace RampShadow.Postpeak

/-- An exact native word, in its forward order. True denotes an odd input. -/
abbrev Word := List Bool

def weight : Word → ℕ
  | [] => 0
  | false :: w => weight w
  | true :: w => weight w + 1

def intercept : Word → ℤ
  | [] => 0
  | false :: w => 2 * intercept w
  | true :: w => 3 ^ weight w + 2 * intercept w

def offset (w : Word) : ℤ := intercept w - 3 ^ weight w

theorem weight_le (w : Word) : weight w ≤ w.length := by
  induction w with
  | nil => simp [weight]
  | cons b w ih => cases b <;> simp [weight] <;> omega

theorem intercept_bounds (w : Word) :
    0 ≤ intercept w ∧ intercept w ≤ 3^w.length-2^w.length := by
  induction w with
  | nil => norm_num [intercept]
  | cons b w ih =>
    have H : (3:ℤ)^weight w ≤ 3^w.length := pow_le_pow_right₀ (by norm_num) (weight_le w)
    have P : (0:ℤ) ≤ 3^w.length := by positivity
    obtain ⟨A,B⟩ := ih
    have R : (0:ℤ) ≤ 3^weight w := by positivity
    cases b <;> simp only [intercept,List.length_cons,pow_succ] <;> constructor <;> linarith

theorem offset_bounds (w : Word) :
    -(3:ℤ)^w.length ≤ offset w ∧ offset w < 3^w.length := by
  have H : (3:ℤ)^weight w ≤ 3^w.length := pow_le_pow_right₀ (by norm_num) (weight_le w)
  have := intercept_bounds w
  have P : (0:ℤ) < 2^w.length := by positivity
  have P' : (0:ℤ) < 3^weight w := by positivity
  unfold offset
  omega

theorem word_of_walk {e k x y} (W : Walk e k x y) :
    ∃ w : Word, w.length=e ∧ weight w=k ∧ 2^e*y=3^k*x+intercept w := by
  induction W with
  | nil x => exact ⟨[],rfl,rfl,by simp [intercept]⟩
  | @even h p x y W IH =>
    obtain ⟨w,eh,pk,eq⟩ := IH
    refine ⟨false::w,by simp [eh],pk,?_⟩
    simp only [intercept,pow_succ]
    linear_combination 2*eq
  | @odd h p x y z edge W IH =>
    obtain ⟨w,eh,pk,eq⟩ := IH
    refine ⟨true::w,by simp [eh],by simp [weight,pk],?_⟩
    simp only [intercept,pk,pow_succ]
    linear_combination 2*eq - (3:ℤ)^p*edge

private theorem three_odd (p : ℕ) : (3:ℤ)^p%2 = 1 := by
  induction p with
  | zero => decide
  | succ p ih => rw [pow_succ,Int.mul_emod,ih]; decide

/-- An integral endpoint for the specified affine word forces all its
    physical branch parities. This also holds for signed starting states. -/
theorem walk_of_word (w : Word) (x y : ℤ)
    (eq : 2^w.length*y=3^(weight w)*x+intercept w) : Walk w.length (weight w) x y := by
  induction w generalizing x with
  | nil => simp [weight,intercept] at eq; subst x; exact Walk.nil _
  | cons b w IH =>
    cases b with
    | false =>
      simp only [List.length_cons,weight,intercept,pow_succ] at eq ⊢
      have par : (3:ℤ)^weight w*x%2=0 := by
        have fac : 3^weight w*x=2*(2^w.length*y-intercept w) := by linarith only [eq]
        rw [fac]; omega
      rw [Int.mul_emod,three_odd] at par
      have xx : x=2*(x/2) := by omega
      have tail : (2:ℤ)^w.length*y = 3^weight w*(x/2)+intercept w := by
        have q := congrArg (fun a : ℤ => (3:ℤ)^weight w*a) xx
        try dsimp at q
        nlinarith only [q,eq]
      simpa only [←xx] using Walk.even (IH _ tail)
    | true =>
      simp only [List.length_cons,weight,intercept,pow_succ] at eq ⊢
      have par : (3:ℤ)^weight w*(3*x+1)%2=0 := by
        have fac : 3^weight w*(3*x+1)=2*(2^w.length*y-intercept w) := by linarith only [eq]
        rw [fac]; omega
      rw [Int.mul_emod,three_odd] at par
      have edge : 3*x+1=2*((3*x+1)/2) := by omega
      apply Walk.odd edge (IH _ ?_)
      have q := congrArg (fun a : ℤ => (3:ℤ)^weight w*a) edge
      try dsimp at q
      nlinarith only [q,eq]

end RampShadow.Postpeak

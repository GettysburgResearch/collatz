import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Physical inverse words whose affine maps synchronize every integer shift. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.TranslationWords

/-- Physical zero is division by two; physical one is the odd affine branch. -/
def evaluate : List Bool → ℚ → ℚ
  | [], x => x
  | false :: w, x => evaluate w x / 2
  | true :: w, x => (1 + 3 * evaluate w x) / 2

def oddCount : List Bool → ℕ
  | [] => 0
  | false :: w => oddCount w
  | true :: w => oddCount w + 1

private theorem eval_append (u v : List Bool) (x : ℚ) :
    evaluate (u++v) x = evaluate u (evaluate v x) := by
  induction u with
  | nil => rfl
  | cons e u ih => cases e <;> simp only [List.cons_append, evaluate, ih]

private theorem odd_append (u v : List Bool) :
    oddCount (u++v) = oddCount u + oddCount v := by
  induction u with
  | nil => simp [oddCount]
  | cons e u ih =>
    cases e <;> simp only [List.cons_append, oddCount, ih]
    omega

/-- The two maps have equal physical length, the prescribed odd count
difference, and the literal rational affine intertwining identity. -/
def Represents (m : ℕ) (z : ℤ) : Prop :=
  ∃ u v : List Bool, u.length = v.length ∧ oddCount v = oddCount u + m ∧
    ∀ x : ℚ, evaluate u ((3:ℚ)^m*x+z) = evaluate v x

private theorem origin : Represents 0 0 := by
  refine ⟨[],[],rfl,rfl,?_⟩
  intro x
  simp [evaluate]

private theorem append_pair (m M : ℕ) (j z : ℤ) (hj : Represents m j)
    (c d : List Bool) (hlen : c.length = d.length)
    (hcount : m + oddCount d = oddCount c + M)
    (ha : ∀ x : ℚ, evaluate c ((3:ℚ)^M*x+z) = (3:ℚ)^m*evaluate d x+j) :
    Represents M z := by
  obtain ⟨u,v,hl,ho,hw⟩ := hj
  refine ⟨u++c,v++d,by simp only [List.length_append, hl, hlen],?_,?_⟩
  · rw [odd_append, odd_append, ho]
    omega
  · intro x
    rw [eval_append, eval_append, ha, hw]

private theorem double_shift (j z : ℤ) (hz : z=2*j) (hj : Represents 0 j) :
    Represents 0 z := by
  apply append_pair 0 0 j z hj [false] [false] rfl rfl
  intro x
  rw [hz]
  simp only [evaluate, pow_zero, one_mul, Int.cast_mul, Int.cast_ofNat]
  ring

private theorem shift_one : Represents 0 1 := by
  apply append_pair 0 0 0 1 origin [false,false,true] [true,false,false] rfl rfl
  intro x
  norm_num [evaluate]
  ring

private theorem odd_shift (j z : ℤ) (hz : 3*z = 4*j+1 ∨ 3*z = 4*j-1)
    (hj : Represents 0 j) : Represents 0 z := by
  rcases hz with hp|hn
  · apply append_pair 0 0 j z hj [false,true] [true,false] rfl rfl
    intro x
    have he : (3:ℚ)*z = 4*j+1 := by exact_mod_cast hp
    simp only [evaluate, pow_zero, one_mul]
    linarith
  · apply append_pair 0 0 j z hj [true,false] [false,true] rfl rfl
    intro x
    have he : (3:ℚ)*z = 4*j-1 := by exact_mod_cast hn
    simp only [evaluate, pow_zero, one_mul]
    linarith

private theorem natural_shift (n : ℕ) : Represents 0 n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases h0 : n = 0
    · subst n
      exact origin
    by_cases h1 : n = 1
    · subst n
      exact shift_one
    by_cases he : n%2 = 0
    · let k := n/2
      have hk : k<n := by dsimp [k]; omega
      have eq : n=2*k := by dsimp [k]; omega
      exact double_shift k n (by exact_mod_cast eq) (ih k hk)
    · let k := (3*n+1)/4
      have hk : k<n := by dsimp [k]; omega
      have hc : 3*n+1 = 4*k ∨ 3*n = 4*k+1 := by dsimp [k]; omega
      apply odd_shift k n _ (ih k hk)
      rcases hc with hn|hp
      · right
        have tt : (3:ℤ)*n+1 = 4*k := by exact_mod_cast hn
        omega
      · left
        exact_mod_cast hp

/-- Every integer shift has an exact pair of native equal-clock words. -/
theorem integer_shift (z : ℤ) : Represents 0 z := by
  cases z with
  | ofNat n => exact natural_shift n
  | negSucc n =>
    obtain ⟨u,v,hl,ho,hw⟩ := natural_shift (n+1)
    refine ⟨v,u,hl.symm,by omega,?_⟩
    intro x
    specialize hw (x+(Int.negSucc n:ℤ))
    simp only [pow_zero, one_mul] at hw ⊢
    convert hw.symm using 2
    push_cast
    ring

/-- If a literal integer affine shift is already represented, prepend either
physical branch to both sources, maintaining equal physical clock. -/
private theorem even_affine (m : ℕ) (d : ℤ) (hp : Represents m (d/2))
    (hd : d%2=0) : Represents m d := by
  apply append_pair m m (d/2) d hp [false] [false] rfl (by simp [oddCount])
  intro x
  have eq : d = 2*(d/2) := by omega
  have hh : (d:ℚ) = 2*((d/2:ℤ):ℚ) := by exact_mod_cast eq
  simp only [evaluate]
  linarith

private theorem odd_affine (m : ℕ) (j d : ℤ) (hd : d=3^m+2*j)
    (hj : Represents m j) : Represents (m+1) d := by
  apply append_pair m (m+1) j d hj [false] [true] rfl (by simp [oddCount])
  intro x
  have hh : (d:ℚ) = 3^m+2*j := by exact_mod_cast hd
  rw [hh, pow_succ]
  simp only [evaluate]
  ring

private theorem power_three_odd (m : ℕ) : (3:ℤ)^m % 2 = 1 := by
  induction m with
  | zero => decide
  | succ m ih => rw [pow_succ, Int.mul_emod, ih]; decide

private theorem raise_nonzero (m : ℕ) (hm : ∀ j : ℤ, Represents m j)
    (d : ℤ) (hd : d≠0) : Represents (m+1) d := by
  induction d using (measure (fun z : ℤ => z.natAbs)).wf.induction with
  | h d ih =>
    by_cases he : d%2=0
    · apply even_affine (m+1) d _ he
      apply ih (d/2) _ (by omega)
      change (d/2).natAbs < d.natAbs
      omega
    · let j := (d-3^m)/2
      have hpow : (3:ℤ)^m % 2 = 1 := power_three_odd _
      have hj : d=3^m+2*j := by dsimp [j]; omega
      exact odd_affine m j d hj (hm j)

/-- Nonidentity maps with slope a nonnegative power of three have native
equal-clock word witnesses with the exact difference of odd counts. -/
theorem integer_affine (m : ℕ) (d : ℤ) : Represents m d := by
  induction m generalizing d with
  | zero => exact integer_shift d
  | succ m ih =>
    by_cases hd : d=0
    · subst d
      let j : ℤ := (1-3^(m+1))/2
      have hpow : (3:ℤ)^(m+1)%2=1 := power_three_odd _
      have hlarge : (3:ℤ)^(m+1)≥3 := by
        have hpos : (0:ℤ)<3^m := by positivity
        rw [pow_succ]
        omega
      have hj : j≠0 := by dsimp [j]; omega
      have he : (3:ℤ)^(m+1)+2*j=1 := by dsimp [j]; omega
      have hh : (3:ℚ)^(m+1)+2*(j:ℚ)=1 := by exact_mod_cast he
      apply append_pair (m+1) (m+1) j 0 (raise_nonzero m ih j hj)
        [true] [true] rfl (by simp only [oddCount]; omega)
      intro x
      simp only [evaluate, Int.cast_zero, add_zero]
      linarith
    · exact raise_nonzero m ih d hd

end Collatz.TranslationWords

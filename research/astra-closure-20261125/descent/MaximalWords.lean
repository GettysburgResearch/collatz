import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Words are stored in reverse chronological order, so cons appends a step. -/
namespace MaximalWords

abbrev Word := List Bool

def odds : Word → ℕ
  | [] => 0
  | b :: w => if b then odds w + 1 else odds w

def carry : Word → ℕ
  | [] => 0
  | b :: w => if b then 3*carry w+2^w.length else carry w

def floorCarry : ℕ → ℕ
  | 0 => 0
  | p+1 => 3*floorCarry p+2^p

private theorem count_le_length (w : Word) : odds w ≤ w.length := by
  induction w with
  | nil => simp [odds]
  | cons b w ih => cases b <;> simp [odds] <;> omega

private theorem floor_le (w : Word) : floorCarry (odds w) ≤ carry w := by
  induction w with
  | nil => decide
  | cons b w ih =>
    cases b
    · exact ih
    · simp only [odds,carry,ite_true,floorCarry]
      have := Nat.pow_le_pow_right (by decide : 0<2) (count_le_length w)
      omega

private theorem floor_mono {p q : ℕ} (h : p≤q) : floorCarry p≤floorCarry q := by
  induction h with
  | refl => exact Nat.le_refl _
  | @step q h ih =>
    change floorCarry p ≤ 3*floorCarry q+2^q
    exact ih.trans ((Nat.le_mul_of_pos_left _ (by decide : 0<3)).trans (Nat.le_add_right _ _))

private theorem floor_gap (p : ℕ) (hp : 2≤p) : 2*3^p < floorCarry (p+1) := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le hp
  induction k with
  | zero => decide
  | succ k ih =>
    change 2*3^(2+k+1) < 3*floorCarry (2+k+1)+2^(2+k+1)
    rw [Nat.pow_succ 3]
    apply Nat.lt_of_lt_of_le _ (Nat.le_add_right _ _)
    simpa only [Nat.mul_left_comm,Nat.mul_comm,Nat.mul_assoc] using
      Nat.mul_lt_mul_of_pos_left (ih (by omega)) (by decide : 0<3)

/-- Even permitting a competing word of a different length and a smaller
carry, the small normalized carry precludes any greater odd count. -/
theorem maximal_of_bound (w v : Word) (hp : 2≤odds w)
    (hs : carry w ≤ 2*3^(odds w)) (hc : carry v ≤ carry w) : odds v ≤ odds w := by
  by_contra! h
  exact Nat.not_le_of_gt (floor_gap _ hp) <|
    (floor_mono (p:=odds w+1) (q:=odds v) (by omega)).trans ((floor_le v).trans (hc.trans hs))

/-- The chronological seed is 11011111. -/
def seed : Word := [true,true,true,true,true,false,true,true]

def block (b : Bool) (w : Word) : Word := b :: true :: true :: w

def encode : List Bool → Word
  | [] => seed
  | b :: bs => block b (encode bs)

private def Safe (w : Word) : Prop := 2≤odds w ∧ carry w+5*2^w.length ≤ 2*3^(odds w)

private theorem safe_one (w : Word) (hs : Safe w) : Safe (true::w) := by
  obtain ⟨hp,hs⟩ := hs
  unfold Safe
  simp [odds,carry,pow_succ]
  omega

private theorem safe_block (b : Bool) (w : Word) (hs : Safe w) : Safe (block b w) := by
  cases b
  · obtain ⟨hp,hs⟩ := hs
    unfold Safe
    simp [block,odds,carry,pow_succ]
    omega
  · exact safe_one _ (safe_one _ (safe_one _ hs))

private theorem safe_encode (bs : List Bool) : Safe (encode bs) := by
  induction bs with
  | nil => unfold Safe; decide
  | cons b bs ih => exact safe_block b _ ih

/-- A complete block boundary or either incomplete tail. -/
theorem protected_words (bs : List Bool) (v w : Word)
    (hw : w=encode bs ∨ w=true::encode bs ∨ w=true::true::encode bs)
    (comp : carry v≤carry w) : odds v≤odds w := by
  have h := safe_encode bs
  have sw : Safe w := by
    rcases hw with rfl|rfl|rfl
    · exact h
    · exact safe_one _ h
    · exact safe_one _ (safe_one _ h)
  obtain ⟨hp,hs⟩ := sw
  exact maximal_of_bound w v hp (by omega) comp

theorem encode_length (bs : List Bool) : (encode bs).length=8+3*bs.length := by
  induction bs with
  | nil => rfl
  | cons b bs ih => simp [encode,block,ih]; omega

theorem encode_injective (xs ys : List Bool) (h : encode xs=encode ys) : xs=ys := by
  induction xs generalizing ys with
  | nil =>
    have hl := congrArg List.length h
    rw [encode_length, encode_length] at hl
    cases ys <;> simp_all
  | cons x xs ih =>
    cases ys with
    | nil =>
      have hl := congrArg List.length h
      rw [encode_length, encode_length] at hl
      simp at hl
    | cons y ys =>
      change x::true::true::encode xs=y::true::true::encode ys at h
      simp only [List.cons.injEq, true_and] at h
      obtain ⟨rfl,tail⟩ := h
      rw [ih ys tail]

#print axioms maximal_of_bound
#print axioms protected_words
#print axioms encode_length
#print axioms encode_injective
end MaximalWords

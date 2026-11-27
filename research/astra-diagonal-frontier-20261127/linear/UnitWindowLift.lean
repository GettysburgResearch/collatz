import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

namespace CollatzWindowLift

def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3*x+1)/2

def visits : ℕ → ℕ → ℕ
  | 0, x => x
  | n+1, x => visits n (shortcut x)

def count : List Bool → ℕ
  | [] => 0
  | false :: w => count w
  | true :: w => count w + 1

def offset : List Bool → ℕ
  | [] => 0
  | false :: w => 2 * offset w
  | true :: w => 3 ^ count w + 2 * offset w

def physical : List Bool → ℕ → ℕ → Prop
  | [], x, y => x = y
  | false :: w, x, y => x % 2 = 0 ∧ physical w (x/2) y
  | true :: w, x, y => x % 2 = 1 ∧ physical w ((3*x+1)/2) y

theorem visits_of_physical (w : List Bool) {x y : ℕ} (h : physical w x y) :
    visits w.length x = y := by
  induction w generalizing x with
  | nil => exact h
  | cons b w ih =>
    cases b with
    | false =>
      obtain ⟨hp, hw⟩ := h
      simpa [visits, shortcut, hp] using ih hw
    | true =>
      obtain ⟨hp, hw⟩ := h
      simpa [visits, shortcut, hp] using ih hw

private theorem pow_three_mod_two (k : ℕ) : 3^k % 2 = 1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ, Nat.mul_mod, ih]

/-- An exact integer affine row already enforces every prescribed parity bit. -/
theorem physical_of_row (w : List Bool) {x y : ℕ}
    (row : 2^w.length*y = 3^count w*x + offset w) : physical w x y := by
  induction w generalizing x with
  | nil => simpa [physical, count, offset] using row.symm
  | cons b w ih =>
    cases b with
    | false =>
      simp only [List.length_cons, count, offset, pow_succ] at row
      have hr := congrArg (· % 2) row
      have hp : x % 2 = 0 := by
        simpa [Nat.mul_mod, Nat.add_mod, pow_three_mod_two] using hr.symm
      refine ⟨hp, ih ?_⟩
      have hx : 2*(x/2) = x := by omega
      calc
        2^w.length * y = 3^count w*(x/2) + offset w := by
          apply Nat.eq_of_mul_eq_mul_left (by decide : 0 < 2)
          calc
            2*(2^w.length*y) = 2^w.length*2*y := by ring
            _ = 3^count w*x + 2*offset w := row
            _ = 2*(3^count w*(x/2) + offset w) := by
              conv_lhs => rw [← hx]
              ring
    | true =>
      simp only [List.length_cons, count, offset, pow_succ] at row
      have hr := congrArg (· % 2) row
      have hp : x % 2 = 1 := by
        have hp' : 0 = (x%2 + 1) % 2 := by
          simpa [Nat.mul_mod, Nat.add_mod, pow_three_mod_two] using hr
        omega
      refine ⟨hp, ih ?_⟩
      have hx : 2*((3*x+1)/2) = 3*x+1 := by omega
      apply Nat.eq_of_mul_eq_mul_left (by decide : 0 < 2)
      calc
        2*(2^w.length*y) = 2^w.length*2*y := by ring
        _ = 3^count w*3*x + (3^count w + 2*offset w) := row
        _ = 3^count w*(3*x+1) + 2*offset w := by ring
        _ = 2*(3^count w*((3*x+1)/2)+offset w) := by
              conv_lhs => rw [← hx]
              ring

private theorem physical_append (v w : List Bool) {x y z : ℕ}
    (h : physical v x y) (h' : physical w y z) : physical (v ++ w) x z := by
  induction v generalizing x with
  | nil =>
    change x = y at h
    simpa [h] using h'
  | cons b v ih =>
    cases b <;> exact ⟨h.1, ih h.2⟩

private theorem count_append (u v : List Bool) : count (u ++ v) = count u + count v := by
  induction u with
  | nil => simp [count]
  | cons b u ih => cases b <;> simp [count, ih, Nat.add_right_comm]

private theorem offset_append (u v : List Bool) :
    offset (u ++ v) = 3^count v * offset u + 2^u.length * offset v := by
  induction u with
  | nil => simp [offset]
  | cons b u ih =>
    cases b <;> simp [offset, count_append, ih, pow_succ, pow_add] <;> ring

private theorem zeros_info (d : ℕ) :
    count (List.replicate d false) = 0 ∧ offset (List.replicate d false) = 0 := by
  induction d with
  | zero => decide
  | succ d ih => simp [List.replicate_succ, count, offset, ih.1, ih.2]

private theorem ones_info (d : ℕ) :
    count (List.replicate d true) = d ∧ offset (List.replicate d true) + 2^d = 3^d := by
  induction d with
  | zero => decide
  | succ d ih =>
    simp only [List.replicate_succ, count, ih.1, offset, pow_succ]
    refine ⟨True.intro, ?_⟩
    calc
      3^d + 2 * offset (List.replicate d true) + 2^d*2
          = 3^d + 2*(offset (List.replicate d true) + 2^d) := by ring
      _ = 3^d*3 := by rw [ih.2]; ring

/-- A prescribed initial odd run, a gap, the movable odd, and the remaining halvings. -/
def mobile (d gap tail : ℕ) : List Bool :=
  List.replicate d true ++ (List.replicate gap false ++ (true :: List.replicate tail false))

theorem mobile_info (d gap tail : ℕ) :
    (mobile d gap tail).length = d+gap+1+tail ∧
    count (mobile d gap tail) = d+1 ∧
    offset (mobile d gap tail) = 3*(3^d-2^d)+2^(d+gap) := by
  have h := ones_info d
  have hd : offset (List.replicate d true) = 3^d-2^d := by omega
  simp [mobile, count_append, offset_append, count, offset, (zeros_info gap).1,
    (zeros_info gap).2, (zeros_info tail).1, (zeros_info tail).2, h.1,
    hd, pow_add]
  omega

/-- Once the indicated nonnegative integer cofactor has cleared the full
modulus, this lift replays the original native prefix and every added bit. -/
theorem prescribed_lift (w : List Bool) (r t d gap tail cofactor y : ℕ)
    (nativeRow : 2^w.length*t = 3^count w*r+offset w)
    (extraRow : 2^(d+gap+1+tail)*y =
      3^(d+1)*(t+3^count w*cofactor) + 3*(3^d-2^d)+2^(d+gap)) :
    physical (w ++ mobile d gap tail) (r+2^w.length*cofactor) y := by
  apply physical_append w _ (y := t+3^count w*cofactor)
  · apply physical_of_row
    calc
      2^w.length * (t+3^count w*cofactor)
          = 2^w.length*t + 2^w.length*3^count w*cofactor := by ring
      _ = 3^count w*(r+2^w.length*cofactor) + offset w := by rw [nativeRow]; ring
  · apply physical_of_row
    obtain ⟨hlen,hcount,hoff⟩ := mobile_info d gap tail
    rw [hlen,hcount,hoff,extraRow]
    omega

#print axioms physical_of_row
#print axioms mobile_info
#print axioms prescribed_lift
#print axioms visits_of_physical

end CollatzWindowLift

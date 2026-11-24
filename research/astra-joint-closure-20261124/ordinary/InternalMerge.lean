import Std

namespace InternalMerge

def step (x : Nat) := if x % 2 = 0 then x / 2 else (3*x+1)/2

def run : Nat → Nat → Nat
  | 0, x => x
  | h+1, x => run h (step x)

theorem append (a b x : Nat) : run (a+b) x = run b (run a x) := by
  induction a generalizing x with
  | zero => simp [run]
  | succ a ih => rw [Nat.succ_add]; exact ih (step x)

theorem halve (h x : Nat) : run h (2^h*x) = x := by
  induction h with
  | zero => simp [run]
  | succ h ih =>
    rw [Nat.pow_succ, Nat.mul_right_comm, Nat.mul_comm _ 2]
    simp [run, step, ih]

theorem ones (h b : Nat) (hb : 0 < b) :
    run h (2^h*b-1) = 3^h*b-1 := by
  induction h generalizing b with
  | zero => simp [run]
  | succ h ih =>
    rw [Nat.pow_succ, Nat.mul_right_comm, Nat.mul_comm _ 2]
    have hp : 0 < 2^h*b := Nat.mul_pos (Nat.pow_pos (by decide)) hb
    have hs : step (2*(2^h*b)-1) = 2^h*(3*b)-1 := by
      unfold step
      rw [Nat.mul_left_comm (2^h) 3 b]
      split <;> omega
    rw [run, hs, ih _ (by omega), Nat.pow_succ, Nat.mul_assoc]

/-- The two arms consist of the source's initial i odd steps and
    the competitor's k odd steps followed by e halvings. -/
theorem internal_meeting (i k e a b y : Nat) (ha : 0 < a) (hb : 0 < b)
    (hy : 3^i*a = y+1) (he : 3^k*b = 2^e*y+1) :
    run i (2^i*a-1) = y ∧ run (k+e) (2^k*b-1) = y := by
  constructor
  · rw [ones i a ha, hy]; omega
  · rw [append, ones k b hb, he, Nat.add_sub_cancel, halve]

/-- An odd inverse edge of a positive endpoint lifts to the negative
    shadow when the sum has a remaining factor of three. -/
theorem reverse_odd_shadow (y v d t : Nat) (hd : 2 ≤ d)
    (hv : 3*v+1 = 2*y) (ht : y+d = 3*t) :
    ∃ f, 3*f = 2*d+1 ∧ 2 ≤ f ∧ 4*f ≤ 3*d ∧ v+f = 2*t := by
  refine ⟨2*t-v, ?_⟩
  omega

/-- A backwards word on the magnitudes of the negative shadow. -/
inductive Shadow : Nat → Nat → Nat → Prop where
  | first : Shadow 1 0 2
  | even {e h d} : Shadow e h d → Shadow (e+1) h (2*d)
  | odd {e h d f} : Shadow e h d → 3*f = 2*d+1 → Shadow e (h+1) f

theorem shadow_budget {e h d} (path : Shadow e h d) :
    2 ≤ d ∧ 4^h*d ≤ 2^e*3^h := by
  induction path with
  | first => decide
  | @even e h d _ ih =>
    constructor
    · omega
    · calc
        4^h * (2*d) = 2*(4^h*d) := Nat.mul_left_comm _ _ _
        _ ≤ 2*(2^e*3^h) := Nat.mul_le_mul_left _ ih.2
        _ = 2^(e+1)*3^h := by rw [Nat.pow_succ, Nat.mul_comm (2^e) 2, Nat.mul_assoc]
  | @odd e h d f _ hf ih =>
    have hc : 4*f ≤ 3*d := by omega
    constructor
    · omega
    · calc
        4^(h+1)*f = 4^h*(4*f) := by rw [Nat.pow_succ, Nat.mul_assoc]
        _ ≤ 4^h*(3*d) := Nat.mul_le_mul_left _ hc
        _ = (4^h*d)*3 := by ac_rfl
        _ ≤ (2^e*3^h)*3 := Nat.mul_le_mul_right _ ih.2
        _ = 2^e*3^(h+1) := by rw [Nat.pow_succ, Nat.mul_assoc]

/-- With D=A+R and 0<R<3^k, a physically admissible k forces
    the full source prime power 3^b to divide the positive remainder. -/
theorem source_remainder (A R b k : Nat)
    (hA : 3^b ∣ A) (hD : 3^k ∣ A+R)
    (hR : 0 < R) (small : R < 3^k) :
    b < k ∧ 3^b ≤ R := by
  have hbk : b < k := by
    apply Classical.byContradiction
    intro h
    have hka : 3^k ∣ A := Nat.dvd_trans (Nat.pow_dvd_pow 3 (by omega)) hA
    have hkR := (Nat.dvd_add_iff_right hka).mpr hD
    have hle := Nat.le_of_dvd hR hkR
    omega
  have hbD := Nat.dvd_trans (Nat.pow_dvd_pow 3 (Nat.le_of_lt hbk)) hD
  exact ⟨hbk, Nat.le_of_dvd hR ((Nat.dvd_add_iff_right hA).mpr hbD)⟩

end InternalMerge

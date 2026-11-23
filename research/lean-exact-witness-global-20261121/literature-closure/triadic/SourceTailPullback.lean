import Std

/-!
Literal complementary pullbacks of a known triadic terminal state.

`true` denotes an odd original input.  Its complementary inverse is
z ↦ 2z.  At a `false` input that inverse is z ↦ (2z-1)/3.
The module proves the complete numerator formula and persistence of a
reduced positive power of three in the denominator.  It does not claim
that a candidate meets a convergence horizon.
-/

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzSourceTailPullback

def evenCount : List Bool → Nat
  | [] => 0
  | true :: es => evenCount es
  | false :: es => evenCount es + 1

/-- Complete complementary carry, written recursively from the first bit. -/
def carry : List Bool → Int
  | [] => 0
  | true :: es => 2 * carry es
  | false :: es => 2 * carry es + 3 ^ evenCount es

/-- Pull a terminal `u / 3^s` backwards through the literal given word. -/
def pullNumerator : List Bool → Int → Nat → Int
  | [], u, _ => u
  | true :: es, u, s => 2 * pullNumerator es u s
  | false :: es, u, s =>
      2 * pullNumerator es u s - 3 ^ (s + evenCount es)

theorem pullNumerator_formula (es : List Bool) (u : Int) (s : Nat) :
    pullNumerator es u s = 2 ^ es.length * u - 3 ^ s * carry es := by
  induction es with
  | nil => simp [pullNumerator, carry]
  | cons e es ih =>
    cases e <;>
      simp only [pullNumerator, carry, List.length_cons, ih,
        Int.pow_succ, Int.pow_add] <;> grind

private theorem three_power_succ (r : Nat) :
    (3 : Int) ^ (r+1) = 3 * 3 ^ r := by
  rw [Int.pow_succ]
  ac_rfl

private theorem unit_twice (a : Int) (h : a % 3 ≠ 0) :
    (2*a) % 3 ≠ 0 := by omega

private theorem unit_twice_sub (a : Int) (r : Nat)
    (h : a % 3 ≠ 0) : (2*a-3^(r+1)) % 3 ≠ 0 := by
  rw [three_power_succ]
  omega

/-- Once a positive reduced triadic denominator exists, no inverse word
can cancel it.  Every original-even letter adds exactly one power. -/
theorem pullNumerator_three_unit (es : List Bool) (u : Int) (s : Nat)
    (positive : 0 < s) (unit : u % 3 ≠ 0) :
    pullNumerator es u s % 3 ≠ 0 := by
  induction es with
  | nil => exact unit
  | cons e es ih =>
    cases e with
    | true => exact unit_twice _ ih
    | false =>
      obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le
        (show 1 ≤ s + evenCount es by omega)
      have shape : s + evenCount es = r + 1 := by omega
      simp only [pullNumerator, shape]
      exact unit_twice_sub _ r ih

private theorem three_power_odd (r : Nat) : (3 : Int)^r % 2 = 1 := by
  induction r with
  | zero => decide
  | succ r ih => rw [three_power_succ]; omega

/-- Every literal inverse selects the required complementary parity;
applying this to each suffix verifies the whole word, not just an endpoint. -/
theorem pullNumerator_head_parity (e : Bool) (es : List Bool)
    (u : Int) (s : Nat) :
    pullNumerator (e :: es) u s % 2 = (if e then 0 else 1) := by
  cases e with
  | true =>
    change (2 * pullNumerator es u s) % 2 = 0
    omega
  | false =>
    change (2 * pullNumerator es u s - 3^(s + evenCount es)) % 2 = 1
    have h := three_power_odd (s + evenCount es)
    omega

/-- The endpoint divisibility retains both the denominator and the carry. -/
theorem pullNumerator_endpoint (es : List Bool) (u : Int) (s : Nat) :
    (2 : Int)^es.length ∣
      3^evenCount es * pullNumerator es u s +
        3^(s+evenCount es) * carry es := by
  refine ⟨3^evenCount es * u, ?_⟩
  rw [pullNumerator_formula, Int.pow_add]
  grind

/-- The numerator obtained by first pulling back `t` original-even steps. -/
def liftNumerator (u : Int) (s t : Nat) : Int :=
  2^t * (u + 3^s) - 3^(s+t)

theorem liftNumerator_zero (u : Int) (s : Nat) :
    liftNumerator u s 0 = u := by
  simp [liftNumerator]

theorem liftNumerator_succ (u : Int) (s t : Nat) :
    liftNumerator u s (t+1) =
      2 * liftNumerator u s t - 3^(s+t) := by
  have hs : s + (t+1) = (s+t)+1 := by omega
  simp only [liftNumerator, hs, Int.pow_succ]
  grind

theorem liftNumerator_three_unit (u : Int) (s t : Nat)
    (positive : 0 < s) (unit : u % 3 ≠ 0) :
    liftNumerator u s t % 3 ≠ 0 := by
  induction t with
  | zero => simpa [liftNumerator_zero] using unit
  | succ t ih =>
    rw [liftNumerator_succ]
    obtain ⟨r, hr⟩ := Nat.exists_eq_add_of_le (show 1 ≤ s+t by omega)
    have shape : s+t = r+1 := by omega
    rw [shape]
    exact unit_twice_sub _ r ih

/-- The full new candidate depends on the unchanged source dual and the
actual target word.  No source or target carry is omitted. -/
theorem source_tail_formula (es : List Bool) (u : Int) (s t : Nat) :
    pullNumerator es (liftNumerator u s t) (s+t) =
      2^(es.length+t) * (u+3^s) -
        3^(s+t) * (2^es.length + carry es) := by
  rw [pullNumerator_formula]
  simp only [liftNumerator, Int.pow_add]
  grind

theorem source_tail_three_unit (es : List Bool) (u : Int) (s t : Nat)
    (positive : 0 < s) (unit : u % 3 ≠ 0) :
    pullNumerator es (liftNumerator u s t) (s+t) % 3 ≠ 0 := by
  exact pullNumerator_three_unit es _ (s+t) (by omega)
    (liftNumerator_three_unit u s t positive unit)

/-- Appending the terminal original cycle `1,0` multiplies the unreduced
dual numerator by three, exactly matching its extra denominator factor. -/
theorem terminal_cycle_credit (A D : Int) :
    4*(2*A) - (3*D+2*A) = 3*(2*A-D) := by grind

end CollatzSourceTailPullback

#print axioms CollatzSourceTailPullback.pullNumerator_formula
#print axioms CollatzSourceTailPullback.pullNumerator_three_unit
#print axioms CollatzSourceTailPullback.pullNumerator_head_parity
#print axioms CollatzSourceTailPullback.pullNumerator_endpoint
#print axioms CollatzSourceTailPullback.liftNumerator_zero
#print axioms CollatzSourceTailPullback.liftNumerator_succ
#print axioms CollatzSourceTailPullback.liftNumerator_three_unit
#print axioms CollatzSourceTailPullback.source_tail_formula
#print axioms CollatzSourceTailPullback.source_tail_three_unit
#print axioms CollatzSourceTailPullback.terminal_cycle_credit

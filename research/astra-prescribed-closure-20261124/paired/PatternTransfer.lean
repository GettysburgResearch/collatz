import Std

/- Exact simultaneous translation of the two physical trajectories in a fixed grade row.
   The probability estimates and ternary routing in README.md are written arguments. -/
namespace PrescribedPair

def odd (n : Nat) : Nat := n % 2

def T (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def trace : Nat → Nat → Nat × Nat
  | 0, x => (x, 0)
  | e + 1, x => let z := trace e (T x); (z.1, odd x + z.2)

theorem lift (e x d : Nat) :
    trace e (x + 2^e * d) =
      ((trace e x).1 + 3^(trace e x).2 * d, (trace e x).2) := by
  induction e generalizing x d with
  | zero => simp [trace]
  | succ e ih =>
    let m := 2^e * d
    have ex : 2^(e+1) * d = 2 * m := by simp [m, Nat.pow_succ]; ac_rfl
    have parity : odd (x + 2*m) = odd x := by simp [odd]
    rw [ex]
    simp only [trace, parity]
    by_cases ev : x % 2 = 0
    · have st : T (x + 2*m) = T x + 2^e * d := by
        simp [T, ev, m]; omega
      rw [st, ih]
      simp [odd, ev]
    · have ox : odd x = 1 := by unfold odd; omega
      have st : T (x + 2*m) = T x + 2^e * (3*d) := by
        have eq : 2^e * (3*d) = 3*m := by dsimp [m]; ac_rfl
        rw [eq]
        simp [T, ev]; omega
      rw [st, ih, ox, Nat.pow_add]
      simp
      ac_rfl

def paired (e p x y : Nat) : Prop :=
  trace e x = (y,p) ∧ trace e (5*x) = (5*y,p)

/-- Every source of a row moves by exactly the same amount when its target increases
    by a multiple of the row's ternary modulus. The companion follows the same lift. -/
theorem pairedTranslate (e p x y d : Nat) (h : paired e p x y) :
    paired e p (x + 2^e*d) (y + 3^p*d) := by
  rcases h with ⟨h₁, h₂⟩
  constructor
  · rw [lift, h₁]
  · have eq : 5*(x+2^e*d) = 5*x+2^e*(5*d) := by
      rw [Nat.mul_add]; ac_rfl
    rw [eq, lift, h₂]
    simp [Nat.mul_add]
    ac_rfl

theorem traceJoin (e h x : Nat) :
    trace (e+h) x =
      ((trace h (trace e x).1).1, (trace e x).2 + (trace h (trace e x).1).2) := by
  induction e generalizing x with
  | zero => simp [trace]
  | succ e ih =>
    rw [Nat.succ_add]
    simp [trace, ih, Nat.add_assoc]

/-- A single physical paired suffix transports an arbitrary translated row to
    a supplied pair. The only clock and grade added are those of that suffix. -/
theorem patternAtTarget (e p x y d h b z : Nat) (row : paired e p x y)
    (route : paired h b (y + 3^p*d) z) :
    paired (e+h) (p+b) (x + 2^e*d) z := by
  obtain ⟨a,c⟩ := pairedTranslate e p x y d row
  obtain ⟨v,w⟩ := route
  constructor <;> simp [traceJoin, a, c, v, w]

theorem translatedSpan (lo hi t : Nat) : (hi+t)-(lo+t) = hi-lo := by omega

private theorem stripHalves (k z : Nat) : trace k (2^k*z) = (z,0) := by
  have base : trace k 0 = (0,0) := by
    induction k with
    | zero => rfl
    | succ i ih => simp [trace, T, odd, ih]
  have h := lift k 0 z
  simpa [base] using h

/-- The router consumes exactly six initial physical steps followed by k common halvings. -/
theorem router (k q s : Nat) (endVal : 7+9*s = 2^k*q) :
    paired (6+k) 2 (49+64*s) q := by
  have initial : paired 6 2 49 7 := by unfold paired; decide
  obtain ⟨a,b⟩ := pairedTranslate 6 2 49 7 s initial
  change trace 6 (49+64*s) = (7+9*s,2) at a
  change trace 6 (5*(49+64*s)) = (5*(7+9*s),2) at b
  rw [endVal] at a b
  have reord : 5*(2^k*q) = 2^k*(5*q) := by ac_rfl
  constructor <;> simp [traceJoin, a, b, reord, stripHalves]

/-- A literal three-point pattern at clock 18 and its infinitely extensible
    arithmetic comparison: the same source spacing survives any admissible router. -/
theorem examplePattern (d k q s x : Nat)
    (source : x = 178433 ∨ x = 178469 ∨ x = 178475)
    (entry : 1489+3^7*d = 49+64*s) (finish : 7+9*s = 2^k*q) :
    paired (18+(6+k)) 9 (x+2^18*d) q := by
  have row : paired 18 7 x 1489 := by
    rcases source with h | h | h <;> subst x <;> unfold paired <;> decide
  have tail := router k q s finish
  rw [← entry] at tail
  exact patternAtTarget 18 7 x 1489 d (6+k) 2 q row tail

#print axioms lift
#print axioms pairedTranslate
#print axioms patternAtTarget
#print axioms translatedSpan
#print axioms router
#print axioms examplePattern
end PrescribedPair

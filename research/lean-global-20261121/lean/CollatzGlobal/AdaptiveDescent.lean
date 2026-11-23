import CollatzGlobal.OrbitLift

/-!
Finite witness-clock normalization for the five-comparison problem.
The algorithm scans a supplied finite source certificate. No ordinary-size
decrease, uniform return-time bound, or all-time terminal-membership oracle
is assumed. The residual closing statement is explicitly a hypothesis.
-/

open CollatzReverseBasin CollatzClosure

namespace CollatzGlobal

theorem hits_iff_orbit (n d : Nat) : Hits n d ↔ orbit n d = 1 := by
  induction d generalizing n with
  | zero => rfl
  | succ d ih => exact ih (shortcut n)

theorem oddCount_add (n s t : Nat) :
    oddCount n (s+t) = oddCount n s + oddCount (orbit n s) t := by
  induction s generalizing n with
  | zero => simp [oddCount, orbit]
  | succ s ih =>
    simpa [oddCount, orbit, Nat.succ_add, Nat.add_assoc] using
      congrArg (fun x => n % 2 + x) (ih (shortcut n))

theorem balanced_five_zero (n : Nat) : BalancedFive n 0 := by
  exact ⟨rfl, rfl⟩

theorem balanced_five_append {n s t : Nat}
    (hs : BalancedFive n s) (ht : BalancedFive (orbit n s) t) :
    BalancedFive n (s+t) := by
  constructor
  · rw [oddCount_add, oddCount_add, hs.1, hs.2, ht.1]
  · rw [orbit_add, orbit_add, hs.2, ht.2]

instance (n d : Nat) : Decidable (BalancedFive n d) :=
  inferInstanceAs (Decidable
    (oddCount (5*n) d = oddCount n d ∧ orbit (5*n) d = 5*orbit n d))

/-- Last balanced return among the finitely many clocks `0,...,d`.
This is a total executable function; time zero is always a candidate. -/
def lastReturn (n : Nat) : Nat → Nat
  | 0 => 0
  | d+1 => if BalancedFive n (d+1) then d+1 else lastReturn n d

theorem lastReturn_le (n d : Nat) : lastReturn n d ≤ d := by
  induction d with
  | zero => exact Nat.le_refl 0
  | succ d ih =>
    unfold lastReturn
    split <;> omega

theorem lastReturn_balanced (n d : Nat) : BalancedFive n (lastReturn n d) := by
  induction d with
  | zero => exact balanced_five_zero n
  | succ d ih =>
    unfold lastReturn
    split
    · assumption
    · exact ih

theorem lastReturn_maximal (n d t : Nat) (ht : t ≤ d)
    (hb : BalancedFive n t) : t ≤ lastReturn n d := by
  induction d with
  | zero => exact ht
  | succ d ih =>
    unfold lastReturn
    split
    · exact ht
    · by_cases htd : t ≤ d
      · exact ih htd
      · have e : t = d+1 := by omega
        subst t
        contradiction

/-- A finite, certificate-relative residual predicate. It deliberately does not
assert the absence of returns after the supplied hit clock. -/
def FiniteResidual (n d : Nat) : Prop :=
  ∀ t : Nat, 0 < t → t ≤ d → ¬ BalancedFive n t

def residualSource (n d : Nat) : Nat := orbit n (lastReturn n d)
def residualClock (n d : Nat) : Nat := d - lastReturn n d

theorem residual_hits {n d : Nat} (h : orbit n d = 1) :
    orbit (residualSource n d) (residualClock n d) = 1 := by
  unfold residualSource residualClock
  rw [← orbit_add]
  have e : lastReturn n d + (d-lastReturn n d) = d := by
    have := lastReturn_le n d
    omega
  rwa [e]

theorem residual_is_finite (n d : Nat) :
    FiniteResidual (residualSource n d) (residualClock n d) := by
  intro t hpos hle hb
  have htotal := balanced_five_append (lastReturn_balanced n d) hb
  have hbound : lastReturn n d + t ≤ d := by
    have := lastReturn_le n d
    unfold residualClock at hle
    omega
  have hmax := lastReturn_maximal n d (lastReturn n d+t) hbound htotal
  omega

theorem finite_residual_last_zero {n d : Nat} (h : FiniteResidual n d) :
    lastReturn n d = 0 := by
  have hb := lastReturn_balanced n d
  have hl := lastReturn_le n d
  by_cases hz : lastReturn n d = 0
  · exact hz
  · have hn := h (lastReturn n d) (by omega) hl
    exact False.elim (hn hb)

/-- The finite normalization is idempotent: its output has no further return
to consume within the supplied source certificate. -/
theorem normalization_idempotent (n d : Nat) :
    residualSource (residualSource n d) (residualClock n d) = residualSource n d ∧
    residualClock (residualSource n d) (residualClock n d) = residualClock n d := by
  have hz := finite_residual_last_zero (residual_is_finite n d)
  constructor
  · change orbit (residualSource n d)
      (lastReturn (residualSource n d) (residualClock n d)) = residualSource n d
    rw [hz]
    rfl
  · change residualClock n d -
      lastReturn (residualSource n d) (residualClock n d) = residualClock n d
    rw [hz, Nat.sub_zero]

theorem even_balanced_one (n : Nat) (he : n % 2 = 0) : BalancedFive n 1 := by
  have hf : (5*n)%2 = 0 := by omega
  constructor
  · simp [oddCount, he, hf]
  · simp only [orbit, shortcut, he, hf, ↓reduceIte]
    omega

/-- Every certified finite residual is odd, including the zero-clock case. -/
theorem finite_residual_odd {n d : Nat} (hit : orbit n d = 1)
    (h : FiniteResidual n d) : n % 2 = 1 := by
  rcases Nat.mod_two_eq_zero_or_one n with he | ho
  · by_cases hd : d = 0
    · subst d
      change n = 1 at hit
      omega
    · have hno := h 1 (by omega) (by omega)
      exact False.elim (hno (even_balanced_one n he))
  · exact ho

/-- The target membership question is preserved exactly by normalization. -/
theorem residual_five_basin (n d : Nat) :
    Basin (5*n) ↔ Basin (5*residualSource n d) := by
  have h := orbit_basin (5*n) (lastReturn n d)
  rw [(lastReturn_balanced n d).2] at h
  exact h.symm

/-- A supplied ordinary target certificate at the residual compiles into an
ordinary target certificate at the original source, with the exact clock. -/
theorem compile_residual_clock {n d e : Nat}
    (h : orbit (5*residualSource n d) e = 1) :
    orbit (5*n) (lastReturn n d+e) = 1 := by
  rw [orbit_add, (lastReturn_balanced n d).2]
  exact h

/-- Any selected positive return strictly lowers the remaining certificate
clock, independently of whether its ordinary endpoint grows. -/
theorem return_decreases_certificate_clock {n d t : Nat}
    (h : orbit n d = 1) (ht : 0 < t) (hle : t ≤ d) :
    d-t < d ∧ orbit (orbit n t) (d-t) = 1 := by
  constructor
  · omega
  · rw [← orbit_add]
    have e : t+(d-t)=d := by omega
    rwa [e]

/-- The remaining *finite-certificate* closing obligation. No assertion that
it holds is included in this development. -/
def ResidualFiveClosure : Prop :=
  ∀ n d : Nat, orbit n d = 1 → FiniteResidual n d → Basin (5*n)

/-- Every source certificate is normalized by the total finite scan above.
Consequently this residual statement is exactly universal forward-five closure. -/
theorem five_closure_iff_finite_residual :
    (∀ n : Nat, Basin n → Basin (5*n)) ↔ ResidualFiveClosure := by
  constructor
  · intro H n d hd _
    exact H n ⟨d, (hits_iff_orbit n d).mpr hd⟩
  · intro H n hn
    obtain ⟨d, hd⟩ := hn
    have hit := (hits_iff_orbit n d).mp hd
    have out := H (residualSource n d) (residualClock n d)
      (residual_hits hit) (residual_is_finite n d)
    exact (residual_five_basin n d).mpr out

/-! Kernel-reduced ordinary examples expose the rank distinction. The last
return can increase the positive integer while shortening its certificate. -/

theorem expanding_return_example :
    BalancedFive 19483 30 ∧ orbit 19483 30 = 21091 := by decide

set_option maxRecDepth 100000 in
theorem expanding_source_certificate : orbit 19483 127 = 1 := by decide

set_option maxRecDepth 100000 in
set_option maxHeartbeats 1000000 in
theorem expanding_normal_form :
    lastReturn 19483 127 = 30 ∧
    residualSource 19483 127 = 21091 ∧ residualClock 19483 127 = 97 := by decide

theorem rank_one_finite_residual :
    orbit 5 4 = 1 ∧ FiniteResidual 5 4 := by
  constructor
  · decide
  · intro t ht hle
    have : t = 1 ∨ t = 2 ∨ t = 3 ∨ t = 4 := by omega
    rcases this with h | h | h | h <;> subst t <;> decide

theorem asynchronous_numerical_return :
    orbit 5 2 = 4 ∧ orbit 25 10 = 20 := by decide

end CollatzGlobal

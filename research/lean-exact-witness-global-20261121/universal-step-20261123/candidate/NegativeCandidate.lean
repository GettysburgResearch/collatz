/-
Finite arithmetic for the negative-numerator exact recognizer.
No universal candidate-existence premise and no infinite conjugacy axiom.
The written packet supplies completeness from the pinned triadic rigidity
theorem and the forced terminal segment.  This module proves the local
halving, its finite clock bound, backward-code height bounds, and soundness
of the executable ordinary convergence checker.
-/
import Std

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace CollatzNegativeCandidate

/-- A negative numerator update with a nonnegative added term halves its
absolute size.  Both literal positive-denominator branches have this form. -/
theorem negative_halving (w v c : Int) (hw : w < 0) (hv : v < 0)
    (hc : 0 ≤ c) (edge : 2*v = w+c) :
    2*v.natAbs ≤ w.natAbs := by
  have aw := Int.ofNat_natAbs_of_nonpos (Int.le_of_lt hw)
  have av := Int.ofNat_natAbs_of_nonpos (Int.le_of_lt hv)
  omega

/-- Exact finite decay, with no exponent-dependent weight. -/
theorem halving_trace (m : Nat → Nat) (K : Nat)
    (steps : ∀ j, j < K → 2*m (j+1) ≤ m j) :
    2^K*m K ≤ m 0 := by
  induction K with
  | zero => simp
  | succ K ih =>
      have old := ih (by intro j hj; exact steps j (by omega))
      have last := Nat.mul_le_mul_left (2^K) (steps K (by omega))
      rw [Nat.pow_succ, Nat.mul_assoc]
      exact Nat.le_trans last old

/-- Fewer than E transitions can end at a positive integer magnitude if
the initial magnitude is smaller than 2^E. -/
theorem negative_clock (m : Nat → Nat) (K E : Nat)
    (steps : ∀ j, j < K → 2*m (j+1) ≤ m j)
    (terminal : 0 < m K) (budget : m 0 < 2^E) : K < E := by
  have decay := halving_trace m K steps
  have lower : 2^K ≤ 2^K*m K := by
    simpa using Nat.mul_le_mul_left (2^K) terminal
  apply Classical.byContradiction
  intro bad
  have powers := Nat.pow_le_pow_right (by decide : 0 < 2)
    (show E ≤ K by omega)
  omega

/-- Backward negative numerator code from the pair (8,-1/9).
An original odd inverse doubles A. An original even inverse adds 3^r
while increasing the reduced denominator exponent. -/
inductive NegativeCode : Nat → Nat → Nat → Prop where
  | terminal : NegativeCode 1 2 0
  | odd {A r K : Nat} : NegativeCode A r K →
      NegativeCode (2*A) r (K+1)
  | even {A r K : Nat} : NegativeCode A r K →
      NegativeCode (2*A+3^r) (r+1) (K+1)

theorem code_positive {A r K : Nat} (code : NegativeCode A r K) : 0 < A := by
  induction code with
  | terminal => decide
  | odd old ih => omega
  | @even A r K old ih =>
      have pos := Nat.pow_pos (by decide : 0 < 3) (n := r)
      omega

theorem code_clock_bound {A r K : Nat} (code : NegativeCode A r K) :
    2^K ≤ A := by
  induction code with
  | terminal => decide
  | @odd A r K old ih =>
      simp only [Nat.pow_succ]
      omega
  | @even A r K old ih =>
      have pos := Nat.pow_pos (by decide : 0 < 3) (n := r)
      simp only [Nat.pow_succ]
      omega

theorem code_exponent_bound {A r K : Nat} (code : NegativeCode A r K) :
    2 ≤ r ∧ r ≤ K+2 := by
  induction code with
  | terminal => decide
  | odd old ih => omega
  | even old ih => omega

/-- Sharp numerator/denominator inequality. Equality is realized by the
all-even backward code; its ordinary inputs are powers of two. -/
theorem code_sharp_height {A r K : Nat} (code : NegativeCode A r K) :
    3^r ≤ A+2^(r+1) := by
  induction code with
  | terminal => decide
  | @odd A r K old ih => omega
  | @even A r K old ih =>
      simp only [Nat.pow_succ]
      simp only [Nat.pow_succ] at ih
      omega

/-- A binary-encoded giant exponent can be rejected before constructing
3^r: every successful reduced negative code satisfies 3^r ≤ 9A. -/
theorem code_denominator_bound {A r K : Nat} (code : NegativeCode A r K) :
    3^r ≤ 9*A := by
  induction code with
  | terminal => decide
  | @odd A r K old ih => omega
  | @even A r K old ih =>
      simp only [Nat.pow_succ]
      omega

theorem code_funded_clock {A r K E : Nat} (code : NegativeCode A r K)
    (budget : A < 2^E) : K+3 ≤ E+2 := by
  have lower := code_clock_bound code
  have small : K < E := by
    apply Classical.byContradiction
    intro bad
    have powers := Nat.pow_le_pow_right (by decide : 0 < 2)
      (show E ≤ K by omega)
    omega
  omega

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => orbit (shortcut n) k

def Terminal (n : Nat) (w : Int) (r : Nat) : Prop :=
  n=4 ∧ r=1 ∧ w=1

instance (n : Nat) (w : Int) (r : Nat) : Decidable (Terminal n w r) :=
  inferInstanceAs (Decidable (n=4 ∧ r=1 ∧ w=1))

def Compatible (n : Nat) (w : Int) : Prop :=
  (n % 2 = 0 ∧ w % 2 = 1) ∨ (n % 2 = 1 ∧ w % 2 = 0)

instance (n : Nat) (w : Int) : Decidable (Compatible n w) :=
  inferInstanceAs (Decidable
    ((n % 2 = 0 ∧ w % 2 = 1) ∨ (n % 2 = 1 ∧ w % 2 = 0)))

def nextNumerator (n : Nat) (w : Int) (r : Nat) : Int :=
  if n % 2 = 0 then (w+(3:Int)^(r-1))/2 else w/2

def nextExponent (n r : Nat) : Nat := if n % 2 = 0 then r-1 else r

/-- The executable numerator update has the asserted halving property
on a compatible negative-to-negative step. -/
theorem literal_negative_halving (n : Nat) (w : Int) (r : Nat)
    (compatible : Compatible n w) (negative : w < 0)
    (nextNegative : nextNumerator n w r < 0) :
    2*(nextNumerator n w r).natAbs ≤ w.natAbs := by
  have aw := Int.ofNat_natAbs_of_nonpos (Int.le_of_lt negative)
  have av := Int.ofNat_natAbs_of_nonpos (Int.le_of_lt nextNegative)
  by_cases even : n % 2 = 0
  · have positive : (0:Int) < 3^(r-1) := Int.pow_pos (by decide)
    simp only [nextNumerator, even, ite_true] at nextNegative av ⊢
    omega
  · have parity : w % 2 = 0 := by
      rcases compatible with h | h
      · exact False.elim (even h.1)
      · exact h.2
    simp only [nextNumerator, even, ite_false] at nextNegative av ⊢
    omega

/-- Fuel bounds negative transitions only. Exact terminal equality is
checked even at fuel zero. All wrong crossings and exhausted denominators
are rejected, rather than continued through the positive sector. -/
def negativeSeek : Nat → Nat → Int → Nat → Bool
  | 0, n, w, r => decide (Terminal n w r)
  | fuel+1, n, w, r =>
      if Terminal n w r then true
      else if w < 0 ∧ 0 < r ∧ Compatible n w then
        negativeSeek fuel (shortcut n) (nextNumerator n w r) (nextExponent n r)
      else false

/-- Every accepted execution supplies an actual ordinary hit, with the
exact two finishing clocks 4→2→1. No completeness assumption is used. -/
theorem negativeSeek_sound (fuel n : Nat) (w : Int) (r : Nat)
    (accepted : negativeSeek fuel n w r = true) :
    ∃ k, k ≤ fuel+2 ∧ orbit n k = 1 := by
  induction fuel generalizing n w r with
  | zero =>
      have term : Terminal n w r := by simpa [negativeSeek] using accepted
      have hn : n=4 := term.1
      subst n
      exact ⟨2, by omega, by decide⟩
  | succ fuel ih =>
      by_cases term : Terminal n w r
      · have hn : n=4 := term.1
        subst n
        exact ⟨2, by omega, by decide⟩
      · by_cases guard : w < 0 ∧ 0 < r ∧ Compatible n w
        · have next : negativeSeek fuel (shortcut n) (nextNumerator n w r)
              (nextExponent n r) = true := by
            simpa [negativeSeek, term, guard] using accepted
          obtain ⟨k,bound,hit⟩ := ih _ _ _ next
          exact ⟨k+1, by omega, by simpa [orbit] using hit⟩
        · simp [negativeSeek, term, guard] at accepted

/-- Literal first-crossing certificate. No positive-sector continuation
is admitted except the exact endpoint (4,1/3). -/
inductive NegativePath : Nat → Int → Nat → Nat → Prop where
  | terminal : NegativePath 4 1 1 0
  | step {n : Nat} {w : Int} {r k : Nat}
      (negative : w < 0) (denominator : 0 < r)
      (compatible : Compatible n w)
      (tail : NegativePath (shortcut n) (nextNumerator n w r)
        (nextExponent n r) k) : NegativePath n w r (k+1)

private theorem path_negative {n : Nat} {w : Int} {r k : Nat}
    (path : NegativePath n w r k) (positive : 0 < k) : w < 0 := by
  cases path with
  | terminal => omega
  | step negative _ _ _ => exact negative

private theorem path_numerator_bound {n : Nat} {w : Int} {r k : Nat}
    (path : NegativePath n w r k) : k=0 ∨ 2^(k-1) ≤ w.natAbs := by
  induction path with
  | terminal => exact Or.inl rfl
  | @step n w r k negative denominator compatible tail ih =>
      apply Or.inr
      by_cases zero : k=0
      · simp only [zero, Nat.zero_add, Nat.sub_self, Nat.pow_zero]
        have size := Int.ofNat_natAbs_of_nonpos (Int.le_of_lt negative)
        omega
      · have nextNegative := path_negative tail (by omega)
        have halves := literal_negative_halving n w r compatible negative nextNegative
        have old : 2^(k-1) ≤ (nextNumerator n w r).natAbs := by
          rcases ih with eq | lower
          · exact False.elim (zero eq)
          · exact lower
        have exponent : k-1+1=k := by omega
        have doubled := Nat.mul_le_mul_right 2 old
        rw [← Nat.pow_succ, Nat.succ_eq_add_one, exponent] at doubled
        simpa using Nat.le_trans doubled (by simpa [Nat.mul_comm] using halves)

/-- Every genuine negative first-crossing certificate is funded by any
E with |w|<2^E. This proves the linear binary-length clock bound. -/
theorem negativePath_clock {n : Nat} {w : Int} {r k E : Nat}
    (path : NegativePath n w r k) (budget : w.natAbs < 2^E) : k ≤ E := by
  rcases path_numerator_bound path with zero | lower
  · omega
  · apply Classical.byContradiction
    intro bad
    have exponent : E ≤ k-1 := by omega
    have powers := Nat.pow_le_pow_right (by decide : 0 < 2) exponent
    omega

/-- The executable checker accepts every such literal certificate when
its supplied fuel covers the certificate length. -/
theorem negativeSeek_complete {n : Nat} {w : Int} {r k : Nat}
    (path : NegativePath n w r k) (fuel : Nat) (funded : k ≤ fuel) :
    negativeSeek fuel n w r = true := by
  induction path generalizing fuel with
  | terminal => cases fuel <;> simp [negativeSeek, Terminal]
  | @step n w r k negative denominator compatible tail ih =>
      cases fuel with
      | zero => omega
      | succ fuel =>
          by_cases term : Terminal n w r
          · simp [negativeSeek, term]
          · have next := ih fuel (by omega)
            simpa [negativeSeek, term, negative, denominator, compatible] using next

example : negativeSeek 3 3 (-4) 2 = true := by decide
example : negativeSeek 1 8 (-1) 2 = true := by decide
example : negativeSeek 1 16 (-1) 2 = false := by decide
example : negativeSeek 1 16 (-1) 40 = false := by decide

end CollatzNegativeCandidate

#print axioms CollatzNegativeCandidate.negative_halving
#print axioms CollatzNegativeCandidate.halving_trace
#print axioms CollatzNegativeCandidate.negative_clock
#print axioms CollatzNegativeCandidate.code_positive
#print axioms CollatzNegativeCandidate.code_clock_bound
#print axioms CollatzNegativeCandidate.code_exponent_bound
#print axioms CollatzNegativeCandidate.code_sharp_height
#print axioms CollatzNegativeCandidate.code_denominator_bound
#print axioms CollatzNegativeCandidate.code_funded_clock
#print axioms CollatzNegativeCandidate.literal_negative_halving
#print axioms CollatzNegativeCandidate.negativeSeek_sound
#print axioms CollatzNegativeCandidate.negativePath_clock
#print axioms CollatzNegativeCandidate.negativeSeek_complete

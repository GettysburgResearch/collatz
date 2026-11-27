import Std

namespace Collatz.OctaveOccupation

def occupied (x : Nat) : Nat := if x = 0 then 0 else 1

/-- The nonnegative difference at an edge after paying for the occupied
terminal octave. It determines the left level given the right level. -/
def dropCode (left right : Nat) : Nat :=
  left + occupied right - right

theorem drop_balance (left right : Nat) (rise : right ≤ left + 1) :
    dropCode left right + right = left + occupied right := by
  simp only [dropCode, occupied]
  split <;> omega

theorem recover_left (left right : Nat) (rise : right ≤ left + 1) :
    dropCode left right + (right - 1) = left := by
  have balance := drop_balance left right rise
  simp only [occupied] at balance
  split at balance <;> omega

/-- Encode edges in reverse order, beginning at the terminal level. -/
def encode (height : Nat → Nat) : Nat → List Nat
  | 0 => []
  | k + 1 => dropCode (height k) (height (k+1)) :: encode height k

def countOccupied (height : Nat → Nat) : Nat → Nat
  | 0 => 0
  | k + 1 => countOccupied height k + occupied (height (k+1))

theorem encode_length (height : Nat → Nat) (k : Nat) :
    (encode height k).length = k := by
  induction k <;> simp_all [encode]

theorem encode_mass (height : Nat → Nat) (k : Nat)
    (rise : ∀ j < k, height (j+1) ≤ height j + 1) :
    (encode height k).sum + height k = height 0 + countOccupied height k := by
  induction k with
  | zero => simp [encode, countOccupied]
  | succ k ih =>
    have previous := ih (fun j hj => rise j (by omega))
    have last := drop_balance (height k) (height (k+1)) (rise k (by omega))
    simp only [encode, List.sum_cons, countOccupied]
    omega

theorem encode_injective (u v : Nat → Nat) (k : Nat)
    (ru : ∀ j < k, u (j+1) ≤ u j + 1)
    (rv : ∀ j < k, v (j+1) ≤ v j + 1)
    (terminal : u k = v k) (equalCode : encode u k = encode v k) :
    ∀ j ≤ k, u j = v j := by
  induction k with
  | zero =>
    intro j hj
    obtain rfl : j = 0 := by omega
    exact terminal
  | succ k ih =>
    simp only [encode, List.cons.injEq] at equalCode
    have lu := recover_left (u k) (u (k+1)) (ru k (by omega))
    have lv := recover_left (v k) (v (k+1)) (rv k (by omega))
    rw [equalCode.1, terminal] at lu
    have e : u k = v k := by omega
    intro j hj
    by_cases last : j = k+1
    · simpa [last] using terminal
    · exact ih (fun i hi => ru i (by omega)) (fun i hi => rv i (by omega))
        e equalCode.2 j (by omega)

set_option exponentiation.threshold 20000 in
/-- Integer form of (128/25) f(4/75) < log 3. -/
theorem entropy_margin : 79^(79*128) < 3^1875 * (75^75 * 4^4)^128 := by
  decide +kernel

#print axioms drop_balance
#print axioms recover_left
#print axioms encode_length
#print axioms encode_mass
#print axioms encode_injective
#print axioms entropy_margin

end Collatz.OctaveOccupation

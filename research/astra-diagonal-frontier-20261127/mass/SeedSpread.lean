import Std

/-! Finite arithmetic for ordinary principal-terminal leakage. A row records
the residues of selected physical prefixes after one odd-unit dilation.
All finite computations use kernel reduction. -/

namespace SeedSpread

def modulus : Nat := 6561

def codes : List (List Nat) :=
  [[1,1,2,1,1,1,3,4], [1,1,2,1,2,2,1,4], [1,1,1,1,1,1,4,4],
   [1,1,2,1,2,2,3,2], [1,2,2,1,1,1,4,2], [1,2,2,2,1,2,2,2],
   [1,1,2,1,1,2,4,2], [1,2,1,2,1,2,1,4], [1,1,1,1,4,1,3,2],
   [1,1,1,1,1,1,2,6], [1,2,1,1,2,1,4,2], [1,2,1,2,1,1,4,2],
   [1,1,3,1,1,2,1,4], [1,2,1,1,1,1,3,4]]

def residues : List Nat :=
  [1477, 6526, 1384, 5296, 2863, 4888, 5014,
   1639, 859, 4972, 4753, 3997, 4636, 3907]

def acceptsFrom (i a : Nat) : List Nat → Bool
  | [] => true
  | e :: rest => 0 < e && 4 * (a + e) ≤ 7 * (i+1) && acceptsFrom (i+1) (a+e) rest

def carry (w : List Nat) : Nat :=
  (w.foldl (fun (state : Nat × Nat) e =>
    (state.1 + e, 3 * state.2 + 2 ^ state.1)) (0,0)).2

theorem selected_words :
    (codes.zip residues).all (fun p => p.1.length == 8 && p.1.sum == 14 &&
      acceptsFrom 0 0 p.1 && (2^14 * p.2) % modulus == carry p.1 % modulus) = true := by
  decide +kernel

def withinGaps : Nat → List Nat → Bool
  | _, [] => true
  | x, y :: ys => y ≤ x + 2982 && withinGaps y ys

def insertNat (x : Nat) : List Nat → List Nat
  | [] => [x]
  | y :: ys => if x ≤ y then x :: y :: ys else y :: insertNat x ys

def sortNat : List Nat → List Nat
  | [] => []
  | x :: xs => insertNat x (sortNat xs)

def row (a : Nat) : Bool :=
  if a % 3 == 0 then true else
    match sortNat (residues.map (fun r => (a*r) % modulus)) with
    | [] => false
    | x :: xs => withinGaps x (xs ++ [x+modulus])

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem rows_first_half : ((List.range 3281).all row) = true := by
  decide +kernel

theorem row_at {a : Nat} (ha : a < 3281) : row a = true :=
  (List.all_eq_true.mp rows_first_half) a (List.mem_range.mpr ha)

theorem next_even_terminal_fails (n e A : Nat)
    (ht : 4*A = 7*n) (he : 2 ≤ e) : 7*(n+1) < 4*(A+e) := by omega

theorem block_pairs :
    carry [1,2] = 5 ∧ carry [2,1] = 7 ∧
    carry [1,3] = 5 ∧ carry [2,2] = 7 ∧
    9*81 < 8*128 ∧ 3*81^3 < 128^3 ∧ 9*81^5 < 128^5 := by decide +kernel

/-- With signed remainders at consecutive denominators q and 9q,
these bounds ensure that the modular congruence is equality. -/
theorem no_wrap (q r s u : Int) (hu : u = 8 ∨ u = 16) (hq : 0 < q)
    (h₁ : -q ≤ 26*r) (h₂ : 26*r ≤ q)
    (h₃ : -9*q ≤ 26*s) (h₄ : 26*s ≤ 9*q)
    (hd : q ∣ s - u*r) : s = u*r := by
  have habs : (s-u*r).natAbs < q.natAbs := by
    rcases hu with rfl | rfl <;> omega
  have := Int.eq_zero_of_dvd_of_natAbs_lt_natAbs hd habs
  omega

#print axioms block_pairs
#print axioms no_wrap
#print axioms selected_words
#print axioms rows_first_half
#print axioms row_at
#print axioms next_even_terminal_fails

end SeedSpread

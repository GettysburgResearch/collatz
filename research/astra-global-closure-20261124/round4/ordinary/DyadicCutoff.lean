import Mathlib.Tactic

/-! Finite, integer first-passage estimates for the actual shortcut parity coefficients. -/
set_option autoImplicit false
namespace Collatz.DyadicCutoff

def words : ℕ → List (List Bool)
  | 0 => [[]]
  | k+1 => ((words k).map (false :: ·)) ++ ((words k).map (true :: ·))

private theorem length_words (k : ℕ) : (words k).length = 2^k := by
  induction k with
  | zero => rfl
  | succ k ih => simp [words, ih, pow_succ]; omega

/-- Starting from numerator a and threshold b, subsequent multipliers are
1/2 and 3/2. The empty prefix is included. -/
def crosses (a b : ℕ) : List Bool → Bool
  | [] => decide (b ≤ a)
  | bit :: tail => decide (b ≤ a) || crosses (if bit then 3*a else a) (2*b) tail

def hits (a b k : ℕ) := ((words k).filter (crosses a b)).length

private theorem immediate (a b : ℕ) (hb : b ≤ a) (w : List Bool) : crosses a b w = true := by
  cases w <;> simp [crosses, hb]

private theorem hits_of_le (a b k : ℕ) (hb : b ≤ a) : hits a b k = 2^k := by
  rw [hits, List.filter_eq_self.mpr (fun w _ => immediate a b hb w), length_words]

private theorem hits_succ (a b k : ℕ) (below : ¬ b ≤ a) :
    hits a b (k+1) = hits a (2*b) k + hits (3*a) (2*b) k := by
  simp [hits, words, List.filter_map, Function.comp_def, crosses, below]

/-- Finite maximal inequality on literal binary words. For a=1, b=Z this
bounds the number of length-k words with some prefix multiplier at least Z. -/
theorem first_passage (a b k : ℕ) : b * hits a b k ≤ a * 2^k := by
  induction k generalizing a b with
  | zero =>
    by_cases hb : b ≤ a
    · simpa [hits_of_le a b 0 hb] using hb
    · simp [hits, words, crosses, hb]
  | succ k ih =>
    by_cases hb : b ≤ a
    · rw [hits_of_le a b (k+1) hb]
      exact Nat.mul_le_mul_right _ hb
    · rw [hits_succ a b k hb, pow_succ]
      have h := Nat.add_le_add (ih a (2*b)) (ih (3*a) (2*b))
      nlinarith

def step (x : ℕ) := if x%2 = 0 then x/2 else (3*x+1)/2

def parity (x : ℕ) := decide (x%2 = 1)

def bits : ℕ → ℕ → List Bool
  | 0, _ => []
  | k+1, x => parity x :: bits k (step x)

def last : ℕ → ℕ → ℕ
  | 0, x => x
  | k+1, x => last k (step x)

def scale : List Bool → ℕ
  | [] => 1
  | b::w => (if b then 3 else 1) * scale w

def carry : List Bool → ℕ
  | [] => 0
  | b::w => (if b then scale w else 0) + 2*carry w

private theorem first_edge (x : ℕ) :
    2*step x = (if parity x then 3 else 1)*x + (if parity x then 1 else 0) := by
  by_cases he : x%2 = 0
  · have ho : ¬ x%2 = 1 := by omega
    simp [step, parity, he]; omega
  · have ho : x%2 = 1 := by omega
    simp [step, parity, ho]; omega

/-- The same multiplier in the binary estimate is the exact physical row slope. -/
theorem affine (k x : ℕ) :
    2^k * last k x = scale (bits k x)*x + carry (bits k x) := by
  induction k generalizing x with
  | zero => simp [last, scale, carry, bits]
  | succ k ih =>
    rw [pow_succ, last, bits, scale, carry]
    let w := bits k (step x)
    have mul : 2^(k+1)*last k (step x) = scale w * (2*step x) + 2*carry w := by
      rw [pow_succ]
      calc
        2^k * 2 * last k (step x) = 2 * (2^k * last k (step x)) := by ring
        _ = _ := by rw [ih]; dsimp [w]; ring
    rw [first_edge] at mul
    cases h : parity x <;> simp [h, w, pow_succ] at mul ⊢ <;> nlinarith

private theorem scale_odd (w : List Bool) : Odd (scale w) := by
  induction w with
  | nil => exact ⟨0,rfl⟩
  | cons b w ih =>
    cases b
    · simpa only [scale, Bool.false_eq_true, ↓reduceIte, one_mul] using ih
    · exact (show Odd (3:ℕ) from ⟨1,rfl⟩).mul ih

/-- Equal chronological parities force the ordinary source difference to be
a multiple of the complete binary modulus. This includes arbitrary translation. -/
theorem one_residue (k x y : ℕ) (eqw : bits k x = bits k y) :
    2^k ∣ y-x := by
  have hx := affine k x
  have hy := affine k y
  rw [eqw] at hx
  let m := scale (bits k y)
  have h : (2^k) ∣ m * (y-x) := by
    have hm : m * (y-x) = 2^k * last k y - 2^k * last k x := by
      rw [hx, hy, Nat.mul_sub]; dsimp [m]; omega
    rw [hm]
    exact Nat.dvd_sub (Nat.dvd_mul_right _ _) (Nat.dvd_mul_right _ _)
  have base : Nat.Coprime 2 m := Nat.coprime_two_left.mpr (scale_odd (bits k y))
  have cop : (2^k).Coprime m := base.pow_left k
  exact cop.dvd_of_dvd_mul_left h

private theorem bits_mem (k x : ℕ) : bits k x ∈ words k := by
  induction k generalizing x with
  | zero => simp [bits, words]
  | succ k ih =>
    rw [bits, words, List.mem_append]
    cases hp : parity x
    · exact Or.inl (List.mem_map.mpr ⟨_, ih _, rfl⟩)
    · exact Or.inr (List.mem_map.mpr ⟨_, ih _, rfl⟩)

/-- Maximal inequality for an actual set of positive or nonnegative integer
origins in one arbitrarily translated complete binary period. -/
theorem source_first_passage (S : Finset ℕ) (k Z : ℕ)
    (width : ∀ x ∈ S, ∀ y ∈ S, x < y + 2^k)
    (hit : ∀ x ∈ S, crosses 1 Z (bits k x) = true) :
    Z * S.card ≤ 2^k := by
  classical
  let W := (words k).filter (crosses 1 Z)
  have hcard : S.card ≤ W.toFinset.card := by
    apply Finset.card_le_card_of_injOn (bits k)
    · intro x hx
      exact List.mem_toFinset.mpr (List.mem_filter.mpr ⟨bits_mem k x, hit x hx⟩)
    · intro x hx y hy eqw
      rcases lt_trichotomy x y with h | eq | h
      · have dv := Nat.le_of_dvd (show 0 < y-x by omega) (one_residue k x y eqw)
        have up := width y hy x hx
        omega
      · exact eq
      · have dv := Nat.le_of_dvd (show 0 < x-y by omega) (one_residue k y x eqw.symm)
        have up := width x hx y hy
        omega
  have bound : S.card ≤ hits 1 Z k := hcard.trans (List.toFinset_card_le W)
  exact (Nat.mul_le_mul_left Z bound).trans (by simpa using first_passage 1 Z k)

#print axioms source_first_passage
#print axioms first_passage
#print axioms affine
#print axioms one_residue
end Collatz.DyadicCutoff

import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Physical parity echoes for the ordinary shortcut Collatz map. -/

namespace PhysicalEcho

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def orbit : ℕ → ℕ → ℕ
  | 0, x => x
  | t+1, x => orbit t (step x)

/-- Equality of the first h physical shortcut parity bits of two sources. -/
def agree (h x y : ℕ) : Prop :=
  ∀ i < h, orbit i x % 2 = orbit i y % 2

theorem orbit_add (a b x : ℕ) : orbit (a + b) x = orbit b (orbit a x) := by
  induction a generalizing x with
  | zero => simp [orbit]
  | succ a ih => simpa [Nat.succ_add, orbit] using ih (step x)

private theorem lift_congruence {q x y : ℕ} (hp : x % 2 = y % 2)
    (ht : step x ≡ step y [MOD 2 ^ q]) : x ≡ y [MOD 2 ^ (q+1)] := by
  have hm := ht.mul_left' 2
  rw [← pow_succ'] at hm
  by_cases hx : x % 2 = 0
  · have hy := hp.symm.trans hx
    have ex : 2 * step x = x := by simp [step, hx]; omega
    have ey : 2 * step y = y := by simp [step, hy]; omega
    rwa [ex, ey] at hm
  · have hy : y % 2 ≠ 0 := by omega
    have ex : 2 * step x = 3*x+1 := by simp [step, hx]; omega
    have ey : 2 * step y = 3*y+1 := by simp [step, hy]; omega
    rw [ex, ey] at hm
    have hco : Nat.Coprime (2 ^ (q+1)) 3 :=
      (show Nat.Coprime 2 3 from by decide).pow_left _
    exact Nat.ModEq.cancel_left_of_coprime hco (hm.add_right_cancel' 1)

theorem agree_congruent (h x y : ℕ) (w : agree h x y) : x ≡ y [MOD 2 ^ h] := by
  induction h generalizing x y with
  | zero => simp [Nat.ModEq, Nat.mod_one]
  | succ h ih =>
    apply lift_congruence (w 0 (by omega))
    apply ih
    intro i hi
    exact w (i+1) (by omega)

private theorem step_height (x : ℕ) : 2 * (step x + 1) ≤ 3 * (x + 1) := by
  unfold step
  split <;> omega

theorem orbit_height (d x : ℕ) : 2^d * (orbit d x + 1) ≤ 3^d * (x+1) := by
  induction d generalizing x with
  | zero => simp [orbit]
  | succ d ih =>
    calc
      2^(d+1) * (orbit (d+1) x + 1) = 2 * (2^d * (orbit d (step x) + 1)) := by
        simp only [orbit, pow_succ]; ring
      _ ≤ 2 * (3^d * (step x+1)) := Nat.mul_le_mul_left _ (ih _)
      _ = 3^d * (2 * (step x+1)) := by ring
      _ ≤ 3^d * (3 * (x+1)) := Nat.mul_le_mul_left _ (step_height x)
      _ = 3^(d+1) * (x+1) := by rw [pow_succ]; ring

/-- Coinciding h-bit windows at positions 0 and d pin down the actual state
    whenever the integer height fits in the common parity modulus. -/
theorem echo_return (d h x : ℕ) (w : agree h x (orbit d x))
    (height : 3^d * (x+1) < 2^d * 2^h) : orbit d x = x := by
  have hy : orbit d x + 1 < 2^h :=
    Nat.lt_of_mul_lt_mul_left <| (orbit_height d x).trans_lt height
  have htwo : (2:ℕ)^d ≤ 3^d := Nat.pow_le_pow_left (by decide) d
  have hx : x+1 < 2^h :=
    Nat.lt_of_mul_lt_mul_left <| (Nat.mul_le_mul_right (x+1) htwo).trans_lt height
  exact ((agree_congruent h x _ w).eq_of_lt_of_lt (by omega) (by omega)).symm

/-- A square at the beginning of an ordinary orbit forces a genuine return
    once its half-length passes the displayed, source-dependent threshold. -/
theorem square_return (d x : ℕ) (w : agree d x (orbit d x))
    (height : 3^d * (x+1) < 4^d) : orbit d x = x := by
  apply echo_return d d x w
  simpa [← mul_pow] using height

private theorem bernoulli (d : ℕ) : (d+3) * 3^d ≤ 3 * 4^d := by
  induction d with
  | zero => decide
  | succ d ih =>
    simp only [pow_succ]
    nlinarith [Nat.zero_le (d * 3^d), Nat.mul_le_mul_left 4 ih]

/-- The logarithmic cutoff in square_return is in particular reached once
    d > 3x. This elementary bound suffices for cofinal square prefixes. -/
theorem large_square_return (d x : ℕ) (w : agree d x (orbit d x))
    (hd : 3*x < d) : orbit d x = x := by
  apply square_return d x w
  have h := Nat.mul_lt_mul_of_pos_right (show 3*(x+1) < d+3 by omega)
    (show 0 < 3^d by positivity)
  have h' := h.trans_le (bernoulli d)
  nlinarith

/-- In particular, if the raw parity word at x begins with arbitrarily long
    squares then the orbit from x is periodic. -/
theorem periodic_of_cofinal_squares (x : ℕ)
    (hs : ∀ k : ℕ, ∃ d, k < d ∧ agree d x (orbit d x)) :
    ∃ d > 0, orbit d x = x := by
  obtain ⟨d, hd, hw⟩ := hs (3*x)
  exact ⟨d, by omega, large_square_return d x hw hd⟩

#print axioms PhysicalEcho.periodic_of_cofinal_squares

/-- The odd-step count is tied to the base integer's actual itinerary. -/
def odds : ℕ → ℕ → ℕ
  | 0, _ => 0
  | t+1, x => (if x % 2 = 0 then 0 else 1) + odds t (step x)

private theorem shift_step (x k : ℕ) :
    step (x+2*k) = step x + (if x % 2 = 0 then 1 else 3)*k := by
  have hp : (x+2*k)%2 = x%2 := by omega
  simp only [step, hp]
  split <;> omega

/-- At any cut through a physical parity cylinder, the free source quotient
    is multiplied by exactly the displayed integer. -/
theorem transport (j r x k : ℕ) :
    orbit j (x + 2^(j+r)*k) = orbit j x + (2^r * 3^(odds j x))*k := by
  induction j generalizing x k with
  | zero => simp [orbit, odds]
  | succ j ih =>
    have he : 2^(j+1+r)*k = 2*(2^(j+r)*k) := by
      rw [Nat.succ_add, pow_succ]; ring
    simp only [orbit, he, shift_step, odds]
    by_cases hx : x % 2 = 0
    · simp only [hx, ite_true, one_mul, zero_add]
      exact ih (step x) k
    · simp only [hx, ite_false]
      rw [pow_add 3 1, pow_one]
      rw [show 3 * (2^(j+r)*k) = 2^(j+r)*(3*k) by ring, ih]
      ring

/-- The spacing at the cut j of a full length-L word. -/
def spacing (L j x : ℕ) : ℕ := 2^(L-j) * 3^(odds j x)

theorem cut_value {L j : ℕ} (x k : ℕ) (hj : j ≤ L) :
    orbit j (x + 2^L*k) = orbit j x + spacing L j x * k := by
  simpa only [spacing, Nat.add_sub_of_le hj] using transport j (L-j) x k

/-- Varying the free quotient never changes any of the first L parity bits. -/
theorem same_word (L x k : ℕ) : agree L x (x+2^L*k) := by
  intro j hj
  rw [cut_value x k (by omega : j ≤ L)]
  have htwo : 2 ∣ spacing L j x := by
    have he : L-j = (L-j-1)+1 := by omega
    unfold spacing
    rw [he, pow_succ]
    exact dvd_mul_of_dvd_left (dvd_mul_left _ _) _
  rcases htwo with ⟨a, ha⟩
  rw [ha, Nat.mul_assoc]
  omega

/-- The lower half of a word's cylinder above any physical base is exact. -/
theorem physical_ray {L x y : ℕ} (hxy : x ≤ y) :
    agree L x y ↔ ∃ k, y = x+2^L*k := by
  constructor
  · intro hw
    have hd := (Nat.modEq_iff_dvd' hxy).mp (agree_congruent L x y hw)
    obtain ⟨k,hk⟩ := hd
    exact ⟨k, by omega⟩
  · rintro ⟨k,rfl⟩
    exact same_word L x k

/-- The unit-quotient pair attains the proposed divisor at every cut at once.
    Thus no larger positive divisor is universal for these differences. -/
theorem sharp_simultaneously (L x : ℕ) :
    agree L x (x+2^L) ∧ ∀ j ≤ L, orbit j (x+2^L) - orbit j x = spacing L j x := by
  refine ⟨by simpa using same_word L x 1, ?_⟩
  intro j hj
  have h := cut_value x 1 hj
  simpa using congrArg (· - orbit j x) h

/-- Two cuts and two source displacements have zero two-by-two determinant
    after subtracting each cut's base value. -/
theorem rank_one_cuts {L i j : ℕ} (x a b : ℕ) (hi : i ≤ L) (hj : j ≤ L) :
    (orbit i (x+2^L*a) - orbit i x) * (orbit j (x+2^L*b) - orbit j x) =
    (orbit i (x+2^L*b) - orbit i x) * (orbit j (x+2^L*a) - orbit j x) := by
  simp only [cut_value x a hi, cut_value x b hi, cut_value x a hj,
    cut_value x b hj, Nat.add_sub_cancel_left]
  ring

/-- Simultaneous integer height caps on all cuts restrict one quotient.
    The numerical bound at each cut is exact, including its demand on the base. -/
theorem window_caps (L x k : ℕ) (cap : ℕ → ℕ) :
    (∀ j ≤ L, orbit j (x+2^L*k) ≤ cap j) ↔
    ∀ j ≤ L, orbit j x ≤ cap j ∧ k ≤ (cap j - orbit j x) / spacing L j x := by
  have hpos (j : ℕ) : 0 < spacing L j x := by unfold spacing; positivity
  constructor
  · intro h j hj
    have he := h j hj
    rw [cut_value x k hj] at he
    constructor
    · omega
    · apply (Nat.le_div_iff_mul_le (hpos j)).mpr
      rw [Nat.mul_comm]
      omega
  · intro h j hj
    obtain ⟨hb,hk⟩ := h j hj
    have hm := (Nat.le_div_iff_mul_le (hpos j)).mp hk
    rw [Nat.mul_comm] at hm
    rw [cut_value x k hj]
    omega

#print axioms PhysicalEcho.physical_ray
#print axioms PhysicalEcho.sharp_simultaneously
#print axioms PhysicalEcho.rank_one_cuts
#print axioms PhysicalEcho.window_caps

/-- For the mask 11b on each three-bit block, write integral block boundaries
    as 4y-1. A viable even y is 0 mod 8, a viable odd y is 7 mod 8. -/
theorem mask_block (y : ℕ) (hy : 0 < y) :
    orbit 3 (4*y-1) = (if y%2=0 then 27*y/2-1 else (9*y-1)/2) := by
  simp [orbit, step]
  split <;> split <;> split <;> split <;> omega

theorem mask_block_continues_iff (y : ℕ) (hy : 0 < y) :
    orbit 3 (4*y-1) % 4 = 3 ↔ y%8=0 ∨ y%8=7 := by
  rw [mask_block y hy]
  split <;> omega

theorem mask_even_transport (k : ℕ) (hk : 0 < k) :
    orbit 3 (4*(8*k)-1) = 4*(27*k)-1 := by
  rw [mask_block (8*k) (by omega)]
  split <;> omega

theorem mask_odd_transport (k : ℕ) :
    orbit 3 (4*(8*k+7)-1) = 4*(9*k+8)-1 := by
  rw [mask_block (8*k+7) (by omega)]
  split <;> omega

theorem mask_block_growth (x : ℕ) (hx : x%4 = 3) : x < orbit 3 x := by
  let y := x/4+1
  have hy : 0 < y := by dsimp [y]; omega
  have he : x = 4*y-1 := by dsimp [y]; omega
  rw [he, mask_block y hy]
  split <;> omega

/-- An all-time positive ordinary realization of the mask would exhibit
    increasing physical block heights. -/
theorem mask_escape (x : ℕ) (legal : ∀ k, orbit (3*k) x % 4 = 3) (K : ℕ) :
    x + K ≤ orbit (3*K) x := by
  induction K with
  | zero => simp [orbit]
  | succ k ih =>
    rw [Nat.mul_succ, orbit_add]
    have h := mask_block_growth _ (legal k)
    omega

#print axioms PhysicalEcho.mask_escape
#print axioms PhysicalEcho.mask_block_continues_iff
#print axioms PhysicalEcho.mask_even_transport
#print axioms PhysicalEcho.mask_odd_transport

end PhysicalEcho

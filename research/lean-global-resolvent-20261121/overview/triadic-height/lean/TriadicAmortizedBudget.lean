import TriadicDualClosure
import Mathlib.Data.Nat.Log

/-!
A single integer product amortizes every denominator drop of the literal
triadic complementary trajectory.  This file does not construct a candidate.
The imported paired-step module is unchanged PR178 source at
4e204f54136c79cf8c9393b34e3330594f99ae0a.
-/

set_option autoImplicit false

namespace CollatzTriadicBudget

open CollatzTriadicDual

/-- The full product pays for every possible denominator-level injection. -/
def weight : ℕ → ℤ
  | 0 => 1
  | r + 1 => (1 + 3 ^ r) * weight r

/-- One potential across the signed numerator and all denominator levels. -/
def potential (x w : ℤ) (r : ℕ) : ℤ := x * |w| * weight r

/-- The one initial integer bound, including the zero-numerator candidate. -/
def initialBudget (n a : ℤ) (r : ℕ) : ℤ := n * max 1 |a| * weight r

/-- Literal binary length of the positive initial bound. -/
def binaryBudget (n a : ℤ) (r : ℕ) : ℕ :=
  Nat.log 2 (initialBudget n a r).toNat + 1

theorem weight_pos (r : ℕ) : 0 < weight r := by
  induction r with
  | zero => norm_num [weight]
  | succ r ih =>
    simp only [weight]
    exact mul_pos (by positivity) ih

theorem weight_ge_one (r : ℕ) : 1 ≤ weight r := by
  have := weight_pos r
  omega

theorem potential_pos {x w : ℤ} {r : ℕ}
    (hx : 0 < x) (hw : w ≠ 0) : 0 < potential x w r := by
  exact mul_pos (mul_pos hx (abs_pos.mpr hw)) (weight_pos r)

theorem potential_ge_x {x w : ℤ} {r : ℕ}
    (hx : 0 ≤ x) (hw : w ≠ 0) : x ≤ potential x w r := by
  have ha : 1 ≤ |w| := by have := abs_pos.mpr hw; omega
  have hf := weight_ge_one r
  have hm : 1 ≤ |w| * weight r := by nlinarith
  have hh := mul_le_mul_of_nonneg_left hm hx
  simpa [potential, mul_assoc] using hh

theorem denominator_numerator_bound {w w' : ℤ} {r : ℕ}
    (hw : w ≠ 0) (he : 2 * w' = w + 3 ^ r) :
    2 * |w'| ≤ |w| * (1 + 3 ^ r) := by
  have ha : 1 ≤ |w| := by have := abs_pos.mpr hw; omega
  have hp : 0 ≤ (3 : ℤ) ^ r := by positivity
  have hb : 2 * |w'| = |w + 3 ^ r| := by
    have hh := congrArg abs he
    simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
  have ht := abs_add_le w ((3 : ℤ) ^ r)
  rw [abs_of_nonneg hp] at ht
  have hh := mul_le_mul_of_nonneg_right ha hp
  nlinarith

theorem denominator_potential_quarter {x w x' w' : ℤ} {r : ℕ}
    (hx : 0 ≤ x) (hw : w ≠ 0)
    (ex : 2 * x' = x) (ew : 2 * w' = w + 3 ^ r) :
    4 * potential x' w' r ≤ potential x w (r + 1) := by
  have ha := denominator_numerator_bound hw ew
  have hf : 0 ≤ weight r := le_of_lt (weight_pos r)
  have hh := mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_left ha hx) hf
  calc
    4 * potential x' w' r = x * (2 * |w'|) * weight r := by
      calc
        4 * potential x' w' r = (2 * x') * (2 * |w'|) * weight r := by
          unfold potential; ring
        _ = x * (2 * |w'|) * weight r := by rw [ex]
    _ ≤ x * (|w| * (1 + 3 ^ r)) * weight r := hh
    _ = potential x w (r + 1) := by simp only [potential, weight]; ring

/-- Every nonterminal nonzero step contracts, except for the identified
integral `w=1` tie. The denominator-drop case is uniformly paid here. -/
theorem step_contract_or_tie {x w x' w' : ℤ} {r r' : ℕ}
    (hx : 1 < x) (hw : w ≠ 0)
    (hs : TriadicStep x w r x' w' r') :
    6 * potential x' w' r' ≤ 5 * potential x w r ∨
      (r = 0 ∧ w = 1 ∧ r' = 0 ∧ w' = 2 ∧ 2 * x' = x ∧
        potential x' w' r' = potential x w r) := by
  cases hs with
  | odd ho _ ex ew =>
    left
    have hx3 : 3 ≤ x := by omega
    have ha : 2 * |w'| = |w| := by
      have hh := congrArg abs ew
      simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
    have hp : 4 * potential x' w' r = (3 * x + 1) * |w| * weight r := by
      calc
        4 * potential x' w' r = (2 * x') * (2 * |w'|) * weight r := by
          unfold potential; ring
        _ = (3 * x + 1) * |w| * weight r := by rw [ex, ha]
    have hb : 0 ≤ |w| * weight r := mul_nonneg (abs_nonneg _) (le_of_lt (weight_pos r))
    have hd := mul_nonneg (show 0 ≤ x - 3 by omega) hb
    unfold potential at hp ⊢
    nlinarith
  | evenDen _ _ ex ew =>
    left
    have hb := denominator_potential_quarter (by omega : 0 ≤ x) hw ex ew
    have hp := potential_pos (by omega : 0 < x) hw (r := r' + 1)
    nlinarith
  | evenInt _ ho ex ew =>
    by_cases h1 : w = 1
    · right
      have hw' : w' = 2 := by omega
      refine ⟨rfl, h1, rfl, hw', ex, ?_⟩
      simp only [potential, weight, h1, hw']
      norm_num
      omega
    · left
      have ha : 2 * |w'| = |3 * w + 1| := by
        have hh := congrArg abs ew
        simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
      have hb : 3 * |3 * w + 1| ≤ 10 * |w| := by
        by_cases h : 0 ≤ w
        · have hw3 : 3 ≤ w := by omega
          rw [abs_of_nonneg h, abs_of_nonneg (by omega : 0 ≤ 3 * w + 1)]
          omega
        · rw [abs_of_neg (by omega : w < 0), abs_of_neg (by omega : 3 * w + 1 < 0)]
          omega
      have hh := mul_le_mul_of_nonneg_left hb (by omega : 0 ≤ x)
      have hp : 4 * (x' * |w'|) = x * |3 * w + 1| := by
        calc
          4 * (x' * |w'|) = (2 * x') * (2 * |w'|) := by ring
          _ = x * |3 * w + 1| := by rw [ex, ha]
      simp only [potential, weight, mul_one]
      nlinarith

theorem step_nonincrease {x w x' w' : ℤ} {r r' : ℕ}
    (hx : 1 < x) (hw : w ≠ 0)
    (hs : TriadicStep x w r x' w' r') :
    potential x' w' r' ≤ potential x w r := by
  rcases step_contract_or_tie hx hw hs with hc | ht
  · have hp := potential_pos (by omega : 0 < x) hw (r := r)
    omega
  · exact le_of_eq ht.2.2.2.2.2

theorem step_nonincrease_allow_zero {x w x' w' : ℤ} {r r' : ℕ}
    (hx : 1 < x) (hs : TriadicStep x w r x' w' r') :
    potential x' w' r' ≤ potential x w r := by
  by_cases hw : w = 0
  · rw [hw] at hs ⊢
    have hz := (zero_step hs).1
    simp [potential, hz]
  · exact step_nonincrease hx hw hs

/-- The only tie forces a contracting odd step if its next test passes
and its next ordinary state is nonterminal. -/
theorem two_step_contraction {x w x' w' x'' w'' : ℤ} {r r' r'' : ℕ}
    (hx : 1 < x) (hw : w ≠ 0) (hx' : 1 < x') (hw' : w' ≠ 0)
    (hs : TriadicStep x w r x' w' r')
    (hs' : TriadicStep x' w' r' x'' w'' r'') :
    6 * potential x'' w'' r'' ≤ 5 * potential x w r := by
  rcases step_contract_or_tie hx hw hs with hc | ht
  · have hm := step_nonincrease hx' hw' hs'
    omega
  · rcases step_contract_or_tie hx' hw' hs' with hc' | ht'
    · rw [ht.2.2.2.2.2] at hc'
      exact hc'
    · have htwo := ht.2.2.2.1
      have hone := ht'.2.1
      omega

/-- At zero entry, the same old product bounds the complete ensuing odd-tail
integer. This includes the signed denominator-cancellation crossing. -/
theorem zero_entry_bound {x w x' : ℤ} {r r' : ℕ}
    (hx : 1 < x) (hw : w ≠ 0)
    (hs : TriadicStep x w r x' 0 r') :
    x' + 1 ≤ potential x w r := by
  have hp := potential_ge_x (by omega : 0 ≤ x) hw (r := r)
  cases hs with
  | odd _ _ _ ew => omega
  | evenDen _ _ ex _ => omega
  | evenInt _ _ _ ew => omega

/-- Four two-step contractions halve a nonnegative starting product. -/
theorem eight_step_half {p₀ p₂ p₄ p₆ p₈ : ℤ}
    (hp : 0 ≤ p₀)
    (h₀ : 6 * p₂ ≤ 5 * p₀) (h₂ : 6 * p₄ ≤ 5 * p₂)
    (h₄ : 6 * p₆ ≤ 5 * p₄) (h₆ : 6 * p₈ ≤ 5 * p₆) :
    2 * p₈ ≤ p₀ := by omega

/-- A nonzero nonterminal compatible trajectory cannot consume eight times
the binary-height budget of its one initial weighted product. -/
theorem finite_nonzero_budget (x w : ℕ → ℤ) (r : ℕ → ℕ) (E : ℕ)
    (hx : ∀ i ≤ 8 * E, 1 < x i)
    (hw : ∀ i ≤ 8 * E, w i ≠ 0)
    (hs : ∀ i < 8 * E, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1)))
    (hb : potential (x 0) (w 0) (r 0) < (2 : ℤ) ^ E) : False := by
  let P : ℕ → ℤ := fun i => potential (x i) (w i) (r i)
  have hpos : ∀ i ≤ 8 * E, 0 < P i := by
    intro i hi
    exact potential_pos (by have := hx i hi; omega) (hw i hi)
  have htwo : ∀ i, i + 2 ≤ 8 * E → 6 * P (i + 2) ≤ 5 * P i := by
    intro i hi
    exact two_step_contraction (hx i (by omega)) (hw i (by omega))
      (hx (i + 1) (by omega)) (hw (i + 1) (by omega))
      (hs i (by omega)) (hs (i + 1) (by omega))
  have hpow : ∀ k ≤ E, (2 : ℤ) ^ k * P (8 * k) ≤ P 0 := by
    intro k
    induction k with
    | zero => intro _; simp
    | succ k ih =>
      intro hk
      have hh : 2 * P (8 * (k + 1)) ≤ P (8 * k) := by
        have h₀ := htwo (8 * k) (by omega)
        have h₂ := htwo (8 * k + 2) (by omega)
        have h₄ := htwo (8 * k + 4) (by omega)
        have h₆ := htwo (8 * k + 6) (by omega)
        have hp := hpos (8 * k) (by omega)
        convert eight_step_half (le_of_lt hp) h₀ h₂ h₄ h₆ using 1
      have hh' := mul_le_mul_of_nonneg_left hh (by positivity : 0 ≤ (2 : ℤ) ^ k)
      have hi := ih (by omega)
      rw [pow_succ]
      nlinarith
  have he := hpow E (le_refl E)
  have hp := hpos (8 * E) (le_refl _)
  have hl : 1 ≤ P (8 * E) := by omega
  have hh := mul_le_mul_of_nonneg_left hl (by positivity : 0 ≤ (2 : ℤ) ^ E)
  change P 0 < (2 : ℤ) ^ E at hb
  nlinarith

/-- A finite all-odd original segment forces exactly the required divisibility
of its unchanged initial integer. -/
theorem finite_odd_divisibility (x : ℕ → ℤ) (L : ℕ)
    (hs : ∀ i < L, 2 * x (i + 1) = 3 * x i + 1) :
    (2 : ℤ) ^ L ∣ x 0 + 1 := by
  have h23 : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have hh : ∀ k i : ℕ, i + k ≤ L → (2 : ℤ) ^ k ∣ x i + 1 := by
    intro k
    induction k with
    | zero => intro i _; simp
    | succ k ih =>
      intro i hi
      have hd : (2 : ℤ) ^ (k + 1) ∣ 3 * (x i + 1) := by
        obtain ⟨a, ha⟩ := ih (i + 1) (by omega)
        refine ⟨a, ?_⟩
        rw [pow_succ]
        nlinarith [hs i (by omega)]
      exact h23.pow_left.dvd_of_dvd_mul_left hd
  exact hh L 0 (by omega)

/-- Once zero appears, all later compatible numerator states are zero. -/
theorem finite_zero_persistence (x w : ℕ → ℤ) (r : ℕ → ℕ) (L : ℕ)
    (hzero : w 0 = 0)
    (hs : ∀ i < L, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1))) :
    (∀ i ≤ L, w i = 0) ∧ (2 : ℤ) ^ L ∣ x 0 + 1 := by
  have hz : ∀ i ≤ L, w i = 0 := by
    intro i
    induction i with
    | zero => intro _; exact hzero
    | succ i ih =>
      intro hi
      have h := hs i (by omega)
      rw [ih (by omega)] at h
      exact (zero_step h).1
  refine ⟨hz, finite_odd_divisibility x L ?_⟩
  intro i hi
  have h := hs i hi
  rw [hz i (by omega)] at h
  exact (zero_step h).2

/-- The finite closing theorem, including every signed/zero case. Neither
all-time compatibility nor prior convergence is a premise. -/
theorem finite_paired_horizon (x w : ℕ → ℤ) (r : ℕ → ℕ) (E : ℕ)
    (hx : ∀ i ≤ 9 * E + 1, 0 < x i)
    (hs : ∀ i < 9 * E + 1, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1)))
    (hinit : potential (x 0) (w 0) (r 0) < (2 : ℤ) ^ E)
    (hzeroInit : x 0 + 1 ≤ (2 : ℤ) ^ E) :
    ∃ i ≤ 9 * E + 1, x i = 1 := by
  by_contra hn
  have hx1 : ∀ i ≤ 9 * E + 1, 1 < x i := by
    intro i hi
    have hp := hx i hi
    have he : x i ≠ 1 := by intro he; exact hn ⟨i, hi, he⟩
    omega
  have hz : ∃ j, w j = 0 ∧ j ≤ 8 * E := by
    by_contra hz
    have hw : ∀ i ≤ 8 * E, w i ≠ 0 := by
      intro i hi he
      exact hz ⟨i, he, hi⟩
    exact finite_nonzero_budget x w r E
      (fun i hi => hx1 i (by omega)) hw (fun i hi => hs i (by omega)) hinit
  let j := Nat.find hz
  have hj : w j = 0 ∧ j ≤ 8 * E := Nat.find_spec hz
  have hfirst : ∀ i < j, w i ≠ 0 := by
    intro i hi he
    have hm := Nat.find_min' hz (show w i = 0 ∧ i ≤ 8 * E from ⟨he, by omega⟩)
    change j ≤ i at hm
    omega
  have hmono : ∀ i ≤ 9 * E + 1,
      potential (x i) (w i) (r i) ≤ potential (x 0) (w 0) (r 0) := by
    intro i
    induction i with
    | zero => intro _; exact le_refl _
    | succ i ih =>
      intro hi
      exact le_trans (step_nonincrease_allow_zero (hx1 i (by omega))
        (hs i (by omega))) (ih (by omega))
  have hjBound : x j + 1 ≤ (2 : ℤ) ^ E := by
    by_cases hj0 : j = 0
    · simpa [hj0] using hzeroInit
    · have hj1 : 1 ≤ j := by omega
      have hp := hs (j - 1) (by omega)
      rw [Nat.sub_add_cancel hj1, hj.1] at hp
      have hb := zero_entry_bound (hx1 (j - 1) (by omega))
        (hfirst (j - 1) (by omega)) hp
      have hm := hmono (j - 1) (by omega)
      omega
  have htail := finite_zero_persistence (fun i => x (j + i))
    (fun i => w (j + i)) (fun i => r (j + i)) (E + 1)
    (by simpa using hj.1) (by
      intro i hi
      have h := hs (j + i) (by omega)
      simpa [Nat.add_assoc] using h)
  have hd : (2 : ℤ) ^ (E + 1) ∣ x j + 1 := by simpa using htail.2
  have hlarge := Int.le_of_dvd (by have := hx j (by omega); omega : 0 < x j + 1) hd
  have hp : 0 < (2 : ℤ) ^ E := by positivity
  rw [pow_succ] at hlarge
  omega

/-- Literal finite candidates inherit the horizon theorem. The two explicit
height inequalities are discharged by the proposed binary-length budget. -/
theorem finite_candidate_reaches_one (n a : ℤ) (r E : ℕ)
    (hn : 0 < n)
    (hP : potential n a r < (2 : ℤ) ^ E)
    (hnSize : n + 1 ≤ (2 : ℤ) ^ E)
    (hc : ∀ k < 9 * E + 1, compatible (trajectory ⟨n, a, r⟩ k)) :
    ∃ k ≤ 9 * E + 1, orbit n k = 1 := by
  let s : ℕ → State := trajectory ⟨n, a, r⟩
  have hp : ∀ i ≤ 9 * E + 1, 0 < (s i).x := by
    intro i _
    change 0 < (trajectory ⟨n, a, r⟩ i).x
    rw [trajectory_x]
    exact orbit_pos hn i
  have hs : ∀ i < 9 * E + 1, TriadicStep (s i).x (s i).w (s i).r
      (s (i + 1)).x (s (i + 1)).w (s (i + 1)).r := by
    intro i hi
    exact next_step (s i) (hc i hi)
  obtain ⟨k, hk, he⟩ := finite_paired_horizon
    (fun i => (s i).x) (fun i => (s i).w) (fun i => (s i).r) E
    hp hs hP hnSize
  refine ⟨k, hk, ?_⟩
  simpa only [s, trajectory_x] using he

theorem initialBudget_pos {n a : ℤ} {r : ℕ} (hn : 0 < n) :
    0 < initialBudget n a r := by
  have hm : 0 < max (1 : ℤ) |a| := lt_of_lt_of_le (by norm_num) (le_max_left _ _)
  exact mul_pos (mul_pos hn hm) (weight_pos r)

theorem initialBudget_ge_n {n a : ℤ} {r : ℕ} (hn : 0 ≤ n) :
    n ≤ initialBudget n a r := by
  have hm : 1 ≤ max (1 : ℤ) |a| := le_max_left _ _
  have hf := weight_ge_one r
  have hh : 1 ≤ max (1 : ℤ) |a| * weight r := by nlinarith
  have hb := mul_le_mul_of_nonneg_left hh hn
  simpa [initialBudget, mul_assoc] using hb

theorem initialBudget_ge_potential {n a : ℤ} {r : ℕ} (hn : 0 ≤ n) :
    potential n a r ≤ initialBudget n a r := by
  have hh := mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_left (le_max_right (1 : ℤ) |a|) hn)
    (le_of_lt (weight_pos r))
  exact hh

theorem binaryBudget_covers {n a : ℤ} {r : ℕ} (hn : 0 < n) :
    initialBudget n a r < (2 : ℤ) ^ binaryBudget n a r := by
  have hp := initialBudget_pos (a := a) (r := r) hn
  have hc : ((initialBudget n a r).toNat : ℤ) = initialBudget n a r :=
    Int.toNat_of_nonneg (le_of_lt hp)
  have hh := Nat.lt_pow_succ_log_self (by norm_num : 1 < (2 : ℕ))
    (initialBudget n a r).toNat
  have hh' : ((initialBudget n a r).toNat : ℤ) <
      (2 : ℤ) ^ (Nat.log 2 (initialBudget n a r).toNat + 1) := by
    exact_mod_cast hh
  simpa only [hc, binaryBudget] using hh'

/-- Fully explicit finite candidate theorem: the only candidate premise is
the first `9*bl(n*max(1,|a|)*F(r))+1` literal parity tests. -/
theorem finite_triadic_height_certificate (n a : ℤ) (r : ℕ)
    (hn : 0 < n)
    (hc : ∀ k < 9 * binaryBudget n a r + 1,
      compatible (trajectory ⟨n, a, r⟩ k)) :
    ∃ k ≤ 9 * binaryBudget n a r + 1, orbit n k = 1 := by
  have hb := binaryBudget_covers (a := a) (r := r) hn
  have hp := initialBudget_ge_potential (a := a) (r := r) (le_of_lt hn)
  have hx := initialBudget_ge_n (a := a) (r := r) (le_of_lt hn)
  exact finite_candidate_reaches_one n a r (binaryBudget n a r)
    hn (by omega) (by omega) hc

end CollatzTriadicBudget

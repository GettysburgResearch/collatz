import TriadicAmortizedBudget

set_option autoImplicit false

namespace CollatzTriadicRigidity

open CollatzTriadicDual CollatzTriadicBudget

theorem weight_mono : Monotone weight := by
  intro i j hij
  induction j with
  | zero =>
    have hi : i = 0 := by omega
    simp [hi]
  | succ j ih =>
    by_cases h : i ≤ j
    · apply le_trans (ih h)
      have hp : 0 ≤ (3 : ℤ) ^ j := by positivity
      have hf := weight_pos j
      simp only [weight]
      nlinarith [mul_nonneg hp (le_of_lt hf)]
    · have hi : i = j + 1 := by omega
      simp [hi]

theorem weight_covers_power (r : ℕ) : 1 + (3 : ℤ) ^ r ≤ 2 * weight r := by
  induction r with
  | zero => norm_num [weight]
  | succ r ih =>
    have hp : 1 ≤ (3 : ℤ) ^ r := by
      have hpos : 0 < (3 : ℤ) ^ r := by positivity
      omega
    have hh := mul_le_mul_of_nonneg_left ih (by positivity : 0 ≤ 1 + (3 : ℤ) ^ r)
    simp only [weight, pow_succ]
    nlinarith [mul_nonneg (show 0 ≤ (3 : ℤ) ^ r - 1 by omega) (show 0 ≤ (3 : ℤ) ^ r by positivity)]

theorem step_exponent_le {x w x' w' : ℤ} {r r' : ℕ}
    (hs : TriadicStep x w r x' w' r') : r' ≤ r := by
  cases hs <;> omega

/-- The zero-tail reserve forces the ordinary hit before the nonzero
budget is exhausted; it is not spent delaying the hit itself. -/
theorem finite_early_hit (x w : ℕ → ℤ) (r : ℕ → ℕ) (E : ℕ)
    (hx : ∀ i ≤ 9 * E + 1, 0 < x i)
    (hs : ∀ i < 9 * E + 1, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1)))
    (hinit : potential (x 0) (w 0) (r 0) < (2 : ℤ) ^ E)
    (hzeroInit : x 0 + 1 ≤ (2 : ℤ) ^ E) :
    ∃ i ≤ 8 * E, x i = 1 := by
  by_contra hn
  have hx1 : ∀ i ≤ 8 * E, 1 < x i := by
    intro i hi
    have hp := hx i (by omega)
    have he : x i ≠ 1 := by intro he; exact hn ⟨i, hi, he⟩
    omega
  have hz : ∃ j, w j = 0 ∧ j ≤ 8 * E := by
    by_contra hz
    have hw : ∀ i ≤ 8 * E, w i ≠ 0 := by
      intro i hi he
      exact hz ⟨i, he, hi⟩
    exact finite_nonzero_budget x w r E hx1 hw
      (fun i hi => hs i (by omega)) hinit
  let j := Nat.find hz
  have hj : w j = 0 ∧ j ≤ 8 * E := Nat.find_spec hz
  have hfirst : ∀ i < j, w i ≠ 0 := by
    intro i hi he
    have hm := Nat.find_min' hz (show w i = 0 ∧ i ≤ 8 * E from ⟨he, by omega⟩)
    change j ≤ i at hm
    omega
  have hmono : ∀ i ≤ 8 * E,
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

def cycleDefect (x w : ℤ) (r : ℕ) : ℤ := w - (3 - x) * 3 ^ r

theorem cycle_step_defect {x w x' w' : ℤ} {r r' : ℕ}
    (hx : x = 1 ∨ x = 2) (hs : TriadicStep x w r x' w' r') :
    (x' = 1 ∨ x' = 2) ∧
    (2 * cycleDefect x' w' r' = cycleDefect x w r ∨
      2 * cycleDefect x' w' r' = 3 * cycleDefect x w r) := by
  cases hs with
  | odd ho _ ex ew =>
    have h1 : x = 1 := by omega
    have h2 : x' = 2 := by omega
    refine ⟨Or.inr h2, Or.inl ?_⟩
    simp only [cycleDefect, h1, h2]
    nlinarith
  | evenDen he _ ex ew =>
    have h2 : x = 2 := by omega
    have h1 : x' = 1 := by omega
    refine ⟨Or.inl h1, Or.inl ?_⟩
    simp only [cycleDefect, h1, h2, pow_succ]
    nlinarith
  | evenInt he _ ex ew =>
    have h2 : x = 2 := by omega
    have h1 : x' = 1 := by omega
    refine ⟨Or.inl h1, Or.inr ?_⟩
    simp only [cycleDefect, h1, h2, pow_zero]
    nlinarith

/-- A finite complementary match to the 1,2 cycle forces dyadic
divisibility of the exact numerator difference from its standard dual. -/
theorem finite_cycle_divisibility (x w : ℕ → ℤ) (r : ℕ → ℕ) (L : ℕ)
    (hx0 : x 0 = 1 ∨ x 0 = 2)
    (hs : ∀ i < L, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1))) :
    (2 : ℤ) ^ L ∣ cycleDefect (x 0) (w 0) (r 0) := by
  have hc : ∀ i ≤ L, x i = 1 ∨ x i = 2 := by
    intro i
    induction i with
    | zero => intro _; exact hx0
    | succ i ih =>
      intro hi
      exact (cycle_step_defect (ih (by omega)) (hs i (by omega))).1
  have h23 : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have hh : ∀ k i : ℕ, i + k ≤ L →
      (2 : ℤ) ^ k ∣ cycleDefect (x i) (w i) (r i) := by
    intro k
    induction k with
    | zero => intro i _; simp
    | succ k ih =>
      intro i hi
      obtain ⟨a, ha⟩ := ih (i + 1) (by omega)
      rcases (cycle_step_defect (hc i (by omega)) (hs i (by omega))).2 with he | he
      · refine ⟨a, ?_⟩
        rw [pow_succ]
        nlinarith
      · have hd : (2 : ℤ) ^ (k + 1) ∣ 3 * cycleDefect (x i) (w i) (r i) := by
          refine ⟨a, ?_⟩
          rw [pow_succ]
          nlinarith
        exact h23.pow_left.dvd_of_dvd_mul_left hd
  exact hh L 0 (by omega)

theorem cycle_defect_bound {w B : ℤ} {r : ℕ}
    (hpot : |w| * weight r ≤ B) (hweight : 2 * weight r ≤ B) :
    |w - 2 * (3 : ℤ) ^ r| ≤ 2 * B := by
  have hf := weight_pos r
  have hb : 0 ≤ B := by omega
  have hp : 0 ≤ (3 : ℤ) ^ r := by positivity
  have hw := weight_covers_power r
  have h1 := mul_le_mul_of_nonneg_right hweight hp
  have h2 := mul_le_mul_of_nonneg_left hw hb
  have hm : (|w| + 2 * (3 : ℤ) ^ r) * weight r ≤ (2 * B) * weight r := by
    nlinarith
  have hl : |w| + 2 * (3 : ℤ) ^ r ≤ 2 * B := by nlinarith
  have ht : |w - 2 * (3 : ℤ) ^ r| ≤ |w| + 2 * (3 : ℤ) ^ r := by
    have hh := abs_add_le w (-(2 * (3 : ℤ) ^ r))
    simpa only [sub_eq_add_neg, abs_neg,
      abs_of_nonneg (by positivity : 0 ≤ 2 * (3 : ℤ) ^ r)] using hh
  exact le_trans ht hl

theorem int_zero_of_dvd_of_abs_lt {d M : ℤ} (_hM : 0 < M)
    (hd : M ∣ d) (hb : |d| < M) : d = 0 := by
  by_contra hz
  have ha : 0 < |d| := abs_pos.mpr hz
  have hdabs : M ∣ |d| := by
    rcases le_or_gt 0 d with h | h
    · simpa [abs_of_nonneg h] using hd
    · simpa [abs_of_neg h] using dvd_neg.mpr hd
  have hm := Int.le_of_dvd ha hdabs
  omega

/-- An H-prefix with the two explicit initial height bounds already hits
the exact standard paired cycle by 8E. -/
theorem finite_paired_rigidity (x w : ℕ → ℤ) (r : ℕ → ℕ) (E : ℕ) (B : ℤ)
    (hx : ∀ i ≤ 9 * E + 1, 0 < x i)
    (hs : ∀ i < 9 * E + 1, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1)))
    (hpot : potential (x 0) (w 0) (r 0) ≤ B)
    (hb : B < (2 : ℤ) ^ E)
    (hweight : 2 * weight (r 0) ≤ B)
    (hzeroInit : x 0 + 1 ≤ (2 : ℤ) ^ E) :
    ∃ i ≤ 8 * E, x i = 1 ∧ w i = 2 * (3 : ℤ) ^ r i := by
  have hex : ∃ i, i ≤ 8 * E ∧ x i = 1 :=
    finite_early_hit x w r E hx hs (lt_of_le_of_lt hpot hb) hzeroInit
  let t := Nat.find hex
  have ht : t ≤ 8 * E ∧ x t = 1 := Nat.find_spec hex
  have hfirst : ∀ i < t, 1 < x i := by
    intro i hi
    have hp := hx i (by omega)
    have hn : x i ≠ 1 := by
      intro he
      have hm := Nat.find_min' hex (show i ≤ 8 * E ∧ x i = 1 from ⟨by omega, he⟩)
      change t ≤ i at hm
      omega
    omega
  have hmono : ∀ i ≤ t,
      potential (x i) (w i) (r i) ≤ potential (x 0) (w 0) (r 0) := by
    intro i
    induction i with
    | zero => intro _; exact le_refl _
    | succ i ih =>
      intro hi
      exact le_trans (step_nonincrease_allow_zero (hfirst i (by omega))
        (hs i (by omega))) (ih (by omega))
  have hr : ∀ i ≤ t, r i ≤ r 0 := by
    intro i
    induction i with
    | zero => intro _; exact le_refl _
    | succ i ih =>
      intro hi
      exact le_trans (step_exponent_le (hs i (by omega))) (ih (by omega))
  have hwt : 2 * weight (r t) ≤ B := by
    have hh := weight_mono (hr t (le_refl _))
    omega
  have hpt : |w t| * weight (r t) ≤ B := by
    have hh := le_trans (hmono t (le_refl _)) hpot
    simpa only [potential, ht.2, one_mul] using hh
  have hbound := cycle_defect_bound hpt hwt
  have hd := finite_cycle_divisibility (fun i => x (t + i))
    (fun i => w (t + i)) (fun i => r (t + i)) (E + 1)
    (Or.inl (by simpa using ht.2)) (by
      intro i hi
      have h := hs (t + i) (by omega)
      simpa [Nat.add_assoc] using h)
  have hd' : (2 : ℤ) ^ (E + 1) ∣ w t - 2 * (3 : ℤ) ^ r t := by
    simpa [cycleDefect, ht.2] using hd
  have hb' : |w t - 2 * (3 : ℤ) ^ r t| < (2 : ℤ) ^ (E + 1) := by
    rw [pow_succ]
    omega
  have hz := int_zero_of_dvd_of_abs_lt (by positivity : 0 < (2 : ℤ) ^ (E + 1)) hd' hb'
  exact ⟨t, ht.1, ht.2, by omega⟩

theorem initial_two_tests_budget {n a : ℤ} {r : ℕ}
    (hn : 0 < n)
    (h0 : compatible (trajectory ⟨n, a, r⟩ 0))
    (h1 : compatible (trajectory ⟨n, a, r⟩ 1)) :
    2 * weight r ≤ initialBudget n a r := by
  have hm : 1 ≤ max (1 : ℤ) |a| := le_max_left _ _
  have hf := weight_pos r
  by_cases hn1 : n = 1
  · have haeven : a % 2 = 0 := by
      change (n + a) % 2 = 1 at h0
      omega
    have ha0 : a ≠ 0 := by
      intro he
      simp [trajectory, next, compatible, hn1, he] at h1
    have ha2 : 2 ≤ |a| := by
      rcases le_or_gt 0 a with ha | ha
      · rw [abs_of_nonneg ha]
        omega
      · rw [abs_of_neg ha]
        omega
    have hm2 : 2 ≤ max (1 : ℤ) |a| := le_trans ha2 (le_max_right _ _)
    simp only [initialBudget, hn1, one_mul]
    exact mul_le_mul_of_nonneg_right hm2 (le_of_lt hf)
  · have hn2 : 2 ≤ n := by omega
    have hh := mul_le_mul_of_nonneg_left hm (le_of_lt hn)
    have hm2 : 2 ≤ n * max (1 : ℤ) |a| := by nlinarith
    exact mul_le_mul_of_nonneg_right hm2 (le_of_lt hf)

/-- The exact supplied finite candidate reaches the standard paired cycle,
not merely an original hit of one, at the earlier 8E clock. -/
theorem finite_triadic_exact_pair (n a : ℤ) (r : ℕ)
    (hn : 0 < n)
    (hc : ∀ k < 9 * binaryBudget n a r + 1,
      compatible (trajectory ⟨n, a, r⟩ k)) :
    ∃ k ≤ 8 * binaryBudget n a r,
      (trajectory ⟨n, a, r⟩ k).x = 1 ∧
      (trajectory ⟨n, a, r⟩ k).w =
        2 * (3 : ℤ) ^ (trajectory ⟨n, a, r⟩ k).r := by
  let E := binaryBudget n a r
  let B := initialBudget n a r
  let s : ℕ → State := trajectory ⟨n, a, r⟩
  have hE : 1 ≤ E := by simp only [E, binaryBudget]; omega
  have hb : B < (2 : ℤ) ^ E := binaryBudget_covers hn
  have hp : potential n a r ≤ B := initialBudget_ge_potential (le_of_lt hn)
  have hnB : n ≤ B := initialBudget_ge_n (le_of_lt hn)
  have hwB : 2 * weight r ≤ B :=
    initial_two_tests_budget hn (hc 0 (by omega)) (hc 1 (by omega))
  have hx : ∀ i ≤ 9 * E + 1, 0 < (s i).x := by
    intro i _
    change 0 < (trajectory ⟨n, a, r⟩ i).x
    rw [trajectory_x]
    exact orbit_pos hn i
  have hs : ∀ i < 9 * E + 1, TriadicStep (s i).x (s i).w (s i).r
      (s (i + 1)).x (s (i + 1)).w (s (i + 1)).r := by
    intro i hi
    exact next_step (s i) (hc i hi)
  exact finite_paired_rigidity (fun i => (s i).x) (fun i => (s i).w)
    (fun i => (s i).r) E B hx hs hp hb hwB (by change n + 1 ≤ (2 : ℤ) ^ E; omega)

def exactCycle (s : State) : Prop :=
  (s.x = 1 ∧ s.w = 2 * (3 : ℤ) ^ s.r) ∨
  (s.x = 2 ∧ s.w = (3 : ℤ) ^ s.r)

theorem exactCycle_compatible {s : State} (h : exactCycle s) : compatible s := by
  have h3 : (3 : ℤ) ^ s.r % 2 = 1 :=
    Int.odd_iff.mp (Odd.pow (by norm_num : Odd (3 : ℤ)))
  rcases h with ⟨hx, hw⟩ | ⟨hx, hw⟩ <;>
    unfold compatible <;> rw [hx, hw] <;> omega

theorem exactCycle_next {s : State} (h : exactCycle s) : exactCycle (next s) := by
  have hx : s.x = 1 ∨ s.x = 2 := h.elim (fun h => Or.inl h.1) (fun h => Or.inr h.1)
  have hd : cycleDefect s.x s.w s.r = 0 := by
    rcases h with ⟨hx, hw⟩ | ⟨hx, hw⟩ <;> simp [cycleDefect, hx, hw]
  have hs := cycle_step_defect hx (next_step s (exactCycle_compatible h))
  have hd' : cycleDefect (next s).x (next s).w (next s).r = 0 := by
    rcases hs.2 with he | he <;> rw [hd] at he <;> omega
  rcases hs.1 with hx' | hx'
  · left
    refine ⟨hx', ?_⟩
    simp only [cycleDefect, hx'] at hd'
    omega
  · right
    refine ⟨hx', ?_⟩
    simp only [cycleDefect, hx'] at hd'
    omega

/-- A successful own-height prefix proves all-time compatibility of this
same unchanged signed triadic candidate. No new candidate is chosen. -/
theorem finite_certificate_alltime (n a : ℤ) (r : ℕ)
    (hn : 0 < n)
    (hc : ∀ k < 9 * binaryBudget n a r + 1,
      compatible (trajectory ⟨n, a, r⟩ k)) :
    ∀ k, compatible (trajectory ⟨n, a, r⟩ k) := by
  obtain ⟨t, ht, hx, hw⟩ := finite_triadic_exact_pair n a r hn hc
  let s : ℕ → State := trajectory ⟨n, a, r⟩
  have hf : ∀ j, exactCycle (s (t + j)) := by
    intro j
    induction j with
    | zero => exact Or.inl ⟨hx, hw⟩
    | succ j ih =>
      have hh := exactCycle_next ih
      have heq : t + (j + 1) = (t + j) + 1 := by omega
      rw [heq]
      exact hh
  intro k
  by_cases hk : k < t
  · exact hc k (by omega)
  · have htk : t ≤ k := by omega
    have hh := hf (k - t)
    rw [Nat.add_sub_of_le htk] at hh
    exact exactCycle_compatible hh

theorem finite_certificate_iff_alltime (n a : ℤ) (r : ℕ) (hn : 0 < n) :
    (∀ k < 9 * binaryBudget n a r + 1,
      compatible (trajectory ⟨n, a, r⟩ k)) ↔
    (∀ k, compatible (trajectory ⟨n, a, r⟩ k)) := by
  exact ⟨finite_certificate_alltime n a r hn, fun h k _ => h k⟩

end CollatzTriadicRigidity

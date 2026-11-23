import Mathlib.Tactic
import Mathlib.Order.WellFounded
import Mathlib.RingTheory.Coprime.Basic

/-!
A complete well-founded closing implication for a supplied all-time triadic
parity dual. The existence of that dual is not assumed as an axiom or proved.
The ordinary coordinate and the signed numerator are integers throughout.
-/

namespace CollatzTriadicDual

/-- A complementary parity step with the denominator written as `3^r`.
The second constructor cancels one factor of three, including when the
fraction was not in lowest terms. -/
inductive TriadicStep : ℤ → ℤ → ℕ → ℤ → ℤ → ℕ → Prop
  | odd {x w x' w' : ℤ} {r : ℕ}
      (hx : x % 2 = 1) (hw : w % 2 = 0)
      (ex : 2 * x' = 3 * x + 1) (ew : 2 * w' = w) :
      TriadicStep x w r x' w' r
  | evenDen {x w x' w' : ℤ} {r : ℕ}
      (hx : x % 2 = 0) (hw : w % 2 = 1)
      (ex : 2 * x' = x) (ew : 2 * w' = w + 3 ^ r) :
      TriadicStep x w (r + 1) x' w' r
  | evenInt {x w x' w' : ℤ}
      (hx : x % 2 = 0) (hw : w % 2 = 1)
      (ex : 2 * x' = x) (ew : 2 * w' = 3 * w + 1) :
      TriadicStep x w 0 x' w' 0

/-- The denominator-canceling integer rules are exactly the complementary
rational Collatz branches. -/
theorem step_rational {x w x' w' : ℤ} {r r' : ℕ}
    (h : TriadicStep x w r x' w' r') :
    (w' : ℚ) / 3 ^ r' =
      if x % 2 = 0 then (3 * ((w : ℚ) / 3 ^ r) + 1) / 2
      else ((w : ℚ) / 3 ^ r) / 2 := by
  cases h with
  | odd hx _ _ ew =>
    have hx0 : x % 2 ≠ 0 := by omega
    simp only [hx0, ite_false]
    have hq : 2 * (w' : ℚ) = w := by exact_mod_cast ew
    have h3 : (3 : ℚ) ^ r ≠ 0 := pow_ne_zero _ (by norm_num)
    field_simp
    nlinarith
  | evenDen hx _ _ ew =>
    simp only [hx, ite_true, pow_succ]
    have hq : 2 * (w' : ℚ) = w + (3 : ℚ) ^ r' := by exact_mod_cast ew
    field_simp
    nlinarith
  | evenInt hx _ _ ew =>
    simp only [hx, ite_true, pow_zero, div_one]
    have hq : 2 * (w' : ℚ) = 3 * w + 1 := by exact_mod_cast ew
    linarith

/-- A positive ordinary integer cannot have an all-odd infinite tail.
The proof retains the fixed original integer and uses divisibility by every
power of two, rather than a bounded-prefix search. -/
theorem no_all_odd (x : ℕ → ℤ) (hpos : 0 < x 0)
    (hstep : ∀ i, 2 * x (i + 1) = 3 * x i + 1) : False := by
  have h23 : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have hpow : ∀ k i : ℕ, (2 : ℤ) ^ k ∣ x i + 1 := by
    intro k
    induction k with
    | zero => intro i; simp
    | succ k ih =>
      intro i
      have hd : (2 : ℤ) ^ (k + 1) ∣ 3 * (x i + 1) := by
        obtain ⟨a, ha⟩ := ih (i + 1)
        refine ⟨a, ?_⟩
        rw [pow_succ]
        nlinarith [hstep i]
      exact h23.pow_left.dvd_of_dvd_mul_left hd
  let k := (x 0 + 1).toNat
  have hk : (k : ℤ) = x 0 + 1 := Int.toNat_of_nonneg (by omega)
  have hsmall : (2 : ℤ) ^ k ≤ x 0 + 1 :=
    Int.le_of_dvd (by omega) (hpow k 0)
  have hbig : (k : ℤ) < (2 : ℤ) ^ k := by
    exact_mod_cast (Nat.lt_two_pow_self (n := k))
  omega

/-- A zero numerator forces the odd branch and remains zero. -/
theorem zero_step {x x' w' : ℤ} {r r' : ℕ}
    (h : TriadicStep x 0 r x' w' r') :
    w' = 0 ∧ 2 * x' = 3 * x + 1 := by
  cases h with
  | odd _ _ ex ew => exact ⟨by omega, ex⟩
  | evenDen _ hw _ _ => norm_num at hw
  | evenInt _ hw _ _ => norm_num at hw

/-- Every numerator of an all-time positive complementary path is nonzero. -/
theorem numerator_ne_zero (x w : ℕ → ℤ) (r : ℕ → ℕ)
    (hpos : ∀ i, 0 < x i)
    (hstep : ∀ i, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1))) :
    ∀ i, w i ≠ 0 := by
  intro i hi
  have hz : ∀ k : ℕ, w (i + k) = 0 := by
    intro k
    induction k with
    | zero => simpa using hi
    | succ k ih =>
      have hs := hstep (i + k)
      rw [ih] at hs
      simpa [Nat.add_assoc] using (zero_step hs).1
  apply no_all_odd (fun k => x (i + k)) (by simpa using hpos i)
  intro k
  have hs := hstep (i + k)
  rw [hz k] at hs
  simpa [Nat.add_assoc] using (zero_step hs).2

/-- Twice the signed-numerator product, with a tie breaker for `w=1`. -/
def energy (x w : ℤ) : ℕ :=
  (2 * (x * |w|) + if w = 1 then 1 else 0).toNat

private theorem marker_bounds (w : ℤ) :
    (0 : ℤ) ≤ (if w = 1 then 1 else 0) ∧
    (if w = 1 then 1 else 0 : ℤ) ≤ 1 := by
  split_ifs <;> omega

private theorem energy_lt_of_product_lt {x w x' w' : ℤ}
    (hx : 0 < x) (hw : w ≠ 0)
    (hp : x' * |w'| < x * |w|) :
    energy x' w' < energy x w := by
  have habs : 0 < |w| := abs_pos.mpr hw
  have hP : 0 < x * |w| := mul_pos hx habs
  have hm := marker_bounds w
  have hm' := marker_bounds w'
  unfold energy
  apply (Int.toNat_lt_toNat (by omega)).mpr
  omega

private theorem odd_product_lt {x w x' w' : ℤ}
    (hx : 1 < x) (hw : w ≠ 0)
    (ex : 2 * x' = 3 * x + 1) (ew : 2 * w' = w) :
    x' * |w'| < x * |w| := by
  have ea : 2 * |w'| = |w| := by
    have hh := congrArg abs ew
    simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
  have ep : 4 * (x' * |w'|) = (3 * x + 1) * |w| := by
    calc
      4 * (x' * |w'|) = (2 * x') * (2 * |w'|) := by ring
      _ = (3 * x + 1) * |w| := by rw [ex, ea]
  have habs : 0 < |w| := abs_pos.mpr hw
  have hd : 0 < (x - 1) * |w| := mul_pos (by omega) habs
  nlinarith

private theorem even_product_lt {x w x' w' : ℤ}
    (hx : 0 < x) (_hw : w ≠ 0) (hw1 : w ≠ 1)
    (ex : 2 * x' = x) (ew : 2 * w' = 3 * w + 1) :
    x' * |w'| < x * |w| := by
  have ea : 2 * |w'| = |3 * w + 1| := by
    have hh := congrArg abs ew
    simpa only [abs_mul, show |(2 : ℤ)| = 2 by norm_num] using hh
  have ep : 4 * (x' * |w'|) = x * |3 * w + 1| := by
    calc
      4 * (x' * |w'|) = (2 * x') * (2 * |w'|) := by ring
      _ = x * |3 * w + 1| := by rw [ex, ea]
  have hd : |3 * w + 1| < 4 * |w| := by
    by_cases h : 0 ≤ w
    · rw [abs_of_nonneg h, abs_of_nonneg (by omega : 0 ≤ 3 * w + 1)]
      omega
    · rw [abs_of_neg (by omega : w < 0),
        abs_of_neg (by omega : 3 * w + 1 < 0)]
      omega
  have hh := mul_lt_mul_of_pos_left hd hx
  nlinarith

/-- The complete rank decreases in every nonterminal, nonzero paired step.
The denominator exponent is the first coordinate; this is not a bounded
word grammar or an assumed drift estimate. -/
theorem step_rank {x w x' w' : ℤ} {r r' : ℕ}
    (hx : 1 < x) (hw : w ≠ 0)
    (h : TriadicStep x w r x' w' r') :
    Prod.Lex (· < ·) (· < ·) (r', energy x' w') (r, energy x w) := by
  cases h with
  | odd _ _ ex ew =>
    apply Prod.Lex.right
    exact energy_lt_of_product_lt (by omega) hw (odd_product_lt hx hw ex ew)
  | evenDen _ _ _ _ =>
    apply Prod.Lex.left
    omega
  | evenInt _ _ ex ew =>
    apply Prod.Lex.right
    by_cases h1 : w = 1
    · subst w
      have hw' : w' = 2 := by omega
      subst w'
      unfold energy
      norm_num
      omega
    · exact energy_lt_of_product_lt (by omega) hw
        (even_product_lt (by omega) hw h1 ex ew)

/-- A supplied all-time triadic parity dual forces the positive ordinary
coordinate to reach one. No absence-of-cycles assumption is needed. -/
theorem triadic_pair_reaches_one (x w : ℕ → ℤ) (r : ℕ → ℕ)
    (hpos : ∀ i, 0 < x i)
    (hstep : ∀ i, TriadicStep (x i) (w i) (r i)
      (x (i + 1)) (w (i + 1)) (r (i + 1))) :
    ∃ i, x i = 1 := by
  by_contra hn
  have hn' : ∀ i, x i ≠ 1 := by simpa using hn
  have hw := numerator_ne_zero x w r hpos hstep
  let f : ℕ → ℕ × ℕ := fun i => (r i, energy (x i) (w i))
  have hd : ∀ i, Prod.Lex (· < ·) (· < ·) (f (i + 1)) (f i) := by
    intro i
    exact step_rank (by have := hpos i; have := hn' i; omega) (hw i) (hstep i)
  have hf : WellFounded (Prod.Lex (· < ·) (· < ·) :
      (ℕ × ℕ) → (ℕ × ℕ) → Prop) :=
    Nat.lt_wfRel.wf.prod_lex Nat.lt_wfRel.wf
  exact (wellFounded_iff_isEmpty_descending_chain.mp hf).false ⟨f, hd⟩


/-- Ordinary shortcut Collatz on signed integers; the theorem uses positive inputs. -/
def shortcut (x : ℤ) : ℤ :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

/-- The literal ordinary shortcut orbit, with no stopping-time oracle. -/
def orbit (n : ℤ) : ℕ → ℤ
  | 0 => n
  | k + 1 => shortcut (orbit n k)

/-- Finite initial data for a possible triadic dual. -/
structure State where
  x : ℤ
  w : ℤ
  r : ℕ

/-- Deterministic numerator evolution. Parity compatibility is checked separately. -/
def next (s : State) : State :=
  if s.x % 2 = 0 then
    match s.r with
    | 0 => ⟨s.x / 2, (3 * s.w + 1) / 2, 0⟩
    | r + 1 => ⟨s.x / 2, (s.w + 3 ^ r) / 2, r⟩
  else ⟨(3 * s.x + 1) / 2, s.w / 2, s.r⟩

/-- The trajectory generated from one unchanged finite candidate. -/
def trajectory (s : State) : ℕ → State
  | 0 => s
  | k + 1 => next (trajectory s k)

/-- Opposite parity of the ordinary coordinate and the numerator. -/
def compatible (s : State) : Prop := (s.x + s.w) % 2 = 1

/-- The stored ordinary coordinate is exactly one ordinary shortcut step. -/
theorem next_x (s : State) : (next s).x = shortcut s.x := by
  unfold next shortcut
  split_ifs <;> simp_all
  cases s.r <;> rfl

/-- The first coordinate remains the original ordinary orbit at every clock. -/
theorem trajectory_x (s : State) (k : ℕ) :
    (trajectory s k).x = orbit s.x k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    simp only [trajectory, orbit, next_x, ih]

/-- Literal positive ordinary inputs stay positive under the shortcut map. -/
theorem shortcut_pos {x : ℤ} (hx : 0 < x) : 0 < shortcut x := by
  unfold shortcut
  split_ifs with h <;> omega

/-- Positivity here follows from the actual ordinary map, not from a dual hypothesis. -/
theorem orbit_pos {n : ℤ} (hn : 0 < n) (k : ℕ) : 0 < orbit n k := by
  induction k with
  | zero => exact hn
  | succ k ih => exact shortcut_pos ih

/-- One passed parity test gives the exact denominator-canceling paired step. -/
theorem next_step (s : State) (h : compatible s) :
    TriadicStep s.x s.w s.r (next s).x (next s).w (next s).r := by
  unfold compatible at h
  by_cases hx : s.x % 2 = 0
  · have hw : s.w % 2 = 1 := by omega
    cases hr : s.r with
    | zero =>
      simp only [next, hx, ite_true, hr]
      exact TriadicStep.evenInt hx hw (by omega) (by omega)
    | succ r =>
      have h3 : (3 : ℤ) ^ r % 2 = 1 :=
        Int.odd_iff.mp (Odd.pow (by norm_num : Odd (3 : ℤ)))
      simp only [next, hx, ite_true, hr]
      exact TriadicStep.evenDen hx hw (by omega) (by omega)
  · have hx1 : s.x % 2 = 1 := by omega
    have hw : s.w % 2 = 0 := by omega
    simp only [next, hx, ite_false]
    exact TriadicStep.odd hx1 hw (by omega) (by omega)

/-- Full convergence follows from one finite triadic candidate whose actual
complementary parity tests pass at every clock. This statement constructs
neither that candidate nor its all-time compatibility. -/
theorem alltime_triadic_candidate_reaches_one (n a : ℤ) (r : ℕ)
    (hn : 0 < n)
    (hc : ∀ k, compatible (trajectory ⟨n, a, r⟩ k)) :
    ∃ k, orbit n k = 1 := by
  let s : ℕ → State := trajectory ⟨n, a, r⟩
  have hp : ∀ k, 0 < (s k).x := by
    intro k
    change 0 < (trajectory ⟨n, a, r⟩ k).x
    rw [trajectory_x]
    exact orbit_pos hn k
  have hs : ∀ k, TriadicStep (s k).x (s k).w (s k).r
      (s (k + 1)).x (s (k + 1)).w (s (k + 1)).r := by
    intro k
    exact next_step (s k) (hc k)
  obtain ⟨k, hk⟩ := triadic_pair_reaches_one
    (fun k => (s k).x) (fun k => (s k).w) (fun k => (s k).r) hp hs
  refine ⟨k, ?_⟩
  simpa only [s, trajectory_x] using hk

end CollatzTriadicDual

import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Data.Finset.Max
import Mathlib.Algebra.Order.Archimedean.Basic

/-!
# Finite coefficient consequences of a common pressure maximum

The positive weight and its exact edge balance are explicit inputs.
Generic attainment of its ordinary maximum and the two-sided conclusion
for all supplied actual finite unit paths are proved here. Constructing
the infinite Collatz product and instantiating these hypotheses remain
the written argument in SOURCE_CLOSURE.md. No global Collatz conclusion
or conjectural analytic fact is installed as an axiom.
-/

namespace CollatzShell.TwoSidedPressure

set_option autoImplicit false

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Positive odd ordinary units. -/
def Unit (n : ℕ) : Prop := 0 < n ∧ n % 2 = 1 ∧ n % 3 ≠ 0

/-- Exact positive odd-gap paths within the supplied ordinary component. -/
inductive GapPath (E : ℕ → Prop) : ℕ → List ℕ → ℕ → Prop
  | nil {n : ℕ} : E n → Unit n → GapPath E n [] n
  | cons {n q z a : ℕ} {w : List ℕ} : E n → Unit n → 0 < a →
      3 * n + 1 = 2 ^ a * q → GapPath E q w z → GapPath E n (a :: w) z

theorem path_endpoints {E : ℕ → Prop} {n q : ℕ} {w : List ℕ}
    (hp : GapPath E n w q) : E n ∧ E q := by
  induction hp with
  | nil he _ => exact ⟨he, he⟩
  | cons he _ _ _ _ ih => exact ⟨he, ih.2⟩

theorem path_positive_clock {E : ℕ → Prop} {n q : ℕ} {w : List ℕ}
    (hp : GapPath E n w q) (hw : w ≠ []) : 0 < w.sum := by
  cases hp with
  | nil => simp at hw
  | cons _ _ ha _ _ => simp only [List.sum_cons]; omega

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- The complete finite pressure balance is proved along every actual path. -/
theorem path_balance {E : ℕ → Prop} {r : ℕ → R}
    (hb : ∀ (n q a : ℕ), E n → E q → Unit n → Unit q → 0 < a →
      3 * n + 1 = 2 ^ a * q → (2 : R) ^ a * r n = 3 * r q)
    {n q : ℕ} {w : List ℕ} (hp : GapPath E n w q) :
    (2 : R) ^ w.sum * r n = (3 : R) ^ w.length * r q := by
  induction hp with
  | nil => simp
  | @cons n q z a w he hu ha heq ht ih =>
    have hq := (path_endpoints ht).1
    have huq : Unit q := by cases ht <;> assumption
    have hs := hb n q a he hq hu huq ha heq
    simp only [List.sum_cons, List.length_cons, pow_add, pow_succ]
    calc
      2 ^ a * 2 ^ w.sum * r n = 2 ^ w.sum * (2 ^ a * r n) := by ring
      _ = 2 ^ w.sum * (3 * r q) := by rw [hs]
      _ = 3 * (2 ^ w.sum * r q) := by ring
      _ = 3 * (3 ^ w.length * r z) := by rw [ih]
      _ = 3 ^ w.length * 3 * r z := by ring

/-- A positive ordinary weight bounded by 1/n attains a global maximum. -/
theorem attained_maximum [Archimedean R] {E : ℕ → Prop} {r : ℕ → R}
    (hne : ∃ n, E n)
    (hp : ∀ n, E n → 0 < n ∧ 0 < r n)
    (hb : ∀ n, E n → (n : R) * r n ≤ 1) :
    ∃ m, E m ∧ ∀ n, E n → r n ≤ r m := by
  classical
  obtain ⟨p, hep⟩ := hne
  have hpp := (hp p hep).2
  obtain ⟨N, hN⟩ := exists_nat_gt (1 / r p)
  have hNr : 1 < (N : R) * r p := (div_lt_iff₀ hpp).mp hN
  have hpb := hb p hep
  have hpN : p < N := by
    have hh : (p : R) < N := by nlinarith
    exact_mod_cast hh
  let S : Finset ℕ := (Finset.range N).filter E
  have hpS : p ∈ S := by simp [S, hpN, hep]
  obtain ⟨m, hmS, hmax⟩ := Finset.exists_max_image S r ⟨p, hpS⟩
  refine ⟨m, (Finset.mem_filter.mp hmS).2, ?_⟩
  intro n hen
  by_cases hnN : n < N
  · exact hmax n (by simp [S, hnN, hen])
  · have hnR : (N : R) ≤ n := by exact_mod_cast (Nat.le_of_not_gt hnN)
    have hnr := mul_le_mul_of_nonneg_right hnR hpp.le
    have hnb := hb n hen
    have hnp : r n < r p := by
      have hnpos : (0 : R) < n := by exact_mod_cast (hp n hen).1
      nlinarith
    exact hnp.le.trans (hmax p hpS)

theorem distinct_powers {A h : ℕ} (hA : 0 < A) : 2 ^ A ≠ 3 ^ h := by
  intro he
  have hm := congrArg (fun n : ℕ => n % 2) he
  norm_num [Nat.pow_mod, Nat.ne_of_gt hA] at hm

/-- One finite forward balance at the selected maximum. -/
theorem forward_coefficient {A h : ℕ} {r₀ r₁ : R}
    (hA : 0 < A) (hp : 0 < r₀) (hm : r₁ ≤ r₀)
    (hb : (2 : R) ^ A * r₀ = (3 : R) ^ h * r₁) :
    2 ^ A < 3 ^ h := by
  have h3 : (0 : R) < 3 ^ h := pow_pos (by norm_num) h
  have he : (2 : R) ^ A ≤ 3 ^ h := by nlinarith
  have hn : 2 ^ A ≤ 3 ^ h := by exact_mod_cast he
  exact lt_of_le_of_ne hn (distinct_powers hA)

/-- The same maximum bounds every finite incoming balance in the other direction. -/
theorem inverse_coefficient {A h : ℕ} {r₀ r₁ : R}
    (hA : 0 < A) (hp : 0 < r₀) (hm : r₁ ≤ r₀)
    (hb : (2 : R) ^ A * r₁ = (3 : R) ^ h * r₀) :
    3 ^ h < 2 ^ A := by
  have h2 : (0 : R) < 2 ^ A := pow_pos (by norm_num) A
  have he : (3 : R) ^ h ≤ 2 ^ A := by nlinarith
  have hn : 3 ^ h ≤ 2 ^ A := by exact_mod_cast he
  exact lt_of_le_of_ne hn (Ne.symm (distinct_powers hA))

/-- One attained ordinary root supplies both directions for every nonempty
actual finite unit path, with no depth or gap cap. -/
theorem common_root_two_sided [Archimedean R] {E : ℕ → Prop} {r : ℕ → R}
    (hne : ∃ n, E n)
    (hp : ∀ n, E n → Unit n ∧ 0 < r n)
    (hbound : ∀ n, E n → (n : R) * r n ≤ 1)
    (hbal : ∀ (n q a : ℕ), E n → E q → Unit n → Unit q → 0 < a →
      3 * n + 1 = 2 ^ a * q → (2 : R) ^ a * r n = 3 * r q) :
    ∃ m, E m ∧ (∀ n, E n → r n ≤ r m) ∧
      (∀ (q : ℕ) (w : List ℕ), w ≠ [] → GapPath E m w q →
        2 ^ w.sum < 3 ^ w.length) ∧
      (∀ (n : ℕ) (w : List ℕ), w ≠ [] → GapPath E n w m →
        3 ^ w.length < 2 ^ w.sum) := by
  obtain ⟨m, hem, hm⟩ := attained_maximum hne
    (fun n hen => ⟨(hp n hen).1.1, (hp n hen).2⟩) hbound
  refine ⟨m, hem, hm, ?_, ?_⟩
  · intro q w hw hh
    exact forward_coefficient (path_positive_clock hh hw) (hp m hem).2
      (hm q (path_endpoints hh).2) (path_balance hbal hh)
  · intro n w hw hh
    exact inverse_coefficient (path_positive_clock hh hw) (hp m hem).2
      (hm n (path_endpoints hh).1) (path_balance hbal hh)

/-- The full affine correction is retained when converting to ordinary growth. -/
theorem forward_value_growth {n q A h C : ℕ}
    (hn : 0 < n) (hc : 2 ^ A < 3 ^ h)
    (he : 2 ^ A * q = 3 ^ h * n + C) : n < q := by
  have hp : 0 < 2 ^ A := Nat.pow_pos (by decide)
  nlinarith

theorem forward_gap_one {a : ℕ} (ha : 0 < a) (hc : 2 ^ a < 3) : a = 1 := by
  by_contra he
  have hge : 2 ≤ a := by omega
  have hh : 2 ^ 2 ≤ 2 ^ a := Nat.pow_le_pow_right (by decide) hge
  norm_num at hh
  omega

/-- A positive incoming weight cannot meet the same maximum at gap one. -/
theorem no_incoming_gap_one {r₀ r₁ : R}
    (hp : 0 < r₀) (hm : r₁ ≤ r₀)
    (hb : 2 * r₁ = 3 * r₀) : False := by
  nlinarith

/-- Exact ordinary residues of a unit root with forward gap one and no
incoming positive odd unit gap one. Multiples of three are not admitted
as incoming sources in this statement. -/
theorem maximum_root_residues {m q : ℕ}
    (hm : 0 < m) (hu : m % 3 ≠ 0) (ho : q % 2 = 1)
    (hf : 3 * m + 1 = 2 * q)
    (hi : ∀ n : ℕ, 0 < n → n % 2 = 1 → n % 3 ≠ 0 →
      3 * n + 1 = 2 * m → False) :
    m % 36 = 7 ∨ m % 36 = 19 ∨ m % 36 = 23 ∨ m % 36 = 31 := by
  have hm4 : m % 4 = 3 := by omega
  have h2 : m % 9 ≠ 2 := by
    intro h
    apply hi (6 * (m / 9) + 1) <;> omega
  have h8 : m % 9 ≠ 8 := by
    intro h
    apply hi (6 * (m / 9) + 5) <;> omega
  have h4 : (m % 36) % 4 = 3 :=
    (Nat.mod_mod_of_dvd m (by decide : 4 ∣ 36)).trans hm4
  have h9 : (m % 36) % 9 = m % 9 :=
    Nat.mod_mod_of_dvd m (by decide : 9 ∣ 36)
  have h3 : (m % 36) % 3 = m % 3 :=
    Nat.mod_mod_of_dvd m (by decide : 3 ∣ 36)
  have h36 : m % 36 < 36 := Nat.mod_lt m (by decide)
  have hx : m % 9 = 1 ∨ m % 9 = 4 ∨ m % 9 = 5 ∨ m % 9 = 7 := by omega
  rcases hx with hx | hx | hx | hx <;> omega

end CollatzShell.TwoSidedPressure

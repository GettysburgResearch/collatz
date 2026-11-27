import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Dimension.Constructions

/-! Positive ordinary indices, with no convention needed for a leading zero. -/

namespace CollatzShortProbe
open Module

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

private def samples (K : Type*) {V : Type*} [Field K] [AddCommGroup V] [Module K V]
    (F : ℕ → V) (B k : ℕ) : Submodule K V :=
  Submodule.span K (F '' Set.Ico B (2 ^ k * B))

private theorem samples_mono (F : ℕ → V) (B : ℕ) {i j : ℕ} (h : i ≤ j) :
    samples K F B i ≤ samples K F B j := by
  apply Submodule.span_mono
  apply Set.image_mono
  exact Set.Ico_subset_Ico_right (Nat.mul_le_mul_right B (Nat.pow_le_pow_right (by decide) h))

private theorem sample_mem (F : ℕ → V) {B n k : ℕ} (hn : B ≤ n) (hk : n < 2 ^ k * B) :
    F n ∈ samples K F B k :=
  Submodule.subset_span ⟨n, ⟨hn, hk⟩, rfl⟩

private theorem level_stabilizes [FiniteDimensional K V] (F : ℕ → V) (B : ℕ) :
    ∃ j ≤ finrank K V, samples K F B j = samples K F B (j + 1) := by
  by_contra! h
  have grow : ∀ n ≤ finrank K V + 1, n ≤ finrank K (samples K F B n) := by
    intro n hn
    induction n with
    | zero => omega
    | succ i ih =>
      have hi : i ≤ finrank K V := by omega
      have strict := lt_of_le_of_ne (samples_mono (K := K) F B (Nat.le_succ i)) (h i hi)
      have more := Submodule.finrank_lt_finrank_of_lt strict
      have before := ih (by omega)
      exact Nat.succ_le_of_lt (lt_of_le_of_lt before more)
  have lower := grow (finrank K V + 1) (by omega)
  have upper := Submodule.finrank_le (samples K F B (finrank K V + 1))
  omega

/-- A binary-linear sequence on positive inputs is zero at every positive input if
a linear probe vanishes below two to the dimension. Only the two exact binary
recurrences on the positive integers are needed. -/
theorem probe_band [FiniteDimensional K V] (B : ℕ) (hB : 0 < B) (F : ℕ → V) (a₀ a₁ : V →ₗ[K] V)
    (even : ∀ n > 0, F (2 * n) = a₀ (F n))
    (odd : ∀ n > 0, F (2 * n + 1) = a₁ (F n))
    (out : V →ₗ[K] K)
    (localZero : ∀ n ≥ B, n < 2 ^ finrank K V * B → out (F n) = 0) :
    ∀ n ≥ B, out (F n) = 0 := by
  obtain ⟨j, hj, hs⟩ := level_stabilizes (K := K) F B
  have growStep (A : V →ₗ[K] V) (b : ℕ) (hb : b ≤ 1)
      (step : ∀ n > 0, F (2*n+b) = A (F n)) :
      samples K F B j ≤ (samples K F B j).comap A := by
    apply Submodule.span_le.mpr
    rintro x ⟨n, ⟨hn, hk⟩, rfl⟩
    change A (F n) ∈ samples K F B j
    rw [← step n (by omega), hs]
    apply sample_mem F (by omega)
    rw [pow_succ, Nat.mul_right_comm]
    omega
  have ev := growStep a₀ 0 (by decide) (by simpa using even)
  have od := growStep a₁ 1 (by decide) odd
  have base (n) (hn : B ≤ n) (hn2 : n < 2*B) : F n ∈ samples K F B j := by
    rw [hs]
    apply sample_mem F hn
    rw [pow_succ, Nat.mul_assoc]
    exact lt_of_lt_of_le hn2 (Nat.le_mul_of_pos_left _ (Nat.two_pow_pos _))
  have allMem : ∀ n ≥ B, F n ∈ samples K F B j := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro hn
      by_cases h1 : n < 2*B
      · exact base n hn h1
      have halfB : B ≤ n/2 := by omega
      have halfPos : 0 < n/2 := by omega
      have prev := ih (n/2) (by omega) halfB
      by_cases parity : n % 2 = 0
      · have he := even (n/2) halfPos
        have eqn : 2 * (n/2) = n := by omega
        rw [eqn] at he
        rw [he]
        exact ev prev
      · have ho := odd (n/2) halfPos
        have eqn : 2 * (n/2) + 1 = n := by omega
        rw [eqn] at ho
        rw [ho]
        exact od prev
  have zeroSpace : samples K F B j ≤ LinearMap.ker out := by
    apply Submodule.span_le.mpr
    rintro x ⟨n, ⟨hn, hk⟩, rfl⟩
    exact localZero n hn (lt_of_lt_of_le hk (Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) hj)))
  intro n hn
  exact zeroSpace (allMem n hn)

/-- Entries record the source and the three carry possibilities for tripling. -/
private def features (F : ℕ → V) (n : ℕ) : V × V × V × V :=
  (F n, F (3*n), F (3*n+1), F (3*n+2))

private def liftEven (a₀ a₁ : V →ₗ[K] V) :
    (V × V × V × V) →ₗ[K] (V × V × V × V) where
  toFun z := (a₀ z.1, a₀ z.2.1, a₁ z.2.1, a₀ z.2.2.1)
  map_add' _ _ := by simp
  map_smul' _ _ := by simp

private def liftOdd (a₀ a₁ : V →ₗ[K] V) :
    (V × V × V × V) →ₗ[K] (V × V × V × V) where
  toFun z := (a₁ z.1, a₁ z.2.2.1, a₀ z.2.2.2, a₁ z.2.2.2)
  map_add' _ _ := by simp
  map_smul' _ _ := by simp

private theorem feature_laws (F : ℕ → V) (a₀ a₁ : V →ₗ[K] V)
    (even : ∀ n > 0, F (2*n) = a₀ (F n))
    (odd : ∀ n > 0, F (2*n+1) = a₁ (F n)) :
    (∀ n > 0, features F (2*n) = liftEven a₀ a₁ (features F n)) ∧
    (∀ n > 0, features F (2*n+1) = liftOdd a₀ a₁ (features F n)) := by
  constructor <;> intro n hn
  · change (_, _, _, _) = (_, _, _, _)
    simp only [Prod.mk.injEq]
    refine ⟨even n hn, ?_, ?_, ?_⟩
    · convert even (3*n) (by omega) using 1
      · congr 1; omega
      · rfl
    · convert odd (3*n) (by omega) using 1
      · congr 1; omega
      · rfl
    · convert even (3*n+1) (by omega) using 1
      · congr 1; omega
      · rfl
  · change (_, _, _, _) = (_, _, _, _)
    simp only [Prod.mk.injEq]
    refine ⟨odd n hn, ?_, ?_, ?_⟩
    · convert odd (3*n+1) (by omega) using 1
      · congr 1; omega
      · rfl
    · convert even (3*n+2) (by omega) using 1
      · congr 1; omega
      · rfl
    · convert odd (3*n+2) (by omega) using 1
      · congr 1; omega
      · rfl

/-- The even and odd shortcut identities form a complete finite test for an ordinary
binary linear representation. The test is valid over an arbitrary field. -/
theorem finite_edge_band [FiniteDimensional K V] (B : ℕ) (hB : 0 < B) (F : ℕ → V) (a₀ a₁ : V →ₗ[K] V)
    (even : ∀ n > 0, F (2*n) = a₀ (F n))
    (odd : ∀ n > 0, F (2*n+1) = a₁ (F n))
    (out : V →ₗ[K] K)
    (shortEven : ∀ n ≥ B, n < 2^(4*finrank K V)*B → out (F (2*n)) = out (F n))
    (shortOdd : ∀ n ≥ B, n < 2^(4*finrank K V)*B → out (F (2*n+1)) = out (F (3*n+2))) :
    (∀ n ≥ B, out (F (2*n)) = out (F n)) ∧
    (∀ n ≥ B, out (F (2*n+1)) = out (F (3*n+2))) := by
  let π₀ : (V × V × V × V) →ₗ[K] V := LinearMap.fst K V _
  let π₃ : (V × V × V × V) →ₗ[K] V :=
    (LinearMap.snd K V V).comp ((LinearMap.snd K V _).comp (LinearMap.snd K V _))
  let eProbe := (out.comp a₀).comp π₀ - out.comp π₀
  let oProbe := (out.comp a₁).comp π₀ - out.comp π₃
  obtain ⟨he, ho⟩ := feature_laws F a₀ a₁ even odd
  have dim : finrank K (V × V × V × V) = 4*finrank K V := by
    simp only [Module.finrank_prod]
    omega
  have e := probe_band B hB (features F) _ _ he ho eProbe (by
    intro n hn h
    rw [dim] at h
    change out (a₀ (F n)) - out (F n) = 0
    rw [← even n (by omega), shortEven n hn h, sub_self])
  have o := probe_band B hB (features F) _ _ he ho oProbe (by
    intro n hn h
    rw [dim] at h
    change out (a₁ (F n)) - out (F (3*n+2)) = 0
    rw [← odd n (by omega), shortOdd n hn h, sub_self])
  constructor <;> intro n hn
  · rw [even n (by omega)]
    exact sub_eq_zero.mp (e n hn)
  · rw [odd n (by omega)]
    exact sub_eq_zero.mp (o n hn)

#print axioms probe_band
#print axioms finite_edge_band

end CollatzShortProbe

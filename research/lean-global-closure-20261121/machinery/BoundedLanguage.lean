import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Set.Finite.Lattice
import Mathlib.Data.Set.Finite.Range
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Exact integral inverse sets for bounded affine block languages

An affine block sends `x` to `(u*x+c)/v`, where `u > 1` and `u,v`
are coprime integers. The defect `(v-u)*m-c` at an integer endpoint
controls every repetition count, using the entire repeated correction.

This file proves the exact divisibility criterion and finiteness under
arbitrary independent block repetition. It does not prove Collatz.
-/

namespace CollatzBoundedLanguage

/-- Numerator correction after `e` repetitions of `(u*x+c)/v`. -/
def correction (u v c : ℤ) : ℕ → ℤ
  | 0 => 0
  | e + 1 => v * correction u v c e + c * u ^ e

theorem correction_identity (u v c : ℤ) (e : ℕ) :
    (v - u) * correction u v c e = c * (v ^ e - u ^ e) := by
  induction e with
  | zero => simp [correction]
  | succ e ih =>
      simp only [correction, pow_succ]
      calc
        (v - u) * (v * correction u v c e + c * u ^ e) =
            v * ((v - u) * correction u v c e) + (v - u) * c * u ^ e := by ring
        _ = c * (v ^ e * v - u ^ e * u) := by rw [ih]; ring

/-- Full affine equation for an integer source and endpoint. -/
def Reaches (u v c : ℤ) (e : ℕ) (q m : ℤ) : Prop :=
  v ^ e * m = u ^ e * q + correction u v c e

theorem defect_identity {u v c q m : ℤ} {e : ℕ}
    (h : Reaches u v c e q m) :
    u ^ e * ((v - u) * q - c) = v ^ e * ((v - u) * m - c) := by
  have hi := correction_identity u v c e
  unfold Reaches at h
  nlinarith only [hi, congrArg (fun z : ℤ => (v - u) * z) h]

theorem numerator_defect_identity (u v c m : ℤ) (e : ℕ) :
    (v - u) * (v ^ e * m - correction u v c e) =
      v ^ e * ((v - u) * m - c) + c * u ^ e := by
  have hi := correction_identity u v c e
  nlinarith only [hi]

/-- Exact integral-preimage test, with no restriction on the endpoint sign. -/
theorem exists_reaches_iff_dvd {u v c m : ℤ} (hc : IsCoprime u v) (e : ℕ) :
    (∃ q : ℤ, Reaches u v c e q m) ↔ u ^ e ∣ (v - u) * m - c := by
  have hpow : IsCoprime (u ^ e) (v ^ e) := hc.pow
  have hdiff : IsCoprime (u ^ e) (v - u) := by
    have hh : IsCoprime u (v - u) := by
      simpa using (IsCoprime.sub_mul_left_right_iff (x := u) (y := v) (z := 1)).mpr hc
    exact hh.pow_left
  constructor
  · rintro ⟨q, hq⟩
    apply hpow.dvd_of_dvd_mul_left
    rw [← defect_identity hq]
    exact dvd_mul_right _ _
  · intro hd
    have hn : u ^ e ∣ v ^ e * m - correction u v c e := by
      apply hdiff.dvd_of_dvd_mul_left
      rw [numerator_defect_identity]
      exact dvd_add (dvd_mul_of_dvd_right hd _) (dvd_mul_left _ _)
    rcases hn with ⟨q, hq⟩
    exact ⟨q, by unfold Reaches; linarith only [hq]⟩

structure Block where
  u : ℕ
  v : ℤ
  c : ℤ
  u_large : 1 < u
  coprime : IsCoprime (u : ℤ) v

namespace Block

def defect (b : Block) (m : ℤ) : ℤ := (b.v - (b.u : ℤ)) * m - b.c

def Sources (b : Block) (m : ℤ) : Set ℤ :=
  {q | ∃ e : ℕ, Reaches b.u b.v b.c e q m}

theorem u_ne_zero (b : Block) : (b.u : ℤ) ≠ 0 := by
  have hu := b.u_large
  have : b.u ≠ 0 := by omega
  exact_mod_cast this

theorem slope_ne (b : Block) : b.v - (b.u : ℤ) ≠ 0 := by
  intro h
  have hv : b.v = (b.u : ℤ) := sub_eq_zero.mp h
  have hu : IsUnit (b.u : ℤ) := isCoprime_self.mp (by simpa [hv] using b.coprime)
  have he : b.u = 1 := by simpa using Int.isUnit_iff_natAbs_eq.mp hu
  have hl := b.u_large
  omega

/-- All nonempty-odd-count Collatz blocks instantiate the hypotheses automatically. -/
def ofCounts (s L : ℕ) (c : ℤ) (hs : 0 < s) : Block where
  u := 3 ^ s
  v := (2 : ℤ) ^ L
  c := c
  u_large := Nat.one_lt_pow (by omega) (by norm_num)
  coprime := by
    have h : IsCoprime (3 : ℤ) 2 := ⟨1, -1, by norm_num⟩
    simpa only [Nat.cast_pow, Nat.cast_ofNat] using (h.pow (m := s) (n := L))

theorem reaches_unique (b : Block) {e : ℕ} {q₁ q₂ m : ℤ}
    (h₁ : Reaches b.u b.v b.c e q₁ m)
    (h₂ : Reaches b.u b.v b.c e q₂ m) : q₁ = q₂ := by
  apply mul_left_cancel₀ (pow_ne_zero e b.u_ne_zero)
  unfold Reaches at h₁ h₂
  linarith only [h₁, h₂]

def preimage (b : Block) (e : ℕ) (m : ℤ) : ℤ :=
  (b.v ^ e * m - correction b.u b.v b.c e) / (b.u : ℤ) ^ e

theorem preimage_eq_of_reaches (b : Block) {e : ℕ} {q m : ℤ}
    (h : Reaches b.u b.v b.c e q m) : b.preimage e m = q := by
  apply Int.ediv_eq_of_eq_mul_right (pow_ne_zero e b.u_ne_zero)
  unfold Reaches at h
  linarith only [h]

theorem preimage_reaches_iff_dvd (b : Block) (e : ℕ) (m : ℤ) :
    Reaches b.u b.v b.c e (b.preimage e m) m ↔
      (b.u : ℤ) ^ e ∣ b.defect m := by
  constructor
  · intro h
    exact (exists_reaches_iff_dvd b.coprime e).mp ⟨_, h⟩
  · intro hd
    obtain ⟨q, hq⟩ := (exists_reaches_iff_dvd b.coprime e).mpr hd
    simpa only [b.preimage_eq_of_reaches hq] using hq

theorem zero_defect_source (b : Block) {m q : ℤ} {e : ℕ}
    (hm : b.defect m = 0) (hq : Reaches b.u b.v b.c e q m) : q = m := by
  have hi := defect_identity hq
  have hm' : (b.v - (b.u : ℤ)) * m - b.c = 0 := hm
  rw [hm', mul_zero] at hi
  have hq' : (b.v - (b.u : ℤ)) * q - b.c = 0 :=
    (mul_eq_zero.mp hi).resolve_left (pow_ne_zero e b.u_ne_zero)
  apply mul_left_cancel₀ b.slope_ne
  linarith only [hm', hq']

/-- A coarse effective exponent cutoff; the exact cutoff is the prime valuation. -/
theorem exponent_lt_defect (b : Block) {m q : ℤ} {e : ℕ}
    (hm : b.defect m ≠ 0) (hq : Reaches b.u b.v b.c e q m) :
    e < (b.defect m).natAbs := by
  have hd : (b.u : ℤ) ^ e ∣ b.defect m :=
    (exists_reaches_iff_dvd b.coprime e).mp ⟨q, hq⟩
  have hb := Int.natAbs_le_of_dvd_ne_zero hd hm
  have hp : b.u ^ e ≤ (b.defect m).natAbs := by
    simpa using hb
  exact (Nat.lt_pow_self b.u_large).trans_le hp

theorem sources_finite (b : Block) (m : ℤ) : (b.Sources m).Finite := by
  by_cases hm : b.defect m = 0
  · apply (Set.finite_singleton m).subset
    intro q hq
    rcases hq with ⟨e, he⟩
    exact b.zero_defect_source hm he
  · let f : Fin (b.defect m).natAbs → ℤ := fun e =>
      (b.v ^ e.val * m - correction b.u b.v b.c e.val) / (b.u : ℤ) ^ e.val
    apply (Set.finite_range f).subset
    intro q hq
    rcases hq with ⟨e, he⟩
    refine ⟨⟨e, b.exponent_lt_defect hm he⟩, ?_⟩
    apply Int.ediv_eq_of_eq_mul_right (pow_ne_zero e b.u_ne_zero)
    unfold Reaches at he
    linarith only [he]

/-- Exact finite inverse list. The coarse cutoff makes it executable without valuations. -/
def inverseFinset (b : Block) (m : ℤ) : Finset ℤ :=
  if b.defect m = 0 then {m}
  else ((Finset.range (b.defect m).natAbs).filter
    (fun e => (b.u : ℤ) ^ e ∣ b.defect m)).image (fun e => b.preimage e m)

theorem mem_inverseFinset (b : Block) (q m : ℤ) :
    q ∈ b.inverseFinset m ↔ q ∈ b.Sources m := by
  by_cases hm : b.defect m = 0
  · simp only [inverseFinset, hm, ↓reduceIte, Finset.mem_singleton]
    constructor
    · rintro rfl
      exact ⟨0, by simp [Reaches, correction]⟩
    · rintro ⟨e, he⟩
      exact b.zero_defect_source hm he
  · simp only [inverseFinset, hm, ↓reduceIte]
    constructor
    · intro h
      obtain ⟨e, he, hq⟩ := Finset.mem_image.mp h
      have hd := (Finset.mem_filter.mp he).2
      exact ⟨e, hq ▸ (b.preimage_reaches_iff_dvd e m).mpr hd⟩
    · rintro ⟨e, he⟩
      apply Finset.mem_image.mpr
      refine ⟨e, ?_, b.preimage_eq_of_reaches he⟩
      apply Finset.mem_filter.mpr
      exact ⟨Finset.mem_range.mpr (b.exponent_lt_defect hm he),
        (exists_reaches_iff_dvd b.coprime e).mp ⟨q, he⟩⟩

end Block

/-- Complete inverse sources for a finite ordered block list; each exponent is arbitrary. -/
def Sources : List Block → ℤ → Set ℤ
  | [], m => {m}
  | b :: bs, m => ⋃ y ∈ Sources bs m, b.Sources y

theorem sources_finite (bs : List Block) (m : ℤ) : (Sources bs m).Finite := by
  induction bs with
  | nil => exact Set.finite_singleton m
  | cons b bs ih =>
      exact ih.biUnion (fun y _ => b.sources_finite y)

/-- Exact finite backward recursion for arbitrary independent exponents. -/
def inverseFinset : List Block → ℤ → Finset ℤ
  | [], m => {m}
  | b :: bs, m => (inverseFinset bs m).biUnion (fun y => b.inverseFinset y)

theorem mem_inverseFinset (bs : List Block) (q m : ℤ) :
    q ∈ inverseFinset bs m ↔ q ∈ Sources bs m := by
  induction bs generalizing q with
  | nil => simp [inverseFinset, Sources]
  | cons b bs ih =>
      simp only [inverseFinset, Finset.mem_biUnion, Sources, Set.mem_iUnion]
      constructor
      · rintro ⟨y, hy, hq⟩
        exact ⟨y, (ih y).mp hy, (b.mem_inverseFinset q y).mp hq⟩
      · rintro ⟨y, hy, hq⟩
        exact ⟨y, (ih y).mpr hy, (b.mem_inverseFinset q y).mpr hq⟩

end CollatzBoundedLanguage

import CycleWordAlgebra
import Mathlib.Data.Finset.Card
import Mathlib.Data.Nat.ModEq
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-!
# Complete-carry decoding and weighted ternary fibers

The chronological shortcut carry is imported without changing its clock.
At fixed length and odd count it determines the entire word. Its integer
quotient by a supplied modulus therefore counts the possible words in one
residue fiber. The final weighted estimate retains arbitrary word weights;
it does not bound repeated-word mass or assert an actual-law decay rate.
-/

namespace CollatzShell.CarryFibers

open Collatz.HighVariance.CycleWordAlgebra
open scoped BigOperators

set_option autoImplicit false

theorem carry_head_parity (b : Bool) (w : List Bool) :
    carry (b :: w) % 2 = if b then 1 else 0 := by
  cases b <;> simp [carry, Nat.add_mod, Nat.pow_mod]

/-- The complete chronological carry decodes every bit once both clocks
are retained. Trailing zeroes are why the length hypothesis is needed. -/
theorem word_eq_of_length_ones_carry {u v : List Bool}
    (hl : u.length = v.length) (ho : ones u = ones v)
    (hc : carry u = carry v) : u = v := by
  induction u generalizing v with
  | nil =>
    cases v with
    | nil => rfl
    | cons b v => simp at hl
  | cons b u ih =>
    cases v with
    | nil => simp at hl
    | cons c v =>
      have hbc : b = c := by
        have hm := congrArg (fun n : Nat => n % 2) hc
        rw [carry_head_parity, carry_head_parity] at hm
        cases b <;> cases c <;> simp_all
      subst c
      have hl' : u.length = v.length := by simpa using hl
      have ho' : ones u = ones v := by
        cases b <;> simp_all [ones]
      have hc' : carry u = carry v := by
        simp only [carry] at hc
        rw [ho'] at hc
        omega
      exact congrArg (List.cons b) (ih hl' ho' hc')

/-- Quotient and remainder of the full carry recover the same word. -/
theorem word_eq_of_carry_div_mod {u v : List Bool} {Q : Nat}
    (hl : u.length = v.length) (ho : ones u = ones v)
    (hd : carry u / Q = carry v / Q)
    (hm : carry u % Q = carry v % Q) : u = v := by
  apply word_eq_of_length_ones_carry hl ho
  calc
    carry u = carry u % Q + Q * (carry u / Q) := (Nat.mod_add_div _ _).symm
    _ = carry v % Q + Q * (carry v / Q) := by rw [hm, hd]
    _ = carry v := Nat.mod_add_div _ _

/-- A residue fiber with carry quotient below R contains at most R words.
All words retain their original length and odd count. -/
theorem residue_fiber_card_le (S : Finset (List Bool)) (L p Q R a : Nat)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (hm : ∀ w ∈ S, carry w % Q = a)
    (hd : ∀ w ∈ S, carry w / Q < R) : S.card ≤ R := by
  have hh : S.card ≤ (Finset.range R).card :=
    Finset.card_le_card_of_injOn (fun w => carry w / Q)
      (fun w hw => Finset.mem_range.mpr (hd w hw))
      (fun u hu v hv he => word_eq_of_carry_div_mod
        ((hl u hu).trans (hl v hv).symm)
        ((ho u hu).trans (ho v hv).symm) he
        ((hm u hu).trans (hm v hv).symm))
  simpa using hh

/-- Only the width of a carry-quotient interval is paid. Its location
may be arbitrarily high. -/
theorem residue_fiber_card_le_interval (S : Finset (List Bool))
    (L p Q b R a : Nat)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (hm : ∀ w ∈ S, carry w % Q = a)
    (hlo : ∀ w ∈ S, b ≤ carry w / Q)
    (hhi : ∀ w ∈ S, carry w / Q < b + R) : S.card ≤ R := by
  have hh : S.card ≤ (Finset.range R).card := by
    apply Finset.card_le_card_of_injOn (fun w => carry w / Q - b)
    · intro w hw
      apply Finset.mem_range.mpr
      change carry w / Q - b < R
      have h1 := hlo w hw
      have h2 := hhi w hw
      omega
    · intro u hu v hv hh
      change carry u / Q - b = carry v / Q - b at hh
      apply word_eq_of_carry_div_mod (Q := Q)
        ((hl u hu).trans (hl v hv).symm)
        ((ho u hu).trans (ho v hv).symm)
      · have h1 := hlo u hu
        have h2 := hlo v hv
        omega
      · exact (hm u hu).trans (hm v hv).symm
  simpa using hh

/-- Carries smaller than the modulus have no collisions at fixed clocks. -/
theorem word_eq_of_small_carry_mod {u v : List Bool} {Q : Nat}
    (hl : u.length = v.length) (ho : ones u = ones v)
    (hu : carry u < Q) (hv : carry v < Q)
    (hm : carry u % Q = carry v % Q) : u = v := by
  exact word_eq_of_length_ones_carry hl ho
    (by simpa [Nat.mod_eq_of_lt hu, Nat.mod_eq_of_lt hv] using hm)

/-- An exact complete affine identity sends an ordinary endpoint residue
to the corresponding full-carry residue. No source is replaced by a
freely selected modular representative. -/
theorem endpoint_residue_to_carry {L p n q C a : Nat}
    (he : 2 ^ L * q = 3 ^ p * n + C)
    (hr : q % (3 ^ p) = a) : C % (3 ^ p) = (2 ^ L * a) % (3 ^ p) := by
  have hh := congrArg (fun z : Nat => z % (3 ^ p)) he
  simpa [Nat.add_mod, Nat.mul_mod, hr] using hh.symm

/-- The same fiber count for endpoints of supplied complete ordinary
affine identities, retaining both clocks and all correction terms. -/
theorem actual_endpoint_fiber_card_le (S : Finset (List Bool)) (L p R a : Nat)
    (source endpoint : List Bool → Nat)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (he : ∀ w ∈ S, 2 ^ L * endpoint w = 3 ^ p * source w + carry w)
    (hr : ∀ w ∈ S, endpoint w % (3 ^ p) = a)
    (hd : ∀ w ∈ S, carry w / (3 ^ p) < R) : S.card ≤ R := by
  exact residue_fiber_card_le S L p (3 ^ p) R ((2 ^ L * a) % (3 ^ p))
    hl ho (fun w hw => endpoint_residue_to_carry (he w hw) (hr w hw)) hd

/-- The source-preserving endpoint version also pays only interval width. -/
theorem actual_endpoint_fiber_card_le_interval (S : Finset (List Bool))
    (L p b R a : Nat) (source endpoint : List Bool → Nat)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (he : ∀ w ∈ S, 2 ^ L * endpoint w = 3 ^ p * source w + carry w)
    (hr : ∀ w ∈ S, endpoint w % (3 ^ p) = a)
    (hlo : ∀ w ∈ S, b ≤ carry w / (3 ^ p))
    (hhi : ∀ w ∈ S, carry w / (3 ^ p) < b + R) : S.card ≤ R := by
  exact residue_fiber_card_le_interval S L p (3 ^ p) b R
    ((2 ^ L * a) % (3 ^ p)) hl ho
    (fun w hw => endpoint_residue_to_carry (he w hw) (hr w hw)) hlo hhi

/-- Equal complete-word carries force the original ordinary sources to
have the same residue at the original binary clock. -/
theorem same_carry_source_mod {L p n₁ n₂ q₁ q₂ C : Nat}
    (h₁ : 2 ^ L * q₁ = 3 ^ p * n₁ + C)
    (h₂ : 2 ^ L * q₂ = 3 ^ p * n₂ + C) :
    n₁ % (2 ^ L) = n₂ % (2 ^ L) := by
  have hh : Nat.ModEq (2 ^ L) (3 ^ p * n₁ + C) (3 ^ p * n₂ + C) := by
    rw [← h₁, ← h₂]
    simp [Nat.ModEq]
  have hp := Nat.ModEq.add_right_cancel' C hh
  have hc : (2 ^ L).Coprime (3 ^ p) :=
    ((by decide : Nat.Coprime 2 3).pow_left L).pow_right p
  exact Nat.ModEq.cancel_left_of_coprime hc hp

/-- The original source block pays repeated words: equal carries and
equal binary source quotients force the same source and endpoint. -/
theorem same_carry_same_source_block {L p n₁ n₂ q₁ q₂ C : Nat}
    (h₁ : 2 ^ L * q₁ = 3 ^ p * n₁ + C)
    (h₂ : 2 ^ L * q₂ = 3 ^ p * n₂ + C)
    (hb : n₁ / (2 ^ L) = n₂ / (2 ^ L)) : n₁ = n₂ ∧ q₁ = q₂ := by
  have hm := same_carry_source_mod h₁ h₂
  have hn : n₁ = n₂ := by
    calc
      n₁ = n₁ % (2 ^ L) + 2 ^ L * (n₁ / (2 ^ L)) := (Nat.mod_add_div _ _).symm
      _ = n₂ % (2 ^ L) + 2 ^ L * (n₂ / (2 ^ L)) := by rw [hm, hb]
      _ = n₂ := Nat.mod_add_div _ _
  refine ⟨hn, ?_⟩
  have hpow : 0 < 2 ^ L := Nat.pow_pos (by decide)
  rw [hn] at h₁
  exact Nat.eq_of_mul_eq_mul_left hpow (h₁.trans h₂.symm)

/-- At fixed two clocks, carry quotient and original source quotient,
the ternary endpoint residue recovers the complete word and both values.
This applies at every translated source height, without a maximum height. -/
theorem actual_box_injection {u v : List Bool} {L p n₁ n₂ q₁ q₂ : Nat}
    (huL : u.length = L) (hvL : v.length = L)
    (hup : ones u = p) (hvp : ones v = p)
    (h₁ : 2 ^ L * q₁ = 3 ^ p * n₁ + carry u)
    (h₂ : 2 ^ L * q₂ = 3 ^ p * n₂ + carry v)
    (hr : q₁ % (3 ^ p) = q₂ % (3 ^ p))
    (hcq : carry u / (3 ^ p) = carry v / (3 ^ p))
    (hsq : n₁ / (2 ^ L) = n₂ / (2 ^ L)) :
    u = v ∧ n₁ = n₂ ∧ q₁ = q₂ := by
  have hcm : carry u % (3 ^ p) = carry v % (3 ^ p) :=
    (endpoint_residue_to_carry h₁ hr).trans
      (endpoint_residue_to_carry h₂ rfl).symm
  have huv := word_eq_of_carry_div_mod (huL.trans hvL.symm)
    (hup.trans hvp.symm) hcq hcm
  refine ⟨huv, ?_⟩
  rw [huv] at h₁
  exact same_carry_same_source_block h₁ h₂ hsq

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- A small arithmetic fiber controls its original weighted square. -/
theorem fiber_weight_square_le (S : Finset (List Bool)) (L p Q R a : Nat)
    (weight : List Bool → K)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (hm : ∀ w ∈ S, carry w % Q = a)
    (hd : ∀ w ∈ S, carry w / Q < R) :
    (∑ w ∈ S, weight w) ^ 2 ≤ (R : K) * ∑ w ∈ S, weight w ^ 2 := by
  have hcard : (S.card : K) ≤ R := by
    exact_mod_cast residue_fiber_card_le S L p Q R a hl ho hm hd
  calc
    (∑ w ∈ S, weight w) ^ 2 ≤ (S.card : K) * ∑ w ∈ S, weight w ^ 2 := by
      simpa using Finset.sum_mul_sq_le_sq_mul_sq S (fun _ => (1 : K)) weight
    _ ≤ (R : K) * ∑ w ∈ S, weight w ^ 2 :=
      mul_le_mul_of_nonneg_right hcard (Finset.sum_nonneg (fun _ _ => sq_nonneg _))

/-- Summing every residue retains the same arbitrary word weights. The
right side includes repeated occurrences already combined in each weight. -/
theorem carry_collision_le (S : Finset (List Bool)) (L p Q R : Nat)
    (hQ : 0 < Q) (weight : List Bool → K)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (hd : ∀ w ∈ S, carry w / Q < R) :
    (∑ a ∈ Finset.range Q,
      (∑ w ∈ S.filter (fun w => carry w % Q = a), weight w) ^ 2) ≤
      (R : K) * ∑ w ∈ S, weight w ^ 2 := by
  calc
    (∑ a ∈ Finset.range Q,
      (∑ w ∈ S.filter (fun w => carry w % Q = a), weight w) ^ 2) ≤
        ∑ a ∈ Finset.range Q,
          (R : K) * ∑ w ∈ S.filter (fun w => carry w % Q = a), weight w ^ 2 := by
      apply Finset.sum_le_sum
      intro a _
      exact fiber_weight_square_le (S.filter (fun w => carry w % Q = a))
        L p Q R a weight
        (fun w hw => hl w (Finset.mem_filter.mp hw).1)
        (fun w hw => ho w (Finset.mem_filter.mp hw).1)
        (fun _ hw => (Finset.mem_filter.mp hw).2)
        (fun w hw => hd w (Finset.mem_filter.mp hw).1)
    _ = (R : K) * ∑ w ∈ S, weight w ^ 2 := by
      rw [← Finset.mul_sum]
      congr 1
      exact Finset.sum_fiberwise_of_maps_to
        (fun w _ => Finset.mem_range.mpr (Nat.mod_lt (carry w) hQ))
        (fun w => weight w ^ 2)

/-- An endpoint collision upper bound for exactly the supplied word
weights and complete ordinary affine identities. Repeated-word weights
are retained on the right; no bound on their size is assumed or inferred. -/
theorem actual_endpoint_collision_le_interval (S : Finset (List Bool)) (L p b R : Nat)
    (source endpoint : List Bool → Nat) (weight : List Bool → K)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (he : ∀ w ∈ S, 2 ^ L * endpoint w = 3 ^ p * source w + carry w)
    (hlo : ∀ w ∈ S, b ≤ carry w / (3 ^ p))
    (hhi : ∀ w ∈ S, carry w / (3 ^ p) < b + R) :
    (∑ a ∈ Finset.range (3 ^ p),
      (∑ w ∈ S.filter (fun w => endpoint w % (3 ^ p) = a), weight w) ^ 2) ≤
      (R : K) * ∑ w ∈ S, weight w ^ 2 := by
  have hQ : 0 < 3 ^ p := Nat.pow_pos (by decide)
  calc
    (∑ a ∈ Finset.range (3 ^ p),
      (∑ w ∈ S.filter (fun w => endpoint w % (3 ^ p) = a), weight w) ^ 2) ≤
        ∑ a ∈ Finset.range (3 ^ p),
          (R : K) * ∑ w ∈ S.filter (fun w => endpoint w % (3 ^ p) = a), weight w ^ 2 := by
      apply Finset.sum_le_sum
      intro a _
      have hcard := actual_endpoint_fiber_card_le_interval
        (S.filter (fun w => endpoint w % (3 ^ p) = a)) L p b R a source endpoint
        (fun w hw => hl w (Finset.mem_filter.mp hw).1)
        (fun w hw => ho w (Finset.mem_filter.mp hw).1)
        (fun w hw => he w (Finset.mem_filter.mp hw).1)
        (fun _ hw => (Finset.mem_filter.mp hw).2)
        (fun w hw => hlo w (Finset.mem_filter.mp hw).1)
        (fun w hw => hhi w (Finset.mem_filter.mp hw).1)
      have hh : ((S.filter (fun w => endpoint w % (3 ^ p) = a)).card : K) ≤ R := by
        exact_mod_cast hcard
      have hc : (∑ w ∈ S.filter (fun w => endpoint w % (3 ^ p) = a), weight w) ^ 2 ≤
          ((S.filter (fun w => endpoint w % (3 ^ p) = a)).card : K) *
            ∑ w ∈ S.filter (fun w => endpoint w % (3 ^ p) = a), weight w ^ 2 := by
        simpa using Finset.sum_mul_sq_le_sq_mul_sq
          (S.filter (fun w => endpoint w % (3 ^ p) = a))
          (fun _ => (1 : K)) weight
      exact hc.trans
        (mul_le_mul_of_nonneg_right hh (Finset.sum_nonneg (fun _ _ => sq_nonneg _)))
    _ = (R : K) * ∑ w ∈ S, weight w ^ 2 := by
      rw [← Finset.mul_sum]
      congr 1
      exact Finset.sum_fiberwise_of_maps_to
        (fun w _ => Finset.mem_range.mpr (Nat.mod_lt (endpoint w) hQ))
        (fun w => weight w ^ 2)

/-- The zero-based carry bound is a specialization of the interval theorem. -/
theorem actual_endpoint_collision_le (S : Finset (List Bool)) (L p R : Nat)
    (source endpoint : List Bool → Nat) (weight : List Bool → K)
    (hl : ∀ w ∈ S, w.length = L)
    (ho : ∀ w ∈ S, ones w = p)
    (he : ∀ w ∈ S, 2 ^ L * endpoint w = 3 ^ p * source w + carry w)
    (hd : ∀ w ∈ S, carry w / (3 ^ p) < R) :
    (∑ a ∈ Finset.range (3 ^ p),
      (∑ w ∈ S.filter (fun w => endpoint w % (3 ^ p) = a), weight w) ^ 2) ≤
      (R : K) * ∑ w ∈ S, weight w ^ 2 := by
  exact actual_endpoint_collision_le_interval S L p 0 R source endpoint weight hl ho he
    (fun _ _ => Nat.zero_le _) (fun w hw => by simpa using hd w hw)

end CollatzShell.CarryFibers

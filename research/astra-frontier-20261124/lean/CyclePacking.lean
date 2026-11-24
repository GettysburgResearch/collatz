module

public import Mathlib.Data.Nat.ModEq
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Data.Finset.Max
public import Mathlib.Data.Fintype.Prod
public import Mathlib.Data.Fintype.Card
public import Mathlib.Data.List.Induction
public import Mathlib.Dynamics.PeriodicPts.Defs
public import Mathlib.Logic.Equiv.Fin.Rotate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Ordinary shortcut cycles with contracting binary parity blocks.
The finite index permutation may consist of several cycles. All edges are
literal ordinary branches, and the distinct-state hypothesis is used only
when converting a bound on observed states to a bound on indexed positions. -/

@[expose] public section
namespace Collatz.ElementaryPacking

def step (x : ℕ) : ℕ :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

/-- The ordinary equations themselves enforce parity and exact halving. -/
def Follows : List Bool → ℕ → ℕ → Prop
  | [], x, y => x = y
  | false :: w, x, y => ∃ z, x = 2 * z ∧ Follows w z y
  | true :: w, x, y => ∃ z, 3 * x + 1 = 2 * z ∧ Follows w z y

def ones : List Bool → ℕ
  | [] => 0
  | false :: w => ones w
  | true :: w => ones w + 1

def carry : List Bool → ℕ
  | [] => 0
  | false :: w => 2 * carry w
  | true :: w => 3 ^ ones w + 2 * carry w

def bits (n x : ℕ) : List Bool := match n with
  | 0 => []
  | k+1 => decide (x % 2 = 1) :: bits k (step x)

/-- The literal shortcut trajectory has exactly this legally realized word. -/
theorem bits_follows (n x : ℕ) : Follows (bits n x) x (step^[n] x) := by
  induction n generalizing x with
  | zero => rfl
  | succ k ih =>
    rw [Function.iterate_succ_apply]
    by_cases hx : x % 2 = 0
    · have hx' : x % 2 ≠ 1 := by omega
      simp only [bits, hx', decide_false, Follows]
      exact ⟨step x, by simp only [step, hx, ite_true]; omega, ih _⟩
    · have hx' : x % 2 = 1 := by omega
      simp only [bits, hx', decide_true, Follows]
      exact ⟨step x, by simp only [step, hx, ite_false]; omega, ih _⟩

theorem bits_length (n x : ℕ) : (bits n x).length = n := by
  induction n generalizing x with
  | zero => rfl
  | succ k ih => simp [bits, ih]

theorem follows_append {u v : List Bool} {x y z : ℕ}
    (hu : Follows u x y) (hv : Follows v y z) : Follows (u ++ v) x z := by
  induction u generalizing x with
  | nil => simpa [Follows] using hu ▸ hv
  | cons b u ih =>
    cases b <;> obtain ⟨t, ht, htail⟩ := hu <;> exact ⟨t, ht, ih htail⟩

theorem follows_affine {w : List Bool} {x y : ℕ} (h : Follows w x y) :
    2 ^ w.length * y = 3 ^ ones w * x + carry w := by
  induction w generalizing x with
  | nil => simpa [ones, carry] using h.symm
  | cons b w ih =>
    cases b
    · obtain ⟨z, rfl, hz⟩ := h
      have ht := ih hz
      simp only [List.length_cons, pow_succ, ones, carry]
      calc
        2 ^ w.length * 2 * y = 2 * (2 ^ w.length * y) := by ring
        _ = _ := by rw [ht]; ring
    · obtain ⟨z, hz, htail⟩ := h
      have ht := ih htail
      simp only [List.length_cons, ones, carry, pow_succ]
      calc
        2 ^ w.length * 2 * y = 2 * (2 ^ w.length * y) := by ring
        _ = 3 ^ ones w * (2 * z) + 2 * carry w := by rw [ht]; ring
        _ = _ := by rw [← hz]; ring

theorem ones_le_length (w : List Bool) : ones w ≤ w.length := by
  induction w with
  | nil => decide
  | cons b w ih => cases b <;> simp only [ones, List.length_cons] <;> omega

/-- The extremal carry at a given length is the one for the all-ones word. -/
theorem carry_plus_pow_le (w : List Bool) : carry w + 2 ^ w.length ≤ 3 ^ w.length := by
  induction w with
  | nil => decide
  | cons b w ih =>
    have hp : 3 ^ ones w ≤ (3 : ℕ) ^ w.length :=
      Nat.pow_le_pow_right (by decide) (ones_le_length w)
    cases b <;> simp only [carry, List.length_cons, pow_succ] <;> omega

theorem carry_lt_pow (w : List Bool) : carry w < 3 ^ w.length := by
  have h := carry_plus_pow_le w
  have hp : 0 < (2 : ℕ) ^ w.length := by positivity
  omega

theorem same_future {w : List Bool} {x y u v : ℕ}
    (hx : Follows w x u) (hy : Follows w y v) : x ≡ y [MOD 2 ^ w.length] := by
  have he : 2 ^ w.length * u ≡ 2 ^ w.length * v [MOD 2 ^ w.length] := by
    simp [Nat.ModEq]
  rw [follows_affine hx, follows_affine hy] at he
  have hcop : Nat.Coprime ((2 : ℕ) ^ w.length) (3 ^ ones w) :=
    (by decide : Nat.Coprime 2 3).pow _ _
  exact (he.add_right_cancel' _).cancel_left_of_coprime hcop

variable {ι : Type*} [Fintype ι] [Nonempty ι]

/-- Given a possibly variable-length contracting partition, every cyclic boundary
satisfies an integer affine inequality at some represented word. -/
theorem cycle_barrier (next : ι ≃ ι) (x : ι → ℕ) (word : ι → List Bool)
    (legal : ∀ i, Follows (word i) (x i) (x (next i)))
    (contracts : ∀ i, 3 ^ ones (word i) < (2 : ℕ) ^ (word i).length)
    (i : ι) : ∃ j, 2 ^ (word j).length * x i ≤ 3 ^ ones (word j) * x i + carry (word j) := by
  classical
  obtain ⟨m, _, hm⟩ := Finset.exists_max_image Finset.univ x Finset.univ_nonempty
  obtain ⟨j, hj⟩ := next.surjective m
  refine ⟨j, ?_⟩
  have hedge := follows_affine (legal j)
  rw [hj] at hedge
  have hpred := Nat.mul_le_mul_left (3 ^ ones (word j)) (hm j (Finset.mem_univ _))
  have hdiff := Nat.mul_le_mul_left (2 ^ (word j).length - 3 ^ ones (word j))
    (hm i (Finset.mem_univ _))
  have hN : 2 ^ (word j).length - 3 ^ ones (word j) + 3 ^ ones (word j) =
      (2 : ℕ) ^ (word j).length := Nat.sub_add_cancel (contracts j).le
  have hmi := congrArg (fun z : ℕ => z * x i) hN
  have hmm := congrArg (fun z : ℕ => z * x m) hN
  rw [Nat.add_mul] at hmi hmm
  omega

theorem boundary_lt_pow (next : ι ≃ ι) (x : ι → ℕ) (word : ι → List Bool)
    (legal : ∀ i, Follows (word i) (x i) (x (next i)))
    (contracts : ∀ i, 3 ^ ones (word i) < (2 : ℕ) ^ (word i).length)
    {A : ℕ} (lengths : ∀ i, (word i).length ≤ A) (i : ι) : x i < 3 ^ A := by
  obtain ⟨j, h⟩ := cycle_barrier next x word legal contracts i
  have hstep := Nat.mul_le_mul_right (x i) (Nat.succ_le_of_lt (contracts j))
  rw [Nat.succ_mul] at hstep
  have hc := carry_lt_pow (word j)
  have hA : 3 ^ (word j).length ≤ (3 : ℕ) ^ A := Nat.pow_le_pow_right (by decide) (lengths j)
  omega

/-- Two legally equal consecutive atoms identify their boundary states. -/
theorem two_words_identify (next : ι ≃ ι) (x : ι → ℕ) (word : ι → List Bool)
    (legal : ∀ i, Follows (word i) (x i) (x (next i)))
    (contracts : ∀ i, 3 ^ ones (word i) < (2 : ℕ) ^ (word i).length)
    {A : ℕ} (lengths : ∀ i, (word i).length = A) {i j : ι}
    (hw : word i = word j) (hv : word (next i) = word (next j)) : x i = x j := by
  have h := follows_append (legal i) (legal (next i))
  have h' := follows_append (legal j) (legal (next j))
  rw [← hw, ← hv] at h'
  have hc := same_future h h'
  rw [List.length_append, lengths, lengths] at hc
  have hbase : (3 : ℕ)^A ≤ 2^(A+A) := by
    rw [pow_add, ← mul_pow]
    exact Nat.pow_le_pow_left (by decide) _
  have hb := boundary_lt_pow next x word legal contracts (fun k => (lengths k).le)
  exact hc.eq_of_lt_of_lt ((hb i).trans_le hbase) ((hb j).trans_le hbase)

/-- A primitive block cycle has distinct boundary states. With K dictionary
labels its index size is at most K², even with different odd counts per label. -/
theorem card_le_dictionary_sq {κ : Type*} [Fintype κ]
    (next : ι ≃ ι) (x : ι → ℕ) (atom : κ → List Bool) (label : ι → κ)
    (distinct : Function.Injective x)
    (legal : ∀ i, Follows (atom (label i)) (x i) (x (next i)))
    (contracts : ∀ i, 3 ^ ones (atom (label i)) < (2 : ℕ) ^ (atom (label i)).length)
    {A : ℕ} (lengths : ∀ i, (atom (label i)).length = A) :
    Fintype.card ι ≤ (Fintype.card κ)^2 := by
  have hinj : Function.Injective (fun i => (label i, label (next i))) := by
    intro i j h
    apply distinct
    apply two_words_identify next x (fun k => atom (label k)) legal contracts lengths
    · exact congrArg atom (congrArg Prod.fst h)
    · exact congrArg atom (congrArg Prod.snd h)
  simpa [Fintype.card_prod, pow_two] using Fintype.card_le_of_injective _ hinj

/-- Entry point for one literal ordinary starting value. The minimal period is
that of the A-step return map. It is measured in blocks. -/
theorem orbit_period_le_dictionary_sq (n A : ℕ) (dictionary : Finset (List Bool))
    (contracts : ∀ w ∈ dictionary, 3 ^ ones w < (2 : ℕ) ^ A)
    (contains : ∀ t < Function.minimalPeriod (step^[A]) n,
      bits A ((step^[A])^[t] n) ∈ dictionary) :
    Function.minimalPeriod (step^[A]) n ≤ dictionary.card ^ 2 := by
  classical
  let f := step^[A]
  let r := Function.minimalPeriod f n
  change r ≤ _
  by_cases hr : r = 0
  · simp [hr]
  let : NeZero r := ⟨hr⟩
  let x (i : Fin r) := f^[i.val] n
  let label (i : Fin r) : ↥dictionary := ⟨bits A (x i), contains i i.isLt⟩
  have hn (i : Fin r) : x (finRotate r i) = f (x i) := by
    have hval : (finRotate r i).val = (i.val + 1) % r := by
      rw [finRotate_apply, Fin.val_add]
      change (i.val + 1 % r) % r = _
      exact Nat.add_mod_mod _ _ _
    change f^[(finRotate r i).val] n = f (f^[i.val] n)
    rw [hval]
    exact (Function.iterate_mod_minimalPeriod_eq (f := f) (x := n)).trans
      (Function.iterate_succ_apply' f _ _)
  have hd : Function.Injective x := by
    intro i j h
    exact Fin.ext ((Function.iterate_eq_iterate_iff_of_lt_minimalPeriod i.isLt j.isLt).mp h)
  have hlegal (i : Fin r) : Follows (label i).val (x i) (x (finRotate r i)) := by
    rw [hn]
    exact bits_follows A (x i)
  have hlen (i : Fin r) : (label i).val.length = A := bits_length A (x i)
  have hc (i : Fin r) : 3 ^ ones (label i).val < (2 : ℕ) ^ (label i).val.length := by
    rw [hlen]
    exact contracts _ (label i).property
  simpa only [Fintype.card_fin, Fintype.card_coe] using
    card_le_dictionary_sq (finRotate r) x Subtype.val label hd hlegal hc hlen

/-- No proper prefix has already had its first coefficient crossing. -/
def BeforeCrossing (w : List Bool) : Prop :=
  ∀ u v : List Bool, w = u ++ v → v ≠ [] → 2 ^ u.length ≤ (3 : ℕ) ^ ones u

theorem ones_append (u v : List Bool) : ones (u ++ v) = ones u + ones v := by
  induction u with
  | nil => simp [ones]
  | cons b u ih =>
    cases b
    · simp only [List.cons_append, ones, ih]
    · simp only [List.cons_append, ones, ih]
      omega

theorem carry_append (u v : List Bool) :
    carry (u ++ v) = 3 ^ ones v * carry u + 2 ^ u.length * carry v := by
  induction u with
  | nil => simp [carry]
  | cons b u ih =>
    cases b <;> simp only [List.cons_append, carry, ih, ones_append, pow_add,
      List.length_cons, pow_succ] <;> ring

theorem beforeCrossing_carry (w : List Bool) (hc : BeforeCrossing w) :
    3 * carry w ≤ ones w * 3 ^ ones w := by
  induction w using List.reverseRecOn with
  | nil => decide
  | append_singleton u b ih =>
    have hu : BeforeCrossing u := by
      intro w v hv _
      apply hc w (v ++ [b])
      · rw [hv, List.append_assoc]
      · simp
    have hi := ih hu
    have hl := hc u [b] rfl (by simp)
    cases b <;> simp only [carry_append, ones_append, carry, ones, pow_zero, pow_succ,
      Nat.add_zero, Nat.zero_add, Nat.mul_zero, Nat.mul_one, Nat.one_mul] <;>
      nlinarith only [hi, hl]

/-- Maximum first-crossing carry at a fixed odd count. The recurrence uses the
largest possible binary position of the next odd bit. -/
def crossingCarry : ℕ → ℕ
  | 0 => 0
  | p+1 => 3 * crossingCarry p + 2 ^ (3 ^ p).log2

def crossingLength (p : ℕ) : ℕ := (3 ^ p).log2 + 1

def centerFloor (p : ℕ) : ℕ :=
  crossingCarry p / (2 ^ crossingLength p - 3 ^ p)

theorem firstCrossing_length (w : List Bool) (hc : BeforeCrossing w)
    (contracts : 3 ^ ones w < (2 : ℕ) ^ w.length) : w.length = crossingLength (ones w) := by
  induction w using List.reverseRecOn with
  | nil => simp [ones] at contracts
  | append_singleton u b _ =>
    have hpre := hc u [b] rfl (by simp)
    cases b
    · simp only [List.length_append, List.length_cons, List.length_nil, Nat.zero_add,
        ones_append, ones, Nat.add_zero] at contracts ⊢
      unfold crossingLength
      rw [(Nat.log2_eq_iff (by positivity)).2 ⟨hpre, contracts⟩]
    · simp only [List.length_append, List.length_cons, List.length_nil, Nat.zero_add,
        ones_append, ones, pow_succ] at contracts
      omega

theorem beforeCrossing_envelope (w : List Bool) (hc : BeforeCrossing w) :
    carry w ≤ crossingCarry (ones w) := by
  induction w using List.reverseRecOn with
  | nil => decide
  | append_singleton u b ih =>
    have hu : BeforeCrossing u := by
      intro w v hv _
      apply hc w (v ++ [b])
      · rw [hv, List.append_assoc]
      · simp
    have hi := ih hu
    have hpre := hc u [b] rfl (by simp)
    have hpos := (Nat.le_log2 (by positivity : (3 : ℕ) ^ ones u ≠ 0)).mpr hpre
    have hbit := Nat.pow_le_pow_right (by decide : 0 < 2) hpos
    cases b
    · simpa [carry_append, ones_append, carry, ones] using hi
    · simp only [carry_append, ones_append, carry, ones, pow_zero, pow_succ, Nat.add_zero,
        Nat.zero_add, Nat.mul_zero, Nat.mul_one, Nat.one_mul, crossingCarry]
      omega

/-- A written or computed ceiling for the scalar floor centers only requires
the weights actually represented in the cycle. -/
theorem firstCrossing_center_bound (next : ι ≃ ι) (x : ι → ℕ) (word : ι → List Bool)
    (legal : ∀ i, Follows (word i) (x i) (x (next i)))
    (contracts : ∀ i, 3 ^ ones (word i) < (2 : ℕ) ^ (word i).length)
    (prefixes : ∀ i, BeforeCrossing (word i)) (i : ι) :
    ∃ j, x i ≤ centerFloor (ones (word j)) := by
  obtain ⟨j, hb⟩ := cycle_barrier next x word legal contracts i
  refine ⟨j, ?_⟩
  unfold centerFloor
  rw [← firstCrossing_length _ (prefixes j) (contracts j)]
  apply (Nat.le_div_iff_mul_le (Nat.sub_pos_of_lt (contracts j))).mpr
  have hN := Nat.sub_add_cancel (contracts j).le
  have hm := congrArg (fun z : ℕ => z * x i) hN
  rw [Nat.add_mul] at hm
  rw [Nat.mul_comm (x i)]
  have hend := beforeCrossing_envelope _ (prefixes j)
  omega

/-- Elementary height gate for a cyclic partition of first coefficient-crossing
words. A zero-bit word has zero ones and is covered by the same inequality. -/
theorem firstCrossing_boundary (next : ι ≃ ι) (x : ι → ℕ) (word : ι → List Bool)
    (legal : ∀ i, Follows (word i) (x i) (x (next i)))
    (contracts : ∀ i, 3 ^ ones (word i) < (2 : ℕ) ^ (word i).length)
    (prefixes : ∀ i, BeforeCrossing (word i)) {A P : ℕ} (hP : 0 < P)
    (lengths : ∀ i, (word i).length ≤ A) (weights : ∀ i, ones (word i) ≤ P)
    (i : ι) : 3 * x i < P * 2 ^ A := by
  obtain ⟨j, hb⟩ := cycle_barrier next x word legal contracts i
  have hstep := Nat.mul_le_mul_right (x i) (Nat.succ_le_of_lt (contracts j))
  rw [Nat.succ_mul] at hstep
  have hbound : x i ≤ carry (word j) := by omega
  calc
    3 * x i ≤ 3 * carry (word j) := Nat.mul_le_mul_left _ hbound
    _ ≤ ones (word j) * 3 ^ ones (word j) := beforeCrossing_carry _ (prefixes j)
    _ ≤ P * 3 ^ ones (word j) := Nat.mul_le_mul_right _ (weights j)
    _ < P * 2 ^ A := Nat.mul_lt_mul_of_pos_left ((contracts j).trans_le
      (Nat.pow_le_pow_right (by decide) (lengths j))) hP

/-- The packed binary length of a primitive positive first-crossing partition. -/
theorem firstCrossing_period (next : ι ≃ ι) (x : ι → ℕ) (word : ι → List Bool)
    (positive : ∀ i, 0 < x i) (distinct : Function.Injective x)
    (legal : ∀ i, Follows (word i) (x i) (x (next i)))
    (contracts : ∀ i, 3 ^ ones (word i) < (2 : ℕ) ^ (word i).length)
    (prefixes : ∀ i, BeforeCrossing (word i)) {A P : ℕ} (hA : 0 < A) (hP : 0 < P)
    (lengths : ∀ i, (word i).length ≤ A) (weights : ∀ i, ones (word i) ≤ P) :
    3 * (∑ i, (word i).length) < A * (P * 2 ^ A) := by
  classical
  obtain ⟨m, _, hm⟩ := Finset.exists_max_image Finset.univ x Finset.univ_nonempty
  let ix (i : ι) : Fin (x m) :=
    ⟨x i - 1, by have := hm i (Finset.mem_univ _); have := positive i; omega⟩
  have hinj : Function.Injective ix := by
    intro i j h
    have hv : x i - 1 = x j - 1 := congrArg Fin.val h
    apply distinct
    have := positive i
    have := positive j
    omega
  have hcard : Fintype.card ι ≤ x m := by
    simpa only [Fintype.card_fin] using Fintype.card_le_of_injective ix hinj
  have hlen : (∑ i, (word i).length) ≤ Fintype.card ι * A := by
    calc
      _ ≤ ∑ _i : ι, A := Finset.sum_le_sum (fun i _ => lengths i)
      _ = _ := by simp
  calc
    3 * (∑ i, (word i).length) ≤ 3 * (Fintype.card ι * A) := Nat.mul_le_mul_left _ hlen
    _ = A * (3 * Fintype.card ι) := by ring
    _ ≤ A * (3 * x m) := Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ hcard)
    _ < A * (P * 2 ^ A) := Nat.mul_lt_mul_of_pos_left
      (firstCrossing_boundary next x word legal contracts prefixes hP lengths weights m) hA

#print axioms bits_follows
#print axioms bits_length
#print axioms follows_append
#print axioms follows_affine
#print axioms ones_le_length
#print axioms carry_plus_pow_le
#print axioms carry_lt_pow
#print axioms same_future
#print axioms cycle_barrier
#print axioms boundary_lt_pow
#print axioms two_words_identify
#print axioms card_le_dictionary_sq
#print axioms orbit_period_le_dictionary_sq
#print axioms ones_append
#print axioms carry_append
#print axioms beforeCrossing_carry
#print axioms firstCrossing_length
#print axioms beforeCrossing_envelope
#print axioms firstCrossing_center_bound
#print axioms firstCrossing_boundary
#print axioms firstCrossing_period

end Collatz.ElementaryPacking

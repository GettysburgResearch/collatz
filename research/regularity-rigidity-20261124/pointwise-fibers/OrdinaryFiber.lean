module

public import LeanCore
public import Mathlib.Data.Finset.Card
public import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Ring

/-! Ordinary inverse fibers at a fixed physical clock. Every bit below is in chronological
order. The inverse theorem enforces each physical parity by decoding one division at a time. -/

@[expose] public section

namespace OrdinaryFiber

open RegularityRigidity (T)

/-- The accumulated affine numerator for a chronological source word. -/
def carry : List Bool → ℕ
  | [] => 0
  | false :: w => 2 * carry w
  | true :: w => 3 ^ w.count true + 2 * carry w

/-- The first `e` parity bits of the actual signed integer orbit. -/
def parityWord : ℕ → ℤ → List Bool
  | 0, _ => []
  | e + 1, x => decide (x % 2 = 1) :: parityWord e (T x)

private def numerator (b : Bool) (x : ℤ) : ℤ := if b then 3 * x + 1 else x

private theorem three_pow_mod_two (k : ℕ) : (3 : ℤ) ^ k % 2 = 1 := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [pow_succ, Int.mul_emod, ih]
    decide

private theorem numerator_even_iff (b : Bool) (x : ℤ) :
    numerator b x % 2 = 0 ↔ decide (x % 2 = 1) = b := by
  cases b <;> simp [numerator]
  omega

private theorem numerator_half {b : Bool} {x : ℤ} (h : decide (x % 2 = 1) = b) :
    numerator b x / 2 = T x := by
  subst b
  by_cases he : x % 2 = 0
  · simp [T, numerator, he]
  · have ho : x % 2 = 1 := by omega
    simp [T, numerator, ho]

/-- The odd coefficient makes the parity test a consequence of the cleared equation. -/
private theorem decode_half (a r c t : ℤ) (ha : a % 2 = 1) :
    a * r + 2 * c = 2 * t ↔ r % 2 = 0 ∧ a * (r / 2) + c = t := by
  constructor
  · intro h
    have he : (a * r + 2 * c) % 2 = 0 := by rw [h]; omega
    rw [Int.add_emod, Int.mul_emod a r, ha, one_mul] at he
    have hr : r % 2 = 0 := by omega
    have hm : 2 * (r / 2) = r := by omega
    have hh : 2 * (a * (r / 2) + c) = 2 * t := calc
      _ = a * (2 * (r / 2)) + 2 * c := by ring
      _ = _ := by rw [hm, h]
    exact ⟨hr, by omega⟩
  · rintro ⟨hr, h⟩
    have hm : 2 * (r / 2) = r := by omega
    calc
      a * r + 2 * c = a * (2 * (r / 2)) + 2 * c := by rw [hm]
      _ = 2 * (a * (r / 2) + c) := by ring
      _ = _ := by rw [h]

private theorem cons_affine (b : Bool) (w : List Bool) (x : ℤ) :
    (3 : ℤ) ^ ((b :: w).count true) * x + carry (b :: w) =
      (3 : ℤ) ^ w.count true * numerator b x + 2 * carry w := by
  cases b <;> simp [numerator, carry, pow_succ]
  ring

/-- Exact equality is equivalent to both the physical parity word and the prescribed endpoint. -/
theorem affine_iff_orbit (w : List Bool) (x q : ℤ) :
    (3 : ℤ) ^ w.count true * x + carry w = (2 : ℤ) ^ w.length * q ↔
      parityWord w.length x = w ∧ (T^[w.length]) x = q := by
  induction w generalizing x with
  | nil => simp [parityWord, carry]
  | cons b w ih =>
    rw [cons_affine, List.length_cons, pow_succ, mul_right_comm _ 2 q, mul_comm _ 2,
      decode_half _ _ _ _ (three_pow_mod_two _), numerator_even_iff,
      parityWord, Function.iterate_succ_apply, List.cons.injEq]
    constructor
    · rintro ⟨hb, ht⟩
      rw [numerator_half hb] at ht
      obtain ⟨hw, hq⟩ := (ih (T x)).mp ht
      exact ⟨⟨hb, hw⟩, hq⟩
    · rintro ⟨⟨hb, hw⟩, hq⟩
      exact ⟨hb, by rw [numerator_half hb]; exact (ih (T x)).mpr ⟨hw, hq⟩⟩

/-- The integral inverse to a word at the fixed ordinary target `q`. -/
def inverse (w : List Bool) (q : ℤ) : ℤ :=
  ((2 : ℤ) ^ w.length * q - carry w) / (3 : ℤ) ^ w.count true

theorem inverse_iff_dvd (w : List Bool) (q : ℤ) :
    (3 : ℤ) ^ w.count true ∣ (2 : ℤ) ^ w.length * q - carry w ↔
      parityWord w.length (inverse w q) = w ∧ (T^[w.length]) (inverse w q) = q := by
  rw [← affine_iff_orbit, ← eq_sub_iff_add_eq]
  unfold inverse
  constructor
  · intro h
    rw [mul_comm, Int.ediv_mul_cancel h]
  · intro h
    exact ⟨_, h.symm⟩

/-- One further ternary digit decides whether the integral inverse is a unit. -/
theorem unit_inverse_iff (w : List Bool) (q : ℤ) :
    ((3 : ℤ) ^ w.count true ∣ (2 : ℤ) ^ w.length * q - carry w) ∧
      ¬ (3 : ℤ) ^ (w.count true + 1) ∣ (2 : ℤ) ^ w.length * q - carry w ↔
    (parityWord w.length (inverse w q) = w ∧ (T^[w.length]) (inverse w q) = q) ∧
      ¬ (3 : ℤ) ∣ inverse w q := by
  have extra (hd : (3 : ℤ) ^ w.count true ∣ (2 : ℤ) ^ w.length * q - carry w) :
      (3 : ℤ) ^ (w.count true + 1) ∣ (2 : ℤ) ^ w.length * q - carry w ↔
        3 ∣ inverse w q := by
    have h := (affine_iff_orbit ..).mpr ((inverse_iff_dvd w q).mp hd)
    rw [← eq_sub_iff_add_eq] at h
    rw [pow_succ, ← h]
    exact mul_dvd_mul_iff_left (pow_ne_zero _ (by decide : (3 : ℤ) ≠ 0))
  constructor
  · rintro ⟨hd, hn⟩
    exact ⟨(inverse_iff_dvd w q).mp hd, (extra hd).not.mp hn⟩
  · rintro ⟨h, hn⟩
    have hd := (inverse_iff_dvd w q).mpr h
    exact ⟨hd, (extra hd).not.mpr hn⟩

/-- For positive target and offset at most one half, the integral inverse attaches
in the closed height interval from one half to one times the target scale. -/
theorem inverse_height (w : List Bool) (q : ℤ) (hq : 1 ≤ q)
    (hd : (3 : ℤ) ^ w.count true ∣ (2 : ℤ) ^ w.length * q - carry w)
    (hb : 2 * carry w ≤ 2 ^ w.length) :
    0 < inverse w q ∧
      (2 : ℤ) ^ w.length * q ≤ 2 * ((3 : ℤ) ^ w.count true * inverse w q) ∧
      (3 : ℤ) ^ w.count true * inverse w q ≤ (2 : ℤ) ^ w.length * q := by
  have h := (affine_iff_orbit ..).mpr ((inverse_iff_dvd w q).mp hd)
  have h2 : 0 < (2 : ℤ) ^ w.length := pow_pos (by decide) _
  have h3 : 0 < (3 : ℤ) ^ w.count true := pow_pos (by decide) _
  have hl : (2 : ℤ) ^ w.length ≤ (2 : ℤ) ^ w.length * q := by
    simpa using mul_le_mul_of_nonneg_left hq h2.le
  have hb' : 2 * (carry w : ℤ) ≤ (2 : ℤ) ^ w.length := by exact_mod_cast hb
  have hc : 0 ≤ (carry w : ℤ) := Int.natCast_nonneg _
  exact ⟨pos_of_mul_pos_right (by omega : 0 < (3 : ℤ) ^ w.count true * inverse w q) h3.le,
    by omega, by omega⟩

/-- Equal clocks, equal odd counts and the fivefold carry relation attach BOTH word arms. -/
theorem paired_decoder (u v : List Bool) (x q : ℤ)
    (he : v.length = u.length) (hp : v.count true = u.count true) :
    ((3 : ℤ) ^ u.count true * x + carry u = (2 : ℤ) ^ u.length * q ∧
      carry v = 5 * carry u) ↔
    (parityWord u.length x = u ∧ (T^[u.length]) x = q) ∧
      (parityWord v.length (5 * x) = v ∧ (T^[v.length]) (5 * x) = 5 * q) := by
  rw [← affine_iff_orbit, ← affine_iff_orbit, he, hp]
  constructor
  · rintro ⟨h, hc⟩
    refine ⟨h, ?_⟩
    rw [hc, Nat.cast_mul, Nat.cast_ofNat]
    calc
      _ = 5 * ((3 : ℤ) ^ u.count true * x + carry u) := by ring
      _ = _ := by rw [h]; ring
  · rintro ⟨h, hv⟩
    refine ⟨h, ?_⟩
    have h' : (carry v : ℤ) = 5 * carry u := by
      calc
        _ = (2 : ℤ) ^ u.length * (5 * q) - 3 ^ u.count true * (5 * x) := by omega
        _ = 5 * ((2 : ℤ) ^ u.length * q - 3 ^ u.count true * x) := by ring
        _ = _ := by rw [← h]; ring
    exact_mod_cast h'

private theorem carry_mod_two (b : Bool) (w : List Bool) :
    carry (b :: w) % 2 = (if b then 1 else 0) := by
  cases b
  · simp [carry]
  · simp [carry, Nat.add_mod, Nat.pow_mod 3 _ 2]

/-- At known length and odd count, the carry identifies the chronological word, including zeros. -/
theorem carry_injective {u v : List Bool} (he : u.length = v.length)
    (hp : u.count true = v.count true) (hc : carry u = carry v) : u = v := by
  induction u generalizing v with
  | nil => simpa using he.symm
  | cons b u ih =>
    cases v with
    | nil => simp at he
    | cons d v =>
      have hb := congrArg (fun n => n % 2) hc
      change carry (b :: u) % 2 = carry (d :: v) % 2 at hb
      rw [carry_mod_two, carry_mod_two] at hb
      have hbd : b = d := by cases b <;> cases d <;> simp_all
      subst d
      have hlength : u.length = v.length := by simpa using he
      have hcount : u.count true = v.count true := by simpa [List.count_cons] using hp
      have hcarry : carry u = carry v := by
        cases b <;> simp only [carry, hcount] at hc <;> omega
      exact congrArg (List.cons b) (ih hlength hcount hcarry)

/-- A finite family with carry at most K in one endpoint residue has at most
`⌊K / 3^p⌋ + 1` members, uniformly in that residue and in the physical clock. -/
theorem fixed_clock_ceiling (s : Finset (List Bool)) (e p K r : ℕ)
    (hs : ∀ w ∈ s, w.length = e ∧ w.count true = p ∧ carry w ≤ K ∧ carry w % 3 ^ p = r) :
    s.card ≤ K / 3 ^ p + 1 := by
  have h := Finset.card_le_card_of_injOn (s := s) (t := Finset.range (K / 3 ^ p + 1))
      (fun w => carry w / 3 ^ p) (by
        intro w hw
        exact Finset.mem_range.mpr (Nat.lt_succ_of_le (Nat.div_le_div_right (hs w hw).2.2.1))) (by
        intro u hu v hv heq
        change carry u / 3 ^ p = carry v / 3 ^ p at heq
        obtain ⟨hlu, hpu, _, hru⟩ := hs u hu
        obtain ⟨hlv, hpv, _, hrv⟩ := hs v hv
        apply carry_injective (hlu.trans hlv.symm) (hpu.trans hpv.symm)
        calc
          carry u = carry u % 3 ^ p + 3 ^ p * (carry u / 3 ^ p) := (Nat.mod_add_div ..).symm
          _ = carry v % 3 ^ p + 3 ^ p * (carry v / 3 ^ p) := by rw [hru, hrv, heq]
          _ = carry v := Nat.mod_add_div ..)
  simpa using h

/-- A concrete finite list of hypotheses on a source word and its companion. The fine
ternary test uses the prescribed ordinary integer q at exactly one extra ternary digit. -/
structure PairedWord (e p : ℕ) (q : ℤ) (u v : List Bool) : Prop where
  length_eq : u.length = e
  odd_count : u.count true = p
  starts_odd : u.head? = some true
  same_length : v.length = u.length
  same_count : v.count true = u.count true
  companion_carry : carry v = 5 * carry u
  half_offset : 2 * carry u ≤ 2 ^ u.length
  integral : (3 : ℤ) ^ u.count true ∣ (2 : ℤ) ^ u.length * q - carry u
  unit : ¬ (3 : ℤ) ^ (u.count true + 1) ∣ (2 : ℤ) ^ u.length * q - carry u

theorem odd_source_of_word (w : List Bool) (x : ℤ) (ho : w.head? = some true)
    (h : parityWord w.length x = w) : x % 2 = 1 := by
  cases w with
  | nil => simp at ho
  | cons b w =>
    have hb : b = true := by simpa using ho
    subst b
    change decide (x % 2 = 1) :: parityWord w.length (T x) = true :: w at h
    exact of_decide_eq_true (List.cons.inj h).1

/-- For one fixed positive ordinary target the image of a finite compatible word family
has the same cardinality. Every start is positive, odd, a ternary unit, in the indicated
half-scale height interval, and both ordinary arms land at the supplied targets at clock e. -/
theorem ordinary_paired_fiber (s : Finset (List Bool)) (companion : List Bool → List Bool)
    (e p : ℕ) (q : ℤ) (hq : 1 ≤ q)
    (hs : ∀ u ∈ s, PairedWord e p q u (companion u)) :
    let starts := s.image (fun u => inverse u q)
    starts.card = s.card ∧ ∀ x ∈ starts,
      0 < x ∧ x % 2 = 1 ∧ ¬ (3 : ℤ) ∣ x ∧
      (T^[e]) x = q ∧ (T^[e]) (5 * x) = 5 * q ∧
      (2 : ℤ) ^ e * q ≤ 2 * ((3 : ℤ) ^ p * x) ∧
      (3 : ℤ) ^ p * x ≤ (2 : ℤ) ^ e * q := by
  classical
  constructor
  · apply Finset.card_image_of_injOn
    intro u hu v hv hx
    change inverse u q = inverse v q at hx
    have h := hs u hu
    have k := hs v hv
    have hword := ((inverse_iff_dvd u q).mp h.integral).1
    have kword := ((inverse_iff_dvd v q).mp k.integral).1
    rw [h.length_eq, hx] at hword
    rw [k.length_eq] at kword
    exact hword.symm.trans kword
  · intro x hx
    obtain ⟨u, hu, rfl⟩ := Finset.mem_image.mp hx
    have h := hs u hu
    have ⟨hstart, hunit⟩ := (unit_inverse_iff u q).mp ⟨h.integral, h.unit⟩
    have ha := (affine_iff_orbit ..).mpr hstart
    have hend := ((paired_decoder u (companion u) (inverse u q) q h.same_length h.same_count).mp
      ⟨ha, h.companion_carry⟩).2.2
    have ⟨hpos, hlo, hhi⟩ := inverse_height u q hq h.integral h.half_offset
    have hodd := odd_source_of_word u (inverse u q) h.starts_odd hstart.1
    rw [h.same_length, h.length_eq] at hend
    rw [h.length_eq] at hstart
    rw [h.length_eq, h.odd_count] at hlo hhi
    exact ⟨hpos, hodd, hunit, hstart.2, hend, hlo, hhi⟩

/-- The ceiling applies directly to chronological words that reach one specified ordinary
integer at fixed clocks. The common carry residue follows from the physical orbit. -/
theorem ordinary_fiber_ceiling (s : Finset (List Bool)) (e p K : ℕ) (q : ℤ)
    (hs : ∀ w ∈ s, w.length = e ∧ w.count true = p ∧ carry w ≤ K ∧
      ∃ x : ℤ, parityWord w.length x = w ∧ (T^[w.length]) x = q) :
    s.card ≤ K / 3 ^ p + 1 := by
  apply fixed_clock_ceiling s e p K (((2 : ℤ) ^ e * q % (3 : ℤ) ^ p).toNat)
  intro w hw
  obtain ⟨he, hp, hK, x, hx⟩ := hs w hw
  refine ⟨he, hp, hK, ?_⟩
  have hf := (affine_iff_orbit w x q).mpr hx
  rw [he, hp] at hf
  have hm : ((carry w % 3 ^ p : ℕ) : ℤ) = (2 : ℤ) ^ e * q % (3 : ℤ) ^ p := by
    rw [Int.natCast_emod, Nat.cast_pow, Nat.cast_ofNat, ← hf, Int.mul_add_emod_self_left]
  exact_mod_cast congrArg Int.toNat hm

#print axioms three_pow_mod_two
#print axioms numerator_even_iff
#print axioms numerator_half
#print axioms decode_half
#print axioms cons_affine
#print axioms affine_iff_orbit
#print axioms inverse_iff_dvd
#print axioms unit_inverse_iff
#print axioms inverse_height
#print axioms paired_decoder
#print axioms carry_mod_two
#print axioms carry_injective
#print axioms fixed_clock_ceiling
#print axioms odd_source_of_word
#print axioms ordinary_paired_fiber
#print axioms ordinary_fiber_ceiling

end OrdinaryFiber

import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Basic.Real.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.Normed.Ring.InfiniteSum
import Mathlib.Analysis.Normed.Group.Tannery
import Mathlib.Analysis.PSeries
import Mathlib.Tactic

/-!
Exact source-cylinder research for the accelerated positive odd map.
No convergence estimate is assumed in the definitions below.
-/

namespace CollatzPrimitiveSurvival

noncomputable section

set_option maxHeartbeats 200000

def valuation (n : ℕ) : ℕ := (3 * n + 1).factorization 2
def oddStep (n : ℕ) : ℕ := (3 * n + 1) / 2 ^ valuation n

theorem oddStep_pos (n : ℕ) : 0 < oddStep n := by
  exact Nat.ordCompl_pos 2 (by omega : 3 * n + 1 ≠ 0)

theorem oddStep_odd (n : ℕ) : oddStep n % 2 = 1 := by
  have h := Nat.not_dvd_ordCompl Nat.prime_two (by omega : 3 * n + 1 ≠ 0)
  change ¬ 2 ∣ oddStep n at h
  omega

theorem oddStep_identity (n : ℕ) : 2 ^ valuation n * oddStep n = 3 * n + 1 := by
  exact Nat.ordProj_mul_ordCompl_eq_self (3 * n + 1) 2

theorem valuation_pos {n : ℕ} (hn : n % 2 = 1) : 0 < valuation n := by
  have hd : 2 ∣ 3 * n + 1 := by omega
  exact Nat.Prime.dvd_iff_one_le_factorization Nat.prime_two (by omega) |>.mp hd

def total : List ℕ → ℕ
  | [] => 0
  | a :: w => a + total w

def offset : List ℕ → ℕ
  | [] => 0
  | a :: w => 3 ^ w.length + 2 ^ a * offset w

def Valid (w : List ℕ) : Prop := ∀ a ∈ w, 0 < a

def Run : List ℕ → ℕ → ℕ → Prop
  | [], n, r => n = r
  | a :: w, n, r => ∃ m, 3 * n + 1 = 2 ^ a * m ∧ m % 2 = 1 ∧ Run w m r

def orbit : ℕ → ℕ → ℕ
  | 0, n => n
  | q + 1, n => orbit q (oddStep n)

def trace : ℕ → ℕ → List ℕ
  | 0, _ => []
  | q + 1, n => valuation n :: trace q (oddStep n)

theorem trace_length (q n : ℕ) : (trace q n).length = q := by
  induction q generalizing n with
  | zero => rfl
  | succ q ih => simp [trace, ih]

theorem trace_valid {n : ℕ} (hn : n % 2 = 1) (q : ℕ) : Valid (trace q n) := by
  induction q generalizing n with
  | zero => simp [Valid, trace]
  | succ q ih =>
    intro a ha
    simp only [trace, List.mem_cons] at ha
    rcases ha with rfl | ha
    · exact valuation_pos hn
    · exact ih (oddStep_odd n) a ha

theorem run_trace (q n : ℕ) : Run (trace q n) n (orbit q n) := by
  induction q generalizing n with
  | zero => rfl
  | succ q ih =>
    exact ⟨oddStep n, (oddStep_identity n).symm, oddStep_odd n, ih _⟩

theorem run_affine {w : List ℕ} {n r : ℕ} (h : Run w n r) :
    2 ^ total w * r = 3 ^ w.length * n + offset w := by
  induction w generalizing n with
  | nil => simpa [Run, total, offset] using h.symm
  | cons a w ih =>
    obtain ⟨m, hm, _, hr⟩ := h
    have hw := ih hr
    simp only [total, offset, List.length_cons, pow_add, pow_succ]
    calc
      2 ^ a * 2 ^ total w * r = 2 ^ a * (2 ^ total w * r) := by ring
      _ = 2 ^ a * (3 ^ w.length * m + offset w) := by rw [hw]
      _ = 3 ^ w.length * (2 ^ a * m) + 2 ^ a * offset w := by ring
      _ = _ := by rw [← hm]; ring

theorem valid_total {w : List ℕ} (hw : Valid w) : w.length ≤ total w := by
  induction w with
  | nil => simp [total]
  | cons a w ih =>
    have ha := hw a (by simp)
    have hv : Valid w := fun b hb => hw b (by simp [hb])
    have hi := ih hv
    simp only [List.length_cons, total]
    omega

theorem total_append (v w : List ℕ) : total (v ++ w) = total v + total w := by
  induction v with
  | nil => simp [total]
  | cons a v ih => simp [total, ih, Nat.add_assoc]

theorem offset_append (v w : List ℕ) :
    offset (v ++ w) = 3 ^ w.length * offset v + 2 ^ total v * offset w := by
  induction v with
  | nil => simp [offset, total]
  | cons a v ih =>
    simp only [List.cons_append, offset, List.length_append, total, pow_add, ih]
    ring

theorem run_append {v w : List ℕ} {n m r : ℕ} (hv : Run v n m) (hw : Run w m r) :
    Run (v ++ w) n r := by
  induction v generalizing n with
  | nil => simpa [Run] using hv ▸ hw
  | cons a v ih =>
    obtain ⟨z, hz, ho, hr⟩ := hv
    exact ⟨z, hz, ho, ih hr⟩

theorem two_three_coprime (a b : ℕ) : Nat.Coprime (2 ^ a) (3 ^ b) :=
  (by decide : Nat.Coprime 2 3).pow a b

/-- Every finite valuation word has an odd terminal representative in the
canonical ternary interval. This is just a finite modular calculation. -/
theorem residue_exists (w : List ℕ) :
    ∃ r : ℕ, 0 < r ∧ r < 2 * 3 ^ w.length ∧ r % 2 = 1 ∧
      Nat.ModEq (3 ^ w.length) (2 ^ total w * r) (offset w) := by
  let M := 3 ^ w.length
  have hM : M ≠ 0 := pow_ne_zero _ (by decide)
  let : NeZero M := ⟨hM⟩
  let u : ZMod M := ((2 ^ (total w + 1) : ℕ) : ZMod M)
  let z : ZMod M := ((offset w : ZMod M) - ((2 ^ total w : ℕ) : ZMod M)) * u⁻¹
  refine ⟨2 * z.val + 1, by omega, ?_, by omega, ?_⟩
  · have hz := ZMod.val_lt z
    change 2 * z.val + 1 < 2 * M
    omega
  · apply (ZMod.natCast_eq_natCast_iff _ _ M).mp
    have hu : u * u⁻¹ = 1 :=
      ZMod.coe_mul_inv_eq_one (2 ^ (total w + 1)) (two_three_coprime _ _)
    have hp : u = 2 * ((2 ^ total w : ℕ) : ZMod M) := by
      simp [u, pow_succ, mul_comm]
    simp only [Nat.cast_mul, Nat.cast_add, Nat.cast_one, ZMod.natCast_zmod_val]
    change ((2 ^ total w : ℕ) : ZMod M) * (2 * z + 1) = (offset w : ZMod M)
    calc
      _ = u * z + ((2 ^ total w : ℕ) : ZMod M) := by rw [hp]; ring
      _ = _ := by dsimp [z]; rw [show u * (((offset w : ZMod M) - ((2 ^ total w : ℕ) : ZMod M)) * u⁻¹) =
          ((offset w : ZMod M) - ((2 ^ total w : ℕ) : ZMod M)) * (u * u⁻¹) by ring, hu]; ring

/-- A positive odd target satisfying the complete ternary congruence has a
positive ordinary source, with every inverse step legal. -/
theorem inverse_source_exists {w : List ℕ} (hw : Valid w) {r : ℕ}
    (hr : 0 < r) (ho : r % 2 = 1)
    (hcong : Nat.ModEq (3 ^ w.length) (2 ^ total w * r) (offset w)) :
    ∃ n : ℕ, 0 < n ∧ n % 2 = 1 ∧ Run w n r := by
  induction w using List.reverseRecOn generalizing r with
  | nil => exact ⟨r, hr, ho, rfl⟩
  | append_singleton w a ih =>
    have ha : 0 < a := hw a (by simp)
    have hw' : Valid w := fun b hb => hw b (by simp [hb])
    have hbasic : Nat.ModEq (3 * 3 ^ w.length)
        (2 ^ total w * (2 ^ a * r)) (3 * offset w + 2 ^ total w) := by
      simpa [total_append, offset_append, total, offset, pow_add, pow_succ,
        Nat.mul_comm, Nat.mul_left_comm, Nat.mul_assoc] using hcong
    have hmod : Nat.ModEq 3 (2 ^ total w * (2 ^ a * r)) (2 ^ total w * 1) := by
      have hd := hbasic.of_dvd (dvd_mul_right 3 (3 ^ w.length))
      simpa [Nat.ModEq, Nat.add_mod] using hd
    have hc : Nat.ModEq 3 (2 ^ a * r) 1 :=
      Nat.ModEq.cancel_left_of_coprime (two_three_coprime (total w) 1).symm hmod
    let m := (2 ^ a * r) / 3
    have hdiv : 3 * m + 1 = 2 ^ a * r := by
      have := Nat.mod_add_div (2 ^ a * r) 3
      change (2 ^ a * r) % 3 = 1 % 3 at hc
      omega
    have hpow : 2 ≤ 2 ^ a := by
      exact Nat.le_of_dvd (pow_pos (by decide) _) (dvd_pow_self 2 (by omega))
    have hm : 0 < m := by nlinarith
    have heven : (2 ^ a * r) % 2 = 0 := by
      have hd : 2 ∣ 2 ^ a * r := dvd_mul_of_dvd_left (dvd_pow_self 2 (by omega)) r
      omega
    have hm_odd : m % 2 = 1 := by omega
    have hcancel : Nat.ModEq (3 * 3 ^ w.length)
        (3 * (2 ^ total w * m) + 2 ^ total w) (3 * offset w + 2 ^ total w) := by
      convert hbasic using 1
      rw [← hdiv]
      ring
    have hprev : Nat.ModEq (3 ^ w.length) (2 ^ total w * m) (offset w) :=
      Nat.ModEq.mul_left_cancel' (by decide : 3 ≠ 0)
        (hcancel.add_right_cancel' (2 ^ total w))
    obtain ⟨n, hn, hno, hrun⟩ := ih hw' hm hm_odd hprev
    refine ⟨n, hn, hno, run_append hrun ?_⟩
    exact ⟨r, hdiv, ho, rfl⟩

theorem valuation_of_step {n m a : ℕ} (hm : m % 2 = 1)
    (h : 3 * n + 1 = 2 ^ a * m) : valuation n = a := by
  have hm0 : m ≠ 0 := by omega
  have hm2 : ¬ 2 ∣ m := by omega
  unfold valuation
  rw [h, Nat.factorization_mul (pow_ne_zero _ (by decide)) hm0,
    Finsupp.add_apply, Nat.factorization_eq_zero_of_not_dvd hm2]
  simp [Nat.prime_two.factorization_pow]

theorem oddStep_of_step {n m a : ℕ} (hm : m % 2 = 1)
    (h : 3 * n + 1 = 2 ^ a * m) : oddStep n = m := by
  unfold oddStep
  rw [valuation_of_step hm h, h]
  exact Nat.mul_div_right _ (pow_pos (by decide) _)

theorem run_determines {w : List ℕ} {n r : ℕ} (h : Run w n r) :
    trace w.length n = w ∧ orbit w.length n = r := by
  induction w generalizing n with
  | nil => exact ⟨rfl, h⟩
  | cons a w ih =>
    obtain ⟨m, he, ho, hr⟩ := h
    obtain ⟨ht, hor⟩ := ih hr
    simp only [List.length_cons, trace, orbit, valuation_of_step ho he,
      oddStep_of_step ho he, ht, hor, and_self]

theorem run_shift {w : List ℕ} {n r : ℕ} (h : Run w n r) (k : ℕ) :
    Run w (n + 2 ^ (total w + 1) * k) (r + 2 * 3 ^ w.length * k) := by
  induction w generalizing n k with
  | nil => simpa [Run, total] using congrArg (fun t => t + 2 * k) h
  | cons a w ih =>
    obtain ⟨m, he, ho, hr⟩ := h
    refine ⟨m + 2 ^ (total w + 1) * (3 * k), ?_, ?_, ?_⟩
    · simp only [total, show a + total w + 1 = a + (total w + 1) by omega, pow_add]
      nlinarith [he]
    · simp [Nat.add_mod, Nat.mul_mod, pow_succ, ho]
    · convert ih hr (3 * k) using 1
      simp only [List.length_cons, pow_succ]
      ring

/-- Existence of the complete positive primitive cylinder, not merely a
formal residue solution or a 2-adic source. -/
theorem primitive_exists {w : List ℕ} (hw : Valid w) :
    ∃ b r : ℕ, 0 < b ∧ b % 2 = 1 ∧ b < 2 ^ (total w + 1) ∧
      0 < r ∧ r % 2 = 1 ∧ r < 2 * 3 ^ w.length ∧ Run w b r := by
  obtain ⟨r, hr, hrb, ho, hc⟩ := residue_exists w
  obtain ⟨b, hb, hbo, hrun⟩ := inverse_source_exists hw hr ho hc
  refine ⟨b, r, hb, hbo, ?_, hr, ho, hrb, hrun⟩
  have he := run_affine hrun
  have hp : 0 < 2 ^ total w := pow_pos (by decide) _
  have ht : 0 < 3 ^ w.length := pow_pos (by decide) _
  rw [pow_succ]
  nlinarith

def Words : ℕ → Type
  | 0 => Unit
  | q + 1 => ℕ × Words q

def letters : {q : ℕ} → Words q → List ℕ
  | 0, _ => []
  | _ + 1, w => (w.1 + 1) :: letters w.2

theorem letters_length {q : ℕ} (w : Words q) : (letters w).length = q := by
  induction q with
  | zero => rfl
  | succ q ih => simpa [letters] using congrArg Nat.succ (ih w.2)

theorem letters_valid {q : ℕ} (w : Words q) : Valid (letters w) := by
  induction q with
  | zero => simp [letters, Valid]
  | succ q ih =>
    intro a ha
    simp only [letters, List.mem_cons] at ha
    rcases ha with rfl | ha
    · omega
    · exact ih w.2 a ha

theorem letters_injective {q : ℕ} : Function.Injective (@letters q) := by
  induction q with
  | zero => intro x y _; cases x; cases y; rfl
  | succ q ih =>
    intro x y h
    have hh := List.cons.inj h
    apply Prod.ext
    · omega
    · exact ih hh.2

def code : (q : ℕ) → ℕ → Words q
  | 0, _ => ()
  | q + 1, n => (valuation n - 1, code q (oddStep n))

theorem letters_code {n : ℕ} (hn : n % 2 = 1) (q : ℕ) :
    letters (code q n) = trace q n := by
  induction q generalizing n with
  | zero => rfl
  | succ q ih =>
    simp only [code, letters, trace, ih (oddStep_odd n)]
    congr 1
    have := valuation_pos hn
    omega

@[irreducible] noncomputable def primitive {q : ℕ} (w : Words q) : ℕ × ℕ :=
  ((primitive_exists (letters_valid w)).choose,
    (primitive_exists (letters_valid w)).choose_spec.choose)

theorem primitive_spec {q : ℕ} (w : Words q) :
    0 < (primitive w).1 ∧ (primitive w).1 % 2 = 1 ∧
    (primitive w).1 < 2 ^ (total (letters w) + 1) ∧
    0 < (primitive w).2 ∧ (primitive w).2 % 2 = 1 ∧
    (primitive w).2 < 2 * 3 ^ q ∧ Run (letters w) (primitive w).1 (primitive w).2 := by
  simpa only [primitive, letters_length] using
    (primitive_exists (letters_valid w)).choose_spec.choose_spec

theorem orbit_pos {n : ℕ} (hn : 0 < n) (q : ℕ) : 0 < orbit q n := by
  induction q generalizing n with
  | zero => exact hn
  | succ q ih => exact ih (oddStep_pos n)

theorem orbit_odd {n : ℕ} (hn : n % 2 = 1) (q : ℕ) : orbit q n % 2 = 1 := by
  induction q generalizing n with
  | zero => exact hn
  | succ q ih => exact ih (oddStep_odd n)

noncomputable def liftSource {q : ℕ} (w : Words q) (k : ℕ) : ℕ :=
  (primitive w).1 + 2 ^ (total (letters w) + 1) * k

theorem liftSource_pos {q : ℕ} (w : Words q) (k : ℕ) : 0 < liftSource w k := by
  have := (primitive_spec w).1
  unfold liftSource
  omega

theorem liftSource_odd {q : ℕ} (w : Words q) (k : ℕ) : liftSource w k % 2 = 1 := by
  have h := (primitive_spec w).2.1
  simp [liftSource, pow_succ, Nat.add_mod, Nat.mul_mod, h]

theorem liftSource_run {q : ℕ} (w : Words q) (k : ℕ) :
    Run (letters w) (liftSource w k) ((primitive w).2 + 2 * 3 ^ q * k) := by
  simpa only [liftSource, letters_length] using
    run_shift (primitive_spec w).2.2.2.2.2.2 k

theorem liftSource_code {q : ℕ} (w : Words q) (k : ℕ) : code q (liftSource w k) = w := by
  apply letters_injective
  rw [letters_code (liftSource_odd w k)]
  simpa only [letters_length] using (run_determines (liftSource_run w k)).1

theorem liftSource_orbit {q : ℕ} (w : Words q) (k : ℕ) :
    orbit q (liftSource w k) = (primitive w).2 + 2 * 3 ^ q * k := by
  simpa only [letters_length] using (run_determines (liftSource_run w k)).2

/-- Every positive ordinary odd source is in the primitive cylinder of its
actual valuation word. The same source is retained when q changes. -/
theorem source_in_cylinder {n : ℕ} (_hn : 0 < n) (ho : n % 2 = 1) (q : ℕ) :
    ∃ k : ℕ, n = liftSource (code q n) k := by
  let w := code q n
  obtain ⟨hb, hbo, hbb, hr, hro, hrr, hrun⟩ := primitive_spec w
  have hactual : Run (letters w) n (orbit q n) := by
    simpa only [w, letters_code ho] using run_trace q n
  have he := run_affine hactual
  have hep := run_affine hrun
  rw [letters_length] at he hep
  have hcong : Nat.ModEq (3 ^ q)
      (2 ^ total (letters w) * orbit q n) (2 ^ total (letters w) * (primitive w).2) := by
    rw [Nat.ModEq, he, hep]
    simp [Nat.add_mod]
  have hterm : Nat.ModEq (3 ^ q) (orbit q n) (primitive w).2 :=
    Nat.ModEq.cancel_left_of_coprime (two_three_coprime (total (letters w)) q).symm hcong
  have hpar : Nat.ModEq 2 (orbit q n) (primitive w).2 := by
    change orbit q n % 2 = (primitive w).2 % 2
    rw [orbit_odd ho, hro]
  have hfull : Nat.ModEq (2 * 3 ^ q) (orbit q n) (primitive w).2 :=
    (Nat.modEq_and_modEq_iff_modEq_mul ((by decide : Nat.Coprime 2 3).pow_right q)).mp
      ⟨hpar, hterm⟩
  have hmod : orbit q n % (2 * 3 ^ q) = (primitive w).2 := by
    rw [Nat.ModEq, Nat.mod_eq_of_lt hrr] at hfull
    exact hfull
  let k := orbit q n / (2 * 3 ^ q)
  have hy : orbit q n = (primitive w).2 + 2 * 3 ^ q * k := by
    have := Nat.mod_add_div (orbit q n) (2 * 3 ^ q)
    rw [hmod] at this
    exact this.symm
  refine ⟨k, ?_⟩
  change n = (primitive w).1 + 2 ^ (total (letters w) + 1) * k
  have hp : 0 < 3 ^ q := pow_pos (by decide) _
  rw [hy] at he
  rw [pow_succ]
  nlinarith

def OddPositive := {n : ℕ // 0 < n ∧ n % 2 = 1}

noncomputable def cylinderMap (q : ℕ) (v : Words q × ℕ) : OddPositive :=
  ⟨liftSource v.1 v.2, liftSource_pos v.1 v.2, liftSource_odd v.1 v.2⟩

theorem cylinderMap_bijective (q : ℕ) : Function.Bijective (cylinderMap q) := by
  constructor
  · intro x y h
    have he : liftSource x.1 x.2 = liftSource y.1 y.2 := congrArg Subtype.val h
    have hw : x.1 = y.1 := by
      simpa only [liftSource_code] using congrArg (code q) he
    apply Prod.ext hw
    rw [hw] at he
    unfold liftSource at he
    exact Nat.eq_of_mul_eq_mul_left (pow_pos (by decide) _) (Nat.add_left_cancel he)
  · intro n
    obtain ⟨k, hk⟩ := source_in_cylinder n.property.1 n.property.2 q
    refine ⟨(code q n.val, k), ?_⟩
    exact Subtype.ext hk.symm

/-- Complete, disjoint ordinary source partition, constructed and proved
from the finite valuation equations. -/
noncomputable def cylinderEquiv (q : ℕ) : (Words q × ℕ) ≃ OddPositive :=
  Equiv.ofBijective (cylinderMap q) (cylinderMap_bijective q)

theorem cylinderEquiv_apply (q : ℕ) (v : Words q × ℕ) :
    cylinderEquiv q v = cylinderMap q v := rfl

def wordWeight {q : ℕ} (w : Words q) : ℝ := (1 / 16 : ℝ) ^ total (letters w)

theorem wordWeight_nonneg {q : ℕ} (w : Words q) : 0 ≤ wordWeight w := by
  unfold wordWeight
  positivity

theorem wordWeight_sum (q : ℕ) :
    Summable (@wordWeight q) ∧ (∑' w : Words q, wordWeight w) = (1 / 15 : ℝ) ^ q := by
  induction q with
  | zero =>
    change Summable (fun _ : Unit => (1 / 16 : ℝ) ^ 0) ∧ _
    constructor
    · exact summable_of_hasFiniteSupport (Set.toFinite _)
    · simp [wordWeight, letters, total, Words]
  | succ q ih =>
    have hg : HasSum (fun a : ℕ => (1 / 16 : ℝ) ^ (a + 1)) (1 / 15) := by
      convert (hasSum_geometric_of_lt_one (by norm_num : (0 : ℝ) ≤ 1 / 16)
        (by norm_num : (1 / 16 : ℝ) < 1)).mul_left (1 / 16 : ℝ) using 1
      · ext a
        rw [pow_succ]
        ring
      · norm_num
    have hprod := hg.summable.mul_of_nonneg ih.1
      (fun a => by positivity) (fun w => wordWeight_nonneg w)
    have heq : (@wordWeight (q + 1)) =
        fun v : ℕ × Words q => (1 / 16 : ℝ) ^ (v.1 + 1) * wordWeight v.2 := by
      funext v
      simp [wordWeight, letters, total, pow_add]
    rw [heq]
    refine ⟨hprod, ?_⟩
    change (∑' v : ℕ × Words q, (1 / 16 : ℝ) ^ (v.1 + 1) * wordWeight v.2) = _
    rw [hprod.tsum_prod]
    simp_rw [tsum_mul_left, ih.2]
    rw [tsum_mul_right, hg.tsum_eq, pow_succ]
    ring

def weight (n : ℕ) : ℝ := ((n : ℝ) ^ 4)⁻¹

theorem weight_nonneg (n : ℕ) : 0 ≤ weight n := by unfold weight; positivity

theorem weight_pos {n : ℕ} (hn : 0 < n) : 0 < weight n := by unfold weight; positivity

theorem weight_summable : Summable weight :=
  Real.summable_nat_pow_inv.mpr (by decide : 1 < 4)

theorem oddWeight_summable : Summable (fun n : OddPositive => weight n.val) :=
  weight_summable.subtype _

def aliveTerm (q : ℕ) (n : OddPositive) : ℝ :=
  if orbit q n.val = 1 then 0 else weight n.val

noncomputable def aliveMass (q : ℕ) : ℝ := ∑' n : OddPositive, aliveTerm q n

noncomputable def primitiveTerm {q : ℕ} (w : Words q) : ℝ :=
  if (primitive w).2 = 1 then 0 else weight (primitive w).1

noncomputable def primitiveMoment (q : ℕ) : ℝ := ∑' w : Words q, primitiveTerm w

noncomputable def liftRemainder (q : ℕ) : ℝ :=
  ∑' w : Words q, ∑' k : ℕ, weight (liftSource w (k + 1))

theorem aliveTerm_nonneg (q : ℕ) (n : OddPositive) : 0 ≤ aliveTerm q n := by
  unfold aliveTerm
  split <;> first | exact le_rfl | exact weight_nonneg _

theorem aliveTerm_le_weight (q : ℕ) (n : OddPositive) : aliveTerm q n ≤ weight n.val := by
  unfold aliveTerm
  split <;> first | exact le_rfl | exact weight_nonneg _

theorem aliveTerm_summable (q : ℕ) : Summable (aliveTerm q) :=
  Summable.of_nonneg_of_le (aliveTerm_nonneg q) (aliveTerm_le_weight q) oddWeight_summable

theorem alive_lift_zero {q : ℕ} (w : Words q) :
    aliveTerm q (cylinderMap q (w, 0)) = primitiveTerm w := by
  simp only [aliveTerm, cylinderMap, liftSource_orbit, mul_zero, add_zero]
  simp [primitiveTerm, liftSource]

theorem alive_lift_succ {q : ℕ} (w : Words q) (k : ℕ) :
    aliveTerm q (cylinderMap q (w, k + 1)) = weight (liftSource w (k + 1)) := by
  have h := (primitive_spec w).2.2.2.1
  have hp : 0 < 3 ^ q := pow_pos (by decide) _
  have hn : (primitive w).2 + 2 * 3 ^ q * (k + 1) ≠ 1 := by nlinarith
  simp only [aliveTerm, cylinderMap, liftSource_orbit, ite_eq_right hn]

theorem liftWeight_summable (q : ℕ) :
    Summable (fun v : Words q × ℕ => weight (liftSource v.1 v.2)) := by
  have h : Summable ((fun n : OddPositive => weight n.val) ∘ cylinderEquiv q) :=
    (cylinderEquiv q).summable_iff.mpr oddWeight_summable
  simpa only [Function.comp_def, cylinderEquiv_apply, cylinderMap] using h

theorem aliveLift_summable (q : ℕ) :
    Summable (fun v : Words q × ℕ => aliveTerm q (cylinderMap q v)) := by
  have h : Summable (aliveTerm q ∘ cylinderEquiv q) :=
    (cylinderEquiv q).summable_iff.mpr (aliveTerm_summable q)
  simpa only [Function.comp_def, cylinderEquiv_apply] using h

theorem primitiveTerm_summable (q : ℕ) : Summable (@primitiveTerm q) := by
  have h := (aliveLift_summable q).comp_injective
    (show Function.Injective (fun w : Words q => (w, 0)) by intro x y h; exact Prod.mk.inj h |>.1)
  simpa only [Function.comp_def, alive_lift_zero] using h

theorem liftTail_summable (q : ℕ) :
    Summable (fun v : Words q × ℕ => weight (liftSource v.1 (v.2 + 1))) := by
  have h := (liftWeight_summable q).comp_injective
    (show Function.Injective (fun v : Words q × ℕ => (v.1, v.2 + 1)) by
      intro x y h
      exact Prod.ext (Prod.mk.inj h).1 (Nat.add_right_cancel (Prod.mk.inj h).2))
  simpa only [Function.comp_def] using h

theorem aliveMass_decomposition (q : ℕ) : aliveMass q = primitiveMoment q + liftRemainder q := by
  have he : aliveMass q = ∑' v : Words q × ℕ, aliveTerm q (cylinderMap q v) :=
    by simpa only [cylinderEquiv_apply, aliveMass] using ((cylinderEquiv q).tsum_eq (aliveTerm q)).symm
  rw [he, (aliveLift_summable q).tsum_prod]
  have hsplit : ∀ w : Words q,
      (∑' k : ℕ, aliveTerm q (cylinderMap q (w, k))) =
        primitiveTerm w + ∑' k : ℕ, weight (liftSource w (k + 1)) := by
    intro w
    rw [((aliveLift_summable q).prod_factor w).tsum_eq_zero_add, alive_lift_zero]
    simp only [alive_lift_succ]
  simp_rw [hsplit]
  exact (primitiveTerm_summable q).tsum_add (liftTail_summable q).prod

noncomputable def zetaFour : ℝ := ∑' k : ℕ, weight (k + 1)

theorem positiveWeight_summable : Summable (fun k : ℕ => weight (k + 1)) :=
  (summable_nat_add_iff 1).mpr weight_summable

theorem zetaFour_nonneg : 0 ≤ zetaFour := tsum_nonneg fun _ => weight_nonneg _

theorem liftTail_pointwise {q : ℕ} (w : Words q) (k : ℕ) :
    weight (liftSource w (k + 1)) ≤ (1 / 16 : ℝ) * wordWeight w * weight (k + 1) := by
  have hM : (0 : ℝ) < 2 ^ (total (letters w) + 1) := by positivity
  have hk : (0 : ℝ) < (k + 1 : ℕ) := by positivity
  have hl : (0 : ℝ) < (liftSource w (k + 1) : ℕ) := by
    exact_mod_cast liftSource_pos w (k + 1)
  have hle : 2 ^ (total (letters w) + 1) * ((k + 1 : ℕ) : ℝ) ≤
      (liftSource w (k + 1) : ℕ) := by
    unfold liftSource
    push_cast
    exact le_add_of_nonneg_left (Nat.cast_nonneg _)
  unfold weight
  calc
    _ ≤ ((2 ^ (total (letters w) + 1) * ((k + 1 : ℕ) : ℝ)) ^ 4)⁻¹ := by
      apply inv_anti₀ (by positivity)
      exact pow_le_pow_left₀ (by positivity) hle 4
    _ = (1 / 16 : ℝ) * wordWeight w * (((k + 1 : ℕ) : ℝ) ^ 4)⁻¹ := by
      have hpower : (((2 : ℝ) ^ (total (letters w) + 1)) ^ 4)⁻¹ =
          (1 / 16 : ℝ) ^ (total (letters w) + 1) := by
        rw [← pow_mul, Nat.mul_comm (total (letters w) + 1) 4, pow_mul]
        calc
          (((2 : ℝ) ^ 4) ^ (total (letters w) + 1))⁻¹ =
              (((2 : ℝ) ^ 4)⁻¹) ^ (total (letters w) + 1) := (inv_pow _ _).symm
          _ = _ := congrArg (fun x : ℝ => x ^ (total (letters w) + 1))
            (by norm_num : ((2 : ℝ) ^ 4)⁻¹ = 1 / 16)
      unfold wordWeight
      rw [mul_pow, mul_inv_rev, hpower, pow_succ]
      ring

theorem liftRemainder_nonneg (q : ℕ) : 0 ≤ liftRemainder q :=
  tsum_nonneg fun _ => tsum_nonneg fun _ => weight_nonneg _

theorem liftRemainder_bound (q : ℕ) :
    liftRemainder q ≤ zetaFour / 16 * (1 / 15 : ℝ) ^ q := by
  have hbound := ((wordWeight_sum q).1.mul_left (1 / 16 : ℝ)).mul_of_nonneg
    positiveWeight_summable (fun w => mul_nonneg (by norm_num) (wordWeight_nonneg w))
    (fun k => weight_nonneg _)
  have hb := Summable.tsum_le_tsum
    (fun v : Words q × ℕ => liftTail_pointwise v.1 v.2) (liftTail_summable q) hbound
  rw [(liftTail_summable q).tsum_prod, hbound.tsum_prod] at hb
  change liftRemainder q ≤ _ at hb
  simp_rw [tsum_mul_left] at hb
  rw [tsum_mul_right, tsum_mul_left, (wordWeight_sum q).2] at hb
  change liftRemainder q ≤ (1 / 16) * (1 / 15) ^ q * zetaFour at hb
  convert hb using 1
  ring

open Filter
open scoped Topology

theorem liftRemainder_tendsto_zero : Tendsto liftRemainder atTop (𝓝 0) := by
  apply squeeze_zero liftRemainder_nonneg liftRemainder_bound
  have h := tendsto_pow_atTop_nhds_zero_of_lt_one
    (by norm_num : (0 : ℝ) ≤ 1 / 15) (by norm_num : (1 / 15 : ℝ) < 1)
  simpa only [mul_zero] using h.const_mul (zetaFour / 16)

theorem oddStep_one : oddStep 1 = 1 :=
  oddStep_of_step (by decide : 1 % 2 = 1) (by decide : 3 * 1 + 1 = 2 ^ 2 * 1)

theorem orbit_one (q : ℕ) : orbit q 1 = 1 := by
  induction q with
  | zero => rfl
  | succ q ih => simpa only [orbit, oddStep_one] using ih

theorem orbit_add (q t n : ℕ) : orbit (q + t) n = orbit t (orbit q n) := by
  induction q generalizing n with
  | zero => simp [orbit]
  | succ q ih =>
    rw [show q + 1 + t = q + t + 1 by omega]
    simpa only [orbit] using ih (oddStep n)

theorem orbit_eq_one_of_le {q k n : ℕ} (hk : orbit k n = 1) (h : k ≤ q) :
    orbit q n = 1 := by
  rw [← Nat.add_sub_of_le h, orbit_add, hk, orbit_one]

def AllOddConverge : Prop :=
  ∀ n : ℕ, 0 < n → n % 2 = 1 → ∃ q : ℕ, orbit q n = 1

theorem allOddConverge_iff_aliveMass_tendsto_zero :
    AllOddConverge ↔ Tendsto aliveMass atTop (𝓝 0) := by
  constructor
  · intro h
    have hp : ∀ n : OddPositive, Tendsto (fun q => aliveTerm q n) atTop (𝓝 0) := by
      intro n
      obtain ⟨k, hk⟩ := h n.val n.property.1 n.property.2
      have he : ∀ᶠ q in atTop, aliveTerm q n = 0 := by
        filter_upwards [eventually_ge_atTop k] with q hq
        simp [aliveTerm, orbit_eq_one_of_le hk hq]
      apply tendsto_const_nhds.congr'
      filter_upwards [he] with q hq
      exact hq.symm
    have ht := tendsto_tsum_of_dominated_convergence oddWeight_summable hp
      (Filter.Eventually.of_forall (fun q n => by
        rw [Real.norm_eq_abs, abs_of_nonneg (aliveTerm_nonneg q n)]
        exact aliveTerm_le_weight q n))
    change Tendsto (fun q => ∑' n : OddPositive, aliveTerm q n) atTop (𝓝 0)
    simpa only [tsum_zero] using ht
  · intro h n hn ho
    by_contra hnever
    have hnq : ∀ q : ℕ, orbit q n ≠ 1 := by simpa using hnever
    let z : OddPositive := ⟨n, hn, ho⟩
    have hbound : ∀ q, weight n ≤ aliveMass q := by
      intro q
      have ht := (aliveTerm_summable q).le_tsum z (fun m _ => aliveTerm_nonneg q m)
      simpa [z, aliveTerm, hnq q, aliveMass] using ht
    have hbad : weight n ≤ 0 := ge_of_tendsto h (Filter.Eventually.of_forall hbound)
    exact (weight_pos hn).not_ge hbad

/-- Exact cycle-sensitive arithmetic criterion. The theorem proves an
equivalence; it does not assert that the moment on the right tends to zero. -/
theorem allOddConverge_iff_primitiveMoment_tendsto_zero :
    AllOddConverge ↔ Tendsto primitiveMoment atTop (𝓝 0) := by
  rw [allOddConverge_iff_aliveMass_tendsto_zero]
  constructor
  · intro h
    have ht := h.sub liftRemainder_tendsto_zero
    simpa only [aliveMass_decomposition, add_sub_cancel_right, sub_self] using ht
  · intro h
    have ht := h.add liftRemainder_tendsto_zero
    simpa only [← aliveMass_decomposition, zero_add] using ht

/-! The acceleration convention is connected explicitly to the ordinary
positive-integer map: even n maps to n/2; odd n maps to 3n+1. -/

def ordinaryStep (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else 3 * n + 1

def OrdinaryBasin (n : ℕ) : Prop := ∃ k : ℕ, ordinaryStep^[k] n = 1

def FullCollatz : Prop := ∀ n : ℕ, 0 < n → OrdinaryBasin n

def OddBasin (n : ℕ) : Prop := ∃ q : ℕ, orbit q n = 1

theorem ordinaryStep_twice (n : ℕ) : ordinaryStep (2 * n) = n := by
  simp [ordinaryStep]

theorem ordinaryStep_of_odd {n : ℕ} (hn : n % 2 = 1) : ordinaryStep n = 3 * n + 1 := by
  simp [ordinaryStep, hn]

theorem ordinaryBasin_pre (n : ℕ) (h : OrdinaryBasin (ordinaryStep n)) : OrdinaryBasin n := by
  obtain ⟨k, hk⟩ := h
  exact ⟨k + 1, by simpa only [Function.iterate_succ_apply] using hk⟩

theorem ordinaryBasin_mul_two_pow {n : ℕ} (h : OrdinaryBasin n) (a : ℕ) :
    OrdinaryBasin (2 ^ a * n) := by
  induction a with
  | zero => simpa using h
  | succ a ih =>
    rw [pow_succ', mul_assoc]
    apply ordinaryBasin_pre
    simpa only [ordinaryStep_twice] using ih

theorem ordinaryBasin_of_oddBasin {n : ℕ} (ho : n % 2 = 1) (h : OddBasin n) :
    OrdinaryBasin n := by
  obtain ⟨q, hq⟩ := h
  induction q generalizing n with
  | zero =>
    have hn : n = 1 := hq
    exact ⟨0, hn⟩
  | succ q ih =>
    have hn := ih (oddStep_odd n) hq
    have hs := ordinaryBasin_mul_two_pow hn (valuation n)
    rw [oddStep_identity] at hs
    apply ordinaryBasin_pre n
    simpa only [ordinaryStep_of_odd ho] using hs

theorem oddBasin_step (n : ℕ) : OddBasin (oddStep n) ↔ OddBasin n := by
  constructor
  · rintro ⟨q, hq⟩
    exact ⟨q + 1, hq⟩
  · rintro ⟨q, hq⟩
    cases q with
    | zero =>
      have hn : n = 1 := hq
      exact ⟨0, by simpa only [orbit, hn] using oddStep_one⟩
    | succ q => exact ⟨q, hq⟩

def oddPart (n : ℕ) : ℕ := n / 2 ^ n.factorization 2

theorem oddPart_twice (n : ℕ) : oddPart (2 * n) = oddPart n := by
  simpa only [pow_one, oddPart] using Nat.ordCompl_self_pow_mul n 1 Nat.prime_two

theorem oddPart_of_odd {n : ℕ} (hn : n % 2 = 1) : oddPart n = n := by
  apply (Nat.ordCompl_eq_self_iff_zero_or_not_dvd n Nat.prime_two).mpr
  right
  omega

theorem oddBasin_oddPart_step (n : ℕ) :
    OddBasin (oddPart (ordinaryStep n)) ↔ OddBasin (oddPart n) := by
  by_cases he : n % 2 = 0
  · have hn : 2 * (n / 2) = n := by omega
    have hp : oddPart (n / 2) = oddPart n := by
      rw [← oddPart_twice (n / 2), hn]
    simp only [ordinaryStep, ite_eq_left he, hp]
  · have ho : n % 2 = 1 := by omega
    rw [ordinaryStep_of_odd ho, oddPart_of_odd ho]
    change OddBasin (oddStep n) ↔ OddBasin n
    exact oddBasin_step n

theorem oddBasin_ordinary_iterate (k n : ℕ) :
    OddBasin (oddPart (ordinaryStep^[k] n)) ↔ OddBasin (oddPart n) := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    rw [Function.iterate_succ_apply]
    exact (ih (ordinaryStep n)).trans (oddBasin_oddPart_step n)

theorem fullCollatz_iff_allOddConverge : FullCollatz ↔ AllOddConverge := by
  constructor
  · intro h n hn ho
    obtain ⟨k, hk⟩ := h n hn
    have hp : OddBasin (oddPart (ordinaryStep^[k] n)) := by
      rw [hk, oddPart_of_odd (by decide : 1 % 2 = 1)]
      exact ⟨0, rfl⟩
    have hz := (oddBasin_ordinary_iterate k n).mp hp
    simpa only [oddPart_of_odd ho, OddBasin] using hz
  · intro h n hn
    have hp : 0 < oddPart n := Nat.ordCompl_pos 2 (by omega)
    have hpo : oddPart n % 2 = 1 := by
      have hh := Nat.not_dvd_ordCompl Nat.prime_two (by omega : n ≠ 0)
      change ¬ 2 ∣ oddPart n at hh
      omega
    have hz := ordinaryBasin_of_oddBasin hpo (h (oddPart n) hp hpo)
    have hs := ordinaryBasin_mul_two_pow hz (n.factorization 2)
    simpa only [oddPart, Nat.ordProj_mul_ordCompl_eq_self] using hs

/-- Full ordinary Collatz is equivalent to the cycle-sensitive source-word
moment tending to zero. This is a closing interface, not the missing estimate. -/
theorem fullCollatz_iff_primitiveMoment_tendsto_zero :
    FullCollatz ↔ Tendsto primitiveMoment atTop (𝓝 0) :=
  fullCollatz_iff_allOddConverge.trans allOddConverge_iff_primitiveMoment_tendsto_zero

end
end CollatzPrimitiveSurvival

#print axioms CollatzPrimitiveSurvival.cylinderMap_bijective
#print axioms CollatzPrimitiveSurvival.aliveMass_decomposition
#print axioms CollatzPrimitiveSurvival.liftRemainder_bound
#print axioms CollatzPrimitiveSurvival.fullCollatz_iff_primitiveMoment_tendsto_zero

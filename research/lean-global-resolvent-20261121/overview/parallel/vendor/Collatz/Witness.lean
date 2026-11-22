/-
Unbounded finite certificates for the odd Collatz basin.
All list lengths and all exponents below are quantified without a cutoff.
-/
import Collatz.Closure
import Init.Data.Nat.Coprime

open CollatzReverseBasin CollatzClosure

namespace CollatzWitness

inductive Witness : Nat → Prop where
  | one : Witness 1
  | step {n m a : Nat} : 0 < a → 3*n+1 = 2^a*m → Witness m → Witness n

theorem witness_odd {n : Nat} (h : Witness n) : n % 2 = 1 := by
  cases h with
  | one => decide
  | @step n m a ha he hm =>
    obtain ⟨b, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : a ≠ 0)
    rw [Nat.pow_succ] at he
    have e : 3*n+1 = 2*(2^b*m) := by grind
    omega

theorem basin_pow_two (a n : Nat) : Basin (2^a*n) ↔ Basin n := by
  induction a with
  | zero => simp
  | succ a ih =>
    have e : 2^(a+1)*n = 2*(2^a*n) := by grind
    rw [e]
    exact (basin_twice _).trans ih

theorem witness_basin {n : Nat} (h : Witness n) : Basin n := by
  induction h with
  | one => exact ⟨0, rfl⟩
  | @step n m a ha he hm ih =>
    have ho := witness_odd (Witness.step ha he hm)
    apply (basin_odd n ho).mp
    rw [he]
    exact (basin_pow_two a m).mpr ih

def PoweredWitness (n : Nat) : Prop := ∃ a m, n = 2^a*m ∧ Witness m

theorem powered_back (n : Nat) (h : PoweredWitness (shortcut n)) : PoweredWitness n := by
  obtain ⟨a,m,he,hm⟩ := h
  by_cases hn : n % 2 = 0
  · have hs : shortcut n = n/2 := by simp [shortcut, hn]
    refine ⟨a+1,m,?_,hm⟩
    rw [hs] at he
    have e : n = 2*(2^a*m) := by omega
    rw [e, Nat.pow_succ]
    grind
  · have hs : 3*n+1 = 2*shortcut n := by unfold shortcut; split <;> omega
    have e : 3*n+1 = 2^(a+1)*m := by rw [hs, he, Nat.pow_succ]; grind
    exact ⟨0,n,by simp,Witness.step (by omega) e hm⟩

theorem basin_powered {n : Nat} (h : Basin n) : PoweredWitness n := by
  obtain ⟨k,hk⟩ := h
  induction k generalizing n with
  | zero =>
    change n = 1 at hk
    subst n
    exact ⟨0,1,rfl,Witness.one⟩
  | succ k ih => exact powered_back n (ih hk)

theorem witness_iff_basin (n : Nat) (hn : n % 2 = 1) : Witness n ↔ Basin n := by
  refine ⟨witness_basin, ?_⟩
  intro h
  obtain ⟨a,m,he,hm⟩ := basin_powered h
  cases a with
  | zero =>
    simp only [Nat.pow_zero, Nat.one_mul] at he
    rwa [he]
  | succ a =>
    rw [Nat.pow_succ] at he
    have e : n = 2*(2^a*m) := by grind
    omega

def total : List Nat → Nat
  | [] => 0
  | a::as => a + total as

def correction : List Nat → Nat
  | [] => 0
  | a::as => 3^as.length + 2^a * correction as

def PositiveGaps (as : List Nat) : Prop := ∀ a ∈ as, 0 < a

/-- A finite word of positive exponent gaps, satisfying the full witness identity. -/
def Certificate (n : Nat) (as : List Nat) : Prop :=
  PositiveGaps as ∧ 3^as.length*n + correction as = 2^total as

theorem witness_certificate {n : Nat} (h : Witness n) : ∃ as, Certificate n as := by
  induction h with
  | one => exact ⟨[],by simp [Certificate, PositiveGaps, correction, total]⟩
  | @step n m a ha he hm ih =>
    obtain ⟨as,hpos,heq⟩ := ih
    refine ⟨a::as,?_,?_⟩
    · intro b hb
      cases hb with
      | head => exact ha
      | tail _ hb => exact hpos b hb
    · simp only [List.length_cons, correction, total, Nat.pow_succ, Nat.pow_add]
      calc
        3^as.length * 3 * n + (3^as.length + 2^a * correction as) =
            3^as.length * (3*n+1) + 2^a * correction as := by grind
        _ = 2^a * (3^as.length*m + correction as) := by rw [he]; grind
        _ = 2^a * 2^total as := by rw [heq]

theorem certificate_witness {n : Nat} {as : List Nat} (h : Certificate n as) : Witness n := by
  induction as generalizing n with
  | nil =>
    have hn : n = 1 := by simpa [Certificate, correction, total] using h.2
    subst n
    exact Witness.one
  | cons a as ih =>
    obtain ⟨hpos,he⟩ := h
    have ha : 0 < a := hpos a (by simp)
    have ht : PositiveGaps as := fun b hb => hpos b (by simp [hb])
    have e : 3^as.length * (3*n+1) + 2^a * correction as = 2^a * 2^total as := by
      simp only [List.length_cons, correction, total, Nat.pow_succ, Nat.pow_add] at he
      grind
    have hd : 2^a ∣ 3^as.length * (3*n+1) := by
      have sumd : 2^a ∣ 3^as.length * (3*n+1) + 2^a * correction as :=
        ⟨2^total as,e⟩
      have rest : 2^a ∣ 2^a * correction as := ⟨correction as,rfl⟩
      exact (Nat.dvd_add_iff_left rest).mpr sumd
    have hc : Nat.Coprime (2^a) (3^as.length) := by
      exact Nat.gcd_pow_right_of_gcd_eq_one (Nat.gcd_pow_left_of_gcd_eq_one (by decide : Nat.gcd 2 3 = 1))
    obtain ⟨m,hm⟩ := hc.dvd_of_dvd_mul_left hd
    have hm_eq : 3*n+1 = 2^a*m := hm
    have tail_eq : 3^as.length*m + correction as = 2^total as := by
      rw [hm_eq] at e
      have ep : 2^a * (3^as.length*m + correction as) = 2^a * 2^total as := by grind
      exact Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide)) ep
    exact Witness.step ha hm_eq (ih ⟨ht,tail_eq⟩)

theorem certificate_iff_basin (n : Nat) (hn : n % 2 = 1) :
    (∃ as, Certificate n as) ↔ Basin n := by
  constructor
  · rintro ⟨as,ha⟩
    exact witness_basin (certificate_witness ha)
  · intro h
    exact witness_certificate ((witness_iff_basin n hn).mpr h)

/-! The original increasing-tuple representation, rather than a fixed word format. -/

/-- `sum j<r, 3^(r-1-j) * 2^(A j)`, written recursively without a library sum. -/
def offset (A : Nat → Nat) : Nat → Nat
  | 0 => 0
  | r+1 => 3 * offset A r + 2^(A r)

def Increasing (r : Nat) (A : Nat → Nat) : Prop :=
  ∀ i j, i < j → j ≤ r → A i < A j

/-- Exactly the positive-integer set in the question. The tuple is extended
arbitrarily beyond `r`; all conditions only inspect indices at most `r`. -/
def E (n : Nat) : Prop :=
  0 < n ∧ ∃ r A, A 0 = 0 ∧ Increasing r A ∧
    3^r*n + offset A r = 2^(A r)

def schedule : List Nat → Nat → Nat
  | [], _ => 0
  | _::_, 0 => 0
  | a::as, i+1 => a + schedule as i

theorem schedule_zero (as : List Nat) : schedule as 0 = 0 := by cases as <;> rfl

theorem schedule_end (as : List Nat) : schedule as as.length = total as := by
  induction as with
  | nil => rfl
  | cons a as ih => simpa [schedule, total] using congrArg (a + ·) ih

theorem schedule_increasing {as : List Nat} (hp : PositiveGaps as) :
    Increasing as.length (schedule as) := by
  induction as with
  | nil => intro i j hij hj; simp at hj; omega
  | cons a as ih =>
    have ha : 0 < a := hp a (by simp)
    have ht : PositiveGaps as := fun b hb => hp b (by simp [hb])
    intro i j hij hj
    cases j with
    | zero => omega
    | succ j =>
      cases i with
      | zero => simp only [schedule]; omega
      | succ i =>
        have h := ih ht i j (by omega) (by simpa using hj)
        simpa only [schedule] using Nat.add_lt_add_left h a

theorem offset_congr {r : Nat} {A B : Nat → Nat}
    (h : ∀ i, i < r → A i = B i) : offset A r = offset B r := by
  induction r with
  | zero => rfl
  | succ r ih =>
    simp only [offset]
    rw [ih (fun i hi => h i (by omega)), h r (by omega)]

theorem offset_schedule_cons (a : Nat) (as : List Nat) (r : Nat) :
    offset (schedule (a::as)) (r+1) = 3^r + 2^a * offset (schedule as) r := by
  induction r with
  | zero => simp [offset, schedule]
  | succ r ih =>
    change 3 * offset (schedule (a::as)) (r+1) + 2^(a + schedule as r) =
      3^(r+1) + 2^a * (3 * offset (schedule as) r + 2^(schedule as r))
    rw [ih, Nat.pow_add, Nat.pow_succ]
    grind

theorem offset_schedule (as : List Nat) : offset (schedule as) as.length = correction as := by
  induction as with
  | nil => rfl
  | cons a as ih =>
    rw [List.length_cons, offset_schedule_cons, ih]
    rfl

theorem schedule_exists (r : Nat) (A : Nat → Nat) (h0 : A 0 = 0)
    (hi : Increasing r A) :
    ∃ as, PositiveGaps as ∧ as.length = r ∧ ∀ i, i ≤ r → schedule as i = A i := by
  induction r generalizing A with
  | zero =>
    refine ⟨[],by simp [PositiveGaps],rfl,?_⟩
    intro i hi
    have e : i = 0 := by omega
    subst i
    exact h0.symm
  | succ r ih =>
    let B := fun i => A (i+1) - A 1
    have hb0 : B 0 = 0 := by simp [B]
    have hbound : ∀ j, j ≤ r → A 1 ≤ A (j+1) := by
      intro j hj
      by_cases hz : j = 0
      · simp [hz]
      · have h := hi 1 (j+1) (by omega) (by omega); omega
    have hbi : Increasing r B := by
      intro i j hij hj
      have hij' := hi (i+1) (j+1) (by omega) (by omega)
      have hsmall := hbound i (by omega)
      dsimp [B]
      omega
    obtain ⟨as,hpos,hlen,hs⟩ := ih B hb0 hbi
    refine ⟨A 1::as,?_,by simp [hlen],?_⟩
    · intro a ha
      cases ha with
      | head => have h := hi 0 1 (by omega) (by omega); omega
      | tail _ ha => exact hpos a ha
    · intro i hir
      cases i with
      | zero => simpa [schedule] using h0.symm
      | succ i =>
        have h := hs i (by omega)
        have hb := hbound i (by omega)
        simp only [schedule, h]
        dsimp [B]
        omega

theorem e_iff_certificate (n : Nat) : E n ↔ ∃ as, Certificate n as := by
  constructor
  · rintro ⟨hn,r,A,h0,hi,he⟩
    obtain ⟨as,hpos,hlen,hs⟩ := schedule_exists r A h0 hi
    refine ⟨as,hpos,?_⟩
    have hc : correction as = offset A r := by
      rw [← offset_schedule, hlen]
      exact offset_congr (fun i hi => hs i (by omega))
    have ht : total as = A r := by rw [← schedule_end, hlen]; exact hs r (by omega)
    simpa only [hlen, hc, ht] using he
  · rintro ⟨as,hpos,he⟩
    have hw : Witness n := certificate_witness ⟨hpos,he⟩
    have hn : 0 < n := by have := witness_odd hw; omega
    refine ⟨hn,as.length,schedule as,schedule_zero as,schedule_increasing hpos,?_⟩
    simpa only [offset_schedule, schedule_end] using he

theorem e_iff_odd_basin (n : Nat) : E n ↔ n % 2 = 1 ∧ Basin n := by
  rw [e_iff_certificate]
  constructor
  · rintro ⟨as,ha⟩
    have h := certificate_witness ha
    exact ⟨witness_odd h,witness_basin h⟩
  · rintro ⟨ho,hb⟩
    exact (certificate_iff_basin n ho).mpr hb

def ResidueImplication : Prop :=
  ∀ x : Nat, E x → (x % 512 = 129 ∨ x % 512 = 257 ∨ x % 512 = 385) → E ((x+1)/2)

/-- The exact unrestricted-length witness implication in the question is equivalent
to convergence of every positive ordinary integer. The finite reverse cover used
in the reverse direction is the explicitly imported PR146 kernel theorem. -/
theorem original_iff_collatz : ResidueImplication ↔ ∀ n : Nat, 0 < n → Basin n := by
  constructor
  · intro h
    apply collatz_iff_deep_reverse_binary.mpr
    intro k hk hx
    have he : E (128*k+1) := (e_iff_odd_basin _).mpr ⟨by omega,hx⟩
    have hr : (128*k+1)%512 = 129 ∨ (128*k+1)%512 = 257 ∨ (128*k+1)%512 = 385 := by omega
    have low := (e_iff_odd_basin _).mp (h (128*k+1) he hr)
    have eq : (128*k+1+1)/2 = 64*k+1 := by omega
    rw [eq] at low
    exact low.2
  · intro h x hx hr
    apply (e_iff_odd_basin _).mpr
    exact ⟨by omega,h _ (by omega)⟩

end CollatzWitness

import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Finite first-exit comparison. The two external asymptotic estimates
are hypotheses in the written application, not Lean axioms. -/
namespace Collatz.ReciprocalCycle
open Real

def InBand (K : ℝ) (t : ℝ) : Prop := 0 ≤ t ∧ t ≤ K

/-- Small one-sided drift cannot change the side of a separated boundary. -/
theorem side_agreement {c e t : ℝ} (he : 0 ≤ e) (h : e < |c-t|) :
    (c+e < t ↔ c < t) ∧ (t < c+e ↔ t < c) := by
  rcases le_total c t with hct | htc
  · rw [abs_of_nonpos (sub_nonpos.mpr hct)] at h
    constructor <;> constructor <;> intro _ <;> linarith
  · rw [abs_of_nonneg (sub_nonneg.mpr htc)] at h
    constructor <;> constructor <;> intro _ <;> linarith

/-- Counts B protected starting values. Every group of B+1 such
starts in an orbit would contain an exact repeat. -/
theorem impossible_long_prefix {B : ℕ} (x : Fin (B+1) → ℝ)
    (S : Finset ℝ) (hcard : S.card ≤ B) (hm : ∀ i, x i ∈ S)
    (hsep : ∀ i j, i < j → x i ≠ x j) : False := by
  let f : Fin (B+1) → S := fun i => ⟨x i, hm i⟩
  have hc : Fintype.card S < Fintype.card (Fin (B+1)) := by
    simpa using Nat.lt_succ_of_le hcard
  obtain ⟨i,j,hij,heq⟩ := Fintype.exists_ne_map_eq_of_card_lt f hc
  have he : x i = x j := congrArg Subtype.val heq
  rcases lt_or_gt_of_ne hij with hl | hr
  · exact hsep i j hl he
  · exact hsep j i hr he.symm

/-- The log pair separation required in the preceding count follows
from the correction being smaller than the homogeneous log gap. -/
theorem no_closed_pair {x y c e : ℝ} (hc : 0 ≤ e) (h : e < |c|)
    (hxy : y - x = c+e) : x ≠ y := by
  intro he
  subst y
  have hz : c = -e := by linarith
  rw [hz, abs_neg, abs_of_nonneg hc] at h
  exact (lt_irrefl e h)

/-- If a physical first exit occurs at j, separated coefficients
through j give the very same first exit and both directions. Time zero
is handled by the shared initial zero, without asking for separation. -/
theorem first_exit {K : ℝ} {j : ℕ} {c y err : ℕ → ℝ}
    (hj : 0 < j) (h0 : c 0 = y 0)
    (hin : ∀ i < j, InBand K (y i)) (hout : ¬ InBand K (y j))
    (hc : ∀ i, 0 < i → i ≤ j → y i = c i + err i)
    (hpos : ∀ i, 0 < i → i ≤ j → 0 ≤ err i)
    (hlo : ∀ i, 0 < i → i ≤ j → err i < |c i - 0|)
    (hhi : ∀ i, 0 < i → i ≤ j → err i < |c i - K|) :
    (∀ i < j, InBand K (c i)) ∧ ¬ InBand K (c j) ∧
    (y j < 0 ↔ c j < 0) ∧ (K < y j ↔ K < c j) := by
  have sides (i : ℕ) (hi : 0 < i) (hi' : i ≤ j) :
      (y i < 0 ↔ c i < 0) ∧ (K < y i ↔ K < c i) := by
    rw [hc i hi hi']
    exact ⟨(side_agreement (hpos i hi hi') (hlo i hi hi')).1,
      (side_agreement (hpos i hi hi') (hhi i hi hi')).2⟩
  have eqb (i : ℕ) (hi : 0 < i) (hi' : i ≤ j) : InBand K (y i) ↔ InBand K (c i) := by
    obtain ⟨a,b⟩ := sides i hi hi'
    unfold InBand
    exact and_congr (by simpa only [not_lt] using not_congr a) (by simpa only [not_lt] using not_congr b)
  refine ⟨?_, fun h => hout ((eqb j hj le_rfl).mpr h), sides j hj le_rfl⟩
  intro i hi
  rcases Nat.eq_zero_or_pos i with h | h
  · simpa [h,h0] using hin i hi
  · exact (eqb i h hi.le).mp (hin i hi)

/-- One odd shortcut edge, written with an integral denominator. -/
theorem odd_log_drift {x y : ℝ} (hx : 0 < x) (he : 2*y = 3*x+1) :
    log y - log x = log 3 - log 2 + log (1+1/(3*x)) := by
  have hy : y = (3*x/2)*(1+1/(3*x)) := by
    field_simp
    nlinarith [he]
  rw [hy, log_mul (by positivity) (by positivity),
    log_div (by positivity) (by norm_num), log_mul (by norm_num) hx.ne']
  ring

/-- The finite window count and the separated repeat equation force a first
physical exit by B+N. All appearances of the observation at the window
endpoint are included. -/
theorem exit_by_window_count {B N : ℕ} {K : ℝ} (y : ℕ → ℝ)
    (hstart : InBand K (y 0)) (S : Finset ℝ) (hcard : S.card ≤ B)
    (hcount : ∀ i, (∀ k ≤ N, InBand K (y (i+k))) → y i ∈ S)
    (hsep : (∀ t ≤ B+N, InBand K (y t)) →
      ∀ i j : Fin (B+1), i < j → y i ≠ y j) :
    ∃ j, 0 < j ∧ j ≤ B+N ∧ (∀ i < j, InBand K (y i)) ∧ ¬InBand K (y j) := by
  classical
  have hnot : ¬ (∀ t ≤ B+N, InBand K (y t)) := by
    intro h
    apply impossible_long_prefix (fun i : Fin (B+1) => y i) S hcard _ (hsep h)
    intro i
    apply hcount
    intro k hk
    exact h _ (Nat.add_le_add (Nat.le_of_lt_succ i.isLt) hk)
  push Not at hnot
  let j := Nat.find hnot
  obtain ⟨hbound,hout⟩ := Nat.find_spec hnot
  refine ⟨j,?_,hbound,?_,hout⟩
  · by_contra! h
    have hz : j = 0 := Nat.eq_zero_of_le_zero h
    change ¬ InBand K (y j) at hout
    exact hout (by rw [hz]; exact hstart)
  · intro i hi
    by_contra hn
    exact Nat.find_min hnot hi ⟨hi.le.trans hbound,hn⟩

def shortcut (n : ℕ) : ℕ :=
  if n%2 = 0 then n/2 else (3*n+1)/2

def trace (x : ℕ) : ℕ → ℕ
  | 0 => x
  | n+1 => shortcut (trace x n)

def oddCount (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => oddCount x n + (trace x n)%2

noncomputable def edgeError (x : ℕ) : ℝ :=
  if x%2=0 then 0 else log (1+1/(3*(x : ℝ)))

noncomputable def errorSum (x : ℕ) : ℕ → ℝ
  | 0 => 0
  | n+1 => errorSum x n + edgeError (trace x n)

theorem shortcut_pos {x : ℕ} (hx : 0 < x) : 0 < shortcut x := by
  unfold shortcut
  split <;> omega

theorem trace_pos {x : ℕ} (hx : 0 < x) (n : ℕ) : 0 < trace x n := by
  induction n with
  | zero => exact hx
  | succ n ih => exact shortcut_pos ih

theorem step_log {x : ℕ} (hx : 0 < x) :
    log (shortcut x : ℝ) - log (x : ℝ) =
      ((x%2 : ℕ) : ℝ)*log 3 - log 2 + edgeError x := by
  have hxr : 0 < (x : ℝ) := by exact_mod_cast hx
  by_cases h : x%2=0
  · have he : 2*(shortcut x) = x := by simp [shortcut,h]; omega
    have he' : ((shortcut x : ℕ) : ℝ) = (x : ℝ) / 2 := by
      have he'' : 2*((shortcut x : ℕ) : ℝ) = (x : ℝ) := by exact_mod_cast he
      linarith
    simp [edgeError,h,he',log_div hxr.ne' (by norm_num : (2:ℝ) ≠ 0)]
  · have ho : x%2=1 := by omega
    have he : 2*(shortcut x) = 3*x+1 := by simp [shortcut,h]; omega
    have he' : 2*((shortcut x : ℕ) : ℝ) = 3*(x : ℝ)+1 := by exact_mod_cast he
    simpa [edgeError, h, ho] using odd_log_drift hxr he'

theorem physical_log {x : ℕ} (hx : 0 < x) (n : ℕ) :
    log (trace x n : ℝ) - log (x : ℝ) =
      (oddCount x n : ℝ)*log 3 - (n : ℝ)*log 2 + errorSum x n := by
  induction n with
  | zero => simp [trace, oddCount, errorSum]
  | succ n ih =>
    have h := step_log (trace_pos hx n)
    simp only [trace, oddCount, errorSum, Nat.cast_add, Nat.cast_succ]
    linear_combination ih+h

theorem error_bounds {x n : ℕ} {X : ℝ} (hX : 0 < X)
    (hf : ∀ i < n, X ≤ (trace x i : ℝ)) :
    0 ≤ errorSum x n ∧ errorSum x n ≤ (n : ℝ)/(3*X) := by
  induction n with
  | zero => simp [errorSum]
  | succ n ih =>
    have hnow := hf n (Nat.lt_succ_self n)
    have hpos : 0 < (trace x n : ℝ) := hX.trans_le hnow
    obtain ⟨ha,hb⟩ := ih (fun i hi => hf i (Nat.lt_succ_of_lt hi))
    have hd : 0 ≤ edgeError (trace x n) ∧ edgeError (trace x n) ≤ 1/(3*X) := by
      unfold edgeError
      split
      · exact ⟨le_rfl, by positivity⟩
      · refine ⟨log_nonneg (le_add_of_nonneg_right (by positivity)),?_⟩
        calc
          log (1+1/(3*(trace x n : ℝ))) ≤ (1+1/(3*(trace x n : ℝ)))-1 :=
            log_le_sub_one_of_pos (by positivity)
          _ = 1/(3*(trace x n : ℝ)) := by ring
          _ ≤ 1/(3*X) := one_div_le_one_div_of_le (by positivity) (by linarith)
    simp only [errorSum,Nat.cast_succ,add_div]
    exact ⟨add_nonneg ha hd.1,add_le_add hb hd.2⟩

noncomputable def level (x n : ℕ) := log (trace x n : ℝ) - log (x : ℝ)
noncomputable def gain (x n : ℕ) := (oddCount x n : ℝ)*log 3 - (n : ℝ)*log 2

/-- Physical conclusion from a finite located-source bound and two uniform
arithmetic separations. The lower separation permits arbitrary integer odd
counts, so subtraction across any actual pair is legitimate. The upper
separation needs only the observed prefixes. All three premises are explicit. -/
theorem ordinary_first_exit {x B N : ℕ} (hx : 0 < x) {K : ℝ} (hK : 0 ≤ K)
    (S : Finset ℕ) (hcard : S.card ≤ B)
    (hcount : ∀ i, (∀ k ≤ N, InBand K (level x (i+k))) → trace x i ∈ S)
    (hlow : ∀ l : ℕ, 0 < l → l ≤ B+N → ∀ u : ℤ,
      ((B+N : ℕ) : ℝ)/(3*x) < |(u:ℝ)*log 3 - (l:ℝ)*log 2|)
    (hupper : ∀ i : ℕ, 0 < i → i ≤ B+N →
      ((B+N : ℕ) : ℝ)/(3*x) < |gain x i - K|) :
    ∃ j, 0 < j ∧ j ≤ B+N ∧
      (∀ i < j, InBand K (level x i) ∧ InBand K (gain x i)) ∧
      ¬InBand K (level x j) ∧ ¬InBand K (gain x j) ∧
      (level x j < 0 ↔ gain x j < 0) ∧ (K < level x j ↔ K < gain x j) := by
  classical
  have hxr : 0 < (x : ℝ) := by exact_mod_cast hx
  let U := B+N
  let H := (U : ℝ)/(3*x)
  have hb (t : ℕ) (ht : t ≤ U) (hs : ∀ k < t, InBand K (level x k)) :
      0 ≤ errorSum x t ∧ errorSum x t ≤ H := by
    have hfloor (k : ℕ) (hk : k < t) : (x:ℝ) ≤ (trace x k : ℝ) := by
      have htr : 0 < (trace x k : ℝ) := by exact_mod_cast trace_pos hx k
      exact (log_le_log_iff hxr htr).mp (sub_nonneg.mp (hs k hk).1)
    obtain ⟨h1,h2⟩ := error_bounds hxr hfloor
    exact ⟨h1,h2.trans (div_le_div_of_nonneg_right (by exact_mod_cast ht) (by positivity))⟩
  let f : ℕ → ℝ := fun n => log (n:ℝ) - log (x:ℝ)
  have hstart : InBand K (level x 0) := by simpa [InBand,level,trace] using hK
  have hsource (i : ℕ) (hi : ∀ k ≤ N, InBand K (level x (i+k))) :
      level x i ∈ S.image f := Finset.mem_image.mpr ⟨_,hcount i hi,rfl⟩
  have hsep (hin : ∀ t ≤ B+N, InBand K (level x t))
      (i j : Fin (B+1)) (hij : i < j) : level x i ≠ level x j := by
    have hi : (i:ℕ) ≤ U := le_trans (Nat.le_of_lt_succ i.isLt) (Nat.le_add_right B N)
    have hj : (j:ℕ) ≤ U := le_trans (Nat.le_of_lt_succ j.isLt) (Nat.le_add_right B N)
    have hlt : (i:ℕ) < (j:ℕ) := hij
    have hi' := hb i hi (fun k hk => hin k (hk.le.trans hi))
    have hj' := hb j hj (fun k hk => hin k (hk.le.trans hj))
    have hlg := hlow ((j:ℕ)-i) (by omega) ((Nat.sub_le ..).trans hj)
      ((oddCount x j : ℤ) - (oddCount x i : ℤ))
    rw [Nat.cast_sub hlt.le, Int.cast_sub, Int.cast_natCast, Int.cast_natCast] at hlg
    intro he
    have hiid := physical_log hx i
    have hjid := physical_log hx j
    change log _ - log _ = log _ - log _ at he
    have diff : ((oddCount x j : ℝ) - (oddCount x i : ℝ))*log 3 -
      ((j:ℝ)-(i:ℝ))*log 2 = errorSum x i - errorSum x j := by
      linear_combination -he + hjid.symm + hiid
    rw [diff] at hlg
    have hu : |errorSum x i-errorSum x j| ≤ H :=
      abs_le.mpr ⟨by linarith [hi'.1,hj'.2],by linarith [hi'.2,hj'.1]⟩
    exact (not_lt_of_ge hu) hlg
  obtain ⟨j,hj,hju,hin,hout⟩ :=
    exit_by_window_count (level x) hstart (S.image f) (Finset.card_image_le.trans hcard) hsource hsep
  have he (i : ℕ) (hi : i ≤ j) := hb i (hi.trans hju) (fun k hk => hin k (hk.trans_le hi))
  have hlow' (i : ℕ) (hi : 0 < i) (hi' : i ≤ j) : errorSum x i < |gain x i - 0| := by
    simpa [gain] using (he i hi').2.trans_lt (hlow i hi (hi'.trans hju) (oddCount x i))
  have hzero : gain x 0 = level x 0 := by simp [level,gain,trace,oddCount]
  obtain ⟨hbefore,hother,hdirection⟩ :=
    first_exit hj hzero hin hout (fun i _ _ => physical_log hx i)
      (fun i _ hi => (he i hi).1) hlow'
      (fun i hi hi' => (he i hi').2.trans_lt (hupper i hi (hi'.trans hju)))
  exact ⟨j,hj,hju,fun i hi => ⟨hin i hi,hbefore i hi⟩,hout,hother,hdirection⟩

#print axioms ordinary_first_exit
#print axioms first_exit
#print axioms exit_by_window_count
#print axioms physical_log
#print axioms error_bounds

end Collatz.ReciprocalCycle

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
Finite entropy for one unchanged family of integer source-path equations.
The geometric product is only a comparison distribution. The observed word
law can be arbitrarily dependent. GapPath is an algebraic path predicate;
actual Syracuse paths satisfy it, and gapWord encodes positive gaps as val+1.
The weak-limit, entropy-dimension and collision consequences are written
separately; this module assumes no open Collatz or analytic proposition.
-/

open scoped BigOperators

namespace CollatzOriginalEntropy

noncomputable def entropy {ι : Type*} [Fintype ι] (p : ι → ℝ) : ℝ :=
  ∑ i, -p i * Real.log (p i)

theorem entropy_le_crossEntropy {ι : Type*} [Fintype ι]
    (p q : ι → ℝ) (hp : ∀ i, 0 ≤ p i) (hq : ∀ i, 0 < q i)
    (hs : ∑ i, p i = 1) (hqs : ∑ i, q i ≤ 1) :
    entropy p ≤ ∑ i, -p i * Real.log (q i) := by
  have hi (i : ι) :
      -p i * Real.log (p i) ≤ -p i * Real.log (q i) + q i - p i := by
    by_cases hz : p i = 0
    · simp only [hz, neg_zero, Real.log_zero, zero_mul, zero_add, sub_zero]
      exact (hq i).le
    · have hpos : 0 < p i := lt_of_le_of_ne (hp i) (Ne.symm hz)
      have hlog := Real.log_le_sub_one_of_pos (div_pos (hq i) hpos)
      rw [Real.log_div (ne_of_gt (hq i)) hz] at hlog
      have hm := mul_le_mul_of_nonneg_left hlog (hp i)
      have hdiv : p i * (q i / p i) = q i := by field_simp
      nlinarith
  have hsum := Finset.sum_le_sum (fun i (_ : i ∈ Finset.univ) => hi i)
  simp only [Finset.sum_sub_distrib, Finset.sum_add_distrib, hs] at hsum
  unfold entropy
  linarith

noncomputable def push {ι κ : Type*} [Fintype ι] [DecidableEq κ]
    (f : ι → κ) (p : ι → ℝ) (j : κ) : ℝ :=
  ∑ i, if f i = j then p i else 0

theorem push_nonneg {ι κ : Type*} [Fintype ι] [DecidableEq κ]
    (f : ι → κ) (p : ι → ℝ) (hp : ∀ i, 0 ≤ p i) (j : κ) :
    0 ≤ push f p j := by
  unfold push
  exact Finset.sum_nonneg (fun i _ => by split_ifs; exact hp i; rfl)

theorem le_push {ι κ : Type*} [Fintype ι] [DecidableEq κ]
    (f : ι → κ) (p : ι → ℝ) (hp : ∀ i, 0 ≤ p i) (i : ι) :
    p i ≤ push f p (f i) := by
  classical
  unfold push
  have h := Finset.single_le_sum
    (s := (Finset.univ : Finset ι))
    (f := fun j => if f j = f i then p j else 0)
    (fun j _ => by split_ifs; exact hp j; rfl) (Finset.mem_univ i)
  simpa using h

theorem push_sum {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq κ]
    (f : ι → κ) (p : ι → ℝ) : (∑ j, push f p j) = ∑ i, p i := by
  classical
  unfold push
  rw [Finset.sum_comm]
  simp

theorem sum_push_mul {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq κ]
    (f : ι → κ) (p : ι → ℝ) (t : κ → ℝ) :
    (∑ j, push f p j*t j) = ∑ i, p i*t (f i) := by
  classical
  unfold push
  simp only [Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _
  simp [ite_mul]

theorem push_comp {ι κ τ : Type*} [Fintype ι] [Fintype κ]
    [DecidableEq κ] [DecidableEq τ] (f : ι → κ) (g : κ → τ) (p : ι → ℝ) :
    push g (push f p) = push (g ∘ f) p := by
  classical
  funext j
  have h := sum_push_mul f p (fun k => if g k=j then 1 else 0)
  simpa [push, mul_ite] using h

theorem entropy_push_le {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq κ]
    (f : ι → κ) (p : ι → ℝ) (hp : ∀ i, 0 ≤ p i) :
    entropy (push f p) ≤ entropy p := by
  classical
  have heq : entropy (push f p) = ∑ i, -p i * Real.log (push f p (f i)) := by
    unfold entropy
    conv_lhs =>
      arg 2
      ext j
      rw [show push f p j = ∑ i, if f i = j then p i else 0 from rfl]
    simp only [← Finset.sum_neg_distrib, Finset.sum_mul]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro i _
    simp only [ite_mul, neg_ite, neg_zero, zero_mul]
    simp [push]
  rw [heq]
  unfold entropy
  apply Finset.sum_le_sum
  intro i _
  by_cases hz : p i = 0
  · simp [hz]
  · have hpos : 0 < p i := lt_of_le_of_ne (hp i) (Ne.symm hz)
    have hlog := Real.log_le_log hpos (le_push f p hp i)
    exact mul_le_mul_of_nonpos_left hlog (neg_nonpos.mpr (hp i))

theorem geometric_mass (ρ : ℝ) (M : ℕ) :
    (∑ a : Fin M, (1-ρ)*ρ^a.val) = 1-ρ^M := by
  have h (n : ℕ) : (∑ a ∈ Finset.range n, (1-ρ)*ρ^a) = 1-ρ^n := by
    induction n with
    | zero => simp
    | succ n ih =>
      rw [Finset.sum_range_succ, ih, pow_succ]
      ring
  exact (Fin.sum_univ_eq_sum_range (fun a : ℕ => (1-ρ)*ρ^a) M).trans (h M)

noncomputable def codeProb {m M : ℕ} (ρ : ℝ) (v : Fin m → Fin M) : ℝ :=
  ∏ i, (1-ρ)*ρ^(v i).val

noncomputable def excess {m M : ℕ} (v : Fin m → Fin M) : ℝ :=
  ∑ i, ((v i).val : ℝ)

theorem codeProb_pos {m M : ℕ} {ρ : ℝ} (hρ : 0 < ρ) (hρ1 : ρ < 1)
    (v : Fin m → Fin M) : 0 < codeProb ρ v := by
  unfold codeProb
  exact Finset.prod_pos (fun i _ => mul_pos (sub_pos.mpr hρ1) (pow_pos hρ _))

theorem codeProb_sum_le {m M : ℕ} {ρ : ℝ} (hρ : 0 < ρ) (hρ1 : ρ < 1) :
    (∑ v : Fin m → Fin M, codeProb ρ v) ≤ 1 := by
  unfold codeProb
  rw [← Fintype.prod_sum (fun (_ : Fin m) (a : Fin M) => (1-ρ)*ρ^a.val)]
  apply Finset.prod_le_one₀
  · intro i _
    apply Finset.sum_nonneg
    intro a _
    exact (mul_pos (sub_pos.mpr hρ1) (pow_pos hρ _)).le
  · intro i _
    rw [geometric_mass]
    have h := (pow_pos hρ M).le
    linarith

theorem log_codeProb {m M : ℕ} {ρ : ℝ} (hρ : 0 < ρ) (hρ1 : ρ < 1)
    (v : Fin m → Fin M) :
    Real.log (codeProb ρ v) =
      (m : ℝ)*Real.log (1-ρ) + excess v*Real.log ρ := by
  unfold codeProb
  rw [Real.log_prod (fun i _ => ne_of_gt (mul_pos (sub_pos.mpr hρ1) (pow_pos hρ _)))]
  simp_rw [Real.log_mul (ne_of_gt (sub_pos.mpr hρ1)) (ne_of_gt (pow_pos hρ _)),
    Real.log_pow]
  simp [excess, Finset.sum_add_distrib, ← Finset.sum_mul, mul_comm]

theorem finite_word_entropy_bound {m M : ℕ} {κ : Type*} [Fintype κ] [DecidableEq κ]
    (f : (Fin m → Fin M) → κ) (p : (Fin m → Fin M) → ℝ)
    (hp : ∀ v, 0 ≤ p v) (hs : ∑ v, p v = 1)
    {ρ : ℝ} (hρ : 0 < ρ) (hρ1 : ρ < 1) :
    entropy (push f p) ≤
      -(m : ℝ)*Real.log (1-ρ) - (∑ v, p v*excess v)*Real.log ρ := by
  apply le_trans (entropy_push_le f p hp)
  have h := entropy_le_crossEntropy p (codeProb ρ) hp
    (codeProb_pos hρ hρ1) hs (codeProb_sum_le hρ hρ1)
  apply h.trans_eq
  simp_rw [log_codeProb hρ hρ1]
  calc
    (∑ v, -p v*((m : ℝ)*Real.log (1-ρ)+excess v*Real.log ρ)) =
        -(∑ v, p v)*((m : ℝ)*Real.log (1-ρ)) -
          (∑ v, p v*excess v)*Real.log ρ := by
      simp only [neg_mul, Finset.sum_mul, ← Finset.sum_neg_distrib,
        ← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro v _
      ring
    _ = _ := by rw [hs]; ring

inductive GapPath : ℕ → List ℕ → ℕ → Prop where
  | nil (n : ℕ) : GapPath n [] n
  | cons {n u r a : ℕ} {w : List ℕ}
      (edge : 3*n+1 = 2^a*u) (tail : GapPath u w r) : GapPath n (a::w) r

def offset : List ℕ → ℕ
  | [] => 0
  | a::w => 3^w.length + 2^a * offset w

theorem gapPath_affine {n r : ℕ} {w : List ℕ} (h : GapPath n w r) :
    3^w.length*n + offset w = 2^w.sum*r := by
  induction h with
  | nil n => simp [offset]
  | @cons n u r a w edge tail ih =>
    simp only [List.length_cons, List.sum_cons, offset, pow_succ, pow_add]
    nlinarith [congrArg (fun x : ℕ => 3^w.length*x) edge,
      congrArg (fun x : ℕ => 2^a*x) ih]

theorem same_word_same_ternary_endpoint {n n' r r' : ℕ} {w : List ℕ}
    (h : GapPath n w r) (h' : GapPath n' w r') :
    r % 3^w.length = r' % 3^w.length := by
  have ha := gapPath_affine h
  have hb := gapPath_affine h'
  have hm : 2^w.sum*r ≡ 2^w.sum*r' [MOD 3^w.length] := by
    rw [← ha, ← hb]
    simp [Nat.ModEq, Nat.add_mod]
  have hc : Nat.Coprime (3^w.length) (2^w.sum) := by
    exact (by decide : Nat.Coprime 3 2).pow _ _
  exact Nat.ModEq.cancel_left_of_coprime hc hm

noncomputable def ternaryCode (w : List ℕ) : Fin (3^w.length) := by
  classical
  exact if h : ∃ r n, GapPath n w r then
    ⟨Classical.choose h % 3^w.length, Nat.mod_lt _ (by positivity)⟩
  else ⟨0, by positivity⟩

theorem endpoint_eq_code {n r : ℕ} {w : List ℕ} (h : GapPath n w r) :
    r % 3^w.length = (ternaryCode w).val := by
  classical
  have he : ∃ s u, GapPath u w s := ⟨r,n,h⟩
  simp only [ternaryCode, dite_eq_left he]
  obtain ⟨u,hu⟩ := Classical.choose_spec he
  exact same_word_same_ternary_endpoint h hu

def gapWord {m M : ℕ} (v : Fin m → Fin M) : List ℕ :=
  List.ofFn (fun i => (v i).val+1)

noncomputable def wordResidue {m M : ℕ} (v : Fin m → Fin M) : Fin (3^m) :=
  ⟨(ternaryCode (gapWord v)).val, by simpa [gapWord] using (ternaryCode (gapWord v)).isLt⟩

theorem physical_endpoint_code {m M n r : ℕ} {v : Fin m → Fin M}
    (h : GapPath n (gapWord v) r) :
    r % 3^m = (wordResidue v).val := by
  simpa [wordResidue, gapWord] using endpoint_eq_code h

/-- The input is an arbitrary finite weighted family of exact gap equations.
No independence is imposed on the words or the sample weights. Every actual
finite Syracuse trajectory is such a family with gap encoded as val+1. -/
theorem finite_original_source_entropy {ι : Type*} [Fintype ι]
    {m M : ℕ} (words : ι → (Fin m → Fin M)) (starts ends : ι → ℕ)
    (paths : ∀ i, GapPath (starts i) (gapWord (words i)) (ends i))
    (p : ι → ℝ) (hp : ∀ i, 0 ≤ p i) (hs : ∑ i, p i=1)
    {ρ : ℝ} (hρ : 0 < ρ) (hρ1 : ρ < 1) :
    entropy (push (fun i => (⟨ends i % 3^m, Nat.mod_lt _ (by positivity)⟩ : Fin (3^m))) p)
    ≤ -(m : ℝ)*Real.log (1-ρ) - (∑ i, p i*excess (words i))*Real.log ρ := by
  classical
  have he (i : ι) :
      (⟨ends i % 3^m, Nat.mod_lt _ (by positivity)⟩ : Fin (3^m)) = wordResidue (words i) := by
    apply Fin.ext
    exact physical_endpoint_code (paths i)
  simp_rw [he]
  have h := finite_word_entropy_bound wordResidue (push words p)
    (push_nonneg words p hp) (by rw [push_sum, hs]) hρ hρ1
  rw [push_comp, sum_push_mul] at h
  exact h

theorem finite_original_source_entropy_of_mean {ι : Type*} [Fintype ι]
    {m M : ℕ} (words : ι → (Fin m → Fin M)) (starts ends : ι → ℕ)
    (paths : ∀ i, GapPath (starts i) (gapWord (words i)) (ends i))
    (p : ι → ℝ) (hp : ∀ i, 0 ≤ p i) (hs : ∑ i, p i=1)
    {a : ℝ} (ha : 1 < a) (hcost : ∑ i, p i*excess (words i) ≤ (m:ℝ)*(a-1)) :
    entropy (push (fun i => (⟨ends i % 3^m, Nat.mod_lt _ (by positivity)⟩ : Fin (3^m))) p)
    ≤ (m:ℝ)*(a*Real.log a-(a-1)*Real.log (a-1)) := by
  let ρ := (a-1)/a
  have ha0 : 0 < a := by linarith
  have ha1 : 0 < a-1 := by linarith
  have hρ : 0 < ρ := div_pos ha1 ha0
  have hρ1 : ρ < 1 := (div_lt_one ha0).mpr (by linarith)
  have hl : Real.log ρ = Real.log (a-1)-Real.log a :=
    Real.log_div ha1.ne' ha0.ne'
  have h1 : 1-ρ = a⁻¹ := by dsimp [ρ]; field_simp; ring
  have hn : 0 ≤ -Real.log ρ := (neg_nonneg.mpr (Real.log_neg hρ hρ1).le)
  have hc := mul_le_mul_of_nonneg_right hcost hn
  calc
    _ ≤ -(m:ℝ)*Real.log (1-ρ) -
        (∑ i, p i*excess (words i))*Real.log ρ :=
      finite_original_source_entropy words starts ends paths p hp hs hρ hρ1
    _ ≤ -(m:ℝ)*Real.log (1-ρ) - ((m:ℝ)*(a-1))*Real.log ρ := by linarith
    _ = _ := by rw [h1, Real.log_inv, hl]; ring

theorem sliding_window_cost_le (a : ℕ → ℝ) (ha : ∀ i, 0 ≤ a i)
    {m N : ℕ} (hm : m ≤ N) :
    (∑ k ∈ Finset.range (N-m+1), ∑ j ∈ Finset.range m, a (k+j))
      ≤ (m : ℝ)*(∑ i ∈ Finset.range N, a i) := by
  rw [Finset.sum_comm]
  calc
    (∑ j ∈ Finset.range m, ∑ k ∈ Finset.range (N-m+1), a (k+j))
        ≤ ∑ _j ∈ Finset.range m, ∑ i ∈ Finset.range N, a i := by
      apply Finset.sum_le_sum
      intro j hj
      have hj' : j < m := Finset.mem_range.mp hj
      apply Finset.sum_le_sum_of_injOn (fun k : ℕ => k+j)
      · intro x _ y _ h
        exact Nat.add_right_cancel h
      · intro k hk
        obtain ⟨x,hx,rfl⟩ := Finset.mem_image.mp hk
        have hx' := Finset.mem_range.mp hx
        apply Finset.mem_range.mpr
        omega
      · intro k _
        rfl
      · intro i _ _
        exact ha i
    _ = _ := by simp [mul_comm]

theorem single_gap_log_identity {x y : ℝ} {a : ℕ}
    (hx : 0 < x) (hy : 0 < y) (h : (2:ℝ)^a*y=3*x+1) :
    (a : ℝ)*Real.log 2 = Real.log 3 + Real.log x - Real.log y +
      Real.log (1+1/(3*x)) := by
  have hz : 0 < 1+1/(3*x) := by positivity
  have he : 3*x+1 = (3*x)*(1+1/(3*x)) := by field_simp
  have hl := congrArg Real.log h
  rw [Real.log_mul (ne_of_gt (pow_pos (by norm_num : (0:ℝ)<2) a)) hy.ne',
    Real.log_pow, he,
    Real.log_mul (ne_of_gt (by positivity : (0:ℝ)<3*x)) hz.ne',
    Real.log_mul (by norm_num : (3:ℝ)≠0) hx.ne'] at hl
  linarith

theorem finite_gap_log_budget (q : ℕ → ℝ) (a : ℕ → ℕ) (N : ℕ)
    (hq : ∀ i ≤ N, 0 < q i)
    (he : ∀ i < N, (2:ℝ)^(a i)*q (i+1)=3*q i+1) :
    (∑ i ∈ Finset.range N, (a i : ℝ))*Real.log 2 =
      (N : ℝ)*Real.log 3 + Real.log (q 0) - Real.log (q N) +
        ∑ i ∈ Finset.range N, Real.log (1+1/(3*q i)) := by
  induction N with
  | zero => simp
  | succ N ih =>
    have hi := ih (fun i h => hq i (by omega)) (fun i h => he i (by omega))
    have hn := single_gap_log_identity (hq N (by omega))
      (hq (N+1) (by omega)) (he N (by omega))
    rw [Finset.sum_range_succ, Finset.sum_range_succ]
    push_cast
    nlinarith

#print axioms entropy_le_crossEntropy
#print axioms push_nonneg
#print axioms le_push
#print axioms push_sum
#print axioms sum_push_mul
#print axioms push_comp
#print axioms entropy_push_le
#print axioms geometric_mass
#print axioms codeProb_pos
#print axioms codeProb_sum_le
#print axioms log_codeProb
#print axioms finite_word_entropy_bound
#print axioms gapPath_affine
#print axioms same_word_same_ternary_endpoint
#print axioms endpoint_eq_code
#print axioms physical_endpoint_code
#print axioms finite_original_source_entropy
#print axioms finite_original_source_entropy_of_mean
#print axioms sliding_window_cost_le
#print axioms single_gap_log_identity
#print axioms finite_gap_log_budget

end CollatzOriginalEntropy

import Mathlib.Algebra.LinearRecurrence
import Mathlib.Algebra.Polynomial.Expand
import Mathlib.RingTheory.Polynomial.Content
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite recurrence rigidity for a dyadic section with multiplier 1/4. -/
namespace Collatz.ReciprocalRigidity.HeckeRank

open Polynomial
open scoped BigOperators

abbrev Seq := ℕ → ℚ

def shift : Module.End ℤ Seq where
  toFun u n := u (n+1)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

private theorem shift_pow (k : ℕ) (u : Seq) (n : ℕ) :
    (shift ^ k) u n = u (n+k) := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    rw [pow_succ', Module.End.mul_apply]
    change (shift^k) u (n+1) = _
    rw [ih]; congr 1; omega

noncomputable def op (p : ℤ[X]) := (aeval shift p : Module.End ℤ Seq)

def Kills (p : ℤ[X]) (u : Seq) : Prop := op p u = 0

private theorem op_at (p : ℤ[X]) (u : Seq) (n : ℕ) :
    op p u n = ∑ j ∈ Finset.range (p.natDegree+1), (p.coeff j : ℚ)*u (n+j) := by
  rw [op, Polynomial.aeval_endomorphism, Polynomial.sum_over_range _ (by simp)]
  simp [Finset.sum_apply, shift_pow, zsmul_eq_mul]

private theorem kills_mul_left {p q : ℤ[X]} {u : Seq} (hp : Kills p u) :
    Kills (q*p) u := by
  unfold Kills op at *; rw [map_mul, Module.End.mul_apply, hp, map_zero]

private theorem reflect_coeff (p : ℤ[X]) (j : ℕ) :
    (p.comp (-X)).coeff j = (-1)^j * p.coeff j := by
  induction p using Polynomial.induction_on' with
  | add p q hp hq => rw [add_comp, coeff_add, hp, hq, coeff_add, mul_add]
  | monomial n a =>
    rw [← C_mul_X_pow_eq_monomial, mul_comp, C_comp, pow_comp, X_comp]
    rw [show (-X : ℤ[X])^n = C ((-1 : ℤ)^n) * X^n by
      rw [map_pow, map_neg, map_one, ← mul_pow, neg_one_mul]]
    rw [← mul_assoc, ← map_mul, C_mul_X_pow_eq_monomial, C_mul_X_pow_eq_monomial]
    by_cases h : n = j <;> simp [coeff_monomial, h, mul_comm]

noncomputable def squared (p : ℤ[X]) := contract 2 (p * p.comp (-X))

private theorem expand_squared (p : ℤ[X]) :
    expand ℤ 2 (squared p) = p * p.comp (-X) := by
  let f := p * p.comp (-X)
  have hf : f.comp (-X) = f := by
    change (p * p.comp (-X)).comp (-X) = _
    rw [mul_comp, comp_neg_X_comp_neg_X, mul_comm]
  ext j
  rw [coeff_expand (by decide)]
  by_cases hj : 2 ∣ j
  · simp only [hj, ↓reduceIte]; rw [squared, coeff_contract (by decide), Nat.div_mul_cancel hj]
  · simp only [hj, ↓reduceIte]
    have hodd : Odd j := Nat.not_even_iff_odd.mp (fun h => hj (even_iff_two_dvd.mp h))
    have h := congrArg (fun q : ℤ[X] => q.coeff j) hf
    rw [reflect_coeff, hodd.neg_one_pow] at h
    change 0 = f.coeff j; omega

private theorem squared_ne_zero {p : ℤ[X]} (hp : p ≠ 0) : squared p ≠ 0 := by
  intro h
  have he := expand_squared p
  rw [h, map_zero] at he
  have hr : p.comp (-X) = 0 := (mul_eq_zero.mp he.symm).resolve_left hp
  have hs := comp_neg_X_comp_neg_X p
  rw [hr, zero_comp] at hs
  exact hp hs.symm

private theorem degree_squared {p : ℤ[X]} (hp : p ≠ 0) :
    (squared p).natDegree = p.natDegree := by
  have he := congrArg natDegree (expand_squared p)
  have hr : p.comp (-X) ≠ 0 := fun h => hp (by simpa [h] using (comp_neg_X_comp_neg_X p).symm)
  rw [natDegree_expand, natDegree_mul hp hr, natDegree_comp] at he
  simp only [natDegree_neg, natDegree_X, mul_one] at he
  omega

private theorem decompose_lc (p : ℤ[X]) :
    (squared p).leadingCoeff = p.leadingCoeff * (p.leadingCoeff * (-1)^p.natDegree) := by
  have he := congrArg leadingCoeff (expand_squared p)
  rw [leadingCoeff_expand (by decide), leadingCoeff_mul, leadingCoeff_comp (by simp)] at he
  simpa using he

private theorem op_monomial (k : ℕ) (a : ℤ) (u : Seq) (n : ℕ) :
    op (monomial k a) u n = (a : ℚ)*u (n+k) := by
  rw [op, aeval_endomorphism, sum_monomial_index _ _ (by simp)]
  simp [shift_pow, zsmul_eq_mul]

private theorem op_decimate (p : ℤ[X]) (u : Seq) (n : ℕ) :
    op p (fun i => u (2*i)) n = op (expand ℤ 2 p) u (2*n) := by
  induction p using Polynomial.induction_on' with
  | add f g hf hg =>
    change (aeval shift (f+g)) _ _ = (aeval shift (expand ℤ 2 (f+g))) _ _
    simp only [map_add, LinearMap.add_apply, Pi.add_apply]; exact congrArg₂ (·+·) hf hg
  | monomial k a => rw [expand_monomial, op_monomial, op_monomial]; ring_nf

private theorem kills_decimate {p : ℤ[X]} {u : Seq} (hp : Kills p u) :
    Kills (squared p) (fun n => u (2*n)) := by
  funext n
  rw [op_decimate, expand_squared, mul_comm]
  exact congrFun (kills_mul_left (q := p.comp (-X)) hp) _

private theorem kills_difference {p : ℤ[X]} {u : Seq} (hp : Kills p u) :
    Kills (p * squared p) (fun n => 4*u (2*n)-u n) := by
  have hd := kills_mul_left (q := p) (kills_decimate hp)
  have ho := kills_mul_left (q := squared p) hp
  rw [mul_comm] at ho
  change op (p * squared p) ((4 : ℤ) • (fun n => u (2*n)) - u) = 0
  rw [map_sub, map_smul, show op (p * squared p) (fun n => u (2*n)) = 0 from hd,
    show op (p * squared p) u = 0 from ho]; simp

private theorem op_last (p : ℤ[X]) (u : Seq) (n : ℕ) :
    op p u n = (∑ i : Fin p.natDegree, (p.coeff i : ℚ)*u (n+i)) +
                  (p.leadingCoeff : ℚ)*u (n+p.natDegree) := by
  rw [op_at, Finset.sum_range_succ, Fin.sum_univ_eq_sum_range (fun j => (p.coeff j : ℚ)*u (n+j))]; rfl

noncomputable def recOf (p : ℤ[X]) : LinearRecurrence ℚ where
  order := p.natDegree
  coeffs i := -(p.coeff i : ℚ) / (p.leadingCoeff : ℚ)

private theorem op_iff (p : ℤ[X]) (hp : p ≠ 0) (u : Seq) (n : ℕ) :
    op p u n = 0 ↔ u (n + (recOf p).order) =
      ∑ i : Fin (recOf p).order, (recOf p).coeffs i * u (n+i) := by
  have hl : (p.leadingCoeff : ℚ) ≠ 0 := by exact_mod_cast leadingCoeff_ne_zero.mpr hp
  rw [op_last]; unfold recOf; dsimp
  simp_rw [div_mul_eq_mul_div, neg_mul]
  simp_rw [div_eq_mul_inv]
  rw [← Finset.sum_mul, Finset.sum_neg_distrib, ← div_eq_mul_inv, eq_div_iff hl, mul_comm (u _)]
  constructor <;> intro h <;> linarith

private theorem solution_iff {p : ℤ[X]} (hp : p ≠ 0) (u : Seq) :
    Kills p u ↔ (recOf p).IsSolution u := by
  constructor
  · intro h n; exact (op_iff p hp u n).mp (congrFun h n)
  · intro h; funext n; exact (op_iff p hp u n).mpr (h n)

private theorem zero_of_initial {p : ℤ[X]} (hp : p ≠ 0) {u : Seq}
    (hk : Kills p u) (hz : ∀ n < p.natDegree, u n = 0) : u = 0 := by
  have hr := (solution_iff hp u).mp hk
  have h0 : (recOf p).IsSolution (0 : Seq) := by intro n; simp
  have hu := (recOf p).eq_mk_of_is_sol_of_eq_init' (init := fun _ => 0) hr (fun n => hz n n.isLt)
  have hv := (recOf p).eq_mk_of_is_sol_of_eq_init' (init := fun _ => 0) h0 (by simp)
  exact hu.trans hv.symm

/-- A global rational recurrence obeying the first `2d` dyadic checks obeys them all. -/
theorem section_globalizes {p : ℤ[X]} {u : Seq} (hp : p ≠ 0) (hk : Kills p u)
    (h : ∀ n < 2*p.natDegree, 4*u (2*n) = u n) : ∀ n, 4*u (2*n) = u n := by
  have hs : p * squared p ≠ 0 := mul_ne_zero hp (squared_ne_zero hp)
  have hz : (fun n => 4*u (2*n)-u n) = (0 : Seq) :=
    zero_of_initial hs (kills_difference hk) (fun n hn => by
      rw [natDegree_mul hp (squared_ne_zero hp), degree_squared hp] at hn
      exact sub_eq_zero.mpr (h n (by omega)))
  intro n; exact sub_eq_zero.mp (congrFun hz n)

private theorem op_constant (c : ℤ) (u : Seq) (n : ℕ) :
    op (C c) u n = (c : ℚ)*u n := by
  rw [op, aeval_endomorphism, sum_C_index (by simp)]; simp [zsmul_eq_mul]

private theorem primitive_kills {p : ℤ[X]} {u : Seq} (hp : p ≠ 0) (hk : Kills p u) :
    Kills p.primPart u := by
  have hh : Kills (C p.content * p.primPart) u := p.eq_C_content_mul_primPart ▸ hk
  have hc : (p.content : ℚ) ≠ 0 := by exact_mod_cast mt content_eq_zero_iff.mp hp
  funext n
  have h := congrFun hh n
  change (aeval shift (C p.content * p.primPart)) u n = 0 at h
  rw [map_mul, Module.End.mul_apply] at h
  change op (C p.content) (op p.primPart u) n = 0 at h
  rw [op_constant] at h
  exact (mul_eq_zero.mp h).resolve_left hc

private theorem reflect_primitive {p : ℤ[X]} (hp : p.IsPrimitive) :
    (p.comp (-X)).IsPrimitive := by
  apply isPrimitive_iff_isUnit_of_C_dvd.mpr
  intro c hc; apply isPrimitive_iff_isUnit_of_C_dvd.mp hp c
  obtain ⟨g, hg⟩ := hc
  use g.comp (-X)
  calc p = (p.comp (-X)).comp (-X) := (comp_neg_X_comp_neg_X p).symm
       _ = _ := by rw [hg, mul_comp, C_comp]

private theorem squared_primitive {p : ℤ[X]} (hp : p.IsPrimitive) :
    (squared p).IsPrimitive := by
  apply isPrimitive_iff_isUnit_of_C_dvd.mpr
  intro c hc
  apply isPrimitive_iff_isUnit_of_C_dvd.mp (hp.mul (reflect_primitive hp)) c
  obtain ⟨g,hg⟩ := hc
  use expand ℤ 2 g
  rw [← expand_squared, hg, map_mul, expand_C]

private theorem scalar_rigidity {p : ℤ[X]} {u : Seq}
    (hp : p ≠ 0) (hpos : 0 < p.natDegree) (hprim : p.IsPrimitive) (hk : Kills p u)
    (hmin : ∀ q : ℤ[X], q ≠ 0 → Kills q u → p.natDegree ≤ q.natDegree)
    (hd : ∀ n, 4*u (2*n) = u n) : p.leadingCoeff = 1 ∨ p.leadingCoeff = -1 := by
  have hFun : (4 : ℤ) • (fun n => u (2*n)) = u := by
    funext n; change (4 : ℚ)*u (2*n) = _; exact hd n
  have hs : Kills (squared p) u := by
    change op (squared p) u = 0
    rw [← hFun, map_smul, show op (squared p) (fun n => u (2*n)) = 0 from kills_decimate hk]; simp
  have hdeg := degree_squared hp
  have hcan : p.cancelLeads (squared p) = C p.leadingCoeff * squared p -
      C (squared p).leadingCoeff * p := by simp [cancelLeads, hdeg]
  have hkill : Kills (p.cancelLeads (squared p)) u := by
    rw [hcan]; unfold Kills op
    rw [map_sub, LinearMap.sub_apply]
    change op (C p.leadingCoeff * squared p) u - op (C (squared p).leadingCoeff * p) u = 0
    rw [show op (C p.leadingCoeff * squared p) u = 0 from kills_mul_left hs,
        show op (C (squared p).leadingCoeff * p) u = 0 from kills_mul_left hk, sub_self]
  have hz : p.cancelLeads (squared p) = 0 := by
    by_contra hz
    have hl := natDegree_cancelLeads_lt_of_natDegree_le_natDegree hdeg.ge (hdeg.symm ▸ hpos)
    have hh := hmin _ hz hkill
    omega
  rw [hcan, sub_eq_zero] at hz
  have hcontent := congrArg content hz
  rw [content_C_mul, content_C_mul, hprim.content_eq_one, (squared_primitive hprim).content_eq_one,
    mul_one, mul_one, ← Int.abs_eq_normalize, ← Int.abs_eq_normalize, decompose_lc,
    abs_mul, abs_mul, abs_pow, abs_neg, abs_one, one_pow, mul_one] at hcontent
  have hne : |p.leadingCoeff| ≠ 0 := mt abs_eq_zero.mp (leadingCoeff_ne_zero.mpr hp)
  have hon : |p.leadingCoeff| = 1 := by
    have hh : |p.leadingCoeff| * (|p.leadingCoeff|-1) = 0 := by nlinarith
    exact sub_eq_zero.mp ((mul_eq_zero.mp hh).resolve_left hne)
  rcases le_total 0 p.leadingCoeff with h|h
  · exact .inl (by simpa [abs_of_nonneg h] using hon)
  · exact .inr (by rw [abs_of_nonpos h] at hon; omega)

/-- A nonzero recurrent dyadic-eigen sequence admits an integral recurrence
with leading coefficient a unit. The proof minimizes the primitive annihilator. -/
theorem integral_leading_unit {u : Seq} (hu : u ≠ 0)
    (hrec : ∃ p : ℤ[X], p ≠ 0 ∧ Kills p u) (hd : ∀ n, 4*u (2*n) = u n) :
    ∃ p : ℤ[X], Kills p u ∧ (p.leadingCoeff = 1 ∨ p.leadingCoeff = -1) := by
  classical
  let P := fun d : ℕ => ∃ p : ℤ[X], p ≠ 0 ∧ Kills p u ∧ p.natDegree = d
  have hex : ∃ d, P d := by obtain ⟨p,hp,hk⟩ := hrec; exact ⟨_,p,hp,hk,rfl⟩
  obtain ⟨q,hq,hkq,hqdeg⟩ := Nat.find_spec hex
  let p := q.primPart
  have hp : p ≠ 0 := q.primPart_ne_zero
  have hk : Kills p u := primitive_kills hq hkq
  have hdg : p.natDegree = Nat.find hex := q.natDegree_primPart.trans hqdeg
  have hpos : 0 < p.natDegree := by
    by_contra h
    exact hu (zero_of_initial hp hk (by intro n hn; omega))
  refine ⟨p,hk,scalar_rigidity hp hpos q.isPrimitive_primPart hk ?_ hd⟩
  intro r hr hkr
  rw [hdg]; apply Nat.find_min'; exact ⟨r,hr,hkr,rfl⟩

private def InGrid (D : ℕ) (x : ℚ) : Prop := ∃ z : ℤ, (D : ℚ)*x = z

private theorem initial_grid (u : Seq) (d : ℕ) :
    ∃ D : ℕ, 0 < D ∧ ∀ n < d, InGrid D (u n) := by
  induction d with
  | zero => exact ⟨1,by decide,by simp⟩
  | succ d ih =>
    obtain ⟨D,hD,hg⟩ := ih
    refine ⟨D*(u d).den, Nat.mul_pos hD (Nat.pos_of_ne_zero (u d).den_nz), ?_⟩
    intro n hn
    by_cases h : n < d
    · obtain ⟨z,hz⟩ := hg n h
      refine ⟨(u d).den*z, ?_⟩
      push_cast; rw [← hz]; ring
    · have he : n = d := by omega
      subst n; refine ⟨(D : ℤ)*(u d).num, ?_⟩
      push_cast; rw [← (u d).mul_den_eq_num]; ring

private theorem full_grid {p : ℤ[X]} {u : Seq} (hk : Kills p u)
    (hp : p.leadingCoeff = 1 ∨ p.leadingCoeff = -1) :
    ∃ D : ℕ, 0 < D ∧ ∀ n, InGrid D (u n) := by
  classical
  obtain ⟨D,hD,hinit⟩ := initial_grid u p.natDegree
  refine ⟨D,hD,?_⟩; intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n < p.natDegree
    · exact hinit n hn
    · let t := n-p.natDegree
      have ht : t+p.natDegree = n := by dsimp [t]; omega
      have hg (i : Fin p.natDegree) : InGrid D (u (t+i)) := ih _ (by have := i.isLt; omega)
      let z := fun i => Classical.choose (hg i)
      have hz (i : Fin p.natDegree) : (D : ℚ)*u (t+i) = z i := Classical.choose_spec (hg i)
      have hs : (D : ℚ)*(∑ i : Fin p.natDegree, (p.coeff i : ℚ)*u (t+i)) =
          ((∑ i : Fin p.natDegree, p.coeff i * z i : ℤ) : ℚ) := by
        push_cast; rw [Finset.mul_sum]; apply Finset.sum_congr rfl
        intro i _; rw [← hz]; ring
      have he := congrFun hk t
      change op p u t = 0 at he
      rw [op_last, ht] at he
      rcases hp with hp|hp
      · refine ⟨-(∑ i : Fin p.natDegree, p.coeff i*z i), ?_⟩
        rw [hp] at he; push_cast at he; rw [Int.cast_neg, ← hs]; simp only [one_mul] at he
        have ha : u n = -(∑ i : Fin p.natDegree, (p.coeff i : ℚ)*u (t+i)) := by linarith
        rw [ha]; ring
      · refine ⟨∑ i : Fin p.natDegree, p.coeff i*z i, ?_⟩
        rw [hp] at he; push_cast at he; rw [← hs]
        have ha : u n = ∑ i : Fin p.natDegree, (p.coeff i : ℚ)*u (t+i) := by linarith
        rw [ha]

private theorem scaled_dyadic {u : Seq} (hd : ∀ n, 4*u (2*n) = u n) (k n : ℕ) :
    (4 : ℚ)^k * u (2^k*n) = u n := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, pow_succ' 2 k, mul_assoc 2, mul_assoc, hd, ih]

/-- The only rational recurrence eigenvector of the even section with eigenvalue
`1/4` is zero. No archimedean hypotheses are needed. -/
theorem recurrent_dyadic_zero {u : Seq} (hrec : ∃ p : ℤ[X], p ≠ 0 ∧ Kills p u)
    (hd : ∀ n, 4*u (2*n) = u n) : u = 0 := by
  by_contra hu
  obtain ⟨p,hk,hunit⟩ := integral_leading_unit hu hrec hd
  obtain ⟨D,hD,hgrid⟩ := full_grid hk hunit
  apply hu; funext n
  obtain ⟨z,hz⟩ := hgrid n
  by_contra hnon
  have hzn : z ≠ 0 := by
    intro h; rw [h, Int.cast_zero] at hz
    exact hnon ((mul_eq_zero.mp hz).resolve_left (by exact_mod_cast Nat.ne_of_gt hD))
  let k := z.natAbs+1
  obtain ⟨w,hw⟩ := hgrid (2^k*n)
  have he : (4 : ℤ)^k*w=z := by
    exact_mod_cast (show (4 : ℚ)^k*(w : ℚ)=(z : ℚ) by
      rw [← hw, ← hz, mul_left_comm, scaled_dyadic hd])
  have hl := Int.natAbs_le_of_dvd_ne_zero (show (4 : ℤ)^k ∣ z from ⟨w,he.symm⟩) hzn
  simp only [Int.natAbs_pow] at hl
  change 4^k ≤ z.natAbs at hl
  have hg : ∀ i : ℕ, i < 4^i := by
    intro i; induction i with
    | zero => decide
    | succ i ih => rw [pow_succ]; omega
  have hh := hg k; dsimp [k] at hh hl; omega

/-- An integer-coefficient homogeneous recurrence, restricted to the prefix
`0,...,N`. Its leading coefficient need only be nonzero. -/
def Fits (p : ℤ[X]) (u : Seq) (N : ℕ) : Prop :=
  ∀ j, j+p.natDegree ≤ N → op p u j = 0

private theorem extend_fits {p : ℤ[X]} (hp : p ≠ 0) {u : Seq} {N : ℕ}
    (hfit : Fits p u N) : ∃ v : Seq, Kills p v ∧ ∀ n ≤ N, v n = u n := by
  let E := recOf p
  let init := fun i : Fin E.order => u i
  let v := E.mkSol init
  have hs : E.IsSolution v := E.is_sol_mkSol init
  refine ⟨v, (solution_iff hp v).mpr hs, ?_⟩
  intro n; induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    by_cases h : n < E.order
    · exact E.mkSol_eq_init init ⟨n,h⟩
    · let t := n-E.order
      have ht : t+E.order=n := by dsimp [t]; omega
      have htu := (op_iff p hp u t).mp (hfit t (ht ▸ hn))
      have he := hs t
      rw [ht] at he htu; rw [he, htu]
      apply Finset.sum_congr rfl
      intro i _; rw [ih (t+i) (by have := i.isLt; omega) (by have := i.isLt; omega)]

/-- Sharp bookkeeping for this proof: the last required dyadic index is `4d-2`.
The result applies to rational recurrences by clearing their finitely many denominators. -/
theorem finite_recurrence_gap {u : Seq} {N : ℕ} {p : ℤ[X]} (hp : p ≠ 0)
    (hfit : Fits p u N) (hd : ∀ n, 2*n ≤ N → 4*u (2*n) = u n)
    (hnz : ∃ n ≤ N, u n ≠ 0) : N+2 < 4*p.natDegree := by
  by_contra hlarge
  obtain ⟨v,hk,ha⟩ := extend_fits hp hfit
  have hg := section_globalizes hp hk (by
    intro n hn; rw [ha (2*n) (by omega), ha n (by omega)]; exact hd n (by omega))
  have hv := recurrent_dyadic_zero ⟨p,hp,hk⟩ hg
  obtain ⟨n,hn,hne⟩ := hnz
  exact hne (by rw [← ha n hn, hv]; rfl)

end Collatz.ReciprocalRigidity.HeckeRank

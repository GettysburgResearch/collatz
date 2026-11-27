import Mathlib.Topology.Instances.AddCircle.DenseSubgroup
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Push
import Mathlib.Tactic.Ring

/-! A uniform finite phase net using only irrationality and compactness.
No quantitative irrationality estimate is assumed. -/
set_option autoImplicit false
set_option warningAsError true

namespace PhaseNet
open Set

theorem irrational_logs : Irrational (Real.log 3 / Real.log 2) := by
  rintro ⟨r,hr⟩
  have two : 0<Real.log 2 := Real.log_pos (by norm_num)
  have three : 0<Real.log 3 := Real.log_pos (by norm_num)
  have rp : (0:ℝ)<r := by rw [hr]; exact div_pos three two
  have rpq : (0:ℚ)<r := by exact_mod_cast rp
  have np : 0<r.num := Rat.num_pos.mpr rpq
  have dp : (0:ℝ)<r.den := by exact_mod_cast r.pos
  have ncast : (r.num.toNat:ℝ)=(r.num:ℝ) := by
    exact_mod_cast (Int.toNat_of_nonneg np.le)
  have eq : (r.num.toNat:ℝ)*Real.log 2=(r.den:ℝ)*Real.log 3 := by
    rw [Rat.cast_def] at hr
    have cross := (div_eq_div_iff (ne_of_gt dp) (ne_of_gt two)).mp hr
    rw [ncast]
    nlinarith only [cross]
  have logs : Real.log ((2:ℝ)^r.num.toNat)=Real.log ((3:ℝ)^r.den) := by
    simpa only [Real.log_pow] using eq
  have real_eq : (2:ℝ)^r.num.toNat=(3:ℝ)^r.den :=
    Real.log_injOn_pos (show 0<(2:ℝ)^r.num.toNat by positivity)
      (show 0<(3:ℝ)^r.den by positivity) logs
  have nat_eq : (2:ℕ)^r.num.toNat=(3:ℕ)^r.den := by exact_mod_cast real_eq
  have npos : 0<r.num.toNat := by omega
  have even : (2:ℕ)^r.num.toNat%2=0 := by
    obtain ⟨k,hk⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : r.num.toNat≠0)
    rw [hk,pow_succ]
    omega
  have odd : (3:ℕ)^r.den%2=1 := by simp [Nat.pow_mod]
  rw [nat_eq,odd] at even
  omega

/-- A compact fundamental interval gives a finite set of positive ternary
indices. The binary exponent then adjusts to every larger real target. -/
theorem additive_net (a L ε : ℝ) (ha : 0<a) (hL : 0<L)
    (irr : Irrational (a/L)) (hε : 0<ε) :
    ∃ D : ℕ, ∀ u : ℝ, 0≤u → ∃ d m : ℕ, d≤D ∧
      u < (m:ℝ)*L-(d:ℝ)*a ∧ (m:ℝ)*L-(d:ℝ)*a < u+ε := by
  classical
  have dense : Dense (AddSubgroup.closure ({a,L}:Set ℝ) : Set ℝ) :=
    dense_addSubgroupClosure_pair_iff.mpr irr
  let U (i : ℤ×ℤ) : Set ℝ :=
    Ioo ((i.1:ℝ)*L-(i.2:ℝ)*a-ε) ((i.1:ℝ)*L-(i.2:ℝ)*a)
  have cover : Icc (0:ℝ) L ⊆ ⋃ i : ℤ×ℤ, U i := by
    intro v _
    obtain ⟨z,hz,lower,upper⟩ := dense.exists_between (by linarith : v<v+ε)
    obtain ⟨p,q,hpq⟩ := AddSubgroup.mem_closure_pair.mp hz
    refine mem_iUnion.mpr ⟨(q,-p),?_⟩
    simp only [U,mem_Ioo,Int.cast_neg]
    simp only [zsmul_eq_mul] at hpq
    constructor <;> linarith
  obtain ⟨t,ht⟩ := isCompact_Icc.elim_finite_subcover U (fun _ => isOpen_Ioo) cover
  let Q : ℕ := t.sup (fun i => i.2.natAbs)
  refine ⟨2*Q,?_⟩
  intro u hu
  let k : ℤ := ⌊(u+(Q:ℝ)*a)/L⌋
  let v : ℝ := u+(Q:ℝ)*a-(k:ℝ)*L
  have fl : (k:ℝ)≤(u+(Q:ℝ)*a)/L := Int.floor_le _
  have fu : (u+(Q:ℝ)*a)/L<(k:ℝ)+1 := Int.lt_floor_add_one _
  have vl : 0≤v := by
    have h := (le_div_iff₀ hL).mp fl
    dsimp [v]
    linarith
  have vu : v<L := by
    have h := (div_lt_iff₀ hL).mp fu
    dsimp [v]
    nlinarith
  obtain ⟨i,hi,hvi⟩ := mem_iUnion₂.mp (ht ⟨vl,vu.le⟩)
  have absbound : i.2.natAbs≤Q := Finset.le_sup (f := fun j : ℤ×ℤ => j.2.natAbs) hi
  have right : i.2≤(Q:ℤ) := Int.le_natAbs.trans (by exact_mod_cast absbound)
  have lower_index : 0 ≤ i.2+(Q:ℤ) := by
    have h : -i.2≤(i.2.natAbs:ℤ) := by simpa using (Int.le_natAbs (a := -i.2))
    omega
  let d : ℤ := i.2+Q
  let m : ℤ := i.1+k
  have dn : 0≤d := by dsimp [d]; omega
  have db : d≤2*Q := by dsimp [d]; omega
  have lo : u<(m:ℝ)*L-(d:ℝ)*a := by
    have h := hvi.2
    dsimp [U,v,m,d] at h ⊢
    push_cast
    linarith
  have up : (m:ℝ)*L-(d:ℝ)*a<u+ε := by
    have h := hvi.1
    dsimp [U,v,m,d] at h ⊢
    push_cast
    linarith
  have mp : (0:ℝ)<m := by
    have da : (0:ℝ)≤(d:ℝ)*a := mul_nonneg (by exact_mod_cast dn) ha.le
    have ml : (0:ℝ)<(m:ℝ)*L := by linarith
    exact (mul_pos_iff_of_pos_right hL).mp ml
  have mn : 0≤m := by exact_mod_cast mp.le
  have dc : (d.toNat:ℝ)=(d:ℝ) := by exact_mod_cast (Int.toNat_of_nonneg dn)
  have mc : (m.toNat:ℝ)=(m:ℝ) := by exact_mod_cast (Int.toNat_of_nonneg mn)
  refine ⟨d.toNat,m.toNat,by omega,?_,?_⟩
  · simpa only [dc,mc] using lo
  · simpa only [dc,mc] using up

theorem pow_ratio_net (ε : ℝ) (positive : 0<ε) :
    ∃ D : ℕ, ∀ u : ℝ, 1≤u → ∃ d m : ℕ, d≤D ∧
      u < (2:ℝ)^m/3^d ∧ (2:ℝ)^m/3^d < (1+ε)*u := by
  have epos : 0<Real.log (1+ε) := Real.log_pos (by linarith)
  obtain ⟨D,net⟩ := additive_net (Real.log 3) (Real.log 2) (Real.log (1+ε))
    (Real.log_pos (by norm_num)) (Real.log_pos (by norm_num)) irrational_logs epos
  refine ⟨D,?_⟩
  intro u hu
  have up : 0<u := by linarith
  obtain ⟨d,m,hd,lo,hi⟩ := net (Real.log u) (Real.log_nonneg hu)
  have id : Real.log ((2:ℝ)^m/3^d)=(m:ℝ)*Real.log 2-(d:ℝ)*Real.log 3 := by
    rw [Real.log_div (by positivity) (by positivity),Real.log_pow,Real.log_pow]
  refine ⟨d,m,hd,?_,?_⟩
  · exact (Real.log_lt_log_iff up (by positivity)).mp (by simpa only [id] using lo)
  · have target : Real.log ((1+ε)*u)=Real.log u+Real.log (1+ε) := by
      rw [Real.log_mul (by positivity) (ne_of_gt up)]
      ring
    exact (Real.log_lt_log_iff (by positivity) (by positivity)).mp
      (by simpa only [id,target] using hi)

#print axioms irrational_logs
#print axioms additive_net
#print axioms pow_ratio_net
end PhaseNet

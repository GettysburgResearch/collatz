module
public import Mathlib.Basic.Real.Basic
public import Mathlib.Data.Fintype.Lattice
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Ring

@[expose] public section

namespace CollatzCriticalTrace

/-- The finite correction product along a supplied positive ordinary odd path. -/
noncomputable def correction (x : ℕ → ℝ) : ℕ → ℝ
  | 0 => 1
  | k+1 => correction x k * (1 + 1/(3*x k))

theorem correction_pos {x : ℕ → ℝ} (hx : ∀ k, 0 < x k) (k : ℕ) :
    0 < correction x k := by
  induction k with
  | zero => norm_num [correction]
  | succ k ih =>
    rw [correction]
    have hk := hx k
    exact mul_pos ih (by positivity)

/-- An actual edge and one critical inverse-weight inequality imply the
corrected trace inequality. No averaging or random parity law is assumed. -/
theorem edge_trace {x y a b mult : ℝ} (hx : 0 < x) (hy : 0 < y)
    (he : y = mult * (x + 1/3)) (hh : mult*a ≤ b) :
    a/x ≤ (b/y) * (1 + 1/(3*x)) := by
  have hx0 : x ≠ 0 := ne_of_gt hx
  have hy0 : y ≠ 0 := ne_of_gt hy
  apply (div_le_iff₀ hx).2
  have heq : (b/y) * (1 + 1/(3*x)) * x = b*(x+1/3)/y := by
    field_simp
  rw [heq]
  apply (le_div_iff₀ hy).2
  have hpos : 0 ≤ x+1/3 := by positivity
  have hm := mul_le_mul_of_nonneg_right hh hpos
  rw [he]
  nlinarith

/-- Every clock retains the same initial trace atom. -/
theorem propagated_trace {x v mult : ℕ → ℝ}
    (hx : ∀ k, 0 < x k)
    (he : ∀ k, x (k+1) = mult k * (x k + 1/3))
    (hv : ∀ k, mult k * v k ≤ v (k+1)) (k : ℕ) :
    v 0 / x 0 ≤ (v k / x k) * correction x k := by
  induction k with
  | zero => simp [correction]
  | succ k ih =>
    have hs := edge_trace (hx k) (hx (k+1)) (he k) (hv k)
    have hm := mul_le_mul_of_nonneg_right hs (le_of_lt (correction_pos hx k))
    calc
      v 0 / x 0 ≤ v k / x k * correction x k := ih
      _ ≤ v (k+1) / x (k+1) * correction x (k+1) := by
        simpa only [correction, mul_assoc, mul_left_comm, mul_comm] using hm

/-- A bounded correction product forces a strictly positive lower trace
ratio along the entire supplied path. -/
theorem trace_ratio_lower {x v mult : ℕ → ℝ} {K : ℝ}
    (hx : ∀ k, 0 < x k) (hv0 : 0 < v 0)
    (he : ∀ k, x (k+1) = mult k * (x k + 1/3))
    (hv : ∀ k, mult k * v k ≤ v (k+1))
    (hK : ∀ k, correction x k ≤ K) (k : ℕ) :
    v 0 / (x 0 * K) ≤ v k / x k := by
  have hK1 : 1 ≤ K := by simpa [correction] using hK 0
  have hK0 : 0 < K := by linarith
  have hp := propagated_trace hx he hv k
  have hvk : 0 ≤ v k / x k := by
    by_contra hn
    have hneg : v k / x k < 0 := lt_of_not_ge hn
    have hm : (v k / x k) * correction x k < 0 :=
      mul_neg_of_neg_of_pos hneg (correction_pos hx k)
    have hstart : 0 < v 0 / x 0 := div_pos hv0 (hx 0)
    linarith
  have hm := mul_le_mul_of_nonneg_left (hK k) hvk
  have hl : v 0 / x 0 ≤ (v k / x k) * K := le_trans hp hm
  have hd := (div_le_iff₀ hK0).2 hl
  simpa [div_div] using hd

/-- This is the exact missing analytic gate: the same trace ratios cannot
approach zero while the ordinary correction product stays bounded. -/
theorem no_arbitrarily_small_trace {x v mult : ℕ → ℝ} {K : ℝ}
    (hx : ∀ k, 0 < x k) (hv0 : 0 < v 0)
    (he : ∀ k, x (k+1) = mult k * (x k + 1/3))
    (hv : ∀ k, mult k * v k ≤ v (k+1))
    (hK : ∀ k, correction x k ≤ K)
    (hsmall : ∀ ε : ℝ, 0 < ε → ∃ k, v k / x k < ε) : False := by
  have hK1 : 1 ≤ K := by simpa [correction] using hK 0
  have hK0 : 0 < K := by linarith
  have heps : 0 < v 0 / (x 0*K) := div_pos hv0 (mul_pos (hx 0) hK0)
  obtain ⟨k, hk⟩ := hsmall _ heps
  exact (not_lt_of_ge (trace_ratio_lower hx hv0 he hv hK k)) hk

/-- Ordinary odd edge arithmetic, with no division-rounding convention. -/
theorem ordinary_edge {x y e : ℕ} (h : 3*x+1 = 2^e*y) :
    (y:ℝ) = (3/(2:ℝ)^e) * ((x:ℝ)+1/3) := by
  have hcast : (3:ℝ)*x+1 = (2:ℝ)^e*y := by exact_mod_cast h
  have hpow : (2:ℝ)^e ≠ 0 := by positivity
  field_simp
  nlinarith

/-- At a minimum of the ratio on a cycle, a retained off-cycle parent
forces a quantitative positive floor. This is the local cycle argument;
the existence and size of the off-cycle contribution remain explicit. -/
theorem cycle_minimum_ratio {x y a b mult κ : ℝ}
    (hx : 0 < x) (hy : 0 < y) (hm : 0 < mult) (hmupper : mult ≤ 3/2)
    (hκ : 0 < κ) (hedge : y = mult * (x+1/3))
    (hside : mult*a + κ ≤ b) (hmin : b/y ≤ a/x) :
    2*κ ≤ b/y := by
  have hmx : (b/y)*x ≤ a := (le_div_iff₀ hx).1 hmin
  have hh := mul_le_mul_of_nonneg_left hmx (le_of_lt hm)
  have he := congrArg (fun z : ℝ => z*(b/y)) hedge
  have hby : y*(b/y) = b := by field_simp
  have hbalance : κ ≤ (mult/3)*(b/y) := by nlinarith
  have hratio : 0 ≤ b/y := by
    by_contra hn
    have hg : b/y < 0 := lt_of_not_ge hn
    have hneg : (mult/3)*(b/y) < 0 := mul_neg_of_pos_of_neg (by positivity) hg
    linarith
  have hupper := mul_le_mul_of_nonneg_right hmupper hratio
  nlinarith

/-- The minimum argument covers every vertex of any finite closed
predecessor family with a positive retained side contribution. -/
theorem finite_closed_trace_floor {ι : Type*} [Finite ι] [Nonempty ι]
    (parent : ι → ι) {x v mult : ι → ℝ} {κ : ℝ}
    (hx : ∀ i, 0 < x i) (hm : ∀ i, 0 < mult i)
    (hmupper : ∀ i, mult i ≤ 3/2) (hκ : 0 < κ)
    (hedge : ∀ i, x i = mult i * (x (parent i)+1/3))
    (hside : ∀ i, mult i*v (parent i)+κ ≤ v i) :
    ∀ i, 2*κ ≤ v i/x i := by
  obtain ⟨i₀, hi₀⟩ := Finite.exists_min (fun i => v i/x i)
  have hfloor := cycle_minimum_ratio (hx (parent i₀)) (hx i₀)
    (hm i₀) (hmupper i₀) hκ (hedge i₀) (hside i₀) (hi₀ (parent i₀))
  intro i
  exact le_trans hfloor (hi₀ i)

/-- An explicit sublinear cutoff bounds every member of every such finite
family; no period bound is used. -/
theorem finite_closed_below_cutoff {ι : Type*} [Finite ι] [Nonempty ι]
    (parent : ι → ι) {q : ι → ℕ} {h : ℕ → ℝ} {mult : ι → ℝ}
    {κ : ℝ} {M : ℕ}
    (hq : ∀ i, 0 < q i) (hm : ∀ i, 0 < mult i)
    (hmupper : ∀ i, mult i ≤ 3/2) (hκ : 0 < κ)
    (hedge : ∀ i, (q i:ℝ) = mult i * ((q (parent i):ℝ)+1/3))
    (hside : ∀ i, mult i*h (q (parent i))+κ ≤ h (q i))
    (htail : ∀ n : ℕ, M ≤ n → 0 < n → h n/(n:ℝ) < 2*κ) :
    ∀ i, q i < M := by
  have hx : ∀ i, (0:ℝ) < q i := by intro i; exact_mod_cast hq i
  have hfloor := finite_closed_trace_floor parent (v := fun i => h (q i)) hx hm hmupper hκ hedge hside
  intro i
  by_contra hn
  have hMi : M ≤ q i := by omega
  exact (not_lt_of_ge (hfloor i)) (htail (q i) hMi (hq i))

/-- A pointwise sublinear excessive trace excludes an unbounded *ordinary*
path once its correction products are bounded. The sublinear estimate is
an explicit hypothesis, not an imported or asserted theorem. -/
theorem bounded_of_sublinear_trace {q e : ℕ → ℕ} {h : ℕ → ℝ} {K : ℝ}
    (hq : ∀ k, 0 < q k) (hh0 : 0 < h (q 0))
    (hedge : ∀ k, 3*q k+1 = 2^(e k)*q (k+1))
    (hexcess : ∀ k, (3/(2:ℝ)^(e k))*h (q k) ≤ h (q (k+1)))
    (hK : ∀ k, correction (fun j => (q j : ℝ)) k ≤ K)
    (hsub : ∀ ε : ℝ, 0 < ε → ∃ M : ℕ,
      ∀ n : ℕ, M ≤ n → 0 < n → h n / (n:ℝ) < ε) :
    ∃ M : ℕ, ∀ k : ℕ, q k < M := by
  classical
  by_contra hn
  have hu : ∀ M : ℕ, ∃ k : ℕ, M ≤ q k := by
    intro M
    by_contra hk
    have hm : ∀ k : ℕ, q k < M := by
      intro k
      have : ¬ M ≤ q k := fun hle => hk ⟨k, hle⟩
      omega
    exact hn ⟨M, hm⟩
  have hqr : ∀ k, (0:ℝ) < q k := by
    intro k
    exact_mod_cast hq k
  apply no_arbitrarily_small_trace (x := fun j => (q j:ℝ))
    (v := fun j => h (q j)) (mult := fun j => 3/(2:ℝ)^(e j))
    hqr hh0 (fun k => ordinary_edge (hedge k)) hexcess hK
  intro ε hε
  obtain ⟨M, hM⟩ := hsub ε hε
  obtain ⟨k, hk⟩ := hu M
  exact ⟨k, hM (q k) hk (hq k)⟩

end CollatzCriticalTrace

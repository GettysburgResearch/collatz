module

public import PassageBoundary
import all PassageBoundary
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageBoundary

open Filter Topology
set_option autoImplicit false
noncomputable section

/-- For a zero-one label this is the fraction of binary continuations
on which the first h successive prefixes all carry label one. -/
def survival (f : ℕ → ℝ) (n : ℕ) : ℕ → ℝ
  | 0 => 1
  | j+1 => f n*(survival f (2*n) j+survival f (2*n+1) j)/2

private theorem cell_children (f : ℕ → ℝ) (n j : ℕ) :
    Cell f n (j+1)=(Cell f (2*n) j+Cell f (2*n+1) j)/2 := by
  unfold Cell
  rw [show 2^(j+1)*(n+1)=2^j*(2*n+1+1) by rw [pow_succ]; ring,
    show 2^(j+1)*n=2^j*(2*n) by rw [pow_succ]; ring,pow_succ (2:ℝ)]
  field_simp
  ring

/-- At any prescribed ordinary prefix, a label of density below one
has zero limiting probability of persisting along every new binary digit.
The result also holds for labels in the real unit interval. -/
theorem survival_vanishes {f : ℕ → ℝ} {d : ℝ} (density : NaturalDensity f d)
    (nonneg : ∀ n, 0≤f n) (bounded : ∀ n, f n≤1) (proper : d<1) (n : ℕ) :
    Tendsto (survival f n) atTop (𝓝 0) := by
  have positive (a j : ℕ) : 0≤survival f a j := by
    induction j generalizing a with
    | zero => simp [survival]
    | succ j ih =>
      exact div_nonneg (mul_nonneg (nonneg a) (add_nonneg (ih _) (ih _))) (by norm_num)
  have down (a j : ℕ) : survival f a (j+1)≤survival f a j := by
    induction j generalizing a with
    | zero => simp only [survival]; linarith [bounded a]
    | succ j ih =>
      exact div_le_div_of_nonneg_right
        (mul_le_mul_of_nonneg_left (add_le_add (ih _) (ih _)) (nonneg a)) (by norm_num)
  have last (a j : ℕ) : survival f a (j+1)≤Cell f a j := by
    induction j generalizing a with
    | zero => simp [survival,Cell,pre_succ]; linarith
    | succ j ih =>
      rw [cell_children]
      change f a*(survival f (2*a) (j+1)+survival f (2*a+1) (j+1))/2≤_
      apply div_le_div_of_nonneg_right _ (by norm_num)
      have sumpos := add_nonneg (positive (2*a) (j+1)) (positive (2*a+1) (j+1))
      exact (mul_le_of_le_one_left sumpos (bounded a)).trans (add_le_add (ih _) (ih _))
  let p := fun a => ⨅ j, survival f a j
  have conv (a : ℕ) : Tendsto (survival f a) atTop (𝓝 (p a)) :=
    tendsto_atTop_ciInf (antitone_nat_of_succ_le (down a))
      ⟨0,fun y ⟨j,eq⟩ => eq ▸ positive a j⟩
  have ppos (a : ℕ) : 0≤p a :=
    le_of_tendsto_of_tendsto' tendsto_const_nhds (conv a) (positive a)
  have shift (a : ℕ) : Tendsto (fun j => survival f a (j+1)) atTop (𝓝 (p a)) :=
    (conv a).comp (tendsto_add_atTop_nat 1)
  have cap (a : ℕ) : p a≤d := le_of_tendsto_of_tendsto' (shift a) (cell_limit density a) (last a)
  have harmonic (a : ℕ) : p a=f a*(p (2*a)+p (2*a+1))/2 :=
    tendsto_nhds_unique (shift a) (((conv (2*a)).add (conv (2*a+1))).const_mul (f a) |>.div_const 2)
  have amplify (a j : ℕ) : p a≤d*survival f a j := by
    induction j generalizing a with
    | zero => simpa [survival] using cap a
    | succ j ih =>
      rw [harmonic a]
      calc
        _ ≤ f a*(d*survival f (2*a) j+d*survival f (2*a+1) j)/2 :=
          div_le_div_of_nonneg_right
            (mul_le_mul_of_nonneg_left (add_le_add (ih _) (ih _)) (nonneg a)) (by norm_num)
        _ = _ := by rw [survival]; ring
  have contracted : p n≤d*p n := le_of_tendsto_of_tendsto' tendsto_const_nhds
    ((conv n).const_mul d) (amplify n)
  have zero : p n=0 := by
    by_contra ne
    have pn := lt_of_le_of_ne (ppos n) (Ne.symm ne)
    nlinarith [mul_pos (sub_pos.mpr proper) pn]
  exact zero ▸ conv n

private theorem complement_density {f : ℕ → ℝ} {d : ℝ} (density : NaturalDensity f d) :
    NaturalDensity (fun n => 1-f n) (1-d) := by
  have total (n : ℕ) : partialSum (fun i => 1-f i) n=(n:ℝ)-partialSum f n := by
    simp [partialSum,Finset.sum_sub_distrib]
  apply (tendsto_const_nhds.sub density).congr'
  filter_upwards [eventually_gt_atTop (0:ℕ)] with n hn
  rw [total]
  have nz : (n:ℝ)≠0 := by exact_mod_cast (Nat.ne_of_gt hn)
  field_simp

/-- If Collatz fails and the stated ordinary density inputs hold, at every
fixed prefix the fractions of continuations retaining either fate both
tend to zero. Thus almost every infinite binary continuation visits both
fates infinitely often. -/
theorem both_fates {d : ℝ} (density : NaturalDensity basin d) (pos : 0<d) (lt : d<1)
    (n : ℕ) :
    Tendsto (survival basin n) atTop (𝓝 0) ∧
      Tendsto (survival (fun i => 1-basin i) n) atTop (𝓝 0) := by
  have lo (i : ℕ) : 0≤basin i := by rcases basin_bits i with h | h <;> norm_num [h]
  have hi (i : ℕ) : basin i≤1 := by rcases basin_bits i with h | h <;> norm_num [h]
  exact ⟨survival_vanishes density lo hi lt n,
    survival_vanishes (complement_density density) (fun i => sub_nonneg.mpr (hi i))
      (fun i => by linarith [lo i]) (by linarith) n⟩

/-- One fixed prefix with a positive limiting fraction of entirely
convergent continuations suffices for the global statement. -/
theorem universal_iff_surviving_prefix (mixed : ¬Universal →
    ∃ d, NaturalDensity basin d ∧ 0<d ∧ d<1) :
    Universal ↔ ∃ n, 0<n ∧ ¬Tendsto (survival basin n) atTop (𝓝 0) := by
  constructor
  · intro h
    have blue (n : ℕ) : basin n=1 := by
      classical
      have yes : n=0 ∨ ReachesOne n := by
        by_cases z : n=0
        · exact Or.inl z
        · exact Or.inr (h n (by omega))
      simp [basin,yes]
    have all (a j : ℕ) : survival basin a j=1 := by
      induction j generalizing a with
      | zero => rfl
      | succ j ih => rw [survival,blue,ih,ih]; norm_num
    refine ⟨1,by decide,?_⟩
    intro zero
    have one : Tendsto (survival basin 1) atTop (𝓝 1) :=
      tendsto_const_nhds.congr (fun j => (all 1 j).symm)
    exact one_ne_zero (tendsto_nhds_unique one zero)
  · rintro ⟨n,_,survives⟩
    by_contra failure
    obtain ⟨d,den,pos,lt⟩ := mixed failure
    exact survives (both_fates den pos lt n).1

#print axioms survival_vanishes
#print axioms both_fates
#print axioms universal_iff_surviving_prefix
end
end Collatz.Itinerary.PassageBoundary

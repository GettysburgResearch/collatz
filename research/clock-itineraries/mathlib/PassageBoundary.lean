module

public import TernaryItinerary
import all TernaryItinerary
public import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageBoundary

open Filter Finset Topology
set_option autoImplicit false
noncomputable section

def partialSum (f : ℕ → ℝ) (n : ℕ) := ∑ i ∈ range n, f i

def Cell (f : ℕ → ℝ) (n j : ℕ) : ℝ :=
  (partialSum f (2^j*(n+1))-partialSum f (2^j*n))/(2:ℝ)^j

def fault (f : ℕ → ℝ) (n : ℕ) := |f (2*n+1)-f (2*n)|

/-- The mass of differing even-start edges in one octave, normalized by
twice the number of parents. -/
def variation (f : ℕ → ℝ) (k : ℕ) : ℝ :=
  (partialSum (fault f) (2^(k+1))-partialSum (fault f) (2^k))/(2:ℝ)^(k+1)

def NaturalDensity (f : ℕ → ℝ) (d : ℝ) :=
  Tendsto (fun n : ℕ => partialSum f n/(n:ℝ)) atTop (𝓝 d)

private theorem pre_succ (f : ℕ → ℝ) (n : ℕ) :
    partialSum f (n+1)=partialSum f n+f n := sum_range_succ f n

private theorem telescopes (F : ℕ → ℝ) (n m : ℕ) :
    ∑ r ∈ range m, (F (n+r+1)-F (n+r))=F (n+m)-F n := by
  induction m with
  | zero => simp
  | succ m ih => rw [sum_range_succ,ih]; simp only [Nat.add_succ]; ring

private def defect (f : ℕ → ℝ) (n : ℕ) := partialSum f (2*n)-2*partialSum f n

private theorem defect_step (f : ℕ → ℝ) (double : ∀ n, f (2*n)=f n) (n : ℕ) :
    defect f (n+1)-defect f n=f (2*n+1)-f (2*n) := by
  simp only [defect,show 2*(n+1)=2*n+1+1 by omega,pre_succ,double]
  ring

private theorem defect_bound (f : ℕ → ℝ) (double : ∀ n, f (2*n)=f n) (n m : ℕ) :
    |defect f (n+m)-defect f n|≤partialSum (fault f) (n+m)-partialSum (fault f) n := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [Nat.add_succ,pre_succ]
    have e := defect_step f double (n+m)
    calc
      _ = |(defect f (n+m)-defect f n)+(f (2*(n+m)+1)-f (2*(n+m)))| := by
        congr 1; linarith
      _ ≤ _ := abs_add_le _ _
      _ ≤ _ := by unfold fault at *; linarith

private theorem cell_step (f : ℕ → ℝ) (double : ∀ n, f (2*n)=f n) (n j : ℕ) :
    |Cell f n (j+1)-Cell f n j| ≤
      (partialSum (fault f) (2^j*(n+1))-partialSum (fault f) (2^j*n))/(2:ℝ)^(j+1) := by
  let m := 2^j*n
  let t := 2^j*(n+1)
  have s1 : 2^(j+1)*(n+1)=2*t := by dsimp only [t]; rw [pow_succ]; ring
  have s0 : 2^(j+1)*n=2*m := by dsimp only [m]; rw [pow_succ]; ring
  have lt : m+2^j=t := by dsimp only [t,m]; ring
  have bound := defect_bound f double m (2^j)
  rw [lt] at bound
  have eq : Cell f n (j+1)-Cell f n j=(defect f t-defect f m)/(2:ℝ)^(j+1) := by
    unfold Cell defect
    rw [s1,s0,pow_succ (2:ℝ)]
    change (partialSum f (2*t)-partialSum f (2*m))/((2:ℝ)^j*2)-
      (partialSum f t-partialSum f m)/(2:ℝ)^j=_
    field_simp
    ring
  rw [eq,abs_div,abs_of_pos (by positivity : 0<(2:ℝ)^(j+1))]
  exact div_le_div_of_nonneg_right bound (by positivity)

def deviation (f : ℕ → ℝ) (k j : ℕ) : ℝ :=
  (∑ r ∈ range (2^k), |Cell f (2^k+r) j-f (2^k+r)|)/(2:ℝ)^k

private theorem deviation_step (f : ℕ → ℝ) (double : ∀ n, f (2*n)=f n) (k j : ℕ) :
    deviation f k (j+1)≤deviation f k j+variation f (k+j) := by
  let L := 2^k
  let F := fun n => partialSum (fault f) (2^j*n)
  have point (r : ℕ) :
      |Cell f (L+r) (j+1)-f (L+r)| ≤ |Cell f (L+r) j-f (L+r)|+
        (F (L+r+1)-F (L+r))/(2:ℝ)^(j+1) := by
    have bound := cell_step f double (L+r) j
    calc
      _ ≤ |Cell f (L+r) j-f (L+r)|+|Cell f (L+r) (j+1)-Cell f (L+r) j| := by
        simpa only [sub_add_sub_cancel] using
          abs_add_le (Cell f (L+r) (j+1)-Cell f (L+r) j) (Cell f (L+r) j-f (L+r)) |>.trans_eq (add_comm ..)
      _ ≤ _ := add_le_add_right bound _
  have total := Finset.sum_le_sum (s:=range L) (fun r _ => point r)
  rw [sum_add_distrib,←Finset.sum_div,telescopes] at total
  have hi : 2^j*(L+L)=2^(k+j+1) := by dsimp only [L]; rw [pow_succ,pow_add]; ring
  have lo : 2^j*L=2^(k+j) := by dsimp only [L]; rw [pow_add]; ring
  have denom : (2:ℝ)^(k+j+1)=(2:ℝ)^(j+1)*2^k := by rw [pow_succ,pow_add,pow_succ]; ring
  have eq : ((F (L+L)-F L)/(2:ℝ)^(j+1))/(2:ℝ)^k=variation f (k+j) := by
    dsimp only [F,variation]
    rw [hi,lo,denom,div_div]
  unfold deviation
  convert div_le_div_of_nonneg_right total (by positivity : 0≤(2:ℝ)^k) using 1
  rw [add_div,eq]

/-- Finite comparison between a parent's label and all its descendants,
with the actual adjacent discrepancies charged once at their own scale. -/
theorem multiscale (f : ℕ → ℝ) (double : ∀ n, f (2*n)=f n) (k j : ℕ) :
    deviation f k j≤∑ i ∈ range j, variation f (k+i) := by
  induction j with
  | zero => simp [deviation,Cell,pre_succ]
  | succ j ih =>
    rw [sum_range_succ]
    exact (deviation_step f double k j).trans (add_le_add_left ih _)

private theorem cell_limit {f : ℕ → ℝ} {d : ℝ} (density : NaturalDensity f d) (n : ℕ) :
    Tendsto (Cell f n) atTop (𝓝 d) := by
  have scaled (a : ℕ) : Tendsto (fun j => partialSum f (2^j*a)/(2:ℝ)^j) atTop (𝓝 ((a:ℝ)*d)) := by
    by_cases zero : a=0
    · subst a; simp [partialSum]
    have ap : 0<a := by omega
    have grow : Tendsto (fun j : ℕ => 2^j*a) atTop atTop :=
      tendsto_atTop_mono (fun j => Nat.le_mul_of_pos_right (2^j) ap)
        (tendsto_pow_atTop_atTop_of_one_lt (by decide : 1<(2:ℕ)))
    have base := (density.comp grow).const_mul (a:ℝ)
    convert base using 1
    funext j
    simp only [Function.comp_apply,Nat.cast_mul,Nat.cast_pow,Nat.cast_ofNat]
    field_simp
  have delta := (scaled (n+1)).sub (scaled n)
  convert delta using 1
  · funext j; unfold Cell; ring
  · push_cast; ring_nf

/-- With a nontrivial natural density, the normalized adjacent discrepancies
carry a fixed amount of mass beyond every starting octave. -/
theorem recurrent_mass {f : ℕ → ℝ} {d : ℝ} (density : NaturalDensity f d)
    (bits : ∀ n, f n=0 ∨ f n=1) (double : ∀ n, f (2*n)=f n) (pos : 0<d) (lt : d<1) :
    ∀ k, ∃ j, min d (1-d)/2 < ∑ i ∈ range j, variation f (k+i) := by
  intro k
  let L := 2^k
  let limit := (∑ r ∈ range L, |d-f (L+r)|)/(2:ℝ)^k
  have conv : Tendsto (deviation f k) atTop (𝓝 limit) := by
    apply Filter.Tendsto.div_const
    apply tendsto_finsetSum
    intro r _
    exact ((cell_limit density (L+r)).sub tendsto_const_nhds).abs
  have point (r : ℕ) : min d (1-d) ≤ |d-f (L+r)| := by
    rcases bits (L+r) with h | h
    · rw [h,sub_zero,abs_of_pos pos]; exact min_le_left ..
    · rw [h,abs_of_neg (by linarith : d-1<0)]; linarith [min_le_right d (1-d)]
  have total := Finset.sum_le_sum (s:=range L) (fun r _ => point r)
  simp only [sum_const,card_range,nsmul_eq_mul] at total
  have floor : min d (1-d)≤limit := by
    apply (le_div_iff₀ (by positivity : 0<(2:ℝ)^k)).mpr
    simpa only [L,Nat.cast_pow,Nat.cast_ofNat,mul_comm] using total
  have pp : 0<min d (1-d) := lt_min pos (by linarith)
  have late := conv.eventually_const_lt (show min d (1-d)/2<limit by linarith)
  obtain ⟨j,hj⟩ := late.exists
  exact ⟨j,lt_of_lt_of_le hj (multiscale f double k j)⟩

def harmonicFault (f : ℕ → ℝ) (n : ℕ) : ℝ := fault f n/(n:ℝ)

private theorem octave_charge (f : ℕ → ℝ) (k : ℕ) :
    variation f k≤partialSum (harmonicFault f) (2^(k+1))-partialSum (harmonicFault f) (2^k) := by
  let L := 2^k
  have shift : 2^(k+1)=L+L := by dsimp only [L]; rw [pow_succ]; omega
  have slab (g : ℕ → ℝ) :
      partialSum g (2^(k+1))-partialSum g L=∑ r ∈ range L, g (L+r) := by
    rw [shift,partialSum,partialSum,sum_range_add]; ring
  change (partialSum (fault f) (2^(k+1))-partialSum (fault f) L)/(2:ℝ)^(k+1)≤_
  rw [slab,slab,Finset.sum_div]
  apply Finset.sum_le_sum
  intro r hr
  have positive : 0<L+r := Nat.add_pos_left (Nat.two_pow_pos _) _
  have large : L+r≤2^(k+1) := by rw [shift]; have := mem_range.mp hr; omega
  apply div_le_div_of_nonneg_left (abs_nonneg _) (by exact_mod_cast positive)
  exact_mod_cast large

private theorem charge_interval (f : ℕ → ℝ) (k j : ℕ) :
    ∑ i ∈ range j, variation f (k+i) ≤
      partialSum (harmonicFault f) (2^(k+j))-partialSum (harmonicFault f) (2^k) := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [sum_range_succ]
    have level := octave_charge f (k+j)
    simpa only [Nat.add_succ] using (add_le_add ih level).trans_eq (by ring)

/-- A binary label with natural density strictly between zero and one,
invariant under doubling, has infinite reciprocal mass of differing
adjacent edges of the specific form (2n, 2n+1). -/
theorem harmonic_divergence {f : ℕ → ℝ} {d : ℝ} (density : NaturalDensity f d)
    (bits : ∀ n, f n=0 ∨ f n=1) (double : ∀ n, f (2*n)=f n) (pos : 0<d) (lt : d<1) :
    ¬Summable (harmonicFault f) := by
  intro summable
  let ε := min d (1-d)/2
  have ep : 0<ε := by dsimp only [ε]; exact div_pos (lt_min pos (sub_pos.mpr lt)) (by norm_num)
  have cauchy := Metric.cauchySeq_iff.mp summable.hasSum.tendsto_sum_nat.cauchySeq
  obtain ⟨K,small⟩ := cauchy ε ep
  obtain ⟨j,mass⟩ := recurrent_mass density bits double pos lt K
  have m1 : K≤2^K := (Nat.lt_two_pow_self (n:=K)).le
  have m2 : K≤2^(K+j) := m1.trans (Nat.pow_le_pow_right (by decide) (by omega))
  have near := small (2^(K+j)) m2 (2^K) m1
  rw [Real.dist_eq] at near
  have upper := (le_abs_self _).trans_lt near
  have bad := mass.trans_le (charge_interval f K j)
  exact (lt_asymm bad upper)

/-- Giving zero the same color as one avoids a convention at the origin.
All measured octaves start at a positive integer. -/
def basin (n : ℕ) : ℝ := by
  classical
  exact if n=0 ∨ ReachesOne n then 1 else 0

private theorem basin_bits (n : ℕ) : basin n=0 ∨ basin n=1 := by
  classical
  unfold basin
  split <;> simp

private theorem basin_double (n : ℕ) : basin (2*n)=basin n := by
  classical
  have eq : ReachesOne (2*n) ↔ ReachesOne n := by
    constructor
    · rintro ⟨j,hit⟩
      cases j with
      | zero => change 2*n=1 at hit; omega
      | succ j => exact ⟨j,by simpa [run,step] using hit⟩
    · rintro ⟨j,hit⟩
      exact ⟨j+1,by simpa [run,step] using hit⟩
  simp [basin,eq]

/-- The external density inputs are visible in the hypothesis. The
remaining statement concerns a series on ordinary positive integers. -/
theorem universal_iff_harmonic (mixed : ¬Universal →
    ∃ d, NaturalDensity basin d ∧ 0<d ∧ d<1) :
    Universal ↔ Summable (harmonicFault basin) := by
  constructor
  · intro h
    have all (n : ℕ) : basin n=1 := by
      classical
      have yes : n=0 ∨ ReachesOne n := by
        by_cases z : n=0
        · exact Or.inl z
        · exact Or.inr (h n (by omega))
      simp [basin,yes]
    have zero : harmonicFault basin=fun _ => 0 := by
      funext n; simp [harmonicFault,fault,all]
    rw [zero]
    exact summable_zero
  · intro finite
    by_contra failure
    obtain ⟨d,den,pos,lt⟩ := mixed failure
    exact harmonic_divergence den basin_bits basin_double pos lt finite

#print axioms multiscale
#print axioms recurrent_mass
#print axioms harmonic_divergence
#print axioms universal_iff_harmonic
end
end Collatz.Itinerary.PassageBoundary

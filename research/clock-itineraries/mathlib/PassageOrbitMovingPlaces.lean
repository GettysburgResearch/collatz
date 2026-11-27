module
public import PassageOrbitOutsideRank
public import Mathlib.Analysis.Complex.ExponentialBounds
public section

namespace Collatz.Itinerary.PassageOrbit

/-- Remove every prime at most B. -/
def roughAbove (B n : ℕ) : ℕ := outside (List.range (B+1)) n

/-- The finite summation used with the published p-adic valuation estimate.
A is log(2t), L is log y and y is the prime cutoff. -/
theorem valuation_sum_budget {ι : Type*} (s : Finset ι) (v : ι → ℝ)
    {A L y t : ℝ} (lp : 0<L) (ap : 0≤A) (yp : 0≤y) (comp : A≤3*L)
    (count : (s.card:ℝ)≤2*y/L) (radius : y^2≤t/100000000)
    (each : ∀i∈s, v i≤2400*A^2*(y/L)) :
    ∑i∈s, v i≤43200*t/100000000 := by
  have square : A^2≤(3*L)^2 := by gcongr
  have term : 2400*A^2*(y/L)≤21600*L*y := by
    calc
      _ ≤ 2400*(3*L)^2*(y/L) := by gcongr
      _ = _ := by field_simp; ring
  calc
    _ ≤ ∑_i∈s, 21600*L*y := Finset.sum_le_sum (fun i hi => (each i hi).trans term)
    _ = (s.card:ℝ)*(21600*L*y) := by simp
    _ ≤ (2*y/L)*(21600*L*y) := by gcongr
    _ = 43200*y^2 := by field_simp; ring
    _ ≤ _ := by linarith

/-- Real and p-adic logarithmic budgets imply the exact integral threshold
needed in the native return test. -/
theorem eighth_power_of_logs {D r t : ℕ} (rp : 0<r)
    (arch : (t:ℝ)*Real.log 2-(t:ℝ)/100≤Real.log D)
    (finite : Real.log D-Real.log r≤43200*(t:ℝ)/100000000) :
    2^(7*t)≤r^8 := by
  have lr : (7*(t:ℝ))*Real.log 2≤8*Real.log r := by
    have ln := Real.log_two_gt_d9
    nlinarith only [arch,finite,mul_nonneg (show 0≤(t:ℝ) by positivity) (sub_nonneg.mpr ln.le)]
  have realBound : (2:ℝ)^(7*t)≤(r:ℝ)^8 := by
    apply (Real.log_le_log_iff (by positivity) (by positivity)).mp
    simpa [Real.log_pow] using lr
  exact_mod_cast realBound

/-- The logarithmic cost of removing the complete small-prime part is the
sum of the corresponding valuations with logarithmic weights. -/
theorem removed_log (B n : ℕ) (np : 0<n) :
    Real.log n-Real.log (roughAbove B n) =
      ∑p∈n.primeFactors.filter (fun p => p≤B), (n.factorization p:ℝ)*Real.log p := by
  let r := roughAbove B n
  let w (m p : ℕ) := (m.factorization p:ℝ)*Real.log p
  have div : r ∣ n := outside_dvd ..
  have incl : r.primeFactors⊆n.primeFactors := Nat.primeFactors_mono div np.ne'
  have rs : Real.log r=∑p∈n.primeFactors, w r p := by
    calc
      _ = ∑p∈r.primeFactors, w r p := Real.log_nat_eq_sum_factorization r
      _ = _ := Finset.sum_subset incl (fun p _ outsideSupport => by
        have hz : r.factorization p=0 := Finsupp.notMem_support_iff.mp
          (by simpa only [Nat.support_factorization] using outsideSupport)
        simp [w,hz])
  have ns : Real.log n=∑p∈n.primeFactors, w n p := Real.log_nat_eq_sum_factorization n
  change Real.log n-Real.log r=_
  rw [ns,rs,←Finset.sum_sub_distrib,Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro p _
  have val := outside_valuation (List.range (B+1)) n p
  change r.factorization p=_ at val
  by_cases small : p≤B
  · have mem : p∈List.range (B+1) := List.mem_range.mpr (by omega)
    simp [w,val,small,mem]
  · have absent : p∉List.range (B+1) := by simpa using small
    simp [w,val,small,absent]

/-- The stated estimates for local valuations, the prime count and the
real linear form suffice for the moving-cutoff determinant estimate. -/
theorem eighth_power_cutoff_from_local_bounds {D t B : ℕ} {A L y : ℝ}
    (dp : 0<D) (lp : 0<L) (ap : 0≤A) (yp : 0≤y) (comp : A≤3*L)
    (count : ((D.primeFactors.filter (fun p => p≤B)).card:ℝ)≤2*y/L)
    (radius : y^2≤(t:ℝ)/100000000)
    (each : ∀p∈D.primeFactors.filter (fun p => p≤B),
      (D.factorization p:ℝ)*Real.log p≤2400*A^2*(y/L))
    (arch : (t:ℝ)*Real.log 2-(t:ℝ)/100≤Real.log D) :
    2^(7*t)≤(roughAbove B D)^8 := by
  apply eighth_power_of_logs (outside_pos _ dp) arch
  rw [show (outside (List.range (B+1)) D)=roughAbove B D from rfl,removed_log B D dp]
  exact valuation_sum_budget _ _ lp ap yp comp count radius each

/-- A moving prime cutoff detects exact return whenever the analytic
determinant lower bound and the finite starting-height bound hold. -/
theorem cutoff_support_iff {a t B : ℕ} (tp : 0<t) (source : (a+1)^4<2^t)
    (bound : 2^(7*t)≤(roughAbove B (determinant a t))^8) :
    (∀p, p.Prime → p ∣ denominator a t → p≤B) ↔ run t a=a := by
  constructor
  · intro supported
    have small : outside (List.range (B+1)) (denominator a t)=1 :=
      (outside_one_iff _ (denominator_pos tp)).mpr (fun p pr dv =>
        List.mem_range.mpr (by have := supported p pr dv; omega))
    by_contra nr
    have heavy := rough_denominator (List.range (B+1)) nr bound
    rw [small,Nat.mul_one] at heavy
    omega
  · intro ret p pr dv
    rw [return_denominator tp ret] at dv
    exact False.elim (pr.not_dvd_one dv)

/-- After stripping primes up to the gap bound, a reduced denominator
and every other nearby raw determinant are relatively prime. -/
theorem rough_coprime_neighbor {a t s J B : ℕ} (tp : 0<t) (different : t≠s)
    (near₁ : t≤s+J) (near₂ : s≤t+J) (cutoff : 3^J≤B) :
    (roughAbove B (denominator a t)).Coprime (determinant a s) := by
  by_contra ncp
  obtain ⟨p,pr,dv,ds⟩ := Nat.Prime.not_coprime_iff_dvd.mp ncp
  have pos := outside_pos (List.range (B+1)) (denominator_pos (a:=a) tp)
  have high : B<p := by
    by_contra! inside
    have mem : p∈List.range (B+1) := List.mem_range.mpr (by omega)
    have val := outside_valuation (List.range (B+1)) (denominator a t) p
    simp [mem] at val
    have nz := pr.factorization_pos_of_dvd pos.ne' dv
    omega
  exact different (large_factor_private near₁ near₂ (cutoff.trans_lt high)
    (dv.trans (outside_dvd (List.range (B+1)) _)) ds)

/-- Every proper arc from every phase of a primitive native cycle is a
nonreturn, including arcs that cross the initially chosen phase. -/
theorem proper_arc_nonreturn {a P r h : ℕ} (ret : run P a=a)
    (primitive : ∀l, 0<l → l<P → run l a≠a) (phase : r<P) (hp : 0<h) (proper : h<P) :
    run h (run r a)≠run r a := by
  intro repeats
  have back : run (P-r) (run r a)=a := by rw [←run_add,Nat.add_sub_of_le phase.le,ret]
  apply primitive h hp proper
  calc
    run h a = run h (run (P-r) (run r a)) := by rw [back]
    _ = run ((P-r)+h) (run r a) := (run_add (P-r) h _).symm
    _ = run (h+(P-r)) (run r a) := by rw [Nat.add_comm (P-r) h]
    _ = run (P-r) (run h (run r a)) := run_add h (P-r) _
    _ = a := by rw [repeats,back]

/-- If each proper arc in a partition has a supported denominator, the
entire period costs at most T native times per arc, provided long arcs
satisfy the prime-to-cutoff determinant lower bound and the source cap. -/
theorem supported_arc_count {a P n M T : ℕ} (ret : run P a=a)
    (primitive : ∀l, 0<l → l<P → run l a≠a)
    (phase len cutoff : Fin n → ℕ) (starts : ∀i, phase i<P) (width : ∀i, run (phase i) a≤M)
    (positive : ∀i, 0<len i) (proper : ∀i, len i<P) (total : ∑i, len i=P)
    (cap : (M+1)^4<2^(T+1)) (support : ∀i p, p.Prime →
      p ∣ denominator (run (phase i) a) (len i) → p≤cutoff i)
    (estimate : ∀i, T<len i → 2^(7*len i)≤
      (roughAbove (cutoff i) (determinant (run (phase i) a) (len i)))^8) : P≤n*T := by
  have short (i : Fin n) : len i≤T := by
    by_contra! long
    have bound : (run (phase i) a+1)^4<2^(len i) :=
      ((Nat.pow_le_pow_left (Nat.succ_le_succ (width i)) _).trans_lt cap).trans_le
        (Nat.pow_le_pow_right (by decide) long)
    have loop := (cutoff_support_iff (positive i) bound (estimate i long)).mp (support i)
    exact proper_arc_nonreturn ret primitive (starts i) (positive i) (proper i) loop
  calc
    P = ∑i, len i := total.symm
    _ ≤ ∑_i : Fin n, T := Finset.sum_le_sum (fun i _ => short i)
    _ = _ := by simp

#print axioms supported_arc_count
#print axioms cutoff_support_iff
#print axioms rough_coprime_neighbor
end Collatz.Itinerary.PassageOrbit

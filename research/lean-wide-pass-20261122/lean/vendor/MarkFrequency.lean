import MarkPhase

/-! Zero temporal density of marked visits, proved by a finite character kernel.
No equidistribution assumption or general Weyl criterion is imported. -/

namespace CollatzShell.ForwardSection.MarkFrequency

open Finset ReturnFourier MarkPhase
open scoped ComplexConjugate

noncomputable def kernel (K : Nat) (u : ℝ) : ℝ :=
  ‖∑ r ∈ range K, character r u‖^2

theorem kernel_nonneg (K : Nat) (u : ℝ) : 0≤kernel K u := sq_nonneg _

theorem frequency_add (r s : Nat) (u : ℝ) :
    character (r+s) u = character r u * character s u := by
  unfold character
  rw [show (((2*Real.pi*((r+s:Nat):ℝ)*u:ℝ):ℂ)*Complex.I) =
    (((2*Real.pi*r*u:ℝ):ℂ)*Complex.I)+(((2*Real.pi*s*u:ℝ):ℂ)*Complex.I) by push_cast; ring]
  exact Complex.exp_add _ _

theorem character_pair_re (r K : Nat) (h : r≤K) (u : ℝ) :
    (character r u * conj (character K u)).re = (character (K-r) u).re := by
  have freq : character K u = character r u * character (K-r) u := by
    rw [← frequency_add,Nat.add_sub_of_le h]
  rw [freq,map_mul,← mul_assoc,Complex.mul_conj',character_norm]
  norm_num

theorem kernel_succ (K : Nat) (u : ℝ) :
    kernel (K+1) u = kernel K u+1+
      2*(∑ r ∈ range K,(character (K-r) u).re) := by
  unfold kernel
  rw [sum_range_succ,Complex.sq_norm,Complex.normSq_add,
    Complex.normSq_eq_norm_sq,Complex.normSq_eq_norm_sq,character_norm]
  have pair : ((∑r∈range K,character r u)*conj (character K u)).re =
      ∑r∈range K,(character (K-r) u).re := by
    rw [sum_mul,Complex.re_sum]
    apply sum_congr rfl
    intro r hr
    exact character_pair_re r K (mem_range.mp hr).le u
  rw [pair]
  norm_num

/-- All finitely many required frequencies have one common ordinary horizon. -/
theorem simultaneous_fourier (n H : Nat) (hn : 0<n)
    (hi : Function.Injective (oddOrbit n)) (δ : ℝ) (hp : 0<δ) :
    ∃ J : Nat, ∀N≥J, ∀k, 0<k → k<H →
      ‖∑j∈range N,character k (height (oddOrbit n j))‖ ≤ δ*N := by
  induction H with
  | zero => exact ⟨0,by intro N _ k _ hk; omega⟩
  | succ H ih =>
    obtain ⟨J,hJ⟩ := ih
    by_cases hz : H=0
    · subst H
      exact ⟨0,by intro N _ k kp kh; omega⟩
    obtain ⟨L,hL⟩ := fourier_averages_vanish n H hn (by omega) hi δ hp
    refine ⟨max J L,?_⟩
    intro N hN k kp kh
    by_cases keq : k=H
    · subst k
      exact (hL N (le_trans (le_max_right _ _) hN)).le
    · exact hJ N (le_trans (le_max_left _ _) hN) k kp (by omega)

/-- A completely finite upper bound for the time sum of the nonnegative kernel. -/
theorem kernel_sum_bound (n K N : Nat) (δ : ℝ) (hd : 0≤δ)
    (freq : ∀k, 0<k → k<K →
      ‖∑j∈range N,character k (height (oddOrbit n j))‖ ≤ δ*N) :
    (∑j∈range N,kernel K (height (oddOrbit n j))) ≤
      (K:ℝ)*N+(K:ℝ)^2*δ*N := by
  induction K with
  | zero => simp [kernel]
  | succ K ih =>
    have prev := ih (fun k hk hK => freq k hk (by omega))
    have cross : (∑r∈range K,∑j∈range N,
        (character (K-r) (height (oddOrbit n j))).re) ≤ (K:ℝ)*(δ*N) := by
      calc _ ≤ ∑r∈range K,δ*N := by
            apply sum_le_sum
            intro r hr
            have rr := mem_range.mp hr
            rw [← Complex.re_sum]
            exact (Complex.re_le_norm _).trans (freq (K-r) (by omega) (by omega))
           _ = _ := by simp
    have sumid : (∑j∈range N,kernel (K+1) (height (oddOrbit n j))) =
        (∑j∈range N,kernel K (height (oddOrbit n j)))+(N:ℝ)+
        2*(∑r∈range K,∑j∈range N,
          (character (K-r) (height (oddOrbit n j))).re) := by
      simp_rw [kernel_succ]
      rw [sum_add_distrib,sum_add_distrib,← mul_sum,sum_comm]
      simp
    rw [sumid]
    have nonneg : 0≤δ*(N:ℝ) := mul_nonneg hd (by positivity)
    push_cast
    nlinarith only [prev,cross,nonneg]

/-- On a small enough leading-phase arc the kernel is uniformly large. -/
theorem kernel_large (K : Nat) (u : ℝ)
    (small : ∀r<K, ‖character r u-1‖≤1/2) :
    (K:ℝ)^2 ≤ 4*kernel K u := by
  let z := ∑r∈range K,character r u
  have near : ‖z-(K:ℂ)‖≤(K:ℝ)/2 := by
    have eq : z-(K:ℂ)=∑r∈range K,(character r u-1) := by simp [z,sum_sub_distrib]
    rw [eq]
    calc _ ≤ ∑r∈range K,‖character r u-1‖ := norm_sum_le _ _
         _ ≤ ∑r∈range K,(1/2:ℝ) := sum_le_sum (fun r hr => small r (mem_range.mp hr))
         _ = _ := by simp [div_eq_mul_inv]
  have triangle := norm_sub_le z (z-(K:ℂ))
  have eq : z-(z-(K:ℂ))=(K:ℂ) := by ring
  rw [eq] at triangle
  have knorm : ‖(K:ℂ)‖=(K:ℝ) := by simp
  rw [knorm] at triangle
  change (K:ℝ)^2 ≤ 4*‖z‖^2
  nlinarith [norm_nonneg z]

theorem kernel_sub_nat (K : Nat) (u : ℝ) (a : Nat) :
    kernel K (u-a)=kernel K u := by simp [kernel,character_sub_nat]

/-- A finite initial segment and a nonnegative kernel control the visit count. -/
theorem kernel_count_bound (y : Nat → ℝ) (P : Nat → Prop) [DecidablePred P]
    (K N J : Nat)
    (tail : ∀j, J≤j → P j → (K:ℝ)^2≤4*kernel K (y j)) :
    (K:ℝ)^2*(((range N).filter P).card:ℝ) ≤
      (K:ℝ)^2*J+4*(∑j∈range N,kernel K (y j)) := by
  let m := (range N).filter P
  let lo := m.filter (fun j => j<J)
  let hi := m.filter (fun j => ¬j<J)
  have low : lo.card≤J := by
    have sub : lo⊆range J := by
      intro j hj
      exact mem_range.mpr (mem_filter.mp hj).2
    simpa using card_le_card sub
  have subhi : hi⊆range N := by
    intro j hj
    exact (mem_filter.mp (mem_filter.mp hj).1).1
  have high : (K:ℝ)^2*(hi.card:ℝ) ≤ 4*(∑j∈range N,kernel K (y j)) := by
    calc _ = ∑j∈hi,(K:ℝ)^2 := by simp [mul_comm]
         _ ≤ ∑j∈hi,4*kernel K (y j) := by
            apply sum_le_sum
            intro j hj
            obtain ⟨jm,jl⟩ := mem_filter.mp hj
            exact tail j (by omega) (mem_filter.mp jm).2
         _ = 4*(∑j∈hi,kernel K (y j)) := by rw [mul_sum]
         _ ≤ _ := mul_le_mul_of_nonneg_left
            (sum_le_sum_of_subset_of_nonneg subhi (by intro j _ _; exact kernel_nonneg _ _)) (by norm_num)
  have split : (m.card:ℝ)=(lo.card:ℝ)+(hi.card:ℝ) := by
    exact_mod_cast (card_filter_add_card_filter_not (s:=m) (fun j => j<J)).symm
  change (K:ℝ)^2*(m.card:ℝ)≤_
  rw [split,mul_add]
  exact add_le_add (mul_le_mul_of_nonneg_left (by exact_mod_cast low) (sq_nonneg _)) high

/-- The finite Fourier theorem and an actual tail majorant imply zero visit density. -/
theorem counts_vanish_of_kernel_tail (n : Nat) (hn : 0<n)
    (hinj : Function.Injective (oddOrbit n)) (P : Nat → Prop) [DecidablePred P]
    (tail : ∀K : Nat, 0<K → ∃J : Nat, ∀j : Nat, J≤j → P j →
      (K:ℝ)^2≤4*kernel K (height (oddOrbit n j))) :
    ∀ ε : ℝ, 0<ε → ∃N₀ : Nat, ∀N≥N₀,
      (((range N).filter P).card:ℝ) < ε*N := by
  intro ε hp
  obtain ⟨K,hK⟩ := exists_nat_gt (16/ε)
  have kr : (0:ℝ)<K := (div_pos (by norm_num) hp).trans hK
  have kp : 0<K := by exact_mod_cast kr
  have kb : 16<(K:ℝ)*ε := (div_lt_iff₀ hp).mp hK
  let A : ℝ := (K:ℝ)^2
  have ap : 0<A := by dsimp [A]; positivity
  let δ : ℝ := ε/16
  have dp : 0<δ := by dsimp [δ]; positivity
  have coeff : 4*(K:ℝ)+4*A*δ < A*ε/2 := by
    have scaled := mul_lt_mul_of_pos_left kb kr
    dsimp [A,δ]
    nlinarith only [scaled]
  obtain ⟨J,hJ⟩ := tail K kp
  obtain ⟨F,hF⟩ := simultaneous_fourier n K hn hinj δ dp
  obtain ⟨L,hL⟩ := exists_nat_gt (2*J/ε)
  have clock : 2*(J:ℝ)<(L:ℝ)*ε := (div_lt_iff₀ hp).mp hL
  refine ⟨max F (L+1),?_⟩
  intro N hN
  have NF : F≤N := le_trans (le_max_left _ _) hN
  have NL : L+1≤N := le_trans (le_max_right _ _) hN
  have nr : (0:ℝ)<N := by exact_mod_cast (show 0<N by omega)
  have lr : (L:ℝ)≤N := by exact_mod_cast (show L≤N by omega)
  have clockN : 2*(J:ℝ)<(N:ℝ)*ε := clock.trans_le (mul_le_mul_of_nonneg_right lr hp.le)
  have head : A*J < (A*ε/2)*N := by
    have scaled := mul_lt_mul_of_pos_left clockN ap
    nlinarith only [scaled]
  have rest := mul_lt_mul_of_pos_right coeff nr
  have count := kernel_count_bound (fun j => height (oddOrbit n j)) P K N J hJ
  have mean := kernel_sum_bound n K N δ dp.le (hF N NF)
  have combined : A*(((range N).filter P).card:ℝ) ≤
      A*J+(4*(K:ℝ)+4*A*δ)*N := by
    calc _ ≤ A*J+4*(∑j∈range N,kernel K (height (oddOrbit n j))) := count
         _ ≤ A*J+4*((K:ℝ)*N+(K:ℝ)^2*δ*N) :=
           add_le_add le_rfl (mul_le_mul_of_nonneg_left mean (by norm_num))
         _ = _ := by dsimp [A]; ring
  have strict : A*(((range N).filter P).card:ℝ) < A*(ε*N) := by
    apply combined.trans_lt
    calc _ < (A*ε/2)*N+(A*ε/2)*N := add_lt_add head rest
         _ = _ := by ring
  exact (mul_lt_mul_iff_right₀ ap).mp strict

/-- The actual section definition supplies the kernel majorant on each
    injective odd orbit. No phase-frequency hypothesis is assumed. -/
theorem marked_kernel_tail (n : Nat) (hinj : Function.Injective (oddOrbit n))
    (K : Nat) (hk : 0<K) :
    ∃J : Nat, ∀j : Nat, J≤j → Marked (oddOrbit n j) →
      (K:ℝ)^2≤4*kernel K (height (oddOrbit n j)) := by
  let δ : ℝ := 1/(8*Real.pi*K)
  have kr : (0:ℝ)<K := by exact_mod_cast hk
  have dp : 0<δ := by dsimp [δ]; positivity
  obtain ⟨J,hJ⟩ := marked_phase_eventually_small hinj dp
  refine ⟨J,?_⟩
  intro j hj hm
  obtain ⟨pl,pu⟩ := hJ j hj hm
  rw [← kernel_sub_nat K (height (oddOrbit n j)) (oddOrbit n j).log2]
  apply kernel_large
  intro r hr
  have rr : (r:ℝ)≤K := by exact_mod_cast hr.le
  calc
    _ ≤ 4*Real.pi*r*|height (oddOrbit n j)-((oddOrbit n j).log2:ℝ)| := character_change _ _
    _ = 4*Real.pi*r*(height (oddOrbit n j)-((oddOrbit n j).log2:ℝ)) := by rw [abs_of_nonneg pl]
    _ ≤ 4*Real.pi*r*δ := mul_le_mul_of_nonneg_left pu (by positivity)
    _ ≤ 4*Real.pi*K*δ := mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_left rr (by positivity)) dp.le
    _ = 1/2 := by dsimp [δ]; field_simp; ring

/-- Number of marked visits in the first `N` odd states of one fixed source. -/
def markedVisits (n N : Nat) : Nat :=
  ((range N).filter (fun j => Marked (oddOrbit n j))).card

/-- Every injective positive ordinary odd orbit visits the marked section
    with temporal density zero. This is the full epsilon definition of
    zero density, proved directly from the actual Fourier estimate. -/
theorem marked_visits_density_zero (n : Nat) (hn : n%2=1)
    (hinj : Function.Injective (oddOrbit n)) :
    ∀ ε : ℝ, 0<ε → ∃N₀ : Nat, ∀N≥N₀,
      (markedVisits n N:ℝ)<ε*N := by
  exact counts_vanish_of_kernel_tail n (by omega) hinj
    (fun j => Marked (oddOrbit n j)) (marked_kernel_tail n hinj)

#print axioms kernel_sum_bound
#print axioms kernel_large
#print axioms kernel_count_bound
#print axioms counts_vanish_of_kernel_tail
#print axioms marked_visits_density_zero

end CollatzShell.ForwardSection.MarkFrequency

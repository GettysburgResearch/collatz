import Mathlib.Analysis.Asymptotics.SpecificAsymptotics
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.Complex.Trigonometric
import ForwardSection

/-!
# Asymptotic rotation and Fourier cancellation

A quantitative finite identity makes the limiting argument independent of any
growth rate or summability of the perturbations. The Collatz specialization
uses odd-clock binary logarithms, exactly as PR 173's forward section theorem.
-/

open Filter Finset
open scoped Topology BigOperators

namespace CollatzShell.PhaseFrequency

/-- The mean of a finite initial segment; its value at zero is harmless. -/
noncomputable def mean (u : Nat → ℂ) (N : Nat) : ℂ :=
  (N : ℂ)⁻¹ * ∑ j ∈ range N, u j

/-- Exact endpoint identity for an approximate complex rotation. -/
theorem rotation_sum_identity (u : Nat → ℂ) (r : ℂ) (N : Nat) :
    (r - 1) * (∑ j ∈ range N, u j) =
      u N - u 0 - ∑ j ∈ range N, (u (j+1) - r*u j) := by
  induction N with
  | zero => simp
  | succ N ih =>
    simp only [sum_range_succ]
    rw [mul_add, ih]
    ring

/-- A finite version of the cancellation estimate, valid on an actual supplied
prefix. The right side retains every increment defect. -/
theorem rotation_sum_norm_bound (u : Nat → ℂ) (r : ℂ) (N : Nat)
    (bound : ∀ j, ‖u j‖ ≤ 1) :
    ‖r-1‖ * ‖∑ j ∈ range N, u j‖ ≤
      2 + ∑ j ∈ range N, ‖u (j+1)-r*u j‖ := by
  calc
    ‖r-1‖ * ‖∑ j ∈ range N, u j‖ = ‖(r-1)*(∑ j ∈ range N, u j)‖ :=
      (norm_mul _ _).symm
    _ = ‖u N-u 0-∑ j ∈ range N, (u (j+1)-r*u j)‖ := by
      rw [rotation_sum_identity]
    _ ≤ ‖u N-u 0‖ + ‖∑ j ∈ range N, (u (j+1)-r*u j)‖ := norm_sub_le _ _
    _ ≤ 2 + ∑ j ∈ range N, ‖u (j+1)-r*u j‖ := by
      exact add_le_add ((norm_sub_le _ _).trans (by linarith [bound N, bound 0]))
        (norm_sum_le _ _)

/-- A bounded sequence satisfying an asymptotic nontrivial rotation has zero
Cesàro mean. No summability assumption is imposed on the increment defects. -/
theorem mean_zero_of_rotation (u : Nat → ℂ) (r : ℂ) (hr : r ≠ 1)
    (bound : ∀ j, ‖u j‖ ≤ 1)
    (defect : Tendsto (fun j => u (j+1) - r*u j) atTop (𝓝 0)) :
    Tendsto (mean u) atTop (𝓝 0) := by
  have ends : Tendsto (fun N : Nat => (N:ℂ)⁻¹ * (u N-u 0)) atTop (𝓝 0) := by
    apply squeeze_zero_norm (a := fun N : Nat => 2/(N:ℝ))
    · intro N
      calc
        ‖(N:ℂ)⁻¹ * (u N-u 0)‖ = (N:ℝ)⁻¹ * ‖u N-u 0‖ := by
          simp [norm_inv]
        _ ≤ (N:ℝ)⁻¹ * 2 := by
          gcongr
          exact (norm_sub_le _ _).trans (by linarith [bound N, bound 0])
        _ = 2/(N:ℝ) := by ring
    · exact tendsto_const_div_atTop_nhds_zero_nat 2
  have avg := defect.cesaro_smul
  have avg' : Tendsto
      (fun N : Nat => (N:ℂ)⁻¹ * ∑ j ∈ range N, (u (j+1)-r*u j))
      atTop (𝓝 0) := by
    simpa only [Complex.real_smul, Complex.ofReal_inv, Complex.ofReal_natCast] using avg
  have prod : Tendsto (fun N => (r-1)*mean u N) atTop (𝓝 0) := by
    have h := ends.sub avg'
    simp only [sub_zero] at h
    convert h using 1
    funext N
    dsimp [mean]
    rw [← mul_sub, ← rotation_sum_identity]
    ring
  have h := (tendsto_const_nhds (x := (r-1)⁻¹)).mul prod
  simpa [← mul_assoc, inv_mul_cancel₀ (sub_ne_zero.mpr hr)] using h

/-- Additive characters of the circle, with integer frequency. -/
noncomputable def character (k : Nat) (x : ℝ) : ℂ :=
  Complex.exp ((2 * Real.pi * k * x : ℝ) * Complex.I)

theorem character_norm (k : Nat) (x : ℝ) : ‖character k x‖ = 1 :=
  Complex.norm_exp_ofReal_mul_I _

theorem character_add (k : Nat) (x y : ℝ) :
    character k (x+y) = character k x * character k y := by
  unfold character
  rw [← Complex.exp_add]
  congr 1
  push_cast
  ring

theorem character_nat (k a : Nat) : character k (a:ℝ) = 1 := by
  unfold character
  convert Complex.exp_nat_mul_two_pi_mul_I (k*a) using 1
  push_cast
  ring

theorem character_neg_nat (k a : Nat) : character k (-(a:ℝ)) = 1 := by
  have h := character_add k (a:ℝ) (-(a:ℝ))
  rw [character_nat] at h
  simpa [character] using h.symm

theorem character_continuous (k : Nat) : Continuous (character k) := by
  unfold character
  fun_prop

open ForwardSection

/-- The rotation supplied by the Collatz multiplier has no positive-frequency
resonance. This uses only the elementary integer-power separation in PR 173. -/
theorem character_alpha_ne_one (k : Nat) (hk : 0<k) : character k alpha ≠ 1 := by
  intro h
  have ap : 0<alpha := by linarith [rotation_bounds.1]
  have pos : 0 ≤ ((2 * Real.pi * k * alpha : ℝ) * Complex.I).im := by
    simpa using (show 0≤2*Real.pi*k*alpha by positivity)
  obtain ⟨a, eq⟩ := Complex.exp_eq_one_iff_of_im_nonneg pos |>.mp h
  have imag := congrArg Complex.im eq
  simp at imag
  have exactPhase : (k:ℝ)*alpha=a := by
    apply mul_left_cancel₀ (by positivity : (2*Real.pi:ℝ)≠0)
    nlinarith [imag]
  have impossible := grid_barrier (N := 4^k) (q := k) (a := a)
    (by positivity) hk (by rw [exactPhase]; simp only [sub_self, abs_zero]; positivity)
  omega

/-- The exact positive logarithmic correction at an odd Collatz step. -/
noncomputable def phaseError (x : Nat) : ℝ :=
  Real.logb 2 (1+1/(3*(x:ℝ)))

private theorem part_positive {x : Nat} (hx : 0<x) : 0<oddPart x :=
  Nat.ordCompl_pos 2 hx.ne'

private theorem odd_orbit_positive {n : Nat} (hn : 0<n) (j : Nat) :
    0<oddOrbit n j := by
  cases j with
  | zero => exact hn
  | succ j => exact part_positive (by omega : 0<3*oddOrbit n j+1)

/-- Exact phase equation; the integer valuation disappears in circle characters. -/
theorem odd_phase_identity (x : Nat) (hx : 0<x) :
    height (oddStep x) = height x+alpha-(twos (3*x+1):ℝ)+phaseError x := by
  have xp : (0:ℝ)<x := by exact_mod_cast hx
  have op : 0<oddStep x := part_positive (by omega : 0<3*x+1)
  have op' : (oddStep x:ℝ)≠0 := by positivity
  have split : 2^(twos (3*x+1))*oddStep x=3*x+1 :=
    Nat.ordProj_mul_ordCompl_eq_self _ _
  have num : (2:ℝ)^(twos (3*x+1))*(oddStep x:ℝ)=
      (3*(x:ℝ))*(1+1/(3*(x:ℝ))) := by
    have h : (2:ℝ)^(twos (3*x+1))*(oddStep x:ℝ)=3*(x:ℝ)+1 := by
      exact_mod_cast split
    rw [h]
    field_simp
  have base := congrArg (Real.logb 2) num
  simp only [Real.logb_mul (by positivity : (2:ℝ)^twos (3*x+1)≠0) op',
    Real.logb_pow, logb_two, mul_one,
    Real.logb_mul (by positivity : 3*(x:ℝ)≠0)
      (by positivity : 1+1/(3*(x:ℝ))≠0),
    Real.logb_mul (by norm_num : (3:ℝ)≠0) xp.ne'] at base
  dsimp only [height, alpha, phaseError]
  linarith

/-- Escape to infinity alone makes the correction vanish; no escape rate is used. -/
theorem phaseError_tendsto_zero (x : Nat → Nat) (escape : Tendsto x atTop atTop) :
    Tendsto (fun j => phaseError (x j)) atTop (𝓝 0) := by
  have small := (tendsto_const_div_atTop_nhds_zero_nat (1/3:ℝ)).comp escape
  have arg : Tendsto (fun j => 1+1/(3*(x j:ℝ))) atTop (𝓝 1) := by
    have h := (tendsto_const_nhds (x := (1:ℝ))).add small
    convert h using 1
    · funext j
      change 1+1/(3*(x j:ℝ)) = 1+(1/3)/(x j:ℝ)
      rw [div_div]
    · norm_num
  have h := (Real.continuousAt_logb (b := 2) (by norm_num : (1:ℝ)≠0)).tendsto.comp arg
  simpa [phaseError, Function.comp_def] using h

/-- The exact accumulated size drift in odd clocks. -/
theorem odd_height_sum (n : Nat) (hn : 0<n) (N : Nat) :
    height (oddOrbit n N) = height n+(N:ℝ)*alpha -
      (∑ j ∈ range N, (twos (3*oddOrbit n j+1):ℝ)) +
      ∑ j ∈ range N, phaseError (oddOrbit n j) := by
  induction N with
  | zero => simp [oddOrbit]
  | succ N ih =>
    change height (oddStep (oddOrbit n N)) = _
    rw [odd_phase_identity _ (odd_orbit_positive hn N), ih]
    simp only [sum_range_succ, Nat.cast_add, Nat.cast_one]
    ring

private theorem odd_height_nonneg (n : Nat) (hn : 0<n) (N : Nat) :
    0≤height (oddOrbit n N) := by
  exact Real.logb_nonneg (by norm_num) (by exact_mod_cast odd_orbit_positive hn N)

/-- Three low bits already give a useful lower bound for the number of halvings. -/
def lowBits (x : Nat) : Nat :=
  1+(if x%4=1 then 1 else 0)+(if x%8=5 then 1 else 0)

theorem lowBits_le_valuation (x : Nat) (hx : x%2=1) :
    lowBits x ≤ twos (3*x+1) := by
  have positive : 3*x+1≠0 := by omega
  have one : 1≤twos (3*x+1) := by
    apply (Nat.prime_two.pow_dvd_iff_le_factorization positive).mp
    norm_num
    apply Nat.dvd_of_mod_eq_zero
    omega
  have two (h : x%4=1) : 2≤twos (3*x+1) := by
    apply (Nat.prime_two.pow_dvd_iff_le_factorization positive).mp
    norm_num
    apply Nat.dvd_of_mod_eq_zero
    omega
  have three (h : x%8=5) : 3≤twos (3*x+1) := by
    apply (Nat.prime_two.pow_dvd_iff_le_factorization positive).mp
    norm_num
    apply Nat.dvd_of_mod_eq_zero
    omega
  unfold lowBits
  split <;> split <;> omega

private theorem odd_orbit_is_odd (n : Nat) (hn : n%2=1) (j : Nat) :
    oddOrbit n j%2=1 := by
  cases j with
  | zero => exact hn
  | succ j =>
    have h : ¬2∣oddPart (3*oddOrbit n j+1) :=
      Nat.not_dvd_ordCompl Nat.prime_two (by omega : 3*oddOrbit n j+1≠0)
    change oddPart (3*oddOrbit n j+1)%2=1
    omega

/-- Finite occupation inequality for one actual positive odd orbit. No escape or
statistical hypothesis is needed for this finite-prefix statement. -/
theorem lowBits_sum_bound (n : Nat) (hn : n%2=1) (N : Nat) :
    (∑ j ∈ range N, (lowBits (oddOrbit n j):ℝ)) ≤
      height n+(N:ℝ)*alpha+∑ j ∈ range N, phaseError (oddOrbit n j) := by
  have np : 0<n := by omega
  have low : (∑ j ∈ range N, (lowBits (oddOrbit n j):ℝ)) ≤
      ∑ j ∈ range N, (twos (3*oddOrbit n j+1):ℝ) := by
    apply sum_le_sum
    intro j _
    exact_mod_cast lowBits_le_valuation _ (odd_orbit_is_odd n hn j)
  have eq := odd_height_sum n np N
  have h := odd_height_nonneg n np N
  linarith

noncomputable def lowBitsMean (n N : Nat) : ℝ :=
  (N:ℝ)⁻¹ * ∑ j ∈ range N, (lowBits (oddOrbit n j):ℝ)

/-- Any divergent odd orbit must retain a low-bit bias: its truncated valuation
mean is eventually no larger than log₂(3) plus any prescribed epsilon. -/
theorem lowBitsMean_eventually_le (n : Nat) (hn : n%2=1)
    (escape : Tendsto (oddOrbit n) atTop atTop) (ε : ℝ) (hε : 0<ε) :
    ∀ᶠ N in atTop, lowBitsMean n N ≤ alpha+ε := by
  have avg := (phaseError_tendsto_zero (oddOrbit n) escape).cesaro
  have small := (tendsto_const_div_atTop_nhds_zero_nat (height n)).add avg
  have tail : ∀ᶠ N : Nat in atTop, height n/(N:ℝ) +
      (N:ℝ)⁻¹ * ∑ j ∈ range N, phaseError (oddOrbit n j) < ε := by
    exact small.eventually (by simpa using gt_mem_nhds hε)
  filter_upwards [tail, eventually_ge_atTop 1] with N hN pos
  have Nr : (0:ℝ)<N := by exact_mod_cast pos
  have bound := mul_le_mul_of_nonneg_left (lowBits_sum_bound n hn N)
    (inv_nonneg.mpr Nr.le)
  have algebra : (N:ℝ)⁻¹ * (height n+(N:ℝ)*alpha+
      ∑ j ∈ range N, phaseError (oddOrbit n j)) =
      alpha+(height n/(N:ℝ)+(N:ℝ)⁻¹*∑ j ∈ range N, phaseError (oddOrbit n j)) := by
    field_simp [Nr.ne']
    ring
  rw [algebra] at bound
  exact bound.trans (by linarith)

/-- Any actual limiting low-bit average above the rotation threshold excludes
escape of that orbit. This does not exclude a nontrivial bounded cycle. -/
theorem no_escape_of_lowBitsMean_limit (n : Nat) (hn : n%2=1) (L : ℝ)
    (hL : alpha<L) (average : Tendsto (lowBitsMean n) atTop (𝓝 L)) :
    ¬Tendsto (oddOrbit n) atTop atTop := by
  intro escape
  have upper := lowBitsMean_eventually_le n hn escape ((L-alpha)/2) (by linarith)
  have lower : ∀ᶠ N : Nat in atTop, alpha+(L-alpha)/2<lowBitsMean n N :=
    average.eventually (lt_mem_nhds (show alpha+(L-alpha)/2<L by linarith))
  obtain ⟨N,hN⟩ := (upper.and lower).exists
  linarith [hN.1,hN.2]

theorem alpha_lt_seven_fourths : alpha<(7:ℝ)/4 := by
  have h := Real.logb_lt_logb (b := 2) (x := (3:ℝ)^4) (y := (2:ℝ)^7)
    (by norm_num) (by norm_num) (by norm_num)
  simp only [Real.logb_pow, logb_two] at h
  norm_num at h
  dsimp only [alpha]
  linarith

theorem no_escape_of_unbiased_lowBits (n : Nat) (hn : n%2=1)
    (average : Tendsto (lowBitsMean n) atTop (𝓝 ((7:ℝ)/4))) :
    ¬Tendsto (oddOrbit n) atTop atTop :=
  no_escape_of_lowBitsMean_limit n hn _ alpha_lt_seven_fourths average

/-- Exact multiplicative recurrence of the Fourier mode on the odd orbit. -/
theorem character_odd_step (k x : Nat) (hx : 0<x) :
    character k (height (oddStep x)) =
      character k alpha * character k (height x) * character k (phaseError x) := by
  rw [odd_phase_identity x hx]
  simp only [sub_eq_add_neg, character_add, character_neg_nat, mul_one]
  ring

/-- Every nonzero Fourier mode of the odd binary-log phases cancels on every
divergent ordinary orbit. Equivalently, this is Weyl's Fourier condition for
uniform distribution of the binary logarithmic phases. The theorem is conditional on actual
escape of this fixed orbit, and proves no rate for shrinking targets. -/
theorem divergent_odd_fourier_mean (n : Nat) (hn : n%2=1)
    (escape : Tendsto (oddOrbit n) atTop atTop) (k : Nat) (hk : 0<k) :
    Tendsto (mean (fun j => character k (height (oddOrbit n j)))) atTop (𝓝 0) := by
  have np : 0<n := by omega
  apply mean_zero_of_rotation _ (character k alpha) (character_alpha_ne_one k hk)
  · intro j
    exact (character_norm k _).le
  · have error := (character_continuous k).continuousAt.tendsto.comp
        (phaseError_tendsto_zero (oddOrbit n) escape)
    have error' : Tendsto (fun j => character k (phaseError (oddOrbit n j))-1)
        atTop (𝓝 0) := by
      simpa [character] using error.sub (tendsto_const_nhds (x := (1:ℂ)))
    apply squeeze_zero_norm (a := fun j => ‖character k (phaseError (oddOrbit n j))-1‖)
    · intro j
      change ‖character k (height (oddStep (oddOrbit n j))) -
        character k alpha * character k (height (oddOrbit n j))‖ ≤ _
      rw [character_odd_step k _ (odd_orbit_positive np j)]
      rw [← mul_sub_one, norm_mul, norm_mul, character_norm, character_norm]
      simp
    · simpa using error'.norm

/-- A nonrepeating ordinary odd orbit escapes every finite set. A separately
supplied quantitative growth hypothesis is unnecessary. -/
theorem nonrepeating_odd_fourier_mean (n : Nat) (hn : n%2=1)
    (nonrepeat : Function.Injective (oddOrbit n)) (k : Nat) (hk : 0<k) :
    Tendsto (mean (fun j => character k (height (oddOrbit n j)))) atTop (𝓝 0) :=
  divergent_odd_fourier_mean n hn nonrepeat.nat_tendsto_atTop k hk

/-- A repeated value traps this deterministic trajectory in an explicitly finite
initial range. This is independent of the Collatz arithmetic. -/
theorem odd_repeat_finite_range (n i j : Nat) (hij : i<j)
    (hrep : oddOrbit n i=oddOrbit n j) (k : Nat) :
    ∃ r<j, oddOrbit n k=oddOrbit n r := by
  induction k with
  | zero => exact ⟨0,by omega,rfl⟩
  | succ k ih =>
    obtain ⟨r,hr,eq⟩ := ih
    by_cases next : r+1<j
    · refine ⟨r+1,next,?_⟩
      simp only [oddOrbit, eq]
    · have last : r+1=j := by omega
      refine ⟨i,hij,?_⟩
      calc
        oddOrbit n (k+1) = oddOrbit n (r+1) := by simp only [oddOrbit, eq]
        _ = oddOrbit n j := by rw [last]
        _ = oddOrbit n i := hrep.symm

/-- Unboundedness of one actual odd trajectory implies escape. The finite-repeat
case cannot be smuggled into the asymptotic rotation argument. -/
theorem unbounded_odd_injective (n : Nat)
    (unbounded : ∀ B, ∃ j, B<oddOrbit n j) : Function.Injective (oddOrbit n) := by
  have ordered : ∀ i j, i<j → oddOrbit n i≠oddOrbit n j := by
    intro i j hij hrep
    let B := ∑ r ∈ range j, oddOrbit n r
    obtain ⟨k,hk⟩ := unbounded B
    obtain ⟨r,hr,eq⟩ := odd_repeat_finite_range n i j hij hrep k
    have bound : oddOrbit n r≤B :=
      Finset.single_le_sum (fun s _ => Nat.zero_le (oddOrbit n s)) (mem_range.mpr hr)
    rw [eq] at hk
    omega
  intro i j eq
  by_contra ne
  rcases lt_or_gt_of_ne ne with h | h
  · exact ordered i j h eq
  · exact ordered j i h eq.symm

theorem unbounded_odd_fourier_mean (n : Nat) (hn : n%2=1)
    (unbounded : ∀ B, ∃ j, B<oddOrbit n j) (k : Nat) (hk : 0<k) :
    Tendsto (mean (fun j => character k (height (oddOrbit n j)))) atTop (𝓝 0) :=
  nonrepeating_odd_fourier_mean n hn (unbounded_odd_injective n unbounded) k hk

#print axioms mean_zero_of_rotation
#print axioms character_alpha_ne_one
#print axioms divergent_odd_fourier_mean
#print axioms nonrepeating_odd_fourier_mean
#print axioms unbounded_odd_fourier_mean
#print axioms lowBitsMean_eventually_le
#print axioms no_escape_of_unbiased_lowBits

end CollatzShell.PhaseFrequency

import AnalyticCoupling
import PhaseFrequency
import Mathlib.NumberTheory.Harmonic.Bounds
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds

/-!
# An explicit temporal counting bound

The parameter choice below converts the finite Fourier-kernel estimate into
a uniform logarithmic bound.  All constants are deliberately conservative.
The final application concerns one actual finite ordinary odd-orbit segment;
its distinctness hypothesis will remain explicit.
-/

namespace CollatzShell.TemporalDensity

open ForwardSection

noncomputable def logBudget (K N : Nat) : ℝ :=
  ((4:ℝ)^K+1)*(2+4*Real.pi*K*(1+Real.log N))

theorem log_le_digits (N : Nat) (hp : 0<N) :
    Real.log (N:ℝ)≤(N.log2:ℝ)+1 := by
  have upper : (N:ℝ)<(2:ℝ)^(N.log2+1) := by
    exact_mod_cast (Nat.lt_log2_self (n:=N))
  have logs := (Real.log_lt_log (by exact_mod_cast hp) upper).le
  rw [Real.log_pow] at logs
  have digits : (0:ℝ)≤(N.log2:ℝ)+1 := by positivity
  have ltwo := mul_le_mul_of_nonneg_left log_two_bounds.2 digits
  push_cast at logs
  linarith

theorem log_budget_bound (N K : Nat) (hp : 0<N) (kp : 0<K)
    (digits : N.log2+1≤16384*(K+1)) :
    logBudget K N≤(2:ℝ)^21*(4:ℝ)^K*(K:ℝ)^2 := by
  have kr : (1:ℝ)≤K := by exact_mod_cast kp
  have lp : 0≤Real.log (N:ℝ) :=
    Real.log_nonneg (by exact_mod_cast hp)
  have ld : Real.log (N:ℝ)≤16384*((K:ℝ)+1) := by
    have c : (N.log2:ℝ)+1≤16384*((K:ℝ)+1) := by exact_mod_cast digits
    exact (log_le_digits N hp).trans c
  have linear : 1+Real.log (N:ℝ)≤32769*(K:ℝ) := by linarith
  have squared : (1:ℝ)≤(K:ℝ)^2 := one_le_pow₀ kr
  have body : 2+4*Real.pi*(K:ℝ)*(1+Real.log N)≤1048576*(K:ℝ)^2 := by
    calc
      _ ≤ 2+16*(K:ℝ)*(1+Real.log N) := by
        have pi : 4*Real.pi≤16 := by linarith only [Real.pi_le_four]
        exact add_le_add le_rfl (mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_right pi (by positivity)) (by linarith only [lp]))
      _ ≤ 2+16*(K:ℝ)*(32769*(K:ℝ)) := by gcongr
      _ ≤ 1048576*(K:ℝ)^2 := by nlinarith only [squared]
  have power : (1:ℝ)≤(4:ℝ)^K := one_le_pow₀ (by norm_num)
  have factor : (4:ℝ)^K+1≤2*(4:ℝ)^K := by linarith only [power]
  unfold logBudget
  calc
    _ ≤ (2*(4:ℝ)^K)*(1048576*(K:ℝ)^2) :=
      mul_le_mul factor body (by positivity) (by positivity)
    _ = (2:ℝ)^21*(4:ℝ)^K*(K:ℝ)^2 := by norm_num; ring

theorem parameter_power_bounds (N K : Nat) (np : 0<N) (kp : 0<K)
    (floor : 16384*K≤N.log2) :
    K*2^(8192*K)≤N ∧ 4*K*(2^21*4^K*K^2)≤N := by
  have lower : 2^(16384*K)≤N := (Nat.le_log2 np.ne').mp floor
  have kpow : K≤2^K := Nat.le_of_lt (Nat.lt_two_pow_self (n:=K))
  have first : K*2^(8192*K)≤2^(16384*K) := by
    calc
      _ ≤ 2^K*2^(8192*K) := Nat.mul_le_mul_right _ kpow
      _ = 2^(8193*K) := by rw [← pow_add]; congr 1; omega
      _ ≤ 2^(16384*K) := Nat.pow_le_pow_right (by decide) (by omega)
  have cube : K^3≤2^(3*K) := by
    calc
      _ ≤ (2^K)^3 := Nat.pow_le_pow_left kpow 3
      _ = 2^(3*K) := by rw [← pow_mul]; congr 1; omega
  have second : 4*K*(2^21*4^K*K^2)≤2^(16384*K) := by
    calc
      _ = 2^23*4^K*K^3 := by norm_num; ring
      _ ≤ 2^23*4^K*2^(3*K) := Nat.mul_le_mul_left _ cube
      _ = 2^(23+5*K) := by
        rw [show (4:Nat)=2^2 by decide,← pow_mul,← pow_add,← pow_add]
        congr 1
        omega
      _ ≤ 2^(16384*K) := Nat.pow_le_pow_right (by decide) (by omega)
  exact ⟨first.trans lower,second.trans lower⟩

/-- A finite arithmetic conversion.  The following application supplies its
    kernel estimate from the actual trajectory rather than assuming it. -/
theorem logarithmic_count_of_kernel (N V : Nat) (vN : V≤N)
    (kernel : ∀ B K : Nat, 1120*Real.pi*(K:ℝ)≤(B:ℝ)+1 →
      (K:ℝ)^2*(V:ℝ)≤(K:ℝ)^2*(2:ℝ)^B+4*K*N+
        4*(K:ℝ)^2*logBudget K N) :
    (N.log2+1)*V≤196608*N := by
  by_cases np : 0<N
  · let K := N.log2/16384
    by_cases kp : 0<K
    · have floor : 16384*K≤N.log2 := by
        dsimp [K]
        have h := Nat.div_mul_le_self N.log2 16384
        omega
      have digits : N.log2+1≤16384*(K+1) := by
        have h := Nat.mod_lt N.log2 (by decide : 0<16384)
        have eq := Nat.mod_add_div N.log2 16384
        dsimp [K]
        omega
      have digits' : N.log2+1≤32768*K := by omega
      have condition : 1120*Real.pi*(K:ℝ)≤((8192*K:Nat):ℝ)+1 := by
        have pi := Real.pi_le_four
        have kr : (0:ℝ)≤K := by positivity
        push_cast
        nlinarith
      have h := kernel (8192*K) K condition
      have budget := log_budget_bound N K np kp digits
      obtain ⟨pow₁,pow₂⟩ := parameter_power_bounds N K np kp floor
      have p₁ : (K:ℝ)*(2:ℝ)^(8192*K)≤N := by exact_mod_cast pow₁
      have p₂ : 4*(K:ℝ)*((2:ℝ)^21*(4:ℝ)^K*(K:ℝ)^2)≤N := by
        exact_mod_cast pow₂
      have error : 4*(K:ℝ)*logBudget K N≤N :=
        (mul_le_mul_of_nonneg_left budget (by positivity)).trans p₂
      have kr : (0:ℝ)<K := by exact_mod_cast kp
      have kp₁ := mul_le_mul_of_nonneg_left p₁ kr.le
      have kp₂ := mul_le_mul_of_nonneg_left error kr.le
      have product : (K:ℝ)^2*(V:ℝ)≤(K:ℝ)*(6*(N:ℝ)) := by
        nlinarith only [h,kp₁,kp₂]
      have small : (K:ℝ)*(V:ℝ)≤6*(N:ℝ) := by
        apply (mul_le_mul_iff_right₀ kr).mp
        nlinarith only [product]
      have smallNat : K*V≤6*N := by exact_mod_cast small
      calc
        (N.log2+1)*V ≤ (32768*K)*V := Nat.mul_le_mul_right _ digits'
        _ = 32768*(K*V) := by ring
        _ ≤ 32768*(6*N) := Nat.mul_le_mul_left _ smallNat
        _ = 196608*N := by ring
    · have small : N.log2+1≤16384 := by dsimp [K] at kp; omega
      have m := Nat.mul_le_mul small vN
      nlinarith
  · have z : N=0 := by omega
    subst N
    simp_all

/-- Every actual finite ordinary odd segment with distinct observed states
    has an explicit logarithmic bound on its marked visits.  The unobserved
    endpoint at time `N` may repeat an earlier value. -/
theorem marked_visits_logarithmic_finite (n N : Nat) (hn : n%2=1)
    (hi : Set.InjOn (oddOrbit n) (↑(Finset.range N) : Set Nat)) :
    (N.log2+1)*MarkFrequency.markedVisits n N≤196608*N := by
  have bound : MarkFrequency.markedVisits n N≤N := by
    unfold MarkFrequency.markedVisits
    exact (Finset.card_filter_le _ _).trans (by simp)
  apply logarithmic_count_of_kernel N (MarkFrequency.markedVisits n N) bound
  intro B K phase
  have finite := AnalyticCoupling.marked_visits_finite_bound n N B K (by omega) hi phase
  have major : AnalyticCoupling.fourierBudget K N≤logBudget K N := by
    unfold AnalyticCoupling.fourierBudget logBudget
    gcongr
    exact harmonic_le_one_add_log N
  exact finite.trans (add_le_add le_rfl
    (mul_le_mul_of_nonneg_left major (by positivity)))

/-- A single fixed nonrepeating ordinary odd trajectory satisfies the same
    bound at every horizon, with a constant independent of its source. -/
theorem marked_visits_logarithmic (n : Nat) (hn : n%2=1)
    (hi : Function.Injective (oddOrbit n)) (N : Nat) :
    (N.log2+1)*MarkFrequency.markedVisits n N≤196608*N :=
  marked_visits_logarithmic_finite n N hn hi.injOn

/-- Actual unboundedness supplies distinctness by determinism.  This theorem
    does not assume an escape rate or summable reciprocal trajectory. -/
theorem unbounded_marked_visits_logarithmic (n : Nat) (hn : n%2=1)
    (unbounded : ∀ B, ∃ j, B<oddOrbit n j) (N : Nat) :
    (N.log2+1)*MarkFrequency.markedVisits n N≤196608*N :=
  marked_visits_logarithmic n hn (PhaseFrequency.unbounded_odd_injective n unbounded) N

#print axioms logarithmic_count_of_kernel
#print axioms marked_visits_logarithmic_finite
#print axioms marked_visits_logarithmic
#print axioms unbounded_marked_visits_logarithmic

end CollatzShell.TemporalDensity

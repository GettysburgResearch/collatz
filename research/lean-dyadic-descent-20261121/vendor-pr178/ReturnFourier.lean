import ForwardSection
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-! Finite, deterministic Fourier control for actual odd Collatz orbits.

The estimate applies to every ordinary prefix.  Injectivity is used only in
the reciprocal-sum estimate, never as a probabilistic independence premise.
-/

namespace CollatzShell.ForwardSection.ReturnFourier

open Finset

noncomputable def character (k : Nat) (u : ℝ) : ℂ :=
  Complex.exp (((2 * Real.pi * k * u : ℝ) : ℂ) * Complex.I)

theorem character_norm (k : Nat) (u : ℝ) : ‖character k u‖ = 1 :=
  Complex.norm_exp_ofReal_mul_I _

theorem character_add (k : Nat) (u v : ℝ) :
    character k (u+v) = character k u * character k v := by
  unfold character
  rw [show (((2*Real.pi*k*(u+v):ℝ):ℂ)*Complex.I) =
    (((2*Real.pi*k*u:ℝ):ℂ)*Complex.I)+(((2*Real.pi*k*v:ℝ):ℂ)*Complex.I) by push_cast; ring]
  exact Complex.exp_add _ _

theorem character_nat (k a : Nat) : character k a = 1 := by
  unfold character
  rw [show (((2*Real.pi*k*(a:ℝ):ℝ):ℂ)*Complex.I) =
    ((k*a:Nat):ℂ)*(2*Real.pi*Complex.I) by push_cast; ring]
  exact Complex.exp_nat_mul_two_pi_mul_I (k*a)

theorem character_sub_nat (k : Nat) (u : ℝ) (a : Nat) :
    character k (u-a) = character k u := by
  have h := character_add k (u-a) a
  rw [sub_add_cancel,character_nat,mul_one] at h
  exact h.symm

private theorem imaginary_exp_change (u : ℝ) :
    ‖Complex.exp ((u:ℂ)*Complex.I)-1‖ ≤ 2*|u| := by
  have normarg : ‖(u:ℂ)*Complex.I‖ = |u| := by simp
  by_cases small : |u|≤1
  · simpa [normarg] using Complex.norm_exp_sub_one_le (x:=(u:ℂ)*Complex.I) (by rwa [normarg])
  · have bound := norm_sub_le (Complex.exp ((u:ℂ)*Complex.I)) (1:ℂ)
    rw [Complex.norm_exp_ofReal_mul_I,norm_one] at bound
    linarith

theorem character_change (k : Nat) (u : ℝ) :
    ‖character k u-1‖ ≤ 4*Real.pi*k*|u| := by
  have h := imaginary_exp_change (2*Real.pi*k*u)
  have nonneg : 0≤2*Real.pi*(k:ℝ) := by positivity
  calc _ ≤ 2*|2*Real.pi*k*u| := h
       _ = _ := by rw [abs_mul,abs_of_nonneg nonneg]; ring

private theorem odd_positive {n : Nat} (hn : 0<n) (j : Nat) :
    0<oddOrbit n j := by
  cases j with
  | zero => exact hn
  | succ j => exact Nat.ordCompl_pos 2 (by omega)

/-- The public, exact phase equation; the error is bounded by the actual state. -/
theorem actual_phase_step (x : Nat) (hx : 0<x) :
    ∃ e : ℝ, 0≤e ∧ e≤1/(x:ℝ) ∧
      height (oddStep x) = height x+alpha-(twos (3*x+1):ℝ)+e := by
  have xp : (0:ℝ)<x := by exact_mod_cast hx
  let d : ℝ := 1/(3*(x:ℝ))
  have dp : 0<d := by dsimp [d]; positivity
  let e := Real.logb 2 (1+d)
  have ep : 0≤e := Real.logb_nonneg (by norm_num) (by linarith)
  have small : e≤1/(x:ℝ) := by
    change Real.log (1+d)/Real.log 2 ≤ _
    apply (div_le_iff₀ (Real.log_pos (by norm_num))).mpr
    have up := Real.log_le_sub_one_of_pos (show 0<1+d by linarith)
    have dl : d*x=1/3 := by dsimp [d]; field_simp
    rw [show 1/(x:ℝ)*Real.log 2=Real.log 2/x by ring]
    apply (le_div_iff₀ xp).mpr
    nlinarith [mul_le_mul_of_nonneg_right up xp.le,log_two_bounds.1]
  have num : (2:ℝ)^(twos (3*x+1))*(oddStep x:ℝ)= (3*x)*(1+d) := by
    have h : (2:ℝ)^(twos (3*x+1))*(oddStep x:ℝ)=3*(x:ℝ)+1 := by
      exact_mod_cast Nat.ordProj_mul_ordCompl_eq_self (3*x+1) 2
    rw [h]; dsimp [d]; field_simp
  have base := congrArg (Real.logb 2) num
  have op : 0<oddStep x := Nat.ordCompl_pos 2 (by omega)
  have op' : (oddStep x:ℝ)≠0 := by positivity
  simp only [Real.logb_mul (by positivity : (2:ℝ)^twos (3*x+1)≠0) op',
    Real.logb_pow,logb_two,mul_one,
    Real.logb_mul (by positivity : 3*(x:ℝ)≠0) (by linarith : 1+d≠0),
    Real.logb_mul (by norm_num : (3:ℝ)≠0) xp.ne'] at base
  refine ⟨e,ep,small,?_⟩
  dsimp only [height,alpha,e] at *
  linarith

theorem actual_character_step (k x : Nat) (hx : 0<x) :
    ‖character k (height (oddStep x))-character k alpha*character k (height x)‖
      ≤ 4*Real.pi*k/(x:ℝ) := by
  obtain ⟨e,el,eu,h⟩ := actual_phase_step x hx
  rw [h,character_add,character_sub_nat,character_add]
  have algebra : character k (height x)*character k alpha*character k e-
      character k alpha*character k (height x) =
      (character k alpha*character k (height x))*(character k e-1) := by ring
  rw [algebra,norm_mul,norm_mul,character_norm,character_norm,one_mul,one_mul]
  calc _ ≤ 4*Real.pi*k*e := by simpa [abs_of_nonneg el] using character_change k e
       _ ≤ 4*Real.pi*k*(1/(x:ℝ)) := mul_le_mul_of_nonneg_left eu (by positivity)
       _ = _ := by ring

/-- The integer halving cocycle is retained in the actual logarithmic height. -/
theorem actual_log_cocycle (n N : Nat) (hn : 0<n) :
    ∃ E : ℝ, 0≤E ∧ E≤∑j∈range N,1/(oddOrbit n j:ℝ) ∧
      height (oddOrbit n N) = height n+(N:ℝ)*alpha-
        (∑j∈range N,(twos (3*oddOrbit n j+1):ℝ))+E := by
  induction N with
  | zero => exact ⟨0,by simp [oddOrbit]⟩
  | succ N ih =>
    obtain ⟨E,El,Eu,hE⟩ := ih
    obtain ⟨e,el,eu,he⟩ := actual_phase_step _ (odd_positive hn N)
    refine ⟨E+e,by linarith,?_,?_⟩
    · rw [sum_range_succ]; linarith
    · rw [oddOrbit,he,hE,sum_range_succ]
      push_cast
      ring

/-- Exact coboundary telescope, including the endpoint terms. -/
theorem sum_coboundary (z : Nat → ℂ) (w : ℂ) (N : Nat) :
    (1-w)*(∑ j ∈ range N,z j) = z 0-z N+
      ∑ j ∈ range N,(z (j+1)-w*z j) := by
  induction N with
  | zero => simp
  | succ N ih => rw [sum_range_succ,sum_range_succ]; rw [mul_add,ih]; ring

/-- A pointwise finite estimate, for the actual ordinary odd orbit. -/
theorem odd_prefix_fourier (n k N : Nat) (hn : 0<n) :
    ‖1-character k alpha‖ * ‖∑ j ∈ range N,character k (height (oddOrbit n j))‖
      ≤ 2 + 4*Real.pi*k*(∑ j ∈ range N,1/(oddOrbit n j:ℝ)) := by
  let z := fun j => character k (height (oddOrbit n j))
  rw [← norm_mul,sum_coboundary]
  calc
    _ ≤ ‖z 0-z N‖+‖∑ j ∈ range N,(z (j+1)-character k alpha*z j)‖ := norm_add_le _ _
    _ ≤ 2+∑ j ∈ range N,‖z (j+1)-character k alpha*z j‖ := by
      have endpts := norm_sub_le (z 0) (z N)
      have zn (j : Nat) : ‖z j‖=1 := character_norm _ _
      rw [zn,zn] at endpts
      norm_num at endpts
      exact add_le_add endpts (norm_sum_le _ _)
    _ ≤ 2+∑ j ∈ range N,4*Real.pi*k/(oddOrbit n j:ℝ) := by
      apply add_le_add le_rfl
      apply sum_le_sum
      intro j _
      exact actual_character_step k _ (odd_positive hn j)
    _ = _ := by rw [mul_sum]; congr 1; apply sum_congr rfl; intro j _; ring

/-- Distinct states give a sublinear reciprocal budget.  The cutoff is free. -/
theorem reciprocal_set_cutoff (s : Finset Nat) (hp : ∀x∈s,0<x) (K : Nat) :
    (∑x∈s,1/(x:ℝ)) ≤ (K:ℝ)+(s.card:ℝ)/(K+1) := by
  let lo := s.filter (fun x => x≤K)
  let hi := s.filter (fun x => ¬x≤K)
  have cardlo : lo.card≤K := by
    have sub : lo⊆Icc 1 K := by
      intro x hx
      obtain ⟨xs,xk⟩ := mem_filter.mp hx
      exact mem_Icc.mpr ⟨hp x xs,xk⟩
    simpa using card_le_card sub
  have cardhi : hi.card≤s.card := card_filter_le _ _
  have low : (∑x∈lo,1/(x:ℝ))≤lo.card := by
    calc _ ≤ ∑x∈lo,(1:ℝ) := by
          apply sum_le_sum
          intro x hx
          have hx' : (1:ℝ)≤x := by exact_mod_cast hp x (mem_filter.mp hx).1
          simpa using one_div_le_one_div_of_le (by norm_num : (0:ℝ)<1) hx'
         _ = _ := by simp
  have high : (∑x∈hi,1/(x:ℝ))≤(hi.card:ℝ)/(K+1) := by
    calc _ ≤ ∑x∈hi,(1:ℝ)/(K+1) := by
          apply sum_le_sum
          intro x hx
          have hx' : (K:ℝ)+1≤x := by exact_mod_cast (show K+1≤x by have := (mem_filter.mp hx).2; omega)
          exact one_div_le_one_div_of_le (by positivity) hx'
         _ = _ := by simp [div_eq_mul_inv]
  have split : (∑x∈s,1/(x:ℝ)) = (∑x∈lo,1/(x:ℝ))+(∑x∈hi,1/(x:ℝ)) :=
    (sum_filter_add_sum_filter_not s (fun x => x≤K) _).symm
  rw [split]
  exact (add_le_add low high).trans (add_le_add (by exact_mod_cast cardlo)
    (div_le_div_of_nonneg_right (by exact_mod_cast cardhi) (by positivity)))

theorem odd_prefix_reciprocal_cutoff (n N K : Nat) (hn : 0<n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat)) :
    (∑j∈range N,1/(oddOrbit n j:ℝ)) ≤ (K:ℝ)+(N:ℝ)/(K+1) := by
  let s := (range N).image (oddOrbit n)
  have card : s.card=N := by simpa [s] using card_image_of_injOn hi
  have hp : ∀x∈s,0<x := by
    intro x hx
    obtain ⟨j,_,rfl⟩ := mem_image.mp hx
    exact odd_positive hn j
  have h := reciprocal_set_cutoff s hp K
  rw [card] at h
  simpa [s,sum_image hi] using h

theorem injective_prefix_fourier (n k N K : Nat) (hn : 0<n)
    (hi : Set.InjOn (oddOrbit n) (↑(range N) : Set Nat)) :
    ‖1-character k alpha‖ * ‖∑ j ∈ range N,character k (height (oddOrbit n j))‖
      ≤ 2 + 4*Real.pi*k*((K:ℝ)+(N:ℝ)/(K+1)) := by
  exact (odd_prefix_fourier n k N hn).trans (add_le_add le_rfl
    (mul_le_mul_of_nonneg_left (odd_prefix_reciprocal_cutoff n N K hn hi) (by positivity)))

/-- Irrationality here needs only separation of the integer powers of two and three. -/
theorem character_alpha_ne_one (k : Nat) (hk : 0<k) : character k alpha≠1 := by
  intro h
  obtain ⟨a,ha⟩ := Complex.exp_eq_one_iff.mp h
  have hi := congrArg Complex.im ha
  simp only [Complex.mul_im,Complex.mul_re,Complex.ofReal_re,Complex.ofReal_im,Complex.I_im,
    Complex.I_re,Complex.intCast_re,Complex.intCast_im,
    Complex.re_ofNat,Complex.im_ofNat,mul_zero,mul_one,zero_mul,
    add_zero,sub_zero] at hi
  have eq : (k:ℝ)*alpha=(a:ℝ) := by
    apply mul_left_cancel₀ (show (2*Real.pi:ℝ)≠0 by positivity)
    nlinarith only [hi]
  have kp : (0:ℝ)<k := by exact_mod_cast hk
  have ap : 0<a := by
    have positive : (0:ℝ)<a := by
      rw [← eq]
      exact mul_pos kp (lt_trans (by norm_num) rotation_bounds.1)
    exact_mod_cast positive
  let b := a.natAbs
  have ab : (b:ℤ)=a := by rw [show (b:ℤ)=|a| from Int.natCast_natAbs _,abs_of_pos ap]
  have br : (b:ℝ)=a := by exact_mod_cast ab
  have near : |(k:ℝ)*alpha-b|≤1/(((4^k:Nat):ℝ)+1) := by rw [eq,br,sub_self,abs_zero]; positivity
  have impossible := grid_barrier (N:=4^k) (by positivity) hk near
  omega

/-- The Fourier averages of every injective positive ordinary odd orbit vanish.
    This is the epsilon definition of the limit, with no random-start premise. -/
theorem fourier_averages_vanish (n k : Nat) (hn : 0<n) (hk : 0<k)
    (hinj : Function.Injective (oddOrbit n)) :
    ∀ ε : ℝ, 0<ε → ∃ N₀ : Nat, ∀ N : Nat, N₀≤N →
      ‖∑ j ∈ range N,character k (height (oddOrbit n j))‖ < ε*N := by
  intro ε hp
  let C : ℝ := 4*Real.pi*k
  let g : ℝ := ‖1-character k alpha‖
  have cp : 0≤C := by dsimp [C]; positivity
  have gp : 0<g := by
    apply norm_pos_iff.mpr
    exact sub_ne_zero.mpr (character_alpha_ne_one k hk).symm
  have eg : 0<ε*g := mul_pos hp gp
  obtain ⟨K,hK⟩ := exists_nat_gt (2*C/(ε*g))
  have kbound : 2*C < (K:ℝ)*(ε*g) := (div_lt_iff₀ eg).mp hK
  have small : C/(K+1) < ε*g/2 := by
    apply (div_lt_iff₀ (by positivity : (0:ℝ)<K+1)).mpr
    nlinarith
  obtain ⟨J,hJ⟩ := exists_nat_gt ((2+C*K)/(ε*g/2))
  have const : 2+C*K < (J:ℝ)*(ε*g/2) := (div_lt_iff₀ (by positivity)).mp hJ
  refine ⟨J+1,?_⟩
  intro N hN
  have np : (0:ℝ)<N := by exact_mod_cast (show 0<N by omega)
  have jl : (J:ℝ)≤N := by exact_mod_cast (show J≤N by omega)
  have constN : 2+C*K < (N:ℝ)*(ε*g/2) :=
    const.trans_le (mul_le_mul_of_nonneg_right jl (by positivity))
  have smallN := mul_lt_mul_of_pos_left small np
  have main := injective_prefix_fourier n k N K hn hinj.injOn
  change g * ‖∑ j ∈ range N,character k (height (oddOrbit n j))‖ ≤
    2+C*((K:ℝ)+(N:ℝ)/(K+1)) at main
  have algebra : 2+C*((K:ℝ)+(N:ℝ)/(K+1)) =
      2+C*K+(N:ℝ)*(C/(K+1)) := by ring
  rw [algebra] at main
  have scaled : g * ‖∑ j ∈ range N,character k (height (oddOrbit n j))‖ <
      g*(ε*N) := by
    apply main.trans_lt
    calc _ < (N:ℝ)*(ε*g/2)+(N:ℝ)*(ε*g/2) := add_lt_add constN smallN
         _ = _ := by ring
  exact (mul_lt_mul_iff_right₀ gp).mp scaled

/-- With an odd source, `odd_orbit_hit` identifies every state here with an
    actual ordinary shortcut iterate of that same source. -/
theorem ordinary_odd_fourier_limit (n k : Nat) (hn : n%2=1) (hk : 0<k)
    (hinj : Function.Injective (oddOrbit n)) :
    ∀ ε : ℝ, 0<ε → ∃ N₀ : Nat, ∀ N : Nat, N₀≤N →
      ‖∑ j ∈ range N,character k (height (oddOrbit n j))‖ < ε*N :=
  fourier_averages_vanish n k (by omega) hk hinj

#print axioms odd_prefix_fourier
#print axioms actual_log_cocycle
#print axioms injective_prefix_fourier
#print axioms fourier_averages_vanish
#print axioms ordinary_odd_fourier_limit

end CollatzShell.ForwardSection.ReturnFourier

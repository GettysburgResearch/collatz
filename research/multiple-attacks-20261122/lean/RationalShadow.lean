module

public import WitnessSynthesis

@[expose] public section

/-!
# Rational shadows that certify successful ordinary descent

The numerator machine has a fixed positive odd denominator. Its finite
parity computation is lifted to actual positive Collatz integers. No
eventual-periodicity statement for rational Collatz orbits is assumed.
-/

namespace CollatzRationalShadow

open CollatzShell CollatzShell.WitnessGlobal

def numeratorStep (d h : Nat) : Nat :=
  if h % 2 = 0 then h / 2 else (3*h+d)/2

def numeratorOrbit : Nat → Nat → Nat → Nat
  | 0, _, h => h
  | k+1, d, h => numeratorOrbit k d (numeratorStep d h)

def numeratorOdds : Nat → Nat → Nat → Nat
  | 0, _, _ => 0
  | k+1, d, h =>
      (if h%2=0 then 0 else 1) + numeratorOdds k d (numeratorStep d h)

private theorem numerator_step_double (d h : Nat) (odd : d%2=1) :
    2*numeratorStep d h = if h%2=0 then h else 3*h+d := by
  unfold numeratorStep
  split <;> omega

private theorem ordinary_step_double (n : Nat) :
    2*step n = if n%2=0 then n else 3*n+1 := by
  unfold step
  split <;> omega

theorem numerator_step_lift (d n v h : Nat) (odd : d%2=1)
    (pin : d*n=2*v+h) :
    d*step n = (if h%2=0 then v else 3*v) + numeratorStep d h := by
  have parity : n%2=h%2 := by
    have eq := congrArg (fun x : Nat => x%2) pin
    simpa only [Nat.mul_mod,Nat.add_mod,odd,Nat.one_mul,Nat.mod_mod,
      Nat.mod_self,Nat.zero_mul,Nat.zero_mod,Nat.zero_add] using eq
  have dn := congrArg (fun x : Nat => d*x) (ordinary_step_double n)
  have dh := numerator_step_double d h odd
  by_cases hp : h%2=0
  · have np : n%2=0 := by omega
    simp only [ite_eq_left hp,ite_eq_left np] at dn dh ⊢
    nlinarith only [pin,dn,dh]
  · have np : n%2≠0 := by omega
    simp only [ite_eq_right hp,ite_eq_right np] at dn dh ⊢
    nlinarith only [pin,dn,dh]

/-- A rational numerator shadow controls precisely the available binary
horizon and keeps the original ordinary target. -/
theorem rational_shadow_lift (k d n v h : Nat) (odd : d%2=1)
    (pin : d*n=2^k*v+h) :
    d*orbit k n = 3^(numeratorOdds k d h)*v+numeratorOrbit k d h := by
  induction k generalizing n v h with
  | zero => simpa [orbit,numeratorOdds,numeratorOrbit] using pin
  | succ k ih =>
      have pin' : d*n=2*(2^k*v)+h := by rw [pow_succ] at pin; nlinarith only [pin]
      have stepPin := numerator_step_lift d n (2^k*v) h odd pin'
      by_cases hp : h%2=0
      · simp only [ite_eq_left hp] at stepPin
        have lifted := ih (step n) v (numeratorStep d h) stepPin
        simpa only [orbit,numeratorOdds,numeratorOrbit,ite_eq_left hp,Nat.zero_add]
          using lifted
      · simp only [ite_eq_right hp] at stepPin
        have stepPin' : d*step n=2^k*(3*v)+numeratorStep d h := by
          nlinarith only [stepPin]
        have lifted := ih (step n) (3*v) (numeratorStep d h) stepPin'
        simpa only [orbit,numeratorOdds,numeratorOrbit,ite_eq_right hp,pow_add,
          pow_one,mul_assoc,mul_left_comm,mul_comm] using lifted

/-- A checked rational prefix gives an actual strict descent whenever its
integer high-part saving pays the exact rational endpoint offset. -/
theorem rational_shadow_descent (k d n v h : Nat) (odd : d%2=1)
    (pin : d*n=2^k*v+h)
    (paid : 3^(numeratorOdds k d h)*v+numeratorOrbit k d h<2^k*v+h) :
    orbit k n<n := by
  have lifted := rational_shadow_lift k d n v h odd pin
  have dp : 0<d := by omega
  exact (Nat.mul_lt_mul_left dp).mp (by omega : d*orbit k n<d*n)

/-- A returning rational shadow with contraction pays every positive
integer displacement, regardless of its size or the supplied source tail. -/
theorem periodic_shadow_descent (k d n v h : Nat) (odd : d%2=1)
    (pin : d*n=2^k*v+h) (positive : 0<v)
    (returns : numeratorOrbit k d h=h)
    (contracts : 3^(numeratorOdds k d h)<2^k) : orbit k n<n := by
  apply rational_shadow_descent k d n v h odd pin
  rw [returns]
  exact Nat.add_lt_add_right (Nat.mul_lt_mul_of_pos_right contracts positive) h

/-- Repeated identical source gaps retain their complete fixed-point
denominator. This identity has no parity approximation or word cutoff. -/
theorem repeated_gap_identity (a e r u D : Nat) (denominator : D+3=2^a)
    (trace : GapTrace r u (List.replicate e a)) :
    (2^a)^e*(D*u)+3^e=3^e*(D*r)+(2^a)^e := by
  induction e generalizing r with
  | zero =>
      have eq : r=u := by simpa [GapTrace] using trace
      simpa using congrArg (fun x => D*x+1) eq.symm
  | succ e ih =>
      simp only [List.replicate_succ,GapTrace] at trace
      obtain ⟨_,v,edge,rest⟩ := trace
      have tail := ih v rest
      have first : (2^a)*(D*v)+3=3*(D*r)+2^a := by
        have eq := congrArg (fun x : Nat => D*x) edge
        ring_nf at eq ⊢
        omega
      have left := congrArg (fun x : Nat => (2^a)*x) tail
      simp only [pow_succ]
      have right' := congrArg (fun x : Nat => 3^e*x) first
      ring_nf at left right' ⊢
      omega

/-- Physical divisibility of a repeated source block gives a positive
dyadic displacement from its rational fixed point. -/
theorem repeated_gap_displacement (a e r u D : Nat) (denominator : D+3=2^a)
    (large : 1<D*r) (trace : GapTrace r u (List.replicate e a)) :
    ∃ t, 0<t ∧ D*r=2^(a*e)*t+1 := by
  have eq := repeated_gap_identity a e r u D denominator trace
  have dr : D*r=(D*r-1)+1 := by omega
  have eq' : 3^e*(D*r-1)+(2^a)^e=(2^a)^e*(D*u) := by
    have dr' := congrArg (fun x : Nat => 3^e*x) dr
    ring_nf at eq dr' ⊢
    omega
  have divides : (2^a)^e ∣ 3^e*(D*r-1)+(2^a)^e := ⟨D*u,eq'⟩
  have prod : (2^a)^e ∣ 3^e*(D*r-1) :=
    (Nat.dvd_add_iff_left (dvd_refl ((2^a)^e))).mpr divides
  have cop : Nat.Coprime ((2^a)^e) (3^e) :=
    (((by decide : Nat.Coprime 2 3).pow_left a).pow_left e).pow_right e
  obtain ⟨t,ht⟩ := cop.dvd_of_dvd_mul_left prod
  have tp : 0<t := by
    by_contra hn
    have tz : t=0 := by omega
    simp only [tz,Nat.mul_zero] at ht
    omega
  refine ⟨t,tp,?_⟩
  rw [pow_mul]
  omega

/-- An affine target over a pinned repeated source block inherits the
same rational shadow. This is the general successful macro interface. -/
theorem affine_source_shadow_descent
    (k d r A B C h t : Nat) (odd : d%2=1)
    (source : d*r=2^h*t+C) (horizon : k≤h)
    (paid : 3^(numeratorOdds k d (A*C+d*B))*(2^(h-k)*A*t)+
      numeratorOrbit k d (A*C+d*B) <
      2^k*(2^(h-k)*A*t)+(A*C+d*B)) :
    orbit k (A*r+B)<A*r+B := by
  have factor : 2^h=2^k*2^(h-k) := by
    rw [← pow_add,show k+(h-k)=h by omega]
  have pin : d*(A*r+B)=2^k*(2^(h-k)*A*t)+(A*C+d*B) := by
    calc
      d*(A*r+B)=A*(d*r)+d*B := by ring
      _ =A*(2^h*t+C)+d*B := by rw [source]
      _ =2^k*(2^(h-k)*A*t)+(A*C+d*B) := by rw [factor]; ring
  exact rational_shadow_descent k d (A*r+B) (2^(h-k)*A*t)
    (A*C+d*B) odd pin paid

theorem three_twos_carry_descent (r u : Nat) (positive : 0<r)
    (trace : GapTrace r u (List.replicate 3 2)) :
    orbit 5 (9*r+2)<9*r+2 := by
  by_cases one : r=1
  · subst r
    decide
  · obtain ⟨t,tp,pin⟩ := repeated_gap_displacement 2 3 r u 1
      (by decide) (by omega) trace
    norm_num at pin
    have target : 1*(9*r+2)=2^5*(18*t)+11 := by omega
    apply rational_shadow_descent 5 1 (9*r+2) (18*t) 11 (by decide) target
    have code : numeratorOdds 5 1 11=3 ∧ numeratorOrbit 5 1 11=10 := by decide
    rw [code.1,code.2]
    norm_num
    omega

theorem two_threes_carry_descent (r u : Nat) (positive : 0<r)
    (trace : GapTrace r u (List.replicate 2 3)) :
    orbit 5 (9*r+2)<9*r+2 := by
  obtain ⟨t,tp,pin⟩ := repeated_gap_displacement 3 2 r u 5
    (by decide) (by omega) trace
  norm_num at pin
  have target : 5*(9*r+2)=2^5*(18*t)+19 := by omega
  apply rational_shadow_descent 5 5 (9*r+2) (18*t) 19 (by decide) target
  have code : numeratorOdds 5 5 19=3 ∧ numeratorOrbit 5 5 19=19 := by decide
  rw [code.1,code.2]
  norm_num
  omega

theorem numerator_orbit_add (k l d h : Nat) :
    numeratorOrbit (k+l) d h=numeratorOrbit l d (numeratorOrbit k d h) := by
  induction k generalizing h with
  | zero => simp [numeratorOrbit]
  | succ k ih =>
      simpa only [Nat.succ_add,numeratorOrbit] using ih (numeratorStep d h)

theorem numerator_odds_add (k l d h : Nat) :
    numeratorOdds (k+l) d h=
      numeratorOdds k d h+numeratorOdds l d (numeratorOrbit k d h) := by
  induction k generalizing h with
  | zero => simp [numeratorOdds,numeratorOrbit]
  | succ k ih =>
      simp only [Nat.succ_add,numeratorOdds,numeratorOrbit]
      rw [ih]
      omega

theorem numerator_trace_append (k l d h middle endpoint p q : Nat)
    (first : numeratorOdds k d h=p ∧ numeratorOrbit k d h=middle)
    (last : numeratorOdds l d middle=q ∧ numeratorOrbit l d middle=endpoint) :
    numeratorOdds (k+l) d h=p+q ∧ numeratorOrbit (k+l) d h=endpoint := by
  simp only [numerator_orbit_add,numerator_odds_add,first.1,first.2,last.1,last.2,
    and_self]

theorem numerator_cycle_repeat (k e d h p : Nat)
    (cycle : numeratorOdds k d h=p ∧ numeratorOrbit k d h=h) :
    numeratorOdds (k*e) d h=p*e ∧ numeratorOrbit (k*e) d h=h := by
  induction e with
  | zero => simp [numeratorOdds,numeratorOrbit]
  | succ e ih =>
      have joined := numerator_trace_append (k*e) k d h h h (p*e) p ih cycle
      simpa only [Nat.mul_succ] using joined

private theorem four_shadow_prefix :
    numeratorOdds 6 13 35=5 ∧ numeratorOrbit 6 13 35=179 := by
  decide

private theorem four_shadow_cycle :
    numeratorOdds 24 13 179=15 ∧ numeratorOrbit 24 13 179=179 := by
  have h0 : numeratorOdds 3 13 473=1 ∧ numeratorOrbit 3 13 473=179 := by decide
  have h1 : numeratorOdds 6 13 131=4 ∧ numeratorOrbit 6 13 131=179 :=
    numerator_trace_append 3 3 13 131 473 179 3 1 (by decide) h0
  have h2 : numeratorOdds 9 13 1048=4 ∧ numeratorOrbit 9 13 1048=179 :=
    numerator_trace_append 3 6 13 1048 131 179 0 4 (by decide) h1
  have h3 : numeratorOdds 12 13 2786=5 ∧ numeratorOrbit 12 13 2786=179 :=
    numerator_trace_append 3 9 13 2786 1048 179 1 4 (by decide) h2
  have h4 : numeratorOdds 15 13 2462=7 ∧ numeratorOrbit 15 13 2462=179 :=
    numerator_trace_append 3 12 13 2462 2786 179 2 5 (by decide) h3
  have h5 : numeratorOdds 18 13 2174=9 ∧ numeratorOrbit 18 13 2174=179 :=
    numerator_trace_append 3 15 13 2174 2462 179 2 7 (by decide) h4
  have h6 : numeratorOdds 21 13 635=12 ∧ numeratorOrbit 21 13 635=179 :=
    numerator_trace_append 3 18 13 635 2174 179 3 9 (by decide) h5
  have h7 : numeratorOdds 24 13 179=15 ∧ numeratorOrbit 24 13 179=179 :=
    numerator_trace_append 3 21 13 179 635 179 3 12 (by decide) h6
  exact h7

private theorem four_shadow_suffix :
    numeratorOdds 18 13 179=11 ∧ numeratorOrbit 18 13 179=131 := by
  have h0 : numeratorOdds 3 13 1048=0 ∧ numeratorOrbit 3 13 1048=131 := by decide
  have h1 : numeratorOdds 6 13 2786=1 ∧ numeratorOrbit 6 13 2786=131 :=
    numerator_trace_append 3 3 13 2786 1048 131 1 0 (by decide) h0
  have h2 : numeratorOdds 9 13 2462=3 ∧ numeratorOrbit 9 13 2462=131 :=
    numerator_trace_append 3 6 13 2462 2786 131 2 1 (by decide) h1
  have h3 : numeratorOdds 12 13 2174=5 ∧ numeratorOrbit 12 13 2174=131 :=
    numerator_trace_append 3 9 13 2174 2462 131 2 3 (by decide) h2
  have h4 : numeratorOdds 15 13 635=8 ∧ numeratorOrbit 15 13 635=131 :=
    numerator_trace_append 3 12 13 635 2174 131 3 5 (by decide) h3
  have h5 : numeratorOdds 18 13 179=11 ∧ numeratorOrbit 18 13 179=131 :=
    numerator_trace_append 3 15 13 179 635 131 3 8 (by decide) h4
  exact h5

attribute [local irreducible] numeratorOdds numeratorOrbit

theorem forty_eight_fours_shadow :
    numeratorOdds 192 13 35=121 ∧ numeratorOrbit 192 13 35=131 := by
  have cycles := numerator_cycle_repeat 24 7 13 179 15 four_shadow_cycle
  simp only [Nat.reduceMul] at cycles
  have tail := numerator_trace_append 168 18 13 179 179 131 105 11 cycles four_shadow_suffix
  simp only [Nat.reduceAdd] at tail
  have result := numerator_trace_append 6 186 13 35 179 131 5 116 four_shadow_prefix tail
  simp only [Nat.reduceAdd] at result
  exact result

theorem forty_eight_fours_carry_descent (r u : Nat) (positive : 0<r)
    (trace : GapTrace r u (List.replicate 48 4)) :
    orbit 192 (9*r+2)<9*r+2 := by
  obtain ⟨t,tp,pin⟩ := repeated_gap_displacement 4 48 r u 13
    (by decide) (by omega) trace
  simp only [Nat.reduceMul] at pin
  have target : 13*(9*r+2)=2^192*(9*t)+35 := by
    calc
      13*(9*r+2)=9*(13*r)+26 := by ring
      _ =9*(2^192*t+1)+26 := by rw [pin]
      _ =2^192*(9*t)+35 := by ring
  apply rational_shadow_descent 192 13 (9*r+2) (9*t) 35 (by decide) target
  rw [forty_eight_fours_shadow.1,forty_eight_fours_shadow.2]
  have margin : 3^121+11≤(2^192 : Nat) := by norm_num
  have gain := Nat.mul_le_mul_right (9*t) margin
  nlinarith only [gain,tp]

end CollatzRationalShadow

#print axioms CollatzRationalShadow.numerator_step_lift
#print axioms CollatzRationalShadow.rational_shadow_lift
#print axioms CollatzRationalShadow.rational_shadow_descent
#print axioms CollatzRationalShadow.periodic_shadow_descent
#print axioms CollatzRationalShadow.repeated_gap_identity
#print axioms CollatzRationalShadow.repeated_gap_displacement
#print axioms CollatzRationalShadow.affine_source_shadow_descent
#print axioms CollatzRationalShadow.three_twos_carry_descent
#print axioms CollatzRationalShadow.two_threes_carry_descent
#print axioms CollatzRationalShadow.numerator_orbit_add
#print axioms CollatzRationalShadow.numerator_odds_add
#print axioms CollatzRationalShadow.numerator_trace_append
#print axioms CollatzRationalShadow.numerator_cycle_repeat
#print axioms CollatzRationalShadow.forty_eight_fours_shadow
#print axioms CollatzRationalShadow.forty_eight_fours_carry_descent

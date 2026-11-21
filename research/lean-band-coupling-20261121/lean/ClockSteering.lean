module

public import ForwardSection

@[expose] public section


/-!
# Forward forcing with an independent clock and floor

`ForwardSection.steer` fixes a square-root odd-step clock and a quarter-source
floor. This module separates those parameters and retains the exact
phase-error cost. The algebraic odd-map statement permits any positive
source; the ordinary-orbit interpretation and the ordinary-clock theorems
require an odd source. The integer phase carry remains explicit.
-/

namespace CollatzShell.ForwardSection

open Real

/-- At an odd endpoint no smaller than its source, the number of ordinary
shortcut clocks is at most twice the number of accelerated odd steps. -/
theorem odd_orbit_bounded_hit {n : Nat} (hn : n%2=1) (j : Nat)
    (lower : n≤oddOrbit n j) :
    ∃ t≤2*j, orbit t n=oddOrbit n j := by
  have np : 0<n := by omega
  refine ⟨clock n j,?_,clock_exact hn j⟩
  have weight : 2^(clock n j)*n≤4^j*n :=
    (Nat.mul_le_mul_left _ lower).trans (clock_weight np j)
  have power : 2^(clock n j)≤2^(2*j) := by
    simpa [pow_mul] using Nat.le_of_mul_le_mul_right weight np
  exact (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp power


/-- A caller may choose the odd-step budget and the floor independently.
Either the actual orbit crosses the floor, or it reaches the prescribed phase
on its upper side. The error is the grid cost `3/q` plus the actual finite
perturbation budget `j/m`. No bound on the integer `z` is asserted. -/
theorem steer_window (n N m : Nat) (np : 0<n) (Np : 0<N) (mp : 0<m)
    (theta : ℝ) :
    ∃ q : Nat, 0<q ∧ q≤N ∧ N+1≤4^q ∧
      ∃ j : Nat, j<q ∧ (oddOrbit n j<m ∨ ∃ z : ℤ,
        0≤height (oddOrbit n j)-(theta+z) ∧
        (q:ℝ)*(height (oddOrbit n j)-(theta+z))≤3+(q:ℝ)*j/m) := by
  obtain ⟨a,q,qp,qn,cop,sep,approx⟩ := rotation_grid N Np
  refine ⟨q,qp,qn,sep,?_⟩
  by_cases floor : ∀ i<q, m≤oddOrbit n i
  · obtain ⟨j,jq,z,gl,gu⟩ := grid_point qp cop (height n-theta)
    obtain ⟨A,e,el,eu,eq⟩ := phase_orbit np mp j
      (fun i hi => floor i (hi.trans jq))
    have qr : (0:ℝ)<q := by exact_mod_cast qp
    have jr : (0:ℝ)≤j := by positivity
    have al : |(j:ℝ)*(q*alpha-a)|≤1 := by
      rw [abs_mul,abs_of_nonneg jr]
      calc (j:ℝ)*|q*alpha-a| ≤ j*(1/((N:ℝ)+1)) :=
             mul_le_mul_of_nonneg_left approx jr
           _ = j/((N:ℝ)+1) := by ring
           _ ≤ 1 := (div_le_one (by positivity)).mpr
             (by exact_mod_cast (by omega : j≤N+1))
    have algebra : (q:ℝ)*(height (oddOrbit n j)-(theta+((z-(A:ℤ):ℤ):ℝ))) =
        q*((height n-theta)+j*((a:ℝ)/q)-z)+j*(q*alpha-a)+q*e := by
      rw [eq]; push_cast; field_simp; ring
    refine ⟨j,jq,Or.inr ⟨z-(A:ℤ),?_,?_⟩⟩
    · apply nonneg_of_mul_nonneg_right (a:= (q:ℝ)) _ qr
      rw [algebra]
      linarith [(abs_le.mp al).1,mul_nonneg qr.le el]
    · have cost : (q:ℝ)*e≤q*j/m := by
        simpa only [mul_div_assoc] using mul_le_mul_of_nonneg_left eu qr.le
      rw [algebra]
      linarith [(abs_le.mp al).2]
  · push Not at floor
    obtain ⟨j,jq,drop⟩ := floor
    exact ⟨j,jq,Or.inl drop⟩

/-- The same forcing statement with an explicit phase-width allowance.
The lower bound `Q` may come from any Diophantine estimate stronger than the
elementary `N+1 ≤ 4^q`. It is a hypothesis about these finite denominators,
not an unproved assertion about all Collatz trajectories. -/
theorem steer_with_precision (n N m Q : Nat)
    (np : 0<n) (Np : 0<N) (mp : 0<m) (Qp : 0<Q)
    (denominator : ∀ q : Nat, 0<q → q≤N → N+1≤4^q → Q≤q)
    (theta : ℝ) :
    ∃ j<N, oddOrbit n j<m ∨ ∃ z : ℤ,
      0≤height (oddOrbit n j)-(theta+z) ∧
      height (oddOrbit n j)-(theta+z)≤3/(Q:ℝ)+(N:ℝ)/m := by
  obtain ⟨q,qp,qn,sep,j,jq,drop | ⟨z,lo,hi⟩⟩ := steer_window n N m np Np mp theta
  · exact ⟨j,jq.trans_le qn,Or.inl drop⟩
  · have qr : (0:ℝ)<q := by exact_mod_cast qp
    have mr : (0:ℝ)<m := by exact_mod_cast mp
    have Qr : (0:ℝ)<Q := by exact_mod_cast Qp
    have Qq : (Q:ℝ)≤q := by exact_mod_cast denominator q qp qn sep
    have jN : (j:ℝ)≤N := by exact_mod_cast jq.le.trans qn
    refine ⟨j,jq.trans_le qn,Or.inr ⟨z,lo,?_⟩⟩
    have bound : height (oddOrbit n j)-(theta+z)≤3/(q:ℝ)+(j:ℝ)/m := by
      apply le_of_mul_le_mul_left (a := (q:ℝ)) _ qr
      convert hi using 1
      field_simp
    calc _ ≤ 3/(q:ℝ)+(j:ℝ)/m := bound
         _ ≤ 3/(Q:ℝ)+(N:ℝ)/m := add_le_add
           (div_le_div_of_nonneg_left (by norm_num) Qr Qq)
           (div_le_div_of_nonneg_right jN mr.le)

/-- A completely explicit lower denominator bound. -/
theorem denominator_of_power_gap {N Q : Nat} (gap : 4^(Q-1)<N+1)
    (q : Nat) (_qp : 0<q) (_qn : q≤N) (sep : N+1≤4^q) : Q≤q := by
  by_contra contra
  have qQ : q≤Q-1 := by omega
  have power : 4^q≤4^(Q-1) := Nat.pow_le_pow_right (by decide) qQ
  omega

/-- On a non-descending prefix the phase visit fits in fewer than `2*N`
ordinary shortcut clocks. This is the regime that can be coupled to a
`d`-bit parity shadow by choosing `2*N ≤ d+1`. -/
theorem steer_non_descending (n N Q : Nat)
    (hn : n%2=1) (Np : 0<N) (Qp : 0<Q)
    (gap : 4^(Q-1)<N+1)
    (noDrop : ∀ j<N, n≤oddOrbit n j) (theta : ℝ) :
    ∃ t<2*N, ∃ j<N, orbit t n=oddOrbit n j ∧ n≤orbit t n ∧
      ∃ z : ℤ, 0≤height (orbit t n)-(theta+z) ∧
        height (orbit t n)-(theta+z)≤3/(Q:ℝ)+(N:ℝ)/n := by
  have np : 0<n := by omega
  obtain ⟨j,jN,drop | ⟨z,lo,hi⟩⟩ := steer_with_precision n N n Q
    np Np np Qp (denominator_of_power_gap gap) theta
  · have := noDrop j jN
    omega
  · obtain ⟨t,tj,hit⟩ := odd_orbit_bounded_hit hn j (noDrop j jN)
    refine ⟨t,by omega,j,jN,hit,?_,z,?_,?_⟩
    · rw [hit]; exact noDrop j jN
    · simpa only [hit] using lo
    · simpa only [hit] using hi

/-- The integer carry must be positive when a non-descending endpoint lies
strictly below the source's phase. This is the extra variable that a phase
approximation alone does not bound from above. -/
theorem positive_phase_carry {x y epsilon : ℝ} {z : ℤ}
    (lower : x≤y) (error : y-(x-epsilon+z)<epsilon) : 1≤z := by
  by_contra contra
  have zn : z≤0 := by omega
  have zr : (z:ℝ)≤0 := by exact_mod_cast zn
  linarith

/-- A genuine consequence of the integer carry: a source that never drops
over the finite odd prefix must gain almost a full binary octave within
the corresponding ordinary clock budget. This is a growth conclusion;
it does not supply the later descent needed for Collatz convergence. -/
theorem no_descent_forces_height_gain (n N Q : Nat)
    (hn : n%2=1) (Np : 0<N) (Qp : 0<Q)
    (gap : 4^(Q-1)<N+1)
    (noDrop : ∀ j<N, n≤oddOrbit n j)
    (epsilon : ℝ) (precision : 3/(Q:ℝ)+(N:ℝ)/n<epsilon) :
    ∃ t<2*N, height n+1-epsilon≤height (orbit t n) := by
  obtain ⟨t,tN,j,jN,hit,lower,z,lo,hi⟩ := steer_non_descending n N Q
    hn Np Qp gap noDrop (height n-epsilon)
  have np : 0<n := by omega
  have logLower : height n≤height (orbit t n) := by
    exact logb_le_logb_of_le (by norm_num : (1:ℝ)<2)
      (by exact_mod_cast np) (by exact_mod_cast lower)
  have carry : 1≤z := positive_phase_carry logLower (hi.trans_lt precision)
  have zr : (1:ℝ)≤z := by exact_mod_cast carry
  exact ⟨t,tN,by linarith⟩

#print axioms odd_orbit_bounded_hit
#print axioms steer_window
#print axioms steer_with_precision
#print axioms steer_non_descending
#print axioms positive_phase_carry
#print axioms no_descent_forces_height_gain

end CollatzShell.ForwardSection

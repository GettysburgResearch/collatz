import ForwardSection
import OffsetDescent
import MarkedOffsetReturn

/-!
# One-sided dyadic approximations for descending marked returns

The irrational rotation estimates are the proved PR173 `rotation_grid` and
`grid_barrier` theorems.  A modular inverse selects the positive side of a
rational grid; no statement about a random parity sequence is used.
-/

namespace CollatzShell.ForwardSection.InfiniteDescent

open Real

/-- Select the first positive grid residue.  The approximation error is too
    small to cross zero, so the resulting approximation has the required sign. -/
theorem positive_side_of_grid {N q a : Nat} (qbig : 2≤q) (qn : q≤N)
    (cop : a.Coprime q) (err : |(q:ℝ)*alpha-a|≤1/((N:ℝ)+1)) :
    ∃ j b : Nat, 0<j ∧ j<q ∧
      0<(j:ℝ)*alpha-b ∧ (q:ℝ)*((j:ℝ)*alpha-b)<2 ∧
      (j:ℝ)*((j:ℝ)*alpha-b)<2 := by
  obtain ⟨u,hu⟩ := Int.mod_coprime cop
  let J := u%(q:ℤ)
  have qz : (0:ℤ)<q := by exact_mod_cast (by omega : 0<q)
  have jl : 0≤J := Int.emod_nonneg _ qz.ne'
  have ju : J<q := Int.emod_lt_of_pos _ qz
  let j := J.toNat
  have je : (j:ℤ)=J := Int.toNat_of_nonneg jl
  have jq : j<q := by exact_mod_cast (je.trans_lt ju)
  have modj : (a:ℤ)*j ≡ 1 [ZMOD ↑q] := by
    rw [je]
    calc (a:ℤ)*J ≡ a*u [ZMOD ↑q] := (Int.mod_modEq _ _).mul_left _
         _ ≡ 1 [ZMOD ↑q] := hu
  obtain ⟨z,hz⟩ := Int.modEq_iff_dvd.mp modj.symm
  have zp : 0≤z := by
    by_contra h
    have zl : z≤-1 := by omega
    have bound := mul_le_mul_of_nonneg_left zl qz.le
    have nonneg : (0:ℤ)≤(a:ℤ)*j := by positivity
    have two : (2:ℤ)≤q := by exact_mod_cast qbig
    nlinarith
  let b := z.toNat
  have be : (b:ℤ)=z := Int.toNat_of_nonneg zp
  have eq : a*j=1+q*b := by
    have iz : (a:ℤ)*j=1+(q:ℤ)*b := by rw [be]; linarith
    exact_mod_cast iz
  have jp : 0<j := by
    by_contra h
    have jz : j=0 := by omega
    rw [jz,Nat.mul_zero] at eq
    omega
  have qr : (0:ℝ)<q := by exact_mod_cast (by omega : 0<q)
  have jr : (0:ℝ)<j := by exact_mod_cast jp
  have nr : (0:ℝ)<(N:ℝ)+1 := by positivity
  have small : (j:ℝ)*(1/((N:ℝ)+1))<1 := by
    rw [mul_one_div]
    apply (div_lt_one nr).mpr
    exact_mod_cast (show j<N+1 by omega)
  have low := mul_le_mul_of_nonneg_left (abs_le.mp err).1 jr.le
  have high := mul_le_mul_of_nonneg_left (abs_le.mp err).2 jr.le
  have er : (a:ℝ)*j=1+(q:ℝ)*b := by exact_mod_cast eq
  have identity : (q:ℝ)*((j:ℝ)*alpha-b)=(j:ℝ)*((q:ℝ)*alpha-a)+1 := by
    nlinarith
  have posprod : 0<(q:ℝ)*((j:ℝ)*alpha-b) := by rw [identity]; nlinarith
  have pos : 0<(j:ℝ)*alpha-b := (mul_pos_iff_of_pos_left qr).mp posprod
  have upper : (q:ℝ)*((j:ℝ)*alpha-b)<2 := by rw [identity]; nlinarith
  have jqr : (j:ℝ)<q := by exact_mod_cast jq
  exact ⟨j,b,jp,jq,pos,upper,lt_trans (mul_lt_mul_of_pos_right jqr pos) upper⟩

/-- Arbitrarily large exponents approach a dyadic power from above at reciprocal
    precision.  The one-sided constant is two.  The proof uses two applications
    of PR173's elementary integer-power separation bound. -/
theorem arbitrarily_large_positive_approximants (K : Nat) :
    ∃ j b : Nat, K<j ∧ 0<(j:ℝ)*alpha-b ∧
      (j:ℝ)*((j:ℝ)*alpha-b)<2 := by
  let B := 4^K
  let M := 2*(B+1)
  let N := 4^M
  have Bp : 0<B := by dsimp [B]; positivity
  have Np : 0<N := by dsimp [N]; positivity
  obtain ⟨a,q,qp,qn,cop,sep,approx⟩ := rotation_grid N Np
  have mq : M≤q := by
    by_contra h
    have less : q<M := by omega
    have power := Nat.pow_lt_pow_right (by decide : 1<4) less
    change 4^q<N at power
    omega
  have qbig : 2≤q := by dsimp [M] at mq; omega
  obtain ⟨j,b,jp,_,pos,upper,scaled⟩ := positive_side_of_grid qbig qn cop approx
  have castmq : 2*((B:ℝ)+1)≤q := by exact_mod_cast mq
  have denom : (0:ℝ)<(B:ℝ)+1 := by positivity
  have weighted : ((B:ℝ)+1)*((j:ℝ)*alpha-b)<1 := by
    have comp := mul_le_mul_of_nonneg_right castmq pos.le
    nlinarith
  have small : |(j:ℝ)*alpha-b|≤1/((B:ℝ)+1) := by
    rw [abs_of_pos pos]
    apply (le_div_iff₀ denom).mpr
    nlinarith
  have barrier := grid_barrier Bp jp small
  have kj : K<j := by
    by_contra h
    have le : j≤K := by omega
    have power := Nat.pow_le_pow_right (by decide : 0<4) le
    change 4^j≤B at power
    omega
  exact ⟨j,b,kj,pos,scaled⟩

/-- A coarse integer bound sufficient to absorb every fixed offset. -/
theorem quadratic_le_two_pow (d : Nat) (large : 5≤d) : d*(d+1)≤2^d := by
  induction d with
  | zero => omega
  | succ d ih =>
    by_cases base : d=4
    · subst d; decide
    have hd : 5≤d := by omega
    have prev := ih hd
    rw [pow_succ]
    nlinarith

theorem fixed_offset_bounds {d r : Nat} (large : 5≤d) (rd : r≤d) :
    r<2^d ∧ (d+1)*r≤70*2^d := by
  have small := Nat.lt_two_pow_self (n:=d)
  have square := quadratic_le_two_pow d large
  constructor
  · omega
  · nlinarith

/-- After sufficiently many terminal cycles, the fixed certificate's original
    odd count is repaid by a strict ordinary affine contraction. -/
theorem padded_coefficient_contract {p q h : Nat} (large : 5*p<q) :
    3^q<2^(h+2*(q-p)) := by
  let m := q-5*p
  have mp : 0<m := by dsimp [m]; omega
  have qm : q=5*p+m := by dsimp [m]; omega
  have ex : h+2*(q-p)=h+8*p+2*m := by omega
  have start : 3^(5*p)≤2^(8*p) := by
    calc 3^(5*p)=(3^5)^p := pow_mul 3 5 p
         _ ≤ (2^8)^p := Nat.pow_le_pow_left (by decide : 3^5≤2^8) p
         _ = _ := (pow_mul 2 8 p).symm
  have rest : 3^m<4^m := Nat.pow_lt_pow_left (by decide) mp.ne'
  calc 3^q=3^(5*p)*3^m := by rw [qm,pow_add]
       _ ≤ 2^(8*p)*3^m := Nat.mul_le_mul_right _ start
       _ < 2^(8*p)*4^m := Nat.mul_lt_mul_of_pos_left rest (by positivity)
       _ = 2^(8*p+2*m) := by
         rw [show (4:Nat)=2^2 by decide,← pow_mul,← pow_add]
       _ ≤ 2^(h+8*p+2*m) := Nat.pow_le_pow_right (by decide) (by omega)
       _ = _ := by rw [ex]

/-- The same finite prefix repays any prescribed natural multiplier. -/
theorem padded_coefficient_contract_scaled {p q h C : Nat}
    (large : 5*(p+C+1)<q) :
    (C+1)*3^q<2^(h+2*(q-p)) := by
  have contract := padded_coefficient_contract (p:=p+C+1) (h:=h) large
  have multiplier : C+1≤2^(2*(C+1)) := by
    have low := Nat.lt_two_pow_self (n:=C+1)
    have high := Nat.pow_le_pow_right (by decide : 0<2)
      (show C+1≤2*(C+1) by omega)
    omega
  have ex : 2*(C+1)+(h+2*(q-(p+C+1)))=h+2*(q-p) := by omega
  calc (C+1)*3^q < (C+1)*2^(h+2*(q-(p+C+1))) :=
         Nat.mul_lt_mul_of_pos_left contract (by omega)
       _ ≤ 2^(2*(C+1))*2^(h+2*(q-(p+C+1))) := Nat.mul_le_mul_right _ multiplier
       _ = _ := by rw [← pow_add,ex]

/-- Every supplied certificate for one fixed positive odd offset yields
    arbitrarily large actual marked-to-marked strict descents.  Both endpoints
    are ordinary integers on one trajectory, and the return index is positive.

    This is an unbounded family, not a statement that every marked point has a
    decreasing return.  The offset is fixed before the dyadic exponent is chosen. -/
theorem arbitrarily_strong_from_certificate {r h : Nat} (odd : r%2=1)
    (hit : orbit h r=1) (C N : Nat) :
    ∃ d y k : Nat, N<2^d+r ∧ Marked (2^d+r) ∧ Marked y ∧
      y<2^d+r ∧ C*y<2^d+r ∧ 0<k ∧ returns (2^d+r) k=y ∧
      (Basin (2^d+r) ↔ Basin y) := by
  let p := OffsetDescent.oddCount h r
  obtain ⟨q,a,large,lower,upper⟩ := arbitrarily_large_positive_approximants (N+5*(p+C+1)+r+5)
  let s := q-p
  let d := h+2*s+1
  let n := 2^d+r
  let y := 2*3^q+1
  have rp : 0<r := by omega
  have qp : 0<q := by omega
  have pl : p≤q := by omega
  have pq : p+s=q := by dsimp [s]; omega
  have qd : q≤d := by dsimp [d,s]; omega
  have dlarge : 5≤d := by omega
  have rd : r≤d := by omega
  have bounds := fixed_offset_bounds dlarge rd
  have initial : Marked n :=
    MarkedOffsetReturn.marked_dyadic_offset (by omega) odd bounds.1 bounds.2
  have target : Marked y :=
    MarkedOffsetReturn.endpoint_marked_of_phase qp lower upper.le
  have endpoint : orbit (h+2*s) n=y := by
    change orbit (h+2*s) (2^(h+2*s+1)+r)=2*3^q+1
    rw [MarkedOffsetReturn.padded_lift_endpoint hit s 1]
    change 3^(p+s)*2^1+1=2*3^q+1
    rw [pq]
    ring
  have contract : 3^q<2^(h+2*s) :=
    padded_coefficient_contract (p:=p) (h:=h) (by omega)
  have decrease : y<n := by
    have scaled := Nat.mul_lt_mul_of_pos_left contract (by decide : 0<2)
    have power : 2*2^(h+2*s)=2^d := by dsimp [d]; rw [pow_succ]; omega
    rw [power] at scaled
    dsimp [y,n]
    omega
  have strong : C*y<n := by
    have coeff := padded_coefficient_contract_scaled (p:=p) (h:=h) (C:=C) (by omega : 5*(p+C+1)<q)
    have scaled := Nat.mul_lt_mul_of_pos_left coeff (by decide : 0<2)
    have power : 2*2^(h+2*s)=2^d := by dsimp [d]; rw [pow_succ]; omega
    change 2*((C+1)*3^q)<2*2^(h+2*s) at scaled
    rw [power] at scaled
    have two := Nat.lt_two_pow_self (n:=q)
    have three := Nat.pow_le_pow_left (by decide : 2≤3) q
    have ample : C<2*3^q := by omega
    dsimp [y,n]
    nlinarith
  have np : 0<n := by dsimp [n]; positivity
  obtain ⟨k,cap⟩ := captures np (h+2*s) (endpoint ▸ target)
  have visited : returns n k=y := cap.trans endpoint
  have kp : 0<k := by
    cases k with
    | zero => simp only [returns] at visited; omega
    | succ k => omega
  have high : N<n := by
    have power := Nat.lt_two_pow_self (n:=d)
    dsimp [n]
    omega
  exact ⟨d,y,k,high,initial,target,decrease,strong,kp,visited,basin_at_hit ⟨_,endpoint⟩⟩

theorem arbitrarily_large_from_certificate {r h : Nat} (odd : r%2=1)
    (hit : orbit h r=1) (N : Nat) :
    ∃ d y k : Nat, N<2^d+r ∧ Marked (2^d+r) ∧ Marked y ∧
      y<2^d+r ∧ 0<k ∧ returns (2^d+r) k=y ∧
      (Basin (2^d+r) ↔ Basin y) := by
  obtain ⟨d,y,k,high,initial,target,drop,_,kp,visited,basin⟩ :=
    arbitrarily_strong_from_certificate odd hit 1 N
  exact ⟨d,y,k,high,initial,target,drop,kp,visited,basin⟩

theorem arbitrarily_large_certified_offset_descents {r : Nat} (odd : r%2=1)
    (known : Basin r) (N : Nat) :
    ∃ d y k : Nat, N<2^d+r ∧ Marked (2^d+r) ∧ Marked y ∧
      y<2^d+r ∧ 0<k ∧ returns (2^d+r) k=y ∧
      (Basin (2^d+r) ↔ Basin y) := by
  obtain ⟨h,hit⟩ := known
  exact arbitrarily_large_from_certificate odd hit N

/-- Arbitrarily large lifts of every certified odd offset admit an arbitrarily
    strong strict contraction in the actual marked-return dynamics. -/
theorem arbitrarily_strong_certified_offset_descents {r : Nat} (odd : r%2=1)
    (known : Basin r) (C N : Nat) :
    ∃ d y k : Nat, N<2^d+r ∧ Marked (2^d+r) ∧ Marked y ∧
      y<2^d+r ∧ C*y<2^d+r ∧ 0<k ∧ returns (2^d+r) k=y ∧
      (Basin (2^d+r) ↔ Basin y) := by
  obtain ⟨h,hit⟩ := known
  exact arbitrarily_strong_from_certificate odd hit C N

/-- An unconditional infinite family: for every size threshold and every
    contraction factor, some marked `2^d+1` has an actual later marked value
    smaller by that factor.  The proof supplies the trivial offset certificate
    directly; there is no unproved basin hypothesis. -/
theorem power_plus_one_arbitrarily_strong (C N : Nat) :
    ∃ d y k : Nat, N<2^d+1 ∧ Marked (2^d+1) ∧ Marked y ∧
      y<2^d+1 ∧ C*y<2^d+1 ∧ 0<k ∧ returns (2^d+1) k=y ∧
      (Basin (2^d+1) ↔ Basin y) := by
  exact arbitrarily_strong_from_certificate (r:=1) (h:=0) (by decide) rfl C N

#print axioms arbitrarily_large_positive_approximants
#print axioms arbitrarily_large_certified_offset_descents
#print axioms arbitrarily_strong_certified_offset_descents
#print axioms power_plus_one_arbitrarily_strong

end CollatzShell.ForwardSection.InfiniteDescent

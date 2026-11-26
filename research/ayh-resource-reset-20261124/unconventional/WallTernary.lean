import WallWords

namespace WallTernary
open WallRefinement WallGeneral WallRational

private theorem hit_one (a u : Nat) (big : 2≤a) (unit : u%3≠0) :
    ∃ k t, 0<k ∧ 2^k*u=3^a*t+1 := by
  let j := a-1
  let Q := 3^a
  let L := 2*3^j
  have aeq : j+1=a := by dsimp [j];omega
  obtain ⟨e,z,_,ez⟩ := TernaryPowerLift.cofinal j u 1 unit
  obtain ⟨b,eb⟩ := TernaryPowerLift.period j
  rw [aeq] at ez eb
  have eu : 2^e ≡ u [MOD Q] := by rw [ez];simp [Nat.ModEq,Q]
  have lb : 2^L ≡ 1 [MOD Q] := by dsimp [L];rw [eb];simp [Nat.ModEq,Q]
  let N := L*(e+2)
  let k := N-e
  have lp : 1≤L := by
    have q : 0<3^j := by positivity
    dsimp [L];omega
  have large : e+2≤N := by
    dsimp [N];simpa using Nat.mul_le_mul_right (e+2) lp
  have power : 2^N ≡ 1 [MOD Q] := by simpa [N,pow_mul] using lb.pow (e+2)
  have rel : 2^k*u ≡ 1 [MOD Q] := by
    apply (eu.mul_left (2^k)).symm.trans
    rw [←pow_add,show k+e=N by dsimp [k];omega]
    exact power
  have q4 : 4<Q := by
    dsimp [Q]
    have high : 3^2≤3^a := Nat.pow_le_pow_right (by decide) big
    omega
  have re : (2^k*u)%Q=1 := Eq.trans rel (Nat.mod_eq_of_lt (by omega))
  obtain rep := Nat.mod_add_div (2^k*u) Q
  rw [re] at rep
  refine ⟨k,(2^k*u)/Q,by dsimp [k];omega,?_⟩
  change 2^k*u=Q*((2^k*u)/Q)+1
  omega

private theorem ternary_clock (a u : Nat) (big : 2≤a) (unit : u%3≠0) :
    ∃ j, 0<j ∧ ∀ (C : Coloring) (n : Nat), Mixed C n →
      index C n j≠2^j*n+(2^j*u)/(3^a) := by
  obtain ⟨k,t,kp,eq⟩ := hit_one a u big unit
  let Q := 3^a
  have q4 : 4<Q := by
    dsimp [Q]
    have high : 3^2≤3^a := Nat.pow_le_pow_right (by decide) big
    omega
  have kp2 : 2^k=2*2^(k-1) := by nth_rw 1 [show k=(k-1)+1 by omega];rw [pow_succ];ring
  have powerOdd (i : Nat) : 3^i%2=1 := by
    induction i with
    | zero => decide
    | succ i ih => rw [pow_succ,Nat.mul_mod,ih]
  have qOdd : Q%2=1 := powerOdd a
  have tOdd : t%2=1 := by
    have em := congrArg (fun w : Nat => w%2) eq
    change (2^k*u)%2=(Q*t+1)%2 at em
    rw [kp2,show 2*2^(k-1)*u=2*(2^(k-1)*u) by ring] at em
    rw [Nat.add_mod,Nat.mul_mod Q t,qOdd] at em
    omega
  have power : 2^(k+2)*u=Q*(4*t)+4 := by
    rw [pow_add,show 2^k*2^2*u=4*(2^k*u) by ring,eq]
    dsimp [Q];ring
  have div : (2^(k+2)*u)/Q=4*t := by
    apply Nat.div_eq_of_lt_le
    · rw [power,Nat.mul_comm Q (4*t)];omega
    · rw [power,Nat.add_mul,Nat.one_mul,Nat.mul_comm Q (4*t)];omega
  refine ⟨k+2,by omega,?_⟩
  intro C n cut wall
  change index C n (k+2)=2^(k+2)*n+(2^(k+2)*u)/Q at wall
  rw [div,show 2^(k+2)*n=8*(2^(k-1)*n) by rw [pow_add,kp2];ring] at wall
  let m := index C n (k+2)/8
  have bad := forbidden_even_run C cut (k+2) 0 m
  apply bad
  dsimp [m]
  omega

/-- A rational wall address with reduced purely ternary denominator at least
nine would append 100 at an actual phase of its dyadic expansion. -/
theorem excludes_power_three (C : Coloring) {n : Nat} (cut : Mixed C n)
    (a u : Nat) (big : 2≤a) (unit : u%3≠0) :
    ¬ ∀ j, index C n j=2^j*n+(2^j*u)/(3^a) := by
  obtain ⟨j,_,bad⟩ := ternary_clock a u big unit
  exact fun all => bad C n cut (all j)

theorem finite_floor (C : Coloring) (n N Q u j : Nat) (le : j≤N) (fits : u<Q)
    (e : Q*index C n N+u=2^N*(Q*n+u)) :
    index C n j=2^j*n+(2^j*u)/Q := by
  let m := index C n j
  let k := N-j
  have clock : j+k=N := by dsimp [k];omega
  have endpt : index C m k=index C n N := by
    dsimp [m];rw [←WallPeriodic.index_add,clock]
  rw [←clock,pow_add,show 2^j*2^k*(Q*n+u)=2^k*(2^j*(Q*n+u)) by ring,clock,←endpt] at e
  have bounds := WallWords.range C m k
  have lo : 2^k*(Q*m) ≤ 2^k*(2^j*(Q*n+u)) := by
    rw [←e,show 2^k*(Q*m)=Q*(2^k*m) by ring]
    exact le_trans (Nat.mul_le_mul_left Q bounds.1) (by omega)
  have hi : 2^k*(2^j*(Q*n+u)) < 2^k*(Q*(m+1)) := by
    rw [←e,show 2^k*(Q*(m+1))=Q*(2^k*(m+1)) by ring]
    have hard := Nat.mul_le_mul_left Q (show index C m k+1≤2^k*(m+1) by omega)
    rw [Nat.mul_add,Nat.mul_one] at hard
    omega
  have dl := Nat.le_of_mul_le_mul_left lo (by positivity : 0<2^k)
  have dh := Nat.lt_of_mul_lt_mul_left hi
  have quotient : (2^j*(Q*n+u))/Q=m := Nat.div_eq_of_lt_le
    (by simpa [Nat.mul_comm Q m] using dl) (by simpa [Nat.mul_comm Q (m+1)] using dh)
  rw [show 2^j*(Q*n+u)=Q*(2^j*n)+2^j*u by ring,Nat.mul_add_div (by omega : 0<Q)] at quotient
  exact quotient.symm

private theorem anchor_eq (L p n d a u k : Nat) (den : d+1=2^L)
    (dpos : 0<d) (frac : p*3^a=d*u) :
    3^a*address L p n k+u=2^(L*k)*(3^a*n+u) := by
  apply Nat.eq_of_mul_eq_mul_left dpos
  have addr := address_eq L p n d k den
  calc
    d*(3^a*address L p n k+u) = 3^a*(d*address L p n k)+d*u := by ring
    _ = 3^a*(d*address L p n k+p) := by rw [←frac];ring
    _ = 3^a*(2^(L*k)*(d*n+p)) := by rw [addr]
    _ = 2^(L*k)*(d*(3^a*n)+p*3^a) := by ring
    _ = d*(2^(L*k)*(3^a*n+u)) := by rw [frac];ring


/-- For a purely ternary reduced denominator at least nine, one finite
clock excludes the repeated word from every ordinary wall at every root. -/
theorem ternary_bound (L p d a u : Nat) (pos : 0<L) (den : d+1=2^L) (dpos : 0<d)
    (fits : u<3^a) (big : 2≤a) (unit : u%3≠0) (frac : p*3^a=d*u) :
    ∃ K, 0<K ∧ ∀ (C : Coloring) (n : Nat), Mixed C n →
      index C n (L*K)≠address L p n K := by
  obtain ⟨k,kp,clock⟩ := ternary_clock a u big unit
  refine ⟨k,kp,?_⟩
  intro C n cut eq
  apply clock C n cut
  apply finite_floor C n (L*k) (3^a) u k (by simpa using Nat.mul_le_mul_right k pos) fits
  rw [eq];exact anchor_eq L p n d a u k den dpos frac

/-- A periodic word representing a reduced fraction with ternary denominator
at least nine cannot track an ordinary mixed edge. -/
theorem rejects_ternary_word (C : Coloring) {n : Nat} (cut : Mixed C n)
    (L p d a u : Nat) (pos : 0<L) (den : d+1=2^L) (dpos : 0<d)
    (fits : u<3^a) (big : 2≤a) (unit : u%3≠0) (frac : p*3^a=d*u) :
    ∃ k, index C n (L*k)≠address L p n k := by
  obtain ⟨k,_,bad⟩ := ternary_bound L p d a u pos den dpos fits big unit frac
  exact ⟨k,bad C n cut⟩

end WallTernary

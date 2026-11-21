import OffsetDescent
import Mathlib.Data.Nat.Factorization.Basic

/-!
# Original-source descent and a finite residual set of first gaps

For odd `n`, the first gap of the source `3*n` is the exponent `A` in
`9*n+1 = 2^A*u`, with `u` odd.  The arithmetic is the same as the high-gap
handoff in PR177, but the conclusions below compare actual forward values
with the ORIGINAL `n`.  No certificate for `3*n` is assumed.

All even gaps at least four and all odd gaps at least nine give explicit
ordinary descent.  Together with gaps zero and one, this leaves only
`{2,3,5,7}` for a source that never descends.  The restriction applies to the
original source, not every future orbit state.
-/

namespace CollatzShell.MergerDispatch

open OffsetDescent

/-- The high-gap handoff as a direct identity on the wanted ordinary source. -/
theorem two_steps_nine_gap {n A u : Nat} (large : 2≤A)
    (source : 9*n+1=2^A*u) :
    orbit 2 n=2^(A-2)*u+1 := by
  have split : 2^A=4*2^(A-2) := by
    calc 2^A=2^(2+(A-2)) := by congr 1; omega
         _ = _ := by rw [pow_add]; norm_num
  rw [split,mul_assoc] at source
  have residue : n%4=3 := by omega
  have odd : n%2≠0 := by omega
  have nextOdd : ((3*n+1)/2)%2≠0 := by omega
  simp only [orbit,step,odd,nextOdd,ite_false]
  omega

/-- Exact terminal-cycle transport on an arbitrary high coefficient. -/
theorem one_even_lift (b u : Nat) :
    orbit (2*b) (2^(2*b)*u+1)=3^b*u+1 := by
  simpa only [oddCount_twice_one,orbit_twice_one] using affine_lift (2*b) 1 u

theorem one_odd_lift (b u : Nat) :
    orbit (2*b+1) (2^(2*b+1)*u+1)=3^(b+1)*u+2 := by
  rw [orbit_add]
  have split : 2^(2*b+1)*u+1=2^(2*b)*(2*u)+1 := by rw [pow_succ]; ring
  rw [split,one_even_lift]
  rw [show 3^b*(2*u)=2*(3^b*u) by ring]
  have odd : (2*(3^b*u)+1)%2≠0 := by omega
  simp only [orbit,step,odd,ite_false]
  rw [show 3^(b+1)*u=3*(3^b*u) by rw [pow_succ]; ring]
  omega

/-- Exact even-gap endpoint after its final halving; no supplied basin
    hypothesis is used.  Strict descent requires the later `b ≥ 1` guard. -/
theorem even_gap_endpoint {n b u : Nat} (source : 9*n+1=2^(2*b+2)*u)
    (odd : u%2=1) :
    2*orbit (2*b+3) n=3^b*u+1 := by
  have first := two_steps_nine_gap (n:=n) (A:=2*b+2) (u:=u) (by omega) source
  have middle : orbit (2*b+2) n=3^b*u+1 := by
    rw [show 2*b+2=2+2*b by omega,orbit_add,first]
    simpa using one_even_lift b u
  rw [show 2*b+3=(2*b+2)+1 by omega,orbit_add,middle]
  have powOdd : 3^b%2=1 := by simp [Nat.pow_mod]
  have even : (3^b*u+1)%2=0 := by
    rw [Nat.add_mod,Nat.mul_mod,powOdd,odd]
  simp only [orbit,step,even,ite_true]
  omega

private theorem even_gap_margin {b : Nat} (large : 2≤b) :
    9*3^b+20≤2*2^(2*b+2) := by
  induction b,large using Nat.le_induction with
  | base => decide
  | succ b hb ih =>
    have grow : 2^(2*(b+1)+2)=4*2^(2*b+2) := by
      rw [show 2*(b+1)+2=(2*b+2)+2 by omega,pow_add]
      ring
    rw [show 3^(b+1)=3^b*3 from pow_succ 3 b,grow]
    omega

theorem even_gap_descent {n b u : Nat} (large : 1≤b)
    (source : 9*n+1=2^(2*b+2)*u) (odd : u%2=1) :
    orbit (2*b+3) n<n := by
  have endpoint := even_gap_endpoint source odd
  have up : 0<u := by omega
  by_cases first : b=1
  · subst b
    norm_num only [Nat.reduceMul,Nat.reduceAdd,Nat.reducePow] at source endpoint ⊢
    have three : 3≤u := by omega
    omega
  · have margin := Nat.mul_le_mul_right u (even_gap_margin (b:=b) (by omega))
    nlinarith

/-- On an odd first gap, the exact endpoint has the affine form appearing in
    the remaining certificate-transfer problem. -/
theorem odd_gap_endpoint {n b u : Nat} (source : 9*n+1=2^(2*b+3)*u) :
    orbit (2*b+3) n=3^(b+1)*u+2 := by
  have first := two_steps_nine_gap (n:=n) (A:=2*b+3) (u:=u) (by omega) source
  rw [show 2*b+3=2+(2*b+1) by omega,orbit_add,first]
  simpa using one_odd_lift b u

/-- Stop one clock before the odd-gap endpoint. This exact earlier value is
    smaller for every odd gap at least nine. -/
theorem odd_gap_early_endpoint {n b u : Nat} (source : 9*n+1=2^(2*b+3)*u) :
    orbit (2*b+2) n=2*(3^b*u)+1 := by
  have first := two_steps_nine_gap (n:=n) (A:=2*b+3) (u:=u) (by omega) source
  rw [show 2*b+3-2=2*b+1 by omega] at first
  rw [show 2*b+2=2+2*b by omega,orbit_add,first]
  rw [show 2^(2*b+1)*u+1=2^(2*b)*(2*u)+1 by rw [pow_succ]; ring]
  rw [one_even_lift]
  ring

private theorem odd_gap_margin {b : Nat} (large : 3≤b) :
    18*3^b+20≤2^(2*b+3) := by
  induction b,large using Nat.le_induction with
  | base => decide
  | succ b hb ih =>
    have grow : 2^(2*(b+1)+3)=4*2^(2*b+3) := by
      rw [show 2*(b+1)+3=(2*b+3)+2 by omega,pow_add]
      ring
    rw [show 3^(b+1)=3^b*3 from pow_succ 3 b,grow]
    omega

theorem odd_gap_descent {n b u : Nat} (large : 3≤b)
    (source : 9*n+1=2^(2*b+3)*u) (up : 0<u) :
    orbit (2*b+2) n<n := by
  have endpoint := odd_gap_early_endpoint source
  have margin := Nat.mul_le_mul_right u (odd_gap_margin large)
  nlinarith

/-- An actual orbit with no descent leaves only four first-gap values for its
    original tripled source.  No assertion about every future state is made. -/
theorem no_descent_gap_residual {n A u : Nat} (np : 1<n)
    (source : 9*n+1=2^A*u) (odd : u%2=1)
    (floor : ∀ t, n≤orbit t n) :
    A=2 ∨ A=3 ∨ A=5 ∨ A=7 := by
  by_contra missing
  have up : 0<u := by omega
  have nonzero : A≠0 := by
    intro zero
    rw [zero,pow_zero,one_mul] at source
    have even : n%2=0 := by omega
    have h := floor 1
    simp only [orbit,step,even,ite_true] at h
    omega
  have notOne : A≠1 := by
    intro one
    rw [one] at source
    norm_num at source
    have residue : n%4=1 := by omega
    have oddN : n%2≠0 := by omega
    have nextEven : ((3*n+1)/2)%2=0 := by omega
    have h := floor 2
    simp only [orbit,step,oddN,nextEven,ite_false,ite_true] at h
    omega
  by_cases parity : A%2=0
  · let b := A/2-1
    have large : 1≤b := by dsimp [b]; omega
    have decomp : A=2*b+2 := by dsimp [b]; omega
    rw [decomp] at source
    have drop := even_gap_descent large source odd
    have h := floor (2*b+3)
    omega
  · let b := (A-3)/2
    have large : 3≤b := by dsimp [b]; omega
    have decomp : A=2*b+3 := by dsimp [b]; omega
    rw [decomp] at source
    have drop := odd_gap_descent large source up
    have h := floor (2*b+2)
    omega

/-- The same restriction at the canonical exact valuation. -/
theorem no_descent_valuation_residual {n : Nat} (np : 1<n)
    (floor : ∀ t, n≤orbit t n) :
    let A := (9*n+1).factorization 2
    A=2 ∨ A=3 ∨ A=5 ∨ A=7 := by
  have split : 9*n+1=2^((9*n+1).factorization 2)*ordCompl[2] (9*n+1) :=
    (Nat.ordProj_mul_ordCompl_eq_self (9*n+1) 2).symm
  have notEven : ¬2∣ordCompl[2] (9*n+1) :=
    Nat.not_dvd_ordCompl Nat.prime_two (by omega : 9*n+1≠0)
  exact no_descent_gap_residual np split (by omega) floor

/-- The smaller positive source is also a common-orbit partner. In fact it
    is the earlier actual iterate identified by `odd_gap_early_endpoint`. -/
theorem odd_gap_smaller_partner {n b u : Nat} (large : 3≤b)
    (source : 9*n+1=2^(2*b+3)*u) (up : 0<u) :
    ∃ w : Nat, 0<w ∧ w<n ∧ orbit 1 w=orbit (2*b+3) n := by
  refine ⟨2*(3^b*u)+1,by positivity,?_,?_⟩
  · rw [← odd_gap_early_endpoint source]
    exact odd_gap_descent large source up
  · rw [odd_gap_endpoint source]
    have odd : (2*(3^b*u)+1)%2≠0 := by omega
    simp only [orbit,step,odd,ite_false]
    rw [show 3^(b+1)*u=3*(3^b*u) by rw [pow_succ]; ring]
    omega

/-- Ordinary component minimality, always measured against the original
    source.  The two clocks may differ. -/
def ComponentMinimum (n : Nat) : Prop :=
  ∀ m i j : Nat, 0<m → orbit i m=orbit j n → n≤m

private theorem ordinary_orbit_positive (t n : Nat) (np : 0<n) :
    0<orbit t n := by
  induction t generalizing n with
  | zero => exact np
  | succ t ih =>
    apply ih
    unfold step
    split <;> omega

/-- A component minimum satisfies the same four-gap forward restriction. -/
theorem component_minimum_gap_residual {n A u : Nat} (np : 1<n)
    (source : 9*n+1=2^A*u) (odd : u%2=1)
    (floor : ComponentMinimum n) : A=2 ∨ A=3 ∨ A=5 ∨ A=7 := by
  have forward : ∀ t, n≤orbit t n := by
    intro t
    exact floor (orbit t n) 0 t (ordinary_orbit_positive t n (by omega)) rfl
  exact no_descent_gap_residual np source odd forward

/-- Canonical exact valuation restriction for a positive component minimum
    other than one. -/
theorem component_minimum_valuation_residual {n : Nat} (np : 1<n)
    (floor : ComponentMinimum n) :
    let A := (9*n+1).factorization 2
    A=2 ∨ A=3 ∨ A=5 ∨ A=7 := by
  have split : 9*n+1=2^((9*n+1).factorization 2)*ordCompl[2] (9*n+1) :=
    (Nat.ordProj_mul_ordCompl_eq_self (9*n+1) 2).symm
  have notEven : ¬2∣ordCompl[2] (9*n+1) :=
    Nat.not_dvd_ordCompl Nat.prime_two (by omega : 9*n+1≠0)
  exact component_minimum_gap_residual np split (by omega) floor

/-- The least-counterexample application uses ordinary value minimality and
    exact common-orbit equality; it does not assume a certificate for `3*n`. -/
theorem least_counterexample_valuation_residual {n : Nat} (np : 1<n)
    (bad : ¬Basin n) (smaller : ∀ m, 0<m → m<n → Basin m) :
    let A := (9*n+1).factorization 2
    A=2 ∨ A=3 ∨ A=5 ∨ A=7 := by
  apply component_minimum_valuation_residual np
  intro m i j mp meet
  by_contra missing
  have known := smaller m mp (by omega)
  apply bad
  apply (basin_at_hit (show Hits n (orbit j n) from ⟨j,rfl⟩)).mpr
  rw [← meet]
  exact (basin_at_hit (show Hits m (orbit i m) from ⟨i,rfl⟩)).mp known

#print axioms two_steps_nine_gap
#print axioms even_gap_descent
#print axioms odd_gap_early_endpoint
#print axioms odd_gap_descent
#print axioms no_descent_valuation_residual
#print axioms odd_gap_smaller_partner
#print axioms component_minimum_valuation_residual
#print axioms least_counterexample_valuation_residual

end CollatzShell.MergerDispatch

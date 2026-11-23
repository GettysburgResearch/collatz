module

public import ShellCover

@[expose] public section

/-!
# Deleting initial odd steps through a synchronous endpoint diamond

These are physical common-future certificates for one fixed ordinary source.
The generic theorem removes `r` initial odd steps and gives an exact factor
`2^r` improvement in source height. Its diamond hypothesis is explicit; no
universal diamond cover is asserted. The two-clock specialization below
discharges it on an infinite residue family.
-/

namespace CollatzShell

/-- A synchronous diamond at the end of an initial odd run permits deletion
of `r` initial odd steps. The new source is smaller by an exact dyadic factor
after adding one. -/
theorem rising_erase_prefix (k r h u : Nat) (hr : 0<r) (hrk : r<k)
    (hu : 0<u)
    (diamond : orbit h (3^(k-r)*u-1) =
      orbit h (3^r*(3^(k-r)*u)-1)) :
    let n := 2^k*u-1
    let x := 2^(k-r)*u-1
    0<x ∧ 2^r*(x+1)=n+1 ∧ x<n ∧
      orbit (k-r+h) x=orbit (k+h) n := by
  dsimp only
  have core : 0<2^(k-r)*u := by positivity
  have two : 2≤2^(k-r) := (show 2=2^1 by rfl) ▸
    Nat.pow_le_pow_right (by decide : 0<2) (by omega : 1≤k-r)
  have two_r : 2≤2^r := (show 2=2^1 by rfl) ▸
    Nat.pow_le_pow_right (by decide : 0<2) hr
  have bigcore : 2≤2^(k-r)*u := by nlinarith only [two,hu]
  have scale : 2^k*u=2^r*(2^(k-r)*u) := by
    calc
      2^k*u=2^(r+(k-r))*u := by rw [show r+(k-r)=k by omega]
      _ =2^r*(2^(k-r)*u) := by rw [pow_add]; ring
  have scale3 : 3^r*(3^(k-r)*u)=3^k*u := by
    rw [← Nat.mul_assoc,← pow_add,show r+(k-r)=k by omega]
  have lower : 2*(2^(k-r)*u)≤2^k*u := by
    rw [scale]
    exact Nat.mul_le_mul_right _ two_r
  refine ⟨by omega,?_,by omega,?_⟩
  · rw [Nat.sub_add_cancel (by omega : 1≤2^(k-r)*u),
      Nat.sub_add_cancel (by omega : 1≤2^k*u)]
    exact scale.symm
  · rw [orbit_add,orbit_add,(odd_run (k-r) u hu).1,(odd_run k u hu).1]
    simpa only [scale3] using diamond

/-- The half-source version used to lift endpoint diamonds from the
literature-inspired affine word search. -/
theorem rising_half_source_of_diamond (k h u : Nat) (hk : 2≤k) (hu : 0<u)
    (diamond : orbit h (3^(k-1)*u-1) =
      orbit h (3*(3^(k-1)*u)-1)) :
    let n := 2^k*u-1
    let x := 2^(k-1)*u-1
    0<x ∧ 2*x+1=n ∧ x<n ∧
      orbit (k-1+h) x=orbit (k+h) n := by
  have d : orbit h (3^(k-1)*u-1)=
      orbit h (3^1*(3^(k-1)*u)-1) := by simpa using diamond
  obtain ⟨xp,scale,lower,merge⟩ :=
    rising_erase_prefix k 1 h u (by decide) (by omega) hu d
  dsimp only at *
  refine ⟨xp,?_,lower,merge⟩
  norm_num only [pow_one] at scale
  omega

/-- The endpoint pair `v-1,3*v-1` has a two-clock diamond when `v=3 mod 4`.
No convergence assumption is used. -/
theorem half_source_two_clock_diamond (v : Nat) (phase : v%4=3) :
    orbit 2 (v-1)=orbit 2 (3*v-1) := by
  have ae : (v-1)%2=0 := by omega
  have aq : ((v-1)/2)%2≠0 := by omega
  have be : (3*v-1)%2=0 := by omega
  have bq : ((3*v-1)/2)%2=0 := by omega
  simp only [orbit,step,ae,aq,be,bq,ite_true,ite_false]
  omega

/-- A strictly stronger source-size conclusion than the three-quarter-source
partner in PR184: the same residue family has partner `(n-1)/2`. -/
theorem rising_half_source_partner (k u : Nat) (hk : 2≤k) (hu : 0<u)
    (phase : (3^(k-1)*u)%4=3) :
    let n := 2^k*u-1
    let x := 2^(k-1)*u-1
    0<x ∧ 2*x+1=n ∧ x<n ∧ orbit (k+1) x=orbit (k+2) n := by
  have diamond := half_source_two_clock_diamond (3^(k-1)*u) phase
  have result := rising_half_source_of_diamond k 2 u hk hu diamond
  simpa only [show k-1+2=k+1 by omega] using result

#print axioms rising_erase_prefix
#print axioms rising_half_source_of_diamond
#print axioms half_source_two_clock_diamond
#print axioms rising_half_source_partner

end CollatzShell

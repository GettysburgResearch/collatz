module

public import ShellCover

@[expose] public section

/-!
# A complete-denominator exclusion for an alphabet-four cycle schema

Let `P = [1,1,4,1,1,1,2]` be an odd-gap word. Its affine map is
`x ↦ -41 + (2187/2048)*(x+41)`. A gap two has affine map
`x ↦ 1 + (3/4)*(x-1)`.

The cycle word `P^k [2]^k` therefore has the full periodic denominator
`8192^k-6561^k` and numerator
`8192^k-6561^k + 42*(6561^k-6144^k)`.

This file proves nondivisibility for every positive k, with an exact finite
check for k<17 and an algebraic strict interval for the entire infinite tail.
It also excludes any integer cycle satisfying the two repeated-block affine
equations. No convergence assumption or denominator-factor sieve is used.
-/

namespace CollatzFixedBlock

def denominator (k : Nat) : Nat := 8192^k-6561^k
def correction (k : Nat) : Nat := 42*(6561^k-6144^k)
def numerator (k : Nat) : Nat := denominator k+correction k

theorem denominator_pos (k : Nat) (hk : 0<k) : 0<denominator k := by
  have h := Nat.pow_lt_pow_left (by decide : 6561<8192) (by omega : k≠0)
  dsimp [denominator]
  omega

theorem correction_pos (k : Nat) (hk : 0<k) : 0<correction k := by
  have h := Nat.pow_lt_pow_left (by decide : 6144<6561) (by omega : k≠0)
  dsimp [correction]
  omega

theorem tail_power_margin (k : Nat) (hk : 17≤k) :
    43*6561^k<8192^k := by
  have base : 43*6561^17<8192^17 := by norm_num
  have rem : 6561^(k-17)≤8192^(k-17) :=
    Nat.pow_le_pow_left (by decide : 6561≤8192) (k-17)
  have pos : 0<6561^(k-17) := by positivity
  calc
    43*6561^k=(43*6561^17)*6561^(k-17) := by
      conv_lhs => rw [show k=17+(k-17) by omega, pow_add]
      ring
    _ <8192^17*6561^(k-17) := Nat.mul_lt_mul_of_pos_right base pos
    _ ≤8192^17*8192^(k-17) := Nat.mul_le_mul_left _ rem
    _ =8192^k := by rw [← pow_add, show 17+(k-17)=k by omega]

theorem tail_strict_interval (k : Nat) (hk : 17≤k) :
    denominator k<numerator k ∧ numerator k<2*denominator k := by
  have hp := correction_pos k (by omega)
  have bound := tail_power_margin k hk
  have cor : correction k≤42*6561^k :=
    Nat.mul_le_mul_left 42 (Nat.sub_le _ _)
  have deq : denominator k+6561^k=8192^k := by
    dsimp [denominator]
    omega
  have neq : numerator k=denominator k+correction k := rfl
  omega

theorem full_denominator_nondivisibility (k : Nat) (hk : 0<k) :
    ¬denominator k ∣ numerator k := by
  by_cases large : 17≤k
  · obtain ⟨lo,hi⟩ := tail_strict_interval k large
    have dp := denominator_pos k hk
    rintro ⟨q,hq⟩
    have qpos : 0<q := by
      by_contra h
      have qz : q=0 := by omega
      simp only [qz,Nat.mul_zero] at hq
      omega
    by_cases one : q=1
    · simp [one] at hq
      omega
    · have two : 2≤q := by omega
      have mul := Nat.mul_le_mul_left (denominator k) two
      omega
  · have bound : k≤16 := by omega
    have small : k=1 ∨ k=2 ∨ k=3 ∨ k=4 ∨ k=5 ∨ k=6 ∨ k=7 ∨ k=8 ∨
        k=9 ∨ k=10 ∨ k=11 ∨ k=12 ∨ k=13 ∨ k=14 ∨ k=15 ∨ k=16 := by omega
    rcases small with rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl <;>
      norm_num [denominator,numerator,correction]

theorem no_integer_cycle_equation (k n : Nat) (hk : 0<k)
    (eqn : denominator k*n=numerator k) : False := by
  exact full_denominator_nondivisibility k hk ⟨n,eqn.symm⟩

/-- These are the two complete repeated-block equations in a form with no
natural subtraction. They imply the full cycle denominator equation. -/
theorem paired_affine_equation (k n m : Nat) (hk : 0<k)
    (pin : 2048^k*(m+41)=2187^k*(n+41))
    (twos : 4^k*n+3^k=3^k*m+4^k) : denominator k*n=numerator k := by
  have p := congrArg (fun x : Nat => 3^k*x) pin
  have t := congrArg (fun x : Nat => 2048^k*x) twos
  have a : 3^k*2048^k=6144^k := by rw [← mul_pow]; norm_num
  have b : 3^k*2187^k=6561^k := by rw [← mul_pow]; norm_num
  have c : 2048^k*4^k=8192^k := by rw [← mul_pow]; norm_num
  have d : 2048^k*3^k=6144^k := by rw [← mul_pow]; norm_num
  simp only [Nat.mul_add,← Nat.mul_assoc,a,b,c,d] at p t
  have ltA := Nat.pow_lt_pow_left (by decide : 6561<8192) (by omega : k≠0)
  have ltB := Nat.pow_lt_pow_left (by decide : 6144<6561) (by omega : k≠0)
  have deq : denominator k+6561^k=8192^k := by
    dsimp [denominator]
    omega
  have ceq : correction k+42*6144^k=42*6561^k := by
    dsimp [correction]
    omega
  have eqn : denominator k*n=numerator k := by
    dsimp [numerator]
    nlinarith only [p,t,deq,ceq]
  exact eqn

theorem no_paired_affine_cycle (k n m : Nat) (hk : 0<k)
    (pin : 2048^k*(m+41)=2187^k*(n+41))
    (twos : 4^k*n+3^k=3^k*m+4^k) : False := by
  exact no_integer_cycle_equation k n hk (paired_affine_equation k n m hk pin twos)

/-- A uniform bound on every integer cycle quotient, with no parameter census. -/
theorem cycle_equation_small (k n : Nat) (hk : 0<k)
    (eqn : denominator k*n=numerator k) : n<170 := by
  have ratio : 8192*6561^k≤6561*8192^k := by
    have rem := Nat.pow_le_pow_left (by decide : 6561≤8192) (k-1)
    calc
      8192*6561^k=(8192*6561)*6561^(k-1) := by
        conv_lhs => rw [show k=1+(k-1) by omega,pow_add]
        ring
      _ ≤(8192*6561)*8192^(k-1) := Nat.mul_le_mul_left _ rem
      _ =6561*8192^k := by
        conv_rhs => rw [show k=1+(k-1) by omega,pow_add]
        ring
  have dp := denominator_pos k hk
  have ltA := Nat.pow_lt_pow_left (by decide : 6561<8192) (by omega : k≠0)
  have deq : denominator k+6561^k=8192^k := by
    dsimp [denominator]
    omega
  have cor : correction k≤42*6561^k :=
    Nat.mul_le_mul_left 42 (Nat.sub_le _ _)
  change denominator k*n=denominator k+correction k at eqn
  by_contra failure
  have lower := Nat.mul_le_mul_left (denominator k) (show 170≤n by omega)
  nlinarith only [ratio,dp,deq,cor,eqn,lower]

/-- Integrality of even the first signed-pin block requires a source at least
2007; the full repeated-block equation retains this necessary condition. -/
theorem pin_source_large (k n m : Nat) (hk : 0<k)
    (pin : 2048^k*(m+41)=2187^k*(n+41)) : 2007≤n := by
  have divpow : 2048∣2048^k := dvd_pow_self 2048 (by omega : k≠0)
  have divprod : 2048∣2187^k*(n+41) := by
    rw [← pin]
    exact dvd_mul_of_dvd_left divpow (m+41)
  have cop : Nat.Coprime 2048 (2187^k) :=
    (by decide : Nat.Coprime 2048 2187).pow_right k
  have divsource : 2048∣n+41 := cop.dvd_of_dvd_mul_left divprod
  have bound := Nat.le_of_dvd (by omega : 0<n+41) divsource
  omega

theorem no_paired_affine_cycle_uniform (k n m : Nat) (hk : 0<k)
    (pin : 2048^k*(m+41)=2187^k*(n+41))
    (twos : 4^k*n+3^k=3^k*m+4^k) : False := by
  have small := cycle_equation_small k n hk (paired_affine_equation k n m hk pin twos)
  have large := pin_source_large k n m hk pin
  omega

/-- Arithmetic gap paths retain the exact equations of ordinary odd steps.
We omit parity/positivity restrictions, so an exclusion of this larger
relation also excludes all ordinary positive paths with the supplied gaps. -/
def GapPath : List Nat → Nat → Nat → Prop
  | [], n, m => n=m
  | g::w, n, m => ∃u, 3*n+1=2^g*u ∧ GapPath w u m

def BlockPath (w : List Nat) : Nat → Nat → Nat → Prop
  | 0, n, m => n=m
  | k+1, n, m => ∃u, GapPath w n u ∧ BlockPath w k u m

def pinWord : List Nat := [1,1,4,1,1,1,2]

set_option maxHeartbeats 1000000 in
theorem pin_block_identity (n m : Nat) (h : GapPath pinWord n m) :
    2048*(m+41)=2187*(n+41) := by
  simp only [pinWord,GapPath] at h
  rcases h with ⟨n1,h1,n2,h2,n3,h3,n4,h4,n5,h5,n6,h6,n7,h7,last⟩
  norm_num at h1 h2 h3 h4 h5 h6 h7
  nlinarith only [h1,h2,h3,h4,h5,h6,h7,last]

theorem repeated_pin_identity (k n m : Nat) (h : BlockPath pinWord k n m) :
    2048^k*(m+41)=2187^k*(n+41) := by
  induction k generalizing n m with
  | zero => simpa [BlockPath] using h.symm
  | succ k ih =>
      obtain ⟨u,first,rest⟩ := h
      have edge := pin_block_identity n u first
      have tail := ih u m rest
      calc
        2048^(k+1)*(m+41)=2048*(2048^k*(m+41)) := by ring
        _ =2048*(2187^k*(u+41)) := by rw [tail]
        _ =2187^k*(2048*(u+41)) := by ring
        _ =2187^k*(2187*(n+41)) := by rw [edge]
        _ =2187^(k+1)*(n+41) := by ring

theorem repeated_twos_identity (k n m : Nat) (h : BlockPath [2] k n m) :
    4^k*m+3^k=3^k*n+4^k := by
  induction k generalizing n m with
  | zero => simpa [BlockPath] using h.symm
  | succ k ih =>
      obtain ⟨u,first,rest⟩ := h
      have edge : 3*n+1=4*u := by simpa [GapPath] using first
      have tail := ih u m rest
      have e := congrArg (fun x : Nat => 3^k*x) edge
      have t := congrArg (fun x : Nat => 4*x) tail
      simp only [pow_succ]
      nlinarith only [e,t]

/-- No integer gap cycle is a positive number of copies of the signed-pin
block followed by the same number of gap-two steps. -/
theorem no_repeated_gap_cycle (k n m : Nat) (hk : 0<k)
    (pin : BlockPath pinWord k n m) (twos : BlockPath [2] k m n) : False := by
  exact no_paired_affine_cycle k n m hk
    (repeated_pin_identity k n m pin) (repeated_twos_identity k m n twos)

/-- The same all-parameter ordinary-gap exclusion, now without using any
finite parameter check: real size and exact dyadic integrality conflict. -/
theorem no_repeated_gap_cycle_uniform (k n m : Nat) (hk : 0<k)
    (pin : BlockPath pinWord k n m) (twos : BlockPath [2] k m n) : False := by
  exact no_paired_affine_cycle_uniform k n m hk
    (repeated_pin_identity k n m pin) (repeated_twos_identity k m n twos)

#print axioms denominator_pos
#print axioms correction_pos
#print axioms tail_power_margin
#print axioms tail_strict_interval
#print axioms full_denominator_nondivisibility
#print axioms no_integer_cycle_equation
#print axioms paired_affine_equation
#print axioms no_paired_affine_cycle
#print axioms cycle_equation_small
#print axioms pin_source_large
#print axioms no_paired_affine_cycle_uniform
#print axioms pin_block_identity
#print axioms repeated_pin_identity
#print axioms repeated_twos_identity
#print axioms no_repeated_gap_cycle
#print axioms no_repeated_gap_cycle_uniform

end CollatzFixedBlock

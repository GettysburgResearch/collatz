import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.ModEq
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-! Whole-orbit kernels for the explicit interval of semigroup holes. -/

namespace Collatz.SemigroupPhysical

open Finset

/-- The full physical weighted difference has the same positive source in both branches. -/
theorem physical_step {R : Type*} [CommRing R] {x x' y y' : R}
    (edge : (2*x' = x ∧ y' = 2*y) ∨ (2*x' = 3*x+1 ∧ 3*y' = 2*y)) :
    y'*(4*x'+1)-y*(4*x+1)=y := by
  rcases edge with ⟨hx,hy⟩ | ⟨hx,hy⟩
  · rw [hy, ← hx]
    ring
  · linear_combination 2*y'*hx + (2*x+1)*hy

/-- This uses a literal closed integer trajectory reduced to a ring. -/
theorem physical_sum_zero {R : Type*} [CommRing R] {n : ℕ} (x y : ℕ → R)
    (hx : x n = x 0) (hy : y n = y 0)
    (edges : ∀ i < n, (2*x (i+1) = x i ∧ y (i+1) = 2*y i) ∨
      (2*x (i+1) = 3*x i+1 ∧ 3*y (i+1) = 2*y i)) :
    ∑ i ∈ range n, y i = 0 := by
  let f (i : ℕ) := y i*(4*x i+1)
  have go : ∀ k ≤ n, ∑ i ∈ range k, y i = f k - f 0 := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
      intro hk
      rw [sum_range_succ, ih (k.le_succ.trans hk)]
      have e := physical_step (edges k hk)
      change f (k+1)-f k = y k at e
      rw [← e]
      ring
  simpa [f, hx, hy] using go n le_rfl

def liftHeight (n l r i : ℕ) : ℕ := i + if l ≤ i ∧ i < r then n else 0

def geo {R : Type*} [CommRing R] (z : R) (k : ℕ) : R := ∑ i ∈ range k, z^i

theorem geo_diff {R : Type*} [CommRing R] (z : R) (k : ℕ) :
    (z-1)*geo z k = z^k-1 := by
  induction k with
  | zero => simp [geo]
  | succ k ih =>
    simp only [geo, sum_range_succ] at *
    rw [mul_add, ih, pow_succ]
    ring

/-- A truncated geometric sum over the interval of actual holes. -/
theorem hole_prefix {R : Type*} [CommRing R] (z : R) {n l r : ℕ}
    (hlr : l ≤ r) (_hr : r ≤ n) (k : ℕ) :
    (z-1)*(∑ i ∈ range k, z^(liftHeight n l r i)) =
      z^k-1+(z^n-1)*(z^(min k r)-z^(min k l)) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, mul_add, ih]
    by_cases h₁ : k < l
    · have h₂ : k < r := lt_of_lt_of_le h₁ hlr
      simp only [Nat.min_eq_left (Nat.le_of_lt h₁), Nat.min_eq_left (Nat.le_of_lt h₂),
        Nat.min_eq_left (Nat.succ_le_of_lt h₁), Nat.min_eq_left (Nat.succ_le_of_lt h₂), liftHeight, not_le.mpr h₁, false_and,
        ite_false, Nat.add_zero, pow_succ]
      ring
    · have h₃ := Nat.le_of_not_gt h₁
      by_cases h₂ : k < r
      · simp only [Nat.min_eq_right h₃, Nat.min_eq_right (Nat.le.step h₃),
          Nat.min_eq_left (Nat.le_of_lt h₂), Nat.min_eq_left (Nat.succ_le_of_lt h₂), liftHeight, h₃, h₂,
          and_self, ite_true, pow_add, pow_succ]
        ring
      · have h₄ := Nat.le_of_not_gt h₂
        simp only [Nat.min_eq_right h₃, Nat.min_eq_right (Nat.le.step h₃),
          Nat.min_eq_right h₄, Nat.min_eq_right (Nat.le.step h₄), liftHeight, h₂, and_false,
          ite_false, Nat.add_zero, pow_succ]
        ring

theorem physical_29 {R : Type*} [CommRing R] {z : R} {n l r : ℕ}
    (hlr : l ≤ r) (hr : r ≤ n) (hz : z^n=3)
    (hl : 8*z^l=9) (hrr : 3*z^r=4)
    (hsum : ∑ i ∈ range n, z^(liftHeight n l r i) = 0) :
    (58 : R)=0 := by
  have h := hole_prefix z hlr hr n
  rw [hsum, mul_zero, hz, min_eq_right hr, min_eq_right (hlr.trans hr)] at h
  linear_combination -24*h + 6*hl - 16*hrr

private theorem pow2_lane (k : ℕ) :
    2^(k+3)%504=8 ∨ 2^(k+3)%504=16 ∨ 2^(k+3)%504=32 ∨
    2^(k+3)%504=64 ∨ 2^(k+3)%504=128 ∨ 2^(k+3)%504=256 := by
  induction k with
  | zero => decide
  | succ k ih =>
    have ep : k+1+3=(k+3)+1 := by omega
    rw [ep, pow_succ, Nat.mul_mod]
    rcases ih with h|h|h|h|h|h <;> rw [h] <;> decide

private theorem pow3_lane (k : ℕ) :
    3^(k+2)%504=9 ∨ 3^(k+2)%504=27 ∨ 3^(k+2)%504=81 ∨
    3^(k+2)%504=243 ∨ 3^(k+2)%504=225 ∨ 3^(k+2)%504=171 := by
  induction k with
  | zero => decide
  | succ k ih =>
    have ep : k+1+2=(k+2)+1 := by omega
    rw [ep, pow_succ, Nat.mul_mod]
    rcases ih with h|h|h|h|h|h <;> rw [h] <;> decide

/-- The integral obstruction is a fixed finite modular calculation for all clocks.
It consumes 58 directly, avoiding a separate parity cancellation in ZMod. -/
theorem no_divisor_58 {n u D : ℕ} (hn : 3 ≤ n) (hu : 2 ≤ u)
    (hD : 3^u+D=2^n) (dvd : D ∣ 58) : False := by
  have hclass : D=1 ∨ D=2 ∨ D=29 ∨ D=58 := by
    have hd := Nat.le_of_dvd (by decide : 0<58) dvd
    have cert : ∀ i : Fin 59, i.val ∣ 58 → i.val=1 ∨ i.val=2 ∨ i.val=29 ∨ i.val=58 := by
      decide +kernel
    exact cert ⟨D, by omega⟩ dvd
  have h2 := pow2_lane (n-3)
  have h3 := pow3_lane (u-2)
  rw [Nat.sub_add_cancel hn] at h2
  rw [Nat.sub_add_cancel hu] at h3
  have eq := congrArg (fun a : ℕ => a%504) hD
  change (3^u+D)%504=2^n%504 at eq
  rw [Nat.add_mod] at eq
  rcases hclass with rfl|rfl|rfl|rfl <;>
    rcases h3 with h|h|h|h|h|h <;> rw [h] at eq <;> norm_num at eq <;> omega

#print axioms physical_step
#print axioms physical_sum_zero
#print axioms hole_prefix
#print axioms physical_29
#print axioms no_divisor_58

end Collatz.SemigroupPhysical

namespace Collatz.SemigroupPhysical

open Finset

theorem rank_reindex {R : Type*} [AddCommMonoid R] {n u : ℕ} (hn : 0<n)
    (cop : n.Coprime u) (f : ℕ → R) :
    ∑ i ∈ range n, f (i*u%n) = ∑ i ∈ range n, f i := by
  let m (i : Fin n) : Fin n := ⟨i.val*u%n, Nat.mod_lt _ hn⟩
  have inj : Function.Injective m := by
    intro i j h
    have h' : i.val*u ≡ j.val*u [MOD n] := congrArg Fin.val h
    have eq := Nat.ModEq.cancel_right_of_coprime cop h'
    exact Fin.ext (by simpa [Nat.ModEq, Nat.mod_eq_of_lt i.isLt, Nat.mod_eq_of_lt j.isLt] using eq)
  let e := Equiv.ofBijective m (Finite.injective_iff_bijective.mp inj)
  have eq := Equiv.sum_comp e (fun j : Fin n => f j.val)
  calc
    _ = ∑ i : Fin n, (fun k : ℕ => f (k*u%n)) i.val :=
      (Fin.sum_univ_eq_sum_range (fun k : ℕ => f (k*u%n)) n).symm
    _ = ∑ i : Fin n, f i.val := eq
    _ = _ := Fin.sum_univ_eq_sum_range f n

def height (n u l r i : ℕ) : ℕ := liftHeight n l r (i*u%n)

/-- The explicit interval is a legal binary calendar at every clock. -/
theorem height_edge {n u v l r : ℕ} (hN : n=u+v) (hU : v<u)
    (hr : r≤v) (hv : 0<v) (i : ℕ) :
    height n u l r (i+1)=height n u l r i+u ∨
    height n u l r (i+1)+n=height n u l r i+u := by
  let a := i*u%n
  have ha : a<n := Nat.mod_lt _ (by omega)
  have hi : (i+1)*u%n=(a+u)%n := by rw [Nat.succ_mul, Nat.add_mod, Nat.mod_eq_of_lt (by omega : u<n)]
  unfold height
  change liftHeight n l r ((i+1)*u%n) = liftHeight n l r a+u ∨
    liftHeight n l r ((i+1)*u%n)+n = liftHeight n l r a+u
  rw [hi]
  by_cases av : a<v
  · have small : a+u<n := by omega
    rw [Nat.mod_eq_of_lt small]
    simp only [liftHeight]
    split_ifs <;> omega
  · have wrap : n ≤ a+u := by omega
    rw [Nat.mod_eq_sub_mod wrap, Nat.mod_eq_of_lt (by omega : a+u-n<n)]
    simp only [liftHeight]
    split_ifs <;> omega

/-- The selected powers of 2 and 3 produce a root in the full modulus. -/
theorem bezout_root {G : Type*} [CommGroup G] {x y : G} {n u : ℕ}
    (cop : n.Coprime u) (hxy : x^n=y^u) : ∃ z : G, z^u=x ∧ z^n=y := by
  let a := Nat.gcdB n u
  let b := Nat.gcdA n u
  have hab : (n:ℤ)*b+(u:ℤ)*a=1 := by
    have h := Nat.gcd_eq_gcd_ab n u
    rw [show n.gcd u=1 from cop] at h
    exact h.symm
  have eq : x^(n:ℤ)=y^(u:ℤ) := by simpa using hxy
  use x^a*y^b
  constructor
  · rw [← zpow_natCast, mul_zpow, ← zpow_mul, ← zpow_mul]
    calc
      _ = x^(a*(u:ℤ))*(y^(u:ℤ))^b := by rw [← zpow_mul, mul_comm b (u:ℤ)]
      _ = x^(a*(u:ℤ))*(x^(n:ℤ))^b := by rw [← eq]
      _ = x^(a*(u:ℤ)+(n:ℤ)*b) := by rw [← zpow_mul, zpow_add]
      _ = x := by rw [show a*(u:ℤ)+(n:ℤ)*b=1 by simpa [mul_comm,a,b,add_comm] using hab, zpow_one]
  · rw [← zpow_natCast, mul_zpow, ← zpow_mul, ← zpow_mul]
    calc
      _ = (x^(n:ℤ))^a*y^(b*(n:ℤ)) := by rw [← zpow_mul, mul_comm a (n:ℤ)]
      _ = (y^(u:ℤ))^a*y^(b*(n:ℤ)) := by rw [eq]
      _ = y^((u:ℤ)*a+b*(n:ℤ)) := by rw [← zpow_mul, zpow_add]
      _ = y := by rw [show (u:ℤ)*a+b*(n:ℤ)=1 by simpa [mul_comm,a,b,add_comm] using hab, zpow_one]

theorem physical_primes {n u D : ℕ} (hn : 0<n) (hu : 0<u) (hD : 3^u+D=2^n) :
    Nat.Coprime 2 D ∧ Nat.Coprime 3 D := by
  constructor
  · apply Nat.prime_two.coprime_iff_not_dvd.mpr
    intro hd
    have htwo : 2 ∣ 2^n := dvd_pow_self 2 (by omega)
    rw [← hD] at htwo
    have h : 2 ∣ 3^u := (Nat.dvd_add_iff_left hd).mpr htwo
    exact (by decide : ¬ 2 ∣ 3) (Nat.prime_two.dvd_of_dvd_pow h)
  · apply Nat.prime_three.coprime_iff_not_dvd.mpr
    intro hd
    have hthree : 3 ∣ 3^u := dvd_pow_self 3 (by omega)
    have h : 3 ∣ 2^n := hD ▸ Nat.dvd_add hthree hd
    exact (by decide : ¬ 3 ∣ 2) (Nat.prime_three.dvd_of_dvd_pow h)

theorem specialized_root {n u D : ℕ} (hn : 0<n) (hu : 0<u) (cop : n.Coprime u)
    (hD : 3^u+D=2^n) : ∃ z : ZMod D, z^u=2 ∧ z^n=3 := by
  obtain ⟨h2,h3⟩ := physical_primes hn hu hD
  let x := ZMod.unitOfCoprime 2 h2
  let y := ZMod.unitOfCoprime 3 h3
  have hx : (x : ZMod D)=2 := ZMod.coe_unitOfCoprime 2 h2
  have hy : (y : ZMod D)=3 := ZMod.coe_unitOfCoprime 3 h3
  have eq : x^n=y^u := by
    apply Units.ext
    simpa [Units.val_pow_eq_pow_val, hx, hy, Nat.cast_add, Nat.cast_pow] using
      (congrArg (fun a : ℕ => (a : ZMod D)) hD).symm
  obtain ⟨z, hz, hz'⟩ := bezout_root cop eq
  exact ⟨z, by simpa [hx] using congrArg Units.val hz, by simpa [hy] using congrArg Units.val hz'⟩

/-- The genuine natural-valued shortcut updates along the completely specified
height calendar cannot close at the positive determinant of this family. -/
theorem no_ordinary_interval_cycle {n u v l r D : ℕ}
    (hN : n=u+v) (hL : l+u=2*v) (hR : r+v=u)
    (hl : 0<l) (hlr : l<r) (hrv : r<v) (hvu : v<u)
    (cop : n.Coprime u) (hD : 3^u+D=2^n)
    (x : ℕ → ℕ) (close : x n=x 0)
    (step : ∀ i<n, 2*x (i+1)=
      if height n u l r (i+1)=height n u l r i+u then x i else 3*x i+1) :
    False := by
  obtain ⟨z, zu, zn⟩ := specialized_root (by omega) (by omega) cop hD
  let y (i : ℕ) : ZMod D := z^(height n u l r i)
  have endy : y n=y 0 := by simp [y, height]
  have edges (i : ℕ) (hi : i<n) :
      (2*(x (i+1) : ZMod D)=x i ∧ y (i+1)=2*y i) ∨
      (2*(x (i+1) : ZMod D)=3*x i+1 ∧ 3*y (i+1)=2*y i) := by
    have path := step i hi
    rcases height_edge (l:=l) hN hvu hrv.le (by omega) i with e|e
    · left
      simp only [e, ite_true] at path
      constructor
      · simpa only [Nat.cast_mul, Nat.cast_add, Nat.cast_ofNat, Nat.cast_one] using
          congrArg (fun k : ℕ => (k : ZMod D)) path
      · simp [y,e,pow_add,zu,mul_comm]
    · right
      have diff : height n u l r (i+1)≠height n u l r i+u := by omega
      simp only [diff, ite_false] at path
      constructor
      · simpa only [Nat.cast_mul, Nat.cast_add, Nat.cast_ofNat, Nat.cast_one] using
          congrArg (fun k : ℕ => (k : ZMod D)) path
      · have e' := congrArg (fun a : ℕ => z^a) e
        simpa [y,pow_add,zu,zn,mul_comm] using e'
  have sum0 := physical_sum_zero (fun i => (x i : ZMod D)) y (by rw [close]) endy edges
  have ranks := rank_reindex (by omega : 0<n) cop (fun i => z^(liftHeight n l r i))
  have hs : ∑ i ∈ range n, z^(liftHeight n l r i)=0 := ranks ▸ sum0
  have zl : 8*z^l=9 := by
    have h : l+u*3=n*2 := by omega
    have e := congrArg (fun k : ℕ => z^k) h
    simp only [pow_add,pow_mul,zu,zn] at e
    linear_combination e
  have zr : 3*z^r=4 := by
    have h : r+n=u*2 := by omega
    have e := congrArg (fun k : ℕ => z^k) h
    simp only [pow_add,pow_mul,zu,zn] at e
    linear_combination e
  have zero58 := physical_29 hlr.le (by omega) zn zl zr hs
  exact no_divisor_58 (by omega) (by omega) hD ((ZMod.natCast_eq_zero_iff 58 D).mp zero58)

#print axioms rank_reindex
#print axioms height_edge
#print axioms bezout_root
#print axioms specialized_root
#print axioms no_ordinary_interval_cycle

end Collatz.SemigroupPhysical

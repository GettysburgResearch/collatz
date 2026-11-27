module
public import TernaryItinerary
import all TernaryItinerary
public import Mathlib.Tactic
public import Mathlib.Data.Nat.ModEq
public import Mathlib.Data.Nat.Dist
public section

namespace Collatz.Itinerary.PassageOrbit

theorem diff_le_max (x y : ℕ) : Nat.dist x y≤max x y := by
  rw [Nat.dist_eq_max_sub_min]
  exact Nat.sub_le ..

theorem dvd_diff {d x y : ℕ} : d ∣ Nat.dist x y ↔ x ≡ y [MOD d] := by
  rcases le_total x y with h|h
  · simpa [Nat.dist,Nat.sub_eq_zero_of_le h] using (Nat.modEq_iff_dvd' (n:=d) h).symm
  · rw [show Nat.dist x y=x-y by simp [Nat.dist,Nat.sub_eq_zero_of_le h]]
    exact (Nat.modEq_iff_dvd' h).symm.trans ⟨Nat.ModEq.symm,Nat.ModEq.symm⟩

theorem diff_coprime_left {x y : ℕ} (h : x.Coprime y) : (Nat.dist x y).Coprime x := by
  rcases le_total x y with le|le
  · simpa [Nat.dist,Nat.sub_eq_zero_of_le le] using (Nat.coprime_sub_self_left le).mpr h.symm
  · simpa [Nat.dist,Nat.sub_eq_zero_of_le le] using (Nat.coprime_self_sub_left le).mpr h.symm

/-- Number of odd sources in the first t shortcut steps. -/
def oddCount (a : ℕ) : ℕ → ℕ
  | 0 => 0
  | t+1 => oddCount a t + (run t a)%2

def determinant (a t : ℕ) : ℕ := Nat.dist (2^t) (3^(oddCount a t))

/-- Absolute reduced denominator of the affine fixed point of a literal prefix.
The carry version of the gcd is proved below. -/
def denominator (a t : ℕ) : ℕ :=
  determinant a t / (determinant a t).gcd (Nat.dist (run t a) a)

theorem state_succ (a t : ℕ) : run (t+1) a=step (run t a) := by
  rw [run_add]; simp [run]

theorem oddCount_increment (a t h : ℕ) :
    oddCount a t ≤ oddCount a (t+h) ∧ oddCount a (t+h) ≤ oddCount a t + h := by
  induction h with
  | zero => simp
  | succ h ih =>
    rw [Nat.add_succ, oddCount]
    have := Nat.mod_lt (run (t+h) a) (by decide : 0<2)
    omega

theorem denominator_dvd (a t : ℕ) : denominator a t ∣ determinant a t :=
  Nat.div_dvd_of_dvd (Nat.gcd_dvd_left ..)

private theorem two_three (t u : ℕ) : (2^t).Coprime (3^u) :=
  ((by decide : Nat.Coprime 2 3).pow_left t).pow_right u

theorem determinant_pos {a t : ℕ} (positive : 0<t) : 0<determinant a t := by
  have p : 2^t ≠ 3^(oddCount a t) := by
    have e : 2 ∣ 2^t := dvd_pow_self 2 (by omega)
    obtain ⟨z,hz⟩ := ((by decide : Odd 3).pow (n:=oddCount a t))
    rintro eq
    obtain ⟨w,hw⟩ := e
    omega
  unfold determinant Nat.dist
  omega

theorem denominator_pos {a t : ℕ} (h : 0<t) : 0<denominator a t := by
  have p := determinant_pos (a:=a) h
  unfold denominator
  exact Nat.div_pos (Nat.le_of_dvd p (Nat.gcd_dvd_left ..)) (Nat.gcd_pos_of_pos_left _ p)

/-- A common divisor of two raw determinants divides the determinant of
the intervening word. -/
theorem common_divisor_dvd_gap {a t h g : ℕ} (d₁ : g ∣ determinant a t)
    (d₂ : g ∣ determinant a (t+h)) : g ∣
      Nat.dist (2^h) (3^(oddCount a (t+h)-oddCount a t)) := by
  have m₁ := dvd_diff.mp d₁
  have m₂ := dvd_diff.mp d₂
  have c : g.Coprime (2^t) := (diff_coprime_left (two_three t (oddCount a t))).of_dvd_left d₁
  have eq : 3^(oddCount a (t+h)) =
      3^(oddCount a t)*3^(oddCount a (t+h)-oddCount a t) := by
    rw [←pow_add, Nat.add_sub_of_le (oddCount_increment a t h).1]
  change 2^(t+h) ≡ 3^(oddCount a (t+h)) [MOD g] at m₂
  rw [pow_add,eq] at m₂
  apply dvd_diff.mpr
  exact (m₂.trans (m₁.mul_right _).symm).cancel_left_of_coprime c

/-- Two actual reduced denominators have only a bounded common factor.
More precisely it divides the determinant over the intervening word. -/
theorem common_factor_dvd {a t h : ℕ} :
    (denominator a t).gcd (denominator a (t+h)) ∣
      Nat.dist (2^h) (3^(oddCount a (t+h)-oddCount a t)) := by
  exact common_divisor_dvd_gap ((Nat.gcd_dvd_left ..).trans (denominator_dvd ..))
    ((Nat.gcd_dvd_right ..).trans (denominator_dvd ..))

theorem common_divisor_le {a t h g : ℕ} (hh : 0<h) (d₁ : g ∣ determinant a t)
    (d₂ : g ∣ determinant a (t+h)) : g≤3^h := by
  have delta := oddCount_increment a t h
  let v := oddCount a (t+h)-oddCount a t
  have hv : v≤h := by dsimp [v]; omega
  have p : 0<Nat.dist (2^h) (3^v) := by
    have e : 2 ∣ 2^h := dvd_pow_self 2 (by omega)
    have o : Odd (3^v) := (by decide : Odd 3).pow
    obtain ⟨z,hz⟩ := o
    obtain ⟨w,hw⟩ := e
    have ne : 2^h ≠ 3^v := by omega
    unfold Nat.dist; omega
  have bound := Nat.le_of_dvd p (common_divisor_dvd_gap d₁ d₂)
  have x : 2^h≤3^h := Nat.pow_le_pow_left (by decide) h
  have y : 3^v≤3^h := Nat.pow_le_pow_right (by decide) hv
  change _ ≤ Nat.dist (2^h) (3^v) at bound
  exact bound.trans ((diff_le_max _ _).trans (max_le x y))

theorem common_factor_le {a t h : ℕ} (hh : 0<h) :
    (denominator a t).gcd (denominator a (t+h)) ≤ 3^h :=
  common_divisor_le hh ((Nat.gcd_dvd_left ..).trans (denominator_dvd ..))
    ((Nat.gcd_dvd_right ..).trans (denominator_dvd ..))

theorem adjacent_determinants_coprime (a t : ℕ) :
    (determinant a t).Coprime (determinant a (t+1)) := by
  have d := common_divisor_dvd_gap (Nat.gcd_dvd_left (determinant a t) (determinant a (t+1)))
    (Nat.gcd_dvd_right ..)
  let v := oddCount a (t+1)-oddCount a t
  have h := oddCount_increment a t 1
  have cap : v≤1 := by dsimp [v]; omega
  change _ ∣ Nat.dist (2^1) (3^v) at d
  have eq : Nat.dist (2^1) (3^v)=1 := by interval_cases v <;> decide
  rw [eq] at d
  exact Nat.eq_one_of_dvd_one d

/-- A factor larger than the whole gap bound is absent from every other
raw determinant in that neighborhood. -/
theorem large_factor_private {a t s J p : ℕ} (near₁ : t≤s+J) (near₂ : s≤t+J)
    (large : 3^J<p) (x : p ∣ denominator a t) (y : p ∣ determinant a s) : t=s := by
  have raw := x.trans (denominator_dvd ..)
  by_contra ne
  rcases lt_or_gt_of_ne ne with h|h
  · have d : p ∣ determinant a (t+(s-t)) := by rwa [Nat.add_sub_of_le h.le]
    have b := common_divisor_le (by omega : 0<s-t) raw d
    exact (Nat.not_le_of_gt large) (b.trans (Nat.pow_le_pow_right (by decide) (by omega)))
  · have d : p ∣ determinant a (s+(t-s)) := by rwa [Nat.add_sub_of_le h.le]
    have b := common_divisor_le (by omega : 0<t-s) y d
    exact (Nat.not_le_of_gt large) (b.trans (Nat.pow_le_pow_right (by decide) (by omega)))

/-- Every divisor of the determinant divides the affine carry exactly when
it divides the difference between the endpoint and source. -/
theorem carry_criterion {a t C b : ℕ}
    (edge : 2^t*run t a=3^(oddCount a t)*a+C) (bd : b ∣ determinant a t) :
    b ∣ C ↔ b ∣ Nat.dist (run t a) a := by
  have modClock := dvd_diff.mp bd
  have cop : b.Coprime (2^t) :=
    (diff_coprime_left (two_three t (oddCount a t))).of_dvd_left bd
  rw [dvd_diff]
  constructor
  · intro bc
    have hc : C ≡ 0 [MOD b] := Nat.modEq_zero_iff_dvd.mpr bc
    have h := (modClock.mul_right a).symm
    apply Nat.ModEq.cancel_left_of_coprime cop
    rw [edge]
    simpa using h.add hc
  · intro ha
    have h := (ha.mul_left (2^t)).trans (modClock.mul_right a)
    rw [edge] at h
    have hh : C ≡ 0 [MOD b] := by
      apply Nat.ModEq.add_left_cancel' (3^(oddCount a t)*a)
      simpa using h
    exact Nat.modEq_zero_iff_dvd.mp hh

theorem carry_gcd {a t C : ℕ}
    (edge : 2^t*run t a=3^(oddCount a t)*a+C) :
    (determinant a t).gcd C = (determinant a t).gcd (Nat.dist (run t a) a) := by
  apply Nat.dvd_antisymm
  · apply Nat.dvd_gcd (Nat.gcd_dvd_left ..)
    exact (carry_criterion edge (Nat.gcd_dvd_left ..)).mp (Nat.gcd_dvd_right ..)
  · apply Nat.dvd_gcd (Nat.gcd_dvd_left ..)
    exact (carry_criterion edge (Nat.gcd_dvd_left ..)).mpr (Nat.gcd_dvd_right ..)

end Collatz.Itinerary.PassageOrbit

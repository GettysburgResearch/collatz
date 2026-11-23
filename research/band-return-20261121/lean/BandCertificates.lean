import SectionDynamics
import BandCore

/-!
Certified stopping prefixes for the actual marked section.

The affine cylinder and lower-bound lemmas use the credited compatibility
extraction in `BandCore`. The explicit orbit bridge below connects its
source-first convention with PR173's clock-first convention. No convergence certificate for a varying offset is
assumed to fit inside its dyadic depth.
-/

namespace CollatzBandCertificates

open CollatzShell CollatzShell.ForwardSection

theorem core_orbit_eq_shell (n t : Nat) :
    CollatzBandCore.orbit n t = CollatzShell.orbit t n := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact ih (CollatzShell.step n)

/-- An actual stopping prefix necessarily has a contracting affine slope. -/
theorem stopping_prefix_multiplier {a t : Nat} (drop : orbit t a < a) :
    3^(CollatzBandCore.oddCount a t) < 2^t := by
  have lower : 3^(CollatzBandCore.oddCount a t)*a ≤ 2^t*orbit t a := by
    simpa only [core_orbit_eq_shell] using CollatzBandCore.orbit_linear_lower a t
  have strict : 3^(CollatzBandCore.oddCount a t)*a < 2^t*a :=
    lower.trans_lt (Nat.mul_lt_mul_of_pos_left drop (by positivity))
  exact Nat.lt_of_mul_lt_mul_right strict

/-- One checked stopping prefix certifies its entire binary cylinder. -/
theorem stopping_prefix_cylinder {a t : Nat} (drop : orbit t a < a) (q : Nat) :
    orbit t (a+2^t*q) < a+2^t*q := by
  have image : orbit t (a+2^t*q) = orbit t a+3^(CollatzBandCore.oddCount a t)*q := by
    simpa only [core_orbit_eq_shell] using (CollatzBandCore.high_bit_lift a t q).1
  rw [image]
  exact Nat.add_lt_add_of_lt_of_le drop
    (Nat.mul_le_mul_right q (stopping_prefix_multiplier drop).le)

/-- The offset's stopping prefix is sufficient; a complete hit-to-one
certificate for the offset is unnecessary. Its clock must fit the depth. -/
theorem dyadic_offset_descent {a t d : Nat} (drop : orbit t a < a) (td : t ≤ d) :
    orbit t (2^d+a) < 2^d+a := by
  have split : a+2^t*2^(d-t) = 2^d+a := by
    rw [← Nat.pow_add, show t+(d-t)=d by omega, Nat.add_comm]
  simpa only [split] using stopping_prefix_cylinder drop (2^(d-t))

theorem certified_offset_endpoint {a t d : Nat} (hit : orbit t a = 1) (td : t ≤ d) :
    orbit t (2^d+a) = 1+3^(CollatzBandCore.oddCount a t)*2^(d-t) := by
  have image := (CollatzBandCore.high_bit_lift a t (2^(d-t))).1
  rw [core_orbit_eq_shell, core_orbit_eq_shell, hit] at image
  have split : a+2^t*2^(d-t) = 2^d+a := by
    rw [← Nat.pow_add, show t+(d-t)=d by omega, Nat.add_comm]
  simpa only [split] using image

theorem certified_offset_descent {a t d : Nat} (ha : 1 < a)
    (hit : orbit t a = 1) (td : t ≤ d) : orbit t (2^d+a) < 2^d+a := by
  have drop : orbit t a<a := by rw [hit]; exact ha
  exact dyadic_offset_descent drop td

private theorem quadratic_below_binary (d : Nat) : d*(d+1) ≤ 2^(d+1) := by
  induction d with
  | zero => decide
  | succ d ih =>
    by_cases hd : d=0
    · subst d; decide
    by_cases ho : d=1
    · subst d; decide
    calc
      (d+1)*(d+1+1) ≤ (d+1)*(2*d) := Nat.mul_le_mul_left (d+1) (by omega)
      _ = 2*(d*(d+1)) := by ring
      _ ≤ 2*2^(d+1) := Nat.mul_le_mul_left 2 ih
      _ = 2^(d+1+1) := by rw [Nat.pow_succ]; ring

/-- Every fixed odd offset eventually lies inside the shrinking marked band.
The explicit sufficient threshold `a ≤ d` avoids an asymptotic assumption. -/
theorem marked_of_odd_offset_le_depth {a d : Nat} (odd : a%2=1) (ad : a ≤ d) :
    Marked (2^d+a) := by
  have dp : 0 < d := by omega
  have ap : a < 2^d := ad.trans_lt (Nat.lt_two_pow_self)
  have low : 2^d ≤ 2^d+a := by omega
  have high : 2^d+a < 2^(d+1) := by rw [Nat.pow_succ]; omega
  have positive : 0 < 2^d+a := by positivity
  have ld : (2^d+a).log2 = d := by
    have hl := (Nat.le_log2 positive.ne').mpr low
    have hu := (Nat.log2_lt positive.ne').mpr high
    omega
  have even : (2^d)%2=0 := by
    obtain ⟨e,rfl⟩ := Nat.exists_eq_succ_of_ne_zero dp.ne'
    rw [Nat.pow_succ]
    omega
  refine ⟨by omega, ?_⟩
  unfold InSection
  rw [ld, Nat.add_sub_cancel_left]
  have one := Nat.mul_le_mul_left (d+1) ad
  have two := quadratic_below_binary d
  rw [Nat.pow_succ] at two
  nlinarith

/-- A certified odd offset gives an unbounded family of genuinely marked
starts with actual strict stopping certificates. -/
theorem unbounded_marked_certified_offsets {a t : Nat} (odd : a%2=1)
    (ha : 1<a) (hit : orbit t a=1) (B : Nat) :
    ∃ n, B<n ∧ Marked n ∧ orbit t n<n := by
  let d := a+t+B
  have ad : a≤d := by dsimp [d]; omega
  have td : t≤d := by dsimp [d]; omega
  have Bd : B≤d := by dsimp [d]; omega
  refine ⟨2^d+a, ?_, marked_of_odd_offset_le_depth odd ad,
    certified_offset_descent ha hit td⟩
  have power : d<2^d := Nat.lt_two_pow_self
  omega

private theorem orbit_positive {n : Nat} (hn : 0<n) (t : Nat) : 0<orbit t n := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih =>
    apply ih
    unfold step
    split <;> omega

/-- This is the legitimate ordinary least-counterexample use of a stopping
certificate. The ordinary floor is an explicit hypothesis, not inferred
from a clock-weighted rank or from membership in the marked section. -/
theorem basin_of_offset_stopping_floor {a t d : Nat}
    (drop : orbit t a<a) (td : t≤d)
    (floor : ∀ m, 0<m → m<2^d+a → Basin m) : Basin (2^d+a) := by
  have stop := dyadic_offset_descent drop td
  have positive : 0<orbit t (2^d+a) := orbit_positive (by positivity) t
  exact Hits.trans (y := orbit t (2^d+a)) ⟨t,rfl⟩ (floor _ positive stop)

end CollatzBandCertificates

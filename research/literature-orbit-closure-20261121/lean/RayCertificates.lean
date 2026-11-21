module

public import OffsetDescent

@[expose] public section

/-!
An exact certificate kernel for infinite arithmetic-progressions of smaller
ordinary Collatz partners. Every field is checked by a finite decidable
predicate; `ray_certificate_sound` then proves the ordinary merger for every
nonnegative progression parameter. No global coverage premise is asserted.
-/

namespace CollatzShell.RayCertificates

open OffsetDescent

structure Row where
  source : Nat
  partner : Nat
  increment : Nat
  partnerClock : Nat
  deriving DecidableEq, Repr

def Valid (modulus sourceClock : Nat) (r : Row) : Prop :=
  0 < r.partner ∧ r.partner < r.source ∧ r.source < modulus ∧
  0 < r.increment ∧ r.increment < modulus ∧
  2 ^ sourceClock ∣ modulus ∧ 2 ^ r.partnerClock ∣ r.increment ∧
  orbit r.partnerClock r.partner = orbit sourceClock r.source ∧
  3 ^ oddCount sourceClock r.source * (modulus / 2 ^ sourceClock) =
    3 ^ oddCount r.partnerClock r.partner * (r.increment / 2 ^ r.partnerClock)

instance (M h : Nat) (r : Row) : Decidable (Valid M h r) := by
  unfold Valid
  infer_instance

theorem ray_certificate_sound (M h : Nat) (r : Row) (valid : Valid M h r)
    (z : Nat) :
    0 < r.partner + r.increment * z ∧
    r.partner + r.increment * z < r.source + M * z ∧
    orbit r.partnerClock (r.partner + r.increment * z) =
      orbit h (r.source + M * z) := by
  obtain ⟨positive, smaller, _source_bound, _increment_positive,
    slope_smaller, source_div, partner_div, endpoint, slope⟩ := valid
  have source_factor : 2 ^ h * (M / 2 ^ h) = M := by
    exact Nat.mul_div_cancel' source_div
  have partner_factor : 2 ^ r.partnerClock *
      (r.increment / 2 ^ r.partnerClock) = r.increment := by
    exact Nat.mul_div_cancel' partner_div
  have source_ray : r.source + M * z =
      2 ^ h * ((M / 2 ^ h) * z) + r.source := by
    rw [← Nat.mul_assoc, source_factor]
    omega
  have partner_ray : r.partner + r.increment * z =
      2 ^ r.partnerClock * ((r.increment / 2 ^ r.partnerClock) * z) +
        r.partner := by
    rw [← Nat.mul_assoc, partner_factor]
    omega
  refine ⟨by omega, ?_, ?_⟩
  · have monotone := Nat.mul_le_mul_right z (Nat.le_of_lt slope_smaller)
    omega
  · rw [source_ray, partner_ray, orbit_shift, orbit_shift, endpoint]
    simpa only [← Nat.mul_assoc] using congrArg
      (fun s => s * z + orbit h r.source) slope.symm

theorem basin_of_valid_ray (M h : Nat) (r : Row) (valid : Valid M h r)
    (z : Nat) (smaller : ∀ m, 0 < m → m < r.source + M * z → Basin m) :
    Basin (r.source + M * z) := by
  obtain ⟨positive, less, merge⟩ := ray_certificate_sound M h r valid z
  have partner_basin := smaller _ positive less
  have endpoint_basin : Basin (orbit r.partnerClock
      (r.partner + r.increment * z)) :=
    (basin_at_hit (show Hits (r.partner + r.increment * z)
      (orbit r.partnerClock (r.partner + r.increment * z)) from
      ⟨r.partnerClock, rfl⟩)).mp partner_basin
  rw [merge] at endpoint_basin
  exact (basin_at_hit (show Hits (r.source + M * z)
    (orbit h (r.source + M * z)) from ⟨h, rfl⟩)).mpr endpoint_basin

#print axioms ray_certificate_sound
#print axioms basin_of_valid_ray

end CollatzShell.RayCertificates

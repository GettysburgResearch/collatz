import MarkedDensityPotential

/-!
Finite ordinary arithmetic behind the strict clock decrease of the
forward/first-contact reset. The contact theorem and the countable
stationarity argument remain explicit written inputs in CONTACT_CLOCK.md.
-/

namespace CollatzShell.ContactClock

open ForwardSection InverseDensityPotential

set_option maxRecDepth 20000 in
set_option maxHeartbeats 4000000 in
/-- Every unit residue modulo 81 has a positive exponent at most 54
whose product with that residue is 52. This finite certificate is checked
by kernel reduction, with no primality or generator claim assumed. -/
theorem unit_residue_cover :
    ∀ r : Fin 81, r.val % 3 ≠ 0 →
      ∃ e : Fin 55, 0 < e.val ∧ (2^e.val * r.val) % 81 = 52 := by
  decide

theorem unit_exponent (q : Nat) (hq : q % 3 ≠ 0) :
    ∃ e : Nat, 0 < e ∧ e ≤ 54 ∧ (2^e * q) % 81 = 52 := by
  let r : Fin 81 := ⟨q % 81, Nat.mod_lt q (by decide)⟩
  have hr : r.val % 3 ≠ 0 := by
    change (q % 81) % 3 ≠ 0
    rw [Nat.mod_mod_of_dvd q (by decide : 3 ∣ 81)]
    exact hq
  obtain ⟨e, he, hit⟩ := unit_residue_cover r hr
  refine ⟨e.val, he, by omega, ?_⟩
  change (2^e.val * (q % 81)) % 81 = 52 at hit
  simpa only [Nat.mul_mod, Nat.mod_mod] using hit

/-- A positive odd unit target has an actual unit parent in the
17-mod-27 class. The displayed equation preserves its exact odd clock. -/
theorem noncontact_parent_ladder (q : Nat) (hq : OddUnit q) :
    ∃ s e : Nat, 0 < e ∧ e ≤ 54 ∧
      3*(54*s+17)+1 = 2^e*q ∧ oddStep (54*s+17) = q := by
  obtain ⟨e, he, bound, hit⟩ := unit_exponent q hq.2.2
  have even : (2^e*q) % 2 = 0 := by
    obtain ⟨t, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt he)
    simp [pow_succ, Nat.mul_mod]
  let s := (2^e*q) / 162
  have eqn : 3*(54*s+17)+1 = 2^e*q := by
    dsimp [s]
    omega
  refine ⟨s, e, he, bound, eqn, ?_⟩
  change ordCompl[2] (3*(54*s+17)+1) = q
  rw [eqn]
  exact Nat.ordCompl_pow_mul_of_not_dvd e Nat.prime_two (by
    rcases hq with ⟨_, odd, _⟩
    omega)

/-- The chosen parent has two genuine gap-one odd-unit predecessors. -/
theorem two_gap_one_predecessors (s : Nat) :
    OddUnit (24*s+7) ∧ OddUnit (36*s+11) ∧ OddUnit (54*s+17) ∧
      oddStep (24*s+7) = 36*s+11 ∧
      oddStep (36*s+11) = 54*s+17 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · unfold OddUnit
    omega
  · unfold OddUnit
    omega
  · unfold OddUnit
    omega
  · change ordCompl[2] (3*(24*s+7)+1) = 36*s+11
    rw [show 3*(24*s+7)+1 = 2^1*(36*s+11) by ring]
    exact Nat.ordCompl_pow_mul_of_not_dvd 1 Nat.prime_two (by omega)
  · change ordCompl[2] (3*(36*s+11)+1) = 54*s+17
    rw [show 3*(36*s+11)+1 = 2^1*(54*s+17) by ring]
    exact Nat.ordCompl_pow_mul_of_not_dvd 1 Nat.prime_two (by omega)

theorem parent_above_contact (V : Nat → ℝ) (s : Nat)
    (floor : 1 ≤ V (24*s+7))
    (firstEdge : 3*V (24*s+7) ≤ 2*V (36*s+11))
    (secondEdge : 3*V (36*s+11) ≤ 2*V (54*s+17)) :
    (9 : ℝ)/4 ≤ V (54*s+17) ∧ 2 < V (54*s+17) := by
  constructor <;> linarith

#print axioms unit_residue_cover
#print axioms unit_exponent
#print axioms noncontact_parent_ladder
#print axioms two_gap_one_predecessors
#print axioms parent_above_contact

end CollatzShell.ContactClock

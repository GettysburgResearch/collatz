import Closure.PsiDescent

open CollatzReverseBasin CollatzClosure PsiDescent

namespace PsiCharged

/-- The actual ordinary cylinder from the expanding balanced return. -/
def ExpansionStep (m q : Nat) : Prop :=
  ∃ t : Nat, m = 2469887 + 4194304*t ∧ q = 2816534 + 4782969*t

/-- A finite consecutive run of that same guarded return. -/
inductive ExpansionChain : Nat → Nat → Nat → Prop
  | nil (m : Nat) : ExpansionChain 0 m m
  | cons {k m n q : Nat} :
      ExpansionStep m n → ExpansionChain k n q → ExpansionChain (k+1) m q

/-- Positive affine potential centered at the rational fixed point of the return. -/
def expansionCharge (m : Nat) : Nat := 588665*m + 6867833

theorem expansion_step_profile {m q : Nat} (h : ExpansionStep m q) :
    orbit 22 m = q ∧ orbit 22 (3*m-1) = 3*q-1 ∧
    oddCount 22 m = 14 ∧ oddCount 22 (3*m-1) = 14 ∧ m < q := by
  obtain ⟨t, rfl, rfl⟩ := h
  exact expanding_return t

theorem expansion_step_affine {m q : Nat} (h : ExpansionStep m q) :
    4194304*q = 4782969*m + 6867833 := by
  obtain ⟨t, rfl, rfl⟩ := h
  omega

/-- Each expansion divides the binary part of this positive charge by 2^22. -/
theorem expansion_step_charge {m q : Nat} (h : ExpansionStep m q) :
    4194304*expansionCharge q = 4782969*expansionCharge m := by
  have ha := expansion_step_affine h
  unfold expansionCharge
  omega

theorem expansion_step_height {m q : Nat} (h : ExpansionStep m q) :
    3*(q+12) ≤ 4*(m+12) := by
  have ha := expansion_step_affine h
  omega

theorem expansion_chain_profile {k m q : Nat} (h : ExpansionChain k m q) :
    orbit (22*k) m = q ∧ orbit (22*k) (3*m-1) = 3*q-1 ∧
    oddCount (22*k) m = 14*k ∧ oddCount (22*k) (3*m-1) = 14*k := by
  induction h with
  | nil m => simp [orbit, oddCount]
  | @cons k m n q hs hc ih =>
    have s := expansion_step_profile hs
    have clock : 22*(k+1) = 22+22*k := by omega
    rw [clock, orbit_add, orbit_add, oddCount_add, oddCount_add,
      s.1, s.2.1, s.2.2.1, s.2.2.2.1, ih.1, ih.2.1, ih.2.2.1, ih.2.2.2]
    omega

theorem expansion_chain_charge {k m q : Nat} (h : ExpansionChain k m q) :
    4194304^k*expansionCharge q = 4782969^k*expansionCharge m := by
  induction h with
  | nil m => simp
  | @cons k m n q hs hc ih =>
    have s := expansion_step_charge hs
    calc
      4194304^(k+1)*expansionCharge q =
          4194304*(4194304^k*expansionCharge q) := by grind
      _ = 4194304*(4782969^k*expansionCharge n) := by rw [ih]
      _ = 4782969^k*(4194304*expansionCharge n) := by grind
      _ = 4782969^k*(4782969*expansionCharge m) := by rw [s]
      _ = 4782969^(k+1)*expansionCharge m := by grind

/-- A fixed positive ordinary source has a finite, explicit binary expansion budget. -/
theorem expansion_chain_divisibility {k m q : Nat} (h : ExpansionChain k m q) :
    4194304^k ∣ expansionCharge m := by
  have eqn := expansion_chain_charge h
  have hd : 4194304^k ∣ 4782969^k*expansionCharge m :=
    ⟨expansionCharge q, eqn.symm⟩
  have cop : Nat.gcd (4194304^k) (4782969^k) = 1 :=
    Nat.pow_gcd_pow_of_gcd_eq_one (by decide)
  have hg := Nat.dvd_gcd_mul_iff_dvd_mul.mpr hd
  simpa [cop] using hg

theorem expansion_chain_budget {k m q : Nat} (h : ExpansionChain k m q) :
    4194304^k ≤ expansionCharge m := by
  exact Nat.le_of_dvd (by unfold expansionCharge; omega)
    (expansion_chain_divisibility h)

theorem no_unbounded_expansion (m : Nat) :
    ¬ (∀ k : Nat, ∃ q : Nat, ExpansionChain k m q) := by
  intro h
  obtain ⟨q, hq⟩ := h (expansionCharge m)
  have hb := expansion_chain_budget hq
  have hp : expansionCharge m < 4194304^(expansionCharge m) :=
    Nat.lt_pow_self (by decide)
  omega

theorem expansion_chain_height {k m q : Nat} (h : ExpansionChain k m q) :
    3^k*(q+12) ≤ 4^k*(m+12) := by
  induction h with
  | nil m => simp
  | @cons k m n q hs hc ih =>
    have s := expansion_step_height hs
    calc
      3^(k+1)*(q+12) = 3*(3^k*(q+12)) := by grind
      _ ≤ 3*(4^k*(n+12)) := Nat.mul_le_mul_left 3 ih
      _ = 4^k*(3*(n+12)) := by grind
      _ ≤ 4^k*(4*(m+12)) := Nat.mul_le_mul_left (4^k) s
      _ = 4^(k+1)*(m+12) := by grind

theorem power_ratio (k r : Nat) (hkr : k ≤ r) :
    3^r*4^k ≤ 4^r*3^k := by
  have e : r = k+(r-k) := by omega
  have h := Nat.mul_le_mul_left (3^k*4^k) (pow_three_le_four (r-k))
  have e3 : 3^r = 3^k*3^(r-k) := by
    calc
      3^r = 3^(k+(r-k)) := congrArg (fun n : Nat => 3^n) e
      _ = 3^k*3^(r-k) := Nat.pow_add _ _ _
  have e4 : 4^r = 4^k*4^(r-k) := by
    calc
      4^r = 4^(k+(r-k)) := congrArg (fun n : Nat => 4^n) e
      _ = 4^k*4^(r-k) := Nat.pow_add _ _ _
  calc
    3^r*4^k = (3^k*4^k)*3^(r-k) := by
      rw [e3]
      grind
    _ ≤ (3^k*4^k)*4^(r-k) := h
    _ = 4^r*3^k := by
      rw [e4]
      grind

theorem paid_height {k r m q : Nat} (h : ExpansionChain k m q) (hkr : k ≤ r) :
    3^r*(q+12) ≤ 4^r*(m+12) := by
  have hh := expansion_chain_height h
  have hp := power_ratio k r hkr
  have hm : 3^k*(3^r*(q+12)) ≤ 3^k*(4^r*(m+12)) := by
    calc
      3^k*(3^r*(q+12)) = 3^r*(3^k*(q+12)) := by grind
      _ ≤ 3^r*(4^k*(m+12)) := Nat.mul_le_mul_left (3^r) hh
      _ = (3^r*4^k)*(m+12) := by grind
      _ ≤ (4^r*3^k)*(m+12) := Nat.mul_le_mul_right (m+12) hp
      _ = 3^k*(4^r*(m+12)) := by grind
  exact Nat.le_of_mul_le_mul_left hm (Nat.pow_pos (by decide))

/-- A long enough even-valuation exit repays any finite run of expanding blocks. -/
theorem charged_exit_bound {k r v m q u : Nat}
    (h : ExpansionChain k m q) (hkr : k ≤ r)
    (hq : 3*q = 4^(r+1)*v+2) (hu : 2*u = 3^r*v+1) :
    8*u ≤ 3*m+40 := by
  have hh := paid_height h hkr
  have eqn : 4^r*(8*u)+2*3^r = 3*(3^r*q)+4*4^r := by
    have e1 := congrArg (fun n : Nat => 3^r*n) hq
    have e2 := congrArg (fun n : Nat => 4*4^r*n) hu
    simp only [Nat.pow_succ] at e1
    grind
  have liftq : 3^r*q ≤ 3^r*(q+12) :=
    Nat.mul_le_mul_left (3^r) (by omega)
  have hm : 4^r*(8*u) ≤ 4^r*(3*m+40) := by
    calc
      4^r*(8*u) ≤ 3*(3^r*q)+4*4^r := by omega
      _ ≤ 3*(3^r*(q+12))+4*4^r :=
        Nat.add_le_add_right (Nat.mul_le_mul_left 3 liftq) (4*4^r)
      _ ≤ 3*(4^r*(m+12))+4*4^r :=
        Nat.add_le_add_right (Nat.mul_le_mul_left 3 hh) (4*4^r)
      _ = 4^r*(3*m+40) := by grind
  exact Nat.le_of_mul_le_mul_left hm (Nat.pow_pos (by decide))

/-- Actual composed trajectories, equal odd counts, and a strict ordinary descent. -/
theorem charged_paired_descent {k r v m q u : Nat}
    (h : ExpansionChain k m q) (hkr : k ≤ r) (hm : 9 ≤ m)
    (hq : 3*q = 4^(r+1)*v+2) (hu : 2*u = 3^r*v+1) :
    orbit (22*k+(2*r+3)) m = u ∧
    orbit (22*k+(2*r+3)) (3*m-1) = 3*u-1 ∧
    oddCount (22*k+(2*r+3)) m = 14*k+r+1 ∧
    oddCount (22*k+(2*r+3)) (3*m-1) = 14*k+r+1 ∧
    0 < u ∧ u < m := by
  have run := expansion_chain_profile h
  have finish := paired_descent r v q u hq hu
  have bound := charged_exit_bound h hkr hq hu
  rw [orbit_add (22*k) (2*r+3) m, orbit_add (22*k) (2*r+3) (3*m-1),
    oddCount_add (22*k) (2*r+3) m, oddCount_add (22*k) (2*r+3) (3*m-1), run.1, run.2.1,
    run.2.2.1, run.2.2.2, finish.1, finish.2.1, finish.2.2.1, finish.2.2.2.1]
  exact ⟨rfl, rfl, by omega, by omega, finish.2.2.2.2.1, by omega⟩

/-- A reverse-closure failure survives the complete paid itinerary at a smaller base. -/
theorem charged_failure_descends {k r v m q u : Nat}
    (h : ExpansionChain k m q) (hkr : k ≤ r) (hm : 9 ≤ m)
    (hq : 3*q = 4^(r+1)*v+2) (hu : 2*u = 3^r*v+1) :
    0 < u ∧ u < m ∧ (Fail 3 1 m ↔ Fail 3 1 u) := by
  have hp := charged_paired_descent h hkr hm hq hu
  have hs := basin_orbit (22*k+(2*r+3)) m
  have ht := basin_orbit (22*k+(2*r+3)) (3*m-1)
  rw [hp.1] at hs
  rw [hp.2.1] at ht
  refine ⟨hp.2.2.2.2.1, hp.2.2.2.2.2, ?_⟩
  unfold Fail
  exact ⟨fun hf => ⟨fun hu => hf.1 (hs.mp hu), ht.mpr hf.2⟩,
         fun hf => ⟨fun hm => hf.1 (hs.mpr hm), ht.mp hf.2⟩⟩

/-- The expanding counterexample is repaid on a whole 29-clock cylinder. -/
theorem repaid_expanding_cylinder (t : Nat) :
    orbit 29 (2469887+536870912*t) = 594113+129140163*t ∧
    orbit 29 (3*(2469887+536870912*t)-1) = 3*(594113+129140163*t)-1 ∧
    oddCount 29 (2469887+536870912*t) = 17 ∧
    oddCount 29 (3*(2469887+536870912*t)-1) = 17 ∧
    0 < 594113+129140163*t ∧
    594113+129140163*t < 2469887+536870912*t := by
  have hrun : ExpansionChain 1 (2469887+536870912*t) (2816534+612220032*t) := by
    apply ExpansionChain.cons (n := 2816534+612220032*t)
    · exact ⟨128*t, by omega, by omega⟩
    · exact ExpansionChain.nil _
  have h := charged_paired_descent (r := 2) (v := 132025+28697814*t)
    (u := 594113+129140163*t) hrun (by decide) (by omega) (by omega) (by omega)
  simpa using h

#print axioms expansion_chain_budget
#print axioms no_unbounded_expansion
#print axioms charged_exit_bound
#print axioms charged_paired_descent
#print axioms charged_failure_descends
#print axioms repaid_expanding_cylinder

end PsiCharged

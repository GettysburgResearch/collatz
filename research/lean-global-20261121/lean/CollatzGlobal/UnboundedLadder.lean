import CollatzGlobal.AdaptiveDescent

/-! Universal clocked transport for the valuation-two ladder. The underlying
unbounded family is credited to PR166; this module proves its actual ordinary
orbits and equal odd counts in the kernel, for every ladder length. -/

open CollatzReverseBasin CollatzClosure

namespace CollatzGlobal

theorem two_step_four (n : Nat) :
    orbit (4*n+1) 2 = 3*n+1 ∧ oddCount (4*n+1) 2 = 1 := by
  have h1 : shortcut (4*n+1) = 6*n+2 := by
    unfold shortcut
    split <;> omega
  have h2 : shortcut (6*n+2) = 3*n+1 := by
    unfold shortcut
    split <;> omega
  simp [orbit, oddCount, h1, h2, Nat.add_mod, Nat.mul_mod]

/-- All members of the exponent-parametrized source ladder, with exact clock
and count. This is induction on an unrestricted exponent. -/
theorem four_ladder (n r : Nat) :
    orbit (4^r*n+1) (2*r) = 3^r*n+1 ∧ oddCount (4^r*n+1) (2*r) = r := by
  induction r generalizing n with
  | zero => simp [orbit, oddCount]
  | succ r ih =>
    have start : 4^(r+1)*n+1 = 4*(4^r*n)+1 := by grind
    have mid : 3*(4^r*n)+1 = 4^r*(3*n)+1 := by grind
    have clock : 2*(r+1) = 2+2*r := by omega
    have p := two_step_four (4^r*n)
    have h := ih (3*n)
    constructor
    · rw [start, clock, orbit_add, p.1, mid, h.1]
      grind
    · rw [start, clock, oddCount_add, p.1, p.2, mid, h.2]
      omega

theorem four_step_five (n : Nat) :
    orbit (80*n+5) 4 = 15*n+1 ∧ oddCount (80*n+5) 4 = 1 := by
  have h1 : shortcut (80*n+5) = 120*n+8 := by unfold shortcut; split <;> omega
  have h2 : shortcut (120*n+8) = 60*n+4 := by unfold shortcut; split <;> omega
  have h3 : shortcut (60*n+4) = 30*n+2 := by unfold shortcut; split <;> omega
  have h4 : shortcut (30*n+2) = 15*n+1 := by unfold shortcut; split <;> omega
  simp [orbit, oddCount, h1, h2, h3, h4, Nat.add_mod, Nat.mul_mod]

/-- The target arm has one fewer odd input after the source ladder clock. -/
theorem five_four_ladder (n r : Nat) :
    orbit (5*(4^(r+2)*n+1)) (2*(r+2)) = 5*3^(r+1)*n+1 ∧
    oddCount (5*(4^(r+2)*n+1)) (2*(r+2)) = r+1 := by
  have start : 5*(4^(r+2)*n+1) = 80*(4^r*n)+5 := by
    rw [Nat.pow_add]
    simp
    grind
  have mid : 15*(4^r*n)+1 = 4^r*(15*n)+1 := by grind
  have clock : 2*(r+2) = 4+2*r := by omega
  have p := four_step_five (4^r*n)
  have h := four_ladder (15*n) r
  constructor
  · rw [start, clock, orbit_add, p.1, mid, h.1]
    rw [Nat.pow_succ]
    grind
  · rw [start, clock, oddCount_add, p.1, p.2, mid, h.2]
    omega

/-- Four final steps repair the one-count deficit whenever the source ends in
the last valuation-at-least-four cylinder. -/
theorem ladder_last_four (a b : Nat) (eq : 3*b+2=5*a) (ha : a%16=5) :
    orbit b 4 = 5*orbit a 4 ∧ oddCount b 4 = oddCount a 4 + 1 := by
  have h1a : shortcut a = (3*a+1)/2 := by unfold shortcut; split <;> omega
  have h2a : shortcut ((3*a+1)/2) = (3*a+1)/4 := by unfold shortcut; split <;> omega
  have h3a : shortcut ((3*a+1)/4) = (3*a+1)/8 := by unfold shortcut; split <;> omega
  have h4a : shortcut ((3*a+1)/8) = (3*a+1)/16 := by unfold shortcut; split <;> omega
  have h1b : shortcut b = (5*a-1)/2 := by unfold shortcut; split <;> omega
  have h2b : shortcut ((5*a-1)/2) = (5*a-1)/4 := by unfold shortcut; split <;> omega
  have h3b : shortcut ((5*a-1)/4) = (5*a-1)/8 := by unfold shortcut; split <;> omega
  have h4b : shortcut ((5*a-1)/8) = 5*((3*a+1)/16) := by unfold shortcut; split <;> omega
  constructor
  · simp [orbit, h1a, h2a, h3a, h4a, h1b, h2b, h3b, h4b]
  · simp only [oddCount, h1a, h2a, h3a, h1b, h2b, h3b]
    omega

/-- Every ordinary ladder length has a balanced return. The modular guard
is evaluated on the actual source endpoint, not a hypothetical parity word. -/
theorem unbounded_ladder_balanced (n r : Nat) (h : (3^(r+2)*n+1)%16=5) :
    BalancedFive (4^(r+2)*n+1) (2*(r+2)+4) := by
  have src := four_ladder n (r+2)
  have dst := five_four_ladder n r
  have eq : 3*(5*3^(r+1)*n+1)+2=5*(3^(r+2)*n+1) := by
    rw [show r+2=(r+1)+1 by omega, Nat.pow_succ]
    grind
  have tail := ladder_last_four (3^(r+2)*n+1) (5*3^(r+1)*n+1) eq h
  constructor
  · rw [oddCount_add, oddCount_add, src.1, src.2, dst.1, dst.2, tail.2]
    omega
  · rw [orbit_add, orbit_add, src.1, dst.1]
    exact tail.1

theorem unbounded_ladder_failure (n r : Nat) (h : (3^(r+2)*n+1)%16=5) :
    FiveFailure (4^(r+2)*n+1) ↔ FiveFailure ((3^(r+3)*n+4)/16) := by
  have root := unbounded_ladder_balanced n r h
  have src := four_ladder n (r+2)
  have h1 : shortcut (3^(r+2)*n+1) = (3*(3^(r+2)*n+1)+1)/2 := by
    unfold shortcut
    split <;> omega
  have h2 : shortcut ((3*(3^(r+2)*n+1)+1)/2) = (3*(3^(r+2)*n+1)+1)/4 := by
    unfold shortcut
    split <;> omega
  have h3 : shortcut ((3*(3^(r+2)*n+1)+1)/4) = (3*(3^(r+2)*n+1)+1)/8 := by
    unfold shortcut
    split <;> omega
  have h4 : shortcut ((3*(3^(r+2)*n+1)+1)/8) = (3*(3^(r+2)*n+1)+1)/16 := by
    unfold shortcut
    split <;> omega
  have endp : orbit (4^(r+2)*n+1) (2*(r+2)+4) = (3^(r+3)*n+4)/16 := by
    rw [orbit_add, src.1]
    simp only [orbit, h1, h2, h3, h4]
    congr 1
    rw [show r+3=(r+2)+1 by omega, Nat.pow_succ]
    grind
  simpa only [endp] using five_failure_return root

theorem ladder_endpoint_smaller (n r : Nat) :
    (3^(r+3)*n+4)/16 < 4^(r+2)*n+1 := by
  have h := Nat.mul_le_mul_right n (Nat.pow_le_pow_left (show 3≤4 by decide) (r+2))
  have e : 3^(r+3)*n=3*(3^(r+2)*n) := by
    rw [show r+3=(r+2)+1 by omega, Nat.pow_succ]
    grind
  rw [e]
  omega

theorem ladder_endpoint_positive (n r : Nat) (h : (3^(r+2)*n+1)%16=5) :
    0 < (3^(r+3)*n+4)/16 := by
  have e : 3^(r+3)*n+4=3*(3^(r+2)*n+1)+1 := by
    rw [show r+3=(r+2)+1 by omega, Nat.pow_succ]
    grind
  rw [e]
  omega

/-- Explicit nonempty ordinary progressions for every ladder length. -/
theorem ladder_guard_parametrized (q r : Nat) :
    (3^(r+2)*(4*3^(r+2)+16*q)+1)%16=5 := by
  have odd := three_pow_odd (r+2)
  have residue : 3^(r+2)%4=1 ∨ 3^(r+2)%4=3 := by omega
  have sq : (3^(r+2))^2%4=1 := by
    rw [Nat.pow_mod]
    rcases residue with hr | hr <;> simp [hr]
  have e : 3^(r+2)*(4*3^(r+2)+16*q)+1 = 4*(3^(r+2))^2+16*(3^(r+2)*q)+1 := by
    grind
  rw [e]
  omega

theorem unbounded_ladder_descent (n r : Nat) (h : (3^(r+2)*n+1)%16=5) :
    ∃ m, 0<m ∧ m<4^(r+2)*n+1 ∧
      (FiveFailure (4^(r+2)*n+1) ↔ FiveFailure m) := by
  exact ⟨(3^(r+3)*n+4)/16, ladder_endpoint_positive n r h,
    ladder_endpoint_smaller n r, unbounded_ladder_failure n r h⟩

/-- The one-rung case, in its complete ordinary cylinder. -/
theorem one_rung_balanced (q : Nat) : BalancedFive (49+64*q) 6 := by
  have h : BalancedFive 49 6 := by unfold BalancedFive; decide
  simpa using balanced_five_lift h q

theorem one_rung_failure (q : Nat) :
    FiveFailure (49+64*q) ↔ FiveFailure (7+9*q) := by
  have h : BalancedFive 49 6 := by unfold BalancedFive; decide
  simpa [orbit, oddCount, shortcut] using five_failure_cylinder h q

end CollatzGlobal

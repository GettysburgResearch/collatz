module

public import ShellCover
public import Mathlib.Data.Nat.Factorization.Basic

@[expose] public section

/-!
# Convergent sources with arbitrary first odd hitting depth

The six residue classes modulo nine define an actual positive odd unit parent
at least twice its target. Repeated parents of 5 give strictly increasing,
explicitly convergent sources whose first accelerated odd hit of 5 has every
prescribed depth. This is the physical clock witness in
STRICT_GREEN_VOLTERRA.md; no operator or Collatz conjecture is assumed here.
-/

namespace CollatzOddDepth

def Unit (q : Nat) : Prop := 0 < q ∧ q % 2 = 1 ∧ q % 3 ≠ 0

def oddStep (n : Nat) : Nat := ordCompl[2] (3*n+1)

def oddOrbit : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => oddOrbit k (oddStep n)

def parent (q : Nat) : Nat :=
  match q % 9 with
  | 1 => 48*(q/9)+5
  | 2 => 24*(q/9)+5
  | 4 => 192*(q/9)+85
  | 5 => 24*(q/9)+13
  | 7 => 48*(q/9)+37
  | _ => 96*(q/9)+85

def parentExponent (q : Nat) : Nat :=
  match q % 9 with
  | 1 => 4
  | 2 => 3
  | 4 => 6
  | 5 => 3
  | 7 => 4
  | _ => 5

/-- The exact affine table retains positivity, oddness, and the ternary unit. -/
theorem parent_spec (q : Nat) (hq : Unit q) :
    Unit (parent q) ∧ 2*q ≤ parent q ∧
      3*parent q+1 = 2^(parentExponent q)*q ∧ 0 < parentExponent q := by
  rcases hq with ⟨hpos, hodd, hunit⟩
  have choices : q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega
  rcases choices with h|h|h|h|h|h <;>
    norm_num [parent, parentExponent, h, Unit] <;> omega

/-- `ordCompl` removes precisely the displayed power of two, since q is odd. -/
theorem odd_step_parent (q : Nat) (hq : Unit q) : oddStep (parent q) = q := by
  change ordCompl[2] (3*parent q+1) = q
  rw [(parent_spec q hq).2.2.1]
  exact Nat.ordCompl_pow_mul_of_not_dvd (parentExponent q) Nat.prime_two (by
    have hodd := hq.2.1
    omega)

/-- The same inverse edge is an exact finite ordinary shortcut trajectory. -/
theorem parent_clock (q : Nat) (hq : Unit q) :
    CollatzShell.orbit (parentExponent q) (parent q) = q := by
  obtain ⟨hparent, _, heq, hexp⟩ := parent_spec q hq
  cases h : parentExponent q with
  | zero => omega
  | succ e =>
      rw [h, show 2^(e+1)*q = 2*(2^e*q) by ring] at heq
      have st : CollatzShell.step (parent q) = 2^e*q := by
        simp [CollatzShell.step, hparent.2.1]
        omega
      simp only [CollatzShell.orbit, st, CollatzShell.orbit_pad]

def ladder : Nat → Nat
  | 0 => 5
  | j+1 => parent (ladder j)

theorem ladder_unit (j : Nat) : Unit (ladder j) := by
  induction j with
  | zero => norm_num [ladder, Unit]
  | succ j ih => exact (parent_spec (ladder j) ih).1

theorem ladder_doubles (j : Nat) : 2*ladder j ≤ ladder (j+1) :=
  (parent_spec (ladder j) (ladder_unit j)).2.1

theorem ladder_growth (j : Nat) : 5*2^j ≤ ladder j := by
  induction j with
  | zero => simp [ladder]
  | succ j ih =>
      have hd := ladder_doubles j
      rw [pow_succ]
      omega

theorem ladder_cofinal (j : Nat) : j+5 ≤ ladder j := by
  induction j with
  | zero => simp [ladder]
  | succ j ih => have hd := ladder_doubles j; omega

theorem ladder_strictMono : StrictMono ladder := by
  apply strictMono_nat_of_lt_succ
  intro j
  have hp := (ladder_unit j).1
  have hd := ladder_doubles j
  omega

theorem odd_orbit_add (i j n : Nat) :
    oddOrbit (i+j) n = oddOrbit j (oddOrbit i n) := by
  induction i generalizing n with
  | zero => simp [oddOrbit]
  | succ i ih => simpa [Nat.succ_add, oddOrbit] using ih (oddStep n)

theorem odd_orbit_ladder (i j : Nat) :
    oddOrbit i (ladder (i+j)) = ladder j := by
  induction i with
  | zero => simp [oddOrbit]
  | succ i ih =>
      simpa only [Nat.succ_add, ladder, oddOrbit,
        odd_step_parent (ladder (i+j)) (ladder_unit (i+j))] using ih

theorem odd_orbit_ladder_prefix (i j : Nat) (hi : i ≤ j) :
    oddOrbit i (ladder j) = ladder (j-i) := by
  have h := odd_orbit_ladder i (j-i)
  simpa only [Nat.add_sub_of_le hi] using h

theorem odd_step_five : oddStep 5 = 1 := by
  change ordCompl[2] (2^4) = 1
  exact Nat.ordCompl_self_pow Nat.prime_two

theorem odd_step_one : oddStep 1 = 1 := by
  change ordCompl[2] (2^2) = 1
  exact Nat.ordCompl_self_pow Nat.prime_two

theorem odd_orbit_one (k : Nat) : oddOrbit k 1 = 1 := by
  induction k with
  | zero => rfl
  | succ k ih => simpa only [oddOrbit, odd_step_one] using ih

theorem ladder_odd_converges (j : Nat) : oddOrbit (j+1) (ladder j) = 1 := by
  rw [odd_orbit_add]
  have hit := odd_orbit_ladder j 0
  simp only [Nat.add_zero, ladder] at hit
  rw [hit]
  exact odd_step_five

theorem ladder_tail_one (j k : Nat) :
    oddOrbit (j+1+k) (ladder j) = 1 := by
  rw [odd_orbit_add, ladder_odd_converges, odd_orbit_one]

/-- The prescribed hit is the unique odd hit of 5, including after convergence. -/
theorem ladder_first_hit (j k : Nat) : oddOrbit k (ladder j) = 5 ↔ k = j := by
  constructor
  · intro h
    by_cases hk : k ≤ j
    · rw [odd_orbit_ladder_prefix k j hk] at h
      have hc := ladder_cofinal (j-k)
      omega
    · have ht := ladder_tail_one j (k-(j+1))
      have heq : j+1+(k-(j+1)) = k := by omega
      rw [heq] at ht
      omega
  · intro h
    subst k
    simpa only [Nat.add_zero, ladder] using odd_orbit_ladder j 0

theorem ladder_basin (j : Nat) : CollatzShell.Basin (ladder j) := by
  induction j with
  | zero => exact ⟨4, by decide⟩
  | succ j ih =>
      exact (CollatzShell.basin_at_hit
        (show CollatzShell.Hits (ladder (j+1)) (ladder j) from
          ⟨parentExponent (ladder j), parent_clock (ladder j) (ladder_unit j)⟩)).mpr ih

/-- Every member lies in the retained nonperiodic domain, despite converging. -/
theorem ladder_nonperiodic (j k : Nat) (hk : 0 < k) :
    oddOrbit k (ladder j) ≠ ladder j := by
  by_cases hkj : k ≤ j
  · rw [odd_orbit_ladder_prefix k j hkj]
    exact ne_of_lt (ladder_strictMono (by omega : j-k < j))
  · have ht := ladder_tail_one j (k-(j+1))
    have heq : j+1+(k-(j+1)) = k := by omega
    rw [heq] at ht
    rw [ht]
    have hc := ladder_cofinal j
    omega

/-- No finite odd-clock window contains all actual first hits, even in the
explicitly verified basin of one. The witnesses grow at least exponentially. -/
theorem arbitrary_first_odd_depth (N : Nat) :
    ∃ n : Nat, Unit n ∧ CollatzShell.Basin n ∧ 5*2^(N+1) ≤ n ∧
      oddOrbit (N+1) n = 5 ∧ ∀ k ≤ N, oddOrbit k n ≠ 5 := by
  refine ⟨ladder (N+1), ladder_unit _, ladder_basin _, ladder_growth _, ?_, ?_⟩
  · exact (ladder_first_hit (N+1) (N+1)).mpr rfl
  · intro k hk hit
    have he := (ladder_first_hit (N+1) k).mp hit
    omega

end CollatzOddDepth

#print axioms CollatzOddDepth.parent_spec
#print axioms CollatzOddDepth.odd_step_parent
#print axioms CollatzOddDepth.parent_clock
#print axioms CollatzOddDepth.ladder_unit
#print axioms CollatzOddDepth.ladder_doubles
#print axioms CollatzOddDepth.ladder_growth
#print axioms CollatzOddDepth.ladder_cofinal
#print axioms CollatzOddDepth.ladder_strictMono
#print axioms CollatzOddDepth.odd_orbit_add
#print axioms CollatzOddDepth.odd_orbit_ladder
#print axioms CollatzOddDepth.odd_orbit_ladder_prefix
#print axioms CollatzOddDepth.odd_step_five
#print axioms CollatzOddDepth.odd_step_one
#print axioms CollatzOddDepth.odd_orbit_one
#print axioms CollatzOddDepth.ladder_odd_converges
#print axioms CollatzOddDepth.ladder_tail_one
#print axioms CollatzOddDepth.ladder_first_hit
#print axioms CollatzOddDepth.ladder_basin
#print axioms CollatzOddDepth.ladder_nonperiodic
#print axioms CollatzOddDepth.arbitrary_first_odd_depth

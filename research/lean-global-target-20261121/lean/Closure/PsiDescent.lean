import Collatz.Closure

open CollatzReverseBasin CollatzClosure

namespace PsiDescent

/-- A deterministic ordinary path, without a stopping-time convention. -/
def orbit : Nat → Nat → Nat
  | 0, n => n
  | t+1, n => orbit t (shortcut n)

/-- Number of odd inputs along that path. -/
def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | t+1, n => n % 2 + oddCount t (shortcut n)

theorem orbit_add (a b n : Nat) :
    orbit (a+b) n = orbit b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih => simpa [orbit, Nat.succ_add] using ih (shortcut n)

theorem oddCount_add (a b n : Nat) :
    oddCount (a+b) n = oddCount a n + oddCount b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [orbit, oddCount]
  | succ a ih =>
    simp only [Nat.succ_add, oddCount, orbit]
    rw [ih]
    omega

theorem orbit_two_four (t : Nat) : orbit 2 (4*t+1) = 3*t+1 := by
  simp only [orbit]
  unfold shortcut
  split <;> split <;> omega

theorem oddCount_two_four (t : Nat) : oddCount 2 (4*t+1) = 1 := by
  simp only [oddCount]
  unfold shortcut
  split <;> omega

/-- Arbitrary-length exact profile, rather than just basin equivalence. -/
theorem power_four_profile (r v : Nat) :
    orbit (2*r) (4^r*v+1) = 3^r*v+1 ∧
    oddCount (2*r) (4^r*v+1) = r := by
  induction r generalizing v with
  | zero => simp [orbit, oddCount]
  | succ r ih =>
    have ec : 2*(r+1) = 2+2*r := by omega
    have es : 4^(r+1)*v+1 = 4*(4^r*v)+1 := by grind
    have en : 3*(4^r*v)+1 = 4^r*(3*v)+1 := by grind
    have ep : 3^r*(3*v)+1 = 3^(r+1)*v+1 := by grind
    rw [ec, es, orbit_add, oddCount_add, orbit_two_four, oddCount_two_four, en]
    constructor
    · exact (ih (3*v)).1.trans ep
    · have h := (ih (3*v)).2
      omega

/-- The even entrance has exactly one odd input in its two clocks. -/
theorem even_entrance (m A : Nat) (h : 3*m = 4*A+2) :
    orbit 2 m = A+1 ∧ oddCount 2 m = 1 := by
  simp only [orbit, oddCount]
  unfold shortcut
  constructor
  · split <;> split <;> omega
  · split <;> omega

theorem pow_three_le_four (r : Nat) : 3^r ≤ 4^r := by
  induction r with
  | zero => decide
  | succ r ih =>
    simp only [Nat.pow_succ]
    omega

/-- Both members have the same profile at a strictly smaller new failure index.
The equations are the exact integral guards; they imply positivity themselves. -/
theorem paired_descent (r v m u : Nat)
    (hm : 3*m = 4^(r+1)*v+2) (hu : 2*u = 3^r*v+1) :
    orbit (2*r+3) m = u ∧
    orbit (2*r+3) (3*m-1) = 3*u-1 ∧
    oddCount (2*r+3) m = r+1 ∧
    oddCount (2*r+3) (3*m-1) = r+1 ∧
    0 < u ∧ u < m := by
  have ep4 : 4^(r+1)*v = 4*(4^r*v) := by grind
  have ep3 : 3^(r+1)*v = 3*(3^r*v) := by grind
  have entrance := even_entrance m (4^r*v) (by omega)
  have source := power_four_profile r v
  have target := power_four_profile (r+1) v
  have hm' : 3*m-1 = 4^(r+1)*v+1 := by omega
  have hu' : 3^(r+1)*v+1 = 2*(3*u-1) := by omega
  have half (n : Nat) : shortcut (2*n) = n := by simp [shortcut]
  have parity (n : Nat) : (2*n)%2 = 0 := by omega
  have ec1 : 2*r+3 = (2+2*r)+1 := by omega
  have ec2 : 2*r+3 = 2*(r+1)+1 := by omega
  have source_end : orbit (2+2*r) m = 2*u := by
    rw [orbit_add, entrance.1]
    exact source.1.trans hu.symm
  have source_count : oddCount (2+2*r) m = r+1 := by
    rw [oddCount_add, entrance.1, entrance.2, source.2]
    omega
  have hp : 3^r ≤ 4^r := pow_three_le_four r
  have hmul : 3^r*v ≤ 4^r*v := Nat.mul_le_mul_right v hp
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [ec1, orbit_add, source_end]
    simp [orbit, half]
  · rw [hm', ec2, orbit_add, target.1, hu']
    simp [orbit, half]
  · rw [ec1, oddCount_add, source_end, source_count]
    simp [oddCount, parity]
  · rw [hm', ec2, oddCount_add, target.1, target.2, hu']
    simp [oddCount, parity]
  · omega
  · omega

theorem basin_orbit (t n : Nat) : Basin (orbit t n) ↔ Basin n := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih =>
    exact (ih (shortcut n)).trans (basin_step n)

/-- A reverse-closure failure in this entire family gives a smaller failure. -/
theorem failure_descends (r v m u : Nat)
    (hm : 3*m = 4^(r+1)*v+2) (hu : 2*u = 3^r*v+1) :
    Fail 3 1 m ↔ Fail 3 1 u := by
  have h := paired_descent r v m u hm hu
  have hs := basin_orbit (2*r+3) m
  have ht := basin_orbit (2*r+3) (3*m-1)
  rw [h.1] at hs
  rw [h.2.1] at ht
  unfold Fail
  exact ⟨fun hf => ⟨fun hu => hf.1 (hs.mp hu), ht.mpr hf.2⟩,
         fun hf => ⟨fun hm => hf.1 (hs.mpr hm), ht.mp hf.2⟩⟩

/-- Minimality is only a hypothesis about this relation, not an assumed Collatz fact. -/
theorem not_minimal_failure (r v m u : Nat)
    (hm : 3*m = 4^(r+1)*v+2) (hu : 2*u = 3^r*v+1)
    (minimal : ∀ q : Nat, 0 < q → q < m → ¬ Fail 3 1 q) :
    ¬ Fail 3 1 m := by
  have h := paired_descent r v m u hm hu
  intro hf
  exact minimal u h.2.2.2.2.1 h.2.2.2.2.2
    ((failure_descends r v m u hm hu).mp hf)

theorem step_lift (n a : Nat) :
    shortcut (n+2*a) = shortcut n + 3^(n%2)*a := by
  rcases Nat.mod_two_eq_zero_or_one n with h | h
  · simp [shortcut, h, Nat.add_mod]
    omega
  · simp [shortcut, h, Nat.add_mod]
    omega

/-- Exact finite binary lift of a deterministic profile. -/
theorem profile_lift (k n t : Nat) :
    orbit k (n+2^k*t) = orbit k n + 3^(oddCount k n)*t ∧
    oddCount k (n+2^k*t) = oddCount k n := by
  induction k generalizing n t with
  | zero => simp [orbit, oddCount]
  | succ k ih =>
    have e : n+2^(k+1)*t = n+2*(2^k*t) := by grind
    have hs : shortcut (n+2^(k+1)*t) = shortcut n+2^k*(3^(n%2)*t) := by
      rw [e, step_lift]
      grind
    have hm : (n+2^(k+1)*t)%2 = n%2 := by rw [e]; omega
    have h := ih (shortcut n) (3^(n%2)*t)
    simp only [orbit, oddCount, hs, hm]
    constructor
    · rw [h.1, Nat.pow_add]
      grind
    · rw [h.2]

/-- A whole ordinary cylinder refutes an all-returns-contract completion rule. -/
theorem expanding_return (t : Nat) :
    orbit 22 (2469887+4194304*t) = 2816534+4782969*t ∧
    orbit 22 (3*(2469887+4194304*t)-1) = 3*(2816534+4782969*t)-1 ∧
    oddCount 22 (2469887+4194304*t) = 14 ∧
    oddCount 22 (3*(2469887+4194304*t)-1) = 14 ∧
    2469887+4194304*t < 2816534+4782969*t := by
  have s := profile_lift 22 2469887 t
  have q := profile_lift 22 7409660 (3*t)
  have s_end : orbit 22 2469887 = 2816534 := by decide
  have q_end : orbit 22 7409660 = 8449601 := by decide
  have s_count : oddCount 22 2469887 = 14 := by decide
  have q_count : oddCount 22 7409660 = 14 := by decide
  have p2 : 2^22 = (4194304 : Nat) := by decide
  have p3 : 3^14 = (4782969 : Nat) := by decide
  rw [s_end, s_count, p2, p3] at s
  rw [q_end, q_count, p2, p3] at q
  have input : 3*(2469887+4194304*t)-1 = 7409660+4194304*(3*t) := by omega
  have output : 3*(2816534+4782969*t)-1 = 8449601+4782969*(3*t) := by omega
  rw [input, output]
  exact ⟨s.1, q.1, s.2, q.2, by omega⟩

def BalancedReturn (j n : Nat) : Prop :=
  oddCount j n = oddCount j (3*n-1) ∧
  orbit j (3*n-1)+1 = 3*orbit j n

theorem expanding_first_return_base :
    ∀ j : Fin 22, j.val = 0 ∨ ¬ BalancedReturn j.val 2469887 := by
  unfold BalancedReturn
  decide

/-- The entire cylinder has no positive balanced return before clock22. -/
theorem expanding_first_return (t j : Nat) (hj : 0 < j) (hl : j < 22) :
    ¬ BalancedReturn j (2469887+4194304*t) := by
  have hbase := expanding_first_return_base ⟨j, hl⟩
  have hb : ¬ BalancedReturn j 2469887 := by simpa [Nat.ne_of_gt hj] using hbase
  have ep : 2^22 = 2^j*2^(22-j) := by
    rw [← Nat.pow_add]
    congr 1
    omega
  have ep2 : 2^22 = (4194304 : Nat) := by decide
  have hs := profile_lift j 2469887 (2^(22-j)*t)
  have ht := profile_lift j 7409660 (2^(22-j)*(3*t))
  have es : 2469887+2^j*(2^(22-j)*t) = 2469887+4194304*t := by
    rw [← Nat.mul_assoc, ← ep, ep2]
  have et : 7409660+2^j*(2^(22-j)*(3*t)) = 3*(2469887+4194304*t)-1 := by
    rw [← Nat.mul_assoc, ← ep, ep2]
    omega
  rw [es] at hs
  rw [et] at ht
  intro hr
  apply hb
  unfold BalancedReturn at hr ⊢
  have hc : oddCount j 2469887 = oddCount j 7409660 := by
    rw [hs.2, ht.2] at hr
    exact hr.1
  constructor
  · exact hc
  · have he := hr.2
    rw [hs.1, ht.1, hc] at he
    change orbit j 7409660+1 = 3*orbit j 2469887
    grind

#print axioms paired_descent
#print axioms failure_descends
#print axioms not_minimal_failure
#print axioms profile_lift
#print axioms expanding_return
#print axioms expanding_first_return

end PsiDescent

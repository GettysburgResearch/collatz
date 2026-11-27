import Std

/-! Finite coefficient identities for the dyadically removable specialization,
and the autonomous two-carry control. All clocks and states are natural numbers. -/
namespace Collatz.Adelic

def clock (g : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => clock g n + g n

/-- Numerator obtained by division of the shifted series by 1 - 3z,
written with integer recurrences so no convergence assumption enters. -/
def scaledPartial (q₀ : Nat) (g d : Nat → Nat) : Nat → Nat
  | 0 => q₀
  | n+1 => 3 * scaledPartial q₀ g d n + 2 ^ clock g n * d n

theorem scaled_physical (q g d : Nat → Nat)
    (step : ∀ n, 2 ^ g n * q (n+1) = 3 * q n + d n) (n : Nat) :
    scaledPartial (q 0) g d n = 2 ^ clock g n * q n := by
  induction n with
  | zero => simp [scaledPartial, clock]
  | succ n ih =>
    calc
      scaledPartial (q 0) g d (n+1)
          = 3 * (2 ^ clock g n * q n) + 2 ^ clock g n * d n := by rw [scaledPartial, ih]
      _ = 2 ^ clock g n * (3 * q n + d n) := by rw [Nat.mul_add]; ac_rfl
      _ = 2 ^ clock g (n+1) * q (n+1) := by
        rw [← step n, clock, Nat.pow_add, Nat.mul_assoc]

/-- The smallest odd integer strictly above 3x/2 when x is odd. -/
def defect (x : Nat) : Nat := if x%4=1 then 3 else 1
def rounded (x : Nat) : Nat := (3*x+defect x)/2

theorem rounded_step (x : Nat) (ho : x%2=1) :
    2 * rounded x = 3*x + defect x ∧ (rounded x)%2=1 ∧
      x < rounded x ∧ (defect x=1 ∨ defect x=3) := by
  unfold rounded defect
  split <;> omega

def orbit (q : Nat) : Nat → Nat
  | 0 => q
  | n+1 => rounded (orbit q n)

theorem orbit_odd (q : Nat) (ho : q%2=1) (n : Nat) :
    (orbit q n)%2=1 := by
  induction n with
  | zero => exact ho
  | succ n ih => exact (rounded_step (orbit q n) ih).2.1

theorem orbit_increases (q : Nat) (ho : q%2=1) (n : Nat) :
    orbit q n < orbit q (n+1) :=
  (rounded_step (orbit q n) (orbit_odd q ho n)).2.2.1

theorem control_telescope (q : Nat) (ho : q%2=1) (n : Nat) :
    scaledPartial q (fun _ => 1) (fun i => defect (orbit q i)) n =
      2^n * orbit q n := by
  have h (k : Nat) : clock (fun _ => 1) k = k := by
    induction k with
    | zero => rfl
    | succ k ih => rw [clock, ih]
  have ps (k : Nat) : 2 ^ (1:Nat) * orbit q (k+1) = 3*orbit q k + defect (orbit q k) :=
    (rounded_step (orbit q k) (orbit_odd q ho k)).1
  simpa only [orbit, h] using
    scaled_physical (orbit q) (fun _ => 1) (fun i => defect (orbit q i)) ps n

#print axioms scaled_physical
#print axioms rounded_step
#print axioms orbit_odd
#print axioms orbit_increases
#print axioms control_telescope

/-- Smallest odd integer strictly above 3x / 2^g for odd x and g ∈ {1,2}. -/
def nearOdd (g x : Nat) : Nat := 2 * ((3*x+2^g)/(2*2^g)) + 1

theorem bounded_rounding (g x : Nat) (hgap : g=1 ∨ g=2) (ho : x%2=1) :
    let y := nearOdd g x
    let D := 2^g*y - 3*x
    y%2=1 ∧ 2^g*y=3*x+D ∧ (D=1 ∨ D=3 ∨ D=5 ∨ D=7) := by
  rcases hgap with h | h <;> subst g <;> simp [nearOdd] <;> omega

theorem partial_split (q₀ : Nat) (g d : Nat → Nat) (n : Nat) :
    scaledPartial q₀ g d n = 3^n * q₀ + scaledPartial 0 g d n := by
  induction n with
  | zero => simp [scaledPartial]
  | succ n ih =>
    rw [scaledPartial, ih, Nat.mul_add, Nat.pow_succ, scaledPartial]
    ac_rfl

theorem carry_bound (g d : Nat → Nat) (hg : ∀ n, g n ≤ 2) (hd : ∀ n, d n ≤ 7) (n : Nat) :
    scaledPartial 0 g d n ≤ (7*n)*4^n := by
  have hclock (j : Nat) : clock g j ≤ 2*j := by
    induction j with
    | zero => exact Nat.zero_le _
    | succ j hj => rw [clock, Nat.mul_succ]; have := hg j; omega
  induction n with
  | zero => simp [scaledPartial]
  | succ n ih =>
    have p : 2^(clock g n) ≤ 4^n := by
      have t := Nat.pow_le_pow_right Nat.zero_lt_two (hclock n)
      simpa only [Nat.pow_mul] using t
    have hterm := Nat.mul_le_mul p (hd n)
    have hprev := Nat.mul_le_mul_left 3 ih
    calc
      scaledPartial 0 g d (n+1) ≤ 3*((7*n)*4^n) + 4^n*7 :=
        Nat.add_le_add hprev hterm
      _ ≤ (7*(n+1))*4^(n+1) := by
        rw [Nat.pow_succ, Nat.mul_succ 7 n, Nat.add_mul]
        have hmul : (7*n)*(4^n*4) = 4*((7*n)*4^n) := by ac_rfl
        have hmul' : 7*(4^n*4) = 4*(4^n*7) := by ac_rfl
        rw [hmul, hmul']
        omega

/-- Any repeated ordinary state on bounded-gap, bounded-carry dynamics is
at most the complete additive block numerator at that clock. -/
theorem short_return_bound (q g d : Nat → Nat)
    (step : ∀ n, 2 ^ g n * q (n+1) = 3 * q n + d n)
    (hg : ∀ n, g n ≤ 2) (hd : ∀ n, d n ≤ 7)
    (n : Nat) (ret : q n = q 0) (hpos : 0 < scaledPartial 0 g d n) :
    q 0 ≤ (7*n)*4^n := by
  have eq := scaled_physical q g d step n
  rw [partial_split,ret] at eq
  have ha : 3^n < 2^clock g n := by
    apply Classical.byContradiction
    intro hn
    have := Nat.mul_le_mul_right (q 0) (show 2^clock g n ≤ 3^n by omega)
    omega
  have hmul := Nat.mul_le_mul_right (q 0) (show 3^n+1 ≤ 2^clock g n by omega)
  rw [Nat.add_mul, Nat.one_mul] at hmul
  have bound := carry_bound g d hg hd n
  omega

#print axioms bounded_rounding
#print axioms partial_split
#print axioms carry_bound
#print axioms short_return_bound

end Collatz.Adelic

/-
Exact dyadic precision for repetitions of any supplied ordinary parity block.

The block consists of an initial even run followed by an arbitrary positive-gap
word.  All repetitions are actual integral Collatz prefixes.  No convergence
of either the block or the full Collatz map is assumed.

A nonfixed block cannot repeat indefinitely: its affine displacement loses
exactly the block clock in dyadic valuation at each repetition.  This theorem
does not assert that changing blocks share a common decreasing measure.
-/
import Collatz.SignedShadow

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzHighGapPump
open CollatzUnboundedGapReset

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace CollatzAffineBlockPrecision

/-- Initial halvings followed by the supplied literal odd-gap word.  The last
endpoint may be even; each subsequent nonempty repetition supplies its own
actual parity requirements. -/
def Block (e : Nat) (word : List Nat) (n endpoint : Nat) : Prop :=
  ∃ q, n=2^e*q ∧ Prefix q word endpoint

def clock (e : Nat) (word : List Nat) : Nat := e+total word

def offset (e : Nat) (word : List Nat) : Nat := 2^e*correction word

/-- The numerator of the displacement of the block from its starting value.
The signed definition retains contracting blocks and possible fixed points. -/
def balance (e : Nat) (word : List Nat) (n : Nat) : Int :=
  (3: Int)^word.length*(n: Int)+(offset e word: Int)-
    (2: Int)^clock e word*(n: Int)

theorem block_affine (e n endpoint : Nat) (word : List Nat)
    (path : Block e word n endpoint) :
    2^clock e word*endpoint=3^word.length*n+offset e word := by
  obtain ⟨q,parent,exactWord⟩ := path
  have multiplied := congrArg (2^e*·) exactWord.2
  simp only [clock,offset,parent,Nat.pow_add]
  grind

private theorem orbit_halvings (e q : Nat) : orbit (2^e*q) e=q := by
  induction e with
  | zero => simp [orbit]
  | succ e ih =>
    have step : shortcut (2^(e+1)*q)=2^e*q := by
      have factor : 2^(e+1)*q=2*(2^e*q) := by
        rw [Nat.pow_succ]
        ac_rfl
      rw [factor]
      unfold shortcut
      simp
    rw [orbit,step,ih]

/-- The algebraic prefix is tied to the actual ordinary shortcut clock. -/
theorem block_orbit (e n endpoint : Nat) (word : List Nat)
    (path : Block e word n endpoint) : orbit n (clock e word)=endpoint := by
  obtain ⟨q,parent,exactWord⟩ := path
  rw [parent,clock,orbit_add,orbit_halvings]
  exact CollatzSignedShadow.prefix_orbit exactWord

/-- For F(n)=(A*n+C)/B, the displacement D(n)=A*n+C-B*n obeys
B*D(F(n))=A*D(n).  Here A=3^length and B=2^clock. -/
theorem balance_transport (e n endpoint : Nat) (word : List Nat)
    (path : Block e word n endpoint) :
    (2: Int)^clock e word*balance e word endpoint=
      (3: Int)^word.length*balance e word n := by
  have affine : (2: Int)^clock e word*(endpoint: Int)=
      (3: Int)^word.length*(n: Int)+(offset e word: Int) := by
    exact_mod_cast block_affine e n endpoint word path
  unfold balance
  grind

theorem balance_magnitude_transport (e n endpoint : Nat) (word : List Nat)
    (path : Block e word n endpoint) :
    2^clock e word*(balance e word endpoint).natAbs=
      3^word.length*(balance e word n).natAbs := by
  have magnitude := congrArg Int.natAbs (balance_transport e n endpoint word path)
  simpa [Int.natAbs_mul,Int.natAbs_pow] using magnitude

/-- Repetitions use the same complete block, with all actual intermediate
endpoints exposed.  This does not allow changing the block between calls. -/
def RepeatedBlock (e : Nat) (word : List Nat) (states : Nat → Nat)
    (count : Nat) : Prop :=
  ∀ j, j<count → Block e word (states j) (states (j+1))

theorem repeated_actual_orbit (e count j : Nat) (word : List Nat)
    (states : Nat → Nat) (repeated : RepeatedBlock e word states count)
    (within : j≤count) :
    orbit (states 0) (clock e word*j)=states j := by
  induction j with
  | zero => simp [orbit]
  | succ j ih =>
    have previous := ih (by omega)
    rw [Nat.mul_succ,orbit_add,previous]
    exact block_orbit e (states j) (states (j+1)) word (repeated j (by omega))

private theorem power_transport (A B count : Nat) (values : Nat → Nat)
    (steps : ∀ j, j<count → B*values (j+1)=A*values j) :
    B^count*values count=A^count*values 0 := by
  induction count with
  | zero => simp
  | succ count ih =>
    have previous := ih (fun j below => steps j (by omega))
    have last := steps count (by omega)
    simp only [Nat.pow_succ]
    calc
      B^count*B*values (count+1) = B^count*(B*values (count+1)) := by ac_rfl
      _ = B^count*(A*values count) := by rw [last]
      _ = A*(B^count*values count) := by ac_rfl
      _ = A*(A^count*values 0) := by rw [previous]
      _ = A^count*A*values 0 := by ac_rfl

/-- The exact transport through arbitrarily many legal repetitions. -/
theorem repeated_balance (e count : Nat) (word : List Nat) (states : Nat → Nat)
    (repeated : RepeatedBlock e word states count) :
    2^(clock e word*count)*(balance e word (states count)).natAbs=
      3^(word.length*count)*(balance e word (states 0)).natAbs := by
  have transport := power_transport (3^word.length) (2^clock e word) count
    (fun j => (balance e word (states j)).natAbs)
    (fun j below => balance_magnitude_transport e (states j) (states (j+1))
      word (repeated j below))
  simpa [Nat.pow_mul] using transport

/-- Every repeated clock is paid by an actual power of two in the initial
displacement.  The conclusion also correctly permits zero displacement. -/
theorem repetition_precision (e count : Nat) (word : List Nat)
    (states : Nat → Nat) (repeated : RepeatedBlock e word states count) :
    2^(clock e word*count) ∣ (balance e word (states 0)).natAbs := by
  have transport := repeated_balance e count word states repeated
  have divides : 2^(clock e word*count) ∣
      3^(word.length*count)*(balance e word (states 0)).natAbs :=
    ⟨(balance e word (states count)).natAbs,transport.symm⟩
  have coprime : Nat.Coprime (2^(clock e word*count)) (3^(word.length*count)) :=
    Nat.Coprime.pow _ _ (by decide : Nat.Coprime 2 3)
  exact coprime.dvd_of_dvd_mul_left divides

/-- A numerical bound requiring no valuation function or search cutoff. -/
theorem repetition_clock_bound (e count : Nat) (word : List Nat)
    (states : Nat → Nat) (repeated : RepeatedBlock e word states count)
    (nonfixed : balance e word (states 0)≠0) :
    clock e word*count≤(balance e word (states 0)).natAbs.log2 := by
  have positive : 0<(balance e word (states 0)).natAbs := by omega
  exact (Nat.le_log2 (by omega)).mpr
    (Nat.le_of_dvd positive (repetition_precision e count word states repeated))

/-- Exact valuation loss, stated using an arbitrary supplied odd factor.
No fixed block length, multiplier, correction, or repetition count is bounded. -/
theorem repetition_exact_precision (e count H oddPart : Nat) (word : List Nat)
    (states : Nat → Nat) (repeated : RepeatedBlock e word states count)
    (factor : (balance e word (states 0)).natAbs=2^H*oddPart)
    (odd : oddPart%2=1) :
    clock e word*count≤H ∧
    (balance e word (states count)).natAbs=
      2^(H-clock e word*count)*(3^(word.length*count)*oddPart) := by
  have twoUnit : Nat.Coprime 2 oddPart := by
    change Nat.gcd 2 oddPart=1
    rw [Nat.gcd_succ,odd]
    simp
  have divides := repetition_precision e count word states repeated
  rw [factor] at divides
  have powerDivides : 2^(clock e word*count) ∣ 2^H :=
    (twoUnit.pow_left _).dvd_of_dvd_mul_right divides
  have paid : clock e word*count≤H :=
    (Nat.pow_dvd_pow_iff_le_right (by decide : 1<2)).mp powerDivides
  refine ⟨paid,?_⟩
  have power : 2^H=2^(clock e word*count)*2^(H-clock e word*count) := by
    rw [←Nat.pow_add,Nat.add_sub_of_le paid]
  apply Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide : 0<2))
  rw [repeated_balance e count word states repeated,factor,power]
  ac_rfl

/-- The nonfixed hypothesis is necessary: a genuine periodic point has zero
displacement.  At every other starting point, one supplied block cannot be
an infinite actual loop. -/
theorem no_infinite_repetition (e : Nat) (word : List Nat) (states : Nat → Nat)
    (positiveClock : 0<clock e word)
    (nonfixed : balance e word (states 0)≠0) :
    ¬(∀ j, Block e word (states j) (states (j+1))) := by
  intro forever
  let count := (balance e word (states 0)).natAbs.log2+1
  have bound := repetition_clock_bound e count word states
    (fun j _ => forever j) nonfixed
  have lower : count≤clock e word*count :=
    Nat.le_mul_of_pos_left count positiveClock
  dsimp [count] at bound lower
  omega

theorem expanding_balance_positive (e n : Nat) (word : List Nat)
    (positive : 0<n) (expanding : 2^clock e word<3^word.length) :
    0<balance e word n := by
  have scaled := Nat.mul_lt_mul_of_pos_right expanding positive
  have scaledInt : (2: Int)^clock e word*(n: Int)<
      (3: Int)^word.length*(n: Int) := by exact_mod_cast scaled
  have correctionNonnegative : 0≤(offset e word: Int) := by omega
  unfold balance
  omega

/-- An expanding block has a negative affine fixed point, so no positive
integer can be the exceptional fixed point in the preceding theorem. -/
theorem expanding_no_infinite_repetition (e : Nat) (word : List Nat)
    (states : Nat → Nat) (positive : 0<states 0)
    (positiveClock : 0<clock e word)
    (expanding : 2^clock e word<3^word.length) :
    ¬(∀ j, Block e word (states j) (states (j+1))) := by
  apply no_infinite_repetition e word states positiveClock
  have strictlyPositive := expanding_balance_positive e (states 0) word positive expanding
  omega

/-- Odd-even-odd has multiplier9, clock3, and displacement n+7. -/
theorem odd_even_odd_balance (n : Nat) : balance 0 [2,1] n=(n: Int)+7 := by
  simp [balance,clock,offset,total,correction]
  omega

end CollatzAffineBlockPrecision

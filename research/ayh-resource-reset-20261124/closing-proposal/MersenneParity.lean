import ReverseBasin

/-! Ordinary merger between the Mersenne inputs of exponents 2k+1 and 2k+2.
Their first 2k+1 and 2k+2 steps respectively reach shifted ternary powers. -/
namespace CollatzMersenneParity
open CollatzReverseBasin

private theorem memStep (n : ℕ) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩
    exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

def atClock : ℕ → ℕ → ℕ
  | 0, n => n
  | k+1, n => atClock k (shortcut n)

theorem hits_atClock (k n : ℕ) : Hits n k ↔ atClock k n = 1 := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact ih (shortcut n)

private theorem atClockAdd (k t n : ℕ) :
    atClock (k+t) n = atClock t (atClock k n) := by
  induction k generalizing n with
  | zero => simp [atClock]
  | succ k ih => simpa [Nat.succ_add, atClock] using ih (shortcut n)

private theorem memClock (k n : ℕ) : Basin (atClock k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih (shortcut n)).trans (memStep n)

theorem ascent (k t : ℕ) (ht : 0<t) :
    atClock k (2^k*t-1) = 3^k*t-1 := by
  induction k generalizing t with
  | zero => simp [atClock]
  | succ k ih =>
    have hp : 0<2^k*t := Nat.mul_pos (Nat.pow_pos (by decide : 0 < 2)) ht
    have e : shortcut (2^(k+1)*t-1)=2^k*(3*t)-1 := by
      rw [show 2^(k+1)*t=2*(2^k*t) by ring,show 2^k*(3*t)=3*(2^k*t) by ring]
      unfold shortcut
      split <;> omega
    rw [atClock, e, ih (3*t) (by omega)]
    ring_nf

private theorem threeOddResidue (k : ℕ) : 3^(2*k+1)%4=3 := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [show 2*(k+1)+1=(2*k+1)+2 by omega,pow_add,Nat.mul_mod,ih]
    decide

/-- Both positive arms meet at their actual far ends after the two-speed
Mersenne ascents. Only two further clocks on each shifted power are needed. -/
theorem even_mersenne_meeting (k : ℕ) :
    atClock ((2*k+2)+2) (2^(2*k+2)-1) =
    atClock ((2*k+1)+2) (2^(2*k+1)-1) := by
  let u : ℕ := 3^(2*k+1)
  have res : u%4=3 := threeOddResidue k
  have upper : 3^(2*k+2)=3*u := by
    dsimp [u]; rw [show 2*k+2=(2*k+1)+1 by omega,pow_succ,Nat.mul_comm]
  have lo := ascent (2*k+1) 1 (by decide)
  have hi := ascent (2*k+2) 1 (by decide)
  simp only [Nat.mul_one] at lo hi
  rw [atClockAdd, atClockAdd (2*k+1), hi, lo, upper]
  change shortcut (shortcut (3*u-1)) = shortcut (shortcut (u-1))
  have a : shortcut (u-1)=(u-1)/2 := by unfold shortcut; split <;> omega
  have b : shortcut (3*u-1)=(3*u-1)/2 := by unfold shortcut; split <;> omega
  rw [a,b]
  unfold shortcut; split <;> split <;> omega

theorem even_mersenne_basin (k : ℕ) :
    Basin (2^(2*k+2)-1) ↔ Basin (2^(2*k+1)-1) := by
  have h := (memClock ((2*k+2)+2) (2^(2*k+2)-1)).symm
  rw [even_mersenne_meeting] at h
  exact h.trans (memClock _ _)

end CollatzMersenneParity

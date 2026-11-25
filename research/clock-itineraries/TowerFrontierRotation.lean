module

public import Std

public section

namespace Collatz.Itinerary.TowerFrontier

set_option autoImplicit false

private theorem toggle_factor (k : Nat) :
    ∃ t : Nat, 3^(2^(k+1)) = 1 + (8*2^k)*(2*t+1) := by
  induction k with
  | zero => exact ⟨0, by decide⟩
  | succ k ih =>
    obtain ⟨t, h⟩ := ih
    refine ⟨t+2*(2^k)*(2*t+1)*(2*t+1), ?_⟩
    rw [Nat.pow_succ 2 (k+1), Nat.pow_mul, h, Nat.pow_succ 2 k]
    grind

/-- Multiplying by a suitable power of three reaches any prescribed extension
    of the same odd three-bit residue in at most one period. -/
theorem rotate {x a : Nat} (odd : x%2=1) (root : x%8=a%8) (k : Nat) :
    ∃ d < 2^(k+1), (3^d*x)%(8*2^k) = a%(8*2^k) := by
  induction k with
  | zero => exact ⟨0, by decide, by simpa using root⟩
  | succ k ih =>
    obtain ⟨d, small, hd⟩ := ih
    let m := 8*2^k
    let z := 3^d*x
    have hm : 0<m := Nat.mul_pos (by decide) (Nat.two_pow_pos _)
    have hz : z%2=1 := by simp [z, Nat.mul_mod, Nat.pow_mod, odd]
    have base : z%m=a%m := hd
    have lift : 8*2^(k+1)=2*m := by simp only [m,Nat.pow_succ]; ac_rfl
    rw [lift, Nat.pow_succ 2 (k+1)]
    by_cases done : z%(2*m)=a%(2*m)
    · exact ⟨d, by omega, done⟩
    obtain ⟨t, ht⟩ := toggle_factor k
    have twist : 3^(d+2^(k+1))*x = z+m*((2*t+1)*z) := by
      rw [Nat.pow_add, ht]
      simp only [z,m,Nat.mul_add,Nat.mul_one,Nat.add_mul]
      ac_rfl
    have oddFactor : ((2*t+1)*z)%2 = 1 := by simp [Nat.mul_mod, hz]
    have twice : (2*t+1)*z = 2*(((2*t+1)*z)/2)+1 := by omega
    have twisted : (3^(d+2^(k+1))*x)%(2*m)=(z+m)%(2*m) := by
      rw [twist, twice, Nat.mul_add, Nat.mul_one]
      have rearrange : z+(m*(2*(((2*t+1)*z)/2))+m) =
          z+m+(2*m)*(((2*t+1)*z)/2) := by ac_rfl
      rw [rearrange, Nat.add_mul_mod_self_left]
    have hop : (z+m)%(2*m)=a%(2*m) := by
      have zr := Nat.mod_lt z (Nat.mul_pos (by decide : 0<2) hm)
      have ar := Nat.mod_lt a (Nat.mul_pos (by decide : 0<2) hm)
      have h1 : z%(2*m)%m=z%m := Nat.mod_mod_of_dvd _ ⟨2,Nat.mul_comm _ _⟩
      have h2 : a%(2*m)%m=a%m := Nat.mod_mod_of_dvd _ ⟨2,Nat.mul_comm _ _⟩
      have decomp (u : Nat) (hu : u<2*m) : u%m = if u<m then u else u-m := by
        split
        · exact Nat.mod_eq_of_lt ‹_›
        · have h : u=m+(u-m) := by omega
          calc
            u%m = (m+(u-m))%m := congrArg (·%m) h
            _ = u-m := by rw [Nat.add_mod_left, Nat.mod_eq_of_lt (by omega : u-m<m)]
      have stepmod : (z+m)%(2*m) = (z%(2*m)+m)%(2*m) := by
        rw [Nat.mod_add_mod]
      rw [stepmod]
      rw [decomp _ zr] at h1
      rw [decomp _ ar] at h2
      by_cases low : z%(2*m)<m
      · rw [Nat.mod_eq_of_lt (by omega : z%(2*m)+m<2*m)]
        split at h1 <;> split at h2 <;> omega
      · have eq : z%(2*m)+m=2*m+(z%(2*m)-m) := by omega
        rw [eq,Nat.add_mod_left,Nat.mod_eq_of_lt (by omega : z%(2*m)-m<2*m)]
        split at h1 <;> split at h2 <;> omega
    exact ⟨d+2^(k+1), by omega, twisted.trans hop⟩

end Collatz.Itinerary.TowerFrontier

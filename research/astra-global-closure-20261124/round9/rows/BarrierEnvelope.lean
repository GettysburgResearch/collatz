module

public import Std

public section

namespace Collatz.BalancedBarrier

set_option autoImplicit false

/-- At raw clock t the offset is num/den and the denominator is 2^t.
Level is the running maximum of even surplus minus its current value. -/
structure Account where
  num : Nat
  den : Nat
  level : Nat
  peak : Nat
  odds : Nat
  evens : Nat

def start : Account := ⟨0,1,0,0,0,0⟩

/-- True is an odd shortcut input. -/
def advance (s : Account) : Bool → Account
  | true => {s with num := 3*s.num+s.den, den := 2*s.den,
                    level := s.level+1, odds := s.odds+1}
  | false => {s with den := 2*s.den, level := s.level-1, evens := s.evens+1,
                     peak := if s.level=0 then s.peak+1 else s.peak}

def envelope (s : Account) : Prop :=
  (s.num+s.den)*2^s.level ≤ (2*s.den)*3^s.level

def coherent (s : Account) : Prop := s.level+s.evens=s.peak+s.odds

theorem advance_envelope (s : Account) (bit : Bool) (good : envelope s) :
    envelope (advance s bit) := by
  cases s with
  | mk c d l h o e =>
    change (c+d)*2^l ≤ 2*d*3^l at good
    cases bit with
    | true =>
      change (3*c+d+2*d)*2^(l+1) ≤ (2*(2*d))*3^(l+1)
      calc
        _ = 6*((c+d)*2^l) := by rw [Nat.pow_succ]; grind
        _ ≤ 6*(2*d*3^l) := Nat.mul_le_mul_left _ good
        _ = _ := by rw [Nat.pow_succ]; grind
    | false =>
      cases l with
      | zero =>
        simpa [envelope,advance] using (show c+2*d ≤ 2*(2*d) by simp at good; omega)
      | succ j =>
        change (c+2*d)*2^j ≤ (2*(2*d))*3^j
        have old : 2*((c+d)*2^j) ≤ 2*(3*(d*3^j)) := by
          calc
            _ = (c+d)*2^(j+1) := by rw [Nat.pow_succ]; grind
            _ ≤ 2*d*3^(j+1) := good
            _ = _ := by rw [Nat.pow_succ]; grind
        have half : (c+d)*2^j ≤ 3*(d*3^j) := by omega
        have little := Nat.mul_le_mul_left d (Nat.pow_le_pow_left (by decide : 2≤3) j)
        calc
          _ = (c+d)*2^j+d*2^j := by grind
          _ ≤ 3*(d*3^j)+d*3^j := Nat.add_le_add half little
          _ = _ := by grind

theorem advance_coherent (s : Account) (bit : Bool) (good : coherent s) :
    coherent (advance s bit) := by
  cases s with
  | mk c d l h o e =>
    change l+e=h+o at good
    cases bit <;> cases l <;> simp [coherent,advance] <;> omega

/-- The update records the actual running maximum of prefix even surplus. -/
theorem advance_peak (s : Account) (bit : Bool) (good : coherent s) :
    (advance s bit).peak = max s.peak ((advance s bit).evens-(advance s bit).odds) := by
  cases s with
  | mk c d l h o e =>
    change l+e=h+o at good
    cases bit <;> cases l <;> simp [advance] <;> omega

def read (s : Account) : List Bool → Account
  | [] => s
  | bit::tail => read (advance s bit) tail

theorem after_word (s : Account) (bits : List Bool) (lo : envelope s) (hi : coherent s) :
    envelope (read s bits) ∧ coherent (read s bits) := by
  induction bits generalizing s with
  | nil => exact ⟨lo,hi⟩
  | cons bit tail ih =>
    exact ih (advance s bit) (advance_envelope s bit lo) (advance_coherent s bit hi)

/-- On a balanced word this is the integer numerator version of
beta + 1 ≤ 2*(3/2)^H, where H is the maximum prefix even surplus. -/
theorem balanced_carry (bits : List Bool) (balanced : (read start bits).evens=(read start bits).odds) :
    ((read start bits).num+(read start bits).den)*2^(read start bits).peak
      ≤ (2*(read start bits).den)*3^(read start bits).peak := by
  obtain ⟨bound,hr⟩ := after_word start bits (by simp [envelope,start]) (by rfl)
  unfold coherent at hr
  have level_eq : (read start bits).level=(read start bits).peak := by omega
  simpa [envelope,level_eq] using bound

/-- Exact raw edges also force the indicated source parities by reduction
modulo two. The chronological list determines the physical clock. -/
inductive Follows : List Bool → Nat → Nat → Prop where
  | nil (x : Nat) : Follows [] x x
  | cons {bit : Bool} {bits : List Bool} {x y q : Nat}
      (edge : 2*y = if bit then 3*x+1 else x) (tail : Follows bits y q) :
      Follows (bit::bits) x q

private theorem advance_affine {s : Account} {x y a : Nat} {bit : Bool}
    (edge : 2*y = if bit then 3*x+1 else x) (old : s.den*x=3^s.odds*a+s.num) :
    (advance s bit).den*y=3^(advance s bit).odds*a+(advance s bit).num := by
  cases bit with
  | false =>
    change 2*y=x at edge
    change (2*s.den)*y=3^s.odds*a+s.num
    calc
      _ = s.den*(2*y) := by ac_rfl
      _ = _ := by rw [edge,old]
  | true =>
    change 2*y=3*x+1 at edge
    change (2*s.den)*y=3^(s.odds+1)*a+(3*s.num+s.den)
    calc
      _ = s.den*(2*y) := by ac_rfl
      _ = s.den*(3*x+1) := by rw [edge]
      _ = 3*(s.den*x)+s.den := by grind
      _ = _ := by rw [old,Nat.pow_succ]; grind

theorem Follows.affine {bits : List Bool} {x q a : Nat} (path : Follows bits x q)
    (s : Account) (initial : s.den*x=3^s.odds*a+s.num) :
    (read s bits).den*q=3^(read s bits).odds*a+(read s bits).num := by
  induction path generalizing s with
  | nil => exact initial
  | cons edge _ ih => exact ih _ (advance_affine edge initial)

theorem denominator (bits : List Bool) (s : Account) :
    (read s bits).den = 2^bits.length*s.den := by
  induction bits generalizing s with
  | nil => simp [read]
  | cons bit bits ih =>
    rw [read,ih,List.length_cons,Nat.pow_succ]
    cases bit <;> simp [advance,Nat.mul_assoc]

/-- The rational relative-carry cutoff is tested using the same ordinary
source x and endpoint q. Its barrier inequality contains only integers. -/
theorem physical_barrier {bits : List Bool} {x q p r : Nat}
    (path : Follows bits x q)
    (balanced : (read start bits).evens=(read start bits).odds)
    (relative : (p*q)*2^bits.length ≤
       r*(2^bits.length*q-3^(read start bits).odds*x)) :
    (r+p*q)*2^(read start bits).peak ≤ (2*r)*3^(read start bits).peak := by
  let s := read start bits
  have den : s.den=2^bits.length := by simpa [s,start] using denominator bits start
  have pos : 0<s.den := by rw [den]; exact Nat.pow_pos (by decide)
  have aff : s.den*q=3^s.odds*x+s.num := path.affine start (by simp [start])
  have cut : (p*q)*s.den ≤ r*s.num := by
    change (p*q)*2^bits.length ≤ r*(2^bits.length*q-3^s.odds*x) at relative
    rw [←den,aff,Nat.add_sub_cancel_left] at relative
    exact relative
  have envelope_bound : (s.num+s.den)*2^s.peak ≤ (2*s.den)*3^s.peak := balanced_carry bits balanced
  have shifted : (r+p*q)*s.den ≤ r*(s.num+s.den) := by
    rw [Nat.add_mul,Nat.mul_add]
    omega
  have conclusion : ((r+p*q)*2^s.peak)*s.den ≤ ((2*r)*3^s.peak)*s.den := by
    calc
      _ = ((r+p*q)*s.den)*2^s.peak := by ac_rfl
      _ ≤ (r*(s.num+s.den))*2^s.peak := Nat.mul_le_mul_right _ shifted
      _ = r*((s.num+s.den)*2^s.peak) := by ac_rfl
      _ ≤ r*((2*s.den)*3^s.peak) := Nat.mul_le_mul_left _ envelope_bound
      _ = _ := by ac_rfl
  exact Nat.le_of_mul_le_mul_right conclusion pos

#print axioms advance_envelope
#print axioms advance_peak
#print axioms balanced_carry
#print axioms Follows.affine
#print axioms denominator
#print axioms physical_barrier

end Collatz.BalancedBarrier

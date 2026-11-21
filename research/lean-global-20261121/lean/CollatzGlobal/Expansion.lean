import CollatzGlobal.OrbitLift

/-! The ordinary expansion obstruction. The proof uses only natural-number
orbits and exact high-bit lifting; no signed trajectory is assumed legal. -/

open CollatzReverseBasin CollatzClosure

namespace CollatzGlobal

theorem orbit_zero (t : Nat) : orbit 0 t=0 := by
  induction t with
  | zero => rfl
  | succ t ih => simpa [orbit, shortcut] using ih

/-- The positive corrections in an actual shortcut word cannot lower its
linear contribution. -/
theorem orbit_linear_lower (n t : Nat) :
    3^(oddCount n t)*n ≤ 2^t*orbit n t := by
  induction t generalizing n with
  | zero => simp [orbit, oddCount]
  | succ t ih =>
    have h := ih (shortcut n)
    rcases Nat.mod_two_eq_zero_or_one n with he | ho
    · have hn : n=2*shortcut n := by unfold shortcut; split <;> omega
      simp only [orbit, oddCount, he, Nat.zero_add]
      have hm := Nat.mul_le_mul_left 2 h
      calc
        3^(oddCount (shortcut n) t)*n = 3^(oddCount (shortcut n) t)*(2*shortcut n) :=
          congrArg (fun z => 3^(oddCount (shortcut n) t)*z) hn
        _ = 2*(3^(oddCount (shortcut n) t)*shortcut n) := by grind
        _ ≤ 2*(2^t*orbit (shortcut n) t) := hm
        _ = 2^(t+1)*orbit (shortcut n) t := by grind
    · have hs : 3*n≤2*shortcut n := by unfold shortcut; split <;> omega
      have h1 := Nat.mul_le_mul_left (3^(oddCount (shortcut n) t)) hs
      have h2 := Nat.mul_le_mul_left 2 h
      simp only [orbit, oddCount, ho]
      calc
        3^(1+oddCount (shortcut n) t)*n = 3^(oddCount (shortcut n) t)*(3*n) := by
          rw [Nat.pow_add]
          simp
          grind
        _ ≤ 3^(oddCount (shortcut n) t)*(2*shortcut n) := h1
        _ = 2*(3^(oddCount (shortcut n) t)*shortcut n) := by grind
        _ ≤ 2*(2^t*orbit (shortcut n) t) := h2
        _ = 2^(t+1)*orbit (shortcut n) t := by grind

/-- A canonical binary representative has its endpoint in the canonical
ternary range corresponding to its actual odd count. -/
theorem canonical_endpoint_bound (n t : Nat) (hn : n<2^t) :
    orbit n t < 3^(oddCount n t) := by
  induction t generalizing n with
  | zero => simp [orbit, oddCount] at *; omega
  | succ t ih =>
    have hb : 0<2^t := Nat.pow_pos (by decide)
    have pow2 : 2^(t+1)=2*2^t := by grind
    rw [pow2] at hn
    rcases Nat.mod_two_eq_zero_or_one n with he | ho
    · have hs : shortcut n<2^t := by unfold shortcut; split <;> omega
      simpa [orbit, oddCount, he] using ih (shortcut n) hs
    · have hs : shortcut n<3*2^t := by unfold shortcut; split <;> omega
      have hq : shortcut n/2^t≤2 := by
        have hd : shortcut n/2^t<3 := (Nat.div_lt_iff_lt_mul hb).mpr hs
        omega
      have hr : shortcut n%2^t<2^t := Nat.mod_lt _ hb
      have e : shortcut n%2^t+2^t*(shortcut n/2^t)=shortcut n := Nat.mod_add_div _ _
      have lift := high_bit_lift (shortcut n%2^t) t (shortcut n/2^t)
      rw [e] at lift
      have small := ih (shortcut n%2^t) hr
      simp only [orbit, oddCount, ho]
      rw [lift.1, lift.2, Nat.pow_add]
      simp only [Nat.pow_one]
      generalize hquot : shortcut n/2^t=q at hq ⊢
      rcases (show q=0 ∨ q=1 ∨ q=2 by omega) with h0|h1|h2
      · rw [h0]; omega
      · rw [h1]; omega
      · rw [h2]; omega

/-- No actual expanding finite word can end in the residue one modulo
its full ternary multiplier. In particular, a finite expanding inverse
dictionary cannot cover every sufficiently large ordinary endpoint. -/
theorem expanding_endpoint_not_one_mod (n t : Nat)
    (hexpand : 2^t<3^(oddCount n t)) :
    orbit n t % 3^(oddCount n t) ≠ 1 := by
  intro bad
  have hb : 0<2^t := Nat.pow_pos (by decide)
  have hr : n%2^t<2^t := Nat.mod_lt _ hb
  have e : n%2^t+2^t*(n/2^t)=n := Nat.mod_add_div _ _
  have lift := high_bit_lift (n%2^t) t (n/2^t)
  rw [e] at lift
  have small := canonical_endpoint_bound (n%2^t) t hr
  have lower := orbit_linear_lower (n%2^t) t
  rw [lift.1, lift.2] at bad
  have hres : orbit (n%2^t) t % 3^(oddCount (n%2^t) t)=1 := by
    simpa [Nat.add_mod, Nat.mul_mod] using bad
  rw [Nat.mod_eq_of_lt small] at hres
  rw [hres] at lower
  rw [lift.2] at hexpand
  have zero : n%2^t=0 := by
    by_cases hz : n%2^t=0
    · exact hz
    · have hm := Nat.mul_le_mul_left (3^(oddCount (n%2^t) t)) (show 1≤n%2^t by omega)
      simp only [Nat.mul_one] at hm lower
      omega
  rw [zero, orbit_zero] at hres
  omega

end CollatzGlobal

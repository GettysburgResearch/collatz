import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace MersenneReset

private theorem twoModThree (n : ℕ) :
    2 ^ n % 3 = if n % 2 = 0 then 1 else 2 := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [pow_succ, Nat.mul_mod, ih]
    split <;> rename_i h <;> simp <;> omega

private theorem threeModEight (n : ℕ) :
    3 ^ n % 8 = if n % 2 = 0 then 1 else 3 := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [pow_succ, Nat.mul_mod, ih]
    split <;> rename_i h <;> simp <;> omega

private theorem twoModEightOfThreeLe (n : ℕ) (h : 3 ≤ n) : 2 ^ n % 8 = 0 := by
  obtain ⟨a, rfl⟩ := Nat.exists_eq_add_of_le h
  simp [pow_add]

private theorem odd_powers (m b k : ℕ) (hm : 0 < m)
    (h : 3 ^ m + 2 ^ b = 2 ^ (b + k) + 1) : b % 2 = 1 ∧ k % 2 = 1 := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : m ≠ 0)
  have z := congrArg (fun t : ℕ => t % 3) h
  change (3 ^ d.succ + 2^b) % 3 = (2^(b+k) + 1) % 3 at z
  rw [Nat.add_mod (3^d.succ), Nat.add_mod (2^(b+k)), pow_succ, Nat.mul_mod, twoModThree, twoModThree] at z
  split at z <;> split at z
  all_goals norm_num at z
  all_goals omega

private theorem oddSource (m b k : ℕ) (hm : m % 2 = 1)
    (hb : b % 2 = 1) (hk : k % 2 = 1)
    (h : 3 ^ m + 2 ^ b = 2 ^ (b + k) + 1) : m = 1 ∧ k = 1 := by
  have z := congrArg (fun t : ℕ => t % 8) h
  change (3 ^ m + 2 ^ b) % 8 = (2^(b+k) + 1) % 8 at z
  rw [Nat.add_mod (3^m), Nat.add_mod (2^(b+k)), threeModEight] at z
  simp only [show m % 2 ≠ 0 by omega, ↓reduceIte] at z
  have small : b + k < 3 := by
    by_contra! large
    rw [twoModEightOfThreeLe _ large] at z
    by_cases t : 3 ≤ b
    · rw [twoModEightOfThreeLe _ t] at z
      omega
    · obtain rfl : b = 1 := by omega
      norm_num at z
  obtain rfl : b = 1 := by omega
  obtain rfl : k = 1 := by omega
  have h3 : 3 ^ m = 3 ^ 1 := by norm_num at h ⊢; omega
  exact ⟨Nat.pow_right_injective (by decide : 2 ≤ 3) h3, rfl⟩

/-- A dyadic divisor of an odd square minus one is at most twice the larger
neighbour of the square root. The square root must exceed one. -/
theorem twoPowerOnOddSquare (z b : ℕ) (hz : 1 < z) (oddz : Odd z)
    (hd : 2 ^ b ∣ (z - 1) * (z + 1)) : 2 ^ b ≤ 2 * (z + 1) := by
  cases b with
  | zero => simp; omega
  | succ b =>
    obtain ⟨t, ht⟩ := oddz
    have zminus : z - 1 = 2 * t := by omega
    have zplus : z + 1 = 2 * (t + 1) := by omega
    rw [pow_succ] at hd ⊢
    by_cases hto : Odd t
    · have hdiv : 2 ^ b ∣ t * (z + 1) := by
        apply Nat.dvd_of_mul_dvd_mul_left (by decide : 0 < 2)
        simpa only [zminus, Nat.mul_assoc, Nat.mul_comm (2 ^ b) 2] using hd
      have hcop := (Nat.coprime_two_left.mpr hto).pow_left b
      have hle := Nat.le_of_dvd (show 0 < z + 1 by omega) (hcop.dvd_of_dvd_mul_left hdiv)
      omega
    · have hodd : Odd (t+1) := by
        rw [Nat.odd_iff] at hto ⊢
        omega
      have hdiv : 2 ^ b ∣ (t+1) * (z-1) := by
        apply Nat.dvd_of_mul_dvd_mul_left (by decide : 0 < 2)
        simpa only [zplus, Nat.mul_comm, Nat.mul_left_comm, Nat.mul_assoc] using hd
      have hcop := (Nat.coprime_two_left.mpr hodd).pow_left b
      have hle := Nat.le_of_dvd (show 0 < z - 1 by omega) (hcop.dvd_of_dvd_mul_left hdiv)
      omega

/-- Exponent form of every positive Mersenne-to-Mersenne transition containing
exactly one Syracuse step whose division exponent exceeds one. -/
theorem oneResetExponents (m b k : ℕ) (hm : 0 < m) (hb : 0 < b) (hk : 0 < k)
    (h : 3 ^ m + 2 ^ b = 2 ^ (b + k) + 1) :
    (m = 1 ∧ b = 1 ∧ k = 1) ∨ (m = 2 ∧ b = 3 ∧ k = 1) := by
  obtain ⟨ob, ok⟩ := odd_powers m b k hm h
  by_cases om : m % 2 = 1
  · obtain ⟨rfl, rfl⟩ := oddSource m b k om ob ok h
    rw [pow_add] at h
    norm_num at h
    have h2 : 2 ^ b = 2 ^ 1 := by norm_num; omega
    exact Or.inl ⟨rfl, Nat.pow_right_injective (by decide) h2, rfl⟩
  · let d := m / 2
    let j := (b + k) / 2
    have dm : m = d + d := by dsimp [d]; omega
    have jk : b + k = j + j := by dsimp [j]; omega
    let z := 3 ^ d
    let y := 2 ^ j
    have zd : 1 < z := by
      change 3 ^ 0 < 3 ^ d
      apply Nat.pow_lt_pow_right (by decide)
      dsimp [d]; omega
    have oz : Odd z := (by decide : Odd 3).pow
    have sq : z*z + 2^b = y*y + 1 := by
      simpa only [dm, jk, pow_add, z, y] using h
    have zb : 2^b ∣ (z-1)*(z+1) := by
      use 2^k-1
      have p : 0 < 2 ^ k := Nat.pow_pos (by decide)
      have hs : z*z + 2^b = 2^b * 2^k + 1 := by
        simpa only [dm, pow_add, z] using h
      have sm : z - 1 + 1 = z := by omega
      have pm : 2^k-1+1=2^k := by omega
      nlinarith only [hs, congrArg (fun t => t*(z+1)) sm,
        congrArg (fun t => 2^b*t) pm]
    have bound := twoPowerOnOddSquare z b zd oz zb
    have pb : 2 ≤ 2^b := by
      exact Nat.pow_le_pow_right (by decide : 0 < 2) (show 1 ≤ b by omega)
    have yz : z < y := by nlinarith
    have succ : y = z + 1 := by nlinarith [sq_nonneg (y-z-1 : ℤ)]
    have poweq : 2^j = 3^d+1 := succ
    have dj : d=1 := by
      have hg := congrArg (fun t : ℕ => t % 8) poweq
      change 2^j % 8 = (3^d+1)%8 at hg
      rw [Nat.add_mod, threeModEight] at hg
      have jl : j < 3 := by
        by_contra! h3
        rw [twoModEightOfThreeLe _ h3] at hg
        split at hg <;> norm_num at hg
      have pl : 2^j ≤ 2^2 := Nat.pow_le_pow_right (by decide) (by omega)
      have hle : 3^d ≤ 3^1 := by norm_num at pl ⊢; omega
      by_contra! hne
      have hd : 1 < d := by dsimp [d] at *; omega
      have := Nat.pow_lt_pow_right (by decide : 1 < 3) hd
      omega
    have mm : m=2 := by omega
    have yy : j=2 := Nat.pow_right_injective (by decide : 2 ≤ 2) (by simpa [dj] using poweq)
    obtain rfl : m = 2 := mm
    obtain rfl : b = 3 := by
      have x : 2 ^ b = 2 ^ 3 := by norm_num [dj, yy, y, z] at sq ⊢; omega
      exact Nat.pow_right_injective (by decide) x
    exact Or.inr ⟨rfl, rfl, by omega⟩

/-- A run of actual exponent-one odd equations, read in time order. -/
inductive Ones : ℕ → ℕ → ℕ → Prop where
  | nil (x : ℕ) : Ones 0 x x
  | cons {t x y z : ℕ} (first : 2*y = 3*x+1) (later : Ones t y z) :
      Ones (t+1) x z

theorem onesAffine {t x z : ℕ} (path : Ones t x z) :
    2^t*(z+1) = 3^t*(x+1) := by
  induction path with
  | nil x => simp
  | @cons t x y z first later ih =>
    have one : 2*(y+1) = 3*(x+1) := by omega
    calc
      2^(t+1)*(z+1) = 2*(2^t*(z+1)) := by rw [pow_succ]; ring
      _ = 2*(3^t*(y+1)) := by rw [ih]
      _ = 3^(t+1)*(x+1) := by
        rw [pow_succ]
        nlinarith only [congrArg (fun a : ℕ => 3^t*a) one]

private theorem doubled (t u : ℕ) : 2^(t+1)*u = 2*(2^t*u) := by
  rw [pow_succ]
  ring

private theorem oddFactorUnique {a b u v : ℕ} (hu : Odd u) (hv : Odd v)
    (eqn : 2^a*u = 2^b*v) : a=b := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => rfl
    | succ b =>
      rw [pow_zero, one_mul, doubled] at eqn
      obtain ⟨s,hs⟩ := hu
      omega
  | succ a ih =>
    cases b with
    | zero =>
      rw [pow_zero, one_mul, doubled] at eqn
      obtain ⟨s,hs⟩ := hv
      omega
    | succ b =>
      rw [doubled, doubled] at eqn
      exact congrArg Nat.succ (ih (by omega))

/-- Exact ordinary paths, with an arbitrary number of exponent-one odd steps
before and after the one transition whose exponent is at least two. -/
theorem physicalOneReset {m k b t s z y : ℕ}
    (hm : 0 < m) (hk : 0 < k) (hb : 0 < b)
    (pre : Ones t (2^m-1) z) (reset : 2^(b+1)*y=3*z+1)
    (post : Ones s y (2^k-1)) :
    (m=1 ∧ k=1 ∧ t=0 ∧ b=1 ∧ s=0) ∨
    (m=2 ∧ k=1 ∧ t=1 ∧ b=3 ∧ s=0) := by
  have km : 2^k-1+1 = 2^k := by have := Nat.pow_pos (by decide : 0<2) (n:=k); omega
  have mm : 2^m-1+1 = 2^m := by have := Nat.pow_pos (by decide : 0<2) (n:=m); omega
  have suffix := onesAffine post
  rw [km, ← pow_add] at suffix
  have sz : s=0 := by
    cases s with
    | zero => rfl
    | succ s =>
      have tri : 3 ∣ 2^(s.succ+k) := by
        rw [suffix, pow_succ]
        use 3^s*(y+1)
        ring
      have hr := Nat.mod_eq_zero_of_dvd tri
      rw [twoModThree] at hr
      split at hr <;> omega
  have yy : y=2^k-1 := by
    simp [sz] at suffix
    omega
  have hpref := onesAffine pre
  rw [mm] at hpref
  obtain ⟨c,hc⟩ : ∃ c, b=c+1 := ⟨b-1,by omega⟩
  have div4 : 4*(2^c*y) = 3*z+1 := by
    calc
      4*(2^c*y) = 2^(b+1)*y := by rw [hc, pow_succ, pow_succ]; ring
      _ = 3*z+1 := reset
  let w := (z+1)/2
  have zw : z+1=2*w := by dsimp [w]; omega
  have ow : Odd w := by rw [Nat.odd_iff]; dsimp [w]; omega
  have p2 : 2^(t+1)*w = 2^m*3^t := by
    calc
      2^(t+1)*w = 2^t*(2*w) := by rw [pow_succ]; ring
      _ = 3^t*2^m := by rw [← zw]; exact hpref
      _ = 2^m*3^t := by ring
  have tm := oddFactorUnique ow ((by decide : Odd 3).pow (n:=t)) p2
  rw [← tm] at p2
  have wt := Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide) (n:=t+1)) p2
  rw [wt] at zw
  have yk : y+1=2^k := by omega
  have eqn : 3^m+2^b = 2^(b+k)+1 := by
    rw [← tm, pow_succ 3, pow_add]
    rw [doubled] at reset
    nlinarith only [reset, zw, congrArg (fun a : ℕ => 2^b*a) yk]
  rcases oneResetExponents m b k hm hb hk eqn with a | a <;> omega

/-- The two remaining itineraries both occur on positive odd integers. -/
theorem bothPhysicalCasesOccur :
    (Ones 0 1 1 ∧ 2^(1+1)*1=3*1+1 ∧ Ones 0 1 1) ∧
    (Ones 1 3 5 ∧ 2^(3+1)*1=3*5+1 ∧ Ones 0 1 1) := by
  exact ⟨⟨.nil _, by decide, .nil _⟩, ⟨.cons (by decide) (.nil 5), by decide, .nil _⟩⟩

#print axioms twoModThree
#print axioms threeModEight
#print axioms twoModEightOfThreeLe
#print axioms odd_powers
#print axioms oddSource
#print axioms onesAffine
#print axioms doubled
#print axioms oddFactorUnique
#print axioms bothPhysicalCasesOccur
#print axioms physicalOneReset
#print axioms oneResetExponents
#print axioms twoPowerOnOddSquare

end MersenneReset

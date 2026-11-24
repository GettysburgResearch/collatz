import Std

/-! Arithmetic used to apply the unit equation theorem to actual mountain returns. -/
namespace MountainReturns

structure Run where
  oddSteps : Nat
  evenSteps : Nat

def up (b : Run) : Int := 3 ^ b.oddSteps
def halfUp (b : Run) : Int := 2 ^ b.oddSteps
def clock (b : Run) : Int := 2 ^ (b.oddSteps + b.evenSteps)

def oddProduct : List Run → Int
  | [] => 1
  | b :: bs => up b * oddProduct bs

def clockProduct : List Run → Int
  | [] => 1
  | b :: bs => clock b * clockProduct bs

/-- All signed carry terms are retained, including both ends of every odd run. -/
def atoms : List Run → List Int
  | [] => []
  | b :: bs =>
    up b * oddProduct bs :: -(halfUp b * oddProduct bs) ::
      (atoms bs).map (fun v => clock b * v)

inductive Path : List Run → Int → Int → Prop
  | nil (x) : Path [] x x
  | cons {b bs x y z}
      (step : clock b * y = up b * (x + 1) - halfUp b)
      (tail : Path bs y z) : Path (b :: bs) x z

private theorem scale_sum (u : Int) (xs : List Int) :
    (xs.map (fun v => u * v)).sum = u * xs.sum := by
  induction xs with
  | nil => simp
  | cons x xs ih => simp [ih, Int.mul_add]

theorem full_carry {bs : List Run} {x z : Int} (hp : Path bs x z) :
    clockProduct bs * z = oddProduct bs * x + (atoms bs).sum := by
  induction hp with
  | nil x => simp [oddProduct, clockProduct, atoms]
  | @cons b bs x y z hs _ ih =>
    simp only [oddProduct, clockProduct, atoms, List.sum_cons, scale_sum]
    calc
      clock b * clockProduct bs * z = clock b * (clockProduct bs * z) := Int.mul_assoc ..
      _ = clock b * (oddProduct bs * y + (atoms bs).sum) := by rw [ih]
      _ = oddProduct bs * (clock b * y) + clock b * (atoms bs).sum := by grind
      _ = _ := by rw [hs]; grind

/-- A signed atom has an odd coefficient, including when its sign is negative. -/
def dyadicAtom (a : Nat × Int) : Int := 2 ^ a.1 * (2 * a.2 + 1)

private theorem tail_divisible (a : Nat) (xs : List (Nat × Int))
    (h : ∀ v ∈ xs, a ≤ v.1) : (2 : Int) ^ a ∣ (xs.map dyadicAtom).sum := by
  induction xs with
  | nil => simp
  | cons v xs ih =>
    have hv := h v (by simp)
    have hx := ih (by intro u hu; exact h u (by simp [hu]))
    have dv : (2 : Int) ^ a ∣ dyadicAtom v := by
      obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le hv
      unfold dyadicAtom
      rw [hk, Int.pow_add]
      exact ⟨2 ^ k * (2 * v.2 + 1), Int.mul_assoc ..⟩
    simpa using Int.dvd_add dv hx

/-- Applies to every selected sublist, using its first retained atom. -/
theorem separated_sum_ne_zero (a : Nat) (c : Int) (xs : List (Nat × Int))
    (h : ∀ v ∈ xs, a < v.1) :
    dyadicAtom (a, c) + (xs.map dyadicAtom).sum ≠ 0 := by
  obtain ⟨k, hk⟩ := tail_divisible (a + 1) xs h
  simp only [dyadicAtom, hk, Int.pow_succ]
  have hn : (2 : Int) ^ a ≠ 0 := Int.pow_ne_zero (by decide)
  intro hz
  have he : (2 : Int) ^ a * (2 * c + 1 + 2 * k) = 0 := by grind
  have := (Int.mul_eq_zero.mp he).resolve_left hn
  omega

#print axioms full_carry
#print axioms separated_sum_ne_zero

/-- Uniform comparison at the exact odd-run length, for k at least two. -/
theorem ternary_square (j : Nat) :
    (3 : Int) ^ (j+2) ≤ (2 ^ (j+2) - 1 : Int) * (2 ^ (j+2) - 1) := by
  induction j with
  | zero => decide
  | succ j ih =>
    have h : 0 < (2 : Int) ^ (j+2) := Int.pow_pos (by decide)
    change (3 : Int) ^ ((j+2)+1) ≤
      (2 ^ ((j+2)+1) - 1 : Int) * (2 ^ ((j+2)+1) - 1)
    simp only [Int.pow_succ _ (j+2)]
    grind

/-- After clearing the powers, the whole common factor divides the carry. -/
theorem common_carry {x y u v t g : Int}
    (he : t*y + u = v*x + v) (hx : g ∣ x) (hy : g ∣ y) : g ∣ v-u := by
  obtain ⟨a, rfl⟩ := hx
  obtain ⟨b, rfl⟩ := hy
  exact ⟨t*b-v*a, by grind⟩

/-- Last step of the rank-one classification. The previous two arithmetic
lemmas and the odd-factor identity supply its clock and divisibility inputs. -/
theorem primitive_target {b s t K gap y : Nat}
    (hb : 3 ≤ b) (hs : 1 ≤ s) (ht : 1 ≤ t)
    (htarget : y = b ^ t) (hgap : 0 < gap) (hsmall : gap < b*b)
    (hdiv : b ^ min s t ∣ gap)
    (hclock : K ≤ b+1) (hpeak : s=1 → 2*y < K*(b+1)) : t=1 := by
  by_cases h : 2 ≤ t
  · have hlow : b*b ≤ y := by
      rw [htarget]
      simpa [Nat.pow_succ] using (Nat.pow_le_pow_of_le (a := b) (by omega) h :
        b ^ 2 ≤ b ^ t)
    have hfirst : s = 1 := by
      have hd := Nat.le_of_dvd hgap hdiv
      by_cases h' : 2 ≤ s
      · have hm : 2 ≤ min s t := by omega
        have hz := Nat.pow_le_pow_of_le (a := b) (by omega) hm
        simp [Nat.pow_succ] at hz
        omega
      · omega
    have hp := hpeak hfirst
    have hbound := Nat.mul_le_mul_right (b+1) hclock
    have hb' := Nat.mul_le_mul_right b hb
    simp only [Nat.add_mul, Nat.mul_add, Nat.one_mul, Nat.mul_one] at hbound hp
    omega
  · omega

#print axioms ternary_square
#print axioms common_carry
#print axioms primitive_target

/-- Integer form of the exceptional approximation to (3/2)^k. Here
U=2^k, W=3^k, b is the common base and c=(W-U)/b. -/
theorem exceptional_rounding {U W a b c : Nat}
    (ha : 1 ≤ a) (hbase : b+1=U*a) (hc : b*c+U=W) (hsq : W<U*U) :
    W+c=U*(a*c+1) ∧ U*c<W := by
  have hu : U ≤ b+1 := by
    rw [hbase]
    simpa using Nat.mul_le_mul_left U ha
  have hcu : c < U := by
    by_cases hh : U ≤ c
    · have hb := Nat.mul_le_mul_right U hu
      have hd := Nat.mul_le_mul_left b hh
      simp only [Nat.add_mul, Nat.one_mul] at hb
      omega
    · omega
  have hz := Nat.mul_le_mul_right c hu
  simp only [Nat.add_mul, Nat.one_mul] at hz
  constructor
  · calc
      W+c = (b+1)*c + U := by grind
      _ = U*(a*c+1) := by rw [hbase]; grind
  · omega

#print axioms exceptional_rounding

end MountainReturns

/-
Natural-number energy for finite source-witness prefix replacement.
Lean core only. These elementary inequalities do not assert a complete
Collatz certificate or the unresolved global closure.
-/
import Collatz.Closure

namespace CollatzWitnessEnergy

/-- Energy of the ordinary values preceding a common witness suffix. -/
def prefixEnergy (c : Nat) : List Nat → Nat
  | [] => 0
  | x :: xs => c ^ x + prefixEnergy c xs

@[simp] theorem prefixEnergy_nil (c : Nat) : prefixEnergy c [] = 0 := rfl

@[simp] theorem prefixEnergy_cons (c x : Nat) (xs : List Nat) :
    prefixEnergy c (x :: xs) = c ^ x + prefixEnergy c xs := rfl

@[simp] theorem prefixEnergy_append (c : Nat) (xs ys : List Nat) :
    prefixEnergy c (xs ++ ys) = prefixEnergy c xs + prefixEnergy c ys := by
  induction xs with
  | nil => simp [prefixEnergy]
  | cons x xs ih => simp [prefixEnergy, ih, Nat.add_assoc]

/-- Identical values may be cancelled as multisets; their order is irrelevant. -/
theorem prefixEnergy_perm {c : Nat} {xs ys : List Nat} (h : xs.Perm ys) :
    prefixEnergy c xs = prefixEnergy c ys := by
  induction h with
  | nil => rfl
  | cons x h ih => simp [prefixEnergy, ih]
  | swap x y xs => simp [prefixEnergy, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm]
  | trans h₁ h₂ ih₁ ih₂ => exact ih₁.trans ih₂

/-- Every list member contributes its complete nonnegative energy. -/
theorem pow_le_prefixEnergy_of_mem {c p : Nat} {xs : List Nat} (hp : p ∈ xs) :
    c ^ p ≤ prefixEnergy c xs := by
  induction xs with
  | nil => simp at hp
  | cons x xs ih =>
    rcases List.mem_cons.mp hp with h | h
    · subst p; simp [prefixEnergy]
    · have ht := ih h
      simp only [prefixEnergy]
      omega

/-- A uniform value bound gives a length times maximum-energy bound. -/
theorem prefixEnergy_le_length_mul_pow {c p : Nat} {xs : List Nat}
    (hc : 0 < c) (hbound : ∀ x ∈ xs, x ≤ p) :
    prefixEnergy c xs ≤ xs.length * c ^ p := by
  induction xs with
  | nil => simp [prefixEnergy]
  | cons x xs ih =>
    have hx : x ≤ p := hbound x (by simp)
    have hxs : ∀ y ∈ xs, y ≤ p := by
      intro y hy
      exact hbound y (by simp [hy])
    have hpow : c ^ x ≤ c ^ p := Nat.pow_le_pow_right hc hx
    have htail := ih hxs
    simp only [prefixEnergy, List.length_cons]
    calc
      c ^ x + prefixEnergy c xs ≤ c ^ p + xs.length * c ^ p :=
        Nat.add_le_add hpow htail
      _ = (xs.length + 1) * c ^ p := by
        rw [Nat.add_mul, Nat.one_mul, Nat.add_comm]

/-- Fewer than `c` values strictly below `p` have total energy below `c^p`. -/
theorem prefixEnergy_lt_pow {c p : Nat} {xs : List Nat}
    (hc : 0 < c) (hlen : xs.length < c)
    (hbelow : ∀ x ∈ xs, x < p) :
    prefixEnergy c xs < c ^ p := by
  cases p with
  | zero =>
    cases xs with
    | nil => simp [prefixEnergy]
    | cons x xs =>
      have impossible := hbelow x (by simp)
      omega
  | succ p =>
    have hbound : ∀ x ∈ xs, x ≤ p := by
      intro x hx
      have := hbelow x hx
      omega
    have hle := prefixEnergy_le_length_mul_pow hc hbound
    have hpow : 0 < c ^ p := Nat.pow_pos hc
    have hmul : xs.length * c ^ p < c * c ^ p :=
      Nat.mul_lt_mul_of_pos_right hlen hpow
    calc
      prefixEnergy c xs ≤ xs.length * c ^ p := hle
      _ < c * c ^ p := hmul
      _ = c ^ (p + 1) := by rw [Nat.pow_succ, Nat.mul_comm]

/-- Replacing a removed peak by fewer than `c` strictly smaller values
strictly decreases the energy, regardless of the other removed values. -/
theorem prefixEnergy_replacement_lt {c p : Nat} {removed inserted : List Nat}
    (hc : 0 < c) (hlen : inserted.length < c)
    (hp : p ∈ removed) (hbelow : ∀ x ∈ inserted, x < p) :
    prefixEnergy c inserted < prefixEnergy c removed :=
  Nat.lt_of_lt_of_le (prefixEnergy_lt_pow hc hlen hbelow)
    (pow_le_prefixEnergy_of_mem hp)

/-- The deleted witness tail is arbitrary and cancels exactly. -/
theorem prefixEnergy_replacement_lt_with_suffix {c p : Nat}
    {removed inserted : List Nat} (suffix : List Nat)
    (hc : 0 < c) (hlen : inserted.length < c)
    (hp : p ∈ removed) (hbelow : ∀ x ∈ inserted, x < p) :
    prefixEnergy c (inserted ++ suffix) < prefixEnergy c (removed ++ suffix) := by
  rw [prefixEnergy_append, prefixEnergy_append]
  exact Nat.add_lt_add_right (prefixEnergy_replacement_lt hc hlen hp hbelow) _

/-- Each inserted value may use a different removed dominator. A largest
removed value supplies a single common peak for the energy argument. -/
theorem prefixEnergy_dominated_lt {c : Nat} {removed inserted : List Nat}
    (hc : 0 < c) (hlen : inserted.length < c) (hne : removed ≠ [])
    (hdom : ∀ x ∈ inserted, ∃ y ∈ removed, x < y) :
    prefixEnergy c inserted < prefixEnergy c removed := by
  apply prefixEnergy_replacement_lt hc hlen (List.max_mem hne)
  intro x hx
  obtain ⟨y, hy, hxy⟩ := hdom x hx
  exact Nat.lt_of_lt_of_le hxy (List.le_max_of_mem hy)

/-- Reordering and cancelling a shared finite multiset also preserve the
strict comparison; this common part need not be a contiguous witness tail. -/
theorem prefixEnergy_cancelled_replacement_lt {c : Nat}
    {old new removed inserted common : List Nat}
    (hc : 0 < c) (hlen : inserted.length < c) (hne : removed ≠ [])
    (hold : old.Perm (removed ++ common))
    (hnew : new.Perm (inserted ++ common))
    (hdom : ∀ x ∈ inserted, ∃ y ∈ removed, x < y) :
    prefixEnergy c new < prefixEnergy c old := by
  rw [prefixEnergy_perm hold, prefixEnergy_perm hnew,
    prefixEnergy_append, prefixEnergy_append]
  exact Nat.add_lt_add_right (prefixEnergy_dominated_lt hc hlen hne hdom) _

/-- The independently screened finite program inserts at most eight values. -/
theorem prefixEnergy9_replacement_lt_with_suffix {p : Nat}
    {removed inserted : List Nat} (suffix : List Nat)
    (hlen : inserted.length ≤ 8) (hp : p ∈ removed)
    (hbelow : ∀ x ∈ inserted, x < p) :
    prefixEnergy 9 (inserted ++ suffix) < prefixEnergy 9 (removed ++ suffix) :=
  prefixEnergy_replacement_lt_with_suffix suffix (by decide) (by omega) hp hbelow

end CollatzWitnessEnergy

module
public import Mathlib.Data.Finset.Card
public import Mathlib.Algebra.BigOperators.Group.List.Basic
public import Mathlib.Data.Rat.Cast.Order
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.GCongr

@[expose] public section

namespace CollatzClockSlice

/- A list records the positive inverse exponents minus one, in reverse order.
Thus every natural list is admissible as a word of positive letters. -/
def clock (w : List ℕ) : ℕ := w.length + w.sum

def numerator : List ℕ → ℕ
  | [] => 0
  | a :: w => 2^(a+1) * numerator w + 3^w.length

lemma numerator_mod_two (a : ℕ) (w : List ℕ) : numerator (a::w) % 2 = 1 := by
  simp [numerator, pow_succ, Nat.add_mod, Nat.mul_mod, Nat.pow_mod]

lemma pow_two_odd_cancel {a b m n : ℕ}
    (hm : m%2=1) (hn : n%2=1) (he : 2^a*m=2^b*n) : a=b ∧ m=n := by
  have hab : a=b := by
    by_contra hne
    rcases lt_or_gt_of_ne hne with hlt | hgt
    · obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_lt hlt
      rw [hd] at he
      simp only [pow_add, pow_succ] at he
      have hp : 0 < 2^a := by positivity
      have he' : 2^a*m=2^a*(2*(2^d*n)) := by nlinarith [he]
      have hc := Nat.eq_of_mul_eq_mul_left hp he'
      have hm0 : m%2=0 := by simp [hc]
      omega
    · obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_lt hgt
      rw [hd] at he
      simp only [pow_add, pow_succ] at he
      have hp : 0 < 2^b := by positivity
      have he' : 2^b*n=2^b*(2*(2^d*m)) := by nlinarith [he]
      have hc := Nat.eq_of_mul_eq_mul_left hp he'
      have hn0 : n%2=0 := by simp [hc]
      omega
  subst b
  exact ⟨rfl, Nat.eq_of_mul_eq_mul_left (by positivity) he⟩

/-- The complete offset numerator and total clock reconstruct every letter.
No bound is placed on any letter or on the total clock. -/
theorem numerator_injective_fixed_length_sum {w v : List ℕ}
    (hl : w.length=v.length) (hs : w.sum=v.sum)
    (hn : numerator w=numerator v) : w=v := by
  induction w generalizing v with
  | nil =>
    have hv : v=[] := by simpa using hl.symm
    exact hv.symm
  | cons a w ih =>
    cases v with
    | nil => simp at hl
    | cons b v =>
      have hl' : w.length=v.length := by simpa using hl
      cases w with
      | nil =>
        have hv : v=[] := by simpa using hl'.symm
        subst v
        simp at hs
        subst b
        rfl
      | cons c w =>
        have hv : v ≠ [] := by
          intro he
          simp [he] at hl'
        have hoddv : numerator v % 2=1 := by
          cases v with
          | nil => contradiction
          | cons d v => exact numerator_mod_two d v
        have he : 2^(a+1)*numerator (c::w) = 2^(b+1)*numerator v := by
          simpa [numerator, hl'] using hn
        obtain ⟨hab, hnum⟩ := pow_two_odd_cancel (numerator_mod_two c w) hoddv he
        have hab' : a=b := by omega
        subst b
        have hs' : (c::w).sum=v.sum := by simpa using hs
        exact congrArg (List.cons a) (ih hl' hs' hnum)

/-- Exact real-offset localization, written without rational division:
`C + 2^A ≤ 3^k 2^(A-k)`. -/
theorem numerator_clock_bound (w : List ℕ) :
    numerator w + 2^(clock w) ≤ 3^w.length * 2^w.sum := by
  induction w with
  | nil => norm_num [numerator, clock]
  | cons a w ih =>
    have hm := Nat.mul_le_mul_left (2^(a+1)) ih
    have hpow : 1 ≤ 2^(a+w.sum) := Nat.one_le_pow _ _ (by omega)
    have hprod : 3^w.length ≤ 3^w.length * 2^(a+w.sum) := by
      simpa using Nat.mul_le_mul_left (3^w.length) hpow
    simp only [clock, List.length_cons, List.sum_cons] at *
    have hclock : w.length+1+(a+w.sum) = a+1+(w.length+w.sum) := by omega
    rw [hclock, pow_add]
    simp only [numerator, pow_succ]
    simp only [pow_succ, pow_add] at hm hprod
    simp only [pow_add]
    nlinarith

lemma numerator_lt (w : List ℕ) : numerator w < 3^w.length * 2^w.sum := by
  have hb := numerator_clock_bound w
  have hp : 0 < 2^(clock w) := by positivity
  omega

/-- Every complete fixed-clock residue slice has at most `2^(A-k)` words.
The theorem works for any finite collection, with no truncation of letters. -/
theorem fixed_clock_card_bound (S : Finset (List ℕ)) (k B r : ℕ)
    (hl : ∀ w ∈ S, w.length=k)
    (hs : ∀ w ∈ S, w.sum=B)
    (hr : ∀ w ∈ S, numerator w % 3^k=r) :
    S.card ≤ 2^B := by
  classical
  have hmap : Set.MapsTo (fun w => numerator w / 3^k) S (Finset.range (2^B)) := by
    intro w hw
    apply Finset.mem_range.mpr
    apply (Nat.div_lt_iff_lt_mul (by positivity : 0 < 3^k)).2
    have hb := numerator_lt w
    simpa [hl w hw, hs w hw, Nat.mul_comm] using hb
  have hinj : Set.InjOn (fun w => numerator w / 3^k) (S : Set (List ℕ)) := by
    intro w hw v hv he
    change numerator w / 3^k = numerator v / 3^k at he
    apply numerator_injective_fixed_length_sum
    · rw [hl w hw, hl v hv]
    · rw [hs w hw, hs v hv]
    · have hrem : numerator w % 3^k = numerator v % 3^k := by rw [hr w hw, hr v hv]
      have hwdiv := Nat.mod_add_div (numerator w) (3^k)
      have hvdiv := Nat.mod_add_div (numerator v) (3^k)
      rw [hrem, he] at hwdiv
      exact hwdiv.symm.trans hvdiv
  have hc := Finset.card_le_card_of_injOn _ hmap hinj
  simpa using hc

/-- A single complete total-clock slice contributes at most `(3/2)^k`
to its normalized ternary density. -/
theorem fixed_clock_mass_bound (S : Finset (List ℕ)) (k B r : ℕ)
    (hl : ∀ w ∈ S, w.length=k)
    (hs : ∀ w ∈ S, w.sum=B)
    (hr : ∀ w ∈ S, numerator w % 3^k=r) :
    (S.card : ℚ) * (3:ℚ)^k / 2^(k+B) ≤ (3/2:ℚ)^k := by
  have hc : (S.card : ℚ) ≤ (2:ℚ)^B := by
    exact_mod_cast fixed_clock_card_bound S k B r hl hs hr
  calc
    (S.card : ℚ) * (3:ℚ)^k / 2^(k+B)
      ≤ (2:ℚ)^B * 3^k / 2^(k+B) := by gcongr
    _ = (3/2:ℚ)^k := by
      rw [pow_add, div_pow]
      field_simp

#print axioms numerator_mod_two
#print axioms pow_two_odd_cancel
#print axioms numerator_injective_fixed_length_sum
#print axioms numerator_clock_bound
#print axioms numerator_lt
#print axioms fixed_clock_card_bound
#print axioms fixed_clock_mass_bound

end CollatzClockSlice

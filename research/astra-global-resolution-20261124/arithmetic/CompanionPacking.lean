import Std

/-! Integer congruences for the rational companion's bounded past and for
the repeated-trial alternative. The denominator of a positive phase is
cleared before constructing a path. -/
namespace CompanionPacking

def bit : Bool → Nat | false => 0 | true => 1
def clock (w : List Bool) : Nat := (w.map (fun e => 1 + bit e)).sum

/-- The chronological companion carries are integral with factor 3 on
every step and denominator 2 or 4 according to the observed bit. -/
def carry : List Bool → Nat
  | [] => 0
  | e :: w => 3^w.length * bit e + 2^(1+bit e) * carry w

inductive Walk (m : Nat) : List Bool → Nat → Nat → Prop where
  | nil (x) : Walk m [] x x
  | cons {e w x y z} (step : 2^(1+bit e)*y = 3*x+m*bit e)
      (tail : Walk m w y z) : Walk m (e::w) x z

theorem companion_affine {m w x z} (path : Walk m w x z) :
    2^(clock w)*z = 3^w.length*x + m*carry w := by
  induction path with
  | nil => simp [clock, carry]
  | @cons e w x y z step tail ih =>
    simp only [clock, List.map_cons, List.sum_cons, List.length_cons,
      carry, Nat.pow_add, Nat.pow_succ] at *
    grind

/-- Two bounded end numerators with a common ternary past coincide on
the same grid even when the initial states differ. -/
theorem bounded_past_unique {m w x y z t : _} (p : Walk m w x z)
    (q : Walk m w y t) (hz : z < 3^w.length) (ht : t < 3^w.length) : z=t := by
  have aux {i j u v : Nat} (pi : Walk m w i u) (pj : Walk m w j v)
      (hu : u ≤ v) (hv : v < 3^w.length) : u=v := by
    have hx := companion_affine pi
    have hy := companion_affine pj
    have hsum : 2^(clock w)*v - 2^(clock w)*u =
        3^w.length*j - 3^w.length*i := by omega
    rw [← Nat.mul_sub, ← Nat.mul_sub] at hsum
    have hd : 3^w.length ∣ 2^(clock w)*(v-u) := ⟨j-i, hsum⟩
    have cop := ((by decide : Nat.Coprime 3 2).pow_left w.length).pow_right (clock w)
    have hd' := cop.dvd_of_dvd_mul_left hd
    by_cases eq : u=v
    · exact eq
    · have hpos : 0 < v-u := by omega
      have := Nat.le_of_dvd hpos hd'
      omega
  rcases Nat.le_total z t with h | h
  · exact aux p q h ht
  · exact (aux q p h hz).symm

/-- Each bounded endpoint with a positive incoming floor forces enough
powers of two in its literal suffix. -/
theorem past_weight_test {m w x z B : _} (p : Walk m w x z)
    (hfloor : m ≤ 4*x) (hcap : z ≤ B*m) (hm : 0 < m) :
    3^w.length ≤ (4*B)*2^(clock w) := by
  have ha := companion_affine p
  have hp : (3^w.length)*m ≤ (3^w.length)*(4*x) :=
    Nat.mul_le_mul_left _ hfloor
  have hq := Nat.mul_le_mul_left (2^(clock w)) hcap
  have hmul : (3^w.length)*m ≤ ((4*B)*2^(clock w))*m := by grind
  exact Nat.le_of_mul_le_mul_right hmul hm

/-- If shifted actual starts agree on a suffix of the trial period and
are different, their size bounds the dyadic precision. -/
theorem repeated_trial_budget {n i j u v k : Nat} (hne : u ≠ v)
    (hb : 2^i*u ≤ 3^i*(n+1)) (hc : 2^j*v ≤ 3^j*(n+1))
    (shared : 2^k ∣ u-v ∧ 2^k ∣ v-u) :
    (2^i*2^k ≤ 3^i*(n+1)) ∨ (2^j*2^k ≤ 3^j*(n+1)) := by
  rcases Nat.lt_or_gt_of_ne hne with h | h
  · have hgap := Nat.le_of_dvd (show 0 < v-u by omega) shared.2
    exact Or.inr (Nat.le_trans (Nat.mul_le_mul_left _ (show 2^k ≤ v by omega)) hc)
  · have hgap := Nat.le_of_dvd (show 0 < u-v by omega) shared.1
    exact Or.inl (Nat.le_trans (Nat.mul_le_mul_left _ (show 2^k ≤ u by omega)) hb)

#print axioms companion_affine
#print axioms bounded_past_unique
#print axioms past_weight_test
#print axioms repeated_trial_budget

end CompanionPacking

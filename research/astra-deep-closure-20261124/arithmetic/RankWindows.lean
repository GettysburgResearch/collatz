import Std

/-! The unit-equation counts and the published verification floor are external
written inputs. These declarations certify the finite identities and the Farey
and counting implications at the numerical cutoff. -/
namespace RankWindows

/-- The list contains the actual powers of two stripped in consecutive odd steps. -/
inductive Path : Nat → List Nat → Nat → Prop where
  | nil (x : Nat) : Path x [] x
  | cons {x y z q qs} (h : q*y = 3*x+1) (tail : Path y qs z) : Path x (q::qs) z

/-- The first carry is constant and all later carries are prefix products. -/
def carry : List Nat → Nat
  | [] => 0
  | q :: qs => 3^qs.length + q*carry qs

theorem unroll {x y : Nat} {qs : List Nat} (h : Path x qs y) :
    qs.prod*y = 3^qs.length*x + carry qs := by
  induction h with
  | nil x => simp [carry]
  | @cons x u y q qs step _ ih =>
    simp only [List.prod_cons, List.length_cons, carry, Nat.pow_succ]
    calc
      q * qs.prod * y = q * (qs.prod*y) := by grind
      _ = q * (3^qs.length*u + carry qs) := by rw [ih]
      _ = 3^qs.length * (q*u) + q*carry qs := by grind
      _ = _ := by rw [step]; grind

/-- Signs rule out a zero subsum involving the largest term when the positive
constant has been isolated on the other side of a unit equation. -/
theorem no_cancellation {largest constant negatives part : Nat}
    (h : largest = constant+negatives) (hc : 0<constant) (hp : part≤negatives) :
    part < largest := by omega

theorem neighbors_coprime {x y q : Nat} (h : q*y = 3*x+1) : Nat.gcd x y = 1 := by
  have hx := Nat.gcd_dvd_left x y
  have hy := Nat.gcd_dvd_right x y
  have a : Nat.gcd x y ∣ 3*x := Nat.dvd_mul_left_of_dvd hx 3
  have b : Nat.gcd x y ∣ 3*x+1 := h ▸ Nat.dvd_mul_left_of_dvd hy q
  have c := Nat.dvd_sub b a
  simpa using c

/-- The contribution of long gaps to their total length bounds their count. -/
theorem gap_budget (H : Nat) (gs : List Nat) :
    (H+1)*(gs.filter (fun g => H<g)).length ≤ gs.sum := by
  induction gs with
  | nil => simp
  | cons g gs ih =>
    by_cases short : H<g
    · simp [short, Nat.mul_add]; omega
    · simp [short]; omega

theorem farey_between {a b c d u v : Nat} (det : c*b = a*d+1)
    (hl : a*v < b*u) (hr : d*u < c*v) : b+d ≤ v := by
  have one : a*v+1 ≤ b*u := hl
  have two : d*u+1 ≤ c*v := hr
  have left := Nat.mul_le_mul_left d one
  have right := Nat.mul_le_mul_left b two
  have ident : c*b*v = (a*d+1)*v := by rw [det]
  grind

theorem exact_period_floor {A p : Nat}
    (hl : 103768467013*p < 65470613321*A)
    (hr : 6586818670*A < 10439860591*p) : 72057431991 ≤ p := by
  exact farey_between (by decide) hl hr

theorem pell_edge (x y q : Int) (h : q*y=3*x+1) :
    (6*x+1)^2-1 = 12*q*x*y := by grind

theorem ratio_five_pell (x y z q t X : Int)
    (hy : q*y=3*x+1) (hz : t*z=15*x+1) (hX : 2*X=15*x+3) :
    4*(X^2-1)=5*q*t*y*z := by
  calc
    4*(X^2-1) = (2*X-2)*(2*X+2) := by grind
    _ = (15*x+1)*(5*(3*x+1)) := by rw [hX]; grind
    _ = _ := by rw [←hy, ←hz]; grind

theorem paired_first_two_exclusive (u v : Int) (hu : u%3=0) (hv : v%3=0) :
    2*u^2-1 ≠ v := by
  let k := u/3
  have e : u=3*k := by dsimp [k]; omega
  have f : 2*u^2-1=3*(6*k*k)-1 := by rw [e]; grind
  omega

def lucas (P : Int) : Nat → Int
  | 0 => 0
  | 1 => 1
  | n+2 => P*lucas P (n+1) - lucas P n

theorem sixth_factor (P : Int) :
    lucas P 6 = P*(P^2-1)*(P^2-3) := by simp [lucas]; grind

theorem first_two_exclusive (x z : Int) (hx : x%2=1) (hz : z%2=1) :
    2*(6*x+1)^2-1 ≠ 6*z+1 := by
  let k := x/2
  have e : x=2*k+1 := by dsimp [k]; omega
  have he : 2*(6*x+1)^2-1 = 4*(72*k*k+84*k+24)+1 := by rw [e]; grind
  omega

def isum (f : Nat → Int) : Nat → Int
  | 0 => 0
  | n+1 => isum f n + f n

private theorem zero_prefix (n : Nat) (f : Nat → Int) (h : ∀ i, i<n → f i=0) :
    isum f n=0 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [isum]
    rw [ih (by intro i hi; exact h i (by omega)), h n (by omega)]
    rfl

/-- Fresh-prime rows on the projected valuation vectors imply full independence. -/
theorem triangular_independence (n : Nat) (a : Nat → Nat → Int) (c : Nat → Int)
    (lower : ∀ j, j<n → ∀ i, i<j → a j i=0)
    (diag : ∀ j, j<n → a j j≠0)
    (relation : ∀ j, j<n → isum (fun i => c i*a j i) n=0) :
    ∀ i, i<n → c i=0 := by
  induction n with
  | zero => omega
  | succ n ih =>
    have last := relation n (by omega)
    simp only [isum] at last
    have z : isum (fun i => c i*a n i) n=0 := by
      apply zero_prefix
      intro i hi
      simp [lower n (by omega) i hi]
    rw [z, Int.zero_add] at last
    have cn : c n=0 := (Int.mul_eq_zero.mp last).resolve_right (diag n (by omega))
    have prev : ∀ j, j<n → isum (fun i => c i*a j i) n=0 := by
      intro j hj
      simpa [isum,cn] using relation j (by omega)
    have prior := ih (by intro j hj; exact lower j (by omega))
      (by intro j hj; exact diag j (by omega)) prev
    intro i hi
    by_cases eq : i=n
    · simpa [eq] using cn
    · exact prior i (by omega)

theorem cycle_rank_cutoffs (p m : Nat) (floor : 137500000000<p)
    (cover : p≤2*m+2^32*32) : p<5000*m := by omega

theorem thirty_rank_cutoff (p m : Nat) (floor : 137500000000<p)
    (cover : p≤2*m+2^31*31) : p<4*m := by omega

#print axioms unroll
#print axioms no_cancellation
#print axioms neighbors_coprime
#print axioms gap_budget
#print axioms farey_between
#print axioms exact_period_floor
#print axioms pell_edge
#print axioms ratio_five_pell
#print axioms paired_first_two_exclusive
#print axioms sixth_factor
#print axioms first_two_exclusive
#print axioms triangular_independence
#print axioms cycle_rank_cutoffs
#print axioms thirty_rank_cutoff
end RankWindows

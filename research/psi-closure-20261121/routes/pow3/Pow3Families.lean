/-
Route pow3 — the powers-of-three family.  Lean 4.34.1, core only, on top of the ψ-closure packet
(`research/psi-closure-20261121/lean`).  Standalone file; compile with the packet's oleans on
LEAN_PATH (see NOTES.md).

STATUS: `∀ i, Basin (3^i)` is NOT proved here.  It stays OPEN.

Normalization: `shortcut n = n/2` (n even), `(3n+1)/2` (n odd); `Basin n` = the orbit reaches 1.

Proved here (every theorem: axioms propext / Classical.choice / Quot.sound only):
  §1 `iter_add_pow`, `basin_shift`      linearity of iterates in the added multiple of `2^n`
  §2 `master`, `periodic_exchange`, `basin_steps`
                                        exchange over ℤ for every cycle and every odd denominator
     `basin_pow_eight_sub_five`, `basin_cycle_one_fifth`   two instances outside the packet
  §3 `pow_three_iff_shift_closure`      an equivalent form of the target
  §4 `basin_pow_three_odd`, `basin_mersenne_even/odd/pair`, `basin_pow_three_mersenne`
                                        powers of three and Mersenne numbers in repunit coordinates
  §5 `pow_three_pair_normal_form(_odd)`, `basin_pow_three_consecutive`, `basin_shift_to_one`
  §6 `basin_pow_three_dyadic_odd/even`  `3^(4^t u) ~ 3^(4^t u - 1)` for all `t ≥ 1` (unbounded depth)
  §7 `basin_adjacent_family`, `basin_pow_three_consecutive_gen`,
     `pow_three_mersenne_closure_pair`, `pow_three_pair_closure_form`

Overlap with concurrent work (statements read at the PR heads, not rebuilt here):
  * `basin_mersenne_pair` is PR #176 `mersenne_even_exponent_fold` (MersenneRecursion.lean).
  * `basin_iter` is PR #181 `basin_orbit`; the special cases of `iter_add_pow`/`master` at the fixed
    point -1 and at the cycle {1,2}, with odd counts, are PR #179 `ones_block`/`twos_block` and
    PR #181 `power_four_profile`.
  * PR #181 `paired_descent` transports a closure pair `(m, 3m-1)` through the {1,2}-cycle
    exchange; `pow_three_pair_normal_form_odd` is the same mechanism applied to `(3^(N-1), 3^N)`.
-/
import Collatz
open CollatzReverseBasin CollatzClosure

namespace CollatzPow3

/-! ## 1. Iterates and linearity over ℕ -/

/-- `n` ordinary steps. -/
def iter : Nat → Nat → Nat
  | 0, x => x
  | n+1, x => iter n (shortcut x)

/-- Number of odd steps among the first `n`. -/
def odds : Nat → Nat → Nat
  | 0, _ => 0
  | n+1, x => x % 2 + odds n (shortcut x)

theorem basin_iter (n : Nat) : ∀ x : Nat, Basin (iter n x) ↔ Basin x := by
  induction n with
  | zero => intro x; exact Iff.rfl
  | succ n ih => intro x; exact (ih (shortcut x)).trans (basin_step x)

theorem two_shortcut_even (y : Nat) (h : y % 2 = 0) : 2 * shortcut y = y := by
  unfold shortcut; split <;> omega

theorem two_shortcut_odd (y : Nat) (h : y % 2 = 1) : 2 * shortcut y = 3*y + 1 := by
  unfold shortcut; split <;> omega

theorem shortcut_add_even (x Y : Nat) (h : x % 2 = 0) : shortcut (x + 2*Y) = shortcut x + Y := by
  have a := two_shortcut_even (x + 2*Y) (by omega)
  have b := two_shortcut_even x h
  omega

theorem shortcut_add_odd (x Y : Nat) (h : x % 2 = 1) : shortcut (x + 2*Y) = shortcut x + 3*Y := by
  have a := two_shortcut_odd (x + 2*Y) (by omega)
  have b := two_shortcut_odd x h
  omega

/-- Linearity: `T^n (x + 2^n u) = T^n x + 3^(odd steps of x) u`. -/
theorem iter_add_pow (n : Nat) : ∀ x u : Nat,
    iter n (x + 2^n * u) = iter n x + 3^(odds n x) * u := by
  induction n with
  | zero => intro x u; simp [iter, odds]
  | succ n ih =>
    intro x u
    have e1 : 2^(n+1) * u = 2 * (2^n * u) := by grind
    show iter n (shortcut (x + 2^(n+1) * u))
        = iter n (shortcut x) + 3^(x % 2 + odds n (shortcut x)) * u
    rw [e1]
    rcases Nat.mod_two_eq_zero_or_one x with h | h
    · rw [shortcut_add_even x _ h, ih, h, Nat.zero_add]
    · have e2 : 3 * (2^n * u) = 2^n * (3 * u) := by grind
      have e3 : 3^(1 + odds n (shortcut x)) * u = 3^(odds n (shortcut x)) * (3 * u) := by grind
      rw [shortcut_add_odd x _ h, e2, ih, h, e3]

/-- Exchange at a natural base point. -/
theorem basin_shift (n x u : Nat) :
    Basin (x + 2^n * u) ↔ Basin (iter n x + 3^(odds n x) * u) := by
  rw [← iter_add_pow]
  exact (basin_iter n _).symm

/-! ## 2. Master exchange lemma over ℤ (every cycle, every odd denominator) -/

/-- The `3x+d` shortcut map on integers. -/
def Tz (d : Nat) (c : Int) : Int := if c % 2 = 0 then c / 2 else (3*c + d) / 2

def bitZ (c : Int) : Nat := if c % 2 = 0 then 0 else 1

def iterZ (d : Nat) : Nat → Int → Int
  | 0, c => c
  | n+1, c => iterZ d n (Tz d c)

def oddsZ (d : Nat) : Nat → Int → Nat
  | 0, _ => 0
  | n+1, c => bitZ c + oddsZ d n (Tz d c)

/-- If `d·y = 2^n·w + c` with `d` odd, then `d·T^n(y) = 3^o·w + c'`, where `c'` is the `n`-th
iterate of `c` under the `3x+d` map and `o` its number of odd steps. -/
theorem master (d : Nat) (hd : d % 2 = 1) (n : Nat) : ∀ (y : Nat) (w c : Int),
    ((d * y : Nat) : Int) = 2^n * w + c →
    ((d * iter n y : Nat) : Int) = 3^(oddsZ d n c) * w + iterZ d n c := by
  induction n with
  | zero =>
    intro y w c h
    have h0 : (2:Int)^0 * w + c = 3^0 * w + c := by simp
    exact h.trans h0
  | succ n ih =>
    intro y w c h
    have e1 : (2:Int)^(n+1) * w = 2 * (2^n * w) := by grind
    rw [e1] at h
    have hpar : (d * y) % 2 = y % 2 := by
      rw [Nat.mul_mod, hd]; omega
    have hcc : c % 2 = 0 ∨ c % 2 = 1 := by omega
    show ((d * iter n (shortcut y) : Nat) : Int)
        = 3^(bitZ c + oddsZ d n (Tz d c)) * w + iterZ d n (Tz d c)
    rcases hcc with hc | hc
    · have hy : y % 2 = 0 := by
        generalize (2:Int)^n * w = W at h
        generalize d * y = Z at h hpar
        omega
      have hT : Tz d c = c / 2 := by unfold Tz; split <;> omega
      have hb : bitZ c = 0 := by unfold bitZ; split <;> omega
      have hZ : 2 * (d * shortcut y) = d * y := by
        rw [Nat.mul_left_comm, two_shortcut_even y hy]
      have hIH : ((d * shortcut y : Nat) : Int) = 2^n * w + Tz d c := by
        rw [hT]
        generalize (2:Int)^n * w = W at h ⊢
        generalize d * shortcut y = Z' at hZ ⊢
        generalize d * y = Z at h hZ
        omega
      rw [ih (shortcut y) w (Tz d c) hIH, hb, Nat.zero_add]
    · have hy : y % 2 = 1 := by
        generalize (2:Int)^n * w = W at h
        generalize d * y = Z at h hpar
        omega
      have hT : Tz d c = (3*c + d) / 2 := by unfold Tz; split <;> omega
      have hb : bitZ c = 1 := by unfold bitZ; split <;> omega
      have hZ : 2 * (d * shortcut y) = 3 * (d * y) + d := by
        rw [Nat.mul_left_comm, two_shortcut_odd y hy]; grind
      have e2 : (2:Int)^n * (3 * w) = 3 * (2^n * w) := by grind
      have hIH : ((d * shortcut y : Nat) : Int) = 2^n * (3*w) + Tz d c := by
        rw [hT, e2]
        generalize (2:Int)^n * w = W at h ⊢
        generalize d * shortcut y = Z' at hZ ⊢
        generalize d * y = Z at h hZ
        omega
      have e3 : (3:Int)^(1 + oddsZ d n (Tz d c)) * w = 3^(oddsZ d n (Tz d c)) * (3 * w) := by
        grind
      rw [ih (shortcut y) (3*w) (Tz d c) hIH, hb, e3]

theorem basin_of_master (d : Nat) (hd : d % 2 = 1) (n y y' : Nat) (w c : Int)
    (h : ((d * y : Nat) : Int) = 2^n * w + c)
    (h' : ((d * y' : Nat) : Int) = 3^(oddsZ d n c) * w + iterZ d n c) :
    Basin y ↔ Basin y' := by
  have m := master d hd n y w c h
  rw [← h'] at m
  have e0 : d * iter n y = d * y' := Int.ofNat.inj m
  have e : iter n y = y' := Nat.eq_of_mul_eq_mul_left (by omega) e0
  rw [← e]
  exact (basin_iter n y).symm

theorem iterZ_add (d a b : Nat) : ∀ c : Int, iterZ d (a + b) c = iterZ d b (iterZ d a c) := by
  induction a with
  | zero =>
    intro c
    show iterZ d (0 + b) c = iterZ d b c
    rw [Nat.zero_add]
  | succ a ih =>
    intro c
    have e : a + 1 + b = (a + b) + 1 := by omega
    rw [e]
    exact ih (Tz d c)

theorem oddsZ_add (d a b : Nat) : ∀ c : Int,
    oddsZ d (a + b) c = oddsZ d a c + oddsZ d b (iterZ d a c) := by
  induction a with
  | zero =>
    intro c
    show oddsZ d (0 + b) c = 0 + oddsZ d b c
    simp only [Nat.zero_add]
  | succ a ih =>
    intro c
    have e : a + 1 + b = (a + b) + 1 := by omega
    rw [e]
    show bitZ c + oddsZ d (a + b) (Tz d c)
        = (bitZ c + oddsZ d a (Tz d c)) + oddsZ d b (iterZ d a (Tz d c))
    rw [ih (Tz d c)]; omega

theorem iterZ_period (d p : Nat) (c : Int) (hper : iterZ d p c = c) (k : Nat) :
    iterZ d (p * k) c = c ∧ oddsZ d (p * k) c = oddsZ d p c * k := by
  induction k with
  | zero =>
    show iterZ d 0 c = c ∧ oddsZ d 0 c = oddsZ d p c * 0
    exact ⟨rfl, rfl⟩
  | succ k ih =>
    have e : p * (k + 1) = p * k + p := Nat.mul_succ p k
    rw [e, iterZ_add, oddsZ_add, ih.1, ih.2, hper]
    exact ⟨rfl, (Nat.mul_succ _ _).symm⟩

/-- Periodic exchange: if `c` is `p`-periodic under the `3x+d` map with `o` odd steps per period,
then `(2^(pk) w + c)/d` and `(3^(ok) w + c)/d` are in the same component, for every `k`. -/
theorem periodic_exchange (d : Nat) (hd : d % 2 = 1) (p : Nat) (c : Int)
    (hper : iterZ d p c = c) (k y y' : Nat) (w : Int)
    (h : ((d * y : Nat) : Int) = 2^(p*k) * w + c)
    (h' : ((d * y' : Nat) : Int) = 3^(oddsZ d p c * k) * w + c) :
    Basin y ↔ Basin y' := by
  have per := iterZ_period d p c hper k
  apply basin_of_master d hd (p*k) y y' w c h
  rw [per.1, per.2]
  exact h'

/-- Finite-step certificate on a residue class: `y = 2^n w + c`, `y' = 3^o w + c'`. -/
theorem basin_steps (n y y' : Nat) (w c : Int) (o : Nat) (c' : Int)
    (ho : oddsZ 1 n c = o) (hc' : iterZ 1 n c = c')
    (h : (y : Int) = 2^n * w + c) (h' : (y' : Int) = 3^o * w + c') : Basin y ↔ Basin y' := by
  apply basin_of_master 1 (by decide) n y y' w c
  · rw [Nat.one_mul]; exact h
  · rw [Nat.one_mul, ho, hc']; exact h'

/-! ### Two instances of `periodic_exchange` beyond the packet's cycles -/

theorem three_pow_two_mul (j : Nat) : 3^(2*j) = 9^j := by
  have h := Nat.pow_mul 3 2 j
  have e : (3:Nat)^2 = 9 := rfl
  rw [e] at h
  exact h

theorem eight_pow (k : Nat) : (8:Nat)^k = 2^(3*k) := by
  have h := Nat.pow_mul 2 3 k
  have e : (2:Nat)^3 = 8 := rfl
  rw [e] at h
  exact h.symm

/-- Cycle `-5 → -7 → -10 → -5`: `8^k u - 5 ~ 9^k u - 5`. -/
theorem basin_pow_eight_sub_five (k u : Nat) (hu : 5 ≤ 8^k * u) :
    Basin (8^k * u - 5) ↔ Basin (9^k * u - 5) := by
  have hper : iterZ 1 3 (-5) = -5 := by decide
  have ho : oddsZ 1 3 (-5) = 2 := by decide
  have hle : 8^k * u ≤ 9^k * u := Nat.mul_le_mul_right u (Nat.pow_le_pow_left (by omega) k)
  rw [eight_pow, ← three_pow_two_mul] at hle
  rw [eight_pow] at hu
  apply periodic_exchange 1 (by decide) 3 (-5) hper k _ _ (u : Int)
  · rw [Nat.one_mul, eight_pow]
    have hc : ((2^(3*k) * u : Nat) : Int) = 2^(3*k) * (u : Int) := by simp
    rw [← hc]
    generalize 2^(3*k) * u = Q at hu ⊢
    omega
  · rw [Nat.one_mul, ho, ← three_pow_two_mul]
    have hc : ((3^(2*k) * u : Nat) : Int) = 3^(2*k) * (u : Int) := by simp
    rw [← hc]
    generalize 3^(2*k) * u = Q' at hle ⊢
    generalize 2^(3*k) * u = Q at hu hle
    omega

/-- Rational cycle `1/5 → 4/5 → 2/5 → 1/5`: `(8^k w + 1)/5 ~ (3^k w + 1)/5`. -/
theorem basin_cycle_one_fifth (k y y' w : Nat) (h : 5*y = 8^k*w + 1) (h' : 5*y' = 3^k*w + 1) :
    Basin y ↔ Basin y' := by
  have hper : iterZ 5 3 1 = 1 := by decide
  have ho : oddsZ 5 3 1 = 1 := by decide
  rw [eight_pow] at h
  apply periodic_exchange 5 (by decide) 3 1 hper k y y' (w : Int)
  · rw [h]; simp
  · rw [h', ho, Nat.one_mul]; simp

/-! ## 3. An equivalent form of the target -/

theorem iter_one_even (k : Nat) : iter (2*k) 1 = 1 ∧ odds (2*k) 1 = k := by
  induction k with
  | zero => exact ⟨rfl, rfl⟩
  | succ k ih =>
    have e : 2*(k+1) = 2*k + 1 + 1 := by omega
    have s1 : shortcut 1 = 2 := rfl
    have s2 : shortcut 2 = 1 := rfl
    rw [e]
    constructor
    · show iter (2*k) (shortcut (shortcut 1)) = 1
      rw [s1, s2]; exact ih.1
    · show 1 % 2 + (shortcut 1 % 2 + odds (2*k) (shortcut (shortcut 1))) = k + 1
      rw [s1, s2, ih.2]; omega

/-- `∀ i, 3^i ∈ C` ⟺ `C` is closed under `x ↦ x + 2^n` at every time `n` at which the orbit of
`x` sits at 1. -/
theorem pow_three_iff_shift_closure :
    (∀ i : Nat, Basin (3^i)) ↔ (∀ x n : Nat, iter n x = 1 → Basin (x + 2^n)) := by
  constructor
  · intro H x n hx
    have h := basin_shift n x 1
    rw [hx, Nat.mul_one, Nat.mul_one] at h
    rw [h]
    cases ho : odds n x with
    | zero =>
      show Basin 2
      exact ⟨1, rfl⟩
    | succ o =>
      have e : 1 + 3^(o+1) = 3 * 3^o + 1 := by grind
      rw [e]
      exact (basin_odd (3^o) (three_pow_odd o)).mpr (H o)
  · intro H i
    have h1 := H 1 (2*(i+1)) (iter_one_even (i+1)).1
    have e4 : 2^(2*(i+1)) = (2^2)^(i+1) := Nat.pow_mul 2 2 (i+1)
    have e5 : (2:Nat)^2 = 4 := rfl
    rw [e5] at e4
    rw [e4, Nat.add_comm] at h1
    exact (basin_four_pow_succ_iff_three_pow i).mp h1

/-! ## 4. Repunit coordinates: `σ_j = (9^j - 1)/8` -/

theorem nine_pow_mod_eight (j : Nat) : 9^j % 8 = 1 := by
  induction j with
  | zero => rfl
  | succ j ih => rw [Nat.pow_succ]; omega

/-- `σ_j ≡ j (mod 8)`. -/
theorem repunit_mod_eight (j : Nat) : ((9^j - 1)/8) % 8 = j % 8 := by
  induction j with
  | zero => rfl
  | succ j ih =>
    have hm := nine_pow_mod_eight j
    rw [Nat.pow_succ]
    generalize 9^j = X at ih hm ⊢
    omega

theorem three_mul_pow_odd (j : Nat) : 3 * 3^(2*j+1) = 9^(j+1) := by
  have h := three_pow_two_mul (j+1)
  have e2 : 2*(j+1) = (2*j+1)+1 := by omega
  have p : 3^((2*j+1)+1) = 3^(2*j+1) * 3 := by rw [Nat.pow_succ]
  rw [e2, p] at h
  omega

/-- `3^(2j+1) ~ 4σ_{j+1} + 1`  (and `3^(2j) = 8σ_j + 1` on the nose). -/
theorem basin_pow_three_odd (j : Nat) :
    Basin (3^(2*j+1)) ↔ Basin (4 * ((9^(j+1) - 1)/8) + 1) := by
  have hm := nine_pow_mod_eight (j+1)
  have hodd := three_pow_odd (2*j+1)
  have e := three_mul_pow_odd j
  have hs : shortcut (3^(2*j+1)) = 4 * ((9^(j+1) - 1)/8) + 1 := by
    have h2 := two_shortcut_odd _ hodd
    generalize 9^(j+1) = X at e hm ⊢
    generalize 3^(2*j+1) = P at e h2 ⊢
    omega
  rw [← hs]
  exact (basin_step _).symm

/-- `2^(2j+2) - 1 ~ σ_{j+1}`. -/
theorem basin_mersenne_even (j : Nat) :
    Basin (2^(2*j+2) - 1) ↔ Basin ((9^(j+1) - 1)/8) := by
  have hA := basin_pow_two_pred (2*j+2) 1 (by omega)
  rw [Nat.mul_one, Nat.mul_one] at hA
  have hm := nine_pow_mod_eight (j+1)
  have e : 3^(2*j+2) = 9^(j+1) := three_pow_two_mul (j+1)
  rw [e] at hA
  generalize 9^(j+1) = X at hA hm ⊢
  have h1 : Basin (X - 1) ↔ Basin ((X - 1)/8) :=
    basin_steps 3 _ _ (((X - 1)/8 : Nat) : Int) 0 0 0 (by decide) (by decide) (by omega) (by omega)
  exact hA.trans h1

/-- `2^(2j+1) - 1 ~ σ_{j+1}`. -/
theorem basin_mersenne_odd (j : Nat) :
    Basin (2^(2*j+1) - 1) ↔ Basin ((9^(j+1) - 1)/8) := by
  have hB := basin_pow_two_pred (2*j+1) 1 (by omega)
  rw [Nat.mul_one, Nat.mul_one] at hB
  have hm := nine_pow_mod_eight (j+1)
  have e := three_mul_pow_odd j
  generalize 9^(j+1) = X at e hm ⊢
  generalize 3^(2*j+1) = P at e hB
  have h1 : Basin (P - 1) ↔ Basin ((X - 1)/8) :=
    basin_steps 3 _ _ (((P - 3)/8 : Nat) : Int) 2 1 1 (by decide) (by decide) (by omega) (by omega)
  exact hB.trans h1

/-- Mersenne exponents `2j+1` and `2j+2` share a component. -/
theorem basin_mersenne_pair (j : Nat) : Basin (2^(2*j+2) - 1) ↔ Basin (2^(2*j+1) - 1) :=
  (basin_mersenne_even j).trans (basin_mersenne_odd j).symm

theorem basin_four_succ_odd (x : Nat) (hx : x % 2 = 1) : Basin (4*x+1) ↔ Basin x :=
  (basin_exch (4*x+1) (3*x+1) x rfl rfl).trans (basin_odd x hx)

/-- `3^(4k+1) ~ 2^(4k+2) - 1` (hence also `~ 2^(4k+1) - 1`). -/
theorem basin_pow_three_mersenne (k : Nat) : Basin (3^(4*k+1)) ↔ Basin (2^(4*k+2) - 1) := by
  have h1 := basin_pow_three_odd (2*k)
  have h2 := basin_mersenne_even (2*k)
  have hodd : ((9^(2*k+1) - 1)/8) % 2 = 1 := by
    have := repunit_mod_eight (2*k+1); omega
  have e1 : 2*(2*k)+1 = 4*k+1 := by omega
  have e2 : 2*(2*k)+2 = 4*k+2 := by omega
  rw [e1] at h1
  rw [e2] at h2
  exact h1.trans ((basin_four_succ_odd _ hodd).trans h2.symm)

/-! ## 5. Consecutive powers of three after the structured phase -/

/-- Normal form.  If `3^N = 1 + 4^s q` with `s ≥ 1`, put `w = 3^(s-1) q`.  Then
`3^N ~ 3w + 1` and `3^(N-1) ~ 2w + 1`.  The depth of this identity grows with `s`. -/
theorem pow_three_pair_normal_form (N s q : Nat) (hN : 1 ≤ N) (hs : 1 ≤ s)
    (h : 3^N = 1 + 4^s * q) :
    (Basin (3^N) ↔ Basin (3 * (3^(s-1) * q) + 1)) ∧
    (Basin (3^(N-1)) ↔ Basin (2 * (3^(s-1) * q) + 1)) := by
  obtain ⟨s', rfl⟩ : ∃ s', s = s' + 1 := ⟨s - 1, by omega⟩
  obtain ⟨N', rfl⟩ : ∃ N', N = N' + 1 := ⟨N - 1, by omega⟩
  have es : s' + 1 - 1 = s' := by omega
  have eN : N' + 1 - 1 = N' := by omega
  rw [es, eN]
  constructor
  · have h1 := basin_pow_four_succ (s'+1) q
    have e1 : 4^(s'+1) * q + 1 = 3^(N'+1) := by
      generalize 4^(s'+1) * q = A at h ⊢
      omega
    have e2 : 3^(s'+1) * q + 1 = 3 * (3^s' * q) + 1 := by grind
    rw [e1, e2] at h1
    exact h1
  · have hodd := three_pow_odd N'
    have h2 := two_shortcut_odd _ hodd
    have e3 : 3^(N'+1) = 3 * 3^N' := by rw [Nat.pow_succ]; omega
    have e4 : 4^(s'+1) * q = 2 * (4^s' * (2*q)) := by grind
    have hsc : shortcut (3^N') = 4^s' * (2*q) + 1 := by
      rw [e3, e4] at h
      generalize 4^s' * (2*q) = A at h ⊢
      generalize 3^N' = P at h h2 ⊢
      omega
    have h1 := basin_pow_four_succ s' (2*q)
    have e5 : 3^s' * (2*q) + 1 = 2 * (3^s' * q) + 1 := by grind
    rw [← hsc, e5] at h1
    exact (basin_step _).symm.trans h1

/-- Class certificate: for `w ≡ 1 (mod 8)`, `3w+1` and `2w+1` meet at `9⌊w/8⌋ + 2`. -/
theorem basin_three_two_mod8 (w : Nat) (hw : w % 8 = 1) : Basin (3*w+1) ↔ Basin (2*w+1) := by
  have h1 : Basin (3*w+1) ↔ Basin (9*(w/8) + 2) :=
    basin_steps 3 _ _ ((3*(w/8) : Nat) : Int) 4 1 2 (by decide) (by decide) (by omega) (by omega)
  have h2 : Basin (2*w+1) ↔ Basin (9*(w/8) + 2) :=
    basin_steps 4 _ _ ((w/8 : Nat) : Int) 3 2 2 (by decide) (by decide) (by omega) (by omega)
  exact h1.trans h2.symm

/-- Consecutive powers of three share a component whenever `3^N = 1 + 4^s q` with
`3^(s-1) q ≡ 1 (mod 8)`.  One statement for all `s`; the number of steps is `2s + 3`. -/
theorem basin_pow_three_consecutive (N s q : Nat) (hN : 1 ≤ N) (hs : 1 ≤ s)
    (h : 3^N = 1 + 4^s * q) (hw : (3^(s-1) * q) % 8 = 1) :
    Basin (3^N) ↔ Basin (3^(N-1)) := by
  have nf := pow_three_pair_normal_form N s q hN hs h
  exact nf.1.trans ((basin_three_two_mod8 _ hw).trans nf.2.symm)

/-- The same normal form when `3^N - 1` has odd 2-adic order: `3^N = 1 + 2·4^s q`.
(The pair transport `(m, 3m-1) ↦ (u, 3u-1)` of PR #181 is the same mechanism in another form.) -/
theorem pow_three_pair_normal_form_odd (N s q : Nat) (hN : 1 ≤ N)
    (h : 3^N = 1 + 2 * (4^s * q)) :
    (Basin (3^N) ↔ Basin (2 * (3^s * q) + 1)) ∧
    (Basin (3^(N-1)) ↔ Basin (3^s * q + 1)) := by
  obtain ⟨N', rfl⟩ : ∃ N', N = N' + 1 := ⟨N - 1, by omega⟩
  have eN : N' + 1 - 1 = N' := by omega
  rw [eN]
  constructor
  · have h1 := basin_pow_four_succ s (2*q)
    have e0 : 4^s * (2*q) = 2 * (4^s * q) := by grind
    have e1 : 4^s * (2*q) + 1 = 3^(N'+1) := by
      rw [e0]
      generalize 4^s * q = A at h ⊢
      omega
    have e2 : 3^s * (2*q) + 1 = 2 * (3^s * q) + 1 := by grind
    rw [e1, e2] at h1
    exact h1
  · have hodd := three_pow_odd N'
    have h2 := two_shortcut_odd _ hodd
    have e3 : 3^(N'+1) = 3 * 3^N' := by rw [Nat.pow_succ]; omega
    have hsc : shortcut (3^N') = 4^s * q + 1 := by
      rw [e3] at h
      generalize 4^s * q = A at h ⊢
      generalize 3^N' = P at h h2 ⊢
      omega
    have h1 := basin_pow_four_succ s q
    rw [← hsc] at h1
    exact (basin_step _).symm.trans h1

/-- Exchange invariant.  If the orbit of `x` sits at 1 at time `n` after `o` odd steps, then
`x + 2^n u ~ 4^o u + 1`: a perturbation `Δ = 2^n u` of `x` is carried to `1 + 2^(2o-n) Δ`. -/
theorem basin_shift_to_one (n x u : Nat) (hx : iter n x = 1) :
    Basin (x + 2^n * u) ↔ Basin (4^(odds n x) * u + 1) := by
  have h := basin_shift n x u
  have e : iter n x + 3^(odds n x) * u = 3^(odds n x) * u + 1 := by rw [hx]; omega
  rw [e] at h
  exact h.trans (basin_pow_four_succ (odds n x) u).symm

/-! ## 6. An infinite family of exponent classes with `3^N ~ 3^(N-1)`, of unbounded depth -/

/-- `3^(4^(t+1)) = 1 + 4^(t+2) e` with `e ≡ 5 (mod 8)`. -/
theorem three_pow_four_pow (t : Nat) : ∃ e, 3^(4^(t+1)) = 1 + 4^(t+2) * e ∧ e % 8 = 5 := by
  induction t with
  | zero => exact ⟨5, by decide, by decide⟩
  | succ t ih =>
    obtain ⟨e, he, hm⟩ := ih
    have p4 : 4^(t+1+1) = 4^(t+1) * 2 * 2 := by
      have p : 4^(t+1+1) = 4^(t+1) * 4 := by rw [Nat.pow_succ]
      omega
    have e1 : 3^(4^(t+1+1)) = ((3^(4^(t+1)))^2)^2 := by
      rw [p4, Nat.pow_mul, Nat.pow_mul]
    have s1 : (1 + 4^(t+2) * e)^2 = 1 + 32 * 4^t * (e + 8 * (4^t * e^2)) := by grind
    have s2 : (1 + 32 * 4^t * (e + 8 * (4^t * e^2)))^2
        = 1 + 4^(t+1+2) * ((e + 8 * (4^t * e^2)) + 16 * (4^t * (e + 8 * (4^t * e^2))^2)) := by
      grind
    refine ⟨(e + 8 * (4^t * e^2)) + 16 * (4^t * (e + 8 * (4^t * e^2))^2), ?_, ?_⟩
    · rw [e1, he, s1, s2]
    · generalize 4^t * e^2 = B
      generalize 4^t * (e + 8 * B)^2 = B'
      omega

theorem one_add_pow_mod (Y e u : Nat) :
    ∃ q, (1 + 8*Y*e)^u = 1 + 8*Y*q ∧ q % 8 = (u*e) % 8 := by
  induction u with
  | zero => exact ⟨0, by simp, by simp⟩
  | succ u ih =>
    obtain ⟨q, hq, hm⟩ := ih
    refine ⟨q + e + 8*(Y*q*e), ?_, ?_⟩
    · rw [Nat.pow_succ, hq]; grind
    · have e1 : (u+1)*e = u*e + e := Nat.succ_mul u e
      rw [e1]
      generalize Y*q*e = B
      generalize u*e = A at hm ⊢
      omega

/-- `3^(4^(t+1) u) = 1 + 4^(t+2) q` with `q ≡ 5u (mod 8)`. -/
theorem three_pow_dyadic (t u : Nat) :
    ∃ q, 3^(4^(t+1) * u) = 1 + 4^(t+2) * q ∧ q % 8 = (5*u) % 8 := by
  obtain ⟨e, he, hm⟩ := three_pow_four_pow t
  have hX : 4^(t+2) = 8 * (2 * 4^t) := by grind
  obtain ⟨q, hq, hqm⟩ := one_add_pow_mod (2 * 4^t) e u
  refine ⟨q, ?_, ?_⟩
  · rw [Nat.pow_mul, he, hX]; exact hq
  · rw [hqm, Nat.mul_mod u e 8, hm]; omega

theorem basin_pow_three_dyadic_aux (t u q : Nat) (hu : 0 < u)
    (h : 3^(4^(t+1) * u) = 1 + 4^(t+2) * q) (hw : (3^(t+1) * q) % 8 = 1) :
    Basin (3^(4^(t+1) * u)) ↔ Basin (3^(4^(t+1) * u - 1)) := by
  have hN : 1 ≤ 4^(t+1) * u := Nat.mul_pos (Nat.pow_pos (by omega)) hu
  have e : t + 2 - 1 = t + 1 := by omega
  exact basin_pow_three_consecutive (4^(t+1) * u) (t+2) q hN (by omega) h (by rw [e]; exact hw)

/-- For every `a` and every `u ≡ 7 (mod 8)`: `3^(4^(2a+1) u) ~ 3^(4^(2a+1) u - 1)`.
The two orbits meet after `4a + 7` steps; `a = 0` is the class `N ≡ 28 (mod 32)`. -/
theorem basin_pow_three_dyadic_odd (a u : Nat) (hu : u % 8 = 7) :
    Basin (3^(4^(2*a+1) * u)) ↔ Basin (3^(4^(2*a+1) * u - 1)) := by
  obtain ⟨q, hq, hqm⟩ := three_pow_dyadic (2*a) u
  have h3 : 3^(2*a+1) % 8 = 3 := by
    have h := nine_pow_mod_eight a
    rw [← three_pow_two_mul] at h
    rw [Nat.pow_succ]; omega
  apply basin_pow_three_dyadic_aux (2*a) u q (by omega) hq
  rw [Nat.mul_mod (3^(2*a+1)) q 8, h3, hqm]; omega

/-- For every `a` and every `u ≡ 5 (mod 8)`: `3^(4^(2a+2) u) ~ 3^(4^(2a+2) u - 1)`.
The two orbits meet after `4a + 9` steps; `a = 0` is the class `N ≡ 80 (mod 128)`. -/
theorem basin_pow_three_dyadic_even (a u : Nat) (hu : u % 8 = 5) :
    Basin (3^(4^(2*a+2) * u)) ↔ Basin (3^(4^(2*a+2) * u - 1)) := by
  show Basin (3^(4^(2*a+1+1) * u)) ↔ Basin (3^(4^(2*a+1+1) * u - 1))
  obtain ⟨q, hq, hqm⟩ := three_pow_dyadic (2*a+1) u
  have h3 : 3^(2*a+1+1) % 8 = 1 := by
    have h := nine_pow_mod_eight (a+1)
    have e : 2*(a+1) = 2*a+1+1 := by omega
    rw [← three_pow_two_mul, e] at h
    exact h
  apply basin_pow_three_dyadic_aux (2*a+1) u q (by omega) hq
  rw [Nat.mul_mod (3^(2*a+1+1)) q 8, h3, hqm]; omega

/-! ## 7. Two free depth parameters, and the link to the closure pair -/

/-- Consecutive integers with a common fate (classical coalescence), one statement for all `a`:
if `3^a c ≡ 3 (mod 4)` then `2^(a+1) c - 2` and `2^(a+1) c - 1` meet after `a + 3` steps. -/
theorem basin_adjacent_family (a c : Nat) (hc : (3^a * c) % 4 = 3) :
    Basin (2^(a+1) * c - 2) ↔ Basin (2^(a+1) * c - 1) := by
  have hcpos : 0 < c := by
    rcases Nat.eq_zero_or_pos c with h | h
    · rw [h] at hc; simp at hc
    · exact h
  have hR := basin_pow_two_pred (a+1) c hcpos
  have hL := basin_pow_two_pred a c hcpos
  have e1 : 2^(a+1) * c - 2 = 2 * (2^a * c - 1) := by
    have e : 2^(a+1) * c = 2 * (2^a * c) := by grind
    rw [e]; omega
  have e2 : 3^(a+1) * c = 3 * (3^a * c) := by grind
  rw [e1, hR, e2]
  generalize 3^a * c = X at hc hL ⊢
  have h1 : Basin (X - 1) ↔ Basin (3*(X/4) + 2) :=
    basin_steps 2 _ _ ((X/4 : Nat) : Int) 2 1 2 (by decide) (by decide) (by omega) (by omega)
  have h2 : Basin (3*X - 1) ↔ Basin (3*(X/4) + 2) :=
    basin_steps 2 _ _ ((3*(X/4) + 2 : Nat) : Int) 0 0 0 (by decide) (by decide) (by omega) (by omega)
  exact (basin_twice _).trans (hL.trans (h1.trans h2.symm))

/-- Consecutive powers of three with two free depth parameters `s` and `a`:
if `3^N = 1 + 4^s q`, `3^(s-1) q + 1 = 2^(a+1) c` and `3^a c ≡ 1 (mod 4)`, then `3^N ~ 3^(N-1)`.
The orbits meet after `2s + a + 3` steps.  (`a = 0` is `basin_pow_three_consecutive`.) -/
theorem basin_pow_three_consecutive_gen (N s q a c : Nat) (hN : 1 ≤ N) (hs : 1 ≤ s)
    (h : 3^N = 1 + 4^s * q) (hw : 3^(s-1) * q + 1 = 2^(a+1) * c) (hc : (3^a * c) % 4 = 1) :
    Basin (3^N) ↔ Basin (3^(N-1)) := by
  have nf := pow_three_pair_normal_form N s q hN hs h
  generalize 3^(s-1) * q = w at hw nf
  have hc3 : (3^a * (3*c)) % 4 = 3 := by
    have e : 3^a * (3*c) = 3 * (3^a * c) := by grind
    rw [e]; omega
  have adj := basin_adjacent_family a (3*c) hc3
  have hpsi := basin_psi (w+1) (by omega)
  have e1 : 2^(a+1) * (3*c) - 2 = 3*w + 1 := by
    have e : 2^(a+1) * (3*c) = 3 * (2^(a+1) * c) := by grind
    rw [e, ← hw]; omega
  have e2 : 2^(a+1) * (3*c) - 1 = 3*(w+1) - 1 := by
    have e : 2^(a+1) * (3*c) = 3 * (2^(a+1) * c) := by grind
    rw [e, ← hw]
  have e3 : 2*(w+1) - 1 = 2*w + 1 := by omega
  rw [e1, e2] at adj
  rw [e3] at hpsi
  exact nf.1.trans (adj.trans (hpsi.symm.trans nf.2.symm))

/-- At exponents with `3^N = 1 + 32 q`, `q` odd (that is `N ≡ 8 (mod 16)`), the Mersenne number
and the previous power of three form a closure pair `(y, 3y - 1)`:
`2^N - 1 ~ y` and `3^(N-1) ~ 3y - 1` with `y = (3q+1)/2`. -/
theorem pow_three_mersenne_closure_pair (N q : Nat) (h : 3^N = 1 + 32*q) (hq : q % 2 = 1) :
    (Basin (2^N - 1) ↔ Basin ((3*q+1)/2)) ∧
    (Basin (3^(N-1)) ↔ Basin (3*((3*q+1)/2) - 1)) := by
  have hN : 1 ≤ N := by
    rcases Nat.eq_zero_or_pos N with h0 | h0
    · rw [h0, Nat.pow_zero] at h; omega
    · exact h0
  constructor
  · have hA := basin_pow_two_pred N 1 (by omega)
    rw [Nat.mul_one, Nat.mul_one, h] at hA
    have h1 : Basin (1 + 32*q - 1) ↔ Basin q :=
      basin_steps 5 _ _ (q : Int) 0 0 0 (by decide) (by decide) (by omega) (by omega)
    have h2 := basin_step q
    have e : shortcut q = (3*q+1)/2 := by
      have := two_shortcut_odd q hq; omega
    rw [e] at h2
    exact hA.trans (h1.trans h2.symm)
  · have h' : 3^N = 1 + 2 * (4^2 * q) := by rw [h]; omega
    have nf := (pow_three_pair_normal_form_odd N 2 q hN h').2
    have e : 3^2 * q + 1 = 2 * (3*((3*q+1)/2) - 1) := by omega
    rw [e] at nf
    exact nf.trans (basin_twice _)

/-- The first tail class without a certificate.  If `3^N = 1 + 4^s q` and
`3·(3^(s-1) q) + 1 = 8x` with `x` odd, then `3^N ~ m` and `3^(N-1) ~ 3m - 1` for `m = 3x + 1`:
the two consecutive powers of three form a closure pair `(m, 3m - 1)` (in the opposite order to
the ladder pair `((3^N+1)/2, (3^(N+1)+1)/2)`).  Closing this class needs the open closure lemma
at `m`. -/
theorem pow_three_pair_closure_form (N s q x : Nat) (hN : 1 ≤ N) (hs : 1 ≤ s)
    (h : 3^N = 1 + 4^s * q) (hx : 3 * (3^(s-1) * q) + 1 = 8*x) (hodd : x % 2 = 1) :
    (Basin (3^N) ↔ Basin (3*x+1)) ∧ (Basin (3^(N-1)) ↔ Basin (3*(3*x+1) - 1)) := by
  have nf := pow_three_pair_normal_form N s q hN hs h
  generalize 3^(s-1) * q = w at hx nf
  constructor
  · have h1 : Basin (3*w+1) ↔ Basin x :=
      basin_steps 3 _ _ (x : Int) 0 0 0 (by decide) (by decide) (by omega) (by omega)
    exact nf.1.trans (h1.trans (basin_odd x hodd).symm)
  · have hpsi := basin_psi (w+1) (by omega)
    have e3 : 2*(w+1) - 1 = 2*w + 1 := by omega
    rw [e3] at hpsi
    have h2 : Basin (3*(w+1) - 1) ↔ Basin (3*(3*x+1) - 1) :=
      basin_steps 3 _ _ (x : Int) 1 2 2 (by decide) (by decide) (by omega) (by omega)
    exact nf.2.trans (hpsi.trans h2)

end CollatzPow3

open CollatzPow3
#print axioms iter_add_pow
#print axioms master
#print axioms periodic_exchange
#print axioms basin_steps
#print axioms basin_pow_eight_sub_five
#print axioms basin_cycle_one_fifth
#print axioms pow_three_iff_shift_closure
#print axioms basin_pow_three_odd
#print axioms basin_mersenne_pair
#print axioms basin_pow_three_mersenne
#print axioms pow_three_pair_normal_form
#print axioms basin_pow_three_consecutive
#print axioms pow_three_pair_normal_form_odd
#print axioms basin_shift_to_one
#print axioms three_pow_dyadic
#print axioms basin_pow_three_dyadic_odd
#print axioms basin_pow_three_dyadic_even
#print axioms basin_adjacent_family
#print axioms basin_pow_three_consecutive_gen
#print axioms pow_three_mersenne_closure_pair
#print axioms pow_three_pair_closure_form
#print axioms basin_mersenne_even
#print axioms basin_mersenne_odd
#print axioms basin_shift
#print axioms basin_three_two_mod8

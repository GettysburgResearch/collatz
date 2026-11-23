import BandTransport
import Mathlib.Data.Finset.Max

/-!
An arithmetic bridge for a proposed ordinary upper envelope of the inverse
Syracuse density.  No such upper envelope is asserted here.

The additive contribution of an off-path parent matters: it makes the
normalized density strictly increase above one finite floor.  A vanishing
normalized envelope then confines every orbit to that floor, treating cycles
and escaping orbits in the same argument.
-/

namespace CollatzShell.InverseDensityPotential

open ForwardSection

def OddUnit (n : Nat) : Prop := 0 < n ∧ n % 2 = 1 ∧ n % 3 ≠ 0

theorem odd_step_split (n : Nat) :
    2 ^ twos (3*n+1) * oddStep n = 3*n+1 :=
  Nat.ordProj_mul_ordCompl_eq_self (3*n+1) 2

theorem odd_step_unit (n : Nat) : OddUnit (oddStep n) := by
  have hp : 0 < oddStep n := Nat.ordCompl_pos 2 (by omega : 3*n+1 ≠ 0)
  have ho : ¬ 2 ∣ oddStep n :=
    Nat.not_dvd_ordCompl Nat.prime_two (by omega : 3*n+1 ≠ 0)
  have split := odd_step_split n
  refine ⟨hp, by omega, ?_⟩
  intro h
  have he := congrArg (fun x : Nat => x % 3) split
  simp [Nat.mul_mod, h] at he

theorem odd_step_exponent_pos {n : Nat} (hn : n % 2 = 1) :
    1 ≤ twos (3*n+1) := by
  have split := odd_step_split n
  have ho := (odd_step_unit n).2.1
  by_contra h
  have hz : twos (3*n+1) = 0 := by omega
  rw [hz, pow_zero, one_mul] at split
  omega

theorem hits_odd_unit (n : Nat) (hn : 0 < n) :
    ∃ q, OddUnit q ∧ Hits n q := by
  let a := oddPart n
  have split : 2 ^ twos n * a = n := Nat.ordProj_mul_ordCompl_eq_self n 2
  have ho : a % 2 = 1 := by
    have h := Nat.not_dvd_ordCompl Nat.prime_two hn.ne'
    change ¬ 2 ∣ a at h
    omega
  have hit : Hits n a := ⟨twos n, by
    calc orbit (twos n) n = orbit (twos n) (2^twos n*a) := by rw [split]
         _ = a := orbit_pad _ _⟩
  refine ⟨oddStep a, odd_step_unit a, hit.trans ?_⟩
  simpa [oddOrbit] using odd_orbit_hit ho 1

def secondClock (q : Nat) : Nat :=
  match q % 9 with
  | 1 => 4 | 2 => 3 | 4 => 6 | 5 => 5 | 7 => 6 | _ => 5

def secondSource (q : Nat) : Nat :=
  match q % 9 with
  | 1 => 48*(q/9)+5
  | 2 => 24*(q/9)+5
  | 4 => 192*(q/9)+85
  | 5 => 96*(q/9)+53
  | 7 => 192*(q/9)+149
  | _ => 96*(q/9)+85

/-- Two distinct short odd unit parents exist at every positive unit target.
Both inverse exponents are at most six.  This is ordinary integer arithmetic,
with no density assumption. -/
theorem two_short_unit_parents (q : Nat) (hu : q % 3 ≠ 0) :
    ∃ b₁ b₂ e₁ e₂ : Nat,
      OddUnit b₁ ∧ OddUnit b₂ ∧ b₁ < b₂ ∧
      1 ≤ e₁ ∧ e₁ < e₂ ∧ e₂ ≤ 6 ∧
      3*b₁+1 = 2^e₁*q ∧ 3*b₂+1 = 2^e₂*q := by
  refine ⟨BandTransport.inverseSource q, secondSource q,
    BandTransport.inverseClock q, secondClock q, ?_⟩
  have cases : q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega
  rcases cases with h|h|h|h|h|h
  all_goals
    simp only [OddUnit, BandTransport.inverseSource, BandTransport.inverseClock,
      secondSource, secondClock, h]
    norm_num
    omega

/-- Whichever actual parent is supplied, a different short unit parent is
available. The different source contributes extra mass in a positive inverse
transfer formula. -/
theorem short_off_parent (q n : Nat) (hu : q % 3 ≠ 0) :
    ∃ b e : Nat, OddUnit b ∧ n ≠ b ∧ 1 ≤ e ∧ e ≤ 6 ∧
      3*b+1 = 2^e*q := by
  obtain ⟨b₁,b₂,e₁,e₂,hb₁,hb₂,ltb,he₁,he₂,bound,a₁,a₂⟩ :=
    two_short_unit_parents q hu
  by_cases eq : n = b₁
  · exact ⟨b₂,e₂,hb₂,by omega,by omega,bound,a₂⟩
  · exact ⟨b₁,e₁,hb₁,eq,he₁,by omega,a₁⟩

/-- Every displayed parent equation is an actual shortcut orbit certificate. -/
theorem inverse_affine_clock (n q e : Nat) (ho : n % 2 = 1) (he : 1 ≤ e)
    (affine : 3*n+1 = 2^e*q) : orbit e n = q := by
  cases e with
  | zero => omega
  | succ k =>
    have eveneq : 3*n+1 = 2*(2^k*q) := by
      simpa [pow_succ, Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm] using affine
    have st : step n = 2^k*q := by simp [step, ho, eveneq]
    simpa only [orbit, st] using orbit_pad k q

/-- The exact real inequality behind the inverse-density drift.  The second
parent supplies `c`, while `k` is the exact power of two on the physical edge. -/
theorem normalized_strict_increase
    {n q k x y c : ℝ} (hn : 0 < n) (hq : 0 < q)
    (hk : 2 ≤ k) (hc : 0 < c) (edge : k*q = 3*n+1)
    (transfer : 3*x+k*c ≤ k*y) (small : x/n < 2*c) : x/n < y/q := by
  have hsmall : x < 2*c*n := (div_lt_iff₀ hn).mp small
  have htransfer := mul_le_mul_of_nonneg_left transfer hn.le
  have hscale : 2*c*n ≤ k*c*n := by
    have h := mul_le_mul_of_nonneg_right hk (by positivity : 0 ≤ c*n)
    nlinarith
  have heq := congrArg (fun a : ℝ => a*x) edge
  have hmul : k*(q*x) < k*(n*y) := by nlinarith
  have hxy : q*x < n*y := by
    by_contra h
    have contrary := mul_le_mul_of_nonneg_left (le_of_not_gt h)
      (by linarith : 0 ≤ k)
    exact (not_lt_of_ge contrary) hmul
  exact (div_lt_div_iff₀ hn hq).mpr (by nlinarith)

noncomputable def normalized (F : Nat → ℝ) (n : Nat) := F n / n

/-- An explicitly quantified upper-envelope property.  It is an open input,
not an imported or postulated density theorem. -/
def Sublinear (F : Nat → ℝ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ M : Nat,
    ∀ n : Nat, M ≤ n → OddUnit n → normalized F n < ε

/-- The additive inverse transfer on each actual odd edge. -/
def AdditiveTransfer (F : Nat → ℝ) (c : ℝ) : Prop :=
  ∀ n : Nat, OddUnit n →
    3*F n+(2:ℝ)^twos (3*n+1)*c ≤
      (2:ℝ)^twos (3*n+1)*F (oddStep n)

/-- A two-parent portion of the positive inverse-density equation.  It is
kept explicit, rather than assuming existence of a pointwise density limit. -/
def PairTransfer (F : Nat → ℝ) : Prop :=
  ∀ q n b e f : Nat, OddUnit q → OddUnit n → OddUnit b → n ≠ b →
    1 ≤ e → 1 ≤ f → 3*n+1 = 2^e*q → 3*b+1 = 2^f*q →
      3*F n/(2:ℝ)^e + 3*F b/(2:ℝ)^f ≤ F q

/-- The previously analytic off-parent step is reduced to explicit ordinary
arithmetic.  The constant is uniform in the supplied edge and its exponent. -/
theorem additive_transfer_of_pair_floor
    {F : Nat → ℝ} {c₀ : ℝ} (hc₀ : 0 < c₀)
    (floor : ∀ n, OddUnit n → c₀ ≤ F n)
    (pair : PairTransfer F) : AdditiveTransfer F (3*c₀/64) := by
  intro n hn
  let q := oddStep n
  let e := twos (3*n+1)
  have hq : OddUnit q := odd_step_unit n
  have he : 1 ≤ e := odd_step_exponent_pos hn.2.1
  have edge : 3*n+1 = 2^e*q := (odd_step_split n).symm
  obtain ⟨b,f,hb,ne,hf,fu,other⟩ := short_off_parent q n hq.2.2
  have full := pair q n b e f hq hn hb ne he hf edge other
  have fp : (0:ℝ) < 2^f := by positivity
  have ep : (0:ℝ) < 2^e := by positivity
  have fb : (2:ℝ)^f ≤ 64 := by
    norm_num at *
    exact le_trans (pow_le_pow_right₀ (by norm_num : (1:ℝ) ≤ 2) fu) (by norm_num)
  have extra : 3*c₀/64 ≤ 3*F b/(2:ℝ)^f := by
    apply (le_div_iff₀ fp).mpr
    have hflo := floor b hb
    have hp := mul_le_mul_of_nonneg_left fb (by positivity : 0 ≤ 3*c₀/64)
    nlinarith
  have sum : 3*F n/(2:ℝ)^e+3*c₀/64 ≤ F q := by linarith
  calc
    3*F n+(2:ℝ)^twos (3*n+1)*(3*c₀/64) =
      (2:ℝ)^e*(3*F n/(2:ℝ)^e+3*c₀/64) := by
        dsimp [e]
        field_simp
    _ ≤ (2:ℝ)^e*F q := mul_le_mul_of_nonneg_left sum ep.le

theorem normalized_increases {F : Nat → ℝ} {c : ℝ}
    (hc : 0 < c) (transfer : AdditiveTransfer F c)
    {n : Nat} (hn : OddUnit n) (small : normalized F n < 2*c) :
    normalized F n < normalized F (oddStep n) := by
  have hq := odd_step_unit n
  have hk : (2:ℝ) ≤ (2:ℝ)^twos (3*n+1) := by
    exact_mod_cast Nat.le_self_pow
      (by have := odd_step_exponent_pos hn.2.1; omega : twos (3*n+1) ≠ 0) 2
  have edge : (2:ℝ)^twos (3*n+1)*(oddStep n:ℝ) = 3*(n:ℝ)+1 := by
    exact_mod_cast odd_step_split n
  exact normalized_strict_increase
    (by exact_mod_cast hn.1) (by exact_mod_cast hq.1) hk hc edge
    (transfer n hn) small

/-- A decaying positive potential with additive inverse transfer supplies one
finite absorbing floor.  `P` may be convergence, or hitting that floor. -/
theorem all_odd_units_of_floor
    {F : Nat → ℝ} {c : ℝ} {N : Nat} {P : Nat → Prop}
    (hc : 0 < c) (positive : ∀ n, OddUnit n → 0 < normalized F n)
    (sublinear : Sublinear F) (transfer : AdditiveTransfer F c)
    (small : ∀ n, N ≤ n → OddUnit n → normalized F n < 2*c)
    (base : ∀ n, OddUnit n → n < N → P n)
    (backward : ∀ n, OddUnit n → P (oddStep n) → P n) :
    ∀ n, OddUnit n → P n := by
  classical
  intro n hn
  by_contra bad
  obtain ⟨M, hM⟩ := sublinear (normalized F n) (positive n hn)
  let S := (Finset.range M).filter
    (fun m => OddUnit m ∧ ¬ P m ∧ normalized F n ≤ normalized F m)
  have bounded : ∀ m, OddUnit m → normalized F n ≤ normalized F m → m < M := by
    intro m hm hge
    by_contra h
    exact (not_lt_of_ge hge) (hM m (by omega) hm)
  have member : n ∈ S := by
    simp only [S, Finset.mem_filter, Finset.mem_range]
    exact ⟨bounded n hn le_rfl, hn, bad, le_rfl⟩
  obtain ⟨m, hm, maximal⟩ := S.exists_max_image (normalized F) ⟨n, member⟩
  have data : OddUnit m ∧ ¬ P m ∧ normalized F n ≤ normalized F m :=
    (Finset.mem_filter.mp hm).2
  have high : N ≤ m := by
    by_contra h
    exact data.2.1 (base m data.1 (by omega))
  have increase := normalized_increases hc transfer data.1 (small m high data.1)
  have nextUnit := odd_step_unit m
  have nextBad : ¬ P (oddStep m) := fun h => data.2.1 (backward m data.1 h)
  have nextGe : normalized F n ≤ normalized F (oddStep m) :=
    data.2.2.trans increase.le
  have nextMember : oddStep m ∈ S := by
    simp only [S, Finset.mem_filter, Finset.mem_range]
    exact ⟨bounded _ nextUnit nextGe, nextUnit, nextBad, nextGe⟩
  exact (not_lt_of_ge (maximal _ nextMember)) increase

/-- The same argument excludes both escape and cycles above the selected
floor: every positive source physically hits an odd ternary unit below it. -/
theorem finite_absorbing_floor
    {F : Nat → ℝ} {c : ℝ} (hc : 0 < c)
    (positive : ∀ n, OddUnit n → 0 < normalized F n)
    (sublinear : Sublinear F) (transfer : AdditiveTransfer F c) :
    ∃ N : Nat, ∀ n : Nat, 0 < n →
      ∃ q : Nat, OddUnit q ∧ q < N ∧ Hits n q := by
  obtain ⟨N, hN⟩ := sublinear (2*c) (by positivity)
  let P : Nat → Prop := fun n => ∃ q, OddUnit q ∧ q < N ∧ Hits n q
  have all : ∀ n, OddUnit n → P n := by
    refine all_odd_units_of_floor (P := P) hc positive sublinear transfer hN ?_ ?_
    · intro n hn hsmall
      exact ⟨n, hn, hsmall, 0, rfl⟩
    · intro n hn hnext
      rcases hnext with ⟨q, hq, hqN, hit⟩
      have first : Hits n (oddStep n) := by
        simpa [oddOrbit] using odd_orbit_hit hn.2.1 1
      exact ⟨q, hq, hqN, first.trans hit⟩
  refine ⟨N, ?_⟩
  intro n hn
  obtain ⟨a, ha, hit⟩ := hits_odd_unit n hn
  obtain ⟨q, hq, hqN, hitq⟩ := all a ha
  exact ⟨q, hq, hqN, hit.trans hitq⟩

theorem universal_of_inverse_envelope_and_base
    {F : Nat → ℝ} {c : ℝ} {N : Nat}
    (hc : 0 < c) (positive : ∀ n, OddUnit n → 0 < normalized F n)
    (sublinear : Sublinear F) (transfer : AdditiveTransfer F c)
    (small : ∀ n, N ≤ n → OddUnit n → normalized F n < 2*c)
    (base : ∀ n, OddUnit n → n < N → Basin n) : Universal := by
  have all : ∀ n, OddUnit n → Basin n :=
    all_odd_units_of_floor hc positive sublinear transfer small base
      (fun n hn h => (basin_at_hit (by
        simpa [oddOrbit] using odd_orbit_hit hn.2.1 1)).mpr h)
  intro n hn
  obtain ⟨q, hq, hit⟩ := hits_odd_unit n hn
  exact (basin_at_hit hit).mpr (all q hq)

end CollatzShell.InverseDensityPotential

#print axioms CollatzShell.InverseDensityPotential.normalized_strict_increase
#print axioms CollatzShell.InverseDensityPotential.two_short_unit_parents
#print axioms CollatzShell.InverseDensityPotential.inverse_affine_clock
#print axioms CollatzShell.InverseDensityPotential.additive_transfer_of_pair_floor
#print axioms CollatzShell.InverseDensityPotential.finite_absorbing_floor
#print axioms CollatzShell.InverseDensityPotential.universal_of_inverse_envelope_and_base

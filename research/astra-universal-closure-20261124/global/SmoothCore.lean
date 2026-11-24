import MinimumFailure

namespace Collatz.SmoothCore

open Collatz.SourceDeletion Collatz.MinimumFailure

/-- The least positive base supporting a bad power of three, and the first bad
power above this base. Minimality applies to all positive bases, including evens. -/
structure FirstTower (w r : Nat) : Prop where
  positive : 0 < w
  bad : ¬ Good (3^r*w)
  smaller : ∀ a, 0 < a → a < w → ∀ j, Good (3^j*a)
  earlier : ∀ j, j < r → Good (3^j*w)

theorem exists_first_tower (failure : ∃ n, 0 < n ∧ ¬ Good n) :
    ∃ w r, FirstTower w r := by
  classical
  have supports : ∃ w, 0<w ∧ ∃ r : Nat, ¬Good (3^r*w) := by
    obtain ⟨n, hn, bad⟩ := failure
    exact ⟨n, hn, 0, by simpa using bad⟩
  let w := Nat.find supports
  have hw : 0<w ∧ ∃ r : Nat, ¬Good (3^r*w) := Nat.find_spec supports
  let r := Nat.find hw.2
  refine ⟨w, r, hw.1, Nat.find_spec hw.2, ?_, ?_⟩
  · intro a ha lt j
    by_contra bad
    exact (Nat.not_lt_of_ge (Nat.find_min' supports ⟨ha,j,bad⟩)) lt
  · intro j lt
    by_contra bad
    exact (Nat.not_lt_of_ge (Nat.find_min' hw.2 bad)) lt

theorem base_good {w r : Nat} (tower : FirstTower w r) : Good w := by
  apply (label_eq_one w).mp
  apply all_below label label_step w _ w tower.positive (by omega)
  intro v hv _ lt
  have h₀ : Good v := by simpa using tower.smaller v hv lt 0
  have h₁ : Good (3*v) := by simpa using tower.smaller v hv lt 1
  exact ((label_eq_one v).mpr h₀).trans ((label_eq_one _).mpr h₁).symm

theorem base_is_unit {w r : Nat} (tower : FirstTower w r) :
    w%2 = 1 ∧ w%3 ≠ 0 ∧ 0 < r := by
  have hw := tower.positive
  constructor
  · by_contra odd
    have even : w=2*(w/2) := by omega
    have g := tower.smaller (w/2) (by omega) (by omega) r
    apply tower.bad
    apply (good_step _).mp
    have eq : 3^r*w = 2*(3^r*(w/2)) := by
      calc
        3^r*w = 3^r*(2*(w/2)) := congrArg (fun t => 3^r*t) even
        _ = 2*(3^r*(w/2)) := by ac_rfl
    simpa [eq,step] using g
  constructor
  · intro div
    have eq : w=3*(w/3) := by omega
    have g := tower.smaller (w/3) (by omega) (by omega) (r+1)
    apply tower.bad
    convert g using 1
    conv_lhs => rw [eq]
    ring
  · by_contra zero
    have eq : r=0 := by omega
    exact tower.bad (by simpa [eq] using base_good tower)

/-- Every exponent in a smaller positive base's 2,3-smooth tower is good. -/
theorem smooth_reservoir {w r : Nat} (tower : FirstTower w r)
    {a : Nat} (ha : 0<a) (lt : a<w) (i j : Nat) : Good (2^i*(3^j*a)) := by
  induction i with
  | zero => simpa using tower.smaller a ha lt j
  | succ i ih =>
    apply (good_step _).mp
    rw [show 2^(i+1)*(3^j*a) = 2*(2^i*(3^j*a)) by ring]
    simpa [step] using ih

/-- Literal shortcut run, including its first even endpoint. -/
theorem odd_run_end {m n a : Nat} (eq : n+1=2^m*a) :
    run m n + 1 = 3^m*a := by
  induction m generalizing n a with
  | zero => simpa [run] using eq
  | succ m ih =>
    rw [show 2^(m+1)*a=2*(2^m*a) by ring] at eq
    have s : step n + 1 = 2^m*(3*a) := by
      rw [show 2^m*(3*a)=3*(2^m*a) by ring]
      unfold step
      split <;> omega
    rw [run, ih s]
    ring

private theorem power_three_eight (r : Nat) : 3^r%8=1 ∨ 3^r%8=3 := by
  induction r with
  | zero => decide
  | succ r ih =>
    rw [pow_succ, Nat.mul_mod]
    rcases ih with h | h <;> rw [h] <;> decide

private theorem good_three : Good 3 := ⟨5, by decide⟩

/-- There is no equality exception to the size comparison for an actual bad
tower. Equality would force its bad element to be a power of three one below
a power of two, hence at most three. -/
theorem strict_base_of_clock {w r m a : Nat} (tower : FirstTower w r)
    (start : 3^r*w+1=2^m*a) (clock : 3^r<2^m) : a<w := by
  by_contra large
  have g : w≤a := by omega
  have hw := tower.positive
  have bound := Nat.mul_le_mul_left (2^m) g
  have gap := Nat.mul_le_mul_right w (show 3^r+1 ≤ 2^m by omega)
  rw [Nat.add_mul, Nat.one_mul] at gap
  have one : w=1 := by omega
  have ha : a=1 := by
    rw [one,Nat.mul_one] at start
    by_contra no
    have largeA : 2≤a := by omega
    have two := Nat.mul_le_mul_left (2^m) largeA
    omega
  rw [one,ha,Nat.mul_one,Nat.mul_one] at start
  have small : m<3 := by
    by_contra no
    obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le (show 3≤m by omega)
    rw [hk,pow_add] at start
    change 3^r+1=8*2^k at start
    rcases power_three_eight r with h | h <;> omega
  apply tower.bad
  rw [one,Nat.mul_one]
  rcases (show m=0 ∨ m=1 ∨ m=2 by omega) with h | h | h
  · rw [h] at start
    simp at start
  · have eq : 3^r=1 := by simpa [h] using start
    rw [eq]; exact good_one
  · rw [h] at start
    change 3^r+1=4 at start
    have eq : 3^r=3 := by omega
    rw [eq]; exact good_three

/-- The finite comparisons below are equalities at ordinary physical clocks. -/
theorem same_three (k : Nat) : run 3 (8*k+4)=run 3 (8*k+5) := by
  have x := lift 3 4 k
  have y := lift 3 5 k
  change run 3 (4+8*k)=2+3*k at x
  change run 3 (5+8*k)=2+3*k at y
  simpa [Nat.add_comm] using x.trans y.symm

theorem higher_three (k : Nat) : run 3 (8*k+6)=run 3 (3*(8*k+7)) := by
  have x := lift 3 6 k
  have y := lift 3 21 (3*k)
  change run 3 (6+8*k)=8+9*k at x
  change run 3 (21+8*(3*k))=8+3*(3*k) at y
  rw [show 8*k+6=6+8*k by omega, x, show 3*(8*k+7)=21+8*(3*k) by ring,y]
  ring

theorem same_four (k : Nat) : run 4 (16*k+2)=run 4 (16*k+3) := by
  have x := lift 4 2 k
  have y := lift 4 3 k
  change run 4 (2+16*k)=2+9*k at x
  change run 4 (3+16*k)=2+9*k at y
  simpa [Nat.add_comm] using x.trans y.symm

theorem lower_four (k : Nat) : run 4 (48*k+8)=run 4 (16*k+3) := by
  have x := lift 4 8 (3*k)
  have y := lift 4 3 k
  change run 4 (8+16*(3*k))=2+3*(3*k) at x
  change run 4 (3+16*k)=2+9*k at y
  rw [show 48*k+8=8+16*(3*k) by ring,x,show 16*k+3=3+16*k by omega,y]
  ring

private theorem good_of_meeting {x y h : Nat} (p : run h x=run h y)
    (g : Good y) : Good x :=
  (good_run h x).mp (p ▸ (good_run h y).mpr g)

/-- Four exit classes force a physical merger with a power in a smaller tower,
without any upper bound on the even exit or on the intervening excursion. -/
theorem forbid_small_base_exit {w r a m : Nat} (tower : FirstTower w r)
    (size : a<w) (ha : 0<a) (start : 3^r*w+1=2^(m+1)*a) :
    let A := 3^(m+1)*a
    ¬ (A%8=5 ∨ A%8=7 ∨ A%16=3 ∨ A%16=9) := by
  dsimp only
  let A := 3^(m+1)*a
  change ¬ (A%8=5 ∨ A%8=7 ∨ A%16=3 ∨ A%16=9)
  intro pattern
  let x := run (m+1) (3^r*w)
  have endAt : x + 1 = A := odd_run_end start
  have gA : Good A := tower.smaller a ha size (m+1)
  have cancel : ∀ {v h : Nat}, run h x=run h v → Good v → False := by
    intro v h path g
    exact tower.bad ((good_run (m+1) _).mp (good_of_meeting path g))
  rcases pattern with five | seven | three | nine
  · let k := A/8
    have e : A=8*k+5 := by dsimp [k]; omega
    exact cancel (show run 3 x=run 3 A by rw [show x=8*k+4 by omega,e]; exact same_three k) gA
  · let k := A/8
    have e : A=8*k+7 := by dsimp [k]; omega
    have g : Good (3*A) := by
      rw [show 3*A=3^(m+2)*a by dsimp [A]; ring]
      exact tower.smaller a ha size _
    exact cancel (show run 3 x=run 3 (3*A) by rw [show x=8*k+6 by omega,e]; exact higher_three k) g
  · let k := A/16
    have e : A=16*k+3 := by dsimp [k]; omega
    exact cancel (show run 4 x=run 4 A by rw [show x=16*k+2 by omega,e]; exact same_four k) gA
  · let B := 3^m*a
    have mul : A=3*B := by dsimp [A,B]; ring
    let k := B/16
    have e : B=16*k+3 := by dsimp [k]; omega
    have g : Good B := tower.smaller a ha size _
    exact cancel (show run 4 x=run 4 B by rw [show x=48*k+8 by omega,e]; exact lower_four k) g

/-- A first bad power cannot meet its source two powers below, even when its
initial odd run is short relative to its ternary exponent. -/
theorem forbid_two_power_return {w r : Nat} (tower : FirstTower w (r+2)) :
    (3^(r+2)*w)%512 ≠ 85 := by
  intro pat
  let b := 3^r*w
  have eq : 3^(r+2)*w=9*b := by dsimp [b]; ring
  rw [eq] at pat
  let k := b/512
  have eb : b=237+512*k := by dsimp [k]; omega
  have x := lift 9 237 k
  have y := lift 9 2133 (9*k)
  change run 9 (237+512*k)=38+81*k at x
  change run 9 (2133+512*(9*k))=38+9*(9*k) at y
  have path : run 9 (3^(r+2)*w)=run 9 b := by
    rw [eq,eb,x,show 9*(237+512*k)=2133+512*(9*k) by ring,y]
    ring
  exact tower.bad (good_of_meeting path (tower.earlier r (by omega)))

private theorem split_twos (n : Nat) (h : 0<n) :
    ∃ k a : Nat, 0<a ∧ a%2=1 ∧ n=2^k*a := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases odd : n%2=1
    · exact ⟨0,n,h,odd,by simp⟩
    obtain ⟨k,a,ha,oa,eq⟩ := ih (n/2) (by omega) (by omega)
    refine ⟨k+1,a,ha,oa,?_⟩
    rw [show 2^(k+1)*a=2*(2^k*a) by ring,←eq]
    omega

private theorem good_pow_two (i a : Nat) : Good (2^i*a) ↔ Good a := by
  induction i with
  | zero => simp
  | succ i ih =>
    rw [show 2^(i+1)*a=2*(2^i*a) by ring]
    have s : step (2*(2^i*a))=2^i*a := by simp [step]
    have base := (good_step (2*(2^i*a))).symm
    rw [s] at base
    exact base.trans ih

/-- The odd base after splitting the bad multiple plus one is itself good,
irrespective of how large it is: it is downstream of the preceding good power. -/
theorem next_base_good {w r m a : Nat} (tower : FirstTower w (r+1))
    (start : 3^(r+1)*w+1=2^(m+1)*a) : Good a := by
  have last := tower.earlier r (by omega)
  have oddw := (base_is_unit tower).1
  have oddp : 3^r%2=1 := by rcases power_three_eight r with h | h <;> omega
  have odd : (3^r*w)%2=1 := by rw [Nat.mul_mod,oddw,oddp]
  have split : 3*(3^r*w)+1 = 2*(2^m*a) := by
    calc
      _ = 3^(r+1)*w+1 := by ring
      _ = _ := start
      _ = _ := by ring
  have s : step (3^r*w)=2^m*a := by unfold step; split <;> omega
  exact (good_pow_two m a).mp (s ▸ (good_step _).mpr last)

/-- A purely ordinary, positive-integer closing target. The destination may
lie on an earlier power of the same base or any power of any smaller base.
The target does not presuppose a counterexample or a basin label. -/
def FrontierMerger : Prop :=
  ∀ w r m a : Nat, 0<w → w%2=1 → w%3≠0 → 0<r → 0<a → a%2=1 →
    3^r*w+1=2^(m+1)*a →
    (2^(m+1)≤3^r ∨ (3^(m+1)*a)%16=1 ∨ (3^(m+1)*a)%16=11) →
    (2≤r → (3^r*w)%512≠85) →
    ∃ b j h k : Nat, 0<b ∧ (b<w ∨ (b=w ∧ j<r)) ∧
      run h (3^r*w)=run k (3^j*b)

/-- The implication consumes a merger only on the surviving arithmetic cases.
The merger itself is open. -/
theorem universal_iff_frontier_merger :
    (∀ n : Nat, 0<n → Good n) ↔ FrontierMerger := by
  constructor
  · intro allGood w r _ _ hw _ _ hr _ _ _ _ _
    have hpow : 0<3^r*w := Nat.mul_pos (Nat.pow_pos (by decide : 0<3)) hw
    obtain ⟨h₁,e₁⟩ := allGood _ hpow
    obtain ⟨h₂,e₂⟩ := allGood _ hw
    exact ⟨w,0,h₁,h₂,hw,Or.inr ⟨rfl,hr⟩,by simpa using e₁.trans e₂.symm⟩
  · intro close n hn
    by_contra bad
    obtain ⟨w,r,tower⟩ := exists_first_tower ⟨n,hn,bad⟩
    obtain ⟨ow,unit,hr⟩ := base_is_unit tower
    have oddp : 3^r%2=1 := by rcases power_three_eight r with h | h <;> omega
    have odd : (3^r*w)%2=1 := by rw [Nat.mul_mod,ow,oddp]
    obtain ⟨m,a,ha,oa,eq⟩ := split_twos ((3^r*w+1)/2) (by omega)
    have start : 3^r*w+1=2^(m+1)*a := by
      rw [show 2^(m+1)*a=2*(2^m*a) by ring,←eq]; omega
    have survivor : 2^(m+1)≤3^r ∨ (3^(m+1)*a)%16=1 ∨ (3^(m+1)*a)%16=11 := by
      by_cases low : 2^(m+1)≤3^r
      · exact Or.inl low
      have cutoff := strict_base_of_clock tower start (by omega)
      have excluded := forbid_small_base_exit tower cutoff ha start
      dsimp only at excluded
      have oddpA : 3^(m+1)%2=1 := by rcases power_three_eight (m+1) with h | h <;> omega
      have oddA : (3^(m+1)*a)%2=1 := by rw [Nat.mul_mod,oa,oddpA]
      exact Or.inr (by omega)
    have no85 : 2≤r → (3^r*w)%512≠85 := by
      intro upper
      obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le upper
      rw [Nat.add_comm] at hk
      subst r
      exact forbid_two_power_return tower
    obtain ⟨b,j,h,k,hb,lt,meet⟩ := close w r m a tower.positive ow unit hr ha oa start survivor no85
    have lighter : Good (3^j*b) := by
      rcases lt with less | ⟨rfl,earlier⟩
      · exact tower.smaller b hb less j
      · exact tower.earlier j earlier
    exact tower.bad ((good_run h _).mp (meet ▸ (good_run k _).mpr lighter))

#print axioms exists_first_tower
#print axioms base_good
#print axioms base_is_unit
#print axioms strict_base_of_clock
#print axioms smooth_reservoir
#print axioms odd_run_end
#print axioms same_three
#print axioms higher_three
#print axioms same_four
#print axioms lower_four
#print axioms forbid_small_base_exit
#print axioms forbid_two_power_return
#print axioms next_base_good
#print axioms universal_iff_frontier_merger

end Collatz.SmoothCore

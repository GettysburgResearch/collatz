import PositiveWordDescent

/-! Pointwise odd-clock bounds on ordinary trajectories outside the basin.
Only odd inputs incur the multiplicative correction. -/
set_option exponentiation.threshold 10000

namespace OddClockFloor

open CollatzReverseBasin WordRank

def below (root : Nat) : Nat → Nat → Bool
  | 0, x => decide (x < root)
  | k+1, x => decide (x < root) || below root k (shortcut x)

private theorem step_pos (x : Nat) (positive : 0 < x) : 0 < shortcut x := by
  unfold shortcut
  split <;> omega

theorem run_pos (h x : Nat) (positive : 0 < x) : 0 < run h x := by
  induction h generalizing x with
  | zero => exact positive
  | succ h ih => exact ih _ (step_pos x positive)

private theorem below_sound (root fuel x : Nat) (ok : below root fuel x = true) :
    ∃ k, run k x < root := by
  induction fuel generalizing x with
  | zero => exact ⟨0, of_decide_eq_true ok⟩
  | succ fuel ih =>
    simp only [below,Bool.or_eq_true,decide_eq_true_eq] at ok
    rcases ok with hit | later
    · exact ⟨0,hit⟩
    · obtain ⟨k,hk⟩ := ih _ later
      exact ⟨k+1,hk⟩

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
private theorem small_table :
    (List.range 2720).all (fun n => decide (n≤1) || below n 81 n) = true := by
  decide +kernel

theorem small_good (x : Nat) (pos : 0 < x) (bound : x < 2720) : Basin x := by
  induction x using Nat.strong_induction_on with
  | h n ih =>
    by_cases one : n=1
    · subst n; exact ⟨0,rfl⟩
    have mem : n ∈ List.range 2720 := List.mem_range.mpr bound
    have row := List.all_eq_true.mp small_table n mem
    simp only [Bool.or_eq_true,decide_eq_true_eq] at row
    rcases row with impossible | row
    · omega
    obtain ⟨k,hk⟩ := below_sound n 81 n row
    exact (PositiveWordDescent.basinRun k n).mp (ih _ hk (run_pos _ _ pos) (by omega))

private theorem step_low (x : Nat) : 3^(x%2)*x ≤ 2*shortcut x := by
  by_cases par : x%2=0
  · simp [shortcut,par]; omega
  · have odd : x%2=1 := by omega
    simp [shortcut,odd]; omega

theorem linear_lower (h x : Nat) : 3^(odds h x)*x ≤ 2^h*run h x := by
  induction h generalizing x with
  | zero => simp [odds,run]
  | succ h ih =>
    let t := odds h (shortcut x)
    change 3^(x%2+t)*x ≤ 2^(h+1)*run h (shortcut x)
    calc
      _ = 3^t*(3^(x%2)*x) := by rw [pow_add]; ring
      _ ≤ 3^t*(2*shortcut x) := Nat.mul_le_mul_left _ (step_low x)
      _ = 2*(3^t*shortcut x) := by ring
      _ ≤ 2*(2^h*run h (shortcut x)) := Nat.mul_le_mul_left _ (ih _)
      _ = _ := by ring

private theorem scaled_step (B x : Nat) (bound : B ≤ x) :
    B^(x%2)*(2*shortcut x) ≤ (3*B+1)^(x%2)*x := by
  by_cases par : x%2=0
  · simp [shortcut,par]; omega
  · have odd : x%2=1 := by omega
    have eq : 2*shortcut x=3*x+1 := by simp [shortcut,odd]; omega
    rw [odd,eq,pow_one,pow_one]
    calc B*(3*x+1) = 3*B*x+B := by ring
         _ ≤ 3*B*x+x := Nat.add_le_add_left bound _
         _ = _ := by ring

theorem odd_clock_upper (h B x : Nat) (floor : ∀ i<h, B≤run i x) :
    B^(odds h x)*(2^h*run h x) ≤ (3*B+1)^(odds h x)*x := by
  induction h generalizing x with
  | zero => simp [odds,run]
  | succ h ih =>
    let p := x%2
    let q := odds h (shortcut x)
    have pre := scaled_step B x (floor 0 (by omega))
    have tail := ih (shortcut x) (fun i hi => floor (i+1) (by omega))
    change B^(p+q)*(2^(h+1)*run h (shortcut x)) ≤ (3*B+1)^(p+q)*x
    calc
      _ = (B^p*2)*(B^q*(2^h*run h (shortcut x))) := by rw [pow_add]; ring
      _ ≤ (B^p*2)*((3*B+1)^q*shortcut x) := Nat.mul_le_mul_left _ tail
      _ = (3*B+1)^q*(B^p*(2*shortcut x)) := by ring
      _ ≤ (3*B+1)^q*((3*B+1)^p*x) := Nat.mul_le_mul_left _ pre
      _ = _ := by rw [pow_add]; ring

theorem bad_upper (h B x : Nat) (bound : B ≤ 2720) (pos : 0<x) (bad : ¬Basin x) :
    B^(odds h x)*(2^h*run h x) ≤ (3*B+1)^(odds h x)*x := by
  apply odd_clock_upper
  intro i _
  by_contra! small
  exact bad ((PositiveWordDescent.basinRun i x).mp (small_good _ (run_pos i x pos) (by omega)))

private theorem ratio_le {A B U V q K : Nat}
    (base : B≤A) (exp : q≤K) (cut : A^K*V<B^K*U) : A^q*V<B^q*U := by
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le exp
  by_contra! no
  apply Nat.not_le_of_lt cut
  calc
    B^(q+d)*U = (B^q*U)*B^d := by rw [pow_add]; ring
    _ ≤ (A^q*V)*A^d := Nat.mul_le_mul no (Nat.pow_le_pow_left base d)
    _ = _ := by rw [pow_add]; ring

theorem bad_drop (h B x K : Nat) (bound : B≤2720) (pos : 0<x) (bad : ¬Basin x)
    (budget : (3*B+1)^(odds h x)*K < B^(odds h x)*2^h) :
    K*run h x < x := by
  let q := odds h x
  have up := bad_upper h B x bound pos bad
  have strict := Nat.mul_lt_mul_of_pos_right budget pos
  have drop : (B^q*2^h)*(K*run h x)<(B^q*2^h)*x := by
    calc
      _ = K*(B^q*(2^h*run h x)) := by ring
      _ ≤ K*((3*B+1)^q*x) := Nat.mul_le_mul_left _ up
      _ = ((3*B+1)^q*K)*x := by ring
      _ < _ := strict
  exact Nat.lt_of_mul_lt_mul_left drop

set_option exponentiation.threshold 10000 in
private theorem cut620 : (3*226+1)^620*2^40 < 226^620*(2:Nat)^1024 := by decide +kernel

theorem bad_clock_1024 (x : Nat) (pos : 0<x) (bad : ¬Basin x) :
    2^40*run 1024 x<x ↔ odds 1024 x≤620 := by
  constructor
  · intro drop
    by_contra! bigger
    have powers := Nat.pow_le_pow_right (by decide : 0<3) bigger
    have cut : (2:Nat)^1024 ≤ 2^40*3^621 := by decide +kernel
    have lo := linear_lower 1024 x
    have imp : 2^1024*x ≤ 2^1024*(2^40*run 1024 x) := by
      calc
        _ ≤ (2^40*3^621)*x := Nat.mul_le_mul_right _ cut
        _ ≤ (2^40*3^(odds 1024 x))*x := Nat.mul_le_mul_right _ (Nat.mul_le_mul_left _ powers)
        _ = 2^40*(3^(odds 1024 x)*x) := by ring
        _ ≤ 2^40*(2^1024*run 1024 x) := Nat.mul_le_mul_left _ lo
        _ = _ := by ring
    exact Nat.not_le_of_lt drop (Nat.le_of_mul_le_mul_left imp (Nat.pow_pos (by decide : 0<2)))
  · intro below
    apply bad_drop 1024 226 x (2^40) (by decide) pos bad
    exact ratio_le (by decide) below cut620

private theorem cut646 : (3*2720+1)^646*1 < 2720^646*(2:Nat)^1024 := by decide +kernel

/-- On a bad positive ordinary input, the tower criterion holds at the
specified endpoint for every positive base, including bases below 2^1024. -/
theorem bad_tower_clock_1024 (w r : Nat) (pos : 0<w) (bad : ¬Basin (3^r*w)) :
    run 1024 (3^r*w)<w ↔ odds 1024 (3^r*w)+r≤646 := by
  let q := odds 1024 (3^r*w)
  change run 1024 (3^r*w)<w ↔ q+r≤646
  constructor
  · intro drop
    by_contra! bigger
    have lo := linear_lower 1024 (3^r*w)
    have cut : (2:Nat)^1024 ≤ 3^647 := by decide +kernel
    have base : 2^1024≤3^(q+r) := cut.trans (Nat.pow_le_pow_right (by decide : 0<3) bigger)
    have impossible : 2^1024*w≤2^1024*run 1024 (3^r*w) := by
      calc
        _ ≤ 3^(q+r)*w := Nat.mul_le_mul_right _ base
        _ = 3^q*(3^r*w) := by rw [pow_add]; ring
        _ ≤ _ := lo
    exact Nat.not_le_of_lt drop (Nat.le_of_mul_le_mul_left impossible (Nat.pow_pos (by decide : 0<2)))
  · intro budget
    let B : Nat := 2720
    let A : Nat := 3*B+1
    have cut : A^(q+r)<B^(q+r)*2^1024 := by
      simpa only [Nat.mul_one] using ratio_le (by decide) budget cut646
    have ratio : A^q*3^r<B^q*2^1024 := by
      have joined : (A^q*3^r)*B^r < (B^q*2^1024)*B^r := by
        calc
          _ = A^q*(3*B)^r := by rw [mul_pow]; ring
          _ ≤ A^q*A^r := Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (by decide : 3*B≤A) _)
          _ = A^(q+r) := (pow_add ..).symm
          _ < B^(q+r)*2^1024 := cut
          _ = _ := by rw [pow_add]; ring
      exact Nat.lt_of_mul_lt_mul_right joined
    have up := bad_upper 1024 B (3^r*w) (by decide) (Nat.mul_pos (Nat.pow_pos (by decide)) pos) bad
    have joined : (B^q*2^1024)*run 1024 (3^r*w)<(B^q*2^1024)*w := by
      calc
        _ = B^q*(2^1024*run 1024 (3^r*w)) := by ring
        _ ≤ A^q*(3^r*w) := up
        _ = (A^q*3^r)*w := by ring
        _ < _ := Nat.mul_lt_mul_of_pos_right ratio pos
    exact Nat.lt_of_mul_lt_mul_left joined

#print axioms bad_tower_clock_1024
#print axioms small_good
#print axioms odd_clock_upper
#print axioms bad_upper
#print axioms bad_drop
#print axioms bad_clock_1024
end OddClockFloor

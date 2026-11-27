import CarryAlignment
import Mathlib.Data.Nat.Factorization.Basic

namespace Collatz.FirstPassage

def ReachesOne (n : ℕ) : Prop := ∃ h, run n h=1

private theorem run_add_ct (n h k : ℕ) : run n (h+k)=run (run n h) k := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih => simpa [Nat.succ_add,run] using ih (step n)

private theorem good_next_ct {n : ℕ} (hn : ReachesOne n) : ReachesOne (step n) := by
  obtain ⟨h,hit⟩ := hn
  cases h with
  | zero =>
    change n=1 at hit
    subst n
    exact ⟨1,by decide⟩
  | succ h => exact ⟨h,hit⟩

private theorem good_meet_ct {x m h : ℕ} (meet : run x h=step m)
    (hm : ReachesOne m) : ReachesOne x := by
  obtain ⟨k,hk⟩ := good_next_ct hm
  exact ⟨h+k,by rw [run_add_ct,meet,hk]⟩

private theorem two_at_one_ct (v : ℕ) : run (1+4*v) 2=1+3*v := by
  exact run_binary_translate 1 v 2

private theorem four_tower_ct (k u : ℕ) : run (1+4^k*u) (2*k)=1+3^k*u := by
  induction k generalizing u with
  | zero => simp [run]
  | succ k ih =>
    rw [show 2*(k+1)=2+2*k by omega,run_add_ct]
    rw [show 4^(k+1)*u=4*(4^k*u) by ring,two_at_one_ct]
    rw [show 3*(4^k*u)=4^k*(3*u) by ring,ih]
    ring

private theorem step_odd_plus_ct {b : ℕ} (hb : b%2=1) : step (1+3*b)=step b := by
  have h : (1+3*b)%2=0 := by omega
  simp [step,h,hb,Nat.add_comm]

private theorem pow_three_mod_two_ct (k : ℕ) : 3^k%2=1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ,Nat.mul_mod,ih]

/-- With an even binary valuation the canonical lower itself physically
meets a positive multiple of three of size at most 3(z-1)/16. -/
theorem even_four_tower_meet (a u : ℕ) (hu : u%2=1) :
    run (1+4^(a+2)*u) (2*(a+2)+1)=step (3^(a+1)*u) ∧
    32*(3^(a+1)*u) ≤ 6*(4^(a+2)*u) := by
  have hp : 3^(a+1)%2=1 := pow_three_mod_two_ct _
  have h : (3^(a+1)*u)%2=1 := by simp [Nat.mul_mod,hp,hu]
  constructor
  · rw [run_add_ct,four_tower_ct]
    change step (1+3^(a+2)*u)=step (3^(a+1)*u)
    rw [show 3^(a+2)*u=3*(3^(a+1)*u) by ring]
    exact step_odd_plus_ct h
  · have c : 3^a≤4^a := Nat.pow_le_pow_left (by decide) a
    have b := Nat.mul_le_mul_right u c
    calc
      32*(3^(a+1)*u)=96*(3^a*u) := by ring
      _ ≤ 96*(4^a*u) := Nat.mul_le_mul_left _ b
      _ = _ := by ring

/-- With an odd binary valuation the original upper physically meets a
multiple of three of size at most 9(z-1)/32. -/
theorem odd_four_tower_meet (a u : ℕ) (hu : u%2=1) :
    run (3*(1+2*4^(a+2)*u)) (2*a+6)=step (3^(a+2)*u) ∧
    32*(3^(a+2)*u) ≤ 9*(2*4^(a+2)*u) := by
  have hp : 3^(a+2)%2=1 := pow_three_mod_two_ct _
  have h : (3^(a+2)*u)%2=1 := by simp [Nat.mul_mod,hp,hu]
  have five : run (3+32*(3*4^a*u)) 5=1+27*4^a*u := by
    have e := run_binary_translate 3 (3*4^a*u) 5
    change run (3+32*(3*4^a*u)) 5=1+9*(3*4^a*u) at e
    rw [e]; ring
  constructor
  · rw [show 2*a+6=5+2*a+1 by omega,run_add_ct,run_add_ct]
    rw [show 3*(1+2*4^(a+2)*u)=3+32*(3*4^a*u) by ring,five]
    rw [show 27*4^a*u=4^a*(27*u) by ring,four_tower_ct]
    change step (1+3^a*(27*u))=step (3^(a+2)*u)
    rw [show 3^a*(27*u)=3*(3^(a+2)*u) by ring]
    exact step_odd_plus_ct h
  · have c : 3^a≤4^a := Nat.pow_le_pow_left (by decide) a
    have b := Nat.mul_le_mul_right u c
    calc
      32*(3^(a+2)*u)=288*(3^a*u) := by ring
      _ ≤ 288*(4^a*u) := Nat.mul_le_mul_left _ b
      _ = _ := by ring

/-- On the whole 1 mod 16 row in this range, every bad source has a
good triple. No location on the bounded cycle is assumed. -/
theorem small_canonical_orientation {M y : ℕ} (row : y%16=1)
    (size : 9*(y-1)<32*M)
    (smallTriple : ∀ n : ℕ, 0<n → 3∣n → n<M → ReachesOne n) :
    ReachesOne y ∨ ReachesOne (3*y) := by
  by_cases hy : y=1
  · subst y; exact Or.inl ⟨0,rfl⟩
  have form : y=1+16*(y/16) := by omega
  have nonzero : y/16≠0 := by omega
  obtain ⟨e,u,hu,he⟩ := Nat.exists_eq_two_pow_mul_odd nonzero
  have uodd : u%2=1 := by rcases hu with ⟨v,hv⟩; omega
  have upos : 0<u := by omega
  let a := e/2
  have casesE : e=2*a ∨ e=2*a+1 := by dsimp [a]; omega
  rcases casesE with even|odd
  · have ys : y=1+4^(a+2)*u := by
      calc
        y=1+16*(2^e*u) := by nth_rw 1 [form]; rw [he]
        _ = _ := by rw [even,pow_mul]; ring
    obtain ⟨hit,lim⟩ := even_four_tower_meet a u uodd
    rw [ys] at size ⊢
    have good : ReachesOne (3^(a+1)*u) := by
      apply smallTriple
      · positivity
      · exact ⟨3^a*u,by ring⟩
      · omega
    exact Or.inl (good_meet_ct hit good)
  · have ys : y=1+2*4^(a+2)*u := by
      calc
        y=1+16*(2^e*u) := by nth_rw 1 [form]; rw [he]
        _ = _ := by rw [odd,pow_succ,pow_mul]; ring
    obtain ⟨hit,lim⟩ := odd_four_tower_meet a u uodd
    rw [ys] at size ⊢
    have good : ReachesOne (3^(a+2)*u) := by
      apply smallTriple
      · positivity
      · exact ⟨3^(a+1)*u,by ring⟩
      · omega
    exact Or.inr (good_meet_ct hit good)

#print axioms even_four_tower_meet
#print axioms odd_four_tower_meet
#print axioms small_canonical_orientation

end Collatz.FirstPassage

namespace Collatz.FirstPassage

/-- A least canonical reverse disagreement within the small-triple range
is the least bad canonical integer, including over all other components. -/
theorem all_earlier_canonical_good {M z : ℕ} (size : 9*(z-1)<32*M)
    (smallTriple : ∀ n : ℕ, 0<n → 3∣n → n<M → ReachesOne n)
    (least : ∀ y : ℕ, y%48=17 → y<z → ReachesOne (3*y) → ReachesOne y)
    {y : ℕ} (row : y%48=17) (earlier : y<z) : ReachesOne y := by
  have r : y%16=1 := by omega
  have k : 9*(y-1)<32*M := by omega
  exact (small_canonical_orientation r k smallTriple).elim id (least y row earlier)

/-- The fourth-clock reduction is a bijection from the positive canonical
row onto 10 mod 27, with both parametrizations using the same integer k. -/
theorem canonical_fourth_value (k : ℕ) : run (17+48*k) 4=10+27*k := by
  have hit := run_binary_translate 17 (3*k) 4
  change run (17+16*(3*k)) 4=10+9*(3*k) at hit
  simpa only [show 16*(3*k)=48*k by ring,show 9*(3*k)=27*k by ring] using hit

#print axioms all_earlier_canonical_good
#print axioms canonical_fourth_value

end Collatz.FirstPassage

namespace Collatz.FirstPassage

private theorem odds_add_ct (n h k : ℕ) :
    odds n (h+k)=odds n h+odds (run n h) k := by
  induction h generalizing n with
  | zero => simp [odds,run]
  | succ h ih => simp [Nat.succ_add,odds,run,ih,Nat.add_assoc]

private theorem odds_translate_ct (c u h : ℕ) : odds (c+2^h*u) h=odds c h := by
  induction h generalizing c u with
  | zero => rfl
  | succ h ih =>
    rw [show 2^(h+1)*u=2*(2^h*u) by ring,odds,odds]
    have one := run_binary_translate c (2^h*u) 1
    change step (c+2*(2^h*u))=step c+3^(c%2+0)*(2^h*u) at one
    rw [one,show 3^(c%2+0)*(2^h*u)=2^h*(3^(c%2)*u) by ring,ih]
    omega

private theorem four_tower_grade_ct (k u : ℕ) : odds (1+4^k*u) (2*k)=k := by
  induction k generalizing u with
  | zero => rfl
  | succ k ih =>
    rw [show 2*(k+1)=2+2*k by omega,odds_add_ct]
    rw [show 4^(k+1)*u=4*(4^k*u) by ring,two_at_one_ct]
    rw [show 3*(4^k*u)=4^k*(3*u) by ring,ih]
    have h := odds_translate_ct 1 (4^k*u) 2
    change odds (1+4*(4^k*u)) 2=1 at h
    omega

/-- The entire original good upper suffix is the suffix of the smaller
positive multiple at its first ordinary successor, with exact prefix grade. -/
theorem odd_tower_upper_grade (k u : ℕ) (hu : u%2=1) :
    run (3*(1+2*4^(k+2)*u)) (2*k+6)=step (3^(k+2)*u) ∧
    odds (3*(1+2*4^(k+2)*u)) (2*k+6)=k+2 ∧
    run (1+2*4^(k+2)*u) (2*(k+2))=1+2*(3^(k+2)*u) := by
  refine ⟨(odd_four_tower_meet k u hu).1,?_,?_⟩
  · rw [show 2*k+6=5+2*k+1 by omega,odds_add_ct,odds_add_ct,run_add_ct]
    rw [show 3*(1+2*4^(k+2)*u)=3+32*(3*4^k*u) by ring]
    have five := run_binary_translate 3 (3*4^k*u) 5
    change run (3+32*(3*4^k*u)) 5=1+9*(3*4^k*u) at five
    have count := odds_translate_ct 3 (3*4^k*u) 5
    change odds (3+32*(3*4^k*u)) 5=2 at count
    rw [five,count,show 9*(3*4^k*u)=4^k*(27*u) by ring,
      four_tower_grade_ct,four_tower_ct]
    have oddPower := pow_three_mod_two_ct k
    have evenTarget : (1+3^k*(27*u))%2=0 := by
      simp [Nat.add_mod,Nat.mul_mod,oddPower,hu]
    simp [odds,evenTarget,Nat.add_comm]
  · rw [show 2*4^(k+2)*u=4^(k+2)*(2*u) by ring,four_tower_ct]
    ring

private theorem child_even_ct (b : ℕ) : run (2*(2*b)+1) 2=1+3*b := by
  rw [show 2*(2*b)+1=1+4*b by ring,two_at_one_ct]

/-- At an even block of length 2k+1 on the same actual good neighbor
word the bad child physically merges with 3^k times the continuing suffix. -/
theorem odd_even_block_child (k b : ℕ) (hb : b%2=1) :
    run (2*(2*4^k*b)+1) (2*k+3)=step (3^k*b) := by
  rw [show 2*k+3=2+2*k+1 by omega,run_add_ct,run_add_ct,
    show 2*4^k*b=2*(4^k*b) by ring,child_even_ct]
  rw [show 3*(4^k*b)=4^k*(3*b) by ring,four_tower_ct]
  change step (1+3^k*(3*b))=step (3^k*b)
  rw [show 3^k*(3*b)=3*(3^k*b) by ring]
  apply step_odd_plus_ct
  simp [Nat.mul_mod,pow_three_mod_two_ct,hb]

/-- At an even block of length 2k+2 on the same good neighbor word the
new child coefficient is exactly 3^(k+1). -/
theorem even_even_block_child (k b : ℕ) :
    run (2*(4^(k+1)*b)+1) (2*k+2)=1+2*(3^(k+1)*b) := by
  rw [show 2*k+2=2+2*k by omega,run_add_ct,
    show 4^(k+1)*b=2*(2*4^k*b) by ring,child_even_ct]
  rw [show 3*(2*4^k*b)=4^k*(6*b) by ring,four_tower_ct]
  ring

#print axioms odd_tower_upper_grade
#print axioms odd_even_block_child
#print axioms even_even_block_child

end Collatz.FirstPassage

namespace Collatz.FirstPassage

private theorem floor_one_eq_ct (x : ℕ) :
    2*step x=3^(x%2)*x+x%2 := by
  have d : x%2=0 ∨ x%2=1 := by omega
  rcases d with d|d <;> simp [step,d] <;> omega

/-- Clearing the affine word denominator, every odd departure charges the
endpoint at most 1/(3s) of its size when its physical source is at least s.
This bound does not assume a record clock or a simple path. -/
theorem floor_affine_remainder (x h s : ℕ)
    (floorAt : ∀ j<h, s≤run x j) :
    3*s*(2^h*run x h) ≤ 3*s*(3^(odds x h)*x)+odds x h*(2^h*run x h) := by
  induction h with
  | zero => simp [run,odds]
  | succ h ih =>
    have prev := ih (fun j hj => floorAt j (by omega))
    let v := run x h
    let p := odds x h
    have hv : s≤v := floorAt h (by omega)
    change 3*s*(2^h*v) ≤ 3*s*(3^p*x)+p*(2^h*v) at prev
    have ec := floor_one_eq_ct v
    rw [run_add_ct,odds_add_ct]
    change 3*s*(2^(h+1)*step v) ≤
      3*s*(3^(p+(v%2+0))*x)+(p+(v%2+0))*(2^(h+1)*step v)
    rw [Nat.add_zero,pow_succ,show 2^h*2*step v=2^h*(2*step v) by ring,ec]
    rcases (show v%2=0 ∨ v%2=1 by omega) with even|odd
    · simpa [even] using prev
    · simp only [odd,pow_one]
      rw [pow_succ]
      have first := Nat.mul_le_mul_left 3 prev
      have last := Nat.mul_le_mul_left (3*2^h) hv
      have extra : 0≤p*2^h := Nat.zero_le _
      nlinarith only [first,last,extra,Nat.zero_le (2^h)]

#print axioms floor_affine_remainder

end Collatz.FirstPassage

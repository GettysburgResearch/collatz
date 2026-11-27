import FirstPassage

set_option maxRecDepth 8192

namespace Collatz.FirstPassage

def charge (n h : ℕ) : ℤ := (h : ℤ) - 2 * odds n h

def HitCharge (n : ℕ) (d : ℤ) : Prop := ∃ h, run n h = 1 ∧ charge n h = d

private theorem run_add' (n h k : ℕ) : run n (h+k) = run (run n h) k := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih => simpa [Nat.succ_add,run] using ih (step n)

private theorem odds_add' (n h k : ℕ) :
    odds n (h+k) = odds n h + odds (run n h) k := by
  induction h generalizing n with
  | zero => simp [odds,run]
  | succ h ih => simp [Nat.succ_add,odds,run,ih,Nat.add_assoc]

private theorem charge_add' (n h k : ℕ) :
    charge n (h+k) = charge n h + charge (run n h) k := by
  simp only [charge,odds_add',Nat.cast_add]; ring

private theorem cycle_return (s : ℕ) : run 1 (2*s) = 1 ∧ charge 1 (2*s) = 0 := by
  induction s with
  | zero => decide
  | succ s ih =>
    rw [Nat.mul_succ,run_add',charge_add',ih.1,ih.2]
    decide

private theorem cycle_invariant (n h : ℕ) (hn : n=1 ∨ n=2) :
    (run n h = 1 ∨ run n h = 2) ∧ charge n h = (n:ℤ) - run n h := by
  induction h generalizing n with
  | zero => simpa [run,charge,odds] using hn
  | succ h ih =>
    rcases hn with rfl|rfl
    · specialize ih 2 (by decide)
      have ht : step 1 = 2 := by decide
      rw [show h+1=1+h by omega, run_add',charge_add']
      change (run (step 1) h = 1 ∨ run (step 1) h = 2) ∧
        charge 1 1 + charge (step 1) h = (1:ℤ) - run (step 1) h
      rw [ht,ih.2,show charge 1 1 = -1 by decide]
      exact ⟨ih.1,by omega⟩
    · specialize ih 1 (by decide)
      have ht : step 2 = 1 := by decide
      rw [show h+1=1+h by omega, run_add',charge_add']
      change (run (step 2) h = 1 ∨ run (step 2) h = 2) ∧
        charge 2 1 + charge (step 2) h = (2:ℤ) - run (step 2) h
      rw [ht,ih.2,show charge 2 1 = 1 by decide]
      exact ⟨ih.1,by omega⟩

private theorem hit_ordered {n i j : ℕ} (hij : i ≤ j)
    (hi : run n i = 1) (hj : run n j = 1) : charge n i = charge n j := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le hij
  rw [run_add',hi] at hj
  rw [charge_add',hi,(cycle_invariant 1 k (by decide)).2,hj]
  simp

/-- Every visit to one has the same integer charge, including later cycle laps. -/
theorem charge_unique {n : ℕ} {d e : ℤ} (hd : HitCharge n d)
    (he : HitCharge n e) : d=e := by
  obtain ⟨i,hi,rfl⟩ := hd
  obtain ⟨j,hj,rfl⟩ := he
  rcases Nat.le_total i j with h|h
  · exact hit_ordered h hi hj
  · exact (hit_ordered h hj hi).symm

private theorem hit_transport {n : ℕ} {d : ℤ} (hd : HitCharge n d) (a : ℕ) :
    HitCharge (run n a) (d-charge n a) := by
  obtain ⟨h,hit,hq⟩ := hd
  have ord : a+(h+a)=h+2*a := by omega
  have ht : run n (h+2*a)=1 := by rw [run_add',hit,(cycle_return a).1]
  have hc : charge n (h+2*a)=d := by rw [charge_add',hit,(cycle_return a).2,hq,add_zero]
  rw [←ord,run_add'] at ht
  rw [←ord,charge_add'] at hc
  exact ⟨h+a,ht,by linarith⟩

/-- A physical merger at any two clocks fixes the difference of hit charges. -/
theorem merger_charge {x y a b : ℕ} {d e : ℤ}
    (hx : HitCharge x d) (hy : HitCharge y e) (meet : run x a = run y b) :
    d-e = charge x a - charge y b := by
  have h := hit_transport hx a
  rw [meet] at h
  have eq := charge_unique h (hit_transport hy b)
  linarith

/-- Clock/grade-balanced transport across two actual arms preserves
the difference between their two eventual hit charges. -/
theorem paired_charge {x y a b c d : ℕ} {u v U V : ℤ}
    (hx : HitCharge x u) (hy : HitCharge y v)
    (hX : HitCharge (3*x) U) (hY : HitCharge (3*y) V)
    (ml : run x a = run y b) (mu : run (3*x) c = run (3*y) d)
    (bal : charge x a - charge y b = charge (3*x) c - charge (3*y) d) :
    u-U = v-V := by
  have a₀ := merger_charge hx hy ml
  have b₀ := merger_charge hX hY mu
  linarith

/-- 65 is an ordinary rank-43 upper-hit control. Its sole smaller canonical
parent is 17, and even arbitrarily late balanced two-arm mergers fail. -/
theorem no_balanced_65 {y a b c d : ℕ} (row : y%48=17) (small : y<65)
    (ml : run 65 a = run y b) (mu : run (3*65) c = run (3*y) d) :
    charge 65 a - charge y b ≠ charge (3*65) c - charge (3*y) d := by
  have yy : y=17 := by omega
  subst y
  have h₁ : HitCharge 65 3 := ⟨19,by decide,by decide⟩
  have h₂ : HitCharge 17 3 := ⟨9,by decide,by decide⟩
  have h₃ : HitCharge (3*65) (-10) := ⟨76,by decide,by decide⟩
  have h₄ : HitCharge (3*17) 3 := ⟨17,by decide,by decide⟩
  intro bal
  have e := paired_charge h₁ h₂ h₃ h₄ ml mu bal
  norm_num at e

/-- Ordinary edges can be traversed in either direction. Each paid edge
uses the leastness implication at a strictly smaller canonical source. -/
inductive CutWalk (cut : ℕ) : ℕ → ℕ → ℤ → ℤ → Prop where
  | nil (x : ℕ) : CutWalk cut x x 0 0
  | forward {x y : ℕ} {l p : ℤ} (next : CutWalk cut (step x) y l p) :
      CutWalk cut x y (l+1) (p+(x%2:ℕ))
  | backward {x y : ℕ} {l p : ℤ} (next : CutWalk cut x y l p) :
      CutWalk cut (step x) y (l-1) (p-(x%2:ℕ))
  | jump {x y : ℕ} {l p : ℤ} (row : x%48=17) (small : x<cut)
      (next : CutWalk cut (3*x) y l p) : CutWalk cut x y l p

private theorem hit_back {x : ℕ} {d : ℤ} (h : HitCharge (step x) d) :
    HitCharge x (d+charge x 1) := by
  obtain ⟨n,eq,hd⟩ := h
  refine ⟨1+n,?_,?_⟩
  · rw [run_add']; exact eq
  · rw [charge_add']
    change charge x 1+charge (step x) n=d+charge x 1
    omega

private theorem cut65_sum {x y : ℕ} {l p d e : ℤ}
    (path : CutWalk 65 x y l p) (start : HitCharge x d) (last : HitCharge y e) :
    d-e=l-2*p := by
  induction path generalizing d e with
  | nil x =>
    have eq := charge_unique start last
    omega
  | @forward x y l p _ ih =>
    have next := hit_transport start 1
    change HitCharge (step x) (d-charge x 1) at next
    have h := ih next last
    simp [charge,odds] at h
    omega
  | @backward x y l p _ ih =>
    have h := ih (hit_back start) last
    simp [charge,odds] at h
    omega
  | @jump x y l p row small _ ih =>
    have xx : x=17 := by omega
    subst x
    have h17 : HitCharge 17 3 := ⟨9,by decide,by decide⟩
    have h51 : HitCharge (3*17) 3 := ⟨17,by decide,by decide⟩
    have hd := charge_unique start h17
    have h := ih h51 last
    omega

/-- Even an arbitrarily long path with any number of smaller canonical
implication jumps cannot connect 65 to its triple with net clock zero. -/
theorem no_zero_clock_walk_65 {l p : ℤ} (path : CutWalk 65 65 (3*65) l p) :
    l%2=1 := by
  have h₁ : HitCharge 65 3 := ⟨19,by decide,by decide⟩
  have h₂ : HitCharge (3*65) (-10) := ⟨76,by decide,by decide⟩
  have h := cut65_sum path h₁ h₂
  omega

#print axioms no_zero_clock_walk_65
#print axioms charge_unique
#print axioms merger_charge
#print axioms paired_charge
#print axioms no_balanced_65

end Collatz.FirstPassage

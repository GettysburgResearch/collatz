import Portal

namespace Collatz.TernaryPortal

/-- A block of physically distinct starting pairs sharing one clock, grade
and ordered pair of outcomes. -/
def PairedBlock (base size k p x : Nat) : Prop :=
  ∀ i < size, run k (base+i) = x ∧ run k (3*(base+i)-1) = 3*x-1 ∧
    odds k (base+i) = p ∧ odds k (3*(base+i)-1) = p

private theorem lift_block {b n k p x : Nat} (hb : 0 < b) (hx : 0 < x)
    (seed : PairedBlock b n k p x) (t : Nat) :
    PairedBlock (b+2^k*t) n k p (x+3^p*t) := by
  intro i hi
  obtain ⟨ra, rb, oa, ob⟩ := seed i hi
  obtain ⟨la, lpa⟩ := prefix_lift k (b+i) t
  obtain ⟨lb, lpb⟩ := prefix_lift k (3*(b+i)-1) (3*t)
  rw [ra,oa] at la
  rw [oa] at lpa
  rw [rb,ob] at lb
  rw [ob] at lpb
  have low : b+2^k*t+i=(b+i)+2^k*t := by omega
  have high : 3*(b+2^k*t+i)-1=(3*(b+i)-1)+2^k*(3*t) := by
    rw [show 2^k*(3*t)=3*(2^k*t) by ring]
    omega
  rw [low, show 3*((b+i)+2^k*t)-1=(3*(b+i)-1)+2^k*(3*t) by simpa [low] using high,
      la,lb,lpa,lpb]
  rw [show 3^p*(3*t)=3*(3^p*t) by ring]
  omega

theorem paired_adjacent (t : Nat) :
    PairedBlock (204+256*t) 2 8 3 (22+27*t) := by
  refine lift_block (b:=204) (n:=2) (k:=8) (p:=3) (x:=22) (by decide) (by decide) ?_ t
  intro i hi
  rcases (show i=0 ∨ i=1 by omega) with rfl | rfl <;> decide

theorem paired_three (t : Nat) :
    PairedBlock (24748+32768*t) 3 15 6 (551+729*t) := by
  refine lift_block (b:=24748) (n:=3) (k:=15) (p:=6) (x:=551) (by decide) (by decide) ?_ t
  intro i hi
  rcases (show i=0 ∨ i=1 ∨ i=2 by omega) with rfl | rfl | rfl <;> decide

private theorem four_cross_table :
    ∀ r : Fin 16, ∃ i j : Fin 4,
      run 4 (r.val+1+i.val) = run 4 (3*(r.val+1+j.val)-1) ∧
      odds 4 (r.val+1+i.val) = odds 4 (3*(r.val+1+j.val)-1)+1 := by decide

/-- One of four consecutive lower starts physically merges with one of the
four upper starts by the fourth clock. -/
theorem four_cross (base : Nat) (hb : 0 < base) :
    ∃ i < 4, ∃ j < 4, run 4 (base+i) = run 4 (3*(base+j)-1) := by
  let r : Fin 16 := ⟨(base-1)%16, Nat.mod_lt _ (by decide)⟩
  let t := (base-1)/16
  have rep : base = r.val+1+16*t := by
    dsimp [r,t]
    omega
  obtain ⟨i,j,hit,grades⟩ := four_cross_table r
  obtain ⟨lo,_⟩ := prefix_lift 4 (r.val+1+i.val) t
  obtain ⟨up,_⟩ := prefix_lift 4 (3*(r.val+1+j.val)-1) (3*t)
  rw [show (2:Nat)^4=16 by decide] at lo up
  have lower : base+i.val=(r.val+1+i.val)+16*t := by omega
  have upper : 3*(base+j.val)-1=(3*(r.val+1+j.val)-1)+16*(3*t) := by omega
  refine ⟨i.val,i.isLt,j.val,j.isLt,?_⟩
  rw [lower,upper,lo,up,hit,grades,pow_succ]
  ring

private theorem short_table :
    ∀ r : Fin 8, ∀ k : Fin 4, 0 < k.val → ∃ i : Fin 4,
      odds k.val (r.val+i.val) ≠ odds k.val r.val := by decide

private theorem nonconstant_short (base k : Nat) (hk : 0 < k) (h3 : k < 4) :
    ∃ i < 4, odds k (base+i) ≠ odds k base := by
  let r : Fin 8 := ⟨base%8,Nat.mod_lt _ (by decide)⟩
  let t := base/8
  have rep : base = r.val+8*t := by dsimp [r,t]; omega
  have pw : 2^k * 2^(3-k)=8 := by rw [←pow_add,show k+(3-k)=3 by omega]; decide
  have sim (j : Nat) : odds k (base+j)=odds k (r.val+j) := by
    obtain ⟨_,hh⟩ := prefix_lift k (r.val+j) (2^(3-k)*t)
    rw [←Nat.mul_assoc,pw] at hh
    simpa only [show base+j=(r.val+j)+8*t by omega] using hh
  obtain ⟨i,hi⟩ := short_table r ⟨k,h3⟩ hk
  exact ⟨i.val,i.isLt,by simpa only [sim i.val,show odds k base=odds k r.val by simpa using sim 0] using hi⟩

/-- Three is the sharp upper limit on consecutive starting pairs with a
common nonmerged output and equal per-arm grade. -/
theorem no_paired_four (base k p x : Nat) (hb : 0 < base) (hx : 0 < x) :
    ¬ PairedBlock base 4 k p x := by
  intro block
  by_cases hk : k = 0
  · subst k
    obtain ⟨h0,_,_,_⟩ := block 0 (by decide)
    obtain ⟨h1,_,_,_⟩ := block 1 (by decide)
    simp [run] at h0 h1
    omega
  by_cases hs : k < 4
  · obtain ⟨i,hi,hn⟩ := nonconstant_short base k (by omega) hs
    obtain ⟨_,_,o0,_⟩ := block 0 (by decide)
    obtain ⟨_,_,oi,_⟩ := block i hi
    simp only [Nat.add_zero] at o0
    exact hn (oi.trans o0.symm)
  obtain ⟨i,hi,j,hj,e⟩ := four_cross base hb
  obtain ⟨li,_,_,_⟩ := block i hi
  obtain ⟨_,uj,_,_⟩ := block j hj
  have prop := congrArg (run (k-4)) e
  rw [←run_add,←run_add,show 4+(k-4)=k by omega,li,uj] at prop
  omega

#print axioms paired_adjacent
#print axioms paired_three
#print axioms four_cross
#print axioms no_paired_four

end Collatz.TernaryPortal

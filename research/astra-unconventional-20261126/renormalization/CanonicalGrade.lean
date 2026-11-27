import GradedMinima

/-! The canonical (17 mod 48) upper-word constraint. Fifty-four elementary
hits and one exact dyadic insertion cover every sufficiently high charge. -/
namespace Collatz.CanonicalGrade
open Collatz.SourceDeletion Collatz.GradedMinima
set_option exponentiation.threshold 10000
set_option maxRecDepth 65536

def expand (w : Nat) : Nat := 2^54*w+5*((2^54-1)/27)

theorem expand_eq (w : Nat) : 27*expand w+5=2^54*(27*w+5) := by unfold expand; ring

private def firstShift := (expand 17-17)/48

theorem canonical (k : Nat) : expand (17+48*k)=17+48*(2^54*k+firstShift) := by
  unfold firstShift expand; ring

private theorem twoOdds (k : Nat) :
    4*run 2 (3*(17+48*k))=27*(17+48*k)+5 ∧ odds 2 (3*(17+48*k))=2 := by
  have v := lift 2 51 (36*k)
  change run 2 (51+4*(36*k))=116+9*(36*k) at v
  have eqn : 3*(17+48*k)=51+4*(36*k) := by ring
  rw [eqn,v]
  constructor
  · ring
  · simp only [odds,step]; split_ifs <;> omega

private theorem halves (d u : Nat) : run d (2^d*u)=u ∧ odds d (2^d*u)=0 := by
  induction d with
  | zero => simp [run,odds]
  | succ d ih =>
    rw [pow_succ,show 2^d*2*u=2*(2^d*u) by ring,run,odds]
    have h : step (2*(2^d*u))=2^d*u := by unfold step; split <;> omega
    rw [h,ih.1,ih.2]; omega

/-- The added 54 halving clocks have no effect on any following upper word. -/
theorem upper_insertion (k d : Nat) :
    let w := 17+48*k
    run (56+d) (3*expand w)=run (2+d) (3*w) ∧
      odds (56+d) (3*expand w)=odds (2+d) (3*w) := by
  let w := 17+48*k
  have a := twoOdds k
  have b := twoOdds (2^54*k+firstShift)
  rw [←canonical] at b
  have val : run 2 (3*expand w)=2^54*run 2 (3*w) := by
    apply Nat.eq_of_mul_eq_mul_left (by decide : 0<4)
    rw [show 4*(2^54*run 2 (3*w))=2^54*(4*run 2 (3*w)) by ring, a.1,b.1]
    exact expand_eq _
  obtain ⟨v,o⟩ := Collatz.RankTwoControl.append 2 54 (3*expand w)
  rw [val,(halves 54 _).1] at v
  rw [val,(halves 54 _).2,b.2] at o
  obtain ⟨v1,o1⟩ := Collatz.RankTwoControl.append 56 d (3*expand w)
  obtain ⟨v2,o2⟩ := Collatz.RankTwoControl.append 2 d (3*w)
  rw [←v] at v2 o2
  exact ⟨v1.trans v2.symm, by dsimp [w] at *; omega⟩

private def seeds : List (Nat × Nat) := [(275873,26), (171425,27), (48545,22), (25889,21), (28577,26), (8609,21), (3233,18), (6785,27), (1313,20), (2129,27), (785,24), (161,17), (257,24), (641,35), (1361,44), (17,17), (113,34), (1409,55), (2945,64), (3185,69), (497,60), (881,67), (5297,84), (1649,79), (1841,84), (2177,89), (1985,92), (305,83), (65,76), (593,95), (689,100), (4625,117), (3953,120), (833,113), (13313,136), (15857,141), (13841,144), (22385,151), (26609,156), (55553,165), (11729,158), (78017,175), (53873,176), (19505,173), (40049,182), (115457,193), (103601,196), (92993,199), (79217,202), (31553,199), (350801,220), (108401,215), (514673,230), (147569,225)]

def seed (i : Fin 54) : Nat × Nat := seeds.getD i.val (17,17)

set_option maxHeartbeats 6000000 in
/-- The 54 consecutive unshifted ordinary-hit charges range from -18 to 35. -/
theorem all_seed_charges : ∀ i : Fin 54,
    let w := (seed i).1
    let h := (seed i).2
    w%48=17 ∧ run h (3*w)=1 ∧ 2*odds h (3*w)+18=h+i.val := by decide

#print axioms expand_eq
#print axioms canonical
#print axioms upper_insertion
#print axioms all_seed_charges
end Collatz.CanonicalGrade

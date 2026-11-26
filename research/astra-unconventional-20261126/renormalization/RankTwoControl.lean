import PhysicalWindow

/-! A complete, convergent control against two upper-grade-priority merger rules. -/
namespace Collatz.RankTwoControl
open Collatz.SourceDeletion

theorem append (h d x : Nat) :
    run (h+d) x=run d (run h x) ∧ odds (h+d) x=odds h x+odds d (run h x) := by
  induction h generalizing x with
  | zero => simp [run,odds]
  | succ h ih =>
    obtain ⟨a,b⟩ := ih (step x)
    rw [Nat.succ_add]
    simp only [run,odds,a,b]
    exact ⟨trivial,by omega⟩

theorem cycle_pairs (h : Nat) : run (2*h) 1=1 ∧ odds (2*h) 1=h := by
  induction h with
  | zero => decide
  | succ h ih =>
    rw [show 2*(h+1)=2+2*h by omega]
    obtain ⟨a,b⟩ := append 2 (2*h) 1
    rw [show run 2 1=1 by decide,ih.1] at a
    rw [show run 2 1=1 by decide,show odds 2 1=1 by decide,ih.2] at b
    exact ⟨a,by omega⟩

private theorem cycle_cost (d : Nat) (hit : run d 1=1) : 2*odds d 1=d := by
  by_cases even : d%2=0
  · have eqn : d=2*(d/2) := by omega
    conv_lhs => arg 2; rw [eqn,(cycle_pairs _).2]
    omega
  · have eqn : d=2*(d/2)+1 := by omega
    have it := (append (2*(d/2)) 1 1).1
    rw [(cycle_pairs _).1,←eqn,hit] at it
    exact False.elim ((by decide : ¬1=run 1 1) it)

private theorem terminal_charge_ordered {x H J : Nat} (le : H≤J)
    (hx : run H x=1) (jx : run J x=1) : 2*odds H x+J=2*odds J x+H := by
  obtain ⟨a,b⟩ := append H (J-H) x
  rw [Nat.add_sub_of_le le,hx,jx] at a
  rw [Nat.add_sub_of_le le,hx] at b
  have cyc := cycle_cost _ a.symm
  omega

/-- All hits at one on the same ordinary trajectory have the same charge. -/
theorem terminal_charge {x H J : Nat} (hx : run H x=1) (jx : run J x=1) :
    2*odds H x+J=2*odds J x+H := by
  rcases Nat.le_total H J with le|le
  · exact terminal_charge_ordered le hx jx
  · exact (terminal_charge_ordered le jx hx).symm

theorem growth (h y : Nat) (pos : 0<y) :
    2^h*run h y ≤ 4^(odds h y)*y := by
  induction h generalizing y with
  | zero => simp [run,odds]
  | succ h ih =>
    have py : 0<step y := by unfold step; split <;> omega
    have single : 2*step y≤4^(y%2)*y := by
      unfold step
      split
      · rename_i ev; rw [ev,pow_zero]; omega
      · have odd : y%2=1 := by omega
        rw [odd,pow_one]; omega
    simp only [run,odds,pow_succ,pow_add]
    calc
      _ = 2*(2^h*run h (step y)) := by ring
      _ ≤ 2*(4^(odds h (step y))*step y) := Nat.mul_le_mul_left _ (ih _ py)
      _ = 4^(odds h (step y))*(2*step y) := by ring
      _ ≤ 4^(odds h (step y))*(4^(y%2)*y) := Nat.mul_le_mul_left _ single
      _ = _ := by ring

set_option maxRecDepth 32768 in
private theorem hard_peak :
    run 89 (3^11-1)=1 ∧ odds 89 (3^11-1)=45 := by decide

set_option maxRecDepth 32768 in
private theorem plus18 : run 127 (3^18+1)=1 ∧ odds 127 (3^18+1)=62 := by decide

set_option maxRecDepth 32768 in
private theorem plus45 : run 303 (3^45+1)=1 ∧ odds 303 (3^45+1)=146 := by decide

/-- No canonical upper-grade-two peak shares an augmented same-clock endpoint
with the actual lower peak of the first third-grade hard control. -/
theorem no_augmented_plus (s h : Nat) (class_s : s%27=18)
    (same : run h (3^s+1)=run h (3^11-1))
    (paid : s+odds h (3^s+1)=11+odds h (3^11-1)) : False := by
  let H := 89+2*h
  have hp := append 89 (2*h) (3^11-1)
  rw [hard_peak.1,hard_peak.2,(cycle_pairs h).1,(cycle_pairs h).2] at hp
  obtain ⟨a,b⟩ := append h (H-h) (3^s+1)
  obtain ⟨a',b'⟩ := append h (H-h) (3^11-1)
  have le : h≤H := by dsimp [H]; omega
  rw [Nat.add_sub_of_le le,same] at a b
  rw [Nat.add_sub_of_le le] at a' b'
  have hit : run H (3^s+1)=1 := by rw [a,←a']; exact hp.1
  have work : 2*s+2*odds H (3^s+1)=H+23 := by dsimp [H] at *; omega
  have bound := growth H (3^s+1) (Nat.succ_pos _)
  rw [hit,Nat.mul_one] at bound
  have p4 (t : Nat) : (4:Nat)^t=2^(2*t) := by rw [pow_mul]; norm_num
  have put : (4:Nat)^s*4^(odds H (3^s+1))=2^H*2^23 := by
    rw [p4,p4,←pow_add,work,pow_add]
  have bound' := Nat.mul_le_mul_left (4^s) bound
  have bnd : (4:Nat)^s≤2^23*(3^s+1) := by
    have pre : 2^H*4^s≤2^H*(2^23*(3^s+1)) := calc
      _ = 4^s*2^H := by ring
      _ ≤ _ := bound'
      _ = (4^s*4^(odds H (3^s+1)))*(3^s+1) := by ring
      _ = _ := by rw [put]; ring
    exact Nat.le_of_mul_le_mul_left pre (Nat.two_pow_pos H)
  have small : s<60 := by
    by_contra! ge
    obtain ⟨t,eqn⟩ := Nat.exists_eq_add_of_le ge
    have growing (d : Nat) : 2^23*(3^(60+d)+1)<(4:Nat)^(60+d) := by
      induction d with
      | zero => decide
      | succ d ih =>
        rw [show 60+(d+1)=(60+d)+1 by omega,pow_succ (3:Nat) (60+d),pow_succ (4:Nat) (60+d)]
        omega
    rw [eqn] at bnd
    exact (Nat.not_lt_of_ge bnd) (growing t)
  have cases : s=18 ∨ s=45 := by omega
  rcases cases with eqn|eqn
  · subst s
    have fixed := terminal_charge hit plus18.1
    rw [plus18.2] at fixed
    omega
  · subst s
    have fixed := terminal_charge hit plus45.1
    rw [plus45.2] at fixed
    omega

private theorem pair_floor (s t u : Nat) (within : t≤2*s) :
    3^s*u+1 ≤ run t (4^s*u+1) := by
  induction s generalizing t u with
  | zero =>
    have eqn : t=0 := by omega
    simp [eqn,run]
  | succ s ih =>
    let v := 4^s*u
    have val : 4^(s+1)*u+1=4*v+1 := by dsimp [v]; ring
    have a : step (4*v+1)=6*v+2 := by unfold step; split <;> omega
    have b : step (6*v+2)=3*v+1 := by unfold step; split <;> omega
    have cmp : 3^s*u≤v := Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide) _)
    have lower : 3^(s+1)*u=3*(3^s*u) := by ring
    cases t with
    | zero => rw [run,val,lower]; omega
    | succ t =>
      cases t with
      | zero => rw [val,run,a,run,lower]; omega
      | succ t =>
        have row : 3*v+1=4^s*(3*u)+1 := by dsimp [v]; ring
        rw [run,run,val,a,b,row]
        have tail := ih t (3*u) (by omega)
        convert tail using 1; ring

private def prefixMax : Nat → Nat → Nat
  | 0,x => x
  | h+1,x => max x (prefixMax h (step x))

private theorem bounded_by_prefix (h t n : Nat) (lt : t≤h) : run t n≤prefixMax h n := by
  induction h generalizing t n with
  | zero =>
    have eqn : t=0 := by omega
    simp [eqn,run,prefixMax]
  | succ h ih =>
    cases t with
    | zero => exact Nat.le_max_left _ _
    | succ t => exact (ih t (step n) (by omega)).trans (Nat.le_max_right _ _)

private theorem cycle_small (t x : Nat) (cases : x=1 ∨ x=2) : run t x≤2 := by
  induction t generalizing x with
  | zero => change x≤2; omega
  | succ t ih =>
    apply ih
    rcases cases with eqn|eqn <;> subst x <;> decide

set_option maxRecDepth 32768 in
private theorem actual_maximum : prefixMax 107 3233=638468 ∧ run 107 3233=1 := by decide

/-- Every point on the lower orbit of the supplied hard control is strictly
below every rank-two parent's lower arm until its own upper-hit deadline. -/
theorem before_upper_hit (s v h t : Nat) (hs : 18≤s) (param : 27*v+1=4^s)
    (within : t≤2*s+5) : run h 3233 < run t (32*v+1) := by
  have upper : run h 3233≤638468 := by
    by_cases early : h≤107
    · rw [←actual_maximum.1]; exact bounded_by_prefix _ _ _ early
    · have tail := (append 107 (h-107) 3233).1
      rw [Nat.add_sub_of_le (by omega),actual_maximum.2] at tail
      rw [tail]; exact (cycle_small _ _ (Or.inl rfl)).trans (by decide)
  have power : 3^18≤(3:Nat)^s := Nat.pow_le_pow_right (by decide) hs
  have min_power : 3*3^s+2≤2*4^s := by
    have grow (n : Nat) : 3*3^(n+2)+2≤2*4^(n+2) := by
      induction n with
      | zero => decide
      | succ n ih =>
        rw [show n+1+2=(n+2)+1 by omega,pow_succ (3:Nat) (n+2),pow_succ (4:Nat) (n+2)]
        omega
    simpa only [Nat.sub_add_cancel (show 2≤s by omega)] using grow (s-2)
  have first : 3^s≤18*v := by omega
  have a : step (32*v+1)=48*v+2 := by unfold step; split <;> omega
  have b : step (48*v+2)=24*v+1 := by unfold step; split <;> omega
  have c : step (24*v+1)=36*v+2 := by unfold step; split <;> omega
  have d : step (36*v+2)=18*v+1 := by unfold step; split <;> omega
  have e : step (18*v+1)=27*v+2 := by unfold step; split <;> omega
  have lower : 3^s+1≤run t (32*v+1) := by
    by_cases early : t<5
    · have cases : t=0 ∨ t=1 ∨ t=2 ∨ t=3 ∨ t=4 := by omega
      rcases cases with h|h|h|h|h <;> subst t <;> simp only [run,a,b,c,d] <;> omega
    · have pre : run 5 (32*v+1)=4^s+1 := by simp only [run,a,b,c,d,e]; omega
      have tail := (append 5 (t-5) (32*v+1)).1
      rw [Nat.add_sub_of_le (by omega),pre] at tail
      rw [tail]
      simpa using pair_floor s (t-5) 1 (by omega)
  norm_num at power
  omega

#print axioms terminal_charge
#print axioms no_augmented_plus
#print axioms before_upper_hit
end Collatz.RankTwoControl

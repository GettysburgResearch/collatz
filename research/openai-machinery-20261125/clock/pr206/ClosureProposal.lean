module

public import CycleDetection
public import CycleAmplification
public import FixedGate
import all TernaryItinerary
import all FixedGate

public section
namespace Collatz.Itinerary.Proposal

open FixedGate CycleRows
set_option autoImplicit false

/-- A test of the cumulative clock on one actual forward orbit. -/
@[expose] def Crosses (a : Nat) : Prop :=
  ∃ k, (k+1)*(3^k)^6 < (2^(elapsed k a))^6

/-- Crossing the clock boundary either produces a smaller odd value or
certifies a nontrivial cycle on this very source's trajectory. -/
theorem crossing_descent_or_cycle {a k : Nat} {c : Bool} (ha : 2<a) (ho : a%2=1)
    (hc : a%3=digit c) (clock : (k+1)*(3^k)^6 < (2^(elapsed k a))^6) :
    after k a<a ∨ ReachesNontrivialCycle a := by
  obtain ⟨rs,hl,r,_,_⟩ := route_exists k a ho hc
  by_cases lt : after k a<a
  · exact .inl lt
  have lower : a≤after k a := by omega
  have prod := Nat.mul_lt_mul_of_pos_right clock (Nat.pow_pos (by omega : 0<a) (n:=6))
  have raise := Nat.mul_le_mul_left ((2^(elapsed k a))^6) (Nat.pow_le_pow_left lower 6)
  apply Or.inr
  apply reached_cycle_of_distortion r (by omega)
  simpa only [hl,Nat.mul_pow,Nat.mul_assoc] using Nat.lt_of_lt_of_le prod raise

private theorem double_le_pow (i : Nat) : 2*i≤2^i := by
  induction i with
  | zero => decide
  | succ i ih =>
    rw [Nat.pow_succ]
    by_cases h : i=0
    · subst i; decide
    · omega

private theorem neutral_eventually_crosses (t : Nat) :
    ∃ i, (t+i+1)*(3^(t+i))^6 < (2^(2*i))^6 := by
  let A := (3^t)^6
  let i := t+2+A
  have apos : 0<A := Nat.pow_pos (Nat.pow_pos (by decide))
  have twice := double_le_pow i
  have cap : t+i+1<2^i := by dsimp [i] at *; omega
  have capA : A≤2^i := by dsimp [i] at *; omega
  have small :=
    Nat.lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_right cap apos) (Nat.mul_le_mul_left (2^i) capA)
  have final : (2^i*2^i)*(3^i)^6 ≤ (2^(2*i))^6 := by
    calc
      _ = (4*3^6)^i := by
        rw [Nat.mul_pow,Nat.pow_right_comm 3 6 i,show 4^i=2^i*2^i by rw [←Nat.mul_pow]]
      _ ≤ (4^6)^i := Nat.pow_le_pow_left (by decide) i
      _ = _ := by rw [Nat.pow_mul,Nat.pow_right_comm]
  refine ⟨i,?_⟩
  have mult := Nat.mul_lt_mul_of_pos_right small (Nat.pow_pos (Nat.pow_pos (by decide : 0<3) (n:=i)) (n:=6))
  simpa only [A,Nat.pow_add,Nat.mul_pow,Nat.mul_assoc] using Nat.lt_of_lt_of_le mult final

private theorem elapsed_add (i j a : Nat) :
    elapsed (i+j) a = elapsed i a + elapsed j (after i a) := by
  induction i generalizing a with
  | zero => simp [elapsed,after]
  | succ i ih => simp only [Nat.succ_add,elapsed,after,ih,Nat.add_assoc]

private theorem clock_one (n : Nat) : elapsed n 1=2*n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [snoc_clock,after_one,ih]
    change 2*n+2=2*(n+1)
    omega

theorem crosses_of_hit {a : Nat} {c : Bool} (ho : a%2=1) (hc : a%3=digit c)
    (hit : ReachesOne a) : Crosses a := by
  obtain ⟨t,h⟩ := hit
  obtain ⟨rs,hl,r,odd,_⟩ := route_exists t a ho hc
  have le := r.depth_le_clock
  have clock : t+(elapsed t a-t)=elapsed t a := by omega
  have eq := r.follow
  rw [←clock,run_add,h] at eq
  have atOne : after t a=1 := by
    rcases small_cycle (elapsed t a-t) 1 (Or.inl rfl) with h₁ | h₂ <;> omega
  obtain ⟨i,large⟩ := neutral_eventually_crosses t
  have ex : 2*i≤elapsed (t+i) a := by rw [elapsed_add,atOne,clock_one]; omega
  exact ⟨t+i,Nat.lt_of_lt_of_le large
    (Nat.pow_le_pow_left (Nat.pow_le_pow_right (by decide) ex) 6)⟩

private theorem no_cycle_of_universal (all : Universal) : ¬NontrivialCycle := by
  rintro ⟨q,s,rs,above,len,loop⟩
  obtain ⟨t,hit⟩ := all q (by omega)
  have pos := loop.depth_le_clock
  have periodic (i : Nat) : run (i*s) q=q := by
    induction i with
    | zero => simp [run]
    | succ i ih => rw [Nat.succ_mul,run_add,ih,loop.follow]
  have enough : t≤(t+1)*s := by
    have hh := Nat.mul_le_mul_left (t+1) (show 1≤s by omega)
    omega
  have endLap := periodic (t+1)
  have split : (t+1)*s=t+((t+1)*s-t) := by omega
  rw [split,run_add,hit] at endLap
  rcases small_cycle ((t+1)*s-t) 1 (Or.inl rfl) with l | l <;> omega

/-- The two required global statements concern only an integer clock on
ordinary forward iterates and absence of finite row witnesses. -/
theorem universal_iff_clocks_and_rows : Universal ↔
    (∀ (a : Nat) (c : Bool), a%2=1 → a%3=digit c → Crosses a) ∧
    (∀ b, ¬Witness b) := by
  constructor
  · intro all
    exact ⟨fun a c ho hc => crosses_of_hit ho hc (all a (by omega)),
      fun _ w => no_cycle_of_universal all (witness_implies_cycle w)⟩
  · rintro ⟨crosses,empty⟩
    have no : ¬NontrivialCycle := by
      intro loop
      obtain ⟨b,_,w⟩ := CycleAmplification.cycle_amplifies loop 0
      exact empty b w
    have good (a : Nat) (c : Bool) (ho : a%2=1) (hc : a%3=digit c) : ReachesOne a := by
      induction a using Nat.strongRecOn generalizing c with
      | ind a ih =>
        by_cases h : a=1
        · subst a; exact ⟨0,rfl⟩
        obtain ⟨k,hk⟩ := crosses a c ho hc
        obtain ⟨rs,_,r,odd,d,hd⟩ := route_exists k a ho hc
        rcases crossing_descent_or_cycle (by omega) ho hc hk with smaller | arrived
        · obtain ⟨j,hj⟩ := ih _ smaller d odd hd
          exact ⟨elapsed k a+j,by rw [run_add,r.follow,hj]⟩
        · obtain ⟨_,q,s,marks,_,above,len,lap⟩ := arrived
          exact False.elim (no ⟨q,s,marks,above,len,lap⟩)
    apply Classical.byContradiction
    intro fail
    obtain ⟨a,c,ho,hc,bad⟩ := odd_bad_unit fail
    exact bad (good a c ho hc)

#print axioms crossing_descent_or_cycle
#print axioms crosses_of_hit
#print axioms universal_iff_clocks_and_rows
end Collatz.Itinerary.Proposal

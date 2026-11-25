module

public import ClosureProposal
import all ClosureProposal
import all FixedGate
import all TernaryItinerary

public section
namespace Collatz.Itinerary.ClockBridge

open FixedGate
set_option autoImplicit false

/-- Number of odd shortcut inputs in the actual first t ordinary steps. -/
def odds : Nat → Nat → Nat
  | 0, _ => 0
  | t+1, a => odds t (step a) + a%2

/-- The ordinary lift preserves the full previous branch count and moves the
endpoint by its exact odd multiplier. For d=1 the two new endpoint bits differ. -/
theorem ordinary_lift (t a d : Nat) :
    run t (a+2^t*d) = run t a + 3^(odds t a)*d ∧
    odds t (a+2^t*d) = odds t a := by
  induction t generalizing a d with
  | zero => simp [run,odds]
  | succ t ih =>
    let m := 2^t*d
    have lift : a+2^(t+1)*d = a+2*m := by simp [m,Nat.pow_succ]; ac_rfl
    rw [lift]
    have par : (a+2*m)%2 = a%2 := by omega
    by_cases e : a%2=0
    · have s : step (a+2*m) = step a+m := by simp [step,par,e]; omega
      simpa [run,odds,s,par,e,m] using ih (step a) d
    · have o : a%2=1 := by omega
      have s : step (a+2*m) = step a+2^t*(3*d) := by
        have eq : 2^t*(3*d)=3*m := by dsimp [m]; ac_rfl
        rw [eq]
        simp [step,par,o]
        omega
      obtain ⟨h₁,h₂⟩ := ih (step a) (3*d)
      simp only [run,odds,s,par,o,h₁,h₂,Nat.pow_succ,Nat.mul_assoc, and_self]

/-- Enumerate a complete dyadic row by splitting each residue into its two lifts. -/
def rowSum : Nat → (Nat → Nat) → Nat
  | 0, f => f 0
  | t+1, f => rowSum t (fun a => f a + f (a+2^t))

private theorem sum_split (l : List Nat) (f g : Nat → Nat) :
    (l.map (fun a => f a+g a)).sum = (l.map f).sum+(l.map g).sum := by
  induction l with
  | nil => simp
  | cons a l ih => simp only [List.map_cons,List.sum_cons,ih]; omega

/-- The binary recursion visits every ordinary representative in the stated
half-open interval exactly once. -/
theorem rowSum_eq_range (t : Nat) (f : Nat → Nat) :
    rowSum t f = ((List.range (2^t)).map f).sum := by
  induction t generalizing f with
  | zero => simp [rowSum,List.range_succ]
  | succ t ih =>
    rw [rowSum,ih,sum_split,show 2^(t+1)=2^t+2^t by rw [Nat.pow_succ]; omega]
    simp only [List.range_add,List.map_append,List.sum_append,List.map_map]
    simp [Function.comp_def,Nat.add_comm]

private theorem rowScale (t m : Nat) (f : Nat → Nat) :
    rowSum t (fun a => m*f a) = m*rowSum t f := by
  induction t generalizing f with
  | zero => rfl
  | succ t ih =>
    simp only [rowSum,←Nat.mul_add]
    exact ih _

private theorem rowMono (t : Nat) {f g : Nat → Nat} (h : ∀ a, f a ≤ g a) :
    rowSum t f ≤ rowSum t g := by
  induction t generalizing f g with
  | zero => exact h 0
  | succ t ih => exact ih (fun a => Nat.add_le_add (h a) (h _))

private theorem odds_snoc (t a : Nat) :
    odds (t+1) a = odds t a + run t a%2 := by
  induction t generalizing a with
  | zero => simp [odds,run]
  | succ t ih =>
    change odds (t+1) (step a)+a%2 = (odds t (step a)+a%2)+run t (step a)%2
    rw [ih]; omega

private theorem odds_le (t a : Nat) : odds t a ≤ t := by
  induction t generalizing a with
  | zero => exact Nat.le_refl _
  | succ t ih =>
    have := ih (step a)
    simp only [odds]; omega

/-- Integer tilt, two per even input and three per odd input. -/
def weight (t a : Nat) := 2^(t-odds t a) * 3^(odds t a)

private theorem weight_snoc (t a : Nat) :
    weight (t+1) a = weight t a*(2+run t a%2) := by
  have le := odds_le t a
  rcases (show run t a%2=0 ∨ run t a%2=1 by omega) with h|h
  · simp only [weight,odds_snoc,h,Nat.add_zero]
    rw [show t+1-odds t a = (t-odds t a)+1 by omega,Nat.pow_succ]
    ac_rfl
  · simp only [weight,odds_snoc,h,Nat.add_sub_add_right,Nat.pow_succ]
    ac_rfl

private theorem sibling_weight (t a d : Nat) (odd : d%2=1) :
    weight (t+1) a + weight (t+1) (a+2^t*d) = 5*weight t a := by
  obtain ⟨endpoint,count⟩ := ordinary_lift t a d
  have w : weight t (a+2^t*d)=weight t a := by simp [weight,count]
  have p (n : Nat) : 3^n%2=1 := by
    induction n with
    | zero => decide
    | succ n ih => rw [Nat.pow_succ,Nat.mul_mod,ih]
  have flip : (3^(odds t a)*d)%2=1 := by rw [Nat.mul_mod,p,odd]
  rw [weight_snoc,weight_snoc,w,endpoint,←Nat.mul_add]
  have bits : 2+run t a%2+(2+(run t a+3^(odds t a)*d)%2)=5 := by omega
  rw [bits,Nat.mul_comm]

/-- Exact tilted mass of every ordinary affine dyadic row of odd stride.
The row b=2, d=3 starts at the shortcut images of the odd inputs 2r+1. -/
theorem ordinary_pressure (t b d : Nat) (odd : d%2=1) :
    rowSum t (fun r => weight t (b+d*r)) = 5^t := by
  induction t with
  | zero => simp [rowSum,weight,odds]
  | succ t ih =>
    simp only [rowSum]
    have pair (a : Nat) : weight (t+1) (b+d*a) + weight (t+1) (b+d*(a+2^t))
        = 5*weight t (b+d*a) := by
      rw [show b+d*(a+2^t)=b+d*a+2^t*d by rw [Nat.mul_add]; ac_rfl]
      exact sibling_weight t _ _ odd
    simp only [pair,rowScale,ih,Nat.pow_succ,Nat.mul_comm]

private theorem weight_mono (t j k : Nat) (kj : k≤j) (jt : j≤t) :
    2^(t-k)*3^k ≤ 2^(t-j)*3^j := by
  induction j with
  | zero => have : k = 0 := by omega
            subst k; exact Nat.le_refl _
  | succ j ih =>
    by_cases same : k=j+1
    · rw [same]; exact Nat.le_refl _
    have prev := ih (by omega) (by omega)
    apply Nat.le_trans prev
    rw [show t-j=(t-(j+1))+1 by omega,Nat.pow_succ,Nat.pow_succ]
    have fact : 2^(t-(j+1))*2*3^j = (2^(t-(j+1))*3^j)*2 := by ac_rfl
    rw [fact,←Nat.mul_assoc]
    exact Nat.mul_le_mul_left _ (by decide : 2≤3)

/-- Exact integer Chernoff certificate for inputs whose t-step post-initial
ordinary segment contains at least k odd inputs. The right side is independent
of the ordinary row offset and odd stride. -/
theorem high_odd_row_bound (t k b d : Nat) (odd : d%2=1) :
    (2^(t-k)*3^k) * rowSum t (fun r => if k≤odds t (b+d*r) then 1 else 0) ≤ 5^t := by
  rw [←ordinary_pressure t b d odd,←rowScale]
  apply rowMono
  intro r
  split
  · rename_i h
    simpa [weight] using weight_mono t (odds t (b+d*r)) k h (odds_le _ _)
  · simp

private theorem odds_add (i j a : Nat) :
    odds (i+j) a = odds i a + odds j (run i a) := by
  induction i generalizing a with
  | zero => simp [odds,run]
  | succ i ih =>
    simp only [Nat.succ_add,odds,run,ih]
    omega

private theorem even_block (n y : Nat) : odds n (2^n*y)=0 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have norm : 2^(n+1)*y = 2*(2^n*y) := by rw [Nat.pow_succ]; ac_rfl
    simpa [norm,odds,step] using ih

private theorem gap_count {e a y : Nat} (g : Gap e a y) : odds e a=1 := by
  cases e with
  | zero => have := g.pos; omega
  | succ n =>
    have eqn := g.eqn
    have h : 2^(n+1)*y = 2*(2^n*y) := by rw [Nat.pow_succ]; ac_rfl
    rw [h] at eqn
    have s : step a = 2^n*y := by simp [step,g.oddSource]; omega
    simp [odds,s,even_block,g.oddSource]

private theorem elapsed_orbit (k a : Nat) (odd : a%2=1) :
    odds (elapsed k a) a=k ∧ (run (elapsed k a) a)%2=1 := by
  induction k generalizing a with
  | zero => simp [elapsed,odds,run,odd]
  | succ k ih =>
    have g := next_gap odd
    obtain ⟨count,parity⟩ := ih (next a).2 g.oddTarget
    rw [elapsed,odds_add,run_add,g.follow,gap_count g,count,parity]
    exact ⟨by omega,rfl⟩

/-- In the actual t post-initial shortcut positions, reaching the kth odd
return by t gives at least k odd inputs. This transfers the exact PR 206
accelerated clock to the ordinary dyadic row. -/
theorem clock_le_implies_odds {k a t : Nat} (odd : a%2=1) (clock : elapsed k a≤t) :
    k ≤ odds t (step a) := by
  obtain ⟨count,parity⟩ := elapsed_orbit k a odd
  have atReturn := odds_snoc (elapsed k a) a
  change odds (elapsed k a) (step a)+a%2 = _ at atReturn
  rw [count,parity,odd] at atReturn
  have splitT : t=elapsed k a + (t-elapsed k a) := by omega
  rw [splitT,odds_add]
  omega

/-- A rational tail estimate stated directly in the PR 206 clock on ordinary
starts 2*(d*r+m)+1 for every odd d, uniformly in d and m. -/
theorem clock_failure_bound (t k m d : Nat) (odd : d%2=1)
    (threshold : (k+1)*(3^k)^6 < (2^(t+1))^6) :
    (2^(t-k)*3^k) * rowSum t (fun r =>
      if (2^(elapsed k (2*(d*r+m)+1)))^6 ≤ (k+1)*(3^k)^6 then 1 else 0) ≤ 5^t := by
  have stride : (3*d)%2=1 := by omega
  apply Nat.le_trans _ (high_odd_row_bound t k (3*m+2) (3*d) stride)
  apply Nat.mul_le_mul_left
  apply rowMono
  intro r
  let a := 2*(d*r+m)+1
  have par : a%2=1 := by dsimp [a]; omega
  have stepA : step a=3*m+2+(3*d)*r := by
    rw [Nat.mul_assoc]; simp [step,par,a]; omega
  change (if (2^(elapsed k a))^6 ≤ _ then 1 else 0) ≤ _
  split
  · rename_i fail
    have le : elapsed k a ≤ t := by
      by_cases le : elapsed k a ≤ t
      · exact le
      · have late : t+1 ≤ elapsed k a := by omega
        have h := Nat.pow_le_pow_left (Nat.pow_le_pow_right (by decide : 0<2) late) 6
        omega
    have h := clock_le_implies_odds par le
    rw [stepA] at h
    simp [h]
  · exact Nat.zero_le _


private theorem linear_bound (n : Nat) : 3*n+1 ≤ 2^(n+1) := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [Nat.pow_succ]
    cases n with
    | zero => decide
    | succ n => omega

private theorem triple_cut (n : Nat) : (3*n+1)*(3^(3*n))^6 < (2^(5*n+1))^6 := by
  have term : (3^(3*n))^6=(3^18)^n := by
    rw [←Nat.pow_mul,←Nat.pow_mul]
    congr 1; omega
  have cap : (2^(5*n+1))^6=64*(2^30)^n := by
    rw [Nat.pow_succ 2 (5*n),Nat.mul_pow,←Nat.pow_mul,←Nat.pow_mul]
    have eq : 5*n*6=30*n := by omega
    rw [eq,Nat.mul_comm]
  rw [term,cap]
  have small := Nat.mul_le_mul_right ((3^18)^n) (linear_bound n)
  have pair : 2^(n+1)*((3^18)^n) = 2*((2*3^18)^n) := by
    rw [Nat.pow_succ,Nat.mul_pow]
    ac_rfl
  rw [pair] at small
  have compare := Nat.pow_le_pow_left (by decide : 2*3^18 ≤ 2^30) n
  have positive := Nat.pow_pos (n:=n) (by decide : 0<2^30)
  omega

/-- Among 32^n ordinary representatives in any such odd-stride row,
the proportion failing the (3n)th clock test is at most (3125/3456)^n.
All comparisons in the kernel statement are exact natural-number ones. -/
theorem exponentially_sparse_clock (n m d : Nat) (odd : d%2=1) :
    108^n * rowSum (5*n) (fun r =>
      if (2^(elapsed (3*n) (2*(d*r+m)+1)))^6 ≤ (3*n+1)*(3^(3*n))^6 then 1 else 0)
      ≤ 3125^n := by
  have h := clock_failure_bound (5*n) (3*n) m d odd (triple_cut n)
  rw [show 5*n-3*n=2*n by omega,Nat.pow_mul,Nat.pow_mul,←Nat.mul_pow,Nat.pow_mul] at h
  simpa only [Nat.pow_mul] using h


private theorem central_arithmetic {b : Nat} (hb : 0<b) :
    (b+1)*(3^b)^6 < (2^(2*b))^6 := by
  have count : b+1≤2^b := Nat.lt_two_pow_self
  have low := Nat.mul_le_mul_right ((3^b)^6) count
  have h : 2^b*(3^b)^6 = (2*3^6)^b := by
    rw [Nat.mul_pow,Nat.pow_right_comm 3 6 b]
  have upper : (2^(2*b))^6 = (4^6)^b := by rw [Nat.pow_mul,Nat.pow_right_comm]
  rw [upper]
  rw [h] at low
  exact Nat.lt_of_le_of_lt low (Nat.pow_lt_pow_left (by decide : 2*3^6<4^6) (Nat.ne_of_gt hb))

/-- Every positive-depth balanced source counted at (b,2b) crosses the
PR 206 boundary at that very depth. A central-row lower count cannot serve
as a lower count for clock failure at the same horizon. -/
theorem balanced_forces_cross {b x : Nat} (hb : 0<b) (bal : elapsed b x=2*b) :
    (b+1)*(3^b)^6 < (2^(elapsed b x))^6 := by rw [bal]; exact central_arithmetic hb

/-- Exact cost of appending j odd returns at the terminal of a balanced
prefix. This includes the inherited starting clock, without resampling. -/
theorem balanced_suffix_iff {b x q : Nat} (bal : elapsed b x=2*b)
    (dest : after b x=q) (j : Nat) :
    (2^(elapsed (b+j) x))^6 ≤ (b+j+1)*(3^(b+j))^6 ↔
    (2^(2*b))^6*(2^(elapsed j q))^6 ≤ (b+j+1)*((3^b)^6*(3^j)^6) := by
  rw [Proposal.elapsed_add,bal,dest,Nat.pow_add,Nat.mul_pow,Nat.pow_add,Nat.mul_pow]

private theorem elapsed_ge (k a : Nat) (odd : a%2=1) : k≤elapsed k a := by
  induction k generalizing a with
  | zero => exact Nat.zero_le _
  | succ k ih =>
    have g := next_gap odd
    have rest := ih (next a).2 g.oddTarget
    have pos := g.pos
    simp only [elapsed]; omega

/-- A balanced prefix ending at a genuine odd terminal cannot supply our
3n-th failure even after a suffix of j odd returns unless b≤2n and n≤j. -/
theorem balanced_failure_needs_suffix {b j n x q : Nat} (bal : elapsed b x=2*b)
    (dest : after b x=q) (odd : q%2=1) (index : b+j=3*n)
    (fail : (2^(elapsed (b+j) x))^6 ≤ (b+j+1)*(3^(b+j))^6) :
    b≤2*n ∧ n≤j := by
  have cap := triple_cut n
  rw [←index] at cap
  have total := Nat.lt_of_le_of_lt fail cap
  have bound : elapsed (b+j) x ≤ 5*n := by
    by_cases h : elapsed (b+j) x≤5*n
    · exact h
    · have late : 5*n+1≤elapsed (b+j) x := by omega
      have := Nat.pow_le_pow_left (Nat.pow_le_pow_right (by decide : 0<2) late) 6
      omega
  rw [Proposal.elapsed_add,bal,dest] at bound
  have := elapsed_ge j q odd
  omega

/-- Even the enlarged balanced terminal shell q≤2^b places every original
source in [1,9^n] once b≤2n. This bound holds across all such b simultaneously. -/
theorem aligned_balanced_height {b n q x : Nat} {rs : List Bool}
    (r : Route q rs (2*b) x) (len : rs.length=b) (shell : q≤2^b) (depth : b≤2*n) :
    x≤9^n := by
  have bound : 3^b*x ≤ 3^b*3^b := by
    calc
      3^b*x ≤ 2^(2*b)*q := by simpa only [len] using r.scale
      _ ≤ 2^(2*b)*2^b := Nat.mul_le_mul_left _ shell
      _ = 8^b := by rw [Nat.pow_mul,←Nat.mul_pow]
      _ ≤ 9^b := Nat.pow_le_pow_left (by decide) b
      _ = 3^b*3^b := by rw [←Nat.mul_pow]
  have first := Nat.le_of_mul_le_mul_left bound (Nat.pow_pos (by decide : 0<3))
  have second := Nat.pow_le_pow_right (by decide : 0<3) depth
  simpa only [Nat.pow_mul] using Nat.le_trans first second

/-- Even before a balanced prefix ends, depths b≤9n with terminal q≤2^n
cannot supply enough distinct positive original integers to defeat the
3n-th clock bound. The PR 207 ceiling-sqrt shell lies here when n≥9. -/
theorem early_balanced_height {b n q x : Nat} {rs : List Bool}
    (r : Route q rs (2*b) x) (len : rs.length=b) (shell : q≤2^n) (depth : b≤9*n) :
    108^n*x ≤ 3125^n := by
  let z := 9*n-b
  have splitClock : 9*n = b+z := by dsimp [z]; omega
  have affine : 3^b*x ≤ 4^b * 2^n := by
    apply Nat.le_trans _ (Nat.mul_le_mul_left _ shell)
    simpa only [len,Nat.pow_mul] using r.scale
  have scaled : 3^(9*n)*x ≤ 4^(9*n)*2^n := by
    rw [splitClock,Nat.pow_add,Nat.pow_add]
    calc
      (3^b*3^z)*x = 3^z*(3^b*x) := by ac_rfl
      _ ≤ 4^z*(4^b*2^n) := Nat.mul_le_mul (Nat.pow_le_pow_left (by decide) z) affine
      _ = _ := by ac_rfl
  have ceiling : (108^n*x)*3^(9*n) ≤ 3125^n*3^(9*n) := by
    calc
      (108^n*x)*3^(9*n) = 108^n*(3^(9*n)*x) := by ac_rfl
      _ ≤ 108^n*(4^(9*n)*2^n) := Nat.mul_le_mul_left _ scaled
      _ = (108*(4^9*2))^n := by rw [Nat.pow_mul,Nat.mul_pow,Nat.mul_pow]
      _ ≤ (3125*3^9)^n := Nat.pow_le_pow_left (by decide) n
      _ = 3125^n*3^(9*n) := by rw [Nat.mul_pow,Nat.pow_mul]
  exact Nat.le_of_mul_le_mul_right ceiling (Nat.pow_pos (by decide : 0<3))

/-- The minimum of an escaping ordinary odd tail fails every clock test,
using the descent-or-cycle implication of the frozen PR 206. -/
theorem minimum_tail_fails {a : Nat} {c : Bool} (above : 2<a) (odd : a%2=1)
    (color : a%3=digit c) (floor : ∀ k, a≤after k a)
    (noCycle : ¬CycleRows.ReachesNontrivialCycle a) (k : Nat) :
    (2^(elapsed k a))^6 ≤ (k+1)*(3^k)^6 := by
  by_cases h : (2^(elapsed k a))^6 ≤ (k+1)*(3^k)^6
  · exact h
  · have cross := Proposal.crossing_descent_or_cycle above odd color (Nat.lt_of_not_ge h)
    cases cross with
    | inl descend => have := floor k; omega
    | inr cycle => exact False.elim (noCycle cycle)

private theorem base_pred (q : Nat) (odd : q%2=1) (unit : q%3≠0) :
    ∃ e x, Gap e x q ∧ x%3=q%3 := by
  have cases9 : q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega
  rcases cases9 with h|h|h|h|h|h
  · refine ⟨2,(4*q-1)/3,⟨by decide,?_,odd,?_⟩,?_⟩ <;> omega
  · refine ⟨3,(8*q-1)/3,⟨by decide,?_,odd,?_⟩,?_⟩ <;> omega
  · refine ⟨6,(64*q-1)/3,⟨by decide,?_,odd,?_⟩,?_⟩ <;> omega
  · refine ⟨5,(32*q-1)/3,⟨by decide,?_,odd,?_⟩,?_⟩ <;> omega
  · refine ⟨4,(16*q-1)/3,⟨by decide,?_,odd,?_⟩,?_⟩ <;> omega
  · refine ⟨1,(2*q-1)/3,⟨by decide,?_,odd,?_⟩,?_⟩ <;> omega

private theorem lengthen {e x q : Nat} (g : Gap e x q) (j : Nat) :
    ∃ y, Gap (e+6*j) y q ∧ y%3=x%3 := by
  induction j with
  | zero => exact ⟨x,by simpa using g,rfl⟩
  | succ j ih =>
    obtain ⟨y,edge,color⟩ := ih
    refine ⟨64*y+21,⟨by have := g.pos; omega,by omega,g.oddTarget,?_⟩,by omega⟩
    rw [show e+6*(j+1)=(e+6*j)+6 by omega,Nat.pow_add,Nat.mul_right_comm,edge.eqn]
    omega

/-- For every eligible odd target and every finite horizon, a genuine
one-gap predecessor in the same ternary class passes *all* positive clock
tests through that horizon. Forward behavior from q is completely preserved. -/
theorem crossing_predecessor (q K : Nat) (odd : q%2=1) (unit : q%3≠0) :
    ∃ e y, Gap e y q ∧ y%3=q%3 ∧
      ∀ j, 0<j → j≤K → (j+1)*(3^j)^6 < (2^(elapsed j y))^6 := by
  obtain ⟨e,x,g,color⟩ := base_pred q odd unit
  obtain ⟨y,edge,same⟩ := lengthen g K
  refine ⟨_,y,edge,same.trans color,?_⟩
  intro j pos bound
  have time : 2*j≤elapsed j y := by
    cases j with
    | zero => omega
    | succ j =>
      simp only [elapsed,gap_next edge]
      omega
  exact Nat.lt_of_lt_of_le (central_arithmetic pos)
    (Nat.pow_le_pow_left (Nat.pow_le_pow_right (by decide : 0<2) time) 6)

/-- Both ordinary starts converge and have the same ternary color. The
target fails the third test while its one-gap predecessor crosses it. -/
theorem backward_transfer_control :
    Gap 10 2389 7 ∧ 2389%6=7%6 ∧ run 11 7=1 ∧ run 21 2389=1 ∧
    elapsed 3 7=4 ∧ elapsed 3 2389=12 ∧
    (2^(elapsed 3 7))^6 ≤ 4*(3^3)^6 ∧ 4*(3^3)^6 < (2^(elapsed 3 2389))^6 := by
  exact ⟨⟨by decide,by decide,by decide,by decide⟩,by decide⟩


/-- A genuine positive odd source with a prescribed string of unit gaps. -/
def nearPower (k u : Nat) := 2*(2^k*u)-1

private theorem unitGap (k u : Nat) (hu : 0<u) :
    Gap 1 (nearPower (k+1) u) (nearPower k (3*u)) := by
  let m := 2^k*u
  have pos : 0<m := Nat.mul_pos (Nat.two_pow_pos k) hu
  have a : nearPower (k+1) u = 4*m-1 := by
    unfold nearPower
    rw [Nat.pow_succ]
    have h : 2*(2^k*2*u) = 4*m := by dsimp [m]; change 2*(2^k*2*u)= (2*2)*(2^k*u); ac_rfl
    rw [h]
  have b : nearPower k (3*u) = 6*m-1 := by
    unfold nearPower
    have h : 2*(2^k*(3*u)) = 6*m := by dsimp [m]; change 2*(2^k*(3*u))=(2*3)*(2^k*u); ac_rfl
    rw [h]
  rw [a,b]
  constructor <;> first | decide | omega | (change 2*(6*m-1)=3*(4*m-1)+1; omega)

theorem unit_prefix (j k u : Nat) (bound : j≤k) (hu : 0<u) :
    elapsed j (nearPower k u)=j := by
  induction j generalizing k u with
  | zero => rfl
  | succ j ih =>
    cases k with
    | zero => omega
    | succ k =>
      have gap := gap_next (unitGap k u hu)
      simp only [elapsed,gap]
      rw [ih k (3*u) (by omega) (by omega)]
      omega

/-- No universal finite horizon for the forward-clock half of PR 206,
even after restricting ordinary sources to the eligible ternary class 2. -/
theorem arbitrarily_long_failure (K : Nat) :
    ∃ a, 0<a ∧ a%2=1 ∧ a%3=digit true ∧
      ∀ j, j≤K → (2^(elapsed j a))^6 ≤ (j+1)*(3^j)^6 := by
  refine ⟨nearPower K 3, ?_, ?_, ?_, ?_⟩
  · simp only [nearPower]; have := Nat.two_pow_pos K; omega
  · simp only [nearPower]; have := Nat.two_pow_pos K; omega
  · change (2*(2^K*3)-1)%3=2; have := Nat.two_pow_pos K; omega
  · intro j hj
    rw [unit_prefix j K 3 hj (by decide)]
    have h := Nat.pow_le_pow_left (Nat.pow_le_pow_left (by decide : 2≤3) j) 6
    have h' := Nat.mul_le_mul_right ((3^j)^6) (show 1≤j+1 by omega)
    omega

/-- Same ordinary source bits through the first eight odd returns, same
admissible ternary color, opposite verdict at the tenth odd return. -/
theorem split_pair :
    1535%512=3071%512 ∧ 1535%3=2 ∧ 3071%3=2 ∧
    elapsed 8 1535=8 ∧ elapsed 8 3071=8 ∧
    elapsed 10 1535=19 ∧ elapsed 10 3071=11 ∧
    11*(3^10)^6 < (2^(elapsed 10 1535))^6 ∧
    (2^(elapsed 10 3071))^6 ≤ 11*(3^10)^6 := by decide

theorem pair_left_crosses : Proposal.Crosses 1535 :=
  ⟨10, split_pair.2.2.2.2.2.2.2.1⟩

#print axioms rowSum_eq_range
#print axioms ordinary_lift
#print axioms ordinary_pressure
#print axioms high_odd_row_bound
#print axioms clock_le_implies_odds
#print axioms clock_failure_bound
#print axioms exponentially_sparse_clock
#print axioms balanced_forces_cross
#print axioms balanced_suffix_iff
#print axioms balanced_failure_needs_suffix
#print axioms aligned_balanced_height
#print axioms early_balanced_height
#print axioms minimum_tail_fails
#print axioms crossing_predecessor
#print axioms backward_transfer_control
#print axioms unit_prefix
#print axioms arbitrarily_long_failure
#print axioms split_pair
#print axioms pair_left_crosses
end Collatz.Itinerary.ClockBridge

import ShadowBarrier

/-! Cut an arbitrary physical visitor at the ternary precision of the supplied
ordinary target.  Neither the visitor clock nor its odd count is bounded. -/
namespace Collatz.PhysicalWindow
open Collatz.SourceDeletion Collatz.SignedBudget Collatz.ShadowBarrier

def offset : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, x => 3^(odds h (step x))*(x%2) + 2*offset h (step x)

private theorem single (x : Nat) : 2*step x = 3^(x%2)*x + x%2 := by
  by_cases ev : x%2=0
  · simp only [step,ev,ite_true,pow_zero,one_mul,Nat.add_zero]; omega
  · have od : x%2=1 := by omega
    simp only [step,ev,ite_false]; rw [od,pow_one]; omega

theorem affine (h w : Nat) :
    2^h*run h w = 3^(odds h w)*w + offset h w := by
  induction h generalizing w with
  | zero => simp [run,odds,offset]
  | succ h ih =>
    simp only [run,odds,offset,pow_add,pow_succ]
    calc
      _ = 2*(2^h*run h (step w)) := by ring
      _ = 2*(3^(odds h (step w))*step w + offset h (step w)) := by rw [ih]
      _ = 3^(odds h (step w))*(2*step w)+2*offset h (step w) := by ring
      _ = _ := by rw [single]; ring

theorem offset_bound (h w : Nat) : offset h w + 2^h ≤ 3^h := by
  induction h generalizing w with
  | zero => simp [offset]
  | succ h ih =>
    have a := ih (step w)
    have b : 3^(odds h (step w))*(w%2) ≤ (3:Nat)^h := calc
      _ ≤ 3^(odds h (step w))*1 := Nat.mul_le_mul_left _ (by omega)
      _ ≤ _ := by rw [Nat.mul_one]; exact Nat.pow_le_pow_right (by decide) (odd_le _ _)
    simp only [offset,pow_succ]
    omega

/-- A common final clock produces a *small integer* center. The case c=−1
is precisely a same-clock Mersenne peak with the augmented grades equal. -/
theorem cut (h j u N : Nat)
    (same : run h u = run h (3^j-1))
    (paid : N+odds h u = j+odds h (3^j-1)) :
    ∃ c : Int, (u:Int) = 3^N+c ∧ -(2*3^h) ≤ c ∧ c ≤ 3^h ∧
      (c = -1 ↔ u = 3^N-1) := by
  let x : Nat := 3^j-1
  let p := odds h x
  let q := odds h u
  let c : Int := (u:Int)-3^N
  have px : (x:Int) = (3:Int)^j-1 := by
    dsimp [x]; rw [Nat.cast_sub (Nat.pow_pos (by decide) : 1≤(3:Nat)^j)]; push_cast; rfl
  have eqn : (3:Int)^q*c = (offset h x:Int)-(3:Int)^p-(offset h u:Int) := by
    have lo := affine h x
    have hi := affine h u
    change run h u=run h x at same
    rw [same,lo] at hi
    have hi' := congrArg (fun z : Nat => (z:Int)) hi
    push_cast at hi'
    rw [px] at hi'
    have pp : (3:Int)^q*3^N=(3:Int)^p*3^j := by
      rw [←pow_add,←pow_add]
      congr 1
      change N+q=j+p at paid
      omega
    dsimp only [c]; rw [mul_sub,pp]
    change (3:Int)^p*((3:Int)^j-1)+offset h x=3^q*(u:Int)+offset h u at hi'
    linarith only [hi']
  have ub := offset_bound h u
  have xb := offset_bound h x
  have bp : (3:Int)^p ≤ 3^h := by exact_mod_cast Nat.pow_le_pow_right (by decide : 0<(3:Nat)) (odd_le h x)
  have b1 : (offset h u:Int) ≤ (3:Int)^h := by exact_mod_cast (Nat.le_trans (Nat.le_add_right _ _) ub)
  have b2 : (offset h x:Int) ≤ (3:Int)^h := by exact_mod_cast (Nat.le_trans (Nat.le_add_right _ _) xb)
  have oq : (1:Int)≤3^q := by
    have p0 : (0:Int)<3^q := by positivity
    omega
  have nonneg : (0:Int) ≤ 3^p := by positivity
  have nonnegH : (0:Int) ≤ 3^h := by positivity
  have lb : -(2*(3:Int)^h)≤c := by
    by_contra! fail
    have cn : c≤0 := by omega
    have scale := Int.mul_le_mul_of_nonpos_right oq cn
    simp only [one_mul] at scale
    omega
  have ubc : c≤(3:Int)^h := by
    by_contra! fail
    have cn : 0≤c := by omega
    have scale := Int.mul_le_mul_of_nonneg_right oq cn
    simp only [one_mul] at scale
    omega
  refine ⟨c,by dsimp [c]; ring,lb,ubc,?_⟩
  have pos : 1 ≤ (3:Nat)^N := Nat.pow_pos (by decide)
  have sub : ((3^N-1:Nat):Int) = (3:Int)^N-1 := by rw [Nat.cast_sub pos]; push_cast; rfl
  dsimp [c]
  constructor
  · intro eqn
    apply Int.ofNat_inj.mp
    rw [sub]; omega
  · intro eqn
    rw [eqn,sub]; ring

/-- Splitting on a prescribed number of initial odd inputs is always possible
for the actual word. -/
theorem split_odds (h w k : Nat) (hk : k≤odds h w) :
    ∃ i t, h=i+t ∧ odds i w=k ∧ odds t (run i w)=odds h w-k ∧
      run t (run i w)=run h w := by
  induction h generalizing w k with
  | zero => exact ⟨0,0,rfl,by symm; simpa [odds] using hk,by simp [odds],rfl⟩
  | succ h ih =>
    by_cases zero : k=0
    · subst k; exact ⟨0,h+1,by omega,rfl,by simp [run],rfl⟩
    · have p : k-w%2≤odds h (step w) := by simp only [odds] at hk; omega
      obtain ⟨i,t,split,first,remain,eqn⟩ := ih (step w) (k-w%2) p
      exact ⟨i+1,t,by omega,by simp only [odds]; omega,by simp only [run,odds]; omega,eqn⟩

theorem rise (h w : Nat) : 2^(odds h w)*(run h w+1) ≤ 3^(odds h w)*(w+1) := by
  induction h generalizing w with
  | zero => simp [run,odds]
  | succ h ih =>
    have one : 2^(w%2)*(step w+1) ≤ 3^(w%2)*(w+1) := by
      by_cases ev : w%2=0
      · simp only [step,ev,ite_true,pow_zero,one_mul]; omega
      · have od : w%2=1 := by omega
        simp only [step,ev,ite_false]; rw [od,pow_one]; omega
    simp only [run,odds,pow_add]
    calc
      _ = 2^(w%2)*(2^(odds h (step w))*(run h (step w)+1)) := by ring
      _ ≤ 2^(w%2)*(3^(odds h (step w))*(step w+1)) := Nat.mul_le_mul_left _ (ih _)
      _ = 3^(odds h (step w))*(2^(w%2)*(step w+1)) := by ring
      _ ≤ 3^(odds h (step w))*(3^(w%2)*(w+1)) := Nat.mul_le_mul_left _ one
      _ = _ := by ring

/-- Exact positive-center inequality for an arbitrarily long visitor. -/
theorem positive_cost {h w N : Nat} {c : Int} (pos : 0<c)
    (ending : (run h w:Int)=3^N+c) :
    (3:Int)^N*2^(odds h w-N) ≤ c*3^(odds h w-N)*(w+1) := by
  let e := odds h w-N
  obtain ⟨i,t,_,first,rest,finish⟩ := split_odds h w e (Nat.sub_le _ _)
  have depth : odds t (run i w) ≤ N := by dsimp [e] at rest; omega
  rw [←finish] at ending
  have floor := positive_floor pos ending depth
  have gain : (2:Int)^e*((run i w:Int)+1) ≤ (3:Int)^e*(w+1) := by
    exact_mod_cast (first ▸ rise i w : 2^e*(run i w+1)≤3^e*(w+1))
  calc
    _ ≤ (c*(run i w:Int))*2^e := Int.mul_le_mul_of_nonneg_right floor (by positivity)
    _ ≤ c*(2^e*((run i w:Int)+1)) := by
      have : 0≤c*(2:Int)^e := by positivity
      linarith only [this]
    _ ≤ c*((3:Int)^e*(w+1)) := Int.mul_le_mul_of_nonneg_left gain (by omega)
    _ = _ := by ring

/-- Exact negative-center inequality for an arbitrarily long visitor. -/
theorem negative_cost {h w N : Nat} {c : Int} (neg : c ≤ -2)
    (room : 2*(-c) ≤ (2:Int)^N) (ending : (run h w:Int)=3^N+c) :
    (8:Int)^N*4^(odds h w-N) ≤ 4*potential c*9^(odds h w-N)*((w:Int)+1)^2 := by
  let e := odds h w-N
  obtain ⟨i,t,_,first,rest,finish⟩ := split_odds h w e (Nat.sub_le _ _)
  have depth : odds t (run i w) ≤ N := by dsimp [e] at rest; omega
  rw [←finish] at ending
  have floor := negative_floor neg room ending depth
  have gain : (2:Int)^e*((run i w:Int)+1) ≤ (3:Int)^e*(w+1) := by
    exact_mod_cast (first ▸ rise i w : 2^e*(run i w+1)≤3^e*(w+1))
  have gain' : (2:Int)^e*(run i w:Int) ≤ (3:Int)^e*(w+1) := by
    have p : 0 ≤ (2:Int)^e := by positivity
    linarith only [p,gain]
  have sq := pow_le_pow_left₀ (show 0≤(2:Int)^e*(run i w:Int) by positivity) gain' 2
  have pc : 0 ≤ 4*potential c := by have := potential_lower c; nlinarith [sq_nonneg c]
  have p2 : ((2:Int)^e)^2=4^e := by rw [←pow_mul,Nat.mul_comm,pow_mul]; norm_num
  have p3 : ((3:Int)^e)^2=9^e := by rw [←pow_mul,Nat.mul_comm,pow_mul]; norm_num
  calc
    _ ≤ (4*(run i w:Int)^2*potential c)*4^e :=
      Int.mul_le_mul_of_nonneg_right floor (by positivity)
    _ = (4*potential c)*((2:Int)^e*(run i w:Int))^2 := by rw [mul_pow,p2]; ring
    _ ≤ (4*potential c)*((3:Int)^e*(w+1))^2 := Int.mul_le_mul_of_nonneg_left sq pc
    _ = _ := by rw [mul_pow,p3]; ring

#print axioms affine
#print axioms offset_bound
#print axioms cut
#print axioms split_odds
#print axioms rise
#print axioms positive_cost
#print axioms negative_cost
end Collatz.PhysicalWindow

import PhysicalWindow

/-! An off-ascent visitor must pay for the shortest signed word rooted at −2
and a further, strictly quantified odd budget. -/
namespace Collatz.AscentMerger
open Collatz.SourceDeletion Collatz.SignedBudget Collatz.ShadowBarrier Collatz.PhysicalWindow

def SignedClock (r S : Nat) : Prop :=
  ∃ s : Int, travel S s = -2 ∧ digits S s = r

private theorem step_ramp (b : Nat) (pos : 0<b) : step (2*b-1)=3*b-1 := by
  unfold step
  split <;> omega

theorem ramp (r a : Nat) (pos : 0<a) :
    run r (2^r*a-1)=3^r*a-1 ∧ odds r (2^r*a-1)=r := by
  induction r generalizing a with
  | zero => simp [run,odds]
  | succ r ih =>
    have p : 0<2^r*a := Nat.mul_pos (Nat.two_pow_pos _) pos
    have eqn : 2^(r+1)*a=2*(2^r*a) := by ring
    have scaled : 3*(2^r*a)=2^r*(3*a) := by ring
    obtain ⟨lo,ct⟩ := ih (3*a) (by omega)
    simp only [run,odds,eqn,step_ramp _ p,scaled,lo,ct]
    rw [show (2*(2^r*a)-1)%2=1 by omega, pow_succ]
    constructor
    · rw [Nat.mul_assoc]
    · omega

/-- The ordinary branch structure at a first intersection with an odd final
native input determines the visitor's different predecessor. -/
theorem other_predecessor {u v y : Nat} (odd : u%2=1) (native : step u=y)
    (visitor : step v=y) (diff : u≠v) : v=2*y := by
  unfold step at native visitor
  split at native <;> split at visitor <;> omega

private theorem through_precision {h b r a : Nat} (pos : 0<a)
    (ending : run h b+2=2*a*3^r) (depth : odds h b ≤ r) :
    ∃ s : Int, travel h s = -2 ∧ digits h s = odds h b ∧
      (2:Int)^(h-odds h b+1)*((2:Int)^r*a-1) < b+1 := by
  have eqn : (run h b:Int)=(2*(a:Int))*3^r+(-2) := by
    have c := congrArg (fun n : Nat => (n:Int)) ending
    push_cast at c
    linarith only [c]
  obtain ⟨s,hs,hq,bs⟩ := shadow_coeff eqn depth
  have mag := negative_magnitude h s (by omega)
  rw [hs,hq] at mag
  let q := odds h b
  let F : Int := 2^(h-q+1)
  have left : -s ≤ F := by
    change -s ≤ (2:Int)^(h-q)*(-(-2)) at mag
    dsimp [F]; rw [pow_succ]; linarith only [mag]
  have scale : F*2^q=2^(h+1) := by
    dsimp [F]; rw [←pow_add]; congr 1
    have := odd_le h b
    dsimp [q]; omega
  have economic : (2:Int)^r ≤ 2^q*3^(r-q) := calc
    _ = 2^q*2^(r-q) := by rw [←pow_add]; congr 1; dsimp [q]; omega
    _ ≤ _ := Int.mul_le_mul_of_nonneg_left (pow_le_pow_left₀ (by decide) (by decide) _) (by positivity)
  have bound :=
    Int.mul_le_mul_of_nonneg_left (Int.mul_le_mul_of_nonneg_right economic
     (show 0≤(a:Int) by positivity)) (show 0≤F by dsimp [F]; positivity)
  change (b:Int)=s+2^h*(2*a*3^(r-q)) at bs
  have rewrite_prod : F*(2^q*3^(r-q)*a) = 2^h*(2*(a:Int)*3^(r-q)) := by
    rw [show F*(2^q*3^(r-q)*a) = (F*2^q)*(a*3^(r-q)) by ring,scale,pow_succ]; ring
  rw [rewrite_prod] at bound
  refine ⟨s,hs,hq,?_⟩
  change F*(2^r*(a:Int)-1) < b+1
  linarith only [bound,bs,left]

/-- This is the lower bound for one supplied visitor. The returned S is
witnessed by an actual signed integer with its complete negative itinerary. -/
theorem lower_witness {H w r a : Nat} (pos : 0<a) (small : w<2^r*a-1)
    (ending : run H w+2=2*a*3^r) :
    r < odds H w ∧ ∃ S, SignedClock r S ∧
      (2:Nat)^(odds H w-r+(S-r+1)) < 3^(odds H w-r) := by
  let e := odds H w-r
  have src : (w:Int)+1 ≤ (2:Int)^r*a-1 := by
    have pos' : 0<(2:Nat)^r*a := Nat.mul_pos (Nat.two_pow_pos _) pos
    have pn : w+1 ≤ 2^r*a-1 := by omega
    have cint := congrArg (fun x : Nat => (x:Int)) (Nat.sub_add_cancel (show 1≤(2:Nat)^r*a by omega))
    have le : (w:Int)+1 ≤ ((2^r*a-1:Nat):Int) := by exact_mod_cast pn
    push_cast at cint
    omega
  have plenty : r < odds H w := by
    by_contra! de
    obtain ⟨_,_,_,bad⟩ := through_precision pos ending de
    have one : (1:Int)≤2^(H-odds H w+1) := by
      have p : (0:Int)<2^(H-odds H w+1) := by positivity
      omega
    have grow := Int.mul_le_mul_of_nonneg_right one
      (show 0≤(2:Int)^r*a-1 by omega)
    simp only [one_mul] at grow
    omega
  obtain ⟨i,S,_,first,rest,finish⟩ := split_odds H w e (Nat.sub_le _ _)
  have finalOdds : odds S (run i w)=r := by dsimp [e] at rest; omega
  have end' : run S (run i w)+2=2*a*3^r := by rw [finish,ending]
  obtain ⟨s,hs,hq,limit⟩ := through_precision pos end' finalOdds.le
  rw [finalOdds] at hq limit
  refine ⟨plenty,S,⟨s,hs,hq⟩,?_⟩
  have gain : (2:Int)^e*((run i w:Int)+1) ≤ 3^e*((w:Int)+1) := by
    exact_mod_cast (first ▸ rise i w : 2^e*(run i w+1)≤3^e*(w+1))
  have cmp : (2:Int)^(e+(S-r+1))*((w:Int)+1) < 3^e*((w:Int)+1) := calc
    _ = 2^e*(2^(S-r+1)*((w:Int)+1)) := by rw [pow_add]; ring
    _ ≤ 2^e*(2^(S-r+1)*(2^r*(a:Int)-1)) :=
      Int.mul_le_mul_of_nonneg_left (Int.mul_le_mul_of_nonneg_left src (by positivity)) (by positivity)
    _ < 2^e*((run i w:Int)+1) := Int.mul_lt_mul_of_pos_left limit (by positivity)
    _ ≤ _ := gain
  have strict := (mul_lt_mul_iff_left₀ (show 0<(w:Int)+1 by omega)).mp cmp
  exact_mod_cast strict

/-- The matching, all-odd continuation and the chosen signed word yield
ordinary positive trajectories with the promised exact odd count. -/
theorem sharp_word {S r k a d : Nat} {s : Int} (pos : 0<a) (pd : 0<d)
    (sh : travel S s = -2) (sq : digits S s = r)
    (fit : (3:Int)^k*d = (2:Int)^(S+1)*a+s+1) :
    run (k+S+1) (2^k*d-1)=3^r*a-1 ∧ odds (k+S+1) (2^k*d-1)=k+r := by
  have append (p q x : Nat) : run (p+q) x=run q (run p x) ∧
      odds (p+q) x=odds p x+odds q (run p x) := by
    induction p generalizing x with
    | zero => simp [run,odds]
    | succ p ih =>
      obtain ⟨f,g⟩ := ih (step x)
      rw [Nat.succ_add,run,odds,run,odds,f,g]
      constructor <;> omega
  obtain ⟨row,grade⟩ := ramp k d pd
  let b := 3^k*d-1
  have pd' : 1≤(3:Nat)^k*d := Nat.mul_pos (Nat.pow_pos (by decide)) pd
  have bc : (b:Int) = s+2^S*(2*(a:Int)) := by
    dsimp [b]; rw [Nat.cast_sub pd']; push_cast
    rw [pow_succ] at fit
    linarith only [fit]
  obtain ⟨h,o⟩ := signed_lift S s (2*(a:Int))
  rw [←bc,sh,sq] at h
  rw [←bc,sq] at o
  obtain ⟨f,g⟩ := physical S b
  rw [f] at h
  rw [g] at o
  have pa : 0<(3:Nat)^r*a := Nat.mul_pos (Nat.pow_pos (by decide)) pos
  have z : run S b = 2*(3^r*a-1) := by
    have eq' : ((2*(3^r*a-1):Nat):Int) = 2*((3:Int)^r*a-1) := by
      push_cast [Nat.cast_sub (show 1≤(3:Nat)^r*a by omega)]; rfl
    apply Int.ofNat_inj.mp
    rw [h,eq']; ring
  have u := append k S (2^k*d-1)
  rw [row,grade] at u
  change run (k+S) (2^k*d-1) = run S b ∧
    odds (k+S) (2^k*d-1)=k+odds S b at u
  have v := append (k+S) 1 (2^k*d-1)
  rw [u.1,u.2,z,o] at v
  have even (n : Nat) : run 1 (2*n)=n ∧ odds 1 (2*n)=0 := by
    simp only [run,odds,step]; split <;> omega
  rw [(even _).1,(even _).2,Nat.add_zero] at v
  exact v

#print axioms ramp
#print axioms other_predecessor
#print axioms lower_witness
#print axioms sharp_word
end Collatz.AscentMerger

import UpperRepresentative

namespace Collatz.CrossingRank

open UpperRepresentative (step run)

private theorem append (i j n : Nat) : run (i+j) n = run j (run i n) := by
  induction i generalizing n with
  | zero => simp [run]
  | succ i ih => rw [Nat.succ_add, run, run, ih]

private theorem halve_power (k a : Nat) : run k (2^k*a) = a := by
  induction k with
  | zero => simp [run]
  | succ k ih =>
    rw [Nat.pow_succ, show 2^k*2*a = 2*(2^k*a) by grind, run]
    rw [show step (2*(2^k*a)) = 2^k*a by unfold step; split <;> omega]
    exact ih

/-- The two participants follow the same number of physical clocks to these endpoints.
The lower input may be used without any restriction on the length of the odd run. -/
theorem shadow {d a x u : Nat} (ha : 0<a)
    (source : x+1=2^(d+1)*a) (exit : 3^d*a=4*u+1) :
    run (d+2) x = 6*u+1 ∧ run (d+2) ((x-1)/2) = u := by
  have two : 2^(d+1)*a = 2*(2^d*a) := by rw [Nat.pow_succ]; grind
  have positive : 0 < 2^d*a := Nat.mul_pos (Nat.pow_pos (by decide)) ha
  have upper := UpperRepresentative.all_odd (d+1) a ha
  have lower := UpperRepresentative.all_odd d a ha
  have three : 3^(d+1)*a = 3*(3^d*a) := by rw [Nat.pow_succ]; grind
  rw [← source, Nat.add_sub_cancel, three, exit] at upper
  rw [show 2^d*a-1=(x-1)/2 by omega, exit] at lower
  constructor
  · rw [show d+2=(d+1)+1 by omega, append, upper]
    simp only [run]; unfold step; split <;> omega
  · rw [append d 2, lower]
    simp only [run]; unfold step; split <;> split <;> omega

def clock (t : Nat) := 56+72*t
def high (t : Nat) := 7*2^(clock t)
def ternary (t : Nat) := 7*3^(55+72*t)
def source (t : Nat) := (high t-1)/3
def returned (t : Nat) := (ternary t-1)/4

private theorem scales (t : Nat) :
    high (t+1) = high t*2^72 ∧ ternary (t+1) = ternary t*3^72 := by
  simp only [high, ternary, clock]
  rw [show 56+72*(t+1)=(56+72*t)+72 by omega,
      show 55+72*(t+1)=(55+72*t)+72 by omega, Nat.pow_add, Nat.pow_add]
  constructor <;> grind

private theorem arithmetic (t : Nat) :
    high t%54=28 ∧ ternary t%32=13 ∧ 4*high t<ternary t ∧
    4*2^(83+108*t)<ternary t := by
  induction t with
  | zero => decide
  | succ t ih =>
    obtain ⟨h,b⟩ := scales t
    rw [h, b, show 83+108*(t+1)=(83+108*t)+108 by omega, Nat.pow_add]
    rw [Nat.mul_mod (high t) (2^72) 54, Nat.mul_mod (ternary t) (3^72) 32,
      ih.1, ih.2.1]
    exact ⟨by decide, by decide, by omega, by omega⟩

/-- The initial triple crosses, then its second run joins the returned triple.
The initial good arm reaches 1 in the displayed number of actual clocks. -/
theorem crossing (t : Nat) :
    let m := clock t
    let q := source t
    let u := returned t
    (3*q)%27=0 ∧ q%2=1 ∧ u%8=3 ∧ 2*(3*q)<6*u+1 ∧
    run (m+11) q=1 ∧ run (m+1) (3*q)=6*u+1 ∧
    run (m+1) ((3*q-1)/2)=u ∧ run (m+5) (3*q)=run 3 (3*u) := by
  dsimp only
  obtain ⟨h,b,large,_⟩ := arithmetic t
  have hq : high t=3*source t+1 ∧ source t%2=1 ∧ (3*source t)%27=0 := by
    unfold source; omega
  have hu : ternary t=4*returned t+1 ∧ returned t%8=3 := by unfold returned; omega
  let d := 55+72*t
  have md : clock t=d+1 := by unfold clock d; omega
  have hpow : high t=2*(2^d*7) := by unfold high; rw [md, Nat.pow_succ]; grind
  have atSeven : run (clock t) (source t)=7 := by
    rw [md, run]
    rw [show step (source t)=2^d*7 by unfold step; split <;> omega]
    exact halve_power d 7
  have paths := shadow (d:=d) (a:=7) (x:=3*source t) (u:=returned t) (by decide)
    (by rw [← md, ← hq.1]; unfold high; grind)
    (by rw [← hu.1]; unfold ternary d; grind)
  have stepCount : clock t+1=d+2 := by omega
  rw [← stepCount] at paths
  refine ⟨hq.2.2, hq.2.1, hu.2, by omega, ?_, paths.1, paths.2, ?_⟩
  · rw [append, atSeven]; decide
  · rw [show clock t+5=(clock t+1)+4 by omega, append, paths.1]
    let k := returned t/8
    have uk : returned t=8*k+3 := by unfold k; omega
    rw [uk]; simp only [run]; unfold step
    split <;> split <;> split <;> split <;> split <;> split <;> split <;> omega

private theorem lower_bound (k z : Nat) : z ≤ 2^k * run k z := by
  induction k generalizing z with
  | zero => simp [run]
  | succ k ih =>
    have first : z ≤ 2*step z := by unfold step; split <;> omega
    have rest := Nat.mul_le_mul_left 2 (ih (step z))
    rw [run, Nat.pow_succ, show 2^k*2*run k (step z)=2*(2^k*run k (step z)) by grind]
    omega

/-- Every hitting clock of the physically returned source incurs this growing cost. -/
theorem returned_clock (t h : Nat) (hit : run h (returned t)=1) : 83+108*t ≤ h := by
  have p := (arithmetic t).2.2.2
  have low : 2^(83+108*t) ≤ returned t := by unfold returned; omega
  have upper := lower_bound h (returned t)
  rw [hit, Nat.mul_one] at upper
  by_cases small : h < 83+108*t
  · have less := Nat.pow_lt_pow_right (by decide : 1<2) small
    omega
  · omega

#print axioms shadow
#print axioms crossing
#print axioms returned_clock
end Collatz.CrossingRank

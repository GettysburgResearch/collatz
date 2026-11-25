import SignedCycleDilation

/-! Whole exponent progressions on the rank-three family 81z+271=128*2^j.
All affine walks and modular exponent certificates are checked in the kernel. -/
namespace MersenneTwoCenter
open CollatzReverseBasin CollatzTwoOdd SignedCycleDilation

structure Row where
  first : Nat
  period : Nat
  den : Nat
  numerator : Nat
  clock : Nat
  residue : Nat

def row (i : Fin 13) : Row :=
  match i.val with
  | 0 => ⟨5903, 6561, 531441, 2692031, 18, 19145024⟩
  | 1 => ⟨1286, 6561, 531441, 4970719, 19, 11586752⟩
  | 2 => ⟨2258, 19683, 1594323, 7686973, 19, 58825952⟩
  | 3 => ⟨11889, 19683, 1594323, 8962877, 20, 22745312⟩
  | 4 => ⟨44, 19683, 1594323, 10144829, 20, 30587408⟩
  | 5 => ⟨1124, 19683, 1594323, 10984637, 20, 46228832⟩
  | 6 => ⟨1529, 19683, 1594323, 11299565, 20, 61660304⟩
  | 7 => ⟨5174, 19683, 1594323, 14133917, 20, 47488544⟩
  | 8 => ⟨13347, 19683, 1594323, 16685725, 21, 17076608⟩
  | 9 => ⟨1502, 19683, 1594323, 19049629, 21, 24918704⟩
  | 10 => ⟨12221, 19683, 1594323, 20414317, 21, 71108144⟩
  | 11 => ⟨2582, 19683, 1594323, 20729245, 21, 40560128⟩
  | _ => ⟨2987, 19683, 1594323, 21359101, 21, 55991600⟩

private def block (s : Row) := 48*s.den
private def wa (s : Row) := 48*2^(s.clock+2)
private def wb (s : Row) := (2^(s.clock+2)*s.residue-s.numerator)/s.den
private def za (s : Row) := 512*block s/81
private def zb (s : Row) := (512*s.residue-271)/81

private def powerMod : Nat → Nat → Nat → Nat → Nat
  | 0, _, _, m => 1%m
  | h+1, b, e, m =>
    let x := powerMod h b (e/2) m
    let t := (x*x)%m
    if e%2=0 then t else (t*b)%m

private theorem powerMod_sound (h b e m : Nat) (he : e<2^h) :
    powerMod h b e m=b^e%m := by
  induction h generalizing e with
  | zero =>
    have ex : e=0 := by simpa using he
    subst e; rfl
  | succ h ih =>
    have half : e/2<2^h := by rw [pow_succ] at he; omega
    have sq : (powerMod h b (e/2) m * powerMod h b (e/2) m)%m=b^(e/2+e/2)%m := by
      rw [ih _ half,pow_add,Nat.mul_mod_mod,Nat.mod_mul_mod]
    simp only [powerMod,sq]
    split
    · exact congrArg (fun n : Nat => b^n%m) (by omega)
    · rw [Nat.mod_mul_mod,←pow_succ]
      exact congrArg (fun n : Nat => b^n%m) (by omega)

private def rules (s : Row) : Prop :=
  9+162*s.first<2^24 ∧ 162*s.period<2^24 ∧
  powerMod 24 2 (9+162*s.first) (block s)=s.residue ∧
  (powerMod 24 2 (162*s.period) (block s)*s.residue)%(block s)=s.residue ∧
  81*za s=512*block s ∧ 81*zb s+271=512*s.residue ∧
  wa s%48=0 ∧ wb s%48=17 ∧ wa s≤za s ∧ wb s<zb s ∧
  2^7*(za s/2^7)=za s ∧ 2^s.clock*(wa s/2^s.clock)=wa s ∧
  2^(s.clock+2)*(3*wa s/2^(s.clock+2))=3*wa s ∧
  3^(count 7 (zb s:Int))*(za s/2^7)=4*block s ∧
  value 7 (zb s)+1=4*s.residue ∧
  3^(count s.clock (wb s:Int))*(wa s/2^s.clock)=4*block s ∧
  value s.clock (wb s)+1=4*s.residue ∧
  3^(count (s.clock+2) ((3*wb s:Nat):Int))*(3*wa s/2^(s.clock+2))=block s ∧
  value (s.clock+2) (3*wb s)=s.residue

set_option maxRecDepth 4096 in
set_option maxHeartbeats 2000000 in
private theorem checked : ∀ i : Fin 13, rules (row i) := by
  unfold rules; decide

private theorem pow_basin (k : Nat) : Basin (2^k) := by
  induction k with
  | zero => exact ⟨0,rfl⟩
  | succ k ih =>
    refine (basin_value 1 _).mp ?_
    rw [show value 1 (2^(k+1))=2^k by simp [value,shortcut,pow_succ]]
    exact ih

/-- The supplied ordinary source, on each full exponent progression, has
a strictly smaller residue-17 query with the same lower status and a
triple that actually hits a power of two. -/
theorem progress (i : Fin 13) (t z : Nat)
    (hz : 81*z+271=512*2^(9+162*((row i).first+(row i).period*t))) :
    ∃ w, w%48=17 ∧ w<z ∧ (Basin w ↔ Basin z) ∧ Basin (3*w) := by
  let s:=row i
  have ok : rules s := checked i
  obtain ⟨bh,sh,base,period,sa,sb,wr,ws,le,lt,cz,cw,cu,
      dz,ez,dw,ew,du,eu⟩ := ok
  change 9+162*s.first<2^24 at bh
  change 162*s.period<2^24 at sh
  change powerMod 24 2 (9+162*s.first) (block s)=s.residue at base
  change (powerMod 24 2 (162*s.period) (block s)*s.residue)%(block s)=s.residue at period
  rw [powerMod_sound _ _ _ _ bh] at base
  rw [powerMod_sound _ _ _ _ sh] at period
  have remainder (u : Nat) : 2^(9+162*(s.first+s.period*u))%(block s)=s.residue := by
    induction u with
    | zero => simpa using base
    | succ u ih =>
      rw [show 9+162*(s.first+s.period*(u+1))=162*s.period+(9+162*(s.first+s.period*u)) by ring,
        pow_add,Nat.mul_mod,ih,period]
  let N:=2^(9+162*(s.first+s.period*t))
  let q:=N/(block s)
  have hn : N=block s*q+s.residue := by
    change N=block s*(N/(block s))+s.residue
    rw [←remainder t]
    exact (Nat.div_add_mod _ _).symm
  change 81*z+271=512*N at hz
  have zrow : z=za s*q+zb s := by
    have eq : 81*(za s*q+zb s)+271=512*N := by
      rw [hn,show 81*(za s*q+zb s)+271=81*za s*q+(81*zb s+271) by ring,sa,sb]
      ring
    omega
  let w:=wa s*q+wb s
  have lowerw := lift_value s.clock (wa s) (wb s) q cw
  have lowerz := lift_value 7 (za s) (zb s) q cz
  rw [dw] at lowerw
  rw [dz] at lowerz
  change value s.clock w=_ at lowerw
  rw [←zrow] at lowerz
  have eq : value s.clock w=value 7 z := by
    rw [lowerw,lowerz,Nat.add_right_cancel (ew.trans ez.symm)]
  have upper := lift_value (s.clock+2) (3*wa s) (3*wb s) q cu
  rw [du,eu,←hn,show 3*wa s*q+3*wb s=3*w by dsimp [w]; ring] at upper
  have lo : Basin w ↔ Basin z := by
    rw [←basin_value s.clock w,←basin_value 7 z,eq]
  have up : Basin (3*w) := by
    rw [←basin_value (s.clock+2) (3*w),upper]; exact pow_basin _
  refine ⟨w, ?_, ?_, lo, up⟩
  · dsimp [w]; simp [Nat.add_mod,Nat.mul_mod,wr,ws]
  · have m := Nat.mul_le_mul_right q le
    change wa s*q+wb s<z; rw [zrow]; exact Nat.add_lt_add_of_le_of_lt m lt

theorem least_excluded (i : Fin 13) (t z : Nat)
    (hz : 81*z+271=512*2^(9+162*((row i).first+(row i).period*t)))
    (hd : ReverseDefect z) (least : ∀ v, ReverseDefect v → z≤v) : False := by
  obtain ⟨w,wr,wl,lo,up⟩ := progress i t z hz
  exact (Nat.not_le_of_gt wl) (least w ⟨wr,up,fun h => hd.2.2 (lo.mp h)⟩)

#print axioms progress
#print axioms least_excluded
end MersenneTwoCenter

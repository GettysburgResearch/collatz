import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

namespace OddUnitLift

set_option maxRecDepth 8192

def T (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2

def orbit : Nat → Nat → Nat
  | 0, x => x
  | h+1, x => orbit h (T x)

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, x => odds h (T x) + x%2

/-- Lifting one fixed finite parity prefix with its actual odd count. -/
theorem highBit (h x t : Nat) : orbit h (x+2^h*t) = orbit h x+3^(odds h x)*t := by
  induction h generalizing x t with
  | zero => simp [orbit,odds]
  | succ h ih =>
    have eq : 2^(h+1)*t = 2*(2^h*t) := by ring
    by_cases even : x%2=0
    · have st : T (x+2^(h+1)*t) = T x+2^h*t := by rw [eq]; unfold T; split <;> omega
      simp only [orbit,odds]; rw [st,ih,even,Nat.add_zero]
    · have odd : x%2=1 := by omega
      have st : T (x+2^(h+1)*t) = T x+2^h*(3*t) := by
        rw [eq,show 2^h*(3*t) = 3*(2^h*t) by ring]; unfold T; split <;> omega
      simp only [orbit,odds]; rw [st,ih,odd,pow_succ]; ring

private structure Prefix where
  h : Nat
  b : Nat
  p : Nat
  g : Nat
  y : Nat

private def bank : List Prefix := [
  ⟨10,261,3,2,7⟩, ⟨16,35569,4,3,44⟩, ⟨11,797,5,1,95⟩,
  ⟨23,7962413,6,3,692⟩, ⟨17,122181,7,1,2039⟩, ⟨20,1013037,7,2,2113⟩]

private def shift (w : Prefix) := 52488/(2^w.g*3^w.p*3)
private def valid (w : Prefix) : Prop :=
  0<w.b ∧ w.b%2=1 ∧ 0<w.p ∧ 1≤w.g ∧ w.g≤3 ∧ w.h≤23 ∧
  odds w.h w.b=w.p ∧ orbit w.h w.b=w.y ∧
  1+odds w.h (3*w.b)=w.p+w.g ∧ orbit w.h (3*w.b)+1=3^w.g*w.y ∧
  2^w.g*3^w.p*(3*shift w)=52488
private instance (w : Prefix) : Decidable (valid w) := by unfold valid; infer_instance

private def trial (w : Prefix) (z : Nat) := (z/2^w.g-w.y)/3^w.p
private def accepts (w : Prefix) (z : Nat) : Prop :=
  z=2^w.g*(w.y+3^w.p*trial w z) ∧ (w.b+2^w.h*trial w z)%3 ≠ 0
private instance (w : Prefix) (z : Nat) : Decidable (accepts w z) := by unfold accepts; infer_instance

private theorem sixPrefixes : bank.all (fun w => decide (valid w)) = true := by decide +kernel
private theorem allCells : (List.range 243).all (fun i => bank.any
    (fun w => decide (accepts w (136+216*i)))) = true := by decide +kernel

private theorem cover (z : Nat) (h8 : z%8=0) (h27 : z%27=1) :
    ∃ w ∈ bank, ∃ t, z=2^w.g*(w.y+3^w.p*t) ∧ (w.b+2^w.h*t)%3 ≠ 0 := by
  have tab : ∀ r : Fin 216, r.val%8=0 → r.val%27=1 → r.val=136 := by decide
  have hmod := tab ⟨z%216,Nat.mod_lt _ (by decide)⟩
    (by simpa only [Nat.mod_mod_of_dvd z (by decide : 8∣216)] using h8)
    (by simpa only [Nat.mod_mod_of_dvd z (by decide : 27∣216)] using h27)
  let i := (z/216)%243
  let j := (z/216)/243
  have idx : i<243 := Nat.mod_lt _ (by decide)
  have hz : z=(136+216*i)+52488*j := by dsimp [i,j]; change z%216=136 at hmod; omega
  have ha := List.all_eq_true.mp allCells i (List.mem_range.mpr idx)
  obtain ⟨w,hw,hi⟩ := List.any_eq_true.mp ha
  have ok : accepts w (136+216*i) := of_decide_eq_true hi
  have info : valid w := of_decide_eq_true (List.all_eq_true.mp sixPrefixes w hw)
  obtain ⟨_,_,_,_,_,_,_,_,_,_,stride⟩ := info
  let t := trial w (136+216*i)
  refine ⟨w,hw,t+3*shift w*j,?_,?_⟩
  · calc z = (136+216*i)+52488*j := hz
         _ = (2^w.g*(w.y+3^w.p*t))+(2^w.g*3^w.p*(3*shift w))*j := by rw [ok.1,stride]
         _ = _ := by ring
  · rw [show w.b+2^w.h*(t+3*shift w*j) = (w.b+2^w.h*t)+3*(2^w.h*shift w*j) by ring]
    have := ok.2; change (w.b+2^w.h*t)%3 ≠ 0 at this; omega

/-- Both ordered ordinary endpoints of a supplied positive integer Q = 1 (mod 27), 8 | Q. -/
theorem pairedLift (z : Nat) (h8 : z%8=0) (h27 : z%27=1) :
    ∃ u h g Y : Nat, 0<u ∧ u%2=1 ∧ u%3≠0 ∧ 1≤g ∧ g≤3 ∧ h≤23 ∧ g≤h ∧
      z=2^g*Y ∧ orbit h u=Y ∧ orbit h (3*u)+1=3^g*Y := by
  obtain ⟨w,hw,t,hz,unit⟩ := cover z h8 h27
  have info : valid w := of_decide_eq_true (List.all_eq_true.mp sixPrefixes w hw)
  obtain ⟨pos,baseOdd,_,gpos,gmax,hmax,hp,hy,hq,hey,_⟩ := info
  have gh : w.g≤w.h := by
    have cert : bank.all (fun b => decide (b.g≤b.h))=true := by decide
    exact of_decide_eq_true (List.all_eq_true.mp cert w hw)
  obtain ⟨j,hj⟩ : ∃ j, w.h=j+1 := ⟨w.h-1, by omega⟩
  have baseStep : 2^w.h*t=2*(2^j*t) := by rw [hj]; ring
  have oddU : (w.b+2^w.h*t)%2=1 := by rw [baseStep]; omega
  refine ⟨w.b+2^w.h*t,w.h,w.g,w.y+3^w.p*t,by omega,oddU,unit,gpos,gmax,hmax,gh,hz,?_,?_⟩
  · rw [highBit,hy,hp]
  · rw [show 3*(w.b+2^w.h*t) = 3*w.b+2^w.h*(3*t) by ring, highBit]
    have eq : 3^(odds w.h (3*w.b))*3 = 3^w.g*3^w.p := by
      calc 3^(odds w.h (3*w.b))*3 = 3^(1+odds w.h (3*w.b)) := by rw [add_comm,pow_succ]
           _ = _ := by rw [hq,pow_add,Nat.mul_comm]
    calc orbit w.h (3*w.b)+3^(odds w.h (3*w.b))*(3*t)+1 =
          (orbit w.h (3*w.b)+1)+(3^(odds w.h (3*w.b))*3)*t := by ring
         _ = _ := by rw [hey,eq]; ring

private theorem halvingRun (m a : Nat) : orbit m (2^m*a) = a := by
  induction m with
  | zero => simp [orbit]
  | succ k ih =>
    have he : T (2*(2^k*a)) = 2^k*a := by unfold T; split <;> omega
    rw [show 2^(k+1)*a=2*(2^k*a) by ring]
    change orbit k (T (2*(2^k*a))) = a
    rw [he,ih]

private theorem oddRun (m n a : Nat) (hn : n+1=2^m*a) : orbit m n+1=3^m*a := by
  induction m generalizing n a with
  | zero => simpa [orbit] using hn
  | succ k ih =>
    have h : n+1=2*(2^k*a) := by rw [hn]; ring
    have hs : T n+1=3*(2^k*a) := by unfold T; split <;> omega
    change orbit k (T n)+1=3^(k+1)*a
    rw [ih (T n) (3*a) (by rw [hs]; ring)]; ring

private theorem addOrbit (i j x : Nat) : orbit (i+j) x=orbit j (orbit i x) := by
  induction i generalizing x with
  | zero => simp [orbit]
  | succ i ih => rw [Nat.succ_add]; exact ih (T x)

def Meets (x y : Nat) : Prop := ∃ i j, orbit i x=orbit j y

private theorem merged {x y z : Nat} (a : Meets x y) (b : Meets y z) : Meets x z := by
  obtain ⟨i,j,h⟩ := a; obtain ⟨k,l,h'⟩ := b
  refine ⟨i+k,l+j,?_⟩
  rw [addOrbit,h,← addOrbit,Nat.add_comm j k,addOrbit,h',← addOrbit]

private theorem flip {x y : Nat} (h : Meets x y) : Meets y x := by
  obtain ⟨i,j,a⟩ := h; exact ⟨j,i,a.symm⟩

private theorem neighbor (x : Nat) (hx : x%4=3) : Meets (x-1) (3*x-1) := by
  refine ⟨2,2,?_⟩; simp only [orbit,T]; split <;> split <;> split <;> split <;> omega

/-- The source and target in the original odd directed comparison both keep their own component. -/
theorem orderedOddRay (m a v : Nat) (hm : 0<m) (ha : a%2=1) (hv : v%9=2)
    (hs : 3*v+1=2^m*a) : ∃ u, 0<u ∧ u%2=1 ∧ u%3≠0 ∧ Meets v u ∧ Meets (9*v+2) (3*u) := by
  obtain ⟨k,rfl⟩ : ∃ k,m=k+1 := ⟨m-1,by omega⟩
  have e : 3*v+1=2*(2^k*a) := by rw [hs]; ring
  have once : T v=2^k*a := by unfold T; split <;> omega
  have left : Meets v a := ⟨k+1,0,by change orbit k (T v)=a; rw [once,halvingRun]⟩
  let y := 3^(k+2)*a
  have edge : Meets (9*v+2) (y-1) := by
    have h := oddRun (k+1) (9*v+2) (3*a) (by rw [show 9*v+2+1=3*(3*v+1) by ring,hs]; ring)
    have eq : 3^(k+1)*(3*a)=y := by dsimp [y]; ring
    exact ⟨k+1,0,by change orbit (k+1) (9*v+2)=y-1; omega⟩
  by_cases up : y%4=3
  · let z := 2^(k+3)*a
    have h8 : z%8=0 := by rw [show z=8*(2^k*a) by dsimp [z]; ring]; omega
    have h27 : z%27=1 := by rw [show z=4*(3*v+1) by rw [hs]; dsimp [z]; ring]; omega
    obtain ⟨u,h,g,Y,pu,ou,hu,_,gmax,_,_,hZ,low,high⟩ := pairedLift z h8 h27
    let d := k+3-g
    have dg : g+d=k+3 := by dsimp [d]; omega
    have hY : Y=2^d*a := by
      have calcY : 2^g*Y=2^g*(2^d*a) := by rw [← hZ,← Nat.mul_assoc,← pow_add,dg]
      exact Nat.eq_of_mul_eq_mul_left (by positivity) calcY
    have reachU : Meets u a := ⟨h+d,0,by rw [addOrbit,low,hY,halvingRun]; rfl⟩
    have grow : orbit h (3*u)+1=2^d*(3^g*a) := by rw [high,hY]; ring
    have tail := oddRun d (orbit h (3*u)) (3^g*a) grow
    have endEq : 3^d*(3^g*a)=3*y := by
      rw [← Nat.mul_assoc,← pow_add,Nat.add_comm d g,dg]; dsimp [y]; ring
    have right : Meets (3*u) (3*y-1) := ⟨h+d,0,by rw [addOrbit]; change orbit d (orbit h (3*u))=3*y-1; omega⟩
    exact ⟨u,pu,ou,hu,merged left (flip reachU),merged (merged edge (neighbor y up)) (flip right)⟩
  · let prev := 3^(k+1)*a
    have ey : y=3*prev := by dsimp [y,prev]; ring
    have po : prev%2=1 := by dsimp [prev]; rw [Nat.mul_mod,ha,Nat.pow_mod]; simp
    have pp : prev%4=3 := by omega
    have h := oddRun (k+1) (3*v) a hs
    have lower : Meets (3*v) (prev-1) := ⟨k+1,0,by change orbit (k+1) (3*v)=prev-1; dsimp [prev]; omega⟩
    have adj := neighbor prev pp; rw [← ey] at adj
    exact ⟨v,by omega,by omega,by omega,⟨0,0,rfl⟩,merged edge (flip (merged lower adj))⟩

set_option format.width 220
#print axioms highBit
#print axioms sixPrefixes
#print axioms allCells
#print axioms pairedLift
#print axioms orderedOddRay

end OddUnitLift

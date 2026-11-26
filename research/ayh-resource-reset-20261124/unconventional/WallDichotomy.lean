import WallTernary
import WallExamples

namespace WallDichotomy
open WallRational WallGeneral WallRefinement

/-- A possibly zero-grade cycle, specified by one concrete repeated state. -/
def Repeats (d a : Int) : Prop :=
  ∃ e h : Nat, 0<h ∧ runD d h (runD d e a)=runD d e a

private theorem zero_grade (d x : Int) (h : Nat) (eq : grade d h x=0) :
    2^h*runD d h x=x := by
  induction h generalizing x with
  | zero => simp [runD]
  | succ h ih =>
    rw [grade] at eq
    by_cases even : x%2=0
    · simp only [even,ite_true,Nat.add_zero] at eq
      have cy := ih (step d x) eq
      rw [runD,pow_succ,show (2^h*2)*runD d h (step d x)=2*(2^h*runD d h (step d x)) by ring,cy]
      simp [step,even];omega
    · simp [even] at eq

private theorem cycle_or_zero (d a : Int) (rep : Repeats d a) :
    Nonempty (PositiveCycle d a) ∨ ∃e, runD d e a=0 := by
  obtain ⟨e,h,hp,back⟩ := rep
  let b := runD d e a
  by_cases zero : grade d h b=0
  · right
    have row := zero_grade d b h zero
    change runD d h b=b at back
    rw [back] at row
    have pow : 1<(2:Int)^h := by
      obtain ⟨t,rfl⟩ : ∃t,h=t+1 := ⟨h-1,by omega⟩
      have z : 0<(2:Int)^t := by positivity
      rw [pow_succ];omega
    refine ⟨e,?_⟩
    change b=0
    have prod : ((2:Int)^h-1)*b=0 := by rw [sub_mul,row];ring
    rcases mul_eq_zero.mp prod with z|z <;> omega
  · exact Or.inl ⟨⟨e,h,back,by change 0<grade d h b;omega⟩⟩

private theorem numerator_affine (d x : Int) (h : Nat) (odd : d%2=1) :
    ∃ z : Int, 2^h*runD d h x=3^(grade d h x)*x+d*z := by
  induction h generalizing x with
  | zero => exact ⟨0,by simp [runD,grade]⟩
  | succ h ih =>
    obtain ⟨z,e⟩ := ih (step d x)
    let g := grade d h (step d x)
    by_cases even : x%2=0
    · refine ⟨2*z,?_⟩
      have phase : 2*step d x=x := by simp [step,even];omega
      rw [runD,pow_succ,grade]
      simp only [even,ite_true,Nat.add_zero]
      calc
        _ = 2*(2^h*runD d h (step d x)) := by ring
        _ = 3^g*(2*step d x)+d*(2*z) := by rw [e];dsimp [g];ring
        _ = _ := by rw [phase]
    · refine ⟨3^g+2*z,?_⟩
      have phase : 2*step d x=3*x+d := by simp [step,even];omega
      rw [runD,pow_succ,grade]
      simp only [even,ite_false,pow_succ]
      calc
        _ = 2*(2^h*runD d h (step d x)) := by ring
        _ = 3^g*(2*step d x)+d*(2*z) := by rw [e];dsimp [g];ring
        _ = _ := by rw [phase];dsimp [g];ring

private theorem split_three (w : Nat) (pos : 0<w) : ∃ v t, t%3≠0 ∧ w=3^v*t := by
  induction w using Nat.strong_induction_on with
  | h w ih =>
    by_cases p : w%3≠0
    · exact ⟨0,w,p,by simp⟩
    · obtain ⟨v,t,o,e⟩ := ih (w/3) (by omega) (by omega)
      refine ⟨v+1,t,o,?_⟩
      calc w=3*(w/3) := by omega
           _=_ := by rw [e,pow_succ];ring

private theorem reduced (p d g : Nat) (pos : 0<p) (small : p<d)
    (div : d ∣ 3^g*p) : ∃ a u, u%3≠0 ∧ u<3^a ∧ p*3^a=d*u := by
  obtain ⟨w,eq⟩ := div
  have wp : 0<w := by
    by_contra! z
    have ge : 0<3^g*p := by positivity
    rw [eq,show w=0 by omega,Nat.mul_zero] at ge
    omega
  obtain ⟨v,t,unit,ew⟩ := split_three w wp
  have tp : 0<t := by omega
  have le : v≤g := by
    by_contra! no
    have pw : 3^g≤3^v := Nat.pow_le_pow_right (by decide) (by omega)
    have wt : 3^v≤w := by rw [ew];simpa using Nat.mul_le_mul_left (3^v) tp
    have lo := Nat.mul_le_mul_left d (le_trans pw wt)
    have big := Nat.mul_lt_mul_of_pos_left small (by positivity : 0<3^g)
    rw [←eq,Nat.mul_comm d] at lo
    omega
  let a := g-v
  have pg : 3^g=3^v*3^a := by rw [←pow_add];congr 1;dsimp [a];omega
  have e : p*3^a=d*t := by
    apply Nat.eq_of_mul_eq_mul_left (by positivity : 0<3^v)
    calc
      _ = 3^g*p := by rw [pg];ring
      _ = d*w := eq
      _ = _ := by rw [ew];ring
  have less : t<3^a := by
    have hh := Nat.mul_lt_mul_of_pos_right small (by positivity : 0<3^a)
    rw [e] at hh
    exact Nat.lt_of_mul_lt_mul_left hh
  exact ⟨a,t,unit,less,e⟩

private theorem zero_forces_three (p d : Nat) (odd : (d:Int)%2=1)
    (left : Bool) (e : Nat)
    (zero : runD d e (if left then -(p:Int) else (d:Int)-p)=0) :
    ∃ g, d ∣ 3^g*p := by
  let x : Int := if left then -(p:Int) else (d:Int)-p
  obtain ⟨w,eq⟩ := numerator_affine d x e odd
  rw [show runD d e x=0 from zero,mul_zero] at eq
  let g := grade d e x
  change 0=3^g*x+d*w at eq
  refine ⟨g,?_⟩
  have integer : (d:Int) ∣ (3:Int)^g*(p:Int) := by
    cases left with
    | true => refine ⟨w,?_⟩;dsimp [x] at eq;grind
    | false => refine ⟨3^g+w,?_⟩;dsimp [x] at eq;grind
  exact_mod_cast integer

/-- For a nonconstant word whose rational shadows both repeat, the only
possible fractions for a persistent ordinary wall are one third and two
thirds. A rational nonzero shadow is a point in the signed 3x+d system. -/
theorem ternary_or_breaks (C : Coloring) {n : Nat} (cut : Mixed C n)
    (L p d : Nat) (pos : 0<L) (pp : 0<p) (small : p<d) (den : d+1=2^L)
    (left : Repeats d (-(p:Int))) (right : Repeats d ((d:Int)-p)) :
    3*p=d ∨ 3*p=2*d ∨ ∃ k, index C n (L*k)≠address L p n k := by
  have odd : (d:Int)%2=1 := by
    obtain ⟨b,eq⟩ : ∃ b,L=b+1 := ⟨L-1,by omega⟩
    rw [eq,pow_succ] at den;omega
  have kill (div : ∃ g, d ∣ 3^g*p) :
      3*p=d ∨ 3*p=2*d ∨ ∃ k, index C n (L*k)≠address L p n k := by
    obtain ⟨g,dv⟩ := div
    obtain ⟨a,u,unit,bound,frac⟩ := reduced p d g pp small dv
    by_cases big : 2≤a
    · exact Or.inr (Or.inr (WallTernary.rejects_ternary_word C cut L p d a u pos den (by omega)
        bound big unit frac))
    · have cases : a=0 ∨ a=1 := by omega
      rcases cases with rfl|rfl
      · simp only [pow_zero] at bound;omega
      · have vals : u=1 ∨ u=2 := by norm_num at bound;omega
        rcases vals with rfl|rfl <;> norm_num at frac <;> omega
  rcases cycle_or_zero _ _ left with hasL|⟨e,z⟩
  · obtain ⟨cL⟩ := hasL
    rcases cycle_or_zero _ _ right with hasR|⟨e,z⟩
    · obtain ⟨cR⟩ := hasR
      exact Or.inr (Or.inr (breaks C cut L p d pos pp den cL cR))
    · exact kill (zero_forces_three p d odd false e z)
  · exact kill (zero_forces_three p d odd true e z)

/-- If both signed numerator phases repeat, every nonconstant period other
than alternating has a word-specific, all-alignment power cap on each ordinary
wall. The cap is uniform in the root and the coloring, and the onset may vary. -/
theorem alternating_or_eventual_cap (L p d : Nat) (pos : 0<L) (pp : 0<p)
    (small : p<d) (den : d+1=2^L)
    (left : Repeats d (-(p:Int))) (right : Repeats d ((d:Int)-p)) :
    3*p=d ∨ 3*p=2*d ∨
      ∃ B, 0<B ∧ ∀ (C : Coloring) (n : Nat), Mixed C n →
        ∃ J, ∀ j≥J, ¬ WallWords.Copies C n j L p B := by
  have odd : (d:Int)%2=1 := by
    obtain ⟨b,eq⟩ : ∃ b,L=b+1 := ⟨L-1,by omega⟩
    rw [eq,pow_succ] at den;omega
  let Cap := ∃ B, 0<B ∧ ∀ (C : Coloring) (n : Nat), Mixed C n →
        ∃ J, ∀ j≥J, ¬ WallWords.Copies C n j L p B
  have kill (div : ∃g, d ∣ 3^g*p) : 3*p=d ∨ 3*p=2*d ∨ Cap := by
    obtain ⟨g,dv⟩ := div
    obtain ⟨a,u,unit,bound,frac⟩ := reduced p d g pp small dv
    by_cases big : 2≤a
    · obtain ⟨B,bp,ban⟩ := WallTernary.ternary_bound L p d a u pos den (by omega)
        bound big unit frac
      refine Or.inr (Or.inr ⟨B,bp,?_⟩)
      intro C n cut
      refine ⟨0,?_⟩
      intro j _ copies
      have e := WallWords.read_blocks C copies
      rw [WallPeriodic.index_add] at e
      exact ban C _ (index_mixed C cut j) e
    · have cases : a=0 ∨ a=1 := by omega
      rcases cases with rfl|rfl
      · simp only [pow_zero] at bound;omega
      · have vals : u=1 ∨ u=2 := by norm_num at bound;omega
        rcases vals with rfl|rfl <;> norm_num at frac <;> omega
  rcases cycle_or_zero _ _ left with hasL|⟨e,z⟩
  · obtain ⟨cL⟩ := hasL
    rcases cycle_or_zero _ _ right with hasR|⟨e,z⟩
    · obtain ⟨cR⟩ := hasR
      exact Or.inr (Or.inr (WallWords.eventual_cap L p d pos pp (by omega) den cL cR))
    · exact kill (zero_forces_three p d odd false e z)
  · exact kill (zero_forces_three p d odd true e z)

end WallDichotomy

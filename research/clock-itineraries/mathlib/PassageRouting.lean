module

public import PassageFusion
import all PassageFusion
import all FiberRouting
import all FiberTransport
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageRouting

open PassageFusion
set_option autoImplicit false

/-- Every earlier state is strictly above the terminal state. -/
def FirstLow (h x b : ℕ) := run h x=b ∧ ∀ j<h, b<run j x

private theorem dyadic_partial (i j b : ℕ) (ij : i≤j) :
    run i (2^j*b)=2^(j-i)*b := by
  conv => lhs; rw [show j=i+(j-i) by omega,pow_add,Nat.mul_assoc]
  exact halve ..

private theorem first_dyadic (j b : ℕ) (bp : 0<b) : FirstLow j (2^j*b) b := by
  refine ⟨halve ..,?_⟩
  intro i ij
  rw [dyadic_partial i j b (by omega)]
  have gt : 1<2^(j-i) := one_lt_pow₀ (by decide) (by omega)
  simpa using Nat.mul_lt_mul_of_pos_right gt bp

private theorem first_cons {h x b : ℕ} (high : b<x) (tail : FirstLow h (step x) b) :
    FirstLow (h+1) x b := by
  refine ⟨tail.1,?_⟩
  intro j hj
  cases j with
  | zero => exact high
  | succ k => exact tail.2 k (by omega)

private theorem first_append {h f x y b : ℕ} (hit : run h x=y)
    (early : ∀ j<h, b<run j x) (tail : FirstLow f y b) : FirstLow (h+f) x b := by
  refine ⟨by rw [run_add,hit,tail.1],?_⟩
  intro j hj
  by_cases before : j<h
  · exact early j before
  · rw [show j=h+(j-h) by omega,run_add,hit]
    exact tail.2 _ (by omega)

private theorem odd_then_halves {f w b : ℕ} (fp : 0<f) (wb : b<w) (bp : 0<b)
    (eq : 2^f*b=3*w+1) : FirstLow f w b := by
  obtain ⟨j,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : f≠0)
  rw [pow_succ,Nat.mul_right_comm] at eq
  have odd : w%2≠0 := by omega
  have sw : step w=2^j*b := by simp only [step,odd,if_false]; omega
  exact first_cons wb (sw ▸ first_dyadic j b bp)

/-- At every sufficiently large common clock, one odd branch routes a
prescribed ternary ray to any positive ternary unit. Its binary correction
has bounded exponent independent of the target and the clock. -/
theorem ray_first (a q : ℕ) : ∃ N, ∀ h≥N, ∀ b, b%3≠0 →
    ∃ t i, b<t ∧ i≤2*3^q ∧
      2^h*b=2^i+3*(a+3^q*t) ∧ FirstLow h (a+3^q*t) b := by
  let P := 2*3^q
  let M := 3*3^q
  let K := 2^P+3*a+M
  refine ⟨K+P+4,?_⟩
  intro h late b ub
  have bp : 0<b := by omega
  have scale : K<2^h := by have := Nat.lt_two_pow_self (n:=h); omega
  have high : 2^P+3*a+M*b<2^h*b := by
    calc
      _ ≤ (2^P+3*a)*b+M*b := Nat.add_le_add_right
        (Nat.le_mul_of_pos_right _ bp) _
      _ = K*b := by dsimp [K]; ring
      _ < _ := Nat.mul_lt_mul_of_pos_right scale bp
  let D := 2^h*b-3*a
  have expand : 2^h*b=D+3*a := (Nat.sub_add_cancel
    (((Nat.le_add_left (3*a) (2^P)).trans (Nat.le_add_right _ (M*b))).trans high.le)).symm
  have du : D%3≠0 := by have := FiberTransport.unit_pow_two h b ub; omega
  obtain ⟨i,_,imax,res⟩ := FiberRouting.small_power q D du
  have mod_eq : 2^i%M=D%M := by simpa only [M,pow_succ,Nat.mul_comm] using res
  have ipow : 2^i≤2^P := Nat.pow_le_pow_right (by decide) imax
  have diff : 2^i+M*b<D := by omega
  let t := (D-2^i)/M
  have mul : M*t=D-2^i := Nat.mul_div_cancel'
    (Nat.dvd_of_mod_eq_zero (Nat.sub_mod_eq_zero_of_mod_eq mod_eq.symm))
  have parts : D=2^i+M*t := by omega
  have bt : b<t := by
    by_contra! ht
    have le := Nat.mul_le_mul_left M ht
    omega
  let y := a+3^q*t
  have route : 2^h*b=2^i+3*y := by rw [expand,parts]; dsimp [y,M]; ring
  let f := h-i
  have spare : i+3≤h := calc
    i+3 ≤ P+3 := Nat.add_le_add_right imax 3
    _ ≤ K+P+3 := Nat.add_le_add_right (Nat.le_add_left P K) 3
    _ ≤ K+P+4 := Nat.add_le_add_left (by decide : 3≤4) _
    _ ≤ h := late
  have hf : i+f=h := by dsimp only [f]; omega
  have fbig : 3≤f := by dsimp only [f]; omega
  let Z := 2^f*b
  have fac : 2^i*Z=2^i+3*y := by
    calc
      _ = 2^(i+f)*b := by dsimp [Z]; rw [pow_add]; ac_rfl
      _ = _ := hf ▸ route
  have unit := FiberTransport.unit_pow_two i 1 (by decide)
  simp only [Nat.mul_one] at unit
  have residues := congrArg (·%3) fac
  have zr : Z%3=1 := by
    rw [Nat.mul_mod] at residues
    rcases (show 2^i%3=1 ∨ 2^i%3=2 by omega) with hi | hi <;>
      rw [hi] at residues <;> omega
  let w := Z/3
  have zw : Z=3*w+1 := by dsimp [w]; omega
  have yw : y=2^i*w := by
    rw [zw] at fac
    nlinarith only [fac]
  have big : 8*b≤Z := Nat.mul_le_mul_right b
    (Nat.pow_le_pow_right (by decide : 0<2) fbig)
  have wb : b<w := by omega
  refine ⟨t,i,bt,imax,route,?_⟩
  change FirstLow h y b
  rw [←hf,yw]
  apply first_append (halve i w) _ (odd_then_halves (by omega) wb bp zw)
  intro j hj
  exact lt_trans wb ((first_dyadic i w (by omega)).2 j hj)

private theorem self_le_run (h x : ℕ) : x≤2^h*run h x := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih =>
    have one : x≤2*step x := by unfold step; split <;> omega
    have tail := Nat.mul_le_mul_left 2 (ih (step x))
    calc
      _ ≤ _ := one
      _ ≤ _ := tail
      _ = _ := by rw [run,pow_succ]; ring

/-- One threshold for a whole finite family, every target coprime to three,
and every later physical clock. The same translation sends all arms to their
first strict low at that target. The position satisfies an exact equation. -/
theorem affine_first (bs : List Ray) :
    ∃ (H q a r N : ℕ), ∀ S≥N, ∀ b, b%3≠0 →
      ∃ x i, 0<x ∧ i≤2*3^q ∧
        3^(q+1)*x+2^H*(2^i+3*a)=2^S*b+3^(q+1)*r ∧
        FirstLow S x b ∧ ∀ z∈bs, FirstLow S (z.value x) b := by
  let anchor : Ray := ⟨0,0⟩
  obtain ⟨w,fusion⟩ := finite_fusion anchor bs
  let H := w.length
  let q := (walk w anchor).grade
  let a := (walk w anchor).base
  let r := position w
  obtain ⟨N,route⟩ := ray_first a q
  refine ⟨H,q,a,r,H+N,?_⟩
  intro S late b ub
  let f := S-H
  have hf : H+f=S := by dsimp [f]; omega
  obtain ⟨t,i,bt,bound,eq,tail⟩ := route f (by dsimp [f]; omega) b ub
  let x := r+2^H*t
  have xp : 0<x := by
    have pos := Nat.mul_pos (Nat.two_pow_pos H) (show 0<t by omega)
    dsimp [x]; omega
  have exact_pos : 3^(q+1)*x+2^H*(2^i+3*a)=2^S*b+3^(q+1)*r := by
    rw [←hf,pow_add 2 H f,Nat.mul_assoc (2^H) (2^f) b,eq]
    dsimp [x]
    rw [pow_succ]
    ring
  have each (z : Ray) (same : walk w z=walk w anchor) : FirstLow S (z.value x) b := by
    have hit := walk_value w z t
    rw [same] at hit
    change run H (z.value x)=a+3^q*t at hit
    rw [←hf]
    apply first_append hit _ tail
    intro j jh
    have size : 2^H*t≤z.value x := by
      have le := Nat.le_mul_of_pos_left x (Nat.pow_pos (by decide : 0<3) (n:=z.grade))
      dsimp [Ray.value,x] at *; omega
    have le := Nat.mul_le_mul_right t (Nat.pow_le_pow_right (by decide : 0<2) (Nat.le_of_lt jh))
    have cap := self_le_run j (z.value x)
    have lower : t≤run j (z.value x) :=
      Nat.le_of_mul_le_mul_left (le.trans (size.trans cap)) (Nat.two_pow_pos j)
    omega
  have root := each anchor rfl
  simp only [anchor,Ray.value,pow_zero,one_mul,zero_add] at root
  exact ⟨x,i,xp,bound,exact_pos,root,fun z hz => each z (fusion z hz)⟩

#print axioms ray_first
#print axioms affine_first
end Collatz.Itinerary.PassageRouting

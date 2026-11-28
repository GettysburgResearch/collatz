module

public import TernaryItinerary
import all TernaryItinerary

public section
namespace Collatz.Itinerary.BasinTransport

set_option autoImplicit false

private theorem odd_run (b m : Nat) (pos : 0<m) :
    run b (2^b*m-1)=3^b*m-1 := by
  induction b generalizing m with
  | zero => simp [run]
  | succ b ih =>
    let z := 2^b*m
    have zp : 0<z := Nat.mul_pos (Nat.pow_pos (by decide)) pos
    have start : 2^(b+1)*m-1=2*z-1 := by
      dsimp [z]; rw [Nat.pow_succ]; congr 1; ac_rfl
    have odd : (2*z-1)%2=1 := by omega
    have next : step (2*z-1)=3*z-1 := by simp [step,odd]; omega
    rw [start,run,next,show 3*z-1=2^b*(3*m)-1 by dsimp [z]; rw [Nat.mul_left_comm]]
    rw [ih (3*m) (by omega),Nat.pow_succ]
    rw [Nat.mul_assoc]

/-- The two affine samples have the same ordinary future. Their leading
coefficient ratio ranges over 2^z*3^b, with b nonnegative and z integral. -/
theorem affine_rays (b d e m : Nat) (pos : 0<m) :
    run (d+b) (2^d*(2^b*m-1)) = run e (2^e*(3^b*m-1)) := by
  rw [run_add,halve,halve,odd_run b m pos]

/-- All starts in the block have the same endpoint at a common physical time. -/
@[expose] def fused (h n width : Nat) : Bool :=
  (List.range width).all (fun j => run h (n+j) == run h n)

private theorem eval_fused {h n width j : Nat} (f : fused h n width=true) (hj : j<width) :
    run h (n+j)=run h n := by
  exact beq_iff_eq.mp (List.all_eq_true.mp f j (List.mem_range.mpr hj))

/-- Couple the two children of n to the single source n, with a one-clock offset. -/
theorem double_tile {h n i : Nat} (f : fused h (2*n) 2=true) (hi : i<2) :
    run (h+1) (2*n+i)=run h n := by
  rw [run_add,eval_fused f hi,←run_add,Nat.add_comm h 1,run_add]
  have eq : run 1 (2*n)=n := by change step (2*n)=n; simp [step]
  rw [eq]

/-- Every one of the twelve pairings of these two blocks is a physical
meeting when both small blocks fuse. The two clocks differ by exactly two. -/
theorem three_four_tile {h n i j : Nat} (a : fused h (4*n) 4=true)
    (b : fused h (3*n) 3=true) (hi : i<4) (hj : j<3) :
    run (h+2) (4*n+i)=run h (3*n+j) := by
  have left := (eval_fused a hi).trans (eval_fused a (j:=1) (by decide)).symm
  have right := (eval_fused b hj).trans (eval_fused b (j:=1) (by decide)).symm
  have bridge : run 2 (4*n+1)=3*n+1 := by
    simp only [run]
    unfold step
    split <;> split <;> omega
  rw [run_add,left,←run_add,Nat.add_comm h 2,run_add,bridge,right]

#print axioms affine_rays
#print axioms double_tile
#print axioms three_four_tile
end Collatz.Itinerary.BasinTransport

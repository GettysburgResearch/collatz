import EarlierOffsets

/-! Ordinary dyadic copies of a prescribed positive pair and explicit mergers
of their displaced neighbors. The centers are retained as separate inputs. -/
set_option autoImplicit false
set_option warningAsError true
namespace DyadicPins
open CoreBranching FloorCounting PeakRigidity EarlierOffsets

private theorem exact_halves (k n : ℕ) : run k (2^k*n)=n := by
  induction k with
  | zero => simp [run]
  | succ k ih =>
    rw [pow_succ,show 2^k*2*n=2*(2^k*n) by ring,run,step_double,ih]

private theorem plus_four (n : ℕ) : run 2 (4*n+1)=3*n+1 := by
  simpa using PaidCheckpoint.positive_turns 1 n

private theorem invariant_run {α : Type*} (f : ℕ → α) (inv : ∀ n, f (step n)=f n)
    (k n : ℕ) : f (run k n)=f n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih (step n)).trans (inv n)

/-- The two right neighbors are physically two steps apart, while the two
centers are pure dyadic lifts of the original ordered pair. -/
theorem pinned_neighbors (k q : ℕ) :
    run (k+2) (2^(k+2)*q)=q ∧ run k (2^k*(3*q))=3*q ∧
    run 2 (2^(k+2)*q+1)=2^k*(3*q)+1 := by
  refine ⟨exact_halves _ _,exact_halves _ _,?_⟩
  rw [pow_add,show 2^k*2^2*q+1=4*(2^k*q)+1 by ring,plus_four]
  ring

/-- Every scale carries the same signed discrepancy of the two fixed centers. -/
theorem signed_pin (f : ℕ → ℤ) (inv : ∀ n, f (step n)=f n) (k q : ℕ) :
    f (3*q)-f q = (f (2^(k+2)*q+1)-f (2^(k+2)*q)) -
      (f (2^k*(3*q)+1)-f (2^k*(3*q))) := by
  obtain ⟨l,r,h⟩ := pinned_neighbors k q
  have hl := invariant_run f inv (k+2) (2^(k+2)*q)
  have hr := invariant_run f inv k (2^k*(3*q))
  have hh := invariant_run f inv 2 (2^(k+2)*q+1)
  rw [l] at hl; rw [r] at hr; rw [h] at hh
  omega

/-- For the actual reach-one predicate, at each depth exactly one center
has the opposite membership from its immediate right neighbor. -/
theorem good_pin_exclusive (k q : ℕ) (diff : ¬ (Good q ↔ Good (3*q))) :
    ¬ ((Good (2^(k+2)*q) ↔ Good (2^(k+2)*q+1)) ↔
       (Good (2^k*(3*q)) ↔ Good (2^k*(3*q)+1))) := by
  obtain ⟨l,r,h⟩ := pinned_neighbors k q
  have hl := good_run (k+2) (2^(k+2)*q)
  have hr := good_run k (2^k*(3*q))
  have hh := good_run 2 (2^(k+2)*q+1)
  rw [l] at hl; rw [r] at hr; rw [h] at hh
  tauto

/-- Four actual trajectories at a prescribed moving low-bit residue. -/
def Row (h x y : ℕ) : Prop :=
  run h (x-1)=y ∧ run h (x+1)=y ∧
  run h (3*x-1)=y ∧ run h (3*x+1)=y

private theorem row_lift (h r v y p : ℕ) (pos : 0<r)
    (base : Row h r y) (grading : grade h (r-1)=p+1 ∧ grade h (r+1)=p+1 ∧
      grade h (3*r-1)=p ∧ grade h (3*r+1)=p) :
    Row h (r+2^h*v) (y+3^(p+1)*v) := by
  obtain ⟨a,b,c,d⟩ := base
  obtain ⟨e,f,g,i⟩ := grading
  have A := (lift_prefix h 0 (r-1) v).1
  have B := (lift_prefix h 0 (r+1) v).1
  have C := (lift_prefix h 0 (3*r-1) (3*v)).1
  have D := (lift_prefix h 0 (3*r+1) (3*v)).1
  simp only [Nat.add_zero,pow_zero,one_mul,a,b,c,d,e,f,g,i] at A B C D
  unfold Row
  have l : r+2^h*v-1=r-1+2^h*v := by omega
  have lt : 3*(r+2^h*v)-1=3*r-1+2^h*(3*v) := by
    rw [Nat.mul_add,show 3*(2^h*v)=2^h*(3*v) by ring]; omega
  rw [l,show (r+2^h*v)+1=r+1+2^h*v by omega,lt,
    show 3*(r+2^h*v)+1=3*r+1+2^h*(3*v) by ring,A,B,C,D,pow_succ]
  constructor <;> first | rfl | constructor <;> first | rfl | constructor <;> ring

private theorem row99 (v : ℕ) : Row 8 (99+256*v) (11+27*v) := by
  exact row_lift 8 99 v 11 2 (by decide) (by unfold Row; decide +kernel) (by decide +kernel)

private theorem row237 (v : ℕ) : Row 9 (237+512*v) (38+81*v) := by
  exact row_lift 9 237 v 38 3 (by decide) (by unfold Row; decide +kernel) (by decide +kernel)

private theorem residue_wheel (a : Fin 512) (odd : a.val%2=1) :
    ∃ i : Fin 128, (3^i.val*a.val)%256=99 ∨ (3^i.val*a.val)%512=237 := by
  revert odd a
  decide +kernel

/-- From any exponent onward, one of the next 128 exponent choices fuses
both displaced neighbors associated to each of the original positive centers. -/
theorem four_collar_window (q start : ℕ) (odd : q%2=1) :
    ∃ k h y : ℕ, start≤k ∧ k<start+128 ∧ h≤9 ∧
      run (k+h) (2^k*q-1)=y ∧ run (2*k+h) (4^k*q+1)=y ∧
      run (k+h) (2^k*(3*q)-1)=y ∧ run (2*k+h) (4^k*(3*q)+1)=y := by
  let a := 3^start*q
  have ao : a%2=1 := by
    dsimp [a]; rw [Nat.mul_mod,Nat.pow_mod]; simp [odd]
  obtain ⟨i,ei⟩ := residue_wheel ⟨a%512,Nat.mod_lt _ (by decide)⟩ (by
    change a%512%2=1; rwa [Nat.mod_mod_of_dvd _ (by decide : 2 ∣ 512)])
  let k := start+i.val
  let x := 3^k*q
  have xeq : x=3^i.val*a := by dsimp [x,k,a]; rw [pow_add]; ring
  have e : x%256=99 ∨ x%512=237 := by
    change (3^i.val*(a%512))%256=99 ∨ (3^i.val*(a%512))%512=237 at ei
    rcases ei with u|u
    · left; rw [xeq,Nat.mul_mod] at *
      simpa [Nat.mod_mod_of_dvd _ (by decide : 256 ∣ 512)] using u
    · right; rw [xeq,Nat.mul_mod]; simpa [Nat.mul_mod] using u
  obtain ⟨h,y,bound,row⟩ : ∃ h y : ℕ, h≤9 ∧ Row h x y := by
    rcases e with e|e
    · exact ⟨8,11+27*(x/256),by decide,by convert row99 (x/256) using 1; omega⟩
    · exact ⟨9,38+81*(x/512),by decide,by convert row237 (x/512) using 1; omega⟩
  obtain ⟨l,r,L,R⟩ := row
  have hp : 0<q := by omega
  refine ⟨k,h,y,by dsimp [k]; omega,by dsimp [k]; omega,bound,?_,?_,?_,?_⟩
  · rw [run_add,ascent k q hp]; exact l
  · rw [run_add,PaidCheckpoint.positive_turns]; exact r
  · rw [run_add,ascent k (3*q) (by omega),show 3^k*(3*q)=3*x by dsimp [x]; ring]
    exact L
  · rw [run_add,PaidCheckpoint.positive_turns,show 3^k*(3*q)=3*x by dsimp [x]; ring]
    exact R

#print axioms pinned_neighbors
#print axioms signed_pin
#print axioms good_pin_exclusive
#print axioms four_collar_window
end DyadicPins

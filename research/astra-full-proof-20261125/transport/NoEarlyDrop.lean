import SignedPrefix

namespace Collatz.NoEarlyDrop
open Collatz.SourceDeletion Collatz.SignedPrefix

def source : Nat → Nat
  | 0 => 77671
  | m+1 => 262144*source m+339815

theorem identity (m : Nat) : 27*source m+35=2^(21+18*m) := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [show 21+18*(m+1)=(21+18*m)+18 by omega,pow_add,←ih]
    simp only [source]; ring

private theorem catRun (i j x : Nat) : run (i+j) x=run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem halves (k t : Nat) : run k (2^k*t)=t := by
  induction k with
  | zero => simp [run]
  | succ k ih =>
    rw [show 2^(k+1)*t=2*(2^k*t) by ring,run]
    have s : step (2*(2^k*t))=2^k*t := by unfold step; split <;> omega
    rw [s]; exact ih

private theorem oddRun (k t : Nat) (pos : 0<t) : run k (2^k*t-1)+1=3^k*t := by
  induction k generalizing t with
  | zero => simp [run]; omega
  | succ k ih =>
    have e : 2^(k+1)*t=2*(2^k*t) := by ring
    have p : 0<2^k*t := Nat.mul_pos (Nat.pow_pos (by decide)) pos
    have s : step (2^(k+1)*t-1)=2^k*(3*t)-1 := by
      rw [e,show 2^k*(3*t)=3*(2^k*t) by ring]; unfold step; split <;> omega
    rw [run,s,ih (3*t) (by omega)]; ring

private theorem cycle_small (j n : Nat) (hn : n=1 ∨ n=2) : run j n≤2 := by
  induction j generalizing n with
  | zero => change n≤2; omega
  | succ j ih => apply ih (step n); rcases hn with h|h <;> subst n <;> decide

private theorem phase (m : Nat) :
    let H := 21+18*m
    run 4 (source m)+1=2^(H-4) ∧ run 6 (3*source m)=2^(H-6) ∧
    run H (3*source m)=1 ∧ odds H (3*source m)=2 := by
  dsimp only
  let H := 21+18*m
  have eq := identity m
  have cast : (3:Int)^3*(source m : Int)= -35+2^H := by
    have cp : (27:Int)*source m+35=2^H := by exact_mod_cast eq
    change 27*(source m:Int)= -35+2^H; omega
  have four : 4+(H-4)=H := by dsimp [H]; omega
  have six : 6+(H-6)=H := by dsimp [H]; omega
  have lo := (integer_endpoint 4 (H-4) 3 0 (source m) (-35) (-1)
    (by rwa [four]) (by decide) (by decide)).1
  have high : (3:Int)^2*((3*source m:Nat):Int)= -35+2^(6+(H-6)) := by
    rw [six,←cast]; push_cast; ring
  have hi := (integer_endpoint 6 (H-6) 2 0 (3*source m) (-35) 0 high (by decide) (by decide)).1
  obtain ⟨hit,od⟩ := upper_certificate (R:=2) (j:=6) (r:=H-6)
    (by rwa [six] : (3:Int)^(2+1)*source m= -35+2^(6+(H-6))) (by decide) (by decide)
  rw [six] at hit od
  have lt : (↑(run 4 (source m)):Int)+1=2^(H-4) := by simp at lo; omega
  exact ⟨by exact_mod_cast lt,by exact_mod_cast (show (run 6 (3*source m):Int)=2^(H-6) by simpa using hi),hit,od⟩

/-- A genuine first two-odd upper hit. Every positive lower clock up to and
including that supplied upper hit exceeds its own starting height. -/
theorem no_early_drop (m : Nat) :
    let H := 21+18*m
    let z := source m
    run H (3*z)=1 ∧ odds H (3*z)=2 ∧
      (∀ i<H, run i (3*z)≠1) ∧
      (∀ i, 0<i → i≤H → z<run i z) ∧
      run 4 z+1=2^(H-4) ∧ run H z+1=3^(H-4) := by
  dsimp only
  let H := 21+18*m
  let z := source m
  have hh : 21≤H := by dsimp [H]; omega
  obtain ⟨four,six,hit,od⟩ := phase m
  change run 4 z+1=2^(H-4) at four
  change run 6 (3*z)=2^(H-6) at six
  have eq := identity m
  change 27*z+35=2^H at eq
  have pow : 2^H=16*2^(H-4) := by calc
    2^H=2^(4+(H-4)) := congrArg (fun x : Nat => 2^x) (by omega)
    _ = 16*2^(H-4) := by rw [pow_add]; rfl
  have z0 : z=16*(z/16)+7 := by rw [pow] at eq; omega
  let t := z/16
  have s1 : step z=24*t+11 := by dsimp [t]; unfold step; split <;> omega
  have s2 : step (24*t+11)=36*t+17 := by unfold step; split <;> omega
  have s3 : step (36*t+17)=54*t+26 := by unfold step; split <;> omega
  have mid : z<run 4 z := by rw [pow,←four] at eq; omega
  refine ⟨hit,od,?_,?_,four,?_⟩
  · intro i lt early
    change i<H at lt
    change run i (3*z)=1 at early
    have pre (k : Nat) (a : 6≤k) (b : k≤H) : run k (3*z)=2^(H-k) := by
      have e : H-6=(k-6)+(H-k) := by omega
      rw [show k=6+(k-6) by omega,catRun,six,e,pow_add,halves]
      congr 1; omega
    by_cases low : i≤H-2
    · have bound := cycle_small (H-2-i) 1 (Or.inl rfl)
      rw [←early,←catRun,show i+(H-2-i)=H-2 by omega,pre (H-2) (by omega) (by omega),
        show H-(H-2)=2 by omega] at bound
      contradiction
    · rw [pre i (by omega) (by omega),show H-i=1 by omega] at early; contradiction
  · intro i pos le
    change i≤H at le
    change z<run i z
    by_cases before : i<4
    · rcases (show i=1 ∨ i=2 ∨ i=3 by omega) with h|h|h <;> subst i <;>
        simp only [run,s1,s2,s3] <;> dsimp [t] <;> omega
    · let k := i-4
      let r := H-i
      have ii : i=4+k := by dsimp [k]; omega
      have size : H-4=k+r := by dsimp [k,r]; omega
      have pos2 : 0<(2:Nat)^r := Nat.pow_pos (by decide)
      have start : run 4 z=2^k*2^r-1 := by rw [size,pow_add] at four; omega
      have finish := oddRun k (2^r) pos2
      rw [ii,catRun,start]
      have ge := Nat.mul_le_mul_right (2^r) (Nat.pow_le_pow_left (by decide : 2≤3) k)
      omega
  · change run H z+1=3^(H-4)
    conv_lhs => rw [show H=4+(H-4) by omega,catRun]
    have st : run 4 z=2^(H-4)*1-1 := by omega
    rw [st,oddRun (H-4) 1 (by decide),Nat.mul_one]

#print axioms identity
#print axioms no_early_drop

end Collatz.NoEarlyDrop

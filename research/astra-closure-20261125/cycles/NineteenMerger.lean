import Std

namespace NineteenMerger

def step (x : Nat) : Nat :=
  if x % 2 = 0 then x / 2 else (3*x+1)/2

def run : Nat → Nat → Nat
  | 0,x => x
  | k+1,x => run k (step x)

def odds : Nat → Nat → Nat
  | 0,_ => 0
  | k+1,x => odds k (step x) + x%2

private theorem step_lift (x z : Nat) :
    step (x+2*z) = step x + 3^(x%2)*z := by
  simp only [step]
  by_cases h : x%2 = 0
  · have h' : (x+2*z)%2=0 := by omega
    simp [h, h']; omega
  · have hr : x%2=1 := by omega
    have hr' : (x+2*z)%2=1 := by omega
    simp [hr, hr']; omega

theorem run_lift (k x z : Nat) :
    run k (x+2^k*z) = run k x + 3^(odds k x)*z := by
  induction k generalizing x z with
  | zero => simp [run, odds]
  | succ k ih =>
    rw [run, odds, Nat.pow_add 3, run]
    have h : 2^(k+1)*z = 2*(2^k*z) := by rw [Nat.pow_succ]; ac_rfl
    rw [h, step_lift]
    rw [show 3^(x%2)*(2^k*z)=2^k*(3^(x%2)*z) by ac_rfl, ih]
    ac_rfl

/-- All odd members of the ternary residue class, through a literal endpoint. -/
theorem family (t : Nat) :
    let s := 187605073 + 2324522934*t
    let y := 259975167 + 3221225472*t
    0 < y ∧ 3 ∣ y ∧ y < 2*s+1 ∧ run 30 y = step s := by
  dsimp only
  have hv : run 30 259975167 = 281407610 := by decide
  have ho : odds 30 259975167 = 19 := by decide
  have h := run_lift 30 259975167 (3*t)
  rw [hv, ho] at h
  have hp : 2^30*(3*t)=3221225472*t := by omega
  rw [hp] at h
  have hs : (187605073+2324522934*t)%2=1 := by omega
  refine ⟨by omega, ⟨86658389+1073741824*t, by omega⟩, by omega, ?_⟩
  simpa only [step, hs, Nat.reduceEqDiff, ite_false] using
    (show run 30 (259975167+3221225472*t) =
      (3*(187605073+2324522934*t)+1)/2 by omega)

theorem whole_residue {s : Nat} (hodd : s%2=1) (hr : s%1162261467=187605073) :
    ∃ y, 0 < y ∧ 3 ∣ y ∧ y < 2*s+1 ∧ run 30 y = step s := by
  let q := s / 1162261467
  have hs : s = 187605073 + 1162261467*q := by
    have h := Nat.mod_add_div s 1162261467
    rw [hr] at h
    exact h.symm
  have parity (n : Nat) : (187605073+1162261467*n)%2 = 1 → n%2=0 := by
    rw [Nat.add_mod, Nat.mul_mod]
    simp only [show 187605073 % 2 = 1 by decide,
      Nat.one_mul, Nat.mod_mod]
    omega
  have hq : q%2 = 0 := parity q (hs ▸ hodd)
  have half := Nat.mod_add_div q 2
  rw [hq, Nat.zero_add] at half
  have eq : s = 187605073+2324522934*(q/2) := calc
    s = 187605073+1162261467*q := hs
    _ = 187605073+1162261467*(2*(q/2)) := congrArg (187605073+1162261467*·) half.symm
    _ = _ := by rw [← Nat.mul_assoc]
  have h := family (q/2)
  dsimp only at h
  exact ⟨_, h.1, h.2.1, eq ▸ h.2.2⟩

#print axioms run_lift
#print axioms family
#print axioms whole_residue

end NineteenMerger

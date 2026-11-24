import TernaryHeadDescent

/-! One complete arithmetic progression of synchronized 81-child fibers,
established by kernel computation on a representative and exact affine lifting. -/
namespace CollatzShell.TernaryHead

private def oddCount : Nat → Nat → Nat
  | 0,_ => 0
  | k+1,n => oddCount k (step n) + n%2

-- The ordinary affine-lift argument is the one in the pinned ShellCover source.
private theorem one_lift (a b : Nat) :
    step (2*a+b) = 3^(b%2)*a + step b := by
  by_cases ev : b%2=0
  · simp [step,ev,show (2*a+b)%2=0 by omega]; omega
  · have odd : b%2=1 := by omega
    simp [step,odd]; omega

private theorem lift_profile (k b t : Nat) :
    orbit k (2^k*t+b) = 3^(oddCount k b)*t+orbit k b := by
  induction k generalizing b t with
  | zero => simp [orbit,oddCount]
  | succ k ih =>
    rw [show 2^(k+1)*t+b=2*(2^k*t)+b by ring]
    simp only [orbit,oddCount,one_lift,pow_add]
    rw [show 3^(b%2)*(2^k*t)+step b=2^k*(3^(b%2)*t)+step b by ring,ih]
    ring

def fiberSeed : Nat := 4472729219385379069831775978630415924694613450521487

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
private theorem fiber_check : ∀ r : Fin 81,
    orbit 172 (81*fiberSeed+r.val) = orbit 172 fiberSeed ∧
    oddCount 172 (81*fiberSeed+r.val)+4 = oddCount 172 fiberSeed := by
  decide +kernel

theorem whole_fiber (t r : Nat) (hr : r<81) :
    let m := 2^172*t+fiberSeed
    orbit 172 (81*m+r) = orbit 172 m := by
  dsimp only
  obtain ⟨endpoint,count⟩ := fiber_check ⟨r,hr⟩
  change orbit 172 (81*fiberSeed+r)=orbit 172 fiberSeed at endpoint
  change oddCount 172 (81*fiberSeed+r)+4=oddCount 172 fiberSeed at count
  rw [show 81*(2^172*t+fiberSeed)+r=2^172*(81*t)+(81*fiberSeed+r) by ring,
    lift_profile,lift_profile,endpoint,←count,pow_add]
  ring

end CollatzShell.TernaryHead

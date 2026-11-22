module

public import ShellCover

@[expose] public section

/-!
# Exact arbitrary-debt transport for an ordinary source gap

The complement map is the positive 3x-1 shortcut map.  It is used only for
finite arithmetic: no convergence assertion about that map is assumed.
Every conclusion about the target uses the existing ordinary Collatz orbit.
-/

namespace CollatzShell.AffineCarry

def minusStep (b : Nat) : Nat :=
  if b % 2 = 0 then b / 2 else (3*b-1)/2

def minusOrbit : Nat → Nat → Nat
  | 0, b => b
  | k+1, b => minusOrbit k (minusStep b)

def minusOdds : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, b => minusOdds k (minusStep b) + b%2

theorem minus_step_positive {b : Nat} (positive : 0<b) : 0<minusStep b := by
  unfold minusStep
  split <;> omega

theorem ordinary_step_positive {n : Nat} (positive : 0<n) : 0<step n := by
  unfold step
  split <;> omega

theorem ordinary_orbit_positive (k n : Nat) (positive : 0<n) : 0<orbit k n := by
  induction k generalizing n with
  | zero => exact positive
  | succ k ih => exact ih (step n) (ordinary_step_positive positive)

/-- The ordinary and complementary steps have the same parity when their
inputs sum to an even number. Their affine constants cancel exactly. -/
theorem complement_step {n b t : Nat} (bn : 0<b) (sum : n+b=2*t) :
    step n+minusStep b=3^(b%2)*t := by
  by_cases even : b%2=0
  · have en : n%2=0 := by omega
    simp [step,minusStep,even,en]
    omega
  · have odd : b%2=1 := by omega
    have on : n%2≠0 := by omega
    simp [step,minusStep,on,odd]
    omega

/-- Exact finite transport across a complementary binary cylinder. No
negative ordinary input and no natural-subtraction underflow is used. -/
theorem complement_orbit (k n b t : Nat) (bn : 0<b)
    (sum : n+b=2^k*t) :
    orbit k n+minusOrbit k b=3^(minusOdds k b)*t := by
  induction k generalizing n b t with
  | zero => simpa [orbit,minusOrbit,minusOdds] using sum
  | succ k ih =>
    have start : n+b=2*(2^k*t) := by rw [sum,pow_succ]; ring
    have first := complement_step bn start
    have after : step n+minusStep b=2^k*(3^(b%2)*t) := by
      rw [first]
      ring
    have result := ih (step n) (minusStep b) (3^(b%2)*t)
      (minus_step_positive bn) after
    simpa only [orbit,minusOrbit,minusOdds,pow_add,Nat.mul_assoc] using result

/-- A supplied source gap transports an arbitrary ternary debt. The
coefficient exponent and the complete nonnegative debt are both retained. -/
theorem gap_transport {r u a p d n : Nat} (hp : 0<p)
    (gap : 3*r+1=2^a*u) (target : n+d=3^p*r) :
    orbit a n+minusOrbit a (3^(p-1)+d)=
      3^(p-1+minusOdds a (3^(p-1)+d))*u := by
  have three : 3^p=3^(p-1)*3 := by
    simpa only [show p-1+1=p by omega] using (pow_succ (3:Nat) (p-1))
  have sum : n+(3^(p-1)+d)=2^a*(3^(p-1)*u) := by
    calc
      n+(3^(p-1)+d)=(n+d)+3^(p-1) := by ring
      _ =3^(p-1)*(3*r+1) := by rw [target,three]; ring
      _ =2^a*(3^(p-1)*u) := by rw [gap]; ring
  have result := complement_orbit a n (3^(p-1)+d) (3^(p-1)*u)
    (by positivity) sum
  rw [pow_add]
  nlinarith [result]

/-- A debt endpoint enters the interval of an explicitly padded retained
source whenever its leading coefficient fits. This is an interval statement,
not an assumption that the target converges. -/
theorem padded_capture {z d p e u : Nat} (positive : 0<z)
    (balance : z+d=3^p*u) (budget : 3^p≤2^(e+1)) :
    0<z ∧ z≤2*(2^e*u)+1 := by
  refine ⟨positive,?_⟩
  have bound := Nat.mul_le_mul_right u budget
  rw [pow_succ] at bound
  nlinarith

/-- Once the exponent is zero, the original unpadded literal source tail
suffices for the interval bound, with every positive debt retained. -/
theorem zero_debt_capture {z d u : Nat} (positive : 0<z)
    (balance : z+d=u) : 0<z ∧ z≤2*u+1 := by omega

/-- The previously unsupported state D2 followed by a gap one has a physical
transition. Its new debt is two; it is not silently replaced by D1. -/
theorem debt_two_gap_one {r u : Nat} (gap : 3*r+1=2*u) :
    step (9*r-1)+2=3*u := by
  have rp : 0<r := by omega
  unfold step
  split <;> omega

/-- Five successive gap-one source clocks transport the failed short-diamond
carry to four below the retained source. This is an infinite affine family. -/
theorem five_ones_capture (v : Nat) (positive : 0<v) :
    orbit 5 (9*(2^5*v-1)+2)+4=3^5*v-1 := by
  have sum : 9*(2^5*v-1)+2+7=2^5*(9*v) := by norm_num; omega
  have result := complement_orbit 5 (9*(2^5*v-1)+2) 7 (9*v) (by decide) sum
  norm_num [minusOrbit,minusOdds,minusStep] at result ⊢
  omega

private theorem five_scaled_odd {n : Nat} (odd : n%2=1) :
    10*step n=15*n+5 := by
  simp only [step,odd,show (1:Nat)≠0 by decide,ite_false]
  omega

private theorem five_scaled_even {n : Nat} (even : n%2=0) :
    10*step n=5*n := by
  simp only [step,even,ite_true]
  omega

/-- One complete rational-offset period, expressed entirely on ordinary
integers. The offset 19/5 follows the parity word 11100. -/
theorem ghost_five_clocks {n v : Nat} (input : 5*n=32*v+19) :
    5*orbit 5 n=27*v+19 := by
  have a : 5*step n=48*v+31 := by
    have result := five_scaled_odd (n:=n) (by omega)
    omega
  have b : 5*step (step n)=72*v+49 := by
    have result := five_scaled_odd (n:=step n) (by omega)
    omega
  have c : 5*step (step (step n))=108*v+76 := by
    have result := five_scaled_odd (n:=step (step n)) (by omega)
    omega
  have d : 5*step (step (step (step n)))=54*v+38 := by
    have result := five_scaled_even (n:=step (step (step n))) (by omega)
    omega
  have e : 5*step (step (step (step (step n))))=27*v+19 := by
    have result := five_scaled_even (n:=step (step (step (step n)))) (by omega)
    omega
  simpa only [orbit] using e

/-- Every length of the rational-offset period has its exact ordinary
realization on the corresponding binary cylinder. -/
theorem ghost_periods (k n v : Nat) (input : 5*n=2^(5*k)*v+19) :
    5*orbit (5*k) n=3^(3*k)*v+19 := by
  induction k generalizing n v with
  | zero => simpa [orbit] using input
  | succ k ih =>
    have power : 2^(5*(k+1))=32*2^(5*k) := by
      rw [show 5*(k+1)=5+5*k by omega,pow_add]
      norm_num
    have first := ghost_five_clocks (n:=n) (v:=2^(5*k)*v) (by
      rw [power] at input
      nlinarith [input])
    have next : 5*orbit 5 n=2^(5*k)*(27*v)+19 := by nlinarith [first]
    have result := ih (orbit 5 n) (27*v) next
    have three : 3^(3*(k+1))=27*3^(3*k) := by
      rw [show 3*(k+1)=3+3*k by omega,pow_add]
      norm_num
    rw [show 5*(k+1)=5+5*k by omega,orbit_add,three]
    nlinarith [result]

private theorem source_three_clocks {n v : Nat} (input : 5*n=8*v+1) :
    5*orbit 3 n=3*v+1 := by
  have a : 5*step n=12*v+4 := by
    have result := five_scaled_odd (n:=n) (by omega)
    omega
  have b : 5*step (step n)=6*v+2 := by
    have result := five_scaled_even (n:=step n) (by omega)
    omega
  have c : 5*step (step (step n))=3*v+1 := by
    have result := five_scaled_even (n:=step (step n)) (by omega)
    omega
  simpa only [orbit] using c

/-- A source cylinder consisting of arbitrary many gap-three blocks. -/
theorem source_threes (k n v : Nat) (input : 5*n=2^(3*k)*v+1) :
    5*orbit (3*k) n=3^k*v+1 := by
  induction k generalizing n v with
  | zero => simpa [orbit] using input
  | succ k ih =>
    have power : 2^(3*(k+1))=8*2^(3*k) := by
      rw [show 3*(k+1)=3+3*k by omega,pow_add]
      norm_num
    have first := source_three_clocks (n:=n) (v:=2^(3*k)*v) (by
      rw [power] at input
      nlinarith [input])
    have next : 5*orbit 3 n=2^(3*k)*(3*v)+1 := by nlinarith [first]
    have result := ih (orbit 3 n) (3*v) next
    rw [show 3*(k+1)=3+3*k by omega,orbit_add,pow_succ]
    nlinarith [result]

/-- The complete actual two-arm calculation at every parameter k. The
ternary coefficient is 3^(4k+2), so a fixed debt-state cutoff cannot cover
even these finite ordinary prefixes. This is not an infinite ordinary orbit. -/
theorem ordinary_debt_amplification (k r v : Nat)
    (input : 5*r=2^(15*k)*v+1) :
    5*orbit (15*k) (9*r+2)+3^(4*k+2)=
      5*3^(4*k+2)*orbit (15*k) r+19 := by
  have source := source_threes (5*k) r v (by
    simpa only [show 3*(5*k)=15*k by omega] using input)
  have target := ghost_periods (3*k) (9*r+2) (9*v) (by
    rw [show 5*(3*k)=15*k by omega]
    nlinarith [input])
  rw [show 3*(5*k)=15*k by omega] at source
  rw [show 5*(3*k)=15*k by omega,show 3*(3*k)=9*k by omega] at target
  have powers : 3^(4*k+2)*3^(5*k)=3^(9*k)*9 := by
    rw [← pow_add,show 4*k+2+5*k=9*k+2 by omega,pow_add]
    norm_num
  calc
    5*orbit (15*k) (9*r+2)+3^(4*k+2)=
        3^(9*k)*(9*v)+19+3^(4*k+2) := by rw [target]
    _ =3^(4*k+2)*(3^(5*k)*v+1)+19 := by
      nlinarith [congrArg (fun x : Nat => x*v) powers]
    _ =5*3^(4*k+2)*orbit (15*k) r+19 := by rw [← source]; ring

end CollatzShell.AffineCarry

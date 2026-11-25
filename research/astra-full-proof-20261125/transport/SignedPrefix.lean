import MinimumFailure
import Mathlib.Tactic.Linarith

/-! Signed rational reference trajectories for ordinary shortcut prefixes. -/
namespace Collatz.SignedPrefix
open Collatz.SourceDeletion Collatz.MinimumFailure

def signedStep (d : Nat) (a : Int) : Int :=
  if a % 2 = 0 then a/2 else (3*a+d)/2

def signedRun (d : Nat) : Nat → Int → Int
  | 0, a => a
  | n+1, a => signedRun d n (signedStep d a)

def signedOdds (d : Nat) : Nat → Int → Nat
  | 0, _ => 0
  | n+1, a => signedOdds d n (signedStep d a) + (a%2).toNat

private theorem one_step (d z : Nat) (a t : Int) (hd : d%2=1)
    (eq : (d:Int)*z=a+2*t) :
    (d:Int)*(step z:Nat) = signedStep d a + 3^((a%2).toNat)*t ∧
      z%2=(a%2).toNat := by
  have odd : (d:Int)%2=1 := by exact_mod_cast hd
  have pr := congrArg (fun n : Int => n%2) eq
  simp [Int.add_emod,Int.mul_emod,odd] at pr
  have par : (z%2 : Nat) = (a%2).toNat := by omega
  refine ⟨?_,par⟩
  by_cases he : z%2=0
  · have ae : a%2=0 := by omega
    have z2 : 2*((z:Int)/2)=(z:Int) := by omega
    have a2 : 2*(a/2)=a := by omega
    simp [step,signedStep,he,ae]
    nlinarith only [eq, congrArg (fun x : Int => (d:Int)*x) z2,a2]
  · have ao : a%2=1 := by omega
    have z2 : 2*((3*(z:Int)+1)/2)=3*(z:Int)+1 := by omega
    have a2 : 2*((3*a+d)/2)=3*a+d := by omega
    simp [step,signedStep,he,ao]
    nlinarith only [eq, congrArg (fun x : Int => (d:Int)*x) z2,a2]

/-- A signed numerator is only a reference. The first endpoint is a literal
iterate of the fixed ordinary input, with all parities certified by the lift. -/
theorem lift_signed (j r d z : Nat) (a t : Int) (hd : d%2=1)
    (eq : (d:Int)*z=a+2^(j+r)*t) :
    (d:Int)*(run j z : Nat)=signedRun d j a+2^r*3^(signedOdds d j a)*t ∧
      odds j z=signedOdds d j a := by
  induction j generalizing z a t with
  | zero => simpa [run,odds,signedRun,signedOdds] using eq
  | succ j ih =>
    have en : (d:Int)*z=a+2*(2^(j+r)*t) := by
      rw [eq,show j+1+r=(j+r)+1 by omega,pow_succ]; ring
    obtain ⟨nx,par⟩ := one_step d z a _ hd en
    have en' : (d:Int)*(step z:Nat)=signedStep d a+2^(j+r)*(3^(a%2).toNat*t) := by
      rw [nx]; ring
    obtain ⟨v,o⟩ := ih (step z) (signedStep d a) _ en'
    simp only [run,odds,signedRun,signedOdds,v,o,par,pow_add]
    exact ⟨by ring,True.intro⟩

private theorem three_odd (q : Nat) : 3^q%2=1 := by
  induction q with
  | zero => decide
  | succ q ih => rw [pow_succ,Nat.mul_mod,ih]

/-- Once the signed reference reaches an integer b, the entire displacement
is an explicit integral monomial. This works for either sign of b. -/
theorem integer_endpoint_scaled (j r q m z : Nat) (a b t : Int)
    (seed : (3:Int)^q*z=a+2^(j+r)*t)
    (phase : signedRun (3^q) j a=3^q*b)
    (count : signedOdds (3^q) j a=q+m) :
    (run j z : Int)=b+2^r*3^m*t ∧ odds j z=q+m := by
  have eq : ((3^q:Nat):Int)*z=a+2^(j+r)*t := by simpa using seed
  obtain ⟨v,o⟩ := lift_signed j r (3^q) z a t (three_odd q) eq
  rw [phase,count] at v
  push_cast at v
  rw [pow_add] at v
  have pos : (0:Int)<3^q := by positivity
  have mul : (3:Int)^q * (run j z : Int)=3^q*(b+2^r*3^m*t) := by rw [v]; ring
  exact ⟨mul_left_cancel₀ (ne_of_gt pos) mul,o.trans count⟩

/-- Once the signed reference reaches an integer b, the entire displacement
is an explicit integral monomial. This works for either sign of b. -/
theorem integer_endpoint (j r q m z : Nat) (a b : Int)
    (seed : (3:Int)^q*z=a+2^(j+r))
    (phase : signedRun (3^q) j a=3^q*b)
    (count : signedOdds (3^q) j a=q+m) :
    (run j z : Int)=b+2^r*3^m ∧ odds j z=q+m := by
  simpa using integer_endpoint_scaled j r q m z a b 1 (by simpa using seed) phase count

/-- Two possibly different upper ranks and clocks produce a physical lower
meeting whenever their ordinary terminal displacements and signed phases agree. -/
theorem common_phase {j k r q s m z w : Nat} {a c b : Int}
    (x : (3:Int)^q*z=a+2^(j+r)) (y : (3:Int)^s*w=c+2^(k+r))
    (first : signedRun (3^q) j a=3^q*b) (second : signedRun (3^s) k c=3^s*b)
    (fo : signedOdds (3^q) j a=q+m) (so : signedOdds (3^s) k c=s+m) :
    run j z=run k w ∧ (Good z ↔ Good w) := by
  have left := (integer_endpoint j r q m z a b x first fo).1
  have right := (integer_endpoint k r s m w c b y second so).1
  have meet : run j z=run k w := by exact_mod_cast left.trans right.symm
  exact ⟨meet,(good_run j z).symm.trans (meet ▸ good_run k w)⟩

private theorem run_add (i j x : Nat) : run (i+j) x=run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem odds_add (i j x : Nat) : odds (i+j) x=odds i x+odds j (run i x) := by
  induction i generalizing x with
  | zero => simp [odds,run]
  | succ i ih => rw [Nat.succ_add]; simp only [odds,run,ih]; omega

private theorem halves (r : Nat) : run r (2^r)=1 ∧ odds r (2^r)=0 := by
  induction r with
  | zero => decide
  | succ r ih => simpa [run,odds,step,pow_succ] using ih

/-- When an upper numerator reaches signed zero after exactly R odds at its
denominator, the ordinary triple ends with literal halvings to one. -/
theorem upper_certificate {R j r z : Nat} {a : Int}
    (seed : (3:Int)^(R+1)*z=a+2^(j+r))
    (zero : signedRun (3^R) j a=0) (rank : signedOdds (3^R) j a=R) :
    run (j+r) (3*z)=1 ∧ odds (j+r) (3*z)=R := by
  have ss : (3:Int)^R*(↑(3*z:Nat):Int)=a+2^(j+r) := by
    push_cast; rw [←seed,pow_succ]; ring
  obtain ⟨x,o⟩ := integer_endpoint j r R 0 (3*z) a 0 ss (by simpa using zero) (by simpa using rank)
  have p : run j (3*z)=2^r := by exact_mod_cast (show (run j (3*z):Int)=2^r by simpa using x)
  rw [run_add,odds_add,p,(halves r).1,(halves r).2]
  simp_all

/-- A physical replacement of arbitrary upper rank. The upper witness at w is
built here; the bad label travels on the genuine meeting between z and w. -/
theorem replace_without_query {j k l r t q R m z w : Nat} {a c b : Int}
    (x : (3:Int)^q*z=a+2^(j+r)) (y : (3:Int)^(R+1)*w=c+2^(k+r))
    (first : signedRun (3^q) j a=3^q*b) (second : signedRun (3^(R+1)) k c=3^(R+1)*b)
    (fo : signedOdds (3^q) j a=q+m) (so : signedOdds (3^(R+1)) k c=R+1+m)
    (clocks : k+r=l+t) (zero : signedRun (3^R) l c=0) (rank : signedOdds (3^R) l c=R)
    (bad : ¬Good z) :
    ¬Good w ∧ run (l+t) (3*w)=1 ∧ odds (l+t) (3*w)=R := by
  have merge := (common_phase x y first second fo so).2
  rw [clocks] at y
  exact ⟨fun h => bad (merge.mpr h),upper_certificate y zero rank⟩

private theorem laps (p b k t : Nat) (cycle : run p b=b) :
    run (p*k) (b+2^(p*k)*t)=b+3^((odds p b)*k)*t := by
  induction k generalizing t with
  | zero => simp [run]
  | succ k ih =>
    rw [show p*(k+1)=p+p*k by ring,run_add,pow_add]
    rw [mul_assoc,lift,cycle,show 3^(odds p b)*(2^(p*k)*t)=2^(p*k)*(3^(odds p b)*t) by ring,ih]
    rw [Nat.mul_succ,pow_add]; ring

/-- An unbounded halving block on any upper prefix having a periodic ordinary
lower center induces k full periods at the lower input. The final cofactor u
is arbitrary and no hit (or rank bound) is assumed. -/
theorem periodic_endpoint {j p k q m z u b : Nat} {a : Int}
    (seed : (3:Int)^q*z=a+2^(j+p*k)*u)
    (phase : signedRun (3^q) j a=3^q*(b: Int))
    (count : signedOdds (3^q) j a=q+m)
    (cycle : run p b=b) :
    run (j+p*k) z=b+3^((odds p b)*k+m)*u := by
  have endZ := (integer_endpoint_scaled j (p*k) q m z a b u seed phase count).1
  have endN : run j z=b+2^(p*k)*3^m*u := by exact_mod_cast endZ
  rw [run_add,endN,show 2^(p*k)*3^m*u=2^(p*k)*(3^m*u) by ring,laps p b k (3^m*u) cycle,pow_add]
  ring

/-- A uniformly checked numerical rate excludes all positive ordinary inputs
on the same row at the same depth, independently of the terminal cofactor. -/
theorem periodic_drop {j p k q m z u b c B : Nat} (positive : 0<u)
    (seed : 3^q*z+c=2^(j+p*k)*u)
    (phase : signedRun (3^q) j (-(c:Int))=3^q*(b: Int))
    (count : signedOdds (3^q) j (-(c:Int))=q+m)
    (cycle : run p b=b)
    (rate : 3^q*B*(b+3^((odds p b)*k+m))+c < 2^(j+p*k)) :
    B*run (j+p*k) z<z := by
  have eq : (3:Int)^q*z+c=2^(j+p*k)*u := by exact_mod_cast seed
  have ep := periodic_endpoint (show (3:Int)^q*z= -(c:Int)+2^(j+p*k)*u by omega) phase count cycle
  rw [ep]
  have ru := Nat.mul_lt_mul_of_pos_right rate positive
  have g : 1≤u := by omega
  have cm : c≤c*u := by simpa using Nat.mul_le_mul_left c g
  have bm : 3^q*B*b≤3^q*B*b*u := by simpa using Nat.mul_le_mul_left (3^q*B*b) g
  have both : 3^q*(B*(b+3^(odds p b*k+m)*u))+c < 3^q*z+c := by
    calc
      _ + c ≤ (3^q*B*(b+3^(odds p b*k+m))+c)*u := by nlinarith only [cm,bm]
      _ < 2^(j+p*k)*u := ru
      _ = 3^q*z+c := seed.symm
  exact Nat.lt_of_mul_lt_mul_left (Nat.lt_of_add_lt_add_right both)

private theorem binomial_lower (A k : Nat) :
    A^k*(A+k) ≤ (A+1)^k*A := by
  induction k with
  | zero => simp
  | succ k ih =>
    have grow := Nat.mul_le_mul_left (A+1) ih
    rw [pow_succ,pow_succ]
    nlinarith only [grow,Nat.zero_le (A^k*k)]

private theorem outrun (A D M k : Nat) (pos : 0<A) (gap : A<D) (depth : M*A≤k) :
    M*A^k < D^k := by
  have lo := binomial_lower A k
  have strict := Nat.mul_lt_mul_of_pos_left (show M*A<A+k by omega) (Nat.pow_pos pos (n:=k))
  have cmp : (M*A^k)*A < (A+1)^k*A := by
    rw [show M*A^k*A=A^k*(M*A) by ring]; exact strict.trans_le lo
  exact (Nat.lt_of_mul_lt_mul_right cmp).trans_le (Nat.pow_le_pow_left gap _)

/-- A concrete, finite threshold for every contractive periodic center, every
positive cofactor u, every requested height factor B, and every later k. -/
theorem periodic_drop_eventual {j p k q m z u b c B : Nat} (positive : 0<u)
    (seed : 3^q*z+c=2^(j+p*k)*u)
    (phase : signedRun (3^q) j (-(c:Int))=3^q*(b:Int))
    (count : signedOdds (3^q) j (-(c:Int))=q+m)
    (cycle : run p b=b) (contracts : 3^(odds p b)<2^p)
    (depth : (3^q*B*(b+3^m)+c)*3^(odds p b) ≤ k) :
    B*run (j+p*k) z<z := by
  apply periodic_drop positive seed phase count cycle
  let A := 3^(odds p b)
  let M := 3^q*B*(b+3^m)+c
  have pos : 0<A := by dsimp [A]; positivity
  have rate := outrun A (2^p) M k pos contracts depth
  have one : 1≤A^k := Nat.pow_pos pos
  have grow := Nat.mul_le_mul_left (3^q*B*b+c) one
  have lo : 3^q*B*(b+3^(odds p b*k+m))+c ≤ M*A^k := by
    rw [pow_add,pow_mul]
    dsimp only [A,M] at grow ⊢
    nlinarith only [grow]
  have high : (2^p)^k ≤ 2^(j+p*k) := by
    rw [←pow_mul]; exact Nat.pow_le_pow_right (by decide) (by omega)
  exact lo.trans_lt (rate.trans_le high)

#print axioms upper_certificate
#print axioms replace_without_query
#print axioms periodic_drop_eventual
#print axioms integer_endpoint_scaled
#print axioms periodic_endpoint
#print axioms periodic_drop

#print axioms lift_signed
#print axioms integer_endpoint
#print axioms common_phase

end Collatz.SignedPrefix

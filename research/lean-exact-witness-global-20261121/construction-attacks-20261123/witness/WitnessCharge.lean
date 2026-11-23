/-
Actual finite Collatz profiles and their terminal-cycle-invariant charge.
No global convergence or target-witness existence premise is asserted.
-/
import Std

set_option autoImplicit false
set_option maxHeartbeats 3000000

namespace CollatzWitnessCharge

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => orbit (step n) k

def odds (n : Nat) : Nat → Nat
  | 0 => 0
  | k+1 => n%2 + odds (step n) k

def charge (n k : Nat) : Int := 2*(odds n k : Int)-(k : Int)

private theorem orbit_add (n a b : Nat) :
    orbit n (a+b)=orbit (orbit n a) b := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih => simpa [orbit,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using ih (step n)

private theorem odds_add (n a b : Nat) :
    odds n (a+b)=odds n a+odds (orbit n a) b := by
  induction a generalizing n with
  | zero => simp [orbit,odds]
  | succ a ih =>
    simpa [orbit,odds,Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using
      congrArg (fun z => n%2+z) (ih (step n))

private theorem charge_add (n a b : Nat) :
    charge n (a+b)=charge n a+charge (orbit n a) b := by
  simp only [charge,odds_add]
  omega

private theorem cycle_stats (k : Nat) : orbit 1 (2*k)=1 ∧ odds 1 (2*k)=k := by
  induction k with
  | zero => simp [orbit,odds]
  | succ k ih =>
    rw [show 2*(k+1)=2+2*k by omega,orbit_add,odds_add]
    simp only [orbit,odds,step] at *
    simp at *
    omega

private theorem cycle_any (k : Nat) :
    orbit 1 k=(if k%2=0 then 1 else 2) ∧ odds 1 k=(k+1)/2 := by
  have div := Nat.mod_add_div k 2
  have small := Nat.mod_lt k (by decide : 0<2)
  rcases (show k%2=0 ∨ k%2=1 by omega) with h|h
  · have form : k=2*(k/2) := by omega
    rw [form]
    have cyc := cycle_stats (k/2)
    constructor
    · simpa using cyc.1
    · omega
  · have form : k=2*(k/2)+1 := by omega
    rw [form,orbit_add,odds_add,(cycle_stats (k/2)).1,(cycle_stats (k/2)).2]
    simp only [orbit,odds,step]
    simp
    omega

/-- An arbitrary number of complete terminal cycles has its actual
clock and odd count. -/
theorem pad_complete (n L p : Nat) (hit : orbit n L=1) :
    orbit n (L+2*p)=1 ∧ odds n (L+2*p)=odds n L+p := by
  rw [orbit_add,odds_add,hit]
  exact ⟨(cycle_stats p).1,by rw [(cycle_stats p).2]⟩

/-- Every forward state of a witnessed source has a complete witness;
the identity retains the exact charge of the consumed prefix. -/
theorem complete_tail (n L k : Nat) (hit : orbit n L=1) :
    orbit (orbit n k) (L+k)=1 ∧
    charge n L=charge n k+charge (orbit n k) (L+k) := by
  have tailHit : orbit (orbit n k) (L+k)=1 := by
    rw [←orbit_add,show k+(L+k)=L+2*k by omega]
    exact (pad_complete n L k hit).1
  have padded : charge n (L+2*k)=charge n L := by
    have h := (pad_complete n L k hit).2
    simp only [charge] at *
    omega
  refine ⟨tailHit,?_⟩
  rw [←charge_add,show k+(L+k)=L+2*k by omega,padded]

/-- All complete certificates for one ordinary source have the same
charge, including all possible standard-cycle padding. -/
theorem complete_charge_unique (n L M : Nat)
    (first : orbit n L=1) (second : orbit n M=1) :
    charge n L=charge n M := by
  obtain ⟨tailHit,eqn⟩ := complete_tail n L M first
  rw [second] at tailHit eqn
  have cyc := cycle_any (L+M)
  have even : (L+M)%2=0 := by
    apply Classical.byContradiction
    intro bad
    simp [bad,tailHit] at cyc
  have zero : charge 1 (L+M)=0 := by
    unfold charge
    rw [cyc.2]
    omega
  omega

private theorem even_step (n : Nat) (even : n%2=0) : 2*step n=n := by
  simp only [step,even,ite_true]
  omega

private theorem odd_step (n : Nat) (odd : n%2=1) : 2*step n=3*n+1 := by
  have notEven : ¬n%2=0 := by omega
  simp only [step,notEven,ite_false]
  omega

/-- A complete clock cannot contain more than two clocks per odd input
plus the original binary height. -/
theorem profile_height (n L : Nat) :
    2^L*orbit n L≤4^(odds n L)*n := by
  induction L generalizing n with
  | zero => simp [orbit,odds]
  | succ L ih =>
    have old := Nat.mul_le_mul_left 2 (ih (step n))
    by_cases even : n%2=0
    · have edge := even_step n even
      simp only [orbit,odds,even,Nat.zero_add,Nat.pow_succ]
      calc
        2^L*2*orbit (step n) L = 2*(2^L*orbit (step n) L) := by grind
        _ ≤ 2*(4^(odds (step n) L)*step n) := old
        _ = 4^(odds (step n) L)*n := by grind
    · have odd : n%2=1 := by omega
      have edge := odd_step n odd
      have bound : 2*step n≤4*n := by omega
      have scaled := Nat.mul_le_mul_left (4^(odds (step n) L)) bound
      simp only [orbit,odds,odd]
      rw [Nat.pow_succ,Nat.pow_add]
      calc
        2^L*2*orbit (step n) L = 2*(2^L*orbit (step n) L) := by grind
        _ ≤ 2*(4^(odds (step n) L)*step n) := old
        _ ≤ 4^1*4^(odds (step n) L)*n := by grind

theorem complete_clock_bound (n L B : Nat) (hit : orbit n L=1)
    (height : n<2^B) : L<B+2*odds n L := by
  have bound := profile_height n L
  rw [hit,Nat.mul_one] at bound
  have strict := Nat.mul_lt_mul_of_pos_left height
    (Nat.pow_pos (by decide : 0<4) (n:=odds n L))
  have powers : 4^(odds n L)*2^B=2^(B+2*odds n L) := by
    rw [Nat.pow_add,Nat.pow_mul]
    change 4^(odds n L)*2^B=2^B*4^(odds n L)
    exact Nat.mul_comm _ _
  rw [powers] at strict
  apply Classical.byContradiction
  intro bad
  have reverse := Nat.pow_le_pow_right (by decide : 0<2)
    (show B+2*odds n L≤L by omega)
  omega

private theorem even_lift (n z : Nat) (even : n%2=0) :
    step (n+2*z)=step n+z := by
  have newEven : (n+2*z)%2=0 := by omega
  simp only [step,even,newEven,ite_true]
  omega

private theorem odd_lift (n z : Nat) (odd : n%2=1) :
    step (n+2*z)=step n+3*z := by
  have oldOdd : ¬n%2=0 := by omega
  have newOdd : ¬(n+2*z)%2=0 := by omega
  simp only [step,oldOdd,newOdd,ite_false]
  omega

/-- An exact lift of both the endpoint and its odd count on the full
ordinary binary cylinder of a supplied word. -/
theorem cylinder_lift (n k t : Nat) :
    orbit (n+2^k*t) k=orbit n k+3^(odds n k)*t ∧
    odds (n+2^k*t) k=odds n k := by
  induction k generalizing n t with
  | zero => simp [orbit,odds]
  | succ k ih =>
    have shape : n+2^(k+1)*t=n+2*(2^k*t) := by rw [Nat.pow_succ]; grind
    rw [shape]
    by_cases even : n%2=0
    · have parity : (n+2*(2^k*t))%2=0 := by omega
      simp only [orbit,odds,even,parity,Nat.zero_add,even_lift n (2^k*t) even]
      exact ih (step n) t
    · have odd : n%2=1 := by omega
      have parity : (n+2*(2^k*t))%2=1 := by omega
      simp only [orbit,odds,odd,parity,odd_lift n (2^k*t) odd]
      have shape2 : step n+3*(2^k*t)=step n+2^k*(3*t) := by grind
      rw [shape2]
      obtain ⟨endEq,countEq⟩ := ih (step n) (3*t)
      refine ⟨?_,by omega⟩
      rw [endEq,Nat.pow_add]
      grind

/-- The exact derivative conditions for an affine half-map merger. -/
def HalfGerm (x y : Nat) : Prop :=
  ∃ l, orbit x (l+1)=orbit y l ∧ odds x (l+1)=odds y l

/-- Matching charges construct a literal merger, using only the two
supplied complete witnesses and explicit standard-cycle padding. -/
theorem half_germ_of_charge (x y L M : Nat)
    (hx : orbit x L=1) (hy : orbit y M=1)
    (balance : charge x L+1=charge y M) : HalfGerm x y := by
  have length : L+2*odds y M=M+2*odds x L+1 := by unfold charge at balance; omega
  obtain ⟨ex,ox⟩ := pad_complete x L (odds y M) hx
  obtain ⟨ey,oy⟩ := pad_complete y M (odds x L) hy
  refine ⟨M+2*odds x L,?_,?_⟩
  · rw [←length,ex,ey]
  · rw [←length,ox,oy]; omega

/-- The same charge condition is necessary at arbitrary merger clocks. -/
theorem half_germ_charge (x y L M : Nat)
    (hx : orbit x L=1) (hy : orbit y M=1)
    (germ : HalfGerm x y) : charge x L+1=charge y M := by
  obtain ⟨l,meeting,counts⟩ := germ
  obtain ⟨tailHit,xCharge⟩ := complete_tail x L (l+1) hx
  rw [meeting] at tailHit xCharge
  have yHit : orbit y (l+(L+(l+1)))=1 := by rw [orbit_add]; exact tailHit
  have yCharge := complete_charge_unique y (l+(L+(l+1))) M yHit hy
  rw [charge_add] at yCharge
  have front : charge x (l+1)+1=charge y l := by unfold charge; omega
  omega

theorem half_germ_iff (x y L M : Nat)
    (hx : orbit x L=1) (hy : orbit y M=1) :
    HalfGerm x y ↔ charge x L+1=charge y M :=
  ⟨half_germ_charge x y L M hx hy,half_germ_of_charge x y L M hx hy⟩

/-- Every accepted germ is an infinite family of actual ordinary
mergers; its target is exactly the half-map of its source. -/
theorem half_germ_family (x y : Nat) (half : 2*y=x+1)
    (germ : HalfGerm x y) :
    ∃ l, ∀ t,
      (x+2^(l+1)*t+1)/2=y+2^l*t ∧
      orbit (x+2^(l+1)*t) (l+1)=orbit (y+2^l*t) l := by
  obtain ⟨l,meeting,counts⟩ := germ
  refine ⟨l,fun t => ⟨?_,?_⟩⟩
  · rw [Nat.pow_succ]
    have shape : x+2^l*2*t+1=2*(y+2^l*t) := by grind
    rw [shape]; omega
  · rw [(cylinder_lift x (l+1) t).1,(cylinder_lift y l t).1,meeting,counts]

private theorem pair_stats (q : Nat) :
    orbit (4*q+1) 2=3*q+1 ∧ odds (4*q+1) 2=1 := by
  have first : step (4*q+1)=6*q+2 := by
    have edge := odd_step (4*q+1) (by omega)
    omega
  have second : step (6*q+2)=3*q+1 := by
    have edge := even_step (6*q+2) (by omega)
    omega
  simp only [orbit,odds,first,second]
  simp only [true_and]
  omega

private theorem block_stats (a m : Nat) :
    orbit (a*4^m+1) (2*m)=3^m*a+1 ∧
    odds (a*4^m+1) (2*m)=m := by
  induction m generalizing a with
  | zero => simp [orbit,odds]
  | succ m ih =>
    have first : a*4^(m+1)+1=4*(a*4^m)+1 := by rw [Nat.pow_succ]; grind
    rw [first,show 2*(m+1)=2+2*m by omega,orbit_add,odds_add,
      (pair_stats _).1,(pair_stats _).2]
    have next : 3*(a*4^m)+1=(3*a)*4^m+1 := by grind
    rw [next]
    obtain ⟨endEq,countEq⟩ := ih (3*a)
    rw [endEq,countEq,Nat.pow_succ]
    constructor
    · grind
    · omega

private theorem front_source (K : Nat) :
    orbit (256*K+1) 8=81*K+1 ∧ odds (256*K+1) 8=4 := by
  have h := block_stats K 4
  simpa [Nat.mul_comm] using h

private theorem front_target (K : Nat) :
    orbit (128*K+1) 7=81*K+2 ∧ odds (128*K+1) 7=4 := by
  have h : orbit (128*K+1) 6=54*K+1 ∧ odds (128*K+1) 6=3 := by
    have old := block_stats (2*K) 3
    simpa [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using old
  have last : step (54*K+1)=81*K+2 := by
    have edge := odd_step (54*K+1) (by omega)
    omega
  rw [show (7:Nat)=6+1 by decide,orbit_add,odds_add,h.1,h.2]
  simp only [orbit,odds,last]
  simp only [true_and]
  omega

private theorem power_two_stats (k : Nat) : orbit (2^k) k=1 ∧ odds (2^k) k=0 := by
  induction k with
  | zero => simp [orbit,odds]
  | succ k ih =>
    have power : 2^(k+1)=2*(2^k) := by rw [Nat.pow_succ]; omega
    rw [power]
    have even : (2*(2^k))%2=0 := by omega
    have next : step (2*(2^k))=2^k := by simp [step,even]
    simpa [orbit,odds,even,next] using ih

private theorem geometric_stats (j m : Nat) :
    orbit (3^j*4^m+1) (2*m)=3^(j+m)+1 ∧
    odds (3^j*4^m+1) (2*m)=m := by
  have h := block_stats (3^j) m
  simpa [Nat.pow_add,Nat.mul_comm] using h

/-- The previously retained four-step family, expressed without a
division: its complete source profile and the target's forced prefix. -/
theorem four_step_profiles (K m : Nat) (identity : 4^m=81*K+1) :
    orbit (256*K+1) (2*m+8)=1 ∧ odds (256*K+1) (2*m+8)=4 ∧
    orbit (128*K+1) (2*m+7)=3^m+1 ∧ odds (128*K+1) (2*m+7)=m+4 := by
  have p4 : 4^m=2^(2*m) := by rw [Nat.pow_mul]
  have source := front_source K
  have target := front_target K
  have endTarget : 81*K+2=4^m+1 := by omega
  have endSource : 81*K+1=2^(2*m) := by omega
  have power := power_two_stats (2*m)
  have geometric := geometric_stats 0 m
  simp only [Nat.pow_zero,Nat.one_mul,Nat.zero_add] at geometric
  rw [show 2*m+8=8+2*m by omega,show 2*m+7=7+2*m by omega,
      orbit_add,odds_add,orbit_add,odds_add,source.1,source.2,target.1,target.2,
      endSource,endTarget,power.1,power.2,geometric.1,geometric.2]
  omega

private theorem power_three_small (m : Nat) (large : 2≤m) : 3^m+1<2^(2*m) := by
  obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le large
  have bound (k : Nat) : 3^(2+k)+1<4^(2+k) := by
    induction k with
    | zero => decide
    | succ k ih =>
      rw [show 2+(k+1)=(2+k)+1 by omega,Nat.pow_succ,Nat.pow_succ]
      omega
  have result := bound k
  rw [←hk] at result
  rw [Nat.pow_mul]
  exact result

/-- Every member of the infinite four-odd-step family excludes ALL
homogeneous affine half-mergers, with no clock or padding bound. -/
theorem no_half_germ_four_step (K m : Nat) (large : 2≤m)
    (identity : 4^m=81*K+1) : ¬ HalfGerm (256*K+1) (128*K+1) := by
  intro germ
  obtain ⟨sourceHit,sourceOdds,targetEnd,targetOdds⟩ := four_step_profiles K m identity
  obtain ⟨l,meeting,counts⟩ := germ
  obtain ⟨tailHit,xCharge⟩ := complete_tail (256*K+1) (2*m+8) (l+1) sourceHit
  rw [meeting] at tailHit xCharge
  have yHit : orbit (128*K+1) (l+((2*m+8)+(l+1)))=1 := by
    rw [orbit_add]; exact tailHit
  have frontCharge : charge (256*K+1) (l+1)+1=charge (128*K+1) l := by
    unfold charge; omega
  have yCharge : charge (128*K+1) (l+((2*m+8)+(l+1)))=1-2*(m:Int) := by
    rw [charge_add]
    have sourceCharge : charge (256*K+1) (2*m+8)= -2*(m:Int) := by
      unfold charge; rw [sourceOdds]; omega
    omega
  obtain ⟨powerHit,powerCharge⟩ := complete_tail (128*K+1)
    (l+((2*m+8)+(l+1))) (2*m+7) yHit
  rw [targetEnd] at powerHit powerCharge
  have prefixCharge : charge (128*K+1) (2*m+7)=1 := by
    unfold charge; rw [targetOdds]; omega
  have bound := complete_clock_bound (3^m+1)
    ((l+((2*m+8)+(l+1)))+(2*m+7)) (2*m) powerHit (power_three_small m large)
  rw [yCharge,prefixCharge] at powerCharge
  unfold charge at powerCharge
  omega

/-- A common-clock merger whose full coefficients agree after inserting
the powers 3^a and 3^b of the two parameterized power families. -/
def PowerGerm (a b : Nat) : Prop :=
  ∃ k, orbit (3^a+1) k=orbit (3^b+1) k ∧
    odds (3^a+1) k+a=odds (3^b+1) k+b

/-- A power germ transports a complete witness and preserves the full
power signature, with no bound on either clock. -/
theorem power_germ_transport (a b L : Nat)
    (hit : orbit (3^a+1) L=1) (germ : PowerGerm a b) :
    ∃ M, orbit (3^b+1) M=1 ∧
      charge (3^a+1) L+2*(a:Int)=charge (3^b+1) M+2*(b:Int) := by
  obtain ⟨k,meeting,counts⟩ := germ
  obtain ⟨tailHit,aCharge⟩ := complete_tail (3^a+1) L k hit
  rw [meeting] at tailHit aCharge
  refine ⟨k+(L+k),?_,?_⟩
  · rw [orbit_add]; exact tailHit
  · rw [charge_add]
    have front : charge (3^a+1) k+2*(a:Int)=charge (3^b+1) k+2*(b:Int) := by
      unfold charge; omega
    omega

/-- Equality of the power signatures constructs a germ by explicit
padding of the two supplied finite witnesses. -/
theorem power_germ_of_charge (a b L M : Nat)
    (ha : orbit (3^a+1) L=1) (hb : orbit (3^b+1) M=1)
    (balance : charge (3^a+1) L+2*(a:Int)=charge (3^b+1) M+2*(b:Int)) :
    PowerGerm a b := by
  have length : L+2*(odds (3^b+1) M+b)=M+2*(odds (3^a+1) L+a) := by
    unfold charge at balance; omega
  obtain ⟨ea,oa⟩ := pad_complete (3^a+1) L (odds (3^b+1) M+b) ha
  obtain ⟨eb,ob⟩ := pad_complete (3^b+1) M (odds (3^a+1) L+a) hb
  refine ⟨L+2*(odds (3^b+1) M+b),?_,?_⟩
  · rw [ea,length,eb]
  · rw [oa,length,ob]; omega

theorem power_germ_iff (a b L M : Nat)
    (ha : orbit (3^a+1) L=1) (hb : orbit (3^b+1) M=1) :
    PowerGerm a b ↔
      charge (3^a+1) L+2*(a:Int)=charge (3^b+1) M+2*(b:Int) := by
  constructor
  · intro germ
    obtain ⟨N,hit,balance⟩ := power_germ_transport a b L ha germ
    rw [complete_charge_unique (3^b+1) N M hit hb] at balance
    exact balance
  · exact power_germ_of_charge a b L M ha hb

private theorem power_germ_extend (a b k t : Nat)
    (meeting : orbit (3^a+1) k=orbit (3^b+1) k)
    (counts : odds (3^a+1) k+a=odds (3^b+1) k+b) :
    orbit (3^a+1) (k+t)=orbit (3^b+1) (k+t) ∧
    odds (3^a+1) (k+t)+a=odds (3^b+1) (k+t)+b := by
  rw [orbit_add,orbit_add,odds_add,odds_add,meeting]
  constructor
  · rfl
  · omega

/-- Arbitrarily many intermediate power comparisons cannot change the
signature: every finite chain is already one power germ. -/
theorem power_germ_transitive (a b c : Nat)
    (ab : PowerGerm a b) (bc : PowerGerm b c) : PowerGerm a c := by
  obtain ⟨k,abMeet,abCounts⟩ := ab
  obtain ⟨l,bcMeet,bcCounts⟩ := bc
  obtain ⟨am,ac⟩ := power_germ_extend a b k l abMeet abCounts
  obtain ⟨bm,bc⟩ := power_germ_extend b c l k bcMeet bcCounts
  have sum : l+k=k+l := by omega
  rw [sum] at bm bc
  exact ⟨k+l,am.trans bm,by omega⟩

/-- A positive germ supplies a full infinite ordinary merger family,
not just a comparison of the two numerical seeds. -/
theorem power_germ_family (a b : Nat) (germ : PowerGerm a b) :
    ∃ k, ∀ t,
      orbit (3^a*(1+2^k*t)+1) k=orbit (3^b*(1+2^k*t)+1) k := by
  obtain ⟨k,meeting,counts⟩ := germ
  refine ⟨k,fun t => ?_⟩
  have shapeA : 3^a*(1+2^k*t)+1=(3^a+1)+2^k*(3^a*t) := by grind
  have shapeB : 3^b*(1+2^k*t)+1=(3^b+1)+2^k*(3^b*t) := by grind
  rw [shapeA,shapeB,(cylinder_lift (3^a+1) k (3^a*t)).1,
    (cylinder_lift (3^b+1) k (3^b*t)).1,meeting]
  have powers := congrArg (fun z => (3:Nat)^z) counts
  simp only [Nat.pow_add] at powers
  grind

private theorem triple_power_small (h : Nat) (positive : 0<h) :
    3^(3*h)+1<2^(5*h) := by
  obtain ⟨k,hk⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : h≠0)
  have bound (k : Nat) : 27^(k+1)+1<32^(k+1) := by
    induction k with
    | zero => decide
    | succ k ih =>
      rw [Nat.pow_succ 27 (k+1),Nat.pow_succ 32 (k+1)]
      omega
  rw [hk,Nat.pow_mul,Nat.pow_mul]
  exact bound k

/-- The power signature grows unboundedly on every convergent triple
exponent. This is a consequence of an ordinary path height inequality. -/
theorem power_signature_lower_bound (h L : Nat) (positive : 0<h)
    (hit : orbit (3^(3*h)+1) L=1) :
    (h:Int)<charge (3^(3*h)+1) L+2*(3*h:Int) := by
  have bound := complete_clock_bound (3^(3*h)+1) L (5*h) hit
    (triple_power_small h positive)
  unfold charge
  omega

/-- No choice of words, clocks, padding, or intermediate power germs
can connect a sufficiently large exponent to a fixed certified seed. -/
theorem no_large_power_germ_to_seed (h b M : Nat) (positive : 0<h)
    (hit : orbit (3^b+1) M=1)
    (budget : charge (3^b+1) M+2*(b:Int)≤(h:Int)) :
    ¬ PowerGerm (3*h) b := by
  intro germ
  have reverse : PowerGerm b (3*h) := by
    obtain ⟨k,meeting,counts⟩ := germ
    exact ⟨k,meeting.symm,counts.symm⟩
  obtain ⟨L,newHit,balance⟩ := power_germ_transport b (3*h) M hit reverse
  have lower := power_signature_lower_bound h L positive newHit
  omega

/-- The ordinary joint-edit rules of the retained compiler, without
any imposed edit or physical-clock bound. -/
inductive Alignment : Nat → Nat → Nat → Prop where
  | done (x : Nat) : Alignment x x 0
  | left {x y t : Nat} : Alignment (step x) y t → Alignment x y (t+1)
  | right {x y t : Nat} : Alignment x (step y) t → Alignment x y (t+1)
  | common {x y t : Nat} : x%2=y%2 → Alignment (step x) (step y) t → Alignment x y t

private theorem charge_head (n k : Nat) :
    charge n (k+1)=2*((n%2 : Nat):Int)-1+charge (step n) k := by
  unfold charge
  simp only [odds]
  omega

/-- Charge is an admissible exact lower potential for the edit metric.
A source witness and a successful alignment construct the target witness;
target convergence is not a premise. -/
theorem alignment_charge_bound {x y t : Nat} (path : Alignment x y t)
    (L : Nat) (hit : orbit x L=1) :
    ∃ M, orbit y M=1 ∧
      -(t:Int)≤charge x L-charge y M ∧ charge x L-charge y M≤(t:Int) := by
  induction path generalizing L with
  | done x => exact ⟨L,hit,by omega,by omega⟩
  | @left x y t rest ih =>
    obtain ⟨tailHit,oldCharge⟩ := complete_tail x L 1 hit
    simp only [orbit] at tailHit oldCharge
    obtain ⟨M,newHit,lower,upper⟩ := ih (L+1) tailHit
    have head : charge x 1=2*((x%2:Nat):Int)-1 := by
      rw [charge_head]; simp [charge,odds]
    have parity := Nat.mod_lt x (by decide : 0<2)
    refine ⟨M,newHit,?_,?_⟩ <;> omega
  | @right x y t rest ih =>
    obtain ⟨M,newHit,lower,upper⟩ := ih L hit
    have targetHit : orbit y (M+1)=1 := newHit
    have head := charge_head y M
    have parity := Nat.mod_lt y (by decide : 0<2)
    refine ⟨M+1,targetHit,?_,?_⟩ <;> omega
  | @common x y t parity rest ih =>
    obtain ⟨tailHit,oldCharge⟩ := complete_tail x L 1 hit
    simp only [orbit] at tailHit oldCharge
    obtain ⟨M,newHit,lower,upper⟩ := ih (L+1) tailHit
    have targetHit : orbit y (M+1)=1 := newHit
    have leftHead : charge x 1=2*((x%2:Nat):Int)-1 := by
      rw [charge_head]; simp [charge,odds]
    have rightHead := charge_head y M
    refine ⟨M+1,targetHit,?_,?_⟩ <;> omega

/-- A fixed four-odd-step source can require arbitrarily many joint
edits. Every terminal padding and every physical merger clock is covered. -/
theorem four_step_edit_lower_bound (K h t : Nat) (positive : 0<h)
    (identity : 4^(3*h)=81*K+1)
    (path : Alignment (256*K+1) (128*K+1) t) : h+1<t := by
  obtain ⟨sourceHit,sourceOdds,targetEnd,targetOdds⟩ := four_step_profiles K (3*h) identity
  obtain ⟨M,targetHit,lower,_⟩ := alignment_charge_bound path (2*(3*h)+8) sourceHit
  obtain ⟨tailHit,split⟩ := complete_tail (128*K+1) M (2*(3*h)+7) targetHit
  rw [targetEnd] at tailHit split
  have sourceCharge : charge (256*K+1) (2*(3*h)+8)= -2*(3*h:Int) := by
    unfold charge; rw [sourceOdds]; omega
  have targetPrefix : charge (128*K+1) (2*(3*h)+7)=1 := by
    unfold charge; rw [targetOdds]; omega
  have signature := power_signature_lower_bound h (M+(2*(3*h)+7)) positive tailHit
  omega

end CollatzWitnessCharge

#print axioms CollatzWitnessCharge.pad_complete
#print axioms CollatzWitnessCharge.complete_tail
#print axioms CollatzWitnessCharge.complete_charge_unique
#print axioms CollatzWitnessCharge.profile_height
#print axioms CollatzWitnessCharge.complete_clock_bound
#print axioms CollatzWitnessCharge.cylinder_lift
#print axioms CollatzWitnessCharge.half_germ_of_charge
#print axioms CollatzWitnessCharge.half_germ_charge
#print axioms CollatzWitnessCharge.half_germ_iff
#print axioms CollatzWitnessCharge.half_germ_family
#print axioms CollatzWitnessCharge.four_step_profiles
#print axioms CollatzWitnessCharge.no_half_germ_four_step
#print axioms CollatzWitnessCharge.power_germ_transport
#print axioms CollatzWitnessCharge.power_germ_of_charge
#print axioms CollatzWitnessCharge.power_germ_iff
#print axioms CollatzWitnessCharge.power_germ_transitive
#print axioms CollatzWitnessCharge.power_germ_family
#print axioms CollatzWitnessCharge.power_signature_lower_bound
#print axioms CollatzWitnessCharge.no_large_power_germ_to_seed
#print axioms CollatzWitnessCharge.alignment_charge_bound
#print axioms CollatzWitnessCharge.four_step_edit_lower_bound

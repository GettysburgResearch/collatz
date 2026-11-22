/-
Binary runs control the actual clock of a positive-gap Collatz prefix.
The finite multiplication transducer below proves its bound on all natural
inputs. No sampled binary words or external analytic premises are used.
-/
import Collatz.SignedShadow

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzHighGapPump
open CollatzUnboundedGapReset

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzBinaryRunClock

/-- A new run begins at a one whose preceding lower bit was zero. -/
def starts (previous bit : Nat) : Nat :=
  if bit=1 ∧ previous=0 then 1 else 0

/-- Count binary runs, retaining the bit immediately below the word. -/
def fromBit (previous n : Nat) : Nat :=
  if _h : n=0 then 0
  else starts previous (n%2) + fromBit (n%2) (n/2)
termination_by n
decreasing_by exact Nat.div_lt_self (Nat.pos_of_ne_zero _h) (by decide)

def runs (n : Nat) : Nat := fromBit 0 n

theorem fromBit_zero (previous : Nat) : fromBit previous 0=0 := by
  rw [fromBit]
  simp

theorem fromBit_step (previous n : Nat) (positive : 0<n) :
    fromBit previous n=starts previous (n%2)+fromBit (n%2) (n/2) := by
  rw [fromBit]
  simp [show n≠0 by omega]

theorem runs_zero : runs 0=0 := fromBit_zero 0

theorem even_fromBit (previous n : Nat) : fromBit previous (2*n)=runs n := by
  by_cases zero : n=0
  · subst n
    simp [runs,fromBit_zero]
  · rw [fromBit_step previous (2*n) (by omega)]
    have parity : 2*n%2=0 := by omega
    have half : 2*n/2=n := by omega
    simp [parity,half,starts,runs]

theorem odd_fromBit (previous n : Nat) :
    fromBit previous (2*n+1)=starts previous 1+fromBit 1 n := by
  rw [fromBit_step previous (2*n+1) (by omega)]
  have parity : (2*n+1)%2=1 := by omega
  have half : (2*n+1)/2=n := by omega
  rw [parity,half]

theorem runs_double (n : Nat) : runs (2*n)=runs n := even_fromBit 0 n

theorem runs_odd (n : Nat) : runs (2*n+1)=1+fromBit 1 n := by
  simpa [runs,starts] using odd_fromBit 0 n

theorem runs_four_one (n : Nat) : runs (4*n+1)=runs n+1 := by
  have form : 4*n+1=2*(2*n)+1 := by omega
  rw [form,runs_odd,even_fromBit]
  omega

theorem runs_mul_pow_two (n a : Nat) : runs (2^a*n)=runs n := by
  induction a with
  | zero => simp
  | succ a ih =>
    have form : 2^(a+1)*n=2*(2^a*n) := by rw [Nat.pow_succ]; ac_rfl
    rw [form,runs_double,ih]

theorem runs_positive_of_odd (n : Nat) (odd : n%2=1) : 0<runs n := by
  have form : n=2*(n/2)+1 := by omega
  rw [form,runs_odd]
  omega

/-- Every exact dyadic divisor of 3*n+1 is bounded by twice the number
of binary runs in n. In particular this bounds the maximal valuation. -/
theorem gap_bound (n a m : Nat) (edge : 3*n+1=2^a*m) : a≤2*runs n := by
  induction a using Nat.strong_induction_on generalizing n m with
  | h a ih =>
    by_cases small : a<2
    · have cases : a=0 ∨ a=1 := by omega
      rcases cases with zero | one
      · omega
      · subst a
        simp only [Nat.pow_one] at edge
        have odd : n%2=1 := by omega
        have positive := runs_positive_of_odd n odd
        omega
    · have age : 2≤a := by omega
      have power : 2^a=4*2^(a-2) := by
        calc
          2^a=2^((a-2)+2) := by congr 1; omega
          _=2^(a-2)*4 := by rw [Nat.pow_add]
          _=4*2^(a-2) := by omega
      rw [power] at edge
      have edge' : 3*n+1=4*(2^(a-2)*m) := by
        calc
          3*n+1=4*2^(a-2)*m := edge
          _=4*(2^(a-2)*m) := by ac_rfl
      have residue : n%4=1 := by omega
      have form : n=4*(n/4)+1 := by omega
      have reduced : 3*(n/4)+1=2^(a-2)*m := by omega
      have earlier := ih (a-2) (by omega) (n/4) m reduced
      rw [form,runs_four_one]
      omega

/- The multiplication-by-three automaton has carry 0,1,2 and remembers
the previous input/output bits. This potential pays every output run. -/
private def potential (carry input output : Nat) : Nat :=
  match carry,input,output with
  | 0,0,_ => 0
  | 0,1,0 => 3
  | 0,1,_ => 2
  | 1,0,0 => 1
  | 1,0,_ => 0
  | 1,1,_ => 2
  | 2,0,_ => 1
  | 2,1,0 => 2
  | 2,1,_ => 1
  | _,_,_ => 0

private theorem potential_edge : ∀ carry : Fin 3, ∀ input output bit : Fin 2,
    starts output.val ((3*bit.val+carry.val)%2) +
      potential ((3*bit.val+carry.val)/2) bit.val ((3*bit.val+carry.val)%2) ≤
    3*starts input.val bit.val + potential carry.val input.val output.val := by
  decide

private theorem potential_terminal : ∀ carry : Fin 3, ∀ input output : Fin 2,
    fromBit output.val carry.val ≤ potential carry.val input.val output.val := by
  intro ⟨carry,hc⟩ ⟨input,hi⟩ ⟨output,ho⟩
  have cs : carry=0 ∨ carry=1 ∨ carry=2 := by omega
  have ins : input=0 ∨ input=1 := by omega
  have outs : output=0 ∨ output=1 := by omega
  rcases cs with rfl | rfl | rfl <;>
    rcases ins with rfl | rfl <;> rcases outs with rfl | rfl <;>
    simp [potential,fromBit,starts]

private theorem transducer_bound (n carry input output : Nat)
    (hc : carry<3) (hi : input<2) (ho : output<2) :
    fromBit output (3*n+carry) ≤
      3*fromBit input n+potential carry input output := by
  induction n using Nat.strong_induction_on generalizing carry input output with
  | h n ih =>
    by_cases zero : n=0
    · subst n
      simpa [fromBit_zero] using
        potential_terminal ⟨carry,hc⟩ ⟨input,hi⟩ ⟨output,ho⟩
    · have positive : 0<n := by omega
      have bitBound : n%2<2 := Nat.mod_lt _ (by decide)
      have nextBound : (3*(n%2)+carry)/2<3 := by omega
      have outBound : (3*(n%2)+carry)%2<2 := Nat.mod_lt _ (by decide)
      have smaller : n/2<n := Nat.div_lt_self positive (by decide)
      have tailBound := ih (n/2) smaller ((3*(n%2)+carry)/2)
        (n%2) ((3*(n%2)+carry)%2) nextBound bitBound outBound
      have edgeBound := potential_edge ⟨carry,hc⟩ ⟨input,hi⟩ ⟨output,ho⟩
        ⟨n%2,bitBound⟩
      dsimp only at edgeBound
      have parity : (3*n+carry)%2=(3*(n%2)+carry)%2 := by omega
      have half : (3*n+carry)/2=3*(n/2)+(3*(n%2)+carry)/2 := by omega
      rw [fromBit_step output (3*n+carry) (by omega),parity,half,
        fromBit_step input n positive]
      change starts output ((3*(n%2)+carry)%2) +
        fromBit ((3*(n%2)+carry)%2) (3*(n/2)+(3*(n%2)+carry)/2) ≤
        3*(starts input (n%2)+fromBit (n%2) (n/2))+potential carry input output
      omega

/-- The run count after tripling an odd input and adding one is at most
three times its original run count, with one unit to spare. -/
theorem triple_add_one_runs (n : Nat) (odd : n%2=1) :
    runs (3*n+1)+1≤3*runs n := by
  have form : n=2*(n/2)+1 := by omega
  have output : 3*n+1=2*(3*(n/2)+2) := by omega
  have bound := transducer_bound (n/2) 2 1 0 (by decide) (by decide) (by decide)
  change runs (3*(n/2)+2) ≤ 3*fromBit 1 (n/2)+2 at bound
  have inputRuns : runs n=1+fromBit 1 (n/2) := by
    calc
      runs n=runs (2*(n/2)+1) := congrArg runs form
      _=1+fromBit 1 (n/2) := runs_odd (n/2)
  rw [output,runs_double,inputRuns]
  omega

/-- An actual positive gap preserves runs under its final halvings. -/
theorem edge_runs (n a m : Nat) (positiveGap : 0<a)
    (edge : 3*n+1=2^a*m) : runs m+1≤3*runs n := by
  have evenPower : 2∣2^a := by
    refine ⟨2^(a-1),?_⟩
    calc
      2^a=2^((a-1)+1) := by congr 1; omega
      _=2^(a-1)*2 := by rw [Nat.pow_succ]
      _=2*2^(a-1) := by omega
  obtain ⟨k,power⟩ := evenPower
  have odd : n%2=1 := by
    have evenEdge : 3*n+1=2*(k*m) := by rw [edge,power]; ac_rfl
    omega
  have bound := triple_add_one_runs n odd
  rw [edge,runs_mul_pow_two] at bound
  exact bound

/-- A complete actual prefix has an ordinary-clock bound depending only on
its initial binary run count and its number of odd events. -/
theorem prefix_clock_bound {n endpoint : Nat} {word : List Nat}
    (path : Prefix n word endpoint) :
    total word≤runs n*(3^word.length-1) := by
  induction word generalizing n with
  | nil => simp [total]
  | cons a tail ih =>
    obtain ⟨positiveGap,middle,edge,rest⟩ :=
      (prefix_cons_iff n a endpoint tail).mp path
    have first := gap_bound n a middle edge
    have next := edge_runs n a middle positiveGap edge
    have remaining := ih rest
    have scaled := Nat.mul_le_mul_right (3^tail.length-1)
      (show runs middle≤3*runs n by omega)
    have positivePower : 1≤3^tail.length := Nat.one_le_pow _ _ (by decide)
    have algebra : 2*runs n+(3*runs n)*(3^tail.length-1)=
        runs n*(3^(tail.length+1)-1) := by
      calc
        2*runs n+(3*runs n)*(3^tail.length-1)=
            runs n*(2+3*(3^tail.length-1)) := by
          simp only [Nat.mul_add]
          ac_rfl
        _=runs n*(3^(tail.length+1)-1) := by
          congr 1
          rw [Nat.pow_succ]
          omega
    simp only [total,List.length_cons]
    omega

/-- The same physical clock bound with an arbitrary supplied run cap. -/
theorem capped_prefix_clock {n endpoint S : Nat} {word : List Nat}
    (path : Prefix n word endpoint) (cap : runs n≤S) :
    total word≤S*(3^word.length-1) :=
  Nat.le_trans (prefix_clock_bound path) (Nat.mul_le_mul_right _ cap)

/-- Run growth is controlled along every supplied actual positive-gap word. -/
theorem prefix_runs_bound {n endpoint : Nat} {word : List Nat}
    (path : Prefix n word endpoint) : runs endpoint≤3^word.length*runs n := by
  induction word generalizing n with
  | nil =>
    have same : n=endpoint := by simpa [correction,total] using path.2
    simp [same]
  | cons a tail ih =>
    obtain ⟨positiveGap,middle,edge,rest⟩ :=
      (prefix_cons_iff n a endpoint tail).mp path
    have next := edge_runs n a middle positiveGap edge
    have remaining := ih rest
    have scaled := Nat.mul_le_mul_left (3^tail.length)
      (show runs middle≤3*runs n by omega)
    simp only [List.length_cons,Nat.pow_succ]
    exact Nat.le_trans remaining (by simpa [Nat.mul_assoc] using scaled)

/-- A bounded-run source cannot reach a bounded endpoint in a fixed number
of odd events from arbitrarily large height. All valuation gaps are included. -/
theorem scaled_source_height_bound {n endpoint S : Nat} {word : List Nat}
    (path : Prefix n word endpoint) (cap : runs n≤S) :
    3^word.length*n≤2^(S*(3^word.length-1))*endpoint := by
  have clock := capped_prefix_clock path cap
  have power : 2^total word≤2^(S*(3^word.length-1)) :=
    Nat.pow_le_pow_right (by decide) clock
  have exactIdentity := path.2
  have upper := Nat.mul_le_mul_right endpoint power
  omega

 /-- The source ceiling after dropping the harmless positive ternary factor. -/
theorem source_height_bound {n endpoint S : Nat} {word : List Nat}
    (path : Prefix n word endpoint) (cap : runs n≤S) :
    n≤2^(S*(3^word.length-1))*endpoint := by
  have upper := scaled_source_height_bound path cap
  have one : 1≤3^word.length := Nat.one_le_pow _ _ (by decide)
  have lower : n≤3^word.length*n := by
    simpa using Nat.mul_le_mul_right n one
  omega

/-- A finite endpoint ceiling gives a uniform finite ceiling for the source
on the same actual run-capped segment. -/
theorem capped_endpoint_source_bound {n endpoint S B : Nat} {word : List Nat}
    (path : Prefix n word endpoint) (cap : runs n≤S) (endBound : endpoint<B) :
    n<2^(S*(3^word.length-1))*B := by
  have source := source_height_bound path cap
  have strict := Nat.mul_lt_mul_of_pos_left endBound
    (Nat.pow_pos (by decide : 0<2) (n:=S*(3^word.length-1)))
  omega

end CollatzBinaryRunClock

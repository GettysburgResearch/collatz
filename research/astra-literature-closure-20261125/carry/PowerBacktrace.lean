import InverseEnvelope

namespace Collatz.PowerBacktrace
open Collatz.SourceDeletion

private theorem cat (a b n : Nat) : run (a+b) n=run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add,run] using ih (step n)

private theorem cost (a b n : Nat) : odds (a+b) n=odds a n+odds b (run a n) := by
  induction a generalizing n with
  | zero => simp [run,odds]
  | succ a ih => simp only [Nat.succ_add,odds,run,ih]; omega

private theorem half (k x : Nat) : run k (2^k*x)=x ∧ odds k (2^k*x)=0 := by
  induction k with
  | zero => simp [run,odds]
  | succ k ih =>
    rw [show 2^(k+1)*x=2*(2^k*x) by ring]
    simpa [run,odds,step] using ih

private theorem prefix_cost (v : Nat) :
    odds 4 (1+16*v)=2 ∧ odds 4 (3*(1+16*v))=2 := by
  change _+_+_+_=2 ∧ _+_+_+_=2
  simp only [odds,Nat.zero_add,step]
  split <;> try omega
  all_goals repeat first | omega | split

/-- The single discrete-log entry condition fixes both real endpoint values
and both odd costs. Its lower inverse height already exceeds the fixed input
whenever that input exceeds one. -/
theorem paid_backtrace {k v x : Nat} (pos : 0<x) (entry : 1+9*v=2^k*x) :
    run (4+k) (1+16*v)=x ∧ odds (4+k) (1+16*v)=2 ∧
    run (4+k) (3*(1+16*v))=3^(k+1)*x-1 ∧
    odds (4+k) (3*(1+16*v))=2+k ∧ (1<x → x<1+16*v) := by
  have lower := lift 4 1 v
  change run 4 (1+16*v)=1+9*v at lower
  have upper := lift 4 3 (3*v)
  change run 4 (3+16*(3*v))=2+9*(3*v) at upper
  rw [show 3+16*(3*v)=3*(1+16*v) by ring] at upper
  have pm : 1≤2^k := Nat.two_pow_pos _
  have comp := Nat.mul_le_mul_right x pm
  simp only [one_mul] at comp
  have eq : run 4 (3*(1+16*v))=2^k*(3*x)-1 := by
    rw [upper,show 2^k*(3*x)=3*(2^k*x) by ring,←entry]; omega
  have large := Collatz.InverseEnvelope.attained k k (3*x) (by omega) (by omega)
  simp only [Nat.sub_self,pow_zero,one_mul] at large
  obtain ⟨lo,up⟩ := prefix_cost v
  rw [cat,cat,cost,cost,lower,eq,entry,lo,up,(half k x).1,(half k x).2,large.2]
  have exp : 3^k*(3*x)=3^(k+1)*x := by ring
  rw [exp] at large
  omega

#print axioms paid_backtrace
end Collatz.PowerBacktrace

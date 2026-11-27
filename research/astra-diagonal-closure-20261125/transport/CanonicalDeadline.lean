import MinimumFailure

namespace Collatz.CanonicalDeadline
open Collatz.SourceDeletion

private theorem cat (a b x : Nat) : run (a+b) x=run b (run a x) := by
  induction a generalizing x with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem catOdd (a b x : Nat) : odds (a+b) x=odds a x+odds b (run a x) := by
  induction a generalizing x with
  | zero => simp [odds,run]
  | succ a ih => simp only [Nat.succ_add,odds,run,ih]; omega

private theorem end_unit {n : Nat} (u : n%3≠0) (h : Nat) : (run h n)%3≠0 := by
  induction h generalizing n with
  | zero => exact u
  | succ h ih => apply ih; unfold step; split <;> omega

/-- Exact ordinary availability of a common successor with *some* tripled
source. It concerns the supplied unit n and has no cost or orbit assumption. -/
theorem one_successor_iff (n : Nat) (unit : n%3≠0) :
    (∃ a, step n=step (3*a)) ↔ n%18=10 := by
  constructor
  · rintro ⟨a,eq⟩; unfold step at eq; split at eq <;> split at eq <;> omega
  · intro rem; refine ⟨(n-1)/9,?_⟩; unfold step; split <;> split <;> omega

/-- For a prescribed odd comparator the required offset is exact. Taking
`a=3^k*u` tests the actual upper suffix's odd value `u` at any chosen rank. -/
theorem prescribed_successor_iff {n a : Nat} (unit : n%3≠0) (odd : a%2=1) :
    step n=step (3*a) ↔ n=9*a+1 := by
  unfold step; split <;> split <;> omega

private theorem odd_steps (k u : Nat) (pos : 0<u) : run k (2^k*u-1)=3^k*u-1 := by
  induction k generalizing u with
  | zero => simp [run]
  | succ k ih =>
    have p : 0<2^k*u := Nat.mul_pos (Nat.two_pow_pos _) pos
    have first : step (2^(k+1)*u-1)=2^k*(3*u)-1 := by
      rw [show 2^(k+1)*u=2*(2^k*u) by ring,show 2^k*(3*u)=3*(2^k*u) by ring]
      unfold step; split <;> omega
    rw [run,first,ih (3*u) (by omega),pow_succ]; congr 1; ring

private theorem half (k u : Nat) : run k (2^k*u)=u ∧ odds k (2^k*u)=0 := by
  induction k with
  | zero => simp [run,odds]
  | succ k ih =>
    rw [show 2^(k+1)*u=2*(2^k*u) by ring]
    simpa [run,odds,step] using ih

private theorem front (c : Nat) :
    let z := 161+256*c
    (∀ i<7, (run i z)%18≠10) ∧ run 7 z=103+162*c ∧
    (∀ i≤8, 1<run i (3*z)) ∧ run 8 (3*z)=17+27*c ∧ odds 8 (3*z)=2 := by
  dsimp only
  have l1 : run 1 (161+256*c)=242+384*c := by
    change step _=_
    unfold step; split <;> omega
  have l2 : run 2 (161+256*c)=121+192*c := by
    rw [show 2=1+1 by decide,cat,l1]; change step _=_
    unfold step; split <;> omega
  have l3 : run 3 (161+256*c)=182+288*c := by
    rw [show 3=2+1 by decide,cat,l2]; change step _=_
    unfold step; split <;> omega
  have l4 : run 4 (161+256*c)=91+144*c := by
    rw [show 4=3+1 by decide,cat,l3]; change step _=_
    unfold step; split <;> omega
  have l5 : run 5 (161+256*c)=137+216*c := by
    rw [show 5=4+1 by decide,cat,l4]; change step _=_
    unfold step; split <;> omega
  have l6 : run 6 (161+256*c)=206+324*c := by
    rw [show 6=5+1 by decide,cat,l5]; change step _=_
    unfold step; split <;> omega
  have l7 : run 7 (161+256*c)=103+162*c := by
    rw [show 7=6+1 by decide,cat,l6]; change step _=_
    unfold step; split <;> omega
  have u1 : run 1 (3*(161+256*c))=725+1152*c := by
    change step _=_
    unfold step; split <;> omega
  have u2 : run 2 (3*(161+256*c))=1088+1728*c := by
    rw [show 2=1+1 by decide,cat,u1]; change step _=_
    unfold step; split <;> omega
  have u3 : run 3 (3*(161+256*c))=544+864*c := by
    rw [show 3=2+1 by decide,cat,u2]; change step _=_
    unfold step; split <;> omega
  have u4 : run 4 (3*(161+256*c))=272+432*c := by
    rw [show 4=3+1 by decide,cat,u3]; change step _=_
    unfold step; split <;> omega
  have u5 : run 5 (3*(161+256*c))=136+216*c := by
    rw [show 5=4+1 by decide,cat,u4]; change step _=_
    unfold step; split <;> omega
  have u6 : run 6 (3*(161+256*c))=68+108*c := by
    rw [show 6=5+1 by decide,cat,u5]; change step _=_
    unfold step; split <;> omega
  have u7 : run 7 (3*(161+256*c))=34+54*c := by
    rw [show 7=6+1 by decide,cat,u6]; change step _=_
    unfold step; split <;> omega
  have u8 : run 8 (3*(161+256*c))=17+27*c := by
    rw [show 8=7+1 by decide,cat,u7]; change step _=_
    unfold step; split <;> omega
  refine ⟨?_,l7,?_,u8,?_⟩
  · intro i hi
    have cases : i=0 ∨ i=1 ∨ i=2 ∨ i=3 ∨ i=4 ∨ i=5 ∨ i=6 := by omega
    rcases cases with e|e|e|e|e|e|e <;> subst i <;> first | rw [l1] | rw [l2] | rw [l3] | rw [l4] | rw [l5] | rw [l6] | change (161+256*c)%18≠10
    all_goals omega
  · intro i hi
    have cases : i=0 ∨ i=1 ∨ i=2 ∨ i=3 ∨ i=4 ∨ i=5 ∨ i=6 ∨ i=7 ∨ i=8 := by omega
    rcases cases with e|e|e|e|e|e|e|e|e <;> subst i <;> first | rw [u1] | rw [u2] | rw [u3] | rw [u4] | rw [u5] | rw [u6] | rw [u7] | rw [u8] | change 1<3*(161+256*c)
    all_goals omega
  · have advance (t n : Nat) : odds (t+1) n=odds t n+(run t n)%2 := by rw [catOdd t 1]; simp [odds]
    rw [show 8=7+1 by decide,advance 7]
    rw [show 7=6+1 by decide,advance 6]
    rw [show 6=5+1 by decide,advance 5]
    rw [show 5=4+1 by decide,advance 4]
    rw [show 4=3+1 by decide,advance 3]
    rw [show 3=2+1 by decide,advance 2]
    rw [show 2=1+1 by decide,advance 1]
    rw [show 1=0+1 by decide,advance 0]
    rw [u1,u2,u3,u4,u5,u6,u7]; simp only [run,odds]; omega

/-- A supplied upper *first* hit with exactly three odds. The lower arm has
no common successor with any tripled input at any clock through that hit.
The numerical scale is arbitrary in the displayed ordinary source row. -/
theorem no_successor_through_first_hit {z e : Nat} (unit : z%3≠0)
    (seed : 81*z+271=256*2^(e+1)) :
    run (e+9) (3*z)=1 ∧ odds (e+9) (3*z)=3 ∧
    (∀ i<e+9, run i (3*z)≠1) ∧
    (∀ i≤e+9, ∀ a, step (run i z)≠step (3*a)) := by
  let c := z/256
  have form : z=161+256*c := by dsimp [c]; omega
  obtain ⟨small,low,notOne,upper,q⟩ := front c
  rw [←form] at small low notOne upper q
  have power : 3*(17+27*c)+1=2^(e+1) := by rw [form] at seed; omega
  have ue : step (17+27*c)=2^e := by rw [pow_succ] at power; unfold step; split <;> omega
  have uo : (17+27*c)%2=1 := by rw [pow_succ] at power; omega
  have after : run 9 (3*z)=2^e := by rw [show 9=8+1 by decide,cat,upper]; exact ue
  have cost : odds 9 (3*z)=3 := by rw [show 9=8+1 by decide,catOdd,q,upper]; simp [odds,uo]
  have skip := half e 1
  simp only [Nat.mul_one] at skip
  constructor
  · rw [Nat.add_comm,cat,after,skip.1]
  constructor
  · rw [Nat.add_comm,catOdd,cost,after,skip.2]
  constructor
  · intro i lt
    by_cases early : i≤8
    · exact (Nat.ne_of_gt (notOne i early))
    · let b := i-9
      have clk : i=9+b := by dsimp [b]; omega
      let d := e-b
      have de : 0<d := by dsimp [d,b]; omega
      have eq : e=b+d := by dsimp [b,d]; omega
      rw [clk,cat,after,eq,pow_add,(half b (2^d)).1]
      exact Nat.ne_of_gt (Nat.one_lt_pow (by omega) (by decide))
  · intro i hi a clash
    have tag := (one_successor_iff _ (end_unit unit i)).mp ⟨a,clash⟩
    by_cases early : i<7
    · exact small i early tag
    let m := e+2
    let b := i-7
    have clk : i=7+b := by dsimp [b]; omega
    have size : b≤m := by dsimp [b,m]; omega
    have seedLow : 103+162*c=2^m-1 := by dsimp [m]; rw [show e+2=(e+1)+1 by omega,pow_succ]; omega
    have dec : m=b+(m-b) := by omega
    rw [clk,cat,low,seedLow,dec,pow_add,odd_steps b _ (Nat.two_pow_pos _)] at tag
    by_cases stop : m=b
    · rw [stop,Nat.sub_self,pow_zero,Nat.mul_one] at tag
      have bp : 0<b := by dsimp [m] at stop; omega
      obtain ⟨v,hv⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : b≠0)
      rw [hv,pow_succ] at tag
      have pp : 0<3^v := Nat.pow_pos (by decide)
      omega
    · have more : m-b=(m-b-1)+1 := by omega
      rw [more,pow_succ,show 3^b*(2^(m-b-1)*2)=2*(3^b*2^(m-b-1)) by ring] at tag
      have p : 0<3^b*2^(m-b-1) := Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.two_pow_pos _)
      omega

#print axioms prescribed_successor_iff
#print axioms one_successor_iff
#print axioms no_successor_through_first_hit
end Collatz.CanonicalDeadline
